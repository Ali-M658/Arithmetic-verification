"""PW.3 / PW.5: the 61 claimed pencil configurations (n = 4 integer sharpness of Theorem A).

Part 1. Every listed Z (parsed verbatim from the bundle): 8 integers, primitive, no pair {z,-z},
        s_1 = s_3 = s_{-1} = 0, four positive and four negative entries, m != m', the 61 pairwise
        distinct modulo Z -> lambda Z and Z -> -Z; the two genus-0 orbifolds (0;m), (0;m') are
        hyperbolic, have equal area and share EXACTLY 3 heat coefficients (direct c_j, heatlib),
        and the criterion (R, P_1, P_3 equal, P_5 different) agrees.
Part 2. The enumeration claim.  pencil4_N{130,220}_mode{0,1}.txt are produced by check_pencil4.c
        (exact int64/int128): classes of primitive 4-sets {e1=0} with equal J = e3^4/e4^3.
        For each ordered pair (A,B) in a class, lambda = e4(A)e3(B)/(e3(A)e4(B)) (exact),
        Z = A + (-lambda B) after cancelling {z,-z} pairs, made primitive, sign-normalised.
        mode 0 = the claim as worded (all four entries of A and of B in [-N,N]);
        mode 1 = at most one entry of A (and of B) outside [-N,N] ('A={a,b,c,-(a+b+c)}, |a|,|b|,|c|<=N').
        An independent pure-Python enumeration re-derives mode 0 for N = 130.
Part 3. Smallest witness {3,10,15,30} ~ {4,5,21,28} from A={-30,-3,5,28}, B={-21,-4,10,15}.
Exits nonzero if an assertion about a VERIFIED fact fails; the claim checks (counts 61/25) are
reported as CLAIM TRUE/FALSE and do not abort, so that the output records the discrepancy.
"""
import sys
from fractions import Fraction as F
from math import gcd
from functools import reduce
from itertools import combinations
from collections import Counter
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from heatlib import shared, criterion_L, is_hyperbolic, s_area, R, P

HERE = __file__.rsplit('/', 1)[0]
txt = open(HERE + '/../statements/pte-witnesses.md').read()
blk = txt.split('### PW.5')[1].split('```')[1]
L61 = [tuple(int(x) for x in l.strip('[] ').split(',')) for l in blk.strip().splitlines()]
assert len(L61) == 61

def canon(Z):
    c = Counter(Z)
    for z in list(c):
        if z > 0 and c[-z] > 0:
            k = min(c[z], c[-z]); c[z] -= k; c[-z] -= k
    Z = list(c.elements())
    if not Z:
        return None
    den = reduce(lambda a, b: a * b // gcd(a, b), [F(z).denominator for z in Z])
    Zi = [int(F(z) * den) for z in Z]
    g = reduce(gcd, Zi)
    Zi = [z // g for z in Zi]
    a = tuple(sorted(Zi)); b = tuple(sorted(-z for z in Zi))
    return min(a, b)

def esym(S, k):
    t = 0
    for c in combinations(S, k):
        p = 1
        for x in c:
            p *= x
        t += p
    return t

def prim(S):
    g = reduce(gcd, S)
    return sorted(x // g for x in S)

def pencil_splits(Z):
    out = []
    for A in combinations(range(8), 4):
        if 0 not in A:
            continue
        a = [Z[i] for i in A]; c = [-Z[i] for i in range(8) if i not in A]
        if sum(a) == 0 and esym(a, 3) == esym(c, 3) and esym(a, 4) == esym(c, 4):
            out.append((prim(a), prim(c)))
    return out

# ---------------- Part 1
print("Part 1: the 61 listed configurations")
canons = set()
nshared = Counter()
maxes = []
for Z in L61:
    assert len(Z) == 8
    assert reduce(gcd, Z) == 1, Z
    assert not any(-z in Z for z in Z), Z
    assert sum(Z) == 0 and sum(z ** 3 for z in Z) == 0 and sum(F(1, z) for z in Z) == 0, Z
    pos = sorted(z for z in Z if z > 0); neg = sorted(-z for z in Z if z < 0)
    assert len(pos) == 4 and len(neg) == 4, Z
    assert pos != neg
    assert min(pos + neg) >= 2  # no padding point 1: both are genuine 4-cone orbifolds
    assert is_hyperbolic(0, pos) and is_hyperbolic(0, neg)
    assert s_area(0, pos) == s_area(0, neg)
    k, c1, c2 = shared(0, pos, 0, neg, 5)
    assert k == criterion_L(0, pos, 0, neg, 5)
    assert R(pos) == R(neg) and P(pos, 1) == P(neg, 1) and P(pos, 3) == P(neg, 3) and P(pos, 5) != P(neg, 5)
    nshared[k] += 1
    canons.add(canon(Z))
    maxes.append(max(map(abs, Z)))
    assert pencil_splits(Z), Z  # every listed Z IS a pencil configuration
assert len(canons) == 61
print("  all 61: primitive, no {z,-z}, s1=s3=s_-1=0, 4+4 signs, entries >= 2, hyperbolic, equal area,"
      " pairwise distinct mod scaling/negation, pencil-decomposable: OK")
print("  shared heat coefficients (direct, = criterion):", dict(nshared))
assert nshared == Counter({3: 61})
print(f"  max |entry| over the list: {max(maxes)};  #Z with max|z|<=220: {sum(m <= 220 for m in maxes)},"
      f" <=130: {sum(m <= 130 for m in maxes)}")

# ---------------- Part 2
def gen(fn):
    out = {}
    for g in open(fn).read().split('\n\n'):
        rows = [list(map(int, l.split())) for l in g.strip().splitlines() if l and not l.startswith('#')]
        for i in range(len(rows)):
            for j in range(len(rows)):
                if i == j:
                    continue
                e3a, e4a, *A = rows[i]; e3b, e4b, *B = rows[j]
                assert sum(A) == 0 and esym(A, 3) == e3a and esym(A, 4) == e4a
                assert sum(B) == 0 and esym(B, 3) == e3b and esym(B, 4) == e4b
                lam = F(e4a * e3b, e4b * e3a)
                assert lam ** 3 * e3b == e3a and lam ** 4 * e4b == e4a
                LB = sorted(lam * b for b in B)
                if LB == sorted(A):
                    continue
                Z = canon([F(a) for a in A] + [-x for x in LB])
                if Z is None:
                    continue
                assert len(Z) == 8
                out.setdefault(Z, set()).add((tuple(A), tuple(B)))
    return out

print("\nPart 2: own enumeration (C, exact) and comparison with the claimed set")
res = {}
for N in (130, 220):
    for mode in (0, 1):
        G = gen(f"{HERE}/pencil4_N{N}_mode{mode}.txt")
        res[(N, mode)] = G
        inlist = sum(1 for z in G if z in canons)
        print(f"  N={N} mode={mode}: {len(G)} distinct configurations; in the claimed list: {inlist};"
              f" generated but not listed: {len(G) - inlist}")
        for z in G:
            # each generated Z is a genuine witness
            pos = sorted(x for x in z if x > 0); neg = sorted(-x for x in z if x < 0)
            assert len(pos) == 4 and sum(z) == 0 and sum(x ** 3 for x in z) == 0 and sum(F(1, x) for x in z) == 0
G0, G1 = res[(220, 0)], res[(220, 1)]
claim61 = len(G0) == 61 and set(G0) == canons
claim25 = len(res[(130, 0)]) == 25
print(f"  CLAIM '61 configurations with entries <= 220' (as worded, mode 0): {'TRUE' if claim61 else 'FALSE'}"
      f" -- own count {len(G0)}")
print(f"  CLAIM '25 with entries <= 130' (as worded, mode 0): {'TRUE' if claim25 else 'FALSE'}"
      f" -- own count {len(res[(130, 0)])}")
print(f"  mode 1 (one entry unrestricted): N=220 -> {len(G1)}, equal to the listed set: {set(G1) == canons};"
      f" N=130 -> {len(res[(130, 1)])}")
assert set(G0) <= canons
# characterisation of the listed set
both = sum(1 for Z in L61 if any(max(map(abs, a)) <= 220 and max(map(abs, b)) <= 220 for a, b in pencil_splits(Z)))
one = sum(1 for Z in L61 if any(min(max(map(abs, a)), max(map(abs, b))) <= 220 for a, b in pencil_splits(Z)))
print(f"  listed Z having a pencil split with BOTH primitive sides <= 220: {both}; with ONE side <= 220: {one}")
for Z in sorted(canons - set(G0), key=lambda z: max(map(abs, z)))[:5]:
    print("   example listed but outside the worded recipe:", Z, "splits (A,B) primitive:", pencil_splits(list(Z)))

# independent pure-Python enumeration, mode 0, N = 130
N = 130
groups = {}
for a in range(-N, N + 1):
    for b in range(a, N + 1):
        for c in range(b, N + 1):
            d = -(a + b + c)
            if d < c or d > N or 0 in (a, b, c, d) or reduce(gcd, (a, b, c, d)) != 1:
                continue
            S = (a, b, c, d)
            e3, e4 = esym(S, 3), esym(S, 4)
            if e3 <= 0:
                continue
            groups.setdefault(F(e3 ** 4, e4 ** 3), []).append(S)
Zpy = set()
for J, mem in groups.items():
    for A in mem:
        for B in mem:
            if A == B:
                continue
            lam = F(esym(A, 4) * esym(B, 3), esym(B, 4) * esym(A, 3))
            LB = sorted(lam * x for x in B)
            if LB == sorted(A):
                continue
            z = canon([F(x) for x in A] + [-x for x in LB])
            if z:
                Zpy.add(z)
print(f"  independent Python enumeration, N=130 mode 0: {len(Zpy)} configurations;"
      f" equals the C result: {Zpy == set(res[(130, 0)])}")
assert Zpy == set(res[(130, 0)])

# ---------------- Part 3
A = [-30, -3, 5, 28]; B = [-21, -4, 10, 15]
assert sum(A) == sum(B) == 0 and esym(A, 3) == esym(B, 3) and esym(A, 4) == esym(B, 4) and esym(A, 2) != esym(B, 2)
Z = canon([F(x) for x in A] + [F(-x) for x in B])
pos = sorted(x for x in A + [-y for y in B] if x > 0); neg = sorted(-x for x in A + [-y for y in B] if x < 0)
print("\nPart 3: A={-30,-3,5,28}, B={-21,-4,10,15}: e1=0, e3, e4 equal (lambda=1), e2:", esym(A, 2), esym(B, 2))
print("  Z = A + (-B) =", sorted(A + [-y for y in B]), "-> m =", pos, ", m' =", neg)
assert sorted([pos, neg]) == [[3, 10, 15, 30], [4, 5, 21, 28]]
smallest = min(canons, key=lambda z: (max(map(abs, z)), z))
print("  smallest listed configuration (by max entry):", smallest)
assert smallest == canon([F(x) for x in [-28, -21, -5, -4, 3, 10, 15, 30]])
print("\nverified facts: ALL OK (claim verdicts above)")
