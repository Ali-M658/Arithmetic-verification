#!/usr/bin/env python3
"""PC.20 (rem:ncone): for 4-cone hyperbolic pillows, search for distinct order multisets
agreeing in the first 3 (resp. 4) heat coefficients.

From Ucar (4.25)/(4.33) the order-t^l cone term is kappa^l (1/m) p_l(m) with p_l of degree
2l+2 and only even powers (check_heat.py prints C_0, C_1, C_2), so at fixed K=-1 and given
the area, the first n coefficients of an n-cone pillow are equivalent to the power sums
(p_{-1}, p_1, p_3, ..., p_{2n-3}) of the orders.  Exact integer/rational arithmetic.
"""
import sys
from itertools import combinations_with_replacement
from math import gcd

M = int(sys.argv[1]) if len(sys.argv) > 1 else 80
FAIL = []
seen3, seen4 = {}, {}
hits3, hits4 = [], []
for t in combinations_with_replacement(range(2, M + 1), 4):
    a, b, c, d = t
    num = b * c * d + a * c * d + a * b * d + a * b * c
    den = a * b * c * d
    if 4 * den - num <= 2 * den:  # hyperbolic iff sum(1 - 1/m) > 2
        continue
    g = gcd(num, den)
    rec = (num // g, den // g)
    k3 = (rec, sum(t), sum(x ** 3 for x in t))
    if k3 in seen3:
        hits3.append((seen3[k3], t))
    else:
        seen3[k3] = t
    k4 = k3 + (sum(x ** 5 for x in t),)
    if k4 in seen4:
        hits4.append((seen4[k4], t))
    else:
        seen4[k4] = t
print(f"4-cone hyperbolic pillows with orders <= {M}")
print(f"  pairs agreeing in (p_-1, p_1, p_3)  [first 3 coefficients]: {len(hits3)}")
for h in hits3[:20]:
    print("   ", h)
print(f"  pairs agreeing in (p_-1, p_1, p_3, p_5) [first 4 coefficients]: {len(hits4)}")
for h in hits4[:20]:
    print("   ", h)
if hits4:
    print("FAIL: K <= 4 would be false for these 4-cone pillows")
    sys.exit(1)
print("no 4-coefficient collision found in range (consistent with K<=n for n=4 in this range)")
