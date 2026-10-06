#!/usr/bin/env python3
"""G5-bis pte-growth: Proposition 3.3 (doubling), exhaustive edge cases.  Exact arithmetic.

For every pair X != Y of n-multisets of positive integers with equal P_j (odd j <= 2L-3)
in a box, build U = X + 2Y + 2Y, V = Y + 2X + 2X, Z = U - V (cancelled), and check:
  (i)   s_j(Z) = 0 for odd j <= 2L-3 and j = -1; Z nonempty; |Z| even, <= 6n; iota(Z) = 0;
        no pair {z,-z};
  (ii)  identity s_j(U)-s_j(V) = (1-2^(j+1)) (s_j(X)-s_j(Y)) for j = -1, 1, 3, ..., 11
        (also on pairs that do NOT have equal power sums);
  (iii) the case split of the statement (1 in X only / 1 in Y only / neither / both),
        the cone counts of (0;U\\{1}) and (0;V\\{1}), hyperbolicity of both, area < 2pi(3n-2),
        and the Lemma-4 padding conditions (R, P_j, |U|=|V|) for the uncancelled pair;
  (iv)  hyperbolicity of the CANCELLED genus-0 realisation (0;U*\\{1}),(0;V*\\{1}) (needed for
        T^cone in Theorem 3.4; not claimed by Prop. 3.3) -- counted, not asserted.
Pairs that are not disjoint are included on purpose (Prop. 3.3 does not assume disjointness).
"""
import itertools, sys
from fractions import Fraction as F
from collections import Counter, defaultdict

fails = 0
def check(cond, msg):
    global fails
    if not cond:
        fails += 1
        print("FAIL " + msg)

def s(ms, j):
    return sum((F(1, x) if j == -1 else F(x) ** j) for x in ms)

def cancel(U, V):
    cu, cv = Counter(U), Counter(V)
    common = cu & cv
    return sorted((cu - common).elements()), sorted((cv - common).elements())

def chi_sum(ms):  # sum (1 - 1/m) over m in ms (1s contribute 0)
    return sum(1 - F(1, m) for m in ms)

def odd(L):
    return list(range(1, 2 * L - 2, 2))

stats = Counter()
example_bad_cancelled = []

def run_pair(X, Y, L):
    n = len(X)
    U = list(X) + [2 * y for y in Y] * 2
    V = list(Y) + [2 * x for x in X] * 2
    # (ii) identity
    for j in [-1] + list(range(1, 12, 2)):
        check(s(U, j) - s(V, j) == (1 - F(2) ** (j + 1)) * (s(X, j) - s(Y, j)), f"identity j={j} X={X} Y={Y}")
    Us, Vs = cancel(U, V)
    Z = Us + [-v for v in Vs]
    # (i)
    check(len(Z) > 0, f"Z empty X={X} Y={Y}")
    for j in odd(L) + [-1]:
        check(s(Z, j) == 0, f"s_{j}(Z) != 0 X={X} Y={Y}")
    check(len(Z) % 2 == 0 and len(Z) <= 6 * n, f"size X={X} Y={Y}")
    check(len(Us) - len(Vs) == 0, f"iota X={X} Y={Y}")
    check(not (set(Us) & set(Vs)), f"pair z,-z X={X} Y={Y}")
    # (iii) uncancelled genus-0 pair
    cX, cY = Counter(X)[1], Counter(Y)[1]
    if cX and not cY:
        case = "1 in X only"
    elif cY and not cX:
        case = "1 in Y only"
    elif not cX and not cY:
        case = "1 in neither"
    else:
        case = "1 in both"
    stats[(n, L, case)] += 1
    m = [u for u in U if u != 1]
    mp = [v for v in V if v != 1]
    check(Counter(U)[1] == cX and Counter(V)[1] == cY, "1s only from X,Y")
    check(len(mp) - len(m) == cX - cY, f"cone-count difference X={X} Y={Y}")
    if case == "1 in X only":
        check(mp == V, "(0;V) is a valid signature when 1 in X only")
        check(len(mp) - len(m) == cX, "difference = multiplicity of 1 in X")
    if case == "1 in neither":
        check(len(mp) == len(m), "equal cone counts when 1 notin X u Y")
    if case == "1 in both" and Counter(X)[1] > Counter(Y)[1]:
        stats[(n, L, "1 in X\\Y as MULTISET difference but 1 in Y: (0;V) has order-1 points")] += 1
    check(sorted(m) != sorted(mp), f"signatures equal X={X} Y={Y}")
    # Lemma 4 converse conditions for paddings U, V with g = g' = 0
    check(s(U, -1) == s(V, -1) and all(s(U, j) == s(V, j) for j in odd(L)) and len(U) == len(V), "Lemma 4 (4.2)")
    sU, sV = -2 + chi_sum(m), -2 + chi_sum(mp)
    check(sU == sV, "equal area")
    check(sU > 0, f"hyperbolic (uncancelled) X={X} Y={Y} s={sU}")
    check(sU < 3 * n - 2, f"area < 2pi(3n-2) X={X} Y={Y}")
    # (iv) cancelled realisation
    sc = -2 + chi_sum([v for v in Vs if v != 1])
    sc2 = -2 + chi_sum([u for u in Us if u != 1])
    check(sc == sc2, "cancelled equal area")
    if sc <= 0:
        stats[(n, L, case, "cancelled genus-0 realisation NOT hyperbolic")] += 1
        if len(example_bad_cancelled) < 5:
            example_bad_cancelled.append((X, Y, Us, Vs, sc))

def pairs(n, L, B):
    buckets = defaultdict(list)
    for ms in itertools.combinations_with_replacement(range(1, B + 1), n):
        buckets[tuple(sum(x ** j for x in ms) for j in odd(L))].append(ms)
    for v in buckets.values():
        for a, b in itertools.combinations(v, 2):
            yield a, b

total = 0
for (n, L, B) in [(2, 2, 40), (3, 2, 14), (4, 2, 8), (3, 3, 40), (4, 3, 16), (4, 4, 30)]:
    cnt = 0
    for X, Y in pairs(n, L, B):
        run_pair(list(X), list(Y), L)
        run_pair(list(Y), list(X), L)
        cnt += 1
    total += cnt
    print(f"n={n} L={L} entries<= {B}: {cnt} unordered pairs (each run both ways)")

# identity on pairs WITHOUT equal sums (pure algebra)
for X in itertools.combinations_with_replacement(range(1, 6), 3):
    for Y in itertools.combinations_with_replacement(range(1, 6), 3):
        U = list(X) + [2 * y for y in Y] * 2
        V = list(Y) + [2 * x for x in X] * 2
        for j in [-1] + list(range(1, 12, 2)):
            check(s(U, j) - s(V, j) == (1 - F(2) ** (j + 1)) * (s(X, j) - s(Y, j)), "identity (unconstrained)")

# U == V impossible for X != Y (generating-function argument): exhaustive small check
for n in (1, 2, 3):
    for X in itertools.combinations_with_replacement(range(1, 9), n):
        for Y in itertools.combinations_with_replacement(range(1, 9), n):
            if X != Y:
                U = sorted(list(X) + [2 * y for y in Y] * 2)
                V = sorted(list(Y) + [2 * x for x in X] * 2)
                check(U != V, f"U == V for X={X} Y={Y}")

print("case statistics:")
for k, v in sorted(stats.items(), key=str):
    print("  ", k, v)
print("examples where the cancelled genus-0 realisation is not hyperbolic:")
for e in example_bad_cancelled:
    print("  ", e)
print()
if fails:
    print(f"FAILURES: {fails}")
    sys.exit(1)
print(f"ALL CHECKS PASSED ({total} unordered pairs)")
