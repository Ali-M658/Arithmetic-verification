"""Exact checks backing COMPARISON.md. Run from repo root:
  python3 review/audit/curvature-divergence/check_comparison.py
"""
import os
import sys
from fractions import Fraction as F
from math import factorial

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy  # noqa: E402
from heatlib import beta, s_ucar, chi, heat_coeff  # noqa: E402

out = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    out.append(s)


x = sympy.symbols('x')
# 1. H(x) = (x/2)/sin(x/2) [(x/2)cot(x/2) - (kx/2)cot(kx/2)] is regular at x = 2 pi n (bracket vanishes there)
for k in [2, 3, 4, 5]:
    H = (x / 2) / sympy.sin(x / 2) * (x / 2 * sympy.cot(x / 2) - k * x / 2 * sympy.cot(k * x / 2))
    for n in [1, 2]:
        e = sympy.symbols('e')
        ser = sympy.series(H.subs(x, 2 * sympy.pi * n + e), e, 0, 1).removeO()
        assert all(ser.coeff(e, -j) == 0 for j in (1, 2)), (k, n, ser)
        br = (x / 2 * sympy.cot(x / 2) - k * x / 2 * sympy.cot(k * x / 2)).subs(x, 2 * sympy.pi * n + e)
        assert sympy.limit(br, e, 0) == 0
log('H regular at x = 2 pi n (n=1,2), bracket -> 0 there, k = 2..5: exact. (The existing proof is right; '
    'REVIEW.md DV.1(c) wrongly lists x = 2 pi n among the poles; no consequence.)')

# 2. values quoted in the divergence proof (D5)
assert heat_coeff(1, -1, 0, (2, 8, 8)) == F(-1601, 480)
assert heat_coeff(1, -1, 0, (3, 3, 12)) == F(-867, 160)
assert heat_coeff(0, -1, 0, (2, 8, 8)) == F(67, 48)
log('a_1(2,8,8) = -1601/480, a_1(3,3,12) = -867/160, a_0(2,8,8) = 67/48: reproduced exactly')

# 3. their iota formula for s_k equals (4.35)
def zeta_hurwitz_neg(nn, a):
    r = sympy.bernoulli(nn + 1, a)
    return -F(int(r.p), int(r.q)) / (nn + 1)


iota = [F(1)] + [F(2 * (-1) ** j, factorial(j)) * zeta_hurwitz_neg(1 + 2 * j, sympy.Rational(1, 2)) for j in range(60)]
for k in range(60):
    sk = sum(F(4) ** (i - k) / factorial(k - i) * iota[i] for i in range(k + 1))
    assert sk == s_ucar(k), k
log('s_k = sum_i 4^{i-k}/(k-i)! iota_i (divergence proof, Theorem 3) equals Ucar (4.35) s_k for k < 60: exact')

# 4. genus 10^4 + {2}: crossover, from the closed form G_2 = (t/2)^2 sech(t/2) (independent of (4.25))
t = sympy.symbols('t')
G2 = sympy.series((t / 2) ** 2 / sympy.cosh(t / 2), t, 0, 26).removeO()
c2 = [F((-1) ** l * factorial(2 * l + 2), 8 * factorial(l + 1) * (2 * l + 1)) * F(str(G2.coeff(t, 2 * l + 2))) for l in range(12)]
b2 = [sum(F(2, 4 ** i * factorial(i)) * c2[l - i] for i in range(l + 1)) for l in range(12)]
assert b2 == [beta(l, 2) for l in range(12)]
C = abs(chi(10 ** 4, (2,))) / 2
dom = [l for l in range(12) if C * s_ucar(l + 1) > b2[l]]
assert dom == list(range(9))
log('genus 10^4 + {2}: smooth part dominates exactly for l = 0..8 (both proof and its attack log say l <= 5)')

# 5. the fractional-part table of the curvature proof (12 a_0)
def a0(o):
    return chi(0, o) / 6 + sum(F(m * m - 1, 12 * m) for m in o)
assert 12 * a0(()) == 4
for n in range(2, 200):
    assert 12 * a0((n, n)) == 2 * n + F(2, n) and 12 * a0((2, 2, n)) == 3 + n + F(1, n)
assert [12 * a0(o) for o in [(2, 3, 3), (2, 3, 4), (2, 3, 5)]] == [7 + F(1, 6), 8 + F(1, 12), 9 + F(1, 30)]
log('curvature proof table of 12 a_0 reproduced exactly')

# 6. Part 4: number of interior sample points x = k/1000 on the level set sum 1/x_i = 10
cnt = 0
for kk in range(1, 1000):
    a = F(kk, 1000)
    s = 1 - a
    if 10 - 1 / a <= 0:
        continue
    disc = s * s - 4 * s / (10 - 1 / a)
    if disc > 0:
        cnt += 1
assert cnt == 299
log('Part 4: 299 sample points k/1000 with a strictly interior level-set fibre (matches F4)')

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check_comparison.txt'), 'w') as fh:
    fh.write('\n'.join(out) + '\nALL CHECKS PASSED\n')
print('ALL CHECKS PASSED')
