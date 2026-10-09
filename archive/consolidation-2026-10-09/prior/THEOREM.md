# Exact first-order angle-robustness cost in a finite oscillator-force space

9 October 2026. Continuation of the quadrature-gate resource review. The previous review and original pilot are preserved unchanged under `prior/`. Results in Sections 2–6 below are new derivations in this checkpoint, not statements quoted from the earlier review or an external paper.

## 1. Fixed physical task

Use the single-mode linear-force Hamiltonian, with hbar=1,

\[
H_\delta(t)=\delta a^\dagger a+
\sum_{j=1}^2 Z_j[f_j(t)a^\dagger+f_j(t)^*a].
\]

The unknown error delta is a constant oscillator detuning for the optimization in this note. The exact phase-even construction inherited from the prior review has a stronger arbitrary-waveform property, discussed separately below.

Both qubits independently draw forces from the same fixed finite-dimensional complex linear space V on [0,T]. Every f in V obeys integral f=0, hence nominal oscillator closure. V may also impose real-weight static displacement moments and endpoint conditions, but it need not be invariant under complex conjugation. Forces are open-loop and error independent. No extra mode, squeezing, qubit rotation sequence, heating channel, loss, or feedback has been introduced.

The cost is

\[
E=\int_0^T(|f_1|^2+|f_2|^2)dt.
\]

The target is the specified nonzero unwrapped phase Theta0 of exp(i Theta0 Z1 Z2). Local-gate equivalences and phase periodicity are not optimization freedoms. E is integrated squared effective force, not total experimental power, dissipated heat, a peak cap or bandwidth. The mode and controls must have the same physical normalization on both sides of each comparison.

Fix an orthonormal force basis r_a. Define the primitive operator A by (Af)(t)=integral_0^t f(u)du and matrices

\[
K_{ab}=\left\langle r_a,\frac{A^\dagger-A}{2i}r_b\right\rangle,
\qquad D_{ab}=\langle A r_a,A r_b\rangle.
\]

Then K=K^dagger and D is strictly positive. Indeed c^dagger D c=||Af||^2; its vanishing implies Af=0 and thus f=0 almost everywhere. In finite dimension, D has a strictly positive smallest eigenvalue.

For force coefficient vectors a,b, the inherited exact closed-loop identities are

\[
\Theta=2\operatorname{Re}(a^\dagger Kb),\qquad
\Theta'_0=-2\operatorname{Re}(a^\dagger Db),\qquad
E=||a||^2+||b||^2. \tag{1}
\]

The derivative concerns the accumulated two-qubit phase; it is not a statement that residual displacements vanish to first order. If every basis element additionally has integral t f=0, that displacement cancellation is automatic and adding Theta'_0=0 gives fourth-order small-static-detuning average infidelity for each fixed finite thermal occupation, as in the earlier pilot.

## 2. Complete scalar characterization of the robust optimum

Put lambda=||K||. The nominal optimum is E_nom=|Theta0|/lambda, with the convention that a zero efficiency cannot implement a nonzero target.

Define

\[
r=\min_{\zeta\in\mathbb R}||K-\zeta D||. \tag{2}
\]

**Theorem.** The exact minimum integrated force cost under nominal closure and first-order static-angle robustness is

\[
\boxed{E_{\rm static}=|\Theta_0|/r.} \tag{3}
\]

If r=0, no nonzero phase is compatible with first-order angle robustness. Otherwise the optimum is attained. The scalar zeta is an optimization multiplier, with frequency units; it is not an error value measured or canceled in the experiment.

It is enough to find the unique real root

\[
\lambda_{\max}(K-\zeta_*D)+\lambda_{\min}(K-\zeta_*D)=0. \tag{4}
\]

At this root, the extremal eigenvalues are +r and -r. Thus the remaining numerical step is a monotone scalar eigenvalue equation, not a nonconvex search through pairs of pulse coefficients. The numerical routine in `cost_solver.py` implements this step in floating point; the proof is the argument below.

### 2.1 Lower bound

Set x=(a+b)/sqrt(2), y=(a-b)/sqrt(2). Equation (1) becomes

\[
\Theta=x^\dagger Kx-y^\dagger Ky,\quad
-\Theta'_0=x^\dagger Dx-y^\dagger Dy,\quad
E=||x||^2+||y||^2.
\]

For any zeta and a robust pair,

\[
|\Theta|=|x^\dagger(K-\zeta D)x-y^\dagger(K-\zeta D)y|
\le ||K-\zeta D||E.
\]

Taking the minimum over zeta gives the lower bound (3).

### 2.2 Existence and uniqueness of the scalar root

Let dmin>0 be the smallest eigenvalue of D. For zeta2>zeta1,

\[
K-\zeta_2D\preceq K-\zeta_1D-(\zeta_2-\zeta_1)d_{\min}I.
\]

Both extremal eigenvalues therefore decrease strictly and continuously with zeta. Their sum crosses zero exactly once, since both are positive for sufficiently negative zeta and negative for sufficiently positive zeta.

To the left of that crossing, the norm equals the positive top eigenvalue and decreases. To the right, it equals the magnitude of the negative bottom eigenvalue and increases. The crossing is the global minimizer of (2).

### 2.3 Explicit attaining force pair

Let u_+,u_- be normalized eigenvectors at the root with eigenvalues +r,-r. For r>0 they are orthogonal. Put q_+=u_+^dagger D u_+>0 and q_-=u_-^dagger D u_->0, and choose

\[
x=\sqrt{\frac{q_-}{q_++q_-}}u_+,
\qquad
y=\sqrt{\frac{q_+}{q_++q_-}}u_-.
\]

Then ||x||^2+||y||^2=1 and x^dagger D x=y^dagger D y. With a=(x+y)/sqrt(2), b=(x-y)/sqrt(2), the pair has E=1, Theta'_0=0 and Theta=r. Scale both by sqrt(|Theta0|/r); reverse one force sign for a negative target. The physical pulses are simultaneous linear combinations within V, not a randomized mixture or a sequential average of gates.

Both physical qubits have equal integrated force E/2 in this construction. No equality of their peak amplitudes is implied.

Finally r=0 iff K=zeta_*D. In this case Theta=-zeta_*Theta'_0, so imposing the derivative condition forces Theta=0. This includes every one-dimensional force space.

## 3. Exactly when does robustness have zero integrated-cost penalty?

For K nonzero,

\[
\boxed{
E_{\rm static}=E_{\rm nom}
\quad\Longleftrightarrow\quad
\lambda_{\max}(K)=-\lambda_{\min}(K)=||K||.
} \tag{5}
\]

If the extremes are balanced, the root (4) is zeta_*=0, so r=lambda. If they are unbalanced, the strictly decreasing/increasing norm branches show that the unique nonzero root has r<lambda. The robust optimum then has strictly larger cost, or is infeasible if r=0.

Thus the underlying condition is equal nominal efficiency for opposite phase orientations, not conjugation invariance by itself. The previous theorem supplies a structural way to guarantee this equality: if V is conjugation invariant, CKC=-K. That forces balanced extremes, and the explicit quadrature compiler additionally yields Theta[delta(t)]=Theta[-delta(t)] for every real waveform in the specified Hamiltonian.

Without conjugation symmetry, (5) guarantees only the zero STATIC first derivative. It does not imply exact all-waveform phase evenness. Conjugation is sufficient but not necessary even for cost equality: on [0,2pi], the space spanned by exp(2it)/sqrt(T) and [exp(-it)/2+sqrt(3)exp(-3it)/2]/sqrt(T) is not conjugation invariant, but K=diag(1/2,-1/2). The scalar construction attains zero-cost static-angle robustness there. This example imposes closure but not the first displacement moment.

The compact-operator equality in the earlier conjugation-invariant review remains unchanged. The new necessity statement and scalar characterization are claimed here only for finite-dimensional V, where D has a uniform positive minimum.

## 4. A nonzero penalty with the same four allowed positive-offset tones

This comparison deliberately uses a nonconjugation-invariant force space. Both competitors receive the exact same space and independent addressing.

Set T=2pi (nu=1). Permit the four offsets n=1,2,3,4 and impose both zero force at endpoints and integral t f=0. Nominal closure follows from the harmonics. The complete remaining space has complex dimension two and basis

\[
r_1=(e^{it}-4e^{2it}+3e^{3it})/\sqrt T,
\qquad
r_2=(e^{it}-3e^{2it}+2e^{4it})/\sqrt T.
\]

These are not orthonormal. Their raw matrices are

\[
G=\begin{pmatrix}26&13\\13&14\end{pmatrix},\quad
K_0=\begin{pmatrix}12&7\\7&13/2\end{pmatrix},\quad
D_0=\begin{pmatrix}6&4\\4&7/2\end{pmatrix}.
\]

Use K=G^(-1/2)K0 G^(-1/2), D=G^(-1/2)D0 G^(-1/2) in the theorem. Equivalently all eigenvalues below are generalized by G. The nominal eigenvalues are

\[
\lambda_\pm=\frac{31}{78}\pm\frac{\sqrt{1405}}{390},
\]

both positive, so no zero-penalty robust optimum can exist. The scalar centering condition in two dimensions is zero trace, giving

\[
\zeta_* =\frac{155}{71},\qquad
r=\frac{\sqrt{190905}}{4615}=0.09467535586548\ldots.
\]

Therefore

\[
\boxed{\frac{E_{\rm static}}{E_{\rm nom}}
=\frac{\lambda_+}{r}=5.21304614632\ldots.} \tag{6}
\]

For Theta0=pi/4, E_nom=1.59133408756... and E_static=8.29569803269... in these units. The ratio, not a numerical optimizer, is the exact minimum over both independent pulse shapes. It is unrelated to the earlier 4.664 fixed-first-pulse benchmark, which concerned the symmetric ±1,±2 space and a restricted construction rather than a fundamental cost.

The new robust pair still has O(delta^2) residual displacements, since the entire space obeys the first moment. Its phase need not be even: direct force-ODE integration gives Theta(+.02)-Theta(-.02)=3.1134e-6 for the constructed target pulse, despite a vanishing first derivative. No new full-error or device-fidelity comparison is claimed.

A physical rescaling to a different T multiplies K and r by 1/nu, D by 1/nu^2, and the multiplier by nu. The cost ratio is unchanged. The finite Fourier expansion is over the gate interval; no assertion of compact support and exact global bandlimitation is made.

## 5. The four-tone no-cost example cannot keep the nominal per-qubit peak cap

The earlier review correctly said its particular conversion could increase individual peaks. We now show that choosing a different zero-cost robust pair cannot remove that issue in the same symmetric four-tone space.

Use its real orthonormal functions u,v and matrices K=kJ, D=diag(d1,d2), where

\[
J=\begin{pmatrix}0&i\\-i&0\end{pmatrix},\quad
k=2/(\sqrt{10}\nu),\quad d_1,d_2>0.
\]

For positive target and exact nominal minimum, equality in the spectral bound forces equal norms and b=Ja. Since (DJ+JD)/2=(d1+d2)J/2, zero static derivative forces a^dagger J a=0. Every such pair, up to a common phase, is

\[
a=A(\cos\vartheta,\sin\vartheta),\qquad
b=iA(\sin\vartheta,-\cos\vartheta),\qquad A=\sqrt{E_{\min}/2}.
\]

This characterizes ALL integrated-cost-optimal robust pairs, not just the original split.

At T=2pi, define unnormalized shapes

\[
U=\sqrt{2/5}(\sin t-2\sin2t),\qquad V=\cos t-\cos2t.
\]

With c=cos t,

\[
4-(U^2+V^2)=\frac{(c+1)^2(12c^2-20c+13)}5\ge0.
\]

The nominal common minimizer therefore has per-qubit peak Fmax=sqrt(2)A/sqrt(T), attained at t=pi. A robust minimizer obeys U(pi)=0,V(pi)=-2. To keep BOTH individual peaks no larger than Fmax would require |sin vartheta|=|cos vartheta|=1/sqrt(2). But U'(pi)=-sqrt(10), V'(pi)=0: at either permitted diagonal orientation the magnitude of a force has a nonzero derivative where it already reaches Fmax. It must exceed that cap on one side of the midpoint.

**Conclusion:** no robust gate at the exact minimum integrated cost obeys the nominal common minimizer's per-qubit peak cap. This is not the solution of the complete peak-constrained optimization at larger E, not a minimum-time theorem, and not a claim about an experimentally measured peak.

## 6. Interpretation and proof scope

The scalar matrix problem says precisely which cost comes from the available control space and which can arise from an avoidable design prescription. In the conjugation-invariant class, the nominal phase operator has equally efficient opposite orientations and a robust pair costs no more. In a class with unbalanced extremes, even joint independent optimization has a strictly positive penalty. Holding one pulse direction fixed can add an additional, avoidable penalty on top of the global optimum.

This is a characterization inside an effective single-mode, single-static-error model. It is not a theorem for arbitrary multimode gate errors, multiple independent derivative constraints, different actuator metrics, loss, heating, or peak-limited controls. Several known schemes solve those different tasks; no superiority over them follows from (3).

The matrix centering argument is elementary spectral optimization. No new general minimax principle, eigensolver, Magnus formula, or orthogonal-quadrature gate is claimed. The contribution to assess is the exact control-space resource classification for the specified physical phase sensitivity, with explicit pulses attaining each bound.

## 7. Verification boundaries

Five new check groups pass on first complete run and repetition, with byte-identical reports. They cover exact extremal-eigenvector attainment, physical Fourier matrices and a symbolic one-sided optimum, the necessary-and-sufficient no-cost condition, independent force ODEs, and the full four-tone equality-locus peak obstruction. Random feasible pulse pairs are supplementary inequality checks, not the proof of optimality.

The largest new projected matrix is 6 by 6. The force ODE evolves two complex displacements and one phase, with no oscillator truncation. The unchanged five-group resource review and five-group pilot also pass and reproduce their canonical reports byte-for-byte, including the pilot's 112-dimensional Schrödinger check. All 30 incoming archive files and both integrity manifests are unchanged. No assertion or tolerance was relaxed.
