"""(f) 3P on C_{155/12} with base O = (1:-1:0) and P = (4:9:18).

Group law (stated in REVIEW.md): for A, B on the cubic, A*B = third intersection of the line AB
(tangent if A = B); A + B = O*(A*B); -A = A*(O*O).  (O = (1:-1:0) turns out to be a flex, so -A = A*O.)
Cross-check: transport to the Weierstrass model of Bremner-Guy-Nowakowski (context DI.2),
tau^2 = s(s^2 + (n^2-6n-3)s + 16n), s = -4e2/Z^2, tau = 4n(n-1)(X-Y)/(X+Y-(n-1)Z), n = lambda,
and compute 3P there with an independent Weierstrass group law.
Exact Fractions / sympy.  Exits nonzero on any failure.
"""
from fractions import Fraction as Fr
from itertools import product
import sympy as sp
from descent_lib import F_lam, normalize, PlaneCubicGroup, Weier, third_point, Out

o = Out()
lam = Fr(155, 12)
X, Y, Z = sp.symbols('X Y Z')
e1, e2, e3 = X + Y + Z, X*Y + Y*Z + Z*X, X*Y*Z
F = sp.expand(12*e1*e2 - 155*e3)
print("C_{155/12}: 12(X+Y+Z)(XY+YZ+ZX) - 155XYZ = 0")
G = sp.groebner([sp.diff(F, v) for v in (X, Y, Z)], X, Y, Z, order='grevlex')
for v in (X, Y, Z):
    o.ok(G.contains(v**6), f"{v}^6 in the ideal of partials: C_155/12 is nonsingular")

P = (4, 9, 18)
o.ok(F_lam(lam, P) == 0, "P = (4:9:18) lies on C_155/12  (S=31, e2=270, e3=648, 31*270 = 155*648/12)")
O = (1, -1, 0)
o.ok(F_lam(lam, O) == 0, "O = (1:-1:0) lies on C_155/12")
C = PlaneCubicGroup(lam, O)
OO = C.OO
print("O*O (tangent at O meets again) =", OO)
o.ok(OO == C.O, "O = (1:-1:0) IS a flex: the tangent -X-Y+(lam-1)Z=0 meets C in 3*O (lam s^3/(lam-1)^2 with s=X+Y)")
# so -A = A*(O*O) = A*O ; the general formula is kept in descent_lib and is valid either way
for B0 in [(0, 1, -1), (1, 0, -1)]:
    o.ok(normalize(third_point(lam, B0, B0)) == normalize(B0), f"{B0} is a flex too")
for B0 in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
    o.ok(normalize(third_point(lam, B0, B0)) != normalize(B0), f"{B0} is not a flex")

P2 = C.add(P, P)
P3 = C.add(P2, P)
P3b = C.add(P, P2)
print("2P =", P2)
print("3P =", P3)
o.ok(P2 == normalize((16352, 288, -365)), "2P = (16352 : 288 : -365)")
o.ok(P3 == P3b, "P + 2P = 2P + P")
right = normalize((162833463, 723926268, 287876366))
wrong = normalize((162833463, 287876366, 723926268))
o.ok(P3 == right, "3P = (162833463 : 723926268 : 287876366)  [corrected claim]")
o.ok(P3 != wrong, "3P != (162833463 : 287876366 : 723926268)  [old printing]")
o.ok(F_lam(lam, wrong) == 0, "the old printing is also a point of C_155/12 (Y<->Z symmetry)")
from math import gcd
o.ok(gcd(gcd(162833463, 723926268), 287876366) == 1, "coordinates of 3P are coprime: unique primitive integer representative up to sign")
o.ok(sorted(right) == sorted(wrong), "unordered: both printings are the same triad {162833463, 287876366, 723926268}")
S = sum(right)
Rv = sum(Fr(1, t) for t in right)
o.ok(S * Rv == lam, f"3P triad has S*R = 155/12 (S = {S})")

# relation between the two printings: sigma = swap(Y,Z); sigma(Q) = -Q + T, T = sigma(O) = (1:0:-1)
sig = lambda Q: normalize((Q[0], Q[2], Q[1]))
T = sig(O)
o.ok(T == (1, 0, -1), "sigma(O) = (1:0:-1)")
o.ok(C.add(P3, wrong) == T, "3P + (old printing) = (1:0:-1), i.e. old printing = -3P + (1:0:-1)")
o.ok(C.order(T) == 3, "(1:0:-1) has order 3 on C_155/12")
o.ok(C.add(C.neg(P3), T) == wrong, "old printing = -3P + (1:0:-1) = sigma(3P)")

# associativity, numerically on a set of rational points (exact)
pts = [normalize(Q) for Q in [P, P2, P3, wrong, (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, -1), (1, 0, -1), sig(P)]]
for Q in pts:
    o.ok(F_lam(lam, Q) == 0, f"{Q} on C_155/12") if False else None
    assert F_lam(lam, Q) == 0
cnt = 0
for A, B, D in product(pts[:7], repeat=3):
    l = C.add(C.add(A, B), D)
    r = C.add(A, C.add(B, D))
    assert l == r, (A, B, D)
    cnt += 1
o.ok(True, f"associativity (A+B)+D = A+(B+D) on {cnt} triples")
for A in pts:
    assert C.add(A, C.neg(A)) == C.O and C.add(A, C.O) == normalize(A)
o.ok(True, "A + (-A) = O and A + O = A on the sample")

# P has infinite order (no small torsion): positive point, multiples grow
o.ok(C.order(P, 12) == 0, "P has no order <= 12 (so P is of infinite order by Mazur's bound <= 12)")

# role of the base point: [3]P computed with other base points
print("[3]P with different base points:")
for B0 in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, -1, 0), (0, 1, -1), (1, 0, -1)]:
    Cb = PlaneCubicGroup(lam, B0)
    q = Cb.mul(3, P)
    tag = "corrected" if q == right else ("old printing" if q == wrong else "")
    print(f"   base {B0}: 3P = {q} {tag}")
    if B0 == (1, -1, 0):
        assert q == right

# independent cross-check through the BGN Weierstrass model (DI.2)
n = lam
A2 = n*n - 6*n - 3
A4 = 16*n
W = Weier(A2, A4)


def fwd(Q):
    Xv, Yv, Zv = (Fr(t) for t in Q)
    if normalize(Q) == normalize(O):
        return None
    s = -4*(Xv*Yv + Yv*Zv + Zv*Xv)/Zv**2
    tau = 4*n*(n - 1)*(Xv - Yv)/(Xv + Yv - (n - 1)*Zv)
    return (s, tau)


def bwd(Pt):
    if Pt is None:
        return normalize(O)
    s, tau = Pt
    u = s*(n - 1)/(s - 4*n)            # (x+y)/z
    w = tau*(u - n + 1)/(4*n*(n - 1))  # (x-y)/z
    return normalize(((u + w)/2, (u - w)/2, 1))


wP = fwd(P)
o.ok(W.on(wP), f"BGN image of P = {wP} lies on tau^2 = s(s^2 + {A2} s + {A4})")
o.ok(bwd(wP) == normalize(P), "BGN inverse maps it back to P")
w3 = W.mul(3, wP)
o.ok(bwd(w3) == right, "3P computed on the BGN Weierstrass model maps back to (162833463 : 723926268 : 287876366)")
w2 = W.mul(2, wP)
o.ok(bwd(w2) == P2, "2P agrees through the BGN model too")
print(f"ALL {o.n} CHECKS PASSED")
