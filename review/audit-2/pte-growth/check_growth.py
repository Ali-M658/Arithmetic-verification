#!/usr/bin/env python3
"""G5-bis pte-growth: arithmetic of Theorems 4.1, 4.2, 4.3.  Exact rationals, no floats.

Write x = A/(2 pi) and t = A/pi (any positive real; we test exact rationals, including every
breakpoint, points just below/above it, and A = 8 pi exactly).
"""
import sys, math, itertools
from fractions import Fraction as F

fails = 0
def check(cond, msg, quiet=False):
    global fails
    if not cond:
        fails += 1
        print("FAIL " + msg)
    elif not quiet:
        print("OK   " + msg)

def floorsqrt(y):
    """largest integer k >= 0 with k^2 <= y, y a nonnegative Fraction (exact)."""
    assert y >= 0
    k = math.isqrt(y.numerator // y.denominator)
    while (k + 1) ** 2 <= y:
        k += 1
    while k * k > y:
        k -= 1
    return k

def ffloor(q):
    return q.numerator // q.denominator

# ---------------- Theorem 4.1 ----------------
def largest_L(x):
    """largest L >= 2 with 3(L-1)^2 + 1 <= x (None if none)."""
    L = None
    l = 2
    while 3 * (l - 1) ** 2 + 1 <= x:
        L = l; l += 1
    return L

eps_list = [F(1, 10 ** 9), F(1, 10 ** 30)]
npts = 0
for m in range(1, 1500):
    bp = F(3 * m * m + 1)
    pts = [bp] + [bp - e for e in eps_list] + [bp + e for e in eps_list]
    for x in pts:
        if x < 4:
            continue
        L = largest_L(x)
        formula = floorsqrt((x - 1) / 3) + 2
        check(L is not None and L + 1 == formula, f"Thm 4.1 floor identity at x={x}", quiet=True)
        npts += 1
check(True, f"Thm 4.1: 'largest L with 3(L-1)^2+1 <= A/2pi' + 1 == floor(sqrt((A/2pi-1)/3)) + 2 at {npts} points (all breakpoints m < 1500, +-1e-9, +-1e-30)")
x = F(4)
check(largest_L(x) == 2 and floorsqrt((x - 1) / 3) + 2 == 3, "Thm 4.1 at A = 8 pi exactly: L = 2, bound = 3")
check(largest_L(F(4) - F(1, 10 ** 20)) is None, "just below A = 8 pi no L >= 2 qualifies (hypothesis A >= 8 pi is sharp for this route)")
# Thm 4.1 first claim: 3 N_odd(L) - 2 <= 3((L-1)^2+1) - 2 = 3(L-1)^2 + 1
for L in range(2, 200):
    check(3 * ((L - 1) ** 2 + 1) - 2 == 3 * (L - 1) ** 2 + 1, "", quiet=True)
check(True, "Thm 4.1: 3((L-1)^2+1)-2 == 3(L-1)^2+1 for L < 200")
# compare with [Sig] Corollary N1 lower bound floor(log_4(x+1)) + 2 (consistency, not needed)
for xi in range(4, 5000):
    x = F(xi)
    lg = 0
    while 4 ** (lg + 1) <= x + 1:
        lg += 1
    check(floorsqrt((x - 1) / 3) + 2 >= lg + 2, "", quiet=True)
check(True, "Thm 4.1 bound >= [Sig] N1 log bound at every integer A/2pi in [4,5000)")

# ---------------- Theorem 4.2(a) ----------------
# |U|+|V| = 2 max(n+g-g', n'+g'-g) and n + g - g' <= 2s + 4 with s = Area/2pi.
cnt = 0
for g in range(0, 4):
    for n in range(0, 8):
        for orders in itertools.combinations_with_replacement(range(2, 9), n):
            s = 2 * g - 2 + sum(1 - F(1, m) for m in orders)
            if s <= 0:
                continue
            for gp in range(0, 4):
                check(n + g - gp <= 2 * s + 4, f"n+g-g' <= 2s+4 fails {g},{orders},{gp}", quiet=True)
                cnt += 1
check(True, f"Thm 4.2(a): n+g-g' <= 2s+4 on {cnt} (signature, g') cases")
check(5 == 2 * (-2 + 5 * F(1, 2)) + 4, "equality case (0;2,2,2,2,2): n = 2s+4")
# evenness: |U|+|V| even and <= 4s+8 = floor(2A/pi)+8 => <= 2 floor(A/pi) + 8
for num in range(0, 4000):
    t = F(num, 37)                                      # t = A/pi
    bound_real = ffloor(2 * t) + 8
    largest_even = bound_real - (bound_real % 2)
    check(largest_even == 2 * ffloor(t) + 8, "", quiet=True)
check(True, "Thm 4.2(a): largest even integer <= floor(2A/pi)+8 equals 2 floor(A/pi)+8 (t = k/37, k < 4000)")
# without evenness the constant would be floor(2A/pi)+8, which can exceed 2floor(A/pi)+8 by 1
check(ffloor(2 * F(3, 2)) + 8 == 2 * ffloor(F(3, 2)) + 8 + 1, "evenness is genuinely used (t = 3/2)")
# worked instance with the [Sig] example (1;15) ~ (0;3,3,5,5), first two coefficients equal
m, mp, g, gp = [15], [3, 3, 5, 5], 1, 0
s1 = 2 * g - 2 + sum(1 - F(1, x) for x in m); s2 = 2 * gp - 2 + sum(1 - F(1, x) for x in mp)
U, V = m + [1], mp
check(s1 == s2 and sum(F(1, u) for u in U) == sum(F(1, v) for v in V) and sum(U) == sum(V)
      and len(V) - len(U) == 2 * (g - gp), "(1;15) vs (0;3,3,5,5): Lemma 4 (4.2) with L = 2")
t = 2 * s1
check(len(U) + len(V) <= 2 * ffloor(t) + 8, f"|U|+|V| = {len(U)+len(V)} <= 2floor(A/pi)+8 = {2*ffloor(t)+8}")
Z = U + [-v for v in V]
check(all(sum(F(z) ** j for z in Z) == sum(F(-z) ** j for z in Z) for j in (1, 2)) and sorted(Z) != sorted(-z for z in Z),
      "[Z] =_{2L-2} [-Z] for L = 2 (PTE of degree 2, size 6); so N(2) <= 6")

# ---------------- Theorem 4.2(b) ----------------
# x = (A/6 pi C)^(1/beta) >= 1: L = floor((x+3)/2) has L >= 2, 2L-3 <= x, L+1 >= x/2.
for num in range(1, 20000):
    x = F(num, 97)
    if x >= 1:
        L = ffloor((x + 3) / 2)
        check(L >= 2 and 2 * L - 3 <= x and L + 1 >= x / 2, f"(b) step at x={x}", quiet=True)
    else:
        check(x / 2 < 1, "(b) otherwise case: bound < 1/2 <= f", quiet=True)
check(True, "Thm 4.2(b): choice L = floor((x+3)/2) valid for x >= 1; for x < 1 the bound is < 1/2")
# concrete instance: N(k) <= k(k+1)/2+1 <= 2k^2 (C = 2, beta = 2), then (b) gives f >= (1/2) sqrt(A/12pi);
for k in range(1, 3000):
    check(F(k * (k + 1), 2) + 1 <= 2 * k * k, "", quiet=True)
check(True, "k(k+1)/2+1 <= 2k^2 for 1 <= k < 3000 (C = 2, beta = 2 admissible)")
for num in range(8 * 50, 200000, 7):
    t = F(num, 50)                                  # t = A/pi >= 8
    thm41 = floorsqrt((t / 2 - 1) / 3) + 2
    check(t / 48 <= thm41 ** 2, f"(b) bound <= Thm 4.1 bound at t={t}", quiet=True)
check(True, "(b) with C=2, beta=2, i.e. (1/2)sqrt(A/12pi), is <= the Thm 4.1 bound on a grid of A/pi in [8, 4000)")

# ---------------- Theorem 4.2(c) ----------------
for k in range(1, 100000):
    L = -(-k // 2) + 1
    check(2 * L - 2 >= k and L + 1 <= 3 * k and L >= 2, "", quiet=True)
check(True, "(c) =>: L = ceil(k/2)+1 has 2L-2 >= k, L >= 2 and L+1 <= 3k for 1 <= k < 1e5")
# commentary: alpha > 1/2 => 1/alpha < 2
for num in range(51, 101):
    a = F(num, 100)
    check(1 / a < 2, "", quiet=True)
check(True, "commentary: alpha in (1/2, 1] gives exponent 1/alpha = 2 - eps with eps = 2 - 1/alpha > 0")

# ---------------- Theorem 4.3 ----------------
# f_g >= L+1 if A >= 8 pi N(2L-3); N(2L-3) <= 2L^2-5L+4.  Claim: f_g(A) >= sqrt(A/(16 pi)) for A >= 16 pi.
# f_n >= L+1 if A >= 2 pi (3N(2L-3)-2).          Claim: f_n(A) >= sqrt(A/(12 pi)) for A >= 8 pi.
for L in range(2, 10 ** 4):
    check((2 * L - 3) * (2 * L - 2) // 2 + 1 == 2 * L * L - 5 * L + 4, "", quiet=True)
check(True, "N(2L-3) <= (2L-3)(2L-2)/2 + 1 == 2L^2-5L+4 for 2 <= L < 1e4")
for num in range(8 * 40, 400000, 3):
    t = F(num, 40)
    if t >= 16:
        L = max(2, floorsqrt(t / 16))
        check(8 * (2 * L * L - 5 * L + 4) <= t and (L + 1) ** 2 >= t / 16, f"f_g at t={t}", quiet=True)
    L = max(2, floorsqrt(t / 12))
    check(2 * (3 * (2 * L * L - 5 * L + 4) - 2) <= t and (L + 1) ** 2 >= t / 12, f"f_n at t={t}", quiet=True)
check(True, "Thm 4.3: f_g(A) >= sqrt(A/16pi) for A >= 16pi and f_n(A) >= sqrt(A/12pi) for A >= 8pi (grid of A/pi up to 1e4)")
check(8 * 2 == 16 and 2 * (3 * 2 - 2) == 8, "thresholds at L = 2 (N(1) = 2): f_g >= 3 from A >= 16pi, f_n >= 3 from A >= 8pi")

print()
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("ALL CHECKS PASSED")
