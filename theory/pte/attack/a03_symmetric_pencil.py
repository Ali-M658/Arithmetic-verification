"""Attack items 3-4: Proposition 2.3 (a)-(c) and Theorem 3.1 (pencil).

(a) iota(A) = sgn s_{-1}(A) for real-rooted Q_A = (odd poly) - e_n, n = 3,5,7,9: exact Sturm counts
    on random perturbations of x*prod(x^2-r_i^2), plus the integer sets of Borwein-Ingalls.
(b) pairs A, lam*B -> balanced configuration.
(T3.1) symbolic weight check of the pencil for m = 4..9; random real pencils (exact Sturm) for
    m = 4..7; own integer pencil search for m = 4 (entries <= 45); the instance {3,10,15,30}.
"""
import sys, os, random, itertools
from fractions import Fraction as F
from collections import defaultdict
import sympy as sp
sys.path.insert(0, os.path.dirname(__file__))
from mylib import psum, iota, config_level, has_pm_pair, cancel_pm, primitive

sys.stdout.reconfigure(line_buffering=True)
x = sp.symbols('x')
random.seed(7)
fail = []


def coeffs_to_e(c):
    """monic coeffs [1, c1, ..., cn] of prod(x - z) -> e_k = (-1)^k c_k."""
    return [(-1) ** k * F(c[k]) for k in range(len(c))]


def power_sums_from_e(e, jmax):
    """Newton: s_j for j=1..jmax from e_0..e_n (exact)."""
    n = len(e) - 1
    s = [F(n)]
    for j in range(1, jmax + 1):
        t = F(0)
        for i in range(1, min(j, n) + 1):
            t += (-1) ** (i - 1) * e[i] * (s[j - i] if j - i > 0 else 0)
        if j <= n:
            t += (-1) ** (j - 1) * j * e[j]
        s.append(t)
    return s


def pos_neg(poly_coeffs):
    P = sp.Poly([sp.Rational(c.numerator, c.denominator) for c in poly_coeffs], x)
    tot = P.count_roots()
    pos = P.count_roots(0, None)
    return tot, pos


# ---------- (a) ----------
cnt = defaultdict(int)
for n in (3, 5, 7, 9):
    L = (n + 1) // 2
    done = 0
    while done < 120:
        rs = [F(random.randint(1, 60), random.randint(1, 4)) for _ in range(L - 1)]
        if len(set(rs)) < len(rs):
            continue
        P = sp.Poly(x * sp.prod([x ** 2 - sp.Rational(r.numerator, r.denominator) ** 2 for r in rs]), x)
        c = [F(int(a.p), int(a.q)) for a in P.all_coeffs()]
        # perturb constant: Q = P - e
        scale = max(abs(a) for a in c)
        e = F(random.randint(-1000, 1000) or 1, 1000) * scale * F(1, random.choice([1, 10, 100, 10 ** 4]))
        Q = c[:-1] + [c[-1] - e]
        tot, pos = pos_neg(Q)
        if tot != n:
            continue
        done += 1
        E = coeffs_to_e(Q)
        assert all(E[k] == 0 for k in range(1, n - 1, 2)) and E[n] == e
        sm1 = E[n - 1] / E[n]
        io = 2 * pos - n
        if sm1 == 0 or io != (1 if sm1 > 0 else -1):
            fail.append(("2.3a", n, rs, e, io, sm1))
        cnt[n] += 1
print("(a) random real-rooted odd-ideal-symmetric Q_A (exact Sturm):", dict(cnt), "all iota = sgn s_-1")

# integer odd ideal symmetric sets (Borwein-Ingalls p.9/p.25 as quoted in the project; recomputed here)
int_sets = [
    [-51, -33, -24, 7, 13, 38, 50],
    [-120, -110, -23, -13, 38, 105, 123],
    [-98, -82, -58, -34, 13, 16, 69, 75, 99],
    [-169, -161, -119, -63, 8, 50, 132, 148, 174],
]
# small 3- and 5-sets found here
for a, b in itertools.combinations(range(-30, 31), 2):
    c = -(a + b)
    S = sorted([a, b, c])
    if 0 in S or has_pm_pair(S) or len(set(S)) < 3:
        continue
    int_sets.append(S)
five = set()
for a, b, c in itertools.combinations(range(-40, 41), 3):
    if 0 in (a, b, c):
        continue
    sg = -(a + b + c)
    tau = -(a ** 3 + b ** 3 + c ** 3)
    if sg == 0:
        continue
    num = sg ** 3 - tau
    if num % (3 * sg):
        continue
    p = num // (3 * sg)
    D = sg * sg - 4 * p
    if D < 0:
        continue
    r = int(D ** 0.5)
    while r * r > D:
        r -= 1
    while (r + 1) ** 2 <= D:
        r += 1
    if r * r != D or (sg + r) % 2:
        continue
    d, e = (sg + r) // 2, (sg - r) // 2
    S = sorted([a, b, c, d, e])
    if 0 in S or has_pm_pair(S):
        continue
    g = 0
    for t in S:
        from math import gcd
        g = gcd(g, t)
    five.add(tuple(t // g for t in S))
int_sets += [list(t) for t in five]
nint = 0
for A in int_sets:
    n = len(A)
    L = (n + 1) // 2
    assert all(psum(A, j) == 0 for j in range(1, 2 * L - 2, 2)), A
    sm1 = psum(A, -1)
    io = iota(A)
    if sm1 == 0 or io != (1 if sm1 > 0 else -1):
        fail.append(("2.3a int", A))
    nint += 1
print(f"(a) integer odd ideal symmetric sets checked: {nint} (sizes 3,5,7,9; 5-sets: {len(five)} primitive, entries<=40)")

# ---------- (b) ----------
nb = 0
by_n = defaultdict(list)
for A in int_sets:
    by_n[len(A)].append(A)
for n, lst in by_n.items():
    L = (n + 1) // 2
    pairs = list(itertools.combinations(lst, 2))
    random.shuffle(pairs)
    for A, B in pairs[:400]:
        for sgn in (1, -1):
            Bs = [sgn * b for b in B]
            lam = -psum(Bs, -1) / psum(A, -1)
            Z = cancel_pm([F(a) for a in A] + [lam * b for b in Bs])
            if not Z:
                continue
            nb += 1
            if iota(Z) != 0 or config_level(Z) < L or len(Z) % 2:
                fail.append(("2.3b", A, Bs))
print(f"(b) {nb} configurations A u lam*B: all balanced (iota=0), level >= L")

# ---------- Theorem 3.1: symbolic weight argument ----------
for m in range(4, 10):
    r, k0 = (m - 1, m - 2) if m % 2 == 0 else (m, m - 3)
    es = sp.symbols(f'e0:{m + 1}')
    e = [sp.Integer(1)] + [es[k] if (k % 2 == 0 or k == r) else sp.Integer(0) for k in range(1, m + 1)]
    s = [sp.Integer(m)]
    for j in range(1, 2 * m):
        t = 0
        for i in range(1, min(j, m) + 1):
            t += (-1) ** (i - 1) * e[i] * (s[j - i] if j - i > 0 else 0)
        if j <= m:
            t += (-1) ** (j - 1) * j * e[j]
        s.append(sp.expand(t))
    ek0 = es[k0]
    ok = all(sp.diff(s[j], ek0) == 0 for j in range(1, 2 * m - 4, 2))
    top = sp.diff(s[2 * m - 3], ek0) != 0
    if not (ok and top):
        fail.append(("3.1 weight", m))
    print(f"(3.1) m={m}: r={r}, k0={k0}: d s_j/d e_k0 = 0 for odd j <= {2 * m - 5}: {ok}; nonzero at j={2 * m - 3}: {top}")

# ---------- Theorem 3.1: random real pencils, exact ----------
pen = defaultdict(lambda: [0, 0])
for m in (4, 5, 6, 7):
    r, k0 = (m - 1, m - 2) if m % 2 == 0 else (m, m - 3)
    L = m - 1
    tries = 0
    while pen[m][0] < 60 and tries < 20000:
        tries += 1
        # A: random real-rooted polynomial with e_odd = 0 for odd k < r: build A = W u -W' ... use
        # generic construction: random coefficients of the allowed shape, keep if all roots real
        E = [F(1)] + [F(0)] * m
        for k in range(1, m + 1):
            if k % 2 == 0 or k == r:
                E[k] = F(random.randint(-60, 60), random.randint(1, 3)) * F(10) ** random.randint(0, k)
        if E[m] == 0:
            continue
        cA = [(-1) ** k * E[k] for k in range(m + 1)]
        if pos_neg(cA)[0] != m:
            continue
        kap = F(random.randint(-200, 200) or 1, random.randint(1, 50)) * (abs(E[k0]) + 1)
        EB = list(E)
        EB[k0] = E[k0] + kap
        cB = [(-1) ** k * EB[k] for k in range(m + 1)]
        if pos_neg(cB)[0] != m:
            continue
        sA, sB = power_sums_from_e(E, 2 * m), power_sums_from_e(EB, 2 * m)
        okm = all(sA[j] == sB[j] for j in range(1, 2 * L - 2, 2)) and E[m - 1] / E[m] == EB[m - 1] / EB[m]
        exact_L = sA[2 * L - 1] != sB[2 * L - 1]
        pA, pB = pos_neg(cA)[1], pos_neg(cB)[1]
        io = (2 * pA - m) - (2 * pB - m)
        pen[m][0] += 1
        if io != 0:
            pen[m][1] += 1
        if not okm or io != 0:
            fail.append(("3.1 real", m, E, kap, io, okm))
    print(f"(3.1) m={m}: {pen[m][0]} random real pencil pairs (both real-rooted): moments ok, iota(Z)=0 in all; "
          f"tries {tries}")

# ---------- own integer pencil search m=4 ----------
N = 45
inv = defaultdict(list)
for a, b, c in itertools.combinations_with_replacement(range(-N, N + 1), 3):
    d = -(a + b + c)
    if 0 in (a, b, c, d) or abs(d) > N or d < c:
        continue
    A = (a, b, c, d)
    e3 = a * b * c + a * b * d + a * c * d + b * c * d
    e4 = a * b * c * d
    if e3 == 0:
        continue
    inv[F(e3 ** 4, e4 ** 3)].append(A)
configs = set()
for key, lst in inv.items():
    for A, B in itertools.combinations(lst, 2):
        e3A = sum(p * q * r_ for p, q, r_ in itertools.combinations(A, 3)); e4A = A[0] * A[1] * A[2] * A[3]
        e3B = sum(p * q * r_ for p, q, r_ in itertools.combinations(B, 3)); e4B = B[0] * B[1] * B[2] * B[3]
        lam = F(e4A * e3B, e4B * e3A)  # lam*B has e3 = e3A, e4 = e4A
        Bl = [lam * b for b in B]
        if sorted(Bl) == sorted(F(t) for t in A):
            continue
        Z = cancel_pm([F(t) for t in A] + [-t for t in Bl])
        if not Z:
            continue
        P = tuple(primitive(Z))
        configs.add(P)
        if len(Z) != 8 or iota(Z) != 0 or config_level(Z) < 3:
            fail.append(("pencil int", A, B))
cs = sorted(configs, key=lambda z: max(abs(t) for t in z))
print(f"(3.1) own m=4 pencil search, |entries| <= {N}: {len(configs)} distinct configurations, all size 8, iota 0, level>=3")
print("      smallest:", cs[:3])
print("      any containing +-1:", [z for z in cs if 1 in z or -1 in z])
A, B = [-30, -3, 5, 28], [-21, -4, 10, 15]
ek = lambda S, k: sum(sp.prod(t) for t in itertools.combinations(S, k))
assert ek(A, 1) == ek(B, 1) == 0 and ek(A, 3) == ek(B, 3) and ek(A, 4) == ek(B, 4) and ek(A, 2) != ek(B, 2)
Z = A + [-b for b in B]
assert sorted(z for z in Z if z > 0) == [4, 5, 21, 28] and sorted(-z for z in Z if z < 0) == [3, 10, 15, 30]
assert config_level(Z) == 3 and tuple(sorted(Z)) in cs
print(f"(3.1) instance A={A}, B={B}: e1=0, e3={ek(A, 3)}, e4={ek(A, 4)} equal, e2 {ek(A, 2)} vs {ek(B, 2)}; "
      f"gives {{3,10,15,30}}~{{4,5,21,28}}, exact 3-configuration: OK")

if fail:
    print("FAILURES:", fail[:5])
    sys.exit(1)
print("ALL CHECKS PASSED")
