# Focused primary-source review

Reviewed 9 October 2026 UTC (10 October in Asia/Shanghai). This review checks the
attribution in the preserved [theorem, Sections 7–8](../archive/consolidation-2026-10-09/THEOREM.md),
[review](../archive/consolidation-2026-10-09/REVIEW.md),
[reading record](../archive/consolidation-2026-10-09/prior/SOURCE_READINGS.md), and
[earlier comparison](../archive/consolidation-2026-10-09/prior/prior/SOURCES.md).
Those historical records remain unchanged. No third-party PDF is redistributed.

## Result and scope

The checked passages support the account's narrow attribution: the optimization
principle and physical pulse-design ingredients have established predecessors.
The candidate contribution remains the exact, attainable integrated-force cost
classification for the specified single-oscillator control class. This review
does not establish its novelty or priority, and does not transfer its numerical
cost factors to laboratory power or peak-amplitude constraints.

The previously reported Bentley and Mostaan Ghalejough full-text access gaps
are resolved for the targeted passages below. An access improvement is not a
priority certificate.

## Blümel et al.: independent-pulse stabilization

**Checked source:** R. Blümel et al., *Power-optimal, stabilized entangling gate
between trapped-ion qubits*, npj Quantum Information 7, 147 (2021).
[arXiv:1905.09292v2](https://arxiv.org/abs/1905.09292v2);
[combined PDF](https://arxiv.org/pdf/1905.09292);
[published article](https://doi.org/10.1038/s41534-021-00489-w).

**Passages read:** combined PDF p. 2, main-text Eqs. (3)–(4) and following
eigenproblem; p. 7, Eq. (9) and surrounding angle/displacement distinction;
p. 22, S16, Eqs. (S82)–(S83) and the construction immediately following them.
Page numbers here count the combined PDF from one.

S82 imposes a bilinear target angle for two separately applied pulses; S83
imposes bilinear sensitivity constraints indexed by mode and derivative order.
The explicit recipe fixes one pulse to the nominal power-optimal eigenpulse,
projects the other into the derivative-constraint complement, equalizes their
norms, and rescales to the target. Independent controls, these bilinear
constraints, and the nominal eigenproblem are therefore inherited ingredients.

**Implication and limit:** the repository's joint optimum specializes to one
positive overlap constraint in its own matched complex effective-force space.
It does not solve the source's general multimode, higher-order problem. The
adapted fixed-first-pulse ratio in the archive is a repository calculation,
not a measured source performance ratio. No plot values were extracted.

## Xia–Wang–Sheu: equality S-lemma

**Checked source:** Y. Xia, S. Wang and R.-L. Sheu, *S-Lemma with Equality and
Its Applications*.
[arXiv:1403.2816v3](https://arxiv.org/abs/1403.2816v3);
[PDF](https://arxiv.org/pdf/1403.2816);
[published article](https://doi.org/10.1007/s10107-015-0907-0).

**Passages read:** p. 3, statements (E1)–(E2) and Assumption 1; Section 3,
p. 11, Theorem 3 and exceptional case (17).

Assumption 1 requires the equality constraint to take both signs. Theorem 3's
exception requires a nonconstant linear constraint (zero quadratic matrix),
alongside additional conditions. It cannot apply to the repository's
nonzero indefinite quadratic constraint.

**Specialization, checked against the repository:** realify complex vectors
and set

$$
h=x^\dagger D x-y^\dagger D y,\qquad
f_\rho=\rho(\|x\|^2+\|y\|^2)-x^\dagger Kx+y^\dagger Ky.
$$

For a nonzero control space with $D>0$, taking $y=0$ or $x=0$ supplies
both signs of $h$. The multiplier certificate is

$$
\operatorname{diag}(\rho I-K+\zeta D,\rho I+K-\zeta D)\succeq0,
$$

equivalent to $\rho\geq\|K-\zeta D\|$. Thus the scalar norm formulation
is a structured application of established mathematics. The explicit
attaining controls are useful constructive exposition, not evidence of a new
general optimization theorem. Empty control spaces must be handled separately.

## Nielsen: average-fidelity normalization

**Checked source:** M. A. Nielsen, *A simple formula for the average gate
fidelity of a quantum dynamical operation*, Physics Letters A 303, 249–252 (2002).
[arXiv:quant-ph/0205035v2](https://arxiv.org/abs/quant-ph/0205035v2);
[PDF](https://arxiv.org/pdf/quant-ph/0205035).

**Passages read:** p. 1, definitions (1)–(2), Eq. (3), and preceding attribution.
For a trace-preserving channel on finite dimension $d$, Eq. (3) gives
$F_{\mathrm{avg}}=(dF_e+1)/(d+1)$. The nominal-relative two-qubit channel
therefore uses $d=4$, giving $(4F_e+1)/5$.

Nielsen explicitly attributes this relation to M., P., and R. Horodecki and
provides a simplified proof. “Nielsen, Eq. (3)” is an appropriate passage
citation; mathematical priority should not be assigned to Nielsen alone.
The repository's thermal-displacement expansion and its coefficient $4/5$
require the repository's own channel calculation as well as this identity.
Eq. (3) alone does not establish the robustness-cost theorem.

## Bentley et al.: previously unread comparison

**Checked source:** C. D. B. Bentley et al., *Numeric optimization for
configurable, parallel, error-robust entangling gates in large ion registers*.
[arXiv:2005.00366v1](https://arxiv.org/abs/2005.00366v1);
[PDF](https://arxiv.org/pdf/2005.00366);
[publication DOI](https://doi.org/10.1002/qute.202000044).

**Passages read:** Section II A–B, Eqs. (6)–(14); Section III A–B,
Eqs. (15)–(28); Section IV's discussion and caption of Fig. 4; Supporting
Information A's fidelity definition and factorization, Eqs. (29)–(34).

The paper already permits ion-specific complex amplitude/phase controls.
Eq. (20) minimizes squared phase-target and residual-displacement errors;
Eqs. (22)–(23) connect the detuning derivative of displacement to its time
moment. Eqs. (26)–(28) impose trajectory-center and symmetry constraints.
The Fig. 4 comparison varies a maximum Rabi-rate bound. These are relevant
antecedents, but their stated objective and resource constraint differ from
the repository's exact integrated-force minimum. Its Eq. (12) operational
fidelity definition should not be silently identified with the repository's
Haar-average channel fidelity.

**Reading limit:** the targeted body passages are now directly inspected;
the entire supplement and every possible implication were not exhaustively
audited. No plot values, numerical device comparisons, or absence-of-theorem
claim are used.

## Ellert-Beck and Ge: power-optimal timing robustness

**Checked source:** L. Ellert-Beck and W. Ge, *Power-optimized amplitude
modulation for robust trapped-ion entangling gates: A study of gate-timing
errors*, Physical Review A 111, 062422 (2025).
[Preprint](https://arxiv.org/abs/2412.17789);
[read PDF](https://arxiv.org/pdf/2412.17789);
[published article](https://doi.org/10.1103/PhysRevA.111.062422).
Passage references below are to the 14-page preprint v1.

**Passages read:** Sections III C–D, Eqs. (26)–(35), and the projection and
whitening immediately after Eq. (35), PDF pp. 6–7.
For a common real amplitude envelope and timing error, derivative conditions
become linear coefficient constraints. Eq. (35) maximizes a phase-to-power
Rayleigh quotient on their kernel, using whitening and an eigenproblem.
This is a direct predecessor for constrained spectral power optimization.
The repository instead imposes a bilinear static-angle-slope constraint on
two independently chosen complex forces. Different errors and control classes
preclude importing either cost factor into the other problem.

## Ruzic et al.: frequency robustness by mode balancing

**Checked source:** B. P. Ruzic et al., *Leveraging motional-mode balancing
and simply parametrized waveforms to perform frequency-robust entangling
gates*, Physical Review Applied 22, 014007 (2024).
[Preprint](https://arxiv.org/abs/2210.02372);
[read PDF](https://arxiv.org/pdf/2210.02372);
[published article](https://doi.org/10.1103/PhysRevApplied.22.014007).
The read ten-page preprint v1 has an earlier title; published metadata and
preprint passage numbering are distinguished here.

**Passages read:** Section II A–D, Eqs. (1), (4), (6), and (10)–(13).
The common amplitude envelope couples to multiple modes. Gaussian pulse
shaping suppresses residual displacement; choosing the detuning to balance
mode contributions cancels the entangling-angle derivative in Eq. (13).
Frequency-robust angle stabilization and its physical interpretation are
therefore established territory. This design uses cancellation between modes;
the repository's one-mode result uses independent forces and determines their
exact matched integrated-force minimum. No experimental-performance comparison
is drawn from the differing models or article versions.

## Mostaan Ghalejough: spectral and tone-number optimization

**Checked source:** M. R. Mostaan Ghalejough, *Design of Tone-Number-Efficient
Robust Entangling Gates in Trapped-Ion Systems*, MSc thesis, Simon Fraser
University (Summer 2026).
[Full institutional PDF](https://theses.lib.sfu.ca/file/thesis/etd24536-mohammadrezamohammadreza-mostaan-mostaanghalejough-mo.pdf).

**Passages read:** printed pp. 18–20, Eqs. (2.41), (2.47)–(2.49); pp. 54–55,
Eqs. (3.22)–(3.25); pp. 63–64, Eq. (3.30) and Algorithm 2.
The first passages use the same pulse on both ions and separate angle and
motional contributions. Before Eq. (2.49), the angle is treated as calibrated
through periodic power recalibration, and the robustness constraint concerns
motional infidelity. Eq. (3.22) minimizes squared amplitudes subject to a target angle
and truncated motional-infidelity bound. The extended-null-space method
selects low-infidelity eigendirections, then optimizes a Rayleigh quotient;
the later SLSQP construction uses squared-amplitude or sparsity objectives.

These passages establish close spectral resource optimization precedent.
Their stated constraints differ from the repository's uncalibrated static
angle derivative and exact joint optimum. The full thesis is now accessible;
this targeted comparison does not assert absence of overlap throughout it.

## Reading boundaries retained

The review was restricted to these seven attribution questions. The earlier
Spiller and Jia readings remain inherited records, not newly verified here.
No comprehensive citation search or assessment of all later literature was
performed. In particular, the new positive-band corollary is elementary once
the cost theorem is available; these readings establish neither its novelty
nor its absence from all prior work. The operative scientific comparison fixes the control space,
normalization, unwrapped target, error model, and resource before comparing
costs. Established quadrature gates, displacement moments, independent
addressing, and familiar spectral machinery must not become novelty claims.

The initial direct Blümel PDF and publisher opens failed in this session; the
arXiv abstract's PDF link subsequently returned the combined paper successfully.
The remaining primary PDFs were readable. Failed preliminary opens do not
override the later successful passage checks or support an absence claim.
