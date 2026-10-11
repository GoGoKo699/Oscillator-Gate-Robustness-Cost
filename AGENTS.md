# Repository working rules

Work only in `GoGoKo699/Oscillator-Gate-Robustness-Cost`. The user has authorized
repository changes and merging; that authorization does not extend to other
repositories. Start with `README.md`, `research/CLAIMS.md`, and
`research/THEORY.md`. The tutorial bridge supplies the single-source learning
route; `research/RELATED_WORK.md` records attribution and exact source passages.
The frontier, spectral restriction, and control-access pages contain the
specialized results. `llms.txt` is the retrieval index for readers and assistants.

## Scientific scope

The model is one ideal linear oscillator, two independently controlled qubits,
one unknown static number-detuning error, and a prescribed finite nominally
closed complex force space. Cost means integrated squared effective force.
Keep the nonzero unwrapped target angle and force normalization fixed in all
comparisons. Distinguish nominal closure, displacement robustness, angle
robustness, and the stronger phase-evenness property.

Do not turn the scoped result into a device-power, heating, peak-constrained,
multimode, arbitrary-error, or finite-detuning optimality claim. Further model
extensions need a new scientific work order. Credit the equality S-lemma,
independent-pulse stabilization, quadrature gates, displacement moments, and
average-fidelity identity. A failed source lookup is not evidence of novelty.

## Reader-facing documentation

Present the complete scientific account with explicit hypotheses and source
attribution. Keep development chronology, review-status claims, abandoned
candidate narratives, and lists of unperformed work out of the reading path.
Maintain one canonical proof or source comparison and link to it from summaries.
Use the Blümel paper and supplement, arXiv:1905.09292v2, as one learning anchor.
For named operators in GitHub mathematics, use `\mathrm{...}`; the renderer
rejects `\operatorname`. Keep mathematical content unchanged in display fixes.
Use fenced `math` blocks for display equations and `$`-backtick delimiters for
inline mathematics so Markdown preserves matrix row breaks and norm bars.

## Preservation and verification

`checks/` contains the scientific implementations and `references/` contains
the four canonical numerical reports. `provenance/reference-integrity.json`
anchors all 11 files and records the original locations of the five migrated
implementations and four reference reports. Preserve their scientific assertions,
tolerances, and reference values. Never regenerate expected hashes or reference
reports to conceal a scientific change. Any intentional source change must have
an explicit reason, a reviewed diff, and verification evidence.

Run `python scripts/verify.py --output-dir /absolute/new/output-directory` in
the pinned environment. Read the receipt: passing scientific assertions,
canonical report identity, and source integrity are distinct facts. Record
environment differences instead of weakening assertions or replacing evidence.
Default verification is strict about reference bytes. The documented
`--allow-report-differences` mode may accept finite floating-point report
differences only after every scientific assertion, structure check, and source
integrity check passes; it must still report byte nonidentity explicitly.
Numerical checks are not analytical proofs or external peer review.

The Fourier helper assumes distinct nonzero integer harmonics over
their common period. Every checked example meets this precondition; the helper
does not validate arbitrary frequency inputs. Preserve its source and use only
the supported inputs documented in `REPRODUCIBILITY.md`.

Before merging, review and verify the actual PR head, inspect hosted results,
and use an expected-head guard. After merging, verify the merged main separately.
Do not claim a commit, hosted run, or merge succeeded without checking its result.
