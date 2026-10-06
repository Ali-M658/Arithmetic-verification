"""Theorem 3.1 (pencil) and Proposition 2.3(c), exact.

Notation: m>=4; m even: r=m-1, k0=m-2; m odd: r=m, k0=m-3.
Hypotheses: A != B m-multisets of nonzero rationals, e_k(A)=e_k(B)=0 for odd k<r,
e_k(A)=e_k(B) for k != k0.
Part 1 (sympy, generic coefficients, m=4..10): with c the free odd coefficient,
   prod_{z in Z}(x - z) has every odd-degree coefficient zero except x^3, which is
   +-c*kappa; this gives the conclusions for every m in the range.
Part 2: exhaustive box searches for pairs (A,B) of integers, m=4..8, all conclusions checked.
Part 3: the 'Equivalently' clause: the product identity alone (without the first bullet)
   does not give the conclusion -- explicit counterexample.
Part 4: degenerate cases (internal pair, empty Z, kappa=0).
Exits nonzero on failure.
"""
import sys, time
from fractions import Fraction as F
from itertools import combinations_with_replacement, combinations
from collections import Counter
import sympy as sp
import confenum as C
from check_descartes import poly_from_roots

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("FAIL:", msg)


def params(m):
    return (m - 1, m - 2) if m % 2 == 0 else (m, m - 3)


def ek(A):
    """e_0..e_m exactly"""
    c = poly_from_roots(A)
    return [c[k] * (-1) ** k for k in range(len(c))]


# ---------------- Part 1: symbolic identity -----------------
def part1():
    x, kap, c = sp.symbols("x kappa c")
    for m in range(4, 11):
        r, k0 = params(m)
        # p_A(x) = x^m + sum_k (-1)^k e_k x^{m-k}; odd k<r vanish.
        es = {k: sp.Symbol(f"e{k}") for k in range(1, m + 1)}
        for k in range(1, r, 2):
            es[k] = 0
        oddfree = [k for k in range(1, m + 1) if k % 2 == 1 and k >= r]
        assert len(oddfree) == 1, (m, oddfree)          # the single free odd e_k is c
        es[oddfree[0]] = c
        pA = x ** m + sum((-1) ** k * es[k] * x ** (m - k) for k in range(1, m + 1))
        pB = sp.expand(pA - kap * x ** (m - k0))
        # Z = A (+) (-B): prod (x - z) = pA(x) * prod (x + b) = pA(x) * (-1)^m pB(-x)
        q = sp.expand(pA * (-1) ** m * pB.subs(x, -x))
        poly = sp.Poly(q, x)
        odd = {d: sp.factor(poly.coeff_monomial(x ** d)) for d in range(1, 2 * m, 2)}
        nz = {d: v for d, v in odd.items() if v != 0}
        check(set(nz) == {3}, f"m={m}: odd coefficients {nz}")
        check(sp.simplify(nz[3] - sp.sign(nz[3].subs({c: 1, kap: 1})) * c * kap) == 0,
              f"m={m}: x^3 coefficient {nz[3]}")
        # B-condition: e_k(B) for odd k<r vanish as well (k0 even)
        check(k0 % 2 == 0, f"k0 parity m={m}")
        print(f"m={m}: r={r}, k0={k0}; odd part of prod_Z(x-z) = {nz[3]} * x^3 "
              f"(free odd coefficient c = e_{oddfree[0]})")
    print("=> e_k(Z)=0 for every odd k except k=2m-3; hence s_j(Z)=0 for odd j<=2m-5,"
          " s_{-1}(Z)=e_{2m-1}/e_{2m}=0, s_{2m-3}(Z)=(2m-3)e_{2m-3}(Z) = +-(2m-3) c kappa.")


# ---------------- Part 2: box searches -----------------
def cancel(Z):
    cnt = Counter(Z)
    for z in list(cnt):
        if z > 0 and -z in cnt:
            k = min(cnt[z], cnt[-z]); cnt[z] -= k; cnt[-z] -= k
    return tuple(sorted(z for z, k in cnt.items() for _ in range(k)))


def sets_with_odd_zero(m, r, H, splits):
    """all A of m nonzero integers, |a|<=H, with e_k(A)=0 (equivalently s_k(A)=0) for odd
    k<r, A = X (+) -Y with (|X|,|Y|) in splits; meet in the middle on (s_1,s_3,..)."""
    js = list(range(1, r, 2))
    out = set()
    for p in splits:
        q = m - p
        D = {}
        for X in combinations_with_replacement(range(1, H + 1), p):
            D.setdefault(tuple(sum(u ** j for u in X) for j in js), []).append(X)
        for Y in combinations_with_replacement(range(1, H + 1), q):
            for X in D.get(tuple(sum(u ** j for u in Y) for j in js), []):
                A = tuple(sorted(list(X) + [-y for y in Y]))
                out.add(A); out.add(tuple(sorted(-a for a in A)))
    return sorted(out)


def check_pair(m, A, B, stats, examples):
    r, k0 = params(m)
    eA, eB = ek(A), ek(B)
    for k in range(1, r, 2):
        check(eA[k] == 0 and eB[k] == 0, f"hyp1 {A} {B}")
    for k in range(1, m + 1):
        if k != k0:
            check(eA[k] == eB[k], f"hyp2 {A} {B}")
    kappa = eA[k0] - eB[k0]                 # coefficient of x^{m-k0} in pA - pB ((-1)^k0 = 1)
    check(kappa != 0, f"kappa=0 but A!=B {A} {B}")
    # 'equivalently': pA - pB = kappa x^{m-k0}
    cA = poly_from_roots(A); cB = poly_from_roots(B)
    diff = [a - b for a, b in zip(cA, cB)]
    check(all(d == 0 for i, d in enumerate(diff) if i != k0) and diff[k0] == kappa,
          f"product identity {A} {B}")
    Z0 = tuple(sorted(list(A) + [-b for b in B]))
    Z = cancel(Z0)
    cfree = eA[r] if m % 2 == 0 else eA[m]
    if not Z:
        stats["empty"] += 1
        check(m % 2 == 0 and cfree == 0, f"empty but c != 0 {A} {B}")
        return
    check(len(Z) == len(Z0) == 2 * m, f"cancellation/size {A} {B} -> {Z}")
    check(C.is_config(Z, m - 1), f"not an (m-1)-configuration {A} {B}")
    check(C.iota(Z) == 0, f"iota != 0 {A} {B}")
    check(C.iota(A) == C.iota(B), f"iota(A) != iota(B) {A} {B}")
    s = C.ps(Z, 2 * m - 3)
    check(s != 0 and abs(s) == (2 * m - 3) * abs(cfree * kappa), f"s_(2m-3) {A} {B}")
    both = any(a > 0 for a in A) and any(a < 0 for a in A)
    stats["nonempty"] += 1
    stats[f"iota(A)={C.iota(A)}"] += 1
    examples.setdefault(m, (A, B, kappa, Z))


def part2():
    plan = [  # (m, H, splits, label)
        (4, 40, [1, 2, 3], "all splits"),
        (5, 150, [2, 3], "splits (2,3),(3,2): by Prop 2.3(a) these are the only ones"),
        (6, 45, [2, 3, 4], "splits (2,4),(3,3),(4,2)"),
        (7, 60, [3, 4], "splits (3,4),(4,3): by Prop 2.3(a) the only ones"),
        (8, 30, [3, 4, 5], "splits (3,5),(4,4),(5,3)"),
    ]
    for m, H, splits, label in plan:
        t0 = time.time()
        r, k0 = params(m)
        sets = sets_with_odd_zero(m, r, H, splits)
        groups = {}
        for A in sets:
            e = ek(A)
            groups.setdefault(tuple(e[k] for k in range(1, m + 1) if k != k0), []).append(A)
        stats = Counter(); examples = {}
        npairs = 0
        for g in groups.values():
            for A, B in combinations(g, 2):
                npairs += 1
                check_pair(m, A, B, stats, examples)
        print(f"m={m} (r={r}, k0={k0}), entries<={H}, {label}: {len(sets)} sets A, "
              f"{npairs} pairs; {dict(stats)}  [{time.time()-t0:.1f}s]")
        if m in examples:
            A, B, kappa, Z = examples[m]
            print(f"    e.g. A={A} B={B} kappa={kappa}\n         Z={Z}")


# ---------------- Part 3: 'Equivalently' clause -----------------
def part3():
    # m=4: product identity pA - pB = kappa x^2 WITHOUT e_1 = 0
    m = 4; H = 25
    groups = {}
    for A in combinations_with_replacement([a for a in range(-H, H + 1) if a != 0], m):
        e = ek(A)
        groups.setdefault((e[1], e[3], e[4]), []).append(A)
    found = None; n = 0
    for g in groups.values():
        for A, B in combinations(g, 2):
            n += 1
            if ek(A)[1] != 0:
                Z = cancel(tuple(sorted(list(A) + [-b for b in B])))
                if Z and not C.is_config(Z, 3):
                    found = (A, B, Z); break
        if found:
            break
    check(found is not None, "no counterexample to the 'Equivalently' clause found")
    A, B, Z = found
    cA = poly_from_roots(A); cB = poly_from_roots(B)
    print("Part 3 ('Equivalently'): A =", A, " B =", B)
    print("   pA - pB =", [a - b for a, b in zip(cA, cB)], "(only x^2 term) but e_1(A) =",
          ek(A)[1], "; Z = A (+) -B =", Z, ": s_1 =", C.ps(Z, 1), " s_3 =", C.ps(Z, 3),
          " s_-1 =", C.ps(Z, -1), "-> not a 3-configuration")


# ---------------- Part 4: degenerate cases -----------------
def part4():
    A = (-2, -1, 1, 2)                       # contains pairs, e_3(A)=c=0
    x = sp.symbols("x")
    pA = sp.expand((x - 1) * (x + 1) * (x - 2) * (x + 2))
    pB = sp.expand(pA - sp.Rational(45, 4) * x ** 2)     # chosen so that B = {+-4, +-1/2}
    rts = sp.roots(sp.Poly(pB, x))
    B = tuple(sorted(F(str(k)) for k, mult in rts.items() for _ in range(mult)))
    check(B == (F(-4), F(-1, 2), F(1, 2), F(4)), f"part4 B {B}")
    Z = cancel(tuple(sorted([F(a) for a in A] + [-b for b in B])))
    check(Z == (), "symmetric pencil pair should cancel completely")
    print("Part 4: A = {+-1,+-2}, B = {+-1/2,+-4} (m=4, c=e_3=0): A (+) -B cancels to the empty set")
    # m odd: an internal pair is impossible because pA(z)+pA(-z) = -2 e_m != 0; m even:
    # pA(z)-pA(-z) = -2 c z, so an internal pair forces c=0 and then A, B are symmetric.
    z, c = sp.symbols("z c")
    for m in (4, 5, 6, 7):
        r, k0 = params(m)
        es = {k: sp.Symbol(f"e{k}") for k in range(1, m + 1)}
        for k in range(1, r, 2):
            es[k] = 0
        pA = lambda t: t ** m + sum((-1) ** k * es[k] * t ** (m - k) for k in range(1, m + 1))
        expr = sp.expand(pA(z) - pA(-z)) if m % 2 == 0 else sp.expand(pA(z) + pA(-z))
        print(f"   m={m}: pA(z) {'-' if m % 2 == 0 else '+'} pA(-z) =", expr)
    print("   kappa = 0 forces pA = pB, i.e. A = B, excluded by hypothesis.")


if __name__ == "__main__":
    part1()
    part3()
    part4()
    part2()
    print("FAILURES:", len(FAIL))
    sys.exit(1 if FAIL else 0)
