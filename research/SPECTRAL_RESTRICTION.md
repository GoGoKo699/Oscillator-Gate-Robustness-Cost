# A spectral restriction can force unbounded robustness cost

The [exact cost theorem](CLAIMS.md#c1-exact-attainable-angle-cost) has a
simple consequence beyond an isolated costly example. If an admissible
first-moment-zero force space uses only positive harmonics in a band
$[a,b]$, with $0<a<b$, then

$$
\boxed{\frac{E_{\mathrm{angle}}}{E_{\mathrm{nom}}}
\geq \frac{a+b}{b-a}.}
$$

The ratio is infinite when the robust target is infeasible. Four consecutive
tones with endpoint and first-moment conditions give a feasible family whose
ratio grows at the same order as this bound. Both statements concern the
same ideal oscillator and integrated-force cost as the original theorem;
they are consequences of that theorem, not a new optimization principle.

## Positive-band bound

Fix $T=2\pi/\nu$ and distinct positive integers $n_\ell$, with
$\omega_\ell=n_\ell\nu\in[a,b]$. Use the orthonormal modes
$\phi_\ell(t)=e^{i\omega_\ell t}/\sqrt T$ and any nonzero complex subspace
$V$ of their span satisfying

$$\int_0^T t f(t)dt=0\quad\text{for every }f\in V.$$

Nominal closure is automatic. Further linear restrictions, including endpoint
conditions, are allowed. If $f=\sum c_\ell\phi_\ell$, its first moment is
$\sqrt T\sum c_\ell/(i\omega_\ell)$. Thus $\sum c_\ell/\omega_\ell=0$.
The primitive is

$$Af=\sum_\ell\frac{c_\ell}{i\omega_\ell}
\left(\phi_\ell-\frac1{\sqrt T}\right).$$

The constant part vanishes on $V$. The phase and overlap operators therefore
are the compressions

$$K=P_V\operatorname{diag}(\omega_\ell^{-1})P_V>0,\qquad
D=P_V\operatorname{diag}(\omega_\ell^{-2})P_V>0.$$

Here and below compression means an operator **on $V$**, not an ambient
matrix padded with zeros. Without the first-moment condition, the primitive
Gram matrix contains an additional rank-one term; the displayed formula for
$D$ and this proof cannot simply be reused.

Put $q=(b-a)/(b+a)$ and $\zeta=2ab/(a+b)$. For $a\leq\omega\leq b$,

$$
\left(\frac1\omega-\frac\zeta{\omega^2}\right)+\frac q\omega
=\frac{2b(\omega-a)}{(a+b)\omega^2}\geq0,
$$

$$
\frac q\omega-\left(\frac1\omega-\frac\zeta{\omega^2}\right)
=\frac{2a(b-\omega)}{(a+b)\omega^2}\geq0.
$$

Compression preserves these inequalities, giving
$-qK\preceq K-\zeta D\preceq qK$. Since $K\preceq\lambda I$, where
$\lambda=\|K\|>0$, it follows that

$$r=\min_\xi\|K-\xi D\|\leq\|K-\zeta D\|\leq q\lambda.$$

The exact cost formulas give the boxed result. This is a bound for every
admissible pair in the space, not a limitation of one chosen pulse ansatz.
It is not asserted to be the sharp universal bound.

## A feasible four-tone family

For each integer $N\geq1$, take the four harmonics
$n=(N,N+1,N+2,N+3)$ with

$$\sum_j c_j=0,\qquad\sum_j\frac{c_j}{n_j}=0.$$

The first condition gives $f(0)=f(T)=0$; the second is the first-moment
condition. Both forces range independently over this entire two-dimensional
complex space. Its full parameterization is

$$c=\operatorname{diag}(n)Uz,\qquad
U=\begin{pmatrix}1&0\\-2&1\\1&-2\\0&1\end{pmatrix},\qquad z\in\mathbb C^2.$$

The two constraint rows are independent and annihilate these two independent
columns. Hence no admissible directions have been discarded.

Define the dimensionless matrices

$$
G=U^T\operatorname{diag}(n^2)U
=\begin{pmatrix}6N^2+12N+8&-4N^2-12N-10\\
-4N^2-12N-10&6N^2+24N+26\end{pmatrix},
$$

$$
K_0=U^T\operatorname{diag}(n)U
=\begin{pmatrix}6N+6&-4N-6\\-4N-6&6N+12\end{pmatrix},\qquad
D_0=U^TU=\begin{pmatrix}6&-4\\-4&6\end{pmatrix}.
$$

The cost of one force is $z^\dagger Gz$. In orthonormal coordinates the
physical operators are
$K=G^{-1/2}K_0G^{-1/2}/\nu$ and
$D=G^{-1/2}D_0G^{-1/2}/\nu^2$.

For compact exact expressions write

$$\begin{aligned}
P_N&=5N^4+30N^3+67N^2+66N+27,\\
Q_N&=10N^2+30N+31,\\
R_N&=25N^4+150N^3+335N^2+330N+139,\\
S_N&=45N^4+270N^3+547N^2+426N+117,\\
B_N&=(2N+3)(5N^2+15N+11).
\end{aligned}$$

Then $\det G=4P_N>0$. The dimensionless nominal efficiency and centered
multiplier are

$$\lambda_N=\frac{B_N+\sqrt{S_N}}{2P_N},\qquad
\zeta_N=\frac{B_N}{Q_N}.$$

Indeed, $\operatorname{tr}(G^{-1}K_0)=B_N/P_N$, and its characteristic
discriminant is $S_N/P_N^2$. Also
$\operatorname{tr}[G^{-1}(K_0-\zeta_ND_0)]=0$ and

$$[G^{-1}(K_0-\zeta_ND_0)]^2=r_N^2I,\qquad
r_N^2=\frac{9R_N}{Q_N^2P_N}>0.$$

This raw pencil is similar to the whitened Hermitian matrix. Its eigenvalues
are $\pm r_N$, so the centering theorem identifies the global robust optimum.
We do not take the Euclidean operator norm of the unwhitened pencil.
Physical efficiencies are $\lambda_N/\nu,r_N/\nu$, and the physical optimal
multiplier is $\nu\zeta_N$. The original $N=1$ example is recovered exactly:
$\zeta_1=155/71$ and $r_1^2=190905/4615^2$.

The leading coefficients give

$$N\lambda_N\longrightarrow1,\qquad
N^2r_N\longrightarrow\frac3{2\sqrt5},\qquad
\boxed{\frac{E_{\mathrm{angle}}}{E_{\mathrm{nom}}}
\sim\frac{2\sqrt5}{3}N.}$$

The band bound here is $(2N+3)/3$: the family matches its **growth order**,
not its prefactor. Robust feasibility holds for every finite $N$. Since
displacement robustness is built into the space, the same robust cost gives
quartic-or-better thermal average infidelity. At fixed $\nu$ and target,

$$E_{\mathrm{nom}}\sim\nu|\Theta_0|N,\qquad
E_{\mathrm{angle}}=E_{\mathrm{quartic}}
\sim\frac{2\sqrt5}{3}\nu|\Theta_0|N^2.$$

## Physical meaning and comparison boundary

In a narrow positive band, the phase per unit integrated oscillator occupation
is nearly fixed. Angle robustness equalizes the two parity sectors' integrated
occupation and therefore cancels the leading phase contribution. Only the
smaller variation across the band remains available to produce the target.
This explains the growing cost without a numerical sweep.

The sequence holds duration, tone count, and absolute width $3\nu$ fixed while
the band's offset from the oscillator grows. Each robust gate is compared
with the nominal optimum **in the same space at that $N$**. The nominal cost
itself grows; this is not a fixed-baseline comparison. The limit belongs to
the ideal force model and does not assert that a laboratory approximation
remains valid at arbitrarily large offsets.

Conjugation-invariant spaces instead have zero extra angle cost after the
same displacement constraints. Independent complex control alone does not
imply that symmetry: a positive-frequency space is a counterexample. Thus
the spectral restriction, rather than detuning robustness alone, drives the
penalty. Its relevance to a particular device needs a justified description
of that device's admissible controls.

The [control-access analysis](CONTROL_ACCESS.md) explains why attenuation
alone cannot impose the one-sided space under the present resource model.
It also separates the effective-force spectrum from laboratory sideband
labels and examines a documented implementation.

## Verification

[The exact symbolic checker](../checks/check_spectral_cost.py) verifies the
band identities, constraint kernel and matrix formulas, centered pencil,
recovery of the old example, and asymptotic constants in three groups. It
uses no fitted sweep or floating-point threshold. The root verifier runs
these supplemental checks separately from the twenty immutable historical
groups. Independent analytical review found no gap in the bound, family,
normalization, or asymptotics. These checks support the proof above; they do
not establish novelty or editorial significance.
