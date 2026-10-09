#!/usr/bin/env python3
"""Narrow checks of the exact static-angle robustness cost. No legacy imports.
Reports are append-only by filename; numerical sampling is not an optimality proof.
"""
from __future__ import annotations
import argparse,json,unittest
from pathlib import Path
import sys
sys.dont_write_bytecode=True
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp
from scipy.linalg import eigh
from cost_solver import robust_optimum,fourier_matrices,whiten

REPORT={}
T=2*np.pi; TARGET=np.pi/4


def response(modes,c1,c2,delta):
    modes=np.asarray(modes);c1=np.asarray(c1);c2=np.asarray(c2)
    def rhs(t,y):
        es=np.exp(1j*modes*t)/np.sqrt(T)
        p=-1j*(c1@es)*np.exp(1j*delta*t)
        q=-1j*(c2@es)*np.exp(1j*delta*t)
        return np.array([p,q,np.imag(y[0].conjugate()*q+y[1].conjugate()*p)],complex)
    sol=solve_ivp(rhs,(0,T),np.zeros(3,complex),method='DOP853',rtol=2e-12,atol=2e-14)
    if not sol.success:raise RuntimeError(sol.message)
    return sol.y[:2,-1],float(sol.y[2,-1].real)

class Checks(unittest.TestCase):
    def test_01_extremal_pencil_and_exact_attainment(self):
        rng=np.random.default_rng(2091009); records=[]
        for n in (2,3,4,6):
            for rep in range(4):
                A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
                B=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
                K=(A+A.conj().T)/2;D=B.conj().T@B+np.eye(n)
                ans=robust_optimum(K,D);a,b=ans.force1,ans.force2
                E=float(np.vdot(a,a).real+np.vdot(b,b).real)
                phase=float(2*np.vdot(a,K@b).real);der=float(-2*np.vdot(a,D@b).real)
                self.assertAlmostEqual(E,1.,places=13)
                self.assertLess(abs(phase-ans.phase_per_cost),2e-12)
                self.assertLess(abs(der),2e-12)
                self.assertLessEqual(ans.phase_per_cost,ans.nominal_phase_per_cost+2e-12)
                vals=eigh(K-ans.multiplier*D,eigvals_only=True)
                self.assertLess(abs(vals[0]+vals[-1]),2e-12)
                # Independent feasible vectors: orthogonalize in the real D-inner product.
                max_random=0.
                for _ in range(60):
                    a=rng.normal(size=n)+1j*rng.normal(size=n)
                    b=rng.normal(size=n)+1j*rng.normal(size=n)
                    Da=D@a;b-=float(np.vdot(a,D@b).real)/float(np.vdot(Da,Da).real)*Da
                    E=np.vdot(a,a).real+np.vdot(b,b).real
                    value=abs(2*np.vdot(a,K@b).real/E)
                    self.assertLessEqual(value,ans.phase_per_cost+1e-12)
                    max_random=max(max_random,float(value))
                records.append({'dimension':n,'mu':ans.multiplier,'r':ans.phase_per_cost,
                    'nominal':ans.nominal_phase_per_cost,'phase_residual':abs(phase-ans.phase_per_cost),
                    'derivative_residual':abs(der),'largest_random_feasible_efficiency':max_random})
        D=np.array([[2.,.3],[.3,1.]])
        ans=robust_optimum(1.7*D,D);self.assertEqual(ans.phase_per_cost,0.)
        REPORT['pencil']={'cases':records,'proportional_K_D':'No nonzero robust phase; zero efficiency.'}

    def test_02_exact_one_sided_control_space(self):
        C=sp.Matrix([[1,1],[-4,-3],[3,0],[0,2]])
        freqs=sp.diag(1,sp.Rational(1,2),sp.Rational(1,3),sp.Rational(1,4))
        G=C.T*C;K=C.T*freqs*C;D=C.T*freqs**2*C
        self.assertEqual(G,sp.Matrix([[26,13],[13,14]]))
        self.assertEqual(K,sp.Matrix([[12,7],[7,sp.Rational(13,2)]]))
        self.assertEqual(D,sp.Matrix([[6,4],[4,sp.Rational(7,2)]]))
        self.assertEqual(sp.ones(1,4)*C,sp.zeros(1,2))
        self.assertEqual(sp.ones(1,4)*freqs*C,sp.zeros(1,2))
        mu=sp.simplify(sp.trace(G.inv()*K)/sp.trace(G.inv()*D))
        r=sp.sqrt(-sp.factor((K-mu*D).det()/G.det()))
        self.assertEqual(mu,sp.Rational(155,71))
        self.assertEqual(sp.simplify(r-sp.sqrt(190905)/4615),0)
        z=sp.Symbol('z');spec=sp.solve((K-z*G).det(),z)
        lam=max(spec,key=lambda a:float(a))
        Gn,Kn,Dn=map(lambda x:np.array(x,float),(G,K,D))
        Kw,Dw,W=whiten(Gn,Kn,Dn);opt=robust_optimum(Kw,Dw)
        self.assertAlmostEqual(opt.multiplier,float(mu),places=12)
        self.assertAlmostEqual(opt.phase_per_cost,float(r),places=13)
        # Independent force/trajectory integral, not the matrix-entry formula.
        Cn=np.array(C,float); modes=np.arange(1,5)
        def bas(t):return np.exp(1j*modes*t)@Cn/np.sqrt(T)
        def traj(t):return ((np.exp(1j*modes*t)-1)/(1j*modes))@Cn/np.sqrt(T)
        def cq(f):return quad(lambda t:float(f(t).real),0,T,epsabs=2e-12)[0]+1j*quad(lambda t:float(f(t).imag),0,T,epsabs=2e-12)[0]
        M=np.array([[cq(lambda t,a=a,b=b:traj(t)[a].conjugate()*bas(t)[b]) for b in range(2)] for a in range(2)])
        Di=np.array([[cq(lambda t,a=a,b=b:traj(t)[a].conjugate()*traj(t)[b]) for b in range(2)] for a in range(2)])
        self.assertLess(np.linalg.norm((M-M.conj().T)/(2j)-Kn),2e-12)
        self.assertLess(np.linalg.norm(Di-Dn),2e-12)
        REPORT['one_sided']={'G':str(G),'K':str(K),'D':str(D),'mu_exact':str(mu),'r_exact':str(r),
            'nominal_efficiency_exact':str(lam),'nominal_efficiency':float(lam),'robust_efficiency':float(r),
            'cost_ratio':float(lam/r),'nominal_cost_at_pi_over_4':float(sp.pi/(4*lam)),
            'robust_cost_at_pi_over_4':float(sp.pi/(4*r)),
            'interpretation':'Same positive-offset, four-tone space and all endpoint/moment constraints for both competitors.'}

    def test_03_no_penalty_criterion_and_conjugation(self):
        rng=np.random.default_rng(938);results=[]
        for top,bottom in ((2.,-2.),(2.,-1.8),(2.,.3),(.5,-2.)):
            K=np.diag([bottom,top]);A=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));D=A.conj().T@A+np.eye(2)
            a=robust_optimum(K,D)
            if top==-bottom:self.assertAlmostEqual(a.phase_per_cost,a.nominal_phase_per_cost,places=12)
            else:self.assertLess(a.phase_per_cost,a.nominal_phase_per_cost-1e-5)
            results.append({'K_extremes':[bottom,top],'ratio':a.nominal_phase_per_cost/a.phase_per_cost})
        k=2/np.sqrt(10);K=np.array([[0,1j*k],[-1j*k,0]]);D=np.diag([.4,.625])
        a=robust_optimum(K,D);self.assertAlmostEqual(a.phase_per_cost,k,places=13);self.assertLess(abs(a.multiplier),1e-14)
        # A physical non-conjugation-invariant space with balanced extrema.
        modes=np.array([2,-1,-3]);C=np.array([[1.,0],[0,.5],[0,np.sqrt(3)/2]])
        G,K,D=fourier_matrices(modes,C);self.assertLess(np.linalg.norm(G-np.eye(2)),1e-14)
        self.assertLess(np.linalg.norm(K-np.diag([.5,-.5])),1e-14)
        a=robust_optimum(K,D);self.assertAlmostEqual(a.phase_per_cost,.5,places=13)
        REPORT['criterion']={'tests':results,'symmetric_four_tone_efficiency':k,
            'nonconjugate_example':{'offsets':modes.tolist(),'phase_spectrum':[.5,-.5],'r':a.phase_per_cost},
            'scope':'Balanced extreme nominal eigenvalues are necessary and sufficient for zero STATIC phase penalty. Arbitrary-waveform evenness does not follow.'}

    def test_04_independent_force_dynamics(self):
        modes=np.arange(1,5);C=np.array([[1,1],[-4,-3],[3,0],[0,2]],float)
        G,K,D=fourier_matrices(modes,C);Kw,Dw,W=whiten(G,K,D);ans=robust_optimum(Kw,Dw)
        fac=np.sqrt(TARGET/ans.phase_per_cost)
        c1=C@W@ans.force1*fac;c2=C@W@ans.force2*fac
        raw={};responses={}
        for eps in (-.02,-.01,-.0002,-.0001,0.,.0001,.0002,.01,.02):
            beta,theta=response(modes,c1,c2,eps);responses[eps]=(beta,theta)
            raw[str(eps)]={'theta':theta,'residual_displacement_norm':float(np.linalg.norm(beta))}
        self.assertLess(abs(responses[0.][1]-TARGET),3e-12)
        self.assertLess(np.linalg.norm(responses[0.][0]),3e-12)
        slope=(responses[-.0002][1]-8*responses[-.0001][1]+8*responses[.0001][1]-responses[.0002][1])/(12*.0001)
        self.assertLess(abs(slope),3e-8)
        ratio=np.linalg.norm(responses[.02][0])/np.linalg.norm(responses[.01][0])
        self.assertTrue(3.7<ratio<4.3)
        asym=responses[.02][1]-responses[-.02][1]
        self.assertGreater(abs(asym),1e-7)
        # Physical waveform derivative checked against the raw matrices, off the robust locus too.
        ca=C@np.array([.2+.1j,-.1+.3j]);cb=C@np.array([.1-.2j,.3+.1j]);h=.0001
        slope2=(response(modes,ca,cb,h)[1]-response(modes,ca,cb,-h)[1])/(2*h)
        theory=-2*np.vdot(np.array([.2+.1j,-.1+.3j]),D@np.array([.1-.2j,.3+.1j])).real
        self.assertLess(abs(slope2-theory),3e-7)
        REPORT['dynamics']={'rows':raw,'fourth_order_stencil_phase_slope':float(slope),
            'second_order_displacement_ratio':float(ratio),'angle_asymmetry_at_plus_minus_002':float(asym),
            'off_locus_derivative_error':float(abs(slope2-theory)),
            'method':'Independent integration of exact force ODE; no truncated oscillator basis.'}

    def test_05_all_minimizers_and_peak_obstruction(self):
        c=sp.Symbol('c',real=True)
        S=sp.Rational(2,5)*(1-c*c)*(1-4*c)**2+(1+c-2*c*c)**2
        self.assertEqual(sp.expand(4-S-(c+1)**2*(12*c*c-20*c+13)/5),0)
        self.assertLess((-20)**2-4*12*13,0)
        # K=k J, D=diag(d1,d2): anticommutator fixes the complete equality locus.
        d1,d2=sp.symbols('d1 d2',positive=True)
        J=sp.Matrix([[0,sp.I],[-sp.I,0]]);D=sp.diag(d1,d2)
        self.assertEqual(sp.simplify((D*J+J*D)/2-(d1+d2)*J/2),sp.zeros(2))
        ar,ai,br,bi=sp.symbols('ar ai br bi',real=True);v=sp.Matrix([ar+sp.I*ai,br+sp.I*bi])
        self.assertEqual(sp.simplify((v.H*J*v)[0]+2*(ar*bi-ai*br)),0)
        # At the midpoint both peak bounds force |sin theta|=|cos theta|=1/sqrt2.
        # Then the nonzero derivative of u makes a peak exceed the common cap.
        t=sp.Symbol('t',real=True)
        u=sp.sqrt(sp.Rational(2,5))*(sp.sin(t)-2*sp.sin(2*t));vfun=sp.cos(t)-sp.cos(2*t)
        self.assertEqual(u.subs(t,sp.pi),0);self.assertEqual(vfun.subs(t,sp.pi),-2)
        self.assertEqual(sp.simplify(sp.diff(u,t).subs(t,sp.pi)+sp.sqrt(10)),0)
        self.assertEqual(sp.diff(vfun,t).subs(t,sp.pi),0)
        f=(u+vfun)/sp.sqrt(2)
        self.assertEqual(sp.simplify(sp.diff(f*f,t).subs(t,sp.pi)-2*sp.sqrt(10)),0)
        REPORT['peak_obstruction']={'sum_square_bound_identity':str(sp.factor(4-S)),
            'all_optimal_robust_pairs':'a=A exp(i phi)(cos theta,sin theta); b=A exp(i phi)(i sin theta,-i cos theta)',
            'midpoint_derivative_of_normalized_peak_square':'2 sqrt(10)',
            'conclusion':'No first-order robust pair at the exact minimum integrated cost satisfies the nominal common optimum per-qubit peak cap. No global peak-constrained optimum is claimed.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():p.error('Refusing to overwrite a report.')
    res=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if res.wasSuccessful() else 'FAIL',test_groups=res.testsRun)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open('x') as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if res.wasSuccessful() else 1)
if __name__=='__main__':main()
