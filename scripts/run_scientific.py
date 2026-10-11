#!/usr/bin/env python3
"""Run the four numerical scientific suites against protected reference reports.

Use a new output directory outside protected source directories. Assertion
failures and canonical-report differences have separate receipt fields. Any
difference yields nonzero exit status without adjusting assertions or tolerances.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

sys.dont_write_bytecode = True
# Keep direct CLI execution and import-based infrastructure tests equivalent.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify import (ENVIRONMENT_OVERRIDES, MANIFEST, REFERENCE_REPORTS, ROOT,
                    check_source, load_manifest, read_json, run_logged,
                    validate_output)

SUITE_SCRIPTS = {
    "consolidation": "checks/check_gate_dynamics.py",
    "cost_audit": "checks/check_robust_cost.py",
    "resource_review": "checks/check_resource_geometry.py",
    "pilot": "checks/check_oscillator_channel.py",
}


def diffs(reference, actual, path=""):
    """Record every changed field, including both values and numeric distances."""
    result = []
    if isinstance(reference, dict) and isinstance(actual, dict):
        if reference.keys() != actual.keys():
            result.append({"path": path, "kind": "keys",
                           "reference": list(reference), "run": list(actual)})
        for key in sorted(reference.keys() & actual.keys()):
            result.extend(diffs(reference[key], actual[key], path + "/" + str(key)))
    elif isinstance(reference, list) and isinstance(actual, list):
        if len(reference) != len(actual):
            result.append({"path": path, "kind": "length",
                           "reference": len(reference), "run": len(actual)})
        for index, (left, right) in enumerate(zip(reference, actual)):
            result.extend(diffs(left, right, path + "/" + str(index)))
    elif reference != actual or type(reference) is not type(actual):
        entry = {"path": path, "reference": reference, "run": actual, "kind": "value"}
        if (isinstance(reference, (int, float)) and not isinstance(reference, bool)
                and isinstance(actual, (int, float)) and not isinstance(actual, bool)):
            entry.update(kind="numeric", absolute_difference=abs(reference - actual))
        result.append(entry)
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        output = validate_output(args.output_dir)
        expected = load_manifest(MANIFEST)
        before = check_source(ROOT, expected)
        if not before["pass"]:
            raise ValueError("Source integrity failed; scientific code was not executed")
    except (OSError, ValueError) as error:
        parser.error(str(error))
    output.mkdir(parents=True, exist_ok=False)
    env = dict(os.environ, **ENVIRONMENT_OVERRIDES)
    records = []
    for suite, script in SUITE_SCRIPTS.items():
        report = output / (suite + ".json")
        reference = ROOT / REFERENCE_REPORTS[suite]
        execution = run_logged(
            [sys.executable, "-B", str(ROOT / script), "--output", str(report)],
            output / (suite + ".log"), env, 120)
        report_exists = report.is_file() and not report.is_symlink()
        item = {"suite": suite, "script": script,
                "reference": REFERENCE_REPORTS[suite], "report": report.name,
                "log": execution["log"], "returncode": execution["returncode"],
                "error": execution["error"], "report_exists": report_exists}
        if report_exists:
            try:
                data, baseline = read_json(report), read_json(reference)
                item.update(status=data.get("status"), groups=data.get("test_groups"),
                            byte_identical=report.read_bytes() == reference.read_bytes(),
                            differences=diffs(baseline, data))
            except (OSError, ValueError, AttributeError) as error:
                item["error"] = f"{type(error).__name__}: {error}"
        records.append(item)
    after = check_source(ROOT, expected)
    passed = all(item["returncode"] == 0 and item.get("status") == "PASS"
                 and item.get("groups") == 5 and item["error"] is None
                 for item in records)
    identical = all(item.get("byte_identical", False) for item in records)
    unchanged = before["pass"] and after["pass"] and before["files"] == after["files"]
    receipt = {
        "schema_version": 1, "scientific_assertions_pass": passed,
        "all_canonical_reports_byte_identical": identical,
        "source_unchanged": unchanged, "source_integrity_before": before,
        "source_integrity_after": after,
        "total_groups": sum(item.get("groups", 0) for item in records
                            if type(item.get("groups", 0)) is int),
        "runs": records, "environment_overrides": ENVIRONMENT_OVERRIDES,
    }
    with (output / "receipt.json").open("x", encoding="utf-8") as stream:
        json.dump(receipt, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({key: value for key, value in receipt.items()
                      if key not in ("source_integrity_before", "source_integrity_after", "runs")},
                     indent=2))
    return 0 if passed and identical and unchanged else 1


if __name__ == "__main__":
    raise SystemExit(main())
