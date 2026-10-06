"""Exact helpers for the trace-formula group (G5-bis blind review).

Everything here is exact (fractions.Fraction / integers / sympy Rational).
No routine in this file uses floating point.
"""
from fractions import Fraction as Fr
from math import comb, factorial
import sympy

# ---------------------------------------------------------------- Bernoulli
_B = {}


def bern_even(n):
    """B_n for EVEN n >= 0 (convention-independent: odd n never used)."""
    assert n % 2 == 0 and n >= 0
    if n not in _B:
        _B[n] = Fr(str(sympy.bernoulli(n)))
    return _B[n]


_BH = {}


def bern_half(n):
    """B_n(1/2), the Bernoulli polynomial at 1/2, for even n (computed from
    the polynomial itself, not from the identity B_n(1/2)=-(1-2^{1-n})B_n)."""
    assert n % 2 == 0
    if n not in _BH:
        x = sympy.Symbol('x')
        _BH[n] = Fr(str(sympy.bernoulli(n, x).subs(x, sympy.Rational(1, 2))))
    return _BH[n]


# ---------------------------------------------------------- power series
def ser_sin(N, a=1):
    """Taylor coefficients of sin(a u) up to u^(N-1), a rational."""
    a = Fr(a)
    return [Fr(0) if n % 2 == 0 else Fr((-1) ** ((n - 1) // 2)) * a ** n / factorial(n)
            for n in range(N)]


def ser_cos(N, a=1):
    a = Fr(a)
    return [Fr((-1) ** (n // 2)) * a ** n / factorial(n) if n % 2 == 0 else Fr(0)
            for n in range(N)]


def ser_mul(f, g, N):
    out = [Fr(0)] * N
    for i, fi in enumerate(f[:N]):
        if fi == 0:
            continue
        for j, gj in enumerate(g[:N - i]):
            if gj:
                out[i + j] += fi * gj
    return out


def ser_inv(f, N):
    assert f[0] != 0
    q = [Fr(0)] * N
    q[0] = 1 / f[0]
    for n in range(1, N):
        s = Fr(0)
        for i in range(1, n + 1):
            if i < len(f) and f[i]:
                s += f[i] * q[n - i]
        q[n] = -s / f[0]
    return q


def ser_shift(f, k):
    """divide by u^k; asserts the first k coefficients vanish."""
    assert all(c == 0 for c in f[:k]), f[:k]
    return f[k:]


# ------------------------------------------- sigma_i: u/sin u = sum sigma_i u^{2i}
def sigmas(I):
    N = 2 * I + 2
    s = ser_shift(ser_sin(N + 1), 1)      # sin u / u
    inv = ser_inv(s, N)
    assert all(inv[2 * i + 1] == 0 for i in range(I))
    return [inv[2 * i] for i in range(I + 1)]


# ---------------------------------------------- phi_k(m): three independent routes
def cot_power_sums(m, E):
    """p_e = sum_{j=1}^{m-1} cot(pi j/m)^e for e = 0..E, exactly.
    cot(pi j/m), j=1..m-1, are the m-1 distinct roots of
    P(X) = ((X+i)^m - (X-i)^m)/(2i) = sum_r C(m,r) sin(pi r/2) X^{m-r}."""
    if m == 1:
        return [Fr(0)] * (E + 1)
    d = m - 1
    # monic coefficients: X^d + e1' X^{d-1} + ... ; coefficient of X^{m-r} is C(m,r)*s_r
    def s(r):
        return 0 if r % 2 == 0 else (-1) ** ((r - 1) // 2)
    lead = Fr(comb(m, 1) * s(1))
    a = [Fr(comb(m, r) * s(r)) / lead for r in range(1, m + 1)]  # a[0]=1 for X^d
    # P/lead = sum_{i=0}^{d} a[i] X^{d-i}
    coef = a  # monic: X^d + coef[1] X^{d-1} + ... + coef[d]
    assert coef[0] == 1 and len(coef) == d + 1
    p = [Fr(d)]
    for e in range(1, E + 1):
        # Newton: e<=d: p_e + c1 p_{e-1} + ... + c_{e-1} p_1 + e c_e = 0
        #         e>d : p_e + c1 p_{e-1} + ... + c_d p_{e-d} = 0
        tot = Fr(0)
        for i in range(1, min(e - 1, d) + 1):
            tot += coef[i] * p[e - i]
        if e <= d:
            tot += e * coef[e]
        p.append(-tot)
    return p


_Q = {}


def q_series_in_c(N):
    """1/(cos u - c sin u) = sum_n q_n(c) u^n, q_n a polynomial in c (list of Fr)."""
    if N in _Q:
        return _Q[N]
    cs, sn = ser_cos(N), ser_sin(N)
    a = [[cs[n]] + [-sn[n]] for n in range(N)]  # a_n(c) = cos_n - c sin_n
    q = [[Fr(1)]]
    for n in range(1, N):
        acc = [Fr(0)] * (n + 1)
        for i in range(1, n + 1):
            ai = a[i]
            if ai[0] == 0 and ai[1] == 0:
                continue
            for e, qe in enumerate(q[n - i]):
                if qe == 0:
                    continue
                acc[e] -= ai[0] * qe
                acc[e + 1] -= ai[1] * qe
        q.append(acc)
    _Q[N] = q
    return q


def phi_direct(m, K):
    """phi_0..phi_K of Phi_m(u)=sum_j 1/(4m sin th_j sin(th_j-u)), from the
    DEFINING SUM: 1/(sin th sin(th-u)) = (1+c^2)/(cos u - c sin u), c=cot th,
    summed over the roots c_j with exact power sums."""
    N = 2 * K + 1
    q = q_series_in_c(N)
    P = cot_power_sums(m, 2 * K + 2)
    out = []
    for k in range(K + 1):
        poly = q[2 * k]
        tot = Fr(0)
        for e, ce in enumerate(poly):
            if ce:
                tot += ce * (P[e] + P[e + 2])     # (1 + c^2) * c^e
        out.append(tot / (4 * m))
    # odd coefficients must vanish (evenness)
    for k in range(K):
        poly = q[2 * k + 1]
        tot = sum((ce * (P[e] + P[e + 2]) for e, ce in enumerate(poly) if ce), Fr(0))
        assert tot == 0, (m, k)
    return out


def phi_closed(m, K):
    """phi_0..phi_K from the CLOSED FORM (cot u - m cot mu)/(4 m sin u),
    by exact power-series arithmetic (no Bernoulli numbers)."""
    if m == 1:
        return [Fr(0)] * (K + 1)
    N = 2 * K + 8
    su, cu = ser_sin(N), ser_cos(N)
    smu, cmu = ser_sin(N, m), ser_cos(N, m)
    num = [x - m * y for x, y in zip(ser_mul(cu, smu, N), ser_mul(su, cmu, N))]
    den = [4 * m * x for x in ser_mul(ser_mul(su, su, N), smu, N)]
    num, den = ser_shift(num, 3), ser_shift(den, 3)
    M = min(len(num), len(den))
    f = ser_mul(num, ser_inv(den[:M], M), M)
    assert all(f[2 * k + 1] == 0 for k in range(K))
    return [f[2 * k] for k in range(K + 1)]


def cn(n):
    """4^n |B_2n| / (2n)!"""
    return Fr(4) ** n * abs(bern_even(2 * n)) / factorial(2 * n)


def mphi_poly(k, sig):
    """m*phi_k(m) as a polynomial in M=m^2 (list, index = power of M), from (phik)."""
    poly = [Fr(0)] * (k + 2)
    for n in range(1, k + 2):
        w = Fr(1, 4) * sig[k + 1 - n] * cn(n)
        poly[n] += w
        poly[0] -= w
    return poly


def p_poly(l, sig):
    """p_l(m) as polynomial in M=m^2, from (bl)."""
    poly = [Fr(0)] * (l + 2)
    for k in range(l + 1):
        w = Fr(factorial(2 * k), factorial(k) * factorial(l - k)) / Fr(4) ** l
        for e, c in enumerate(mphi_poly(k, sig)):
            poly[e] += w * c
    return poly


def p_basis_weights(l, sig):
    """weights w_n with p_l = sum_{n=1}^{l+1} w_n (m^{2n}-1), computed from the
    double sum WITHOUT using the monomial expansion."""
    w = [Fr(0)] * (l + 2)
    for k in range(l + 1):
        a = Fr(factorial(2 * k), factorial(k) * factorial(l - k)) / Fr(4) ** l
        for n in range(1, k + 2):
            w[n] += a * Fr(1, 4) * sig[k + 1 - n] * cn(n)
    return w


def poly_eval(polyM, m):
    M = Fr(m) ** 2
    return sum((c * M ** e for e, c in enumerate(polyM)), Fr(0))


def ucar_mcS_poly(k):
    """m * c^S_k(pi/m) as polynomial in M=m^2, Ucar (4.25) with k->m."""
    poly = [Fr(0)] * (k + 2)
    pref = Fr(1, 4) * Fr((-1) ** k, factorial(k + 1) * (2 * k + 1))
    for j in range(k + 2):
        w = pref * comb(2 * k + 2, 2 * j) * bern_even(2 * j) * bern_half(2 * k + 2 - 2 * j)
        poly[j] += w
        poly[0] -= w
    return poly


def alpha_printed(k):
    """(alphak)"""
    s = sum((comb(k, l) * Fr(-4) ** l * bern_half(2 * l) for l in range(k + 1)), Fr(0))
    return Fr((-1) ** k, factorial(k) * 4 ** k) * s
