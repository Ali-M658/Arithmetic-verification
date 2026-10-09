"""VC7 attack, route A: first-order (in eps) perturbation of the flat rotation,
with conformal metric g = e^{2 eps psi}|dx|^2 and a GENERATING-FUNCTION potential
psi(z) = exp(a.z), a = (a1, a2) arbitrary (complex) vector.

Setting.  Delta_g = -e^{-2 eps psi} lap  =  Delta_0 + eps V + O(eps^2),  V = 2 psi lap,
Delta_0 = -lap.  Duhamel:  K_1(t,x,y) = -int_0^t ds int dz K0(t-s,x,z) 2 psi(z) lap_z K0(s,z,y)
(kernel w.r.t. Lebesgue measure).  For Phi-invariant psi, H(x,y) = K(x,y) e^{-2 eps psi(y)} is the kernel
w.r.t. dvol_g and int H(t,q,Phi q) dvol(q) = int K(t,q,Phi q) dq exactly (the e^{+-2 eps psi} cancel).
So  d/deps|_0 sum_l b_l t^l  =  L(psi)(t) := int dq K_1(t,q,Phi q).

For psi = exp(a.z) every term is a 4-dim Gaussian integral in w = (q,z):
   G(lam,mu) = int exp(-mu|q-z|^2 - lam|z-Phi q|^2 + a.z) dq dz = pi^2/sqrt(det M) exp(J^T M^{-1} J/4),
and  int e^{...} |z-Phi q|^2 = -dG/dlam.  With mu = 1/(4(t-s)), lam = 1/(4s):
   lap_z K0(s,z,y) = K0(s,z,y) (|z-y|^2/(4 s^2) - 1/s).
cos(phi), sin(phi) are kept as symbols c, sn with c^2 + sn^2 = 1; at the end c = 1 - C^2/2.

Linear-in-jet: K = e^{-2 psi}(-lap psi) => K_lin = -lap psi; (-Delta_g)^{l-1} K |_lin = lap^{l-1}(-lap psi)(0)
 = -lap^l psi(0).  For psi = exp(a.z), the degree-2l part is (a.z)^{2l}/(2l)!, whose lap^l is (a.a)^l.
VC7(a) predicts  L(t) = sum_{l>=1} (2/(l-1)!) C^{-2l-2} (-(a.a)^l) t^l = -(2/C^2) x e^x,  x = (a.a) t / C^2,
and (by polarisation, since <a,z>^n spans degree-n polynomials) the dependence on a only through a.a
means NON-RADIAL parts of psi never enter, and odd degrees (half-integer powers t^{n/2}) vanish.
"""
import sympy as sp

t, s, C = sp.symbols('t s C', positive=True)
c, sn = sp.symbols('c sn', real=True)
a1, a2 = sp.symbols('a1 a2')
lam, mu = sp.symbols('lam mu', positive=True)

# Phi q = R q, R = [[c,-sn],[sn,c]]
R = sp.Matrix([[c, -sn], [sn, c]])
I2 = sp.eye(2)
Z2 = sp.zeros(2)
# quadratic form Q(w) = mu|q-z|^2 + lam|z-Rq|^2 = w^T M w, w=(q1,q2,z1,z2)
# |q-z|^2: [[I,-I],[-I,I]];  |z-Rq|^2 = |Rq|^2 - 2 z.Rq + |z|^2: [[R^T R, -R^T],[-R, I]]
def blk(A, B, Cc, D):
    return sp.Matrix(sp.BlockMatrix([[A, B], [Cc, D]]))
RtR = sp.simplify((R.T * R).subs(sn**2, 1 - c**2))
M = mu * blk(I2, -I2, -I2, I2) + lam * blk(RtR, -R.T, -R, I2)
M = M.applyfunc(lambda e: sp.expand(e).subs(sn**2, 1 - c**2))
J = sp.Matrix([0, 0, a1, a2])

def red(e):
    """reduce polynomial/rational expression using sn^2 = 1 - c^2"""
    e = sp.together(sp.expand(e))
    n, d = sp.fraction(e)
    n = sp.expand(n).subs(sn**2, 1 - c**2)
    n = sp.expand(sp.expand(n).subs(sn**2, 1 - c**2))
    d = sp.expand(sp.expand(d).subs(sn**2, 1 - c**2))
    return sp.factor(n) / sp.factor(d)

detM = red(M.det())
Minv = M.inv()
expo = red((J.T * Minv * J)[0, 0] / 4)
print("det M =", detM)
print("exponent J^T M^-1 J/4 =", expo)
aa = a1**2 + a2**2
# rotation invariance: exponent must be (a.a) * f
f = red(expo / aa)
assert sp.simplify(sp.diff(f, a1)) == 0 and sp.simplify(sp.diff(f, a2)) == 0, "exponent not a function of a.a"
print("exponent / (a.a) =", f)

# G = pi^2 / sqrt(detM) * exp(expo).  Note detM should be a perfect square (positive).
sq = sp.sqrt(sp.factor(detM))
G = sp.pi**2 / sq * sp.exp(expo)
Glam = -sp.diff(G, lam)                     # int e^{...} |z - R q|^2
# integrand prefactors: K0(t-s) K0(s) = 1/(4pi(t-s)) 1/(4pi s)
pref = 1 / (4 * sp.pi * (t - s)) / (4 * sp.pi * s)
inner = pref * (Glam / (4 * s**2) - G / s)   # int dq dz K0 K0 e^{a.z} (|z-y|^2/(4s^2) - 1/s)
inner = inner.subs({mu: 1 / (4 * (t - s)), lam: 1 / (4 * s)})
inner = sp.simplify(inner)
print("s-integrand / (-2) =", inner)

# series in X = a.a: replace a.a -> X by working with f
X = sp.symbols('X')
expo_s = sp.simplify(f.subs({mu: 1 / (4 * (t - s)), lam: 1 / (4 * s)}))
print("exponent/(a.a) at mu,lam =", sp.factor(expo_s))

# ---- assertions -------------------------------------------------------------
assert sp.simplify(detM - 4 * lam**2 * mu**2 * (1 - c)**2) == 0
# exponent at (mu,lam) is exactly (a.a) t / C^2 with C^2 = 2 - 2c, independent of s
assert sp.simplify(expo_s - t / (2 - 2 * c)) == 0
cC = 1 - C**2 / 2                         # cos phi in terms of C, phi in (0, 2pi) => 0 < C <= 2
integrand = sp.simplify(inner.subs(c, cC))
print("s-integrand (C form) =", integrand)
assert sp.simplify(sp.diff(integrand, s)) == 0, "s-integrand depends on s"
Lt = sp.simplify(-2 * sp.integrate(integrand, (s, 0, t)))
print("L(t) =", Lt)
xx = aa * t / C**2
assert sp.simplify(Lt - (-(2 / C**2) * xx * sp.exp(xx))) == 0
print("CHECK closed form L(t) = -(2/C^2) x e^x, x=(a.a)t/C^2 : OK")

# Taylor coefficients: coefficient of t^l, compared with VC7(a) applied to psi=exp(a.z)
ser = sp.series(Lt, t, 0, 9).removeO()
for l in range(0, 9):
    coef = sp.simplify(ser.coeff(t, l))
    if l == 0:
        pred = 0
    else:
        lin_jet = -(aa)**l                   # (-Delta_g)^{l-1} K (0) at linear order
        pred = sp.Rational(2, sp.factorial(l - 1)) * C**(-2 * l - 2) * lin_jet
    assert sp.simplify(coef - pred) == 0, (l, coef, pred)
    print(f"l={l}: [t^l] L = {sp.factor(coef)}   == VC7(a) prediction: OK")
print("Odd degrees of psi (half-integer powers t^(n/2)): the generating function depends on a only")
print("through a.a, so all odd-degree Taylor coefficients in a vanish identically: OK")
print("Non-radial parts: dependence only through a.a  => by polarisation L(P) = c_n lap^{n/2} P(0) for every")
print("homogeneous P of degree n, so only Delta_0^l psi(0) enters: OK")
print("phi = pi (m=2, C^2=4) is not special: the formula is a single analytic expression on 0<C<=2.")
print("DONE")
