# Oscillator-gate robustness cost

An exact attainable resource classification for oscillator-mediated two-qubit gates in a prescribed finite control space: first-order angle robustness can be free, strictly costly, or infeasible. The physical cost is integrated squared effective force. It is not total device power or a peak-amplitude constraint.

Read [the theorem and physical error analysis](THEOREM.md), then [the contribution review](REVIEW.md). The [workspace handoff](PROJECT_HANDOFF.md) fixes the scope and source-attribution boundaries. `prior/` preserves the preceding research record; it is not the required first reading path.

The preserved constructive solver is `prior/cost_solver.py`. The independent new checks are in `check_consolidation.py`. To run all twenty check groups and verify the preserved sources:

```bash
python verify.py --output-dir /absolute/path/to/a/new/results-directory
```

The output directory must not exist and must lie outside this package. See `RUN_RECORD.json` and `evidence/report_comparisons.json` for the completed runs. The wrapper reports exact scientific assertions and canonical-report comparisons separately. Numerical checks do not replace the analytical proofs or an external source review.
