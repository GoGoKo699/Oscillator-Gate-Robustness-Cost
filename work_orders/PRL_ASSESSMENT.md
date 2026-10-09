# Author assessment: contribution and PRL prospects

Assessment dated 9 October 2026 UTC. This is an internal scientific and
editorial judgment, not external peer review or an acceptance prediction.

## Present judgment

The scoped mathematics supports development of a focused theory paper.
There is not yet a strong basis for optimism about Physical Review Letters.
The unresolved issue is physical significance and distinctness from close
work, rather than an identified proof gap. The completed QSCOUT audit does
not strengthen the PRL case: it does not establish the one-sided effective-force
restriction needed for the proposed hardware interpretation.

[PRL's stated criteria](https://journals.aps.org/prl/authors) emphasize a
substantial advance, innovation, and interest beyond a narrow specialty.
An exact result in a restricted model may meet that standard, but exactness
alone does not demonstrate it.

## Strongest case

The exact attainable cost separates a limitation of the allowed controls
from inefficiency of a chosen pulse construction. Angle robustness means
equal integrated displacement-induced oscillator occupation in the two
parity sectors, which gives the matrix constraint a physical interpretation.

The [spectral corollary](../research/SPECTRAL_RESTRICTION.md) sharpens this
picture: conjugation symmetry permits free angle robustness, whereas a
narrow positive band forces overhead at least $(a+b)/(b-a)$. A four-tone
family gives feasible, unbounded overhead with the same asymptotic growth
order. This is a more general physical consequence than the original single
cost factor. The thermal result connects the constraint to the leading
observable gate-infidelity coefficient.

## Strongest objections

The equality S-lemma, independent-pulse stabilization, quadrature gates,
moment constraints, and spectral power optimization are established
ingredients. The [primary-source comparison](../research/SOURCE_REVIEW.md)
includes close power-optimal and angle-robust constructions; simply combining
familiar tools or changing an error parameter is not a sufficient novelty
argument. The positive-band bound is itself an elementary consequence of
the cost theorem, not a new optimization method.

Many natural ideal spaces are conjugation invariant: the complex span of
real pulse shapes, unrestricted complex time-bin controls, and symmetric
Fourier sets. The zero-angle-penalty result therefore covers a broad natural
class. Positive-frequency restrictions are legitimate mathematical control
classes, but their physical necessity or usefulness must be justified for
the significance claim to be persuasive. The unbounded family also has a
growing nominal cost and an increasing frequency offset. It is not evidence
of a fixed-cost laboratory advantage.

The model treats one ideal oscillator and integrated squared effective
force. Its strong conclusions should remain in that model. Multimode,
peak-resource, heating, or finite-error claims cannot be supplied by wording
changes or by extrapolating the present bound.

## Decision after the physical-control audit

The [control-access analysis](../research/CONTROL_ACCESS.md) supplies a
fixed-spin sideband mapping and an exact distinction between missing and
attenuated directions. With unrestricted inputs and the present output-force
cost, nonzero gains on independently commanded conjugate directions give the
same conjugate-completed space. Its added angle-robustness cost is zero.
Input-power penalties or amplitude caps would define a different problem.

The checked QSCOUT sources describe programmable tones and a selected
multimode protocol; they do not establish the hard one-sided space. They also
do not certify exact mirrored pulses within all hardware limits. The conclusion
is specific: this candidate fails to supply the proposed physical justification.
It is neither a universal impossibility result nor a claim that robustness is
free on the complete device.

The finite-regime step is not supported because the required restriction has
not been established. No numerical operating window is assigned. The original
classification, positive-band bound, and four-tone asymptotics remain valid
inside their prescribed spaces.

Prioritize a focused theory manuscript built around the exact attainable cost,
parity-occupation interpretation, and free-versus-costly control-space examples.
Further pursuit of the hardware-asymmetry route should await an independently
motivated restriction with an honest force-resource mapping. Additional sweeps
or an unrequested noise/resource extension would not resolve the present
objection. No outside specialist assessment has been obtained, and this bounded
source audit neither determines priority nor predicts an editorial decision.
