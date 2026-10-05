"""Attack item 2: Theorem 2.1 (|iota| <= T - 2L) and Lemma 1.2(4) (T even, T >= 2L+2).

(A) brute force over pairs of multisets U,V of integers in [1..M] (U,V disjoint, R(U)=R(V),
    P1 equal) = every genus/cone collision of small orders, any genera.
(B) random rational L=2 and L=3 configurations of every size up to 12, built by solving for
    the last 2 (L=2) or 3 (L=3) entries exactly.
(C) odd-size configurations: Definition 1.1 does not require T even.
"""
import sys, os, random, itertools
from fractions import Fraction as F
from collections import defaultdict, Counter
from math import isqrt
sys.path.insert(0, os.path.dirname(__file__))
from mylib import psum, iota, config_level, has_pm_pair, rational_roots_cubic, primitive, shared

fail = []

# ---------------- (A) multiset brute force ----------------
M, KMAX = 16, 7
groups = defaultdict(list)
for k in range(1, KMAX + 1):
    for ms in itertools.combinations_with_replacement(range(1, M + 1), k):
        groups[(sum(F(1, x) for x in ms), sum(ms))].append(ms)
npairs = 0
worst = Counter()
tight = Counter()
for key, lst in groups.items():
    if len(lst) < 2:
        continue
    for U, V in itertools.combinations(lst, 2):
        if set(U) & set(V):
            continue
        Z = list(U) + [-v for v in V]
        T = len(Z)
        L = config_level(Z, Lmax=20)
        if L < 2:
            continue
        npairs += 1
        io = iota(Z)
        if T % 2 == 0:
            if abs(io) > T - 2 * L or T < 2 * L + 2:
                fail.append(("A", U, V, L, io))
            if abs(io) == T - 2 * L:
                tight[(L, T, abs(io))] += 1
        worst[(L, T)] = max(worst[(L, T)], abs(io))
sys.stdout.reconfigure(line_buffering=True)
print(f"(A) multisets from [1..{M}], sizes <= {KMAX}: {npairs} disjoint pairs with L>=2 checked")
for (L, T), w in sorted(worst.items()):
    print(f"    L={L} T={T:2d}: max |iota| = {w}  (bound T-2L = {T - 2 * L})")
print("    bound attained (L,T,|iota|):", dict(tight))

# ---------------- (B) random rational configurations ----------------
random.seed(20261006)


def rnd():
    return F(random.randint(-40, 40) or 1, random.randint(1, 6))


def complete_L2(free):
    S, R = sum(free), sum(1 / x for x in free)
    if R == 0 or S == 0:
        return None
    p = S / R  # z1 z2 ; z1+z2 = -S
    disc = S * S - 4 * p
    if disc < 0:
        return None
    n, d = disc.numerator, disc.denominator
    if isqrt(n) ** 2 != n or isqrt(d) ** 2 != d:
        return None
    r = F(isqrt(n), isqrt(d))
    return free + [(-S + r) / 2, (-S - r) / 2]


def complete_L3(free):
    S, C, R = -sum(free), -sum(x ** 3 for x in free), -sum(1 / x for x in free)
    if S * R == 1:
        return None
    e3 = (C - S ** 3) / (3 * (1 - S * R))
    e2 = R * e3
    if e3 == 0:
        return None
    rts = rational_roots_cubic(1, -S, e2, -e3)
    if len(rts) != 3:
        return None
    return free + rts


stats = defaultdict(lambda: [0, 0])  # (L,T) -> [count, max|iota|]
odd_examples = {}


def record(Z, L):
    Z = [F(z) for z in Z]
    if 0 in Z:
        return
    from mylib import cancel_pm
    Z = cancel_pm(Z)
    if not Z:
        return
    lev = config_level(Z, Lmax=20)
    assert lev >= L, (Z, lev, L)
    io = iota(Z)
    T = len(Z)
    st = stats[(lev, T)]
    st[0] += 1
    st[1] = max(st[1], abs(io))
    if T % 2 == 0:
        if abs(io) > T - 2 * lev or T < 2 * lev + 2:
            fail.append(("B", Z, lev, io))
    else:
        odd_examples.setdefault((lev, T), (primitive(Z), io))


# generic completions (bounded number of tries)
for L, comp, nfix in [(2, complete_L2, 2), (3, complete_L3, 3)]:
    for T in range(nfix + 1, 13):
        for _ in range(3000 if L == 2 else 1500):
            free = [rnd() for _ in range(T - nfix)]
            if 0 in free:
                continue
            Z = comp(free)
            if Z is not None:
                record(Z, L)
# lambda-combinations Z = A u lam*B of "odd-moment" pieces (s_1=0 for L=2; s_1=s_3=0 for L=3)
def zero_sum_piece(k):
    W = [rnd() for _ in range(k - 1)]
    return W + [-sum(W)]
odd_pieces = []
pg = defaultdict(list)
for k in range(1, 5):
    for ms in itertools.combinations_with_replacement(range(1, 25), k):
        pg[(k, sum(ms), sum(x ** 3 for x in ms))].append(ms)
for lst in pg.values():
    for X, Y in itertools.combinations(lst, 2):
        if not set(X) & set(Y):
            odd_pieces.append([F(x) for x in X] + [F(-y) for y in Y])
print(f"    {len(odd_pieces)} primitive odd-moment pieces (equal P1,P3, entries <= 24, size <= 4 per side)")
for _ in range(20000):
    A = zero_sum_piece(random.randint(2, 6)); B = zero_sum_piece(random.randint(2, 6))
    sa, sb = psum(A, -1) if 0 not in A else 0, psum(B, -1) if 0 not in B else 0
    if 0 in A or 0 in B or sa == 0 or sb == 0:
        continue
    record(A + [-sb / sa * x for x in B], 2)
for _ in range(20000):
    cA = rnd(); A = [x * cA for x in random.choice(odd_pieces)]; B = random.choice(odd_pieces)
    if cA == 0:
        continue
    sa, sb = psum(A, -1), psum(B, -1)
    if sa == 0 or sb == 0:
        continue
    record(A + [-sb / sa * x for x in B], 3)
print("(B) random exact rational configurations (count, max|iota|) per (L, T):")
for (L, T), (c, w) in sorted(stats.items()):
    tag = "" if T % 2 == 0 else "   <-- ODD size"
    print(f"    L={L} T={T:2d}: {c:3d} configs, max |iota| = {w}, T-2L = {T - 2 * L}{tag}")

# ---------------- (C) odd-size configurations ----------------
print("(C) odd-size L-configurations (Definition 1.1 allows them):")
for (lev, T), (Z, io) in sorted(odd_examples.items()):
    print(f"    L>={lev} T={T}: Z = {Z}, iota = {io}, Lemma 1.2(4) 'T even, T>=2L+2' fails"
          + (f"; also T < 2L+2" if T < 2 * lev + 2 else ""))
Z5 = [-24, -18, -8, 5, 45]
assert psum(Z5, 1) == 0 and psum(Z5, -1) == 0 and not has_pm_pair(Z5)
print(f"    explicit: Z = {Z5}: s_1 = s_-1 = 0, no +-pair, T = 5 < 2L+2 = 6 for L = 2, iota = {iota(Z5)}")
print("    => as written, tau_2 <= 5 < 6 = 2L+2, contradicting Definition 1.3's '2L+2 <= tau_L'.")
print("       (Not realisable by orbifolds: |U|-|V| must be even.  Fix: require T even in Def. 1.1.)")

if fail:
    print("THEOREM 2.1 FAILURES:", fail[:10])
    sys.exit(1)
print("Theorem 2.1 (even T): no counterexample found.  Lemma 1.2(4) as stated for Def. 1.1: BROKEN (odd T).")
sys.exit(2 if odd_examples else 0)
