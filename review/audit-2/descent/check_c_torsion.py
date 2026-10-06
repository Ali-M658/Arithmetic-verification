"""(c) E(Q)_tors = Z/2 x Z/6 for E: y^2 = x^3 + 393x^2 + 3456x, with the twelve listed points.

Exact integer/Fraction arithmetic. Exits nonzero on any failure.
"""
from fractions import Fraction as Fr
from math import gcd, isqrt
from descent_lib import Weier, Out
import sympy as sp

o = Out()
a2, a4 = 393, 3456
E = Weier(a2, a4)
pts = {(0, 0): 2, (-9, 0): 2, (-384, 0): 2, (16, 400): 3, (16, -400): 3,
       (-24, 360): 6, (-24, -360): 6, (-144, 2160): 6, (-144, -2160): 6,
       (216, 5400): 6, (216, -5400): 6}
for P, n in pts.items():
    Pf = (Fr(P[0]), Fr(P[1]))
    o.ok(E.on(Pf), f"{P} on E")
    o.ok(E.order(Pf, 50) == n, f"order of {P} is {n} (computed {E.order(Pf, 50)})")
o.ok(len(pts) + 1 == 12, "11 affine points + O = 12 points")

# group structure: the 12 points form a group; 3 elements of order 2 -> Z/2 x Z/6 (not Z/12)
G = [None] + [(Fr(a), Fr(b)) for (a, b) in pts]
Gs = set(G)
for P in G:
    for Q in G:
        o.ok(E.add(P, Q) in Gs, f"closure: {P} + {Q}") if False else None
        assert E.add(P, Q) in Gs
o.ok(True, "the 12 points are closed under addition (144 sums checked)")
n2 = sum(1 for P in G if P is not None and E.order(P) == 2)
o.ok(n2 == 3, "exactly 3 elements of order 2, so the group of order 12 is Z/2 x Z/6, not Z/12")
o.ok(E.add((Fr(-24), Fr(360)), (Fr(0), Fr(0))) in Gs, "sanity")
# the order-6 point (216,5400) generates a cyclic subgroup; together with (-9,0) (not in it) it generates G
P6 = (Fr(216), Fr(5400))
cyc = {E.mul(k, P6) for k in range(6)}
o.ok(len(cyc) == 6, "<(216,5400)> has order 6")
o.ok((Fr(-9), Fr(0)) not in cyc, "(-9,0) not in <(216,5400)>, so G = <(216,5400)> x <(-9,0)> = Z/6 x Z/2")

# bad primes from the discriminant (Cremona 3.1 formulas)
b2, b4, b6, b8 = 4 * a2, 2 * a4, 0, -a4 * a4
Delta = -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6
fac = sp.factorint(Delta)
o.ok(set(fac) == {2, 3, 5}, f"Delta = {Delta} = {fac}: bad primes of this model are 2, 3, 5")
c4 = b2 * b2 - 24 * b4
print("c4 =", c4, sp.factorint(c4))
# minimality at 2,3,5 not needed: the injectivity statement is about p not dividing 2*Delta

counts = {}
for p in (7, 11, 13, 17, 19, 23):
    Ep = Weier(a2, a4, p=p)
    counts[p] = Ep.count_Fp()
    print(f"#E(F_{p}) = {counts[p]}")
o.ok(counts[7] == 12 and counts[11] == 12, "#E(F_7) = #E(F_11) = 12")
g = 0
for p, n in counts.items():
    g = gcd(g, n)
o.ok(g == 12, f"gcd of #E(F_p), p = 7..23, is {g}")

# reduction mod 7 and mod 11 is injective on the 12 points (consistency with the theorem)
for p in (7, 11):
    red = {None if P is None else (int(P[0]) % p, int(P[1]) % p) for P in G}
    o.ok(len(red) == 12, f"the 12 points stay distinct mod {p}")

# independent: Lutz-Nagell (Cremona Prop 3.3.1, 3.3.2): torsion points are integral and y = 0 or y^2 | Delta0
Delta0 = 27 * 0 + 4 * a2 ** 3 * 0 + 4 * a4 ** 3 - a2 ** 2 * a4 ** 2 - 18 * a2 * a4 * 0
o.ok(Delta == -16 * Delta0, "Delta = -16 Delta0 (Cremona p. 70)")
cand = []
divs = sp.divisors(abs(Delta0))
for yv in [0] + [dd for dd in divs if abs(Delta0) % (dd * dd) == 0]:
    for s in ((1, -1) if yv else (1,)):
        y = s * yv
        # integer roots of x^3 + a2 x^2 + a4 x - y^2
        xs = sp.Poly(sp.Symbol('x') ** 3 + a2 * sp.Symbol('x') ** 2 + a4 * sp.Symbol('x') - y * y).ground_roots()
        for r in xs:
            if r.is_integer:
                cand.append((int(r), y))
tors_found = []
for (x, y) in cand:
    P = (Fr(x), Fr(y))
    n = E.order(P, 12)  # by Mazur no order > 12 ; here we just test orders <= 12
    if n:
        tors_found.append((x, y))
print("Lutz-Nagell candidates:", sorted(cand))
o.ok(set(tors_found) == set(pts), f"Lutz-Nagell: the integral candidates of finite order are exactly the 11 listed affine points")
nonT = [c for c in cand if c not in pts]
for (x, y) in nonT:
    # non-torsion candidates: show a multiple is non-integral (then not torsion, Prop 3.3.1)
    Q = (Fr(x), Fr(y))
    k = 1
    while Q is not None and Q[0].denominator == 1:
        Q = E.add(Q, (Fr(x), Fr(y)))
        k += 1
        assert k < 20
    o.ok(Q is not None, f"candidate {(x, y)}: {k}P is non-integral, so infinite order")
print(f"ALL {o.n} CHECKS PASSED")
