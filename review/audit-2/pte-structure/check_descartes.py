"""Theorem 2.1 (Descartes bound) and Lemma 1.2(4): exhaustive and targeted searches.

Claims tested:
  (T21)  every L-configuration has |iota| <= T-2L            (equivalently P>=L and N>=L)
  (T21.1) orbifold form |U*|+|V*| >= 2L+2|g-g'|               (same inequality, iota=2(g'-g))
  (T21.2) T=2L+2  =>  iota in {0,+-2}
  (L12.4) T even and T >= 2L+2
Reviewer's proof (REVIEW.md): p(x)=prod(x-z) has e_k=0 for odd k<=2L-3 and e_{T-1}=0
(s_{-1}=e_{T-1}/e_T), so at most T-L+1 nonzero coefficients; Descartes gives P,N<=T-L.
Each enumerated configuration is also checked against this certificate.
Exact integer / Fraction arithmetic.  Exits nonzero on any failure.
"""
import sys, time
from fractions import Fraction
from collections import Counter, defaultdict
from itertools import combinations_with_replacement
import confenum as C

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("FAIL:", msg)


def poly_from_roots(Z):
    """coefficients of prod (x - z), highest degree first, exact"""
    c = [Fraction(1)]
    for z in Z:
        n = c + [Fraction(0)]
        for i in range(len(c)):
            n[i + 1] -= z * c[i]
        c = n
    return c


def sign_changes(c):
    s = [x for x in c if x != 0]
    return sum(1 for a, b in zip(s, s[1:]) if (a > 0) != (b > 0))


def certificate(Z, L):
    T = len(Z)
    c = poly_from_roots(Z)            # c[k] = (-1)^k e_k
    for k in range(1, 2 * L - 2, 2):
        check(c[k] == 0, f"e_{k} != 0 for {Z}")
    check(c[T - 1] == 0, f"e_(T-1) != 0 for {Z}")
    nz = sum(1 for x in c if x != 0)
    check(nz <= T - L + 1, f"too many nonzero coefficients {Z}")
    cm = [x * (-1) ** (T - k) for k, x in enumerate(c)]  # p(-x) up to sign
    P = sum(1 for z in Z if z > 0); N = T - P
    check(P <= sign_changes(c) <= T - L, f"Descartes positive {Z}")
    check(N <= sign_changes(cm) <= T - L, f"Descartes negative {Z}")


def part_A():
    print("== Part A: exhaustive enumeration of integer configurations ==")
    attained = defaultdict(list)
    for H, Tmax in [(30, 6), (22, 8), (15, 10), (10, 12)]:
        t0 = time.time()
        Zs = C.enumerate_configs(H, Tmax)
        stats = Counter()
        for Z in Zs:
            T = len(Z); io = C.iota(Z); Ls = C.maxL(Z)
            check(C.is_config(Z, Ls), f"enumeration produced non-config {Z}")
            for L in range(1, Ls + 1):
                check(abs(io) <= T - 2 * L, f"DESCARTES VIOLATION L={L} {Z}")
                check(T % 2 == 0 and T >= 2 * L + 2, f"size bound L={L} {Z}")
                if T == 2 * L + 2:
                    check(io in (0, 2, -2), f"size 2L+2 iota {Z}")
                if abs(io) == T - 2 * L and io != 0:
                    attained[(L, T)].append(Z)
            certificate(Z, Ls)
            stats[(T, Ls, io)] += 1
        print(f"H={H} T<={Tmax}: {len(Zs)} configurations (Z and -Z both counted), "
              f"{time.time()-t0:.1f}s")
        for k in sorted(stats):
            print("   (T, maxL, iota) =", k, "count", stats[k])
    print("attainment |iota| = T-2L > 0 (first example per (L,T)):")
    for k in sorted(attained):
        print("  ", k, len(attained[k]), "e.g.", attained[k][0])
    return attained


def partitions(S, Rr, odd, maxpart, nparts_max, Lsum):
    """multisets U of positive ints <= maxpart with sum S, sum 1/u = Rr (Fraction),
    and sum u^j = odd[j] for j in odd (dict), |U| <= nparts_max.  DFS, nonincreasing."""
    out = []

    def rec(p, S, Rr, od, acc):
        if S == 0:
            if Rr == 0 and all(v == 0 for v in od.values()):
                out.append(tuple(acc))
            return
        if len(acc) >= nparts_max or Rr <= 0:
            return
        for u in range(min(p, S), 0, -1):
            # feasibility for remaining parts all <= u
            if Rr > S:               # 1/w <= w for w>=1
                return
            if Rr < Fraction(S, u * u):   # 1/w >= w/u^2 for w <= u
                break                 # smaller u makes the bound only larger? no: S/u^2 grows as u shrinks
            nod = {}
            ok = True
            for j, v in od.items():
                nv = v - u ** j
                if nv < 0:
                    ok = False; break
                nod[j] = nv
            if not ok:
                continue
            acc.append(u)
            rec(u, S - u, Rr - Fraction(1, u), nod, acc)
            acc.pop()

    rec(maxpart, S, Rr, dict(odd), [])
    return out


def part_B():
    """targeted search for violators: N = |V| <= L-1 negatives (by Z -> -Z this is WLOG)."""
    print("== Part B: targeted search for Descartes violators (N <= L-1) ==")
    for L, HV in [(2, 400), (3, 60), (4, 18)]:
        t0 = time.time(); nV = 0; found = 0
        for q in range(1, L):
            for V in combinations_with_replacement(range(1, HV + 1), q):
                nV += 1
                S = sum(V); Rr = sum(Fraction(1, v) for v in V)
                odd = {j: sum(v ** j for v in V) for j in range(3, 2 * L - 2, 2)}
                for U in partitions(S, Rr, odd, S, 10 ** 6, None):
                    if set(U) & set(V):
                        continue
                    Z = tuple(sorted(list(U) + [-v for v in V]))
                    if len(Z) % 2:
                        continue
                    found += 1
                    check(False, f"VIOLATOR L={L}: {Z}")
        print(f"L={L}: all V with |V|<=L-1, entries<={HV} ({nV} multisets), every U "
              f"(no bound on |U| or its entries): violators found = {found}  "
              f"[{time.time()-t0:.1f}s]")


if __name__ == "__main__":
    # sanity: the pruning in partitions() must not lose solutions.  Cross-check on a
    # brute force for small sums.
    for S in range(1, 19):
        for Rnum in [Fraction(1), Fraction(5, 6), Fraction(3, 2)]:
            brute = set()
            def gen(p, s, acc):
                if s == 0:
                    if sum(Fraction(1, a) for a in acc) == Rnum:
                        brute.add(tuple(acc))
                    return
                for u in range(min(p, s), 0, -1):
                    acc.append(u); gen(u, s - u, acc); acc.pop()
            gen(S, S, [])
            got = set(partitions(S, Rnum, {}, S, 10 ** 6, None))
            check(got == brute, f"partition pruning lost solutions S={S} R={Rnum}")
    print("partition-DFS pruning cross-checked against brute force for S<=18")
    part_A()
    part_B()
    print("FAILURES:", len(FAIL))
    sys.exit(1 if FAIL else 0)
