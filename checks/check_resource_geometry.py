#!/usr/bin/env python3
"""Checks for matched-space oscillator-gate force optimality.

All physical conclusions refer to the single-mode linear-force Hamiltonian and
integrated squared effective force. The projection benchmark is our application
of the published fixed-one-pulse strategy to this control space, not published
experimental data. Reports refuse overwrite. Run with --output NEW_PATH.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import unittest
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.linalg import eigh
from scipy.optimize import minimize_scalar

REPORT: dict = {}
T = 2*np.pi
TARGET = np.pi/4


def cq(fun):
    return quad(lambda t: float(np.real(fun(t))),0,T,epsabs=2e-12,epsrel=2e-12)[0] + 1j*quad(lambda t: float(np.imag(fun(t))),0,T,epsabs=2e-12,epsrel=2e-12)[0]


def basis(t):
    return np.array([(np.sin(t)-2*np.sin(2*t))/np.sqrt(5*np.pi),
                     (np.cos(t)-np.cos(2*t))/np.sqrt(2*np.pi)])


def primitive(t):
    return np.array([(np.cos(2*t)-np.cos(t))/np.sqrt(5*np.pi),
                     (np.sin(t)-.5*np.sin(2*t))/np.sqrt(2*np.pi)])


def fourtone_matrices():
    k=2/np.sqrt(10)
    return np.array([[0,1j*k],[-1j*k,0]]), np.diag([2/5,5/8])


def protocols():
    K,D=fourtone_matrices(); lam=2/np.sqrt(10)
    g=np.array([1j,1.])/np.sqrt(2)
    dg=D@g
    q=g-dg*np.vdot(dg,g)/np.vdot(dg,dg)
    overlap=float(np.linalg.norm(q)); q=q/overlap
    sc=np.sqrt(TARGET/(2*lam)); spj=np.sqrt(TARGET/(2*lam*overlap))
    return {'common':(sc*g,sc*g),
            'split':(sc*np.array([1j,0.]),sc*np.array([0.,1.])),
            'fixed_first_projection':(spj*q,spj*g)}, overlap


def response(c1,c2,eps,shaped=False):
    def rhs(t,z):
        phase=eps*(.7*t+.3*np.sin(1.7*t)/1.7-.2*(np.cos(.4*t)-1)/.4) if shaped else eps*t
        fs=np.array([basis(t)@c1,basis(t)@c2])
        db=-1j*fs*np.exp(1j*phase)
        return np.r_[db,np.imag(z[0].conjugate()*db[1]+z[1].conjugate()*db[0])]
    sol=solve_ivp(rhs,(0,T),np.zeros(3,complex),method='DOP853',rtol=2e-12,atol=2e-14,max_step=T/90)
    if not sol.success: raise ArithmeticError(sol.message)
    return sol.y[:2,-1],float(sol.y[2,-1].real)


class Checks(unittest.TestCase):
    def test_01_exact_matched_control_space(self):
        t=sp.symbols('t',real=True)
        U=sp.sin(t)-2*sp.sin(2*t); V=sp.cos(t)-sp.cos(2*t)
        Au=sp.cos(2*t)-sp.cos(t); Av=sp.sin(t)-sp.sin(2*t)/2
        G=sp.diag(5*sp.pi,2*sp.pi)
        raws=[U,V]; prims=[Au,Av]
        M=sp.Matrix(2,2,lambda i,j:sp.integrate(prims[i]*raws[j],(t,0,2*sp.pi)))
        N=sp.Matrix(2,2,lambda i,j:sp.integrate(prims[i]*prims[j],(t,0,2*sp.pi)))
        W=sp.diag(1/sp.sqrt(5*sp.pi),1/sp.sqrt(2*sp.pi))
        K=sp.simplify(-sp.I*W*M*W); D=sp.simplify(W*N*W)
        self.assertEqual(K,sp.Matrix([[0,2*sp.I/sp.sqrt(10)],[-2*sp.I/sp.sqrt(10),0]]))
        self.assertEqual(D,sp.diag(sp.Rational(2,5),sp.Rational(5,8)))
        self.assertEqual(K*K,sp.Rational(2,5)*sp.eye(2))
        for f in raws:
            self.assertEqual(f.subs(t,0),0);self.assertEqual(f.subs(t,2*sp.pi),0)
            self.assertEqual(sp.integrate(f,(t,0,2*sp.pi)),0)
            self.assertEqual(sp.integrate(t*f,(t,0,2*sp.pi)),0)
        # These are the entire four-frequency endpoint/moment null space.
        constraints=sp.Matrix([[1,1,1,1],[1,sp.Rational(1,2),-1,sp.Rational(-1,2)]])
        self.assertEqual(4-constraints.rank(),2)
        REPORT['exact_space']={'frequencies_in_units_nu':[1,2,-1,-2],
           'complex_dimension':2,'phase_matrix':str(K),'detuning_overlap_matrix':str(D),
           'force_minimum':'pi*sqrt(10)*abs(Theta)/T',
           'interpretation':'Global within the declared four-effective-offset space, including force endpoints and first displacement moment.'}

    def test_02_general_real_basis_optimality(self):
        t=sp.symbols('t',real=True); w=t*t*(1-t)**2
        area0=sp.integrate(w,(t,0,1)); maxres=0.; rows=[]
        alphas=[]
        for n in range(1,7):
            P=sp.legendre(n,2*t-1)
            alphas.append(sp.expand(w*(P-sp.integrate(w*P,(t,0,1))/area0)))
        forces=[sp.diff(a,t) for a in alphas]
        Gs=sp.Matrix(6,6,lambda i,j:sp.integrate(forces[i]*forces[j],(t,0,1)))
        Ls=sp.Matrix(6,6,lambda i,j:sp.integrate(alphas[i]*forces[j],(t,0,1)))
        Ds=sp.Matrix(6,6,lambda i,j:sp.integrate(alphas[i]*alphas[j],(t,0,1)))
        self.assertEqual(Ls+Ls.T,sp.zeros(6))
        for a,f in zip(alphas,forces):
            self.assertEqual(sp.integrate(a,(t,0,1)),0)
            self.assertEqual(f.subs(t,0),0);self.assertEqual(f.subs(t,1),0)
        rng=np.random.default_rng(91026)
        for d in range(2,7):
            G=np.array(Gs[:d,:d],float);L=np.array(Ls[:d,:d],float);D=np.array(Ds[:d,:d],float)
            K=-1j*L
            vals,Q=eigh(K,G);lam=vals[-1];g=Q[:,-1]
            self.assertLess(abs(vals[0]+lam),1e-12)
            f1=(g-g.conjugate())/np.sqrt(2);f2=(g+g.conjugate())/np.sqrt(2)
            E=float((np.vdot(f1,G@f1)+np.vdot(f2,G@f2)).real)
            phase=float(2*np.vdot(f1,K@f2).real)
            sensitivity=float(-2*np.vdot(f1,D@f2).real)
            self.assertAlmostEqual(E,2.,places=11)
            self.assertAlmostEqual(phase/E,lam,places=11)
            self.assertAlmostEqual(sensitivity,0.,places=12)
            fs=[sp.lambdify(t,f,'numpy') for f in forces[:d]]
            localres=0.
            for tt in np.linspace(0,1,113):
                rv=np.array([ff(tt) for ff in fs])
                old=2*abs(rv@g)**2; new=abs(rv@f1)**2+abs(rv@f2)**2
                localres=max(localres,float(abs(new-old)))
            maxres=max(maxres,localres)
            self.assertLess(localres,2e-10)
            for _ in range(80):
                a=rng.normal(size=d)+1j*rng.normal(size=d)
                b=rng.normal(size=d)+1j*rng.normal(size=d)
                e=(np.vdot(a,G@a)+np.vdot(b,G@b)).real
                theta=2*np.vdot(a,K@b).real
                self.assertLessEqual(abs(theta),lam*e+1e-10)
            rows.append({'dimension':d,'spectral_radius':float(lam),'compiled_efficiency':phase/E,
                         'static_angle_derivative':sensitivity})
        REPORT['general_basis']={'cases':rows,'max_pointwise_force_difference':maxres,
          'note':'Finite checks of the general spectral proof, not random-search proof of optimality.'}

    def test_03_published_strategy_matched_comparison(self):
        K,D=fourtone_matrices();lam=2/np.sqrt(10)
        ps,kappa=protocols()
        exact=9/np.sqrt(1762)
        self.assertAlmostEqual(kappa,exact,places=13)
        rows=[]
        for name,(a,b) in ps.items():
            e=float(np.vdot(a,a).real+np.vdot(b,b).real)
            theta=float(2*np.vdot(a,K@b).real)
            deriv=float(-2*np.vdot(a,D@b).real)
            self.assertAlmostEqual(theta,TARGET,places=13)
            numbeta,numtheta=response(a,b,0.)
            self.assertLess(np.linalg.norm(numbeta),1e-11)
            self.assertAlmostEqual(numtheta,TARGET,places=11)
            for aa in (a,b):
                self.assertLess(abs(cq(lambda t:(basis(t)@aa))),1e-12)
                self.assertLess(abs(cq(lambda t:t*(basis(t)@aa))),2e-12)
            dt=1e-5
            slope=(response(a,b,dt)[1]-response(a,b,-dt)[1])/(2*dt)
            self.assertAlmostEqual(slope,deriv,places=7)
            ratio=e/(TARGET/lam)
            if name=='fixed_first_projection': self.assertAlmostEqual(ratio,1/kappa,places=12)
            else:self.assertAlmostEqual(ratio,1.,places=12)
            if name!='common':self.assertLess(abs(deriv),1e-13)
            rows.append({'method':name,'force_cost':e,'relative_cost':ratio,'nominal_phase':theta,
                         'analytic_phase_derivative':deriv,'integrated_phase_derivative':slope})
        # Same original smooth pulse as prior, not a new fitted pulse.
        Ap=np.sqrt(1/(16*np.sqrt(5/2)));Bp=1/(16*Ap)
        a,b=ps['split']
        for t in np.linspace(0,T,67):
            old=np.array([1j*Ap*(-np.sin(t)+2*np.sin(2*t)),-Bp*(np.cos(t)-np.cos(2*t))])
            new=np.array([basis(t)@a,basis(t)@b])
            self.assertLess(np.linalg.norm(old+new),5e-16)
        REPORT['matched_projection_comparison']={'overlap_exact':'9/sqrt(1762)',
            'fixed_first_cost_factor':float(1/kappa),'protocols':rows,
            'scope':'Our single-mode, four-offset application of BG21 S16 recipe, not the published multimode data or a universal comparison with independent-pulse optimizers.'}

    def test_04_resource_hypothesis_controls(self):
        # One-sided one-dimensional spectral space, with closure, centered trajectory,
        # and force endpoints all already satisfied.
        t=sp.symbols('t',real=True)
        f=sp.exp(sp.I*t)-4*sp.exp(2*sp.I*t)+3*sp.exp(3*sp.I*t)
        Af=(sp.exp(sp.I*t)-2*sp.exp(2*sp.I*t)+sp.exp(3*sp.I*t))/sp.I
        self.assertEqual(sp.simplify(sp.diff(Af,t)-f),0)
        for r in (0,1):self.assertEqual(sp.simplify(sp.integrate(t**r*f,(t,0,2*sp.pi))),0)
        self.assertEqual(f.subs(t,0),0);self.assertEqual(f.subs(t,2*sp.pi),0)
        # Independent exponential orthogonality: sums of coefficient squares.
        E=2*sp.pi*(1+16+9); S=2*sp.pi*(1+sp.Rational(16,2)+sp.Rational(9,3)); D=2*sp.pi*(1+4+1)
        self.assertEqual(D/S,sp.Rational(1,2))
        # Conjugation adds negative offsets, and can destroy a spectator notch.
        posnotch=sp.simplify(sp.integrate(f*sp.exp(sp.I*t),(t,0,2*sp.pi)))
        negnotch=sp.simplify(sp.integrate(sp.conjugate(f)*sp.exp(sp.I*t),(t,0,2*sp.pi)))
        self.assertEqual(posnotch,0);self.assertEqual(negnotch,2*sp.pi)
        ps,_=protocols();peaks={}
        grid=np.linspace(0,T,4001)
        for name in ('common','split'):
            peaks[name]=[]
            for coeff in ps[name]:
                vals=np.array([abs(basis(t)@coeff) for t in grid]);k=int(vals.argmax())
                l=grid[max(0,k-2)];r=grid[min(len(grid)-1,k+2)]
                op=minimize_scalar(lambda tt:-abs(basis(tt)@coeff),bounds=(l,r),method='bounded',options={'xatol':1e-14})
                peaks[name].append(float(-op.fun))
        self.assertGreater(max(peaks['split']),max(peaks['common']))
        # A closed circle supplies an exact per-qubit peak counterexample.
        peak_common=1.;peak_split=np.sqrt(2.)
        self.assertAlmostEqual(peak_split**2/peak_common**2,2.)
        REPORT['scope_controls']={'one_sided_offsets':[1,2,3],
            'one_sided_force_shape':'exp(it)-4 exp(2it)+3 exp(3it)',
            'one_dimensional_angle_relation':'Theta_prime=-Theta/2, in nu=1 units',
            'mirror_offsets_needed':[-1,-2,-3],
            'spectator_notch_before':str(posnotch),'conjugate_notch_after':str(negnotch),
            'four_offset_peak_amplitudes':peaks,
            'circle_peak_amplitude_ratio':float(peak_split),
            'warning':'No theorem for per-qubit peak-constrained, arbitrary one-sided, multimode, or physical optical-power optimization.'}

    def test_05_finite_error_and_all_waveform_phase(self):
        ps,_=protocols();rows=[]
        signs=np.array([[1,1],[1,-1],[-1,1],[-1,-1]]); parity=np.prod(signs,axis=1)
        for eps in (.004,.008,.03):
            row={'epsilon':eps}
            for name,(a,b) in ps.items():
                beta,theta=response(a,b,eps)
                bz=signs@beta; diff=bz[:,None]-bz[None,:]
                phase=(theta-TARGET)*(parity[:,None]-parity[None,:])+np.imag(bz[:,None]*bz[None,:].conjugate())
                C=np.exp(1j*phase-(5+.5)*abs(diff)**2)
                self.assertLess(np.max(abs(np.diag(C)-1)),1e-14)
                self.assertGreaterEqual(float(np.linalg.eigvalsh(C).min()),-1e-12)
                inf=float(1-(4+C.sum().real)/20)
                row[name]={'infidelity':inf,'phase_error':theta-TARGET,'residual_norm':float(np.linalg.norm(beta))}
            rows.append(row)
        for name in ('split','fixed_first_projection'):
            ratio=rows[1][name]['infidelity']/rows[0][name]['infidelity']
            self.assertLess(abs(ratio-16),.25)
        ratio=rows[1]['common']['infidelity']/rows[0]['common']['infidelity']
        self.assertLess(abs(ratio-4),.1)
        errors=[]
        for eps in (.03,.21):
            for shaped in (False,True):
                splp=response(*ps['split'],eps,shaped)[1];splm=response(*ps['split'],-eps,shaped)[1]
                cp=response(*ps['common'],eps,shaped)[1];cm=response(*ps['common'],-eps,shaped)[1]
                err=max(abs(splp-splm),abs(splp-(cp+cm)/2))
                self.assertLess(err,2e-11);errors.append(float(err))
        REPORT['finite_error']={'effective_model_thermal_occupation':5.,'rows':rows,
            'max_even_part_identity_error':max(errors),
            'scope':'Finite checks of static fourth-order full-channel scaling; general-waveform statement protects phase only.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():parser.error('Refusing to overwrite report')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',test_groups=result.testsRun)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:json.dump(REPORT,f,sort_keys=True,indent=2,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=='__main__':main()
