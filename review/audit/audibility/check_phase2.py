"""Comparison-phase checks (exact arithmetic throughout).

1. n=5 I_3 control counts: classes vs pairs (to reconcile 2309 classes with a reported 2317).
2. n=4 integer witnesses with orders <= 90: count, primitivity, disjointness.
3. Disjointness of witnesses (n=3 orders <= 60, n=4 orders <= 90).
4. Pair variety: degree sum; diagonal points are smooth points lying on larger components
   (Jacobian rank n-1 at (m,m) with distinct m; off-diagonal points of V converging to (m,m)).
5. Leading principal minors of Theorem B's matrix M are +-Hurwitz determinants (all k), n <= 9.
"""
import os
import random
import subprocess
import tempfile
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
from math import gcd, prod
from functools import reduce

random.seed(3)
HERE = os.path.dirname(os.path.abspath(__file__))


def log(s):
    print(s, flush=True)


# ---------- 1 ----------
tmp = tempfile.mkdtemp()
exe = os.path.join(tmp, "n5_pairs")
subprocess.run(["cc", "-O2", "-o", exe, os.path.join(HERE, "n5_pairs.c")], check=True)
for N in (60, 120):
    o = subprocess.run([exe, str(N)], check=True, capture_output=True, text=True).stdout.strip().splitlines()[-1]
    kv = {k: int(v) for k, v in (x.split("=") for x in o.split())}
    assert kv["I4_collision_pairs"] == 0
    log(f"(1) n=5, orders <= {N}: {kv['I3_collision_classes']} I_3 classes, {kv['I3_collision_pairs']} I_3 pairs, "
        f"{kv['I3_classes_size_ge3']} classes of size >= 3; no I_4 collision")


# ---------- 2, 3 ----------
def key(ms, k):
    """I_k = (R, P_1, ..., P_{2k-3}) with R stored as a reduced integer pair."""
    en = prod(ms)
    en1 = sum(en // x for x in ms)
    g = gcd(en1, en)
    return (en1 // g, en // g) + tuple(sum(x ** j for x in ms) for j in range(1, 2 * k - 2, 2))


def witnesses(n, N):
    g = defaultdict(list)
    for ms in combinations_with_replacement(range(2, N + 1), n):
        if F(sum(prod(ms) // x for x in ms), prod(ms)) < n - 2:  # hyperbolic: R < n-2
            g[key(ms, n - 1)].append(ms)
    return [v for v in g.values() if len(v) > 1]


for n, N in ((3, 60), (4, 90)):
    W = witnesses(n, N)
    prim = []
    for cls in W:
        for a, b in combinations(cls, 2):
            assert not (set(a) & set(b)), (a, b)      # disjointness
            d = reduce(gcd, a + b)
            if d == 1:
                prim.append((a, b))
    npairs = sum(len(c) * (len(c) - 1) // 2 for c in W)
    log(f"(2,3) n={n}, hyperbolic, orders <= {N}: {len(W)} classes, {npairs} pairs, all disjoint; "
        f"primitive pairs (gcd 1): {len(prim)}: {prim[:12]}")
    if n == 4:
        assert ((3, 10, 15, 30), (4, 5, 21, 28)) in prim


# ---------- 4 ----------
for n in range(3, 11):
    degs = list(range(1, 2 * n - 4, 2)) + [2 * n - 1]
    assert len(degs) == n - 1 and sum(degs) == n * n - 2 * n + 3
    assert (sum(degs) > 2 * n) == (n >= 4)
log("(4) degrees 1,3,...,2n-5 and 2n-1: n-1 equations, sum n^2-2n+3, > 2n exactly for n >= 4 (n=3..10)")


def rank(A):
    A = [[F(x) for x in r] for r in A]
    rk, rows, cols = 0, len(A), len(A[0])
    for c in range(cols):
        piv = next((r for r in range(rk, rows) if A[r][c] != 0), None)
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        for r in range(rows):
            if r != rk and A[r][c] != 0:
                f = A[r][c] / A[rk][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[rk])]
        rk += 1
    return rk


def jac(ms, k):
    """Jacobian of I_k = (R, P_1, ..., P_{2k-3}) at ms."""
    return [[-F(1, x * x) for x in ms]] + [[j * F(x) ** (j - 1) for x in ms] for j in range(1, 2 * k - 2, 2)]


for n in range(3, 8):
    ms = random.sample(range(2, 50), n)
    Jm = jac(ms, n - 1)
    full = [r + [-x for x in r] for r in Jm]          # equations I(m) - I(m') at (m, m)
    assert rank(full) == n - 1
    const = [a for a in [7] * n]
    Jc = jac(const, n - 1)
    assert rank([r + [-x for x in r] for r in Jc]) == 1 < n - 1
log("(4) at (m,m) with distinct m the n-1 defining equations have Jacobian rank n-1 (smooth point, local "
    "dimension n+1 > n = dim of the diagonal); at (a..a,a..a) rank 1 (singular), n=3..7")

# explicit off-diagonal points of V converging to a diagonal point: fibre line of check_theoremC, n=3
# e(t) for m = (2,3,5): e1 = 10, e2 = R t = (31/30) t, e3 = t; at t = 30 the multiset is m.
from sympy import Poly, symbols, Rational, oo
z = symbols("z")
for k in range(3, 9):
    t = Rational(30) * (1 + Rational(1, 10 ** k))
    q = Poly(z ** 3 - 10 * z ** 2 + Rational(31, 30) * t * z - t, z)
    assert q.gcd(q.diff(z)).degree() == 0 and q.count_roots(0, oo) == 3
log("(4) m=(2,3,5): for t = 30(1+10^-k), k=3..8, z^3-10z^2+(31/30)t z - t has 3 distinct positive roots m'(t) != m "
    "with I_2(m') = I_2(m); (m, m'(t)) -> (m, m): the diagonal is not a component")


# ---------- 5 ----------
def elem(ms):
    e = [F(1)] + [F(0)] * len(ms)
    for x in ms:
        for k in range(len(ms), 0, -1):
            e[k] += x * e[k - 1]
    return e


def det(A):
    A = [[F(x) for x in r] for r in A]
    n, d = len(A), F(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return F(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            d = -d
        d *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return d


def Tser(ms, n):
    N = 2 * n - 1
    g = [F(0)] * N
    for k in range(1, N, 2):
        g[k] = sum(F(x) ** k for x in ms) / k
    ex = [F(1)] + [F(0)] * (N - 1)
    for m_ in range(1, N):
        ex[m_] = sum((k * 2 * g[k] * ex[m_ - k] for k in range(1, m_ + 1)), F(0)) / m_
    num = [F(0)] + ex[1:]
    den = [F(2)] + ex[1:]
    inv = [F(1, 2)] + [F(0)] * (N - 1)
    for m_ in range(1, N):
        inv[m_] = -sum((den[i] * inv[m_ - i] for i in range(1, m_ + 1)), F(0)) * inv[0]
    return [sum((num[i] * inv[m_ - i] for i in range(m_ + 1)), F(0)) for m_ in range(N)]


def Mmat(ms):
    n = len(ms)
    T = Tser(ms, n)
    M = [[F(0)] * n for _ in range(n)]
    for j in range(n - 1):
        if 2 * j + 1 <= n:
            M[j][2 * j] += 1
        for i in range(j + 1):
            idx = 2 * j - 2 * i
            if 0 < idx <= n:
                M[j][idx - 1] -= T[2 * i + 1]
    M[n - 1][n - 2] += 1
    M[n - 1][n - 1] -= sum(F(1, 1) / x for x in ms)
    return M


def hurwitz(a, j):
    A = lambda i: a[i] if 0 <= i < len(a) else 0
    return [[A(2 * c - r) for c in range(1, j + 1)] for r in range(1, j + 1)]


for n in range(2, 10):
    for _ in range(4):
        ms = [F(random.randint(1, 30), random.randint(1, 4)) * random.choice([1, -1]) for _ in range(n)]
        M = Mmat(ms)
        e = elem(ms)
        for k in range(1, n):
            lead = det([r[:k] for r in M[:k]])
            Hk = det(hurwitz(e, k - 1)) if k >= 2 else F(1)
            assert lead == (-1) ** (k // 2) * Hk, (n, k)
        assert det(M) == (-1) ** (n * (n + 1) // 2) * det(hurwitz(e, n - 1)) / e[n]
log("(5) leading k x k minors of M equal (-1)^floor(k/2) Delta_{k-1}(p) for k <= n-1, and det M = "
    "(-1)^(n(n+1)/2) Delta_{n-1}/e_n, at exact signed rational points, n = 2..9")
print("ALL CHECKS PASSED")
