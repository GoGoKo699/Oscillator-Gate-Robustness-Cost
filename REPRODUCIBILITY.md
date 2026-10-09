# Verification and reproducibility

The complete scientific source is immutable under
`archive/consolidation-2026-10-09/`. The root verifier checks all **89 files**
against [the recovery inventory](provenance/archive.json), runs the
infrastructure regression tests, and invokes the preserved scientific wrapper.
The four scientific suites contain five groups each, for **20 groups** total.
All original assertions, numerical tolerances, and canonical reports remain
unchanged.

The root verifier also runs three exact symbolic groups for the
[spectral-cost corollary](research/SPECTRAL_RESTRICTION.md). These are new
checks outside the archive, recorded separately from its twenty groups and
four canonical reports. They verify the band identities, four-tone matrix
pencil, and asymptotic constants without numerical sweeps.

## Environment and commands

The scientific archive records CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, and
SymPy 1.14.0. The repository pins these libraries and mpmath 1.3.0;
GitHub Actions uses Python 3.13.5. Single-threaded BLAS/OpenMP and disabled
bytecode writes are set by the verifier.

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/verify.py --output-dir verification-results/strict-001
```

The output directory must not exist and must be outside `archive/`, including
through symlink aliases. `verification-results/` is ignored by git; an absolute
external output directory is also supported. Existing reports are never
overwritten. Use a different new directory for each run.

## Two explicit acceptance policies

**Strict mode** is the default. Exit zero requires passing infrastructure and
scientific assertions, unchanged archive bytes, and exact byte identity of all
four regenerated scientific JSON reports with their historical references.
All three supplemental symbolic groups must also pass with a complete report.

**Portability mode** runs the same assertions and preserves the same references:

```bash
.venv/bin/python scripts/verify.py \
  --output-dir verification-results/portable-001 \
  --allow-report-differences
```

It additionally permits finite floating-point report values to differ after
all scientific assertions pass. Keys, list lengths, types, integers, strings,
and booleans must match, all reports and twenty groups must be present, and
source integrity must pass before and after execution. Nonfinite values,
subprocess failures, missing reports, or altered archive files remain fatal.
The supplemental symbolic checks must pass under either policy; portability
never waives their failure or an incomplete report.
It does not establish numerical equality or certified error intervals; the
original scientific assertions define the scientific acceptance tolerances.

This mode does not change the preserved wrapper's strict return code. The root
receipt records that code and the chosen policy separately. The CI workflow
uses portability mode because numerical libraries and CPU implementations can
produce different diagnostic bytes even at the same package versions. Every
raw difference remains in the uploaded scientific receipt. CI success must
not be described as canonical byte reproduction unless the byte field is true.

## Inspect the result

Read `<output-dir>/receipt.json` and the logs, not just the exit code:

| Receipt field | Meaning |
|---|---|
| `verification_pass` | Pass under the explicitly recorded acceptance policy |
| `acceptance_policy` | Strict reference-byte identity or explicit floating-point-difference policy |
| `archive_integrity_before/after` | Full inventory, including missing, extra, changed, and unsupported paths |
| `infrastructure_tests` | Command, log, exit code, and execution error |
| `scientific.scientific_assertions_pass` | All four unchanged scientific suites passed all twenty groups |
| `scientific.all_canonical_reports_byte_identical` | Exact reference-byte comparison, never inferred from a scientific pass |
| `scientific.wrapper_returncode` | Unmodified historical wrapper's exit code |
| `supplemental_run` | Symbolic-check command, log, exit code, and execution error |
| `supplemental_scientific` | Separate three-group pass, report validation, exact method, and report hash |
| `report_comparisons` | Independently inspected generated/reference files, hashes, and difference classification |
| `source` and `environment` | Commit, tree, working-tree status, verifier inputs, interpreter, packages, and thread settings |

`scientific/receipt.json` preserves every canonical-report difference from the
original wrapper. Its four reports and logs remain adjacent. No canonical
evidence is rewritten. A dirty source status identifies a development run;
review the exact clean PR head and merged main separately for release evidence.
`spectral-cost.json` and `spectral-cost.log` sit beside the root receipt and
record the supplemental proof identities. Source identity includes the new
checker as well as the wrapper and infrastructure tests.

## Recovery-platform review

The first restored scientific run used CPython 3.12.14. A second used the
recorded CPython 3.13.5, with the same pinned scientific packages. Both passed
all twenty groups and kept every source byte unchanged. Their four regenerated
reports are byte-identical **to each other**, but differ from the archive in
123 finite floating-point fields:

| Suite | Changed fields | Maximum absolute difference from historical JSON |
|---|---:|---:|
| Consolidation | 38 | $3.550\times10^{-13}$ |
| Cost audit | 80 | $3.241\times10^{-10}$ |
| Resource review | 3 | $4.164\times10^{-17}$ |
| Pilot | 2 | $1.219\times10^{-17}$ |

The largest difference is in a displacement-ratio diagnostic near 3.93; the
phase-slope diagnostic differs by approximately $1.074\times10^{-11}$.
The actual changed fields, exact deltas, and report hashes are retained in
[the platform review](provenance/platform-review.json). No key, shape, type,
exact symbolic value, or pass status changed. Matching Python versions did not
restore historical byte identity, so this record does not attribute the cause
to Python alone or claim a fully identical historical execution environment.

The platform review records initial recovery runs, not the final commit or a
hosted run. GitHub Actions verifies the actual PR head on pull requests and
the pushed commit on main, and uploads receipts even on failure. Inspect the
specific commit/run and its artifact before claiming hosted verification.
