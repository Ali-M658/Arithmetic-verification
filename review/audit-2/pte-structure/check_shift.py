"""Proposition 3.2 (shift), exact.
[X] =_k [Y]: s_j(X)=s_j(Y) for 1<=j<=k;  Z(c) = (X+c) (+) (-(Y+c)),  c notin -X u -Y.
 1. s_j(Z(c)) = 0 for odd j <= 2L-3 (k >= 2L-3)
 2. iota(Z(c)) = 2(#{x>-c} - #{y>-c}); 0 for c > -min(X u Y); nonzero on an open interval
 3. rho(c) = s_{-1}(Z(c)) is a nonzero rational function of c
PTE solutions are found by the reviewer's own exhaustive search (entries 0..B).
Exits nonzero on failure.
"""
import sys
from fractions import Fraction as F
from itertools import combinations_with_replacement
import sympy as sp
import confenum as C

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("FAIL:", msg)


def pte_solutions(n, k, B):
    """pairs (X,Y) of disjoint n-multisets of integers in [0,B], X<Y, equal s_1..s_k"""
    D = {}
    for X in combinations_with_replacement(range(B + 1), n):
        D.setdefault(tuple(sum(x ** j for x in X) for j in range(1, k + 1)), []).append(X)
    out = []
    for g in D.values():
        for i in range(len(g)):
            for j in range(i + 1, len(g)):
                if not set(g[i]) & set(g[j]):
                    out.append((g[i], g[j]))
    return out


def Zc(X, Y, c):
    return tuple(sorted([x + c for x in X] + [-(y + c) for y in Y]))


def test(X, Y, k):
    n = len(X)
    pts = sorted(set(X) | set(Y))
    # sample c: all midpoints, points beyond the ends, and random rationals
    cs = set()
    for a, b in zip(pts, pts[1:]):
        cs.add(-F(a + b, 2))
    cs |= {-F(pts[0]) + F(1, 3), -F(pts[0]) + 5, -F(pts[-1]) - F(1, 7), -F(pts[-1]) - 4}
    cs |= {F(p, q) for p in range(-3 * max(pts) - 3, 4) for q in (1, 2, 5) if F(p, q) not in
           {F(-x) for x in pts}}
    nonzero_interval = None
    for c in cs:
        if c in {F(-x) for x in pts}:
            continue
        Z = Zc(X, Y, c)
        check(0 not in Z, "zero element")
        for j in range(1, k + 1, 2):
            check(C.ps(Z, j) == 0, f"item 1 X={X} Y={Y} c={c} j={j}")
        io = C.iota(Z)
        check(io == 2 * (sum(1 for x in X if x > -c) - sum(1 for y in Y if y > -c)),
              f"item 2 formula {X} {Y} {c}")
        if c > -min(pts):
            check(io == 0, f"item 2 zero for c > -min {X} {Y} {c}")
    # open intervals of c: between consecutive points t of X u Y (t = -c)
    for a, b in zip(pts, pts[1:]):
        t = F(a + b, 2)
        f = sum(1 for x in X if x > t) - sum(1 for y in Y if y > t)
        if f != 0:
            nonzero_interval = (-F(b), -F(a), 2 * f)
            break
    check(nonzero_interval is not None, f"item 2 no nonzero interval {X} {Y}")
    cc = sp.symbols("c")
    rho = sp.together(sum(1 / (x + cc) for x in X) - sum(1 / (y + cc) for y in Y))
    num, den = sp.fraction(rho)
    check(sp.expand(num) != 0, f"item 3 rho == 0 {X} {Y}")
    # rational zeros of rho and the configurations they produce
    zs = [r for r in sp.Poly(sp.expand(num), cc).all_roots() if r.is_rational] if sp.degree(num, cc) > 0 else []
    made = []
    for r in zs:
        c = F(int(r.p), int(r.q))
        if c in {F(-x) for x in pts}:
            continue
        Z = Zc(X, Y, c)
        s = set(Z)
        nopair = not any(-z in s for z in s)
        made.append((c, C.iota(Z), nopair))
    return nonzero_interval, sp.factor(num), made


def main():
    # n = 1 is impossible for k >= 1
    check(pte_solutions(1, 1, 30) == [], "n=1 PTE")
    print("n=1: no PTE solution of degree >= 1 (x = y forced)")
    for (n, k, B, L) in [(2, 1, 12, 2), (3, 2, 12, 2), (4, 3, 10, 3), (3, 1, 6, 2)]:
        sols = pte_solutions(n, k, B)
        print(f"n={n}, k={k} (L<={(k+3)//2}), entries 0..{B}: {len(sols)} disjoint solutions")
        genus_changing = 0
        if len(sols) > 80:
            sols = sols[:40] + sols[-40:]
            print("   (testing the first 40 and last 40)")
        for idx, (X, Y) in enumerate(sols):
            iv, num, made = test(X, Y, k)
            genus_changing += sum(1 for (c, io, np_) in made if io != 0 and np_)
            if idx < 2:
                print(f"   X={X} Y={Y}: iota=2f on c in ({iv[0]},{iv[1]}) is {iv[2]}; "
                      f"numerator of rho = {num}; rational zeros -> (c, iota, no pair) {made}")
        print(f"   rational zeros of rho giving a pair-free configuration with iota != 0: {genus_changing}")
    print("FAILURES:", len(FAIL))
    sys.exit(1 if FAIL else 0)


main()
