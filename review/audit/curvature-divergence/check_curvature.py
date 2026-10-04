"""CU.1-CU.3: exact checks.
  1. Lemma 2 (CU.2) against Molien's formula for C_n, D_n, T, O, I with exact character values.
  2. The full small-t expansion of sum N_l e^{-l(l+1)t} (Lemma 2 spectrum), computed exactly via
     Hurwitz zeta values, against Ucar (4.25)/(4.33)/(4.35) at every order up to t^24
     (this tests every cone order m <= 13 including m = 2, and the smooth part).
  3. Classification lists (Thurston 13.3.6) by enumeration; a_0 injectivity on the spherical class.
  4. Flat class: c_0 values; Kokotov's residue; Part 4 doubled triangles.
  5. Part 3 integer witnesses.
Run from repo root: python3 review/audit/curvature-divergence/check_curvature.py
"""
import os
import sys
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr
from math import factorial, floor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy  # noqa: E402
from heatlib import beta, s_ucar, bernpoly, chi, heat_coeff, exp_series, series_mul  # noqa: E402

out = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    out.append(s)


# ---------------- 1. Lemma 2 vs Molien ----------------
def lemma2(l, G, orders):
    return F(2 * l + 1, G) + F(1, 2) * sum(2 * (l // m) + 1 - F(2 * l + 1, m) for m in orders)


_cos = {}


def cos2pi(fr):
    fr = fr - floor(fr)
    if fr not in _cos:
        _cos[fr] = sympy.nsimplify(sympy.cos(2 * sympy.pi * sympy.Rational(fr.numerator, fr.denominator)))
    return _cos[fr]


def molien(l, classes, G):
    """dim of invariants in degree-l harmonics: (1/|G|) sum_g chi_l(g), chi_l(theta)=sum_{k=-l}^{l} e^{ik theta}.
    classes: list of (rotation angle / 2pi as Fraction, count)."""
    tot = sympy.Integer(2 * l + 1)  # identity
    for fr, cnt in classes:
        q = fr.denominator
        # sum_{k=-l}^{l} cos(2 pi k fr), grouped by residue of k mod q
        acc = 0
        for r in range(q):
            nk = sum(1 for k in range(-l, l + 1) if k % q == r)
            if nk:
                acc += nk * cos2pi(fr * r)
        tot += cnt * acc
    v = sympy.nsimplify(sympy.radsimp(sympy.expand(tot)))
    v = sympy.simplify(v)
    assert v.is_Rational, v
    return F(int(v.p), int(v.q)) / G


groups = {}
for n in range(2, 9):
    groups[f'C{n}'] = (n, [(F(j, n), 1) for j in range(1, n)], (n, n))
    groups[f'D{n}'] = (2 * n, [(F(j, n), 1) for j in range(1, n)] + [(F(1, 2), n)], (2, 2, n))
groups['T'] = (12, [(F(1, 3), 4), (F(2, 3), 4), (F(1, 2), 3)], (2, 3, 3))
groups['O'] = (24, [(F(1, 4), 3), (F(3, 4), 3), (F(1, 2), 3), (F(1, 3), 4), (F(2, 3), 4), (F(1, 2), 6)], (2, 3, 4))
groups['I'] = (60, [(F(j, 5), 6) for j in range(1, 5)] + [(F(1, 3), 10), (F(2, 3), 10), (F(1, 2), 15)], (2, 3, 5))
for name, (G, cl, orders) in groups.items():
    assert 1 + sum(c for _, c in cl) == G
    assert chi(0, orders) == F(2, G)
    for l in range(0, 41):
        a = lemma2(l, G, orders)
        b = molien(l, cl, G)
        assert a == b and a.denominator == 1 and a >= 0, (name, l, a, b)
log('CU.2 Lemma 2 = Molien count, exact, for C2..C8, D2..D8, T, O, I and l = 0..40')


# ---------------- 2. full expansion from the spectrum vs Ucar ----------------
NT = 25


def periodic_part_series(m):
    """sum_{l>=0} P_m(l) e^{-l(l+1)t}, P_m(l) = (1/2)(2 floor(l/m) + 1 - (2l+1)/m), as a power series in t.
    e^{-l(l+1)t} = e^{t/4} e^{-(l+1/2)^2 t}; l = m q + r; sum_q e^{-u (q+a)^2} with u = m^2 t, a = (r+1/2)/m
    ~ (1/2) sqrt(pi/u) + sum_j (-u)^j/j! * zeta(-2j, a),  zeta(-n, a) = -B_{n+1}(a)/(n+1)."""
    P = [F(1, 2) * (2 * (r // m) + 1 - F(2 * r + 1, m)) for r in range(m)]
    assert sum(P) == 0  # kills the t^{-1/2} term
    ser = []
    for j in range(NT):
        acc = F(0)
        for r in range(m):
            a = F(2 * r + 1, 2 * m)
            acc += P[r] * (-bernpoly(2 * j + 1, a) / (2 * j + 1))
        ser.append(F(-m * m) ** j / factorial(j) * acc)
    return series_mul(exp_series(F(1, 4), NT), ser, NT)


for m in range(2, 14):
    ps = periodic_part_series(m)
    for l in range(NT):
        assert ps[l] == beta(l, m), (m, l)
log(f'Cone series: spectral (Lemma 2 + Hurwitz) expansion = Ucar beta_l(m) (K=1) for m = 2..13, all l = 0..{NT - 1}; exact')

# whole-orbifold check for a few spherical orbifolds (smooth part via s_nu)
for orders in [(), (2, 2), (5, 5), (2, 2, 7), (2, 3, 3), (2, 3, 4), (2, 3, 5)]:
    X = chi(0, orders)
    for l in range(NT - 1):
        spec = X / 2 * s_ucar(l + 1) + sum(periodic_part_series(m)[l] for m in orders)
        assert spec == heat_coeff(l, 1, 0, orders)
log('Whole spherical orbifolds S^2, S^2(2,2), S^2(5,5), S^2(2,2,7), S^2(2,3,3/4/5): spectral expansion = (|chi|/2) s_{l+1} + sum beta_l, exact')

# ---------------- 3. classification and a_0 injectivity ----------------
# genus-0 orientable, chi > 0: sum(1-1/m) < 2 => n <= 3; enumerate orders <= 60 and check the pattern
sph = set()
for n in range(0, 4):
    for ms in cwr(range(2, 61), n):
        if chi(0, ms) > 0:
            sph.add(ms)
def is_listed(ms):
    if len(ms) <= 1:
        return True  # S^2 or teardrop (bad if n=1)
    if len(ms) == 2:
        return True
    a, b, c = ms
    return (a, b) == (2, 2) or ms in [(2, 3, 3), (2, 3, 4), (2, 3, 5)]
assert all(is_listed(ms) for ms in sph)
log('chi>0 genus-0 multisets with orders <= 60 are exactly: (), (n), (n1,n2), (2,2,n), (2,3,3), (2,3,4), (2,3,5)')

flat = set()
for n, top in [(0, 2), (1, 200), (2, 200), (3, 200), (4, 40), (5, 8)]:
    for ms in cwr(range(2, top), n):
        if chi(0, ms) == 0:
            flat.add(ms)
assert flat == {(2, 2, 2, 2), (3, 3, 3), (2, 4, 4), (2, 3, 6)}, flat
assert chi(1, ()) == 0 and all(chi(g, ()) < 0 for g in range(2, 5))
log('chi=0 closed orientable: T^2 and S^2(2,2,2,2), S^2(3,3,3), S^2(2,4,4), S^2(2,3,6) (orders < 200, n <= 5; n >= 5 gives sum >= 5/2)')


def a0(orders, g=0):
    return chi(g, orders) / 6 + sum(F(m * m - 1, 12 * m) for m in orders)


good_sph = {(): a0(())}
NMAX = 3000
for n in range(2, NMAX):
    good_sph[(n, n)] = a0((n, n))
    good_sph[(2, 2, n)] = a0((2, 2, n))
for ms in [(2, 3, 3), (2, 3, 4), (2, 3, 5)]:
    good_sph[ms] = a0(ms)
vals = {}
for ms, v in good_sph.items():
    assert v not in vals, (ms, vals.get(v))
    vals[v] = ms
# closed forms
for n in range(1, 50):
    assert a0((n, n)) == F(n * n + 1, 6 * n) and a0((2, 2, n)) == F(n * n + 1, 12 * n) + F(1, 4)
assert a0((2, 3, 3)) == F(43, 72) and a0((2, 3, 4)) == F(97, 144)  # DGGW Table 1
log(f'a_0 injective on good spherical class (n < {NMAX}); closed forms (n^2+1)/(6n), (n^2+1)/(12n)+1/4; DGGW Table 1 values 43/72, 97/144 reproduced')
# beyond NMAX: a_0(S^2(n,n)) >= n/6 > 1 and a_0(S^2(2,2,n)) >= n/12 > 1 exceed every platonic value; cross-family
# collisions reduce to p | n, n | 2p (see REVIEW.md) -> checked symbolically:
n_, p_ = sympy.symbols('n p', positive=True, integer=True)
eq = sympy.Eq((n_ ** 2 + 1) / (6 * n_), (p_ ** 2 + 1) / (12 * p_) + sympy.Rational(1, 4))
for sub in [p_, 2 * p_]:
    sols = sympy.solve(eq.subs(n_, sub), p_)
    assert all(s == 1 for s in sols), sols  # only p = 1 (S^2(2,2) = S^2(2,2,1)), i.e. the same orbifold
assert max(a0(ms) for ms in [(2, 3, 3), (2, 3, 4), (2, 3, 5)]) < 1
log('cross-family a_0 collisions: n=p or n=2p forced; only p=1 (S^2(2,2) itself). Platonic a_0 < 1.')
# sharpness: chi(S^2(2,2,n)) = chi(S^2(2n,2n)) = 1/n
for n in range(2, 100):
    assert chi(0, (2, 2, n)) == chi(0, (2 * n, 2 * n)) == F(1, n)
log('Part 2 sharpness pair chi(S^2(2,2,n)) = chi(S^2(2n,2n)) = 1/n: exact n = 2..99 (n=1 gives the same orbifold)')

# all higher spherical coefficients positive
for ms in [(), (2, 2), (9, 9), (2, 2, 9), (2, 3, 5)]:
    assert all(heat_coeff(l, 1, 0, ms) > 0 for l in range(40))
log('Part 2: spherical coefficients t^l, l=0..39, all > 0 for sample orbifolds')

# ---------------- 4. flat class ----------------
c0 = {'T2': a0((), 1), '2222': a0((2, 2, 2, 2)), '333': a0((3, 3, 3)), '244': a0((2, 4, 4)), '236': a0((2, 3, 6))}
assert list(c0.values()) == [0, F(1, 2), F(2, 3), F(3, 4), F(5, 6)]
log('Part 1 c_0 =', {k: str(v) for k, v in c0.items()})
# Kokotov Prop 1 residue: Res_{g=0} cot(pi g/b)/sin^2(g/2) = (2/3)(b/2pi - 2pi/b)
g, b = sympy.symbols('g b', positive=True)
res = sympy.residue(sympy.cot(sympy.pi * g / b) / sympy.sin(g / 2) ** 2, g, 0)
assert sympy.simplify(res - sympy.Rational(2, 3) * (b / (2 * sympy.pi) - 2 * sympy.pi / b)) == 0
# (1/16 pi i) * (negatively oriented circle) * residue => -(1/8pi)*... sign check: constant = (1/12)(2pi/b - b/2pi)
const = -sympy.Rational(1, 16) / (sympy.pi * sympy.I) * 2 * sympy.pi * sympy.I * res
assert sympy.simplify(const - sympy.Rational(1, 12) * (2 * sympy.pi / b - b / (2 * sympy.pi))) == 0
mm = sympy.symbols('m', positive=True)
assert sympy.simplify(const.subs(b, 2 * sympy.pi / mm) - (mm ** 2 - 1) / (12 * mm)) == 0
log('Kokotov (10): residue (2/3)(b/2pi - 2pi/b) and constant (1/12)(2pi/b - b/2pi) = (m^2-1)/(12m) at b = 2pi/m: exact')
# DGGW Lemma 5.4 / Prop 5.5 cross-check (high-precision sanity only; the exact statement is the residue above)
for m in range(2, 13):
    sm = sum(1 / (4 * sympy.sin(j * sympy.pi / m) ** 2) for j in range(1, m))
    val = sympy.nsimplify(sympy.N(sm, 60), rational=True)
    assert val == sympy.Rational(m * m - 1, 12)
    assert abs(sympy.N(sm - sympy.Rational(m * m - 1, 12), 80)) < 1e-70
log('sum_{j<m} 1/(4 sin^2(j pi/m)) = (m^2-1)/12 for m=2..12 (80-digit sanity check, DGGW Prop 5.5)')

# Part 4: doubled triangles. Heat data = area and sum (1/alpha_i - alpha_i) with angles pi alpha_i, sum alpha = 1
def tri_c0(al):
    return F(1, 12) * sum(1 / a - a for a in al)
A = (F(1, 4), F(1, 4), F(1, 2))
B = (F(1, 5), F(2, 5), F(2, 5))
assert tri_c0(A) == tri_c0(B) == a0((2, 4, 4)) == F(3, 4)
log('Part 4: doubled (1/4,1/4,1/2) and (1/5,2/5,2/5) both have t^0 coefficient 3/4 (= S^2(2,4,4))')
# one-parameter family on the level set sum 1/alpha = 10: alpha_1 = a free, alpha_2,3 roots of
# z^2 - s z + s/(10 - 1/a) with s = 1 - a; real & positive iff discriminant >= 0
a = sympy.symbols('a', positive=True)
s = 1 - a
disc = s ** 2 - 4 * s / (10 - 1 / a)
ivl = sympy.solve_univariate_inequality(disc >= 0, a, relational=False).intersect(sympy.Interval.open(sympy.Rational(1, 10), 1))
log('  level set sum(1/alpha)=10: alpha_1 ranges over', ivl)
assert ivl.measure > 0
# equilateral: unique minimiser of sum 1/alpha (=9); every c>9 gives a curve
assert sum(1 / x for x in (F(1, 3),) * 3) == 9

# ---------------- 5. Part 3 integer witnesses ----------------
def first_diff(o1, o2, K=-1, L=8):
    for l in range(-1, L):
        if heat_coeff(l, K, 0, o1) != heat_coeff(l, K, 0, o2):
            return l
    return None
assert first_diff((2, 8, 8), (3, 3, 12)) == 1  # agree at t^{-1}, t^0; differ at t^1 => need 3 coefficients
assert first_diff((3, 10, 15, 30), (4, 5, 21, 28)) == 2  # agree at t^{-1}, t^0, t^1 => need 4
log('Part 3 witnesses: {2,8,8}/{3,3,12} first differ at t^1 (k=3 coeffs needed); {3,10,15,30}/{4,5,21,28} first differ at t^2 (k=4)')

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check_curvature.txt'), 'w') as fh:
    fh.write('\n'.join(out) + '\nALL CHECKS PASSED\n')
print('ALL CHECKS PASSED')
