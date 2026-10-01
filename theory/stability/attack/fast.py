"""Fast float64 recovery map for adversarial search (validated against mpmath in attack.py)."""
import numpy as np
from common import Front, H_cone, e_of_m
from fractions import Fraction as F
class Fast:
    def __init__(self, m):
        self.m = sorted(m); n = self.n = len(m)
        fr = Front(n)
        self.Linv = np.array([[float(x) for x in row] for row in fr.Linv.tolist()])
        self.h0 = np.array([float(x) for x in fr.h0])
        self.H = np.array([float(x) for x in H_cone([F(x) for x in m])])
    def T(self, I):
        n = self.n; K = 2*n-3
        U = np.zeros(K+1)
        for l in range(1, n): U[2*l-1] = I[l]/(2*l-1)
        T = np.zeros(K+1)
        for k in range(1, K+1):
            T2 = np.convolve(T[:k], T[:k])[:k]  # T^2 up to degree k-1
            s = 0.0
            for j in range(1, k+1):
                if U[j] == 0: continue
                c = (1.0 if k-j == 0 else 0.0) - (T2[k-j] if k-j < len(T2) else 0.0)
                s += j*U[j]*c
            T[k] = s/k
        return T
    def e(self, dH):
        n = self.n
        I = self.Linv @ (self.H + dH - self.h0)
        T = self.T(I)
        M = np.zeros((n, n)); b = np.zeros(n)
        for j in range(n-1):
            for k in range(1, n+1):
                v = 0.0
                if k == 2*j+1: v += 1
                if k % 2 == 0 and 2*j+1-k >= 1: v -= T[2*j+1-k]
                M[j, k-1] = v
            b[j] = T[2*j+1]
        M[n-1, n-2] = 1; M[n-1, n-1] = -I[0]
        return np.concatenate([[1.0], np.linalg.solve(M, b)])
    def roots(self, dH):
        e = self.e(dH)
        return np.roots([(-1)**j*e[j] for j in range(self.n+1)])
    def F(self, dH):
        r = self.roots(dH)
        xs = np.sort(r.real)
        return np.max(np.abs(xs - np.array(self.m)))
    def ok(self, dH):
        r = self.roots(dH)
        return sorted(int(np.floor(x+0.5)) for x in r.real) == self.m
