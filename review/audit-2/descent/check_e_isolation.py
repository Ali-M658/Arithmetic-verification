"""(e) The isolation statement DE.5: the side claims.

1. For every smooth C_lambda, O=(1:-1:0), (0:1:-1), (1:0:-1) are flexes on the line X+Y+Z=0, so
   (1:0:-1) has order 3 (symbolic check in lambda).
2. sigma = (Y<->Z) satisfies Q + sigma(Q) = (1:0:-1) (checked exactly on many points of many curves),
   so every isosceles point (u:v:v) has 2Q = (1:0:-1) and order 3 or 6.
3. The 1,482 isosceles triples (u,v,v), u != v <= 39, all have order 3 or 6 (exact).
Exits nonzero on any failure.
"""
from fractions import Fraction as Fr
import sympy as sp
from descent_lib import F_lam, normalize, PlaneCubicGroup, Out

o = Out()
X, Y, Z, L, s, t = sp.symbols('X Y Z L s t')
F = (X + Y + Z) * (X * Y + Y * Z + Z * X) - L * X * Y * Z

# 1. flexes: restrict F to the tangent line at each of the three points, symbolically in L
for Pt in [(1, -1, 0), (0, 1, -1), (1, 0, -1)]:
    sub = dict(zip((X, Y, Z), Pt))
    grad = [sp.diff(F, v).subs(sub) for v in (X, Y, Z)]
    o.ok(sp.expand(F.subs(sub)) == 0, f"{Pt} on every C_L")
    # direction D on the tangent line, not proportional to Pt
    D = sp.Matrix(grad).cross(sp.Matrix(Pt))
    line = {X: Pt[0] + t * D[0], Y: Pt[1] + t * D[1], Z: Pt[2] + t * D[2]}
    poly = sp.Poly(sp.expand(F.subs(line, simultaneous=True)), t)
    c = poly.all_coeffs()[::-1] + [0] * 4
    o.ok(sp.simplify(c[0]) == 0 and sp.simplify(c[1]) == 0 and sp.simplify(c[2]) == 0,
         f"{Pt}: tangent line meets C_L with multiplicity 3 (flex) for every L; F|line = {sp.factor(poly.as_expr())}")
line_e1 = sp.factor(F.subs(Z, -X - Y))
o.ok(sp.expand(line_e1 - L * X * Y * (X + Y)) == 0, "on X+Y+Z=0, F = L XY(X+Y): the three flexes are collinear")

# 2. sigma(Q) + Q = T on many points of many curves (points obtained as multiples of a positive point)
T = (1, 0, -1)
sig = lambda Q: normalize((Q[0], Q[2], Q[1]))
tested = 0
for (a, b, c_) in [(4, 9, 18), (15, 55, 66), (16, 40, 80), (2, 3, 7), (3, 5, 11), (1, 2, 6), (5, 7, 13)]:
    lam = Fr((a + b + c_) * (a * b + b * c_ + c_ * a), a * b * c_)
    C = PlaneCubicGroup(lam, (1, -1, 0))
    Q = normalize((a, b, c_))
    R = Q
    for k in range(1, 5):
        assert C.add(R, sig(R)) == T, (lam, R)
        tested += 1
        R = C.add(R, Q)
    o.ok(C.order(T) == 3, f"lambda={lam}: (1:0:-1) has order 3")
o.ok(tested == 28, f"Q + sigma(Q) = (1:0:-1) on {tested} points of 7 curves")

# 3. the isosceles census
cnt = 0
orders = {}
for u in range(1, 40):
    for v in range(1, 40):
        if u == v:
            continue
        lam = Fr((u + 2 * v) * (v * v + 2 * u * v), u * v * v)
        assert lam != 9 and lam > 9
        C = PlaneCubicGroup(lam, (1, -1, 0))
        Q = (u, v, v)
        assert F_lam(lam, Q) == 0
        n = C.order(Q, 12)
        assert C.add(Q, Q) == T
        orders[n] = orders.get(n, 0) + 1
        cnt += 1
o.ok(cnt == 1482, "1,482 isosceles triples (u,v,v), u != v <= 39")
o.ok(set(orders) <= {3, 6} and 0 not in orders, f"all are torsion: order counts {orders}; 2Q = (1:0:-1) for every one")
print(f"ALL {o.n} CHECKS PASSED")
