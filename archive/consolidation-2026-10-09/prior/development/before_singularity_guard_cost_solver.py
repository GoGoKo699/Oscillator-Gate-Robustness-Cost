"""Exact variational reduction for a finite one-mode force-control space.

Inputs are the Hermitian nominal-phase matrix K and strictly positive displacement
Gram matrix D in an orthonormal force basis. Numerical output is floating point,
not a certified interval. The theorem and equality construction are in THEOREM.md.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq

@dataclass
class RobustOptimum:
    multiplier: float
    phase_per_cost: float
    nominal_phase_per_cost: float
    force1: np.ndarray
    force2: np.ndarray


def robust_optimum(K: np.ndarray, D: np.ndarray) -> RobustOptimum:
    K=np.asarray(K,dtype=complex); D=np.asarray(D,dtype=complex)
    if K.ndim!=2 or K.shape[0]!=K.shape[1] or D.shape!=K.shape or len(K)==0:
        raise ValueError('K and D must be equally sized nonempty square matrices.')
    if not np.isfinite(K).all() or not np.isfinite(D).all():
        raise ValueError('Matrices must be finite.')
    if not np.allclose(K,K.conj().T,atol=1e-12,rtol=1e-12) or not np.allclose(D,D.conj().T,atol=1e-12,rtol=1e-12):
        raise ValueError('K and D must be Hermitian.')
    K=(K+K.conj().T)/2; D=(D+D.conj().T)/2
    dmin=float(eigh(D,eigvals_only=True)[0])
    if dmin<=0: raise ValueError('D must be strictly positive definite.')
    lam=float(np.max(abs(eigh(K,eigvals_only=True))))
    if lam==0: return RobustOptimum(0.,0.,0.,np.zeros(len(K),complex),np.zeros(len(K),complex))
    def center(zeta: float) -> float:
        w=eigh(K-zeta*D,eigvals_only=True)
        return float(w[0]+w[-1])
    bound=2*lam/dmin
    zeta=brentq(center,-bound,bound,xtol=1e-14,rtol=1e-14)
    ev,V=eigh(K-zeta*D)
    r=float((ev[-1]-ev[0])/2)
    if r<1e-12*lam:
        return RobustOptimum(zeta,0.,lam,np.zeros(len(K),complex),np.zeros(len(K),complex))
    up=V[:,-1]; um=V[:,0]
    qp=float(np.vdot(up,D@up).real); qm=float(np.vdot(um,D@um).real)
    x=np.sqrt(qm/(qp+qm))*up; y=np.sqrt(qp/(qp+qm))*um
    f1=(x+y)/np.sqrt(2); f2=(x-y)/np.sqrt(2)
    return RobustOptimum(zeta,r,lam,f1,f2)


def fourier_matrices(modes: np.ndarray, C: np.ndarray, nu: float=1.) -> tuple[np.ndarray,np.ndarray,np.ndarray]:
    """Raw matrices for r_a(t)=sum_n C[n,a] exp(i*n*nu*t)/sqrt(T)."""
    modes=np.asarray(modes,dtype=float); C=np.asarray(C,dtype=complex)
    if nu<=0 or np.any(modes==0) or C.ndim!=2 or C.shape[0]!=len(modes):
        raise ValueError('Nonzero modes and a matching coefficient matrix required.')
    v=1/(nu*modes)
    G=C.conj().T@C
    K=C.conj().T@np.diag(v)@C
    D=C.conj().T@(np.diag(v*v)+np.outer(v,v))@C
    return G,K,D


def whiten(G: np.ndarray,K: np.ndarray,D: np.ndarray) -> tuple[np.ndarray,np.ndarray,np.ndarray]:
    e,V=eigh(G)
    if e[0]<=0: raise ValueError('Force Gram matrix must be positive definite.')
    W=(V/np.sqrt(e))@V.conj().T
    return W.conj().T@K@W,W.conj().T@D@W,W
