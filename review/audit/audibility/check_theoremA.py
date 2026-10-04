"""Theorem A (injectivity of I_n), Remark 3 (padding / 3-cone vs 4-cone), adversarial searches.

Exact arithmetic: Fractions, and sympy Gaussian rationals for complex cases.
"""
import random
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product

random.seed(7)
out = []


def log(s):
    out.append(s)
    print(s, flush=True)


def inv(x):
    return 1 / x if not isinstance(x, int) else F(1, x)


def I(ms):
    """I_n(m) = (R, P_1, P_3, ..., P_{2n-3}) with n = len(ms)."""
    n = len(ms)
    return (sum(inv(x) for x in ms),) + tuple(sum(x ** k for x in ms) for k in range(1, 2 * n - 2, 2))


def cond(ms):
    return all(x != 0 for x in ms) and all(ms[i] + ms[j] != 0 for i, j in combinations(range(len(ms)), 2))


def collisions(pool, n):
    g = defaultdict(list)
    for ms in combinations_with_replacement(pool, n):
        if any(x == 0 for x in ms):
            continue
        g[I(ms)].append(ms)
    return [v for v in g.values() if len(v) > 1]


# 1. positive integers (orders, with 1 allowed = padding), exhaustive
for n, N in ((1, 300), (2, 300), (3, 90), (4, 40)):
    col = collisions(range(1, N + 1), n)
    assert col == [], (n, col[:3])
    log(f"positive integers 1..{N}, n={n}: no two distinct multisets share I_{n}")

# 2. nonzero signed integers: every collision class consists only of multisets violating the hypothesis
for n, K in ((2, 25), (3, 12), (4, 7)):
    pool = [x for x in range(-K, K + 1) if x != 0]
    col = collisions(pool, n)
    for cls in col:
        assert all(not cond(ms) for ms in cls), cls
    log(f"signed integers in [-{K},{K}]\\0, n={n}: {len(col)} collision classes; "
        f"every member has some m_i+m_j=0 (e.g. {col[0][:2] if col else None})")
    if n >= 2:
        assert len(col) > 0  # the hypothesis of Theorem A is genuinely needed

# 3. Gaussian integers
from sympy import I as iu, expand, Rational
for n, K in ((2, 3), (3, 2)):
    pool = [a + b * iu for a in range(-K, K + 1) for b in range(-K, K + 1) if (a, b) != (0, 0)]
    g = defaultdict(list)
    for ms in combinations_with_replacement(range(len(pool)), n):
        v = [pool[i] for i in ms]
        key = (expand(sum(1 / x for x in v)),) + tuple(expand(sum(x ** k for x in v)) for k in range(1, 2 * n - 2, 2))
        g[key].append(tuple(v))
    bad = 0
    ncol = 0
    for cls in g.values():
        if len(cls) > 1:
            ncol += 1
            for v in cls:
                if all(expand(v[i] + v[j]) != 0 for i, j in combinations(range(n), 2)):
                    bad += 1
    assert bad == 0
    log(f"Gaussian integers |Re|,|Im|<={K}, n={n}: {ncol} collision classes, all members violate the hypothesis")

# 4. constructive recovery: from I_n alone, solve Theorem B's system and factor -> m (exact)
from sympy import symbols, Poly, roots, nroots, factor_list, Integer
z = symbols("z")


def recover(Iv, n):
    R = Iv[0]
    Pk = {2 * i + 1: Iv[1 + i] for i in range(n - 1)}
    N = 2 * n - 1
    # tanh series
    g = [F(0)] * N
    for k in range(1, N, 2):
        g[k] = F(Pk[k]) / k
    ex = [F(0)] * N
    ex[0] = F(1)
    for m_ in range(1, N):
        ex[m_] = sum(k * 2 * g[k] * ex[m_ - k] for k in range(1, m_ + 1)) / m_
    num = [F(0)] + ex[1:]
    den = [F(2)] + ex[1:]
    dinv = [F(0)] * N
    dinv[0] = F(1, 2)
    for m_ in range(1, N):
        dinv[m_] = -sum(den[i] * dinv[m_ - i] for i in range(1, m_ + 1)) * dinv[0]
    T = [sum(num[i] * dinv[m_ - i] for i in range(m_ + 1)) for m_ in range(N)]
    A = [[F(0)] * n for _ in range(n)]
    b = [F(0)] * n
    for j in range(n - 1):
        if 2 * j + 1 <= n:
            A[j][2 * j] += 1
        for i in range(j + 1):
            idx = 2 * j - 2 * i
            if idx == 0:
                b[j] += T[2 * i + 1]
            elif idx <= n:
                A[j][idx - 1] -= T[2 * i + 1]
    if n >= 2:
        A[n - 1][n - 2] += 1
    else:
        b[0] -= 1
    A[n - 1][n - 1] -= F(R)
    # Gauss-Jordan
    M = [row[:] + [bb] for row, bb in zip(A, b)]
    for c in range(n):
        piv = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    e = [M[i][n] / M[i][i] for i in range(n)]
    # p(z) = prod (z + m_i) = sum e_k z^{n-k}; recover m as -roots
    p = Poly([1] + [Rational(x.numerator, x.denominator) for x in e], z)
    rts = roots(p)
    ms = []
    for r_, mult in rts.items():
        ms += [-r_] * mult
    return sorted(ms)


cnt = 0
for n in range(1, 8):
    for trial in range(15):
        kind = trial % 3
        if kind == 0:
            ms = [random.randint(2, 60) for _ in range(n)]
        elif kind == 1:  # repeated
            ms = [random.choice([2, 3, 7]) for _ in range(n)]
        else:  # padding with ones
            ms = [1] * random.randint(0, n - 1)
            ms += [random.randint(2, 30) for _ in range(n - len(ms))]
        rec = recover(I(ms), n)
        assert [int(x) for x in rec] == sorted(ms), (ms, rec)
        cnt += 1
log(f"constructive recovery from I_n via Theorem B system: {cnt} multisets, n=1..7, all recovered exactly")

# 5. heat coefficients themselves (Ucar), and Remark 3: 3-cone vs 4-cone, first three coefficients
p0 = lambda m: F(m * m - 1, 12 * m)                                    # b_0(m)
p1 = lambda m: -(F(m ** 4, 360) + F(m ** 2, 36) - F(11, 360)) / m       # b_1(m) with K=-1
a1, a2 = F(1, 3), F(1, 15)  # a_nu/(vol kappa^nu) from (4.35)


def heat3(ms):
    n = len(ms)
    R = sum(F(1, x) for x in ms)
    A4pi = F(n - 2) - R  # area/(2 pi)  ->  area/(4 pi) = (n-2-R)/2
    c1 = A4pi / 2
    c2 = a1 * (-1) * c1 + sum(p0(x) for x in ms)
    c3 = a2 * c1 + sum(p1(x) for x in ms)
    return (c1, c2, c3)


# padding invariance of the actual coefficients
for ms in [(2, 3, 7), (2, 8, 8), (5, 5, 5, 5)]:
    assert heat3(ms) == heat3(ms + (1,)) == heat3(ms + (1, 1))
log("actual c_1,c_2,c_3 (Ucar (4.33),(4.35), K=-1) unchanged by appending order-1 points")

N = 60
three = defaultdict(list)
two = defaultdict(list)
for ms in combinations_with_replacement(range(2, N + 1), 3):
    if sum(F(1, x) for x in ms) < 1:
        h = heat3(ms)
        three[h].append(ms)
        two[h[:2]].append(ms)
hits = []
ctrl = 0
for ms in combinations_with_replacement(range(2, N + 1), 4):
    if sum(F(1, x) for x in ms) < 2:
        h = heat3(ms)
        if h in three:
            hits.append((three[h], ms))
        if h[:2] in two:
            ctrl += 1
assert hits == []
assert ctrl > 0
log(f"Remark 3: 3-cone vs 4-cone hyperbolic, orders <= {N}: no pair shares c_1,c_2,c_3 "
    f"(control: {ctrl} 4-cone multisets share c_1,c_2 with some 3-cone one)")
print("ALL CHECKS PASSED")
