"""DV.1 Lemma 1 (a),(b); DV.2 leading coefficient lambda_l; s_nu > 0 (input of DV.4).
All checks exact. Run from repo root:
  python3 review/audit/curvature-divergence/check_lemma1.py
"""
import os
import sys
from fractions import Fraction as F
from math import comb, factorial

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy  # noqa: E402
from heatlib import bern, bern_half, c_ucar, beta, s_ucar, series_mul, exp_series  # noqa: E402

t = sympy.symbols('t')
out = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    out.append(s)


# ---------- (a) via an independent symbolic Taylor expansion of G_k ----------
NS = 22  # sympy series order (t^0..t^21); independent of the Bernoulli algebra
for k in range(2, 7):
    G = (t / 2) / sympy.sinh(t / 2) * (k * t / 2 * sympy.coth(k * t / 2) - t / 2 * sympy.coth(t / 2))
    ser = sympy.series(G, t, 0, NS).removeO()
    for l in range(0, (NS - 2) // 2):
        g = sympy.Rational(ser.coeff(t, 2 * l + 2))
        g = F(int(g.p), int(g.q))
        rhs = F((-1) ** l * factorial(2 * l + 2), 4 * k * factorial(l + 1) * (2 * l + 1)) * g
        assert rhs == c_ucar(l, k), (k, l)
        # odd coefficients vanish
        assert ser.coeff(t, 2 * l + 1) == 0
log('(a) c_l(pi/k) = (-1)^l (2l+2)!/(4k(l+1)!(2l+1)) g_{2l+2}(k): exact, sympy series of G_k, k=2..6, l=0..9')


# ---------- (a) for large l via the Bernoulli product (generating functions of (3.69)) ----------
def g_coeff(N, k):
    """coefficient of t^N in G_k: (t/2)/sinh(t/2) = sum B_{2i}(1/2) t^{2i}/(2i)!,
    (x)coth(x) with x = kt/2: sum B_{2j} k^{2j} t^{2j}/(2j)!."""
    assert N % 2 == 0
    return sum(bern_half(N - 2 * j) / factorial(N - 2 * j) * bern(2 * j) * (F(k) ** (2 * j) - 1) / factorial(2 * j)
               for j in range(N // 2 + 1))


for k in [2, 3, 7, 12]:
    for l in range(0, 60, 7):
        g = g_coeff(2 * l + 2, k)
        assert F((-1) ** l * factorial(2 * l + 2), 4 * k * factorial(l + 1) * (2 * l + 1)) * g == c_ucar(l, k)
log('(a) also exact for k in {2,3,7,12}, l = 0..56 step 7 (Bernoulli product form)')

# ---------- G_2 = (t/2)^2 sech(t/2) ----------
G2 = (t / 2) / sympy.sinh(t / 2) * (t * sympy.coth(t) - t / 2 * sympy.coth(t / 2))
d = sympy.series(G2 - (t / 2) ** 2 / sympy.cosh(t / 2), t, 0, 30).removeO()
assert sympy.simplify(d) == 0
assert sympy.simplify((G2 - (t / 2) ** 2 / sympy.cosh(t / 2)).rewrite(sympy.exp)) == 0
log('(c) G_2(t) = (t/2)^2 sech(t/2): exact (closed form and series to t^29)')

# ---------- (b) sign: (-1)^l g_{2l+2}(k) > 0, c_l > 0, beta_l > 0 ----------
LMAX = 120
for k in list(range(2, 31)) + [49, 50, 97]:
    for l in range(LMAX + 1):
        c = c_ucar(l, k)
        assert c > 0, (k, l)
        assert beta(l, k) > 0, (k, l)
log(f'(b) c_l(pi/k) > 0 and beta_l(k) > 0: exact, k = 2..30, 49, 50, 97, l = 0..{LMAX}')

# the positivity proof uses: x/sin x and (y cot y) expansions. Check the two ingredient sign patterns exactly.
x = sympy.symbols('x')
s1 = sympy.series((x / 2) / sympy.sin(x / 2), x, 0, 40).removeO()
assert all(s1.coeff(x, 2 * i) > 0 for i in range(20))
for k in [2, 3, 5]:
    s2 = sympy.series(x / 2 * sympy.cot(x / 2) - k * x / 2 * sympy.cot(k * x / 2), x, 0, 40).removeO()
    assert s2.coeff(x, 0) == 0 and all(s2.coeff(x, 2 * i) > 0 for i in range(1, 20))
    H = sympy.expand(s1 * s2)
    Gs = sympy.series((t / 2) / sympy.sinh(t / 2) * (k * t / 2 * sympy.coth(k * t / 2) - t / 2 * sympy.coth(t / 2)), t, 0, 40).removeO()
    for l in range(0, 18):
        # H(x) = -G_k(i x): coefficient of x^{2l+2} equals (-1)^l g_{2l+2}
        assert H.coeff(x, 2 * l + 2) == (-1) ** l * Gs.coeff(t, 2 * l + 2)
log('(b) ingredients: (x/2)/sin(x/2) and (x/2)cot(x/2)-(kx/2)cot(kx/2) have positive coefficients; H(x)=-G_k(ix): exact')

# ---------- DV.2: lambda_l is the leading coefficient of p_l(m) = m beta_l(m) ----------
m = sympy.symbols('m')
for l in range(0, 16):
    # build m*c_l(pi/m) as a polynomial in m from (4.25)
    poly = 0
    for i in range(l + 1):
        ll = l - i
        inner = sum(comb(2 * ll + 2, 2 * j) * (m ** (2 * j) - 1) * sympy.Rational(bern(2 * j).numerator, bern(2 * j).denominator)
                    * sympy.Rational(bern_half(2 * ll + 2 - 2 * j).numerator, bern_half(2 * ll + 2 - 2 * j).denominator)
                    for j in range(ll + 2))
        poly += sympy.Rational(2, 4 ** i * factorial(i)) * sympy.Rational((-1) ** ll, 4 * factorial(ll + 1) * (2 * ll + 1)) * inner
    poly = sympy.Poly(sympy.expand(poly), m)
    assert poly.degree() == 2 * l + 2
    lam = abs(sympy.bernoulli(2 * l + 2)) / (2 * sympy.factorial(l + 1) * (2 * l + 1))
    assert poly.LC() == lam
    # p_l(m) as polynomial: check against beta at a few integers
    for mm in [2, 3, 5]:
        v = poly.eval(mm)
        assert F(int(v.p), int(v.q)) == mm * beta(l, mm)
    # parity: p_l is an even polynomial in m
    assert all(poly.coeff_monomial(m ** (2 * r + 1)) == 0 for r in range(l + 2))
log('DV.2 lambda_l = |B_{2l+2}|/(2(l+1)!(2l+1)) is the leading coefficient of p_l(m) = m beta_l(m): exact, l = 0..15')

# ---------- s_nu > 0, and an independent derivation of s_nu from the S^2 spectrum ----------
# S^2: sum_{l>=0} (2l+1) e^{-l(l+1)t} = e^{t/4} * 2 sum_{n>=0} (n+1/2) e^{-(n+1/2)^2 t}
# Euler-Maclaurin / Mellin: 2 sum (n+1/2) e^{-(n+1/2)^2 t} ~ 1/t - sum_{k>=1} B_{2k}(1/2) (-t)^{k-1}/k!
NN = 150
inner = [-bern_half(2 * kk) * F(-1) ** (kk - 1) / factorial(kk) for kk in range(1, NN + 1)]  # coeff of t^{kk-1}
assert all(v > 0 for v in inner)
e = exp_series(F(1, 4), NN + 1)
# full trace: 1/t * e^{t/4} + e^{t/4}*inner ; coefficient of t^nu-1 is s_nu (chi(S^2)=2 => C=1, K=1)
for nu in range(0, NN):
    val = e[nu] + sum(e[i] * inner[nu - 1 - i] for i in range(nu)) if nu >= 1 else e[0]
    assert val == s_ucar(nu), nu
    assert val > 0
log(f's_nu from (4.35) equals the S^2 spectral expansion, and s_nu > 0, exact for nu = 0..{NN - 1}')
log('s_0..s_4 =', [str(s_ucar(i)) for i in range(5)])

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check_lemma1.txt'), 'w') as fh:
    fh.write('\n'.join(out) + '\nALL CHECKS PASSED\n')
print('ALL CHECKS PASSED')
