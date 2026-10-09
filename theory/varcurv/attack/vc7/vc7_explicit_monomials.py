"""VC7 attack, route B: same first-order Duhamel functional as route A, but evaluated for EXPLICIT
polynomial conformal factors psi (radial and non-radial, even and odd degree) by Gaussian moments
(Wick pairing with the covariance (2M)^{-1}), with lap_z K0 obtained by direct differentiation of the
flat heat kernel, and the s-integral done explicitly.  No generating function, no d/dlam trick.

L(psi)(t) = -2 int_0^t ds int dq dz K0(t-s,q,z) psi(z) lap_z K0(s,z,R q).

Prediction from VC7(a):  L(psi)(t) = sum_l t^l (2/(l-1)!) C^{-2l-2} (-lap^l psi(0)).
(For a homogeneous psi of degree n the only possible power is t^{n/2}.)
"""
import sys
import sympy as sp

t, s = sp.symbols('t s', positive=True)
q1, q2, z1, z2 = sp.symbols('q1 q2 z1 z2', real=True)
J = sp.symbols('J1:5')
W = [q1, q2, z1, z2]


def K0(tt, x, y):
    return sp.exp(-((x[0] - y[0])**2 + (x[1] - y[1])**2) / (4 * tt)) / (4 * sp.pi * tt)


def run(c, sn, psi, label):
    """c = cos phi, sn = sin phi exact; psi polynomial in z1,z2."""
    R = sp.Matrix([[c, -sn], [sn, c]])
    y = list(R * sp.Matrix([q1, q2]))
    # lap_z K0(s, z, y) / K0(s, z, y)
    k0s = K0(s, (z1, z2), y)
    lapfac = sp.simplify((sp.diff(k0s, z1, 2) + sp.diff(k0s, z2, 2)) / k0s)
    lapfac = sp.expand(lapfac)
    # total exponent: -|q-z|^2/(4(t-s)) - |z-Rq|^2/(4s) = -w^T M w
    expo = -((q1 - z1)**2 + (q2 - z2)**2) / (4 * (t - s)) - ((z1 - y[0])**2 + (z2 - y[1])**2) / (4 * s)
    expo = sp.expand(expo)
    M = sp.zeros(4)
    for i in range(4):
        for j in range(4):
            M[i, j] = -sp.Rational(1, 2) * sp.diff(expo, W[i], W[j])
    M = M.applyfunc(sp.simplify)
    detM = sp.factor(M.det())
    Sig = (2 * M).inv().applyfunc(sp.factor)           # covariance
    norm = sp.pi**2 / sp.sqrt(detM)                    # int exp(-w^T M w) dw
    Jv = sp.Matrix(J)
    quad = sp.expand((Jv.T * Sig * Jv)[0, 0] / 2)
    P = sp.Poly(sp.expand(psi * lapfac), *W)
    total = 0
    cache = {}
    for mon, coef in P.terms():
        d = sum(mon)
        if d % 2:
            continue
        k = d // 2
        if k not in cache:
            cache[k] = sp.expand(quad**k / sp.factorial(k))
        expr = cache[k]
        for i, e in enumerate(mon):
            if e:
                expr = sp.diff(expr, J[i], e)
        total += coef * expr
    total = sp.simplify(total)
    integrand = sp.simplify(norm * total / (4 * sp.pi * (t - s)) / (4 * sp.pi * s))
    L = sp.simplify(-2 * sp.integrate(integrand, (s, 0, t)))
    # prediction
    C2 = 2 - 2 * c
    lap = lambda f: sp.diff(f, z1, 2) + sp.diff(f, z2, 2)
    pred = 0
    f = psi
    for l in range(1, 8):
        f = lap(f)
        v = f.subs({z1: 0, z2: 0})
        pred += t**l * sp.Rational(2, sp.factorial(l - 1)) * C2**(-l - 1) * (-v)
    ok = sp.simplify(L - pred) == 0
    print(f"{label:55s} L = {sp.nsimplify(L)!s:35s} pred = {sp.simplify(pred)!s:30s} {'OK' if ok else 'MISMATCH'}")
    sys.stdout.flush()
    assert ok, (label, L, pred)
    return L


zc = z1 + sp.I * z2
r2 = z1**2 + z2**2
Re = lambda e: sp.expand(sp.re(sp.expand(e)))
Im = lambda e: sp.expand(sp.im(sp.expand(e)))

h = sp.sqrt(3) / 2
angles = {
    'pi (m=2)': (sp.Integer(-1), sp.Integer(0)),
    '2pi/3 (m=3)': (sp.Rational(-1, 2), h),
    'pi/2 (m=4)': (sp.Integer(0), sp.Integer(1)),
    'pi/3 (m=6)': (sp.Rational(1, 2), h),
    '4pi/3 (m=3,j=2)': (sp.Rational(-1, 2), -h),
}

print("== radial psi = r^(2l), all angles ==")
for name, (c, sn) in angles.items():
    for l in range(1, 5):
        run(c, sn, r2**l, f"phi={name}, psi=r^{2*l}")

print("== mixed radial jet psi = 3 r^2 - 5 r^4 + 7 r^6/2 at phi = 2pi/3 ==")
run(*angles['2pi/3 (m=3)'], 3 * r2 - 5 * r2**2 + sp.Rational(7, 2) * r2**3, "phi=2pi/3, mixed radial")

print("== non-radial, Phi-invariant psi (must give 0) ==")
tests = [
    ('pi (m=2)', Re(zc**2), 'Re z^2'),
    ('pi (m=2)', Im(zc**2) * r2, 'r^2 Im z^2'),
    ('pi (m=2)', Re(zc**4), 'Re z^4'),
    ('pi (m=2)', r2 * Re(zc**4), 'r^2 Re z^4'),
    ('pi (m=2)', r2**2 * Re(zc**2), 'r^4 Re z^2 (weight of l=3)'),
    ('pi (m=2)', r2**3 * Re(zc**2), 'r^6 Re z^2 (weight of l=4)'),
    ('2pi/3 (m=3)', Re(zc**3), 'Re z^3 (odd degree 3)'),
    ('2pi/3 (m=3)', r2 * Im(zc**3), 'r^2 Im z^3 (odd degree 5)'),
    ('2pi/3 (m=3)', Re(zc**6), 'Re z^6'),
    ('2pi/3 (m=3)', r2 * Re(zc**6), 'r^2 Re z^6 (weight of l=4)'),
    ('4pi/3 (m=3,j=2)', Re(zc**3) + r2 * Re(zc**3), 'Re z^3 + r^2 Re z^3'),
    ('pi/2 (m=4)', Re(zc**4) + Im(zc**4) * r2, 'Re z^4 + r^2 Im z^4'),
    ('pi/3 (m=6)', Re(zc**6), 'Re z^6'),
]
for name, psi, lab in tests:
    run(*angles[name], psi, f"phi={name}, psi={lab}")

print("== non-radial + radial combined (only radial part may survive) ==")
run(*angles['pi (m=2)'], r2**2 + 11 * Re(zc**4) - 3 * r2 * Re(zc**2), "phi=pi, r^4 + 11 Re z^4 - 3 r^2 Re z^2")

print("== generic symbolic angle, Re z^4 and r^4 ==")
cs, ss = sp.symbols('c sn', real=True)
# generic angle: substitute rational point on circle (c,sn) = ((1-u^2)/(1+u^2), 2u/(1+u^2)) with u symbolic
u = sp.symbols('u', positive=True)
cu, su = (1 - u**2) / (1 + u**2), 2 * u / (1 + u**2)
run(cu, su, r2**2, "generic phi (u-param), psi=r^4")
run(cu, su, Re(zc**4), "generic phi (u-param), psi=Re z^4 [not Phi-inv.]")
print("DONE")
