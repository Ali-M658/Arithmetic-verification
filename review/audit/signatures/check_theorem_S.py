"""SG.4 (Lemma 4), SG.5 (Theorem S), SG.6 (Cor S1), SG.7 (Cor S2), SG.8 (Theorem T1), lem:sigdata.

Part 1 (Theorem S, abstract form).  For disjoint multisets U*, V* of positive integers
(1 allowed) with |U*| + |V*| even and
     R(U*) = R(V*),   P_j(U*) = P_j(V*)  (j odd, 1 <= j <= 2L-3),
Theorem S says |U*| + |V*| >= 2L+2.  Exhaustive meet-in-the-middle search over
all multisets with entries <= M and sizes a + b <= 2L (no example may exist), and a search at
a + b = 2L+2 (sharpness: examples should exist).

Part 2 (signatures).  All hyperbolic signatures with g <= 2, n <= NMAX, orders <= MMAX.
For every pair of distinct signatures sharing L >= 1 coefficients:
   Lemma 4 (4.2)/(4.3) and the mirror form; Theorem S; Cor S1; Cor S2 (L < floor(A/pi)+4);
   Theorem T1 (genus 0: L < max(n,n')).  Shared counts computed from Psi_k and,
   for all pairs with L >= 2, re-computed with the actual cone coefficients b_l.
Also T1(1): n <= A/pi + 4 with equality iff all orders 2.
"""
import os
import sys
from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement as cwr
from math import floor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sigcommon import shared_count, s_of  # noqa: E402

F = Fraction


def key(S, L):
    return (sum(F(1, x) for x in S),) + tuple(sum(x ** j for x in S) for j in range(1, 2 * L - 2, 2))


def disjoint(A, B):
    return not (set(A) & set(B))


def search(L, M, total_sizes):
    """Return list of (U*, V*) with |U*|+|V*| in total_sizes satisfying the system."""
    maxsize = max(total_sizes)
    groups = defaultdict(list)
    for a in range(0, maxsize + 1):
        for S in cwr(range(1, M + 1), a):
            groups[key(S, L)].append(S)
    found = []
    for kk, lst in groups.items():
        if len(lst) < 2:
            continue
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                A, B = lst[i], lst[j]
                if len(A) + len(B) in total_sizes and (len(A) + len(B)) % 2 == 0 and disjoint(A, B):
                    found.append((A, B))
    return found


print("Part 1: abstract Theorem S")
for L, M in [(1, 60), (2, 40), (3, 16), (4, 9)]:
    bad = search(L, M, set(range(2, 2 * L + 1, 2)))
    assert not bad, (L, bad[:3])
    print(f"  L={L}: no disjoint balanced pair with |U*|+|V*| <= {2 * L} (entries <= {M})")
for L, M in [(1, 12), (2, 12)]:
    ex = search(L, M, {2 * L + 2})
    assert ex
    print(f"  L={L}: sharp, |U*|+|V*| = {2 * L + 2} attained, e.g. {ex[0][0]} vs {ex[0][1]}  ({len(ex)} found)")

print("Part 2: signatures")
NMAX, MMAX, GMAX = 5, 18, 2
sigs = []
for g in range(GMAX + 1):
    for n in range(0, NMAX + 1):
        for m in cwr(range(2, MMAX + 1), n):
            s = s_of(g, m)
            if s > 0:
                sigs.append((g, m, s))
print(f"  {len(sigs)} hyperbolic signatures (g<={GMAX}, n<={NMAX}, orders<={MMAX})")

# T1(1)
for g, m, s in sigs:
    if g == 0:
        n = len(m)
        assert n <= 2 * s + 4  # A/pi = 2s
        assert (n == 2 * s + 4) == all(x == 2 for x in m)
print("  T1(1): n <= A/pi + 4, equality iff all orders 2: OK")


def psi_key(g, m, s, L):
    R = sum(F(1, x) for x in m)
    return (s,) + tuple(sum(x ** (2 * k - 1) for x in m) - R for k in range(1, L))


by_s = defaultdict(list)
for t in sigs:
    by_s[t[2]].append(t)


def pair_checks(t1, t2, L):
    (g, m, s), (gp, mp, _) = t1, t2
    n, nn = len(m), len(mp)
    R, Rp = sum(F(1, x) for x in m), sum(F(1, x) for x in mp)
    d = Rp - R
    assert d.denominator == 1 and d == 2 * (gp - g) + nn - n
    d = int(d)
    U = list(m) + [1] * max(d, 0)
    V = list(mp) + [1] * max(-d, 0)
    assert sum(F(1, x) for x in U) == sum(F(1, x) for x in V)
    for j in range(1, 2 * L - 2, 2):
        assert sum(x ** j for x in U) == sum(x ** j for x in V)
    assert len(V) - len(U) == 2 * (g - gp)
    assert len(U) + len(V) == 2 * max(n + g - gp, nn + gp - g)
    # mirror form, common length N
    N = max(n, nn) + 1
    mN, mpN = list(m) + [1] * (N - n), list(mp) + [1] * (N - nn)
    X = mN + [-x for x in mpN]
    assert sum(F(1, x) for x in X) == 2 * (g - gp)
    for j in range(1, 2 * L - 2, 2):
        assert sum(x ** j for x in X) == 2 * (g - gp)
    # cancel common elements
    Uc, Vc = list(U), list(V)
    for x in list(Uc):
        if x in Vc:
            Uc.remove(x)
            Vc.remove(x)
    tot = len(Uc) + len(Vc)
    assert tot >= 2 * L + 2, (t1, t2, L)
    assert L < max(n + g - gp, nn + gp - g)            # Cor S1 (contrapositive)
    assert L < floor(2 * s) + 4                         # Cor S2
    if g == 0 and gp == 0:
        assert L < max(n, nn)                           # T1(3)
    return tot


npairs = 0
hist = defaultdict(int)
tight = []
for s, grp in by_s.items():
    if len(grp) < 2:
        continue
    for i in range(len(grp)):
        for j in range(i + 1, len(grp)):
            t1, t2 = grp[i], grp[j]
            L = 1
            while psi_key(*t1, L + 1) == psi_key(*t2, L + 1):
                L += 1
                assert L < 20
            tot = pair_checks(t1, t2, L)
            npairs += 1
            hist[L] += 1
            if tot == 2 * L + 2 and L >= 2:
                tight.append((t1[:2], t2[:2], L))
            if L >= 2:
                assert shared_count(t1[0], t1[1], t2[0], t2[1], cap=L + 1) == L
print(f"  {npairs} pairs of distinct signatures with equal area; histogram of shared L: {dict(sorted(hist.items()))}")
print(f"  every pair: Lemma 4 (4.2),(4.3), mirror form, Thm S, Cor S1, Cor S2, T1(3) hold;")
print(f"  shared counts for L >= 2 re-computed with actual cone coefficients: agree")
print(f"  pairs attaining |U*|+|V*| = 2L+2 with L >= 2: {len(tight)}; e.g. {tight[:3]}")

print("ALL CHECKS PASSED")
