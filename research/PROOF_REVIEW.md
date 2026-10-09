# Scoped analytical proof review

Reviewed on 9 October 2026 (UTC). This is a separate-agent analytical check of
the recovered account, not external peer review. It does not establish
publication priority. No archive file was changed.

**Conclusion:** the stated finite-space cost theorem and its full thermal-gate
corollary follow under the declared assumptions. No unresolved mathematical
gap was found in the claims reviewed below. The numerical and source-review
limitations at the end remain distinct from that conclusion.

## Scope and inputs

The scope is one ideal linear oscillator, two independently chosen,
error-independent forces in the same finite complex subspace
$V\subset L^2([0,T])$, nominal closure for every element of that space, one
unknown **static** number-detuning error, and integrated squared effective
force. The target is a fixed nonzero unwrapped angle. The full-channel claim
also assumes an initially uncorrelated thermal oscillator with fixed finite
occupation. These hypotheses are essential to the conclusions stated here.

The analytical inputs were the [consolidated theorem](../archive/consolidation-2026-10-09/THEOREM.md),
the [finite-space theorem](../archive/consolidation-2026-10-09/prior/THEOREM.md),
the [earlier resource review](../archive/consolidation-2026-10-09/prior/prior/REVIEW.md),
and the [original pilot](../archive/consolidation-2026-10-09/prior/prior/prior/PILOT.md).
The [consolidation checker](../archive/consolidation-2026-10-09/check_consolidation.py)
and [preserved solver](../archive/consolidation-2026-10-09/prior/cost_solver.py)
were read to compare their formulas with those arguments. Test execution and
archive-hash verification belong to the separate reproducibility receipt;
they are not asserted by this analytical review.

| Claim | Finding |
|---|---|
| Force-to-$K,D$ reduction and first-order generator | Resolved under nominal closure and the stated force convention |
| Scalar centering and explicit attaining controls | Resolved, including degenerate extrema and the infeasible case |
| Zero extra angle-robustness cost iff balanced extrema | Resolved for finite nonzero $K$ and strictly positive $D$ |
| Full thermal quadratic coefficient and quartic iff | Resolved for each fixed pulse and finite thermal occupation |
| Projection gives the global quartic-error minimum | Resolved within the originally granted control space |
| Below-threshold sensitivity lower bound | Resolved as a leading-coefficient bound, without an attainability claim |
| Symmetric four-tone individual-peak obstruction | Resolved at the exact integrated-cost minimum |

## 1. Force reduction and the physical derivative

Use the inner product $\langle f,g\rangle=\int f^*g$,
$Af(t)=\int_0^t f(s)\,ds$, and $\alpha_j=-iAf_j$.
The exact nominal Magnus cross phase is

$$
\Theta=\operatorname{Im}\int
  (\alpha_1^*\dot\alpha_2+\alpha_2^*\dot\alpha_1)\,dt
=2\operatorname{Re}\langle f_1,Kf_2\rangle,
\qquad K=P_V\frac{A^\dagger-A}{2i}P_V.
$$

This fixes the sign of $K$ for the Hamiltonian and target convention used
in the archive. The primitive Gram matrix is
$D=P_VA^\dagger AP_V$. Its quadratic form can vanish only when
$Af=0$, hence $f=0$ almost everywhere. On a nonzero finite-dimensional
space this implies a strictly positive smallest eigenvalue.

For the nominal conditional displacement
$\beta=Z_1\alpha_1+Z_2\alpha_2$, conjugating the number operator gives

$$
D(\beta)^\dagger nD(\beta)
=n+\beta a^\dagger+\beta^*a+|\beta|^2.
$$

Duhamel differentiation therefore produces the archived right error
generator. Its $Z_1Z_2$ coefficient is
$2\operatorname{Re}\int\alpha_1^*\alpha_2=-\chi$, consistent with
$iU_0^\dagger\partial_\delta e^{i\Theta(\delta)Z_1Z_2}
=-\Theta'(0)Z_1Z_2$ at nominal closure after dropping irrelevant nominal
global phases. Thus

$$
\chi=-2\operatorname{Re}\langle f_1,Df_2\rangle.
$$

No missing endpoint term survives because both nominal final displacements
vanish. Integration by parts gives
$m_j=\int\alpha_j=i\int t f_j$, with the same convention. Setting
$m_1=m_2=\chi=0$ removes the first-order joint error terms that act on
the qubits; the oscillator-only rotation remains. This argument is a strong
derivative on suitable finite-energy vectors, not a uniform operator-norm
statement on an unbounded oscillator Hilbert space.

## 2. Scalar minimization and attainment

In an orthonormal force basis set
$x=(a+b)/\sqrt2$, $y=(a-b)/\sqrt2$. The phase, negative angle
slope, and cost become

$$
\Theta=x^\dagger Kx-y^\dagger Ky,\qquad
-\chi=x^\dagger Dx-y^\dagger Dy,\qquad
E=\|x\|^2+\|y\|^2.
$$

For $\chi=0$, subtracting any real multiple of the second form gives
$|\Theta|\le\|K-\zeta D\|E$. Both extremal eigenvalues of
$L(\zeta)=K-\zeta D$ decrease strictly with $\zeta$, since for
$h>0$, $L(\zeta+h)\preceq L(\zeta)-hd_{\min}I$.
Their continuous sum has exactly one zero. Before that zero the norm equals
the top eigenvalue and strictly decreases; after it the norm equals the
negative bottom eigenvalue and strictly increases. Thus the zero is the
unique global minimizer, without assuming that $K$ and $D$ commute.

For positive optimum radius $r$, choose any normalized eigenvectors
$u_+,u_-$ at the opposite extrema $+r,-r$. They are orthogonal
even if either extremum is degenerate. With
$d_\pm=u_\pm^\dagger Du_\pm>0$, the archived weights

$$
x=\sqrt{\frac{d_-}{d_++d_-}}u_+,\qquad
y=\sqrt{\frac{d_+}{d_++d_-}}u_-
$$

give unit cost, zero slope, and phase exactly $r$. They are actual
simultaneous force coefficients. Scaling the two forces and reversing one
sign when needed attains $|\Theta_0|/r$. The nominal bound
$|\Theta|\le\|K\|E$ is likewise attained using a maximal-magnitude
eigenvector and a suitable relative sign. A positive top eigenvalue is not
required for that nominal construction.

If $r=0$, then $K=\zeta_*D$ and
$\Theta=-\zeta_*\chi$, so a nonzero robust target is impossible.
There is no division by zero or limiting attaining pulse. This includes
every one-dimensional complex force space. If $K=0$, the nominal target
is already infeasible. No infinite-dimensional extension of the positive
$d_{\min}$ centering proof is used.

## 3. Zero penalty and conjugation

For $K\ne0$, equality between nominal and robust efficiencies means
that $\zeta=0$ minimizes the scalar norm. Uniqueness of that minimizer
then gives

$$
\lambda_{\max}(K)+\lambda_{\min}(K)=0.
$$

Conversely this equality centers the extrema at zero and proves zero
additional angle-robustness cost. Thus the criterion is necessary and
sufficient, rather than merely a property of the displayed examples.

Conjugation-invariant $V$ gives $CKC=-K$, hence balanced extrema.
The archived quadrature conversion also preserves pointwise total squared
force and real-weight displacement moments. Its cosine-kernel expression
proves the stronger waveform phase-evenness statement. Balanced extrema
alone prove only the static first-derivative result; they do not supply
that waveform symmetry or first-moment cancellation.

## 4. Full thermal coefficient and quartic error

Write $z=(z_1,z_2)\in\{\pm1\}^2$, $p_z=z_1z_2$, and
$\beta_z=\sum_j z_j\beta_j$. Cyclically tracing the two conditional
displacements against a thermal state gives the channel multiplier

$$
c_{zw}=\exp\!\left[
i(\Theta-\Theta_0)(p_z-p_w)
+i\operatorname{Im}(\beta_z\beta_w^*)
-(\bar n+\tfrac12)|\beta_z-\beta_w|^2\right].
$$

In particular the Weyl phase has the sign stated in the consolidated
account. At nominal closure,
$\beta_j=-i\delta m_j+O(\delta^2)$ and
$\Theta-\Theta_0=\delta\chi+O(\delta^2)$. For this dimension-four
diagonal channel,
$1-F_{\rm avg}=\sum_{z,w}(1-\operatorname{Re}c_{zw})/20$.
The relevant sums are

$$
\sum_{z,w}(p_z-p_w)^2=32,\quad
\sum_{z,w}(z_j-w_j)^2=32,\quad
\sum_{z,w}(z_1-w_1)(z_2-w_2)=0.
$$

The Weyl phase starts at second order and has no real contribution at that
order. Expanding the other terms yields exactly

$$
\lim_{\delta\to0}\frac{1-F_{\rm avg}}{\delta^2}
=\frac45\left[\chi^2+(2\bar n+1)(|m_1|^2+|m_2|^2)\right].
$$

Every weight is strictly positive for the stated thermal states. Hence
quartic-or-better infidelity forces all three quantities to vanish; phase
and displacement errors cannot cancel in this coefficient.

For sufficiency, those vanishings imply $\beta_j=O(\delta^2)$ and
$\Theta-\Theta_0=O(\delta^2)$. The exact channel then gives
$1-F_{\rm avg}=O(\delta^4)$. The required Taylor remainders follow
from fixed $L^2$ forces on a finite interval: they are integrable, all
time moments are bounded, and the displacement and double-integral phase
can be differentiated under their integrals. No assumption that the full
response is even is needed. “Quartic” here means the stated upper-order
bound; it does not require a nonzero fourth-order coefficient.

Because the necessity argument forces each original pulse into
$V_1=\{f\in V_0:\int t f=0\}$, applying the same exact cost theorem
on $V_1$ is a global optimization over all qualifying pairs originally
allowed in $V_0$. An empty space or zero robust efficiency gives
infeasibility. Cost equality after this projection says nothing about the
possible cost of imposing the projection itself.

## 5. Sensitivity floor and peak caveat

For an arbitrary pair, the same decomposition gives
$\Theta=x^\dagger Lx-y^\dagger Ly-\zeta_*\chi$. Therefore
$|\Theta|\le rE+|\zeta_*||\chi|$. Combining its rearrangement with
the positive thermal coefficient proves the archived below-threshold
quadratic-error floor. It is a lower bound, with no proof of simultaneous
attainability at each cost cap. When $\zeta_*=0$, the nominal and
angle-robust minima coincide, and there is no interval requiring the
division by $|\zeta_*|$.

For the symmetric four-tone peak claim, use the real basis $(u,v)$ with
$K=kJ$, $J^2=I$, and positive diagonal $D$. Equality in the
positive-target nominal bound requires $b=Ja$ and equal force norms.
The slope then vanishes exactly when $a^\dagger Ja=0$, because
$DJ+JD=(d_1+d_2)J$. Such a two-component vector is real up to a common
complex phase, including cases with a zero component. This proves the
complete robust equality family stated in the archive.

With the unnormalized shapes $U,V$, the polynomial identity for
$4-(U^2+V^2)$ is nonnegative: the quadratic factor
$12c^2-20c+13$ has negative discriminant and positive leading
coefficient. Equality at $t=\pi$ establishes the nominal common
per-qubit cap $\sqrt2 A/\sqrt T$. Applying this cap to both robust
forces at that time forces
$|\sin\vartheta|=|\cos\vartheta|=1/\sqrt2$. At those orientations,
$U'(\pi)=-\sqrt{10}$ and $V'(\pi)=0$ give a nonzero derivative
of a nonzero force magnitude already at the cap, so it exceeds the cap
on one side of the interior midpoint. The obstruction therefore covers
every exact integrated-cost-optimal robust pair, not just the compiler's
particular output. It does not solve the larger-cost peak-constrained
problem.

## Remaining boundaries

- **Source priority is not resolved by this check.** The archive identifies
  the equality S-lemma and the physical predecessors. This review checks
  the direct arguments; bibliographic coverage and originality require
  the separate source review and, ultimately, external scrutiny.
- **Floating-point residuals are not certified intervals.** The archived
  solver correctly refuses to decide the near-zero robust-efficiency
  case numerically. Its successful finite checks do not prove general
  matrix claims or uniform bounds on the unbounded oscillator.
- **The Fourier helper has an unstated input precondition.** Its raw
  Gram formulas assume distinct nonzero integer harmonics over
  $T=2\pi/\nu$. The function currently checks nonzero modes and shape,
  but does not reject repeated or noninteger modes. Every reviewed
  scientific example uses valid distinct integer modes, so no result
  needs correction. Any future supported API should state or validate
  that precondition before reuse; the immutable helper is unchanged.
- **No broader physical claim follows.** Finite-error operating windows,
  temperature-uniform errors, other initial oscillator states, physical
  actuator power, and changed control models are outside this review.

No new numerical tests were added: the claims were resolved analytically,
and the existing independent implementations already target the displayed
constructions. Repetition of those tests would not strengthen the proof
conclusion.

