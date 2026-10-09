#!/usr/bin/env python3
"""Verify the complete archive and run its unchanged scientific wrapper.

From the repository root: python scripts/verify.py --output-dir verification-results/run-001
The destination must be new and outside archive/. By default exit 0 requires
infrastructure tests, archive integrity, scientific assertions, and canonical
report bytes to pass independently. --allow-report-differences explicitly accepts
finite floating-point report differences only. No baseline or tolerance is updated.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path, PurePosixPath
import platform
import re
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_PATH = "archive/consolidation-2026-10-09"
ARCHIVE = ROOT / ARCHIVE_PATH
MANIFEST = ROOT / "provenance/archive.json"
EXPECTED_FILE_COUNT = 89
SUITES = ("consolidation", "cost_audit", "resource_review", "pilot")
REFERENCE_REPORTS = {
    "consolidation": "evidence/final.json",
    "cost_audit": "prior/evidence/final.json",
    "resource_review": "prior/prior/evidence/first.json",
    "pilot": "prior/prior/prior/evidence/final.json",
}
ENVIRONMENT_OVERRIDES = {
    "PYTHONDONTWRITEBYTECODE": "1",
    "OPENBLAS_NUM_THREADS": "1",
    "OMP_NUM_THREADS": "1",
}


def file_identity(path: Path) -> dict:
    data = path.read_bytes()
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def load_manifest(path: Path, expected_count: int = EXPECTED_FILE_COUNT) -> dict:
    manifest = read_json(path)
    if not isinstance(manifest, dict) or manifest.get("archive_path") != ARCHIVE_PATH:
        raise ValueError("Unexpected archive_path in provenance manifest")
    files = manifest.get("files")
    if not isinstance(files, dict) or len(files) != expected_count:
        raise ValueError(f"Expected exactly {expected_count} archive files")
    if type(manifest.get("file_count")) is not int or manifest["file_count"] != len(files):
        raise ValueError("Manifest file_count does not match files")
    for name, identity in files.items():
        relative = PurePosixPath(name)
        if (not name or relative.is_absolute() or ".." in relative.parts
                or "\\" in name or relative.as_posix() != name or name == "."):
            raise ValueError(f"Unsafe manifest path: {name!r}")
        if not isinstance(identity, dict):
            raise ValueError(f"Invalid identity for {name}")
        if (type(identity.get("bytes")) is not int or identity["bytes"] < 0
                or not isinstance(identity.get("sha256"), str)
                or not re.fullmatch(r"[0-9a-f]{64}", identity["sha256"])):
            raise ValueError(f"Invalid identity for {name}")
    return files


def archive_inventory(archive: Path) -> tuple[dict, list[str]]:
    """Inventory regular files without following symlinks, including hidden files."""
    if archive.is_symlink() or not archive.is_dir():
        raise ValueError("Archive root must be a real directory")
    files, unsupported = {}, []
    for directory, directories, names in os.walk(archive, followlinks=False):
        for name in list(directories):
            path = Path(directory) / name
            if path.is_symlink():
                unsupported.append(path.relative_to(archive).as_posix())
                directories.remove(name)
        for name in names:
            path = Path(directory) / name
            relative = path.relative_to(archive).as_posix()
            if path.is_symlink() or not path.is_file():
                unsupported.append(relative)
            else:
                files[relative] = file_identity(path)
    return dict(sorted(files.items())), sorted(unsupported)


def check_archive(archive: Path, expected: dict) -> dict:
    actual, unsupported = archive_inventory(archive)
    missing = sorted(expected.keys() - actual.keys())
    extra = sorted(actual.keys() - expected.keys())
    changed = sorted(name for name in expected.keys() & actual.keys()
                     if actual[name] != expected[name])
    return {
        "pass": not (missing or extra or changed or unsupported),
        "file_count": len(actual), "missing": missing, "extra": extra,
        "changed": changed, "unsupported_paths": unsupported,
        "files": actual,
    }


def validate_output(requested: Path, protected: Path = ROOT / "archive") -> Path:
    requested = requested.expanduser()
    # Reject a dangling symlink too, before resolving it to a nonexisting target.
    if requested.is_symlink() or requested.exists():
        raise ValueError("Output directory must not already exist")
    output = requested.resolve()
    protected = protected.resolve()
    if output == protected or protected in output.parents:
        raise ValueError("Output directory must lie outside archive/")
    return output


def environment_record() -> dict:
    packages = {}
    for name in ("numpy", "scipy", "sympy", "mpmath"):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None
    return {
        "python": sys.version, "python_executable": sys.executable,
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(), "machine": platform.machine(),
        "packages": packages, "environment_overrides": ENVIRONMENT_OVERRIDES,
    }


def source_record() -> dict:
    def git(*args):
        try:
            result = subprocess.run(["git", *args], cwd=ROOT, text=True,
                                    capture_output=True, timeout=10, check=True)
            return result.stdout.rstrip("\n")
        except (OSError, subprocess.SubprocessError):
            return None

    source_files = [ROOT / "requirements.txt", MANIFEST]
    for directory in (ROOT / "scripts", ROOT / "tests"):
        source_files.extend(sorted(directory.rglob("*.py")))
    return {
        "git_commit": git("rev-parse", "HEAD"),
        "git_tree": git("rev-parse", "HEAD^{tree}"),
        "git_status_before_output": git("status", "--porcelain=v1", "--untracked-files=all"),
        "source_files": {p.relative_to(ROOT).as_posix(): file_identity(p)
                         for p in source_files if p.is_file()},
    }


def run_logged(command: list[str], log: Path, env: dict, timeout: int) -> dict:
    result = {"command": command, "log": log.name, "returncode": None, "error": None}
    with log.open("xb") as stream:
        try:
            process = subprocess.run(command, cwd=ROOT, env=env, stdout=stream,
                                     stderr=subprocess.STDOUT, timeout=timeout)
            result["returncode"] = process.returncode
        except (OSError, subprocess.TimeoutExpired) as error:
            result["error"] = f"{type(error).__name__}: {error}"
    return result


def scientific_summary(receipt: dict | None, returncode: int | None) -> dict:
    """Keep assertion success separate from byte reproducibility and process exit."""
    result = {"scientific_assertions_pass": False,
              "all_canonical_reports_byte_identical": False,
              "source_unchanged": False, "total_groups": 0,
              "wrapper_returncode": returncode, "receipt_valid": False, "runs": []}
    if not isinstance(receipt, dict):
        return result
    runs = receipt.get("runs")
    if (not isinstance(runs, list) or len(runs) != len(SUITES)
            or any(not isinstance(run, dict) for run in runs)
            or sorted(run.get("suite", "") for run in runs) != sorted(SUITES)):
        return result
    complete = receipt.get("total_groups") == 20 and all(
        type(run.get("groups")) is int and run["groups"] == 5
        and run.get("report_exists") is True for run in runs)
    passed = complete and all(run.get("returncode") == 0 and run.get("status") == "PASS"
                              for run in runs)
    identical = complete and all(run.get("byte_identical") is True for run in runs)
    result.update(
        scientific_assertions_pass=passed and receipt.get("scientific_assertions_pass") is True,
        all_canonical_reports_byte_identical=identical and receipt.get("all_canonical_reports_byte_identical") is True,
        source_unchanged=receipt.get("source_unchanged") is True,
        total_groups=sum(run.get("groups", 0) for run in runs if type(run.get("groups")) is int),
        receipt_valid=complete, runs=runs,
    )
    return result


def classify_report_difference(reference, actual, path="") -> dict:
    """Accept only finite float changes; integer metadata must remain identical."""
    result = {"numeric_difference_count": 0, "max_absolute_difference": 0.0,
              "incompatible_paths": []}
    if type(reference) is not type(actual):
        result["incompatible_paths"].append(path + " (type)")
    elif isinstance(reference, dict):
        if reference.keys() != actual.keys():
            result["incompatible_paths"].append(path + " (keys)")
        for key in sorted(reference.keys() & actual.keys()):
            child = classify_report_difference(reference[key], actual[key], path + "/" + key)
            result["numeric_difference_count"] += child["numeric_difference_count"]
            result["max_absolute_difference"] = max(result["max_absolute_difference"], child["max_absolute_difference"])
            result["incompatible_paths"].extend(child["incompatible_paths"])
    elif isinstance(reference, list):
        if len(reference) != len(actual):
            result["incompatible_paths"].append(path + " (length)")
        for index, (left, right) in enumerate(zip(reference, actual)):
            child = classify_report_difference(left, right, path + "/" + str(index))
            result["numeric_difference_count"] += child["numeric_difference_count"]
            result["max_absolute_difference"] = max(result["max_absolute_difference"], child["max_absolute_difference"])
            result["incompatible_paths"].extend(child["incompatible_paths"])
    elif isinstance(reference, float):
        if not math.isfinite(reference) or not math.isfinite(actual):
            result["incompatible_paths"].append(path + " (nonfinite)")
        elif reference != actual:
            difference = abs(reference - actual)
            if not math.isfinite(difference):
                result["incompatible_paths"].append(path + " (nonfinite difference)")
            else:
                result["numeric_difference_count"] = 1
                result["max_absolute_difference"] = difference
    elif reference != actual:
        result["incompatible_paths"].append(path + " (nonnumeric value)")
    return result


def inspect_reports(output: Path, archive: Path = ARCHIVE) -> dict:
    comparisons = []
    for suite, reference_name in REFERENCE_REPORTS.items():
        reference = archive / reference_name
        report = output / (suite + ".json")
        if report.is_symlink() or not report.is_file():
            raise ValueError(f"Missing or nonregular scientific report: {suite}")
        comparison = classify_report_difference(read_json(reference), read_json(report))
        comparison.update(suite=suite, byte_identical=report.read_bytes() == reference.read_bytes(),
                          reference=file_identity(reference), report=file_identity(report))
        comparisons.append(comparison)
    return {
        "runs": comparisons,
        "all_byte_identical": all(item["byte_identical"] for item in comparisons),
        "numeric_difference_count": sum(item["numeric_difference_count"] for item in comparisons),
        "max_absolute_difference": max(item["max_absolute_difference"] for item in comparisons),
        "finite_numeric_differences_only": all(
            not item["incompatible_paths"]
            and (item["byte_identical"] or item["numeric_difference_count"] > 0)
            for item in comparisons),
    }


def verification_passes(record: dict, allow_report_differences: bool) -> bool:
    science = record["scientific"]
    comparisons = record.get("report_comparisons")
    report_policy_pass = bool(comparisons and comparisons["all_byte_identical"]
                             and comparisons["finite_numeric_differences_only"]
                             and science["all_canonical_reports_byte_identical"]
                             and science["wrapper_returncode"] == 0)
    if allow_report_differences and comparisons:
        report_policy_pass |= bool(comparisons["finite_numeric_differences_only"]
                                   and comparisons["numeric_difference_count"] > 0
                                   and not comparisons["all_byte_identical"]
                                   and not science["all_canonical_reports_byte_identical"]
                                   and science["wrapper_returncode"] == 1)
    return bool(
        not record["errors"]
        and record["archive_integrity_before"] and record["archive_integrity_before"]["pass"]
        and record["archive_integrity_after"] and record["archive_integrity_after"]["pass"]
        and record["infrastructure_tests"] and record["infrastructure_tests"]["returncode"] == 0
        and science["receipt_valid"] and science["scientific_assertions_pass"]
        and science["source_unchanged"] and report_policy_pass)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--allow-report-differences", action="store_true",
                        help="Explicitly accept finite floating-point report differences after all scientific assertions pass; "
                             "never accept source, integer, structure, nonfinite, or assertion failures")
    args = parser.parse_args(argv)
    try:
        output = validate_output(args.output_dir)
    except ValueError as error:
        parser.error(str(error))

    source = source_record()
    # mkdir's exclusive creation also catches a competing invocation's directory.
    output.mkdir(parents=True, exist_ok=False)
    record = {
        "schema_version": 1, "started_utc": datetime.now(timezone.utc).isoformat(),
        "source": source, "environment": environment_record(),
        "archive_path": ARCHIVE_PATH, "archive_integrity_before": None,
        "archive_integrity_after": None, "infrastructure_tests": None,
        "scientific_wrapper": None, "scientific": scientific_summary(None, None),
        "report_comparisons": None,
        "acceptance_policy": ("allow_finite_float_report_differences" if args.allow_report_differences
                              else "strict_report_byte_identity"),
        "verification_pass": False, "errors": [],
    }
    expected = None
    try:
        expected = load_manifest(MANIFEST)
        record["archive_integrity_before"] = check_archive(ARCHIVE, expected)
        if not record["archive_integrity_before"]["pass"]:
            raise ValueError("Archive integrity failed; scientific code was not executed")

        env = dict(os.environ, **ENVIRONMENT_OVERRIDES)
        test_tmp = output / "test-tmp"
        test_tmp.mkdir()
        test_env = dict(env, OGRC_TEST_TMPDIR=str(test_tmp),
                        TMPDIR=str(test_tmp), TEMP=str(test_tmp), TMP=str(test_tmp))
        tests = run_logged(
            [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"],
            output / "infrastructure-tests.log", test_env, 120)
        record["infrastructure_tests"] = tests
        if tests["returncode"] != 0:
            raise ValueError("Infrastructure tests failed; scientific code was not executed")

        wrapper = run_logged(
            [sys.executable, "-B", str(ARCHIVE / "verify.py"), "--output-dir", str(output / "scientific")],
            output / "scientific-wrapper.log", env, 600)
        record["scientific_wrapper"] = wrapper
        wrapper_receipt = output / "scientific/receipt.json"
        receipt = read_json(wrapper_receipt) if wrapper_receipt.is_file() else None
        record["scientific"] = scientific_summary(receipt, wrapper["returncode"])
        if receipt is None:
            record["errors"].append("Scientific wrapper did not produce a receipt; inspect scientific-wrapper.log")
        else:
            record["report_comparisons"] = inspect_reports(output / "scientific")
    except (OSError, ValueError, TypeError) as error:
        record["errors"].append(f"{type(error).__name__}: {error}")
    finally:
        if expected is not None:
            try:
                record["archive_integrity_after"] = check_archive(ARCHIVE, expected)
            except (OSError, ValueError) as error:
                record["errors"].append(f"Final archive check failed: {error}")

    science = record["scientific"]
    record["verification_pass"] = verification_passes(record, args.allow_report_differences)
    record["finished_utc"] = datetime.now(timezone.utc).isoformat()
    with (output / "receipt.json").open("x", encoding="utf-8") as stream:
        json.dump(record, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"verification_pass": record["verification_pass"],
                      "acceptance_policy": record["acceptance_policy"],
                      "scientific_assertions_pass": science["scientific_assertions_pass"],
                      "all_canonical_reports_byte_identical": science["all_canonical_reports_byte_identical"],
                      "report_comparisons": [
                          {key: run[key] for key in ("suite", "byte_identical", "numeric_difference_count",
                                                    "max_absolute_difference", "incompatible_paths")}
                          for run in (record["report_comparisons"] or {}).get("runs", [])],
                      "total_groups": science["total_groups"], "errors": record["errors"],
                      "receipt": str(output / "receipt.json")}, indent=2))
    return 0 if record["verification_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
