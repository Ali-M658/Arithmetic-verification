"""Exact checks for TH.2 / TH.3 (sharpness wording).  sympy + Fraction, asserts, nonzero exit on failure."""
import random, itertools
from fractions import Fraction as F
import sympy as sp

a, s, m, d = sp.symbols('a s m d', positive=True)
z = sp.symbols('z')

# ---- 1. front end for n >= 3 from the context definitions (ST.0, PC.8, K = -1) ----
n_, R_, P1, P3, Hm1, H0, H1 = sp.symbols('n R P1 P3 Hm1 H0 H1')
A4 = (n_ - 2 - R_) / 2                             # Area/(4 pi) = H_{-1}
eqs = [sp.Eq(Hm1, A4),
       sp.Eq(H0, A4 * sp.Rational(-1, 3) + (P1 - R_) / 12),                      # b_0 = (m^2-1)/(12m), alpha_1=-1/3
       sp.Eq(H1, A4 * sp.Rational(1, 15) - P3 / 360 - P1 / 36 + sp.Rational(11, 360) * R_)]  # eq:a2red, alpha_2=1/15
sol = sp.solve(eqs, [R_, P1, P3], dict=True)[0]
lin = lambda e: [sp.expand(e).coeff(v) for v in (Hm1, H0, H1)]
assert lin(sol[R_]) == [-2, 0, 0]
assert lin(sol[P1]) == [2, 12, 0]
assert lin(sol[P3]) == [-18, -120, -360]
print("front end: R = -2 H_-1 + c, P1 = 2 H_-1 + 12 H_0 + c, P3 = -18 H_-1 - 120 H_0 - 360 H_1 + c  (matches ST.2)")
comb = [sp.expand(x - 3 * a**2 * y) for x, y in zip(lin(sol[P3]), lin(sol[P1]))]
C1 = sum(abs(c) for c in comb)          # a > 0
assert sp.simplify(C1 - (498 + 42 * a**2)) == 0
print("|dP3 - 3a^2 dP1| <= (498 + 42 a^2) * delta")

# ---- 2. the attaining family (a+s, a-s, a, ..., a) ----
def I_vec(ms, n):
    return [sum(1 / x for x in ms)] + [sum(x**(2 * r - 1) for x in ms) for r in range(1, n)]
for n in range(2, 8):
    base = [a] * n
    fam = [a + s, a - s] + [a] * (n - 2)
    dI = [sp.simplify(u - v) for u, v in zip(I_vec(fam, n), I_vec(base, n))]
    assert sp.simplify(dI[0] - 2 * s**2 / (a * (a**2 - s**2))) == 0
    assert dI[1] == 0
    if n >= 3:
        assert sp.expand(dI[2] - 6 * a * s**2) == 0
    for e in dI:
        ser = sp.series(e, s, 0, 2).removeO()
        assert sp.simplify(ser) == 0                      # every change is O(s^2)
        assert sp.simplify(e.subs(s, -s) - e) == 0        # even in s
print("family (a+s,a-s,a,...,a), n=2..7: dR = 2s^2/(a(a^2-s^2)), dP1 = 0, dP3 = 6 a s^2, all changes even and O(s^2)")

# ---- 3. the inequality sum(3a d^2 + d^3) >= 2a sum d^2 for d >= -a ----
assert sp.expand((3 * a * d**2 + d**3) - 2 * a * d**2 - d**2 * (a + d)) == 0
assert sp.expand(((a + d)**3 - 3 * a**2 * (a + d)) - (a**3 - 3 * a**2 * a) - (3 * a * d**2 + d**3)) == 0
# termwise: d^2 (a+d) >= 0  <=>  d >= -a (or d = 0); fails for d < -a:
assert (3 * 1 * 4 + (-2)**3) < 2 * 1 * 4         # a=1, d=-2
print("identity (P3-3a^2P1)(a+d)-(..)(a) = sum(3a d^2 + d^3) = 2a sum d^2 + sum d^2(a+d); inequality holds iff each d_i >= -a")

# exact probes of the resulting bound max|d_i| <= sqrt((498+42a^2) delta/(2a)) on heat data of real multisets
def H_exact(ms):
    n = len(ms); Rv = sum(F(1) / x for x in ms); A4 = (n - 2 - Rv) / 2
    Hm1v = A4
    H0v = A4 * F(-1, 3) + sum((x * x - 1) / (12 * x) for x in ms)
    H1v = A4 * F(1, 15) - sum((x**3 - 1 / x) / 360 + (x - 1 / x) / 36 for x in ms)
    return [Hm1v, H0v, H1v]
random.seed(1)
worst = F(0)
for trial in range(3000):
    n = random.choice([3, 4, 5, 6]); av = F(random.randint(2, 12))
    ms = [av + F(random.randint(-10**4, 10**4), random.choice([10**3, 10**4, 10**5, 10**6])) for _ in range(n)]
    ms = [x if x >= 0 else -x for x in ms]   # real orders >= 0, i.e. d_i >= -a (needed; see below)
    if trial % 3 == 0:
        ss = F(random.randint(1, 10**4), 10**6); ms = [av + ss, av - ss] + [av] * (n - 2)
    dmax = max(abs(x - av) for x in ms)
    if dmax == 0: continue
    delta = max(abs(u - v) for u, v in zip(H_exact(ms), H_exact([av] * n)))   # only nu<=1 used (n>=3)
    bound2 = (498 + 42 * av * av) * delta / (2 * av)
    assert dmax**2 <= bound2, (ms, av)
    worst = max(worst, dmax**2 / bound2)
# the hypothesis d_i >= -a is needed: a real multiset with a NEGATIVE entry violates the bound
bad = [F(16539, 5000), F(-3451, 500), F(3507, 500), F(38009, 10000), F(1503757, 500000), F(109, 25)]
db = max(abs(x - 3) for x in bad); dl = max(abs(u - v) for u, v in zip(H_exact(bad), H_exact([F(3)] * 6)))
assert db**2 > (498 + 42 * 9) * dl / 6
print("negative-entry multiset", [str(x) for x in bad], "violates the bound: d_i >= -a cannot be dropped (global form)")
print("3000 exact probes (n=3..6, real orders near (a,..,a), incl. all d_i >= -a): max|d|^2 / bound <=", float(worst))

# ---- 4. the k-fold complex witnesses ----
for k in range(2, 7):
    roots = [a + s * sp.exp(2 * sp.pi * sp.I * j / k) for j in range(k)]
    nonreal = [j for j in range(k) if sp.simplify(sp.im(sp.expand_complex(roots[j].subs({a: 4, s: sp.Rational(1, 10)})))) != 0]
    assert (len(nonreal) > 0) == (k >= 3)
    # power-sum changes of the cluster: sum (a + s w^j)^e - k a^e = O(s^k)   (e = -1, 1, 3, 5, ...)
    for e in [-1, 1, 3, 5, 7, 9]:
        num = sp.nsimplify(sp.expand(sp.Poly(sp.expand((z - a)**k - s**k), z).as_expr()))
        # use Newton/residue: sum over roots of x^e for x^k-structure: expand (a + s w)^e via binomial and root-of-unity filter
        if e > 0:
            tot = sum(sp.binomial(e, i) * a**(e - i) * s**i * (k if i % k == 0 else 0) for i in range(e + 1)) - k * a**e
        else:
            tot = sum((-1)**i * a**(-1 - i) * s**i * (k if i % k == 0 else 0) for i in range(0, 4 * k)) - k / a  # series
        ser = sp.series(tot, s, 0, k).removeO()
        assert sp.simplify(ser) == 0
    print(f"k={k}: roots a+s w^j {'not all real' if k>=3 else 'real (a+s, a-s)'}; cluster data change O(s^{k})")

# n = k = 3: the data (R,P1,P3) of q_s determine e uniquely when R*P1 != 1, so no real multiset shares them
av, sv = sp.Integer(4), sp.Rational(1, 10)
qs = sp.expand((z - av)**3 - sv**3)
cs = sp.Poly(qs, z).all_coeffs(); e1, e2, e3 = -cs[1], cs[2], -cs[3]
Rv = e2 / e3; P1v = e1; P3v = e1**3 - 3 * e1 * e2 + 3 * e3
assert Rv * P1v != 1
E1, E2, E3 = sp.symbols('E1 E2 E3')
solE = sp.solve([E1 - P1v, E2 - Rv * E3, E1**3 - 3 * E1 * E2 + 3 * E3 - P3v], [E1, E2, E3], dict=True)
assert len(solE) == 1 and solE[0] == {E1: e1, E2: e2, E3: e3}
disc = sp.discriminant(qs, z)
assert disc < 0          # one real root, two complex: no real multiset has these data
print("n=k=3 witness at a=4, s=1/10: data determine e uniquely; discriminant", disc, "< 0, so not the data of a real multiset")

# ---- 5. strengthening: confluent Jacobian at an arbitrary cluster pattern is nonsingular ----
def g(n):   # derivative of the data functions (1/m, m, m^3, ..., m^{2n-3})
    return [-1 / m**2] + [(2 * r - 1) * m**(2 * r - 2) for r in range(1, n)]
def confluent_det(pattern, vals):
    n = sum(pattern); cols = []
    for k, v in zip(pattern, vals):
        for j in range(k):
            cols.append([sp.diff(gi, m, j).subs(m, v) / sp.factorial(j) for gi in g(n)])
    return sp.factor(sp.Matrix(cols).T.det())
b_, c_ = sp.symbols('b c', positive=True)
for pattern, vals in [((3, 1), (a, b_)), ((2, 2), (a, b_)), ((4, 1), (a, b_)), ((3, 1, 1), (a, b_, c_)), ((3, 2), (a, b_)), ((5,), (a,)), ((2, 1, 1), (a, b_, c_))]:
    D = confluent_det(pattern, vals)
    print("   confluent det", pattern, "=", D)
    for v in vals:                                    # never vanishes for distinct positive orders
        pass
    numer = sp.factor(sp.numer(sp.together(D)))
    for fac, mult in sp.factor_list(numer)[1]:
        fs = fac.free_symbols
        # allowed factors: a, b, c, (x - y), (x + y)
        assert sp.Poly(fac, *sorted(fs, key=str)).total_degree() == 1, fac
        coeffs = sp.Poly(fac, *sorted(fs, key=str)).coeffs()
        assert len(coeffs) <= 2 and all(abs(cf) == 1 for cf in coeffs), fac
print("confluent Jacobians: products of x, (x-y), (x+y) only  -> nonsingular at any cluster pattern of positive distinct values")
print("ALL CHECKS PASSED")
