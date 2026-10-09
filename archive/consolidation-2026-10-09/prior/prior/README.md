# Quadrature-gate resource comparison

Read `REVIEW.md` for the theorem, proof, exact four-tone optimum, resource-matched projection comparison, and limitations. `SOURCES.md` separates inherited ingredients from the derived conditional force-cost equality.

Run the new checks with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python check_review.py --output /tmp/quadrature-review-new.json
```

Run the unchanged previous pilot with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python prior/check_pilot.py --output /tmp/quadrature-pilot-new.json
```

Both scripts refuse to overwrite a report. New results must be written outside the preserved `prior/` tree. The local archive is not a repository initialization or a device implementation. Python dependencies are NumPy, SciPy and SymPy; exact versions used are in `RUN_RECORD.json`.
