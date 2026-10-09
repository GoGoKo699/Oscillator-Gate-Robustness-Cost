#!/usr/bin/env python3
"""Check exact symbolic identities for research/SPECTRAL_RESTRICTION.md.

This supplements, and never rewrites, the twenty archived scientific groups.
It checks identities for symbolic parameters rather than sampling a finite grid.
The report destination must be new and outside archive/.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
GROUP_IDS = ("positive_band_factors", "four_tone_exact_matrices", "matrix_pencil_asymptotics")


def build_report() -> dict:
    import sympy as sp

    def equal(actual, expected, description):
        difference = actual - expected
        if isinstance(difference, sp.MatrixBase):
            valid = all(sp.factor(value) == 0 for value in difference)
        else:
            valid = sp.simplify(difference) == 0
        if not valid:
            raise AssertionError(description + ": " + str(difference))

    def positive_polynomial(expression, variable, description):
        # Positive coefficients and positive variable give a strict certificate.
        if not all(coefficient.is_positive for coefficient in sp.Poly(expression, variable).all_coeffs()):
            raise AssertionError(description)

    def group(identifier, identities, assumptions):
        return {"id": identifier, "status": "PASS", "assumptions": assumptions,
                "identities": {key: str(value) for key, value in identities.items()}}

    groups = []
    try:
        a, b, omega = sp.symbols("a b omega", positive=True)
        q = (b - a) / (b + a)
        band_zeta = 2 * a * b / (a + b)
        k, d = 1 / omega, 1 / omega**2
        lower = 2 * b * (omega - a) / ((a + b) * omega**2)
        upper = 2 * a * (b - omega) / ((a + b) * omega**2)
        equal((k - band_zeta * d) + q * k, lower, "Lower band factor")
        equal(q * k - (k - band_zeta * d), upper, "Upper band factor")
        u, v = sp.symbols("u v", nonnegative=True)
        for factor in (lower, upper):
            nonnegative_form = factor.subs({omega: a + u, b: a + u + v}, simultaneous=True)
            if nonnegative_form.is_nonnegative is not True:
                raise AssertionError("Band factor is not certified nonnegative")
        equal(1 / q, (a + b) / (b - a), "Band cost lower bound")
        groups.append(group(GROUP_IDS[0], {
            "q": q, "zeta": band_zeta, "lower_nonnegative_factor": lower,
            "upper_nonnegative_factor": upper, "cost_ratio_lower_bound": 1 / q,
        }, "0 < a < b; a <= omega <= b; a nonzero first-moment-zero Fourier space"))

        N = sp.symbols("N", integer=True, positive=True)
        nu = sp.symbols("nu", positive=True)
        U = sp.Matrix([[1, 0], [-2, 1], [1, -2], [0, 1]])
        frequencies = [N + offset for offset in range(4)]
        n = sp.diag(*frequencies)
        coefficients = n * U
        endpoint = sp.ones(1, 4) * coefficients
        first_moment = (sp.Matrix([[1 / frequency for frequency in frequencies]]) * coefficients).applyfunc(sp.factor)
        equal(endpoint, sp.zeros(1, 2), "Endpoint constraint")
        equal(first_moment, sp.zeros(1, 2), "First-moment constraint")
        if U.rank() != 2:
            raise AssertionError("The admissible coefficient basis must have rank two")

        G = sp.expand(U.T * n**2 * U)
        K0 = sp.expand(U.T * n * U)
        D0 = U.T * U
        M = sp.Matrix([[6, -4], [-4, 6]])
        J = sp.Matrix([[6, -6], [-6, 12]])
        L = sp.Matrix([[8, -10], [-10, 26]])
        equal(G, N**2 * M + 2 * N * J + L, "Force Gram matrix")
        equal(K0, N * M + J, "Phase matrix")
        equal(D0, M, "Displacement matrix")
        for name, matrix in (("G", G), ("K0", K0), ("D0", D0)):
            positive_polynomial(matrix[0, 0], N, name + " first principal minor")
            positive_polynomial(sp.expand(matrix.det()), N, name + " determinant")

        P = 5 * N**4 + 30 * N**3 + 67 * N**2 + 66 * N + 27
        zeta = (2 * N + 3) * (5 * N**2 + 15 * N + 11) / (10 * N**2 + 30 * N + 31)
        r_squared = 9 * (25 * N**4 + 150 * N**3 + 335 * N**2 + 330 * N + 139) / (
            (10 * N**2 + 30 * N + 31)**2 * P)
        phase_operator = G.inv() * K0
        centered_operator = G.inv() * (K0 - zeta * D0)
        # These coordinate operators are similar to Hermitian whitened matrices.
        # Use their trace, determinant, and spectrum, never their Euclidean norm.
        equal(sp.trace(centered_operator), 0, "Centered generalized trace")
        equal(centered_operator**2, r_squared * sp.eye(2), "Centered eigenvalues are plus/minus r")
        equal(-centered_operator.det(), r_squared, "Centered determinant")
        equal(sp.trace(G.inv() * (K0 / nu - nu * zeta * D0 / nu**2)), 0,
              "Physical centering parameter is nu*zeta")
        numerator, denominator = sp.fraction(r_squared)
        positive_polynomial(sp.expand(numerator), N, "Strict robust feasibility numerator")
        positive_polynomial(sp.expand(denominator), N, "Strict robust feasibility denominator")

        trace = (2 * N + 3) * (5 * N**2 + 15 * N + 11) / P
        discriminant = (45 * N**4 + 270 * N**3 + 547 * N**2 + 426 * N + 117) / P**2
        equal(sp.trace(phase_operator), trace, "Nominal generalized trace")
        equal(sp.trace(phase_operator)**2 - 4 * phase_operator.det(), discriminant,
              "Nominal characteristic discriminant")
        nominal_lambda = (trace + sp.sqrt(discriminant)) / 2
        equal(zeta.subs(N, 1), sp.Rational(155, 71), "Archived N=1 centering parameter")
        equal(r_squared.subs(N, 1), sp.Rational(190905, 4615**2), "Archived N=1 squared efficiency")
        groups.append(group(GROUP_IDS[1], {
            "U": U, "G": G, "K0": K0, "D0": D0,
            "endpoint_row": endpoint, "first_moment_row": first_moment,
            "zeta_dimensionless": zeta, "zeta_physical": nu * zeta,
            "r_squared_dimensionless": r_squared, "lambda_dimensionless": nominal_lambda,
            "physical_K_form": K0 / nu, "physical_D_form": D0 / nu**2,
            "zeta_at_N1": zeta.subs(N, 1), "r_at_N1": sp.sqrt(190905) / 4615,
        }, "N is a positive integer; nu > 0; n=N,...,N+3; c=diag(n)*U*z; force metric G"))

        x = sp.symbols("x", real=True)
        pencil = sp.factor((J - x * M).det())
        equal(pencil, 4 * (5 * x**2 - 15 * x + 9), "Limiting generalized pencil")
        pencil_roots = (sp.Rational(3, 2) - 3 / (2 * sp.sqrt(5)),
                        sp.Rational(3, 2) + 3 / (2 * sp.sqrt(5)))
        for root in pencil_roots:
            equal(pencil.subs(x, root), 0, "Limiting pencil root")
        radius = sp.simplify((pencil_roots[1] - pencil_roots[0]) / 2)
        equal(sp.limit(N * nominal_lambda, N, sp.oo), 1, "Nominal efficiency leading constant")
        equal(sp.limit(N**4 * r_squared, N, sp.oo), radius**2, "Robust squared efficiency leading constant")
        equal(sp.limit(N**2 * sp.sqrt(r_squared), N, sp.oo), radius, "Positive robust efficiency constant")
        ratio_constant = sp.limit(nominal_lambda / (N * sp.sqrt(r_squared)), N, sp.oo)
        equal(ratio_constant, 2 * sp.sqrt(5) / 3, "Cost ratio growth constant")
        equal(sp.limit(zeta - N, N, sp.oo), sp.Rational(3, 2), "Limiting pencil center")
        groups.append(group(GROUP_IDS[2], {
            "M": M, "J": J, "L": L, "det_J_minus_xM": pencil,
            "pencil_eigenvalues": pencil_roots, "lim_N_lambda": sp.Integer(1),
            "lim_N2_r": radius, "lim_ratio_over_N": ratio_constant,
            "lim_zeta_minus_N": sp.Rational(3, 2),
        }, "N tends to positive infinity; efficiencies use the G metric; ratio is independent of nu"))
        return {"schema_version": 1, "suite": "spectral_cost", "status": "PASS",
                "method": "exact_symbolic_algebra", "test_groups": len(groups), "groups": groups,
                "scope_document": "research/SPECTRAL_RESTRICTION.md"}
    except AssertionError as error:
        return {"schema_version": 1, "suite": "spectral_cost", "status": "FAIL",
                "method": "exact_symbolic_algebra", "test_groups": len(groups),
                "groups": groups, "error": str(error)}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    requested = args.output.expanduser()
    if requested.is_symlink() or requested.exists():
        parser.error("Output file must not already exist")
    output = requested.resolve()
    protected = (ROOT / "archive").resolve()
    if output == protected or protected in output.parents:
        parser.error("Output file must lie outside archive/")
    report = build_report()
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as stream:
        json.dump(report, stream, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps({"suite": report["suite"], "status": report["status"],
                      "test_groups": report["test_groups"], "method": report["method"]}, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
