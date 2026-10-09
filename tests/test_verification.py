"""Regression tests for archival boundaries and verification failure semantics."""
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

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("repository_verify", ROOT / "scripts/verify.py")
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class TemporaryRepository(unittest.TestCase):
    def setUp(self):
        # All fixtures stay in this authorized repository, including direct test runs.
        temp_root = Path(os.environ.get("OGRC_TEST_TMPDIR", ROOT / "verification-results/test-tmp"))
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temp_root)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.archive = self.root / "archive"
        self.archive.mkdir()
        (self.archive / "a.txt").write_bytes(b"alpha\n")
        (self.archive / "nested").mkdir()
        (self.archive / "nested/b.txt").write_bytes(b"beta\n")
        self.expected = {"a.txt": verify.file_identity(self.archive / "a.txt"),
                         "nested/b.txt": verify.file_identity(self.archive / "nested/b.txt")}

    def write_manifest(self, files=None):
        path = self.root / "manifest.json"
        files = self.expected if files is None else files
        path.write_text(json.dumps({"archive_path": verify.ARCHIVE_PATH,
                                    "file_count": len(files), "files": files}), encoding="utf-8")
        return path


class IntegrityTests(TemporaryRepository):
    def test_complete_inventory_is_accepted(self):
        expected = verify.load_manifest(self.write_manifest(), expected_count=2)
        result = verify.check_archive(self.archive, expected)
        self.assertTrue(result["pass"])
        self.assertEqual(result["files"], self.expected)

    def test_same_size_corruption_is_detected(self):
        (self.archive / "a.txt").write_bytes(b"ALPHA\n")
        result = verify.check_archive(self.archive, self.expected)
        self.assertFalse(result["pass"])
        self.assertEqual(result["changed"], ["a.txt"])

    def test_missing_and_extra_hidden_files_are_detected(self):
        (self.archive / "a.txt").unlink()
        (self.archive / ".unexpected").write_bytes(b"extra")
        result = verify.check_archive(self.archive, self.expected)
        self.assertFalse(result["pass"])
        self.assertEqual(result["missing"], ["a.txt"])
        self.assertEqual(result["extra"], [".unexpected"])

    def test_manifest_traversal_and_noncanonical_paths_are_rejected(self):
        for name in ("../outside", "/outside", "nested/../../outside", "nested/../a.txt",
                     "nested//b.txt", "./a.txt", "nested\\b.txt", "."):
            with self.subTest(name=name):
                files = {name: self.expected["a.txt"]}
                with self.assertRaises(ValueError):
                    verify.load_manifest(self.write_manifest(files), expected_count=1)

    def test_duplicate_manifest_keys_are_rejected(self):
        path = self.root / "manifest.json"
        path.write_text('{"files": {}, "files": {}}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Duplicate JSON key"):
            verify.load_manifest(path, expected_count=0)

    def test_manifest_count_and_digest_are_validated(self):
        with self.assertRaisesRegex(ValueError, "exactly 89"):
            verify.load_manifest(self.write_manifest())
        invalid = copy.deepcopy(self.expected)
        invalid["a.txt"]["sha256"] = "invalid"
        with self.assertRaisesRegex(ValueError, "Invalid identity"):
            verify.load_manifest(self.write_manifest(invalid), expected_count=2)

    def test_symlink_files_and_directories_cannot_escape_archive(self):
        (self.root / "outside").mkdir()
        (self.root / "outside/data.txt").write_bytes(b"secret")
        (self.archive / "a.txt").unlink()
        (self.archive / "a.txt").symlink_to(self.root / "outside/data.txt")
        (self.archive / "external").symlink_to(self.root / "outside", target_is_directory=True)
        result = verify.check_archive(self.archive, self.expected)
        self.assertFalse(result["pass"])
        self.assertEqual(result["unsupported_paths"], ["a.txt", "external"])
        self.assertNotIn("external/data.txt", result["files"])


class OutputTests(TemporaryRepository):
    def test_new_output_is_accepted_without_creating_it(self):
        target = self.root / "runs/new"
        self.assertEqual(verify.validate_output(target, self.archive), target)
        self.assertFalse(target.exists())

    def test_existing_files_and_directories_are_never_overwritten(self):
        for target in (self.archive, self.archive / "a.txt"):
            with self.subTest(target=target), self.assertRaises(ValueError):
                verify.validate_output(target, self.archive)
        self.assertEqual((self.archive / "a.txt").read_bytes(), b"alpha\n")

    def test_output_inside_archive_including_dotdot_is_rejected(self):
        for target in (self.archive / "new", self.root / "runs/../archive/new"):
            with self.subTest(target=target), self.assertRaisesRegex(ValueError, "outside archive"):
                verify.validate_output(target, self.archive)

    def test_output_symlink_to_archive_is_rejected(self):
        alias = self.root / "alias"
        alias.symlink_to(self.archive, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "outside archive"):
            verify.validate_output(alias / "new", self.archive)

    def test_dangling_output_symlink_is_rejected(self):
        alias = self.root / "alias"
        alias.symlink_to(self.root / "new")
        with self.assertRaisesRegex(ValueError, "already exist"):
            verify.validate_output(alias, self.archive)
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
        # Use the actual preserved differ so its numerical evidence is not replaced.
        archive_wrapper = runpy.run_path(str(verify.ARCHIVE / "verify.py"), run_name="preserved_verifier_test")
        differences = archive_wrapper["diffs"]({"residual": 1.0}, {"residual": 1.0 + 1e-12})
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
    def test_failed_subprocess_preserves_exit_and_log(self):
        log = self.root / "failure.log"
        result = verify.run_logged([sys.executable, "-c", "print('failure details'); raise SystemExit(7)"],
                                   log, dict(os.environ), timeout=10)
        self.assertEqual(result["returncode"], 7)
        self.assertIn("failure details", log.read_text())
        with self.assertRaises(FileExistsError):
            verify.run_logged([sys.executable, "-c", "pass"], log, dict(os.environ), timeout=10)


class ReportPolicyTests(unittest.TestCase):
    def setUp(self):
        self.record = {
            "errors": [], "archive_integrity_before": {"pass": True},
            "archive_integrity_after": {"pass": True},
            "infrastructure_tests": {"returncode": 0},
            "scientific": {"receipt_valid": True, "scientific_assertions_pass": True,
                           "all_canonical_reports_byte_identical": False,
                           "source_unchanged": True, "wrapper_returncode": 1},
            "report_comparisons": {"all_byte_identical": False,
                                   "finite_numeric_differences_only": True,
                                   "numeric_difference_count": 2},
        }

    def test_numeric_report_differences_require_explicit_opt_in(self):
        self.assertFalse(verify.verification_passes(self.record, False))
        self.assertTrue(verify.verification_passes(self.record, True))

    def test_opt_in_never_hides_independent_failures(self):
        failures = [
            ("archive_integrity_before", "pass", False),
            ("archive_integrity_after", "pass", False),
            ("infrastructure_tests", "returncode", 1),
            ("scientific", "receipt_valid", False),
            ("scientific", "scientific_assertions_pass", False),
            ("scientific", "source_unchanged", False),
            ("scientific", "wrapper_returncode", 2),
            ("report_comparisons", "finite_numeric_differences_only", False),
        ]
        for section, field, value in failures:
            with self.subTest(section=section, field=field):
                record = copy.deepcopy(self.record)
                record[section][field] = value
                self.assertFalse(verify.verification_passes(record, True))

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
