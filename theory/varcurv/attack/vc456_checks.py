"""
Exact checks for VC4, VC5, VC6 (the parts that are finite computations), using the
independently computed b_l (twisted_duhamel_output.txt) and exact Pi_i polynomials.
"""
import re
import itertools
import sympy as sp
from fractions import Fraction as Fr

here = __file__.rsplit('/', 1)[0]
X, m = sp.symbols('X m')
k = sp.symbols('k0:6')
txt = open(here + '/twisted_duhamel_output.txt').read()
b = {}
for line in txt.splitlines():
    mm = re.match(r'b_(\d+) = (.*)', line)
    if mm:
        b[int(mm.group(1))] = sp.sympify(mm.group(2), locals={'X': X, **{'k%d' % i: k[i] for i in range(6)}})
inv = sp.sympify(re.search(r"invariants: (\{.*\})", txt).group(1).replace("'", '"'),
                 locals={'k%d' % i: k[i] for i in range(6)})
inv = {str(a): v for a, v in inv.items()}
LM = max(b)

# exact m*Pi_i polynomials: interpolate from exact values (cycle-Laplacian method, as in vc_checks.py)
def Pi_exact(i, mm):
    if mm == 1:
        return sp.Integer(0)
    L = sp.zeros(mm, mm)
    for a in range(mm):
        L[a, a] += 2
        L[a, (a + 1) % mm] -= 1
        L[a, (a - 1) % mm] -= 1
    Minv = (L + sp.ones(mm, mm) / mm).inv()
    return ((Minv ** i).trace() - 1) / mm


IM = LM + 1
Pi = {}
for i in range(1, IM + 1):
    pts = [(mm, mm * Pi_exact(i, mm)) for mm in range(1, 2 * i + 3)]
    poly = sp.expand(sp.interpolate(pts[:-1], m))
    assert poly.subs(m, pts[-1][0]) == pts[-1][1]
    Pi[i] = sp.cancel(poly / m)

# ---------------------------------------------------------------- Pi_i in the Psi basis
# psi_k(m) := m^{2k-1} - 1/m ; claim: Pi_i in span{psi_1..psi_i}, coefficient of psi_i = |B_2i|/(2i)!
psi = {kk: m**(2 * kk - 1) - 1 / m for kk in range(1, IM + 2)}
def to_psi(expr):
    P = sp.Poly(sp.expand(expr * m), m)
    coeffs = {}
    for (e,), cf in P.terms():
        assert e % 2 == 0
        if e > 0:
            coeffs[e // 2] = cf
    rest = sp.expand(expr - sum(cf * psi[kk] for kk, cf in coeffs.items()))
    assert rest == 0, rest
    return coeffs

for i in range(1, IM + 1):
    c = to_psi(Pi[i])
    assert max(c) == i and c[i] == abs(sp.bernoulli(2 * i)) / sp.factorial(2 * i)
print('Pi_i(m) = sum_{k<=i} c_{ik} (m^{2k-1} - 1/m), c_ii = |B_2i|/(2i)! != 0, i=1..%d' % IM)

# ---------------------------------------------------------------- VC5: a_0
gam = sp.symbols('gamma')
a0_point = sp.simplify(-(1 - 1 / m) / 6 + Pi[1])
assert sp.simplify(a0_point - (m - 1)**2 / (12 * m)) == 0
print('VC5: a_0 = chi^orb/6 + sum Pi_1(m_i) = (2-2gamma)/6 + sum (m_i-1)^2/(12 m_i)  [DGGW (5.7) + Gauss-Bonnet]: OK')
f0 = lambda g, ms: Fr(2 - 2 * g, 6) + sum(Fr((x - 1)**2, 12 * x) for x in ms)
assert f0(0, [2] * 8) == f0(0, [3, 3, 3]) == Fr(2, 3)
print('VC5 example: a_0(S^2(2^8)) = a_0(S^2(3,3,3)) = 2/3: OK')

# ---------------------------------------------------------------- VC4
kap = sp.symbols('kappa')
# constant-curvature cone contribution a_l(m) = sum_i beta^kappa_{l,i} Pi_i(m)
def a_cone(l, jet):
    P = sp.Poly(b[l].subs(jet), X)
    return sp.expand(sum(cf * Pi[e] for (e,), cf in P.terms()))

const = {k[0]: kap, **{k[i]: 0 for i in range(1, 6)}}
for l in range(LM + 1):
    c = to_psi(a_cone(l, const))
    assert max(c) == l + 1
    assert sp.simplify(c[l + 1] - kap**l * sp.factorial(2 * l) / sp.factorial(l) * abs(sp.bernoulli(2 * l + 2)) / sp.factorial(2 * l + 2)) == 0
print('VC4: at constant curvature, a_l(p) = sum_{k<=l+1} e_{lk} kappa^l psi_k(m), e_{l,l+1} = (2l)!/l! |B_{2l+2}|/(2l+2)! != 0 (l=0..%d)' % LM)

# brute force: the iff for L = 2..LM+2, over multisets (genus 0, m_i in 2..9, n <= 4), kappa = 1 and kappa = -1
def a_sum(l, ms, jet):
    expr = a_cone(l, jet)
    return sum(sp.Rational(expr.subs(m, x)) for x in ms)

def Psi(kk, ms):
    return sum(Fr(x**(2 * kk - 1)) - Fr(1, x) for x in ms)

def chi(ms):
    return 2 - sum(1 - Fr(1, x) for x in ms)

sigs = []
for n in range(0, 5):
    sigs += list(itertools.combinations_with_replacement(range(2, 10), n))
print('VC4 brute force over %d genus-0 signatures' % len(sigs))
for kv in (1, -1):
    jet = {k[0]: kv, **{k[i]: 0 for i in range(1, 6)}}
    acache = {}
    for ms in sigs:
        acache[ms] = tuple(a_sum(l, ms, jet) for l in range(LM + 1))
    # group by chi^orb (S_0 equal forces chi^orb equal)
    from collections import defaultdict
    by_chi = defaultdict(list)
    for ms in sigs:
        by_chi[chi(ms)].append(ms)
    npairs = 0
    for L in range(2, LM + 3):
        for grp in by_chi.values():
            for s1, s2 in itertools.combinations(grp, 2):
                lhs = all(acache[s1][l] == acache[s2][l] for l in range(0, L - 1))
                rhs = all(Psi(kk, s1) == Psi(kk, s2) for kk in range(1, L))
                assert lhs == rhs, (kv, L, s1, s2)
                npairs += 1
    print('VC4 iff (kappa=%d): verified for L=2..%d on %d (pair, L) instances' % (kv, LM + 2, npairs))

# J-version (L <= 5): common generic jet J = (K, DK, D2K) at all cone points
jetJ = {k[0]: sp.Rational(3, 7), k[1]: sp.Rational(-2, 5), k[2]: sp.Rational(5, 11), k[3]: 0, k[4]: 0, k[5]: 0}
for l in range(1, 4):
    bt = sp.Poly(b[l], X).coeff_monomial(X**(l + 1)).subs(jetJ)
    assert bt != 0
for L in range(2, 6):
    acJ = {ms: tuple(a_sum(l, ms, jetJ) for l in range(0, L - 1)) for ms in sigs}
    for grp in by_chi.values():
        for s1, s2 in itertools.combinations(grp, 2):
            assert (acJ[s1] == acJ[s2]) == all(Psi(kk, s1) == Psi(kk, s2) for kk in range(1, L))
print('VC4 J-version: iff verified for L=2..5 with a generic common jet J')

# kappa = 0 failure: flat cone points contribute nothing for l >= 1
for l in range(1, LM + 1):
    assert sp.expand(b[l].subs({k[i]: 0 for i in range(6)})) == 0
print('flat germ: b_l = 0 for l = 1..%d (so flat cone points contribute only at t^0)' % LM)

# ---------------------------------------------------------------- VC6
def vc6_hyp(m1, m2):
    return (sum(1 - Fr(1, x) for x in m1) == sum(1 - Fr(1, x) for x in m2) > 1 and
            sum(x - Fr(1, x) for x in m1) == sum(x - Fr(1, x) for x in m2))

for kk in range(1, 30):
    assert vc6_hyp((2 * kk, 8 * kk, 8 * kk), (3 * kk, 3 * kk, 12 * kk))
    assert Psi(2, (2 * kk, 8 * kk, 8 * kk)) != Psi(2, (3 * kk, 3 * kk, 12 * kk))
assert vc6_hyp((5, 5, 5), (2, 2, 2, 10)) and Psi(2, (5, 5, 5)) != Psi(2, (2, 2, 2, 10))
kk_ = sp.symbols('k', positive=True)
e1 = sum(1 - 1 / x for x in (2 * kk_, 8 * kk_, 8 * kk_)) - sum(1 - 1 / x for x in (3 * kk_, 3 * kk_, 12 * kk_))
e2 = sum(x - 1 / x for x in (2 * kk_, 8 * kk_, 8 * kk_)) - sum(x - 1 / x for x in (3 * kk_, 3 * kk_, 12 * kk_))
assert sp.simplify(e1) == 0 and sp.simplify(e2) == 0
print('VC6 examples satisfy the hypotheses (family symbolically in k) and have different Psi_2 (so VC4 fails at kappa=0, L=3)')

# flat sphere |prod (z-z_i)^{alpha_i-1} dz|: exponent at infinity
al = sp.symbols('alpha1:6')
n = 5
expo_w = -sum(a - 1 for a in al) - 2          # |dz| = |w|^{-2}|dw|, |z|^{sum(alpha-1)} = |w|^{-sum(alpha-1)}
alpha0 = sum(1 - a for a in al) - 1
assert sp.expand(expo_w - (alpha0 - 1)) == 0
print('VC6: at infinity the metric is |w|^{alpha_0 - 1}|h(w) dw|, h(0)=1, alpha_0 = sum(1-alpha_i) - 1 (cone angle 2 pi alpha_0): OK')
for ms in [(2, 8, 8), (3, 3, 12), (5, 5, 5), (2, 2, 2, 10)]:
    print('   alpha_0%s = %s' % (ms, sum(1 - Fr(1, x) for x in ms) - 1))

# search for further small VC6 pairs (sanity on how special they are)
found = []
pool = []
for nn in range(2, 6):
    pool += list(itertools.combinations_with_replacement(range(2, 31), nn))
key = {}
for ms in pool:
    a = sum(1 - Fr(1, x) for x in ms)
    if a > 1:
        key.setdefault((a, sum(x - Fr(1, x) for x in ms)), []).append(ms)
cnt = sum(1 for v in key.values() if len(v) > 1)
print('VC6: number of distinct (chi, Psi_1) classes with >=2 multisets (n<=5, m<=30): %d; e.g. %s' %
      (cnt, [v for v in key.values() if len(v) > 1][:3]))
print('ALL ASSERTS PASSED')
