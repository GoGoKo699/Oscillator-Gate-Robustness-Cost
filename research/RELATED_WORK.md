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
qubits* (2021), [arXiv:1905.09292v2](https://arxiv.org/abs/1905.09292v2),
[combined PDF](https://arxiv.org/pdf/1905.09292v2).

Main-text Eqs. (3)–(6) minimize a common pulse's squared norm using a projected
phase eigenproblem and impose displacement derivatives as linear constraints.
Supplement S16, Eqs. (S82)–(S83), already gives a bilinear target and bilinear
angle-derivative constraints for two separately applied pulses, including
multiple modes and derivative orders. The ensuing recipe fixes one pulse to
the nominal power-optimal eigenpulse, projects the other into the sensitivity
constraint complement, equalizes their norms, and rescales to the target.

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

The remaining distinction is the exact minimum output-force cost for
**vanishing** angle slope and the attained minimum slope at every feasible
budget. Heating-error minimization and exact sensitivity–cost optimization
are different tasks. The thermal factor in Eq. (89) is retained here.

## Other directly relevant control objectives

The following passages delimit nearby optimization tasks. They supplement the
primary-source anchors in [the source review](SOURCE_REVIEW.md).

| Source and inspected passage | Objective and relation to this result |
|---|---|
| B. P. Ruzic et al., *Leveraging motional-mode balancing and simply parametrized waveforms to perform frequency-robust entangling gates* (2024); [preprint v1](https://arxiv.org/pdf/2210.02372v1), Sec. II D, Eq. (13) | Selects a detuning that cancels angle slopes between modes while Gaussian shaping suppresses displacement. This is a multimode stabilization mechanism, not the present one-mode independent-force optimum. |
| L. Ellert-Beck and W. Ge, *Power-optimized amplitude modulation for robust trapped-ion entangling gates: a study of gate-timing errors* (2025); [preprint v1](https://arxiv.org/pdf/2412.17789v1), Sec. III C–D, Eqs. (26)–(37) | Projects a common amplitude pulse onto timing-robustness constraints and optimizes a phase-to-power Rayleigh quotient. Constrained spectral power optimization is established; the error and bilinear joint-pulse constraint differ here. |
| J.-B. Wang, *Robust quantum gate optimization with first-order derivatives of ion–phonon and ion–ion couplings in trapped ions* (2025); [society full text](https://www.cpsjournals.cn/en/article/doi/10.1088/1674-1056/adb40e), Secs. 3, 4.1–4.2, discussion of Eq. (18) | Uses numerical SLSQP optimization of a displacement/angle derivative-penalty objective with segmented amplitude/phase controls and a peak Rabi cap. Its stated optimization differs from the exact integrated-force minimum and attained sensitivity frontier here. |
| W. Zhang et al., *Robust Mølmer-Sørensen Gate Against Symmetric and Asymmetric Errors* (2025); [preprint v1](https://arxiv.org/pdf/2501.02847v1), Sec. II and Sec. III B–C, especially Eq. (13) | Treats symmetric detuning and asymmetric qubit/laser-frequency errors using displacement conditions and generator-based compensation. The latter introduces composite entangling and single-qubit operations outside this repository's fixed commuting-force model. |
| E. J. Páez, S. S. Vedaie and B. C. Sanders, *Closed-loop control for two-qubit gates with trapped ions* (2026); [preprint v1](https://arxiv.org/html/2607.00462v1), Sec. III.1 and III.3 | Uses a continuously monitored spectator ion and reinforcement-learning control in stochastic multimode dynamics. The controls respond to measurements, whereas the present theorem fixes error-independent open-loop forces. |

Bentley et al.'s ion-specific complex controls and numerical phase/displacement
objective, and Mostaan Ghalejough's 2026 tone-number and spectral resource
optimization, have separate passage-level comparisons in
[the source review](SOURCE_REVIEW.md). In particular, the thesis comparison
distinguishes calibrated angle error from uncalibrated static angle slope.

## Mathematical attribution and physical interpretation

The scalar matrix-norm minimization is a structured application of the
equality S-lemma of Xia, Wang and Sheu; the [source review](SOURCE_REVIEW.md)
checks the sign-changing quadratic hypothesis and excluded exceptional case.
The elementary constructive proof supplies attaining controls without
creating a new general optimization principle. The thermal-channel
calculation also uses the established average-fidelity relation, with the
Horodecki attribution recorded by Nielsen.

The exact budget-dependent sensitivity frontier uses the classical
Toeplitz–Hausdorff theorem and supporting-line geometry. Its
[proof and mathematical source](SENSITIVITY_FRONTIER.md) identify the coherent
attainable set and handle the nominal-budget endpoint separately. The
contribution is this physical specialization and attainment, rather than a
new convexity theorem.

The result combines these ingredients to determine the exact cost of a
specified physical requirement. In the parity interpretation, angle
robustness equates integrated displacement-induced oscillator occupations;
pointwise quadrature balance is sufficient but stronger. The
[control-access analysis](CONTROL_ACCESS.md) explains why accessible conjugate
directions remove the angle penalty under output-force cost, and why their
attenuation alone does not justify excluding them.

The sources and specific versions above support these bounded comparisons.
They do not provide a comprehensive priority determination. Numerical
performance from different noise models, control sets, durations, targets,
or optical-resource conventions is not used to claim superiority.

Source passages checked through 9 October 2026. The Wang comparison uses
the full-text discussion of its objective, controls, and numerical method;
no objective weights are transcribed from its unrendered display equations.
