# Repository working rules

Work only in `GoGoKo699/Oscillator-Gate-Robustness-Cost`. The user has authorized
repository changes and merging; that authorization does not extend to other
repositories. Start with `README.md`, `WORKSPACE.md`, and `work_orders/CURRENT.md`.

## Scientific scope

The model is one ideal linear oscillator, two independently controlled qubits,
one unknown static number-detuning error, and a prescribed finite nominally
closed complex force space. Cost means integrated squared effective force.
Keep the nonzero unwrapped target angle and force normalization fixed in all
comparisons. Distinguish nominal closure, displacement robustness, angle
robustness, and the stronger phase-evenness property.

Do not turn the scoped result into a device-power, heating, peak-constrained,
multimode, arbitrary-error, or finite-detuning optimality claim. Further model
extensions need a new scientific work order. Credit the equality S-lemma,
independent-pulse stabilization, quadrature gates, displacement moments, and
average-fidelity identity. A failed source lookup is not evidence of novelty.

## Preservation and verification

`archive/consolidation-2026-10-09/` is an immutable 89-file source record. Preserve
every byte, including old source versions and reports. Do not edit its tests,
tolerances, manifests, or historical statements. Put corrections, current
exposition, and new checks outside the archive with a reason and source link.
`provenance/archive.json` anchors the recovered file inventory; never regenerate
its expected hashes to conceal an archive change.

Run `python scripts/verify.py --output-dir /absolute/new/output-directory` in
the pinned environment. Read the receipt: passing scientific assertions,
canonical report identity, and source integrity are distinct facts. Record
environment differences instead of weakening assertions or replacing evidence.
Default verification is strict about reference bytes. The documented
`--allow-report-differences` mode may accept finite floating-point report
differences only after every scientific assertion, structure check, and archive
integrity check passes; it must still report byte nonidentity explicitly.
Numerical checks are not analytical proofs or external peer review.

Before merging, review and verify the actual PR head, inspect hosted results,
and use an expected-head guard. After merging, verify the merged main separately.
Do not claim a commit, hosted run, or merge succeeded without checking its result.
