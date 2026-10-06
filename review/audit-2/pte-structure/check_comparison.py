"""Comparison phase: reconcile the producer's count of odd symmetric 5-sets
(theory/pte/attack/a03_symmetric_pencil.py: '102 primitive, entries<=40', where only three
of the five entries are bounded) with check_balanced.py (all five entries <= 40).
Re-implements the producer's enumeration independently (exact integers)."""
import sys, itertools
from math import gcd, isqrt
from functools import reduce
import confenum as C
from check_balanced import odd_sets
five = set()
for a, b, c in itertools.combinations(range(-40, 41), 3):
    if 0 in (a, b, c):
        continue
    sg = -(a + b + c); tau = -(a**3 + b**3 + c**3)
    if sg == 0 or (sg**3 - tau) % (3 * sg):
        continue
    p = (sg**3 - tau) // (3 * sg); D = sg * sg - 4 * p
    if D < 0 or isqrt(D)**2 != D or (sg + isqrt(D)) % 2:
        continue
    r = isqrt(D); S = sorted([a, b, c, (sg + r)//2, (sg - r)//2])
    if 0 in S or any(-t in S for t in S):
        continue
    g = reduce(gcd, [abs(t) for t in S]); five.add(tuple(t // g for t in S))
inbox = {A for A in five if max(abs(t) for t in A) <= 40}
mine, _ = odd_sets(3, 40, 2)
mine_prim = {tuple(sorted(t // reduce(gcd, [abs(u) for u in A]) for t in A)) for A in mine}
print("producer-style count (3 entries bounded by 40, primitive):", len(five))
print("  of these with all 5 entries <= 40:", len(inbox))
print("reviewer (all entries <= 40), primitive:", len(mine_prim))
ok = inbox <= mine_prim
print("in reviewer list, not in producer-style list:", sorted(mine_prim - inbox))
print("producer's all-in-box sets contained in reviewer's list:", ok)
sys.exit(0 if ok else 1)
