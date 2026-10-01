#!/usr/bin/env python3
"""Exact-arithmetic checks for the numerical statements in theory/definitions.tex.

Run from the repository root:  python3 theory/definitions-check.py
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr


def R(m):
    return sum(F(1, x) for x in m)


def P(m, k):
    return sum(x**k for x in m)


def hyperbolic(m):
    return sum(1 - F(1, x) for x in m) > 2


# --- the n = 4 witness quoted in the restated remark ------------------------
a, b = (3, 10, 15, 30), (4, 5, 21, 28)
assert hyperbolic(a) and hyperbolic(b) and sorted(a) != sorted(b)
assert (sum(a), R(a), P(a, 3)) == (sum(b), R(b), P(b, 3)) == (58, F(8, 15), 31402)
assert P(a, 5) != P(b, 5)
print("n=4 witness: S1=58, R=8/15, P3=31402 shared; P5 =", P(a, 5), "vs", P(b, 5))

# --- rigidity-level statement used for n = 3: (R, S1, P3) separates multisets
seen = {}
for S in range(10, 121):
    for p in range(2, S // 3 + 1):
        for q in range(p, (S - p) // 2 + 1):
            r = S - p - q
            if r < q or not hyperbolic((p, q, r)):
                continue
            key = (R((p, q, r)), S, P((p, q, r), 3))
            assert key not in seen, (key, seen[key], (p, q, r))
            seen[key] = (p, q, r)
print("n=3: (R,S1,P3) injective on", len(seen), "hyperbolic multisets with 10<=S1<=120")

# --- the collision pair of Theorem B: same (R, S1), different P3 ------------
t1, t2 = (2, 8, 8), (3, 3, 12)
assert (R(t1), sum(t1)) == (R(t2), sum(t2)) == (F(3, 4), 18)
assert (P(t1, 3), P(t2, 3)) == (1032, 1782)

# --- area/c_1: c_1 = (1 - R)/2 = -chi/2 for (0;p,q,r), chi = 2 - sum(1-1/m) = R - 1
for m in [(2, 3, 7), (2, 8, 8), (3, 3, 12)]:
    chi = 2 - sum(1 - F(1, x) for x in m)
    assert chi == R(m) - 1
print("definitions-check: all assertions passed")
