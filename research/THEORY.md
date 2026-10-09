# Exact force cost of oscillator-gate robustness

For two independently driven qubits coupled to one linear oscillator, the
minimum cost of first-order detuning robustness is determined by two finite
matrices. The phase matrix measures nominal entangling efficiency; the
positive displacement-overlap matrix measures angle sensitivity. Their
relative geometry decides whether robustness is free, costly, or infeasible.
This account gives the dynamics, the exact joint optimum and attaining
controls, and the full thermal-channel consequence.

## 1. Model, resource, and requirements

Set $\hbar=1$, fix $T>0$, and use

$$
H_\delta(t)=\delta a^\dagger a+
\sum_{j=1}^2 Z_j\bigl[f_j(t)a^\dagger+f_j(t)^*a\bigr].
\tag{1}
$$

Here $\delta\in\mathbb R$ is an unknown static error. The predetermined,
error-independent forces $f_1,f_2$ are chosen independently from the same
prescribed finite-dimensional complex space $V\subset L^2([0,T])$. Every
element of $V$ obeys $\int_0^T f(t)\,dt=0$. Frequency, endpoint, or additional
linear moment conditions are included in $V$ before either optimization.
Endpoint conditions refer to spaces with specified regular representatives.

The target is the fixed nonzero **unwrapped** angle $\Theta_0$ in
$\exp(i\Theta_0Z_1Z_2)$, up to an overall phase. Its periodic or local-gate
equivalents are not substitute targets. The cost is

$$
E=\|f_1\|_2^2+\|f_2\|_2^2
=\int_0^T\bigl(|f_1(t)|^2+|f_2(t)|^2\bigr)\,dt.
\tag{2}
$$

Both competitors receive the same $V$, duration, independent addressing, and
force normalization. This is integrated squared effective force. The
[control-access account](CONTROL_ACCESS.md) explains its relation to sideband
controls and why it does not automatically equal actuator input power.

Write $\alpha_j(t)=-i\int_0^t f_j(u)\,du$. The requirements are distinct:

| Requirement | Condition |
|---|---|
| Nominal oscillator closure | $\alpha_1(T)=\alpha_2(T)=0$ |
| First-order displacement robustness | $m_j:=\int_0^T\alpha_j(t)\,dt=0$ for each qubit |
| First-order angle robustness | $\chi:=\partial_\delta\Theta(0)=0$ |
| Phase evenness | $\Theta[\delta(\cdot)]=\Theta[-\delta(\cdot)]$ for every real integrable waveform |

The optimization below concerns static angle robustness. Phase evenness is
a stronger property of a particular construction. The thermal-channel
result combines angle and displacement robustness.

## 2. Exact dynamics and the physical derivative

For static detuning define

$$
\beta_j(t;\delta)=-i\int_0^t f_j(u)e^{i\delta u}\,du,
\qquad
B(t;\delta)=Z_1\beta_1(t;\delta)+Z_2\beta_2(t;\delta).
$$

In the interaction picture of $\delta a^\dagger a$, commutators of the
linear-force Hamiltonian are oscillator scalars times commuting qubit
operators. All higher Magnus commutators vanish. With
$D(\beta)=\exp(\beta a^\dagger-\beta^*a)$, the exact propagator is

$$
U_\delta(T)=e^{-i\delta T a^\dagger a}
e^{i\varphi_{\rm g}(\delta)}e^{i\Theta(\delta)Z_1Z_2}
D\bigl(B(T;\delta)\bigr),
\tag{3}
$$

where $\varphi_{\rm g}$ is an overall phase and

$$
\Theta(\delta)=\operatorname{Im}\int_0^T
\bigl[\beta_1^*\dot\beta_2+\beta_2^*\dot\beta_1\bigr]\,dt.
\tag{4}
$$

The oscillator rotation at the left of (3) disappears under the final
partial trace. At $\delta=0$, nominal closure and $\Theta(0)=\Theta_0$ give
the target qubit unitary and an unchanged oscillator, for any initial
oscillator state.

The exact first derivative gives the meaning and sign of angle sensitivity.
Let $n=a^\dagger a$ and
$q=\int_0^T(|\alpha_1|^2+|\alpha_2|^2)\,dt$. Duhamel's formula and
$D(\beta)^\dagger aD(\beta)=a+\beta$ imply

$$
\begin{aligned}
\left.iU_0(T)^\dagger\partial_\delta U_\delta(T)\right|_0
&=\int_0^T U_0(t)^\dagger nU_0(t)\,dt\\
&=Tn+\sum_{j=1}^2 Z_j(m_ja^\dagger+m_j^*a)
  +qI-\chi Z_1Z_2,
\end{aligned}
\tag{5}
$$

with

$$
\boxed{\chi=-2\operatorname{Re}\int_0^T
\alpha_1(t)^*\alpha_2(t)\,dt.}
\tag{6}
$$

Indeed expanding the displaced number operator produces the cross term
$2Z_1Z_2\operatorname{Re}(\alpha_1^*\alpha_2)$. Comparing with the derivative
of the qubit phase in (3) at nominal closure yields (6). Integration by parts
also gives

$$
m_j=i\int_0^T t f_j(t)\,dt,
\qquad
\beta_j(T;\delta)=-i\delta m_j+O(\delta^2).
\tag{7}
$$

Equation (5) is an operator derivative on the oscillator's finite-number
core; no energy-uniform operator-norm expansion is asserted. Setting
$m_1=m_2=\chi=0$ leaves only an oscillator term and an overall phase at first
order. The bus itself still undergoes its detuning-dependent rotation.

### Integrated occupation of the parity sectors

For a centered oscillator state with mean occupation $\bar n$, the nominal
qubit branch $z=(z_1,z_2)\in\{\pm1\}^2$ has occupation
$\bar n+|z_1\alpha_1+z_2\alpha_2|^2$. Set

$$
I_z=\int_0^T|z_1\alpha_1(t)+z_2\alpha_2(t)|^2\,dt.
$$

Then $I_{++}=I_{--}$, $I_{+-}=I_{-+}$, and

$$
\boxed{\chi=-\tfrac12(I_{++}-I_{+-}).}
\tag{8}
$$

Angle robustness therefore requires equal integrated displacement-induced
occupation in the two parity sectors. Equality at every instant is a
sufficient stronger condition. The paths can enclose different oriented
areas while satisfying this occupation balance.

The trajectory-overlap sensitivity and displacement-moment conditions have
direct precedents, including Huo et al., Appendix G. Their laser-detuning
variable uses the opposite sign to the number detuning in (1). The
[matched source comparison](RELATED_WORK.md) records the normalization and
attribution; these identities are physical inputs to the resource theorem.

## 3. Reduction to two finite matrices

Use $\langle f,g\rangle=\int_0^T f(t)^*g(t)\,dt$ and the primitive operator
$(Af)(t)=\int_0^t f(u)\,du$. In an orthonormal basis of $V$, let

$$
K=P_V\frac{A^\dagger-A}{2i}P_V,
\qquad
D=P_VA^\dagger AP_V,
\tag{9}
$$

where the notation denotes restriction to $V$. For coefficient vectors
$c_1,c_2$ of the two forces, (4) and (6) become

$$
\Theta(0)=2\operatorname{Re}(c_1^\dagger Kc_2),\qquad
\chi=-2\operatorname{Re}(c_1^\dagger Dc_2),\qquad
E=\|c_1\|^2+\|c_2\|^2.
\tag{10}
$$

To verify the phase normalization, substitute $\alpha_j=-iAf_j$ into (4)
at zero detuning. Its integral gives
$\operatorname{Im}(\langle Af_1,f_2\rangle+\langle Af_2,f_1\rangle)$,
which equals the first expression in (10). The overlap expression gives the
second. Thus $K$ is Hermitian. Moreover, $D$ is strictly positive whenever
$V\ne\{0\}$: $\langle f,Df\rangle=\|Af\|^2=0$ implies $Af=0$, hence
$f=0$ almost everywhere. Finite dimension then gives $D\succeq d_{\min}I$
for some $d_{\min}>0$.

For a nonorthonormal basis with positive Gram matrix $G$, use the whitened
matrices $G^{-1/2}K_0G^{-1/2}$ and $G^{-1/2}D_0G^{-1/2}$ in every norm or
eigenvalue below. Raw matrix eigenvalues would use a different resource.

## 4. Exact joint minimum and attaining forces

For $V\ne\{0\}$ define

$$
\lambda=\|K\|,\qquad
r=\min_{\zeta\in\mathbb R}\|K-\zeta D\|.
\tag{11}
$$

**Theorem.** The nominal and static angle-robust minimum costs are

$$
\boxed{
E_{\rm nom}=\frac{|\Theta_0|}{\lambda},\qquad
E_{\rm angle}=\frac{|\Theta_0|}{r}.}
\tag{12}
$$

A zero efficiency means infeasibility for the prescribed nonzero target,
and the corresponding minimum is $+\infty$. Both tasks are infeasible if
$V=\{0\}$. Every finite minimum in (12) is attained.

### Nominal bound and equality

The inequalities
$|\Theta|\leq2\lambda\|c_1\|\|c_2\|\leq\lambda E$ give the nominal bound.
If $Ku=\kappa u$, $\|u\|=1$, and $|\kappa|=\lambda>0$, choose

$$
c_1=\sqrt{\frac{|\Theta_0|}{2\lambda}}u,
\qquad
c_2=\operatorname{sgn}(\Theta_0)\operatorname{sgn}(\kappa)c_1.
$$

This attains the target and the first minimum, including when $K$ has only
negative eigenvalues. If $K=0$, every nominal phase is zero.

### Robust lower bound and unique scalar minimizer

Set $x=(c_1+c_2)/\sqrt2$, $y=(c_1-c_2)/\sqrt2$. Then

$$
\Theta=x^\dagger Kx-y^\dagger Ky,\qquad
-\chi=x^\dagger Dx-y^\dagger Dy,\qquad
E=\|x\|^2+\|y\|^2.
\tag{13}
$$

For $\chi=0$ and any real $\zeta$,

$$
|\Theta|=
\left|x^\dagger(K-\zeta D)x-y^\dagger(K-\zeta D)y\right|
\leq\|K-\zeta D\|E.
\tag{14}
$$

To minimize this bound, write
$u(\zeta)=\lambda_{\max}(K-\zeta D)$ and
$\ell(\zeta)=\lambda_{\min}(K-\zeta D)$. For $\zeta_2>\zeta_1$,

$$
K-\zeta_2D\preceq K-\zeta_1D
-(\zeta_2-\zeta_1)d_{\min}I.
$$

Both endpoints decrease strictly and continuously; each tends to opposite
infinities at the two ends of the real line. Hence there is a unique root

$$
u(\zeta_*)+\ell(\zeta_*)=0.
\tag{15}
$$

To its left the norm equals $u(\zeta)$ and strictly decreases; to its right
it equals $-\ell(\zeta)$ and strictly increases. Thus $\zeta_*$ is the unique
minimizer in (11), and the extreme eigenvalues there are $+r,-r$. No
commutation of $K$ and $D$ is required. The multiplier has frequency units;
it is not a measured or deliberately applied detuning.

### Explicit equality construction

Suppose $r>0$. Choose normalized eigenvectors $u_+,u_-$ of
$L=K-\zeta_*D$ at $+r,-r$ and put
$d_\pm=u_\pm^\dagger Du_\pm>0$. Take

$$
x=\sqrt{\frac{d_-}{d_++d_-}}u_+,
\qquad
y=\sqrt{\frac{d_+}{d_++d_-}}u_-.
\tag{16}
$$

They obey $\|x\|^2+\|y\|^2=1$ and $x^\dagger Dx=y^\dagger Dy$.
Their phase is $x^\dagger Lx-y^\dagger Ly=r$. Therefore

$$
c_1=\sqrt{\frac{|\Theta_0|}{r}}\frac{x+y}{\sqrt2},\qquad
c_2=\operatorname{sgn}(\Theta_0)
\sqrt{\frac{|\Theta_0|}{r}}\frac{x-y}{\sqrt2}
\tag{17}
$$

attain the robust target with cost $|\Theta_0|/r$. The opposite-eigenvalue
vectors are orthogonal even when the extrema are degenerate. Each physical
qubit consequently receives integrated force $E/2$. These are simultaneous
coherent forces in $V$, without mixing or concatenating separate protocols.

If $r=0$, then $K=\zeta_*D$ and (10) gives
$\Theta=-\zeta_*\chi$. No nonzero robust phase is possible. Conversely any
real scalar proportionality $K=\zeta D$ makes $r=0$.

### Attribution and a checkable certificate

The scalar norm formulation is a structured application of the equality
S-lemma of Xia, Wang, and Sheu; the preceding proof exposes its attaining
controls directly. In realified coordinates the equality constraint
$h=x^\dagger Dx-y^\dagger Dy$ is a nonzero indefinite quadratic form.
The equality S-lemma applies to
$f_\rho=\rho E-x^\dagger Kx+y^\dagger Ky$: nonnegativity on $h=0$ is
equivalent to some multiplier giving

$$
\operatorname{diag}(\rho I-K+\zeta D,\rho I+K-\zeta D)\succeq0,
$$

or $\rho\geq\|K-\zeta D\|$. The general optimization principle is established
mathematics; see [the primary-source specialization](SOURCE_REVIEW.md).

An optimal candidate with $r>0$ can be certified by
$rI\pm(K-\zeta D)\succeq0$, together with an actual pair satisfying
$\Theta=\Theta_0$, $\chi=0$, and $E=|\Theta_0|/r$. Finite floating-point
residuals are diagnostics, not exact certificates of semidefiniteness or of
$r=0$.

## 5. Free, costly, and infeasible robustness

For nominally feasible $K\ne0$,

$$
\boxed{E_{\rm angle}=E_{\rm nom}
\quad\Longleftrightarrow\quad
\lambda_{\max}(K)=-\lambda_{\min}(K)=\|K\|.}
\tag{18}
$$

Indeed $r=\lambda$ holds exactly when zero is the unique minimizer in (11),
which by (15) is exactly balanced extreme eigenvalues. Otherwise $r<\lambda$.
Combining this with the infeasibility criterion gives the complete finite
classification:

| Matrices | Outcome for a nonzero target |
|---|---|
| $K=0$ | Nominally infeasible |
| $K\ne0$ and its extreme eigenvalues are balanced | Robust and nominal costs coincide |
| $K\ne0$, unbalanced extrema, and $K$ is not proportional to $D$ | Robustness is feasible and strictly costly |
| $K\ne0$ and $K=\zeta D$ for a real scalar $\zeta$ | Nominally feasible, angle-robustly infeasible |

Every one-dimensional nonzero complex force space has scalar $K,D$, with
$D>0$, so it cannot realize a nonzero robust target. Two or more dimensions
are necessary but not sufficient: proportionality can occur in any dimension.

### Conjugation symmetry and full waveform phase evenness

If $V$ is invariant under $Cf=f^*$, then $C$ commutes with the real primitive
operator and with $P_V$. Its antilinearity changes the sign of $i$, so
$CKC=-K$. Each phase eigenvalue has its opposite, proving (18).

More can be attained in this case. Choose a nominal optimal common force
$f_1=f_2=g$ in the $+\lambda$ eigenspace for a positive target, and form

$$
f_1^{\rm sp}=\frac{g-g^*}{\sqrt2},\qquad
f_2^{\rm sp}=\frac{g+g^*}{\sqrt2}.
\tag{19}
$$

These remain in $V$ and preserve $|f_1|^2+|f_2|^2=2|g|^2$ pointwise. Every
homogeneous moment condition $\int w(t)g(t)\,dt=0$ with real weight $w$
is retained. To see the exact phase property, write
$\sqrt2\alpha_g=X+iY$ for real absolutely continuous $X,Y$ vanishing at
both endpoints. The common forces are $(i\dot X-\dot Y)/\sqrt2$, and the
split forces are $i\dot X,-\dot Y$, with nominal trajectories $X,iY$.

For a real integrable detuning waveform $\delta(t)$ set
$\phi(t)=\int_0^t\delta(s)\,ds$. In the dynamics, replace $\delta T$ by
$\phi(T)$ and $e^{i\delta u}$ by $e^{i\phi(u)}$. Direct substitution gives

$$
\begin{aligned}
\Theta_{\rm sp}[\delta]
&=\int_0^Tdt\int_0^tdu\,\mathcal A(u,t)
  \cos[\phi(t)-\phi(u)],\\
\Theta_{\rm com}[\delta]
&=\int_0^Tdt\int_0^tdu\,
 \bigl\{\mathcal A(u,t)\cos[\phi(t)-\phi(u)]
       +\mathcal B(u,t)\sin[\phi(t)-\phi(u)]\bigr\},
\end{aligned}
\tag{20}
$$

where $\mathcal A(u,t)=\dot X(u)\dot Y(t)-\dot Y(u)\dot X(t)$ and
$\mathcal B(u,t)=\dot X(u)\dot X(t)+\dot Y(u)\dot Y(t)$. Thus

$$
\Theta_{\rm sp}[\delta]=\Theta_{\rm sp}[-\delta]
=\tfrac12\bigl(\Theta_{\rm com}[\delta]+\Theta_{\rm com}[-\delta]\bigr).
\tag{21}
$$

At zero error the phase and cost are preserved, so an optimum can satisfy
this stronger phase symmetry at the nominal minimum. A negative target
follows by reversing one split force. No experiment with reversed unknown
error is performed. This waveform identity protects the phase; it does not
imply cancellation of arbitrary-waveform residual displacement. Balanced
extrema without conjugation symmetry only supply the static result (18).

Quadrature-separated gates are established constructions. Their source
attribution and the independent-pulse predecessors are recorded in
[the matched source comparison](RELATED_WORK.md). For an initially asymmetric
$V$, the [conjugate-completion theorem](CONTROL_ACCESS.md) makes explicit which
new control directions are needed to recover this symmetry.

## 6. Full thermal gate error and its exact minimum

Assume that the initial oscillator is uncorrelated with the qubits and is in
a thermal state with fixed finite $\bar n\geq0$. No output is postselected.
Let $p_z=z_1z_2$, $\beta_z=\sum_jz_j\beta_j(T;\delta)$, and
$\Delta\Theta=\Theta(\delta)-\Theta_0$. After composing with the inverse
nominal qubit gate, the exact channel multiplies $|z\rangle\langle w|$ by

$$
c_{zw}=\exp\!\left[
i\Delta\Theta(p_z-p_w)
+i\operatorname{Im}(\beta_z\beta_w^*)
-\left(\bar n+\tfrac12\right)|\beta_z-\beta_w|^2
\right].
\tag{22}
$$

The Weyl product in the thermal trace gives the displayed phase sign, and
the thermal displacement characteristic function gives its real exponent.
For qubit dimension four, entanglement fidelity is
$F_e=\frac1{16}\sum_{z,w}c_{zw}$. The established identity
$F_{\rm avg}=(4F_e+1)/5$ consequently yields

$$
1-F_{\rm avg}=\frac1{20}\sum_{z,w}(1-\operatorname{Re}c_{zw}).
\tag{23}
$$

Use $\beta_j=-i\delta m_j+O(\delta^2)$ and
$\Delta\Theta=\delta\chi+O(\delta^2)$. The Weyl phase starts at second
order, so it has no real contribution at that order. The sums

$$
\sum_{z,w}(p_z-p_w)^2=32,\quad
\sum_{z,w}(z_j-w_j)^2=32,\quad
\sum_{z,w}(z_1-w_1)(z_2-w_2)=0
$$

then give

$$
\boxed{
\lim_{\delta\to0}\frac{1-F_{\rm avg}(\delta)}{\delta^2}
=\frac45\left[\chi^2+(2\bar n+1)(|m_1|^2+|m_2|^2)\right].}
\tag{24}
$$

This leading thermal displacement-plus-angle coefficient is established in
the gate literature, including Huo et al., Appendix G, Eq. (89). The
[matched source comparison](RELATED_WORK.md) identifies that precedent and
the [source review](SOURCE_REVIEW.md) gives Nielsen's fidelity normalization.

All weights are strictly positive. A quartic-or-better error therefore
requires $m_1=m_2=\chi=0$. Conversely those vanishings give
$\beta_j=O(\delta^2)$ and $\Delta\Theta=O(\delta^2)$; substituting into
(22)--(23) proves

$$
\boxed{1-F_{\rm avg}(\delta)=O(\delta^4)
\quad\Longleftrightarrow\quad m_1=m_2=\chi=0.}
\tag{25}
$$

The Taylor remainders hold for each fixed $L^2$ force on the finite interval:
the forces are integrable, all their time moments are finite, and the
single- and double-integral dynamics can be differentiated under the
integrals. The estimate need not have a nonzero fourth-order coefficient.
It is not uniform over temperature, changing pulse families, or arbitrary
oscillator states.

Now start with any prescribed nominally closed finite space $V_0$ and set

$$
V_1=\left\{f\in V_0:\int_0^T t f(t)\,dt=0\right\}.
\tag{26}
$$

Compute $K_1,D_1$ by restriction to this space. Necessity in (25) forces
every qualifying pair originally in $V_0$ into $V_1$. Applying (12) there
therefore proves the global optimum

$$
\boxed{E_{\rm quartic}(V_0)
=\frac{|\Theta_0|}{r_1},\qquad
r_1=\min_{\zeta\in\mathbb R}\|K_1-\zeta D_1\|.}
\tag{27}
$$

Take this cost as $+\infty$ if $V_1=\{0\}$ or $r_1=0$. When it is finite,
(17) on $V_1$ attains it. If $V_0$ is conjugation invariant then so is $V_1$:
angle robustness is free after the displacement constraint is imposed.
The constraint itself can increase cost, so (27) need not equal
$E_{\rm nom}(V_0)$.

## 7. Related resource consequences

The [exact sensitivity-cost frontier](SENSITIVITY_FRONTIER.md) treats
budgets between the nominal and robust thresholds in this same model. The
optimal robust multiplier already gives a simple supporting bound: retaining
the sensitivity term in (13), for every pair in $V$,

$$
\Theta=x^\dagger Lx-y^\dagger Ly-\zeta_*\chi,\qquad
|\Theta|\leq rE+|\zeta_*|\,|\chi|.
\tag{28}
$$

For $\zeta_*\ne0$, (24) converts a cost cap below the robust threshold into
a positive quadratic-infidelity lower bound. This one supporting inequality
need not attain the exact frontier; the linked derivation optimizes all
supporting directions.

The [spectral restriction theorem](SPECTRAL_RESTRICTION.md) applies (12) to
positive integer harmonics in a band $[a,b]$ with zero first moment. It gives
$E_{\rm angle}/E_{\rm nom}\geq(a+b)/(b-a)$ and a four-tone family with
unbounded overhead of the same growth order. This is a matched comparison
within each specified space; its nominal cost grows as well. The
[control-access analysis](CONTROL_ACCESS.md) distinguishes a truly absent
force direction from a nonzero but attenuated independently commandable
direction under the output-force resource.

Equal integrated costs do not imply equal individual peak amplitudes. The
[four-tone equality-family proof](../archive/consolidation-2026-10-09/prior/THEOREM.md#5-the-four-tone-no-cost-example-cannot-keep-the-nominal-per-qubit-peak-cap)
shows an exact example where every robust cost-minimizer violates the
nominal common pulse's individual peak cap. The present theorem optimizes
the declared effective-force resource with one static detuning and one
oscillator; alternative physical resources and additional error constraints
define different optimization problems.

## Sources and reproducibility

The dynamics and pulse-design ingredients have established predecessors:
quadrature gates in Spiller et al.; independent-pulse bilinear stabilization
and nominal power eigenproblems in Blümel et al.; angle-robust gates in Jia
et al.; displacement, phase-slope, and thermal-error formulas in Huo et al.;
the equality S-lemma in Xia--Wang--Sheu; and the average-fidelity identity in
Nielsen. Bibliographic entries and the matched comparison are in
[RELATED_WORK.md](RELATED_WORK.md); the inspected passages are recorded in
[SOURCE_REVIEW.md](SOURCE_REVIEW.md).

The analytical claims above are proved independently of numerical sampling.
The [verification instructions](../REPRODUCIBILITY.md) reproduce the preserved
dynamical and matrix checks and supplemental exact checks, while separately
reporting archive integrity and reference-report byte identity.
