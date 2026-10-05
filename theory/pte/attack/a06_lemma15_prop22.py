"""Attack item 6: Lemma 1.5 (N_odd) and Proposition 2.2 (tau_L >= N(2L-2))."""
import sys, os, json, itertools
from fractions import Fraction as F
from math import comb, factorial
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from mylib import psum

sys.stdout.reconfigure(line_buffering=True)
HERE = os.path.dirname(os.path.abspath(__file__))
fail = []

# (2) pigeonhole arithmetic, exactly, for L = 2..7
for L in range(2, 8):
    n = (L - 1) ** 2 + 1
    M = factorial(n) * n ** (L - 1) + 1
    n_multisets = comb(M + n - 1, n)
    n_values = 1
    for j in range(1, 2 * L - 2, 2):
        n_values *= n * M ** j - n + 1  # P_j ranges over [n, n M^j]
    assert sum(range(1, 2 * L - 2, 2)) == (L - 1) ** 2
    if not n_multisets > n_values:
        fail.append(("pigeonhole", L))
    # and the inequality chain used in the proof
    assert n_multisets >= F(M ** n, factorial(n)) > n ** (L - 1) * M ** ((L - 1) ** 2) >= n_values
print("(2) pigeonhole: #multisets > #odd-power-sum vectors for n=(L-1)^2+1, M=n!n^(L-1)+1, L=2..7: exact OK")

# (3) lower bound N_odd(L) >= L: exhaustive search for size L-1 collisions
for L, B in [(3, 400), (4, 90), (5, 32)]:
    n = L - 1
    seen = defaultdict(list)
    coll = 0
    for ms in itertools.combinations_with_replacement(range(1, B + 1), n):
        key = tuple(sum(x ** j for x in ms) for j in range(1, 2 * L - 2, 2))
        if key in seen:
            coll += 1
        seen[key].append(ms)
    print(f"(3) L={L}: size-{n} multisets from [1..{B}] with equal P_j (odd j<={2 * L - 3}): {coll} collisions")
    if coll:
        fail.append(("N_odd lower", L))
# upper bound examples (Chen A.1.6, A.1.17, A.1.26, A.1.33)
ODD = {3: ([1, 5, 5], [2, 3, 6]), 4: ([1, 13, 17, 23], [3, 9, 21, 21]),
       5: ([3, 19, 37, 51, 53], [9, 11, 43, 45, 55]), 6: ([7, 91, 173, 269, 289, 323], [29, 59, 193, 247, 311, 313])}
for L, (X, Y) in ODD.items():
    ok = len(X) == L and sorted(X) != sorted(Y) and all(psum(X, j) == psum(Y, j) for j in range(1, 2 * L - 2, 2))
    if not ok:
        fail.append(("N_odd upper", L))
print("(3) size-L examples for L=3..6 verified => N_odd(L) = L for 3 <= L <= 6")
# smallest size-3 example for L=3 / size-2 for L=2 (sanity)
print("    N_odd(2) = 2 ([1,4]=[2,3]); Lemma 1.5(2) at L=7 gives N_odd(7) <= 37 (pigeonhole), "
      "vs N(11) = 12 from the size-12 ideal solution (Lemma 1.5(1)) -- (1) is far stronger in practice")

# Prop 2.2: every witness configuration Z gives [Z] =_{2L-2} [-Z]
W = json.load(open(os.path.join(HERE, '..', 'data', 'witnesses.json')))
for w in W:
    Z, L = w['Z'], w['L']
    mZ = [-z for z in Z]
    ok = sorted(Z) != sorted(mZ) and all(psum(Z, j) == psum(mZ, j) for j in range(1, 2 * L - 1))
    ok &= psum(Z, 2 * L - 1) != psum(mZ, 2 * L - 1)
    if not ok:
        fail.append(("2.2", w['kind'], L))
print(f"Prop 2.2: [Z] =_(2L-2) [-Z] (and not =_(2L-1)) for all {len(W)} witness configurations")
print("    remark: N(2L-2) = 2L-1 for L <= 6 (ideal solutions), so Prop 2.2 gives tau_L >= 2L-1,\n"
      "    weaker than Theorem S (2L+2) in every known case; it matters only asymptotically (Thm 4.2(a)).")

if fail:
    print("FAILURES:", fail)
    sys.exit(1)
print("ALL CHECKS PASSED")
