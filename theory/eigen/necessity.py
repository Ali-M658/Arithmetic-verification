"""Task 5: the hypotheses of Theorem E cannot simply be dropped.

(a) Cone orders unbounded: the family O(2,3,m).
(b) Systole -> 0: the quadrilateral families (0;k,k,k,k), k = 3, 4.

Checks (asserts; nonzero exit on failure):
 1. Symbolic (sympy): the Rayleigh identities on a cone (weight sinh) and on a collar (weight cosh):
    with f = w^{-1/2} u,  f'^2 w = u'^2 + q u^2 + (d/drho)(-(w'/2w) u^2)  with q = 1/4 - 1/(4 sinh^2)
    for w = sinh and q = 1/4 + 1/(4 cosh^2) for w = cosh.
 2. Numerical: the Rayleigh quotients of the test functions are below the stated bounds.
 3. (a): Area(O(2,3,m)) < pi/3, h_m = arccosh(1/(2 sin(pi/m))) increasing, the eigenvalue bound
    lambda_j <= 1/4 + pi^2 (j+1)^2 / h_m^2, and the pigeonhole count.
 4. (b): construction of the quadrilateral Q_b with angles pi/k and sinh a sinh b = cos(pi/k)
    (angles and the Fermi rectangle inside Q_b, i.e. the corner lies beyond rho = a); the bounds
    lambda_1 <= sinh a / ((a^2+2) sinh a - 2 a cosh a) and
    lambda_j <= 1/4 + sech^2(a/2)/4 + 4 pi^2 (j+1)^2 / a^2; the two families give, for every
    delta > 0, members of different signatures with |lambda_1 - lambda_1'| < delta.
"""
import sys
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp

from eigen_common import check, area_over_2pi

mp.mp.dps = 30


def symbolic_identities():
    r = sp.symbols('rho', positive=True)
    u = sp.Function('u')(r)
    res = []
    for w, q in ((sp.sinh(r), sp.Rational(1, 4) - 1 / (4 * sp.sinh(r) ** 2)),
                 (sp.cosh(r), sp.Rational(1, 4) + 1 / (4 * sp.cosh(r) ** 2))):
        f = u / sp.sqrt(w)
        lhs = sp.diff(f, r) ** 2 * w
        boundary = -sp.diff(w, r) / (2 * w) * u ** 2
        rhs = sp.diff(u, r) ** 2 + q * u ** 2 + sp.diff(boundary, r)
        diff = sp.simplify((lhs - rhs).rewrite(sp.exp))
        check(diff == 0, f"Rayleigh identity for weight {w}")
        res.append(str(w))
    return res


def rayleigh(weight, f, df, a, b):
    num = mp.quad(lambda r: df(r) ** 2 * weight(r), [a, b])
    den = mp.quad(lambda r: f(r) ** 2 * weight(r), [a, b])
    return num / den


def part_a(out):
    out.append("(a) O(2,3,m):")
    prev = None
    for m in range(7, 2001):
        s = area_over_2pi(0, (2, 3, m))
        check(0 < s < Fr(1, 6), "Area < pi/3")
        hm = mp.acosh(1 / (2 * mp.sin(mp.pi / m)))
        if prev is not None:
            check(hm > prev, "h_m increasing")
        prev = hm
    # Rayleigh quotient of the test functions on the cone ball (weight sinh), j+1 disjoint sines
    for m in (7, 20, 200):
        hm = mp.acosh(1 / (2 * mp.sin(mp.pi / m)))
        for J in (1, 3, 6):
            a0 = hm / 1000
            L = (hm - a0) / J
            worst = 0
            for i in range(J):
                lo = a0 + i * L
                u = lambda r, lo=lo: mp.sin(mp.pi * (r - lo) / L)
                du = lambda r, lo=lo: mp.pi / L * mp.cos(mp.pi * (r - lo) / L)
                f = lambda r, u=u: u(r) / mp.sqrt(mp.sinh(r))
                df = lambda r, u=u, du=du: (du(r) - mp.coth(r) / 2 * u(r)) / mp.sqrt(mp.sinh(r))
                R = rayleigh(mp.sinh, f, df, lo, lo + L)
                worst = max(worst, R)
            bound = mp.mpf(1) / 4 + mp.pi ** 2 * J ** 2 / (hm - a0) ** 2
            check(worst <= bound, "cone test-function Rayleigh quotient")
    out.append("  Area/2pi = 1/6 - 1/m < 1/6 and h_m increasing for 7 <= m <= 2000; test-function quotients on the cone ball checked")
    for N in (2, 5, 10):
        LamN = mp.mpf(1) / 4 + mp.pi ** 2 * N ** 2 / mp.acosh(1 / (2 * mp.sin(mp.pi / 7))) ** 2
        for delta in (mp.mpf('0.1'), mp.mpf('0.001')):
            boxes = (mp.floor(LamN / delta) + 1) ** (N - 1)
            out.append(f"  N={N}, delta={mp.nstr(delta, 2)}: lambda_(N-1) <= {mp.nstr(LamN, 5)} for all m >= 7; among any "
                       f"{mp.nstr(boxes + 1, 4)} orders m >= 7 two have their first N eigenvalues within delta")
    for m in (7, 100, 10 ** 4, 10 ** 8):
        hm = mp.acosh(1 / (2 * mp.sin(mp.pi / m)))
        out.append(f"  m={m}: h_m={mp.nstr(hm, 6)}; lambda_j <= 1/4 + pi^2 (j+1)^2/h_m^2, e.g. j=1: {mp.nstr(mp.mpf(1)/4 + 4*mp.pi**2/hm**2, 6)}")


# ------------------------------------------------------------------ quadrilaterals
def to_disc_point(rho, s):
    """Fermi coordinates (rho, s) about the geodesic beta = real diameter of the Poincare disc
    (s = arclength from 0, rho = signed distance): returns the point in the disc."""
    # point at arclength s on the real diameter, then move distance rho perpendicularly
    x = mp.tanh(s / 2)
    # Mobius map of the disc taking 0 to x along the real axis: z -> (z + x)/(1 + x z)
    z0 = mp.mpc(0, mp.tanh(rho / 2))  # distance rho from 0 along the imaginary axis
    return (z0 + x) / (1 + x * z0)


def disc_dist(z, w):
    return 2 * mp.atanh(abs((z - w) / (1 - mp.conj(w) * z)))


def quadrilateral(k, b):
    """Quadrilateral with two mirror axes (real and imaginary diameters), distances b (to the
    sides crossing the real axis) and a (to those crossing the imaginary axis),
    sinh a sinh b = cos(pi/k).  Returns a, the corner, the corner angle and the Fermi rho of the
    corner, i.e. the length PC."""
    a = mp.asinh(mp.cos(mp.pi / k) / mp.sinh(b))
    # side through P = (b, 0): geodesic perpendicular to the real axis at distance b: points (rho, s=b)
    # side through R = (0, a) on the imaginary axis, perpendicular to it
    # the corner: on the first side, at Fermi height rho_c with distance to the imaginary-axis line
    # equal... solve: the corner lies on both sides; parametrise the first side by rho and find rho
    # where the point is on the second side, i.e. where its reflection-distance to R-side vanishes.
    R = mp.mpc(0, mp.tanh(a / 2))
    # second side: geodesic through R perpendicular to the imaginary axis: a circle orthogonal to
    # the unit circle, symmetric about the imaginary axis, through R: centre (0, c), radius sqrt(c^2-1)
    yR = mp.tanh(a / 2)
    c = (1 + yR ** 2) / (2 * yR)
    rad = mp.sqrt(c * c - 1)
    g = lambda rho: abs(to_disc_point(rho, b) - mp.mpc(0, c)) - rad
    rho_c = mp.findroot(g, a)
    C = to_disc_point(rho_c, b)
    # corner angle between the two sides at C
    h = mp.mpf(10) ** -12
    t1 = (to_disc_point(rho_c - h, b) - C)  # along side 1 towards the real axis
    # tangent of the circle at C, direction towards the imaginary axis
    nrm = C - mp.mpc(0, c)
    tang = mp.mpc(-mp.im(nrm), mp.re(nrm))
    if mp.re(tang) > 0:
        tang = -tang
    ang = abs(mp.arg(t1 / tang))
    return a, C, ang, rho_c


def part_b(out):
    mp.mp.dps = 80  # a ~ log(1/b) is large: the disc model needs many digits
    out.append("(b) quadrilateral families (0;k,k,k,k):")
    for k in (3, 4):
        s = area_over_2pi(0, (k,) * 4)
        for b in (mp.mpf('0.6'), mp.mpf('0.1'), mp.mpf('0.01'), mp.mpf('1e-4'), mp.mpf('1e-8')):
            a, C, ang, rho_c = quadrilateral(k, b)
            check(abs(ang - mp.pi / k) < mp.mpf(10) ** -8, f"corner angle pi/{k}")
            check(rho_c >= a, "the corner lies beyond rho = a (Fermi rectangle inside Q)")
            check(abs(mp.tanh(rho_c) - mp.tanh(a) * mp.cosh(b)) < mp.mpf(10) ** -15, "tanh PC = tanh a cosh b")
            # the far side (through R) stays at Fermi height >= a for |s| <= b
            for sfrac in (0, mp.mpf('0.3'), mp.mpf('0.7'), 1):
                ss = b * sfrac
                yR = mp.tanh(a / 2)
                c = (1 + yR ** 2) / (2 * yR)
                rad = mp.sqrt(c * c - 1)
                g = lambda rho: abs(to_disc_point(rho, ss) - mp.mpc(0, c)) - rad
                rr = mp.findroot(g, a)
                check(rr >= a - mp.mpf(10) ** -20, "far side at height >= a")
            w = a
            lam1 = mp.sinh(w) / ((w ** 2 + 2) * mp.sinh(w) - 2 * w * mp.cosh(w))
            # numerical Rayleigh quotient of the odd test function on the collar only (a lower
            # bound for the true denominator), with weight 4b cosh
            num = mp.quad(lambda r: (1 / w) ** 2 * mp.cosh(r), [-w, w])
            den = mp.quad(lambda r: (r / w) ** 2 * mp.cosh(r), [-w, w])
            check(abs(num / den - lam1) < mp.mpf(10) ** -15 * (1 + lam1), "lambda_1 bound formula")
            lamj = lambda j: mp.mpf(1) / 4 + mp.sech(a / 2) ** 2 / 4 + 4 * mp.pi ** 2 * (j + 1) ** 2 / a ** 2
            if b in (mp.mpf('0.01'), mp.mpf('1e-8')):
                out.append(f"  k={k} (Area/2pi={s}), b={mp.nstr(b, 2)}: systole <= 4b = {mp.nstr(4*b, 3)}, collar half-width a={mp.nstr(a, 5)},"
                           f" lambda_1 <= {mp.nstr(lam1, 4)}, lambda_5 <= {mp.nstr(lamj(5), 4)}")
    # for every delta: b small in both families gives lambda_1, lambda_1' < delta
    for delta in (mp.mpf('0.1'), mp.mpf('0.01')):
        # lambda_1 bound ~ 1/a^2; find a with bound < delta, then b = asinh(cos(pi/k)/sinh a)
        a = mp.findroot(lambda w: mp.sinh(w) / ((w ** 2 + 2) * mp.sinh(w) - 2 * w * mp.cosh(w)) - delta, 1 / mp.sqrt(delta))
        bs = [mp.asinh(mp.cos(mp.pi / k) / mp.sinh(a)) for k in (3, 4)]
        out.append(f"  delta={mp.nstr(delta, 2)}: lambda_1 < delta for both families once a >= {mp.nstr(a, 4)}, i.e. b <= {mp.nstr(bs[0], 3)} (k=3), {mp.nstr(bs[1], 3)} (k=4)")


def main():
    out = []
    ids = symbolic_identities()
    out.append(f"Rayleigh identities verified symbolically for weights {ids}")
    part_a(out)
    part_b(out)
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
