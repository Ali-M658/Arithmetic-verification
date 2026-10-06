#!/usr/bin/env python3
"""G5-bis pte-growth: Theorem 3.4 (upper bounds) built on explicit data, every condition checked
exactly (Fractions).  For L = 2, 3, 4 (PTE degrees 1, 3, 5):

  * PTE solutions of degree 2L-3 and size 2L-2 = N(2L-3) are found by OUR OWN search
    (degree 1, 3: exhaustive box; degree 5: the symmetric family {a,b,a+b} with equal
    a^2+ab+b^2, checked exhaustively in a box) and cross-checked with eslpower's
    (k=1,..,5) entry [0,5,6,16,17,22] = [1,2,10,12,20,21].
  * tau_L <= 6 N_odd(L): doubling of the N_odd witnesses.
  * T^cone_L <= 6 N(2L-3): cancel, shift min to 1, double; Z contains 1 (primitive), iota = 0,
    cancelled genus-0 realisation hyperbolic.
  * T_L <= 4 N(2L-3): shift construction Z(c) u lambda Z(c'), iota != 0.
  For each configuration: Definition 1.1 (nonempty, nonzero, s_j = 0 odd j <= 2L-3, s_{-1} = 0,
  no {z,-z}, |Z| even), and the orbifold realisation of Lemma 1.2(2) (assumed, PS.0): Lemma-4
  conditions (4.2), genus difference, hyperbolicity, area bounds (Lemma 1.2(5), Thm 4.3 thresholds).
Also: the Prop. 3.3 multiset-difference example where "(0;V)" contains points of order 1.
"""
import itertools, math, sys
from fractions import Fraction as F
from collections import Counter, defaultdict

fails = 0
def check(cond, msg):
    global fails
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        fails += 1

def s(ms, j):
    return sum((1 / F(x) if j == -1 else F(x) ** j) for x in ms)

def odd(L):
    return list(range(1, 2 * L - 2, 2))

def cancel_pairs(Z):
    """remove pairs {z,-z} repeatedly (multiset)."""
    c = Counter(Z)
    for z in list(c):
        if z > 0 and -z in c:
            k = min(c[z], c[-z]); c[z] -= k; c[-z] -= k
    return sorted(c.elements())

def is_config(Z, L):
    ok = (len(Z) > 0 and all(z != 0 for z in Z) and len(Z) % 2 == 0
          and all(s(Z, j) == 0 for j in odd(L)) and s(Z, -1) == 0
          and not any(-z in Z for z in Z if z > 0))
    return ok

def iota(Z):
    return sum(1 for z in Z if z > 0) - sum(1 for z in Z if z < 0)

def primitive(Z):
    den = 1
    for z in Z:
        den = den * F(z).denominator // math.gcd(den, F(z).denominator)
    ints = [int(F(z) * den) for z in Z]
    g = 0
    for x in ints:
        g = math.gcd(g, abs(x))
    return [x // g for x in ints]

def chi_sum(ms):
    return sum(1 - F(1, m) for m in ms)

def realise(Z, L):
    """Lemma 1.2(2) (assumed as stated in PS.0): returns (g, m, g', m', s) or raises."""
    P = primitive(Z)
    U = sorted(z for z in P if z > 0); V = sorted(-z for z in P if z < 0)
    io = len(U) - len(V)
    assert io % 2 == 0
    # (4.2): R(U) = R(V), P_j equal, |V|-|U| = 2(g-g')
    assert s(U, -1) == s(V, -1) and all(s(U, j) == s(V, j) for j in odd(L))
    d = -io // 2       # g - g'
    m = [u for u in U if u != 1]; mp = [v for v in V if v != 1]
    for gmin in range(0, 10):
        g, gp = (gmin + d, gmin) if d >= 0 else (gmin, gmin - d)
        sg = 2 * g - 2 + chi_sum(m); sgp = 2 * gp - 2 + chi_sum(mp)
        assert sg == sgp
        if sg > 0:
            return g, m, gp, mp, sg, P
    raise AssertionError("no hyperbolic genus")

# ---------- own PTE searches ----------
def pte_search(k, n, B):
    seen = {}
    for ms in itertools.combinations_with_replacement(range(0, B + 1), n):
        key = tuple(sum(x ** j for x in ms) for j in range(1, k + 1))
        if key in seen and not (set(seen[key]) & set(ms)):
            return list(seen[key]), list(ms)
        seen.setdefault(key, ms)
    return None

pte = {}
r = pte_search(1, 2, 6); pte[1] = r
check(r is not None, f"own degree-1 size-2 PTE solution: {r}")
r = pte_search(3, 4, 12); pte[3] = r
check(r is not None, f"own degree-3 size-4 PTE solution: {r}")
# degree 5 size 6: symmetric family. {a,b,a+b} has sum x^2 = 2Q, sum x^4 = 2Q^2 with Q = a^2+ab+b^2.
found = None
byQ = defaultdict(list)
for a in range(0, 12):
    for b in range(a, 12):
        byQ[a * a + a * b + b * b].append((a, b))
for Q, lst in sorted(byQ.items()):
    if len(lst) >= 2:
        (a, b), (c, d) = lst[0], lst[1]
        A = sorted([a, b, a + b, -a, -b, -(a + b)]); B = sorted([c, d, c + d, -c, -d, -(c + d)])
        if not (set(A) & set(B)):
            found = (A, B); break
pte[5] = found
check(found is not None, f"own degree-5 size-6 PTE solution (symmetric family): {found}")
for k in (1, 3, 5):
    A, B = pte[k]
    check(len(A) == len(B) == k + 1 and sorted(A) != sorted(B)
          and all(s(A, j) == s(B, j) for j in range(1, k + 1)), f"degree {k}: equal P_1..P_{k}, size {k+1}")
esl = ([0, 5, 6, 16, 17, 22], [1, 2, 10, 12, 20, 21])
check(all(s(esl[0], j) == s(esl[1], j) for j in range(1, 6)), "eslpower (k=1..5) entry re-verified")

def doubling(X, Y):
    U = list(X) + [2 * y for y in Y] * 2
    V = list(Y) + [2 * x for x in X] * 2
    cu, cv = Counter(U), Counter(V); com = cu & cv
    Us = sorted((cu - com).elements()); Vs = sorted((cv - com).elements())
    return U, V, Us + [-v for v in Vs]

Nodd = {2: ([1, 4], [2, 3]), 3: ([1, 5, 5], [2, 3, 6]), 4: ([1, 13, 17, 23], [3, 9, 21, 21])}

for L in (2, 3, 4):
    k = 2 * L - 3
    N = k + 1                         # N(k) = k+1 for k <= 9 (ideal solutions; CMSV p.2)
    print(f"===== L = {L}, k = 2L-3 = {k}, N(k) = {N}")
    # tau_L <= 6 N_odd(L)
    X, Y = Nodd[L]
    U, V, Z = doubling(X, Y)
    check(is_config(Z, L) and iota(Z) == 0 and len(Z) <= 6 * len(X),
          f"tau: doubling of N_odd witness gives L-config, |Z|={len(Z)} <= 6*{len(X)}, iota=0")
    check(len(Z) >= 2 * L + 2, f"tau: |Z| >= 2L+2 = {2*L+2} (Lemma 1.2(4) consistency)")
    # T^cone
    A, B = pte[k]
    ca, cb = Counter(A), Counter(B); com = ca & cb
    A1 = sorted((ca - com).elements()); B1 = sorted((cb - com).elements())
    c0 = 1 - min(A1 + B1)
    X = [a + c0 for a in A1]; Y = [b + c0 for b in B1]
    if 1 in Y:
        X, Y = Y, X
    check(1 in X and 1 not in Y and min(X + Y) >= 1, f"T^cone: shifted, disjoint, 1 in X only: X={X} Y={Y}")
    check(all(s(X, j) == s(Y, j) for j in range(1, k + 1)), "T^cone: shift preserves P_1..P_k")
    U, V, Z = doubling(X, Y)
    check(is_config(Z, L) and iota(Z) == 0, f"T^cone: Z is a balanced L-config, |Z|={len(Z)}")
    check(len(Z) <= 6 * N, f"T^cone: |Z| = {len(Z)} <= 6N(2L-3) = {6*N}")
    P = primitive(Z)
    check(P == Z and 1 in Z, "T^cone: Z primitive integral and contains 1")
    Us = [z for z in Z if z > 0 and z != 1]; Vs = [-z for z in Z if z < 0]
    sc = -2 + chi_sum(Vs)
    check(sc > 0 and sc == -2 + chi_sum(Us), f"T^cone: cancelled genus-0 realisation hyperbolic, Area/2pi = {sc}")
    check(len(Vs) - len(Us) == Counter(Z)[1], "T^cone: cone counts differ by multiplicity of 1")
    # uncancelled pair of Prop 3.3 (used by Thm 4.3 f_n)
    m = [u for u in U if u != 1]
    su = -2 + chi_sum(V)
    check(su > 0 and su == -2 + chi_sum(m) and su < 3 * len(X) - 2,
          f"Prop 3.3 pair (0;U\\1),(0;V): hyperbolic, Area/2pi = {su} < 3n-2 = {3*len(X)-2}")
    check(su <= 3 * N - 2, f"Thm 4.3 f_n threshold: Area/2pi = {su} <= 3N(2L-3)-2 = {3*N-2}")
    # T_L via shift
    X, Y = A1, B1
    vals = sorted(set(X + Y))
    def Zc(c):
        return [F(x) + c for x in X] + [-(F(y) + c) for y in Y]
    def rho(c):
        return sum(1 / (F(x) + c) for x in X) - sum(1 / (F(y) + c) for y in Y)
    c = None
    # search c in the gaps between consecutive values for iota != 0 and rho != 0
    for i in range(len(vals) - 1):
        for t in (F(1, 2), F(1, 3), F(2, 3), F(1, 5)):
            cand = -(vals[i] + t * (vals[i + 1] - vals[i]))
            if iota(Zc(cand)) != 0 and rho(cand) != 0:
                c = cand; break
        if c is not None:
            break
    cp = F(1 - min(vals))
    while rho(cp) == 0:
        cp += 1
    check(c is not None and rho(cp) != 0, f"T: c = {c} (iota(Z(c)) = {iota(Zc(c))}), c' = {cp} (iota = {iota(Zc(cp))})")
    check(iota(Zc(c)) == 2 * (sum(1 for x in X if x > -c) - sum(1 for y in Y if y > -c)), "T: Prop 3.2(2) iota formula")
    lam = -rho(cp) / rho(c)
    Zraw = Zc(c) + [lam * z for z in Zc(cp)]
    check(s(Zraw, -1) == 0, f"T: lambda = {lam} gives s_-1 = 0")
    Z = cancel_pairs(Zraw)
    check(is_config(Z, L), f"T: L-configuration after cancelling +-pairs, |Z| = {len(Z)}")
    check(iota(Z) != 0 and len(Z) <= 4 * N, f"T: iota = {iota(Z)} != 0, |Z| = {len(Z)} <= 4N(2L-3) = {4*N}")
    g, m, gp, mp, sg, P = realise(Z, L)
    check(g != gp, f"T: realisation genera {g} vs {gp}, Area/2pi = {sg}")
    check(sg < len(Z), "T: Lemma 1.2(5) Area < 2pi T")
    check(sg < 4 * N, f"Thm 4.3 f_g threshold: Area/2pi = {sg} < 4N(2L-3) = {4*N} (Area < 8 pi N)")
    print(f"     primitive Z = {P}")

print("===== Prop 3.3 wording: multiset difference with 1 in both")
X, Y = [1, 1, 5], [1, 3, 3]
check(s(X, 1) == s(Y, 1), "X={1,1,5}, Y={1,3,3}: equal P_1 (L = 2); mult_X(1) = 2 > mult_Y(1) = 1")
U, V, Z = doubling(X, Y)
check(1 in V, f"V = {sorted(V)} contains 1: '(0;V)' is not a signature; (0;V\\{{1}}) is meant")
m = [u for u in U if u != 1]; mp = [v for v in V if v != 1]
check(len(mp) - len(m) == 1, "cone counts of (0;U\\1),(0;V\\1) differ by mult_X(1)-mult_Y(1) = 1, not mult_X(1) = 2")
check(-2 + chi_sum(m) > 0, "still hyperbolic")

print()
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("ALL CHECKS PASSED")
