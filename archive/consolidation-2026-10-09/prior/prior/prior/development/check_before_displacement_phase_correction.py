#!/usr/bin/env python3
"""Reproducible checks for the independent-quadrature geometric-gate pilot.

This is a one-mode linear spin-dependent-force model, not a device simulation.
No previous project code is imported. Reports are never overwritten.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import unittest

import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.special import eval_laguerre

T = 2 * np.pi
A = np.sqrt(1 / (16 * np.sqrt(5 / 2)))
B = 1 / (16 * A)
TARGET = np.pi / 4
SIGNS = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
PARITY = SIGNS[:, 0] * SIGNS[:, 1]
REPORT: dict = {}


def paths(t: float, centered: bool = True):
    x = A * (np.cos(t) - np.cos(2 * t))
    y = B * (np.sin(t) - 0.5 * np.sin(2 * t)) if centered else B * (1 - np.cos(t))
    return x, y


def force(t: float, layout: str = 'split', centered: bool = True):
    dx = A * (-np.sin(t) + 2 * np.sin(2 * t))
    dy = B * (np.cos(t) - np.cos(2 * t)) if centered else B * np.sin(t)
    v = np.array([1j * dx, -dy], dtype=complex)
    if layout == 'common':
        v = np.repeat(v.sum() / np.sqrt(2), 2)
    elif layout != 'split':
        raise ValueError('layout must be split or common')
    return v


def accumulated_profile(t: float, name: str):
    if name == 'static':
        return t
    if name == 'cosine':
        return np.sin(t)
    if name == 'shaped':
        return 0.7*t + 0.3*np.sin(1.7*t)/1.7 - 0.2*(np.cos(0.4*t)-1)/0.4
    raise ValueError('Unknown profile')


def profile(t: float, name: str):
    if name == 'static':
        return 1.
    if name == 'cosine':
        return np.cos(t)
    if name == 'shaped':
        return 0.7 + 0.3*np.cos(1.7*t) + 0.2*np.sin(0.4*t)
    raise ValueError('Unknown profile')


def response(epsilon: float, layout: str = 'split', shape: str = 'static',
             centered: bool = True, scale: float = 1., tighter: bool = False):
    """Interaction-picture beta_1,beta_2 and the ZZ Magnus phase."""
    def rhs(t, z):
        db = -1j * scale * force(t, layout, centered) * np.exp(1j * epsilon * accumulated_profile(t, shape))
        dtheta = np.imag(np.conj(z[0])*db[1] + np.conj(z[1])*db[0])
        return np.r_[db, dtheta]
    sol = solve_ivp(rhs, (0, T), np.zeros(3, dtype=complex), method='DOP853',
                    rtol=2e-13 if tighter else 2e-11,
                    atol=2e-15 if tighter else 1e-13,
                    max_step=T/80)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y[:2, -1], float(sol.y[2, -1].real)


def channel(beta, theta: float, nbar: float | None = None, fock: int | None = None,
            target: float = 0.):
    z = SIGNS @ np.asarray(beta)
    dsq = abs(z[:, None]-z[None, :])**2
    phase = (theta-target)*(PARITY[:, None]-PARITY[None, :]) + np.imag(z[:, None]*z[None, :].conj())
    if (nbar is None) == (fock is None):
        raise ValueError('Specify either thermal nbar or Fock number')
    chi = np.exp(-(nbar+0.5)*dsq) if nbar is not None else np.exp(-dsq/2)*eval_laguerre(fock, dsq)
    return np.exp(1j*phase)*chi


def average_infidelity(beta, theta: float, nbar: float):
    c = channel(beta, theta, nbar=nbar, target=TARGET)
    return float(1 - (4+c.sum().real)/20)


def direct_schrodinger(epsilon: float, layout: str, fock: int, cutoff: int = 28, shape: str = 'static'):
    """Full 4*cutoff state integration in the physical oscillator frame."""
    a = np.diag(np.sqrt(np.arange(1, cutoff)), 1).astype(complex)
    adag = a.conj().T
    n = np.diag(np.arange(cutoff))
    N = np.kron(np.eye(4), n)
    L = [np.kron(np.diag(SIGNS[:, j]), a) for j in range(2)]
    R = [q.conj().T for q in L]
    psi0 = np.zeros(4*cutoff, complex)
    psi0[np.arange(4)*cutoff+fock] = 0.5
    def rhs(t, psi):
        f = force(t, layout)
        return -1j*(epsilon*profile(t, shape)*(N@psi)
                     + sum(f[j]*(R[j]@psi)+f[j].conjugate()*(L[j]@psi) for j in range(2)))
    sol = solve_ivp(rhs, (0, T), psi0, method='DOP853', rtol=2e-11, atol=1e-13, max_step=T/80)
    if not sol.success:
        raise RuntimeError(sol.message)
    state = sol.y[:, -1].reshape(4, cutoff)
    rho = state @ state.conj().T
    edge = float(np.sum(abs(state[:, -3:])**2))
    return rho, float(np.sum(abs(state)**2)), edge


class Checks(unittest.TestCase):
    def test_01_exact_geometry_moments_and_coefficients(self):
        t, u = sp.symbols('t u', real=True)
        a, b = sp.symbols('A B', real=True)
        x = a*(sp.cos(t)-sp.cos(2*t)); y = b*(sp.sin(t)-sp.sin(2*t)/2)
        dx = sp.diff(x,t); dy = sp.diff(y,t)
        self.assertEqual(x.subs(t,0),0); self.assertEqual(y.subs(t,0),0)
        self.assertEqual(x.subs(t,2*sp.pi),0); self.assertEqual(y.subs(t,2*sp.pi),0)
        for f in (x,y):
            self.assertEqual(sp.integrate(f,(t,0,2*sp.pi)),0)
        area = sp.simplify(sp.integrate(x*dy-y*dx,(t,0,2*sp.pi)))
        self.assertEqual(area,4*sp.pi*a*b)
        action = sp.simplify(sp.integrate(x*x+y*y,(t,0,2*sp.pi)))
        self.assertEqual(action,sp.pi*(8*a*a+5*b*b)/4)
        energy = sp.simplify(sp.integrate(dx*dx+dy*dy,(t,0,2*sp.pi)))
        self.assertEqual(energy,sp.pi*(5*a*a+2*b*b))
        kernel = dx.subs(t,u)*dy-dy.subs(t,u)*dx
        theta2 = sp.simplify(sp.integrate(sp.integrate(-kernel*(t-u)**2/2,(u,0,t)),(t,0,2*sp.pi)))
        self.assertEqual(theta2,5*sp.pi*a*b/2)
        self.assertEqual(sp.integrate(t*x,(t,0,2*sp.pi)),0)
        self.assertEqual(sp.integrate(t*y,(t,0,2*sp.pi)),-3*sp.pi*b/2)
        REPORT['exact_example'] = {'area':str(area), 'common_phase_derivative':str(-action),
            'force_squared_integral':str(energy), 'split_phase_second_coefficient':str(theta2),
            'split_beta_leading':'beta1=O(epsilon^3), beta2=-(3*pi*B/2)*epsilon^2+O(epsilon^3)',
            'A':float(A),'B':float(B),'T':float(T),'target':float(TARGET)}

    def test_02_equal_resources_and_general_phase_symmetry(self):
        power_error = 0.; symmetry_error = 0.; averaging_error = 0.; rows=[]
        for t in np.linspace(0,T,103):
            power_error=max(power_error,abs(np.vdot(force(t,'split'),force(t,'split')).real
                                           -np.vdot(force(t,'common'),force(t,'common')).real))
        self.assertLess(power_error,2e-15)
        for shape in ('static','cosine','shaped'):
            for eps in (.013,.12,.7):
                p=response(eps,'split',shape)[1]; m=response(-eps,'split',shape)[1]
                c1=response(eps,'common',shape)[1];c2=response(-eps,'common',shape)[1]
                symmetry_error=max(symmetry_error,abs(p-m))
                averaging_error=max(averaging_error,abs(p-(c1+c2)/2))
                self.assertLess(abs(p-m),3e-10)
                self.assertLess(abs(p-(c1+c2)/2),3e-10)
                rows.append({'profile':shape,'epsilon':eps,'split_angle':p,
                             'sign_reversal_error':abs(p-m),'common_even_part_error':abs(p-(c1+c2)/2)})
        REPORT['symmetry']={'max_power_difference':power_error,'max_evenness_error':symmetry_error,
                            'max_phase_symmetrization_error':averaging_error,'cases':rows,
                            'resources':'Same duration and sum_j |f_j(t)|^2 at every time; independent per-qubit controls required.'}

    def test_03_static_drift_scaling_and_exact_thermal_channel(self):
        action = np.pi*(8*A*A+5*B*B)/4
        th2=5*np.pi*A*B/2
        beta2=-3*np.pi*B/2
        nbar=5.
        qcoef=(4/5)*(th2*th2+(2*nbar+1)*beta2*beta2)
        ccoef=(4/5)*action*action
        rows=[]
        for eps in (.005,.01,.02,.05,.1):
            row={'epsilon':eps,'nbar':nbar}
            for layout in ('common','split'):
                b,th=response(eps,layout)
                b2,tht=response(eps,layout,tighter=True)
                err=average_infidelity(b,th,nbar)
                self.assertLess(abs(err-average_infidelity(b2,tht,nbar)),3e-12)
                c=channel(b,th,nbar=nbar)
                self.assertLess(np.linalg.norm(c-c.conj().T),1e-13)
                self.assertGreaterEqual(np.linalg.eigvalsh(c).min(),-1e-11)
                row[layout]={'angle':th,'residual_displacement_norm':float(np.linalg.norm(b)),
                             'average_infidelity':err}
            rows.append(row)
        eps=.002
        bs,ts=response(eps,'split',tighter=True); bc,tc=response(eps,'common',tighter=True)
        self.assertLess(abs(average_infidelity(bs,ts,nbar)/eps**4/qcoef-1),.003)
        self.assertLess(abs(average_infidelity(bc,tc,nbar)/eps**2/ccoef-1),.01)
        self.assertLess(abs((ts-TARGET)/eps**2-th2),2e-4)
        d=.001
        derivative=(response(d,'common',tighter=True)[1]-response(-d,'common',tighter=True)[1])/(2*d)
        self.assertLess(abs(derivative+action),1e-5)
        b0,th0=response(0,tighter=True)
        for nv in (0,5,100):
            self.assertLess(abs(average_infidelity(b0,th0,nv)),2e-12)
        REPORT['static_comparison']={'table':rows,'common_quadratic_coefficient':ccoef,
            'split_quartic_coefficient_at_nbar5':qcoef,'common_phase_slope':-action,
            'limits':'Fixed finite thermal occupation; only the stipulated force model. epsilon=delta/nu, not delta/physical_mode_frequency.'}

    def test_04_full_quantum_dynamics_independent_of_magnus(self):
        rows=[]
        for layout in ('common','split'):
            for number in (0,3):
                eps=.07
                rho,norm,tail=direct_schrodinger(eps,layout,number)
                beta,theta=response(eps,layout)
                expected=channel(beta,theta,fock=number)/4
                error=float(np.linalg.norm(rho-expected))
                self.assertLess(error,3e-9)
                self.assertLess(abs(norm-1),3e-9)
                self.assertLess(tail,1e-12)
                rows.append({'layout':layout,'input_Fock':number,'Hilbert_dimension':112,
                             'reduced_state_error':error,'norm_error':abs(norm-1),'last_three_level_population':tail})
        # Direct state check also covers a time-dependent perturbation.
        rho,norm,tail=direct_schrodinger(.08,'split',0,shape='cosine')
        beta,theta=response(.08,'split','cosine')
        error=float(np.linalg.norm(rho-channel(beta,theta,fock=0)/4))
        self.assertLess(error,3e-9)
        rows.append({'layout':'split','input_Fock':0,'profile':'cosine','Hilbert_dimension':112,
                     'reduced_state_error':error,'norm_error':abs(norm-1),'last_three_level_population':tail})
        REPORT['independent_schrodinger']=rows

    def test_05_scope_controls(self):
        # Time-dependent detuning retains even entangling phase but generally creates O(eps) displacement.
        cosine=[]
        for eps in (.002,.004,.008):
            beta,theta=response(eps,'split','cosine',tighter=True)
            cosine.append({'epsilon':eps,'phase_error':theta-TARGET,
                           'displacement_norm':float(np.linalg.norm(beta)),
                           'average_infidelity_nbar5':average_infidelity(beta,theta,5)})
        self.assertLess(abs(cosine[1]['average_infidelity_nbar5']/cosine[0]['average_infidelity_nbar5']-4),.02)
        # A force-amplitude error is not canceled: the phase scales as amplitude squared.
        amplitude=[]
        for zeta in (.001,.01):
            beta,theta=response(0,'split',scale=1+zeta,tighter=True)
            self.assertAlmostEqual(theta,(1+zeta)**2*TARGET,places=10)
            amplitude.append({'relative_amplitude_error':zeta,'angle':theta,
                              'average_infidelity_nbar5':average_infidelity(beta,theta,5)})
        # Equal-energy paths without the zero-average conditions do not suppress residual displacement.
        p=response(.001,'split',centered=False,tighter=True)[0]
        pp=response(.002,'split',centered=False,tighter=True)[0]
        self.assertLess(abs(np.linalg.norm(pp)/np.linalg.norm(p)-2),.01)
        REPORT['controls']={'oscillating_detuning':cosine,'amplitude_error':amplitude,
            'uncentered_path_displacement_ratio':float(np.linalg.norm(pp)/np.linalg.norm(p)),
            'interpretation':'No claim of arbitrary-waveform full-gate robustness, amplitude robustness, or immunity to heating.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():
        ap.error('Refusing to overwrite an existing report.')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',test_groups=result.testsRun)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:
        json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)

if __name__=='__main__':
    main()
