# Primary-source record

Read on 9 October 2026. These are selected passages sufficient for the stated comparisons, not an exhaustive review of robust-gate literature. The uploaded papers associated with earlier projects were not scientific inputs.

## Q06 — established orthogonal-quadrature bus gate

T. P. Spiller, K. Nemoto, S. L. Braunstein, W. J. Munro, P. van Loock, G. J. Milburn, *Quantum Computation by Communication*, New Journal of Physics 8, 30 (2006).

Primary full-text PDF: https://arxiv.org/pdf/quant-ph/0509202
Retrieved marker: arXiv:quant-ph/0509202v3. Read the interaction definition and Section IV, especially Eqs. (7)–(9), plus the nearby interpretation and selected error discussion. The paper already couples the two qubits to orthogonal bus quadratures and constructs a measurement-free four-displacement entangling gate. We use equations and text, not values extracted from its circuit figures. We do not claim to have audited every implementation proposal in the article.

## S18 — multitone force shaping

Y. Shapira, R. Shaniv, T. Manovitz, N. Akerman, R. Ozeri, *Robust entanglement gates for trapped-ion qubits*, Physical Review Letters 121, 180502 (2018).

Primary full-text PDF: https://arxiv.org/pdf/1805.06806
Retrieved v1. Read the collective Hamiltonian, multitone construction, fidelity convention, and the timing/frequency-robustness distinction in the main text. Their eliminated timing-error orders must not be reported as eliminated oscillator-frequency-error orders. No figure data or experiment values are used in our performance table.

## M20 — phase modulation and displacement stabilization

A. R. Milne, C. L. Edmunds, C. Hempel, F. Roy, S. Mavadia, M. J. Biercuk, *Phase-modulated entangling gates robust to static and time-varying errors*, Physical Review Applied 13, 024022 (2020).

Primary full-text PDF: https://arxiv.org/pdf/1808.10462
Retrieved v3 (25 September2019). Read Section II, the zero-average trajectory condition, Appendix C's exact Magnus propagator, and Appendix F's stated restriction of its filter function to residual spin–motion coupling. Our moment-preservation argument uses a known stabilization condition. Experimental fidelity claims were not reanalyzed.

## BG21 — power-optimal pulses and independently addressed angle stabilization

R. Blümel, N. Grzesiak, N. Pisenti, K. Wright, Y. Nam, *Power-optimal, stabilized entangling gate between trapped-ion qubits*, npj Quantum Information 7,147 (2021).

Publisher: https://www.nature.com/articles/s41534-021-00489-w
Primary combined paper/supplement PDF: https://arxiv.org/pdf/1905.09292
Read main model and discussion of angle stabilization, Supplementary Sections S15–S17, especially Eqs. (S75), (S82), (S83) and the pulse-construction paragraphs. The paper explicitly treats both the same-pulse obstruction and its removal by separate ion pulses. Its pulse-power budget must be translated rather than presumed identical to our rotating-frame effective-force norm. No plotted numerical gains or scaling fits from its figures are used.

This source was followed directly from reference22 and the explicit discussion in J23; it is not represented as a future unread comparison.

## J23 — entangling-angle robustness

Z. Jia, S. Huang, M. Kang, K. Sun, R. F. Spivey, J. Kim, K. R. Brown, *Angle-robust Two-Qubit Gates in a Linear Ion Crystal*, Physical Review A107,032617 (2023).

Primary full-text PDF: https://arxiv.org/pdf/2210.04814
Retrieved v1. Read the introduction, same-Rabi-envelope model, separate displacement/angle derivative conditions, and Section III's opposite-sensitivity concatenation. The introduction explicitly credits BG21's separately addressed arbitrary-order angle stabilization. No comparison with a source's optimized experimental gate is claimed.

Screenshot attempts for pages1 and2 failed. Parsed equations were readable; no value or conclusion relying on those figures is used.

## I24 — separate addressing and motional/spin phases

Y.-H. Hou et al., *Individually addressed entangling gates in a two-dimensional ion crystal*, Nature Communications15,9710 (2024).

Primary publisher HTML: https://www.nature.com/articles/s41467-024-53405-z
Read the addressed-gate description and Methods subsection “Phase-modulated gate design,” including its separate motional-phase and spin-phase variables. This supports the existence of the control types, not that a given device realizes our particular simultaneous envelopes or closes its other modes. Its alternate-addressing implementation and multichannel details are not replaced with our model.

## B25 — recent ramped geometric gates

*Robust Two-Qubit Geometric Phase Gates using Amplitude and Frequency Ramping*, arXiv:2511.14364.

Primary full text: https://arxiv.org/html/2511.14364
Read the opening model/ramp mechanism and implementation qualifications concerning mode-frequency modulation. Some mathematical symbols are missing in rendered text; no equation was reconstructed from the missing symbols. Used only for the directly stated existence of amplitude/frequency-ramped robust gates and for the distinction between an effective frequency term and physical trap modulation.

The separate publisher landing page could not be opened in the final check, so the note does not rely on a claimed publisher version or on a precise publication date. The current primary preprint is an adequate comparator for the qualitative claim.

## Implication boundary

Inherited: oscillator-mediated geometric entanglement, returning the bus, orthogonal-quadrature control, moment-based closure robustness, common-pulse angle obstruction, and independent-pulse angle stabilization.

Derived here: the generic conversion at equal pointwise total squared effective force; exact even-part identity for arbitrary detuning waveforms; preservation of static-displacement moment cancellations; explicit smooth one-mode instance and its full-channel fidelity.

Unresolved: whether that conversion supplies an independently useful resource guarantee beyond existing control constructions once physical control spaces, spectral restrictions, and budgets are matched. No exhaustive priority or gate-optimality claim is made.
