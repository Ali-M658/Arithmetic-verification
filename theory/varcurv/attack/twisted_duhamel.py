"""
Independent computation of Donnelly's coefficients b_l(phi) for a rotation by phi about the
centre p of a rotationally symmetric metric g = dr^2 + f(r)^2 dtheta^2, f'' = -K f.

Method (NOT Schueth's distance-function substitution): parabolic rescaling + Duhamel series
+ Heisenberg conjugation in the Weyl algebra.

  * In Cartesian normal coordinates x, Delta_g = Delta_0 - a(r^2) E - b(r^2) Theta^2, with
      Delta_0 = -(d1^2+d2^2), E = x.grad, Theta = x1 d2 - x2 d1,
      a = (f'/f - 1/r)/r,  b = f^{-2} - r^{-2}   (both even power series in r).
  * Rescale x = sqrt(t) y:  t Delta_g = L_t = Delta_0 + sum_k t^k V_k,
      V_k = -(a_{k-1} |y|^{2k-2} E + b_{k-1} |y|^{2k-2} Theta^2).
  * I(t) = int H(t,x,Phi x) dA = Tr(e^{-L_t} R^*)  (operator trace, basis independent).
  * Duhamel: e^{-(L0+V)} = sum_n (-1)^n int_{0<=s1<=..<=sn<=1} V~(s1)...V~(sn) e^{-L0},
      V~(s) = e^{-s L0} V e^{s L0} = V with y_j -> y_j + 2 s d_j.
  * Tr(y^a d^b e^{-Delta_0} R^*) = int y^a [d_y^b p_1(y,w)]_{w=R^{-1}y} dy : Gaussian moments.
All arithmetic exact (sympy Rationals); cos(phi)=c, sin(phi)=s with s^2 = 1-c^2,
and finally c = 1 - C^2/2.
"""
import sympy as sp
from itertools import product
from functools import lru_cache
from math import comb, factorial
import sys

LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3

r = sp.symbols('r')
k = sp.symbols('k0:6')
c, s, X = sp.symbols('c s X')  # X = C^{-2}

# ---------------- metric data ----------------
N = 2 * LMAX + 4
Kser = sum(k[i] * r**(2 * i) for i in range(LMAX + 1))
# f'' = -K f, f(0)=0, f'(0)=1
coef = [sp.Integer(0)] * (N + 2)
coef[1] = sp.Integer(1)
Kc = sp.Poly(Kser, r).all_coeffs()[::-1]
Kc = Kc + [0] * (N + 2)
for n in range(N):  # coefficient of r^n in f'' : (n+2)(n+1) f_{n+2}
    rhs = -sum(Kc[i] * coef[n - i] for i in range(n + 1))
    coef[n + 2] = sp.expand(rhs / ((n + 2) * (n + 1)))
f = sum(coef[i] * r**i for i in range(N + 2))
fp = sp.diff(f, r)
a_ser = sp.series((fp / f - 1 / r) / r, r, 0, 2 * LMAX).removeO()
b_ser = sp.series(f**-2 - r**-2, r, 0, 2 * LMAX).removeO()
a_c = [sp.expand(a_ser.coeff(r, 2 * i)) for i in range(LMAX)]
b_c = [sp.expand(b_ser.coeff(r, 2 * i)) for i in range(LMAX)]


def lap_radial(h):
    """Delta_g h = -(h'' + f'/f h') for radial h, as series in r."""
    return sp.expand(sp.series(-(sp.diff(h, r, 2) + fp / f * sp.diff(h, r)), r, 0, 2 * LMAX + 1).removeO())


inv = {'K': Kser.subs(r, 0)}
h = Kser
for j in range(1, LMAX + 1):
    h = lap_radial(h)
    inv['D%d' % j] = sp.expand(h.subs(r, 0))

# ---------------- Weyl algebra ----------------
# operator = dict {(a1,a2,b1,b2): coeff}, normal ordered y^a d^b


def mul(A, B):
    out = {}
    for (a1, a2, b1, b2), ca in A.items():
        for (c1, c2, d1, d2), cb in B.items():
            cc = ca * cb
            for i in range(min(b1, c1) + 1):
                f1 = comb(b1, i) * factorial(c1) // factorial(c1 - i)
                for j in range(min(b2, c2) + 1):
                    f2 = comb(b2, j) * factorial(c2) // factorial(c2 - j)
                    key = (a1 + c1 - i, a2 + c2 - j, b1 - i + d1, b2 - j + d2)
                    out[key] = out.get(key, 0) + f1 * f2 * cc
    return {kk: v for kk, v in out.items() if v != 0}


def add(*ops):
    out = {}
    for O in ops:
        for kk, v in O.items():
            out[kk] = out.get(kk, 0) + v
    return {kk: sp.expand(v) for kk, v in out.items() if sp.expand(v) != 0}


def scal(a, A):
    return {kk: a * v for kk, v in A.items()}


def Vtilde(kidx, sig):
    """conjugated V_k at time sig: y_j -> y_j + 2 sig d_j"""
    Y1 = {(1, 0, 0, 0): 1, (0, 0, 1, 0): 2 * sig}
    Y2 = {(0, 1, 0, 0): 1, (0, 0, 0, 1): 2 * sig}
    D1 = {(0, 0, 1, 0): 1}
    D2 = {(0, 0, 0, 1): 1}
    E = add(mul(Y1, D1), mul(Y2, D2))
    Th = add(mul(Y1, D2), scal(-1, mul(Y2, D1)))
    Th2 = mul(Th, Th)
    R2 = add(mul(Y1, Y1), mul(Y2, Y2))
    P = {(0, 0, 0, 0): 1}
    for _ in range(kidx - 1):
        P = mul(P, R2)
    return scal(-1, add(scal(a_c[kidx - 1], mul(P, E)), scal(b_c[kidx - 1], mul(P, Th2))))


# ---------------- trace of normal-ordered monomials ----------------
z1, z2, y1, y2 = sp.symbols('z1 z2 y1 y2')
G = sp.exp(-(z1**2 + z2**2) / 4)


@lru_cache(None)
def hermite(b1, b2):
    return sp.expand(sp.simplify(sp.diff(G, z1, b1, z2, b2) / G))


# M = I - R^{-1}, R = [[c,-s],[s,c]], R^{-1} = [[c,s],[-s,c]]
Mz1 = (1 - c) * y1 - s * y2
Mz2 = s * y1 + (1 - c) * y2


def gauss_moment(p, q):
    """ int y1^p y2^q exp(-alpha |y|^2) dy / (4 pi), alpha = C^2/4 = 1/(4X)."""
    if p % 2 or q % 2:
        return 0
    n1, n2 = p // 2, q // 2
    val = sp.gamma(sp.Rational(2 * n1 + 1, 2)) * sp.gamma(sp.Rational(2 * n2 + 1, 2)) * (4 * X)**(n1 + n2 + 1)
    return sp.nsimplify(val / (4 * sp.pi))


@lru_cache(None)
def T(a1, a2, b1, b2):
    poly = sp.expand(y1**a1 * y2**a2 * hermite(b1, b2).subs({z1: Mz1, z2: Mz2}, simultaneous=True))
    P = sp.Poly(poly, y1, y2)
    tot = 0
    for (p, q), cf in P.terms():
        tot += cf * gauss_moment(p, q)
    return sp.expand(tot)


def to_X(expr):
    """reduce s^2 -> 1-c^2, check evenness in s, express via X = 1/C^2 with c = 1 - 1/(2X)."""
    e = sp.expand(expr)
    e = sp.Poly(e, s)
    out = 0
    for (deg,), cf in e.terms():
        if deg % 2:
            out += cf * s * (1 - c**2)**((deg - 1) // 2)
        else:
            out += cf * (1 - c**2)**(deg // 2)
    out = sp.expand(out)
    assert sp.expand(out.coeff(s, 1)) == 0, "odd in sin(phi)!"
    out = sp.expand(out.subs(c, 1 - 1 / (2 * X)))
    return out


def trace_op(O):
    tot = 0
    for kk, v in O.items():
        tot += v * T(*kk)
    return sp.expand(tot)


def simplex_integrate(expr, sigs):
    """int over 0<=s1<=...<=sn<=1 (iterated: innermost s1 from 0 to s2, ...)."""
    e = expr
    n = len(sigs)
    for i in range(n):
        upper = sigs[i + 1] if i + 1 < n else 1
        e = sp.integrate(sp.expand(e), (sigs[i], 0, upper))
    return sp.expand(e)


def compositions(l):
    """ordered tuples of positive ints summing to l"""
    if l == 0:
        yield ()
        return
    for first in range(1, l + 1):
        for rest in compositions(l - first):
            yield (first,) + rest


sig = sp.symbols('sigma1:12')
results = {}
for l in range(0, LMAX + 1):
    if l == 0:
        bl = to_X(T(0, 0, 0, 0))
    else:
        tot = 0
        for comp in compositions(l):
            n = len(comp)
            O = {(0, 0, 0, 0): 1}
            for i, kk in enumerate(comp):
                O = mul(O, Vtilde(kk, sig[i]))
            O = {kk: simplex_integrate(v, list(sig[:n])) for kk, v in O.items()}
            tot += (-1)**n * trace_op(O)
        bl = to_X(tot)
    results[l] = bl
    print('b_%d =' % l, sp.collect(bl, X), flush=True)

# express in K, Delta K, ...
Kv, D1v, D2v, D3v = sp.symbols('K DK D2K D3K')
print('invariants:', inv)
