#!/usr/bin/env python3
"""G5-bis pte-growth: Lemma 1.5 (N_odd) checks.  Exact integer arithmetic only.

(1) Lemma 1.5(3) upper bounds N_odd(L) <= L for L = 3..6: witnesses
    - L = 3, 4: own exhaustive search (smallest max element);
    - L = 5: own exhaustive search up to a bound (streamed by P_1);
    - L = 5, 6: the eslpower.org table (sources/eslpower_eslp.htm, sections
      "( k = 1, 3, 5, 7 )" and "( k = 1, 3, 5, 7, 9 )"), re-verified exactly.
(2) Lower bound N_odd(L) >= L: the symmetric-multiset lemma ("[Sig] Lemma 5") checked
    exhaustively on small boxes, and N_odd(L) > L-1 checked by exhaustive search for L=2,3,4
    in a box (the proof in REVIEW.md covers all L).
(3) L = 2: N_odd(2) = 2.
(4) Lemma 1.5(2) pigeonhole: exact inequality C(M+n-1,n) > prod_j (n(M^j-1)+1) with
    n = (L-1)^2+1, M = n! n^(L-1), for L = 2..9; and brute force N_odd(L) <= (L-1)^2+1 for L=2,3.
"""
import itertools, math, sys, time
from fractions import Fraction
from collections import defaultdict

def odd_exps(L):
    return list(range(1, 2 * L - 2, 2))          # 1,3,...,2L-3

def psums(ms, exps):
    return tuple(sum(m ** j for m in ms) for j in exps)

def is_witness(X, Y, L):
    X, Y = sorted(X), sorted(Y)
    return (len(X) == len(Y) and X != Y and min(X + Y) >= 1
            and psums(X, odd_exps(L)) == psums(Y, odd_exps(L)))

def first_collision(n, L, B):
    """Exhaustive: all n-multisets of {1..B}; return the collision with smallest max, or None."""
    seen = {}
    best = None
    for ms in itertools.combinations_with_replacement(range(1, B + 1), n):
        key = psums(ms, odd_exps(L))
        if key in seen:
            cand = (seen[key], ms)
            if best is None or max(cand[1]) < max(best[1]):
                best = cand
            # combinations come in lexicographic order; keep scanning (cheap)
        else:
            seen[key] = ms
    return best

def collisions_by_sum(n, L, B, tcap):
    """Stream by P_1 to save memory; return first collision found (smallest P_1)."""
    t0 = time.time()
    exps = odd_exps(L)
    def parts(s, k, lo, hi):
        if k == 0:
            if s == 0:
                yield ()
            return
        for a in range(lo, min(hi, s // k) + 1):
            if a * k > s:
                break
            for rest in parts(s - a, k - 1, a, hi):
                yield (a,) + rest
    for s in range(n, n * B + 1):
        seen = {}
        for ms in parts(s, n, 1, B):
            key = psums(ms, exps[1:])
            if key in seen:
                return seen[key], ms, s
            seen[key] = ms
        if time.time() - t0 > tcap:
            return None, None, s
    return None, None, None

fails = 0
def check(cond, msg):
    global fails
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        fails += 1

print("== (3) L = 2")
check(is_witness([1, 4], [2, 3], 2), "N_odd(2) <= 2 : [1,4] vs [2,3], P_1 = 5")
# n=1 impossible: distinct singletons have distinct P_1
check(True, "N_odd(2) >= 2 trivially (distinct singletons differ in P_1)")

print("== (1) own exhaustive searches, size n = L")
for L, B in [(3, 20), (4, 30)]:
    res = first_collision(L, L, B)
    check(res is not None and is_witness(res[0], res[1], L),
          f"L={L}: own search n={L}, entries <= {B}: {res}")

res = collisions_by_sum(5, 5, 60, tcap=240)
if res[0] is not None:
    check(is_witness(res[0], res[1], 5), f"L=5: own search (streamed by P_1) n=5: {res[0]} vs {res[1]}, P_1={res[2]}")
else:
    print(f"INFO L=5 own search stopped at P_1={res[2]} without a hit (time cap); fetched witness used")

print("== (1) fetched witnesses (eslpower.org eslp.htm), re-verified exactly")
fetched = {
    3: ([2, 10, 12], [3, 8, 13]),                       # "( k = 1, 3 )" line 'Smallest solution' list
    4: ([1, 13, 17, 23], [3, 9, 21, 21]),                # "( k = 1, 3, 5 )"
    5: ([3, 19, 37, 51, 53], [9, 11, 43, 45, 55]),       # "( k = 1, 3, 5, 7 )"
    6: ([7, 91, 173, 269, 289, 323], [29, 59, 193, 247, 311, 313]),  # "( k = 1, 3, 5, 7, 9 )"
}
for L, (X, Y) in fetched.items():
    check(is_witness(X, Y, L), f"L={L}: {X} vs {Y}: odd sums j<= {2*L-3} equal: {psums(X, odd_exps(L))}")
    # next odd exponent differs (so it is not a degree-(2L-1) solution); informational
    j = 2 * L - 1
    print(f"     P_{j}: {sum(x**j for x in X)} vs {sum(y**j for y in Y)}")

print("== (2) lower bound: symmetric lemma, exhaustive on boxes")
def sym_lemma_box(L, B):
    vals = [v for v in range(-B, B + 1) if v != 0]
    cnt = 0
    for m in range(1, 2 * L - 1):            # sizes 1..2L-2
        for ms in itertools.combinations_with_replacement(vals, m):
            if all(sum(x ** j for x in ms) == 0 for j in odd_exps(L)):
                cnt += 1
                if sorted(ms) != sorted(-x for x in ms):
                    return False, ms
    return True, cnt
for L, B in [(2, 12), (3, 7), (4, 4)]:
    ok, info = sym_lemma_box(L, B)
    check(ok, f"L={L}: every multiset of size <= {2*L-2} in [-{B},{B}]\\0 with odd sums j<= {2*L-3} zero is symmetric ({info} such multisets)")

for L, B in [(2, 60), (3, 40), (4, 25)]:
    res = first_collision(L - 1, L, B)
    check(res is None, f"L={L}: no pair of distinct {L-1}-multisets in [1,{B}] with equal odd sums (consistent with N_odd(L) >= L)")

print("== (4) pigeonhole")
for L in range(2, 10):
    n = (L - 1) ** 2 + 1
    M = math.factorial(n) * n ** (L - 1)      # M = n! n^(L-1) already suffices (strict count)
    count = math.comb(M + n - 1, n)
    values = 1
    for j in odd_exps(L):
        values *= n * (M ** j - 1) + 1          # P_j ranges over [n, n M^j]
    check(count > values, f"L={L}: n={n}, M=n!n^(L-1): #multisets > #power-sum vectors")
    check(sum(odd_exps(L)) == (L - 1) ** 2, f"L={L}: sum of odd j <= 2L-3 is (L-1)^2")
    check(math.comb(M + n - 1, n) * math.factorial(n) >= M ** n, f"L={L}: C(M+n-1,n) >= M^n/n!")
# brute force: N_odd(L) <= (L-1)^2+1 for L = 2, 3 (we exhibit size-L, hence also size-((L-1)^2+1) by padding equal elements)
for L in (2, 3):
    n = (L - 1) ** 2 + 1
    res = first_collision(n, L, 12)
    check(res is not None, f"L={L}: a collision of size (L-1)^2+1 = {n} exists in [1,12]: {res}")

print()
if fails:
    print(f"FAILURES: {fails}")
    sys.exit(1)
print("ALL CHECKS PASSED")
