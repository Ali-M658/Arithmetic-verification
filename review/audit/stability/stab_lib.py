"""Independent referee library for the STABILITY group (exact rational arithmetic).

Everything here is derived from the statements file and from the fetched source texts only:
  * cone coefficients from Ucar (4.25) + (4.33), smooth coefficients from Ucar (4.35), K = kappa = -1;
  * Theorem B's linear system as described in the referee brief.
All arithmetic is Fraction-based; no floating point enters any certificate.
"""
from fractions import Fraction as F
from math import comb, factorial
from functools import lru_cache
import itertools

# ---------------------------------------------------------------- Bernoulli numbers
@lru_cache(None)
def bern(n):
    """B_n with B_1 = -1/2."""
    B = [F(1)]
    for m in range(1, n + 1):
        B.append(-sum(comb(m + 1, k) * B[k] for k in range(m)) / (m + 1))
    return B[n]


def bern_poly(n, x):
    return sum(comb(n, k) * bern(k) * x ** (n - k) for k in range(n + 1))


HALF = F(1, 2)
KAPPA = -1

# ---------------------------------------------------------------- Ucar coefficients
def c_S(l, k):
    """Ucar (4.25): c^S_l(pi/k)."""
    s = sum(comb(2 * l + 2, 2 * j) * (F(k) ** (2 * j) - 1) * bern(2 * j) * bern_poly(2 * l + 2 - 2 * j, HALF)
            for j in range(l + 2))
    return F(1, 4 * k) * F((-1) ** l, factorial(l + 1)) * F(1, 2 * l + 1) * s


def cone_b(nu, k, kappa=KAPPA):
    """Ucar (4.33): t^nu coefficient of C for one cone point of order k."""
    return sum(F(2, 4 ** l * factorial(l)) * c_S(nu - l, k) for l in range(nu + 1)) * F(kappa) ** nu


def alpha(j, kappa=KAPPA):
    """Ucar (4.35): a_j(O)/vol(O)."""
    return F(1, factorial(j) * 4 ** j) * sum(comb(j, l) * F(-4) ** l * bern_poly(2 * l, HALF)
                                             for l in range(j + 1)) * F(kappa) ** j


def p_poly_coeffs(nu):
    """pi_{nu,k}: b_nu(m) = (-1)^nu sum_k pi_{nu,k} m^{2k-1}.  Obtained by exact interpolation of
    m*b_nu(m)*(-1)^nu, an even polynomial of degree 2nu+2 in m."""
    import sympy as sp
    x = sp.Symbol('x')
    pts = list(range(1, nu + 3))  # nu+2 values of m^2 determine a degree nu+1 polynomial in m^2
    ys = [sp.Rational(*(lambda q: (q.numerator, q.denominator))(F(m) * cone_b(nu, m) * (-1) ** nu)) for m in pts]
    poly = sp.interpolate(list(zip([m * m for m in pts], ys)), x)
    poly = sp.Poly(sp.expand(poly), x)
    co = [F(0)] * (nu + 2)
    for (d,), c in poly.terms():
        co[d] = F(int(sp.fraction(c)[0]), int(sp.fraction(c)[1]))
    # validate on extra points (exactness check, polynomial identity of degree nu+1 in m^2)
    for m in range(nu + 3, nu + 8):
        assert sum(co[kk] * F(m) ** (2 * kk) for kk in range(nu + 2)) == F(m) * cone_b(nu, m) * (-1) ** nu
    return co


@lru_cache(None)
def PI(nu):
    return tuple(p_poly_coeffs(nu))

# ---------------------------------------------------------------- invariants and heat data
def invariants(m):
    """I_n = (R, P_1, P_3, ..., P_{2n-3}) for a list of orders (rationals allowed)."""
    n = len(m)
    m = [F(x) for x in m]
    return [sum(1 / x for x in m)] + [sum(x ** (2 * l - 1) for x in m) for l in range(1, n)]


def L_matrix(n):
    """Lower triangular L (rows H_{-1}..H_{n-2}, columns R, P_1, ..., P_{2n-3}) built from Ucar."""
    L = [[F(0)] * n for _ in range(n)]
    L[0][0] = F(-1, 2)
    for nu in range(n - 1):
        pi = PI(nu)
        L[nu + 1][0] = -alpha(nu + 1) / 2 + (-1) ** nu * pi[0]
        for k in range(1, nu + 2):
            L[nu + 1][k] = (-1) ** nu * pi[k]
    return L


def h0(n):
    return [F(n - 2, 2)] + [F(n - 2, 2) * alpha(j) for j in range(1, n)]


def heat_direct(m):
    """H_{-1..n-2} computed directly from the Ucar formulas (no use of L)."""
    n = len(m)
    R = sum(F(1) / F(x) for x in m)
    area4pi = F(n - 2, 1) / 2 - R / 2
    H = [area4pi]
    for nu in range(n - 1):
        H.append(area4pi * alpha(nu + 1) + sum(cone_b(nu, x) for x in m))
    return H


def matvec(A, v):
    return [sum(a * b for a, b in zip(row, v)) for row in A]


def heat_from_I(I, n):
    L = L_matrix(n)
    return [x + y for x, y in zip(matvec(L, I), h0(n))]


def inv(A):
    n = len(A)
    M = [list(map(F, row)) + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]


def solve(A, b):
    n = len(A)
    M = [list(map(F, row)) + [F(b[i])] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [M[i][n] for i in range(n)]


def det(A):
    n = len(A)
    M = [list(map(F, row)) for row in A]
    d = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            if M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return d


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def absM(A):
    return [[abs(x) for x in row] for row in A]

# ---------------------------------------------------------------- power series (truncated)
def ps_mul(a, b, N):
    c = [F(0)] * (N + 1)
    for i, x in enumerate(a[:N + 1]):
        if x == 0:
            continue
        for j, y in enumerate(b[:N + 1 - i]):
            c[i + j] += x * y
    return c


@lru_cache(None)
def tan_coeffs(N):
    """Taylor coefficients of tan x up to x^N (exact): tan = sin/cos."""
    s = [F(0)] * (N + 1)
    c = [F(0)] * (N + 1)
    for k in range(N + 1):
        if k % 2:
            s[k] = F((-1) ** ((k - 1) // 2), factorial(k))
        else:
            c[k] = F((-1) ** (k // 2), factorial(k))
    # t = s / c
    t = [F(0)] * (N + 1)
    for k in range(N + 1):
        t[k] = s[k] - sum(c[i] * t[k - i] for i in range(1, k + 1))
    return tuple(t)


def ps_compose(gco, U, N):
    """g(U(z)) for U(0)=0, g given by coefficients."""
    out = [F(0)] * (N + 1)
    P = [F(1)] + [F(0)] * N
    for j in range(N + 1):
        if j > 0:
            P = ps_mul(P, U, N)
        if gco[j] != 0:
            out = [o + gco[j] * p for o, p in zip(out, P)]
    return out


def tanh_coeffs(N):
    t = tan_coeffs(N)
    return tuple(t[k] * (-1) ** ((k - 1) // 2) if k % 2 else F(0) for k in range(N + 1))


def U_series(I, n, N):
    """U(z) = sum_{k odd<=2n-3} P_k z^k / k (only these P are data)."""
    U = [F(0)] * (N + 1)
    for l in range(1, n):
        k = 2 * l - 1
        if k <= N:
            U[k] = F(I[l]) / k
    return U


def T_series(I, n):
    N = 2 * n - 1
    return ps_compose(tanh_coeffs(N), U_series(I, n, N), N)

# ---------------------------------------------------------------- Theorem B system
def M_b(I, n):
    """Square system M e = b in e_1..e_n (columns 0..n-1 <-> e_1..e_n)."""
    T = T_series(I, n)
    M = [[F(0)] * n for _ in range(n)]
    b = [F(0)] * n
    for j in range(n - 1):
        if 2 * j + 1 <= n:
            M[j][2 * j] += 1
        for i in range(j):  # e_{2j-2i}, k = 2j-2i >= 2
            k = 2 * j - 2 * i
            if k <= n:
                M[j][k - 1] -= T[2 * i + 1]
        b[j] = T[2 * j + 1]
    M[n - 1][n - 2] += 1
    M[n - 1][n - 1] -= F(I[0])
    return M, b


def esym(roots):
    """elementary symmetric e_0..e_n of a multiset (rational)."""
    e = [F(1)]
    for x in roots:
        x = F(x)
        e = [a + (x * b if i > 0 else 0) for i, (a, b) in enumerate(zip(e + [F(0)], [F(0)] + e))]
    return e


def poly_from_roots(roots):
    """monic coefficients high->low of prod (z - r)."""
    c = [F(1)]
    for r in roots:
        c = [a - F(r) * b for a, b in zip(c + [F(0)], [F(0)] + c)]
    return c


def heat_from_poly(coef):
    """Heat data of a real monic polynomial z^n - e1 z^{n-1} + ... via Newton's identities
    (R = e_{n-1}/e_n). coef high->low, coef[0]=1."""
    n = len(coef) - 1
    e = [F(1)] + [F(coef[j]) * (-1) ** j for j in range(1, n + 1)]
    # power sums p_1..p_{2n-3} via Newton
    K = 2 * n - 3
    p = [F(n)] + [F(0)] * K
    for k in range(1, K + 1):
        s = F(0)
        for i in range(1, k):
            if i <= n:
                s += (-1) ** (i - 1) * e[i] * p[k - i]
        if k <= n:
            s += (-1) ** (k - 1) * k * e[k]
        p[k] = s
    I = [e[n - 1] / e[n]] + [p[2 * l - 1] for l in range(1, n)]
    return heat_from_I(I, n), I, e


def recover_e(Ht, n, Linv=None):
    if Linv is None:
        Linv = inv(L_matrix(n))
    It = matvec(Linv, [x - y for x, y in zip(Ht, h0(n))])
    M, b = M_b(It, n)
    return [F(1)] + solve(M, b), It


def multiset(m):
    d = {}
    for x in m:
        d[x] = d.get(x, 0) + 1
    return sorted(d.items())

# ---------------------------------------------------------------- Routh-Hurwitz strip counting
def poly_shift(coef, c):
    """coefficients (high->low) of p(z + c)."""
    n = len(coef) - 1
    # Horner-based Taylor shift
    a = list(map(F, coef))
    for i in range(n):
        for j in range(1, n + 1 - i):
            a[j] += c * a[j - 1]
    return a


def rhp_count(coef):
    """Number of roots with Re z > 0 of a real polynomial (high->low), via the Routh array.
    Returns None when the array is singular (a root on, or symmetric about, the imaginary axis):
    the caller treats that as an undecided (failed) case."""
    a = list(map(F, coef))
    while a and a[0] == 0:
        a.pop(0)
    n = len(a) - 1
    if a[-1] == 0:
        return None  # root at 0 lies on the axis
    r0 = a[0::2]
    r1 = a[1::2]
    rows = [r0, r1 + [F(0)] * (len(r0) - len(r1))]
    for _ in range(n - 1):
        p, q = rows[-2], rows[-1]
        if q[0] == 0:
            return None
        new = [(q[0] * p[i + 1] - p[0] * q[i + 1]) / q[0] if i + 1 < len(q) else F(0) for i in range(len(p) - 1)]
        new = new + [F(0)] * (len(q) - len(new))
        rows.append(new)
    first = [r[0] for r in rows[: n + 1]]
    if any(x == 0 for x in first):
        return None
    return sum(1 for x, y in zip(first, first[1:]) if (x > 0) != (y > 0))


def rounds_to(coef, m):
    """True iff rounding real parts of the roots of coef reproduces the multiset m, with every
    real part strictly inside (a-1/2, a+1/2); decided exactly by Routh-Hurwitz counts.
    Returns (ok, detail)."""
    n = len(coef) - 1
    cnt = {}
    for a, k in multiset(m):
        lo = rhp_count(poly_shift(coef, F(a) - HALF))
        hi = rhp_count(poly_shift(coef, F(a) + HALF))
        if lo is None or hi is None:
            return False, ('undecided', a)
        cnt[a] = lo - hi
        if cnt[a] != k:
            return False, ('count', a, cnt[a], k)
    return True, cnt
