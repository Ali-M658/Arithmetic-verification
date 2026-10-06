"""PW.3 / PW.5, n = 5 claim: 'Among all 1,592 primitive [odd symmetric] 5-sets with entries <= 200,
no [pencil] pair exists.'

Pencil at m = 5 (Theorem 3.1: r = 5, k0 = 2): A != B with e1 = e3 = 0 and e4, e5 equal.  For
primitive integer A, B the scaled partner lambda*B (lambda rational) has e4(lambda B) = e4(A),
e5(lambda B) = e5(A) iff J(A) = J(B), J = e4^5/e5^4 (e5 != 0 since entries are nonzero), with
lambda = (e5A/e5B)/(e4A/e4B) when e4 != 0; when e4A = e4B = 0 one needs e5A/e5B to be a rational
fifth power.  A and -A always have equal J (lambda = -1 gives lambda(-A) = A, excluded).

Enumeration (pure Python, independent of check_n5.c): every primitive multiset of 5 nonzero
integers with s1 = s3 = 0 having at least three entries in [-200,200] (the other two solve
d+e = sigma, de = (sigma^3 - tau)/(3 sigma)).  Counts are given for 'all five <= 200',
'at most one > 200', 'at most two > 200'; the first two are compared with check_n5.c output.
The pencil test is run on the largest family.  Exits nonzero on failure of a verified fact.
"""
import sys
from fractions import Fraction as F
from math import gcd, isqrt
from functools import reduce
from itertools import combinations

HERE = __file__.rsplit('/', 1)[0]
N = 200
S = set()
for a in range(-N, N + 1):
    if a == 0:
        continue
    for b in range(a, N + 1):
        if b == 0:
            continue
        for c in range(b, N + 1):
            if c == 0:
                continue
            sg = -(a + b + c); tau = -(a ** 3 + b ** 3 + c ** 3)
            if sg == 0:
                continue  # then tau = 0 would need abc = 0
            num = sg ** 3 - tau
            if num % (3 * sg):
                continue
            p = num // (3 * sg)
            D = sg * sg - 4 * p
            if D < 0:
                continue
            r = isqrt(D)
            if r * r != D or (sg + r) % 2:
                continue
            d = (sg + r) // 2; e = (sg - r) // 2
            if d == 0 or e == 0:
                continue
            v = tuple(sorted((a, b, c, d, e)))
            if reduce(gcd, v) != 1:
                continue
            assert sum(v) == 0 and sum(x ** 3 for x in v) == 0
            S.add(v)

def nbig(v):
    return sum(1 for x in v if abs(x) > N)

fam = {k: sorted(v for v in S if nbig(v) <= k) for k in (0, 1, 2)}
for k in (0, 1, 2):
    up = len(set(min(v, tuple(sorted(-x for x in v))) for v in fam[k]))
    print(f"primitive odd symmetric 5-sets, at most {k} entries with |x|>200: {len(fam[k])}"
          f" (counting A and -A separately), {up} up to sign")
for k in (0, 1):
    C = sorted(tuple(map(int, l.split())) for l in open(f"{HERE}/n5_N200_mode{k}.txt") if not l.startswith('#'))
    assert C == fam[k], k
    print(f"  mode {k}: equals the exhaustive C enumeration check_n5.c ({len(C)} sets)")
assert len(fam[0]) == 602 and len(fam[2]) == 1592
print("CLAIM '1,592 primitive 5-sets with entries <= 200': the number 1,592 is the family"
      " 'at least three entries in [-200,200]' (A and -A both counted); with all entries <= 200 it is 602.")

def esym(S_, k):
    t = 0
    for c in combinations(S_, k):
        p = 1
        for x in c:
            p *= x
        t += p
    return t

def is_fifth_power(q):
    q = F(q)
    def r5(n):
        s = -1 if n < 0 else 1
        n = abs(n)
        x = round(n ** 0.2)
        for y in (x - 1, x, x + 1):
            if y >= 0 and y ** 5 == n:
                return True
        return False
    return r5(q.numerator) and r5(q.denominator)

groups = {}
zero4 = []
for v in fam[2]:
    e4, e5 = esym(v, 4), esym(v, 5)
    assert esym(v, 1) == 0 and esym(v, 3) == 0 and e5 != 0
    if e4 == 0:
        zero4.append((v, e5))
        continue
    groups.setdefault(F(e4 ** 5, e5 ** 4), []).append((v, e4, e5))
pairs = []
for J, mem in groups.items():
    for (A, e4a, e5a) in mem:
        for (B, e4b, e5b) in mem:
            if A == B:
                continue
            lam = F(e5a * e4b, e5b * e4a)
            assert lam ** 4 * e4b == e4a and lam ** 5 * e5b == e5a
            if sorted(lam * x for x in B) != sorted(A):
                pairs.append((A, B, lam))
for (A, e5a) in zero4:
    for (B, e5b) in zero4:
        if A != B and is_fifth_power(F(e5a, e5b)):
            pairs.append((A, B, 'e4=0'))
sizes = {}
for mem in groups.values():
    sizes[len(mem)] = sizes.get(len(mem), 0) + 1
print("J-classes by size (A and -A share a class):", dict(sorted(sizes.items())), "; sets with e4 = 0:", len(zero4))
print("non-trivial pencil pairs among the 1592:", len(pairs))
for p_ in pairs[:10]:
    print("  ", p_)
assert not pairs
print("CLAIM 'no pencil pair' : TRUE on all three families (<=200; at most one >200; at most two >200)")
print("ALL OK")
