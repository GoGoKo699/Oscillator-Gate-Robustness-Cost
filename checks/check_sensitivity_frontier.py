#!/usr/bin/env python3
"""Exact checks of the attainable frontier in research/SENSITIVITY_FRONTIER.md.

The two Fourier modes are an actual nominally closed force space. Their phase
and overlap matrices do not commute. The checks include a smooth support point,
a coherent witness at a nonsmooth support point, and both budget endpoints.
These targeted identities supplement the proof, not a numerical optimization
or a general solver. The report destination must be new and outside archive/.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
GROUP_IDS = (
    "force_geometry_and_fourier_forms",
    "noncommuting_smooth_frontier",
    "coherent_kink_and_robust_endpoint",
    "proportional_infeasibility_and_budget_padding",
)


def build_report() -> dict:
    import sympy as sp

    def equal(actual, expected, description):
        if actual == expected:
            return
        difference = actual - expected
        entries = list(difference) if isinstance(difference, sp.MatrixBase) else [difference]
        if not all(sp.simplify(entry) == 0 for entry in entries):
            raise AssertionError(description + ": " + str(difference))

    def positive(value, description):
        if sp.simplify(value).is_positive is not True:
            raise AssertionError(description + ": " + str(value))

    def group(identifier, identities, assumptions):
        return {"id": identifier, "status": "PASS", "assumptions": assumptions,
                "identities": {key: str(value) for key, value in identities.items()}}

    groups = []
    try:
        K = sp.diag(1, sp.Rational(1, 2))
        D = sp.Matrix([[2, sp.Rational(1, 2)], [sp.Rational(1, 2), sp.Rational(1, 2)]])
        time = sp.symbols("time", real=True)
        forces = [sp.exp(sp.I * n * time) / sp.sqrt(2 * sp.pi) for n in (1, 2)]
        primitives = [(sp.exp(sp.I * n * time) - 1) / (sp.I * n * sp.sqrt(2 * sp.pi))
                      for n in (1, 2)]
        force_gram = sp.Matrix(2, 2, lambda m, n: sp.simplify(sp.integrate(
            sp.conjugate(forces[m]) * forces[n], (time, 0, 2 * sp.pi))))
        primitive_form = sp.Matrix(2, 2, lambda m, n: sp.simplify(sp.integrate(
            sp.conjugate(forces[m]) * primitives[n], (time, 0, 2 * sp.pi))))
        overlap_form = sp.Matrix(2, 2, lambda m, n: sp.simplify(sp.integrate(
            sp.conjugate(primitives[m]) * primitives[n], (time, 0, 2 * sp.pi))))
        equal(force_gram, sp.eye(2), "Force metric from orthonormal Fourier modes")
        equal((primitive_form.conjugate().T - primitive_form) / (2 * sp.I), K,
              "Phase form from the normalized Fourier forces")
        equal(overlap_form, D, "Displacement form from integrated primitives")
        for primitive in primitives:
            equal(primitive.subs(time, 0), 0, "Initial primitive")
            equal(primitive.subs(time, 2 * sp.pi), 0, "Nominal closure")
        commutator = K * D - D * K
        equal(commutator, sp.Matrix([[0, sp.Rational(1, 4)], [-sp.Rational(1, 4), 0]]),
              "The physical forms do not commute")
        positive(D.det(), "Positive overlap determinant")
        positive(D[0, 0], "Positive overlap first principal minor")

        # Unrestricted complex components test coherent forces, not mixtures of
        # different gates. Both Hermitian forms transform by the same unitary.
        x = sp.Matrix(sp.symbols("x0:2", complex=True))
        y = sp.Matrix(sp.symbols("y0:2", complex=True))
        a, b = (x + y) / sp.sqrt(2), (x - y) / sp.sqrt(2)
        equal((a.conjugate().T * a + b.conjugate().T * b)[0],
              (x.conjugate().T * x + y.conjugate().T * y)[0], "Force norm preservation")
        for name, form in (("K", K), ("D", D)):
            equal((a.conjugate().T * form * b + b.conjugate().T * form * a)[0],
                  (x.conjugate().T * form * x - y.conjugate().T * form * y)[0],
                  name + " coherent force identity")
        groups.append(group(GROUP_IDS[0], {
            "primitive_form": primitive_form, "K": K, "D": D, "commutator": commutator,
            "coherent_forces": "a=(x+y)/sqrt(2), b=(x-y)/sqrt(2)",
        }, "T=2*pi; normalized modes exp(i*t), exp(2*i*t); angle robustness only"))

        z = sp.symbols("z", real=True)
        rho_positive_branch = (3 - 5 * z + sp.sqrt(13 * z**2 - 6 * z + 1)) / 4
        z_smooth = sp.sqrt(6) / (3 * sp.sqrt(6) + 1)
        budget = sp.Rational(5, 4)
        u = sp.Matrix([sp.sqrt(3), -sp.sqrt(2)]) / sp.sqrt(5)
        centered = K - z_smooth * D
        rho = sp.simplify((u.T * centered * u)[0])
        equal(u.T * u, sp.ones(1, 1), "Smooth witness unit norm")
        equal(centered * u, rho * u, "Smooth witness is a support eigenvector")
        positive(rho, "Positive active eigenvalue")
        positive(sp.trace(centered), "Positive trace makes the positive eigenvalue dominant")
        positive(2 * rho - sp.trace(centered), "Active eigenvalue is the larger one")
        equal(rho_positive_branch.subs(z, z_smooth), rho, "Exact support norm branch")
        a = b = sp.sqrt(budget / 2) * u
        equal((a.T * a + b.T * b)[0], budget, "Smooth witness budget")
        equal(2 * (a.T * K * b)[0], 1, "Smooth witness target")
        sensitivity = (7 - sp.sqrt(6)) / 4
        equal(2 * (a.T * D * b)[0], sensitivity, "Smooth witness sensitivity magnitude")
        equal((1 - budget * rho) / z_smooth, sensitivity, "Smooth primal/dual equality")
        positive(sensitivity, "Smooth sensitivity is positive")

        # At the minimum nominal budget the supporting dual parameter tends to
        # zero. Requiring a finite nonzero maximizer there would be incorrect.
        nominal_a = sp.Matrix([1 / sp.sqrt(2), 0])
        equal(2 * (nominal_a.T * K * nominal_a)[0], 1, "Nominal endpoint target")
        equal(2 * (nominal_a.T * D * nominal_a)[0], 2, "Nominal endpoint sensitivity")
        equal(sp.limit((1 - rho_positive_branch) / z, z, 0, dir="+"), 2,
              "Nominal endpoint dual supremum")
        old_bound = 5 * (8 - sp.sqrt(13)) / 24
        positive(sensitivity - old_bound, "The exact smooth frontier improves the former lower bound")
        groups.append(group(GROUP_IDS[1], {
            "budget": budget, "unit_vector": u, "support_z": z_smooth, "support_norm": rho,
            "sensitivity": sensitivity, "former_bound": old_bound,
            "nominal_budget": 1, "nominal_sensitivity": 2,
            "nominal_dual_limit": 2,
        }, "Target angle 1; B=5/4 or nominal endpoint B=1; K,D from the physical two-mode space"))

        z_star, r = sp.Rational(3, 5), sp.sqrt(13) / 10
        L = K - z_star * D
        equal(sp.trace(L), 0, "Centered trace")
        equal(L**2, r**2 * sp.eye(2), "Opposite centered eigenvalues")
        v_plus = sp.Matrix([-3, 2 + sp.sqrt(13)]) / sp.sqrt(26 + 4 * sp.sqrt(13))
        v_minus = sp.Matrix([-3, 2 - sp.sqrt(13)]) / sp.sqrt(26 - 4 * sp.sqrt(13))
        equal(v_plus.T * v_plus, sp.ones(1, 1), "Positive support vector normalization")
        equal(v_minus.T * v_minus, sp.ones(1, 1), "Negative support vector normalization")
        equal(v_plus.T * v_minus, sp.zeros(1, 1), "Support vectors orthogonal")
        equal(L * v_plus, r * v_plus, "Positive support eigenvector")
        equal(L * v_minus, -r * v_minus, "Negative support eigenvector")
        k_plus, k_minus = [sp.simplify((v.T * K * v)[0]) for v in (v_plus, v_minus)]
        d_plus, d_minus = [sp.simplify((v.T * D * v)[0]) for v in (v_plus, v_minus)]

        # Check the actual a,b forces at a nonsmooth support point. Distinct
        # x,y blocks produce one deterministic pair of forces, with cross terms
        # cancelling exactly as checked above; no classical mixture is used.
        kink_budget = sp.Integer(2)
        p = sp.Rational(5, 6) + sp.sqrt(13) / 39
        robust_p = sp.Rational(1, 2) + 6 * sp.sqrt(13) / 65
        witnesses = (("kink", kink_budget, p, (5 - sp.sqrt(13)) / 3),
                     ("robust", 1 / r, robust_p, sp.Integer(0)))
        for name, witness_budget, weight, expected_sensitivity in witnesses:
            positive(weight, name + " first coherent weight")
            positive(1 - weight, name + " second coherent weight")
            # Scalar invariants of x=sqrt(B*p)*v_plus and
            # y=sqrt(B*(1-p))*v_minus avoid a numerical eigensolver.
            equal(witness_budget * (weight + 1 - weight), witness_budget, name + " budget")
            equal(witness_budget * (weight * k_plus - (1 - weight) * k_minus), 1,
                  name + " target")
            equal(witness_budget * (weight * d_plus - (1 - weight) * d_minus),
                  expected_sensitivity, name + " sensitivity")
            equal((1 - witness_budget * r) / z_star, expected_sensitivity,
                  name + " primal/dual equality")
        positive((5 - sp.sqrt(13)) / 3, "Kink sensitivity is positive")
        equal(robust_p, d_minus / (d_plus + d_minus), "Robust overlap-cancellation weight")

        # A balanced phase matrix has a degenerate nominal support face. Its
        # overlap interval crosses zero, so the frontier already vanishes at
        # the nominal budget; a single extremal mode would miss this case.
        balanced_K, balanced_D = sp.diag(1, -1), sp.diag(1, 2)
        balanced_x = sp.Matrix([sp.sqrt(sp.Rational(2, 3)), 0])
        balanced_y = sp.Matrix([0, sp.sqrt(sp.Rational(1, 3))])
        equal((balanced_x.T * balanced_x + balanced_y.T * balanced_y)[0], 1,
              "Balanced nominal budget")
        equal((balanced_x.T * balanced_K * balanced_x - balanced_y.T * balanced_K * balanced_y)[0],
              1, "Balanced nominal target")
        equal((balanced_x.T * balanced_D * balanced_x - balanced_y.T * balanced_D * balanced_y)[0],
              0, "Balanced nominal zero sensitivity")
        groups.append(group(GROUP_IDS[2], {
            "support_z": z_star, "support_norm": r, "positive_vector": v_plus,
            "negative_vector": v_minus, "k_plus": k_plus, "k_minus": k_minus,
            "d_plus": d_plus, "d_minus": d_minus, "kink_budget": kink_budget,
            "kink_weight": p, "kink_sensitivity": (5 - sp.sqrt(13)) / 3,
            "robust_budget": 1 / r, "robust_weight": robust_p,
            "robust_sensitivity": 0,
            "balanced_K": balanced_K, "balanced_D": balanced_D,
            "balanced_nominal_budget": 1, "balanced_nominal_sensitivity": 0,
            "force_witness": "x=sqrt(B*p)*v_plus; y=sqrt(B*(1-p))*v_minus; a=(x+y)/sqrt(2); b=(x-y)/sqrt(2)",
        }, "Target angle 1; physical two-mode support-face witnesses, plus a balanced-matrix nominal endpoint"))

        c, target, scale = sp.symbols("c target scale", positive=True)
        proportional_D = sp.diag(1, 2)
        proportional_K = c * proportional_D
        baseline_a = baseline_b = sp.Matrix([0, sp.sqrt(target / (4 * c))])
        equal(2 * (baseline_a.T * proportional_K * baseline_b)[0], target,
              "Proportional nominal target")
        equal(2 * (baseline_a.T * proportional_D * baseline_b)[0], target / c,
              "Proportional sensitivity cannot be cancelled")
        equal(proportional_K - c * proportional_D, sp.zeros(2), "Zero robust efficiency")
        equal(target / c, (target - sp.Integer(0)) / c, "Proportional dual equality at z=c")
        padded_a, padded_b = scale * baseline_a, baseline_b / scale
        equal(2 * (padded_a.T * proportional_K * padded_b)[0], target,
              "Reciprocal scaling preserves target")
        equal(2 * (padded_a.T * proportional_D * padded_b)[0], target / c,
              "Reciprocal scaling preserves sensitivity")
        padded_cost = target * (scale**2 + scale**-2) / (4 * c)
        equal((padded_a.T * padded_a + padded_b.T * padded_b)[0], padded_cost,
              "Reciprocal scaling cost")
        equal(padded_cost.subs(scale, 1), target / (2 * c), "Minimum nominal cost")
        equal(sp.limit(padded_cost, scale, sp.oo), sp.oo, "Continuous padding reaches every larger budget")
        equal(2 * (padded_a.T * sp.zeros(2) * padded_b)[0], 0,
              "K=0 makes every nonzero target infeasible")
        groups.append(group(GROUP_IDS[3], {
            "D": proportional_D, "K": proportional_K,
            "nominal_budget": target / (2 * c), "sensitivity_all_feasible_budgets": target / c,
            "robust_efficiency": 0, "padding_cost": padded_cost,
            "padding_limit": sp.oo, "zero_K_angle": 0,
        }, "c>0, target>0, scale>0; proportional matrices test the robust-infeasible case"))
        return {"schema_version": 1, "suite": "sensitivity_frontier", "status": "PASS",
                "method": "exact_symbolic_algebra", "test_groups": len(groups), "groups": groups,
                "scope_document": "research/SENSITIVITY_FRONTIER.md"}
    except AssertionError as error:
        return {"schema_version": 1, "suite": "sensitivity_frontier", "status": "FAIL",
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
