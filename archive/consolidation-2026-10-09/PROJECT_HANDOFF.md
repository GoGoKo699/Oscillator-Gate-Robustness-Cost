# Workspace handoff: oscillator-gate robustness cost

## Identity and protected projects

Working name: **Oscillator-Gate-Robustness-Cost**. No repository was checked, created, edited or merged during this consolidation. All earlier spin-offs remain protected. This handoff does not authorize changes to them or to a new remote destination.

## Reading order

Start with `THEOREM.md`, then `REVIEW.md`, then the preserved `prior/THEOREM.md` for the finite-space constructions and peak obstruction. The previous symmetry review is `prior/prior/REVIEW.md`; the original exact channel and force compiler are in `prior/prior/prior/PILOT.md`. `prior/cost_solver.py` is the existing floating-point constructive solver. `check_consolidation.py` is a separate checker, not a replacement for it.

## Central scientific claim

For a fixed finite nominally closed force space and one static number-detuning error, exact first-order angle-robustness cost equals |Theta0|/min_zeta ||K-zeta D||. The bound is attained. Balanced extreme phase eigenvalues characterize no added integrated-angle cost. Projection onto first-displacement-moment constraints gives the minimum cost for quartic reduced-qubit infidelity for fixed thermal initial oscillator states. The physical comparison is within the same independent complex controls and the same force normalization.

## Claim hierarchy and attributions

Do not present the S-lemma/eigenvalue centering as a new general optimization theorem. Do not claim the first independent-pulse robust gate, first qubus quadrature gate, or first displacement-moment construction. The candidate contribution is the exact physical control-space cost classification and explicit attaining pulses. The four-tone costly/free examples and the per-qubit peak obstruction support it. The sensitivity/fidelity lower bound is a direct corollary, not a finite-error Pareto optimum.

The Bentley full-text reading boundary remains explicit. A future directly covering result should update the contribution assessment. No access failure is evidence of novelty.

## First bounded workspace task

After any separately authorized repository initialization, perform claims-first exposition and a focused proof/source review of the declared result. Check the exact force-to-K,D reduction, thermal-channel coefficient and the distinction between nominal closure, displacement robustness, angle robustness and phase evenness. Do not expand the model merely to obtain another result.

## Preservation and verification

The incoming archive contains 56 files, including three nested manifests, previous source versions, reports and checkers. Preserve their bytes, scientific assertions and tolerances. `notes/incoming_hashes.json` records those bytes. Write new tests and corrections outside `prior/`; explain discrepancies rather than overwriting reference reports.

`verify.py --output-dir /absolute/new/path` runs five current plus fifteen preserved check groups and checks the original manifests. It reports all numerical differences from canonical JSON; scientific passes and byte identity are separate facts. Read the returned receipt rather than claiming hosted or independent review from a local run. No external PDF is included in this package.
