# Oscillator-gate robustness-cost checkpoint

Read `THEOREM.md` for the finite-control-space cost formula and proofs, then `REVIEW.md` for its contribution assessment and `SOURCE_READINGS.md` for the external-source boundaries.

`cost_solver.py` supplies a numerical implementation of the scalar eigenvalue-centering construction. `check_audit.py` contains five checks. The proof does not rely on a parameter scan or on random feasible-pulse tests.

Run, using a new report filename:

```sh
python check_audit.py --output /tmp/quadrature_cost_new.json
python prior/check_review.py --output /tmp/quadrature_prior_review_new.json
python prior/prior/check_pilot.py --output /tmp/quadrature_prior_pilot_new.json
```

All reports refuse overwrites. `prior/` preserves the entire 30-file incoming archive. Its source, canonical reports, and two manifests are unchanged. `MANIFEST.json` inventories this checkpoint; `RUN_RECORD.json` records the executed checks and source comparisons.

No repository or workspace was modified. No device-level power, peak-constrained optimum, or independent proof review is claimed.
