# Quadrature-separated geometric-gate pilot

The model, exact pulse conversion, proof, resource accounting, and qualified research decision are in [PILOT.md](PILOT.md). Primary-source reading boundaries are in [SOURCES.md](SOURCES.md).

To repeat all five check groups without changing the recorded evidence:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  python check_pilot.py --output /tmp/quadrature_gate_new_report.json
```

An existing output path is rejected. Dependencies are NumPy, SciPy and SymPy. The versions used are recorded in `environment.json`; a lightweight specification is in `requirements.txt`.

The result is exact within a single-mode, linear, spin-dependent-force Hamiltonian. The numerical table is not a trapped-ion device simulation. Separate qubit controls are required. The source comparison credits prior orthogonal-quadrature gates and prior independent-pulse angle stabilization.

The initial scripts and reports are retained because one descriptive displacement coefficient omitted an imaginary unit. The actual dynamics and fidelity calculation were correct. The final checker fixes the description and verifies the complex coefficient independently. No numerical tolerance was relaxed.

No repository initialization or publication is part of this pilot.
