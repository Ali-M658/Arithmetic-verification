"""Exact heat-coefficient primitives, written from the published formulas only.

Sources (fetched texts in review/audit/sources/):
  Ucar arXiv:1711.03405, (3.69) Bernoulli polynomials; (4.25) c^S_l(pi/k);
  (4.33) cone series C = sum_nu sum_l 2/(4^l l!) c^S_{nu-l}(pi/k) kappa^nu t^nu;
  (4.35) smooth coefficients a_nu(O) = vol/(nu! 4^nu) sum_l binom(nu,l)(-4)^l B_{2l}(1/2) kappa^nu;
  Thm 4.20: heat trace ~ (1/4 pi t) sum_nu a_nu t^nu + sum_{cones} C.

Everything here is exact (fractions.Fraction); Bernoulli numbers come from sympy.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial

import sympy


@lru_cache(maxsize=None)
def bern(n):
    """Bernoulli number B_n (convention B_1 = -1/2 is never used: only even n)."""
    assert n % 2 == 0 or n == 0
    r = sympy.bernoulli(n)
    return F(int(r.p), int(r.q))


@lru_cache(maxsize=None)
def bern_half(n):
    """B_n(1/2). For even n, B_n(1/2) = (2^{1-n} - 1) B_n; checked against sympy."""
    assert n % 2 == 0
    v = (F(2) ** (1 - n) - 1) * bern(n)
    if n <= 40:
        r = sympy.bernoulli(n, sympy.Rational(1, 2))
        assert F(int(r.p), int(r.q)) == v
    return v


@lru_cache(maxsize=None)
def bernpoly(n, a):
    """Bernoulli polynomial B_n(a) at a rational a (Fraction), exact."""
    x = sympy.Rational(a.numerator, a.denominator)
    r = sympy.bernoulli(n, x)
    return F(int(r.p), int(r.q))


@lru_cache(maxsize=None)
def c_ucar(l, k):
    """Ucar (4.25): c^S_l(pi/k), k a positive integer (or Fraction)."""
    k = F(k)
    s = F(0)
    for j in range(l + 2):
        s += comb(2 * l + 2, 2 * j) * (k ** (2 * j) - 1) * bern(2 * j) * bern_half(2 * l + 2 - 2 * j)
    return F((-1) ** l, 4) / k / factorial(l + 1) / (2 * l + 1) * s


@lru_cache(maxsize=None)
def beta(l, k):
    """beta_l(k) = sum_{i=0}^l 2/(4^i i!) c_{l-i}(pi/k); the cone series (4.33) is sum_l beta_l kappa^l t^l."""
    return sum(F(2, 4 ** i * factorial(i)) * c_ucar(l - i, k) for i in range(l + 1))


@lru_cache(maxsize=None)
def s_ucar(nu):
    """s_nu := (1/(nu! 4^nu)) sum_l binom(nu,l) (-4)^l B_{2l}(1/2), so that by (4.35)
    a_nu(O) = vol * s_nu * kappa^nu."""
    return sum(comb(nu, l) * F(-4) ** l * bern_half(2 * l) for l in range(nu + 1)) / (factorial(nu) * 4 ** nu)


def chi(genus, orders):
    return F(2 - 2 * genus) - sum((1 - F(1, m) for m in orders), F(0))


def heat_coeff(l, K, genus, orders):
    """Coefficient of t^l (l >= -1) of the heat trace of a closed orientable 2-orbifold of
    constant curvature K in {-1, +1} (area 2 pi |chi| by Gauss-Bonnet, Thurston 13.3.5)."""
    X = chi(genus, orders)
    assert X != 0 and (X > 0) == (K > 0)
    C = abs(X) / 2
    if l == -1:
        return C  # area/(4 pi) = 2 pi |chi| / (4 pi)
    return C * s_ucar(l + 1) * F(K) ** (l + 1) + F(K) ** l * sum(beta(l, m) for m in orders)


def series_mul(a, b, n):
    return [sum(a[i] * b[j - i] for i in range(j + 1)) for j in range(n)]


def exp_series(c, n):
    """Coefficients of exp(c t) up to t^{n-1}."""
    return [F(c) ** j / factorial(j) for j in range(n)]
