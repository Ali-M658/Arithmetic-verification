"""Attack item 5: Propositions 3.2, 3.3 and Theorem 3.4, built independently from the raw PTE inputs
and realised as orbifold pairs checked with own b_l.  Also edge cases of Prop. 3.3."""
import sys, os, random, itertools
from fractions import Fraction as F
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from mylib import psum, iota, config_level, has_pm_pair, cancel_pm, primitive, shared, area

sys.stdout.reconfigure(line_buffering=True)
fail = []


def sym(*a):
    return sorted([t for t in a] + [-t for t in a])


# ideal PTE solutions of size n = 2L-2 (degree 2L-3), as listed in LITERATURE.md (re-verified below)
PTE = {
    2: ([1, 4], [2, 3]),
    3: (sym(3, 11), sym(7, 9)),
    4: (sym(4, 9, 13), sym(1, 11, 12)),
    5: (sym(2, 16, 21, 25), sym(5, 14, 23, 24)),
    6: (sym(18, 245, 331, 471, 508), sym(103, 189, 366, 452, 515)),
    7: (sym(22, 61, 86, 127, 140, 151), sym(35, 47, 94, 121, 146, 148)),
}
ODD = {  # N_odd examples (Chen A.1.6, A.1.17, A.1.26, A.1.33 as quoted)
    3: ([1, 5, 5], [2, 3, 6]),
    4: ([1, 13, 17, 23], [3, 9, 21, 21]),
    5: ([3, 19, 37, 51, 53], [9, 11, 43, 45, 55]),
    6: ([7, 91, 173, 269, 289, 323], [29, 59, 193, 247, 311, 313]),
}
for L, (X, Y) in PTE.items():
    k = 2 * L - 3
    assert len(X) == len(Y) == k + 1 and sorted(X) != sorted(Y)
    assert all(psum(X, j) == psum(Y, j) for j in range(1, k + 1)), L
    assert psum(X, k + 1) != psum(Y, k + 1)
for L, (X, Y) in ODD.items():
    assert len(X) == L and all(psum(X, j) == psum(Y, j) for j in range(1, 2 * L - 2, 2)), L
    assert psum(X, 2 * L - 1) != psum(Y, 2 * L - 1)
print("inputs: ideal PTE solutions of degree 2L-3 for L=2..7 and odd equalities L=3..6 re-verified exactly")


def realise(Z):
    """Lemma 1.2(2): primitive integers, U=Z>0, V=-Z<0, least smaller genus with both hyperbolic."""
    P = primitive(Z)
    U = [z for z in P if z > 0]
    V = [-z for z in P if z < 0]
    io = len(U) - len(V)
    d = -io // 2  # g_U - g_V
    for gmin in range(0, 5):
        gU, gV = (gmin + d, gmin) if d >= 0 else (gmin, gmin - d)
        s1 = (gU, [u for u in U if u != 1])
        s2 = (gV, [v for v in V if v != 1])
        if area(s1) > 0 and area(s2) > 0:
            return s1, s2
    raise RuntimeError


def check_pair(tag, Z, L, need_iota=None, area_bound=None):
    Z = cancel_pm(Z)
    assert Z, tag
    lev = config_level(Z, Lmax=L + 6)
    io = iota(Z)
    s1, s2 = realise(Z)
    sh = shared(s1, s2, lmax=L + 2)
    A = area(s1)
    ok = lev >= L and sh >= L and area(s1) == area(s2) and s1 != s2
    if need_iota == 'nonzero':
        ok &= io != 0 and s1[0] != s2[0]
    if need_iota == 'zero':
        ok &= io == 0
    if area_bound is not None:
        ok &= A < area_bound
    if not ok:
        fail.append((tag, lev, sh, io))
    return len(Z), io, sh, s1, s2, A


def shift(X, Y, c):
    return [x + c for x in X] + [-(y + c) for y in Y]


def rho(X, Y, c):
    return sum(F(1) / (x + c) for x in X) - sum(F(1) / (y + c) for y in Y)


print("\nTheorem 3.4, T_L <= 4N(2L-3): shift + balanced shift, every admissible window c")
for L, (X, Y) in PTE.items():
    X, Y = [F(t) for t in X], [F(t) for t in Y]
    n = len(X)
    pts = sorted(set(X + Y))
    cands = [(a + b) / 2 for a, b in zip(pts, pts[1:])]  # t = -c in each gap
    cp = -min(pts) + F(1, 3)  # balanced window
    while rho(X, Y, cp) == 0:
        cp += 1
    best = None
    for t in cands:
        c = -t
        Zc = shift(X, Y, c)
        if iota(Zc) == 0 or rho(X, Y, c) == 0:
            continue
        lam = -rho(X, Y, cp) / rho(X, Y, c)
        Z = Zc + [lam * z for z in shift(X, Y, cp)]
        T, io, sh, s1, s2, A = check_pair(f"T_L L={L} c={c}", Z, L, 'nonzero', area_bound=2 * len(cancel_pm(Z)))
        if T > 4 * n:
            fail.append(("size", L, T))
        if best is None or T < best[0]:
            best = (T, io, sh, c, s1[0], s2[0], len(s1[1]), len(s2[1]), A)
    print(f"  L={L}: n=N(2L-3)<={n}: {len(cands)} windows tried; least T={best[0]} <= 4n={4 * n}, iota={best[1]}, "
          f"shares>={best[2]}, genera {best[4]}/{best[5]}, area/2pi={float(best[8]):.4f} < T")

print("\nProposition 3.3 / Theorem 3.4: doubling")
for L, (X, Y) in list(PTE.items()):
    # T_cone: translate so least element is 1, side containing 1 is X
    m = min(X + Y)
    Xt, Yt = [t - m + 1 for t in X], [t - m + 1 for t in Y]
    if 1 in Yt:
        Xt, Yt = Yt, Xt
    n = len(Xt)
    U = Xt + [2 * y for y in Yt] * 2
    V = Yt + [2 * x for x in Xt] * 2
    for j in [-1] + list(range(1, 2 * L, 2)):
        assert psum(U, j) - psum(V, j) == (1 - F(2) ** (j + 1)) * (psum(Xt, j) - psum(Yt, j))
    Z = cancel_pm([F(u) for u in U] + [-F(v) for v in V])
    s1 = (0, [u for u in U if u != 1]); s2 = (0, V)
    sh = shared(s1, s2, lmax=L + 2)
    A = area(s1)
    ok = (A == area(s2) and A > 0 and sh >= L and iota(Z) == 0 and len(Z) <= 6 * n and A < 3 * n - 2
          and len(s2[1]) - len(s1[1]) == Xt.count(1) and 1 in primitive(Z))
    if not ok:
        fail.append(("doubling", L))
    print(f"  L={L}: T={len(Z)} <= 6N={6 * n}; cone counts {len(s1[1])} vs {len(s2[1])}; shares {sh}; "
          f"area/2pi={float(A):.4f} < 3n-2={3 * n - 2}; contains 1: {1 in primitive(Z)}")
for L, (X, Y) in ODD.items():
    n = len(X)
    U = X + [2 * y for y in Y] * 2
    V = Y + [2 * x for x in X] * 2
    Z = cancel_pm([F(u) for u in U] + [-F(v) for v in V])
    s1 = (0, [u for u in U if u != 1]); s2 = (0, [v for v in V if v != 1])
    sh = shared(s1, s2, lmax=L + 2)
    A = area(s1)
    if not (A > 0 and sh >= L and iota(Z) == 0 and len(Z) <= 6 * n and A < 3 * n - 2):
        fail.append(("tau doubling", L))
    print(f"  tau_L, L={L}: N_odd={n}: T={len(Z)} <= 6n={6 * n}; cones {len(s1[1])}/{len(s2[1])}; shares {sh}; "
          f"area/2pi={float(A):.4f} < 3n-2={3 * n - 2}")

# Edge cases of Prop. 3.3 (L=2: equal sums only; L=3: P1,P3) over small multisets, all cases of where 1 lies
print("\nProposition 3.3 edge cases (all pairs X != Y, sizes 2..3, entries <= 12, equal odd P_j):")
cases = defaultdict(int)
nonhyp = []
for L, sizes in [(2, (2, 3)), (3, (3,))]:
    for n in sizes:
        grp = defaultdict(list)
        for ms in itertools.combinations_with_replacement(range(1, 13), n):
            grp[tuple(psum(ms, j) for j in range(1, 2 * L - 2, 2))].append(list(ms))
        for lst in grp.values():
            for X, Y in itertools.permutations(lst, 2):
                U = X + [2 * y for y in Y] * 2
                V = Y + [2 * x for x in X] * 2
                Z = cancel_pm([F(u) for u in U] + [-F(v) for v in V])
                if not Z or config_level(Z) < L or iota(Z) != 0 or len(Z) > 6 * n:
                    fail.append(("3.3 generic", X, Y))
                where = ("1inX&Y" if (1 in X and 1 in Y) else "1inX" if 1 in X else "1inY" if 1 in Y else "none")
                cases[(L, where)] += 1
                sV = (0, [v for v in V if v != 1])
                if area(sV) <= 0:
                    nonhyp.append((X, Y))
print("  cases (L, where 1 lies):", dict(cases))
print("  non-hyperbolic genus-0 realisations:", nonhyp[:5], "count", len(nonhyp))
print("  NOTE: Prop. 3.3's bullets cover only '1 in X\\Y' and '1 not in X u Y'; when 1 in Y the stated pair\n"
      "        (0;U\\{1}), (0;V) contains an order-1 'cone point' (must drop 1s from V too). Cosmetic.")

if fail:
    print("FAILURES:", fail[:10])
    sys.exit(1)
print("ALL CHECKS PASSED")
