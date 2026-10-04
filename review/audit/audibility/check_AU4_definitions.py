"""AU.4 witness table, the Phi/Q sign identity, and the definitions items DF.1, DF.6, DF.7.

Exact arithmetic (Fractions, sympy).
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import comb
from sympy import symbols, expand, prod, Poly, Rational

z = symbols("z")
out = []


def log(s):
    out.append(s)
    print(s, flush=True)


def R(ms):
    return sum(F(1, x) for x in ms)


def P(ms, k):
    return sum(x ** k for x in ms)


def Phi(m, mp):
    p = prod([z + x for x in m])
    pp = prod([z + x for x in mp])
    return expand(p * pp.subs(z, -z) - pp * p.subs(z, -z))


def Qdiff(m, mp):
    Q = prod([z - x for x in m]) * prod([z + x for x in mp])
    return expand(Q - Q.subs(z, -z))


# ---- sign identity Phi = (-1)^{n+1}(Q(z)-Q(-z)), symbolic for n=1..6 ----
for n in range(1, 7):
    a = symbols(f"a1:{n+1}")
    b = symbols(f"b1:{n+1}")
    assert expand(Phi(a, b) - (-1) ** (n + 1) * Qdiff(a, b)) == 0
log("Phi(z) = (-1)^(n+1) (Q(z)-Q(-z)) holds identically for n=1..6")

# ---- n=3 row ----
m, mp = (2, 8, 8), (3, 3, 12)
assert R(m) == R(mp) == F(3, 4) and P(m, 1) == P(mp, 1) == 18
assert (P(m, 3), P(mp, 3)) == (1032, 1782)
ph = Phi(m, mp)
assert ph == 500 * z ** 3, ph
assert sum(1 - F(1, x) for x in m) > 2 and sum(1 - F(1, x) for x in mp) > 2
log(f"n=3: {m} vs {mp}: R=3/4, S_1=P_1=18, P_3 = 1032 vs 1782, Phi = {ph}  [all as claimed]")

# ---- n=4 row ----
m, mp = (3, 10, 15, 30), (4, 5, 21, 28)
assert R(m) == R(mp) == F(8, 15) and P(m, 1) == P(mp, 1) == 58 and P(m, 3) == P(mp, 3) == 31402
assert (P(m, 5), P(mp, 5)) == (25159618, 21298618)
ph = Phi(m, mp)
assert ph == 1544400 * z ** 3, ph
assert sum(1 - F(1, x) for x in m) > 2 and sum(1 - F(1, x) for x in mp) > 2
log(f"n=4: {m} vs {mp}: R=8/15, P_1=58, P_3=31402, P_5 = {P(m,5)} vs {P(mp,5)}, Phi = {ph}  [all as claimed]")

# kappa in terms of P_{2n-3}: Q(z)-Q(-z) = 2 kappa z^3 with kappa = (P_{2n-3}(m') - P_{2n-3}(m))/(2n-3)
for (m, mp) in (((2, 8, 8), (3, 3, 12)), ((3, 10, 15, 30), (4, 5, 21, 28))):
    n = len(m)
    kappa = Rational(P(mp, 2 * n - 3) - P(m, 2 * n - 3), 2 * n - 3)
    assert Qdiff(m, mp) == 2 * kappa * z ** 3
    assert Phi(m, mp) == (-1) ** (n + 1) * 2 * kappa * z ** 3
    log(f"   n={n}: kappa = (P_(2n-3)(m') - P_(2n-3)(m))/(2n-3) = {kappa}")

# ---- n=5 counts ----
assert comb(63, 5) == 7028847 and comb(123, 5) == 216071394
log("n=5 multiset counts: C(63,5)=7,028,847 (orders 2..60), C(123,5)=216,071,394 (orders 2..120); "
    "exhaustive search itself in check_n5_search.py")

# ---- DF.1: c_1 = Area/4pi = -chi/2; pillow: (1-R)/2 ----
for (p, q, r) in ((2, 3, 7), (2, 8, 8), (3, 3, 12), (4, 4, 4)):
    chi = 2 - sum(1 - F(1, x) for x in (p, q, r))
    Rr = F(1, p) + F(1, q) + F(1, r)
    assert chi == Rr - 1
    area_over_2pi = -chi            # Gauss-Bonnet, K=-1: K*Area = 2 pi chi
    c1 = area_over_2pi / 2          # Area/(4 pi)
    assert c1 == -chi / 2 == (1 - Rr) / 2
log("DF.1: chi(O(p,q,r)) = R-1 and c_1 = Area/4pi = -chi/2 = (1-R)/2 (Gauss-Bonnet with K=-1)")

# ---- DF.6: K_mult on Pill_3, exactly, for every pillow with orders <= 60 ----
def triples_with_R(Rv):
    """All p<=q<=r, p>=2, with 1/p+1/q+1/r = Rv (finite set); integer arithmetic."""
    A, B = Rv.numerator, Rv.denominator
    res = []
    p = 2
    while 3 * B >= A * p:                       # 1/p >= R/3
        num, den = A * p - B, B * p             # rem = R - 1/p = num/den
        if num > 0:
            q = max(p, den // num + 1)          # need 1/q < rem
            while 2 * den >= num * q:           # 1/q >= rem/2
                rn, rd = num * q - den, den * q  # 1/r = rn/rd
                if rn > 0 and rd % rn == 0 and rd // rn >= q:
                    res.append((p, q, rd // rn))
                q += 1
        p += 1
    return res


def P1(t):
    return sum(t)


def P3(t):
    return sum(x ** 3 for x in t)


dist = defaultdict(int)
ex = {}
for t in combinations_with_replacement(range(2, 61), 3):
    Rv = R(t)
    if Rv >= 1:
        continue
    same_R = [u for u in triples_with_R(Rv) if u != t]
    assert t in triples_with_R(Rv)
    same_RS = [u for u in same_R if P1(u) == P1(t)]
    same_RSP = [u for u in same_RS if P3(u) == P3(t)]
    assert same_RSP == []                     # Theorem A, n=3
    K = 1 if not same_R else (2 if not same_RS else 3)
    dist[K] += 1
    ex.setdefault(K, t)
assert dist[3] > 0
K288 = [u for u in triples_with_R(F(3, 4)) if P1(u) == 18]
assert sorted(K288) == [(2, 8, 8), (3, 3, 12)]
log(f"DF.6: exact K_mult over all hyperbolic pillows with orders <= 60 (competitors unrestricted): "
    f"distribution {dict(sorted(dist.items()))}, examples {ex}; no (R,S_1,P_3) collision; "
    f"(2,8,8),(3,3,12) have K=3")

# ---- DF.7(c): hyperbolicity and numbers (the n=4 row above) ----
for ms in ((3, 10, 15, 30), (4, 5, 21, 28)):
    assert sum(1 - F(1, x) for x in ms) > 2
log("DF.7(c): both 4-multisets hyperbolic; S_1, R, P_3 equal, P_5 differ (see n=4 row)")
print("ALL CHECKS PASSED")
