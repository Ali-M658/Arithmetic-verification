"""Constants of Theorem S2: sigma_k(n), zeta_n, rho_n, kappa, Hadamard and closed-form bounds."""
from common import *
from fractions import Fraction as F
import numpy as np, math
w = sp.symbols('w')
_sig = {}
def sigma(n, K):
    if (n, K) not in _sig:
        ser = sp.series(sp.atanh(w)*sp.sec((n+1)*sp.atanh(w))**2, w, 0, K+1).removeO()
        _sig[(n, K)] = [sp.Rational(ser.coeff(w, k)) for k in range(K+1)]
    return _sig[(n, K)]
def zeta(n):
    s = sigma(n, 2*n)
    best = F(1)
    for j in range(n):
        tot = sum(F(str(s[2*i+1])) for i in range(j) if 2 <= 2*j-2*i <= n)
        best = max(best, tot)
    return best
def scaled(m):
    mu = max(m); mh = [F(x)/F(mu) for x in m]
    return mu, mh
def rho(m):
    n = len(m); mu, mh = scaled(m); eh = e_of_m(mh); s = sigma(n, 2*n)
    E = lambda i: eh[i] if 0 <= i <= n else 0
    best = eh[n]
    for j in range(n-1):
        best = max(best, sum(F(str(s[2*i+1]))*E(2*j-2*i) for i in range(j+1)))
    return best
def kappa(m):
    n = len(m); mu, mh = scaled(m)
    M, b = Mb(I_of_m(mh), n)
    Mi = sp.Matrix(M).inv()
    return max(sum(abs(Mi[i, j]) for j in range(n)) for i in range(n)), Mi
def kappa_bounds(m):
    n = len(m); mu, mh = scaled(m); eh = e_of_m(mh)
    E = lambda i: eh[i] if 0 <= i <= n else 0
    B = [[(-1)**(j+1)*E(2*k+1-j) for j in range(1, n+1)] for k in range(n)]
    Lam = np.prod([math.sqrt(sum(float(B[k][c])**2 for k in range(n))) for c in range(n)])
    Snorm = max(sum(float(E(k)) for k in range(0, n+1, 2) if k <= n-2+0 or True), float(eh[n]))
    # rows k<=n-2 of S: sum_{i<=k} e_{2(k-i)}; computed exactly
    rows = [sum(float(E(2*(k-i))) for i in range(k+1)) for k in range(n-1)] + [float(eh[n])]
    Snorm_exact = max(rows)
    orl = np.prod([float(mh[i]+mh[j]) for i in range(n) for j in range(i+1, n)])
    had = n*Lam*Snorm_exact/orl
    closed = n*math.comb(2*n, n)**(n/2)*2**(n-1)/orl
    return had, closed, Snorm_exact, Snorm
if __name__ == '__main__':
    print('sigma n=3', sigma(3, 5)[1::2], 'n=4', sigma(4, 7)[1::2])
    for n in range(2, 8): print('zeta', n, zeta(n))
    for m in [(2,8,8), (3,3,12), (3,10,15,30), (4,5,21,28), (2,2,2), (1,1,100), (2,3,3,7,9), (2,2,9,9,30,31)]:
        k, _ = kappa(m); had, closed, Se, Sclaim = kappa_bounds(m)
        print(m, 'kappa=%.4g rho=%.4g Had=%.4g closed=%.4g  ||S|| rows=%.4g claimed-formula=%.4g' % (float(k), float(rho(m)), had, closed, Se, Sclaim), 'kappa<=Had', float(k) <= had)
