"""Comparison phase: exact checks of specific sentences of theory/revision/descent.tex and of what
theory/revision/check_descent.py does or does not test.  Exits nonzero on any failure."""
from fractions import Fraction as Fr
import sympy as sp
from descent_lib import Weier, Out

o = Out()
a2, a4 = 393, 3456
E = Weier(a2, a4)

# 1. "the tangent at (16,400) has slope 21 and meets E again at (16,-400)"
x1, y1 = Fr(16), Fr(400)
m = (3 * x1 ** 2 + 2 * a2 * x1 + a4) / (2 * y1)
o.ok(m == 21, "tangent slope at (16,400) is 21")
x3 = m * m - a2 - 2 * x1
o.ok(x3 == 16, "third x on the tangent: m^2 - a2 - 2 x1 = 16")
y_line = y1 + m * (x3 - x1)
o.ok(y_line == 400, "the tangent line at x = 16 has y = 400: its third intersection is (16,400) itself (a flex)")
o.ok(y_line != -400, "(16,-400) is NOT on the tangent line at (16,400): 'meets E again at (16,-400)' is false")
X = sp.symbols('X')
cub = sp.expand(X ** 3 + a2 * X ** 2 + a4 * X - (400 + 21 * (X - 16)) ** 2)
o.ok(sp.factor(cub) == (X - 16) ** 3, f"E restricted to the tangent: {sp.factor(cub)} = (x-16)^3, triple contact")
o.ok(E.add((x1, y1), (x1, y1)) == (Fr(16), Fr(-400)), "2(16,400) = (16,-400) = -(16,400), so order 3 (conclusion right)")

# 2. check_descent.py tests the inverse in the form u=(X+Y)/Z = s(L-1)/(s-4L), (X-Y)/Z = eta/(s-4L),
#    s = x/4, eta = y/8, not the printed psi.  Show the two agree identically.
x, y = sp.symbols('x y')
L = sp.Rational(27, 2)
s_, eta = x / 4, y / 8
u_scr = s_ * (L - 1) / (s_ - 4 * L)
w_scr = eta / (s_ - 4 * L)
u_psi = (25 * x + y + 25 * x - y) / (4 * (x - 216))
w_psi = (25 * x + y - (25 * x - y)) / (4 * (x - 216))
o.ok(sp.simplify(u_scr - u_psi) == 0 and sp.simplify(w_scr - w_psi) == 0,
     "the script's inverse equals the printed psi identically (but the script never evaluates the printed psi in (b))")

# 3. the proof's congruences
for d1 in (2, -2, 3, -3):
    vals = {(d1 * M ** 4 + a2 * M * M * e * e + (a4 // d1) * e ** 4) % 5 for M in range(5) for e in range(5) if (M % 5, e % 5) != (0, 0)}
    o.ok(vals <= {2, 3}, f"E, d1={d1}: right side mod 5 in {sorted(vals)} (non-residues), as in descent.tex (i)")
for w in (1, 4, 7):
    o.ok((5 * w * w - w + 2) % 9 == 6, f"E', d1=15: 5w^2 - w + 2 = 6 mod 9 at w = {w}")
o.ok(262 % 9 == 1 and 3125 % 9 == 2 and 28125 // 9 == 3125 and 140625 // 15 == 9375 and 9375 // 3 == 3125,
     "the constants used in (ii) of descent.tex")
print(f"ALL {o.n} CHECKS PASSED")
