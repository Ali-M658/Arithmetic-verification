"""'Real solutions of that shape exist in abundance' (PW.0 item 6, PW.1 rem:ptet3).

A real (3,5) configuration with five-element side Y is a triple of positive REALS X with
sum x = sum y, sum x^3 = sum y^3, sum 1/x = sum 1/y.  By the derivation in check_t3.c, X is the
root set of f(x) = x^3 - e1 x^2 + e2 x - e3 with e1 = p1, e3 = (p3 - p1^3)/(3(1 - p1 r)), e2 = r e3
(e1, e2, e3 > 0), so X exists iff disc(f) >= 0, and X consists of three distinct positive reals iff
disc(f) > 0.  Here disc(f) is computed EXACTLY (Fractions) for every multiset Y of positive
integers <= 24 (C(28,5) = 98280 multisets), and for a disjointness check X cap Y = empty a
rational root test is unnecessary (X is irrational unless f has a rational root; checked by the
C search).  Exit nonzero if no real solution exists.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr
NMAX = 24
pos = zero = neg = 0
first = None
for Y in cwr(range(1, NMAX + 1), 5):
    p1 = sum(Y); p3 = sum(y ** 3 for y in Y); r = sum(F(1, y) for y in Y)
    e1 = F(p1); e3 = F(p3 - p1 ** 3) / (3 * (1 - p1 * r)); e2 = r * e3
    assert e3 > 0 and e2 > 0
    a, b, c = -e1, e2, -e3
    disc = 18 * a * b * c - 4 * a ** 3 * c + a * a * b * b - 4 * b ** 3 - 27 * c * c
    if disc > 0:
        pos += 1
        if first is None:
            first = (Y, e1, e2, e3)
    elif disc == 0:
        zero += 1
    else:
        neg += 1
tot = pos + zero + neg
print(f"Y ranges over all multisets of 5 positive integers <= {NMAX}: {tot}")
print(f"  disc > 0 (three distinct positive real x): {pos} ({100 * pos / tot:.2f}%)")
print(f"  disc = 0: {zero};  disc < 0 (no real configuration): {neg}")
Y, e1, e2, e3 = first
print(f"  first Y with a real configuration: {Y}, cubic x^3 - {e1} x^2 + {e2} x - {e3}")
import mpmath as mp
mp.mp.dps = 40
rts = mp.polyroots([1, -mp.mpf(e1.numerator) / e1.denominator, mp.mpf(e2.numerator) / e2.denominator,
                    -mp.mpf(e3.numerator) / e3.denominator])
print("  [non-certificate, mpmath 40 digits] its real X:", [mp.nstr(mp.re(t), 15) for t in rts])
assert pos > 0
print("ALL OK")
