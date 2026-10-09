# Claims and physical meaning

## Task and comparison class

Use $\hbar=1$ and

$$
H_\delta(t)=\delta a^\dagger a+
\sum_{j=1}^2 Z_j[f_j(t)a^\dagger+f_j(t)^*a].
$$

The detuning $\delta$ is unknown and static. The two error-independent forces
are chosen independently from the same finite-dimensional complex space
$V\subset L^2([0,T])$. Every member satisfies $\int_0^T f(t)dt=0$.
Additional endpoint, frequency, or moment constraints are part of the space
before optimization. The target is the fixed nonzero **unwrapped** angle
$\Theta_0$ in $\exp(i\Theta_0Z_1Z_2)$; local equivalences and angle periodicity
do not change that target.

The cost is

$$E=\int_0^T(|f_1|^2+|f_2|^2)dt.$$

Robust and nominal competitors have the same independent controls, interval,
normalization, and allowed space. This is an effective-force resource, not a
device-power or individual peak-amplitude resource.

## Four distinct requirements

Write $\alpha_j(t)=-i\int_0^t f_j(u)du$,
$m_j=\int_0^T\alpha_j(t)dt$, and
$\chi=-2\operatorname{Re}\int_0^T\alpha_1^*\alpha_2dt$.

| Requirement | Mathematical condition | Meaning |
|---|---|---|
| Nominal closure | $\alpha_j(T)=0$ | The oscillator disentangles at zero detuning. |
| First-order displacement robustness | $m_1=m_2=0$ | The final displacement has no linear static-detuning term. |
| First-order angle robustness | $\chi=\partial_\delta\Theta(0)=0$ | The entangling angle has no linear static-detuning term. |
| Phase evenness | Phase unchanged under reversal of the whole detuning waveform | A stronger property of the conjugate/quadrature construction, not a consequence of angle robustness alone. |

At nominal closure, $m_j=i\int_0^Tt f_j(t)dt$. The right first-order error
generator contains oscillator-only and global terms, together with
$\sum_jZ_j(m_ja^\dagger+m_j^*a)-\chi Z_1Z_2$.
Thus the first two robustness requirements remove different error terms.
This derivative holds on the oscillator's finite-number core; it is not a
uniform operator-norm estimate on arbitrarily energetic states.

The phase slope has a useful physical interpretation. The two qubit parity
sectors must have equal **integrated** displacement-induced oscillator
occupation. Orthogonal quadratures guarantee equality pointwise, which is
stronger than necessary.

## C1. Exact attainable angle cost

Let $(Af)(t)=\int_0^t f(u)du$ and let $P_V$ project onto the force space. In an
orthonormal basis define

$$
K=P_V\frac{A^\dagger-A}{2i}P_V,\qquad
D=P_VA^\dagger AP_V.
$$

$K$ is Hermitian and $D>0$ in a nonzero finite space. For the coefficient
vectors $a,b$ of the forces,

$$
\Theta=2\operatorname{Re}a^\dagger Kb,\qquad
\chi=-2\operatorname{Re}a^\dagger Db,\qquad
E=\|a\|^2+\|b\|^2.
$$

Put $\lambda=\|K\|$ and $r=\min_{\zeta\in\mathbb R}\|K-\zeta D\|$.
Then

$$
E_{\mathrm{nom}}=\frac{|\Theta_0|}{\lambda},\qquad
E_{\mathrm{angle}}=\frac{|\Theta_0|}{r}.
$$

A zero denominator means infeasibility for the nonzero target. The unique
minimizing multiplier centers the extreme eigenvalues:

$$
\lambda_{\max}(K-\zeta_*D)+\lambda_{\min}(K-\zeta_*D)=0.
$$

For $r>0$, normalized eigenvectors $u_+,u_-$ at $+r,-r$ give attaining
forces. If $d_\pm=u_\pm^\dagger Du_\pm$, use
$x=\sqrt{d_-/(d_++d_-)}u_+$ and
$y=\sqrt{d_+/(d_++d_-)}u_-$, then
$a=(x+y)/\sqrt2$, $b=(x-y)/\sqrt2$. This pair has unit cost, zero slope, and
phase $r$. Scale to the target and reverse one force for a negative target.
These are simultaneous coherent forces, not an average over protocols.

The lower bound and attainment are proved in
[the consolidated theorem, §4](../archive/consolidation-2026-10-09/THEOREM.md)
and [the finite-space proof](../archive/consolidation-2026-10-09/prior/THEOREM.md).
The scalar optimization is a structured equality-S-lemma consequence, not a
new general optimization theorem.

## C2. When the angle penalty vanishes

For $K\ne0$,

$$
E_{\mathrm{angle}}=E_{\mathrm{nom}}
\quad\Longleftrightarrow\quad
\lambda_{\max}(K)=-\lambda_{\min}(K)=\|K\|.
$$

Conjugation-invariant spaces guarantee the balanced spectrum. They also allow
a conjugate-to-quadrature pulse conversion preserving the pointwise sum of
squared forces and real-weight moment constraints. A general balanced
spectrum alone does not imply full waveform phase evenness.

For any nominally feasible space $V$, its conjugate completion
$W=V+\overline V$ obeys
$E_{\mathrm{angle}}(W)=E_{\mathrm{nom}}(W)\leq E_{\mathrm{nom}}(V)$.
Independently commandable conjugate directions with any nonzero gains give
this same $W$ when input amplitudes are unrestricted. This compares different
granted spaces and uses output-force cost. It is not a statement about input
power or uncontrolled leakage. The [control-access proof](CONTROL_ACCESS.md)
also derives the sideband phase dictionary and records the physical reading
of the QSCOUT example.

The preserved examples, with identical endpoint and first-moment conditions
within each comparison, give:

| Allowed tones | Angle cost / nominal cost | Interpretation |
|---|---:|---|
| $\{-2\nu,-\nu,\nu,2\nu\}$ | $1$ | Angle stabilization adds no integrated-force cost. |
| $\{\nu,2\nu,3\nu,4\nu\}$ | $5.213046\ldots$ | A strict penalty is forced by this space, even after global optimization. |

Here $\nu=2\pi/T$. The factor compares costs within each space, not laboratory
performance across two devices. The symmetric example has a separate exact
individual-peak obstruction: its robust cost-minimizers do not meet the
nominal common pulse's individual peak cap.

## C3. The full-gate requirement and its minimum cost

For an initially uncorrelated thermal oscillator with fixed finite mean
occupation $\bar n$, without postselection,

$$
\lim_{\delta\to0}\frac{1-F_{\mathrm{avg}}(\delta)}{\delta^2}
=\frac45\left[\chi^2+(2\bar n+1)(|m_1|^2+|m_2|^2)\right].
$$

The nonnegative terms cannot cancel. The exact thermal channel then gives

$$
1-F_{\mathrm{avg}}=O(\delta^4)
\quad\Longleftrightarrow\quad m_1=m_2=\chi=0.
$$

Project the original nominally closed space $V_0$ onto
$V_1=\{f\in V_0:\int_0^Tt f(t)dt=0\}$. Compute $K_1,D_1$ there. The exact
minimum cost for quartic average infidelity is

$$
E_{\mathrm{quartic}}(V_0)
=\frac{|\Theta_0|}{\min_\zeta\|K_1-\zeta D_1\|}.
$$

Empty $V_1$ or zero efficiency means infeasibility. This is a corollary of the
positive coefficient and C1. In conjugation-invariant spaces angle robustness
is free **after** displacement constraints; imposing those constraints can
itself raise the cost.

## C4. A cost certificate below the robust threshold

Every pair in $V$ satisfies

$$|\Theta|\le rE+|\zeta_*|\,|\chi|.$$

When $\zeta_*\ne0$, a nominally feasible budget below $E_{\mathrm{angle}}$
therefore forces a positive quadratic-infidelity coefficient of at least

$$
\frac45\left(\frac{[|\Theta_0|-rE]_+}{|\zeta_*|}\right)^2.
$$

This lower bound need not be attained. It is not the complete sensitivity-cost
frontier or a finite-detuning guarantee. For $\zeta_*=0$, no cost gap exists
and this division is unnecessary.

## C5. A positive spectral band forces growing cost

Suppose $V\ne\{0\}$ consists of distinct positive integer harmonics
$\omega_\ell=n_\ell\nu\in[a,b]$, where $T=2\pi/\nu$ and $0<a<b$, and
every force has zero first moment. Additional linear constraints are allowed.
Then

$$\frac{E_{\mathrm{angle}}}{E_{\mathrm{nom}}}\geq\frac{a+b}{b-a}.$$

For harmonics $N,N+1,N+2,N+3$ with endpoint and first-moment conditions,
robust feasibility holds at every integer $N\geq1$ and

$$\frac{E_{\mathrm{angle}}}{E_{\mathrm{nom}}}
\sim\frac{2\sqrt5}{3}N.$$

This compares matched optima within each prescribed space; the nominal cost
also grows with $N$. Duration, tone count, and absolute bandwidth stay fixed.
The result is a same-model consequence of C1, with a complete
[spectral proof and normalization](SPECTRAL_RESTRICTION.md). It establishes
neither a sharp universal prefactor nor a device-power or finite-detuning law.

## Evidence and remaining assessment

The archive contains twenty scientific check groups and explicit analytical
proofs. Three supplemental exact symbolic groups check C5. The
[separate proof review](PROOF_REVIEW.md) assesses the original derivations;
the [source review](SOURCE_REVIEW.md) records the established ingredients and
the limits of the literature comparison. Run receipts distinguish numerical
assertions from exact reference-byte identity.

The scoped candidate contribution is an attainable physical cost
classification that separates restrictions of the control space from costs
introduced by a particular construction. The present record establishes
neither exhaustive novelty nor experimental significance beyond the model.
