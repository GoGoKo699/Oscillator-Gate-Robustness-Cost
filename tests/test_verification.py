"""Regression tests for source boundaries and verification failure semantics."""
from __future__ import annotations

import copy
import importlib.util
import json
import os
from pathlib import Path
import runpy
import sys
import tempfile
import unittest
from unittest import mock

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("repository_verify", ROOT / "scripts/verify.py")
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


def passing_supplemental_report():
    return {"schema_version": 1, "suite": "spectral_cost", "status": "PASS",
            "method": "exact_symbolic_algebra", "test_groups": 3,
            "groups": [{"id": identifier, "status": "PASS", "identities": {"example": "0"}}
                       for identifier in verify.SUPPLEMENTAL_GROUPS]}


def passing_frontier_report():
    return {"schema_version": 1, "suite": "sensitivity_frontier", "status": "PASS",
            "method": "exact_symbolic_algebra", "test_groups": 4,
            "groups": [{"id": identifier, "status": "PASS", "identities": {"example": "0"}}
                       for identifier in verify.FRONTIER_GROUPS]}


class TemporaryRepository(unittest.TestCase):
    def setUp(self):
        # All fixtures stay in this authorized repository, including direct test runs.
        temp_root = Path(os.environ.get("OGRC_TEST_TMPDIR", ROOT / "verification-results/test-tmp"))
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temp_root)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.checks = self.root / "checks"
        self.checks.mkdir()
        (self.checks / "a.txt").write_bytes(b"alpha\n")
        (self.root / "references").mkdir()
        (self.root / "references/b.txt").write_bytes(b"beta\n")
        self.expected = {"checks/a.txt": verify.file_identity(self.checks / "a.txt"),
                         "references/b.txt": verify.file_identity(self.root / "references/b.txt")}

    def write_manifest(self, files=None):
        path = self.root / "manifest.json"
        files = self.expected if files is None else files
        path.write_text(json.dumps({"schema_version": 1, "protected_roots": list(verify.PROTECTED_ROOTS),
                                    "file_count": len(files), "files": files}), encoding="utf-8")
        return path


class IntegrityTests(TemporaryRepository):
    def test_complete_inventory_is_accepted(self):
        expected = verify.load_manifest(self.write_manifest(), expected_count=2)
        result = verify.check_source(self.root, expected)
        self.assertTrue(result["pass"])
        self.assertEqual(result["files"], self.expected)

    def test_same_size_corruption_is_detected(self):
        (self.checks / "a.txt").write_bytes(b"ALPHA\n")
        result = verify.check_source(self.root, self.expected)
        self.assertFalse(result["pass"])
        self.assertEqual(result["changed"], ["checks/a.txt"])

    def test_missing_and_extra_hidden_files_are_detected(self):
        (self.checks / "a.txt").unlink()
        (self.checks / ".unexpected").write_bytes(b"extra")
        result = verify.check_source(self.root, self.expected)
        self.assertFalse(result["pass"])
        self.assertEqual(result["missing"], ["checks/a.txt"])
        self.assertEqual(result["extra"], ["checks/.unexpected"])

    def test_manifest_traversal_and_noncanonical_paths_are_rejected(self):
        for name in ("../outside", "/outside", "checks/../../outside", "checks/../a.txt",
                     "checks//b.txt", "./checks/a.txt", "checks\\b.txt", ".",
                     "checks", "scripts/verify.py"):
            with self.subTest(name=name):
                files = {name: self.expected["checks/a.txt"]}
                with self.assertRaises(ValueError):
                    verify.load_manifest(self.write_manifest(files), expected_count=1)

    def test_duplicate_manifest_keys_are_rejected(self):
        path = self.root / "manifest.json"
        path.write_text('{"files": {}, "files": {}}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Duplicate JSON key"):
            verify.load_manifest(path, expected_count=0)

    def test_manifest_count_and_digest_are_validated(self):
        with self.assertRaisesRegex(ValueError, "exactly 11"):
            verify.load_manifest(self.write_manifest())
        invalid = copy.deepcopy(self.expected)
        invalid["checks/a.txt"]["sha256"] = "invalid"
        with self.assertRaisesRegex(ValueError, "Invalid identity"):
            verify.load_manifest(self.write_manifest(invalid), expected_count=2)

    def test_symlink_files_and_directories_cannot_escape_protected_roots(self):
        (self.root / "outside").mkdir()
        (self.root / "outside/data.txt").write_bytes(b"secret")
        (self.checks / "a.txt").unlink()
        (self.checks / "a.txt").symlink_to(self.root / "outside/data.txt")
        (self.checks / "external").symlink_to(self.root / "outside", target_is_directory=True)
        result = verify.check_source(self.root, self.expected)
        self.assertFalse(result["pass"])
        self.assertEqual(result["unsupported_paths"], ["checks/a.txt", "checks/external"])
        self.assertNotIn("checks/external/data.txt", result["files"])

    def test_manifest_schema_and_root_substitution_are_rejected(self):
        path = self.write_manifest()
        valid = json.loads(path.read_text())
        for key, value in (("schema_version", True), ("schema_version", 2),
                           ("protected_roots", ["checks"]),
                           ("protected_roots", ["checks", "../references"])):
            with self.subTest(key=key, value=value):
                path.write_text(json.dumps({**valid, key: value}))
                with self.assertRaisesRegex(ValueError, "schema or protected_roots"):
                    verify.load_manifest(path, expected_count=2)

    def test_missing_protected_root_is_rejected(self):
        (self.root / "references/b.txt").unlink()
        (self.root / "references").rmdir()
        with self.assertRaisesRegex(ValueError, "real directory: references"):
            verify.check_source(self.root, self.expected)

    def test_symlink_protected_root_is_rejected(self):
        (self.root / "references").rename(self.root / "outside")
        (self.root / "references").symlink_to(self.root / "outside", target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "real directory: references"):
            verify.check_source(self.root, self.expected)

    def test_nonregular_protected_file_is_rejected(self):
        os.mkfifo(self.checks / "pipe")
        result = verify.check_source(self.root, self.expected)
        self.assertFalse(result["pass"])
        self.assertEqual(result["unsupported_paths"], ["checks/pipe"])


class OutputTests(TemporaryRepository):
    def test_new_output_is_accepted_without_creating_it(self):
        target = self.root / "runs/new"
        self.assertEqual(verify.validate_output(target, self.root), target)
        self.assertFalse(target.exists())

    def test_existing_files_and_directories_are_never_overwritten(self):
        for target in (self.checks, self.checks / "a.txt"):
            with self.subTest(target=target), self.assertRaises(ValueError):
                verify.validate_output(target, self.root)
        self.assertEqual((self.checks / "a.txt").read_bytes(), b"alpha\n")

    def test_output_inside_every_protected_root_including_dotdot_is_rejected(self):
        targets = [self.root / name / "new" for name in verify.OUTPUT_PROTECTED_ROOTS]
        targets.append(self.root / "runs/../checks/new")
        for target in targets:
            with self.subTest(target=target), self.assertRaisesRegex(ValueError, "outside protected"):
                verify.validate_output(target, self.root)

    def test_output_symlink_to_protected_root_is_rejected(self):
        alias = self.root / "alias"
        alias.symlink_to(self.checks, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "outside protected"):
            verify.validate_output(alias / "new", self.root)

    def test_dangling_output_symlink_is_rejected(self):
        alias = self.root / "alias"
        alias.symlink_to(self.root / "new")
        with self.assertRaisesRegex(ValueError, "already exist"):
            verify.validate_output(alias, self.root)
        self.assertFalse((self.root / "new").exists())


class ScientificResultTests(unittest.TestCase):
    def setUp(self):
        self.receipt = {
            "scientific_assertions_pass": True,
            "all_canonical_reports_byte_identical": True,
            "source_unchanged": True, "total_groups": 20,
            "runs": [{"suite": name, "groups": 5, "report_exists": True,
                      "returncode": 0, "status": "PASS", "byte_identical": True,
                      "differences": []} for name in verify.SUITES],
        }

    def test_numerical_drift_is_reported_separately_from_assertions(self):
        # Use the maintained runner so per-field numerical evidence stays covered.
        runner = runpy.run_path(str(ROOT / "scripts/run_scientific.py"), run_name="runner_test")
        differences = runner["diffs"]({"residual": 1.0}, {"residual": 1.0 + 1e-12})
        self.receipt["runs"][0].update(byte_identical=False, differences=differences)
        self.receipt["all_canonical_reports_byte_identical"] = False
        result = verify.scientific_summary(self.receipt, 1)
        self.assertTrue(result["scientific_assertions_pass"])
        self.assertFalse(result["all_canonical_reports_byte_identical"])
        self.assertEqual(result["wrapper_returncode"], 1)
        self.assertEqual(result["runs"][0]["differences"][0]["kind"], "numeric")
        self.assertGreater(result["runs"][0]["differences"][0]["absolute_difference"], 0)

    def test_suite_failure_cannot_be_hidden_by_receipt_summary(self):
        self.receipt["runs"][1].update(returncode=1, status="FAIL")
        result = verify.scientific_summary(self.receipt, 1)
        self.assertFalse(result["scientific_assertions_pass"])

    def test_missing_receipt_or_suite_cannot_pass(self):
        for receipt in (None, {}, {**self.receipt, "runs": self.receipt["runs"][:-1]}):
            with self.subTest(receipt=receipt):
                result = verify.scientific_summary(receipt, 0)
                self.assertFalse(result["receipt_valid"])
                self.assertFalse(result["scientific_assertions_pass"])

    def test_duplicate_suites_and_missing_groups_cannot_pass(self):
        self.receipt["runs"][0]["suite"] = "pilot"
        self.assertFalse(verify.scientific_summary(self.receipt, 0)["receipt_valid"])
        self.receipt["runs"][0]["suite"] = "consolidation"
        self.receipt["runs"][0]["groups"] = 4
        self.assertFalse(verify.scientific_summary(self.receipt, 0)["scientific_assertions_pass"])

    def test_success_does_not_relabel_a_failing_wrapper_exit(self):
        result = verify.scientific_summary(self.receipt, 2)
        self.assertTrue(result["scientific_assertions_pass"])
        self.assertEqual(result["wrapper_returncode"], 2)


class ExecutionTests(TemporaryRepository):
    def test_runner_refuses_corrupted_sources_before_execution(self):
        spec = importlib.util.spec_from_file_location("scientific_runner", ROOT / "scripts/run_scientific.py")
        runner = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runner)
        (self.checks / "a.txt").write_bytes(b"ALPHA\n")
        with (mock.patch.object(runner, "ROOT", self.root),
              mock.patch.object(runner, "load_manifest", return_value=self.expected),
              mock.patch.object(runner, "run_logged") as execute,
              mock.patch("sys.stderr")):
            with self.assertRaises(SystemExit) as error:
                runner.main(["--output-dir", str(self.root / "run")])
        self.assertEqual(error.exception.code, 2)
        execute.assert_not_called()
        self.assertFalse((self.root / "run").exists())

    def test_relocated_references_keep_byte_and_numeric_comparisons(self):
        output = self.root / "run"
        output.mkdir()
        for suite, relative in verify.REFERENCE_REPORTS.items():
            (self.root / relative).write_text('{"status": "PASS", "residual": 1.0}\n')
            (output / (suite + ".json")).write_text('{"status": "PASS", "residual": 1.0}\n')
        self.assertTrue(verify.inspect_reports(output, self.root)["all_byte_identical"])
        (output / "pilot.json").write_text('{"status": "PASS", "residual": 1.000000000001}\n')
        comparison = verify.inspect_reports(output, self.root)
        self.assertFalse(comparison["all_byte_identical"])
        self.assertTrue(comparison["finite_numeric_differences_only"])
        self.assertEqual(comparison["numeric_difference_count"], 1)

    def test_failed_subprocess_preserves_exit_and_log(self):
        log = self.root / "failure.log"
        result = verify.run_logged([sys.executable, "-c", "print('failure details'); raise SystemExit(7)"],
                                   log, dict(os.environ), timeout=10)
        self.assertEqual(result["returncode"], 7)
        self.assertIn("failure details", log.read_text())
        with self.assertRaises(FileExistsError):
            verify.run_logged([sys.executable, "-c", "pass"], log, dict(os.environ), timeout=10)

    def test_supplemental_cli_refuses_overwrite_and_protected_output(self):
        sentinel = self.root / "existing.json"
        sentinel.write_bytes(b"preserve this report")
        protected_outputs = [ROOT / name / "supplemental-must-not-be-created.json"
                             for name in verify.OUTPUT_PROTECTED_ROOTS]
        for script in ("check_spectral_cost.py", "check_sensitivity_frontier.py"):
            for index, target in enumerate((sentinel, *protected_outputs)):
                with self.subTest(script=script, target=target):
                    result = verify.run_logged(
                        [sys.executable, "-B", str(ROOT / "checks" / script), "--output", str(target)],
                        self.root / f"{script}-refusal-{index}.log", dict(os.environ), timeout=10)
                    self.assertEqual(result["returncode"], 2)
        self.assertEqual(sentinel.read_bytes(), b"preserve this report")
        self.assertTrue(all(not target.exists() for target in protected_outputs))


class SupplementalResultTests(unittest.TestCase):
    def test_complete_exact_report_is_accepted(self):
        result = verify.supplemental_summary(passing_supplemental_report(), 0)
        self.assertTrue(result["scientific_assertions_pass"])
        self.assertTrue(result["report_valid"])
        self.assertEqual(result["test_groups"], 3)

    def test_missing_failed_or_incomplete_report_cannot_pass(self):
        good = passing_supplemental_report()
        bad_group = copy.deepcopy(good)
        bad_group["groups"][1]["status"] = "FAIL"
        missing_identities = copy.deepcopy(good)
        missing_identities["groups"][1]["identities"] = {}
        duplicate = copy.deepcopy(good)
        duplicate["groups"][1]["id"] = duplicate["groups"][0]["id"]
        for report, returncode in ((None, 0), ({}, 0), (good, 1),
                                   ({**good, "status": "FAIL"}, 0),
                                   ({**good, "groups": good["groups"][:-1]}, 0),
                                   ({**good, "test_groups": 2}, 0),
                                   ({**good, "method": "numeric_sweep"}, 0),
                                   (bad_group, 0), (missing_identities, 0), (duplicate, 0)):
            with self.subTest(report=report, returncode=returncode):
                self.assertFalse(verify.supplemental_summary(report, returncode)["scientific_assertions_pass"])


class FrontierResultTests(unittest.TestCase):
    def test_complete_exact_frontier_report_is_accepted(self):
        result = verify.frontier_summary(passing_frontier_report(), 0)
        self.assertTrue(result["scientific_assertions_pass"])
        self.assertTrue(result["report_valid"])
        self.assertEqual(result["test_groups"], 4)

    def test_missing_failed_or_incomplete_frontier_cannot_pass(self):
        good = passing_frontier_report()
        bad_group = copy.deepcopy(good)
        bad_group["groups"][2]["status"] = "FAIL"
        missing_identities = copy.deepcopy(good)
        missing_identities["groups"][2]["identities"] = {}
        duplicate = copy.deepcopy(good)
        duplicate["groups"][2]["id"] = duplicate["groups"][0]["id"]
        for report, returncode in ((None, 0), ({}, 0), (good, 1),
                                   ({**good, "status": "FAIL"}, 0),
                                   ({**good, "groups": good["groups"][:-1]}, 0),
                                   ({**good, "test_groups": 3}, 0),
                                   ({**good, "method": "numeric_sweep"}, 0),
                                   (passing_supplemental_report(), 0),
                                   (bad_group, 0), (missing_identities, 0), (duplicate, 0)):
            with self.subTest(report=report, returncode=returncode):
                self.assertFalse(verify.frontier_summary(report, returncode)["scientific_assertions_pass"])


class ReportPolicyTests(unittest.TestCase):
    def setUp(self):
        self.record = {
            "errors": [], "source_integrity_before": {"pass": True},
            "source_integrity_after": {"pass": True},
            "infrastructure_tests": {"returncode": 0},
            "scientific": {"receipt_valid": True, "scientific_assertions_pass": True,
                           "all_canonical_reports_byte_identical": False,
                           "source_unchanged": True, "wrapper_returncode": 1},
            "report_comparisons": {"all_byte_identical": False,
                                   "finite_numeric_differences_only": True,
                                   "numeric_difference_count": 2},
            "supplemental_scientific": verify.supplemental_summary(passing_supplemental_report(), 0),
            "frontier_scientific": verify.frontier_summary(passing_frontier_report(), 0),
        }

    def test_numeric_report_differences_require_explicit_opt_in(self):
        self.assertFalse(verify.verification_passes(self.record, False))
        self.assertTrue(verify.verification_passes(self.record, True))

    def test_opt_in_never_hides_independent_failures(self):
        failures = [
            ("source_integrity_before", "pass", False),
            ("source_integrity_after", "pass", False),
            ("infrastructure_tests", "returncode", 1),
            ("scientific", "receipt_valid", False),
            ("scientific", "scientific_assertions_pass", False),
            ("scientific", "source_unchanged", False),
            ("scientific", "wrapper_returncode", 2),
            ("report_comparisons", "finite_numeric_differences_only", False),
            ("supplemental_scientific", "returncode", 1),
            ("supplemental_scientific", "scientific_assertions_pass", False),
            ("supplemental_scientific", "report_valid", False),
            ("frontier_scientific", "returncode", 1),
            ("frontier_scientific", "scientific_assertions_pass", False),
            ("frontier_scientific", "report_valid", False),
        ]
        for section, field, value in failures:
            with self.subTest(section=section, field=field):
                record = copy.deepcopy(self.record)
                record[section][field] = value
                self.assertFalse(verify.verification_passes(record, True))

    def test_missing_supplemental_cannot_be_waived_by_report_policy(self):
        del self.record["supplemental_scientific"]
        self.assertFalse(verify.verification_passes(self.record, True))
        self.record["scientific"].update(all_canonical_reports_byte_identical=True, wrapper_returncode=0)
        self.record["report_comparisons"].update(all_byte_identical=True, numeric_difference_count=0)
        self.assertFalse(verify.verification_passes(self.record, False))

    def test_missing_frontier_cannot_be_waived_by_report_policy(self):
        del self.record["frontier_scientific"]
        self.assertFalse(verify.verification_passes(self.record, True))
        self.record["scientific"].update(all_canonical_reports_byte_identical=True, wrapper_returncode=0)
        self.record["report_comparisons"].update(all_byte_identical=True, numeric_difference_count=0)
        self.assertFalse(verify.verification_passes(self.record, False))

    def test_structure_types_and_nonnumeric_changes_are_rejected(self):
        for reference, actual in (({"x": 1}, {"y": 1}), ([1], [1, 2]),
                                  (1, 1.0), (1, 2), (True, False), ("PASS", "FAIL")):
            with self.subTest(reference=reference, actual=actual):
                self.assertTrue(verify.classify_report_difference(reference, actual)["incompatible_paths"])

    def test_nonfinite_values_are_rejected_even_if_unchanged(self):
        for value in (float("nan"), float("inf"), -float("inf")):
            with self.subTest(value=value):
                self.assertTrue(verify.classify_report_difference({"value": value}, {"value": value})["incompatible_paths"])

    def test_finite_numeric_changes_are_counted_without_tolerance(self):
        result = verify.classify_report_difference({"values": [1.0, 2.0]},
                                                  {"values": [1.0 + 1e-12, 3.0]})
        self.assertEqual(result, {"numeric_difference_count": 2,
                                  "max_absolute_difference": 1.0, "incompatible_paths": []})

    def test_finite_values_with_overflowing_difference_are_rejected(self):
        self.assertTrue(verify.classify_report_difference(1e308, -1e308)["incompatible_paths"])

    def test_formatting_only_byte_difference_is_not_waived(self):
        self.record["report_comparisons"]["numeric_difference_count"] = 0
        self.assertFalse(verify.verification_passes(self.record, True))

    def test_strict_policy_accepts_identical_reports_and_successful_wrapper(self):
        self.record["scientific"].update(all_canonical_reports_byte_identical=True, wrapper_returncode=0)
        self.record["report_comparisons"].update(all_byte_identical=True, numeric_difference_count=0)
        self.assertTrue(verify.verification_passes(self.record, False))


if __name__ == "__main__":
    unittest.main()
