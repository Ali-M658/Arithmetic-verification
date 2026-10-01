"""ST.5 Theorem S2: constants sigma_k(n), zeta_n, rho_n; the majorant |dT_k| <= sigma_k eta;
conclusion (b) on exact random perturbations (including eta = 1 and beta = 1/2 edges);
conclusion (a) (Hadamard bound) exactly, using squared norms.
Run from repo root: python3 review/audit/stability/check_s2.py"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s5_lib import *

HERE = os.path.dirname(os.path.abspath(__file__))
out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

# ---- constants
for n in range(2, 9):
    s = sigma_series(n, 2 * n)
    assert s[1] == 1 and s[3] == F(1, 3) + (n + 1) ** 2
assert sigma_series(3, 6)[1:4:2] == (1, F(49, 3))
assert sigma_series(4, 8)[1:6:2] == (1, F(76, 3), F(6628, 15))
def zeta(n):
    s = sigma_series(n, 2 * n)
    z = F(1)
    for j in range(n - 1):
        z = max(z, sum(s[2 * i + 1] for i in range(j) if 2 <= 2 * j - 2 * i <= n))
    return z
assert zeta(3) == 1 and zeta(4) == F(79, 3) and zeta(5) == F(14048, 15)
log('sigma_1 = 1, sigma_3 = 1/3+(n+1)^2 (n=2..8); n=3: (1,49/3); n=4: (1,76/3,6628/15); zeta_3=1, zeta_4=79/3, zeta_5=14048/15: OK')
log('zeta_n for n=2..8:', [str(zeta(n)) for n in range(2, 9)])

def scalefree(m):
    mu = F(max(m))
    return [F(x) / mu for x in m], mu

def T_hat(Ih, n):
    return T_series(Ih, n)

# ---- majorant and conclusion (b)
random.seed(3)
cnt_b = cnt_T = 0
worst_T = F(0); worst_b = F(0)
for trial in range(400):
    n = random.choice([2, 3, 3, 4, 4, 5])
    kind = trial % 4
    if kind == 0:
        m = [F(random.randint(1, 40)) for _ in range(n)]
    elif kind == 1:  # repeated orders / clusters
        a = random.randint(2, 9); m = [F(a)] * (n - 1) + [F(random.randint(1, 30))]
    elif kind == 2:  # large ratios, order 1
        m = [F(1)] + [F(random.choice([1, 2, 1000, 10 ** 6])) for _ in range(n - 1)]
    else:
        m = [F(random.randint(1, 10 ** 4), random.randint(1, 50)) for _ in range(n)]
    mh, mu = scalefree(m)
    Ih = invariants(mh)
    eh = esym(mh)
    s = sigma_series(n, 2 * n)
    eta = F(1) if trial % 5 == 0 else F(random.randint(1, 10 ** 6), 10 ** 6)
    # perturbation of the scale-free invariants, |d| <= eta componentwise (corners included)
    d = [eta * (random.choice([-1, 1]) if trial % 3 else F(random.randint(-1000, 1000), 1000)) for _ in range(n)]
    It = [x + y for x, y in zip(Ih, d)]
    T0 = T_hat(Ih, n); T1 = T_hat(It, n)
    for k in range(1, 2 * n - 2, 2):
        assert abs(T1[k] - T0[k]) <= s[k] * eta, (m, k)
        if s[k] * eta:
            worst_T = max(worst_T, abs(T1[k] - T0[k]) / (s[k] * eta))
        cnt_T += 1
    M, _ = M_b(Ih, n)
    kappa = max(sum(abs(x) for x in row) for row in inv(M))
    g = lambda i: eh[i] if 0 <= i <= n else F(0)
    rho = max([eh[n]] + [sum(s[2 * i + 1] * g(2 * j - 2 * i) for i in range(j + 1)) for j in range(n - 1)])
    z = zeta(n)
    # scale eta down so that beta = kappa*zeta*eta <= 1/2 (edge: exactly 1/2)
    eta_b = min(eta, 1 / (2 * kappa * z))
    db = [x * eta_b / eta for x in d]
    It = [x + y for x, y in zip(Ih, db)]
    Mt, bt = M_b(It, n)
    et = solve(Mt, bt)
    err = max(abs(x - y) for x, y in zip(et, eh[1:]))
    assert err <= 2 * kappa * rho * eta_b, (m, err)
    worst_b = max(worst_b, err / (2 * kappa * rho * eta_b))
    cnt_b += 1
    # conclusion (a): kappa <= n Lambda ||S|| / prod  and the explicit bound; compared via squares
    prod = F(1)
    for i in range(n):
        for j in range(i + 1, n):
            prod *= mh[i] + mh[j]
    B = [[(-1) ** (j + 1) * g(2 * k + 1 - j) for j in range(1, n + 1)] for k in range(n)]
    colsq = [sum(B[k][c] ** 2 for k in range(n)) for c in range(n)]
    assert all(x >= 1 for x in colsq)  # every column of B(e^) has norm >= 1 (used for cofactors)
    Lam2 = F(1)
    for x in colsq:
        Lam2 *= x
    Snorm = max([sum(g(2 * (k - i)) for i in range(k + 1)) for k in range(n - 1)] + [eh[n]])
    assert Snorm <= max(sum(g(k) for k in range(0, n + 1, 2)), eh[n])
    lhs = kappa * prod / (n * Snorm)
    assert lhs >= 0 and lhs ** 2 <= Lam2
    assert Lam2 <= F(comb(2 * n, n)) ** n
    assert Snorm <= 2 ** (n - 1)
log('|dT_k| <= sigma_k(n) eta on %d coefficient checks (max ratio %.4f)' % (cnt_T, float(worst_T)))
log('(b) max|e~-e^| <= 2 kappa rho eta on %d perturbations at beta <= 1/2 (max ratio %.4f)' % (cnt_b, float(worst_b)))
log('(a) Hadamard chain kappa <= n Lambda ||S|| / prod <= n binom(2n,n)^{n/2} 2^{n-1} / prod verified exactly on all cases')

open(os.path.join(HERE, 'check_s2.txt'), 'w').write('\n'.join(out) + '\nALL CHECKS PASSED\n')
print('ALL CHECKS PASSED')
