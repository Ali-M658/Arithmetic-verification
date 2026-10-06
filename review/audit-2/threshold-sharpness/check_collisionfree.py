"""Exact checks for TH.1 (Theorem 5.13 and the collision-free-sums Proposition).
Reads collisions_18_4800.txt (output of check_collisionfree.c) and re-certifies it
independently with fractions.Fraction.  Exits nonzero on any failure."""
import sys
from fractions import Fraction as F
from collections import defaultdict

def triads(S):
    for p in range(2, S // 3 + 1):
        for q in range(p, (S - p) // 2 + 1):
            r = S - p - q
            if q * r + r * p + p * q < p * q * r:
                yield (p, q, r)

def R(t):
    return sum(F(1, m) for m in t)

def fibres(S):
    d = defaultdict(list)
    for t in triads(S):
        d[R(t)].append(t)
    return d

# ---------- (A) threshold ----------
# heat invariants of a triangle orbifold (n = 3), from ST.0 / PC.7:
#   H_{-1} = (n-2-R)/2 = (1-R)/2,   H_0 = (Area/4pi)*alpha_1 + sum (m^2-1)/(12m),  alpha_1 = -1/3
def H(t):
    Rv = R(t); S1 = sum(t)
    Hm1 = (1 - Rv) / 2
    H0 = Hm1 * F(-1, 3) + sum(F(m * m - 1, 12 * m) for m in t)
    return Hm1, H0
for S in range(10, 60):
    for t in triads(S):
        Hm1, H0 = H(t)
        Rv = 1 - 2 * Hm1
        assert Rv == R(t)
        assert 12 * H0 + 2 - Rv == sum(t)          # S1 = 12 a0 + 2 - R  (eq:s1inv)
        assert H0 == F(sum(t)) / 12 + (Rv - 2) / 12
print("(A) (H_-1,H_0) <-> (R,S1) is an affine bijection: S1 = 12 H_0 + 2 - R, R = 1 - 2 H_-1  [checked S<=59]")
print("    hence a triad of sum <= 17 can only share (H_-1,H_0) with a triad of the SAME sum; no larger-sum search needed")
alltri = [t for S in range(0, 18) for t in triads(S)]
assert min(sum(t) for t in alltri) == 10 and [t for t in alltri if sum(t) == 10] == [(3, 3, 4)]
keys = defaultdict(list)
for t in alltri:
    keys[H(t)].append(t)
assert all(len(v) == 1 for v in keys.values())
print(f"(A) all {len(alltri)} hyperbolic triads with S<=17 have pairwise distinct (H_-1,H_0)")
# belt and braces: compare each S<=17 triad with EVERY triad of sum <= 300 (any sum)
big = defaultdict(list)
for S in range(10, 301):
    for t in triads(S):
        big[H(t)].append(t)
for t in alltri:
    assert big[H(t)] == [t]
print("(A) and none shares (H_-1,H_0) with any triad of sum <= 300 (finite cross-check only; the proof is the S1 argument)")
f18 = fibres(18)
c18 = [v for v in f18.values() if len(v) > 1]
assert c18 == [[(2, 8, 8), (3, 3, 12)]] and R((2, 8, 8)) == F(3, 4)
print("(A) S=18: exactly one collision, (2,8,8) ~ (3,3,12), R = 3/4  -> 17 sharp")

# ---------- (B) collision-free sums ----------
claimed = [19] + list(range(21, 26)) + list(range(27, 31)) + [33, 41, 44] + list(range(46, 52)) + \
          [59, 65, 67, 81, 99, 115, 119, 123, 125, 173, 199, 203, 223, 235, 243, 251, 307, 329, 557]
assert len(claimed) == len(set(claimed)) == 38, len(claimed)
print("(B) printed list expands to", len(claimed), "sums")

rows = {}
for line in open("collisions_18_4800.txt"):
    a = line.split()
    S, nt, c = int(a[0]), int(a[1]), int(a[2])
    assert S not in rows
    rows[S] = (nt, c, a[3:] if c else None)
assert sorted(rows) == list(range(18, 4801))
free_C = [S for S in rows if rows[S][1] == 0]
assert free_C == claimed, (free_C, claimed)
print("(B) C search: collision-free sums in [18,4800] =", free_C)

# certify every reported collision pair exactly (distinct, hyperbolic, same sum, same R)
for S, (nt, c, pr) in rows.items():
    if c:
        t1 = tuple(map(int, pr[0].split(","))); t2 = tuple(map(int, pr[1].split(",")))
        for t in (t1, t2):
            assert sum(t) == S and 2 <= t[0] <= t[1] <= t[2] and R(t) < 1
        assert t1 != t2 and R(t1) == R(t2)
print(f"(B) all {sum(1 for v in rows.values() if v[1])} collision witnesses re-verified with Fraction")

# certify collision-freeness independently (full Fraction enumeration) at every claimed sum,
# and the full classification + triad counts for S <= 700
for S in range(18, 701):
    fb = fibres(S)
    nt = sum(len(v) for v in fb.values())
    assert nt == rows[S][0], (S, nt, rows[S][0])
    has = any(len(v) > 1 for v in fb.values())
    assert has == (S not in claimed), S
print("(B) independent Fraction enumeration S<=700: same classification and same triad counts")
assert rows[557][0] == 25575
print("(B) S=557 has", rows[557][0], "hyperbolic triads (claimed 25,575)")

# explicit first pairs
for S, a, b in [(18, (2, 8, 8), (3, 3, 12)), (20, (4, 8, 8), (5, 5, 10)), (26, (4, 10, 12), (5, 6, 15))]:
    fb = fibres(S)
    cols = [v for v in fb.values() if len(v) > 1]
    assert R(a) == R(b) and sum(a) == sum(b) == S
    print(f"    S={S}: collision fibres {cols}")
    assert [a, b] in cols

# scaling lemma and the 3962 / 783 split
has = {S: rows[S][1] == 1 for S in rows}
covered = [S for S in range(18, 4801) if any(has[d] for d in range(18, S) if S % d == 0)]
rest = [S for S in range(18, 4801) if S not in covered]
rest_col = [S for S in rest if has[S]]
print("(B) sums covered by scaling (some proper divisor d>=18 carries a collision):", len(covered))
print("    not covered:", len(rest), " of which with a collision (primitive sums):", len(rest_col),
      " collision-free:", len(rest) - len(rest_col))
assert all(has[S] for S in covered)       # scaling lemma consistent with the data
assert len(covered) == 3962 and len(rest_col) == 783 and len(rest) - len(rest_col) == 38
print("ALL CHECKS PASSED")
