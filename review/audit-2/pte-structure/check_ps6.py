"""PS.6 (statements.tex) versus proof.md: exact witnesses for the wording findings.
Input for 'share L coefficients': [Sig] Lemma 4 (4.1).  Exits nonzero on failure."""
import sys
from fractions import Fraction as F
import confenum as C
from check_dictionary import share, area2pi

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("FAIL:", msg)


def mirror(sig1, sig2):
    """padded, cancelled mirror multiset Z = U* (+) -V* (R(U)=R(V)); None if R-R' not integral"""
    (g, m), (h, mm) = sig1, sig2
    d = sum(F(1, x) for x in mm) - sum(F(1, x) for x in m)
    if d.denominator != 1:
        return None
    d = int(d)
    U = list(m) + [1] * max(d, 0); V = list(mm) + [1] * max(-d, 0)
    for x in list(U):
        if x in V:
            U.remove(x); V.remove(x)
    return tuple(sorted(U + [-v for v in V]))


# (i) 'exactly when Z is an L-configuration' needs the genus condition iota(Z) = 2(g'-g)
s1, s2 = (2, (15,)), (0, (3, 3, 5, 5))
Z = mirror(s1, s2)
check(C.is_config(Z, 2), "Z should be a 2-configuration")
check(C.iota(Z) != 2 * (s2[0] - s1[0]), "genus condition should fail")
check(area2pi(*s1) != area2pi(*s2) and not share(s1, s2, 1), "they should not share c_1")
print("(i)", s1, s2, ": Z =", Z, "is a 2-configuration, iota =", C.iota(Z), "!= 2(g'-g) =",
      2 * (s2[0] - s1[0]), "; Area/2pi =", area2pi(*s1), "vs", area2pi(*s2), "-> not even c_1 shared")
t1 = (1, (15,))
check(share(t1, s2, 2) and C.iota(mirror(t1, s2)) == 2 * (s2[0] - t1[0]), "(1;15) example")
print("    with genus 1 instead of 2: (1;15) ~ (0;3,3,5,5) share 2 coefficients, iota = 2(g'-g) = -2")

# (ii) 'equality ... forces {L, L+2}': equality in |U*|+|V*| >= 2L+2|g-g'| with |g-g'| = 2
Z = (-10, -10, -8, -5, -4, -4, 1, 40)       # found by check_attain.py (L=2, shape (2,6))
check(C.is_config(Z, 2) and C.maxL(Z) == 2, "attain example")
a = (2, (40,)); b = (0, (4, 4, 5, 8, 10, 10))
check(mirror(a, b) == Z and share(a, b, 2) and not share(a, b, 3), "orbifold pair (2;40)~(0;4,4,5,8,10,10)")
nU, nV = 2, 6
check(nU + nV == 2 * 2 + 2 * abs(a[0] - b[0]), "equality in the displayed inequality")
print("(ii) (2;40) and (0;4,4,5,8,10,10) share exactly 2 coefficients; |U*|+|V*| = 8 = 2L+2|g-g'|"
      " (equality), shape {2,6} != {L,L+2} = {2,4}")

# (iii) tex Prop. ptebalanced without '0 notin A': A = {-1,0,1} has s_1 = 0 (L = 2)
A = (-1, 0, 1)
check(sum(A) == 0, "A odd sums")
print("(iii) A = {-1,0,1}: |A| = 3 = 2L-1, s_1(A) = 0, but sum a^{-1} is undefined (0 in A);",
      "the proof.md version excludes it by '0 notin A'")

# (iv) Lemma 1.2(2) 'U \\ {1}' with 1 of multiplicity 2 (from check_dictionary.py)
Z = (-15, -5, -1, -1, 2, 2, 2, 3, 3, 10)
check(C.is_config(Z, 2) and Z.count(-1) == 2, "multiplicity-2 example")
print("(iv) Z =", Z, ": V = {15,5,1,1}; removing a single 1 leaves an order-1 'cone point';"
      " the signature must be (1;5,15)")
print("FAILURES:", len(FAIL))
sys.exit(1 if FAIL else 0)
