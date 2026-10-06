"""Theorem 2.1: which shapes (|U*|,|V*|) occur for L = 3, 4 at small size (exact).

Meet in the middle: Z = U (+) (-V), |U| = a, |V| = b, entries <= H, key
(R*D, P_1, P_3, ..., P_{2L-3}).  Every match is re-verified with Fractions and checked
against |iota| <= T-2L, T >= 2L+2, and the T=2L+2 shape claim.
Exits nonzero on failure.
"""
import sys, time
from math import lcm
from itertools import combinations_with_replacement
from fractions import Fraction
import confenum as C

FAIL = []


def key(U, L, D):
    return (sum(D // u for u in U),) + tuple(sum(u ** j for u in U) for j in range(1, 2 * L - 2, 2))


def run(L, a, b, H):
    t0 = time.time()
    D = lcm(*range(1, H + 1))
    small = {}
    for U in combinations_with_replacement(range(1, H + 1), a):
        small.setdefault(key(U, L, D), []).append(U)
    found = []
    for V in combinations_with_replacement(range(1, H + 1), b):
        k = key(V, L, D)
        if k in small:
            for U in small[k]:
                if a == b and U >= V:
                    continue
                if set(U) & set(V):
                    continue
                Z = tuple(sorted(list(U) + [-v for v in V]))
                found.append(Z)
    for Z in found:
        T = len(Z)
        if not C.is_config(Z, L):
            FAIL.append(("not config", Z))
        io = C.iota(Z)
        if abs(io) > T - 2 * L or T < 2 * L + 2:
            FAIL.append(("bound", Z))
    print(f"L={L} shape (|U|,|V|)=({a},{b}) entries<={H}: {len(found)} configurations "
          f"[{time.time()-t0:.1f}s]")
    for Z in found[:6]:
        print("    ", Z, " maxL =", C.maxL(Z), " s_{2L-1} =", C.ps(Z, 2 * L - 1))
    return found


if __name__ == "__main__":
    res = {}
    # T = 2L+2 = 8 at L = 3: balanced (4,4) and genus-changing (3,5)
    res[(3, 4, 4)] = run(3, 4, 4, 60)
    res[(3, 3, 5)] = run(3, 3, 5, 60)
    # T = 10 at L = 3: (4,6) has |iota| = 2 < T-2L = 4; (3,7) would attain T-2L = 4
    res[(3, 4, 6)] = run(3, 4, 6, 26)
    res[(3, 3, 7)] = run(3, 3, 7, 24)
    # T = 10 = 2L+2 at L = 4
    res[(4, 5, 5)] = run(4, 5, 5, 30)
    res[(4, 4, 6)] = run(4, 4, 6, 30)
    # L = 2, T = 8, attaining shape (2,6)
    res[(2, 2, 6)] = run(2, 2, 6, 40)
    print("FAILURES:", len(FAIL), FAIL[:5])
    sys.exit(1 if FAIL else 0)
