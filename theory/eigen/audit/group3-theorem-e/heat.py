"""Independent exact implementation of the heat invariants of prop:heatinput / lem:Phi
(STATEMENTS.md, Section A).  Exact rationals throughout (sympy for series and Bernoulli numbers)."""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, comb
import sympy as sp

LMAX = 16  # largest l needed


def bern(n):
    r = sp.bernoulli(n)
    if n == 1:  # convention irrelevant here (only even indices used)
        pass
    r = sp.Rational(r)
    return F(int(r.p), int(r.q))


def bernpoly_half(n):
    r = sp.Rational(sp.bernoulli(n, sp.Rational(1, 2)))
    return F(int(r.p), int(r.q))


@lru_cache(None)
def sigma_coeffs(n):
    u = sp.symbols('u')
    s = sp.series(u / sp.sin(u), u, 0, 2 * n + 2).removeO()
    out = []
    for i in range(n + 1):
        c = sp.Rational(s.coeff(u, 2 * i))
        out.append(F(int(c.p), int(c.q)))
    return tuple(out)


SIG = sigma_coeffs(LMAX + 2)
for s_ in SIG:
    assert s_ > 0


@lru_cache(None)
def m_phi(k, m):
    """m*phi_k(m), eq. (phik)."""
    m = F(m)
    tot = F(0)
    for n in range(1, k + 2):
        tot += SIG[k + 1 - n] * F(4) ** n * abs(bern(2 * n)) / factorial(2 * n) * (m ** (2 * n) - 1)
    return tot / 4


@lru_cache(None)
def p_l(l, m):
    m = F(m)
    tot = F(0)
    for k in range(l + 1):
        tot += F(factorial(2 * k), factorial(k) * factorial(l - k)) * m_phi(k, m)
    return tot / F(4) ** l


@lru_cache(None)
def b_l(l, m):
    return (-1) ** l * p_l(l, m) / F(m)


@lru_cache(None)
def alpha(k):
    s = sum(comb(k, l) * F(-4) ** l * bernpoly_half(2 * l) for l in range(k + 1))
    return F((-1) ** k, factorial(k) * 4 ** k) * s


def a_lead(l):
    return abs(bern(2 * l + 2)) / (2 * factorial(l + 1) * (2 * l + 1))


def p_l_coeffs(l):
    """coefficients a_{l,k} of p_l(x)=sum a_{l,k} x^{2k}, by exact interpolation in x^2."""
    x = sp.symbols('x')
    pts = list(range(1, l + 3))
    ys = [p_l(l, m) for m in pts]
    poly = sp.interpolate([(sp.Integer(m) ** 2, sp.Rational(y.numerator, y.denominator)) for m, y in zip(pts, ys)], x)
    poly = sp.Poly(sp.expand(poly), x)
    co = [poly.coeff_monomial(x ** k) for k in range(l + 2)]
    return [F(int(sp.Rational(c).p), int(sp.Rational(c).q)) for c in co]


def chi(g, ms):
    return F(2 - 2 * g) - sum((1 - F(1, m) for m in ms), F(0))


def c_vec(g, ms, J):
    """c_1..c_J exactly; c_1 = Area/4pi = -chi/2."""
    a4 = -chi(g, ms) / 2
    out = [a4]
    for j in range(2, J + 1):
        out.append(alpha(j - 1) * a4 + sum(b_l(j - 2, m) for m in ms))
    return out
