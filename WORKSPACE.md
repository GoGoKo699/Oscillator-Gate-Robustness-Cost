# Workspace

Work only in
[`GoGoKo699/Oscillator-Gate-Robustness-Cost`](https://github.com/GoGoKo699/Oscillator-Gate-Robustness-Cost).
The user has authorized repository modification and merge. Follow
[the repository rules](AGENTS.md) and [current work order](work_orders/CURRENT.md).

## Scientific account

Start with [the claims](research/CLAIMS.md), then read the self-contained
[theory and proofs](research/THEORY.md). The exact jointly attained force cost
classifies static angle robustness in a prescribed finite space. The
[sensitivity frontier](research/SENSITIVITY_FRONTIER.md) determines the optimal
residual angle slope at every feasible budget. On the first-moment kernel,
it also determines the minimum quadratic thermal-infidelity coefficient.

The [spectral corollary](research/SPECTRAL_RESTRICTION.md) gives a positive-band
cost bound and a feasible four-tone family with unbounded overhead. The
[control-access account](research/CONTROL_ACCESS.md) derives the sideband
mapping and distinguishes missing directions from attenuation. Its QSCOUT
sources do not establish a hard one-sided force restriction.

Use [the matched comparison](research/RELATED_WORK.md) and
[source passages](research/SOURCE_REVIEW.md) for attribution. In particular,
the trajectory-overlap sensitivity and leading thermal fidelity expansion
have direct prior literature. The equality S-lemma and numerical-range
convexity are established mathematical ingredients. Keep the contribution
focused on the scoped jointly attained resource characterization.

## Verification and preservation

The immutable scientific archive contains 89 files anchored by
`provenance/archive.json`. Current exposition and new checks live outside it.
See [reproducibility](REPRODUCIBILITY.md) for pinned execution and receipt
interpretation. Review and verify the actual PR head, inspect hosted results,
merge with an expected-head guard, and separately verify merged main.
GitHub PR and Actions records carry exact-commit completion evidence.

The archived Fourier helper assumes distinct nonzero integer harmonics over
their common period. Every archived example meets that precondition; it is
not a validated API for arbitrary frequencies. Do not alter its preserved
source or historical tests to extend its use.
