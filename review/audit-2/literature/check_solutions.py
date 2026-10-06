"""Exact verification of every numerical PTE / GPTE solution quoted in the literature bundle.

Integers and fractions.Fraction only; every check is an assert; exit status nonzero on failure.
Run: /opt/homebrew/Caskroom/miniforge/base/bin/python3 check_solutions.py > check_solutions.txt
"""
from fractions import Fraction as F
import sys

FAIL = []


def psum(xs, e):
    if e == 0:
        p = 1
        for x in xs:
            p *= x
        return p
    return sum(F(x) ** e for x in xs)


def check(label, A, B, exps, must_fail_next=None):
    """A, B multisets of equal size; exps list of exponents that must agree.
    must_fail_next: an exponent at which the sums must differ (used to confirm exact degree)."""
    assert len(A) == len(B), label
    assert sorted(A) != sorted(B), label + " trivial"
    bad = [e for e in exps if psum(A, e) != psum(B, e)]
    ok = not bad
    extra = ""
    if must_fail_next is not None:
        diff = psum(A, must_fail_next) != psum(B, must_fail_next)
        extra = f"; exponent {must_fail_next} differs: {diff}"
        ok = ok and diff
    print(f"[{'OK' if ok else 'FAIL'}] {label}: size {len(A)}, exponents {exps}{extra}" + (f"  BAD at {bad}" if bad else ""))
    if not ok:
        FAIL.append(label)


def pm(xs):
    return [s * x for x in xs for s in (1, -1)]


def neg(xs):
    return [-x for x in xs]


print("== B10: Borwein-Ingalls p.9 table (abbreviated symmetric form) ==")
check("BI size 2 {+-3}/{+-1}", pm([3]), pm([1]), [1], 2)
check("BI size 3 {-2,-1,3} vs negatives", [-2, -1, 3], neg([-2, -1, 3]), [1, 2], 3)
check("BI size 4 {+-3,+-11}/{+-7,+-9}", pm([3, 11]), pm([7, 9]), [1, 2, 3], 4)
check("BI size 5 {-8,-7,1,5,9}", [-8, -7, 1, 5, 9], neg([-8, -7, 1, 5, 9]), [1, 2, 3, 4], 5)
check("BI size 6 {+-4,+-9,+-13}/{+-1,+-11,+-12}", pm([4, 9, 13]), pm([1, 11, 12]), [1, 2, 3, 4, 5], 6)
check("BI size 8 {+-2,+-16,+-21,+-25}/{+-5,+-14,+-23,+-24}", pm([2, 16, 21, 25]), pm([5, 14, 23, 24]), list(range(1, 8)), 8)
seven = [[-51, -33, -24, 7, 13, 38, 50], [-90, -86, -39, -5, 48, 77, 95], [-116, -104, -36, -19, 75, 77, 123],
         [-120, -110, -23, -13, 38, 105, 123], [-134, -75, -66, 8, 47, 87, 133]]
for s in seven:
    check(f"BI p.25 perfect 7-set {s}", s, neg(s), list(range(1, 7)), 7)
    perfect = sorted(x % 7 for x in s) == list(range(7))
    print(f"   complete residue system mod 7 ('perfect'): {perfect}")
    if not perfect:
        FAIL.append("perfect " + str(s))
nine = [[-98, -82, -58, -34, 13, 16, 69, 75, 99], [-169, -161, -119, -63, 8, 50, 132, 148, 174]]
for s in nine:
    check(f"Letac 9-set {s}", s, neg(s), list(range(1, 9)), 9)
    perfect = sorted(x % 9 for x in s) == list(range(9))
    print(f"   complete residue system mod 9: {perfect}")
# CMSV (3) second set is the negative of BI's second 9-set
assert sorted([-174, -148, -132, -50, -8, 63, 119, 161, 169]) == sorted(neg(nine[1]))
print("[OK] CMSV (3) second 9-set = -(BI second 9-set) (same solution, A and B swapped)")
check("BI size 10 #1 (Letac per BLP p.2069)", pm([436, 11857, 20449, 20667, 23750]), pm([12, 11881, 20231, 20885, 23738]), list(range(1, 10)), 10)
check("BI size 10 #2 (Smyth per BI p.10)", pm([133225698289, 189880696822, 338027122801, 432967471212, 529393533005]),
      pm([87647378809, 243086774390, 308520455907, 441746154196, 527907819623]), list(range(1, 10)), 10)

print("\n== B12: Proposition 4 (Smyth) at the two printed rational points ==")


def prop4(x, y):
    A = [4 * x + 4 * y, x * y + x + y - 11, x * y - x - y - 11, x * y + 3 * x - 3 * y + 11, x * y - 3 * x + 3 * y + 11]
    B = [4 * x - 4 * y, x * y - x + y + 11, x * y + x - y + 11, x * y - 3 * x - 3 * y - 11, x * y + 3 * x + 3 * y - 11]
    return A, B


def normalize(S):
    """primitive, sorted absolute values of a +- symmetric set"""
    from math import gcd
    from functools import reduce
    den = reduce(lambda a, b: a * b // gcd(a, b), [F(v).denominator for v in S])
    ints = [abs(int(F(v) * den)) for v in S]
    g = reduce(gcd, ints)
    return sorted(i // g for i in ints)


listed10 = [(sorted([436, 11857, 20449, 20667, 23750]), sorted([12, 11881, 20231, 20885, 23738])),
            (sorted([133225698289, 189880696822, 338027122801, 432967471212, 529393533005]),
             sorted([87647378809, 243086774390, 308520455907, 441746154196, 527907819623]))]
for (x, y) in [(F(153, 61), F(191, 79)), (F(-296313, 249661), F(-1264969, 424999))]:
    on = x * x * y * y - 13 * x * x - 13 * y * y + 121
    print(f"point ({x}, {y}): on curve x^2y^2-13x^2-13y^2+121=0: {on == 0}")
    if on != 0:
        FAIL.append(f"Prop4 point {x},{y}")
    A, B = prop4(x, y)
    check(f"Prop4 solution at ({x},{y})", pm(A), pm(B), list(range(1, 10)), 10)
    nA, nB = normalize(A), normalize(B)
    match = [i for i, (a, b) in enumerate(listed10) if {tuple(a), tuple(b)} == {tuple(nA), tuple(nB)}]
    print(f"   primitive form A={nA} B={nB}; matches BI p.9 size-10 entry #{[m + 1 for m in match]}")
    if not match:
        FAIL.append(f"Prop4 match {x},{y}")
# symbolic: difference of the two products is constant modulo the curve
import sympy as sp
X, Y, Z = sp.symbols('x y z')
A, B = prop4(X, Y)
pA = sp.prod([(Z ** 2 - a ** 2) for a in A])
pB = sp.prod([(Z ** 2 - b ** 2) for b in B])
diff = sp.Poly(sp.expand(pA - pB), Z)
curve = X ** 2 * Y ** 2 - 13 * X ** 2 - 13 * Y ** 2 + 121
nonconst = [(m, c) for m, c in zip(diff.monoms(), diff.coeffs()) if m[0] > 0]
# exact divisibility test via resultant-free approach: reduce modulo curve as polynomial in X^2
red_ok = True
for m, c in nonconst:
    q, r = sp.div(sp.Poly(sp.expand(c), X, Y), sp.Poly(curve, X, Y))
    if not r.is_zero:
        red_ok = False
print(f"[{'OK' if red_ok else 'FAIL'}] Prop. 4 symbolic: every non-constant coefficient (in z) of prod(z^2-A_i^2)-prod(z^2-B_i^2) is divisible by the curve polynomial")
if not red_ok:
    FAIL.append("Prop4 symbolic")

print("\n== D3 / P2: CMSV and BLP ==")
check("BLP/CMSV size 10 (A.277)", pm([71, 131, 180, 307, 308]), pm([99, 100, 188, 301, 313]), list(range(1, 10)), 10)
check("BLP/CMSV size 10 (A.278)", pm([18, 245, 331, 471, 508]), pm([103, 189, 366, 452, 515]), list(range(1, 10)), 10)
check("Kuosa-Meyrignac-Chen size 12 (CMSV (5))", pm([22, 61, 86, 127, 140, 151]), pm([35, 47, 94, 121, 146, 148]), list(range(1, 12)), 12)
check("Broadhurst size 12 (CMSV (6))", pm([257, 891, 1109, 1618, 1896, 2058]), pm([472, 639, 1294, 1514, 1947, 2037]), list(range(1, 12)), 12)
check("Choudhry-Wroblewski size 12 (CMSV (7))", pm([107, 622, 700, 1075, 1138, 1511]), pm([293, 413, 886, 953, 1180, 1510]), list(range(1, 12)), 12)
# Gloden two-parameter (as simplified by BLP p.2064)
f, k = sp.symbols('f k')
al = [-(f ** 2 - k * f + k ** 2) * (-3 * k * f ** 2 + k ** 3 + f ** 3),
      -(k - f) * (f + k) * (f ** 2 - 3 * k * f + k ** 2) * f,
      (-f + 2 * k) * (-f ** 2 - k * f + k ** 2) * k * f,
      (k - f) * (k - 2 * f) * (-f ** 2 + k * f + k ** 2) * k,
      (k - f) * (f ** 4 - 2 * k * f ** 3 - k ** 2 * f ** 2 + k ** 4),
      -(k ** 4 - 2 * f * k ** 3 - k ** 2 * f ** 2 + 4 * k * f ** 3 - f ** 4) * k,
      -(k ** 4 - 5 * k ** 2 * f ** 2 + 4 * k * f ** 3 - f ** 4) * f]
okg = all(sp.expand(sum(a ** e for a in al)) == 0 for e in (1, 3, 5))
print(f"[{'OK' if okg else 'FAIL'}] BLP p.2064 Gloden family: sum alpha_i^e == 0 identically in f,k for e=1,3,5")
if not okg:
    FAIL.append("Gloden family")
ex = [int(a.subs({f: 3, k: 1})) for a in al]
print(f"   f=3,k=1 gives {ex}; BLP prints {{-7, 24, 33, -50, -38, -13, 51}}: match = {sorted(ex) == sorted([-7, 24, 33, -50, -38, -13, 51])}")
if sorted(ex) != sorted([-7, 24, 33, -50, -38, -13, 51]):
    FAIL.append("Gloden example")
print(f"   and this is -(BI perfect 7-set {{-51,-33,-24,7,13,38,50}}): {sorted(ex) == sorted(neg(seven[0]))}")

print("\n== C2 / D1 / D4: Chen survey Example 1.1 and 1.2 (ideal solutions of degree k, size k+1) ==")
deg_sols = {
    6: ([0, 18, 27, 58, 64, 89, 101], [1, 13, 38, 44, 75, 84, 102]),
    7: ([0, 4, 9, 23, 27, 41, 46, 50], [1, 2, 11, 20, 30, 39, 48, 49]),
    8: ([0, 24, 30, 83, 86, 133, 157, 181, 197], [1, 17, 41, 65, 112, 115, 168, 174, 198]),
    9: ([0, 3083, 3301, 11893, 23314, 24186, 35607, 44199, 44417, 47500], [12, 2865, 3519, 11869, 23738, 23762, 35631, 43981, 44635, 47488]),
    11: ([0, 11, 24, 65, 90, 129, 173, 212, 237, 278, 291, 302], [3, 5, 30, 57, 104, 116, 186, 198, 245, 272, 297, 299]),
}
for d, (A, B) in deg_sols.items():
    check(f"Chen Ex.1.1 degree {d} (size {len(A)})", A, B, list(range(1, d + 1)), d + 1)
check("Chen Ex.1.2 A.282 degree 5 non-symmetric", [0, 19, 25, 57, 62, 86], [2, 11, 40, 42, 69, 85], [1, 2, 3, 4, 5], 6)
check("Chen Ex.1.2 A.324 degree 6 non-symmetric", [0, 18, 19, 50, 56, 79, 81], [1, 11, 30, 39, 68, 70, 84], list(range(1, 7)), 7)
check("Chen Ex.1.2 A.358 degree 7 non-symmetric", [0, 7, 23, 50, 53, 81, 82, 96], [1, 5, 26, 42, 63, 72, 88, 95], list(range(1, 8)), 8)

print("\n== S1: Chen Appendix A.1.6, A.1.17, A.1.26, A.1.33 (odd exponents) ==")
S1 = [
    ("A.48 (A.1.6) [1,5,5]=[2,3,6]", [1, 5, 5], [2, 3, 6], [1, 3]),
    ("A.45", [0, 7, 8], [1, 5, 9], [1, 3]), ("A.46", [0, 7, 9], [2, 4, 10], [1, 3]), ("A.47", [12, 23, 28], [13, 21, 29], [1, 3]),
    ("A.178 (A.1.17) [1,13,17,23]=[3,9,21,21]", [1, 13, 17, 23], [3, 9, 21, 21], [1, 3, 5]),
    ("A.179", [0, 24, 33, 51], [7, 13, 38, 50], [1, 3, 5]), ("A.180", [53, 151, 187, 233], [51, 165, 173, 235], [1, 3, 5]),
    ("A.266 (A.1.26) [3,19,37,51,53]=[9,11,43,45,55]", [3, 19, 37, 51, 53], [9, 11, 43, 45, 55], [1, 3, 5, 7]),
    ("A.269 Letac", [0, 34, 58, 82, 98], [13, 16, 69, 75, 99], [1, 3, 5, 7]),
    ("A.270 Letac", [0, 63, 119, 161, 169], [8, 50, 132, 148, 174], [1, 3, 5, 7]),
    ("A.313 (A.1.33) Chen 2000", [7, 91, 173, 269, 289, 323], [29, 59, 193, 247, 311, 313], [1, 3, 5, 7, 9]),
    ("A.314 Wroblewski 2009", [23, 163, 181, 341, 347, 407], [37, 119, 221, 311, 371, 403], [1, 3, 5, 7, 9]),
    ("A.315 Wroblewski 2009", [43, 161, 217, 335, 391, 463], [85, 91, 283, 287, 403, 461], [1, 3, 5, 7, 9]),
    ("A.316 Wroblewski 2009", [57, 399, 679, 995, 1167, 1293], [115, 299, 767, 925, 1205, 1279], [1, 3, 5, 7, 9]),
    ("A.1.33 negative-entry solution (Wroblewski 2009)", [-13, 365, 689, 1111, 1115, 1325], [23, 305, 731, 1037, 1177, 1319], [1, 3, 5, 7, 9]),
    ("A.219 Chernick (A.1.21)", [0, 4, 8, 16, 17], [1, 2, 10, 14, 18], [1, 2, 3, 4]),
    ("A.220 Chernick (A.1.21)", [0, 6, 8, 17, 19], [1, 3, 12, 14, 20], [1, 2, 3, 4]),
    ("A.323 Chernick (A.1.35)", [0, 59, 68, 142, 181, 221, 267], [1, 47, 87, 126, 200, 209, 268], list(range(1, 7))),
]
for lab, A, B, ex in S1:
    nxt = ex[-1] + 2 if ex[0] == 1 and all(e % 2 for e in ex) else ex[-1] + 1
    check(lab, A, B, ex, None)
# The six-term odd solutions (L = 6) must have size L = len(exps)+1
assert all(len(A) == len(ex) + 1 for _, A, _, ex in S1 if ex[0] == 1 and all(e % 2 for e in ex))
print("[OK] each odd-exponent entry has size = (number of exponents) + 1 = L")

print("\n== S3: negative exponents (Chen A.5) ==")
S3 = [
    ("A.650 type (-1,1) [4,10,12]=[5,6,15]", [4, 10, 12], [5, 6, 15], [-1, 1]),
    ("A.651 type (-1,1)", [6, 14, 14], [7, 9, 18], [-1, 1]),
    ("A.685 type (-1,1,3) [3,10,15,30]=[4,5,21,28]", [3, 10, 15, 30], [4, 5, 21, 28], [-1, 1, 3]),
    ("A.686", [7, 15, 50, 75], [9, 10, 56, 72], [-1, 1, 3]),
    ("A.692", [11, 33, 44, 84], [14, 18, 63, 77], [-1, 1, 3]),
    ("kminus.htm (-1,1,3) [7,15,78,91]=[6,25,60,100]", [7, 15, 78, 91], [6, 25, 60, 100], [-1, 1, 3]),
    ("A.693 type (-1,1,5) [81,374,585,891]=[85,286,702,858]", [81, 374, 585, 891], [85, 286, 702, 858], [-1, 1, 5]),
    ("A.661 type (-2,2)", [77, 1057, 1661], [91, 143, 1963], [-2, 2]),
]
for lab, A, B, ex in S3:
    check(lab, A, B, ex)
# A.685 differs at exponent 5 (so it is not of type (-1,1,3,5))
print(f"   A.685 at exponent 5 equal? {psum([3,10,15,30],5) == psum([4,5,21,28],5)}; at 2? {psum([3,10,15,30],2) == psum([4,5,21,28],2)}")

print("\n== Melzak p.234 construction: size 2^n solution of degree n from (1-x)^(n+1) ==")
from math import comb
for n in range(1, 8):
    x0 = 0
    A, B = [], []
    for j in range(n + 2):
        (A if j % 2 == 0 else B).extend([x0 - j] * comb(n + 1, j))
    check(f"Melzak (5) n={n}", A, B, list(range(1, n + 1)), n + 1)
    assert len(A) == 2 ** n

print("\nFAILURES:", FAIL)
sys.exit(1 if FAIL else 0)
