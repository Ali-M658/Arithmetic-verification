"""Attack items 7-8: Theorem 4.1 vs [Sig] Cor. N1, Theorem 4.2(a)-(c) inequalities, Theorem 4.3 thresholds.
All comparisons exact (integers / Fractions); x = A/2pi."""
import sys, os, json
from fractions import Fraction as F
from math import isqrt
sys.path.insert(0, os.path.dirname(__file__))
from mylib import area, sig_to_config

sys.stdout.reconfigure(line_buffering=True)
HERE = os.path.dirname(os.path.abspath(__file__))
fail = []


def new(x):  # floor(sqrt((x-1)/3)) + 2, exact for rational x >= 1
    y = F(x - 1, 3)
    r = isqrt(y.numerator // y.denominator)
    while (r + 1) ** 2 <= y:
        r += 1
    while r * r > y:
        r -= 1
    return r + 2


def old(x):  # floor(log_4(x+1)) + 2
    k = 0
    while 4 ** (k + 1) <= x + 1:
        k += 1
    return k + 2


# breakpoints of both step functions in [4, 10^6]
X = 10 ** 6
bps = {F(4)}
k = 1
while 3 * k * k + 1 <= X:
    bps.add(F(3 * k * k + 1)); k += 1
k = 1
while 4 ** k - 1 <= X:
    bps.add(F(4 ** k - 1)); k += 1
bps = sorted(b for b in bps if b >= 4)
pts = []
for b in bps:
    pts += [b, b - F(1, 10 ** 9)]
pts = sorted(p for p in pts if p >= 4)
less = [p for p in pts if new(p) < old(p)]
greater = [p for p in pts if new(p) > old(p)]
# intervals where new > old
iv = []
for p in pts:
    if new(p) > old(p):
        if iv and iv[-1][1] == 'open':
            continue
        iv.append([p, 'open'])
    else:
        if iv and iv[-1][1] == 'open':
            iv[-1][1] = p
print(f"Thm 4.1 bound vs Cor. N1 on [4, 1e6] ({len(bps)} breakpoints): new < old at {len(less)} points")
print("  first intervals where new > old:", [(str(a), str(b)) for a, b in iv[:3]])
if less:
    fail.append("new < old somewhere")
strict_from_28 = all(new(p) > old(p) for p in pts if p >= 28)
print(f"  strictly larger for every x >= 28: {strict_from_28}")
agree_4_28 = all(new(p) == old(p) for p in pts if 4 <= p < 28)
x0 = F(13)
print(f"  claim '(the two agree on [4,28))': {agree_4_28};  e.g. x = 13: new = {new(x0)}, old = {old(x0)}; "
      f"x = 14.9: new = {new(F(149, 10))}, old = {old(F(149, 10))}")
BROKEN_AGREE = not agree_4_28

# Theorem 4.1 internal: L largest with 3(L-1)^2+1 <= x gives pair of area < 2pi(3((L-1)^2+1)-2) <= A
for x in range(4, 5000):
    L = new(F(x)) - 1
    assert 3 * (L - 1) ** 2 + 1 <= x < 3 * L ** 2 + 1
    assert 3 * ((L - 1) ** 2 + 1) - 2 == 3 * (L - 1) ** 2 + 1
print("Thm 4.1: L = floor(sqrt((x-1)/3)) + 1 is the largest L with 3(L-1)^2+1 <= x, and 3N_odd-2 <= 3(L-1)^2+1: OK")

# Theorem 4.2(b) with the known N(k) <= k(k+1)/2 + 1 <= 2 k^2 (C=2, beta=2), and a few other (C, beta)
import math
for C, beta in [(2, 2), (1, 2), (3, 1.5), (5, 1)]:
    worst = None
    for xi in [4 + i / 7 for i in range(0, 7 * 3000)]:
        A = 2 * math.pi * xi
        claimed = 0.5 * (A / (6 * math.pi * C)) ** (1 / beta)
        # delivered: Thm 4.1 under N_odd(L) <= C(2L)^beta (valid once N(k)<=Ck^beta), plus Cor. N1 fallback
        L = 1
        while 6 * math.pi * C * (2 * (L + 1)) ** beta <= A:
            L += 1
        deliv = max(old(F(round(xi * 7), 7)), L + 1 if L >= 2 else 0)
        if deliv < claimed:
            fail.append(("4.2b", C, beta, xi))
        worst = claimed / deliv if worst is None else max(worst, claimed / deliv)
    print(f"Thm 4.2(b) C={C}, beta={beta}: claimed bound <= delivered bound on x in [4, 3004]; max ratio {worst:.3f}")

# Theorem 4.2(a): T <= 2 floor(A/pi) + 8 on every witness pair (and the S2 inequality behind it)
W = json.load(open(os.path.join(HERE, '..', 'data', 'witnesses.json')))
for w in W:
    s1 = (w['sig1']['g'], w['sig1']['orders']); s2 = (w['sig2']['g'], w['sig2']['orders'])
    U, V, Z = sig_to_config(s1, s2)
    x = area(s1)
    bound = 2 * ((2 * x).numerator // (2 * x).denominator) + 8
    n1, n2, g1, g2 = len(s1[1]), len(s2[1]), s1[0], s2[0]
    lhs = len(U) + len(V)
    if not (lhs <= 2 * max(n1 + g1 - g2, n2 + g2 - g1) <= bound):
        fail.append(("4.2a", w['kind'], w['L']))
print("Thm 4.2(a): |U*|+|V*| <= 2max(n+g-g', n'+g'-g) <= 2floor(A/pi)+8 on all 18 witnesses: OK")

# Theorem 4.3 thresholds against explicit constructions (sizes from a05: ideal n = 2L-2)
print("Thm 4.3: f_g >= L+1 for A >= 8 pi N(2L-3); f_n >= L+1 for A >= 2pi(3N(2L-3)-2):")
for L in range(2, 8):
    n = 2 * L - 2
    print(f"  L={L}: N(2L-3)<={n}: genus threshold A/2pi >= {4 * n}, cone threshold A/2pi >= {3 * n - 2}"
          f"  (witness tables: genus pair at {float(min(area((w['sig1']['g'], w['sig1']['orders'])) for w in W if w['kind'] == 'genus' and w['L'] == L)):.3f},"
          f" cone pair at {float(min(area((w['sig1']['g'], w['sig1']['orders'])) for w in W if w['kind'] == 'cone' and w['L'] == L)):.3f})")
    for kind, thr in (('genus', 4 * n), ('cone', 3 * n - 2)):
        a = min(area((w['sig1']['g'], w['sig1']['orders'])) for w in W if w['kind'] == kind and w['L'] == L)
        if a > thr:
            fail.append(("4.3 witness above threshold", kind, L))

if fail:
    print("FAILURES:", fail)
    sys.exit(1)
if BROKEN_AGREE:
    print("RESULT: inequalities SURVIVE; the parenthetical '(the two agree on [4,28))' after Thm 4.1 is FALSE "
          "(new > old on [13,15)).")
    sys.exit(2)
print("ALL CHECKS PASSED")
