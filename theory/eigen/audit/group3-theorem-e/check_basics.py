"""Sanity checks of the implementation against the stated lemmas (conepoly, triangular)."""
from fractions import Fraction as F
from heat import *

# b_0 = (m^2-1)/(12m); alpha_0=1, alpha_1=-1/3 (c_2 = chi/6)
for m in range(1, 30):
    assert b_l(0, m) == F(m * m - 1, 12 * m)
assert alpha(0) == 1 and alpha(1) == F(-1, 3)
for l in range(0, 12):
    co = p_l_coeffs(l)
    # check interpolation reproduces p_l at extra points (degree exactly 2l+2)
    for m in range(l + 3, l + 8):
        assert sum(c * F(m) ** (2 * k) for k, c in enumerate(co)) == p_l(l, m), (l, m)
    assert co[-1] == a_lead(l) and co[-1] != 0, (l, co[-1], a_lead(l))
    assert p_l(l, 1) == 0
    for m in range(2, 15):
        assert p_l(l, m) > 0
        # triangular: p_l(m)/m = sum_{k>=1} a_{l,k} psi_k(m)
        assert p_l(l, m) / m == sum(co[k] * (F(m) ** (2 * k - 1) - F(1, m)) for k in range(1, l + 2))
print("a_l:", [str(a_lead(l)) for l in range(10)])
print("alpha:", [str(alpha(k)) for k in range(6)])
print("basics OK")
