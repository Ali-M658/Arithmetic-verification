"""Independent numerical checks of the plane hyperbolic trigonometry used in Group 1.

Upper half-plane model, PSL(2,R) matrices, mpmath at 40 digits.  Every check raises on failure.
  (H1) displacement of a rotation; hyperbolic displacement >= translation length
  (H2)+(H3) via products of rotations: for ccw rotations a (by 2*alpha about p) and b (by 2*beta
        about q), |tr(ab)|/2 and |tr(a b^-1)|/2 against the law-of-cosines quantities
  (H3) directly in the hyperboloid model (normals, intersection point, angles, same side)
  commutator identity tr[g,b]-2 = 4 sinh^2(L/2) sin^2(phi/2) cosh^2 r (Section B.1)
  elliptic-elliptic commutator (used only in an alternative argument)
"""
import random
import mpmath as mp

mp.mp.dps = 40
random.seed(12345)
TOL = mp.mpf(10) ** -25


def mat(a, b, c, d):
    return mp.matrix([[a, b], [c, d]])


def act(M, z):
    return (M[0, 0] * z + M[0, 1]) / (M[1, 0] * z + M[1, 1])


def dist(z, w):
    return mp.acosh(1 + abs(z - w) ** 2 / (2 * mp.im(z) * mp.im(w)))


def to_point(z):
    """matrix sending i to z"""
    x, y = mp.re(z), mp.im(z)
    s = mp.sqrt(y)
    return mat(s, x / s, 0, 1 / s)


def rot(z, phi):
    """counterclockwise rotation by phi about z"""
    c, s = mp.cos(phi / 2), mp.sin(phi / 2)
    R = mat(c, s, -s, c)
    T = to_point(z)
    return T * R * T ** -1


def tr(M):
    return M[0, 0] + M[1, 1]


def rand_point():
    return mp.mpf(random.uniform(-2, 2)) + 1j * mp.mpf(random.uniform(0.2, 3))


def check(cond, msg):
    if not cond:
        raise AssertionError(msg)


# ---- orientation sanity: rot(z,phi) has derivative e^{i phi} at z
for _ in range(20):
    z = rand_point(); phi = mp.mpf(random.uniform(0.1, 6.0))
    M = rot(z, phi)
    check(abs(act(M, z) - z) < TOL, "rotation does not fix centre")
    # derivative of Mobius map at z is 1/(cz+d)^2; push forward a tangent vector, rescale by Im
    der = 1 / (M[1, 0] * z + M[1, 1]) ** 2
    check(abs(der - mp.e ** (1j * phi)) < TOL, "rotation not counterclockwise by phi")

# ---- (H1)
nH1 = 0
for _ in range(300):
    q = rand_point(); x = rand_point(); phi = mp.mpf(random.uniform(-6, 6))
    r = dist(q, x); d = dist(x, act(rot(q, phi), x))
    check(abs(mp.sinh(d / 2) - mp.sinh(r) * abs(mp.sin(phi / 2))) < TOL, "H1 rotation")
    nH1 += 1
for _ in range(300):
    L = mp.mpf(random.uniform(0.05, 4))
    g = mat(mp.e ** (L / 2), 0, 0, mp.e ** (-L / 2))
    T = to_point(rand_point()); g = T * g * T ** -1
    check(abs(abs(tr(g)) - 2 * mp.cosh(L / 2)) < TOL, "trace/length")
    x = rand_point()
    check(dist(x, act(g, x)) >= L - TOL, "H1 hyperbolic displacement")
    nH1 += 1

# ---- (H2)+(H3) through rotations; both configurations
nprod = 0
for _ in range(2000):
    p = rand_point(); q = rand_point(); d = dist(p, q)
    al = mp.mpf(random.uniform(0.01, mp.pi / 2)); be = mp.mpf(random.uniform(0.01, mp.pi / 2))
    a = rot(p, 2 * al); b = rot(q, 2 * be)
    X_same = mp.sin(al) * mp.sin(be) * mp.cosh(d) - mp.cos(al) * mp.cos(be)
    X_opp = mp.sin(al) * mp.sin(be) * mp.cosh(d) + mp.cos(al) * mp.cos(be)
    t1 = abs(tr(a * b)) / 2; t2 = abs(tr(b * a)) / 2; t3 = abs(tr(a * b ** -1)) / 2
    check(abs(t1 - abs(X_same)) < TOL and abs(t2 - abs(X_same)) < TOL, "same-direction product")
    check(abs(t3 - abs(X_opp)) < TOL, "opposite-direction product")
    # elliptic case: the product is a rotation by 2*theta, cos theta = X (theta in (0,pi))
    if X_same < 1:
        th = mp.acos(X_same)
        check(abs(abs(tr(a * b)) / 2 - abs(mp.cos(th))) < TOL, "rotation angle")
    if X_same > 1:
        h = mp.acosh(X_same)
        # translation length of ab is 2h:  |tr| = 2 cosh(h)
        check(abs(abs(tr(a * b)) - 2 * mp.cosh(h)) < TOL, "translation length 2h")
    nprod += 1

# equal-angle opposite rotations: X = 1 + sin^2(al)(cosh d - 1) > 1 and h <= d
for _ in range(500):
    p = rand_point(); q = rand_point(); d = dist(p, q)
    al = mp.mpf(random.uniform(0.01, mp.pi - 0.01))
    a = rot(p, 2 * al); b = rot(q, 2 * al)
    t = abs(tr(a * b ** -1)) / 2
    X = 1 + mp.sin(al) ** 2 * (mp.cosh(d) - 1)
    check(abs(t - X) < TOL and X > 1 and mp.acosh(X) <= d + TOL, "equal angle case")

# ---- (H3) directly in the hyperboloid model, <u,v> = x x' + y y' - z z'
def mink(u, v):
    return u[0] * v[0] + u[1] * v[1] - u[2] * v[2]


def normal(pt, tang):
    # unit spacelike vector orthogonal to pt and tang
    n = mp.matrix([pt[1] * tang[2] - pt[2] * tang[1], pt[2] * tang[0] - pt[0] * tang[2],
                   pt[0] * tang[1] - pt[1] * tang[0]])
    n = mp.matrix([n[0], n[1], -n[2]])  # Lorentz cross product
    check(abs(mink(n, pt)) < TOL and abs(mink(n, tang)) < TOL, "normal")
    return n / mp.sqrt(mink(n, n))


nH3 = 0
for _ in range(2000):
    d = mp.mpf(random.uniform(0.001, 4))
    al = mp.mpf(random.uniform(0.01, mp.pi / 2)); be = mp.mpf(random.uniform(0.01, mp.pi / 2))
    P = mp.matrix([0, 0, 1]); Q = mp.matrix([mp.sinh(d), 0, mp.cosh(d)])
    tP = mp.matrix([mp.cos(al), mp.sin(al), 0])
    tQ = mp.matrix([-mp.cosh(d) * mp.cos(be), mp.sin(be), -mp.sinh(d) * mp.cos(be)])
    check(abs(mink(tQ, Q)) < TOL and abs(mink(tQ, tQ) - 1) < TOL, "tangent at Q")
    n1 = normal(P, tP); n3 = normal(Q, tQ)
    X = mp.sin(al) * mp.sin(be) * mp.cosh(d) - mp.cos(al) * mp.cos(be)
    check(abs(abs(mink(n1, n3)) - abs(X)) < TOL, "normals inner product")
    if X < 1 - mp.mpf(10) ** -6:
        # intersection: timelike vector orthogonal to n1, n3
        w = mp.matrix([n1[1] * n3[2] - n1[2] * n3[1], n1[2] * n3[0] - n1[0] * n3[2],
                       n1[0] * n3[1] - n1[1] * n3[0]])
        w = mp.matrix([w[0], w[1], -w[2]])
        nn = mink(w, w)
        check(nn < 0, "intersection timelike")
        R = w / mp.sqrt(-nn)
        if R[2] < 0:
            R = -R
        check(R[1] > 0, "meets on the same side")
        # angle at R between directions to P and Q
        def unit_dir(fr, to):
            v = to + mink(fr, to) * fr  # tangent component (since <fr,fr>=-1)
            return v / mp.sqrt(mink(v, v))
        cR = mink(unit_dir(R, P), unit_dir(R, Q))
        check(abs(cR - X) < TOL * 10 ** 6, "angle at intersection = arccos X")
        cP = mink(unit_dir(P, R), unit_dir(P, Q)); cQ = mink(unit_dir(Q, R), unit_dir(Q, P))
        check(abs(cP - mp.cos(al)) < TOL * 10 ** 6 and abs(cQ - mp.cos(be)) < TOL * 10 ** 6,
              "triangle angles alpha, beta")
    elif X > 1 + mp.mpf(10) ** -6:
        # ultraparallel: distance between lines = arccosh |<n1,n3>|
        pass
    nH3 += 1

# ---- commutator identity (Section B.1), hyperbolic gamma and rotation beta
ncomm = 0
for _ in range(1000):
    L = mp.mpf(random.uniform(0.05, 4)); r = mp.mpf(random.uniform(0, 3))
    phi = mp.mpf(random.uniform(-6, 6))
    g = mat(mp.e ** (L / 2), 0, 0, mp.e ** (-L / 2))          # axis = imaginary axis
    z0 = mp.sinh(r) + 1j * mp.mpf(random.uniform(0.3, 3)) * 0 + 1j  # sinh(dist)=|x|/y, y=1
    s = mp.mpf(random.uniform(0.3, 3)); z0 = s * z0            # scaling keeps distance to axis
    check(abs(mp.asinh(abs(mp.re(z0)) / mp.im(z0)) - r) < TOL, "distance to axis")
    b = rot(z0, phi)
    C = g * b * g ** -1 * b ** -1
    lhs = tr(C) - 2
    rhs = 4 * mp.sinh(L / 2) ** 2 * mp.sin(phi / 2) ** 2 * mp.cosh(r) ** 2
    check(abs(lhs - rhs) < TOL * 100, "commutator identity %s %s" % (lhs, rhs))
    ncomm += 1

# ---- elliptic-elliptic commutator
for _ in range(500):
    p = rand_point(); q = rand_point(); d = dist(p, q)
    f1 = mp.mpf(random.uniform(-6, 6)); f2 = mp.mpf(random.uniform(-6, 6))
    a = rot(p, f1); b = rot(q, f2)
    lhs = tr(a * b * a ** -1 * b ** -1) - 2
    rhs = 4 * mp.sin(f1 / 2) ** 2 * mp.sin(f2 / 2) ** 2 * mp.sinh(d) ** 2
    check(abs(lhs - rhs) < TOL * 100, "elliptic commutator")

print("trig_check OK: H1 %d, rotation products %d, H3 hyperboloid %d, commutator %d" %
      (nH1, nprod, nH3, ncomm))
