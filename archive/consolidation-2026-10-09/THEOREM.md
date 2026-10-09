# Oscillator-mediated gates: exact cost of static-detuning robustness

9 October 2026. Consolidated author-side scientific account. The incoming finite-space theorem, earlier resource review and first pilot are preserved byte-for-byte under `prior/`. The physical error-generator identity, full-channel necessity statement and imperfect-sensitivity cost certificate below are direct consequences derived in this consolidation; they do not change the oscillator or control model.

## 1. Physical task and cost

Set hbar=1 and use

\[
H_\delta(t)=\delta a^\dagger a+\sum_{j=1}^2 Z_j[f_j(t)a^\dagger+f_j(t)^*a].
\]

The unknown detuning delta is constant. Both qubits independently draw error-independent forces from the same prescribed finite-dimensional complex space V of functions on [0,T]. All f in V obey integral f=0, ensuring nominal closure. Endpoint, frequency-support and displacement-moment constraints can be incorporated in V before optimization. The prescribed nonzero, unwrapped target is exp(i Theta0 Z1 Z2). Changing the target by local-gate equivalence or phase periodicity is not an allowed optimization.

The resource is

\[
E=\int_0^T(|f_1|^2+|f_2|^2)dt.
\]

It is integrated squared **effective force**, with fixed physical normalization. Independent addressing is granted to both robust and nominal competitors. This cost is not automatically optical power, heat, bandwidth, a per-qubit peak cap or a minimum gate time. The model has one ideal linear oscillator and no extra stochastic channel or control Hamiltonian. A laboratory mapping has to justify the rotating-frame, mode-isolation and linear-coupling assumptions separately.

## 2. The exact first-order error operator

Define the nominal displacements

\[
\alpha_j(t)=-i\int_0^t f_j(u)du,\qquad
m_j=\int_0^T\alpha_j(t)dt,
\]

and

\[
q=\int_0^T(|\alpha_1|^2+|\alpha_2|^2)dt,\qquad
\chi=\left.\partial_\delta\Theta\right|_0
=-2\operatorname{Re}\int_0^T\alpha_1^*\alpha_2dt.
\]

The right interaction-picture error generator is

\[
\left.iU_0(T)^\dagger\partial_\delta U_\delta(T)\right|_0
=\int_0^T U_0(t)^\dagger nU_0(t)dt
=Tn+\sum_j Z_j(m_j a^\dagger+m_j^*a)+qI-\chi Z_1Z_2. \tag{1}
\]

Proof: the nominal propagator is a commuting-qubit phase times the conditional displacement D[Z1 alpha1+Z2 alpha2]. Its phase commutes with n. Apply D(beta)^dagger a D(beta)=a+beta, expand n, and integrate. Differentiating the propagator by Duhamel's formula gives the first equality.

Equation (1) is an operator derivative on the oscillator's finite-number core, with the usual domain extensions. It is **not** an operator-norm expansion uniform over arbitrarily energetic oscillator states.

At nominal closure, integration by parts gives m_j=i integral t f_j(t)dt. Thus first-moment displacement stabilization removes the linear oscillator terms. The angle condition chi=0 removes the ZZ term. What remains is oscillator-only plus a global phase. This is first-order factorization of the joint evolution, not literal insensitivity of the bus itself to a frequency change.

### Physical meaning of the angle derivative

For a centered initial oscillator with mean occupation nbar, the nominal occupation on the qubit branch z=(z1,z2) is nbar+|z1 alpha1+z2 alpha2|^2. Let I_z be the time integral of its displacement-induced part. Then

\[
\chi=-\tfrac12(I_{++}-I_{+-}). \tag{2}
\]

The two parity sectors must accumulate equal integrated oscillator occupation for first-order angle robustness. They need not have equal occupation at every instant. Orthogonal-quadrature controls enforce pointwise equality and are a stronger sufficient construction; the general spectral optimum only needs the integrated balance.

## 3. Exact leading average-infidelity coefficient

Take an initially uncorrelated thermal oscillator with a fixed finite occupation nbar >=0. No output is postselected. The reduced two-qubit gate is compared with its exact nominal target.

The exact displaced-thermal-state channel implies

\[
\boxed{\lim_{\delta\to0}\frac{1-F_{\rm avg}(\delta)}{\delta^2}
=\frac45\left[\chi^2+(2\bar n+1)(|m_1|^2+|m_2|^2)\right].} \tag{3}
\]

Derivation: let beta_j(delta)=-i integral f_j(t)e^(i delta t)dt and beta_z=sum z_j beta_j. The nominal-relative channel multiplies |z><w| by

\[
\exp\{i(\Theta-\Theta_0)(z_1z_2-w_1w_2)
+i\operatorname{Im}(\beta_z\beta_w^*)
-(\bar n+\tfrac12)|\beta_z-\beta_w|^2\}.
\]

Here beta_j=-i delta m_j+O(delta^2). The fidelity relation Favg=(4 Fe+1)/5 is established [N02]. Expanding the sixteen channel entries gives sum_(z,w)(z1z2-w1w2)^2=32 and sum_(z,w)(zj-wj)^2=32. Cross terms and the second-order Weyl phase cancel in the summed real part, yielding (3).

All terms in (3) are nonnegative. Therefore, within this model,

\[
1-F_{\rm avg}=O(\delta^4)
\quad\Longleftrightarrow\quad
m_1=m_2=0\ \text{and}\ \chi=0. \tag{4}
\]

The reverse direction uses beta_j=O(delta^2) and Theta-Theta0=O(delta^2) in the exact channel, not an assumption that every pulse has an even detuning response. This is a fixed-pulse, fixed-temperature asymptotic statement. It is not a finite-detuning uniform error guarantee or an energy-unconstrained diamond-norm estimate.

**The two errors cannot cancel one another in this leading average-infidelity coefficient.** Angle-only stabilization can still leave quadratic gate error. Conversely, closed trajectories with zero first moments can retain a quadratic error from their angle slope.

## 4. Exact global angle-robust cost

Choose an orthonormal basis in V. With (A f)(t)=integral_0^t f(u)du, define

\[
K=P_V\frac{A^\dagger-A}{2i}P_V,\qquad D=P_V A^\dagger A P_V.
\]

For coefficient vectors a,b,

\[
\Theta=2\operatorname{Re}a^\dagger Kb,\quad
\chi=-2\operatorname{Re}a^\dagger Db,\quad E=\|a\|^2+\|b\|^2.
\]

K is Hermitian; D is strictly positive in a finite nonzero force space. Define

\[
\lambda=\|K\|,\qquad r=\min_{\zeta\in\mathbb R}\|K-\zeta D\|.
\]

The incoming exact theorem is

\[
\boxed{E_{\rm nom}=|\Theta_0|/\lambda,\qquad
E_{\rm angle}=|\Theta_0|/r.} \tag{5}
\]

Zero efficiency means the corresponding nonzero target is infeasible. The unique minimizing multiplier solves

\[
\lambda_{\max}(K-\zeta_*D)+\lambda_{\min}(K-\zeta_*D)=0. \tag{6}
\]

A concise proof also gives a certificate. Set x=(a+b)/sqrt2 and y=(a-b)/sqrt2. Robustness means x^dagger D x=y^dagger D y. For any zeta, the phase is bounded by ||K-zeta D|| E. Both endpoint eigenvalues decrease strictly with zeta, since D>=dmin I>0; hence their sum has a unique zero and the norm is minimized there. At the zero take normalized extreme eigenvectors u+ and u- with eigenvalues +r,-r. Let d+=u+^dagger D u+, d-=u-^dagger D u-. Set

\[
x=\sqrt{\frac{d_-}{d_++d_-}}u_+,\qquad
 y=\sqrt{\frac{d_+}{d_++d_-}}u_-.
\]

The unit-cost pair a=(x+y)/sqrt2,b=(x-y)/sqrt2 has chi=0 and phase r. Scale by sqrt(|Theta0|/r) and reverse one force for a negative target. Degenerate endpoint eigenspaces are allowed. The pulses are a coherent simultaneous control pair, not a mixed or time-averaged protocol.

A claimed solution can be independently checked through

\[
rI\pm(K-\zeta D)\succeq0,
\qquad \Theta=\Theta_0,\quad\chi=0,\quad E=|\Theta_0|/r. \tag{7}
\]

In floating point, residuals in (7) are diagnostics; certified enclosures or exact algebra are needed for a rigorous numerical interval. Infeasibility near r=0 must not be inferred by rounding. The preserved solver explicitly raises an unresolved-numerics exception there.

### Zero penalty and the stronger conjugation case

For K nonzero,

\[
\boxed{E_{\rm angle}=E_{\rm nom}
\iff \lambda_{\max}(K)=-\lambda_{\min}(K)=\|K\|.} \tag{8}
\]

The two extreme nominal phase orientations must have equal efficiency. Conjugation-invariant V guarantees CKC=-K and thus (8). The old conversion f1=(g-g*)/sqrt2, f2=(g+g*)/sqrt2 then also enforces exact phase evenness for arbitrary detuning waveforms, preserves all real-weight moment constraints and the pointwise sum of squared force amplitudes. Without conjugation symmetry, (8) implies static angle robustness but not full waveform evenness.

## 5. Corollary: the exact minimum for quartic full-gate error

Starting with any allowed finite nominally closed space V0, define

\[
V_1=\{f\in V_0:\int_0^T t f(t)dt=0\}.
\]

Compute K1,D1 on that subspace. Equations (4)–(5) give the complete fixed-model result

\[
\boxed{E_{\rm quartic}(V_0)
=\frac{|\Theta_0|}{\min_\zeta\|K_1-\zeta D_1\|}.} \tag{9}
\]

An empty subspace or zero efficiency means infeasibility. Equation (9) minimizes over all pulse pairs originally granted V0, not just a chosen ansatz: (4) forces every qualifying pair into V1. This is a direct combination of established displacement-moment stabilization, the incoming angle-cost theorem, and the positive fidelity coefficient—not a new noise model or a separate optimization principle.

When V0 is conjugation invariant, so is V1. In that case angle robustness adds no cost **after** the displacement constraints are imposed. Enforcing those displacement constraints can itself increase the cost relative to E_nom(V0). It would be incorrect to describe all full-gate robustness as free relative to an unconstrained nominal gate.

## 6. A below-threshold force budget forces a quadratic error

The same optimal multiplier supplies a bound even away from chi=0. For every pulse pair in V,

\[
\boxed{|\Theta|\le rE+|\zeta_*|\,|\chi|.} \tag{10}
\]

It follows by retaining the zeta*(x^dagger D x-y^dagger D y) term instead of imposing robustness. If zeta* is nonzero and a nominal target is achievable at cost E<E_angle, then

\[
|\chi|\ge\frac{[|\Theta_0|-rE]_+}{|\zeta_*|},
\]

and hence

\[
\boxed{\lim_{\delta\to0}\frac{1-F_{\rm avg}(\delta)}{\delta^2}
\ge\frac45\left(\frac{[|\Theta_0|-rE]_+}{|\zeta_*|}\right)^2.} \tag{11}
\]

This is a rigorous leading-coefficient bound, not the exact sensitivity/cost Pareto frontier or a finite-detuning inequality. If zeta*=0 there is no interval between nominal and angle-robust costs; division by zero is neither needed nor allowed.

### Existing four-positive-tone example

Retain the prescribed tones nu,2nu,3nu,4nu with nu=2pi/T and both zero endpoints and zero first displacement moments. For nu=1 its raw basis matrices are

\[
G=\begin{pmatrix}26&13\\13&14\end{pmatrix},\quad
K_0=\begin{pmatrix}12&7\\7&13/2\end{pmatrix},\quad
D_0=\begin{pmatrix}6&4\\4&7/2\end{pmatrix}.
\]

Whitening by G gives zeta*=155/71 and r=sqrt(190905)/4615. For Theta0=pi/4, E_nom=1.59133408756... and E_angle=E_quartic=8.29569803269..., giving the preserved factor 5.21304614632.... No physical benchmark has changed.

With dimensionless detuning epsilon=delta/nu, the following bounds use E/nu:

| Allowed cost | Lower bound on absolute phase slope | Lower bound on lim (1-Favg)/epsilon^2 |
|---|---:|---:|
| Nominal minimum | 0.2907509742 | 0.0676289032 |
| Half the robust minimum | 0.1798815148 | 0.0258858875 |
| 90% of the robust minimum | 0.0359763030 | 0.0010354355 |

The bound holds for every finite fixed thermal occupation and all nominal-target pulses within each cost cap. The values are lower bounds, not claims of attainability. The exact robust optimum removes that quadratic coefficient.

The conjugation-symmetric four-tone space {±nu,±2nu} retains E_angle=E_nom=pi sqrt10 |Theta0|/T after the same endpoint and moment conditions. Its complete equality family still violates the nominal common pulse's individual peak cap. Those preserved results limit the meaning of a zero integrated-cost penalty.

## 7. Mathematical and physical attribution

The constrained scalar norm is a direct structured instance of the **S-lemma with equality** [XWS16]. This identification strengthens the source audit rather than adding another novelty claim. In realified pulse coordinates w=(x,y), use

\[
f_\rho(w)=\rho(\|x\|^2+\|y\|^2)-x^\dagger Kx+y^\dagger Ky,
\qquad h(w)=x^\dagger Dx-y^\dagger Dy.
\]

Since D>0, h is genuinely quadratic and takes both signs. Theorem 3 of [XWS16] applies: f_rho>=0 on h=0 iff some zeta makes f_rho+zeta h>=0 everywhere. The latter is exactly

\[
\operatorname{diag}(\rho I-K+\zeta D,\rho I+K-\zeta D)\succeq0,
\]

or rho>=||K-zeta D||. The matrix optimization therefore must not be advertised as a new minimax or convexity theorem. The short constructive proof above avoids relying on a black-box optimization result, but does not create mathematical priority.

Blümel et al. [BG21] already supplies force-bilinear angle constraints, displacement stabilization, nominal power eigenproblems and a two-independent-pulse stabilization construction. Spiller et al. [Q06] supplies quadrature-separated oscillator gates. Jia et al. [J23] supplies angle-robust gates with a different multimode construction. The candidate physical contribution is the exact cost classification and attaining controls within the explicitly matched single-mode resource class. Newer and older laboratory performance cannot be inferred from the numerical factors here.

## 8. Sources and verification

- [BG21] R. Blümel et al., *Power-optimal, stabilized entangling gate between trapped-ion qubits*, npj Quantum Information 7, 147 (2021), arXiv:1905.09292v2. Primary main text and combined-PDF S16, Eqs. S82–S83 and the ensuing construction inspected. https://arxiv.org/pdf/1905.09292 ; https://doi.org/10.1038/s41534-021-00489-w
- [Q06] T. P. Spiller et al., *Quantum Computation by Communication*, New Journal of Physics 8, 30 (2006), arXiv:quant-ph/0509202v3, Sec. IV and Eqs. (7)–(9). https://arxiv.org/pdf/quant-ph/0509202
- [J23] Z. Jia et al., *Angle-robust two-qubit gates in a linear ion crystal*, Physical Review A 107, 032617 (2023), arXiv:2210.04814. Angle/displacement distinction and discussion inspected; no figure performance data used. https://arxiv.org/pdf/2210.04814
- [N02] M. A. Nielsen, *A simple formula for the average gate fidelity of a quantum dynamical operation*, Physics Letters A 303, 249–252 (2002), arXiv:quant-ph/0205035v2, Eq. (3). https://arxiv.org/pdf/quant-ph/0205035
- [XWS16] Y. Xia, S. Wang, R.-L. Sheu, *S-Lemma with Equality and Its Applications*, Mathematical Programming 156, 513–547 (2016), arXiv:1403.2816v3, Assumption 1 and Theorem 3. The homogeneous indefinite case used here is within the stated hypothesis, not the exceptional linear-constraint case. https://arxiv.org/pdf/1403.2816 ; https://doi.org/10.1007/s10107-015-0907-0

All five new check groups passed in three final runs; an earlier four-group passing version is retained. The three preserved five-group scientific suites passed unchanged. Every repeated report matches its respective canonical JSON byte-for-byte. The new error-operator calculation uses 80 qubit–oscillator dimensions, checks Fock inputs 0,1,2 and reaches a maximum derivative-vector discrepancy 2.67e-13; the small cutoff occupation is a diagnostic, not a rigorous unbounded-oscillator certificate. The prior pilot includes a 112-dimensional Schrödinger check. The mathematical statements rest on the stated proofs, not those finite checks.
