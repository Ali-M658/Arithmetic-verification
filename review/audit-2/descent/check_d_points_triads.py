"""(d) The twelve rational points of C_{27/2}; the positive ones; triads with S_1 = 18k, R = 3/(4k).

Exact integer/Fraction arithmetic.  Exits nonzero on any failure.
"""
from fractions import Fraction as Fr
from math import gcd, isqrt
from itertools import permutations
from descent_lib import F_lam, normalize, PlaneCubicGroup, Out

o = Out()
lam = Fr(27, 2)
listed = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, -1, 0), (0, 1, -1), (1, 0, -1)]
listed += sorted(set(permutations((1, 4, 4)))) + sorted(set(permutations((1, 1, 4))))
for P in listed:
    o.ok(F_lam(lam, P) == 0, f"{P} lies on C_27/2")
o.ok(len({normalize(P) for P in listed}) == 12, "the 12 listed points are pairwise distinct projective points")
# psi(E(Q)) from check_a gives exactly these 12 (recomputed here)
E_pts = [(0, 0), (-9, 0), (-384, 0), (-24, 360), (-24, -360), (-144, 2160), (-144, -2160),
         (16, 400), (16, -400), (216, 5400), (216, -5400)]
img = {(1, -1, 0)} | {normalize((25 * x + y, 25 * x - y, 4 * (x - 216))) for (x, y) in E_pts}
o.ok(img == {normalize(P) for P in listed}, "psi(E(Q)) = the 12 listed points, so C_27/2(Q) = these 12")
pos = sorted(P for P in listed if all(t > 0 for t in normalize(P)) or all(t < 0 for t in normalize(P)))
o.ok(pos == sorted(set(permutations((1, 4, 4))) | set(permutations((1, 1, 4)))),
     f"positive points = 6 permutations of (1,4,4),(1,1,4): {pos}")

# points with a zero coordinate: exactly the six base points (for any lambda)
zero = [P for P in listed if 0 in P]
o.ok(len(zero) == 6, "6 points with a zero coordinate: the base points")

# independent brute force (does not use the descent): all primitive integer points with |coords| <= B
B = 80
found = set()
for X in range(-B, B + 1):
    for Y in range(-B, B + 1):
        # solve for Z: F is quadratic in Z: (X+Y+Z)(XY + Z(X+Y)) - lam X Y Z = 0
        # 2*: 2(X+Y)Z^2 + (2(X+Y)^2 + 2XY - 27XY) Z + 2(X+Y)XY = 0
        a = 2 * (X + Y)
        b = 2 * (X + Y) ** 2 - 25 * X * Y
        c = 2 * (X + Y) * X * Y
        if a == 0:
            if b == 0:
                if c == 0 and (X, Y) != (0, 0):
                    # every Z works? only if F vanishes identically on the line; check Z = 0,1
                    for Z in range(-B, B + 1):
                        if F_lam(lam, (X, Y, Z)) == 0 and gcd(gcd(X, Y), Z) == 1:
                            found.add(normalize((X, Y, Z)))
                continue
            Zs = [Fr(-c, b)]
        else:
            disc = b * b - 4 * a * c
            if disc < 0:
                continue
            r = isqrt(disc)
            if r * r != disc:
                continue
            Zs = [Fr(-b + r, 2 * a), Fr(-b - r, 2 * a)]
        for Z in Zs:
            if (X, Y, Z) == (0, 0, 0):
                continue
            Pn = normalize((X, Y, Z))
            if max(abs(t) for t in Pn) <= B:
                assert F_lam(lam, Pn) == 0
                found.add(Pn)
# (0:0:1) has X = Y = 0 -> add check separately
if F_lam(lam, (0, 0, 1)) == 0:
    found.add((0, 0, 1))
o.ok(found == {normalize(P) for P in listed}, f"brute force |coords| <= {B}: exactly the 12 points ({len(found)})")

# group structure on the cubic with base O = (1:-1:0)
C = PlaneCubicGroup(lam, (1, -1, 0))
orders = {normalize(P): C.order(P) for P in listed}
print("orders on C_27/2 with base O=(1:-1:0):", orders)
o.ok([orders[normalize(P)] for P in listed[:6]] == [6, 6, 2, 1, 3, 3], "base-point orders 6,6,2,1,3,3 in the listed order")
o.ok(orders[(1, 4, 4)] == 6, "(1:4:4) has order 6")
base = {normalize(P) for P in listed[:6]}
trans = {C.add(P, (1, 4, 4)) for P in base}
o.ok(base | trans == {normalize(P) for P in listed} and not (base & trans),
     "the 12 points = six base points and their translates by (1:4:4)")

# ---------------- triads -----------------
def R(t):
    return sum(Fr(1, s) for s in t)


def classes_at(S, Rv):
    out = []
    for a in range(1, S // 3 + 1):
        for b in range(a, (S - a) // 2 + 1):
            c = S - a - b
            if c < b:
                continue
            if Fr(1, a) + Fr(1, b) + Fr(1, c) == Rv:
                out.append((a, b, c))
    return out


for k in list(range(1, 31)) + [36, 42, 49, 60]:
    S, Rv = 18 * k, Fr(3, 4 * k)
    o.ok(S * Rv == lam, f"k={k}: S_1 R = 27/2")
    cl = classes_at(S, Rv)
    o.ok(cl == sorted([(2 * k, 8 * k, 8 * k), (3 * k, 3 * k, 12 * k)]),
         f"k={k}: all positive integer triples with S=18k, R=3/(4k): {cl}")
    for t in cl:
        o.ok(R(t) < 1 and min(t) >= 2, f"k={k}: {t} hyperbolic (R={R(t)} < 1, entries >= 2)")

# non-integer k with 18k integral: the 'for every k' needs k to be a positive integer
print("non-integer k:")
for k in (Fr(1, 2), Fr(3, 2), Fr(5, 2), Fr(1, 3), Fr(2, 3), Fr(1, 6), Fr(7, 6), Fr(1, 18)):
    S = 18 * k
    assert S.denominator == 1
    cl = classes_at(int(S), Fr(3, 4) / k)
    hyp = [t for t in cl if R(t) < 1 and min(t) >= 2]
    print(f"   k={k}: S={S}, members {cl}, hyperbolic {hyp}")
    o.ok(len(cl) <= 1, f"k={k} (non-integer): the class has {len(cl)} member(s), not two")

# exactly one integer representative with sum 18k for each positive point
for k in range(1, 50):
    for base_t in ((1, 4, 4), (1, 1, 4)):
        reps = [m for m in range(1, 18 * k + 1) if m * sum(base_t) == 18 * k]
        o.ok(len(reps) == 1, f"k={k}: unique scaling of {base_t} with sum 18k (m={reps})") if k < 4 else None
        assert len(reps) == 1
o.ok(True, "unique representative with sum 18k for k = 1..49")

# pillows (j,4j,4j) with j odd have no partner (class of size 1)
for j in range(1, 40, 2):
    cl = classes_at(9 * j, R((j, 4 * j, 4 * j)))
    o.ok(cl == [(j, 4 * j, 4 * j)], f"j={j} odd: (j,4j,4j) is alone in its class")
print(f"ALL {o.n} CHECKS PASSED")
