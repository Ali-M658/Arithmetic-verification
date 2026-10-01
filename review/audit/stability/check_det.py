"""ST.3 (Lemma S2.1) and ST.4 (Lemma S2.2): exact checks for n = 2..10.
Run from repo root: python3 review/audit/stability/check_det.py"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stab_lib import *
import sympy as sp

out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

def B_mat(e, n):
    g = lambda i: e[i] if 0 <= i <= n else F(0)
    return [[(-1) ** (j + 1) * g(2 * k + 1 - j) for j in range(1, n + 1)] for k in range(n)]

def S_mat(e, n):
    g = lambda i: e[i] if 0 <= i <= n else F(0)
    S = [[F(0)] * n for _ in range(n)]
    for k in range(n - 1):
        for i in range(k + 1):
            S[k][i] = g(2 * (k - i))
    S[n - 1][n - 1] = (-1) ** n * e[n]
    return S

def W_coeffs(e, d, n):
    """coefficients in w of W_D = (E_f O_D - E_D O_f)/z, D = sum_{k>=1} d_k z^k."""
    f = e + [F(0)] * 2
    D = [F(0)] + list(d) + [F(0)] * 2
    N = 2 * n + 2
    Ef = [f[i] if i % 2 == 0 and i <= n else F(0) for i in range(N)]
    Of = [f[i] if i % 2 == 1 and i <= n else F(0) for i in range(N)]
    ED = [D[i] if i % 2 == 0 and i <= n else F(0) for i in range(N)]
    OD = [D[i] if i % 2 == 1 and i <= n else F(0) for i in range(N)]
    X = [a - b for a, b in zip(ps_mul(Ef, OD, N - 1), ps_mul(ED, Of, N - 1))]
    assert all(X[i] == 0 for i in range(0, N, 2))
    assert all(X[i] == 0 for i in range(2 * n + 1, N))
    return [X[2 * k + 1] for k in range(n)]

random.seed(1)
for n in range(2, 11):
    cn = (-1) ** (n * (n + 1) // 2)
    trials = 0
    cases = []
    for t in range(6):
        cases.append([F(random.randint(1, 60), random.randint(1, 7)) for _ in range(n)])
    cases.append([F(1)] * n)
    cases.append([F(k) for k in range(1, n + 1)])
    cases.append([F(2)] * (n - 1) + [F(3)])
    for m in cases:
        I = invariants(m)
        M, b = M_b(I, n)
        e = esym(m)
        # Theorem B black box: true e solves M e = b
        assert matvec(M, e[1:]) == b
        prod = F(1)
        for i in range(n):
            for j in range(i + 1, n):
                prod *= m[i] + m[j]
        dM = det(M)
        assert dM == cn * prod / e[n], (n, m, dM, cn * prod / e[n])
        # Lemma S2.2
        B = B_mat(e, n); S = S_mat(e, n)
        assert matmul(S, M) == B
        assert det(B) == (-1) ** (n * (n - 1) // 2) * prod
        assert det(S) == (-1) ** n * e[n]
        Mi = inv(M)
        assert Mi == matmul(inv(B), S)
        # B is the map d -> W_D
        d = [F(random.randint(-9, 9), random.randint(1, 5)) for _ in range(n)]
        assert W_coeffs(e, d, n) == matvec(B, d)
        trials += 1
    log('n=%2d: c_n = %+d, det M, B = S M, det B, det S, M^-1 = B^-1 S verified on %d exact cases'
        % (n, cn, trials))

# ST.0 weighted homogeneity: M(I^) = D_r^{-1} M(I) D_c, and e^ solves M(I^) e^ = b(I^)
for n in range(2, 8):
    m = [F(random.randint(1, 50)) for _ in range(n)]
    mu = max(m)
    M, b = M_b(invariants(m), n)
    Mh, bh = M_b(invariants([x / mu for x in m]), n)
    wr = [2 * j + 1 for j in range(n - 1)] + [n - 1]
    for j in range(n):
        assert bh[j] == b[j] / mu ** wr[j]
        for k in range(1, n + 1):
            assert Mh[j][k - 1] == M[j][k - 1] * mu ** k / mu ** wr[j]
    eh = esym([x / mu for x in m])
    assert matvec(Mh, eh[1:]) == bh
log('ST.0 weighted homogeneity M(I^) = D_r^-1 M(I) D_c (row weights 2j+1, n-1; column weights k): OK n=2..7')

# symbolic identity det B = (-1)^{n(n-1)/2} prod(m_i+m_j) for n <= 5 (polynomial identity in m)
for n in range(2, 6):
    ms = sp.symbols('m1:%d' % (n + 1)); z = sp.Symbol('z')
    P = sp.Poly(sp.prod([1 + x * z for x in ms]), z)
    ecoef = [P.coeff_monomial(z ** i) for i in range(n + 1)]
    g = lambda i: ecoef[i] if 0 <= i <= n else 0
    Bs = sp.Matrix(n, n, lambda k, j: (-1) ** (j + 2) * g(2 * k + 1 - (j + 1)))
    lhs = sp.Poly(Bs.det(method='berkowitz'), *ms)
    rhs = sp.Poly((-1) ** (n * (n - 1) // 2) * sp.prod([ms[i] + ms[j] for i in range(n) for j in range(i + 1, n)]), *ms)
    assert lhs == rhs
    log('n=%d: det B = (-1)^{n(n-1)/2} prod(m_i+m_j) as a polynomial identity (sympy)' % n)

# weight count used in the proof: total weight of det B = n(n-1)/2
for n in range(2, 30):
    assert sum(2 * k + 1 for k in range(n)) - sum(range(1, n + 1)) == n * (n - 1) // 2
log('weight of det B equals deg prod(m_i+m_j) = n(n-1)/2: OK')

open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check_det.txt'), 'w').write('\n'.join(out) + '\nALL CHECKS PASSED\n')
print('ALL CHECKS PASSED')
