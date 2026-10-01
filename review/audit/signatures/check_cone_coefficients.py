"""SG.1 (Lemma 1), SG.2 (Lemma 2), SG.3 (Lemma 3) and the 'sum_k a_{l,k} = 0' remark in SG.4.

Derives p_l from Ucar (4.25)/(4.33), cross-checks l = 0, 1, 2 against Schueth
(arXiv:1812.06119, Remark 4.2 and Theorem 4.1), and verifies for l <= LMAX:
  * p_l even, degree 2l+2, p_l(1) = 0, leading coeff |B_{2l+2}|/(2 (l+1)! (2l+1));
  * phi_l(x) = p_l(x)/x = sum_{k=1}^{l+1} a_{l,k} psi_k(x), a_{l,k} = [x^{2k}] p_l, a_{l,l+1} != 0;
  * b_l(1) = 0 (padding);
  * reports sum_{k=1}^{l+1} a_{l,k} (= -p_l(0)), which is NOT zero.
"""
import os
import sys
from fractions import Fraction
from math import factorial

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sigcommon import p_poly, peval, bern_num, b_coef  # noqa: E402

LMAX = 14

# --- cross-check against Schueth -------------------------------------------
F = Fraction
schueth = {
    0: {0: F(-1, 12), 2: F(1, 12)},
    1: {0: F(-1, 360) - F(1, 36), 2: F(1, 36), 4: F(1, 360)},
    2: {0: -F(1, 2520) - F(1, 720) - F(1, 180), 2: F(1, 180), 4: F(1, 720), 6: F(1, 2520)},
}
for l, d in schueth.items():
    P = p_poly(l)
    for i, c in enumerate(P):
        assert c == d.get(i, 0), (l, i, c, d.get(i, 0))
print("Schueth cross-check l=0,1,2: OK")

print("l | deg | p_l(1) | lead == |B|/(2(l+1)!(2l+1)) | a_{l,l+1} | sum_{k>=1} a_{l,k} = -p_l(0)")
nonzero_sum = []
for l in range(LMAX + 1):
    P = p_poly(l)
    deg = len(P) - 1
    assert deg == 2 * l + 2, (l, deg)
    assert all(P[i] == 0 for i in range(1, deg + 1, 2)), "p_l not even"
    assert sum(P) == 0, "p_l(1) != 0"
    lead = abs(bern_num(2 * l + 2)) / (2 * factorial(l + 1) * (2 * l + 1))
    assert P[-1] == lead and lead != 0
    # Lemma 2: phi_l = p_l/x = P0/x + sum_{k>=1} P_{2k} x^{2k-1}
    #        = sum_{k>=1} P_{2k} (x^{2k-1} - x^{-1})   because P0 = -sum_{k>=1} P_{2k}
    a = [P[2 * k] for k in range(1, l + 2)]
    assert P[0] == -sum(a)
    for x in [F(2), F(3), F(7), F(1, 3), F(-5)]:
        lhs = peval(P, x) / x
        rhs = sum(a[k - 1] * (x ** (2 * k - 1) - 1 / x) for k in range(1, l + 2))
        assert lhs == rhs
    assert a[-1] != 0
    # Lemma 3
    assert b_coef(l, 1) == 0
    s = sum(a)
    if s != 0:
        nonzero_sum.append(l)
    print(f"{l:2d} | {deg:3d} | {sum(P)} | {lead} | {a[-1]} | {s}")

# The remark in SG.4 ("because sum_k a_{l,k} = 0") is false with Lemma 2's indexing:
assert nonzero_sum == list(range(LMAX + 1))
print("sum_{k=1}^{l+1} a_{l,k} = -p_l(0) is nonzero for every l <= %d;" % LMAX)
print("the identity that IS true (and is what the mirror-multiset argument needs) is")
print("sum_{k=0}^{l+1} [x^{2k}] p_l = p_l(1) = 0.")
print("ALL CHECKS PASSED")
