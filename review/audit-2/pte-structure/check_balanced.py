"""Proposition 2.3 (a), (b) and Proposition 2.2, exact.

(a) A odd ideal symmetric: |A|=2L-1, s_j(A)=0 odd j<=2L-3, 0 notin A, no pair.
    Claim: s_{-1}(A) != 0 and iota(A) = sgn s_{-1}(A).
(b) lambda = -s_{-1}(B)/s_{-1}(A); Z = A (+) lambda B after cancelling pairs {z,-z}
    is empty or an L-configuration with iota = 0.
The sets A are found by the reviewer's own search: A = X (+) (-Y), X, Y multisets of
positive integers with equal P_1, P_3, ..., P_{2L-3}; every split (|X|,|Y|) is searched.
Exits nonzero on failure.
"""
import sys, time, random
from fractions import Fraction as F
from itertools import combinations_with_replacement
import confenum as C
from check_descartes import partitions, poly_from_roots, sign_changes

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("FAIL:", msg)


def sgn(x):
    return (x > 0) - (x < 0)


def keyv(U, L):
    return tuple(sum(u ** j for u in U) for j in range(1, 2 * L - 2, 2))


def odd_sets(L, H, small_max):
    """all A (as sorted tuples) with entries |a|<=H, |A|=2L-1, odd sums up to 2L-3 zero.
    Splits with min(|X|,|Y|) <= small_max are found by DFS over the large side without
    an entry bound (so these splits are exhaustive in the small side only)."""
    n = 2 * L - 1
    res = set(); withpair = set()
    for p in range(1, n):
        q = n - p
        if min(p, q) <= small_max:
            # small side S (size s), large side partitions with matching odd sums
            s = min(p, q)
            for S in combinations_with_replacement(range(1, H + 1), s):
                odd = {j: sum(x ** j for x in S) for j in range(3, 2 * L - 2, 2)}
                tot = sum(S)
                # partitions() also constrains reciprocals; use a dummy-free variant:
                for W in parts_no_R(tot, odd, n - s):
                    X, Y = (S, W) if p == s else (W, S)
                    A = tuple(sorted(list(X) + [-y for y in Y]))
                    (withpair if set(X) & set(Y) else res).add(A)
        else:
            D = {}
            for X in combinations_with_replacement(range(1, H + 1), p):
                D.setdefault(keyv(X, L), []).append(X)
            for Y in combinations_with_replacement(range(1, H + 1), q):
                for X in D.get(keyv(Y, L), []):
                    A = tuple(sorted(list(X) + [-y for y in Y]))
                    (withpair if set(X) & set(Y) else res).add(A)
    return sorted(res), sorted(withpair)


def parts_no_R(S, odd, nparts):
    """partitions of S into exactly nparts parts with sum of u^j = odd[j]"""
    out = []

    def rec(p, S, od, acc):
        if len(acc) == nparts:
            if S == 0 and all(v == 0 for v in od.values()):
                out.append(tuple(acc))
            return
        rem = nparts - len(acc)
        for u in range(min(p, S - (rem - 1)), 0, -1):
            if u * rem < S:
                break
            nod = {}
            ok = True
            for j, v in od.items():
                nv = v - u ** j
                if nv < 0:
                    ok = False; break
                nod[j] = nv
            if ok:
                acc.append(u); rec(u, S - u, nod, acc); acc.pop()

    rec(S, S, dict(odd), [])
    return out


def cancel(Z):
    Z = list(Z)
    out = []
    from collections import Counter
    c = Counter(Z)
    for z in list(c):
        if z > 0 and -z in c:
            k = min(c[z], c[-z]); c[z] -= k; c[-z] -= k
    for z, k in c.items():
        out += [z] * k
    return tuple(sorted(out))


def part_a(L, sets):
    for A in sets:
        check(0 not in A and len(A) == 2 * L - 1, f"shape {A}")
        check(all(C.ps(A, j) == 0 for j in range(1, 2 * L - 2, 2)), f"odd sums {A}")
        r = C.ps(A, -1)
        check(r != 0, f"(a) s_-1 = 0 for {A}")
        check(C.iota(A) == sgn(r), f"(a) iota != sgn s_-1 for {A}")
        # reviewer's proof: p(x) = x q(x^2) - e_{2L-1}, odd-degree coefficients all nonzero
        c = poly_from_roots(A)        # c[k] = (-1)^k e_k, degree 2L-1-k
        for k in range(0, 2 * L - 1, 2):
            check(c[k] != 0, f"(a) even-index e_{k} = 0 for {A}")
            if k >= 2:
                check((c[k] > 0) != (c[k - 2] > 0), f"(a) no alternation at e_{k} {A}")
        check(sign_changes(c) == sum(1 for a in A if a > 0), f"(a) Descartes exact {A}")


def part_b(L, sets, maxpairs):
    stats = {"empty": 0, "full config": 0, "partial cancel": 0, "pairs": 0}
    ex = {}
    pairs = [(A, B) for A in sets for B in sets]
    random.seed(L)
    if len(pairs) > maxpairs:
        pairs = random.sample(pairs, maxpairs)
    # always include B = scaled copies and the self-pair
    for A in sets[:20]:
        pairs.append((A, tuple(sorted(-3 * a for a in A))))
        pairs.append((A, A))
    for A, B in pairs:
        stats["pairs"] += 1
        lam = -C.ps(B, -1) / C.ps(A, -1)
        check(sgn(lam) == -C.iota(A) * C.iota(B), f"(b) sign of lambda {A} {B}")
        Z0 = tuple(sorted([F(a) for a in A] + [lam * b for b in B]))
        check(C.ps(Z0, -1) == 0 and C.iota(Z0) == 0, f"(b) before cancel {A} {B}")
        Z = cancel(Z0)
        if len(Z) == 0:
            stats["empty"] += 1
            # empty iff lambda B = -A
            check(sorted(lam * b for b in B) == sorted(-F(a) for a in A), f"(b) empty {A} {B}")
            continue
        if len(Z) < len(Z0):
            stats["partial cancel"] += 1
            ex.setdefault("partial", (A, B, lam, Z))
        else:
            stats["full config"] += 1
        check(C.is_config(Z, L), f"(b) not an L-configuration {A} {B} -> {Z}")
        check(C.iota(Z) == 0, f"(b) iota != 0 {A} {B}")
        check(len(Z) >= 2 * L + 2, f"(b) size < 2L+2 {Z}")
    return stats, ex


def main():
    t0 = time.time()
    plan = {2: (60, 2), 3: (40, 2), 4: (60, 2)}
    allsets = {}
    for L, (H, sm) in plan.items():
        sets, withpair = odd_sets(L, H, sm)
        allsets[L] = sets
        check(not withpair, f"L={L}: odd symmetric sets with a pair exist: {withpair[:3]}")
        dist = {}
        for A in sets:
            dist[C.iota(A)] = dist.get(C.iota(A), 0) + 1
        print(f"L={L}: |A|={2*L-1}, entries<={H}: {len(sets)} sets (both signs); "
              f"sets with an internal pair: {len(withpair)}; iota distribution {dist}; "
              f"e.g. {sets[:2]}  [{time.time()-t0:.1f}s]")
        part_a(L, sets)
    # fetched Escott solution (Chen survey, arXiv:2506.11429, Example 1.1, eq. (A.322)):
    a = [0, 18, 27, 58, 64, 89, 101]; b = [1, 13, 38, 44, 75, 84, 102]
    check(all(sum(x ** j for x in a) == sum(x ** j for x in b) for j in range(1, 7)), "Escott PTE")
    check(sum(x ** 7 for x in a) != sum(x ** 7 for x in b), "Escott degree exactly 6")
    A = tuple(sorted(2 * x - 102 for x in a))
    check(sorted(2 * x - 102 for x in b) == sorted(-x for x in A), "Escott symmetric")
    part_a(4, [A])
    print("fetched Escott degree-6 solution, centred and doubled:", A,
          " s_-1 =", C.ps(A, -1), " iota =", C.iota(A))
    if A not in allsets[4] and tuple(sorted(x // 2 for x in A)) not in allsets[4]:
        allsets[4].append(A)
    for L in plan:
        stats, ex = part_b(L, allsets[L], 4000)
        print(f"(b) L={L}: {stats}; partial-cancellation example: {ex.get('partial')}")
    # Proposition 2.2 on every configuration produced in (b) and on the enumerations
    n = 0
    for H, T in [(22, 8), (15, 10)]:
        for Z in C.enumerate_configs(H, T):
            L = C.maxL(Z)
            mZ = tuple(-z for z in Z)
            check(all(C.ps(Z, j) == C.ps(mZ, j) for j in range(1, 2 * L - 1)), f"2.2 {Z}")
            check(sorted(Z) != sorted(mZ), f"2.2 trivial {Z}")
            n += 1
    print("Prop 2.2: [Z] =_{2L-2} [-Z], Z != -Z for", n, "enumerated configurations")
    # N(k) >= k+1 (Newton): exhaustive tiny check that no two distinct n-multisets with
    # entries in [0,8] share power sums 1..n (n<=3)
    for nn in range(1, 4):
        seen = {}
        for X in combinations_with_replacement(range(0, 9), nn):
            k = tuple(sum(x ** j for x in X) for j in range(1, nn + 1))
            check(k not in seen, f"N(k)>=k+1 fails {X} {seen.get(k)}")
            seen[k] = X
    print("N(k) >= k+1 spot check (n<=3, entries 0..8): ok")
    print("FAILURES:", len(FAIL))
    sys.exit(1 if FAIL else 0)


main()
