"""P8 part 4 (counts): do the degeneracy counts quoted in paper-core, threshold and diophantine
agree with each other and with an exact enumeration of every hyperbolic triad with S <= 600?
Exact integer arithmetic.  Run from repo root:  python3 review/audit/consistency/check_counts.py"""
import sys, os
from math import gcd
from fractions import Fraction as Fr
from collections import defaultdict
import sympy as sp

SMAX = 600
out = []
def log(s=""):
    print(s); out.append(s)

def Rkey(p, q, r):
    num, den = p * q + q * r + r * p, p * q * r
    g = gcd(num, den)
    return num // g, den // g

fib = defaultdict(list)            # (S, R) -> triads
for S in range(10, SMAX + 1):
    for p in range(2, S // 3 + 1):
        for q in range(p, (S - p) // 2 + 1):
            r = S - p - q
            num, den = p * q + q * r + r * p, p * q * r
            if num >= den:          # R >= 1: not hyperbolic
                continue
            fib[(S,) + Rkey(p, q, r)].append((p, q, r))
classes = {k: v for k, v in fib.items() if len(v) >= 2}
Npairs = defaultdict(int)
for (S, *_), v in classes.items():
    Npairs[S] += len(v) * (len(v) - 1) // 2
cum, run = {}, 0
for S in range(SMAX + 1):
    run += Npairs.get(S, 0); cum[S] = run

# ---- paper-core
assert all(Npairs.get(S, 0) == 0 for S in range(SMAX + 1) if S <= 17)
assert Npairs[18] == 1 and [v for (S, *_), v in classes.items() if S == 18] == [[(2, 8, 8), (3, 3, 12)]]
paper_tab = {18: 1, 100: 92, 200: 386, 300: 840, 400: 1496, 500: 2210, 600: 3067}
got = {S: cum[S] for S in paper_tab}
log(f"cumulative pairs N(S): {got}")
assert got == paper_tab, ("paper Table tab:density", got, paper_tab)
for S, v in paper_tab.items():   # printed ratios
    assert round(v / S, 2) == {18: 0.06, 100: 0.92, 200: 1.93, 300: 2.80, 400: 3.74, 500: 4.42, 600: 5.11}[S] or (S == 18 and abs(v / S - 0.056) < 5e-4)
    assert abs(v / S ** 2 - {18: 0.0031, 100: 0.0092, 200: 0.0097, 300: 0.0093, 400: 0.0094, 500: 0.0088, 600: 0.0085}[S]) < 5e-5
assert all(cum[S] >= S // 18 for S in range(18, SMAX + 1))                         # thm:density-lower
cl36 = sorted(v for (S, *_), v in classes.items() if S == 36)
assert cl36 == [[(4, 16, 16), (6, 6, 24)], [(6, 15, 15), (8, 8, 20)]] or sorted(map(sorted, cl36)) == sorted(map(sorted, [[(4, 16, 16), (6, 6, 24)], [(6, 15, 15), (8, 8, 20)]]))
log("paper: none for S<=17, unique pair at 18, Table tab:density (pairs) and ratios, floor(S/18) bound, two classes at S=36: OK")
# PC.17 claims every degeneracy at sum S is localized to contacts between ADJACENT least-order strata.
nonadj, same = [], 0
for (S, *_), v in classes.items():
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            d = abs(v[i][0] - v[j][0])
            same += d == 0
            if d >= 2:
                nonadj.append((S, v[i], v[j]))
assert same == 0                                       # lem:chamber: never within a stratum (PC.17 first claim OK)
assert any(S == 36 and {a, bb} == {(4, 16, 16), (6, 6, 24)} for S, a, bb in nonadj)
assert all(any(S == 18 * k and {a, bb} == {(2 * k, 8 * k, 8 * k), (3 * k, 3 * k, 12 * k)} for S, a, bb in nonadj) for k in range(2, SMAX // 18 + 1))
log(f"PC.17 'adjacent least-order strata' claim FAILS: {len(nonadj)} of {cum[SMAX]} pairs (S<=600) join strata whose least orders differ by >=2; "
    f"first: {sorted(nonadj)[:3]}; every scaled base pair k>=2 is one (strata 2k and 3k)")

# ---- threshold: 'reproduces all 2,977 collision fibres ... S<=600'
nfib = len(classes)
log(f"collision fibres (classes of size>=2) with S<=600: {nfib}; pairs: {cum[SMAX]}; sum over fibres of (C(k,2)-1) = {cum[SMAX]-nfib}")
assert nfib == 2977
sizes = defaultdict(int)
for v in classes.values():
    sizes[len(v)] += 1
log(f"fibre sizes: {dict(sorted(sizes.items()))}")
first_size = {}
for (S, *_), v in sorted(classes.items()):
    first_size.setdefault(len(v), S)
log(f"first S of fibre size k (S<=600): {dict(sorted(first_size.items()))}")
assert first_size[3] == 136 and first_size[4] == 408     # DI.6 / DI.11
assert sorted(classes[(136,) + Rkey(15, 55, 66)]) == [(15, 55, 66), (16, 40, 80), (17, 34, 85)]
assert Fr(136) * Fr(Rkey(15, 55, 66)[0], Rkey(15, 55, 66)[1]) == Fr(68, 5)
k4 = classes[[k for k, v in classes.items() if k[0] == 408 and len(v) == 4][0]]
assert all(Fr(408) * Fr(*Rkey(*t)) == Fr(68, 5) for t in k4)                       # 'the S=136 curve lambda=68/5 plus one more'
for S, trip in [(1849, [(168, 820, 861), (172, 645, 1032), (185, 480, 1184), (215, 344, 1290), (253, 276, 1320)]),
                (4600, [(750, 1750, 2100), (756, 1674, 2170), (800, 1400, 2400), (805, 1380, 2415), (882, 1170, 2548), (920, 1104, 2576)])]:
    assert all(sum(t) == S for t in trip) and len({Rkey(*t) for t in trip}) == 1 and all(Fr(*Rkey(*t)) < 1 for t in trip)
log("DI.11 size-3 at 136 (lambda=68/5), size-4 at 408 on the same curve, listed size-5/6 fibres share S and R: OK")

# first adjacent collision per least-order pair (TH.5)
first_col = {}
for (S, *_), v in sorted(classes.items()):
    ps = sorted({t[0] for t in v})
    for i in range(len(v)):
        for j in range(len(v)):
            a, bb = v[i], v[j]
            if bb[0] == a[0] + 1:
                first_col.setdefault(a[0], (S, a, bb))
th5 = {2: (18, (2, 8, 8), (3, 3, 12)), 3: (38, (3, 14, 21), (4, 6, 28)), 4: (20, (4, 8, 8), (5, 5, 10)),
       5: (117, (5, 32, 80), (6, 15, 96)), 6: (34, (6, 14, 14), (7, 9, 18)), 7: (62, (7, 20, 35), (8, 14, 40)),
       8: (64, (8, 20, 36), (9, 15, 40)), 9: (42, (9, 15, 18), (10, 12, 20)), 10: (109, (10, 44, 55), (11, 28, 70)),
       11: (66, (11, 22, 33), (12, 18, 36)), 12: (188, (12, 72, 104), (13, 45, 130)), 13: (94, (13, 39, 42), (14, 28, 52)),
       14: (69, (14, 20, 35), (15, 18, 36)), 22: (422, (22, 92, 308), (23, 77, 322))}
for p, (S, a, bb) in th5.items():
    assert first_col[p][0] == S, (p, first_col[p], S)
    assert sum(a) == sum(bb) == S and Rkey(*a) == Rkey(*bb)
log("TH.5 first adjacent collision sums and colliding pairs (p=2..14, 22): OK")

# Theorem 1 of threshold: overlap iff S >= S*(p)  (overlap: convex hulls of R-sets of strata p,p+1 meet)
def strata_R(S, p):
    vals = []
    for q in range(p, (S - p) // 2 + 1):
        r = S - p - q
        if q >= p and r >= q and Fr(1, p) + Fr(1, q) + Fr(1, r) < 1:
            vals.append(Fr(1, p) + Fr(1, q) + Fr(1, r))
    return vals
Sstar = lambda p: 18 if p == 2 else 19 if p == 3 else 3 * p + 8 if p <= 8 else 3 * p + 7
for p in range(2, 26):
    for S in range(3 * p + 3, min(SMAX, 3 * p + 40) + 1):
        A, Bv = strata_R(S, p), strata_R(S, p + 1)
        ov = bool(A) and bool(Bv) and min(A) <= max(Bv) and min(Bv) <= max(A)
        assert ov == (S >= Sstar(p)) or (not A or not Bv), (p, S)
log("threshold Theorem 1 S*(p) vs brute force overlap, p<=25: OK")

# ---- diophantine
def is_primitive_gcd(v):
    g = 0
    for t in v:
        for x in t:
            g = gcd(g, x)
    return g == 1
pairs = []
for (S, *_), v in classes.items():
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            pairs.append((S, v[i], v[j]))
prim = [pr for pr in pairs if is_primitive_gcd(pr[1:])]
def dual_of(t):
    a, bb, c = t
    e1, e2 = a + bb + c, a * bb + bb * c + c * a
    A = (e2 * a, e2 * bb, e2 * c); Bt = (e1 * bb * c, e1 * c * a, e1 * a * bb)
    g = 0
    for x in A + Bt:
        g = gcd(g, x)
    return tuple(sorted(x // g for x in A)), tuple(sorted(x // g for x in Bt))
ndual = sum(1 for (S, a, bb) in prim if set(dual_of(a)) == {a, bb})
log(f"primitive pairs (gcd of six entries = 1), S<=600: {len(prim)}; of which dual pairs: {ndual}; other: {len(prim)-ndual}")
assert len(prim) == 1753 and ndual == 423
# isolation of base pair for every multiple in range
for k in range(1, SMAX // 18 + 1):
    assert sorted(classes[(18 * k,) + Rkey(2 * k, 8 * k, 8 * k)]) == [(2 * k, 8 * k, 8 * k), (3 * k, 3 * k, 12 * k)]
log("DI.7 base-pair class has exactly two members at every S=18k<=600: OK")
# DI.9 isosceles family D_{u,v}
for u in range(1, 40):
    for v in range(u + 1, 40):
        if gcd(u, v) != 1:
            continue
        g = gcd(2 * u + v, u + 2 * v)
        assert g in (1, 3)
        A = tuple(sorted(x * (2 * u + v) // g for x in (u, v, v))); Bt = tuple(sorted(x * (u + 2 * v) // g for x in (v, u, u)))
        assert sum(A) == sum(Bt) == (2 * u + v) * (u + 2 * v) // g and Fr(*Rkey(*A)) == Fr(*Rkey(*Bt)) == Fr(g, u * v)
assert (lambda u, v: (2 * u + v) * (u + 2 * v) // gcd(2 * u + v, u + 2 * v))(1, 4) == 18
log("DI.9 D_{u,v}: S=(2u+v)(u+2v)/g, R=g/(uv), g in {1,3}, D_{1,4} = base pair: OK")
# DI.2 Weierstrass model and the integral model quoted for lambda = 27/2 (j-invariants)
lam, X = sp.symbols('lambda X')
a2, a4, a6 = (lam - 3) ** 2, 8 * (lam - 3) * (lam - 1), 16 * (lam - 1) ** 2
b2, b4, b6 = 4 * a2, 2 * a4, 4 * a6
b8 = a2 * a6 * 4 - a4 ** 2
Delta = sp.factor(-b2 ** 2 * b8 - 8 * b4 ** 3 - 27 * b6 ** 2 + 9 * b2 * b4 * b6)
assert sp.simplify(Delta - 2 ** 12 * lam ** 2 * (lam - 9) * (lam - 1) ** 3) == 0
def jinv(a2, a4, a6):
    b2, b4, b6 = 4 * a2, 2 * a4, 4 * a6
    b8 = 4 * a2 * a6 - a4 ** 2
    c4 = b2 ** 2 - 24 * b4
    D = -b2 ** 2 * b8 - 8 * b4 ** 3 - 27 * b6 ** 2 + 9 * b2 * b4 * b6
    return sp.Rational(c4) ** 3 / sp.Rational(D)
L = sp.Rational(27, 2)
assert jinv(a2.subs(lam, L), a4.subs(lam, L), a6.subs(lam, L)) == jinv(sp.Integer(393), sp.Integer(3456), sp.Integer(0)) == jinv(L ** 2 - 6 * L - 3, 16 * L, sp.Integer(0))
log("DI.2 discriminant 2^12 l^2 (l-9)(l-1)^3; C_{27/2} model and [0,393,0,3456,0] and the BGN model at n=27/2 have the same j-invariant (393=4(n^2-6n-3), 3456=16*16n): OK")

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_counts.txt"), "w") as f:
    f.write("\n".join(out) + "\nALL COUNT CHECKS PASSED\n")
print("ALL COUNT CHECKS PASSED")
