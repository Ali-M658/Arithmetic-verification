"""Counterexample hunt on explicit Fuchsian groups (hyperboloid model, O(2,1), float64).

Groups: orientation-preserving subgroups Gamma of reflection groups of
  * hyperbolic triangles (pi/p, pi/q, pi/r), 2 <= p <= q <= r <= 12  -> O(p,q,r)
  * the quadrilaterals Q_{k,b} (k = 3, 4; several b), doubles = spheres with four order-k points
For each Gamma (BFS over even reflection words, deduplicated) we compute
  eps_est = min translation length of enumerated hyperbolic elements  (>= true systole)
  dmin    = min distance from a base vertex to a distinct enumerated elliptic point
and test Lemma eig:sep: dmin >= d0(eps_true, M).  Since d0 is nondecreasing in eps and
eps_true <= eps_est, testing dmin >= d0(eps_est, M) is a STRONGER test.
For triangle groups we also estimate the orbifold diameter by sampling and compare with D(A,eps,M)
(Theorem eig:diam) and its closed form; the diameter estimate is a lower bound up to sampling,
so diam_est < D is a necessary condition.
"""
from fractions import Fraction
import math
import numpy as np

J = np.diag([1.0, 1.0, -1.0])


def mink(u, v):
    return u[0] * v[0] + u[1] * v[1] - u[2] * v[2]


def refl(n):
    # v -> v - 2 <v,n> n ;  as matrix:  I - 2 n n^T J
    return np.eye(3) - 2.0 * np.outer(n, n) @ J


def lcross(u, v):
    w = np.cross(u, v)
    return np.array([w[0], w[1], -w[2]])


def unit_normal(pt, tang):
    n = lcross(pt, tang)
    return n / math.sqrt(mink(n, n))


def vertex(n1, n2):
    w = lcross(n1, n2)
    w = w / math.sqrt(-mink(w, w))
    return w if w[2] > 0 else -w


def triangle(p, q, r):
    al, be, ga = math.pi / p, math.pi / q, math.pi / r
    c = math.acosh((math.cos(ga) + math.cos(al) * math.cos(be)) / (math.sin(al) * math.sin(be)))
    P = np.array([0.0, 0.0, 1.0]); Q = np.array([math.sinh(c), 0.0, math.cosh(c)])
    nl = np.array([0.0, 1.0, 0.0])
    n1 = unit_normal(P, np.array([math.cos(al), math.sin(al), 0.0]))
    n3 = unit_normal(Q, np.array([-math.cosh(c) * math.cos(be), math.sin(be), -math.sinh(c) * math.cos(be)]))
    R = vertex(n1, n3)
    normals = [nl, n1, n3]
    verts = [(P, p), (Q, q), (R, r)]
    return normals, verts


def quad(k, b):
    a = math.asinh(math.cos(math.pi / k) / math.sinh(b))
    normals = [np.array([math.cosh(b), 0, math.sinh(b)]), np.array([0, math.cosh(a), math.sinh(a)]),
               np.array([math.cosh(b), 0, -math.sinh(b)]), np.array([0, math.cosh(a), -math.sinh(a)])]
    # the four sides; adjacent pairs meet at angle pi/k
    for i in range(4):
        x = abs(mink(normals[i], normals[(i + 1) % 4]))
        assert abs(x - math.cos(math.pi / k)) < 1e-12
    verts = [(vertex(normals[i], normals[(i + 1) % 4]), k) for i in range(4)]
    return normals, verts


def enumerate_group(normals, maxn, cap):
    R = [refl(n) for n in normals]
    gens = [R[i] @ R[j] for i in range(len(R)) for j in range(len(R)) if i != j]
    seen = {}
    key = lambda g: tuple(np.round(g.ravel(), 7))
    frontier = [np.eye(3)]
    seen[key(np.eye(3))] = np.eye(3)
    while frontier and len(seen) < maxn:
        new = []
        for g in frontier:
            for s in gens:
                h = g @ s
                if h[2, 2] > cap:
                    continue
                kk = key(h)
                if kk not in seen:
                    seen[kk] = h
                    new.append(h)
                    if len(seen) >= maxn:
                        break
            if len(seen) >= maxn:
                break
        frontier = new
    return list(seen.values())


def d0(eps, M):
    return min(eps / 2, math.acosh(1 + 2 / (math.pi ** 2 * M ** 2)))


def Dbound(A, eps, M):
    r0 = d0(eps, M) / 2
    rho1 = math.asinh(math.sinh(r0) * math.sin(math.pi / M))
    v0 = 2 * math.pi * min((math.cosh(r0) - 1) / M, math.cosh(rho1) - 1)
    return 4 * r0 * A / v0, A / math.pi * max(4 * M, M * M) * max(4 / eps, 10 * M / 3)


def analyse(name, normals, verts, area, M, maxn=40000, cap=60.0, diam=False):
    G = enumerate_group(normals, maxn, cap)
    eps = math.inf
    for g in G:
        t = np.trace(g)
        if t > 3 + 1e-9:
            eps = min(eps, math.acosh((t - 1) / 2))
    # elliptic points: images of vertices; distance from base vertices
    dmin = math.inf; pair = None
    for (v, kv) in verts:
        for g in G:
            for (w, kw) in verts:
                x = g @ w
                c = -mink(v, x)
                if c > 1 + 1e-9:
                    dd = math.acosh(c)
                    if dd < dmin:
                        dmin, pair = dd, (kv, kw)
    bound = d0(eps, M)
    ok = dmin >= bound - 1e-9
    out = "%-22s n=%6d eps_est=%.5f dmin=%.5f (orders %s) d0=%.5f  %s" % (
        name, len(G), eps, dmin, pair, bound, "ok" if ok else "FAIL")
    if not ok:
        raise AssertionError(out)
    if diam:
        # sample the fundamental domain (the triangle and its mirror) and estimate the diameter
        P, Q, R = [v for v, _ in verts]
        rng = np.random.default_rng(1)
        pts = []
        for _ in range(120):
            u = rng.dirichlet([1, 1, 1])
            x = u[0] * P + u[1] * Q + u[2] * R
            x = x / math.sqrt(-mink(x, x))
            pts.append(x)
            pts.append(refl(normals[0]) @ x)     # mirror copy
        pts = np.array(pts)
        Gs = np.array([g for g in G if g[2, 2] < 400])
        imgs = np.einsum('gij,pj->gpi', Gs, pts)        # images of every sample
        best = 0.0
        for i in range(len(pts)):
            c = -(imgs[:, :, 0] * pts[i, 0] + imgs[:, :, 1] * pts[i, 1] - imgs[:, :, 2] * pts[i, 2])
            dist = np.arccosh(np.maximum(c.min(axis=0), 1.0))
            best = max(best, dist.max())
        D, closed = Dbound(area, eps, M)
        if not (best < D <= closed * (1 + 1e-12)):
            raise AssertionError("diameter check failed %s %s %s" % (best, D, closed))
        out += "\n%24s diam_est=%.4f  D=%.4g  closed form=%.4g" % ("", best, D, closed)
    print(out)
    return eps, dmin


if __name__ == "__main__":
    tri = [(p, q, r) for p in range(2, 13) for q in range(p, 13) for r in range(q, 13)
           if Fraction(1, p) + Fraction(1, q) + Fraction(1, r) < 1]
    worst_ratio = math.inf
    for (p, q, r) in tri:
        normals, verts = triangle(p, q, r)
        area = 2 * math.pi * (1 - 1 / p - 1 / q - 1 / r)
        eps, dmin = analyse("O(%d,%d,%d)" % (p, q, r), normals, verts, area, r,
                            maxn=20000, diam=(r <= 8 and q <= 5))
        worst_ratio = min(worst_ratio, dmin / d0(eps, r))
    for k in (3, 4):
        for b in (0.02, 0.05, 0.1, 0.3, 0.6, 1.0):
            normals, verts = quad(k, b)
            area = 2 * math.pi * (2 - 4 / k)
            eps, dmin = analyse("O_{%d,b=%.2f}" % (k, b), normals, verts, area, k, maxn=20000,
                                cap=200.0)
            worst_ratio = min(worst_ratio, dmin / d0(eps, k))
            if eps > 4 * b + 1e-9:
                raise AssertionError("eig:N2 systole <= 4b violated?")
    print("group_enum OK: %d triangle groups + 12 quadrilateral groups; min dmin/d0 = %.4f"
          % (len(tri), worst_ratio))
