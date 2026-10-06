"""Theorem 3.1, supplementary search (m=5): for every A found by check_pencil.py's box
search (entries <= 150), look for a second full fibre B of x -> p_A(x)/x^3 consisting of
integers in [-4000, 4000] (at least m-1 = 4 integer points on one nonzero level).
Exact integer arithmetic.  This is a search, not a test of a claim: it reports hits."""
import sys
from check_pencil import sets_with_odd_zero, params, ek
m, H, splits, G = 5, 150, [2, 3], 4000
r, k0 = params(m); d = m - k0
sets = sets_with_odd_zero(m, r, H, splits)
hits = 0
for A in sets:
    e = [int(x) for x in ek(A)]
    vals = {}
    for b in range(-G, G + 1):
        if b == 0:
            continue
        p = sum((-1) ** k * e[k] * b ** (m - k) for k in range(m + 1))
        if p % b ** d:
            continue
        vals.setdefault(p // b ** d, []).append(b)
    for v, bs in vals.items():
        if v != 0 and len(bs) >= m - 1:
            print("hit: A", A, "level", v, "integer points", bs); hits += 1
print(f"m={m}: {len(sets)} sets A (entries<={H}); levels with >= {m-1} integer points in "
      f"[-{G},{G}]: {hits}")
sys.exit(0)
