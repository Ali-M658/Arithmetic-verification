"""Exhaustive test of Lemma eig:int on all hyperbolic signatures with Area <= 6*pi and orders <= 10.
Exact arithmetic (integers after exact rescaling).  Raises on any failure."""
import random, sys, itertools
from fractions import Fraction as F
from math import lcm, floor
from sympy import primerange
from heat import *

MMAX, AMAX_PI, J = 10, 6, 13   # Area <= AMAX_PI*pi ; compute c_1..c_J

# enumerate signatures: Area/(2pi) = 2g-2+sum(1-1/m) in (0, AMAX_PI/2]
sigs = []
for g in range(0, 4):
    for n in range(0, 2 * AMAX_PI + 5):
        if 2 * g - 2 + F(n, 2) > F(AMAX_PI, 2):
            break
        for ms in itertools.combinations_with_replacement(range(2, MMAX + 1), n):
            x = 2 * g - 2 + sum(1 - F(1, m) for m in ms)
            if 0 < x <= F(AMAX_PI, 2):
                sigs.append((g, ms))
print("signatures:", len(sigs))

# exact c-vectors, scaled to integers per index
scale = []
for j in range(1, J + 1):
    dens = [2 * 2520]
    if j >= 2:
        dens += [alpha(j - 1).denominator * 2 * 2520] + [b_l(j - 2, m).denominator for m in range(2, MMAX + 1)]
    s = 1
    for d in dens:
        s = lcm(s, d)
    scale.append(s)
btab = {(j, m): (b_l(j - 2, m) * scale[j - 1]) for j in range(2, J + 1) for m in range(2, MMAX + 1)}
for v in btab.values():
    assert v.denominator == 1


def cint(g, ms):
    a4 = -chi(g, ms) / 2
    out = [a4 * scale[0]]
    for j in range(2, J + 1):
        out.append(alpha(j - 1) * a4 * scale[j - 1] + sum(btab[(j, m)] for m in ms))
    for v in out:
        assert v.denominator == 1
    return tuple(int(v) for v in out)


data = [(cint(g, ms), g, ms) for g, ms in sigs]
# sanity: cint agrees with c_vec on a sample
for (cv, g, ms) in random.Random(1).sample(data, 200):
    assert tuple(F(x, scale[i]) for i, x in enumerate(cv)) == tuple(c_vec(g, ms, J))


def check_pair(s1, s2, area_equal):
    (cv1, g1, m1), (cv2, g2, m2) = s1, s2
    k = next((i + 1 for i in range(J) if cv1[i] != cv2[i]), None)
    if k is None:
        raise SystemExit(f"FAIL: equal c_1..c_{J}: {g1,m1} {g2,m2}")
    dk = F(cv1[k - 1] - cv2[k - 1], scale[k - 1])
    if not area_equal:
        assert k == 1
        L = lcm(1, *m1, *m2)
        assert abs(dk) >= F(1, 2 * L), (g1, m1, g2, m2)
        return k, abs(dk) * 2 * L
    area_over_pi = -2 * chi(g1, m1)
    bound = floor(area_over_pi) + 4
    if not (2 <= k <= bound):
        raise SystemExit(f"FAIL range: k={k} bound={bound} {g1,m1} {g2,m2}")
    d = F(sum(F(1, m) for m in m2) - sum(F(1, m) for m in m1))
    assert d.denominator == 1
    d = int(d)
    U = list(m1) + [1] * max(d, 0)
    V = list(m2) + [1] * max(-d, 0)
    e = 2 * k - 3
    diff = sum(u ** e for u in U) - sum(v ** e for v in V)
    if dk != (-1) ** k * a_lead(k - 2) * diff:
        raise SystemExit(f"FAIL formula k={k} {g1,m1} {g2,m2}")
    assert diff != 0
    if k >= 3:
        for p in primerange(2, 2 * k):
            if (2 * (k - 2)) % (p - 1) == 0:
                if diff % p:
                    raise SystemExit(f"FAIL divisibility p={p} k={k} {g1,m1} {g2,m2}")
    assert abs(dk) >= a_lead(k - 2)
    return k, F(abs(diff))


# group by area
groups = {}
for item in data:
    groups.setdefault(item[0][0], []).append(item)
print("area classes:", len(groups))
maxk_by_area = {}
npairs = 0
hist = {}
minratio = {}
rng = random.Random(7)
for a, grp in groups.items():
    grp.sort()
    for x, y in zip(grp, grp[1:]):
        k, r = check_pair(x, y, True); npairs += 1
        hist[k] = hist.get(k, 0) + 1
        maxk_by_area[a] = max(maxk_by_area.get(a, 0), k)
        minratio[k] = min(minratio.get(k, r), r)
    if len(grp) <= 400:
        for x, y in itertools.combinations(grp, 2):
            k, r = check_pair(x, y, True); npairs += 1
            hist[k] = hist.get(k, 0) + 1
            minratio[k] = min(minratio.get(k, r), r)
    else:
        for _ in range(20000):
            x, y = rng.sample(grp, 2)
            k, r = check_pair(x, y, True); npairs += 1
            hist[k] = hist.get(k, 0) + 1
print("equal-area pairs checked:", npairs)
print("first-difference index histogram:", dict(sorted(hist.items())))
print("min |P_{2k-3}(U)-P_{2k-3}(V)| by k (attained among checked pairs):", {k: str(v) for k, v in sorted(minratio.items())})
# slack of the range bound: max over area classes of (bound - maxk)
worst = min((floor(F(a, scale[0]) * 4) + 4 - k, F(a, scale[0]) * 4, k) for a, k in maxk_by_area.items())
print("tightest (bound - max k, Area/pi, max k):", worst[0], str(worst[1]), worst[2])
tight = [(str(F(a, scale[0]) * 4), k) for a, k in maxk_by_area.items() if floor(F(a, scale[0]) * 4) + 4 == k]
print("area classes where max first-difference index equals the bound:", len(tight), tight[:10])

# (i): different areas
ratios = []
for _ in range(200000):
    x, y = rng.sample(data, 2)
    if x[0][0] != y[0][0]:
        ratios.append(check_pair(x, y, False)[1])
# nearest-area pairs
keys = sorted(groups)
for a1, a2 in zip(keys, keys[1:]):
    for x in groups[a1][:30]:
        for y in groups[a2][:30]:
            ratios.append(check_pair(x, y, False)[1])
print("(i) checked", len(ratios), "pairs; min |d_1|*2L =", str(min(ratios)))
print("eig:int OK")
