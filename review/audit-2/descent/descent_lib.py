"""Exact arithmetic helpers for the G5-bis `descent` review.

Everything is over Q with fractions.Fraction, or over F_p with Python integers.
No floating point is used anywhere as a certificate.
"""
from fractions import Fraction as Fr
from math import gcd
from functools import reduce

# ---------------------------------------------------------------------------
# Weierstrass curves y^2 = x^3 + a2 x^2 + a4 x + a6  (a1 = a3 = 0)
# Points: None is the origin (point at infinity), else a tuple (x, y).
# ---------------------------------------------------------------------------


class Weier:
    def __init__(self, a2, a4, a6=0, p=None):
        self.p = p
        if p is None:
            self.a2, self.a4, self.a6 = Fr(a2), Fr(a4), Fr(a6)
        else:
            self.a2, self.a4, self.a6 = a2 % p, a4 % p, a6 % p

    def _inv(self, t):
        if self.p is None:
            return 1 / Fr(t)
        return pow(t % self.p, self.p - 2, self.p)

    def _red(self, t):
        return t if self.p is None else t % self.p

    def on(self, P):
        if P is None:
            return True
        x, y = P
        return self._red(y * y - (x ** 3 + self.a2 * x * x + self.a4 * x + self.a6)) == 0

    def neg(self, P):
        if P is None:
            return None
        return (P[0], self._red(-P[1]))

    def add(self, P, Q):
        """Chord-tangent law with origin at infinity (Cremona 3.1 conventions,
        a1 = a3 = 0): x3 = m^2 - a2 - x1 - x2, y3 = -(m (x3 - x1) + y1)."""
        if P is None:
            return Q
        if Q is None:
            return P
        x1, y1 = P
        x2, y2 = Q
        if self._red(x1 - x2) == 0:
            if self._red(y1 + y2) == 0:
                return None
            m = self._red((3 * x1 * x1 + 2 * self.a2 * x1 + self.a4) * self._inv(2 * y1))
        else:
            m = self._red((y2 - y1) * self._inv(x2 - x1))
        x3 = self._red(m * m - self.a2 - x1 - x2)
        y3 = self._red(-(m * (x3 - x1) + y1))
        R = (x3, y3)
        assert self.on(R)
        return R

    def mul(self, n, P):
        R = None
        Q = P
        if n < 0:
            n, Q = -n, self.neg(P)
        while n:
            if n & 1:
                R = self.add(R, Q)
            Q = self.add(Q, Q)
            n >>= 1
        return R

    def order(self, P, bound=10 ** 6):
        R = P
        for n in range(1, bound + 1):
            if R is None:
                return n
            R = self.add(R, P)
        return 0

    def count_Fp(self):
        """#E(F_p) by brute force, including the point at infinity."""
        p = self.p
        assert p is not None
        sq = [0] * p
        for y in range(p):
            sq[y * y % p] += 1
        n = 1
        for x in range(p):
            n += sq[(x ** 3 + self.a2 * x * x + self.a4 * x + self.a6) % p]
        return n


# ---------------------------------------------------------------------------
# Plane cubics C_lambda : (X+Y+Z)(XY+YZ+ZX) - lam XYZ = 0 and the
# chord-tangent law with an arbitrary rational base point O.
# ---------------------------------------------------------------------------


def F_lam(lam, P):
    X, Y, Z = P
    return (X + Y + Z) * (X * Y + Y * Z + Z * X) - lam * X * Y * Z


def normalize(P):
    """Projective point with rational coordinates -> primitive integer triple,
    sign fixed so that the first nonzero coordinate is positive."""
    P = [Fr(t) for t in P]
    den = reduce(lambda a, b: a * b // gcd(a, b), [t.denominator for t in P], 1)
    Q = [int(t * den) for t in P]
    g = reduce(gcd, [abs(t) for t in Q])
    assert g > 0, "zero vector is not a projective point"
    Q = [t // g for t in Q]
    for t in Q:
        if t != 0:
            if t < 0:
                Q = [-s for s in Q]
            break
    return tuple(Q)


def same_point(P, Q):
    return normalize(P) == normalize(Q)


def third_point(lam, P, Q):
    """Third intersection of the line PQ (tangent line if P == Q) with C_lam.
    Exact: parametrize the line as P + t D, restrict F to a cubic in t."""
    lam = Fr(lam)
    P = tuple(Fr(t) for t in P)
    Q = tuple(Fr(t) for t in Q)
    assert F_lam(lam, P) == 0 and F_lam(lam, Q) == 0
    if same_point(P, Q):
        # tangent direction: any D with grad F(P) . D = 0, D not proportional to P
        X, Y, Z = P
        e1 = X + Y + Z
        e2 = X * Y + Y * Z + Z * X
        g = (e2 + e1 * (Y + Z) - lam * Y * Z,
             e2 + e1 * (X + Z) - lam * X * Z,
             e2 + e1 * (X + Y) - lam * X * Y)
        assert any(t != 0 for t in g), "singular point"
        # cross product of g with a vector not proportional... pick D = g x P
        D = (g[1] * P[2] - g[2] * P[1], g[2] * P[0] - g[0] * P[2], g[0] * P[1] - g[1] * P[0])
        assert any(t != 0 for t in D)
        # F(P + tD) has a double root at t = 0 (tangent); get the remaining one
        c = _cubic_coeffs(lam, P, D)
        # c0 = c1 = 0 ; c3 t^3 + c2 t^2 -> t = -c2/c3 ; if c3 == 0 third point is D itself
        assert c[0] == 0 and c[1] == 0
        if c[3] == 0:
            return D
        t = -c[2] / c[3]
        return tuple(P[i] + t * D[i] for i in range(3))
    D = tuple(Q[i] - P[i] for i in range(3))
    c = _cubic_coeffs(lam, P, D)
    # roots t = 0 (P) and t = 1 (Q); product of roots = -c0/c3 = 0 ; sum = -c2/c3
    assert c[0] == 0
    if c[3] == 0:
        return D  # third point at "t = infinity"
    t3 = -c[2] / c[3] - 1
    return tuple(P[i] + t3 * D[i] for i in range(3))


def _cubic_coeffs(lam, P, D):
    """Coefficients c0..c3 of F(P + t D) as a polynomial in t (exact)."""
    # evaluate at 4 points and interpolate (exact Fractions)
    ts = [Fr(0), Fr(1), Fr(-1), Fr(2)]
    vals = [F_lam(lam, tuple(P[i] + t * D[i] for i in range(3))) for t in ts]
    f0, f1, fm1, f2 = vals
    c0 = f0
    # f(1) = c0+c1+c2+c3 ; f(-1) = c0-c1+c2-c3 ; f(2) = c0+2c1+4c2+8c3
    s = (f1 + fm1) / 2 - c0  # c2
    c2 = s
    o = (f1 - fm1) / 2  # c1 + c3
    # f2 - c0 - 4 c2 = 2 c1 + 8 c3
    r = f2 - c0 - 4 * c2
    c3 = (r - 2 * o) / 6
    c1 = o - c3
    return (c0, c1, c2, c3)


class PlaneCubicGroup:
    """Group law on C_lam with base point O: P + Q = O * (P * Q), where
    A * B is the third intersection of line AB.  Negation: -P = P * (O * O)."""

    def __init__(self, lam, O):
        self.lam = Fr(lam)
        self.O = normalize(O)
        assert F_lam(self.lam, self.O) == 0
        self.OO = normalize(third_point(self.lam, self.O, self.O))

    def star(self, A, B):
        return normalize(third_point(self.lam, A, B))

    def add(self, P, Q):
        return self.star(self.O, self.star(P, Q))

    def neg(self, P):
        return self.star(P, self.OO)

    def mul(self, n, P):
        if n == 0:
            return self.O
        if n < 0:
            return self.mul(-n, self.neg(P))
        R = normalize(P)
        for _ in range(n - 1):
            R = self.add(R, P)
        return R

    def order(self, P, bound=100):
        R = normalize(P)
        for n in range(1, bound + 1):
            if R == self.O:
                return n
            R = self.add(R, P)
        return 0


class Out:
    """Collect output lines, print them; count asserts."""

    def __init__(self):
        self.n = 0

    def ok(self, cond, msg):
        assert cond, "FAILED: " + msg
        self.n += 1
        print("[ok] " + msg)
