"""(a) phi, psi between C_{27/2} and E: y^2 = x(x+9)(x+384); nonsingularity; Q-isomorphism (no twist).

Exact sympy / Fraction arithmetic.  Exits nonzero on any failure.
"""
import sys
from fractions import Fraction as Fr
import sympy as sp
from descent_lib import F_lam, normalize, Weier, Out

o = Out()
X, Y, Z, x, y, t = sp.symbols('X Y Z x y t')
lam = sp.Rational(27, 2)

# --- equation of C_{27/2} from the definition in DI.1:  (X+Y+Z)(XY+YZ+ZX) = lam XYZ
e1 = X + Y + Z
e2 = X*Y + Y*Z + Z*X
e3 = X*Y*Z
F = sp.expand(2*(e1*e2 - lam*e3))          # integral model, 2 * defining form
print("C_{27/2}: 2(X+Y+Z)(XY+YZ+ZX) - 27XYZ =", sp.factor(F))
o.ok(sp.expand(F - (2*e1*e2 - 27*e3)) == 0, "C_{27/2}: 2 e1 e2 - 27 e3 = 0")

# --- nonsingularity: no common projective zero of F_X, F_Y, F_Z (and F)
G = sp.groebner([sp.diff(F, v) for v in (X, Y, Z)], X, Y, Z, order='grevlex')
# ideal of partials must be (X,Y,Z)-primary: check X^N, Y^N, Z^N in ideal for some N
N = 6
for v in (X, Y, Z):
    o.ok(G.contains(v**N), f"{v}^{N} lies in the ideal of the partials (no singular point over Qbar)")

# also by the discriminant of the Weierstrass model
E_eq = y**2 - (x**3 + 393*x**2 + 3456*x)
o.ok(sp.expand(x*(x+9)*(x+384) - (x**3 + 393*x**2 + 3456*x)) == 0, "x(x+9)(x+384) = x^3+393x^2+3456x")
c, d = 393, 3456
disc_cubic = d**2 * (c**2 - 4*d)
o.ok(disc_cubic != 0, f"disc of x(x^2+cx+d) = d^2(c^2-4d) = {disc_cubic} != 0, E nonsingular")
# Cremona 3.1 b-invariants for [0,393,0,3456,0]
a1, a2, a3, a4, a6 = 0, 393, 0, 3456, 0
b2 = a1*a1 + 4*a2; b4 = a1*a3 + 2*a4; b6 = a3*a3 + 4*a6
b8 = a1*a1*a6 - a1*a3*a4 + 4*a2*a6 + a2*a3*a3 - a4*a4
Delta = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
c4 = b2*b2 - 24*b4
o.ok(Delta == 16*disc_cubic, f"Delta(E) = {Delta} = 16 d^2 (c^2-4d) = {sp.factorint(Delta)}")

# --- the maps
phi_x = -16*e2/Z**2
phi_y = 8*(X - Y)/Z*(-4*e2/Z**2 - 54)
psi = (25*x + y, 25*x - y, 4*(x - 216))

# phi maps C into E: numerator of y^2 - x(x+9)(x+384) at phi is divisible by F
num = sp.together(phi_y**2 - phi_x*(phi_x + 9)*(phi_x + 384))
n_, d_ = sp.fraction(num)
q, r = sp.div(sp.Poly(sp.expand(n_), X, Y, Z), sp.Poly(F, X, Y, Z))
o.ok(r.is_zero, "phi(C) in E: numerator of y^2 - x(x+9)(x+384) at phi is a multiple of F")

# psi maps E into C: F(psi) is a multiple of E_eq
Fpsi = sp.expand(F.subs({X: psi[0], Y: psi[1], Z: psi[2]}, simultaneous=True))
# reduce modulo y^2 = cubic (division in y)
Fpsi_red = sp.expand(sp.rem(sp.Poly(Fpsi, y), sp.Poly(E_eq, y)).as_expr())
o.ok(sp.simplify(Fpsi_red) == 0, "psi(E) in C: F(psi(x,y)) = 0 modulo y^2 = x(x+9)(x+384)")
print("   F(psi) factorised:", sp.factor(Fpsi))
o.ok(sp.expand(Fpsi + 21600*E_eq) == 0, "F(psi(x,y)) = -21600 (y^2 - x(x+9)(x+384)) identically")

# phi is a group homomorphism for the chord-tangent law on C with base O (sample check)
from descent_lib import PlaneCubicGroup
Cg = PlaneCubicGroup(Fr(27, 2), (1, -1, 0))
Ew = Weier(393, 3456)
def psi_pt(p):
    return (1, -1, 0) if p is None else normalize((25*p[0] + p[1], 25*p[0] - p[1], 4*(p[0] - 216)))
tors = [None, (Fr(0), Fr(0)), (Fr(-9), Fr(0)), (Fr(-24), Fr(360)), (Fr(16), Fr(400)), (Fr(216), Fr(5400))]
for p1 in tors:
    for p2 in tors:
        o.ok(psi_pt(Ew.add(p1, p2)) == Cg.add(psi_pt(p1), psi_pt(p2)),
             f"psi(P+Q) = psi(P) + psi(Q) for P={p1}, Q={p2}")

# phi o psi = id on E
sub = {X: psi[0], Y: psi[1], Z: psi[2]}
px = sp.together(phi_x.subs(sub, simultaneous=True))
py = sp.together(phi_y.subs(sub, simultaneous=True))
def reduce_E(expr):
    nn, dd = sp.fraction(sp.together(expr))
    nn = sp.rem(sp.Poly(sp.expand(nn), y), sp.Poly(E_eq, y)).as_expr()
    dd = sp.rem(sp.Poly(sp.expand(dd), y), sp.Poly(E_eq, y)).as_expr()
    return nn, dd
nn, dd = reduce_E(px - x)
o.ok(sp.expand(nn) == 0 or sp.rem(sp.Poly(sp.expand(nn), y), sp.Poly(E_eq, y)).is_zero,
     "phi(psi(x,y)).x = x on E")
nn, dd = reduce_E(py - y)
o.ok(sp.expand(nn) == 0, "phi(psi(x,y)).y = y on E")

# psi o phi = id on C (projectively): cross products of psi(phi(P)) with P vanish mod F
ppsi = [sp.together(c_.subs({x: phi_x, y: phi_y}, simultaneous=True)) for c_ in psi]
P = (X, Y, Z)
for (i, j) in ((0, 1), (0, 2), (1, 2)):
    cr = sp.together(ppsi[i]*P[j] - ppsi[j]*P[i])
    nn, dd = sp.fraction(cr)
    rr = sp.div(sp.Poly(sp.expand(nn), X, Y, Z), sp.Poly(F, X, Y, Z))[1]
    o.ok(rr.is_zero, f"psi(phi(P)) ~ P on C: cross product ({i},{j}) is a multiple of F")

# psi(origin): homogenise with x = u/w^2, y = v/w^3 ; at w = 0 the point is (0:1:0) of E
u, v, w = sp.symbols('u v w')
psi_h = [sp.expand(c_.subs({x: u/w**2, y: v/w**3}, simultaneous=True)*w**3) for c_ in psi]
at_inf = [sp.expand(c_.subs(w, 0)) for c_ in psi_h]
print("   psi at the origin (u:v:0)=(0:1:0):", [c_.subs({u: 0, v: 1}) for c_ in at_inf])
o.ok([c_.subs({u: 0, v: 1}) for c_ in at_inf] == [1, -1, 0], "psi(origin of E) = (1:-1:0) = O")

# --- the twelve points of E, their images under psi, and phi back
E = Weier(393, 3456)
pts = [None, (0, 0), (-9, 0), (-384, 0), (-24, 360), (-24, -360), (-144, 2160), (-144, -2160),
       (16, 400), (16, -400), (216, 5400), (216, -5400)]
pts = [None if p is None else (Fr(p[0]), Fr(p[1])) for p in pts]
imgs = []
for p in pts:
    o.ok(E.on(p), f"{p} on E")
    if p is None:
        im = (1, -1, 0)
    else:
        im = normalize((25*p[0] + p[1], 25*p[0] - p[1], 4*(p[0] - 216)))
    o.ok(F_lam(Fr(27, 2), tuple(Fr(s) for s in im)) == 0, f"psi{p} = {im} on C_27/2")
    imgs.append(im)
    # phi back, when Z != 0
    if im[2] != 0:
        Xv, Yv, Zv = (Fr(s) for s in im)
        E2 = Xv*Yv + Yv*Zv + Zv*Xv
        bx = -16*E2/Zv**2
        by = 8*(Xv - Yv)/Zv*(-4*E2/Zv**2 - 54)
        o.ok((bx, by) == p, f"phi{im} = {p}")
o.ok(len(set(imgs)) == 12, "the 12 images are distinct")
print("images:", imgs)

# --- no twist: #C(F_p) = #E(F_p) for several good p (a nontrivial quadratic twist
#     would give p+1+a instead of p+1-a, differing whenever a != 0)
def count_C(p):
    Fp = lambda P: (2*(P[0]+P[1]+P[2])*(P[0]*P[1]+P[1]*P[2]+P[2]*P[0]) - 27*P[0]*P[1]*P[2]) % p
    n = 0
    # projective points: (1:a:b), (0:1:b), (0:0:1)
    for a_ in range(p):
        for b_ in range(p):
            if Fp((1, a_, b_)) == 0:
                n += 1
    for b_ in range(p):
        if Fp((0, 1, b_)) == 0:
            n += 1
    if Fp((0, 0, 1)) == 0:
        n += 1
    return n
for p in (7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
    nE = Weier(393, 3456, p=p).count_Fp()
    nC = count_C(p)
    o.ok(nE == nC, f"p={p}: #C(F_p) = {nC} = #E(F_p) = {nE} (a_p = {p+1-nE})")

print(f"ALL {o.n} CHECKS PASSED")
