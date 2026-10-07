"""Task 1: diameter bound D(A, eps, M), and the (0;2,3,m) obstruction.

Checks (every one an assert; exit status nonzero on failure):
 1. The hyperbolic trigonometry used in the proofs, on random configurations, with SL(2,R)
    matrices at 40 digits: displacement by a rotation; the trace of a product of two rotations
    (elliptic/hyperbolic dichotomy, law of cosines, translation length); Jorgensen's commutator
    trace for a hyperbolic and an elliptic element.
 2. Lemma D1 (cone separation) against enumerated triangle groups: the least distance between
    distinct elliptic fixed points found is >= d_0(eps, M) = min(eps/2, arccosh(1 + 2/(pi^2 M^2))),
    eps the enumerated systole.
 3. Theorem D: D(A, eps, M) >= an upper bound for the true diameter of triangle orbifolds.
 4. Remark D4 (the family (0;2,3,m)): area < pi/3; the enumerated systole >= sigma_0 = 0.5621...;
    diam >= h_m = arccosh(1/(2 sin(pi/m))) -> infinity; D(pi/3, sigma_0, m) >= h_m.
"""
import random
import sys

import mpmath as mp
import numpy as np

from eigen_common import check, cone_sep, ball_constants, diam_bound, area_over_2pi
from fractions import Fraction as Fr

mp.mp.dps = 40
random.seed(20261007)


# ------------------------------------------------------------------ SL(2,R) geometry
def to_i(z):
    """Matrix taking i to z = x + i y."""
    x, y = mp.re(z), mp.im(z)
    s = mp.sqrt(y)
    return mp.matrix([[s, x / s], [0, 1 / s]])


def rot(z, phi):
    """Rotation by angle phi (counterclockwise) about z, as an SL(2,R) matrix."""
    c, s = mp.cos(phi / 2), mp.sin(phi / 2)
    K = mp.matrix([[c, s], [-s, c]])  # rotation about i; direction fixed consistently below
    P = to_i(z)
    return P * K * mp.inverse(P)


def act(Mx, z):
    return (Mx[0, 0] * z + Mx[0, 1]) / (Mx[1, 0] * z + Mx[1, 1])


def hdist(z, w):
    return mp.acosh(1 + abs(z - w) ** 2 / (2 * mp.im(z) * mp.im(w)))


def tr(Mx):
    return Mx[0, 0] + Mx[1, 1]


def point_at(z, angle, d):
    """Point at distance d from z in direction 'angle' (measured at z, from the upward vertical)."""
    P = to_i(z)
    # point at distance d from i along the geodesic leaving i at angle 'angle'
    w = act(rot(mp.mpc(0, 1), angle), mp.mpc(0, mp.e ** d))
    return act(P, w)


def check_trig():
    n = 0
    for _ in range(200):
        z = mp.mpc(random.uniform(-2, 2), random.uniform(0.3, 3))
        r = mp.mpf(random.uniform(0.01, 3))
        q = point_at(z, mp.mpf(random.uniform(0, 6.28)), r)
        check(abs(hdist(z, q) - r) < mp.mpf(10) ** -30, "point_at distance")
        # (a) displacement by a rotation: sinh(d/2) = sinh(r) sin(phi/2)
        phi = mp.mpf(random.uniform(0.05, 6.2))
        R = rot(q, phi)
        check(abs(act(R, q) - q) < mp.mpf(10) ** -30, "rotation fixes its centre")
        d = hdist(z, act(R, z))
        check(abs(mp.sinh(d / 2) - mp.sinh(r) * abs(mp.sin(phi / 2))) < mp.mpf(10) ** -28, "rotation displacement")
        # (b) product of rotations by 2 alpha about z and 2 beta about q, same orientation:
        #     tr = +-2 (cos a cos b - sin a sin b cosh d)
        a = mp.pi / random.randint(2, 40)
        b = mp.pi / random.randint(2, 40)
        P = rot(z, 2 * a) * rot(q, 2 * b)
        val = mp.cos(a) * mp.cos(b) - mp.sin(a) * mp.sin(b) * mp.cosh(r)
        check(abs(abs(tr(P)) - 2 * abs(val)) < mp.mpf(10) ** -25, "trace of product of rotations")
        X = mp.sin(a) * mp.sin(b) * mp.cosh(r) - mp.cos(a) * mp.cos(b)
        if X > 1:
            # hyperbolic, translation length 2h, cosh h = X <= cosh d
            h = mp.acosh(X)
            check(h <= r + mp.mpf(10) ** -30, "h <= d")
            check(abs(2 * mp.acosh(abs(tr(P)) / 2) - 2 * h) < mp.mpf(10) ** -20, "translation length 2h")
        elif X < 1:
            # elliptic: rotation by 2 theta, cos theta = X (law of cosines for angles)
            theta = mp.acos(X)
            check(abs(abs(tr(P)) / 2 - abs(mp.cos(theta))) < mp.mpf(10) ** -25, "rotation angle 2 theta")
            # the identity cosh d - 1 = 2 cos((th+a+b)/2) cos((th-a-b)/2)/(sin a sin b)
            lhs = mp.cosh(r) - 1
            rhs = 2 * mp.cos((theta + a + b) / 2) * mp.cos((theta - a - b) / 2) / (mp.sin(a) * mp.sin(b))
            check(abs(lhs - rhs) < mp.mpf(10) ** -25, "half-angle identity")
        # (c) Jorgensen: A hyperbolic with translation length L, B rotation by phi about q;
        #     tr[A,B] - 2 = 4 sinh^2(L/2) sin^2(phi/2) cosh^2(r), r = distance from q to the axis.
        #     Also the displacement sinh(disp/2) = sinh(L/2) cosh(r) of a point at distance r.
        L = mp.mpf(random.uniform(0.05, 3))
        Q = to_i(mp.mpc(random.uniform(-2, 2), random.uniform(0.3, 3))) * rot(mp.mpc(0, 1), mp.mpf(random.uniform(0, 6.28)))
        A = Q * mp.matrix([[mp.e ** (L / 2), 0], [0, mp.e ** (-L / 2)]]) * mp.inverse(Q)
        qq = act(mp.inverse(Q), q)  # the axis of A is Q(imaginary axis)
        raxis = mp.asinh(abs(mp.re(qq)) / mp.im(qq))
        check(abs(mp.sinh(hdist(q, act(A, q)) / 2) - mp.sinh(L / 2) * mp.cosh(raxis)) < mp.mpf(10) ** -25,
              "hyperbolic displacement")
        Bm = rot(q, phi)
        comm = A * Bm * mp.inverse(A) * mp.inverse(Bm)
        lhs = tr(comm) - 2
        rhs = 4 * mp.sinh(L / 2) ** 2 * mp.sin(phi / 2) ** 2 * mp.cosh(raxis) ** 2
        check(abs(lhs - rhs) < mp.mpf(10) ** -20 * (1 + abs(rhs)), "Jorgensen commutator trace")
        n += 1
    return n


# ------------------------------------------------------------------ triangle groups
def triangle(p, q, r):
    """Vertices (v_p, v_q, v_r) of the hyperbolic triangle with angles pi/p, pi/q, pi/r, with
    v_p = i and v_q on the imaginary axis above it; v_r to the right."""
    A, B, C = mp.pi / p, mp.pi / q, mp.pi / r
    c = mp.acosh((mp.cos(C) + mp.cos(A) * mp.cos(B)) / (mp.sin(A) * mp.sin(B)))  # side v_p v_q
    b = mp.acosh((mp.cos(B) + mp.cos(A) * mp.cos(C)) / (mp.sin(A) * mp.sin(C)))  # side v_p v_r
    vp = mp.mpc(0, 1)
    vq = mp.mpc(0, mp.e ** c)
    vr = point_at(vp, -A, b)  # angle A clockwise from the upward vertical: to the right
    if mp.re(vr) < 0:
        vr = point_at(vp, A, b)
    check(abs(hdist(vq, vr) - mp.acosh((mp.cos(A) + mp.cos(B) * mp.cos(C)) / (mp.sin(B) * mp.sin(C)))) < 1e-25,
          "triangle side lengths")
    return vp, vq, vr, c, b


def triangle_group(p, q, r):
    vp, vq, vr, _, _ = triangle(p, q, r)
    for sx in (1, -1):
        for sy in (1, -1):
            X = rot(vp, sx * 2 * mp.pi / p)
            Y = rot(vq, sy * 2 * mp.pi / q)
            P = X * Y
            if abs(abs(tr(P)) - 2 * mp.cos(mp.pi / r)) < 1e-25:
                # the fixed point of P must be v_r (or its reflection); check it is a rotation about v_r
                if abs(act(P, vr) - vr) < 1e-20:
                    return X, Y, (vp, vq, vr)
    raise AssertionError("no consistent generator orientation")


def enumerate_group(gens, base, R):
    """All elements g (numpy float64, up to sign) with d(base, g base) <= R, by BFS through
    elements with displacement <= R + 2 * max generator displacement."""
    gs = []
    for g in gens:
        G = np.array([[float(g[0, 0]), float(g[0, 1])], [float(g[1, 0]), float(g[1, 1])]])
        gs += [G, np.linalg.inv(G)]
    b = complex(float(mp.re(base)), float(mp.im(base)))

    def disp(G):
        w = (G[0, 0] * b + G[0, 1]) / (G[1, 0] * b + G[1, 1])
        return np.arccosh(1 + abs(w - b) ** 2 / (2 * b.imag * w.imag))

    gmax = max(disp(G) for G in gs)
    key = lambda G: tuple(np.round((G if (G[0, 0] > 1e-9 or (abs(G[0, 0]) <= 1e-9 and G[0, 1] > 0)) else -G).ravel(), 7))
    I = np.eye(2)
    seen = {key(I): I}
    frontier = [I]
    while frontier:
        nxt = []
        for G in frontier:
            for H in gs:
                K = G @ H
                k = key(K)
                if k in seen:
                    continue
                if disp(K) <= R + 2 * gmax:
                    seen[k] = K
                    nxt.append(K)
        frontier = nxt
    return [G for G in seen.values() if disp(G) <= R]


def analyse(elems):
    """Systole (least translation length) and elliptic fixed points among the given elements."""
    sys_len = np.inf
    fixed = []
    for G in elems:
        t = abs(G[0, 0] + G[1, 1])
        if t > 2 + 1e-9:
            sys_len = min(sys_len, 2 * np.arccosh(t / 2))
        elif t < 2 - 1e-9:
            a, b, c, d = G.ravel()
            # fixed point in H: c z^2 + (d - a) z - b = 0
            disc = complex((d - a) ** 2 + 4 * b * c)
            z = (-(d - a) + np.sqrt(disc)) / (2 * c)
            if z.imag < 0:
                z = (-(d - a) - np.sqrt(disc)) / (2 * c)
            fixed.append(z)
    return sys_len, fixed


def min_fixed_distance(fixed, centre, rad):
    pts = [z for z in fixed if np.arccosh(1 + abs(z - centre) ** 2 / (2 * z.imag * centre.imag)) <= rad]
    # deduplicate
    uniq = []
    for z in pts:
        if all(abs(z - w) > 1e-7 for w in uniq):
            uniq.append(z)
    best = np.inf
    for i in range(len(uniq)):
        for j in range(i):
            z, w = uniq[i], uniq[j]
            best = min(best, np.arccosh(1 + abs(z - w) ** 2 / (2 * z.imag * w.imag)))
    return best, len(uniq)


def main():
    out = []
    n = check_trig()
    out.append(f"trigonometry: {n} random configurations, all identities hold to >= 15 digits")

    # ---------------- Lemma D1 and Theorem D on triangle groups
    out.append("\ntriangle groups: enumerated systole eps, least distance between distinct elliptic fixed points, d_0(eps, M), D(A,eps,M), diam upper bound")
    for pqr in [(2, 3, 7), (2, 3, 8), (2, 4, 5), (2, 8, 8), (3, 3, 12), (3, 3, 4), (4, 4, 4), (2, 5, 20), (3, 4, 6), (7, 7, 7)]:
        X, Y, (vp, vq, vr) = triangle_group(*pqr)
        base = (vp + vq + vr) / 3
        base = mp.mpc(mp.re(base), mp.im(base))
        # radius: enough to see the systole: R >= sys + 2 diam(F); diam(F) <= 2 * longest side
        sides = [hdist(vp, vq), hdist(vp, vr), hdist(vq, vr)]
        R = float(6 + 4 * max(sides))
        R = min(R, 9.5)
        elems = enumerate_group([X, Y], base, R)
        eps, fixed = analyse(elems)
        c = complex(float(mp.re(base)), float(mp.im(base)))
        dmin, nfix = min_fixed_distance(fixed, c, 2.0 + float(max(sides)))
        M = max(pqr)
        d0 = cone_sep(eps, M)
        check(dmin >= d0, f"Lemma D1 fails on {pqr}: {dmin} < {d0}")
        area = 2 * mp.pi * (1 - sum(mp.mpf(1) / x for x in pqr))
        D = diam_bound(area, eps, M)
        diam_up = 2 * max(sides)  # d_O(x, v) <= longest side for a vertex v (convexity), so diam <= 2 max side
        check(D >= diam_up, f"Theorem D inconsistent on {pqr}")
        out.append(f"  {pqr}: eps={eps:.6f}  dmin={dmin:.6f} ({nfix} pts)  d0={float(d0):.3e}  D={float(D):.4g}  diam<={float(diam_up):.4f}")

    # ---------------- Remark D4: (0;2,3,m)
    s_inf = mp.acosh(2 / mp.sqrt(3))
    sigma0 = 2 * mp.asinh(1 / (2 * mp.sqrt(1 + mp.mpf(3) / 4 * mp.cosh(2 * s_inf) ** 2)))
    out.append(f"\n(0;2,3,m): sigma_0 = 2 asinh(1/(2 sqrt(1 + (3/4) cosh^2(2 s_inf)))) = {mp.nstr(sigma0, 12)}, s_inf = arccosh(2/sqrt 3) = {mp.nstr(s_inf, 12)}")
    check(abs(sigma0 - mp.mpf('0.5621')) < 1e-3, "sigma_0 value")
    for m in list(range(7, 31)) + [40, 60]:
        s = area_over_2pi(0, (2, 3, m))
        check(0 < s < Fr(1, 6), "area of (2,3,m) below pi/3")
        sm = mp.acosh(2 * mp.cos(mp.pi / m) / mp.sqrt(3))
        check(sm < s_inf, "s_m < s_inf")
        hm = mp.acosh(1 / (2 * mp.sin(mp.pi / m)))
        vp, vq, vr, c, b = triangle(2, 3, m)  # v_2 = i, v_3 above, v_m right
        check(abs(hdist(vp, vr) - hm) < 1e-25, "h_m = d(v_m, v_2)")
        check(abs(hdist(vp, vq) - sm) < 1e-25, "s_m = d(v_2, v_3)")
        check(hdist(vq, vr) - hdist(vp, vr) <= sm + 1e-30, "triangle inequality used")
        X, Y, _ = triangle_group(2, 3, m)
        base = vp + (vq - vp) * mp.mpf('0.5')
        # the systole: a closed geodesic meets B(v_3, 2 s_m); conjugates with axis meeting it
        # have displacement of v_3 at most sys + 4 s_m.  Enumerate around v_3 with R = 3 + 4 s_inf.
        elems = enumerate_group([X, Y], vq, float(3 + 4 * s_inf))
        eps, _ = analyse(elems)
        check(eps >= sigma0, f"systole bound fails for m={m}: {eps} < {sigma0}")
        D = diam_bound(mp.pi / 3, sigma0, m)
        check(D >= hm, "D(pi/3, sigma_0, m) >= h_m")
        check(hm >= mp.log(m / (2 * mp.pi)), "h_m >= log(m/(2 pi))")
        if m in (7, 8, 10, 15, 20, 30, 60):
            out.append(f"  m={m}: Area/2pi={s} (<1/6), systole(enum)={eps:.6f} >= {float(sigma0):.4f}, diam >= h_m={float(hm):.4f}, D(pi/3,sigma_0,m)={float(D):.4g}")

    # ---------------- Corollary D: closed form D <= (A/pi) max(4M, M^2) max(4/eps, 10M/3)
    for M in range(2, 201):
        x = 2 / (mp.pi ** 2 * M ** 2)
        y = mp.acosh(1 + x)
        check(y >= mp.sqrt(2 * x / (1 + x)), "arccosh(1+x) >= sqrt(2x/(1+x))")
        check(y >= mp.mpf('0.6') / M, "arccosh(1 + 2/(pi^2 M^2)) >= 0.6/M")
        check(mp.sin(mp.pi / M) >= mp.mpf(2) / M, "sin(pi/M) >= 2/M")
        for eps in (mp.mpf('0.01'), mp.mpf('0.3'), 1, 3, 10):
            r0, rho1, v0 = ball_constants(eps, M)
            check(mp.cosh(rho1) - 1 >= (mp.cosh(r0) - 1) * mp.sin(mp.pi / M) ** 2, "cosh rho1 - 1 bound")
            D = diam_bound(1, eps, M)
            closed = max(4 * M, M * M) * max(4 / eps, mp.mpf(10) * M / 3) / mp.pi
            check(D <= closed, f"closed form for D, M={M}, eps={eps}")
    out.append("\nCorollary D (closed form) D(A,eps,M) <= (A/pi) max(4M, M^2) max(4/eps, 10M/3): checked for 2 <= M <= 200, five eps")

    # ---------------- sample values of D
    out.append("\nD(A, eps, M) sample values:")
    for A in (mp.pi / 2, 4 * mp.pi / 3, 2 * mp.pi, 10 * mp.pi):
        for eps in (2, 1, mp.mpf('0.1')):
            row = []
            for M in (3, 12, 100):
                row.append(mp.nstr(diam_bound(A, eps, M), 4))
            out.append(f"  A={mp.nstr(A, 5)}, eps={mp.nstr(eps, 3)}: D for M=3,12,100: {', '.join(row)}")
    # monotonicity in eps used nowhere; asymptotics recorded
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
