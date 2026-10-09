# Author assessment: contribution and PRL prospects

Assessment dated 9 October 2026 UTC. This is an internal scientific and
editorial judgment, not external peer review or an acceptance prediction.

## Present judgment

The scoped mathematics supports development of a focused theory paper.
There is not yet a strong basis for optimism about Physical Review Letters.
The unresolved issue is physical significance and distinctness from close
work, rather than an identified proof gap.

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

## Next scientific decision

Before presenting this as a PRL-ready result, establish one concrete physical
design consequence that follows from the classification and was unavailable
from the closest constructions. The most focused route is to identify a
credible reason for the asymmetric admissible spectrum and map it precisely
to the same effective-force model, normalization, and competitors. The
mapping must explain why adding the missing conjugate controls is unavailable
or changes the resource being compared.

This is a question to resolve, not an assumption already established. A
specialist's critique of overlap and significance would also be informative;
none has been requested or obtained here. Additional numerical sweeps alone
would not resolve the main objection. If the physical restriction cannot be
motivated, the appropriate conclusion is a narrower theory contribution,
without weakening the theorem or promising a particular journal outcome.
