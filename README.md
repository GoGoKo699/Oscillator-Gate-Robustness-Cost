# Oscillator Gate Robustness Cost

**The allowed force space decides whether detuning robustness is free, costly, or impossible.**

Two independently controlled qubits can become entangled by driving a shared
oscillator around closed trajectories. How much extra force is needed to make
the entangling angle insensitive to a small frequency error? This repository
gives the exact minimum integrated squared force, constructs controls that
attain it, and determines the smallest residual angle sensitivity at every
feasible force budget.

| Read next | Purpose |
|---|---|
| [Tutorial bridge](research/TUTORIAL_BRIDGE.md) | Start from one external source, translate its pulse-design framework, and work through an example. |
| [Claims and physical meaning](research/CLAIMS.md) · [Theory and proofs](research/THEORY.md) | Read the model, exact costs, attaining controls, and full-gate consequence. |
| [Sensitivity frontier](research/SENSITIVITY_FRONTIER.md) · [Spectral restriction](research/SPECTRAL_RESTRICTION.md) | Understand every force budget and why a narrow positive band can force a large penalty. |
| [Physical controls](research/CONTROL_ACCESS.md) · [Related work](research/RELATED_WORK.md) | Check the sideband mapping, granted control space, and contribution relative to earlier pulse design. |
| [Verification](REPRODUCIBILITY.md) | Reproduce the scientific checks and inspect their evidence. |
| [LLM guide](llms.txt) | Find relevant research questions, search phrases, and authoritative files. |

## The comparison

Fix one ideal linear oscillator, a gate duration, and two independent,
error-independent complex forces in the same finite-dimensional space
$`V\subset L^2([0,T])`$. Every allowed force closes the oscillator at zero
detuning. Both competitors receive the same space, force normalization, and
nonzero **unwrapped** target angle $`\Theta_0`$ in $`\exp(i\Theta_0Z_1Z_2)`$.
The error is an unknown static oscillator-frequency shift.

The resource is

```math
E=\int_0^T\left(|f_1(t)|^2+|f_2(t)|^2\right)dt.
```

This is integrated squared **effective force**. The
[control-access account](research/CONTROL_ACCESS.md) derives its relation to
sideband drives and distinguishes it from laboratory actuator power and
individual peak-amplitude constraints.

## The exact robustness cost

In a nonzero allowed space, $`K`$ is the Hermitian phase matrix and $`D>0`$ is
the trajectory-overlap matrix. Define

```math
\lambda=\|K\|,\qquad
\rho(\zeta)=\|K-\zeta D\|,\qquad
r=\min_{\zeta\in\mathbb R}\rho(\zeta).
```

The minimum costs of the nominal gate and the first-order angle-robust gate are

```math
E_{\mathrm{nom}}=\frac{|\Theta_0|}{\lambda},\qquad
E_{\mathrm{angle}}=\frac{|\Theta_0|}{r}.
```

A zero denominator means infeasibility for the nonzero target. For a nominally
feasible space, the classification is complete:

| Allowed-space geometry | Angle-robust cost |
|---|---|
| Balanced extreme eigenvalues of $`K`$, so $`r=\lambda`$ | No additional cost. Conjugation-invariant spaces guarantee this case. |
| $`0<r<\lambda`$ | A finite, strictly positive penalty. |
| $`K=cD`$ for a nonzero real $`c`$, so $`r=0`$ | No angle-robust gate at any finite cost. |

The [theory](research/THEORY.md) proves a matching lower bound and constructs
simultaneous coherent forces that attain it. The physical condition is equal
**integrated displacement-induced oscillator occupation** in the two qubit
parity sectors. Their trajectories can enclose different oriented areas while
satisfying this occupation balance.

## Sensitivity at every budget

For a feasible force budget $`B\geq E_{\mathrm{nom}}`$, the smallest absolute
static angle slope is

```math
s(B)=\max\left\{0,\sup_{\zeta\ne0}
\frac{|\Theta_0|-B\rho(\zeta)}{|\zeta|}\right\}.
```

Every value is attained by a pair of controls. The
[frontier](research/SENSITIVITY_FRONTIER.md) is convex and nonincreasing; it
reaches zero precisely when the budget can afford the angle-robust optimum.

For an initially uncorrelated thermal oscillator with fixed finite occupation,
angle and displacement errors contribute separately to the leading average
infidelity. In a space satisfying the first force-moment condition
$`\int_0^T t f(t)dt=0`$, the minimum quadratic coefficient is exactly
$`4s(B)^2/5`$. Projecting an original space onto that moment kernel gives the
exact cost of quartic-or-better small-detuning infidelity. The
[full-gate statement](research/CLAIMS.md#c3-the-full-gate-requirement-and-its-minimum-cost)
specifies the channel and assumptions.

A restriction to positive integer harmonics over their common period, with
zero first force moment and frequencies in $`[a,b]`$, $`0<a<b`$, obeys

```math
\frac{E_{\mathrm{angle}}}{E_{\mathrm{nom}}}\geq\frac{a+b}{b-a}.
```

The [four-tone family](research/SPECTRAL_RESTRICTION.md) has feasible robust
gates at every finite band offset and an unbounded cost ratio as that offset
increases. Each ratio compares the two optima in the same allowed space; the
nominal cost also increases.

## One tutorial, then this result

The selected learning anchor is:

> R. Blümel, N. Grzesiak, N. Pisenti, K. Wright, and Y. Nam,
> **Power-optimal, stabilized entangling gate between trapped-ion qubits** (2021).
> [Author version, arXiv:1905.09292v2](https://arxiv.org/abs/1905.09292v2) ·
> [Paper and supplement in one PDF](https://arxiv.org/pdf/1905.09292v2).

This research article's detailed supplement serves as the tutorial. It develops
linear closure constraints, projected phase matrices, spectral cost
optimization, and independently stabilized pulses. The
[tutorial bridge](research/TUTORIAL_BRIDGE.md) selects the sections, translates
the conventions, and connects that framework to the joint optimization here.
The route assumes standard quantum mechanics and linear algebra.

Independent-pulse stabilization, quadrature gates, displacement moments,
trajectory-overlap sensitivity, and the leading thermal fidelity expansion
have direct predecessors. Equality-S-lemma and numerical-range methods are
established mathematical ingredients. The contribution here is the exact joint
resource classification and attainable tradeoff in the prescribed control
class, together with their spectral and full-gate consequences. The
[matched comparison and source passages](research/RELATED_WORK.md) give the
supporting detail.

## Evidence and reproduction

Use Python 3.13.5 and the pinned dependencies. The command below uses the same
portability policy as GitHub Actions:

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/verify.py \
  --output-dir /absolute/path/to/new-results --allow-report-differences
```

The output directory must be new and outside `archive/`. The verifier runs all
27 scientific groups and the infrastructure tests, and checks all 89 archived
source files. Its receipt separates scientific assertions from canonical
report byte identity. [Verification](REPRODUCIBILITY.md) explains the strict
and portability policies; the latter retains every finite floating-point
report difference. Numerical checks support the analytical proofs.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The [LLM guide](llms.txt) supplies relevant research questions, search phrases,
and direct links to authoritative files. Maintainer instructions are in
[AGENTS.md](AGENTS.md).

Code is available under the [MIT license](LICENSE). Linked third-party papers
are not redistributed or relicensed by this repository.
