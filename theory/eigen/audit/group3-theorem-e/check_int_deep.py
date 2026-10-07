"""Search for equal-area pairs with a DEEP first difference (large orders, few cone points), and
test eig:int (ii) on them: range 2<=k<=floor(Area/pi)+4, formula, integrality, Fermat divisibility.
Signatures: genus 0 with 3..6 cone points, genus 1 with 1..3, genus 2 with 0..2, orders 2..MMAX."""
import itertools, sys
from fractions import Fraction as F
from math import floor
from sympy import primerange
from heat import *

MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 40
NMAX0 = int(sys.argv[2]) if len(sys.argv) > 2 else 5
J = 14

buckets = {}
count = 0
for g, nmax in ((0, NMAX0), (1, 3), (2, 2)):
    for n in range(0, nmax + 1):
        for ms in itertools.combinations_with_replacement(range(2, MMAX + 1), n):
            R = sum((F(1, m) for m in ms), F(0))
            x = 2 * g - 2 + n - R
            if x <= 0:
                continue
            count += 1
            key = (2 * g + n - R, sum(ms) - R)       # area and Psi_1
            buckets.setdefault(key, []).append((g, ms))
print("signatures:", count, "buckets with collisions:", sum(1 for v in buckets.values() if len(v) > 1))


def first_diff(s1, s2):
    c1, c2 = c_vec(*s1, J), c_vec(*s2, J)
    for i in range(J):
        if c1[i] != c2[i]:
            return i + 1, c1[i] - c2[i]
    raise SystemExit(f"FAIL: c_1..c_{J} agree for {s1} {s2}")


hist, maxrec, npairs = {}, [], 0
for key, lst in buckets.items():
    if len(lst) < 2:
        continue
    # refine by Psi_2 cheaply to skip k=3 pairs quickly? no: test all pairs in bucket (all have k>=3)
    for s1, s2 in itertools.combinations(lst, 2):
        k, dk = first_diff(s1, s2)
        npairs += 1
        (g1, m1), (g2, m2) = s1, s2
        aop = -2 * chi(g1, m1)
        bound = floor(aop) + 4
        if not (3 <= k <= bound):
            raise SystemExit(f"FAIL range k={k} bound={bound} {s1} {s2}")
        d = int(sum((F(1, m) for m in m2), F(0)) - sum((F(1, m) for m in m1), F(0)))
        U = list(m1) + [1] * max(d, 0); V = list(m2) + [1] * max(-d, 0)
        e = 2 * k - 3
        diff = sum(u ** e for u in U) - sum(v ** e for v in V)
        if dk != (-1) ** k * a_lead(k - 2) * diff or diff == 0:
            raise SystemExit(f"FAIL formula {s1} {s2}")
        for p in primerange(2, 2 * k):
            if (2 * (k - 2)) % (p - 1) == 0 and diff % p:
                raise SystemExit(f"FAIL divisibility p={p} {s1} {s2}")
        # Separation (thm:sigsep) consistency: |U*|+|V*| >= 2(k-1)+2
        from collections import Counter
        cu, cv = Counter(U), Counter(V)
        common = cu & cv
        size = sum((cu - common).values()) + sum((cv - common).values())
        assert size >= 2 * k, (s1, s2, size, k)
        hist[k] = hist.get(k, 0) + 1
        maxrec.append((k, bound, str(aop), s1, s2, diff))
print("pairs with k>=3 tested:", npairs, "histogram:", dict(sorted(hist.items())))
maxrec.sort(key=lambda r: (-r[0], r[1]))
for r in maxrec[:8]:
    print("k=%d bound=%d Area/pi=%s %s %s P-diff=%d" % r)
tight = [r for r in maxrec if r[0] == r[1]]
print("pairs attaining k = floor(Area/pi)+4:", len(tight), tight[:3])
print("deep eig:int OK")
