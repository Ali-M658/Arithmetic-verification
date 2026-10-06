"""(b) rank E(Q) = 0 for E: y^2 = x(x^2 + 393x + 3456) by 2-isogeny descent (Cremona 3.6, Method 1,
(3.6.2)) on E and on E' (c' = -2c, d' = c^2 - 4d), with exact local-solubility certificates;
plus an independent full 2-Selmer computation over the three rational roots.

Integers / Fractions only.  Exits nonzero on any failure.
"""
from fractions import Fraction as Fr
from itertools import product
from math import gcd, isqrt
from descent_lib import Out, Weier

o = Out()


def vp(n, p):
    n = abs(n)
    assert n != 0
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def is_padic_square_int(n, p):
    """n nonzero integer: is n a square in Q_p ?"""
    k = vp(n, p)
    if k % 2:
        return False
    u = n // p ** k
    if p == 2:
        return u % 8 == 1
    return pow(u % p, (p - 1) // 2, p) == 1


def sqfree_divisors(n):
    ps = [p for p in range(2, abs(n) + 1) if abs(n) % p == 0 and all(p % q for q in range(2, isqrt(p) + 1))]
    out = []
    for s in (1, -1):
        for mask in range(1 << len(ps)):
            m = s
            for i, p in enumerate(ps):
                if mask >> i & 1:
                    m *= p
            out.append(m)
    return ps, out


def sqfree_part(n):
    s = -1 if n < 0 else 1
    n = abs(n)
    r = 1
    p = 2
    while p * p <= n:
        while n % (p * p) == 0:
            n //= p * p
        if n % p == 0:
            r *= p
            n //= p
        p += 1
    return s * r * n


def g_val(d1, c, d2, M, e):
    return d1 * M ** 4 + c * M ** 2 * e ** 2 + d2 * e ** 4


def local_soluble(d1, c, d2, p, kmax):
    """Decide solubility of N^2 = d1 M^4 + c M^2 e^2 + d2 e^4 over Q_p (p prime) or R (p = 0).
    Returns ('yes', witness) or ('no', certificate) ; asserts that one of them is found."""
    if p == 0:
        for M, e in product(range(-30, 31), repeat=2):
            if (M, e) != (0, 0) and g_val(d1, c, d2, M, e) > 0:
                return 'yes', (M, e)
        # certificate: all coefficients <= 0 and d1, d2 < 0 -> negative definite
        assert d1 < 0 and d2 < 0 and c <= 0
        return 'no', 'd1<0, c<=0, d2<0: right side < 0 for (M,e) != 0'
    # solubility witness: primitive integers (M, e) with g a nonzero p-adic square
    for B in range(1, 60):
        for M, e in product(range(-B, B + 1), repeat=2):
            if max(abs(M), abs(e)) != B and B > 1:
                continue
            if gcd(M, e) != 1:
                continue
            gv = g_val(d1, c, d2, M, e)
            if gv != 0 and is_padic_square_int(gv, p):
                return 'yes', (M, e, gv)
    # insolubility: no primitive (M, e) mod p^k with g(M,e) a square mod p^k
    for k in range(1, kmax + 1):
        q = p ** k
        squares = {(N * N) % q for N in range(q)}
        found = False
        for M in range(q):
            for e in range(q):
                if M % p == 0 and e % p == 0:
                    continue
                if g_val(d1, c, d2, M, e) % q in squares:
                    found = True
                    break
            if found:
                break
        if not found:
            return 'no', f'no primitive (M,e) mod {p}^{k} makes the right side a square mod {p}^{k}'
    raise AssertionError(f"undecided: d1={d1}, p={p}")


def global_point(d1, c, d2, B=200):
    for s in range(1, 2 * B):
        for M in range(0, s + 1):
            e = s - M
            if gcd(M, e) != 1:
                continue
            for MM in ((M, e), (-M, e)):
                gv = g_val(d1, c, d2, MM[0], MM[1])
                if gv >= 0 and isqrt(gv) ** 2 == gv:
                    return (isqrt(gv),) + MM
    return None


def descent(c, d, name):
    print(f"\n=== {name}: y^2 = x(x^2 + {c} x + {d});  d = {d}, c^2 - 4d = {c*c - 4*d}")
    dprime = c * c - 4 * d
    ps, divs = sqfree_divisors(d)
    bad = sorted(set([2] + [p for p in range(2, 100) if (d * dprime) % p == 0 and all(p % q for q in range(2, p))]))
    print("primes dividing 2 d d' :", bad, "; squarefree divisors d1 of d:", divs)
    loc_ok, glob_ok = [], []
    for d1 in divs:
        assert d % d1 == 0
        d2 = d // d1
        row = {}
        allloc = True
        for p in bad + [0]:
            kmax = {2: 9, 3: 6, 5: 4}.get(p, 3)
            st, cert = local_soluble(d1, c, d2, p, kmax)
            row['R' if p == 0 else p] = (st, cert)
            if st == 'no':
                allloc = False
        gp = global_point(d1, c, d2)
        if gp is not None:
            N, M, e = gp
            o.ok(N * N == g_val(d1, c, d2, M, e), f"d1={d1}: global point (N,M,e)={gp} on N^2 = d1 M^4 + c M^2 e^2 + d2 e^4")
            o.ok(allloc, f"d1={d1}: global point implies all local tests 'yes' (consistency)")
            glob_ok.append(d1)
            # map to the curve: (x,y) = (d1 u^2, d1 u v) with u = M/e, v = N/e^2  (Cremona 3.6)
            if e != 0:
                u, v = Fr(M, e), Fr(N, e * e)
                P = (d1 * u * u, d1 * u * v)
                o.ok(Weier(c, d).on(P), f"d1={d1}: (d1 u^2, d1 u v) = {P} lies on the curve")
            else:
                print(f"   d1={d1}: point at infinity of the quartic (d1 square)")
        if allloc:
            loc_ok.append(d1)
        txt = "; ".join(f"{k}: {v[0]} [{v[1]}]" for k, v in row.items())
        print(f"d1={d1:>4}, d2={d2:>6}: {txt}; global point: {gp}")
    return set(loc_ok), set(glob_ok)


def is_group(S):
    return all(sqfree_part(a * b) in S for a in S for b in S)


c, d = 393, 3456
cp, dp = -2 * c, c * c - 4 * d
o.ok((cp, dp) == (-786, 140625), "E': c' = -2c = -786, d' = c^2 - 4d = 140625 = 375^2")
o.ok(isqrt(dp) ** 2 == dp, "d' is a square (E has full rational 2-torsion)")
o.ok(d * dp != 0, "d d' != 0 (nonsingular)")

A2, A1 = descent(c, d, "E")
o.ok(A2 == A1 == {1, -1, 6, -6}, f"E: everywhere-locally-soluble set = globally soluble set = {sorted(A1)} = {{+-1, +-6}}")
o.ok(is_group(A1), "E: {+-1,+-6} is a subgroup of Q*/Q*^2")
A2p, A1p = descent(cp, dp, "E'")
o.ok(A2p == A1p == {1}, f"E': everywhere-locally-soluble set = globally soluble set = {sorted(A1p)} = {{1}}")
n1, n1p = len(A1), len(A1p)
e1, e1p = n1.bit_length() - 1, n1p.bit_length() - 1
o.ok(2 ** e1 == n1 and 2 ** e1p == n1p, "n1, n1' are powers of 2")
r = e1 + e1p - 2
o.ok(r == 0, f"(3.6.2): rank = e1 + e1' - 2 = {e1} + {e1p} - 2 = {r}")
o.ok(len(A2) == len(A1) and len(A2p) == len(A1p), "n1 = n2 and n1' = n2': Sha(E)[phi] = Sha(E')[phi'] = 0, no ambiguity")

# consistency with the torsion points: x mod squares (Cremona: (0,0) -> d)
E = Weier(c, d)
tors = [(0, 0), (-9, 0), (-384, 0), (-24, 360), (-24, -360), (-144, 2160), (-144, -2160),
        (16, 400), (16, -400), (216, 5400), (216, -5400)]
img = set()
for (x, y) in tors:
    img.add(sqfree_part(d) if x == 0 else sqfree_part(x))
o.ok(img == {1, -1, 6, -6}, f"images of the torsion points in E(Q)/phi'(E'(Q)): {sorted(img)}")

# ---------------------------------------------------------------------------
# Independent route: full 2-descent with the three rational roots e = 0, -9, -384.
# kappa(P) = (x - e1, x - e2) mod squares; kappa(e1,0) = ((e1-e2)(e1-e3), e1-e2), etc.
# Selmer: (b1, b2) in <-1,2,3,5>^2 lying in the local image at 2, 3, 5 and R.
# Size of the local image: |E(Q_p)/2E(Q_p)| = |E(Q_p)[2]| * |2|_p^{-1} = 8 (p=2), 4 (p odd);
# |E(R)/2E(R)| = 2 (Delta > 0).  [standard input, not in the fetched Cremona text: see REVIEW.md]
# ---------------------------------------------------------------------------
print("\n=== independent route: full 2-Selmer group via the roots 0, -9, -384")
roots = (0, -9, -384)


def cls_p(q, p):
    """class of a nonzero rational in Q_p*/Q_p*^2 (p prime) or R*/R*^2 (p = 0)."""
    q = Fr(q)
    if p == 0:
        return 1 if q > 0 else -1
    n = q.numerator * q.denominator  # same class
    k = vp(n, p)
    u = n // p ** k
    if p == 2:
        return (k % 2, u % 8)
    return (k % 2, 1 if pow(u % p, (p - 1) // 2, p) == 1 else -1)


def kappa(P):
    x, y = P
    e1_, e2_, e3_ = roots
    if x == e1_:
        return ((e1_ - e2_) * (e1_ - e3_), e1_ - e2_)
    if x == e2_:
        return (e2_ - e1_, (e2_ - e1_) * (e2_ - e3_))
    return (x - e1_, x - e2_)


def mult_cls(a, b, p):
    if p == 0:
        return a * b
    if p == 2:
        return ((a[0] + b[0]) % 2, (a[1] * b[1]) % 8)
    return ((a[0] + b[0]) % 2, a[1] * b[1])


expected = {2: 8, 3: 4, 5: 4, 0: 2}
local_img = {}
for p in (2, 3, 5, 0):
    S = set()
    # E(Q) points and rational x with f(x) a local square
    one = 1 if p == 0 else ((0, 1))
    cands = []
    for den in range(1, 60):
        for num in range(-3000, 3000):
            if gcd(num, den) != 1:
                continue
            x = Fr(num, den)
            fx = x * (x + 9) * (x + 384)
            if fx == 0:
                continue
            if p == 0:
                ok = fx > 0
            else:
                n_ = fx.numerator * fx.denominator
                ok = is_padic_square_int(n_, p)
            if ok:
                cands.append((x, None))
        if len(cands) > 4000:
            break
    cands += [(Fr(0), 0), (Fr(-9), 0), (Fr(-384), 0)]
    S = {(one, one)}
    for (x, y) in cands:
        k1, k2 = kappa((x, y))
        cl = (cls_p(k1, p), cls_p(k2, p))
        # close under multiplication
        new = {(mult_cls(cl[0], s[0], p), mult_cls(cl[1], s[1], p)) for s in S}
        S |= new
        if len(S) == expected[p]:
            break
    o.ok(len(S) == expected[p], f"local Kummer image at {'R' if p == 0 else p} has the full size {expected[p]}")
    local_img[p] = S

primes = [-1, 2, 3, 5]
group = []
for mask in range(16):
    m = 1
    for i in range(4):
        if mask >> i & 1:
            m *= primes[i]
    group.append(m)
sel = []
for b1 in group:
    for b2 in group:
        if all((cls_p(b1, p), cls_p(b2, p)) in local_img[p] for p in (2, 3, 5, 0)):
            sel.append((b1, b2))
print("2-Selmer group (b1, b2):", sel)
o.ok(len(sel) == 4, "|Sel^2(E/Q)| = 4")
tors_img = {tuple(sqfree_part(int(t)) for t in kappa((Fr(x), Fr(y)))) for (x, y) in tors}
tors_img.add((1, 1))
o.ok(tors_img == set(sel), f"Sel^2 = kappa(E(Q)[2]) = {sorted(tors_img)}")
# |E(Q)/2E(Q)| = 2^(r+2) <= |Sel^2| = 4  ->  r = 0
o.ok(2 ** (0 + 2) == len(sel), "2^(r+2) <= |Sel^2| = 4 forces r = 0; Sha(E)[2] = 0")

print(f"ALL {o.n} CHECKS PASSED")
