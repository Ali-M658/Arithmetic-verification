"""Constant-curvature heat coefficients of a closed 2-orbifold, derived directly from
Ucar, arXiv:1711.03405, eqs. (4.25), (4.33), (4.35) and Theorem 4.20.

Conventions (Ucar, Thm 4.20 / DGGW Thm 4.8):
    Z(t) ~ (1/(4 pi t)) sum_nu a_nu(O) t^nu  +  sum_{cone points} C(m),
    a_nu(O) = vol(O)/(nu! 4^nu) sum_{l=0}^{nu} binom(nu,l) (-4)^l B_{2l}(1/2) kappa^nu   (4.35)
    C(m)    = sum_nu [ sum_{l=0}^{nu} 2/(4^l l!) c^S_{nu-l}(pi/m) ] kappa^nu t^nu         (4.33)
    c^S_l(pi/k) = 1/(4k) (-1)^l/(l+1)! 1/(2l+1) sum_{j=0}^{l+1} binom(2l+2,2j)(k^{2j}-1) B_{2j} B_{2l+2-2j}(1/2)   (4.25)

Everything is exact (sympy Rational / Fraction).
"""
from fractions import Fraction as Fr
from functools import lru_cache
import sympy as sp

m_sym = sp.Symbol('m', positive=True)


@lru_cache(None)
def B(n):
    """Bernoulli number B_n (only even n and n=0 are used)."""
    assert n == 0 or n % 2 == 0
    return Fr(sp.bernoulli(n).p, sp.bernoulli(n).q)


@lru_cache(None)
def Bhalf(n):
    """B_n(1/2) = (2^{1-n} - 1) B_n for even n."""
    assert n % 2 == 0
    return (Fr(2) ** (1 - n) - 1) * B(n)


def _binom(a, b):
    return Fr(sp.binomial(a, b))


def _fact(a):
    return Fr(sp.factorial(a))


@lru_cache(None)
def cS(l, k):
    """Ucar (4.25): c^S_l(pi/k) for integer k (exact)."""
    s = Fr(0)
    for j in range(0, l + 2):
        s += _binom(2 * l + 2, 2 * j) * (Fr(k) ** (2 * j) - 1) * B(2 * j) * Bhalf(2 * l + 2 - 2 * j)
    return Fr(1, 4 * k) * Fr((-1) ** l) / _fact(l + 1) / (2 * l + 1) * s


@lru_cache(None)
def beta(l, k):
    """K-independent cone coefficient: b_l(k) = kappa^l * beta(l,k)  (Ucar (4.33)/(4.34))."""
    return sum((Fr(2) / (Fr(4) ** i * _fact(i)) * cS(l - i, k) for i in range(l + 1)), Fr(0))


def b(l, k, kappa):
    """Cone contribution of a cone point of order k at order t^l, curvature kappa."""
    return Fr(kappa) ** l * beta(l, k)


@lru_cache(None)
def alpha_unit(nu):
    """a_nu(O)/vol(O) at kappa=+1 (Ucar (4.35)); general kappa multiplies by kappa^nu."""
    s = sum((_binom(nu, l) * Fr(-4) ** l * Bhalf(2 * l) for l in range(nu + 1)), Fr(0))
    return s / (_fact(nu) * Fr(4) ** nu)


def alpha(nu, kappa):
    return alpha_unit(nu) * Fr(kappa) ** nu


# ---------- symbolic polynomial p_l(m) = m * beta_l(m) -----------------------------------
@lru_cache(None)
def cS_sym(l):
    k = m_sym
    s = 0
    for j in range(0, l + 2):
        s += sp.binomial(2 * l + 2, 2 * j) * (k ** (2 * j) - 1) * sp.bernoulli(2 * j) * \
            sp.Rational(Bhalf(2 * l + 2 - 2 * j).numerator, Bhalf(2 * l + 2 - 2 * j).denominator)
    return sp.expand(sp.Rational(1, 4) / k * sp.Integer(-1) ** l / sp.factorial(l + 1) / (2 * l + 1) * s)


@lru_cache(None)
def p_sym(l):
    """p_l(m) := m * beta_l(m), a polynomial in m."""
    e = sum(sp.Rational(2, 4 ** i) / sp.factorial(i) * cS_sym(l - i) for i in range(l + 1))
    return sp.Poly(sp.expand(m_sym * e), m_sym)


def lead_claimed(l):
    """|B_{2l+2}| / (2 (l+1)! (2l+1)) -- the leading coefficient quoted by AU, SG, ST, DV."""
    return abs(B(2 * l + 2)) / (2 * _fact(l + 1) * (2 * l + 1))


# ---------- assembled coefficients ------------------------------------------------------
def heat_coeffs(g, ms, kappa, N):
    """Return dict  power -> coefficient  for powers t^{-1}, t^0, ..., t^{N-2}
    (i.e. the first N coefficients c_1..c_N in the definitions-group indexing), for a closed
    orientable orbifold of genus g, cone orders ms, constant curvature kappa in {-1,+1}.
    Area via Gauss-Bonnet: kappa*Area = 2 pi chi."""
    chi = 2 - 2 * g - sum((1 - Fr(1, m) for m in ms), Fr(0))
    assert kappa in (-1, 1)
    area_over_4pi = chi / (2 * kappa)  # Area/(4pi) = 2 pi chi / kappa / (4 pi)
    assert area_over_4pi > 0
    out = {}
    for nu in range(N):
        power = nu - 1
        val = area_over_4pi * alpha(nu, kappa)
        if power >= 0:
            val += sum((b(power, m, kappa) for m in ms), Fr(0))
        out[power] = val
    return out


def c(j, g, ms, kappa=-1):
    """c_j in def:heatcoef indexing: coefficient of t^{j-2}."""
    return heat_coeffs(g, ms, kappa, j)[j - 2]
