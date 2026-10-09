# Matched-control-space review: angle robustness without extra integrated force

9 October 2026. Continuation of the single-mode quadrature-gate pilot. The original pilot and all its evidence are preserved unchanged under `prior/`.

## 1. Result and allocation

The matched-resource comparison supports a stronger statement than improvement over one common-drive example. For a fixed, conjugation-invariant complex force space, **adding first-order oscillator-detuning robustness of the entangling angle does not increase the minimum integrated squared effective force**. The same optimum can satisfy the pilot's exact phase-sign-reversal symmetry for arbitrary detuning waveforms. Any static-displacement cancellation constraints already built into that force space are retained.

For the complete four-effective-tone space at offsets ±nu and ±2nu, with zero force at the two endpoints and first-order displacement cancellation, the exact common optimum and robust independent optimum coincide:

\[
E_{\min}=\frac{\pi\sqrt{10}}{T}|\Theta_0|,\qquad \nu=2\pi/T.
\]

The smooth pulse in the prior pilot attains this optimum. It was previously optimized only within its displayed ansatz; the present bound covers every pair of complex pulses in the stated tone space.

Applying Blümel et al.'s **fixed-one-pulse projection strategy** to this same effective control space yields a larger cost, by the exact factor sqrt(1762)/9. This is our adaptation of a published construction, not the performance of the source's multimode experiment. The source's general two-pulse constraints already contain our solution: choosing both pulses jointly, rather than freezing one nominal optimum, removes that particular penalty.

**Allocation: retain the conditional equality for focused theorem/contribution review.** No universal hardware improvement or strong PRL forecast follows. The meaningful additional question is whether phase robustness has an unavoidable integrated-force cost once independent conjugate controls are available. It does not in this model. Per-qubit peaks, absent mirror tones, nonidentical actuator metrics, spectator modes and physical laser power are not optimized by this theorem. No repository is opened or modified.

## 2. Unchanged effective model and the matched resources

The Hamiltonian is

\[
H_\delta(t)=\delta(t)a^\dagger a+
\sum_{j=1}^2 Z_j[f_j(t)a^\dagger+f_j(t)^*a],
\qquad E=\sum_j\int_0^T |f_j(t)|^2dt.
\]

Both qubits now receive **the same allowed complex function space** \(\mathcal V\subset L^2([0,T];\mathbb C)\), independently. The comparison does not grant independent addressing only to the robust protocol: it is available to every competitor, including the nominal optimum.

We assume that V is closed and complex linear, all its elements obey integral f=0, and

\[
f\in\mathcal V\Longrightarrow f^*\in\mathcal V.
\]

A finite complex span of real pulse functions satisfying the same homogeneous moment and endpoint conditions is an important example. Extra static-displacement constraints such as integral t^r f=0 have real weights and preserve this property. A common finite-time Fourier basis must contain the reflected offsets if it is to have this symmetry.

The resource is integrated squared **effective force**, not a thermodynamic heat, total optical energy, a peak-amplitude bound, or a fixed number of laboratory lasers. The allowed Fourier offsets refer to the expansion during the gate interval, not a claim that a compactly time-gated pulse is strictly bandlimited on the entire real line. All compared pulses in the finite example have the same gate window and vanishing force endpoints.

We target a specified unwrapped phase \(\Theta_0\), with the example \(\Theta_0=\pi/4\). We do not optimize over changing the target by local correction gates or by exploiting phase periodicity.

## 3. The nominal optimization includes arbitrary independent pulses

Let

\[
(\mathsf A f)(t)=\int_0^t f(u)du,
\quad \mathsf K=P_{\mathcal V}\frac{\mathsf A^\dagger-\mathsf A}{2i}P_{\mathcal V}.
\]

The nominal displacements are \(\alpha_j=-i\mathsf A f_j\). Directly from the exact Magnus phase,

\[
\Theta(f_1,f_2)=2\operatorname{Re}\langle f_1,\mathsf K f_2\rangle.
\]

The operator K is compact and self-adjoint. Complex conjugation C obeys

\[
C\mathsf K C=-\mathsf K,
\]

because A is real and V is conjugation invariant. Its nonzero eigenvalues occur in opposite pairs. Write \(\lambda=\|\mathsf K\|>0\). If lambda=0, this space cannot implement a nonzero target, and the following attainable optimum is not asserted.

For **every** independently chosen pair,

\[
|\Theta|\le2\lambda\|f_1\|\|f_2\|
\le\lambda(\|f_1\|^2+\|f_2\|^2)=\lambda E.
\tag{1}
\]

A common pulse f1=f2=g, with g in the positive eigenvalue lambda eigenspace and scaled appropriately, attains the bound for positive Theta0. The negative target follows by changing one force sign or using the conjugate eigenfunction. Hence

\[
E_{\mathrm{nom}}(\Theta_0)=|\Theta_0|/\lambda.
\tag{2}
\]

This operator-norm optimization is ordinary quadratic-form linear algebra, closely related to the established power-eigenproblem in BG21. It is not claimed as a new general optimal-control technique. The role of the conjugation symmetry in preserving this minimum under angle stabilization is the additional argument.

### A finite real-basis version

For real basis forces \(r_a\), put

\[
G_{ab}=\int r_a r_b\,dt,\qquad
L_{ab}=\int (\mathsf A r_a)r_b\,dt.
\]

Endpoint closure gives L^T=-L. In an orthonormalized basis, K=-iL is an imaginary Hermitian matrix. The phase operator therefore distinguishes opposite loop orientations with equal cost. No complex control phase is a new dimension beyond the complex span already granted to both competitors.

## 4. A robust protocol attains the same lower bound

Apply the preserved pilot conversion to the nominal minimizing common pulse:

\[
f_1^{\rm sp}=\frac{g-g^*}{\sqrt2},\qquad
f_2^{\rm sp}=\frac{g+g^*}{\sqrt2}.
\tag{3}
\]

Both remain in V. The first is purely imaginary and the second real. At every time,

\[
|f_1^{\rm sp}|^2+|f_2^{\rm sp}|^2=2|g|^2.
\]

The nominal phase is unchanged. The exact pilot identity states

\[
\Theta_{\rm sp}[\delta]=\Theta_{\rm sp}[-\delta]
=\tfrac12(\Theta_{\rm com}[\delta]+\Theta_{\rm com}[-\delta]).
\tag{4}
\]

It holds for any real integrable detuning waveform in the specified Hamiltonian. No reversed-error experiment is performed. Equivalently, the nominal conditional trajectories are orthogonal quadrature paths, so their real overlap vanishes at every time. The first-order phase response to any real test waveform vanishes.

Define E_static as the infimum with the extra condition dTheta/ddelta=0 for constant detuning, and E_even with the stronger requirement (4) for all waveforms. The feasible-set inclusions and (1)–(4) give

\[
\boxed{E_{\mathrm{nom}}=E_{\mathrm{static}}=E_{\mathrm{even}}
=|\Theta_0|/\lambda.}
\tag{5}
\]

This is a matched-class optimum, not merely equal cost for two hand-picked pulses. The same conversion applies to finite bases, existing moment constraints, and smooth real waveform subspaces.

For any nonzero extremal eigenfunction, g and g* belong to opposite eigenspaces and are orthogonal. Thus integral g^2=0; the two split forces also have equal integrated costs, each equal to one of the original common forces. This does not imply equal instantaneous amplitudes or equal individual peak amplitudes.

### Phase protection versus full-gate protection

If V additionally imposes integral t f=0, then static-detuning residual displacements are O(delta^2). Equation (4) makes the angle error O(delta^2), so the average reduced two-qubit gate infidelity is O(delta^4) for a fixed thermal oscillator state. The comparison nominal optimum already has the same displacement stabilization but generally has an O(delta) angle error.

Without the first-moment condition, the equality (5) still protects the phase, but residual displacement can yield quadratic full-gate infidelity. Arbitrary-waveform phase evenness does not cancel arbitrary-waveform residual displacement. Higher even angle derivatives are not canceled by (4).

## 5. Exact four-tone solution with matched endpoint and displacement conditions

Take the full complex span of \(e^{in\nu t}\), n=±1,±2, and require

\[
f(0)=f(T)=0,\qquad \int_0^T t f(t)dt=0.
\]

The zeroth moment already vanishes for these nonzero harmonics. In the coefficient basis ordered as (1,2,-1,-2), the two independent constraints are sum c_n=0 and sum c_n/n=0. The resulting space has complex dimension two, with real orthonormal basis

\[
u(t)=\sqrt{\frac2{5T}}[\sin\nu t-2\sin2\nu t],
\qquad v(t)=\frac1{\sqrt T}[\cos\nu t-\cos2\nu t].
\]

Here the function u(t) should not be confused with the frequency nu. Define D by \(D_{ab}=\langle\mathsf A r_a,\mathsf A r_b\rangle\), with r=(u,v). Exact integration gives

\[
K=\frac{2}{\sqrt{10}\nu}
\begin{pmatrix}0&i\\-i&0\end{pmatrix},
\qquad
D=\frac1{\nu^2}\begin{pmatrix}2/5&0\\0&5/8\end{pmatrix}.
\tag{6}
\]

The angle and static derivative are \(2\operatorname{Re}F^\dagger K G\) and \(-2\operatorname{Re}F^\dagger D G\). Since \(\|K\|=T/(\pi\sqrt{10})\), (5) gives

\[
\boxed{E_{\min}=\pi\sqrt{10}|\Theta_0|/T.}
\tag{7}
\]

A unit common eigenvector is g=(i,1)^T/sqrt2. Its compiled pair is (i,0)^T and (0,1)^T, with the same scalar amplitude. Up to a simultaneous sign change of both forces, these are exactly the prior pilot's smooth pulse with B/A=sqrt(5/2). No new tone or pulse duration is added to obtain the quartic static error in this comparison.

This does **not** prove that the four-tone space has the lowest possible force cost among all imaginable waveform spaces. It proves the unrestricted and phase-robust optima within this explicitly fixed space, and equality (5) in any other space satisfying its hypotheses.

## 6. Applying the predecessor's fixed-first-pulse construction fairly

BG21 S16 starts with a nominal power-optimal pulse G, holds its direction fixed, and chooses the other pulse in the orthogonal complement of the derivative vectors. In a one-parameter setting this becomes projection away from DG; normalizations then match the gate and equalize pulse costs. Its source equations are real bilinear forms. A complex force basis can be represented by twice as many real coefficients, so that same algebraic prescription has an unambiguous application to (6).

This section is **our adapted benchmark**. The source's laboratory pulse functions and multimode example are not silently replaced with our effective model or counted as experimental comparison data.

For the normalized g above, let

\[
Q_g=I-\frac{|Dg\rangle\langle Dg|}{\|Dg\|^2},\qquad
\kappa=\|Q_g g\|=\frac9{\sqrt{1762}}.
\]

With one pulse direction fixed to g, the optimal allowed second direction is \(Q_g g/\kappa\). Because Kg=lambda g, the maximum phase efficiency in this restricted strategy is lambda kappa. Optimizing the two overall amplitudes gives equal integrated force on each qubit and

\[
\frac{E_{\rm fixed\ first}}{E_{\min}}
=\frac1\kappa=\frac{\sqrt{1762}}9
=4.664020413736748\ldots.
\tag{8}
\]

For T=2pi, Theta0=pi/4, with nu=1:

| Choice | Integrated force cost | Static angle derivative |
|---|---:|---:|
| Nominal common optimum | 1.241823533224513 | -0.636434560777563 |
| Globally minimizing split pair | 1.241823533224513 | 0 |
| Fixed-first-pulse projection, adapted as above | 5.791890309217822 | 0 |

All rows use the same four effective offsets, duration, independent addressing permission, endpoint conditions, and displacement moment constraints. The robust rows both have fourth-order small-static-error reduced gate infidelity. Their leading coefficients need not agree.

The factor 4.664 is not a universal superiority factor over published independently controlled gates. The source's full constraints permit the split pair; it is the choice to freeze a particular common optimum that incurs this penalty in our symmetric space. Joint optimization, or choosing an appropriate first quadrature at the outset, can attain (7). The source's experimental or multimode power claims have not been refuted.

## 7. Resource controls that prevent an overbroad conclusion

### 7.1 Per-qubit peaks are not preserved

For the prior smooth example at nu=1, the common forces each have maximum amplitude 0.4445698525. The split forces have maxima 0.5439284179 and 0.6287167148. These are evaluations of the explicit pulses, not hardware peak measurements. They have equal integrated per-qubit force but unequal peaks.

An even simpler exact control is a circular common force g(t)=exp(it). The compiled forces are i sqrt2 sin t and sqrt2 cos t. The pointwise total squared force remains two, but each maximum amplitude rises from one to sqrt2. Equation (5) therefore does not optimize with the same individual peak cap. It is not a peak-limited speed theorem.

### 7.2 A one-sided control space need not permit the conversion

On [0,2pi], let V_plus consist of complex multiples of

\[
f(t)=e^{it}-4e^{2it}+3e^{3it}.
\]

This waveform has zero endpoints, zero zeroth moment, and zero first moment. Its only effective offsets are positive. For independently scaled copies f1=c1 f, f2=c2 f, exact orthogonality of exponentials gives

\[
\Theta=48\pi\operatorname{Re}(c_1^*c_2),\qquad
\Theta'(0)=-24\pi\operatorname{Re}(c_1^*c_2)=-\Theta/2.
\]

A nonzero entangling phase cannot be first-order angle robust in this particular one-dimensional complex control space. The compiler adds reflected negative offsets, which are not permitted. This is not a no-go theorem for every higher-dimensional one-sided control space.

### 7.3 Spectator closure need not survive

The same f satisfies

\[
\int_0^{2\pi} f(t)e^{it}dt=0,
\qquad
\int_0^{2\pi} f(t)^*e^{it}dt=2\pi.
\]

Consequently, a spectator-mode closure condition at one offset need not survive conjugation unless the corresponding opposite-offset condition is also imposed. That is why a single-mode result cannot be directly compared to full-ion-chain closures. Adding mirror constraints changes the admitted space and its numerical minimum, even though (5) continues to hold if the resulting space is conjugation invariant.

### 7.4 Laboratory real forces and rotating-frame complex forces are not identical resources

BG21 uses real laboratory pulse functions multiplied by mode-dependent rotating phases. Those effective sets do not automatically satisfy conjugation invariance about one chosen mode. Hou et al. I24 documents how changing red/blue phase differences permits a motional phase change while keeping the qubit spin axis fixed, after the stated rotating-wave approximation. That establishes a relevant control type, not exact synthesis of our pulses in a specific apparatus or closure of its other modes.

Equal squared effective force is not enough to compare real optical power when actuator gains, Lamb–Dicke factors, nonlinear transfer functions, tone generation or per-channel limits differ. Both competitors must be evaluated under the same corresponding metric; no such hardware theorem is claimed here.

## 8. What remains additional after attribution

The 2006 qubus primitive already provides orthogonal-quadrature geometric gates. The phase-evenness proof applies to its finite-duration linear-force realization under our detuning model. BG21 already provides the nominal eigenproblem, the identical-pulse sensitivity obstruction, and separate-pulse angle-stabilization constraints. The present theorem combines the pilot's conversion with the nominal spectral bound; it does not introduce a new eigensolver, Magnus formula, or gate primitive.

The prospective contribution is the exact matched-class equality: **conjugation-symmetric independent controls contain an angle-robust optimum at the same integrated-force cost as the entire nominal class**. It specifies when an observed or algorithmic stabilization penalty is avoidable, and when missing control symmetry prevents the inference. The four-tone example is a complete analytic certificate, not a favorable result against an arbitrarily chosen baseline.

A short implication-level reconstruction matters: the theorem follows from a simple spectral bound plus the exact conversion. This may ultimately be judged a concise control-theory completion rather than a broadly significant new gate principle. The targeted sources inspected do not directly state this combined equality, but no exhaustive priority or implementation advantage is established. The broader BG21 feasible set can contain the optimum; the new point is the explicit certificate and control-symmetry condition, not an assertion that established independent optimization is incapable of finding it.

**Next allocation:** assess and consolidate the zero-added-integrated-force statement and its hypotheses. Do not expand to heating, stronger error orders or many-mode devices merely to keep this lead alive. The residual significance question is whether the exact resource equality, rather than another fidelity comparison, is independently consequential enough for the intended paper.

## 9. Verification

Five new check groups passed on their first complete run and on repetition. They verify the exact complete four-tone nullspace and matrices; the general construction in five real polynomial control spaces; the adapted projection benchmark; peak/spectral/spectator countercontrols; and the finite-error thermal channel and phase identity. The largest new projected matrix has complex dimension six. Random samples test the inequalities but do not prove optimality; the spectral bound above does.

The unchanged five-group pilot also passed and reproduced its canonical report byte-for-byte, including its 112-dimensional direct qubit–oscillator Schrödinger check. The new two reports are byte-identical to each other. All 18 incoming archive files and their integrity manifest remain unchanged. No scientific assertion or tolerance was adjusted, and no protected repository or old scientific project was accessed.

The web PDF text for BG21 and Q06 was readable; attempted PDF page screenshots failed. No figure ordinate or graph-derived performance number is used here. The 4.664 factor and all tabulated costs are our exact or directly computed matched-space results. The primary-source record describes the read boundaries.
