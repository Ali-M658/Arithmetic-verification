#!/usr/bin/env python3
"""
P6 check: DGGW's invariant c on triangular pillows (exact arithmetic, real asserts).

DGGW (5.13): c = 2 chi(O) + sum_i (m_i - 1/m_i) = 12 x (t^0 coefficient), metric-free.
For a pillow O(p,q,r): chi = -1 + R, so c = S_1 + R - 2 with S_1 = p+q+r, R = 1/p+1/q+1/r.

Checks:
  1. The DGGW Table 2 entries (arXiv p. 29 / MMJ p. 233) agree with c = S_1 + R - 2.
  2. For hyperbolic pillows 0 < R < 1, so c alone determines (S_1, R) = (floor(c)+2, frac(c)):
     DGGW's single metric-free invariant carries exactly the information of the first two
     coefficients of a hyperbolic pillow (manuscript Cor. D).
  3. c(2,8,8) = c(3,3,12): the pair of Theorem B is a collision of DGGW's c itself, and it is
     the first one (exhaustive over S_1 <= 18), matching Theorem A/B. This is the concrete
     form of DGGW Remark 5.16 ('c does not seem sufficiently strong ...').
"""
import sys
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr

ok = True
def check(cond, msg):
    global ok
    if not cond:
        ok = False; print("FAIL:", msg)
    assert cond, msg

def c_dggw(ms, chi_underlying=2):
    chi = chi_underlying - sum(1 - F(1, m) for m in ms)
    return 2*chi + sum(m - F(1, m) for m in ms), chi

# 1. Table 2 (values as printed: chi, c)
table2 = {
    (2, 2, 2): (F(1, 2), F(11, 2)),     # 5 1/2
    (2, 3, 3): (F(1, 6), 7 + F(1, 6)),
    (2, 3, 4): (F(1, 12), 8 + F(1, 12)),
    (2, 3, 5): (F(1, 30), 9 + F(1, 30)),
    (3, 3, 3): (F(0), F(8)),
    (2, 4, 4): (F(0), F(9)),
    (2, 3, 6): (F(0), F(10)),
    (3, 3, 4): (F(-1, 12), 8 + F(11, 12)),
    (3, 4, 4): (F(-1, 6), 9 + F(5, 6)),
    (3, 3, 5): (F(-2, 15), 9 + F(13, 15)),
    (2, 4, 5): (F(-1, 20), 9 + F(19, 20)),
}
for ms, (chi_t, c_t) in table2.items():
    c, chi = c_dggw(ms)
    check(chi == chi_t and c == c_t, f"Table 2 mismatch at {ms}: {chi},{c} vs {chi_t},{c_t}")
    S1, R = sum(ms), sum(F(1, m) for m in ms)
    check(c == S1 + R - 2, f"c != S1+R-2 at {ms}")
# O(2,2,m): chi = 1/m, c = 3 + m + 1/m
for m in range(2, 50):
    c, chi = c_dggw((2, 2, m))
    check(chi == F(1, m) and c == 3 + m + F(1, m), f"O(2,2,{m})")
print("1. DGGW Table 2 reproduced; c = S_1 + R - 2 on pillows")

# 2./3. hyperbolic pillows up to S_1 = 18
hyp = [t for S in range(3, 19) for t in cwr(range(2, S), 3)
       if sum(t) == S and sum(F(1, m) for m in t) < 1]
byc = {}
for t in hyp:
    c, _ = c_dggw(t)
    R = sum(F(1, m) for m in t)
    check(0 < R < 1, "R not in (0,1)")
    check(int(c // 1) + 2 == sum(t) and c - (c // 1) == R, f"c does not encode (S1,R) at {t}")
    byc.setdefault(c, []).append(t)
coll = {c: v for c, v in byc.items() if len(v) > 1}
check(list(coll.values()) == [[(2, 8, 8), (3, 3, 12)]], f"unexpected collisions {coll}")
print(f"2. {len(hyp)} hyperbolic pillows with S_1 <= 18: c alone encodes (S_1, R)")
print(f"3. only c-collision with S_1 <= 18: {list(coll.values())[0]}, c = {list(coll.keys())[0]}")
if not ok:
    sys.exit(1)
print("ALL CHECKS PASSED")
