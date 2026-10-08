"""
Attack on the "every Riemannian orbisurface / radial part of the jet" clauses of VC1/VC3:
a NON-rotationally-symmetric metric germ with only a Z_2 (resp. Z_m) symmetry.

Geodesic polar coordinates g = dr^2 + f(r,theta)^2 dtheta^2, f_rr = -K f, f(0)=0, f_r(0)=1,
with K(r,theta) a prescribed Z_2-symmetric polynomial in normal coordinates containing
non-radial (frequency 2, 4, ...) parts.  Then
   Delta_g - Delta_0 = -A E - B Theta^2 + Ct Theta,
   A = (f_r/f - 1/r)/r, B = f^{-2} - r^{-2}, Ct = f_theta / f^3,
and the same rescaling + Duhamel + Weyl-algebra machinery as twisted_duhamel.py gives
b_l(phi) for phi = 2 pi j/m.  Exact arithmetic.
Usage: python nonradial_test.py LMAX
"""
import sys
import sympy as sp
from math import comb, factorial
from functools import lru_cache

LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3
r, w = sp.symbols('r w')          # w = e^{i theta}
y1, y2 = sp.symbols('y1 y2')
I = sp.I

# ---------------- K(r,theta) as polynomial in r with Laurent coefficients in w ----------------
k0, k1, k2, k3 = sp.symbols('k0 k1 k2 k3')
h2, g2, g4, q2, q4, q6 = sp.symbols('h2 g2 g4 q2 q4 q6')
cosj = lambda j: (w**j + w**-j) / 2
Kpol = (k0 + r**2 * (k1 + h2 * cosj(2)) + r**4 * (k2 + g2 * cosj(2) + g4 * cosj(4))
        + r**6 * (k3 + q2 * cosj(2) + q4 * cosj(4) + q6 * cosj(6)))
Kpol = sp.expand(Kpol)
NR = 2 * LMAX + 3  # need f up to r^{2 LMAX + 3}


def rcoeffs(expr, n):
    expr = sp.expand(expr)
    return [sp.expand(expr.coeff(r, i)) for i in range(n + 1)]


Kc = rcoeffs(Kpol, NR)
fc = [sp.Integer(0)] * (NR + 3)
fc[1] = sp.Integer(1)
for n in range(NR):
    fc[n + 2] = sp.expand(-sum(Kc[i] * fc[n - i] for i in range(n + 1)) / ((n + 2) * (n + 1)))
# h := f/r = 1 + sum_{n>=1} fc[n+1] r^n
hc = [fc[n + 1] for n in range(NR + 1)]


def ser_mul(a, b, n):
    return [sp.expand(sum(a[i] * b[j - i] for i in range(j + 1))) for j in range(n + 1)]


def ser_inv(a, n):
    out = [sp.Integer(0)] * (n + 1)
    out[0] = 1 / a[0]
    for j in range(1, n + 1):
        out[j] = sp.expand(-sum(a[i] * out[j - i] for i in range(1, j + 1)) / a[0])
    return out


NS = 2 * LMAX  # need coefficient series to r^{2 LMAX - 2}
hinv = ser_inv(hc, NS + 2)
# f_r/f - 1/r = h'/h ; A = h'/(h r): h' = sum n hc[n] r^{n-1}
hp = [sp.expand((n + 1) * hc[n + 1]) for n in range(NS + 2)]
A_ser = ser_mul(hp, hinv, NS + 1)           # h'/h, starts at r^1
A_ser = [A_ser[n + 1] for n in range(NS)]   # divide by r
# B = r^{-2}(h^{-2} - 1)
h2inv = ser_mul(hinv, hinv, NS + 2)
B_ser = [h2inv[n + 2] for n in range(NS)]
# Ct = f_theta/f^3 = r h_theta / (r^3 h^3) = r^{-2} h_theta h^{-3}
dth = lambda e: sp.expand(I * w * sp.diff(e, w))
hth = [dth(c) for c in hc[:NS + 3]]
h3inv = ser_mul(h2inv, hinv, NS + 2)
C_full = ser_mul(hth, h3inv, NS + 2)
assert C_full[0] == 0 and C_full[1] == 0
C_ser = [C_full[n + 2] for n in range(NS)]


def to_cart(coef_w, n):
    """r^n * (Laurent poly in w) -> polynomial in y1,y2"""
    e = sp.expand(coef_w)
    out = 0
    P = sp.Poly(sp.expand(e * w**(n + 2)), w)
    for (dw,), cf in P.terms():
        if cf == 0:
            continue
        j = dw - (n + 2)
        aj = abs(j)
        assert n >= aj and (n - aj) % 2 == 0, (n, j)
        z = (y1 + I * y2) if j >= 0 else (y1 - I * y2)
        out += cf * (y1**2 + y2**2)**((n - aj) // 2) * z**aj
    out = sp.expand(out)
    assert not out.has(I), out
    return out


Acart = [to_cart(A_ser[n], n) for n in range(NS)]
Bcart = [to_cart(B_ser[n], n) for n in range(NS)]
Ccart = [to_cart(C_ser[n], n) for n in range(NS)]
# odd degrees must vanish (Z_2 symmetric K)
for n in range(1, NS, 2):
    assert Acart[n] == 0 and Bcart[n] == 0 and Ccart[n] == 0

# ---------------- Weyl algebra (same as twisted_duhamel.py) ----------------


def mul(Aop, Bop):
    out = {}
    for (a1, a2, b1, b2), ca in Aop.items():
        for (c1, c2, d1, d2), cb in Bop.items():
            cc = ca * cb
            for i in range(min(b1, c1) + 1):
                f1 = comb(b1, i) * factorial(c1) // factorial(c1 - i)
                for j in range(min(b2, c2) + 1):
                    f2 = comb(b2, j) * factorial(c2) // factorial(c2 - j)
                    key = (a1 + c1 - i, a2 + c2 - j, b1 - i + d1, b2 - j + d2)
                    out[key] = out.get(key, 0) + f1 * f2 * cc
    return {kk: sp.expand(v) for kk, v in out.items() if sp.expand(v) != 0}


def add(*ops):
    out = {}
    for O in ops:
        for kk, v in O.items():
            out[kk] = out.get(kk, 0) + v
    return {kk: sp.expand(v) for kk, v in out.items() if sp.expand(v) != 0}


def scal(a, Aop):
    return {kk: a * v for kk, v in Aop.items()}


ONE = {(0, 0, 0, 0): sp.Integer(1)}


def poly_op(p, Y1, Y2):
    """multiplication by polynomial p(y) conjugated: p(Y1,Y2) (Y's commute)."""
    P = sp.Poly(p, y1, y2)
    out = {}
    pw1 = {0: ONE}
    pw2 = {0: ONE}
    for (e1, e2), cf in P.terms():
        for e, pw, Y in ((e1, pw1, Y1), (e2, pw2, Y2)):
            while max(pw) < e:
                pw[max(pw) + 1] = mul(pw[max(pw)], Y)
        out = add(out, scal(cf, mul(pw1[e1], pw2[e2])))
    return out


def Vtilde(kidx, sig):
    Y1 = {(1, 0, 0, 0): 1, (0, 0, 1, 0): 2 * sig}
    Y2 = {(0, 1, 0, 0): 1, (0, 0, 0, 1): 2 * sig}
    D1 = {(0, 0, 1, 0): 1}
    D2 = {(0, 0, 0, 1): 1}
    E = add(mul(Y1, D1), mul(Y2, D2))
    Th = add(mul(Y1, D2), scal(-1, mul(Y2, D1)))
    Th2 = mul(Th, Th)
    d = 2 * (kidx - 1)
    return add(scal(-1, mul(poly_op(Acart[d], Y1, Y2), E)),
               scal(-1, mul(poly_op(Bcart[d], Y1, Y2), Th2)),
               mul(poly_op(Ccart[d], Y1, Y2), Th))


z1, z2 = sp.symbols('z1 z2')
G = sp.exp(-(z1**2 + z2**2) / 4)


@lru_cache(None)
def hermite(b1, b2):
    return sp.expand(sp.simplify(sp.diff(G, z1, b1, z2, b2) / G))


def make_T(phi):
    c, s = sp.cos(phi), sp.sin(phi)
    C2 = sp.nsimplify(2 - 2 * c)
    Mz1 = (1 - c) * y1 - s * y2
    Mz2 = s * y1 + (1 - c) * y2
    Xv = 1 / C2

    @lru_cache(None)
    def T(a1, a2, b1, b2):
        poly = sp.expand(y1**a1 * y2**a2 * hermite(b1, b2).subs({z1: Mz1, z2: Mz2}, simultaneous=True))
        tot = 0
        for (p, q), cf in sp.Poly(poly, y1, y2).terms():
            if p % 2 or q % 2:
                continue
            tot += cf * sp.gamma(sp.Rational(p + 1, 2)) * sp.gamma(sp.Rational(q + 1, 2)) * (4 * Xv)**((p + q) // 2 + 1) / (4 * sp.pi)
        return sp.expand(sp.nsimplify(sp.expand(tot)))
    return T


def compositions(l):
    if l == 0:
        yield ()
        return
    for first in range(1, l + 1):
        for rest in compositions(l - first):
            yield (first,) + rest


sig = sp.symbols('sigma1:12')


def simplex_integrate(expr, sigs):
    e = expr
    n = len(sigs)
    for i in range(n):
        upper = sigs[i + 1] if i + 1 < n else 1
        e = sp.integrate(sp.expand(e), (sigs[i], 0, upper))
    return sp.expand(e)


# precompute the sigma-integrated Duhamel operators once (independent of phi)
DUH = {}
for l in range(1, LMAX + 1):
    tot = {}
    for comp in compositions(l):
        n = len(comp)
        O = ONE
        for i, kk in enumerate(comp):
            O = mul(O, Vtilde(kk, sig[i]))
        O = {kk: simplex_integrate(v, list(sig[:n])) for kk, v in O.items()}
        tot = add(tot, scal((-1)**n, O))
    DUH[l] = tot
    print('Duhamel operator for t^%d: %d monomials' % (l, len(tot)), flush=True)


def b_l(l, phi):
    T = make_T(phi)
    if l == 0:
        return T(0, 0, 0, 0)
    return sp.expand(sum(v * T(*kk) for kk, v in DUH[l].items()))


# ---------------- invariants at p for this non-radial metric ----------------
Ex = lambda u: sp.expand(y1 * sp.diff(u, y1) + y2 * sp.diff(u, y2))
Thx = lambda u: sp.expand(y1 * sp.diff(u, y2) - y2 * sp.diff(u, y1))
NSL = NS


def lap_g(u, order):
    """Delta_g u as polynomial in y truncated at total degree `order` (x-coordinates; same as y here)."""
    out = -(sp.diff(u, y1, 2) + sp.diff(u, y2, 2))
    for d in range(0, NSL, 2):
        out += -Acart[d] * Ex(u) - Bcart[d] * Thx(Thx(u)) + Ccart[d] * Thx(u)
    P = sp.Poly(sp.expand(out), y1, y2)
    return sp.expand(sum(cf * y1**a * y2**b for (a, b), cf in P.terms() if a + b <= order))


Kcart = sum(to_cart(Kc[n], n) for n in range(0, 2 * LMAX + 1))
Kv = Kcart.subs({y1: 0, y2: 0})
L1 = lap_g(Kcart, 2 * LMAX)
DKv = L1.subs({y1: 0, y2: 0})
L2 = lap_g(L1, 2 * LMAX - 2)
D2Kv = L2.subs({y1: 0, y2: 0})
print('K =', Kv, ' Delta_g K(p) =', DKv, ' Delta_g^2 K(p) =', sp.expand(D2Kv))

mm_ = sp.symbols('m')
A = lambda m: sp.Rational((m**2 - 1) * (m**2 + 3) * (3 * m**4 + 2 * m**2 + 19), 30240 * m)
B = lambda m: sp.Rational(-(m**2 - 1) * (7 * m**6 + 47 * m**4 + 173 * m**2 + 733), 201600 * m)
D = lambda m: sp.Rational((m**2 - 1) * (m**2 + 11) * (3 * m**4 + 10 * m**2 + 227), 3628800 * m)

if LMAX >= 3:
    # m = 2 : phi = pi.  Jet has frequency 2 and 4 parts (h2, g2, g4).
    b3pi = b_l(3, sp.pi)
    a3 = sp.expand(b3pi / 2)
    claim = sp.expand(A(2) * Kv**3 + B(2) * Kv * DKv + D(2) * D2Kv)
    print('m=2: a_3(p) - VC3 claim =', sp.expand(a3 - claim))
    assert sp.expand(a3 - claim) == 0
    print('VC3 at m=2 with non-radial Z_2-symmetric jet (h2,g2,g4 != 0): CONFIRMED')
    # m = 4: phi = pi/2, pi, 3pi/2 (jet with only frequencies 0, 4 is Z_4 symmetric)
    sub4 = {h2: 0, g2: 0, q2: 0, q6: 0}
    tot = sum(b_l(3, sp.pi * j / 2) for j in range(1, 4)).subs(sub4)
    claim4 = sp.expand((A(4) * Kv**3 + B(4) * Kv * DKv + D(4) * D2Kv).subs(sub4))
    assert sp.expand(tot / 4 - claim4) == 0
    print('VC3 at m=4 with frequency-4 jet (g4 != 0): CONFIRMED')
    for l in range(1, LMAX + 1):
        e = b_l(l, sp.pi)
        print('b_%d(pi) depends on non-radial params:' % l, sorted(str(s) for s in e.free_symbols & {h2, g2, g4, q2, q4, q6}))
if LMAX >= 4:
    b4pi = b_l(4, sp.pi)
    print('b_4(pi) =', sp.collect(b4pi, [h2]))
    print('=> at m=2, l=4 the traceless Hessian (h2) enters quadratically: m >= l-1 in VC1 is necessary' if b4pi.has(h2)
          else 'b_4(pi) independent of h2')
print('DONE')
