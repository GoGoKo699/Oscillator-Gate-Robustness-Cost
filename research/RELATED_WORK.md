# Related work and matched comparison

The question here is the **minimum additional integrated force required for
static-detuning robustness within a fixed control space**. Independent pulse
design, quadrature-mediated entanglement, displacement moments, and spectral
optimization all have established precedents. This comparison identifies the
optimization being solved rather than comparing fidelity numbers obtained
under different physical assumptions.

## The comparison being made

| Item | Fixed in the present result |
|---|---|
| Controls | Two independently chosen, error-independent complex forces in the same finite nominally closed space $V$ |
| Dynamics and error | One ideal linear oscillator with one unknown static number-detuning error $\delta a^\dagger a$ |
| Target | A prescribed nonzero unwrapped angle in $\exp(i\Theta_0Z_1Z_2)$ |
| Resource | $E=\int_0^T(\lvert f_1\rvert^2+\lvert f_2\rvert^2)dt$, with the same normalization and duration for both competitors |
| Robustness | Zero angle derivative; for quartic thermal average infidelity, also zero first displacement derivatives |
| Optimization | Joint minimization over both forces, including an explicit attaining pair and a matching lower bound |

With these choices, the result is an attainable cost classification:
$E_{\mathrm{angle}}=\frac{\lvert\Theta_0\rvert}{\min_{\zeta\in\mathbb R}\lVert K-\zeta D\rVert}$,
with zero extra angle cost exactly when the extreme eigenvalues of $K$ are
balanced. The [claims](CLAIMS.md) state feasibility conventions and the
full-gate corollary; the [spectral restriction](SPECTRAL_RESTRICTION.md) gives
a family whose matched cost ratio grows without bound. The
[sensitivity frontier](SENSITIVITY_FRONTIER.md) also gives the attained minimum
absolute angle slope at every feasible force budget, including budgets below
the robust threshold. These statements depend on the granted space and
output-force resource.

## Closest physical constructions

### Blümel et al.: independently stabilized pulses

R. Blümel et al., *Power-optimal, stabilized entangling gate between trapped-ion
qubits*, npj Quantum Information 7, 147 (2021),
[published article](https://doi.org/10.1038/s41534-021-00489-w),
[arXiv:1905.09292v2](https://arxiv.org/abs/1905.09292v2),
[combined PDF](https://arxiv.org/pdf/1905.09292v2).

Main-text Eqs. (3)–(6) minimize a common pulse's squared norm using a projected
phase eigenproblem and impose displacement derivatives as linear constraints.
Supplement S16, Eqs. (S82)–(S83), already gives a bilinear target and bilinear
angle-derivative constraints for two separately applied pulses, including
multiple modes and derivative orders. The ensuing recipe fixes one pulse to
the nominal power-optimal eigenpulse, projects the other into the sensitivity
constraint complement, equalizes their norms, and rescales to the target.
The main phase eigenproblem is on combined-PDF p. 2, the angle/displacement
distinction is on p. 7 around Eq. (9), and S16 is on p. 22.

The distinction here is joint optimization of both pulses for one positive
overlap constraint in a matched complex force space. The source's fixed-first
construction is a feasible-design predecessor; its broader multimode,
higher-order task is not solved by the present theorem. Its optical-control
normalization must be translated before comparing costs. The archive's
adapted fixed-first-pulse comparison is a calculation in this repository's
model, not an experimental ratio from the source.

### Jia et al.: cancellation between concatenated gates

Z. Jia et al., *Angle-robust two-qubit gates in a linear ion crystal* (2023),
[arXiv:2210.04814v1](https://arxiv.org/abs/2210.04814v1),
[PDF](https://arxiv.org/pdf/2210.04814v1).

Sections II–III, Eqs. (1), (6), (9)–(16), distinguish residual displacement
from angle error and impose robustness against correlated mode-frequency
drifts. The construction concatenates two displacement-robust multimode
pulses with opposite angle slopes. The two-ion frequency-reflection
construction assumes equal Lamb–Dicke parameters for its two modes; the
longer-chain construction solves Eq. (16) for two amplitude
scalings with a total target angle $\pi/4$. The drive on the two ions is common
within each pulse. The paper explicitly credits independently addressed
angle stabilization to Blümel et al.

Those passages establish angle stabilization and constructive cancellation.
Their pulse selection and amplitude rescaling do not constitute the present
joint integrated-force minimum over a prescribed one-mode space. Neither
their reported Rabi amplitudes nor their error measure in Eq. (6) is a
substitute for a matched resource or Haar-average channel comparison.

### Spiller et al.: orthogonal-quadrature bus gates

T. P. Spiller et al., *Quantum Computation by Communication* (2006),
[arXiv:quant-ph/0509202v3](https://arxiv.org/abs/quant-ph/0509202v3),
[PDF](https://arxiv.org/pdf/quant-ph/0509202v3).

Section IV, Eqs. (7)–(9), couples the qubits to orthogonal oscillator
quadratures. Four conditional displacements close the bus trajectory and
produce a two-qubit phase without measuring the bus. The phase is set by the
enclosed area. Orthogonal-quadrature entanglement and automatic bus
disentanglement are therefore inherited constructions.

The present result concerns continuous forces in a specified finite space,
static-detuning derivatives, and their exact integrated-force cost. The
conjugation construction provides a sufficient zero-penalty mechanism, while
balanced spectral extrema give the necessary and sufficient condition.
The displacement sequence alone supplies neither this matched optimization
nor a force normalization with which to compare its cost.

### Wu, Wang and Duan: the reduced thermal channel

Y. Wu, S.-T. Wang and L.-M. Duan, *Noise analysis for high-fidelity quantum
entangling gates in an anharmonic linear Paul trap* (2018),
[arXiv:1802.03640v2](https://arxiv.org/html/1802.03640v2), Sec. II B,
Eqs. (33)–(41), derives the reduced thermal channel, including displacement
overlap phases and thermal characteristic functions, and its average gate
fidelity. Their Eq. (41) is the fidelity expression used by Huo et al. below.
The source tracks additional Lamb–Dicke corrections; the present ideal
linear-oscillator model retains only the conditional-displacement dynamics.
The thermal channel and its fidelity normalization are established inputs to
the present cost calculation.

### Huo et al.: overlap identity and thermal fidelity

Z. Huo, Y. Shen, X. Yuan and X.-M. Zhang, *Scalable suppression of heating
errors in large trapped-ion quantum processors*,
[arXiv:2507.13457v2](https://arxiv.org/html/2507.13457v2) (1 September 2026).

Section III, Eqs. (4)–(9), optimizes a multimode heating-error surrogate using
independent pulse coefficients, a bilinear phase target, and linear closure
and displacement-derivative constraints. Its positive-extraction construction
links the two pulse vectors and minimizes a quadratic trajectory cost.

Appendix G, Eq. (89), already gives the leading thermal average-infidelity
coefficient as $4/5$ times the sum of thermal displacement-error squares and
angle-error square. Eq. (94) gives the displacement-moment relation, and
Eq. (104) identifies the angle slope with the integrated cross-trajectory
overlap. Laser-detuning and oscillator-number-detuning conventions have
opposite signs. These identities are antecedents of the present derivation,
not standalone novelty claims.

The distinction is the exact minimum output-force cost for
**vanishing** angle slope and the attained minimum slope at every feasible
budget. Heating-error minimization and exact sensitivity–cost optimization
are different tasks. The thermal factor in Eq. (89) is retained here.

## Other directly relevant control objectives

The following sources address neighboring optimization tasks with different
constraints, error models, or resource objectives.

| Source and passage | Objective and relation to this result |
|---|---|
| B. P. Ruzic et al., *Leveraging motional-mode balancing and simply parametrized waveforms to perform frequency-robust entangling gates*, Physical Review Applied 22, 014007 (2024); [published article](https://doi.org/10.1103/PhysRevApplied.22.014007), [preprint v1](https://arxiv.org/pdf/2210.02372v1), Sec. II A–D, Eqs. (1), (4), (6), (10)–(13) | Selects a detuning that cancels angle slopes between modes while Gaussian shaping suppresses displacement. The published title differs from the preprint title; section and equation references use v1. This multimode mechanism differs from the present one-mode independent-force optimum. |
| L. Ellert-Beck and W. Ge, *Power-optimized amplitude modulation for robust trapped-ion entangling gates: A study of gate-timing errors*, Physical Review A 111, 062422 (2025); [published article](https://doi.org/10.1103/PhysRevA.111.062422), [preprint v1](https://arxiv.org/pdf/2412.17789v1), Sec. III C–D, Eqs. (26)–(37), PDF pp. 6–7 | Projects a common real amplitude pulse onto linear timing-robustness constraints. Eq. (35) and the following projection/whitening optimize a phase-to-power Rayleigh quotient. The error and bilinear joint-pulse constraint differ here. |
| J.-B. Wang, *Robust quantum gate optimization with first-order derivatives of ion–phonon and ion–ion couplings in trapped ions* (2025); [society full text](https://www.cpsjournals.cn/en/article/doi/10.1088/1674-1056/adb40e), Secs. 3, 4.1–4.2, discussion of Eq. (18) | Uses numerical SLSQP optimization of a displacement/angle derivative-penalty objective with segmented amplitude/phase controls and a peak Rabi cap. Its stated optimization differs from the exact integrated-force minimum and attained sensitivity frontier here. |
| W. Zhang et al., *Robust Mølmer-Sørensen Gate Against Symmetric and Asymmetric Errors* (2025); [preprint v1](https://arxiv.org/pdf/2501.02847v1), Sec. II and Sec. III B–C, especially Eq. (13) | Treats symmetric detuning and asymmetric qubit/laser-frequency errors using displacement conditions and generator-based compensation. The latter introduces composite entangling and single-qubit operations outside this repository's fixed commuting-force model. |
| E. J. Páez, S. S. Vedaie and B. C. Sanders, *Closed-loop control for two-qubit gates with trapped ions* (2026); [preprint v1](https://arxiv.org/html/2607.00462v1), Sec. III.1 and III.3 | Uses a continuously monitored spectator ion and reinforcement-learning control in stochastic multimode dynamics. The controls respond to measurements, whereas the present theorem fixes error-independent open-loop forces. |

### Bentley et al.: independent complex controls

C. D. B. Bentley et al., *Numeric optimization for configurable, parallel,
error-robust entangling gates in large ion registers* (2020),
[arXiv:2005.00366v1](https://arxiv.org/pdf/2005.00366v1),
[published article](https://doi.org/10.1002/qute.202000044).

Sections II A–B, Eqs. (6)–(14), allow ion-specific complex amplitude and phase
controls. Section III A–B, Eqs. (15)–(28), develops pulse optimization and
robustness conditions: Eq. (20) minimizes squared phase-target and residual-
displacement errors; Eqs. (22)–(23) connect the displacement derivative to a
time moment; Eqs. (26)–(28) impose trajectory-center and symmetry constraints.
The discussion and caption of Fig. 4 vary a maximum Rabi-rate bound.

These are direct antecedents for independent controls and displacement
robustness, with an objective and resource constraint different from the
exact integrated-force minimum. The operational fidelity in Eq. (12) and
Supporting Information A, Eqs. (29)–(34), uses its own convention; comparison
with the Haar-average channel fidelity here requires an explicit conversion.

### Mostaan Ghalejough: spectral and tone-number optimization

M. R. Mostaan Ghalejough, *Design of Tone-Number-Efficient Robust Entangling
Gates in Trapped-Ion Systems*, MSc thesis, Simon Fraser University (2026),
[institutional PDF](https://theses.lib.sfu.ca/file/thesis/etd24536-mohammadrezamohammadreza-mostaan-mostaanghalejough-mo.pdf).

Printed pp. 18–20, Eqs. (2.41), (2.47)–(2.49), use the same pulse on both
ions and separate angle and motional errors. Before Eq. (2.49), periodic
power recalibration treats the angle as calibrated; the robustness constraint
concerns motional infidelity. Printed pp. 54–55, Eqs. (3.22)–(3.25), minimize
squared amplitudes subject to a target angle and truncated motional-infidelity
bound. The extended-null-space method selects low-infidelity eigendirections
and then optimizes a Rayleigh quotient. Printed pp. 63–64, Eq. (3.30) and
Algorithm 2, give SLSQP constructions with squared-amplitude or sparsity
objectives.

This is close spectral resource optimization precedent. Its calibrated-angle
and motional-error constraints differ from the uncalibrated static angle
derivative and exact joint force optimum here.

## Mathematical sources

### Equality S-lemma

Y. Xia, S. Wang and R.-L. Sheu, *S-Lemma with Equality and Its Applications*,
[arXiv:1403.2816v3](https://arxiv.org/pdf/1403.2816v3),
[published article](https://doi.org/10.1007/s10107-015-0907-0).

Page 3 gives statements (E1)–(E2) and Assumption 1, which requires the equality
constraint to take both signs. Section 3, p. 11, Theorem 3 and exceptional
case (17), supplies the equality S-lemma. Its exception requires a nonconstant
linear constraint with zero quadratic matrix, alongside additional conditions.
Here the realified form $h=x^\dagger Dx-y^\dagger Dy$ is a nonzero indefinite
quadratic form: $y=0$ and $x=0$ supply its two signs. The exceptional case
therefore does not apply. [Theory §4](THEORY.md#attribution-and-a-checkable-certificate)
gives the resulting block-matrix certificate and constructive attaining forces.

### Average gate fidelity

M. A. Nielsen, *A simple formula for the average gate fidelity of a quantum
dynamical operation*, Physics Letters A 303, 249–252 (2002),
[arXiv:quant-ph/0205035v2](https://arxiv.org/pdf/quant-ph/0205035v2).

Page 1, definitions (1)–(2) and Eq. (3), give
$F_{\mathrm{avg}}=(dF_e+1)/(d+1)$ for a trace-preserving channel in dimension
$d$. Nielsen attributes this relation to M., P., and R. Horodecki and supplies
a simplified proof. The two-qubit channel uses $d=4$, hence $(4F_e+1)/5$.
Wu and Huo above supply the physical thermal-channel and expansion precedents;
[Theory §6](THEORY.md#6-full-thermal-gate-error-and-its-exact-minimum) derives
their specialization and the cost consequence.

### Numerical-range convexity and support lines

J. H. Shapiro, *Notes on the Numerical Range*, 5 May 2017,
[author-hosted PDF](https://www.joelshapiro.org/Pubvit/Downloads/NumRangeNotes/numrange_notes.pdf).

Proposition 1.1(g), p. 2, gives finite-dimensional compactness; Proposition
2.8, pp. 7–8, treats direct sums; Theorem 6.1, pp. 16–17, states and proves
the classical Toeplitz–Hausdorff convexity theorem. Section 9, pp. 23–24,
relates support lines to extremal Hermitian eigenvalues.

The exact budget-dependent sensitivity frontier uses the classical
geometry of the block pair $\operatorname{diag}(K,-K)$ and
$\operatorname{diag}(D,-D)$, whose support function is $\|uK+vD\|$.
The [frontier proof](SENSITIVITY_FRONTIER.md) identifies the coherent
attainable set and handles nominal-budget endpoints and force construction.

## Physical controls and interpretation

- P. J. Lee et al., *Phase Control of Trapped Ion Quantum Gates*,
  [quant-ph/0505203v1](https://arxiv.org/pdf/quant-ph/0505203v1), Section 2.3,
  Eqs. (28)–(30), PDF pp. 13–14: separation of spin and force phases through
  the red/blue sideband phases.
- S. M. Clark et al., *Engineering the Quantum Scientific Computing Open User
  Testbed (QSCOUT): Design details and user guide*,
  [arXiv:2104.00759v1](https://arxiv.org/html/2104.00759v1), Section VI A
  and its phase-synchronization and gate-sequencer subsections (VI.1 in HTML):
  tone programming and finite digital limits.
- C. G. Yale et al., *Realization and Calibration of Continuously Parameterized
  Two-Qubit Gates on a Trapped-Ion Quantum Processor*,
  [arXiv:2504.06259v1](https://arxiv.org/html/2504.06259v1), Introduction,
  Section II, Eqs. (2)–(4) and (13): individually addressed multimode pulses
  and calibrated optical/RF response.

The result combines these ingredients to determine the exact cost of a
specified physical requirement. In the parity interpretation, angle
robustness equates integrated displacement-induced oscillator occupations;
pointwise quadrature balance is sufficient but stronger. The
[control-access analysis](CONTROL_ACCESS.md) explains why accessible conjugate
directions remove the angle penalty under output-force cost, and why their
attenuation alone does not justify excluding them.
