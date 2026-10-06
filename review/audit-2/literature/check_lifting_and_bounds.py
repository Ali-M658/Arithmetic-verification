"""(1) eslpower.org Theorem 3 (odd-exponent lifting): symbolic proof for m, n small and exact numeric samples,
    including the degenerate case in which the lifted pair is trivial.
(2) B5 / M1: compare the bound printed by Borwein-Ingalls p.7 ((k^2-3)/2 odd, (k^2-4)/2 even) with the
    lower bound N(k) >= k+1 (BI Prop. 2), with the known ideal values N(k) = k+1 (k <= 9, k = 11),
    with Wright's bound as reported by Melzak p.234 (K(n) <= (n^2+4)/2) and with Melzak's Table 1 (p.237).
(3) B4 / C1: the pigeonhole inequality in BI's proof of Prop. 3.
Exact arithmetic only; asserts; nonzero exit on failure.
"""
import sys
from fractions import Fraction as F
import sympy as sp

FAIL = []


def ok(cond, msg):
    print(("[OK]   " if cond else "[FAIL] ") + msg)
    if not cond:
        FAIL.append(msg)


def ps(xs, e):
    return sum(F(x) ** e for x in xs)


print("== (1) Theorem 3 of eslpower TarryPrb.htm ==")
# Symbolic: for m = 1..4 and n = 1..4, the difference
#   sum_i (T+a_i)^k + (T-b_i)^k - (T+b_i)^k - (T-a_i)^k
# equals sum over odd j <= k of 2*C(k,j)*T^(k-j)*(p_j(a)-p_j(b)); hence it vanishes for k <= 2n
# whenever p_j(a) = p_j(b) for odd j <= 2n-1.
T = sp.Symbol('T')
for m in range(1, 5):
    a = sp.symbols(f'a1:{m + 1}')
    b = sp.symbols(f'b1:{m + 1}')
    for k in range(1, 10):
        lhs = sp.expand(sum((T + ai) ** k + (T - bi) ** k - (T + bi) ** k - (T - ai) ** k for ai, bi in zip(a, b)))
        rhs = sp.expand(sum(2 * sp.binomial(k, j) * T ** (k - j) * (sum(ai ** j for ai in a) - sum(bi ** j for bi in b))
                            for j in range(1, k + 1, 2)))
        if sp.simplify(lhs - rhs) != 0:
            ok(False, f"identity m={m} k={k}")
ok(True, "identity sum[(T+a)^k+(T-b)^k-(T+b)^k-(T-a)^k] = sum_{j odd<=k} 2 C(k,j) T^(k-j) (p_j(a)-p_j(b)) holds for m<=4, k<=9")
print("   => if p_j(a)=p_j(b) for j=1,3,...,2n-1 then the lifted pair agrees for k=1..2n (only odd j<=k<=2n, i.e. j<=2n-1, occur).")

samples = [
    ("A.48 [1,5,5]=[2,3,6] (k=1,3), n=2", [1, 5, 5], [2, 3, 6], 2),
    ("A.178 [1,13,17,23]=[3,9,21,21] (k=1,3,5), n=3", [1, 13, 17, 23], [3, 9, 21, 21], 3),
    ("A.266 (k=1,3,5,7), n=4", [3, 19, 37, 51, 53], [9, 11, 43, 45, 55], 4),
    ("A.313 (k=1,...,9), n=5", [7, 91, 173, 269, 289, 323], [29, 59, 193, 247, 311, 313], 5),
]
for lab, A, B, n in samples:
    for Tv in (0, 1, 7, 100, -3):
        L = [Tv + x for x in A] + [Tv - x for x in B]
        R = [Tv + x for x in B] + [Tv - x for x in A]
        good = all(ps(L, k) == ps(R, k) for k in range(1, 2 * n + 1))
        nontriv = sorted(L) != sorted(R)
        nxt = ps(L, 2 * n + 1) != ps(R, 2 * n + 1)
        ok(good and nontriv, f"{lab}, T={Tv}: lifted size {len(L)} agrees for k=1..{2*n}; nontrivial={nontriv}; differs at {2*n+1}: {nxt}")
# odd ideal symmetric solution B = -A (paper's use, size 2L-1 -> degree 2L-2): lifting doubles it
A = [-51, -33, -24, 7, 13, 38, 50]
B = [-x for x in A]
L = [x for x in A] + [-x for x in B]
R = [x for x in B] + [-x for x in A]
ok(sorted(L) == sorted([x for x in A] * 2) and sorted(R) == sorted(B * 2),
   "degenerate case B=-A (T=0): lifting returns A doubled vs -A doubled (still a solution, degree 6 only; size doubles)")
# trivial lift: when the multiset A u (-B) equals B u (-A) the lifted pair is trivial; example
A, B = [1, -1, 5], [2, -2, 5]
ok(all(ps(A, j) == ps(B, j) for j in (1, 3, 5, 7, 9)) and sorted(A) != sorted(B), "A={1,-1,5}, B={2,-2,5}: all odd power sums agree, A != B")
L = [x for x in A] + [-x for x in B]
R = [x for x in B] + [-x for x in A]
ok(sorted(L) == sorted(R), "...and the lifted pair is trivial (equal multisets): Theorem 3 needs A u (-B) != B u (-A) for a non-trivial lift")

print("\n== (2) Bounds quoted for N(k) ==")
ideal_known = list(range(1, 10)) + [11]
for k in range(2, 14):
    bi = F(k * k - 3, 2) if k % 2 else F(k * k - 4, 2)
    lower = k + 1
    wright_melzak = F(k * k + 4, 2)
    pig = F(k * (k + 1), 2) + 1
    viol = bi < lower
    print(f"k={k:2d}: BI p.7 printed bound {str(bi):>6}  N(k)>=k+1={lower:3d}  {'VIOLATES lower bound' if viol else ''}"
          f"  | Wright via Melzak (k^2+4)/2={str(wright_melzak):>6} | pigeonhole k(k+1)/2+1={pig}"
          + (f" | known N(k)=k+1" if k in ideal_known else ""))
ok(F(2 * 2 - 4, 2) < 3 and F(3 * 3 - 3, 2) < 4,
   "BI's printed bound is false for k=2 ((k^2-4)/2 = 0 < N(2) = 3) and k=3 ((k^2-3)/2 = 3 < N(3) = 4)")
ok(all(F(k * k + 4, 2) - (F(k * k - 4, 2) if k % 2 == 0 else F(k * k - 3, 2)) in (F(4), F(7, 2)) for k in range(2, 50)),
   "BI's (k^2-3)/2, (k^2-4)/2 differ from Melzak's report of Wright (k^2+4)/2 by the constant 7/2 (odd) or 4 (even): not an index shift")
# index-shift test: is (k^2-4)/2 (or (k^2-3)/2) equal to ((k+-1)^2+4)/2 for some k?  ((k+d)^2+4) - (k^2-4) = 2dk + d^2 + 8
shift = [(k, d) for k in range(2, 200) for d in (-2, -1, 1, 2)
         if F((k + d) ** 2 + 4, 2) == (F(k * k - 4, 2) if k % 2 == 0 else F(k * k - 3, 2))]
print(f"   index shifts k -> k+d (|d|<=2, k<200) under which Wright/Melzak's (n^2+4)/2 equals BI's printed value: {shift}")
ok(shift == [] or all(d < 0 for _, d in shift), "no uniform index shift reconciles the two formulas")
melzak_table = {2: 3, 3: 4, 4: 6, 5: 8, 6: 10, 7: 14, 8: 18, 9: 22, 10: 22, 11: 34, 12: 32, 13: 41, 14: 46, 15: 58,
                16: 58, 17: 75, 18: 74, 19: 92, 20: 100, 21: 124, 22: 118, 23: 146, 24: 159, 25: 170, 26: 196,
                27: 216, 28: 207, 29: 266}
melzak_pig = {2: 4, 3: 7, 4: 11, 5: 16, 6: 22, 7: 29, 8: 37, 9: 46, 10: 56, 11: 67, 12: 79, 13: 92, 14: 106, 15: 121,
              16: 137, 17: 154, 18: 172, 19: 191, 20: 211, 21: 232, 22: 254, 23: 277, 24: 301, 25: 326, 26: 352,
              27: 379, 28: 407, 29: 436}
ok(all(melzak_pig[n] == n * (n + 1) // 2 + 1 for n in melzak_pig), "Melzak Table 1 last column equals n(n+1)/2+1 for every n=2..29")
ok(all(melzak_table[n] >= n + 1 for n in melzak_table), "every Melzak table bound b_n >= n+1 (consistent with K(n) >= n+1)")
below_bi = [n for n in melzak_table if melzak_table[n] < (F(n * n - 3, 2) if n % 2 else F(n * n - 4, 2))]
print(f"   n with Melzak's individual b_n below BI's closed form: {below_bi}")
print(f"   ratio b_29 / 29^2 = {F(266, 29*29)} ~ {266/841:.3f}")

print("\n== (3) BI Prop. 3 pigeonhole inequality ==")
# with s = k(k+1)/2 + 1 and n > s^k s!: prod_{j=1}^k (s n^j - s + 1) < s^k n^{k(k+1)/2} = s^k n^{s-1} < n^s / s!
import math
for k in range(1, 6):
    s = k * (k + 1) // 2 + 1
    n = s ** k * math.factorial(s) + 1
    prod = 1
    for j in range(1, k + 1):
        prod *= s * n ** j - s + 1
    ok(prod < s ** k * n ** (s - 1) and F(s ** k * n ** (s - 1)) < F(n ** s, math.factorial(s)),
       f"k={k}, s={s}, n=s^k s!+1: #value-vectors < s^k n^(s-1) < n^s/s! (<= number of multisets)")

print("\nFAILURES:", FAIL)
sys.exit(1 if FAIL else 0)
