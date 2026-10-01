#!/usr/bin/env python3
"""
Exact checks behind variety.md.

  1. Scale invariance: a set of triples is a degeneracy class (equal S, equal R)
     after rescaling iff the triples share lambda = e1 e2 / e3; lambda = S R.
  2. The pencil e1 e2 = lambda e3 is Beauville's Gamma_1(6) pencil
     (X+Y)(Y+Z)(Z+X) + t XYZ = 0 with t = 1 - lambda (polynomial identity).
  3. A Weierstrass model over Q(lambda), derived here, its discriminant and
     c4, the Kodaira types I6 (inf), I3 (1), I2 (0), I1 (9), and agreement of
     its j-invariant with the Bremner-Guy-Nowakowski model
         tau^2 = sigma (sigma^2 + (n^2 - 6n - 3) sigma + 16 n).
  4. The six base points have orders 1, 2, 3, 3, 6, 6 under the chord-tangent
     law with O = (1:-1:0), at many values of lambda.
  5. Reciprocation is translation by the 2-torsion point (0:0:1) up to a
     coordinate permutation, on many random positive points.
  6. The dual surface: the six cubics e2 x, e2 y, e2 z, e1 yz, e1 zx, e1 xy
     span a 5-dimensional space (one linear relation, equal sums) and their
     base locus is the three coordinate points and the two points
     e1 = e2 = 0; no three of the five are collinear. Hence the image is an
     anticanonical quartic del Pezzo surface in P^4.
  7. Optional (needs cypari2): rank and torsion of selected curves by 2-descent.

Usage: variety_checks.py      (writes data/variety_checks.txt)
"""

from __future__ import annotations

import random
import sys
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cubic_group import O, TRIVIAL, Cubic, dual, lam, normalize  # noqa: E402

OUT: list[str] = []


def say(s=""):
    print(s, flush=True)
    OUT.append(s)


def main() -> int:
    x, y, z, L, t = sp.symbols("x y z lambda t")
    e1, e2, e3 = x + y + z, x*y + y*z + z*x, x*y*z

    # 1. scale invariance
    k = sp.symbols("k", positive=True)
    lam_s = lambda a, b, c: (a + b + c) * (a*b + b*c + c*a) / (a*b*c)
    assert sp.simplify(lam_s(k*x, k*y, k*z) - lam_s(x, y, z)) == 0
    say("PASS 1  lambda = e1 e2/e3 is scale invariant; lambda = S * R")

    # 2. Beauville
    assert sp.expand((x + y) * (y + z) * (z + x) - (e1 * e2 - e3)) == 0
    say("PASS 2  (x+y)(y+z)(z+x) = e1 e2 - e3, so e1 e2 - lambda e3 = Beauville's "
        "Gamma_1(6) pencil with t = 1 - lambda")

    # 3. Weierstrass model, derived by s = (x+y)/z, W = ((x-y)/z)(lambda-1-s), s = 1/X
    X = sp.symbols("X")
    a_, b_ = L - 1, L - 5
    cub = sp.expand((1 - a_ * X) * (4 * X**2 - b_ * X + 1))
    c3, c2, c1, c0 = sp.Poly(cub, X).all_coeffs()
    A2, A4, A6 = sp.factor(c2), sp.factor(c1 * c3), sp.factor(c0 * c3**2)
    assert sp.expand(A2 - (L - 3)**2) == 0
    assert sp.expand(A4 - 8 * (L - 3) * (L - 1)) == 0
    assert sp.expand(A6 - 16 * (L - 1)**2) == 0
    b2, b4, b6, b8 = 4*A2, 2*A4, 4*A6, 4*A2*A6 - A4**2
    c4 = sp.factor(b2**2 - 24*b4)
    Delta = sp.factor(-b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6)
    assert sp.expand(Delta - 4096 * L**2 * (L - 9) * (L - 1)**3) == 0
    say("PASS 3a model y^2 = x^3 + (l-3)^2 x^2 + 8(l-3)(l-1) x + 16(l-1)^2, "
        "Delta = 2^12 l^2 (l-9)(l-1)^3")
    # Kodaira types: multiplicative where ord(Delta) = n > 0 and c4 is a unit
    for place, n in [(0, 2), (1, 3), (9, 1)]:
        assert c4.subs(L, place) != 0
        assert sp.Poly(Delta, L).as_expr().subs(L, place) == 0
        say(f"        lambda = {place}: ord Delta = {n}, c4 = {c4.subs(L, place)} != 0  ->  I{n}")
    # at infinity: weights deg a_i <= i, so ord_inf Delta = 12 - deg Delta, ord_inf c4 = 4 - deg c4
    dD, dc4 = sp.degree(Delta, L), sp.degree(sp.expand(c4), L)
    assert (12 - dD, 4 - dc4) == (6, 0)
    say("        lambda = inf: ord Delta = 6, ord c4 = 0  ->  I6;  Euler numbers 6+3+2+1 = 12 "
        "(rational elliptic surface)")
    # BGN model and j-invariants
    j_ours = sp.cancel(c4**3 / Delta)
    aB, bB = L**2 - 6*L - 3, 16*L
    c4B = 16 * (aB**2 - 3 * bB)                  # for y^2 = x^3 + a x^2 + b x
    DB = 16 * bB**2 * (aB**2 - 4 * bB)
    assert sp.cancel(j_ours - c4B**3 / DB) == 0
    assert sp.factor(aB**2 - 4*bB) == sp.factor((L - 1)**3 * (L - 9))
    say("PASS 3b j-invariant equals that of the Bremner-Guy-Nowakowski model; "
        "their discriminant (n-1)^3 (n-9) reproduced")

    # 4. torsion of the base points
    rng = random.Random(1)
    lams = [Fraction(rng.randint(10, 400), rng.randint(1, 30)) for _ in range(40)]
    lams = [l for l in lams if l not in (0, 1, 9)]
    for l in lams:
        C = Cubic(l)
        orders = [C.order(T) for T in TRIVIAL]
        assert sorted(orders) == [1, 2, 3, 3, 6, 6], (l, orders)
    say(f"PASS 4  base points have orders {{1,2,3,3,6,6}} (a Z/6 subgroup) on {len(lams)} curves")

    # 5. reciprocation = translation by 2-torsion, up to permutation
    T2 = next(T for T in TRIVIAL if Cubic(Fraction(27, 2)).order(T) == 2)
    n = 0
    for _ in range(300):
        p = tuple(rng.randint(1, 60) for _ in range(3))
        l = lam(p)
        if l in (0, 1, 9):
            continue
        C = Cubic(l)
        Q = C.add(p, T2)
        assert tuple(sorted(normalize(Q))) == dual(p), (p, Q)
        n += 1
    say(f"PASS 5  (1/p,1/q,1/r) = P + T2 up to permutation, T2 = {T2}, on {n} random points")

    # 6. dual surface
    cubics = [e2*x, e2*y, e2*z, e1*y*z, e1*z*x, e1*x*y]
    mons = sorted(sp.Poly(sum(cubics), x, y, z).monoms())
    allm = sorted(set(m for c in cubics for m in sp.Poly(c, x, y, z).monoms()))
    M = sp.Matrix([[sp.Poly(c, x, y, z).coeff_monomial(m) for m in allm] for c in cubics])
    assert M.rank() == 5
    assert sp.expand(sum(cubics[:3]) - sum(cubics[3:])) == 0
    w = (-1 + sp.sqrt(3) * sp.I) / 2
    pts = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, w, w**2), (1, w**2, w)]
    for P in pts:
        assert all(sp.expand(c.subs({x: P[0], y: P[1], z: P[2]})) == 0 for c in cubics)
    for P, Q, R in combinations(pts, 3):
        assert sp.expand(sp.Matrix([P, Q, R]).det()) != 0
    say("PASS 6  six cubics span dimension 5 (single relation: equal sums); base points "
        "= 3 coordinate points + {e1=e2=0}, no three collinear -> anticanonical dP4 in P^4, "
        "Pic over Q of rank 1 + 3 + 1 = 5")

    # 7. ranks
    try:
        import cypari2
        pari = cypari2.Pari()
        pari.allocatemem(10**9)

        def info(l):
            A, B = l.numerator, l.denominator
            E = pari.ellinit([0, A*A - 6*A*B - 3*B*B, 0, 16*A*B**3, 0])
            r = pari.ellrank(E)
            return int(r[0]), int(r[1]), str(pari.elltors(E)[1])
        for l, why in [(Fraction(27, 2), "base pair (2,8,8),(3,3,12)"),
                       (Fraction(155, 12), "(4,9,18),(5,6,20), S = 31"),
                       (Fraction(68, 5), "first triple fibre S = 136, first quadruple S = 408"),
                       (Fraction(1849, 120), "first quintuple fibre S = 1849"),
                       (Fraction(230, 21), "quintuple S = 2300, sextuple S = 4600")]:
            lo, hi, tors = info(l)
            say(f"RANK 7  lambda = {l}: rank in [{lo},{hi}], torsion {tors}   ({why})")
    except ImportError:
        say("SKIP 7  cypari2 not installed; rank computations not run")

    (HERE / "data" / "variety_checks.txt").write_text("\n".join(OUT) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
