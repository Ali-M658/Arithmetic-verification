"""Certified systole lower bounds for the ten examples of the eigen paper (Section 7, Table 4), in interval arithmetic.

    python3 theory/eigen/certify_systoles.py          (a few minutes)

The enumeration is that of instances.py (complete by the displacement argument stated there: every closed geodesic
of length l <= L of O = Gamma\\H^2 is the translation length of some g in Gamma with d(x0, g x0) <= L + 2r, and these g
are reached by a breadth-first search over side-adjacent tiles wP, w in the reflection group W, pruned at
d(x0, w x0) > L + 3r), run here in interval arithmetic (mpmath.iv, 60 digits):
  * the side normals of P are computed in interval arithmetic from their closed forms, so every reflection matrix
    R = I - 2 n (Jn)^T, and every product of them, is an interval matrix that contains the exact one;
  * a tile is pruned only if the lower end of the interval for cosh d(x0, w x0) exceeds cosh(L + 3r) (so no tile
    that the exact search keeps is lost), and an element is kept for the length check unless the lower end of
    cosh d(x0, g x0) exceeds cosh(L + 2r);
  * tiles are identified by the midpoint of the interval for w x0; distinct tiles have images of x0 at least
    2 sinh(d(x0, dP)) apart in R^3, and the check below asserts that every interval is far narrower than that;
  * for an orientation-preserving g in SO+(2,1), tr g = 1 + 2 cosh l(g) if g is hyperbolic, tr g <= 3 otherwise
    (no parabolic elements: the groups are cocompact). An element whose trace interval meets 3 stops the run.
    For the others, cosh l >= (tr_lo - 1)/2 gives a certified lower bound on l.
The certified systole lower bound is the least such bound over the hyperbolic elements found, asserted to be at most L
(so that a shortest geodesic is among them) and at least the systole lower bound of data/instances.csv, which is
therefore proved.  Writes data/systoles_certified.csv.
"""
import csv
import math
import os

from mpmath import iv, mp

from eigen_common import check

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
TAUS = ("0.0", "0.4", "0.8", "1.2", "1.6", "2.0", "2.4", "2.8")
L_ENUM = 4
iv.dps = 60


def lor(u, v):
    return -u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def cross(u, v):
    return [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]


def mid(x):
    return float(x.mid)


def triangle(p, q, r):
    al, be, ga = iv.pi / p, iv.pi / q, iv.pi / r
    zero, one = iv.mpf(0), iv.mpf(1)
    n1 = [zero, zero, -one]
    n2 = [zero, -iv.sin(al), iv.cos(al)]
    c1 = (iv.cos(ga) + iv.cos(al) * iv.cos(be)) / iv.sin(al)
    c2 = iv.cos(be)
    n3 = [iv.sqrt(c1 ** 2 + c2 ** 2 - 1), c1, c2]
    return [n2, n1, n3], (p, q, r)


def quadrilateral(tau):
    tau = iv.mpf(tau)
    half = iv.sqrt(iv.mpf(1) / 2)
    sa, sb = half * iv.exp(tau / 2), half * iv.exp(-tau / 2)
    ca, cb = iv.sqrt(1 + sa ** 2), iv.sqrt(1 + sb ** 2)
    zero = iv.mpf(0)
    return [[sa, ca, zero], [sb, zero, cb], [sa, -ca, zero], [sb, zero, -cb]], (3, 3, 3, 3)


def certify(name, normals, orders):
    k = len(normals)
    # vertices v_i = side i meets side i+1 (interval), and the angle check <n_i, n_{i+1}> = -cos(pi/m_i)
    verts = []
    for i in range(k):
        a, b = normals[i], normals[(i + 1) % k]
        g = lor(a, b) + iv.cos(iv.pi / orders[i])
        check(abs(mid(g)) < 1e-40 and float(g.delta) < 1e-40, f"{name}: angle at vertex {i}")
        c = cross([-a[0], a[1], a[2]], [-b[0], b[1], b[2]])
        s = 1 / iv.sqrt(-lor(c, c))
        if mid(c[0]) < 0:
            s = -s
        verts.append([x * s for x in c])
    # interior point: (close to) the Klein centroid of the vertices; any interior point works
    kc = [sum(mid(v[j]) / mid(v[0]) for v in verts) / k for j in (1, 2)]
    sc = 1 / iv.sqrt(1 - iv.mpf(kc[0]) ** 2 - iv.mpf(kc[1]) ** 2)   # x0 on the hyperboloid, as a thin interval
    x0 = [sc, sc * kc[0], sc * kc[1]]
    normals = [n if mid(lor(n, x0)) < 0 else [-c for c in n] for n in normals]
    for n in normals:
        check(lor(n, x0).b < 0, f"{name}: x0 interior")
    # r = max distance from x0 to a vertex (upper end); d(x0, dP) (lower end)
    r_hi = max(float(iv.log(-lor(x0, v) + iv.sqrt(lor(x0, v) ** 2 - 1)).b) for v in verts)
    d_lo = min(float(iv.log(-lor(n, x0) + iv.sqrt(lor(n, x0) ** 2 + 1)).a) for n in normals)  # asinh(-<n,x0>)
    L = L_ENUM
    cosh_prune = math.cosh(L + 3 * r_hi) * (1 + 1e-12)
    cosh_keep = math.cosh(L + 2 * r_hi) * (1 + 1e-12)
    refl = [(n, [-n[0], n[1], n[2]]) for n in normals]
    sep = 2 * math.sinh(d_lo)
    cell, tol = sep / 4, sep / 100
    grid = {}

    def seen_or_add(y):
        yf = [mid(c) for c in y]
        width = max(float(c.delta) for c in y)
        check(width < tol / 100, f"{name}: interval width {width:.1e} against the tile separation {sep:.2e}")
        cc = tuple(int(math.floor(t / cell)) for t in yf)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    for q in grid.get((cc[0] + dx, cc[1] + dy, cc[2] + dz), ()):
                        if abs(q[0] - yf[0]) + abs(q[1] - yf[1]) + abs(q[2] - yf[2]) < tol:
                            return True
        grid.setdefault(cc, []).append(yf)
        return False

    one, zero = iv.mpf(1), iv.mpf(0)
    I = [[one if i == j else zero for j in range(3)] for i in range(3)]
    seen_or_add(x0)
    frontier, ntiles, lows = [(I, 0)], 1, []
    while frontier:
        new = []
        for g, par in frontier:
            for n, Jn in refl:
                gn = [g[i][0] * n[0] + g[i][1] * n[1] + g[i][2] * n[2] for i in range(3)]
                h = [[g[i][j] - 2 * gn[i] * Jn[j] for j in range(3)] for i in range(3)]
                y = [h[i][0] * x0[0] + h[i][1] * x0[1] + h[i][2] * x0[2] for i in range(3)]
                ch = -lor(x0, y)
                if float(ch.a) > cosh_prune:
                    continue
                if seen_or_add(y):
                    continue
                ntiles += 1
                p = 1 - par
                new.append((h, p))
                if p == 0 and float(ch.a) <= cosh_keep:
                    tr = h[0][0] + h[1][1] + h[2][2]
                    check(not (float(tr.a) <= 3 <= float(tr.b)), f"{name}: an element with trace interval containing 3")
                    if float(tr.a) > 3:
                        c = (tr - 1) / 2
                        lows.append(float(iv.log(c + iv.sqrt(c ** 2 - 1)).a))
        frontier = new
    sys_lo = min(lows)
    check(sys_lo <= L, f"{name}: a closed geodesic of length <= L was found")
    return sys_lo, ntiles


def main():
    inst = {r["orbifold"]: r for r in csv.DictReader(open(os.path.join(DATA, "instances.csv")))}
    cases = [("O(2,8,8)", triangle(2, 8, 8)), ("O(3,3,12)", triangle(3, 3, 12))]
    cases += [(f"O_tau={tau}", quadrilateral(tau)) for tau in TAUS]
    rows = []
    for name, (normals, orders) in cases:
        lo, ntiles = certify(name, normals, orders)
        claimed = float(inst[name]["systole_lower_bound"])
        computed = float(inst[name]["systole_computed"])
        check(lo >= claimed, f"{name}: certified {lo} below the claimed lower bound {claimed}")
        check(abs(lo - computed) < 1e-9, f"{name}: certified {lo} against computed {computed}")
        print(f"{name}: systole >= {lo:.12f} (certified; claimed lower bound {claimed}, {ntiles} tiles)", flush=True)
        rows.append([name, f"{lo:.12f}", claimed, ntiles])
    with open(os.path.join(DATA, "systoles_certified.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["orbifold", "systole_certified_lower", "systole_lower_bound_table4", "tiles"])
        w.writerows(rows)
    print("all ten systole lower bounds of Table 4 are certified")


if __name__ == "__main__":
    mp.dps = 30
    main()
