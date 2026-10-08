"""Geometric inputs of the a-posteriori test (eigen paper, Section 7) for its ten examples.

    .venv/bin/python theory/eigen/instances.py          (about 1-2 min)

The examples are doubles of compact convex geodesic polygons P with angles pi/m_i:
  O(2,8,8), O(3,3,12)      P = the triangle with angles pi/p, pi/q, pi/r;
  O_tau, signature (0;3,3,3,3), tau in {0, 0.4, ..., 2.8}   (called vartheta in the papers)
                           P = the quadrilateral with all angles pi/3, symmetric in both axes,
                           sides at distances a (east, west) and b (north, south) from the centre,
                           sinh a sinh b = cos(pi/3) = 1/2, tau = log(sinh a / sinh b).
Model: the hyperboloid {<x,x> = -1, x_0 > 0}, <x,y> = -x_0 y_0 + x_1 y_1 + x_2 y_2; the side lines
are n^perp for unit spacelike normals n, constructed in closed form (no root finding), and the
reflection in a side is x -> x - 2 <x,n> n.  W = the reflection group of P (P is a fundamental
domain), Gamma = its orientation-preserving subgroup of index 2, O = Gamma\\H^2 = the double of P.

1. Systole, by complete enumeration with a displacement cutoff (mpmath, 40 digits).
   Let x0 be an interior point of P and r = max_{y in P} d(x0, y) (the largest distance from x0 to
   a vertex, P being convex).  If gamma in Gamma is hyperbolic, a point y of its axis has a
   W-translate in P: y = w y' with y' in P.  Then gamma' = w^-1 gamma w lies in Gamma (normal of
   index 2), has the same translation length l, its axis passes through y', and
   d(x0, gamma' x0) <= 2 d(x0, y') + l <= 2 r + l.
   So every length l <= L of a closed geodesic of O is the length of an element g in Gamma with
   d(x0, g x0) <= L + 2r.  These are enumerated as tiles wP, w in W, by breadth-first search over
   side-adjacent tiles, pruned at d(x0, w x0) > L + 3r: a tile met by the segment [x0, g x0]
   contains a point z of it, so d(x0, w x0) <= d(x0, z) + d(z, w x0) <= d(x0, g x0) + r, and the
   tiles met by the segment form a side-connected chain from P to gP.  Tiles are identified by
   the image of x0 (W acts freely on the interior of P); distinct images are at least
   2 d(x0, dP) apart.  For an orientation-preserving g in SO+(2,1), tr g = 1 + 2 cosh l(g) when g
   is hyperbolic (tr g > 3) and tr g = 1 + 2 cos(phi) < 3 for a rotation.  The least l found is the
   systole, provided it is <= L.  All cutoffs carry a margin of 1e-6 against round-off (the
   arithmetic has 40 digits).  The run is repeated at 50 digits and must agree to 1e-30.
2. Diameters.
   diam P = max over pairs of vertices of the vertex distance (P convex, the distance convex).
   (a) the true diameter of O.  Same-copy distances are d(x, y) <= diam P (the folding map O -> P
       is 1-Lipschitz and P is convex); opposite-copy distances are
       f(x, y) = min_{z in dP} d(x, z) + d(z, y)
       = min( min_v d(x,v) + d(v,y),  min over sides i whose segment contains the crossing
              point of [x, s_i y] of d(x, s_i y) ),
       since z -> d(x,z) + d(z,y) is convex along each side.  diam O = max(diam P, max_{x,y} f).
       max f is computed by a grid of pairs (Klein-model barycentric grid) and Nelder-Mead from
       the best 40 grid pairs (float64).  Every evaluated value is a distance of O, so the result is
       a lower bound for diam O and, numerically, its value.
   (b) rigorous elementary upper bounds.
       B1 = 2 diam P ("twice the longest side" for a triangle): for x, y in different copies and a
            vertex v, d(x, y') <= d(x, v) + d(v, y) <= 2 diam P; same copy <= diam P.
       B2 = max(diam P, 2 max_v d(z, v)) for any fixed z in dP (here: z chosen to minimise
            max_v d(z, v) over a fine sample of dP), by the same argument through z.
3. D(A, eps, M) of Theorem 4.4 (eigen_common.diam_bound) with eps = the systole lower bound.

Writes theory/eigen/data/instances.csv.  Raises on: geometry checks (angles, area by Gauss-Bonnet,
vertices on their sides), integrality-free checks of the enumeration (the systole found <= L, the
two precisions agree, the tile count against the area of the pruning ball), the systole of the
family equal to 4b (numerics/moduli) and to the committed geometries.json values, the systole lower
bound below the computed value, B2 <= B1, true diameter <= B2.
"""
import csv
import json
import math
import os
import sys

import mpmath as mp
import numpy as np
from scipy.optimize import minimize

from eigen_common import check, diam_bound

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
TAUS = ("0.0", "0.4", "0.8", "1.2", "1.6", "2.0", "2.4", "2.8")
L_ENUM = mp.mpf(4)          # lengths enumerated: every closed geodesic of length <= 4


# ------------------------------------------------------------------ hyperboloid model
def lor(u, v):
    return -u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def cross(u, v):
    return [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]


def meet(n1, n2):
    """Point of H^2 on both lines n1^perp, n2^perp."""
    c = cross([-n1[0], n1[1], n1[2]], [-n2[0], n2[1], n2[2]])   # orthogonal (Euclidean) to J n1, J n2
    q = lor(c, c)
    check(q < 0, "lines meet in H^2")
    s = 1 / mp.sqrt(-q)
    if c[0] < 0:
        s = -s
    return [x * s for x in c]


def dist(x, y):
    return mp.acosh(max(-lor(x, y), mp.mpf(1)))


class Polygon:
    """Convex polygon: unit normals n_i of its sides in cyclic order, vertices v_i = side i n side
    i+1, the angles pi/m_i at v_i, the exact area."""

    def __init__(self, name, normals, orders, area):
        self.name = name
        self.n = normals
        self.k = len(normals)
        self.orders = orders
        self.area = area                          # area of P (the orbifold has 2 area)
        self.v = [meet(normals[i], normals[(i + 1) % self.k]) for i in range(self.k)]
        for i in range(self.k):
            check(abs(lor(normals[i], normals[i])) - 1 < mp.mpf(10) ** -30, "unit normals")
            # angle at v_i between sides i and i+1: <n_i, n_{i+1}> = -cos(pi/m)
            check(abs(lor(normals[i], normals[(i + 1) % self.k]) + mp.cos(mp.pi / orders[i])) < mp.mpf(10) ** -30,
                  f"{name}: angle pi/{orders[i]} at vertex {i}")
            for v in (self.v[i - 1], self.v[i]):
                check(abs(lor(normals[i], v)) < mp.mpf(10) ** -30, "vertex on its side")
        # Gauss-Bonnet: area = (k-2) pi - sum of angles
        check(abs(area - ((self.k - 2) * mp.pi - sum(mp.pi / m for m in orders))) < mp.mpf(10) ** -30, "area")
        # orient normals outward: <n_i, x> < 0 at an interior point
        kc = [sum(v[j] / v[0] for v in self.v) / self.k for j in (1, 2)]
        s = 1 / mp.sqrt(1 - kc[0] ** 2 - kc[1] ** 2)
        self.x0 = [s, s * kc[0], s * kc[1]]       # Klein centroid of the vertices
        self.n = [n if lor(n, self.x0) < 0 else [-c for c in n] for n in self.n]
        for v in self.v:
            for n in self.n:
                check(lor(n, v) < mp.mpf(10) ** -30, "convex: vertices on the inner side of every side")
        self.d_bdry = min(mp.asinh(-lor(n, self.x0)) for n in self.n)
        self.r = max(dist(self.x0, v) for v in self.v)
        self.diamP = max(dist(a, b) for a in self.v for b in self.v)


def triangle(p, q, r):
    al, be, ga = mp.pi / p, mp.pi / q, mp.pi / r
    n1 = [mp.mpf(0), mp.mpf(0), mp.mpf(-1)]                  # the x1-axis
    n2 = [mp.mpf(0), -mp.sin(al), mp.cos(al)]                 # the ray at angle pi/p
    c1 = (mp.cos(ga) + mp.cos(al) * mp.cos(be)) / mp.sin(al)
    c2 = mp.cos(be)
    n3 = [mp.sqrt(c1 ** 2 + c2 ** 2 - 1), c1, c2]
    # cyclic order of sides 2, 1, 3: vertices 2n1 = A (pi/p), 1n3 = B (pi/q), 3n2 = C (pi/r)
    P = Polygon(f"O({p},{q},{r})", [n2, n1, n3], (p, q, r), mp.pi - al - be - ga)
    # side lengths against the law of cosines for angles
    A, B, C = P.v
    for (x, y, opp, a1, a2) in ((A, B, ga, al, be), (A, C, be, al, ga), (B, C, al, be, ga)):
        check(abs(mp.cosh(dist(x, y)) - (mp.cos(opp) + mp.cos(a1) * mp.cos(a2)) / (mp.sin(a1) * mp.sin(a2)))
              < mp.mpf(10) ** -28, "law of cosines")
    return P


def quadrilateral(tau):
    tau = mp.mpf(tau)
    sa, sb = mp.sqrt(mp.mpf(1) / 2) * mp.e ** (tau / 2), mp.sqrt(mp.mpf(1) / 2) * mp.e ** (-tau / 2)
    ca, cb = mp.sqrt(1 + sa ** 2), mp.sqrt(1 + sb ** 2)
    E = [sa, ca, mp.mpf(0)]          # the line through (cosh a, sinh a, 0) orthogonal to the x1-axis
    Nn = [sb, mp.mpf(0), cb]
    Wn = [sa, -ca, mp.mpf(0)]
    S = [sb, mp.mpf(0), -cb]
    P = Polygon(f"O_tau={mp.nstr(tau, 2)}", [E, Nn, Wn, S], (3, 3, 3, 3), 2 * mp.pi / 3)
    P.a, P.b = mp.asinh(sa), mp.asinh(sb)
    # the side distances from the centre are a and b
    o = [mp.mpf(1), mp.mpf(0), mp.mpf(0)]
    check(abs(mp.asinh(abs(lor(E, o))) - P.a) < mp.mpf(10) ** -30, "east side at distance a")
    check(abs(mp.asinh(abs(lor(Nn, o))) - P.b) < mp.mpf(10) ** -30, "north side at distance b")
    return P


# ------------------------------------------------------------------ enumeration
def length_spectrum(P, L, dps):
    """Distinct translation lengths <= L of hyperbolic elements of Gamma, with the number of
    elements g with d(x0, g x0) <= L + 2r realising each; and the number of tiles visited."""
    with mp.workdps(dps):
        eps_margin = mp.mpf(10) ** -6
        x0 = [mp.mpf(c) for c in P.x0]
        r = P.r
        cosh_prune = mp.cosh(L + 3 * r + eps_margin)
        cosh_keep = mp.cosh(L + 2 * r + eps_margin)
        refl = []
        for n in P.n:
            n = [mp.mpf(c) for c in n]
            refl.append((n, [-n[0], n[1], n[2]]))   # x -> x - 2 n <Jn, x>_E
        sep = 2 * math.sinh(float(P.d_bdry))       # Euclidean R^3 separation of distinct images
        cell, tol = sep / 4, sep / 100
        grid = {}

        def seen_or_add(y):
            yf = [float(c) for c in y]
            c = tuple(int(math.floor(t / cell)) for t in yf)
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for dz in (-1, 0, 1):
                        for q in grid.get((c[0] + dx, c[1] + dy, c[2] + dz), ()):
                            if abs(q[0] - yf[0]) + abs(q[1] - yf[1]) + abs(q[2] - yf[2]) < tol:
                                return True
            grid.setdefault(c, []).append(yf)
            return False

        I = [[mp.mpf(int(i == j)) for j in range(3)] for i in range(3)]
        seen_or_add(x0)
        frontier = [(I, 0)]
        ntiles = 1
        lengths = []
        while frontier:
            new = []
            for g, par in frontier:
                for n, Jn in refl:
                    # h = g R, R = I - 2 n (Jn)^T :  h = g - 2 (g n)(Jn)^T
                    gn = [g[i][0] * n[0] + g[i][1] * n[1] + g[i][2] * n[2] for i in range(3)]
                    h = [[g[i][j] - 2 * gn[i] * Jn[j] for j in range(3)] for i in range(3)]
                    y = [h[i][0] * x0[0] + h[i][1] * x0[1] + h[i][2] * x0[2] for i in range(3)]
                    ch = -lor(x0, y)
                    if ch > cosh_prune:
                        continue
                    if seen_or_add(y):
                        continue
                    ntiles += 1
                    p = 1 - par
                    new.append((h, p))
                    if p == 0 and ch <= cosh_keep:
                        tr = h[0][0] + h[1][1] + h[2][2]
                        if tr > 3 + mp.mpf(10) ** -20:
                            l = mp.acosh((tr - 1) / 2)
                            if l <= L:
                                lengths.append(l)
            frontier = new
        lengths.sort()
        distinct = []
        for l in lengths:
            if distinct and abs(l - distinct[-1][0]) < mp.mpf(10) ** -20:
                distinct[-1][1] += 1
            else:
                distinct.append([l, 1])
        # sanity: the tiles visited fill the pruning ball up to its boundary layer
        R = float(L + 3 * r)
        ball_tiles = 2 * math.pi * (math.cosh(R) - 1) / float(P.area)
        check(ntiles >= 0.2 * ball_tiles and ntiles <= 2 * ball_tiles + 100,
              f"{P.name}: {ntiles} tiles against {ball_tiles:.0f} in the pruning ball")
        return distinct, ntiles


# ------------------------------------------------------------------ diameters
def boundary_center_bound(P, nsamp=4000):
    """B2 = max(diam P, 2 max_v d(z, v)) for z on dP minimising max_v d(z, v) over a sample."""
    best = None
    Vh = np.array([[float(c) for c in v] for v in P.v])
    for i in range(P.k):
        a, b = P.v[i - 1], P.v[i]               # side i joins v_{i-1} and v_i
        Ka = np.array([float(a[1] / a[0]), float(a[2] / a[0])])
        Kb = np.array([float(b[1] / b[0]), float(b[2] / b[0])])
        s = np.linspace(0, 1, nsamp)
        K = (1 - s)[:, None] * Ka + s[:, None] * Kb
        X = np.column_stack([np.ones(nsamp), K]) / np.sqrt(1 - (K ** 2).sum(1))[:, None]
        ch = X[:, :1] * Vh[None, :, 0] - X[:, 1:2] * Vh[None, :, 1] - X[:, 2:3] * Vh[None, :, 2]
        m = np.arccosh(np.maximum(ch, 1.0)).max(axis=1)
        j = int(np.argmin(m))
        if best is None or m[j] < best[0]:
            best = (float(m[j]), i, float(s[j]))
    # evaluate the chosen z exactly (any z on dP gives a valid bound)
    _, i, s = best
    a, b = P.v[i - 1], P.v[i]
    s = mp.mpf(s)
    k = [(1 - s) * a[j] / a[0] + s * b[j] / b[0] for j in (1, 2)]
    w = 1 / mp.sqrt(1 - k[0] ** 2 - k[1] ** 2)
    z = [w, w * k[0], w * k[1]]
    check(abs(lor(P.n[i], z)) < mp.mpf(10) ** -25, "z on its side")
    m = max(dist(z, v) for v in P.v)
    return max(P.diamP, 2 * m), z


class FloatPoly:
    """float64 copy of P in the Klein model, for the diameter search."""

    def __init__(self, P):
        self.V = np.array([[float(v[1] / v[0]), float(v[2] / v[0])] for v in P.v])
        self.Vh = np.array([[float(c) for c in v] for v in P.v])
        self.N = np.array([[float(c) for c in n] for n in P.n])
        self.k = P.k
        # side i joins vertex i-1 and vertex i
        self.R = []
        for n in self.N:
            Jn = np.array([-n[0], n[1], n[2]])
            self.R.append(np.eye(3) - 2 * np.outer(n, Jn))

    @staticmethod
    def hyp(K):
        s = 1 / np.sqrt(1 - (K ** 2).sum(-1))
        return np.stack([s, s * K[..., 0], s * K[..., 1]], -1)

    @staticmethod
    def d(X, Y):
        c = X[..., 0] * Y[..., 0] - X[..., 1] * Y[..., 1] - X[..., 2] * Y[..., 2]
        return np.arccosh(np.maximum(c, 1.0))

    def opposite(self, X, Y):
        """f(x, y) = distance between x in one copy and y in the other."""
        with np.errstate(divide="ignore", invalid="ignore"):
            return self._opposite(X, Y)

    def _opposite(self, X, Y):
        out = np.full(X.shape[:-1], np.inf)
        for v in self.Vh:
            out = np.minimum(out, self.d(X, v) + self.d(Y, v))
        for i in range(self.k):
            Ys = Y @ self.R[i].T
            # crossing point of the Klein segment [x, s_i y] with side line i, and its position on
            # the side segment v_{i-1} v_i
            kx = X[..., 1:] / X[..., :1]
            ky = Ys[..., 1:] / Ys[..., :1]
            a, b = self.V[i - 1], self.V[i]
            e = b - a
            nrm = np.array([e[1], -e[0]])
            fx = (kx - a) @ nrm
            fy = (ky - a) @ nrm
            lam = fx / (fx - fy)
            z = kx + lam[..., None] * (ky - kx)
            u = ((z - a) @ e) / (e @ e)
            ok = (u >= 0) & (u <= 1)
            out = np.where(ok, np.minimum(out, self.d(X, Ys)), out)
        return out

    def project(self, k):
        """Nearest point of the Klein polygon (Euclidean projection; only used to keep the search
        inside P)."""
        inside = True
        for i in range(self.k):
            a, b = self.V[i - 1], self.V[i]
            e = b - a
            nrm = np.array([e[1], -e[0]])
            c = self.V.mean(0)
            if (c - a) @ nrm < 0:
                nrm = -nrm
            if (k - a) @ nrm < 0:
                inside = False
        if inside:
            return k
        best, bd = None, np.inf
        for i in range(self.k):
            a, b = self.V[i - 1], self.V[i]
            e = b - a
            u = np.clip(((k - a) @ e) / (e @ e), 0, 1)
            q = a + u * e
            dd = np.sum((k - q) ** 2)
            if dd < bd:
                best, bd = q, dd
        return best


def true_diameter(P, n=36):
    F = FloatPoly(P)
    # sanity: the opposite-copy distance of a point to its own copy is 2 d(x, dP)
    for kk in (F.V.mean(0), 0.5 * F.V.mean(0) + 0.5 * F.V[0], 0.3 * F.V.mean(0) + 0.7 * F.V[1]):
        X = F.hyp(kk)
        dd = min(np.arcsinh(abs(-u[0] * X[0] + u[1] * X[1] + u[2] * X[2])) for u in F.N)
        check(abs(float(F.opposite(X, X)) - 2 * dd) < 1e-9, "f(x, x) = 2 d(x, dP)")
    # Klein grid: barycentric over a fan of triangles from the centroid
    c = F.V.mean(0)
    pts = []
    for i in range(F.k):
        a, b = F.V[i - 1], F.V[i]
        for p in range(n + 1):
            for q in range(n + 1 - p):
                pts.append(c + (a - c) * p / n + (b - c) * q / n)
    K = np.unique(np.round(np.array(pts), 12), axis=0)
    X = F.hyp(K)
    best = []
    for j in range(0, len(X), 400):
        f = F.opposite(X[j:j + 400, None, :], X[None, :, :])
        idx = np.argsort(f, axis=None)[-40:]
        for t in idx:
            a, b = np.unravel_index(t, f.shape)
            best.append((float(f[a, b]), j + a, b))
    best.sort(reverse=True)
    cands = best[:12]

    def neg(z):
        kx, ky = F.project(z[:2]), F.project(z[2:])
        return -float(F.opposite(F.hyp(kx), F.hyp(ky)))

    vmax, arg = cands[0][0], (K[cands[0][1]], K[cands[0][2]])
    for val, a, b in cands:
        res = minimize(neg, np.concatenate([K[a], K[b]]), method="Nelder-Mead",
                       options=dict(xatol=1e-12, fatol=1e-14, maxiter=2000))
        if -res.fun > vmax:
            vmax = -res.fun
            arg = (F.project(res.x[:2]), F.project(res.x[2:]))
    return max(float(P.diamP), vmax), vmax, arg


# ------------------------------------------------------------------ main
def instances():
    out = [("O(2,8,8)", triangle(2, 8, 8), (0, (2, 8, 8))), ("O(3,3,12)", triangle(3, 3, 12), (0, (3, 3, 12)))]
    for tau in TAUS:
        out.append((f"O_tau={tau}", quadrilateral(tau), (0, (3, 3, 3, 3))))
    return out


def floor6(x):
    return mp.floor(x * 10 ** 6) / 10 ** 6


def main():
    mp.mp.dps = 40
    geo = json.load(open(os.path.join(ROOT, "numerics", "moduli", "data", "geometries.json")))["members"]
    rows = []
    for name, P, sig in instances():
        spec40, nt40 = length_spectrum(P, L_ENUM, 40)
        spec50, nt50 = length_spectrum(P, L_ENUM, 50)
        check(nt40 == nt50 and len(spec40) == len(spec50), f"{name}: enumeration independent of precision")
        for (a, ma), (b, mb) in zip(spec40, spec50):
            check(abs(a - b) < mp.mpf(10) ** -30 and ma == mb, f"{name}: lengths agree at 40 and 50 digits")
        check(len(spec40) >= 2 and spec40[1][0] <= L_ENUM, f"{name}: systole and second length below L")
        sysl, second = spec40[0][0], spec40[1][0]
        lb = floor6(sysl)
        check(sysl - lb > mp.mpf(10) ** -20, "lower bound strictly below the computed systole")
        Aorb = 2 * P.area
        diamP = P.diamP
        B1 = 2 * diamP
        B2, z = boundary_center_bound(P)
        check(B2 <= B1 + mp.mpf(10) ** -30, "B2 <= B1")
        dtrue, fmax, arg = true_diameter(P)
        check(dtrue <= B2 + 1e-9, f"{name}: true diameter below the bound B2")
        if name.startswith("O_tau"):
            tau = name.split("=")[1]
            check(abs(sysl - 4 * P.b) < mp.mpf(10) ** -30, f"{name}: systole = 4b")
            check(abs(sysl - mp.mpf(geo[tau]["systole"])) < 1e-12, f"{name}: systole = geometries.json")
            check(abs(B1 - mp.mpf(geo[tau]["diam_O_upper_bound"])) < 1e-9, f"{name}: B1 = geometries.json diam_O_upper_bound")
        Ms = (12,) if name.startswith("O(") else (3, 12)
        Ds = {M: diam_bound(Aorb, lb, M) for M in Ms}
        rows.append(dict(name=name, sig=sig, area_over_pi=mp.nstr(Aorb / mp.pi, 15), systole=sysl, second=second,
                         mult_sys=spec40[0][1], lb=lb, ntiles=nt40, r=P.r, diamP=diamP, B1=B1, B2=B2, dtrue=dtrue,
                         D=Ds, fmax=fmax))
        print(f"{name}: systole {mp.nstr(sysl, 20)} (lower bound {mp.nstr(lb, 7)}), second length "
              f"{mp.nstr(second, 12)}, {nt40} tiles (r = {mp.nstr(P.r, 6)}, cutoff L + 2r = {mp.nstr(L_ENUM + 2 * P.r, 6)});"
              f" diam P {mp.nstr(diamP, 8)}, max opposite-copy distance {fmax:.6f}, B1 = 2 diam P {mp.nstr(B1, 8)}, B2 {mp.nstr(B2, 8)}, true diam {dtrue:.6f};"
              + " D(A,eps,M) " + ", ".join(f"M={M}: {mp.nstr(v, 6)}" for M, v in Ds.items()), flush=True)
    path = os.path.join(HERE, "data", "instances.csv")
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["orbifold", "signature", "area_over_pi", "systole_computed", "systole_lower_bound",
                    "second_length", "tiles_enumerated", "enum_L", "x0_radius_r", "diam_P",
                    "diam_upper_B1_2diamP", "diam_upper_B2", "max_opposite_copy_distance", "diam_true_numerical", "D_M3", "D_M12"])
        for r in rows:
            w.writerow([r["name"], f"{r['sig']}", r["area_over_pi"], mp.nstr(r["systole"], 15), mp.nstr(r["lb"], 7),
                        mp.nstr(r["second"], 12), r["ntiles"], mp.nstr(L_ENUM, 2), mp.nstr(r["r"], 10),
                        mp.nstr(r["diamP"], 12), mp.nstr(r["B1"], 12), mp.nstr(r["B2"], 12), f"{r['fmax']:.6f}", f"{r['dtrue']:.6f}",
                        mp.nstr(r["D"][3], 8) if 3 in r["D"] else "", mp.nstr(r["D"][12], 8)])
    print(f"wrote {os.path.relpath(path, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
