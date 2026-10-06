"""Definition 1.1 and Lemma 1.2 (dictionary), items 1-5, exact.

Input used for item 2 (as the statement does): [Sig] Lemma 4 / (4.1):
  H_L equal  <=>  2g+n-R(m) = 2g'+n'-R(m')  and  Psi_k(m)=Psi_k(m') for 1<=k<=L-1,
  Psi_k(m) = P_{2k-1}(m) - R(m).
Configurations: all integer configurations from confenum (exhaustive in the stated ranges),
reduced to primitive form, in both sign normalisations.
Exits nonzero on failure.
"""
import sys
from fractions import Fraction as F
from math import gcd
from functools import reduce
from collections import Counter
import confenum as C

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("FAIL:", msg)


def area2pi(g, orders):
    return 2 * g - 2 + sum(1 - F(1, m) for m in orders)


def Psi(k, m):
    return sum(F(x) ** (2 * k - 1) for x in m) - sum(F(1, x) for x in m)


def share(sig1, sig2, L):
    (g, m), (h, mm) = sig1, sig2
    if 2 * g + len(m) - sum(F(1, x) for x in m) != 2 * h + len(mm) - sum(F(1, x) for x in mm):
        return False
    return all(Psi(k, m) == Psi(k, mm) for k in range(1, L))


def realise(Z):
    """Lemma 1.2(2): U=Z_{>0}, V=-Z_{<0}, g-g'=-iota/2, smaller genus least with both
    hyperbolic.  Returns (g, U without ALL its 1s), (g', V without all 1s), gmin."""
    U = [z for z in Z if z > 0]; V = [-z for z in Z if z < 0]
    io = len(U) - len(V)
    d = -io // 2                     # g - g'
    mU = [u for u in U if u != 1]; mV = [v for v in V if v != 1]
    for gmin in range(0, 50):
        g, gp = (gmin, gmin - d) if d <= 0 else (gmin + d, gmin)
        if area2pi(g, mU) > 0 and area2pi(gp, mV) > 0:
            return (g, tuple(sorted(mU))), (gp, tuple(sorted(mV))), gmin
        # equal area => both hyperbolic or neither
        check((area2pi(g, mU) > 0) == (area2pi(gp, mV) > 0), f"hyperbolicity differs {Z}")
    raise RuntimeError("no genus works")


def primitive(Z):
    g = reduce(gcd, [abs(z) for z in Z])
    return tuple(sorted(z // g for z in Z))


def main():
    # Definition 1.1: the odd example
    E = (-24, -18, -8, 5, 45)
    check(C.ps(E, 1) == 0 and C.ps(E, -1) == 0, "odd example")
    print("Def 1.1 odd example {-24,-18,-8,5,45}: s_1 =", C.ps(E, 1), " s_{-1} =", C.ps(E, -1))

    Zs = set()
    for H, T in [(22, 8), (15, 10), (10, 12)]:
        for Z in C.enumerate_configs(H, T):
            Zs.add(primitive(Z))
    Zs = sorted(Zs)
    print("primitive integer configurations tested (both signs):", len(Zs))
    stats = Counter()
    examples = {}
    for Z in Zs:
        T = len(Z); io = C.iota(Z); Lz = C.maxL(Z)
        # item 1: scaling
        for lam in (F(-3), F(1, 2), F(-2, 7)):
            W = tuple(lam * z for z in Z)
            check(C.is_config(W, Lz) and len(W) == T and C.iota(W) == (1 if lam > 0 else -1) * io,
                  f"item 1 {Z} {lam}")
        # item 4
        check(T % 2 == 0 and T >= 2 * Lz + 2, f"item 4 {Z}")
        # item 2
        s1, s2, gmin = realise(Z)
        stats[("gmin", gmin, "iota0" if io == 0 else "iota!=0")] += 1
        if gmin >= 1:
            examples.setdefault(("gmin", gmin, io == 0), (Z, s1, s2))
        check(gmin <= 1, f"smaller genus > 1 needed {Z}")
        check(s1 != s2, f"item 2 signatures equal {Z}")
        check(area2pi(*s1) == area2pi(*s2), f"item 2 area {Z}")
        check(s1[0] - s2[0] == -io // 2, f"item 2 genus difference {Z}")
        for L in range(1, Lz + 1):
            check(share(s1, s2, L), f"item 2 share L={L} {Z}")
        exactly = share(s1, s2, Lz) and not share(s1, s2, Lz + 1)
        check(exactly == (C.ps(Z, 2 * Lz - 1) != 0), f"item 2 exactly-L {Z}")
        check(exactly, f"maxL definition {Z}")
        # item 3
        check((s1[0] != s2[0]) == (io != 0), f"item 3 genus {Z}")
        if io == 0:
            ncone_differ = len(s1[1]) != len(s2[1])
            check(ncone_differ == (1 in Z or -1 in Z), f"item 3 cone counts {Z}")
            mult1 = max(Z.count(1), Z.count(-1))
            check(abs(len(s1[1]) - len(s2[1])) == mult1, f"item 3 difference = multiplicity of 1 {Z}")
            if mult1 >= 2:
                examples.setdefault("1 with multiplicity >=2, iota=0", (Z, s1, s2))
        if max(Z.count(1), Z.count(-1)) >= 2:
            examples.setdefault("1 with multiplicity >=2", (Z, s1, s2))
        # item 5
        A = area2pi(*s1)
        if io != 0:
            check(A < T, f"item 5 Area<2piT {Z}")
            stats[("max Area/(2pi T), iota!=0",)] = max(stats[("max Area/(2pi T), iota!=0",)], A / T)
        else:
            V = [-z for z in Z if z < 0]
            g0 = area2pi(0, [v for v in V if v != 1])
            if g0 > 0:
                check(gmin == 0, f"genus-0 hyperbolic but gmin>0 {Z}")
                check(A == -2 + sum(1 - F(1, v) for v in V) and A < F(T, 2) - 2, f"item 5 iota=0 {Z}")
            else:
                stats[("iota=0 and genus-0 realisation NOT hyperbolic",)] += 1
                examples.setdefault("iota=0, genus 0 not hyperbolic", (Z, s1, s2, A))
                check(A < F(T, 2), f"genus-1 area {Z}")
    for k, v in sorted(stats.items(), key=str):
        print("  ", k, v)
    print("examples:")
    for k, v in examples.items():
        print("  ", k, ":", v)

    # L = 1: Definition 1.1 with 2L-3 = -1 (no odd conditions) -- exhaustive small range
    Z1 = C.enumerate_configs(8, 6, Lmin=1)
    g1 = {}; g1ex = {}
    c1 = Counter((len(Z), C.iota(Z)) for Z in Z1)
    for Z in Z1:
        check(C.is_config(Z, 1), f"L=1 enum {Z}")
        check(abs(C.iota(Z)) <= len(Z) - 2 and len(Z) >= 4, f"L=1 Thm 2.1 / size {Z}")
        s1, s2, gmin = realise(Z)
        check(area2pi(*s1) == area2pi(*s2) and s1 != s2, f"L=1 item 2 {Z}")
        g1[(gmin, C.iota(Z) == 0)] = g1.get((gmin, C.iota(Z) == 0), 0) + 1
        if gmin == 1:
            g1ex.setdefault(C.iota(Z) == 0, (Z, s1, s2))
    print("L=1 (entries<=8, T<=6): ", len(Z1), "configurations; (T,iota) counts", sorted(c1.items()))
    print("   e.g.", Z1[0], "-> min size", min(len(Z) for Z in Z1))
    print("L=1: (smaller genus, iota==0) counts:", g1, "; gmin=1 examples:", g1ex)
    # L>=2: the genus-0 realisation is always hyperbolic (proof in REVIEW.md); confirmed above:
    check(all(k[1] == 0 for k in stats if k[0] == "gmin"), "L>=2 needs genus 1")
    print("L>=2 (all tested): smaller genus is always 0")
    # L=1, T=2 impossible: {a,b}, 1/a+1/b=0 forces b=-a
    print("FAILURES:", len(FAIL))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
