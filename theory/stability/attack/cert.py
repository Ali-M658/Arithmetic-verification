"""Independent implementation of the certificates of Proposition S5 (exact rationals)."""
from common import *
from fractions import Fraction as F
import sympy as sp
def ser_mul(a, b, K):
    c = [F(0)]*(K+1)
    for i, x in enumerate(a):
        if x == 0: continue
        for j in range(K+1-i):
            if b[j]: c[i+j] += x*b[j]
    return c
def tan_series(U, K, hyper=False):
    # T' = U'(1 + s T^2), s=+1 tan, -1 tanh ; U[0]=0
    s = -1 if hyper else 1
    T = [F(0)]*(K+1)
    for k in range(1, K+1):
        T2 = ser_mul(T, T, K)
        acc = F(0)
        for j in range(1, k+1):
            if U[j] == 0: continue
            acc += j*U[j]*((1 if k-j == 0 else 0) + s*T2[k-j])
        T[k] = acc/k
    return T
class Cert:
    def __init__(self, m):
        self.m = [F(x) for x in m]; n = self.n = len(m)
        self.fr = Front(n); self.Linv = self.fr.Linv
        self.e = e_of_m(self.m); self.I = I_of_m(self.m)
        M, b = Mb(self.I, n); self.M = sp.Matrix(M); self.Mi = self.M.inv()
        self.absMi = [[F(str(abs(self.Mi[i, j]))) for j in range(n)] for i in range(n)]
        K = self.K = 2*n-3
        U = [F(0)]*(K+1)
        for l in range(1, n): U[2*l-1] = self.I[l]/(2*l-1)
        self.U = U
        T = tan_series(U, K, hyper=True)
        self.sech2 = [F(1)] + [F(0)]*K
        T2 = ser_mul(T, T, K)
        self.sech2 = [self.sech2[i] - T2[i] for i in range(K+1)]
        self.tanU = tan_series(U, K)
        tU2 = ser_mul(self.tanU, self.tanU, K)
        self.sec2U = [(1 if i == 0 else 0) + tU2[i] for i in range(K+1)]
        # G = -M^{-1} N L^{-1}
        syms = sp.symbols('x0:%d' % n)
        Ms, bs = Mb(list(syms), n)
        Fv = sp.Matrix(Ms)*sp.Matrix(self.e[1:]) - sp.Matrix(bs)
        N = Fv.jacobian(syms).subs(dict(zip(syms, self.I)))
        self.G = -self.Mi*N*self.Linv
        z = sp.symbols('z'); self.z = z
        self.pc = [sp.expand(sum((-1)**j*self.G[j-1, c]*z**(n-j) for j in range(1, n+1))) for c in range(n)]
    def bounds(self, rho):
        n, K, e = self.n, self.K, self.e
        bI = [sum(abs(F(str(self.Linv[r, c])))*rho[c] for c in range(n)) for r in range(n)]
        dU = [F(0)]*(K+1)
        for l in range(1, n): dU[2*l-1] = bI[l]/(2*l-1)
        lin = ser_mul([abs(x) for x in self.sech2], dU, K)
        UpdU = [self.U[i] + dU[i] for i in range(K+1)]
        tp = tan_series(UpdU, K)
        s2dU = ser_mul(self.sec2U, dU, K)
        rem = [tp[i] - self.tanU[i] - s2dU[i] for i in range(K+1)]
        dT = [lin[i] + rem[i] for i in range(K+1)]
        E_ = lambda i: e[i] if 0 <= i <= n else F(0)
        r = []; rr = []
        for j in range(n-1):
            r.append(sum(E_(k)*dT[2*j+1-k] for k in range(0, n+1, 2) if 2*j+1-k >= 1))
            rr.append(sum(E_(k)*rem[2*j+1-k] for k in range(0, n+1, 2) if 2*j+1-k >= 1))
        r.append(bI[0]*e[n]); rr.append(F(0))
        dM = [[F(0)]*n for _ in range(n)]
        for j in range(n-1):
            for k in range(2, n+1, 2):
                if 2*j+1-k >= 1: dM[j][k-1] = dT[2*j+1-k]
        dM[n-1][n-1] = bI[0]
        A = [[sum(self.absMi[i][l]*dM[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
        IA = sp.eye(n) - sp.Matrix(A)
        if IA.det() == 0: return None
        IAi = IA.inv()
        v = IAi*sp.ones(n, 1)
        if not all(x > 0 for x in v): return None
        Mr = [sum(self.absMi[i][l]*r[l] for l in range(n)) for i in range(n)]
        E = [F(str(x)) for x in IAi*sp.Matrix(Mr)]
        Mrr = [sum(self.absMi[i][l]*rr[l] for l in range(n)) for i in range(n)]
        AE = [sum(A[i][l]*E[l] for l in range(n)) for i in range(n)]
        varrho = [Mrr[i] + AE[i] for i in range(n)]
        return E, varrho
    RLIST = [F(k, 40) for k in range(20, 0, -1)] + [F(1, 100), F(1, 1000)]
    def test(self, delta, coherent):
        n = self.n; rho = [F(delta)]*n
        bd = self.bounds(rho)
        if bd is None: return False
        E, varrho = bd
        vals = sorted(set(self.m))
        for a in vals:
            ka = self.m.count(a); ok = False
            for r in self.RLIST:
                lhs = r**ka
                for b in vals:
                    if b != a: lhs *= (abs(a-b) - r)**self.m.count(b)
                if not coherent:
                    rhs = sum(E[j-1]*(a+r)**(n-j) for j in range(1, n+1))
                else:
                    rhs = sum(varrho[j-1]*(a+r)**(n-j) for j in range(1, n+1))
                    for c in range(n):
                        taylor = sp.Poly(sp.expand(self.pc[c].subs(self.z, self.z + sp.Rational(a.numerator, a.denominator))), self.z).all_coeffs()[::-1]
                        rhs += rho[c]*sum(abs(F(str(t)))*r**l for l, t in enumerate(taylor))
                if lhs > rhs: ok = True; break
            if not ok: return False
        return True
def best_delta(m, coherent, lo=1e-6, hi=2e-2, it=30):
    C = Cert(m)
    for _ in range(it):
        mid = (lo*hi)**0.5 if hi/lo > 4 else (lo+hi)/2
        if C.test(F(mid).limit_denominator(10**12), coherent): lo = mid
        else: hi = mid
    return lo
if __name__ == '__main__':
    import sys
    for m in [(2,8,8), (3,3,12), (3,10,15,30), (4,5,21,28)]:
        di = best_delta(m, False); dc = best_delta(m, True)
        print(m, 'componentwise (i): %.4e   coherent (ii): %.4e' % (di, dc), flush=True)
