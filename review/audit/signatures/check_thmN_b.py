"""Theorem N(b) (SG.10 / thm:signonuniform (b)) and the Egyptian-fraction step.

Referee's construction (D = 2k-2, eps_i = (-1)^{t(i)}, x_i = i+1, i < 2^D), for a list of
unit fractions 1/p_1 + ... + 1/p_r = 1 with all p_j >= 2:
   U = {x_i : eps_i = +1}  +  sum_j {p_j x_i : eps_i = -1}
   V = {x_i : eps_i = -1}  +  sum_j {p_j x_i : eps_i = +1}
For odd j >= 1: P_j(U) - P_j(V) = (1 - sum_j p_j^j) M_j = 0 for j < D (Prouhet);
for j = -1:     R(U) - R(V)     = (1 - sum_j 1/p_j) M_{-1} = 0.
Exactly one 1 (from i = 0, in U); |U| = |V|; O = (0; U minus {1}), O' = (0; V).
Variants checked: (2,2) [no Egyptian step needed: 1 = 1/2 + 1/2], (2,3,6) [distinct].
Shared coefficients computed with actual cone coefficients b_l: exactly k.

Also checks the Egyptian-fraction lemma: every positive rational q is a finite sum of
DISTINCT unit fractions with denominators >= 2 (harmonic start + Fibonacci-Sylvester greedy),
including q >= 1 and large q, and that the plain greedy algorithm returns denominator 1 for q >= 1.
"""
import os
import sys
import time
from fractions import Fraction
from math import ceil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sigcommon import thue_morse, shared_count, s_of  # noqa: E402

F = Fraction


def egyptian_distinct(q):
    assert q > 0
    out = []
    p = 2
    while F(1, p) <= q:          # harmonic start: 1/2 + 1/3 + ... while it fits
        q -= F(1, p)
        out.append(p)
        p += 1
    while q > 0:                 # greedy on the remainder q < 1/p: denominators > previous
        d = ceil(1 / q)
        assert d >= p
        out.append(d)
        q -= F(1, d)
        p = d + 1
    return out


def greedy_plain(q):
    out = []
    while q > 0:
        d = ceil(1 / q)
        out.append(d)
        q -= F(1, d)
    return out


tests = [F(1), F(2), F(3), F(7, 2), F(1, 2), F(5, 6), F(4, 13), F(100, 37), F(4, 1), F(5, 2), F(999, 1000),
         F(1, 1), F(3, 7), F(7, 15), F(22, 7)]
for q in tests:
    e = egyptian_distinct(q)
    assert sum(F(1, d) for d in e) == q and len(set(e)) == len(e) and min(e) >= 2, (q, e)
assert greedy_plain(F(1)) == [1] and greedy_plain(F(7, 2))[0] == 1
print("Egyptian lemma (distinct, >= 2) on", len(tests), "rationals incl. q >= 1 and q up to 4 (q = 4: 98 terms, largest denominator ~473000 bits): OK")
print("  e.g. 1 =", " + ".join(f"1/{d}" for d in egyptian_distinct(F(1))),
      "; plain greedy for q >= 1 starts with 1/1 (forbidden)")


def build(k, ps):
    D = 2 * k - 2
    U, V = [], []
    for i in range(2 ** D):
        x = i + 1
        plus = not thue_morse(i)
        (U if plus else V).append(x)
        for p in ps:
            (V if plus else U).append(p * x)
    return U, V


for ps in [(2, 2), (2, 3, 6)]:
    assert sum(F(1, p) for p in ps) == 1 and min(ps) >= 2
    for k in range(2, 8):
        t0 = time.time()
        U, V = build(k, ps)
        assert len(U) == len(V)
        assert U.count(1) == 1 and V.count(1) == 0
        m = [x for x in U if x != 1]
        assert min(m) >= 2 and min(V) >= 2
        n = len(m)
        assert len(V) == n + 1
        sO, sO2 = s_of(0, m), s_of(0, V)
        assert sO == sO2 and sO > 0
        sc = shared_count(0, m, 0, V, cap=k + 1)
        assert sc == k, (k, ps, sc)
        print(f"p={ps} k={k}: genus 0, n={n} vs n+1={n + 1}, Area/2pi={float(sO):.3f}, "
              f"shared exactly {sc} (full b_l)  ({time.time() - t0:.1f}s)", flush=True)

# smallest instances (for the record): k=2 with (2,2)
U, V = build(2, (2, 2))
print("k=2 example: O = (0;", sorted(x for x in U if x != 1), ")  O' = (0;", sorted(V), ")")
print("ALL CHECKS PASSED")
