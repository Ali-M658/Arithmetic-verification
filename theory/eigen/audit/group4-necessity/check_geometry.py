"""Group 4 audit: geometry of Q_{k,b}, O(2,3,m) cone ball and systole.  Raises on failure.
Hyperboloid model, <x,y> = x0 y0 + x1 y1 - x2 y2, O = (0,0,1).
"""
import itertools
import mpmath as mp
mp.mp.dps = 40


def mink(x, y):
    return x[0]*y[0] + x[1]*y[1] - x[2]*y[2]


def fermi(rho, s):
    # point at signed distance rho from beta = {(sinh t,0,cosh t)}, foot at arclength s
    return [mp.cosh(rho)*mp.sinh(s), mp.sinh(rho), mp.cosh(rho)*mp.cosh(s)]


def tangent_toward(p, q):
    # unit tangent at p of the geodesic from p to q
    d = mp.acosh(-mink(p, q))
    v = [(q[i] - mp.cosh(d)*p[i])/mp.sinh(d) for i in range(3)]
    return v


# ---------- Q_{k,b} ----------
worst = 0
for k in (3, 4):
    for b in [mp.mpf(10)**e for e in mp.linspace(-4, 0.7, 48)]:
        a = mp.asinh(mp.cos(mp.pi/k)/mp.sinh(b))
        nP = [mp.cosh(b), 0, mp.sinh(b)]            # line perpendicular to beta at s=b
        nPm = [mp.cosh(b), 0, -mp.sinh(b)]          # at s=-b
        nR = [0, mp.cosh(a), mp.sinh(a)]            # perpendicular to beta' at distance a
        nRm = [0, mp.cosh(a), -mp.sinh(a)]
        for n in (nP, nPm, nR, nRm):
            if abs(mink(n, n) - 1) > mp.mpf(10)**-20:
                raise AssertionError("normal not unit")
        if abs(abs(mink(nP, nR)) - mp.cos(mp.pi/k)) > mp.mpf(10)**-20:
            raise AssertionError("cos angle")
        # vertex V: s=b, tanh rho_V = cosh b tanh a ; needs < 1 (lines meet)
        tv = mp.cosh(b)*mp.tanh(a)
        if not tv < 1:
            raise AssertionError(f"P and R lines do not meet: k={k} b={b}")
        rhoV = mp.atanh(tv)
        V = fermi(rhoV, b)
        if abs(mink(V, nP)) > 1e-25 or abs(mink(V, nR)) > 1e-25:
            raise AssertionError("vertex not on both lines")
        if not rhoV > a:
            raise AssertionError("vertex inside collar")
        # interior angle at V: between geodesic V->B=(0,b) [along P side] and V->A'=(a on beta')
        B = fermi(0, b)
        Ap = [0, mp.sinh(a), mp.cosh(a)]
        t1, t2 = tangent_toward(V, B), tangent_toward(V, Ap)
        ang = mp.acos(mink(t1, t2))
        if abs(ang - mp.pi/k) > mp.mpf(10)**-20:
            raise AssertionError(f"interior angle {ang} != pi/{k}")
        # Lambert quarter: angles at O, B, A' are right angles (beta perp beta', P perp beta, R perp beta')
        # rectangle {|rho|<a,|s|<=b} inside the four half-planes containing O
        sO = [mp.sign(mink([0, 0, 1], n)) for n in (nP, nPm, nR, nRm)]
        for rho in mp.linspace(-a*(1 - mp.mpf(10)**-12), a*(1 - mp.mpf(10)**-12), 41):
            for s in mp.linspace(-b, b, 41):
                x = fermi(rho, s)
                for n, sg in zip((nP, nPm, nR, nRm), sO):
                    val = mink(x, n)*sg
                    if val < -mp.mpf(10)**-25*mp.cosh(a)*mp.cosh(b)*mp.cosh(rho)*mp.cosh(s):
                        raise AssertionError(f"rectangle point outside Q: k={k} b={b} rho={rho} s={s}")
                    worst = max(worst, -val)
        # reflection s -> 2b - s fixes the P-line pointwise (doubling across it is smooth in Fermi coords)
        for rho in (mp.mpf('0.3'), a/2):
            x, y = fermi(rho, b + mp.mpf('0.1')), fermi(rho, b - mp.mpf('0.1'))
            # reflection in line with normal n: x - 2<x,n> n
            rx = [x[i] - 2*mink(x, nP)*nP[i] for i in range(3)]
            if max(abs(rx[i] - y[i]) for i in range(3)) > mp.mpf(10)**-25:
                raise AssertionError("reflection in P-line is not s -> 2b-s")
print("Q_{k,b}: unit normals, |<nP,nR>|=cos(pi/k), interior angle pi/k, vertex rho_V>a,"
      " rectangle in Q, reflection = (rho,s)->(rho,2b-s): OK for k=3,4, b in [1e-4, 5]")

# ---------- O(2,3,m) in PSL(2,R) ----------
def gens(m):
    c = 2*mp.cos(mp.pi/m)
    r = (-c + mp.sqrt(c*c - 3))/2
    q = c + r
    x = mp.matrix([[0, -1], [1, 0]])
    y = mp.matrix([[mp.mpf(1)/2, q], [r, mp.mpf(1)/2]])
    return x, y


def fixed_pt(g):
    # fixed point in upper half plane of elliptic g = [[p,q],[r,s]]: r z^2 + (s-p) z - q = 0
    p, q, r, s = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    disc = (s - p)**2 + 4*q*r
    z = (-(s - p) + mp.sqrt(disc))/(2*r)
    if mp.im(z) < 0:
        z = (-(s - p) - mp.sqrt(disc))/(2*r)
    return z


def dist(z, w):
    return mp.acosh(1 + abs(z - w)**2/(2*mp.im(z)*mp.im(w)))


def apply(g, z):
    return (g[0, 0]*z + g[0, 1])/(g[1, 0]*z + g[1, 1])


mp.mp.dps = 30
sinf = mp.acosh(2/mp.sqrt(3))
sigma0 = 2*mp.asinh(1/(2*mp.sqrt(1 + mp.mpf(3)/4*mp.cosh(2*sinf)**2)))
NW = 12   # words (x y^{e1}) ... (x y^{en}), n <= NW
rows = []
for m in [7, 8, 9, 10, 11, 12, 13, 15, 20, 30, 50, 100, 1000]:
    x, y = gens(m)
    for g, o in ((x, 2), (y, 3), (x*y, m)):
        if abs(abs(g[0, 0] + g[1, 1]) - 2*mp.cos(mp.pi/o)) > 1e-20:
            raise AssertionError("generator orders")
    Qp, Pp = fixed_pt(x), fixed_pt(x*y)
    hm = mp.acosh(1/(2*mp.sin(mp.pi/m)))
    if abs(dist(Pp, Qp) - hm) > 1e-15:
        raise AssertionError(f"d(P,Q) != h_m for m={m}: {dist(Pp, Qp)} vs {hm}")
    xs = [x*y, x*y**2]   # x y^{+1}, x y^{-1}
    best = mp.inf
    minPorbit = mp.inf
    for n in range(1, NW + 1):
        for es in itertools.product((0, 1), repeat=n):
            g = mp.eye(2)
            for e in es:
                g = g*xs[e]
            t = abs(g[0, 0] + g[1, 1])
            if t > 2 + 1e-12:
                best = min(best, 2*mp.acosh(t/2))
            # P-orbit distances for embeddedness of the cone ball (also y^{+-1} g)
            for pre in (mp.eye(2), y, y*y):
                h = pre*g
                zP = apply(h, Pp)
                dd = dist(Pp, zP)
                if dd > 1e-10:
                    minPorbit = min(minPorbit, dd)
    rows.append((m, best, minPorbit, 2*hm))
    if not best >= sigma0:
        raise AssertionError(f"systole of O(2,3,{m}) found {best} < sigma0 {sigma0}")
    if not minPorbit >= 2*hm - 1e-12:
        raise AssertionError(f"cone ball radius h_m not embedded for m={m}: {minPorbit} < {2*hm}")
print(f"O(2,3,m): sigma0 = {mp.nstr(sigma0, 10)};  words of length <= {2*NW} in x, y^(+-1)")
print("   m   min translation length found   min_{gP!=P} d(P,gP)   2 h_m")
for m, best, mo, hh in rows:
    print(f"{m:5d}   {mp.nstr(best, 10):>24}   {mp.nstr(mo, 10):>18}   {mp.nstr(hh, 10)}")
print("ALL GEOMETRY CHECKS PASSED")
