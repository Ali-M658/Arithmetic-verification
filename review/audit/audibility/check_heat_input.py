"""AU.0 heat input, re-derived from the formula in Ucar's thesis (arXiv:1711.03405).

Inputs, as printed in the thesis (printed page / PDF page of the arXiv v1 file):
  (4.25) p.134 / PDF p.139:
     c^S_l(pi/k) = 1/(4k) * (-1)^l/(l+1)! * 1/(2l+1)
                   * sum_{j=0}^{l+1} binom(2l+2,2j) (k^{2j}-1) B_{2j} B_{2l+2-2j}(1/2)
  (4.33) p.137 / PDF p.142:
     C = sum_nu sum_{l=0}^{nu} 2/(4^l l!) c^S_{nu-l}(pi/k) kappa^nu t^nu
  Thm 4.20(i) (4.35) p.137: a_nu(O) = vol(O)/(nu! 4^nu) sum_l binom(nu,l)(-4)^l B_{2l}(1/2) kappa^nu
  Thm 4.20(ii) p.138 / PDF p.143: a cone point of order k contributes C to the heat trace,
     whose expansion is (1/(4 pi t)) sum a_nu t^nu + sum_N I_N/|Iso N|.
So the cone contribution at t^nu is b_nu(k) = kappa^nu * (1/k) * p_nu(k) with
     p_nu(k) = sum_{l=0}^{nu} 2/(4^l l!) * k * c^S_{nu-l}(pi/k).
Cross-checks: DGGW (arXiv:0805.3148) Prop 5.5 gives I_N = (m^2-1)/12 + O(t) for a cone point,
|Iso N| = m; Schueth (arXiv:1812.06119) Thm 4.1 (p.14) gives the t^2 coefficient.
Exact arithmetic throughout (sympy rationals).
"""
import sys
from sympy import (Rational, bernoulli, binomial, factorial, symbols, Poly, expand,
                   simplify, S, Abs)

k = symbols("k")
LMAX = 12


def kc(r):
    """k * c^S_r(pi/k), a polynomial in k, from (4.25)."""
    tot = S(0)
    for j in range(0, r + 2):
        tot += binomial(2 * r + 2, 2 * j) * (k ** (2 * j) - 1) * bernoulli(2 * j) \
            * bernoulli(2 * r + 2 - 2 * j, Rational(1, 2))
    return expand(Rational(1, 4) * (-1) ** r / factorial(r + 1) / (2 * r + 1) * tot)


def p(nu):
    return expand(sum(Rational(2, 4 ** l) / factorial(l) * kc(nu - l) for l in range(nu + 1)))


out = []
fails = 0
for l in range(LMAX + 1):
    pl = p(l)
    P = Poly(pl, k)
    even = all(m[0] % 2 == 0 for m in P.monoms())
    deg = P.degree()
    lead = P.LC()
    claim = Abs(bernoulli(2 * l + 2)) / (2 * factorial(l + 1) * (2 * l + 1))
    signed = (-1) ** l * bernoulli(2 * l + 2) / (2 * factorial(l + 1) * (2 * l + 1))
    at1 = pl.subs(k, 1)
    ok = even and deg == 2 * l + 2 and lead == claim and lead == signed and at1 == 0 and lead != 0
    assert even, l
    assert deg == 2 * l + 2, l
    assert lead == claim == signed, l
    assert at1 == 0, l
    out.append(f"l={l:2d}  deg={deg:2d} even={even} p_l(1)={at1} lead={lead}  "
               f"|B_{2*l+2}|/(2(l+1)!(2l+1))={claim}")
    if l <= 3:
        out.append(f"       p_{l}(k) = {pl}")

# sign of Bernoulli numbers used to replace (-1)^l B_{2l+2} by |B_{2l+2}| (checked much further)
for l in range(0, 80):
    b = bernoulli(2 * l + 2)
    assert b != 0 and (b > 0) == (l % 2 == 0), l
out.append("sign(B_{2l+2}) = (-1)^l checked for l < 80")

# Cross-check l=0 with DGGW Prop 5.5: I_N/|Iso N| = (m^2-1)/(12 m)
assert simplify(p(0) / k - (k ** 2 - 1) / (12 * k)) == 0
out.append("l=0 agrees with DGGW Prop 5.5: (m^2-1)/(12m)")

# Cross-check l=2 with Schueth Thm 4.1 at constant curvature (Delta K = 0)
schueth = (Rational(1, 2520) * (k ** 5 - 1 / k) + Rational(1, 720) * (k ** 3 - 1 / k)
           + Rational(1, 180) * (k - 1 / k))
assert simplify(p(2) / k - schueth) == 0
out.append("l=2 agrees with Schueth Thm 4.1 (K^2 term; Delta K = 0)")

# Smooth part (4.35) is vol * rational constant: verified symbolically by its form; record values
nu_vals = []
for nu in range(0, 6):
    val = sum(binomial(nu, l) * (-4) ** l * bernoulli(2 * l, Rational(1, 2)) for l in range(nu + 1)) \
        / (factorial(nu) * 4 ** nu)
    nu_vals.append(f"a_{nu}/(vol*kappa^{nu}) = {val}")
assert nu_vals[0].endswith("= 1")
out += nu_vals

# Triangularity: sum_i b_l(m_i) = K^l [ lead*P_{2l+1} + ... + p_l(0)*R ], with coefficient on P_{2l+1}
# equal to K^l * lead != 0, and only odd power sums appear.
for l in range(LMAX + 1):
    P = Poly(p(l), k)
    # (1/k) p_l(k) = sum_c coeff_c k^{c-1}; c even -> odd exponents c-1 in {-1,1,...,2l+1}
    exps = sorted(m[0] - 1 for m in P.monoms())
    assert all(e % 2 == 1 or e == -1 for e in exps) and max(exps) == 2 * l + 1
out.append("each b_l(m) is a Q-combination of m^{-1}, m, m^3, ..., m^{2l+1}; top term nonzero")

# Padding: b_l(1) = 0 for all l <= LMAX; area 2pi(n-2-R) unchanged by adding an order-1 point
for l in range(LMAX + 1):
    assert p(l).subs(k, 1) == 0
out.append("b_l(1) = 0 for l <= 12; n-2-R invariant under (n,R)->(n+1,R+1)")

text = "\n".join(out)
print(text)
print("ALL CHECKS PASSED")
