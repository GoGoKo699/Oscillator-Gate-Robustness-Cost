#!/usr/bin/env python3
"""Independent checks of the scoped gate-cost theorem and operational interpretation.

No previous scientific module is imported. Finite checks do not constitute an
external proof audit. All outputs are append-only by filename.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import unittest
sys.dont_write_bytecode = True
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

T = 2 * np.pi
TARGET = np.pi / 4
Z = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]], float)
PARITY = Z[:, 0] * Z[:, 1]
REPORT: dict = {}


def centered_pair(K: np.ndarray, D: np.ndarray):
    """Bisection implementation independent of the preserved Brent solver."""
    K, D = np.asarray(K, complex), np.asarray(D, complex)
    if K.shape != D.shape or K.ndim != 2 or K.shape[0] != K.shape[1]:
        raise ValueError('Matching square matrices required')
    dmin = np.linalg.eigvalsh(D)[0]
    if dmin <= 0:
        raise ValueError('Strictly positive D required')
    lam = np.linalg.norm(K, 2)
    if lam == 0:
        raise ValueError('No nominal entangling phase')
    lo, hi = -2 * lam / dmin, 2 * lam / dmin
    for _ in range(85):
        mid = (lo + hi) / 2
        ev = np.linalg.eigvalsh(K - mid * D)
        if ev[0] + ev[-1] > 0:
            lo = mid
        else:
            hi = mid
    zeta = (lo + hi) / 2
    ev, vectors = np.linalg.eigh(K - zeta * D)
    radius = (ev[-1] - ev[0]) / 2
    if radius < 1e-11 * lam:
        raise ArithmeticError('Near-zero efficiency needs an exact feasibility decision')
    up, um = vectors[:, -1], vectors[:, 0]
    dp = np.vdot(up, D @ up).real
    dm = np.vdot(um, D @ um).real
    x = np.sqrt(dm / (dp + dm)) * up
    y = np.sqrt(dp / (dp + dm)) * um
    return zeta, radius, (x + y) / np.sqrt(2), (x - y) / np.sqrt(2)


def fourier_forms(modes):
    n = np.asarray(modes, float)
    return np.diag(1 / n), np.diag(1 / n**2) + np.outer(1 / n, 1 / n)


def response(modes, c1, c2, detuning):
    modes = np.asarray(modes, float)
    coeff = np.vstack((c1, c2))
    def rhs(t, y):
        dot = -1j * (coeff @ np.exp(1j * modes * t)) / np.sqrt(T)
        dot *= np.exp(1j * detuning * t)
        phase_dot = (y[0].conjugate() * dot[1] + y[1].conjugate() * dot[0]).imag
        return np.array([dot[0], dot[1], phase_dot], complex)
    sol = solve_ivp(rhs, (0, T), np.zeros(3, complex), method='DOP853',
                    rtol=2e-12, atol=2e-14)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y[:2, -1], float(sol.y[2, -1].real)


def infidelity(beta, phase_error, nbar):
    displacement = Z @ beta
    diff = displacement[:, None] - displacement[None, :]
    weyl = (displacement[:, None] * displacement.conj()[None, :]).imag
    phase = phase_error * (PARITY[:, None] - PARITY[None, :]) + weyl
    exponent = -(nbar + .5) * abs(diff)**2 + 1j * phase
    # Sum of 1-Re(channel entry), divided by d(d+1)=20. Avoid 1-F subtraction.
    return float(-np.expm1(exponent).real.sum() / 20)


def symmetric_examples():
    modes = np.array([1, 2, -1, -2])
    C = np.column_stack((np.array([-1j, 2j, 1j, -2j]) / np.sqrt(10),
                         np.array([.5, -.5, .5, -.5])))
    k = 2 / np.sqrt(10)
    scale = np.sqrt(TARGET / (2 * k))
    common = C @ np.array([1j, 1]) / np.sqrt(2) * scale
    return modes, C, (common, common), (C @ np.array([1j, 0]) * scale,
                                       C @ np.array([0, 1]) * scale)


class Checks(unittest.TestCase):
    def test_01_first_order_joint_error_operator(self):
        modes = np.array([1, 2, -1])
        c1 = np.array([.12+.08j, -.05+.03j, .09-.07j])
        c2 = np.array([-.04+.06j, .11-.02j, .04+.10j])
        coeff = Z @ np.vstack((c1, c2))
        K, D = fourier_forms(modes)
        cut, inputs = 20, 3
        levels = np.arange(cut)
        lower = np.diag(np.sqrt(np.arange(1, cut)), 1).astype(complex)
        num = np.diag(levels)
        initial = np.zeros((2, 4, cut, inputs), complex)
        initial[0, :, :inputs, :] = np.eye(inputs)[None, :, :]
        roots = np.sqrt(np.arange(1, cut))[None, :, None]
        def action(psi, force):
            result = np.zeros_like(psi)
            result[:, 1:, :] += force[:, None, None] * roots * psi[:, :-1, :]
            result[:, :-1, :] += force.conj()[:, None, None] * roots * psi[:, 1:, :]
            return result
        def rhs(t, y):
            psi, tangent = y.reshape(2, 4, cut, inputs)
            force = (coeff @ np.exp(1j * modes * t)) / np.sqrt(T)
            return np.stack((-1j * action(psi, force),
                             -1j * action(tangent, force) - 1j * levels[None, :, None] * psi)).ravel()
        sol = solve_ivp(rhs, (0, T), initial.ravel(), t_eval=np.linspace(0, T, 401),
                        method='DOP853', rtol=2e-12, atol=2e-14)
        self.assertTrue(sol.success)
        state, tangent = sol.y[:, -1].reshape(2, 4, cut, inputs)
        errors, nominal_errors, integrals = [], [], []
        for j, cz in enumerate(coeff):
            nominal_phase = np.vdot(cz, K @ cz).real
            m = np.sqrt(T) * np.sum(cz / modes)
            q = np.vdot(cz, D @ cz).real
            Gz = T * num + m * lower.conj().T + m.conjugate() * lower + q * np.eye(cut)
            expected = -1j * np.exp(1j * nominal_phase) * Gz[:, :inputs]
            errors.append(float(np.linalg.norm(tangent[j] - expected)))
            nominal_errors.append(float(np.linalg.norm(state[j] - np.exp(1j * nominal_phase) * np.eye(cut)[:, :inputs])))
            integrals.append(float(q))
        self.assertLess(max(errors),2e-9)
        self.assertLess(max(nominal_errors),2e-11)
        occupation = sol.y.reshape(2,4,cut,inputs,-1)[0]
        tail = float(np.max(np.sum(abs(occupation[:,-2:,:,:])**2,axis=1)))
        self.assertLess(tail,1e-18)
        slope = -2*np.vdot(c1,D@c2).real
        self.assertAlmostEqual(-(integrals[0]-integrals[1])/2,slope,places=13)
        REPORT['joint_error_operator'] = {'max_tangent_vector_error':max(errors),
            'max_nominal_return_error':max(nominal_errors),'cutoff':cut,'full_qubit_oscillator_dimension':4*cut,
            'initial_oscillator_numbers':[0,1,2],'largest_top_two_level_probability':tail,
            'integrated_branch_displaced_occupation':integrals,'phase_slope':float(slope),
            'scope':'Finite-core check of the first derivative; not a uniform operator-norm truncation certificate.'}

    def test_02_spectral_optimum_and_certificate(self):
        rng=np.random.default_rng(910262); records=[]
        for d in (2,3,5):
            for rep in range(3):
                X=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
                Y=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
                K=(X+X.conj().T)/2;D=Y.conj().T@Y+np.eye(d)
                zeta,r,a,b=centered_pair(K,D)
                energy=np.vdot(a,a).real+np.vdot(b,b).real
                phase=2*np.vdot(a,K@b).real
                slope=-2*np.vdot(a,D@b).real
                L=K-zeta*D
                certificate_min=min(np.linalg.eigvalsh(r*np.eye(d)-L)[0],np.linalg.eigvalsh(r*np.eye(d)+L)[0])
                self.assertAlmostEqual(energy,1,places=13)
                self.assertLess(abs(slope),2e-12)
                self.assertLess(abs(phase-r),2e-12)
                self.assertGreater(certificate_min,-2e-12)
                for _ in range(10):
                    ca=rng.normal(size=d)+1j*rng.normal(size=d)
                    cb=rng.normal(size=d)+1j*rng.normal(size=d)
                    E=np.vdot(ca,ca).real+np.vdot(cb,cb).real
                    ph=2*np.vdot(ca,K@cb).real;sl=-2*np.vdot(ca,D@cb).real
                    self.assertLessEqual(abs(ph),r*E+abs(zeta)*abs(sl)+2e-10)
                records.append({'dimension':d,'radius':float(r),'zeta':float(zeta),
                                'slope_residual':float(abs(slope)),'certificate_min_eigenvalue':float(certificate_min)})
        # Degenerate opposite extremes: the construction does not assume simplicity.
        K=np.diag([-2.,-2.,2.,2.]);D=np.array([[2,.1,0,.2],[.1,1,0,0],[0,0,3,.1],[.2,0,.1,4.]])
        z,r,a,b=centered_pair(K,D)
        self.assertLess(abs(z),1e-14);self.assertAlmostEqual(r,2,places=13)
        # Exact proportional obstruction and exact one-sided scalar certificate.
        p,q,z=sp.symbols('p q z',real=True)
        D0=sp.Matrix([[2,sp.Rational(1,3)],[sp.Rational(1,3),1]])
        self.assertEqual(sp.simplify((sp.Rational(7,3)*D0-sp.Rational(7,3)*D0)),sp.zeros(2))
        G=sp.Matrix([[26,13],[13,14]])
        K0=sp.Matrix([[12,7],[7,sp.Rational(13,2)]])
        D0=sp.Matrix([[6,4],[4,sp.Rational(7,2)]])
        zstar=sp.Rational(155,71);r2=sp.Rational(190905,4615**2)
        P=G.inv()*(K0-zstar*D0)
        self.assertEqual(sp.trace(P),0)
        self.assertEqual(sp.simplify(P*P-r2*sp.eye(2)),sp.zeros(2))
        REPORT['certificate']={'random_diagnostics':records,'max_projected_matrix':5,
            'one_sided_exact_pencil_square':str(r2),'degenerate_extremes':'PASS',
            'proof_role':'Positive-semidefinite upper witness plus explicitly feasible attaining pair. Numerical residuals are diagnostics, not interval enclosures.'}

    def test_03_full_channel_quadratic_coefficient(self):
        # Exact combinatorics for averaging a diagonal two-qubit channel.
        self.assertEqual(int(np.sum((PARITY[:,None]-PARITY[None,:])**2)),32)
        for j in (0,1):self.assertEqual(int(np.sum((Z[:,j,None]-Z[None,:,j])**2)),32)
        cases=[]
        modes,C,common,robust=symmetric_examples()
        cases.extend([('moment_common',modes,*common),('moment_robust',modes,*robust)])
        # Pure quadratures with nominal closure but without first-moment cancellation.
        s=np.sqrt(TARGET)
        cases.append(('phase_only',np.array([1,-1]),np.array([.5,-.5])*s,np.array([.5,.5])*s))
        cases.append(('generic',np.array([1,2,-1]),np.array([.12+.08j,-.05+.03j,.09-.07j]),
                      np.array([-.04+.06j,.11-.02j,.04+.1j])))
        rows=[]
        for label,n,c1,c2 in cases:
            K,D=fourier_forms(n)
            theta0=2*np.vdot(c1,K@c2).real
            slope=-2*np.vdot(c1,D@c2).real
            m=np.sqrt(T)*np.array([np.sum(c1/n),np.sum(c2/n)])
            nbar=2.3
            predicted=.8*(slope*slope+(2*nbar+1)*np.vdot(m,m).real)
            values=[]
            for h in (.002,.001):
                losses=[]
                for delta in (-h,h):
                    beta,theta=response(n,c1,c2,delta)
                    losses.append(infidelity(beta,theta-theta0,nbar))
                values.append(float(sum(losses)/(2*h*h)))
            self.assertLess(abs(values[-1]-predicted),2e-4*(1+predicted))
            if predicted>1e-8:
                self.assertLess(abs(values[-1]-predicted),abs(values[0]-predicted)+2e-9)
            if label=='moment_robust':
                self.assertLess(predicted,1e-27)
                self.assertTrue(3.9<values[0]/values[1]<4.1)
            if label=='phase_only':
                self.assertLess(abs(slope),1e-14);self.assertGreater(predicted,1.)
            rows.append({'case':label,'theta0':float(theta0),'slope':float(slope),
                         'sum_squared_displacement_derivatives':float(np.vdot(m,m).real),
                         'predicted_quadratic_infidelity':float(predicted),
                         'symmetrized_error_over_delta_squared':values})
        REPORT['full_gate_error']={'thermal_occupation':2.3,'cases':rows,
            'identity':'lim (1-Favg)/delta^2 = 4/5 [Theta_prime^2+(2*nbar+1) sum_j |int alpha_j|^2]',
            'scope':'Fixed pulse and fixed thermal occupation; not a uniform bound for arbitrary energy oscillator states.'}

    def test_04_nonzero_sensitivity_cost_floor(self):
        lam=31/78+np.sqrt(1405)/390;r=np.sqrt(190905)/4615;zeta=155/71
        Enom=TARGET/lam;Erob=TARGET/r
        rows=[]
        for E in (Enom,.5*Erob,.75*Erob,.9*Erob):
            lower=max(0.,TARGET-r*E)/abs(zeta)
            rows.append({'energy_cap':float(E),'fraction_of_robust_minimum':float(E/Erob),
                         'absolute_phase_slope_lower_bound':float(lower),
                         'quadratic_infidelity_coefficient_lower_bound':float(.8*lower*lower)})
        # Physical one-sided pulses, not arbitrary Hermitian matrices alone.
        C=np.array([[1,1],[-4,-3],[3,0],[0,2]],complex);n=np.arange(1,5)
        K,D=fourier_forms(n);rawK=C.conj().T@K@C;rawD=C.conj().T@D@C
        rng=np.random.default_rng(6292);matched=0;worst_slack=np.inf
        for _ in range(200):
            a=rng.normal(size=2)+1j*rng.normal(size=2)
            b=rng.normal(size=2)+1j*rng.normal(size=2)
            ph=2*np.vdot(a,rawK@b).real
            if abs(ph)<1e-10:continue
            a*=np.sqrt(TARGET/abs(ph));b*=np.sqrt(TARGET/abs(ph))*np.sign(ph)
            c1=C@a;c2=C@b
            E=np.vdot(c1,c1).real+np.vdot(c2,c2).real
            slope=-2*np.vdot(a,rawD@b).real
            bound=max(0.,TARGET-r*E)/abs(zeta)
            self.assertGreaterEqual(abs(slope)+1e-11,bound)
            self.assertLess(abs(np.sum(c1/n))+abs(np.sum(c2/n)),1e-12)
            worst_slack=min(worst_slack,abs(slope)-bound)
            if E<Erob:matched+=1
        self.assertGreater(matched,1)
        # Resource/model control: force-amplitude error cannot be canceled this way.
        z=sp.symbols('z');theta=sp.symbols('theta',real=True)
        self.assertEqual(sp.diff((1+z)**2*theta,z).subs(z,0),2*theta)
        REPORT['cost_floor']={'nominal_minimum':float(Enom),'robust_minimum':float(Erob),'bounds':rows,
             'physical_below_threshold_controls':matched,'minimum_observed_slope_bound_slack':float(worst_slack),
             'warning':'Bounds, not an exact finite-tolerance Pareto frontier. Amplitude-error derivative remains 2*Theta0.'}


    def test_05_project_displacement_constraints_before_cost(self):
        records=[]
        for modes in (np.array([1,2,-1,-2]),np.arange(1,5)):
            # Start with all four tones, then impose exactly the two physical
            # endpoint/first-moment constraints by an independent SVD.
            constraints=np.vstack((np.ones(4),1/modes))
            _,sv,Vh=np.linalg.svd(constraints)
            C=Vh.conj().T[:,2:]
            self.assertLess(np.linalg.norm(constraints@C),1e-14)
            Kf,Df=fourier_forms(modes)
            K=C.conj().T@Kf@C;D=C.conj().T@Df@C
            zeta,r,a,b=centered_pair(K,D)
            c1=C@a;c2=C@b
            self.assertLess(abs(np.sum(c1/modes))+abs(np.sum(c2/modes)),1e-14)
            self.assertLess(abs(2*np.vdot(c1,Df@c2).real),1e-13)
            self.assertAlmostEqual(2*np.vdot(c1,Kf@c2).real,r,places=13)
            expected=2/np.sqrt(10) if np.any(modes<0) else np.sqrt(190905)/4615
            self.assertAlmostEqual(r,expected,places=13)
            # This block form is the precise homogeneous S-lemma reconstruction.
            d=len(K);M=np.block([[K,np.zeros_like(K)],[np.zeros_like(K),-K]])
            H=np.block([[D,np.zeros_like(D)],[np.zeros_like(D),-D]])
            certificate=r*np.eye(2*d)-M+zeta*H
            self.assertGreater(np.linalg.eigvalsh(certificate)[0],-2e-13)
            records.append({'effective_offsets':modes.tolist(),'projected_dimension':int(C.shape[1]),
                'singular_values_of_constraints':sv.tolist(),'robust_efficiency':float(r),
                'dual_block_min_eigenvalue':float(np.linalg.eigvalsh(certificate)[0])})
        REPORT['full_gate_projection']={'cases':records,
            'scope':'No new control space: reconstructs both existing four-tone examples by projection before scalar optimization.',
            'mathematical_attribution':'The displayed homogeneous block problem is a direct specialization of the equality S-lemma; the gate dictionary is derived here.'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    if args.output.exists():p.error('Refusing to overwrite evidence')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',test_groups=result.testsRun,
                  previous_modules_imported=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=='__main__':main()
