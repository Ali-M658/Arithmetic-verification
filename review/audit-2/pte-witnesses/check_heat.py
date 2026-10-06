"""Check the heat-coefficient convention used by every other check in this folder.

(1) p_l is an even polynomial of degree 2l+2, p_l(1)=0, leading coeff |B_{2l+2}|/(2(l+1)!(2l+1)).
(2) b_0(m) = (m^2-1)/(12m)  (classical cone term).
(3) Cone terms and smooth terms agree EXACTLY with Ucar arXiv:1711.03405 (4.25),(4.33),(4.35)
    (fetched text, review/audit-2/sources/ucar_1711.03405.txt, p.137) for l <= 12, m <= 40.
(4) Non-certificate (mpmath, 50 digits): closed form of Phi_m(u) agrees with the trig sum
    sum_{j=1}^{m-1} 1/(4m sin(theta_j) sin(theta_j - u)) at sample points, and the series
    coefficients phi_k(m) agree with a numerical Taylor expansion.
Exits nonzero on failure.
"""
import sys
from fractions import Fraction as F
from math import factorial
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from heatlib import p_poly, peval, b, alpha, ucar_b, ucar_alpha, bern, m_phi

for l in range(0, 13):
    p = p_poly(l)
    assert all(e % 2 == 0 for e in p), l
    assert max(p) == 2 * l + 2, l
    assert peval(p, 1) == 0, l
    lead = abs(bern(2 * l + 2)) / (2 * factorial(l + 1) * (2 * l + 1))
    assert p[2 * l + 2] == lead, (l, p[2 * l + 2], lead)
print("p_l even, deg 2l+2, p_l(1)=0, leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)): l=0..12 OK")
for l in range(4):
    print(f"  p_{l}(m) =", " + ".join(f"({c})m^{e}" for e, c in sorted(p_poly(l).items())))

for m in range(1, 60):
    assert b(0, m) == F(m * m - 1, 12 * m)
print("b_0(m) = (m^2-1)/(12m), m=1..59 OK")

for l in range(0, 13):
    for m in range(1, 41):
        assert b(l, m) == ucar_b(l, m), (l, m)
for k in range(0, 14):
    assert alpha(k) == ucar_alpha(k), k
print("cone terms b_l(m) == Ucar (4.25)+(4.33) at kappa=-1 for l<=12, m<=40: OK")
print("alpha_k == Ucar (4.35) at kappa=-1 for k<=13: OK")
print("alpha_0..alpha_4 =", [str(alpha(k)) for k in range(5)])
print("b_1(m)  =", " + ".join(f"({c})m^{e - 1}" for e, c in sorted(p_poly(1).items())), "  times (-1)")

# (4) non-certificate numerical cross-check of the closed form of Phi_m
import mpmath as mp
mp.mp.dps = 50
for m in range(2, 9):
    for u in [mp.mpf('0.013'), mp.mpf('0.07'), mp.mpf('0.2')]:
        trig = sum(1 / (4 * m * mp.sin(mp.pi * j / m) * mp.sin(mp.pi * j / m - u)) for j in range(1, m))
        closed = (mp.cot(u) - m * mp.cot(m * u)) / (4 * m * mp.sin(u))
        assert abs(trig - closed) < mp.mpf(10) ** -40, (m, u)
        ser = sum(mp.mpf(peval(m_phi(k), m).numerator) / peval(m_phi(k), m).denominator / m * u ** (2 * k)
                  for k in range(0, 60))
        assert abs(ser - closed) < mp.mpf(10) ** -30, (m, u, ser, closed)
print("[non-certificate, mpmath 50 digits] Phi_m closed form == trig sum and == series, m=2..8: OK")
print("ALL OK")
