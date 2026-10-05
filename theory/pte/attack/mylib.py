"""Independent exact helpers for the referee attack. No imports from the project code."""
from fractions import Fraction as F
from math import comb, factorial, gcd
from functools import lru_cache
from collections import Counter


@lru_cache(maxsize=None)
def bern(n):
    """Bernoulli number B_n with B_1 = -1/2 (recurrence sum_{j<=n} C(n+1,j) B_j = 0)."""
    if n == 0:
        return F(1)
    return -sum(comb(n + 1, j) * bern(j) for j in range(n)) / (n + 1)


def bern_half(n):
    """B_n(1/2) = (2^{1-n} - 1) B_n."""
    return (F(2) ** (1 - n) - 1) * bern(n)


@lru_cache(maxsize=None)
def c_coeffs(l):
    """c_l(pi/k) = sum_j w_j (k^{2j}-1) / k ; return list of w_j (Ucar 4.25)."""
    pref = F(1, 4) * F((-1) ** l, factorial(l + 1) * (2 * l + 1))
    return [pref * comb(2 * l + 2, 2 * j) * bern(2 * j) * bern_half(2 * l + 2 - 2 * j)
            for j in range(l + 2)]


@lru_cache(maxsize=None)
def p_poly(l):
    """k*b_l(k) at K=-1 as a dict {power: coeff}, power even, from (4.25)+(4.33)."""
    out = Counter()
    for i in range(l + 1):
        w = F(2, 4 ** i * factorial(i))
        for j, cj in enumerate(c_coeffs(l - i)):
            out[2 * j] += w * cj
            out[0] -= w * cj
    sgn = (-1) ** l  # K^l with K=-1
    return {p: sgn * c for p, c in out.items() if c != 0}


def b(l, k):
    """Cone contribution b_l(k) at K = -1, exact."""
    k = F(k)
    return sum(c * k ** p for p, c in p_poly(l).items()) / k


def area(sig):
    g, m = sig
    return 2 * g - 2 + sum(1 - F(1, x) for x in m)


def shared(sig1, sig2, lmax=12):
    """Exact number of shared heat coefficients (c_1 = area, c_{l+2} <-> C_l)."""
    if area(sig1) != area(sig2):
        return 0
    s = 1
    for l in range(lmax):
        if sum(b(l, x) for x in sig1[1]) != sum(b(l, x) for x in sig2[1]):
            return s
        s += 1
    return s  # at least


def psum(Z, j):
    return sum(F(z) ** j for z in Z)


def iota(Z):
    return sum(1 for z in Z if z > 0) - sum(1 for z in Z if z < 0)


def cancel_pm(Z):
    """Remove +-pairs from a multiset."""
    c = Counter(Z)
    for z in list(c):
        if z > 0 and -z in c:
            t = min(c[z], c[-z])
            c[z] -= t
            c[-z] -= t
    return sorted(c.elements())


def config_level(Z, Lmax=40):
    """Largest L such that Z is an L-configuration (s_-1=0, odd s_j=0 j<=2L-3); 1 if only s_-1."""
    assert len(Z) > 0 and all(z != 0 for z in Z)
    if psum(Z, -1) != 0:
        return 0
    L = 1
    while L < Lmax and psum(Z, 2 * L - 1) == 0:
        L += 1
    return L  # s_{2L-1} != 0 (or cap)


def has_pm_pair(Z):
    s = set(Z)
    return any(-z in s for z in s)


def primitive(Z):
    """Scale a rational multiset to coprime integers (positive scale)."""
    Z = [F(z) for z in Z]
    den = 1
    for z in Z:
        den = den * z.denominator // gcd(den, z.denominator)
    I = [int(z * den) for z in Z]
    g = 0
    for x in I:
        g = gcd(g, abs(x))
    return sorted(x // g for x in I)


def sig_to_config(sig1, sig2):
    """Pad with 1s so R(U)=R(V), cancel common entries, return (U*, V*, Z=U*u-V*)."""
    (g1, m1), (g2, m2) = sig1, sig2
    d = sum(F(1, x) for x in m2) - sum(F(1, x) for x in m1)
    assert d.denominator == 1, "areas differ or not integral padding"
    d = int(d)
    U = Counter(m1) + Counter({1: max(d, 0)})
    V = Counter(m2) + Counter({1: max(-d, 0)})
    common = U & V
    U, V = U - common, V - common
    Us, Vs = sorted(U.elements()), sorted(V.elements())
    return Us, Vs, sorted(Us + [-v for v in Vs])


# ---------------- exact rational roots of cubics ----------------
def _isqrt_floor(n):
    from math import isqrt
    return isqrt(n) if n >= 0 else None


def _floordiv(a, b):
    return a // b


def int_roots_monic_cubic(A, B, C):
    """All integer roots (with multiplicity) of y^3 + A y^2 + B y + C, A,B,C ints. Exact."""
    from math import isqrt
    h = lambda y: ((y + A) * y + B) * y + C
    M = 1 + max(abs(A), abs(B), abs(C))
    D = 4 * A * A - 12 * B  # disc of h' = 3y^2 + 2Ay + B
    cuts = []
    if D > 0:
        s = isqrt(D)  # floor sqrt
        # critical points (-2A -+ sqrt(D))/6 ; use safe integer brackets
        c1lo = (-2 * A - s - 1) // 6 - 1
        c1hi = -((2 * A + s) // 6) + 1
        c2lo = (-2 * A + s) // 6 - 1
        c2hi = -((2 * A - s - 1) // 6) + 1
        cuts = [c1lo, c1hi, c2lo, c2hi]
    pts = sorted(set([-M] + [min(max(c, -M), M) for c in cuts] + [M]))
    roots = set()
    # brute-force the small neighbourhoods of the critical points (non-monotone zone)
    for c in cuts:
        for y in range(c - 2, c + 3):
            if h(y) == 0:
                roots.add(y)
    # bisection on each monotone stretch between consecutive cut points
    for lo, hi in zip(pts, pts[1:]):
        flo, fhi = h(lo), h(hi)
        if flo == 0:
            roots.add(lo)
        if fhi == 0:
            roots.add(hi)
        if (flo < 0 < fhi) or (fhi < 0 < flo):
            a, bb = lo, hi
            inc = flo < fhi
            while bb - a > 1:
                mid = (a + bb) // 2
                fm = h(mid)
                if fm == 0:
                    roots.add(mid)
                    break
                if (fm < 0) == inc:
                    a = mid
                else:
                    bb = mid
    # multiplicities by deflation
    out = []
    coeffs = [1, A, B, C]
    for r in sorted(roots):
        while True:
            # synthetic division
            q = [coeffs[0]]
            for c in coeffs[1:]:
                q.append(c + q[-1] * r)
            if q[-1] != 0 or len(coeffs) == 1:
                break
            out.append(r)
            coeffs = q[:-1]
            if len(coeffs) == 1:
                break
    return out


def rational_roots_cubic(a3, a2, a1, a0):
    """Rational roots with multiplicity of a3 t^3 + a2 t^2 + a1 t + a0 (rational coeffs, a3 != 0)."""
    cs = [F(c) for c in (a3, a2, a1, a0)]
    den = 1
    for c in cs:
        den = den * c.denominator // gcd(den, c.denominator)
    I = [int(c * den) for c in cs]
    g = 0
    for x in I:
        g = gcd(g, x)
    I = [x // g for x in I]
    a3, a2, a1, a0 = I
    # t = y / a3  ->  y^3 + a2 y^2 + a1 a3 y + a0 a3^2 = 0
    ys = int_roots_monic_cubic(a2, a1 * a3, a0 * a3 * a3)
    return [F(y, a3) for y in ys]
