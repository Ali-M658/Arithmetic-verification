#!/usr/bin/env python3
"""Phase-2 comparison checks (read-only use of paper/main.tex and theory/threshold/proof.md
statements).  Exact arithmetic; exits nonzero on failure.

1. tab:enum of paper/main.tex parsed entry by entry and compared with the referee listing.
2. Identities used in the existing proof of Theorem 1 / Prop 3 (theory/threshold/proof.md):
   quadratic and discriminant in (a), the gap at 3p+7 in (c), the S*+1 fractions in (d),
   the p=2 bound in Lemma 1, x*-18.
3. The odd-parity monotonicity claim of (b): exact sweep, plus the symbolic reason.
4. The S = 3p+2 formal tangency (qualifier for Prop 3(1)).
"""
import os
import re
import sys
from fractions import Fraction as Fr
import sympy as sp

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
FAIL = []


def check(c, m):
    print(("PASS " if c else "FAIL ") + m)
    if not c:
        FAIL.append(m)


# ---------------------------------------------------------------- 1. tab:enum
tex = open(os.path.join(ROOT, "paper", "main.tex")).read()
blk = tex[tex.index(r"\label{tab:enum}"):tex.index(r"\end{longtable}")]
rows = []
curS = None
for line in blk.splitlines():
    m = re.match(r"\s*(\d+)?\s*&\s*(?:\\textbf\{)?\$\((\d+),(\d+),(\d+)\)\$\}?\s*&\s*(?:\\textbf\{)?\$(\d+)/(\d+)\$\}?\s*&\s*(?:\\textbf\{)?(\w+)", line)
    if m:
        if m.group(1):
            curS = int(m.group(1))
        p, q, r = map(int, m.group(2, 3, 4))
        rows.append((curS, (p, q, r), Fr(int(m.group(5)), int(m.group(6))), m.group(7)))
mine = []
for S in range(10, 19):
    for p in range(2, S // 3 + 1):
        for q in range(p, (S - p) // 2 + 1):
            r = S - p - q
            if p * q + q * r + r * p < p * q * r:
                mine.append((S, (p, q, r), Fr(p * q + q * r + r * p, p * q * r)))
print(f"tab:enum rows parsed: {len(rows)}; referee triads: {len(mine)}")
check(len(rows) == len(mine) == 83, "same number of entries (83)")
check([(a, b) for a, b, _, _ in rows] == [(a, b) for a, b, _ in mine], "same triads, same order")
bad = [(a, b, c, d) for (a, b, c, _), (_, _, d) in zip(rows, mine) if c != d]
check(not bad, f"every R value agrees exactly {bad}")
check(all(r[1] == (p, q, S - p - q) and sum(r[1]) == r[0] for r, (S, (p, q, _), _) in zip(rows, mine)), "row sums = S")
status_ok = all((st == "collision") == (S == 18 and t in ((2, 8, 8), (3, 3, 12))) for S, t, _, st in rows)
check(status_ok, "status column: 'collision' exactly for (2,8,8),(3,3,12)")
for S in range(10, 19):
    Rs = [R for s, _, R, _ in rows if s == S]
    if S <= 17:
        assert len(set(Rs)) == len(Rs)
check(True, "R distinct within each sum S<=17 (table values)")
# cross-sum equal R values in the table (not collisions, but worth noting)
from collections import defaultdict
byR = defaultdict(list)
for S, t, R, _ in rows:
    byR[R].append((S, t))
print("   equal R across different sums (not collisions):", sum(1 for v in byR.values() if len(v) > 1), "values")

# ---------------------------------------------------------------- 2. existing-proof identities
p, S = sp.symbols("p S")
phi = 4 / (S - p) - 1 / (S - 2 * p - 2)
tau = (p - 1) / (p * (p + 1))
quad = (p - 1) * S ** 2 - (6 * p ** 2 + 2 * p - 2) * S + 3 * p * (p + 1) * (3 * p + 2)
xs = 3 * p * (p + 1) / (p - 1)
check(sp.expand(sp.discriminant(quad, S) - 4 * (2 * p + 1) ** 2 * (p - 1) ** 0) == 0 or
      sp.simplify(sp.discriminant(quad, S) / (4 * (2 * p + 1) ** 2)) == 1, "(a) discriminant 4(2p+1)^2")
check(sp.simplify(phi - tau + (p - 1) * (S - 3 * p - 2) * (S - xs) / (p * (p + 1) * (S - p) * (S - 2 * p - 2))) == 0,
      "(a) phi-tau = -(p-1)(S-3p-2)(S-x*)/(p(p+1)(S-p)(S-2p-2))")
g37 = 1 / p + 1 / (p + 3) + 1 / (p + 4) - 2 / (p + 1) - 1 / (p + 5)
check(sp.simplify(g37 + 2 * (p ** 2 - 5 * p - 30) / (p * (p + 1) * (p + 3) * (p + 4) * (p + 5))) == 0, "(c) gap at 3p+7")
u = sp.symbols("u")
check(sp.expand((p ** 2 - 5 * p - 30).subs(p, 9 + u) - (u ** 2 + 13 * u + 6)) == 0, "(c) p=9+u: u^2+13u+6")
check(sp.simplify(sp.diff(phi, S) * (S - p) ** 2 * (S - 2 * p - 2) ** 2 + (S - 3 * p - 4) * (3 * S - 5 * p - 4)) == 0,
      "(b) numerator of phi' = -(S-3p-4)(3S-5p-4)")


def gap(pp, SS):
    D = SS - pp
    return Fr(1, pp) + Fr(1, D // 2) + Fr(1, D - D // 2) - Fr(2, pp + 1) - Fr(1, SS - 2 * pp - 2)


Sst = {2: 18, 3: 19, 4: 20, 5: 23, 6: 26, 7: 29, 8: 32}
claimed = [Fr(-7, 936), Fr(-1, 72), Fr(-19, 3960), Fr(-1, 180), Fr(-76, 15015), Fr(-1, 231), Fr(-17, 4680)]
mineS1 = [gap(pp, Sst[pp] + 1) for pp in range(2, 9)]
print("   gap(S*+1), p=2..8:", mineS1)
check(mineS1 == claimed, "(d) the seven gap(S*+1) fractions")
check(gap(3, 18) == Fr(1, 840) and gap(7, 28) == Fr(1, 2310) and gap(8, 31) == Fr(1, 10296), "(d) odd-sum gaps 1/840, 1/2310, 1/10296")
check(Fr(101, 168) - Fr(3, 5) == Fr(1, 840) and Fr(257, 770) == Fr(1, 3) + Fr(1, 2310), "(d) displayed differences")
check(Fr(1, 7) + Fr(1, 10) + Fr(1, 11) == Fr(257, 770), "R^-_{28,7} = 257/770")
check(sp.simplify(xs - 18 - 3 * (p - 2) * (p - 3) / (p - 1)) == 0, "Cor 2: x*-18 = 3(p-2)(p-3)/(p-1)")
# Lemma 1, p=2: R^-_{S,3} <= 1/3 + 4(S-3)/((S-3)^2-1), decreasing, at 18: 1/3+60/224 < 7/10
check(Fr(1, 3) + Fr(60, 224) < Fr(7, 10), "Lemma 1 (p=2): 1/3+60/224 < 7/10")
check(all(Fr(1, 3) + Fr(4 * (s - 3), (s - 3) ** 2 - 1) >= Fr(1, 3) + Fr(4 * (s - 2), (s - 2) ** 2 - 1) for s in range(18, 3000)),
      "Lemma 1 (p=2): bound decreasing in S")
check(all((Fr(1, 2) + Fr(1, 5) + Fr(1, s - 7) < 1) for s in range(18, 3000)), "(2,5,S-7) hyperbolic for S>=18")

# ---------------------------------------------------------------- 3. odd-parity monotonicity
# real-variable odd gap h(S) = phi - tau + 4/(D(D^2-1)), D = S-p
D = S - p
h = phi - tau + 4 / (D * (D ** 2 - 1))
corr_d = sp.diff(4 / (D * (D ** 2 - 1)), S)
check(sp.simplify(corr_d + 4 * (3 * D ** 2 - 1) / (D ** 2 * (D ** 2 - 1) ** 2)) == 0, "correction 4/(D(D^2-1)) has derivative -4(3D^2-1)/(D^2(D^2-1)^2) < 0")
ok = True
for pp in range(2, 400):
    # all odd-D sums from 3p+3 to 3p+400: strictly decreasing for S >= x*, and in fact for S > 3p+4
    odd = [s for s in range(3 * pp + 3, 3 * pp + 400) if (s - pp) % 2 == 1]
    vals = [gap(pp, s) for s in odd]
    ok &= all(vals[i] > vals[i + 1] for i in range(len(vals) - 1) if odd[i] >= 3 * pp + 4)
check(ok, "odd-parity gap strictly decreasing over consecutive odd-D sums S>=3p+4, 2<=p<400 (exact sweep)")
# bottom of the range: gap(3p+3) = gap(3p+5) exactly for every p (no strict decrease there)
check(all(gap(pp, 3 * pp + 3) == gap(pp, 3 * pp + 5) for pp in range(2, 2000)),
      "gap(3p+3) = gap(3p+5) for every p: the odd gap is NOT strictly decreasing on all of S>=3p+3")
check(sp.simplify((1 / p + 1 / (p + 1) + 1 / (p + 2) - 3 / (p + 1)) - (1 / p + 1 / (p + 2) - 2 / (p + 1))) == 0,
      "symbolic: gap(3p+3) - gap(3p+5) = 0")
check(all(Fr(3 * pp * (pp + 1), pp - 1) > 3 * pp + 5 for pp in range(2, 5000)), "x*(p) > 3p+5, so the claim restricted to S>=x* is unaffected")

# ---------------------------------------------------------------- 4. S = 3p+2
ok = True
for pp in range(2, 2000):
    SS = 3 * pp + 2
    bal = (pp, pp + 1, pp + 1)            # balanced triad of stratum p at S=3p+2
    spr = (pp + 1, pp + 1, SS - 2 * pp - 2)  # formal 'spread triad of stratum p+1'
    ok &= sorted(spr) == list(bal) and gap(pp, SS) == 0
check(ok, "S=3p+2: formal gap 0 for every p, the two 'triads' coincide ((p+1,p+1,p)); stratum p+1 empty there")
print("   paper/proof.md statement of Prop 3(1) omits S>=3p+3; the proof uses it implicitly (root 3p+2 excluded in (a)).")

print()
if FAIL:
    print(f"{len(FAIL)} FAILURE(S):", *FAIL, sep="\n  ")
    sys.exit(1)
print("ALL COMPARISON CHECKS PASSED")
