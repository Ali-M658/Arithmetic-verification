"""Searches behind the genus witnesses at L = 4, 5 (proof.md section 5).

Imbalanced piece: an even ideal symmetric solution {±a} =_{2m-1} {±b} (from enum_sym6.c / enum_sym8.c,
data/sym6_400.txt: all 19,450 size-6 solutions with entries <= 400; data/sym8_140.txt: all 43 size-8
solutions with entries <= 140; each re-verified here), shifted by every half-sum c = -(x+x')/2 of two
elements of one side, with cancelling pairs removed.
Balanced piece:
  L = 4: every (1,3,5) odd-power equality of size 4 with entries <= 60 (computed here);
  L = 5: the (1,3,5,7) equality [3,19,37,51,53] = [9,11,43,45,55] and every balanced shifted piece of
         size <= 14 from the size-8 list.
Z = P u t B with t fixing s_{-1}; report the least |Z| with iota != 0.
Usage: python3 genus_search.py 4   (about 20 min)   |   python3 genus_search.py 5   (about 10 min)
Logs of the runs: data/genus_search_L4_log.txt, data/genus_search_L5_log.txt.
"""
import itertools
import os
import sys
import time
from collections import defaultdict
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pte_common import cancel, iota, is_config, normalize, pm  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
L = int(sys.argv[1])
half = {4: 3, 5: 4}[L]
pairs = [tuple(map(int, line.split())) for line in open(os.path.join(HERE, "data", {4: "sym6_400.txt", 5: "sym8_140.txt"}[L]))]
for v in pairs:
    a, b = v[:half], v[half:]
    assert all(sum(x ** (2 * j) for x in a) == sum(x ** (2 * j) for x in b) for j in range(1, half)) and not set(a) & set(b)
Bs = []
if L == 4:
    d = defaultdict(list)
    for q in itertools.combinations_with_replacement(range(1, 61), 4):
        d[(sum(q), sum(x ** 3 for x in q), sum(x ** 5 for x in q))].append(q)
    for lst in d.values():
        for a, b in itertools.combinations(lst, 2):
            if not set(a) & set(b):
                Bs.append([F(x) for x in a] + [-F(y) for y in b])
else:
    Bs.append([F(x) for x in (3, 19, 37, 51, 53)] + [-F(y) for y in (9, 11, 43, 45, 55)])
Ps = []
for v in pairs:
    X, Y = pm(v[:half]), pm(v[half:])
    hs = {F(0)}
    for S in (X, Y):
        for a, b in itertools.combinations_with_replacement(S, 2):
            hs.add(-F(a + b, 2))
    for c in hs:
        P = [F(x) + c for x in X] + [-(F(y) + c) for y in Y]
        if 0 in P:
            continue
        P = cancel(P)
        if not P:
            continue
        if iota(P) == 0:
            if L == 5 and len(P) <= 14:
                Bs.append(P)
        else:
            Ps.append((len(P), P, v, c))
print(f"L={L}: {len(pairs)} PTE solutions, {len(Ps)} imbalanced pieces, {len(Bs)} balanced pieces", flush=True)
Ps.sort(key=lambda t: t[0])
best = (10 ** 9, None)
t0 = time.time()
for i, (n, P, v, c) in enumerate(Ps):
    if n >= best[0] + 8:
        break
    rP = sum(1 / p for p in P)
    for B in Bs:
        rB = sum(1 / b for b in B)
        if rB == 0 or rP == 0:
            continue
        Z = cancel(P + [(-rB / rP) * b for b in B])
        if Z and iota(Z) != 0 and len(Z) < best[0]:
            assert is_config(Z, L)
            best = (len(Z), normalize(Z), v, c)
            print("new best", best[0], v, c, flush=True)
    if i % 2000 == 0:
        print("progress", i, f"{time.time() - t0:.0f}s", "best", best[0], flush=True)
print("FINAL", best[0], best[2], best[3])
assert best[0] == {4: 16, 5: 20}[L]
print("ALL CHECKS PASSED")
