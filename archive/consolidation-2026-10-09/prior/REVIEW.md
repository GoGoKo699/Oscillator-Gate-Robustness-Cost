# Contribution review: when angle robustness costs integrated force

9 October 2026. This is a continuation of the fresh quadrature-control exploration only. No repository has been accessed, created, or modified.

## What changed

The preceding result gave a sufficient symmetry condition under which first-order entangling-angle robustness and the nominal gate have the same optimal integrated-force cost. The current derivation closes the corresponding finite-control-space optimization without assuming that symmetry:

- E_static=|Theta0|/min_zeta ||K-zeta D||, with an explicitly attaining pair.
- Zero penalty occurs iff the nominal phase matrix has balanced largest positive and negative eigenvalues.
- The conjugation-invariant theorem follows immediately, and retains its stronger arbitrary-waveform phase-even construction.
- A fixed four-positive-tone space with endpoint and first-moment constraints has a rigorously unavoidable cost factor 5.213046..., contrasted with the factor one in the symmetric ±1,±2 space.
- Within the symmetric four-tone space, every robust integrated-cost minimizer violates the nominal common optimum's per-qubit peak cap. The no-cost statement cannot silently be promoted to simultaneous peak preservation.

These are new author-side derivations. They are not quoted external results, not a correction to the preserved conditional theorem, and not a new microscopic gate model. The multiplier is a mathematical parameter, not the unknown physical detuning.

## Strongest predecessor reconstruction

### Blümel et al., npj Quantum Information 7, 147 (2021)

The primary combined PDF arXiv:1905.09292v2 explicitly provides nominal power-eigenproblem optimization and independently applied pulse functions. Its S16 Eqs. (S82)–(S83) impose a bilinear target and bilinear derivative constraints; its subsequent construction freezes one nominal optimum and projects the second pulse. S17 first reduces sensitive directions and then uses that construction. The main text and S16 report increased power for the illustrated stabilization procedures.

Our general scalar solution is a specialization to ONE positive-definite displacement-overlap constraint, not a solution of their many-mode, arbitrary-order system. Their source force functions are real laboratory functions with mode-dependent phases; those are not silently identified with arbitrary complex one-mode forces. The earlier factor 4.664 is an adapted comparison in the declared symmetric space, not an experimental ratio or proof that their full independent-pulse feasible set excludes our optimum.

Their quadratic formalism already contains the optimization ingredients. The additional result is a closed global solution and precise zero-penalty criterion for the stated physical specialization. It would be an overclaim to describe it as a new general quadratic optimization principle or the first independently controlled angle-robust gate.

### Spiller et al., New Journal of Physics 8, 30 (2006)

Section IV of arXiv:quant-ph/0509202v3, especially Eqs. (7)–(9), gives the orthogonal-quadrature controlled-displacement gate and bus return without measurement. Applying the pilot's stipulated number-detuning error to its finite-duration linear-force version gives the same phase-evenness mechanism. The gate primitive is inherited.

### Jia et al., Physical Review A 107, 032617 (2023)

Section III A of arXiv:2210.04814 derives opposite angle sensitivities by reflecting detunings around two motional frequencies, then concatenates half-angle gates. That comparison uses two modes and a common drift with specified weights. It is not ruled out by our one-mode identical-force obstruction. Its reported power cost cannot be transferred into our matched complex control space, and our scalar definite-D result does not optimize that entire multimode problem.

### Other relevant controls and current status

Arrazola and Casanova, Communications Physics 6, 123 (2023), construct low-intensity dynamical-decoupling sequences with static longitudinal coupling and qubit pulses. The primary article distinguishes the qubit-control Rabi amplitudes from the effective oscillator force; those constraints do not match our independently programmable complex-force space. This is a relevant counterexample to interpreting our resource as all laboratory gate costs.

Bowers et al., Physical Review Letters 137, 080602 (20 August 2026), report robust trapped-ion gates using amplitude and frequency ramping. Publisher metadata/abstract and the NIST primary record confirm its current publication; no experimental fidelity or power number is used for a claimed advantage. The new theorem is not the first robust oscillator-mediated operation.

Bentley et al., arXiv:2005.00366, remains a relevant independent-control numerical-optimization predecessor identified in the prior source log. Its PDF retrieval failed again. No absence assertion about its complete body, or source-access novelty claim, is made here. The available core predecessors are sufficient to delimit this theorem's claim: a single-mode analytic optimum, not an assertion that numerical independent control cannot discover it.

## What the evidence supports

The result now has a complete bounded resource question: for a fixed finite closed pulse space, does first-order oscillator-detuning angle robustness impose an integrated-force penalty, and what is its optimum? The theorem answers both, including feasible and infeasible cases, instead of evaluating only a favorable pulse or stating a sufficient symmetry condition.

The positive physical case is that it separates a penalty forced by the allowed control space from one introduced by freezing a pulse or imposing additional restrictions. The same single-mode apparatus model supports both an exact zero penalty and a strictly unavoidable penalty. The theorem gives explicit optimal force pairs and identifies the resource condition under which the zero-cost conclusion applies.

The strongest skepticism remains significance. The mathematical reduction is elementary, and it addresses one effective mode and one static derivative, not the full set of errors limiting current hardware. Establishing a new gate primitive, a universal speedup, or a laboratory power advantage is outside the result. The retrieved primary sources do not directly state the complete scalar cost formula in the inspected sections, but that is not exhaustive priority clearance.

## Allocation

**GO for consolidation of one bounded control-cost result.** The conjunction of the exact global optimum, the zero-penalty criterion, and the control-space counterexample is more informative than an isolated quadrature pulse conversion. It merits a versioned scientific account and author-facing significance assessment; it does not justify a strong PRL prediction.

No further noise model, higher derivative order, spectator-mode optimization, or larger pulse catalogue is a prerequisite for assessing this claim. The next useful phase is a compact claims-first account with independent scrutiny of the two-level force reduction, the scalar spectral proof, and the strongest optical-control predecessors. Repository work still requires an explicitly selected destination and permission; none is created here.

The central sentence is: **For oscillator-mediated gates in a specified finite control space, first-order angle robustness can either be free or carry an unavoidable integrated-force penalty; the exact distinction is the spectrum of the nominal phase operator.**
