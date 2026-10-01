"""Independent implementation: heat coefficients, front end, Theorem B system, recovery."""
import pickle
from fractions import Fraction as F
import sympy as sp
import mpmath as mp
_d = pickle.load(open(__file__.replace('common.py', 'cone.pkl'), 'rb'))
ALPHA = _d['alpha']; PCONE = _d['p']
NUMAX = len(PCONE) - 1

def Lmat(N):
    """(N x N) L for H_{-1..N-2} in terms of I=(R,P1,..,P_{2N-3})."""
    L = [[F(0)]*N for _ in range(N)]
    L[0][0] = F(-1, 2)
    for nu in range(N-1):
        pi = PCONE[nu]; s = (-1)**nu
        L[nu+1][0] = -ALPHA[nu+1]/2 + s*pi[0]
        for k in range(1, nu+2):
            L[nu+1][k] = s*pi[k]
    return sp.Matrix(L)

def h0(n, N=None):
    N = N or n
    return sp.Matrix([F(n-2, 2)*ALPHA[j] for j in range(N)])

def I_of_m(m, N=None):
    n = len(m); N = N or n
    R = sum(1/x for x in m)
    return [R] + [sum(x**(2*l-1) for x in m) for l in range(1, N)]

def H_cone(m, N=None):
    """Direct cone-by-cone evaluation, exact for rational m."""
    n = len(m); N = N or n
    R = sum(F(1)/F(x) for x in m)
    A = F(n-2)/2 - R/2
    H = [A]
    for nu in range(N-1):
        H.append(A*ALPHA[nu+1] + sum((-1)**nu*sum(c*F(x)**(2*k) for k, c in enumerate(PCONE[nu]))/F(x) for x in m))
    return H

def e_of_m(m):
    n = len(m); e = [F(1)] + [F(0)]*n
    for x in m:
        for k in range(n, 0, -1):
            e[k] += e[k-1]*x
    return e

def I_of_e(e, N=None):
    """I from e (e[0]=1) via Newton; R=e_{n-1}/e_n.  Works for any ring elements."""
    n = len(e)-1; N = N or n
    K = 2*N-3
    # power sums p_k via Newton: p_k = (-1)^{k-1} k e_k + sum_{i=1}^{k-1} (-1)^{i-1} e_i p_{k-i}
    E = lambda i: e[i] if 0 <= i <= n else 0
    p = [None]*(K+1)
    for k in range(1, K+1):
        s = (-1)**(k-1)*k*E(k)
        for i in range(1, k):
            s += (-1)**(i-1)*E(i)*p[k-i]
        p[k] = s
    return [e[n-1]/e[n]] + [p[2*l-1] for l in range(1, N)]

def T_of_I(I, n):
    """Coefficients T_1..T_{2n-3} of tanh(U), U=sum P_k z^k/k (odd k). Returns dict k->T_k (list index)."""
    K = 2*n-3
    U = [0]*(K+1)
    for l in range(1, n):
        U[2*l-1] = I[l]/(2*l-1)
    # tanh via T' = U'(1-T^2): T_k = (1/k) sum_{j} j U_j [ (1-T^2) ]_{k-j}
    T = [0]*(K+1)
    T2 = [0]*(K+1)
    for k in range(1, K+1):
        s = 0
        for j in range(1, k+1):
            if U[j] == 0: continue
            c = (1 if k-j == 0 else 0) - T2[k-j]
            s += j*U[j]*c
        T[k] = s/k
        # update T2 up to k
        for kk in range(k, K+1):
            pass
        T2 = [sum(T[a]*T[b-a] for a in range(0, b+1)) for b in range(K+1)]
    return T

def Mb(I, n):
    T = T_of_I(I, n)
    M = [[0]*n for _ in range(n)]
    b = [0]*n
    for j in range(n-1):
        for k in range(1, n+1):
            v = 0
            if k == 2*j+1: v += 1
            if k % 2 == 0 and 2*j+1-k >= 1: v -= T[2*j+1-k]
            M[j][k-1] = v
        b[j] = T[2*j+1]
    M[n-1][n-2] = 1; M[n-1][n-1] = -I[0]
    return M, b

def recover_e(I, n, exact=False):
    M, b = Mb(I, n)
    if exact:
        sol = sp.Matrix(M).LUsolve(sp.Matrix(b))
        return [1] + list(sol)
    Mm = mp.matrix(M); bm = mp.matrix(b)
    sol = mp.lu_solve(Mm, bm)
    return [mp.mpf(1)] + [sol[i] for i in range(n)]

def roots_from_e(e):
    n = len(e)-1
    coeffs = [(-1)**j*e[j] for j in range(n+1)]
    return mp.polyroots(coeffs, maxsteps=500, extraprec=400)

class Front:
    def __init__(self, n):
        self.n = n
        self.L = Lmat(n); self.Linv = self.L.inv(); self.h0 = h0(n)
    def I_from_H(self, H):
        v = sp.Matrix(H) - self.h0
        return list(self.Linv*v)

def recover(H, n, front=None, dps=60):
    """Full recovery map from data H (list of mpf or Fraction). Returns roots."""
    front = front or Front(n)
    with mp.workdps(dps):
        Linv = mp.matrix([[mp.mpf(F(x).numerator)/F(x).denominator for x in row] for row in front.Linv.tolist()])
        h = [mp.mpf(F(x).numerator)/F(x).denominator for x in front.h0]
        Hv = mp.matrix([mp.mpf(H[i]) if not isinstance(H[i], F) else mp.mpf(H[i].numerator)/H[i].denominator for i in range(n)])
        I = Linv*(Hv - mp.matrix(h))
        I = [I[i] for i in range(n)]
        e = recover_e(I, n)
        return roots_from_e(e)

def rounds_ok(roots, m):
    xs = sorted(float(mp.re(z)) for z in roots)
    return [round(x) for x in xs] == sorted(m), max(abs(x-y) for x, y in zip(xs, sorted(m)))
