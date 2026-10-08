"""
Exact checks of VC1 (Pi_i), VC2, VC3 against
  * the independent b_l computed by twisted_duhamel.py (parsed from twisted_duhamel_output.txt),
  * Schueth arXiv:1812.06119 Thm 3.7 / Thm 4.1 (fetched),
  * Ucar arXiv:1711.03405 (4.25), (4.33)-(4.34) (fetched).
Exact arithmetic only (sympy Rational); all checks are asserts.
"""
import re
import sympy as sp
from fractions import Fraction

here = __file__.rsplit('/', 1)[0]
X, m, x = sp.symbols('X m x')
k = sp.symbols('k0:6')
KK, DK, D2K, D3K = sp.symbols('K DK D2K D3K')

# ------------------------------------------------------------------ parse b_l
txt = open(here + '/twisted_duhamel_output.txt').read()
b = {}
for line in txt.splitlines():
    mm = re.match(r'b_(\d+) = (.*)', line)
    if mm:
        b[int(mm.group(1))] = sp.sympify(mm.group(2), locals={'X': X, **{'k%d' % i: k[i] for i in range(6)}})
inv = sp.sympify(re.search(r"invariants: (\{.*\})", txt).group(1).replace("'", '"'),
                 locals={'k%d' % i: k[i] for i in range(6)})
inv = {str(a): v for a, v in inv.items()}
print('parsed b_l for l =', sorted(b))
LM = max(b)

# ------------------------------------------------------------------ Pi_i exact
def Pi_exact(i, mm):
    """(1/m) sum_{j=1}^{m-1} x_j^{-i}, x_j = 4 sin^2(pi j/m), exactly: the x_j are the nonzero
    eigenvalues of the Laplacian L of the m-cycle, so sum_j x_j^{-i} = tr((L + J/m)^{-i}) - 1."""
    if mm == 1:
        return sp.Integer(0)
    L = sp.zeros(mm, mm)
    for a in range(mm):
        L[a, a] += 2 if mm > 2 else 2
        L[a, (a + 1) % mm] -= 1
        L[a, (a - 1) % mm] -= 1
    J = sp.ones(mm, mm) * sp.Rational(1, mm)
    Minv = (L + J).inv()
    return ((Minv ** i).trace() - 1) / mm


claimed_mPi = {
    1: (m**2 - 1) / 12,
    2: (m**2 - 1) * (m**2 + 11) / 720,
    3: (m**2 - 1) * (2 * m**4 + 23 * m**2 + 191) / 60480,
    4: (m**2 - 1) * (m**2 + 11) * (3 * m**4 + 10 * m**2 + 227) / 3628800,
}
IMAX = 7
PI = {(i, mm): Pi_exact(i, mm) for i in range(1, IMAX + 1) for mm in range(1, 2 * IMAX + 8)}
# numeric sanity of the exact routine
import mpmath as mp
mp.mp.dps = 50
for (i, mm), v in PI.items():
    if mm >= 2:
        num = sum(mp.mpf(1) / (4 * mp.sin(mp.pi * j / mm)**2)**i for j in range(1, mm)) / mm
        assert abs(num - mp.mpf(v.p) / v.q) < mp.mpf(10)**-40
for i, expr in claimed_mPi.items():
    for mm in range(1, 2 * IMAX + 8):
        assert sp.Rational(expr.subs(m, mm)) == mm * PI[(i, mm)], (i, mm)
print('VC1: m*Pi_i formulas for i=1..4 confirmed exactly for m=1..%d' % (2 * IMAX + 7))

mPi_poly = {}
for i in range(1, IMAX + 1):
    pts = [(mm, mm * PI[(i, mm)]) for mm in range(1, 2 * i + 2)]
    poly = sp.expand(sp.interpolate(pts, m))
    for mm in range(2 * i + 2, 2 * IMAX + 8):          # extra points: genuinely a polynomial
        assert poly.subs(m, mm) == mm * PI[(i, mm)]
    P = sp.Poly(poly, m)
    assert P.degree() == 2 * i
    assert all(e[0] % 2 == 0 for e in P.monoms()), 'not even'
    assert poly.subs(m, 1) == 0
    assert P.LC() == abs(sp.bernoulli(2 * i)) / sp.factorial(2 * i)
    mPi_poly[i] = poly
print('VC1: m*Pi_i is an even polynomial of degree 2i, vanishing at m=1, leading coeff |B_2i|/(2i)!  (i=1..%d; '
      'checked on %d extra points)' % (IMAX, 6))
Pi = {i: sp.cancel(mPi_poly[i] / m) for i in mPi_poly}

# ------------------------------------------------------------------ b_l structure
for l in range(LM + 1):
    P = sp.Poly(b[l], X)
    degs = sorted(e[0] for e in P.monoms())
    assert min(degs) >= 1 and max(degs) <= l + 1, (l, degs)
    print('VC1: b_%d is a polynomial in X=C^-2 with powers %s (no X^0, no negative powers of X)' % (l, degs))

# b_0, b_1, b_2 vs Donnelly / Schueth Thm 3.7 (fetched)
assert sp.expand(b[0] - X) == 0
assert sp.expand(b[1] - 2 * k[0] * X**2) == 0
DKk = inv['D1']
assert sp.expand(b[2] - ((12 * X**3 - 2 * X**2) * k[0]**2 - 2 * X**3 * DKk)) == 0
print('b_0=1/C^2, b_1=2K/C^4, b_2 = (12/C^6 - 2/C^4)K^2 - 2/C^6 Delta K  [Schueth Thm 3.7]: CONFIRMED')

# ------------------------------------------------------------------ VC3
if LM >= 3:
    D2 = inv['D2']
    claim_b3 = (120 * X**4 - 32 * X**3 + sp.Rational(4, 3) * X**2) * k[0]**3 + (-42 * X**4 + 8 * X**3) * k[0] * DKk + X**4 * D2
    assert sp.expand(b[3] - claim_b3) == 0
    print('VC3: b_3(phi) formula CONFIRMED (independent Weyl-algebra Duhamel computation)')
    A = sp.factor(120 * Pi[4] - 32 * Pi[3] + sp.Rational(4, 3) * Pi[2])
    B = sp.factor(-42 * Pi[4] + 8 * Pi[3])
    D = sp.factor(Pi[4])
    A_cl = (m**2 - 1) * (m**2 + 3) * (3 * m**4 + 2 * m**2 + 19) / (30240 * m)
    B_cl = -(m**2 - 1) * (7 * m**6 + 47 * m**4 + 173 * m**2 + 733) / (201600 * m)
    D_cl = (m**2 - 1) * (m**2 + 11) * (3 * m**4 + 10 * m**2 + 227) / (3628800 * m)
    for name, u, v in [('A', A, A_cl), ('B', B, B_cl), ('D', D, D_cl)]:
        assert sp.simplify(u - v) == 0, name
        print('VC3: %s(m) = %s CONFIRMED' % (name, v))
    # direct exact average for m = 2..15 of the X-polynomial (not via the Pi polynomials)
    for mm in range(2, 16):
        tot = 0
        for (e,), cf in sp.Poly(b[3], X).terms():
            tot += cf * PI[(e, mm)]
        val = sp.expand(A_cl.subs(m, mm) * k[0]**3 + B_cl.subs(m, mm) * k[0] * DKk + D_cl.subs(m, mm) * D2)
        assert sp.expand(tot - val) == 0
    print('VC3: a_3(p) = A K^3 + B K DK + D D^2K also confirmed by direct exact averaging for m=2..15')

# ------------------------------------------------------------------ Schueth Thm 4.1
S41 = (sp.Rational(1, 2520) * (m**5 - 1 / m) + sp.Rational(1, 720) * (m**3 - 1 / m) + sp.Rational(1, 180) * (m - 1 / m)) * KK**2 \
    - (sp.Rational(1, 15120) * (m**5 - 1 / m) + sp.Rational(1, 1440) * (m**3 - 1 / m) + sp.Rational(1, 180) * (m - 1 / m)) * DK
mine2 = (12 * Pi[3] - 2 * Pi[2]) * KK**2 - 2 * Pi[3] * DK
assert sp.simplify(S41 - mine2) == 0
print('Schueth Thm 4.1 (a_2 cone contribution) reproduced exactly from my b_2')

# ------------------------------------------------------------------ Ucar constant curvature
def ucar_C(nu, kk):
    """(4.33)-(4.34): sum_{l=0}^{nu} 2/(4^l l!) c^S_{nu-l}(pi/k), coefficient of kappa^nu."""
    def cS(L):
        tot = sum(sp.binomial(2 * L + 2, 2 * j) * (kk**(2 * j) - 1) * sp.bernoulli(2 * j) *
                  sp.bernoulli(2 * L + 2 - 2 * j, sp.Rational(1, 2)) for j in range(L + 2))
        return sp.Rational(1, 4) / kk * (-1)**L / (sp.factorial(L + 1) * (2 * L + 1)) * tot
    return sum(sp.Rational(2, 4**l) / sp.factorial(l) * cS(nu - l) for l in range(nu + 1))

for l in range(LM + 1):
    bc = sp.Poly(b[l].subs({k[i]: 0 for i in range(1, 6)}).subs(k[0], 1), X)
    for mm in range(2, 16):
        mine = sum(cf * PI[(e, mm)] for (e,), cf in bc.terms())
        assert sp.nsimplify(mine) == sp.nsimplify(ucar_C(l, mm)), (l, mm)
print('Constant curvature: (1/m) sum_j b_l(2 pi j/m)|_{K=kappa} = Ucar (4.33)-(4.34) for l=0..%d, m=2..15' % LM)
if LM >= 3:
    for mm in range(2, 31):
        assert sp.Rational(A_cl.subs(m, mm)) == ucar_C(3, mm)
    print('VC3: A(m) = Ucar coefficient of kappa^3, m=2..30: CONFIRMED')

# ------------------------------------------------------------------ VC2
r, v = sp.symbols('r v')


def f_series(Kcoef, N):
    co = [sp.Integer(0)] * (N + 3)
    co[1] = 1
    Kc = list(Kcoef) + [0] * (N + 3)
    for n in range(N):
        co[n + 2] = sp.expand(-sum(Kc[i // 2] * co[n - i] for i in range(0, n + 1, 2)) / ((n + 2) * (n + 1)))
    return sum(co[i] * r**i for i in range(N + 3))


def top_formula(l, Kcoef):
    """4^l l! [v^{2l}] (f^{-1})'(v).  By Lagrange inversion, [v^{2l}] (f^{-1})' = (2l+1)[v^{2l+1}] f^{-1}
    = [r^{2l}] (r/f(r))^{2l+1}; computed with truncated power series in r (exact)."""
    N = 2 * l + 1
    fr = f_series(Kcoef, N + 1)
    h = sp.Poly(sp.expand(sp.cancel(fr / r)), r)          # f/r = 1 + O(r^2)
    hc = [h.coeff_monomial(r**i) for i in range(2 * l + 1)]
    # inverse power series of h truncated at r^{2l}
    inv = [sp.Integer(0)] * (2 * l + 1)
    inv[0] = sp.Integer(1)
    for n in range(1, 2 * l + 1):
        inv[n] = sp.expand(-sum(hc[i] * inv[n - i] for i in range(1, n + 1)))
    # raise to the power 2l+1
    pw = [sp.Integer(1)] + [sp.Integer(0)] * (2 * l)
    for _ in range(2 * l + 1):
        pw = [sp.expand(sum(pw[i] * inv[n - i] for i in range(n + 1))) for n in range(2 * l + 1)]
    return sp.expand(4**l * sp.factorial(l) * pw[2 * l])


Ksym = list(k)
for l in range(1, LM + 1):
    assert sp.expand(top_formula(l, Ksym[:l + 1]) - sp.Poly(b[l], X).coeff_monomial(X**(l + 1))) == 0
    print('VC2: top coefficient beta_{%d,%d} = 4^l l! [v^2l](f^-1)\' matches my b_%d' % (l, l + 1, l))

# (ii) constant curvature, l up to 12
kap = sp.symbols('kappa')
for l in range(1, 13):
    val = top_formula(l, [kap])
    assert sp.expand(val - sp.factorial(2 * l) / sp.factorial(l) * kap**l) == 0
    ucar_lead = sp.Rational(2) * sp.Rational(1, 4) * (-1)**l * sp.bernoulli(2 * l + 2) / (sp.factorial(l + 1) * (2 * l + 1))
    assert ucar_lead == sp.factorial(2 * l) / sp.factorial(l) * abs(sp.bernoulli(2 * l + 2)) / sp.factorial(2 * l + 2)
print('VC2(ii): beta_{l,l+1}|const = (2l)!/l! kappa^l for l=1..12, and |B_{2l+2}|/(2l+2)! times it = Ucar leading m^{2l+1} coefficient')

# (i) linear part: coefficient of k_{l-1} must be 2 * 4^{l-1} (l-1)!  [flat (div grad)^{l-1} r^{2(l-1)} = 4^{l-1}((l-1)!)^2]
for l in range(1, 9):
    val = top_formula(l, Ksym[:l] if l <= 6 else Ksym[:6] + [sp.Symbol('k%d' % j) for j in range(6, l)])
    kl = (Ksym + [sp.Symbol('k%d' % j) for j in range(6, 10)])[l - 1]
    lin = sp.Poly(val, *(Ksym + [sp.Symbol('k%d' % j) for j in range(6, 10)])[:max(l, 1)])
    lin_terms = {mon: cf for mon, cf in lin.terms() if sum(mon) == 1}
    target_k = 2 * 4**(l - 1) * sp.factorial(l - 1)
    assert len(lin_terms) == 1 and list(lin_terms.values())[0] == target_k, (l, lin_terms)
    # check the flat-Laplacian normalisation: (d^2)^{l-1} r^{2l-2} at 0 = 4^{l-1}((l-1)!)^2
    rr = sp.symbols('rr', positive=True)
    h = rr**(2 * l - 2)
    for _ in range(l - 1):
        h = sp.expand(sp.diff(h, rr, 2) + sp.diff(h, rr) / rr)
    assert h == 4**(l - 1) * sp.factorial(l - 1)**2
    assert target_k == 2 * h / sp.factorial(l - 1)
print('VC2(i): linear part of beta_{l,l+1} = 2 (-Delta)^{l-1}K/(l-1)!  for l=1..8 (exact)')

# (iii)
if 'D3' in inv:
    D3 = inv['D3']
    cl4 = 1680 * k[0]**4 - 904 * k[0]**2 * DKk + sp.Rational(98, 3) * k[0] * inv['D2'] + sp.Rational(124, 3) * DKk**2 - sp.Rational(1, 3) * D3
    val4 = top_formula(4, Ksym[:5])
    print('VC2(iii) l=4: formula - claim =', sp.expand(val4 - cl4))
    assert sp.expand(val4 - cl4) == 0
    print('VC2(iii): beta_{4,5} claim CONFIRMED against 4^4 4! [v^8](f^-1)\'')
cl = {1: 2 * k[0], 2: 12 * k[0]**2 - 2 * DKk,
      3: 120 * k[0]**3 - 42 * k[0] * DKk + inv.get('D2', 0)}
for l in (1, 2, 3):
    assert sp.expand(top_formula(l, Ksym[:l + 1]) - cl[l]) == 0
print('VC2(iii): beta_{1,2}, beta_{2,3}, beta_{3,4} CONFIRMED')

# (iv) & Schueth's m^5 coefficient
assert sp.Poly(sp.expand(m * S41), m).coeff_monomial(m**6) == sp.expand(abs(sp.bernoulli(6)) / sp.factorial(6) * (12 * KK**2 - 2 * DK))
print('VC2(iv): m^5 coefficient of Schueth Thm 4.1 = |B_6|/6! * beta_{2,3}: CONFIRMED')
print('ALL ASSERTS PASSED')
