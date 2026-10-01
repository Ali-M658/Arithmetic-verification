"""Theorem B (determinant of the linear system), the Orlando identity, and Remark 2 (Jacobian).

All checks exact: sympy polynomial identities for small n, and exact Fraction evaluation at
random rational (also negative / complex-rational) points for n up to 10.
"""
import random
import sys
from fractions import Fraction as F
from itertools import combinations
from sympy import symbols, Matrix, expand, cancel, Poly, Rational, prod, I, together, nsimplify

random.seed(20260615)
NMAX_SYM = 6
NMAX_PT = 10
lines = []


def log(s):
    lines.append(s)
    print(s)


# ---------- power-series helpers over an arbitrary exact ring (Fraction or sympy) ----------
def ser_mul(a, b, N):
    c = [0] * N
    for i, x in enumerate(a[:N]):
        if x == 0:
            continue
        for j, y in enumerate(b[:N - i]):
            c[i + j] += x * y
    return c


def ser_inv(a, N):
    # a[0] must be invertible
    inv = [0] * N
    inv[0] = 1 / a[0] if not isinstance(a[0], int) else F(1, a[0])
    for n in range(1, N):
        s = 0
        for i in range(1, min(n, len(a) - 1) + 1):
            s += a[i] * inv[n - i]
        inv[n] = -s * inv[0]
    return inv


def ser_exp(g, N):
    # g[0] = 0; e' = g' e
    e = [0] * N
    e[0] = F(1)
    for n in range(1, N):
        s = 0
        for k in range(1, n + 1):
            if k < len(g):
                s += k * g[k] * e[n - k]
        e[n] = s / n
    return e


def elem(ms):
    e = [F(1)] + [F(0)] * len(ms)
    for x in ms:
        for k in range(len(ms), 0, -1):
            e[k] += x * e[k - 1]
    return e


def det_frac(A):
    A = [row[:] for row in A]
    n = len(A)
    d = F(1)
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
            if f != 0:
                for cc in range(c, n):
                    A[r][cc] -= f * A[c][cc]
    return d


def T_from_powersums(ms, n):
    """T(z) = tanh(sum_{k odd<=2n-3} P_k z^k/k), computed from heat invariants only."""
    N = 2 * n - 1
    g = [F(0)] * N
    for kk in range(1, N, 2):
        g[kk] = sum(F(x) ** kk for x in ms) / kk
    e2 = ser_exp([2 * x for x in g], N)
    num = [e2[0] - 1] + e2[1:]
    den = [e2[0] + 1] + e2[1:]
    return ser_mul(num, ser_inv(den, N), N)


def system(T, R, n):
    """Rows j=0..n-2: e_{2j+1} - sum_{i=0}^{j} T_{2i+1} e_{2j-2i} = 0; last row e_{n-1} - R e_n = 0.
    Unknowns e_1..e_n (columns 0..n-1); e_0 = 1 moves to b; e_k = 0 for k > n."""
    M = [[0] * n for _ in range(n)]
    b = [0] * n
    for j in range(n - 1):
        if 2 * j + 1 <= n:
            M[j][2 * j] += 1
        for i in range(j + 1):
            idx = 2 * j - 2 * i
            if idx == 0:
                b[j] += T[2 * i + 1]
            elif idx <= n:
                M[j][idx - 1] -= T[2 * i + 1]
    if n - 1 >= 1:
        M[n - 1][n - 2] += 1
    else:
        b[n - 1] -= 1
    M[n - 1][n - 1] -= R
    return M, b


def hurwitz(a, j):
    """Holtz-Tyaglov (1.37): j x j matrix with (r,c) entry a_{2c-r} (1-indexed), a_i=0 outside."""
    def A(i):
        return a[i] if 0 <= i < len(a) else 0
    return [[A(2 * c - r) for c in range(1, j + 1)] for r in range(1, j + 1)]


def cn_pred(n):
    return (-1) ** (n * (n + 1) // 2)


# ---------------- 1. symbolic identity in e_1..e_n -----------------
log("== symbolic: det M as a rational function of e_1..e_n, T = O/E ==")
for n in range(2, NMAX_SYM + 1):
    es = symbols(f"e1:{n+1}")
    e = [1] + list(es)
    N = 2 * n - 1
    E = [e[k] if (k % 2 == 0 and k <= n) else 0 for k in range(N)]
    O = [e[k] if (k % 2 == 1 and k <= n) else 0 for k in range(N)]
    # T = O * E^{-1} (truncated): E^{-1} by recursion with sympy entries
    Einv = [0] * N
    Einv[0] = 1
    for m_ in range(1, N):
        Einv[m_] = expand(-sum(E[i] * Einv[m_ - i] for i in range(1, m_ + 1)))
    T = [expand(sum(O[i] * Einv[m_ - i] for i in range(m_ + 1))) for m_ in range(N)]
    R = e[n - 1] / e[n]
    M, b = system(T, R, n)
    # true e solves the system
    for row, rhs in zip(M, b):
        assert expand(together(sum(c * x for c, x in zip(row, es)) - rhs)) == 0
    # multiply the last row by e_n (polynomial entries): det of the scaled matrix is e_n det M
    Ms = [row[:] for row in M]
    Ms[n - 1] = [expand(c * e[n]) for c in Ms[n - 1]]
    dMe = expand(Matrix(Ms).det(method="berkowitz"))
    H = expand(Matrix(hurwitz(e, n - 1)).det())
    ratio = cancel(dMe / H)
    assert ratio.is_Rational and ratio != 0, (n, ratio)
    assert ratio == cn_pred(n), (n, ratio)
    log(f"n={n}: det M = ({ratio}) * Delta_{n-1}(p)/e_n identically; (-1)^(n(n+1)/2) = {cn_pred(n)}")

# ---------------- 2. Orlando: Delta_{n-1}(p) = prod_{i<j}(m_i+m_j), symbolic -----------------
log("== symbolic Orlando with p(z)=prod(z+m_i), a_k = e_k ==")
for n in range(2, 7):
    ms = symbols(f"m1:{n+1}")
    e = [1] + [0] * n
    for x in ms:
        for kk in range(n, 0, -1):
            e[kk] = expand(e[kk] + x * e[kk - 1])
    H = expand(Matrix(hurwitz(e, n - 1)).det())
    target = expand(prod([ms[i] + ms[j] for i, j in combinations(range(n), 2)]))
    assert expand(H - target) == 0
    log(f"n={n}: Delta_{n-1}(p) = prod_(i<j)(m_i+m_j) exactly (sign +1)")

# ---------------- 3. exact point checks, n = 2..10, T built from power sums -----------------
log("== exact points: T from tanh of odd power sums; det M vs c_n prod(m_i+m_j)/prod m_i ==")
found = {}
for n in range(2, NMAX_PT + 1):
    for trial in range(12):
        kind = trial % 4
        if kind == 0:
            ms = [F(random.randint(2, 40)) for _ in range(n)]
        elif kind == 1:
            ms = [F(random.randint(-30, 30) or 7, random.randint(1, 9)) for _ in range(n)]
        elif kind == 2:  # repeated orders
            base = [F(random.randint(2, 9)) for _ in range(max(1, n // 2))]
            ms = [random.choice(base) for _ in range(n)]
        else:  # padding by ones
            ms = [F(1)] * (n // 2) + [F(random.randint(2, 30)) for _ in range(n - n // 2)]
        if any(x == 0 for x in ms):
            continue
        T = T_from_powersums(ms, n)
        R = sum(1 / x for x in ms)
        M, b = system(T, R, n)
        e = elem(ms)
        for row, rhs in zip(M, b):
            assert sum(c * x for c, x in zip(row, e[1:])) == rhs
        d = det_frac(M)
        pm = F(1)
        for i, j in combinations(range(n), 2):
            pm *= ms[i] + ms[j]
        pr = F(1)
        for x in ms:
            pr *= x
        H = det_frac(hurwitz(e, n - 1))
        assert H == pm, (n, ms)
        if pm == 0:
            assert d == 0
            continue
        c = d * pr / pm
        found.setdefault(n, set()).add(c)
    assert found[n] == {cn_pred(n)}, (n, found[n])
    log(f"n={n:2d}: c_n = {sorted(found[n])}   (-1)^(n(n+1)/2) = {cn_pred(n)}")
claimed = {3: 1, 4: 1, 5: -1, 6: -1, 7: 1, 8: 1}
for n, c in claimed.items():
    assert found[n] == {c}
log("claimed list c_3..c_8 = +1,+1,-1,-1,+1,+1 confirmed; c_2 = -1, c_9 = -1, c_10 = -1")

# n = 1 (outside the theorem): system is the single row e_0 - R e_1 = 0, M = [-R]
M, b = system([0, 0], F(1, 5), 1)
assert M == [[-F(1, 5)]] and b == [-1]
log("n=1 (not claimed): M = [-R], det = -1/m = (-1)^1 * Delta_0/e_1, so the formula persists")

# ---------------- 4. complex rational point, and singular points m_i + m_j = 0 -----------------
log("== complex and degenerate points ==")
from sympy import Rational as Q
for n in (2, 3, 4, 5):
    ms = [Q(random.randint(1, 9)) + I * Q(random.randint(-9, 9)) for _ in range(n)]
    es = [1] + [0] * n
    for x in ms:
        for kk in range(n, 0, -1):
            es[kk] = expand(es[kk] + x * es[kk - 1])
    N = 2 * n - 1
    g = [0] * N
    for kk in range(1, N, 2):
        g[kk] = expand(sum(x ** kk for x in ms) / kk)
    # exp(2g) with sympy entries
    ex = [0] * N
    ex[0] = 1
    for m_ in range(1, N):
        ex[m_] = expand(sum(kk * 2 * g[kk] * ex[m_ - kk] for kk in range(1, m_ + 1)) / m_)
    num = [0] + ex[1:]
    den = [2] + ex[1:]
    dinv = [0] * N
    dinv[0] = Q(1, 2)
    for m_ in range(1, N):
        dinv[m_] = expand(-sum(den[i] * dinv[m_ - i] for i in range(1, m_ + 1)) * dinv[0])
    T = [expand(sum(num[i] * dinv[m_ - i] for i in range(m_ + 1))) for m_ in range(N)]
    R = expand(sum(1 / x for x in ms))
    M, b = system(T, R, n)
    d = expand(Matrix(M).det())
    target = expand(cn_pred(n) * prod([ms[i] + ms[j] for i, j in combinations(range(n), 2)]) / prod(ms))
    assert expand(d - target) == 0
    log(f"n={n}: Gaussian-rational point {ms}: formula holds")

# singular: m contains a, -a. det M = 0 and X(z) = z^2 g(z), f = (1 - a^2 z^2) g, is a kernel vector
for n in (2, 3, 4, 5):
    a = F(3)
    rest = [F(random.randint(2, 9)) for _ in range(n - 2)]
    ms = [a, -a] + rest
    T = T_from_powersums(ms, n)
    R = sum(1 / x for x in ms)
    M, b = system(T, R, n)
    assert det_frac(M) == 0
    g = elem(rest)  # g(z) = prod_{rest}(1 + x z)
    X = [F(0), F(0)] + g  # z^2 g(z), degree n
    X = X[: n + 1] + [F(0)] * (n + 1 - len(X))
    assert all(sum(c * x for c, x in zip(row, X[1:])) == 0 for row in M)
    assert any(x != 0 for x in X[1:])
    log(f"n={n}: m={[str(x) for x in ms]}: det M = 0, explicit kernel vector z^2 g(z) verified")

# ---------------- 5. Remark 2: Jacobian of I_n -----------------
log("== Remark 2: Jacobian of (R, P_1, P_3, ..., P_{2n-3}) ==")
for n in range(1, NMAX_SYM + 1):
    ms = symbols(f"m1:{n+1}")
    funcs = [sum(1 / x for x in ms)] + [sum(x ** kk for x in ms) for kk in range(1, 2 * n - 2, 2)]
    J = Matrix([[f.diff(x) for x in ms] for f in funcs])
    dJ = cancel(J.det())
    V = prod([ms[j] - ms[i] for i, j in combinations(range(n), 2)])
    Om = prod([ms[i] + ms[j] for i, j in combinations(range(n), 2)])
    cJ = -prod([2 * r - 1 for r in range(1, n)])
    assert cancel(dJ - cJ * V * Om / prod([x ** 2 for x in ms])) == 0
    log(f"n={n}: Jacobian = {cJ} * V(m) prod(m_i+m_j)/prod m_i^2 (symbolic)")
for n in range(8, NMAX_PT + 1):
    for _ in range(5):
        ms = [F(random.randint(-50, 50) or 1, random.randint(1, 7)) for _ in range(n)]
        J = [[-1 / x ** 2 for x in ms]] + [[kk * x ** (kk - 1) for x in ms] for kk in range(1, 2 * n - 2, 2)]
        V = F(1)
        Om = F(1)
        for i, j in combinations(range(n), 2):
            V *= ms[j] - ms[i]
            Om *= ms[i] + ms[j]
        pr2 = F(1)
        for x in ms:
            pr2 *= x * x
        cJ = -1
        for r in range(1, n):
            cJ *= 2 * r - 1
        assert det_frac(J) == cJ * V * Om / pr2
    log(f"n={n}: Jacobian formula holds at 5 exact rational points")

print("ALL CHECKS PASSED")
