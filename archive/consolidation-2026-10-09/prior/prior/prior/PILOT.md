# Quadrature separation for an oscillator-mediated entangling gate

9 October 2026. Independent Merlin–Arthur research pilot.

## Decision and contribution boundary

**Retain one bounded control-comparison question, without opening a repository or claiming PRL-level originality.** In the declared one-mode linear-force model, a simple reassignment of a common pulse's two quadratures to separately controlled qubits preserves its nominal entangling gate, duration, and pointwise total squared force. It removes every odd contribution of an oscillator-detuning waveform to the entangling Magnus phase. It also preserves the common pulse's static-detuning displacement moment cancellations. A smooth example has fourth-order, rather than second-order, average gate infidelity in static detuning.

The added control is real: two independently addressable effective forces replace one common envelope. This is not a free improvement for a globally addressed device, an optimum over all independently addressed gates, or a comparison of total apparatus costs.

Orthogonal-quadrature conditional-displacement gates are established, including Spiller et al. [Q06]. Closed-loop thermal-insensitive gates, zero-average displacement trajectories, multitone robustness, phase modulation, and entangling-angle robustness also have direct predecessors [S18,M20,BG21,J23,B25]. Independently addressed angle stabilization and the obstruction for identical ion pulses are already explicitly treated by [BG21], Supplementary Sections S15–S17. The candidate remainder is the **equal-budget pulse conversion and exact detuning-response identity**, not invention of a quantum bus, geometric entanglement, or separate-quadrature control. In particular, the phase-evenness proof below applies to the old orthogonal-displacement primitive too when the same detuning model is imposed. That implication must not be withheld until manuscript preparation.

The next bounded task is a resource-matched comparison with the established two-pulse stabilization and independently controlled qubus constructions: translate the complex effective forces into permitted drive controls and determine whether the no-extra-force guarantee remains a useful distinction. Another favorable numerical example is not needed. The current result merits that comparison because it removes an unavoidable common-envelope phase error without extending the pulse, but its contribution size remains uncertain.

No protected project or repository was accessed or modified. Earlier uploaded source PDFs and earlier scientific checkers were not inputs to this calculation.

## 1. Model and error convention

Set hbar=1. One harmonic oscillator a mediates two qubits with fixed, commuting Pauli operators Z1,Z2:

\[
H_\delta(t)=\delta(t)a^\dagger a+
\sum_{j=1}^2 Z_j[f_j(t)a^\dagger+f_j(t)^*a]. \tag{1}
\]

The complex forces f_j are predetermined and do not depend on the unknown detuning error. The nominal oscillator frequency has been removed by a rotating frame, so delta=0 is the calibrated model. This is an exactly solvable effective linear-force Hamiltonian. A trapped-ion interpretation additionally needs the rotating-wave and Lamb–Dicke regimes and isolation of the relevant mode. Changes of the force strength with actual oscillator frequency, spectator modes, oscillator squeezing from a changing trap, heating, dissipation, and qubit noise are absent from (1), not automatically canceled.

The primary examples in [S18,M20,J23] use the same type of oscillator-mediated interaction. Independent motional phase and amplitude controls are meaningful in individually addressed implementations [I24], but that source is not an implementation of the pulse proposed here.

Resource accounting is by the duration T and

\[
\mathcal P(t)=|f_1(t)|^2+|f_2(t)|^2,
\qquad E_f=\int_0^T\mathcal P(t)dt. \tag{2}
\]

These are squared effective-force amplitudes. They need not equal the total optical power of two different devices. Per-qubit peak amplitude, bandwidth, number of physical tones, calibration channels, and addressing hardware are not required to match.

Initially the oscillator and qubits are uncorrelated. At nominal closure the oscillator state may be arbitrary. Detuning-error fidelity estimates below assume a fixed finite thermal occupation nbar; they are not uniform over arbitrarily hot initial states as the error tends to zero.

## 2. Exact dynamics and the relevant two errors

Let

\[
\phi(t)=\int_0^t\delta(s)ds,
\qquad \dot\beta_j(t)=-if_j(t)e^{i\phi(t)},\qquad\beta_j(0)=0.
\]

In the interaction picture of delta(t)n, the Magnus series terminates after its commutator term. Ignoring an overall phase,

\[
U_I(T)=e^{i\Theta Z_1Z_2}
D[Z_1\beta_1(T)+Z_2\beta_2(T)],
\]

where

\[
\Theta=\operatorname{Im}\int_0^T
[\beta_1^*\dot\beta_2+\beta_2^*\dot\beta_1]dt. \tag{3}
\]

The physical propagator also has the oscillator-only rotation exp[-i phi(T)n]. It does not change the reduced-qubit channel after tracing out the oscillator.

The displacements beta_j(T) determine residual spin–oscillator entanglement. Theta determines the two-qubit rotation angle. These are different errors. [J23] explicitly distinguishes and addresses both; [M20] gives the standard displacement/Magnus framework and emphasizes residual-mode decoupling. No new solvability or fidelity principle is claimed here.

## 3. A general pulse conversion

Let x,y be real, piecewise continuously differentiable on [0,T], with both coordinates zero at both endpoints. Write alpha=x+iy. Define two arrangements:

\[
\begin{array}{c|cc|cc}
&f_1&f_2&\beta_1(t;0)&\beta_2(t;0)\\\hline
\text{common}&(i\dot x-\dot y)/\sqrt2&(i\dot x-\dot y)/\sqrt2
&(x+iy)/\sqrt2&(x+iy)/\sqrt2\\
\text{split}&i\dot x&-\dot y&x&iy
\end{array} \tag{4}
\]

Every common complex envelope determines x,y by integration, so this is a conversion of a general closed common-force pulse, not only the example in Section 6.

Both arrangements have beta1(T)=beta2(T)=0, and

\[
\Theta_0=\int_0^T(x\dot y-y\dot x)dt. \tag{5}
\]

Thus both give exp(i Theta0 Z1Z2) times the oscillator identity, up to a global phase. They also satisfy, exactly at every time,

\[
|f_1|^2+|f_2|^2=\dot x^2+\dot y^2. \tag{6}
\]

The sum of the two forces' squared norms and the gate duration therefore do not increase. The split controls do require separate access to the two qubits' force quadratures. In terms of the original common force f, the two new forces are (f-f*)/sqrt(2) and (f+f*)/sqrt(2). Complex conjugation reflects its frequency components, so the conversion can require additional tone frequencies even while preserving the pointwise total squared norm. Equal tone count or an unchanged one-sided spectral restriction is not claimed.

### Same conditional energy, different geometric area

For computational signs z1,z2=+/-1, the split trajectory is

\[
\alpha_{z_1z_2}(t)=z_1x(t)+iz_2y(t),
\qquad |\alpha_{z_1z_2}(t)|^2=x(t)^2+y(t)^2. \tag{7}
\]

For an initial vacuum or centered thermal oscillator, all four conditional branches therefore have equal oscillator occupation at every nominal time, while their oriented areas depend on z1 z2. The spin phase can be generated by orientation without a difference of conditional mean oscillator energy.

This does not make the branches identical: an environment sensitive to the displacement can distinguish them. There is no decoherence-free-subspace or heating-immunity claim. For a nonzero coherent initial amplitude, the added cross terms in occupation need separate treatment; Eq. (7) refers to the spin-induced displacement.

## 4. Exact cancellation of the odd detuning phase

For arbitrary real delta(t), substitute (4) in (3). If

\[
A(u,t)=\dot x(u)\dot y(t)-\dot y(u)\dot x(t),
\quad B(u,t)=\dot x(u)\dot x(t)+\dot y(u)\dot y(t),
\]

then

\[
\Theta_{\rm split}[\delta]=
\int_0^Tdt\int_0^tdu\ A(u,t)\cos[\phi(t)-\phi(u)], \tag{8}
\]

\[
\Theta_{\rm common}[\delta]=
\int_0^Tdt\int_0^tdu\{A(u,t)\cos[\phi(t)-\phi(u)]
+B(u,t)\sin[\phi(t)-\phi(u)]\}. \tag{9}
\]

Therefore

\[
\boxed{\Theta_{\rm split}[\delta]=\Theta_{\rm split}[-\delta]
=\tfrac12\big(\Theta_{\rm common}[\delta]+\Theta_{\rm common}[-\delta]\big).} \tag{10}
\]

This is an exact functional identity, not an average over realizations of a random error. No second gate with reversed unknown error is physically run. If delta(t)=epsilon d(t) for a fixed integrable waveform, every odd Taylor coefficient of the split entangling phase vanishes.

**Only the entangling phase is protected in this arbitrary-waveform statement.** The final displacements can still be linear in epsilon. Full-gate fourth-order infidelity below uses additional moment conditions and a static error.

### A restricted obstruction for common-envelope single-mode gates

At nominal closure, first-order perturbation by epsilon d(t)n gives

\[
\left.\frac{d\Theta}{d\epsilon}\right|_0
=-2\int_0^T d(t)\operatorname{Re}[\alpha_1^*(t)\alpha_2(t)]dt. \tag{11}
\]

For example, derive this by conjugating n with the nominal controlled displacement; its Z1Z2 coefficient is twice the displayed real overlap. All nominal displacements vanish at T, so there is no endpoint displacement contribution to that first-order spin phase.

For the common arrangement in (4), a constant error gives

\[
\Theta_{\rm common}'(0)=-\int_0^T(x^2+y^2)dt. \tag{12}
\]

It is nonzero for every nontrivial common loop. More generally, fixed real coupling ratios alpha1=c1 alpha, alpha2=c2 alpha give -2 c1 c2 integral |alpha|^2. Optimizing the common envelope alone cannot set it to zero for a nonzero entangling gate.

This is not a no-go theorem for geometric gates generally. Separate controls, additional modes with differently signed coupling products, or noncommuting spin composite operations are outside the restriction. Existing angle-robust gates [J23] are not contradicted.

As an elementary fixed-force-budget bound for (4), Cauchy–Schwarz gives

\[
|\Theta_0|^2\le
\left(\int|\alpha|^2dt\right)
\left(\int|\dot\alpha|^2dt\right)
=|\Theta'_{\rm common}(0)|E_f.
\]

Thus at fixed nonzero target and finite E_f the quadratic error source cannot be made arbitrarily small by this common-envelope class. This is a corollary of (12), not a claim that the numerical example globally optimizes that class.

The identical-pulse obstruction is already identified in [BG21] and summarized in [J23]. Equations (11)–(12) are a transparent trajectory-level proof of that restriction, not a separate priority claim.

## 5. Static-detuning displacement cancellation survives the conversion

For constant detuning,

\[
\beta_j(T;\delta)=\sum_{r\ge0}\frac{(i\delta)^r}{r!}
\int_0^Tt^r\dot\alpha_j(t)dt. \tag{13}
\]

All moment weights t^r are real. If a common complex trajectory obeys the zero moments through some r, its real and imaginary parts obey them separately. Equation (4) therefore preserves every such static-detuning cancellation order.

In particular, zero endpoint displacement and

\[
\int_0^T x(t)dt=\int_0^T y(t)dt=0 \tag{14}
\]

imply beta_j(T;delta)=O(delta^2) for both arrangements. This zero-average-trajectory condition is established pulse-shaping methodology [M20,J23]; it is not newly attributed to the present pilot.

For the split arrangement, (10) additionally gives Theta-Theta0=O(delta^2). With a fixed thermal oscillator state, the reduced gate then has average infidelity O(delta^4). The common arrangement retains a nonzero linear angle error and hence quadratic average infidelity.

## 6. An explicit smooth example

Let nu=2pi/T and tau=nu t. Choose

\[
x(t)=A(\cos\tau-\cos2\tau),\qquad
y(t)=B(\sin\tau-\tfrac12\sin2\tau). \tag{15}
\]

The coordinates, their derivatives, and their time averages vanish as required. The nominal angle and squared-force integral are

\[
\Theta_0=4\pi AB,\qquad E_f=\pi\nu(5A^2+2B^2).
\]

Choose AB=1/16 to obtain Theta0=pi/4. Minimizing E_f **within this two-parameter ansatz**, not over all gates, gives B/A=sqrt(5/2). Numerically,

\[
A=0.19881768219176266,\qquad B=0.31435835742073387.
\]

Put epsilon=delta/nu. This is detuning in units of the inverse pulse duration, **not** the fractional drift of the physical trap frequency. Direct integration of (8) gives

\[
\Theta_{\rm split}=\frac\pi4+\frac{5\pi AB}{2}\epsilon^2+O(\epsilon^4),
\]

\[
\Theta_{\rm common}=\frac\pi4-
\frac\pi4(8A^2+5B^2)\epsilon+O(\epsilon^2). \tag{16}
\]

For the split interaction-picture displacements,

\[
\beta_1(T)=O(\epsilon^3),\qquad
\beta_2(T)=-i\frac{3\pi B}{2}\epsilon^2+O(\epsilon^3). \tag{17}
\]

The factor i in (17) matters for the channel, although not for the leading displacement norm. It was omitted in a descriptive string of the first report, not in the dynamics. The saved repair adds independent symbolic and symmetric-detuning checks of the complex coefficient; no dynamics or numerical tolerance was altered.

### Full thermal channel, not a Bell-state proxy

For a basis sign vector z, put b_z=z1 beta1+z2 beta2 and p_z=z1 z2. The corrected spin coherence factors relative to the target gate are

\[
C_{zz'}=\exp\{i(\Theta-\Theta_0)(p_z-p_{z'})
+i\operatorname{Im}(b_zb_{z'}^*)
-(\bar n+\tfrac12)|b_z-b_{z'}|^2\}. \tag{18}
\]

Tracing the controlled Weyl operators in the thermal state gives this exact map. It has unit diagonal, is completely positive, and is trace preserving. Its average two-qubit gate fidelity is

\[
F_{\rm avg}=\frac{4+\sum_{zz'}C_{zz'}}{20}, \tag{19}
\]

where the sum is real. This follows either from the entanglement fidelity or the trace of the diagonal dephasing superoperator; it is not a fidelity with one chosen output Bell state.

For the split pulse,

\[
1-F_{\rm avg}=\frac45\left[
\left(\frac{5\pi AB}{2}\right)^2+
(2\bar n+1)\left(\frac{3\pi B}{2}\right)^2\right]\epsilon^4
+o(\epsilon^4). \tag{20}
\]

For the common pulse the leading coefficient is

\[
1-F_{\rm avg}=\frac45
\left[\frac\pi4(8A^2+5B^2)\right]^2\epsilon^2+o(\epsilon^2). \tag{21}
\]

At nbar=5, these coefficients are 19.5042189716724 and 0.3240391601217, respectively. Both comparators have the same nominal gate and pointwise total squared force, and **both** already suppress first-order residual displacement.

| epsilon | Common average infidelity | Split average infidelity |
|---:|---:|---:|
| 0.005 | 8.0511101e-6 | 1.2190030e-8 |
| 0.010 | 3.2104565e-5 | 1.9503529e-7 |
| 0.020 | 1.2878287e-4 | 3.1202243e-6 |
| 0.050 | 8.6625693e-4 | 1.2177586e-4 |
| 0.100 | 4.4975201e-3 | 1.9388737e-3 |

These are the exact effective-model channel equations evaluated numerically, not a device simulation or comparison against the best published robust gate. At epsilon=.01 the improvement over the chosen common counterpart is about165-fold. It cannot be used as a general superiority factor over independently controlled alternatives.

## 7. Broken-hypothesis controls

1. For delta(t)=epsilon nu cos(nu t), (10) still holds, but the chosen pulse has residual displacement O(epsilon). At nbar=5, doubling epsilon from .002 to .004 multiplies the average infidelity by approximately four, not sixteen. Arbitrary-waveform phase evenness is not arbitrary-waveform full-gate protection.
2. Scaling both force amplitudes by 1+zeta scales the nominal phase by (1+zeta)^2. There is no force-amplitude-error cancellation.
3. Replacing y by B(1-cos tau) violates the zero-average condition. The split pulse still has even detuning phase, but its final displacement becomes linear in a static error.
4. Orthogonal conditional paths have the same occupation but are distinct oscillator states. Loss, heating, and dephasing processes are not proven harmless. The error model is delta(t)n only.
5. A real rapidly modulated trap can generate oscillator squeezing or change the coupling coefficients. Holding f_j fixed in (1) is a declared model assumption. The physical ramp study [B25] explicitly distinguishes these implementation conditions.

## 8. Implication-level predecessor comparison

**[Q06] is the closest primitive-level predecessor.** Section IV already assigns one qubit to one bus quadrature and the other to its conjugate quadrature, and uses four controlled displacements to form a measurement-free entangling loop. Accordingly, orthogonal addressing, branch-dependent loop orientation, and returning an arbitrary bus state are not new here. Applying (8) to its finite-duration ideal-force realization supplies the same phase-evenness property under the present number-detuning perturbation. The source does not need to have printed that perturbation for this implication to count in our assessment.

**[S18] supplies multitone robust gate shaping.** Its selected-mode drive uses a collective spin operator. Its main text distinguishes elimination of timing-error orders from reducing the leading normal-mode-frequency-error coefficient. Our quartic *frequency* result must not be confused with its quartic or higher *timing* result. Different fidelity conventions also need care.

**[M20] supplies phase modulation and trajectory-centering constraints.** Its Hamiltonian and Appendix C already give the linear-force Magnus structure. Its Appendix F explicitly separates residual displacement and the entangling angle, and derives a filter function for the former. Our comparison is not a criticism that those authors confused the two.

**[BG21] is a closer direct comparator.** Supplementary Sections S15–S17 distinguish the identical-pulse obstruction from two-pulse stabilization. Equations (S82)–(S83) use separate pulse vectors to satisfy both the gate and prescribed frequency-derivative constraints. Hence using different pulses to cancel angle drift is inherited. That construction does not, in the inspected formulas, state the present pointwise-force-preserving conversion. Its real laboratory pulse functions and multimode conditions also cannot be equated silently to the single-mode complex force budget of (2). No resource advantage over that method is established.

**[J23] explicitly solves entangling-angle drift as a control objective.** It starts with equal target-ion Rabi envelopes and constructs pulses with opposite angle sensitivities across the mode spectrum, including concatenation. We have not proved that our pulse is better than its optimized solutions at equal hardware or total physical power. A one-mode common-envelope obstruction cannot be exported to its multimode control set.

**[B25] is a current strong comparator**, using amplitude and motional-frequency ramping to realize robust geometric gates, including initially warm modes. Neither robust geometric entanglement nor avoiding exact ground-state preparation is an available novelty claim.

**[I24] documents separately addressed entangling controls** and distinct motional/spin phase variables. It supports the plausibility of independently setting force quadratures, not a complete implementation of (15), spectator-mode suppression, or an error budget.

The exact mapping (4), its pointwise force equality (6), response identity (10), and preservation of common-pulse moment cancellations are the remaining candidate synthesis. The inspected sections have not supplied an identical compiled-pulse claim. This is a targeted comparison, not exhaustive priority clearance. The fact that the result uses a known qubus primitive leaves a substantive risk that the contribution is a concise control reformulation rather than a new useful gate method.

**One bounded GO for the resource comparison, not for a new-gate claim:** compare the exact conversion with [BG21] and [Q06] under the same permitted effective and physical controls. Determine whether the compiler gives a distinct guarantee rather than assuming one from the small numerical table. Do not start a new experimental platform, more noise models, or a repository merely to keep this pilot going.

## 9. Verification record

Five final groups passed twice, with byte-identical JSON reports. They check:

- symbolic endpoint/moment conditions, phase coefficients, complex displacement coefficients, and the exact nominal force integral;
- phase evenness and common-even-part equality for static and time-dependent errors, and pointwise resource equality;
- the full thermal spin channel, its positivity, numerical refinement, and analytically predicted static-error powers;
- an independently assembled physical-frame Schrodinger equation on a112-dimensional Hilbert space (two qubits and28 oscillator levels), not merely another integration of the displacement equations;
- the three broken-hypothesis controls above.

The full-state calculation uses oscillator Fock inputs0 and3 and both common and split controls. Its largest reduced-density discrepancy is6.70e-13, with negligible population in the top three cutoff levels. A time-dependent-detuning control also agrees. This is a convergence diagnostic, not a rigorously certified oscillator truncation bound.

The first five-group version also passed twice. During the written derivation, a missing imaginary unit was found in its descriptive displacement coefficient. The original script/reports are preserved in development and evidence; the dynamics, phase result, and fidelity tables never used the incorrect string. The final version adds explicit checks and corrects that string. No numerical tolerance was relaxed. No prior project suite was imported or rerun.

The general result rests on (8)–(14), not on the finite examples. Full source-reading boundaries and primary links are in SOURCES.md. The package contains no third-party PDFs or protected-project material.
