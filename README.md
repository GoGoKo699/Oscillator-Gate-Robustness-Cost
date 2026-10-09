# Oscillator-Gate-Robustness-Cost

**When does detuning robustness cost extra force?** For two independently
controlled qubits coupled through one ideal oscillator, the answer depends on
the allowed force space. This project determines the exact minimum integrated
squared force, constructs attaining controls, and classifies angle robustness
as free, costly, or infeasible.

The comparison fixes a finite nominally closed complex force space, gate
duration, force normalization, and nonzero unwrapped entangling angle
$\Theta_0$. For its phase operator $K$ and positive trajectory-overlap operator
$D$, define

$$\lambda=\|K\|,\qquad
\rho(\zeta)=\|K-\zeta D\|,\qquad r=\min_{\zeta\in\mathbb R}\rho(\zeta).$$

The exact nominal and angle-robust costs are

$$\boxed{E_{\mathrm{nom}}=\frac{|\Theta_0|}{\lambda},\qquad
E_{\mathrm{angle}}=\frac{|\Theta_0|}{r}.}$$

A zero denominator means infeasibility. Balanced extreme eigenvalues of $K$
characterize zero additional angle cost. Conjugation-invariant spaces satisfy
this condition. Conversely, a narrow positive spectral band can force a large
penalty: for positive integer harmonics over their common period, with zero
first force moment and frequencies in $[a,b]$,

$$\frac{E_{\mathrm{angle}}}{E_{\mathrm{nom}}}\geq\frac{a+b}{b-a}.$$

A four-tone family has feasible robust gates at every finite band offset and
unbounded cost ratio as that offset increases. The nominal cost also increases;
each ratio compares the two optima in the same allowed space.

The full tradeoff is attainable too. For a feasible force budget
$B\geq E_{\mathrm{nom}}$, the smallest absolute static angle slope is

$$\boxed{s(B)=\max\left\{0,\sup_{\zeta\ne0}
\frac{|\Theta_0|-B\rho(\zeta)}{|\zeta|}\right\}.}$$

In a space with zero first force moment, the minimum leading thermal
average-infidelity coefficient is exactly $4s(B)^2/5$. Projecting an original
space onto that moment kernel gives the exact cost of quartic-or-better
small-detuning infidelity.

## Read the result

| Question | Account |
|---|---|
| What is the model and what is proved? | [Claims and physical meaning](research/CLAIMS.md) |
| How do the dynamics, proofs, and attaining controls work? | [Self-contained theory](research/THEORY.md) |
| What is achievable at each force budget? | [Exact sensitivity frontier](research/SENSITIVITY_FRONTIER.md) |
| How large can the forced penalty become? | [Spectral bound and four-tone family](research/SPECTRAL_RESTRICTION.md) |
| How do effective forces relate to physical controls? | [Sideband mapping and control access](research/CONTROL_ACCESS.md) |
| What does the result add to prior pulse design? | [Matched related-work comparison](research/RELATED_WORK.md) |
| Which sources and proof steps support it? | [Source passages](research/SOURCE_REVIEW.md) and [analytical review](research/PROOF_REVIEW.md) |
| How do I reproduce the checks? | [Verification instructions](REPRODUCIBILITY.md) |

The optimization uses established equality-S-lemma and numerical-range
mathematics. Independent-pulse stabilization, quadrature gates, displacement
moments, trajectory-overlap sensitivity, and the leading thermal fidelity
expansion have direct predecessors. The result developed here is the exact
joint resource classification and attainable tradeoff in the prescribed
control class, together with their spectral and full-gate consequences.

Cost means integrated squared **effective force**. The single-mode,
static-error model supplies the comparison; laboratory actuator power,
individual peak caps, and multimode operation require their own resource and
control specifications. The control-access analysis makes this distinction
explicit.

## Reproduce the checks

Use Python 3.13 and the pinned dependencies:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/verify.py --output-dir /absolute/path/to/new-results
```

The output directory must be new and outside `archive/`. The verifier checks
the preserved scientific suites, supplemental proof identities, infrastructure
regressions, and all 89 archived source files. Its receipt separates scientific
assertions from canonical report byte identity. The documented portability
mode permits finite floating-point report differences only after the required
checks pass, while retaining every difference in the receipt.

The [source archive](archive/consolidation-2026-10-09/README.md),
[hash inventory](provenance/archive.json), and [provenance record](provenance/RECOVERY.md)
preserve the underlying evidence. Maintainers can continue from the
[workspace](WORKSPACE.md) and [current work order](work_orders/CURRENT.md).
