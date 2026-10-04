"""SG.9 (Proposition P) and the block lemmas used in the referee's proof of Theorem N.

Notation: eps_i = (-1)^{t(i)}, i < 2^D.  For integers h, c put
   M_j(h, c) = sum_i eps_i (h i + c)^j     (j = -1 allowed when h i + c != 0).
Checked exactly:
 (P1) M_j(h,c) = 0 for 0 <= j < D (and sum_{T0} f = sum_{T1} f for monomials i^j, j < D);
 (P2) M_{-1}(h,c) > 0 for c, h > 0 (sampled, incl. rationals);
 (B1) r(D) := M_{-1}(3,-1) < 0 for every D (the referee's block with one negative entry);
 (B2) closed form M_{D+1}(h,c) = (-1)^D 2^{D(D-1)/2} (D+1)! h^D (c + h(2^D-1)/2)  (nonzero for c > -h(2^D-1)/2).
"""
import os
import sys
from fractions import Fraction
from math import factorial

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sigcommon import thue_morse, fsum_recip  # noqa: E402

F = Fraction


def M(j, h, c, D):
    tot = F(0)
    for i in range(2 ** D):
        e = -1 if thue_morse(i) else 1
        x = F(h) * i + c
        tot += e * x ** j
    return tot


def Mint_recip(h, c, D):
    pos = [h * i + c for i in range(2 ** D) if not thue_morse(i)]
    neg = [h * i + c for i in range(2 ** D) if thue_morse(i)]
    assert all(x > 0 for x in pos + neg)
    return fsum_recip(pos) - fsum_recip(neg)


# (P1)
for D in range(1, 13):
    for j in range(D):
        s0 = sum(i ** j for i in range(2 ** D) if not thue_morse(i))
        s1 = sum(i ** j for i in range(2 ** D) if thue_morse(i))
        assert s0 == s1, (D, j)
    # degree D fails: the range "< D" is sharp
    s0 = sum(i ** D for i in range(2 ** D) if not thue_morse(i))
    s1 = sum(i ** D for i in range(2 ** D) if thue_morse(i))
    assert s0 != s1
print("(P1) equal power sums for degree < D, D <= 12, and failure at degree D: OK")

# (P2)
cnt = 0
for D in range(1, 9):
    for h in [F(1), F(2), F(3), F(1, 7), F(5, 2), F(100)]:
        for c in [F(1, 1000), F(1, 3), F(1), F(2), F(7, 3), F(50)]:
            assert M(-1, h, c, D) > 0, (D, h, c)
            cnt += 1
print(f"(P2) positivity on {cnt} sampled (D,h,c): OK")

# (B1) block with x_i = 3i - 1: exactly one negative entry (i = 0, value -1)
for D in range(1, 15):
    pos = [3 * i - 1 for i in range(1, 2 ** D) if not thue_morse(i)]
    neg = [3 * i - 1 for i in range(1, 2 ** D) if thue_morse(i)]
    r = F(-1) + fsum_recip(pos) - fsum_recip(neg)  # i=0 term is eps_0/(-1) = -1
    assert r < 0, D
    # the tail sum_{i>=1} eps_i/(3i-1) is itself negative (integral argument)
    assert r + 1 < 0
print("(B1) r(D) = sum eps_i/(3i-1) < 0 and tail < 0 for D <= 14: OK")

# (B2) closed form of the first non-vanishing moment
for D in range(1, 11):
    for (h, c) in [(3, -1), (3, 2), (1, 1), (2, 1), (5, 3)]:
        val = M(D + 1, h, c, D)
        cf = (-1) ** D * 2 ** (D * (D - 1) // 2) * factorial(D + 1) * F(h) ** D * (c + F(h) * (2 ** D - 1) / 2)
        assert val == cf, (D, h, c, val, cf)
        assert val != 0
print("(B2) closed form of M_{D+1}(h,c) for D <= 10: OK")
print("ALL CHECKS PASSED")
