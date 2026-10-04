"""Common exact-arithmetic helpers for the signatures referee checks.

Cone coefficients are derived directly from Ucar, arXiv:1711.03405,
equations (4.25) and (4.33):

  c^S_l(pi/k) = 1/(4k) * (-1)^l/(l+1)! * 1/(2l+1)
                * sum_{j=0}^{l+1} C(2l+2,2j) (k^{2j}-1) B_{2j} B_{2l+2-2j}(1/2)

  b_nu(k) = kappa^nu * sum_{l=0}^{nu} 2/(4^l l!) * c^S_{nu-l}(pi/k)

so p_nu(k) := k b_nu(k)/kappa^nu is a polynomial in k.  We work at kappa = -1.

Heat coefficients: tr e^{-t Delta} ~ sum_j c_j t^{j-2}, with
  c_1 = Area/(4 pi),  c_{l+2} = alpha_l Area + sum_i b_l(m_i)  (l >= 0),
so for two orbifolds of equal area, c_{l+2} agree iff C_l agree.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial, lcm
import sympy as sp

KAPPA = -1


@lru_cache(maxsize=None)
def bern_num(n):
    return Fraction(str(sp.bernoulli(n))) if n != 1 else Fraction(-1, 2)


@lru_cache(maxsize=None)
def bern_half(n):
    # B_n(1/2), exact
    v = sp.bernoulli(n, sp.Rational(1, 2))
    return Fraction(int(sp.numer(v)), int(sp.denom(v)))


def _poly_add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]


@lru_cache(maxsize=None)
def kcS(l):
    """Coefficient list (in powers of k) of the polynomial k * c^S_l(pi/k)."""
    pref = Fraction(1, 4) * Fraction((-1) ** l, factorial(l + 1) * (2 * l + 1))
    coeffs = [Fraction(0)] * (2 * l + 3)
    for j in range(l + 2):
        w = pref * comb(2 * l + 2, 2 * j) * bern_num(2 * j) * bern_half(2 * l + 2 - 2 * j)
        coeffs[2 * j] += w
        coeffs[0] -= w
    return tuple(coeffs)


@lru_cache(maxsize=None)
def p_poly(nu):
    """Coefficient list of p_nu(k) = k b_nu(k)/kappa^nu (Ucar (4.33))."""
    out = [Fraction(0)]
    for l in range(nu + 1):
        w = Fraction(2, 4 ** l * factorial(l))
        out = _poly_add(out, [w * c for c in kcS(nu - l)])
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def peval(coeffs, x):
    r = 0
    for c in reversed(coeffs):
        r = r * x + c
    return r


def b_coef(nu, k):
    """b_nu(k) at curvature -1, exact Fraction."""
    return Fraction(KAPPA ** nu) * peval(p_poly(nu), Fraction(k)) / k


def s_of(g, m):
    """s = -chi = Area/(2 pi)."""
    return 2 * g - 2 + sum(1 - Fraction(1, x) for x in m)


def fsum_recip(xs):
    """Exact sum of 1/x over a list of positive ints (common denominator)."""
    xs = list(xs)
    if not xs:
        return Fraction(0)
    D = 1
    for x in set(xs):
        D = lcm(D, x)
    return Fraction(sum(D // x for x in xs), D)


def cone_sum(nu, m):
    """C_nu(m) = sum b_nu(m_i), exact; uses p_nu(x)/x = (p_nu(x)-p_nu(0))/x + p_nu(0)/x."""
    P = p_poly(nu)
    # (p(x)-p(0))/x is a polynomial with coefficients P[1:]
    q = P[1:]
    num_den = 1
    for c in q:
        num_den = lcm(num_den, c.denominator)
    qi = [int(c * num_den) for c in q]
    poly_part = 0
    for x in m:
        poly_part += peval(qi, x)
    total = Fraction(poly_part, num_den) + P[0] * fsum_recip(m)
    return Fraction(KAPPA ** nu) * total


def shared_count(g1, m1, g2, m2, cap):
    """Largest L <= cap with H_L equal, computed with the actual cone coefficients.
    Returns 0 if areas differ.  Entries equal to 1 are allowed (b_nu(1)=0, no area)."""
    if s_of(g1, m1) != s_of(g2, m2):
        return 0
    L = 1
    while L < cap:
        nu = L - 1  # c_{L+1} involves C_{L-1}
        if cone_sum(nu, m1) != cone_sum(nu, m2):
            return L
        L += 1
    return L


def thue_morse(i):
    return bin(i).count("1") & 1
