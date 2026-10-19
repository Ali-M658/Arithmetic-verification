#!/usr/bin/env python3
"""
The dual family is a quartic del Pezzo surface (the note, Section 4; round 7).

    .venv/bin/python theory/diophantine/dual_delpezzo.py          (seconds; sympy)

The dual pair of x = (a : b : c) (Corollary 1 of the note) is the point
    D(x) = (e2 a, e2 b, e2 c, e1 bc, e1 ca, e1 ab)
of the hyperplane {y1 + y2 + y3 = y4 + y5 + y6} of P^5. Asserted:
  1. the six cubics vanish at the five points (1:0:0), (0:1:0), (0:0:1), (1:w:w^2), (1:w^2:w), w^3 = 1 != w;
  2. they span a space of dimension 5, which is the whole space of plane cubics through these five points
     (10 - 5 conditions, independent since no three of the points are collinear, also asserted);
so x -> D(x) is the anticanonical map of the blow-up X of P^2 in the five points, a del Pezzo surface of degree
9 - 5 = 4 in P^4. Over Q three of the points are rational and two conjugate, so Pic X_Q has rank 1 + 3 + 1 = 5;
the lines through (1:0:0) give the conics H - E_1 ((H - E_1).(-K) = 3 - 1 = 2) with the rational section E_1.
  3. for positive x the entries of D(x) are positive, and the common sum y1 + y2 + y3 lies between the largest
     entry and three times it; the six entries and five of them (the sixth being a Z-linear combination) have the
     same greatest common divisor, so S_D is, up to the factor 3, the anticanonical height of D(x) (checked on
     random positive triples).
Writes nothing; prints a summary.
"""
import random
from fractions import Fraction
from math import gcd

import sympy as sp

a, b, c = sp.symbols("a b c")
e1, e2 = a + b + c, a * b + b * c + c * a
F = [e2 * a, e2 * b, e2 * c, e1 * b * c, e1 * c * a, e1 * a * b]
assert sp.expand(sum(F[:3]) - sum(F[3:])) == 0

w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
pts = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, w, w ** 2), (1, w ** 2, w)]
for p in pts:
    for f in F:
        assert sp.simplify(f.subs({a: p[0], b: p[1], c: p[2]})) == 0, (f, p)
for i in range(5):
    for j in range(i):
        for k in range(j):
            M = sp.Matrix([pts[i], pts[j], pts[k]])
            assert sp.simplify(M.det()) != 0, (pts[i], pts[j], pts[k])

# the sixteen lines of the blow-up: the five exceptional curves, the ten lines through two of the points (the
# coordinate lines, x + y + z = 0 through the two non-real points, and six non-real lines through a vertex and a
# non-real point, whose only real point is the vertex), and the conic e2 = 0 through all five; none meets the open
# positive triangle, since there e1, e2 > 0 and every coordinate is nonzero
for p in pts:
    assert sp.simplify(e2.subs({a: p[0], b: p[1], c: p[2]})) == 0
for p in pts[3:]:
    assert sp.simplify(e1.subs({a: p[0], b: p[1], c: p[2]})) == 0
mons = [a ** i * b ** j * c ** (3 - i - j) for i in range(4) for j in range(4 - i)]
coef = sp.Matrix([[sp.Poly(f, a, b, c).coeff_monomial(m) for m in mons] for f in F])
assert coef.rank() == 5
cond = sp.Matrix([[m.subs({a: p[0], b: p[1], c: p[2]}) for m in mons] for p in pts])
assert sp.simplify(cond).rank() == 5                       # 5 independent conditions: the space has dimension 5

rng = random.Random(1)
for _ in range(2000):
    x = [rng.randint(1, 200) for _ in range(3)]
    s1, s2 = sum(x), x[0] * x[1] + x[1] * x[2] + x[2] * x[0]
    y = [s2 * x[0], s2 * x[1], s2 * x[2], s1 * x[1] * x[2], s1 * x[2] * x[0], s1 * x[0] * x[1]]
    g = gcd(*y)
    assert g == gcd(*y[:5])
    y = [v // g for v in y]
    S = sum(y[:3])
    assert all(v > 0 for v in y) and max(y) <= S <= 3 * max(y)
print("dual family: six cubics through the five points, rank 5 (the anticanonical system); quartic del Pezzo "
      "surface, Picard rank 5 over Q; S_D within a factor 3 of the anticanonical height: all checks passed")
