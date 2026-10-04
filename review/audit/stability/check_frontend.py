"""ST.0-ST.2: Ucar coefficients, Proposition S1 (matrix L), front-end tables.
Run from repo root: python3 review/audit/stability/check_frontend.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stab_lib import *
import mpmath as mp

out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

# --- smooth coefficients (4.35), K=-1
alist = [alpha(j) for j in range(5)]
assert alist == [1, F(-1, 3), F(1, 15), F(-4, 315), F(1, 315)], alist
log('alpha_0..4 =', [str(x) for x in alist], 'OK (matches ST.0)')

# --- cone coefficients: b_nu(m) = (-1)^nu p_nu(m)/m, p_nu even, deg 2nu+2, p_nu(1)=0
for nu in range(8):
    pi = PI(nu)
    assert len(pi) == nu + 2 and pi[-1] != 0
    assert sum(pi) == 0, nu  # p_nu(1) = 0
    for mm in range(1, 12):
        assert F(mm) * cone_b(nu, mm) == (-1) ** nu * sum(pi[k] * F(mm) ** (2 * k) for k in range(nu + 2))
log('b_0(m) = (m^2-1)/(12m):', all(cone_b(0, k) == F(k * k - 1, 12 * k) for k in range(1, 30)))
assert all(cone_b(0, k) == F(k * k - 1, 12 * k) for k in range(1, 30))
log('p_nu coefficients pi_{nu,k} (nu=0..3):')
for nu in range(4):
    log('  nu=%d:' % nu, [str(x) for x in PI(nu)])

# --- independent transcription check (kappa=+1): S^2/Z_k football, two cone points of order k.
# Spectrum: l(l+1) with multiplicity 2*floor(l/k)+1.  Z = 2A + 2C (Ucar, after Cor 4.19).
# Numerical sanity check only (not a certificate): residual after J terms must be O(t^J).
mp.mp.dps = 60
def Z_football(k, t):
    return mp.nsum(lambda l: (2 * mp.floor(l / k) + 1) * mp.e ** (-l * (l + 1) * t), [0, mp.inf])
for k in (2, 3, 5):
    ratios = []
    for t in (mp.mpf('0.0004'), mp.mpf('0.0002')):
        J = 5
        approx = mp.mpf(0)
        for j in range(J + 1):
            a = alpha(j, kappa=1)
            approx += mp.mpf(a.numerator) / a.denominator * (mp.mpf(1) / k) * t ** (j - 1)  # (vol/4pi) alpha_j t^{j-1}, vol=4pi/k
        for nu in range(J):
            b = cone_b(nu, k, kappa=1)
            approx += 2 * mp.mpf(b.numerator) / b.denominator * t ** nu
        resid = Z_football(k, t) - approx
        log('  football k=%d t=%s residual/t^%d = %s' % (k, t, J, mp.nstr(resid / t ** J, 8)))
        ratios.append(resid / t ** J)
    # residual is O(t^J): resid/t^J stabilises (next-order coefficient), so terms t^-1..t^{J-1} are right
    assert abs(ratios[0] / ratios[1] - 1) < mp.mpf('0.02'), ratios

# --- Proposition S1: L lower-triangular, independent of n, H = L I + h0
for n in range(2, 9):
    L = L_matrix(n)
    assert all(L[i][j] == 0 for i in range(n) for j in range(i + 1, n))
    assert L == [row[:n] for row in L_matrix(9)[:n]]
    for _ in range(6):
        import random
        random.seed(n * 100 + _)
        m = [random.randint(2, 40) for _ in range(n)]
        assert heat_direct(m) == heat_from_I(invariants(m), n)
        mq = [F(random.randint(2, 400), random.randint(1, 9)) for _ in range(n)]
        assert heat_direct(mq) == heat_from_I(invariants(mq), n)
    # diagonal formula
    for nu in range(n - 1):
        claimed = F((-1) ** nu) * abs(bern(2 * nu + 2)) / (2 * factorial(nu + 1) * (2 * nu + 1))
        assert L[nu + 1][nu + 1] == claimed, (nu, L[nu + 1][nu + 1], claimed)
    assert h0(n) == [F(n - 2, 2)] + [F(n - 2, 2) * alpha(j) for j in range(1, n)]
log('Prop S1: L lower triangular, n-independent, H = L I + h0 exactly, diagonal formula: OK (n=2..8)')

# --- ST.2 tables
n = 8
Li = inv(L_matrix(n))
rows_claim = {0: [-2], 1: [2, 12], 2: [-18, -120, -360], 3: [30, 252, 1260, 2520],
              4: [F(-70, 3), -240, -1680, -6720, -10080]}
for r, v in rows_claim.items():
    assert Li[r][:r + 1] == [F(x) for x in v], (r, Li[r])
diag_claim = [2, 12, 360, 2520, 10080, 28512, F(43243200, 691), 112320]
ell_claim = [2, 14, 498, 4062, F(56230, 3), F(303654, 5), F(104899830, 691), F(10805786, 35)]
diag = [1 / abs(L_matrix(n)[r][r]) for r in range(n)]
ell = [sum(abs(x) for x in Li[r]) for r in range(n)]
log('diag 1/|L_rr|:', [str(x) for x in diag])
log('ell_r       :', [str(x) for x in ell])
assert diag == [F(x) for x in diag_claim]
assert ell == [F(x) for x in ell_claim]
assert all(Li[r][r] == 1 / L_matrix(n)[r][r] for r in range(n))
log('ST.2 L^{-1} rows, diagonal and row sums: all match')
log('ratios ell/diag for P1,P3,P5:', [str(ell[r] / diag[r]) for r in (1, 2, 3)],
    '~', [round(float(ell[r] / diag[r]), 3) for r in (1, 2, 3)])

# kappa_r ratios on the table multisets
TABLE = [(2, 8, 8), (3, 3, 12), (3, 10, 15, 30), (4, 5, 21, 28), (2, 3, 7), (4, 4, 4), (7, 7, 7),
         (3, 3, 4, 4), (5, 5, 5, 5), (2, 2, 2, 3), (2, 2, 2, 2, 3)]
lo, hi = 10.0, 0.0
for m in TABLE:
    n = len(m)
    Li = inv(L_matrix(n)); H = heat_direct(m); I = invariants(m)
    kap = [sum(abs(Li[r][c]) * abs(H[c]) for c in range(n)) / abs(I[r]) for r in range(n)]
    lo = min(lo, min(map(float, kap))); hi = max(hi, max(map(float, kap)))
    log('  kappa_r', m, [round(float(x), 3) for x in kap])
    if m == (2, 8, 8):
        assert [round(float(x), 2) for x in kap] == [0.33, 0.94, 1.33]
log('kappa_r range over the 11 table multisets: [%.3f, %.3f]' % (lo, hi))

open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check_frontend.txt'), 'w').write('\n'.join(out) + '\nALL CHECKS PASSED\n')
print('ALL CHECKS PASSED')
