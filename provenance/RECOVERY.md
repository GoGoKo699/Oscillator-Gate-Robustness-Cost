# Recovery record — 9 October 2026

The latest project-chat handoff reported a prepared initialization tree
`b2118a15e78202adbfea228ea2c21e4efe14324e` and a last verified main commit
`fa45fc26728865ff52dac1398158cca7aef26f9e`. It explicitly left remote commit,
pull request, merge, and hosted verification unconfirmed.

At takeover, GitHub main still pointed to that initial commit, which contained
only `LICENSE`; there were no other branches or pull requests. The recorded
tree did not resolve through the repository's Git tree API. The available
local checkouts did not contain it either. Its reported 112-file tree and
eight infrastructure tests cannot be certified or reproduced as that exact
unavailable artifact.

The scientific source package **was** recovered:
`quadrature_gate_consolidation_2026-10-09.zip`, 171,772 bytes, SHA-256
`7a19fd462dd28eb2a1b051f220e1de70d235b95fd96071a81b357b04b2759b6a`.
It contains 89 files. All files were extracted without content changes to
`archive/consolidation-2026-10-09/`, and every entry of its top-level manifest
was checked. The new [inventory](archive.json) also covers the manifest itself.

The current README, research pages, workspace instructions, and verification
infrastructure are reconstructed repository work. They are not asserted to
match the unavailable tree. Historical source versions, canonical evidence,
tolerances, nested manifests, and historical publication statements remain
unchanged in the archive.

The current user's authorization names this repository and permits both
modification and merge. It supersedes the archive's earlier historical note
that repository authorization had not yet been given.

Scientific scope follows `PROJECT_HANDOFF.md`: claims-first exposition and
focused proof/source review. No broader oscillator model or resource objective
was added. Current local and hosted verification must be read from the actual
run receipts and GitHub run records, not inferred from the prior chat's
reported local tests.
