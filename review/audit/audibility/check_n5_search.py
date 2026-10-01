"""AU.1 Thm C(3) / AU.4: exhaustive n=5 search for distinct integer multisets sharing I_4=(R,P1,P3,P5).

The heavy enumeration is done by n5_search.c (pure integer arithmetic). It is first validated
against an independent pure-Python brute force (Fractions) at N=22, then run at N=60 and N=120.
Multiset counts are compared with the closed form C(N+3,5).
"""
import os
import subprocess
import sys
import tempfile
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
tmp = tempfile.mkdtemp()
exe = os.path.join(tmp, "n5_search")
subprocess.run(["cc", "-O2", "-o", exe, os.path.join(HERE, "n5_search.c")], check=True)


def run(N):
    out = subprocess.run([exe, str(N)], check=True, capture_output=True, text=True).stdout
    last = out.strip().splitlines()[-1]
    kv = dict(x.split("=") for x in last.split()[0:])
    return out, {k: int(v) for k, v in kv.items()}


def brute(N):
    g3 = defaultdict(list)
    tot = 0
    for ms in combinations_with_replacement(range(2, N + 1), 5):
        tot += 1
        key3 = (sum(F(1, x) for x in ms), sum(ms), sum(x ** 3 for x in ms))
        g3[key3].append(ms)
    c3 = sum(1 for v in g3.values() if len(v) > 1)
    c4 = 0
    for v in g3.values():
        p5 = defaultdict(int)
        for ms in v:
            p5[sum(x ** 5 for x in ms)] += 1
        c4 += sum(c - 1 for c in p5.values() if c > 1)
    return tot, c3, c4


NV = 22
tot, c3, c4 = brute(NV)
_, r = run(NV)
print(f"validation N={NV}: python total={tot} I3classes={c3} I4pairs={c4}; C: {r}")
assert (r["total"], r["I3_collision_classes"], r["I4_collision_pairs"]) == (tot, c3, c4)
assert c3 > 0, "control: I_3 collisions must exist, else the search is insensitive"

for N, claimed in ((60, 7028847), (120, 216071394)):
    out, r = run(N)
    print(out.strip())
    assert r["N"] == N
    assert r["total"] == comb(N + 3, 5) == claimed, (r, comb(N + 3, 5))
    assert r["I3_collision_classes"] > 0
    assert r["I4_collision_pairs"] == 0
    print(f"N={N}: {r['total']} multisets = C({N+3},5) = claimed {claimed}; "
          f"{r['I3_collision_classes']} classes share I_3; none share I_4")
print("ALL CHECKS PASSED")
