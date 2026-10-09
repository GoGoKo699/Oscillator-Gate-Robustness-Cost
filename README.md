# Oscillator-Gate-Robustness-Cost

**When does first-order detuning robustness cost extra force?** For two qubits
coupled through one ideal oscillator, this project gives the exact answer in a
prescribed finite control space: angle robustness can be free, strictly costly,
or infeasible. The optimum is attained by an explicit pair of independent
forces. The resource is integrated squared effective force, with a fixed
normalization and target angle.

For the phase matrix $K$ and positive displacement-overlap matrix $D$, let

$$
\lambda=\lVert K\rVert,\qquad
r=\min_{\zeta\in\mathbb R}\lVert K-\zeta D\rVert.
$$

The nominal and angle-robust minimum costs are
$E_{\mathrm{nom}}=|\Theta_0|/\lambda$ and
$E_{\mathrm{angle}}=|\Theta_0|/r$. Zero efficiency means the prescribed nonzero
target is infeasible. Balanced extreme eigenvalues of $K$ characterize zero
additional angle-robustness cost. The two preserved four-tone examples have
cost factors **1** and **5.213046…**, under their stated matched constraints.

For a fixed thermal oscillator, eliminating both displacement derivatives and
the angle derivative is necessary and sufficient for quartic small-detuning
average infidelity. Projecting onto the first-moment kernel gives the exact
minimum cost for that stronger task. It need not be free relative to the
unconstrained nominal gate.

## Read the result

| Question | Current account |
|---|---|
| What is proved, with which assumptions? | [Claims and physical meaning](research/CLAIMS.md) |
| Where are the complete derivations and constructions? | [Preserved theorem](archive/consolidation-2026-10-09/THEOREM.md) and [finite-space proof](archive/consolidation-2026-10-09/prior/THEOREM.md) |
| What did the focused proof review find? | [Proof review](research/PROOF_REVIEW.md) |
| Which ingredients are established? | [Source review](research/SOURCE_REVIEW.md) |
| How do I reproduce the evidence? | [Verification](REPRODUCIBILITY.md) |
| What is the current task and handoff? | [Workspace](WORKSPACE.md) and [work order](work_orders/CURRENT.md) |

The mathematical optimizer is a structured application of the equality
S-lemma. Independent-pulse stabilization, quadrature gates, and displacement
moments have prior literature. The candidate contribution is the exact
attainable cost classification in this physical control class. Neither a
general novelty claim nor an editorial acceptance forecast is established.

The result concerns a single-mode, static-error, integrated-force model. It
does not determine laboratory power, individual peak limits, or a finite-error
operating window. A preserved peak-cap obstruction makes this distinction
concrete.

## Run the evidence

Use Python 3.13 and the pinned dependencies:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/verify.py --output-dir /absolute/path/to/new-results
```

The output directory must be new and outside `archive/`. The verification
receipt separates infrastructure checks, all twenty scientific check groups,
archive integrity, and canonical report comparisons. A numerical report is
evidence for its stated checks, not a substitute for proof.

Strict mode also requires the old JSON reports to match byte-for-byte. The
recovered environment shows small floating-point differences despite passing
every scientific assertion. The explicitly labeled portability mode used by
CI is documented in [REPRODUCIBILITY.md](REPRODUCIBILITY.md); it reports these
differences and never relabels them as byte identity.

## Provenance

All 89 files from `quadrature_gate_consolidation_2026-10-09.zip` are preserved
under [the archive](archive/consolidation-2026-10-09/README.md), with a complete
[hash inventory](provenance/archive.json). Statements inside that archive about
publication or repository status describe its historical checkpoint.

The subsequent prepared initialization tree could not be recovered. This
repository reconstructs its wrapper around the intact scientific package and
records that limitation in [the recovery note](provenance/RECOVERY.md).
