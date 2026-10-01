"""DV.1(c), DV.2, DV.3, DV.4, DV.5.
Exact (Fraction) for every sign claim, every identity and the peeling arithmetic.
mpmath (60 digits) is used ONLY for labelled asymptotic sanity checks (rates and limits).
Run from repo root: python3 review/audit/curvature-divergence/check_divergence.py
"""
import os
import sys
from fractions import Fraction as F
from math import factorial

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp  # noqa: E402
from heatlib import beta, c_ucar, s_ucar, chi, heat_coeff  # noqa: E402

mp.mp.dps = 60
out = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    out.append(s)


def mpf(fr):
    return mp.mpf(fr.numerator) / fr.denominator


def sigma(m):
    return (mp.pi / m) / mp.sin(mp.pi / m)


def A(l, m):
    return mp.factorial(2 * l) / (mp.factorial(l) * m * mp.sin(mp.pi / m)) * (mp.mpf(m) / (2 * mp.pi)) ** (2 * l + 1)


# ---------------- DV.1(c): rate of the relative error (asymptotic sanity) ----------------
log('[asymptotic sanity] Lemma 1(c): r_l = (-1)^l g_{2l+2}/(2 sigma_k (k/2pi)^{2l+2}) - 1')
for k in [2, 3, 4, 5, 8]:
    rows = []
    for l in [10, 20, 30, 40]:
        # (-1)^l g_{2l+2} = c_l * 4k(l+1)!(2l+1)/(2l+2)!   (Lemma 1(a), verified exactly elsewhere)
        g = mpf(c_ucar(l, k)) * 4 * k * mp.factorial(l + 1) * (2 * l + 1) / mp.factorial(2 * l + 2)
        r = g / (2 * sigma(k) * (mp.mpf(k) / (2 * mp.pi)) ** (2 * l + 2)) - 1
        if k == 2:
            pred = mp.mpf(-3) * mp.mpf(9) ** (-(l + 1))           # pole of sech at x = 3 pi
        else:
            x1 = 4 * mp.pi / k                                     # pole of cot(kx/2) at 4pi/k
            pred = ((x1 / 2) / mp.sin(x1 / 2)) / sigma(k) * mp.mpf(4) ** (-(l + 1))
        rows.append((l, mp.nstr(r, 6), mp.nstr(r / pred, 12)))
        assert abs(r / pred - 1) < mp.mpf('0.02') * (1 if l > 10 else 10)
    log(f'  k={k}:', rows)
log('  => k>=3: r_l ~ [phi(4pi/k)/sigma_k] 4^{-(l+1)} (Theta(4^-l)); k=2: r_l ~ -3 * 9^{-(l+1)} (O(9^-l)), as claimed')

# ---------------- DV.2: Theorem 2 (asymptotic sanity) ----------------
log('[asymptotic sanity] Theorem 2: l^2 * (beta_l/A_l - 1 - pi^2/(2 m^2 (2l-1)))  and  p_l/(lambda_l m^{2l+2})')
for m in [2, 3, 5, 10]:
    rows = []
    for l in [20, 40, 80, 120]:
        q = mpf(beta(l, m)) / A(l, m)
        e2 = (q - 1 - mp.pi ** 2 / (2 * m * m * (2 * l - 1))) * l * l
        lam = abs(mp.bernoulli(2 * l + 2)) / (2 * mp.factorial(l + 1) * (2 * l + 1))
        ratio = m * mpf(beta(l, m)) / (lam * mp.mpf(m) ** (2 * l + 2))
        rows.append((l, mp.nstr(e2, 6), mp.nstr(ratio - sigma(m), 4)))
        assert abs(e2) < 2
    # next term: beta_l ~ sum_i A_{l-i}/(4^i i!); i=2 gives A_{l-2}/(32 A_l) = (1/32)(2pi^2/m^2)^2/((2l-1)(2l-3)) ~ pi^4/(32 m^4 l^2)
    pred = mp.pi ** 4 / (32 * m ** 4)
    log(f'  m={m} sigma={mp.nstr(sigma(m), 8)}', rows, ' predicted l^2-limit pi^4/(32 m^4) =', mp.nstr(pred, 6))
    assert abs(e2 / pred - 1) < 0.05
assert abs(sigma(2) - mp.pi / 2) < mp.mpf(10) ** -50
log('  sigma_2 = pi/2 (max), sigma_m decreasing to 1: x/sin x increasing on (0, pi/2]')

# ---------------- DV.3: Theorem 3 limits and the stated stress tests ----------------
def seq(K, g, orders, L):
    return [heat_coeff(l, K, g, orders) for l in range(L + 1)]


def est(a, l):
    """the three statistics of Theorem 3"""
    e1 = 2 * mp.pi ** 2 * abs(mpf(a[l])) / ((2 * l - 1) * abs(mpf(a[l - 1])))
    e2 = abs(mpf(a[l])) / (l * abs(mpf(a[l - 1])))
    return e1, e2


log('[asymptotic sanity] Theorem 3 statistics e1 -> M^2, e2 -> M^2/pi^2, mu-estimate -> mu')
cases = [(-1, 0, (2, 8, 8)), (-1, 0, (3, 3, 12)), (-1, 0, (3, 10, 15, 30)), (-1, 3, (2, 2, 7, 7, 7)),
         (-1, 1, (2,)), (1, 0, (2, 2)), (1, 0, (2, 2, 9)), (1, 0, (9, 9)), (1, 0, (2, 3, 5)), (-1, 2, (2, 2, 2, 2, 2)),
         (1, 0, (2, 2, 400)), (1, 0, (400, 400))]
for K, g, orders in cases:
    a = seq(K, g, orders, 100)
    M = max(orders)
    mu = orders.count(M)
    e1, e2 = est(a, 100)
    muhat = mpf(a[100]) / (mpf(F(K) ** 100) * A(100, M))
    log(f'  K={K:+d} g={g} {orders}: e1={mp.nstr(e1, 10)} (M^2={M * M}), e2*pi^2={mp.nstr(e2 * mp.pi ** 2, 8)}, mu_hat={mp.nstr(muhat, 8)} (mu={mu})')
    assert abs(e1 - M * M) < 0.01 and abs(muhat - mu) < 0.05 * mu
    # exact: a_l/K^l > 0 for all l >= some l0 (checked up to 100)
    l0 = max([l for l in range(101) if a[l] * F(K) ** l <= 0], default=-1) + 1
    assert l0 <= 20
# n = 0
log('  n = 0:')
for K, g in [(1, 0), (-1, 2), (-1, 7)]:
    a = seq(K, g, (), 200)
    for l in [50, 100, 200]:
        e1, e2 = est(a, l)
        log(f'    K={K:+d} g={g} l={l}: e1={mp.nstr(e1, 10)}  (e1-1)*l={mp.nstr((e1 - 1) * l, 6)}  e2*pi^2={mp.nstr(e2 * mp.pi ** 2, 8)}')
    # exact sign: a_l / K^l has sign K for every l (all l), so for K=-1 the transform coefficients are all negative
    assert all((a[l] * F(K) ** l > 0) == (K > 0) for l in range(201))
log('  n=0: e1 -> 1 with (e1-1) ~ 1/l, i.e. O(1/l) as claimed; with cones e1 - M^2 = O(1/l^2) (see the first block)')

# rate with cones: (e1 - M^2) * l^2 bounded
a = seq(-1, 0, (3, 3, 12), 200)
for l in [50, 100, 200]:
    e1, _ = est(a, l)
    log(f'    {{3,3,12}} l={l}: (e1-144)*l^2 = {mp.nstr((e1 - 144) * l * l, 8)}')

# stated test 1: 1000 x 49 + one 50
orders = (49,) * 1000 + (50,)
X = chi(0, orders)
a = []
C = abs(X) / 2
s_cache = [s_ucar(l + 1) for l in range(0, 401)]
b49 = [beta(l, 49) for l in range(401)]
b50 = [beta(l, 50) for l in range(401)]
for l in range(401):
    a.append(C * s_cache[l] * F(-1) ** (l + 1) + F(-1) ** l * (1000 * b49[l] + b50[l]))
log('  test 1000x49 + 50 (K=-1, genus 0): sqrt(e1) and sqrt(pi^2 e2) at selected l')
for l in [100, 150, 200, 250, 300, 400]:
    e1, e2 = est(a, l)
    log(f'    l={l}: sqrt(e1)={mp.nstr(mp.sqrt(e1), 8)}  sqrt(pi^2 e2)={mp.nstr(mp.sqrt(mp.pi ** 2 * e2), 8)}')
e1, e2 = est(a, 150)
assert round(float(mp.sqrt(e1))) == 49
crossing = next(l for l in range(1, 401) if round(float(mp.sqrt(est(a, l)[0]))) == 50)
log(f'    sqrt(e1) first rounds to 50 at l = {crossing}')

# stated test 2: genus 10^4 with one cone of order 2 (K = -1)
g = 10 ** 4
X = chi(g, (2,))
C = abs(X) / 2
signs = []
for l in range(0, 16):
    smooth = C * s_ucar(l + 1) * F(-1)  # a_l / K^l, smooth part
    cone = beta(l, 2)
    signs.append((l, '+' if smooth + cone > 0 else '-', 'smooth dominates' if abs(smooth) > cone else 'cone dominates'))
log('  test genus 10^4 + {2}: sign of a_l/K^l:', signs)
dom = [l for l, sg, d in signs if d == 'smooth dominates']
log(f'    smooth part dominates exactly for l in {dom}')
assert dom == list(range(9))  # statement says 'for l <= 5': true, but the crossover is at l = 9

# ---------------- DV.4: peeling, exact subtraction, from a tail only ----------------
def peel(K, g, orders, L, W):
    """Use only a_l for L <= l <= L+W. Returns recovered multiset, chi, genus."""
    a = {l: heat_coeff(l, K, g, orders) for l in range(L, L + W + 1)}
    found = []
    top = L + W
    while True:
        e1 =2 * mp.pi ** 2 * abs(mpf(a[top])) / ((2 * top - 1) * abs(mpf(a[top - 1])))
        Mhat = int(mp.nint(mp.sqrt(e1)))
        if Mhat == 1:
            break
        muhat = int(mp.nint(mpf(a[top]) / (mpf(F(K) ** top) * A(top, Mhat))))
        assert muhat >= 1
        found += [Mhat] * muhat
        for l in a:
            a[l] -= muhat * F(K) ** l * beta(l, Mhat)
    # remainder must be exactly C s_{l+1} K^{l+1} with one constant C > 0
    Cs = {a[l] / (s_ucar(l + 1) * F(K) ** (l + 1)) for l in a}
    assert len(Cs) == 1, 'remainder is not a pure smooth sequence'
    Cval = Cs.pop()
    assert Cval > 0
    Xr = K * 2 * Cval
    genus = (2 - Xr - sum(1 - F(1, m) for m in found)) / 2
    return sorted(found), Xr, genus


log('  Corollary 4 peeling from the window L <= l <= L+W only (no coefficient below L used):')
for K, g, orders, L, W in [(-1, 0, (2, 8, 8), 30, 60), (-1, 0, (3, 3, 12), 30, 60), (-1, 0, (3, 10, 15, 30), 40, 60),
                          (-1, 3, (2, 2, 7, 7, 7), 40, 80), (-1, 2, (), 40, 20), (1, 0, (2, 3, 5), 40, 80),
                          (1, 0, (9, 9), 40, 40), (1, 0, (2, 2, 9), 40, 60), (-1, 1, (2,), 40, 60), (1, 0, (), 40, 20)]:
    got, Xr, genus = peel(K, g, orders, L, W)
    assert got == sorted(orders) and Xr == chi(g, orders) and genus == g, (orders, got, Xr, genus)
    log(f'    K={K:+d} g={g} {orders}: recovered {tuple(got)}, chi={Xr}, genus={genus}, area=2pi*{abs(Xr)}')

# ---------------- DV.5: Borel radius and sign ----------------
log('[asymptotic sanity] DV.5: (a_l/l!)^(1/l) * pi^2/M^2 and a_l/(l a_{l-1}) * pi^2/M^2 (-> 1 and -> K)')
for K, g, orders in [(-1, 0, (3, 3, 12)), (1, 0, (2, 2, 9)), (-1, 2, ())]:
    a = seq(K, g, orders, 200)
    M = max(orders) if orders else 1
    for l in [100, 200]:
        root = mp.root(abs(mpf(a[l])) / mp.factorial(l), l) * mp.pi ** 2 / M ** 2
        rat = mpf(a[l]) / (l * mpf(a[l - 1])) * mp.pi ** 2 / M ** 2
        log(f'  K={K:+d} g={g} {orders} l={l}: root={mp.nstr(root, 6)}  ratio={mp.nstr(rat, 8)}')
log('  n=0, K=-1: every a_l/K^l < 0 (exact, above); Pringsheim still applies to -B, radius pi^2, singularity at zeta = K pi^2')

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check_divergence.txt'), 'w') as fh:
    fh.write('\n'.join(out) + '\nALL CHECKS PASSED\n')
print('ALL CHECKS PASSED')
