# Verification and reproducibility

The root verifier runs **33 infrastructure tests** and **27 scientific check
groups**. It also checks all **89 preserved source files** against
[the source inventory](provenance/archive.json) before and after execution.
The [source provenance](provenance/README.md) identifies the archived package.

The four archived scientific suites contain five groups each, for **20 groups**
total. Their assertions, numerical tolerances, and canonical reports are fixed.
Three exact symbolic groups verify the [spectral-cost corollary](research/SPECTRAL_RESTRICTION.md):
band identities, the four-tone matrix pencil, and asymptotic constants.

Four exact groups check the [sensitivity frontier](research/SENSITIVITY_FRONTIER.md):
physical Fourier forms and coherent-force identities, a smooth noncommuting
optimum and nominal endpoint, support-face attainment and the robust endpoint,
and proportional-matrix infeasibility with exact-budget padding. Their report
is separate from the spectral report and the four archived reports. All
**27 scientific groups** (20 archived, 3 spectral, 4 frontier) are required.

## Environment and commands

Use CPython 3.13.5 and the pinned dependencies: NumPy 2.3.5, SciPy 1.17.0,
SymPy 1.14.0, and mpmath 1.3.0. GitHub Actions uses the same versions.
Single-threaded BLAS/OpenMP and disabled bytecode writes are set by the verifier.
The following command uses the CI portability policy; strict mode is described
below.

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/verify.py \
  --output-dir verification-results/portable-001 --allow-report-differences
```

The output directory must not exist and must be outside `archive/`, including
through symlink aliases. `verification-results/` is ignored by git; an absolute
external output directory is also supported. Existing reports are never
overwritten. Use a different new directory for each run.

## Two explicit acceptance policies

**Strict mode** is the default. Exit zero requires passing infrastructure and
scientific assertions, unchanged archive bytes, and exact byte identity of all
four regenerated scientific JSON reports with their references. All seven
supplemental symbolic groups must also pass with complete reports.

```bash
.venv/bin/python scripts/verify.py --output-dir verification-results/strict-001
```

**Portability mode**, selected with `--allow-report-differences`, runs the same
assertions and preserves the same references. It permits finite floating-point
report values to differ after all scientific assertions pass. Keys, list lengths,
types, integers, strings, and booleans must match; all reports and twenty archived
groups must be present; source integrity must pass before and after execution.
Nonfinite values, subprocess failures, missing reports, or altered archive files
remain fatal. Both supplemental symbolic suites must pass under either policy.
The original scientific assertions define the scientific acceptance tolerances;
finite diagnostic differences are recorded, not treated as certified intervals.

This mode does not change the preserved wrapper's strict return code. The root
receipt records that code and the chosen policy separately. CI uses portability
mode because numerical libraries and CPU implementations can produce different
diagnostic bytes even at the same package versions. Every raw difference remains
in the uploaded receipt. CI success establishes canonical byte reproduction
only when the byte-identity field is true.

## Inspect the result

Read `<output-dir>/receipt.json` and the logs, not just the exit code:

| Receipt field | Meaning |
|---|---|
| `verification_pass` | Pass under the explicitly recorded acceptance policy |
| `acceptance_policy` | Strict reference-byte identity or explicit floating-point-difference policy |
| `archive_integrity_before/after` | Full inventory, including missing, extra, changed, and unsupported paths |
| `infrastructure_tests` | Command, log, exit code, and execution error |
| `scientific.scientific_assertions_pass` | All four archived scientific suites passed all twenty groups |
| `scientific.all_canonical_reports_byte_identical` | Exact reference-byte comparison, separately reported from assertion success |
| `scientific.wrapper_returncode` | Preserved wrapper's exit code |
| `supplemental_run` | Symbolic-check command, log, exit code, and execution error |
| `supplemental_scientific` | Three-group spectral pass, report validation, exact method, and report hash |
| `frontier_run` | Frontier-check command, log, exit code, and execution error |
| `frontier_scientific` | Four-group frontier pass, report validation, exact method, and report hash |
| `report_comparisons` | Generated/reference files, hashes, and difference classification |
| `source` and `environment` | Commit, tree, working-tree status, verifier inputs, interpreter, packages, and thread settings |

`scientific/receipt.json` preserves every canonical-report difference from the
wrapper. Its four reports and logs remain adjacent. `spectral-cost.json` and
`sensitivity-frontier.json`, with their accompanying logs, record the exact
symbolic identities. Source identity includes both checkers, the wrapper, and
infrastructure tests. For release evidence, inspect the clean PR-head receipt
and the separate merged-main receipt.

## Floating-point reproducibility

Identical package versions do not guarantee identical floating-point diagnostic
bytes across platforms. The [platform comparison](provenance/platform-review.json)
provides a concrete example: 123 finite report fields differ, with maximum
absolute difference approximately $3.241\times10^{-10}$, while all assertions,
report structures, and source-integrity checks pass. This record contains the
individual deltas and report hashes for its specified environments.

For a release, use the receipt belonging to that exact commit. GitHub Actions
verifies the actual PR head on pull requests and the pushed commit on main,
and uploads receipts even on failure.

## Fourier-helper inputs

The archived Fourier helper supports distinct nonzero integer harmonics over
their common period $T=2\pi/\nu$. All archived examples satisfy this condition.
The helper checks nonzero modes and shape but does not reject repeated or
noninteger inputs; callers must enforce the full precondition. Its Gram formulas
and reference checks apply to this documented input class.
