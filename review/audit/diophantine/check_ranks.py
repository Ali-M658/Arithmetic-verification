"""PARI/GP 2.17.2 certification of ranks and torsion (DI.6, DI.7, DI.11) on the OWN model.

Own model (check_algebra.py): E_lam : W^2 = s(s^2 + (lam^2-6lam-3)s + 16lam), s = -4e2/z^2.
For lam = p/q the integral model is Y^2 = X(X^2 + (p^2-6pq-3q^2)X + 16pq^3), X = q^2 s, Y = q^3 W.

Run from the repository root:
    review/audit/.venv-pari/bin/python review/audit/diophantine/check_ranks.py
"""
import os
import sys
from fractions import Fraction as Fr
from itertools import permutations

import cypari2

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dio_common import (add, normalize, lam_of, to_weier, is_positive, check, finish, Fail, F)  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_ranks.txt")
log = []
pari = cypari2.Pari()
pari.allocatemem(2 * 10 ** 9)


def model(lam):
    p, q = lam.numerator, lam.denominator
    return [0, p * p - 6 * p * q - 3 * q * q, 0, 16 * p * q ** 3, 0]


def plane_to_E(lam, P):
    """image of a plane point with z != 0 on the integral model, as [X, Y] (exact)."""
    s, W = to_weier(lam, P)
    q = lam.denominator
    return [s * q * q, W * q ** 3]


def topari(pt):
    return pari(f"[{pt[0]}, {pt[1]}]")


try:
    ver = pari("version()")
    check([int(v) for v in ver][:3] == [2, 17, 2], f"PARI version {ver}", log)
    log.append(f"     cypari2 {cypari2.__version__ if hasattr(cypari2, '__version__') else '?'}")

    # ---------------- DI.7: C_27/2 --------------------------------------------------------
    lam = Fr(27, 2)
    ai = model(lam)
    check(ai == [0, 393, 0, 3456, 0], f"integral own model of C_27/2 = {ai} (as in the manuscript)", log)
    E = pari.ellinit(ai)
    N = pari.ellglobalred(E)[0]
    rk = pari.ellrank(E)
    log.append(f"     conductor {N}; ellrank(E) = {rk}")
    check(int(rk[0]) == 0 and int(rk[1]) == 0 and int(rk[2]) == 0, "ellrank: r1 = r2 = 0, s = 0", log)
    tor = pari.elltors(E)
    log.append(f"     elltors(E) = {tor}")
    check(int(tor[0]) == 12 and [int(c) for c in tor[1]] == [6, 2], "torsion order 12, structure Z/6 x Z/2", log)
    ar = pari.ellanalyticrank(E)
    log.append(f"     ellanalyticrank(E) = {ar}  (L(E,1) != 0; with modularity + Kolyvagin this independently gives rank 0)")
    check(int(ar[0]) == 0 and float(ar[1]) > 0.1, "analytic rank 0, L(E,1) far from 0", log)
    log.append(f"     ellrootno(E) = {pari.ellrootno(E)}")
    # all 12 torsion points of E
    torpts = set()
    gens = tor[2]
    g1, g2 = gens[0], gens[1]
    for i in range(6):
        for j in range(2):
            P = pari.elladd(E, pari.ellmul(E, g1, i), pari.ellmul(E, g2, j))
            torpts.add(str(P))
    check(len(torpts) == 12, "elltors generators produce 12 distinct points", log)
    # the 12 plane points found independently in check_groups.py
    plane12 = [(0, 0, 1), (0, 1, -1), (0, 1, 0), (1, -1, 0), (1, 0, -1), (1, 0, 0),
               (1, 1, 4), (1, 4, 1), (1, 4, 4), (4, 1, 1), (4, 1, 4), (4, 4, 1)]
    for P in plane12:
        check(F(lam, P) == 0, f"{P} on C_27/2", [])
    img = {}
    for P in plane12:
        if P[2] != 0:
            img[P] = topari(plane_to_E(lam, P))
    img[(1, -1, 0)] = pari("[0]")
    # z = 0 points via the group law: X = A + B in the plane group with A, B having z != 0
    for Pz in [(1, 0, 0), (0, 1, 0)]:
        done = False
        for A in plane12:
            for B in plane12:
                if A[2] != 0 and B[2] != 0 and add(lam, A, B) == normalize(Pz):
                    img[Pz] = pari.elladd(E, img[A], img[B])
                    done = True
                    break
            if done:
                break
        check(done, f"image of {Pz} obtained through the group law", log)
    imgs = {str(v) for v in img.values()}
    for P, v in img.items():
        check(int(pari.ellisoncurve(E, v)) == 1, f"image of {P} = {v} lies on E", [])
    check(imgs == torpts, "the 12 plane points map bijectively onto E(Q)_tors (= E(Q), rank 0)", log)
    pos = sorted(P for P in plane12 if is_positive(P))
    exp = sorted({p for t in [(1, 4, 4), (1, 1, 4)] for p in set(permutations(t))})
    check(pos == exp, f"positive rational points of C_27/2: {pos} = permutations of (1,4,4),(1,1,4)", log)
    # group-law compatibility check: map is a homomorphism on a few pairs
    for A in [(1, 4, 4), (0, 0, 1), (4, 1, 4)]:
        for B in [(1, 1, 4), (0, 1, -1)]:
            C = add(lam, A, B)
            check(str(pari.elladd(E, img[A], img[B])) == str(img[C]), f"map respects addition: {A}+{B}={C}", [])
    log.append("PASS plane-cubic group law and PARI group law agree on test sums")

    # ---------------- DI.6/DI.11: fibre curves ----------------------------------------------
    fibres = {
        "S=136": [(15, 55, 66), (16, 40, 80), (17, 34, 85)],
        "S=1849": [(168, 820, 861), (172, 645, 1032), (185, 480, 1184), (215, 344, 1290), (253, 276, 1320)],
        "S=4600": [(750, 1750, 2100), (756, 1674, 2170), (800, 1400, 2400), (805, 1380, 2415), (882, 1170, 2548),
                   (920, 1104, 2576)],
        "Thm3": [(4, 9, 18)],
    }
    claimed = {"S=136": 2, "S=1849": 3, "S=4600": 3, "Thm3": 2}
    for name, trips in fibres.items():
        lams = {lam_of(t) for t in trips}
        check(len(lams) == 1, f"{name}: all listed triples have the same lambda = {lams}", log)
        lam = lams.pop()
        if name != "Thm3":
            S = int(name.split("=")[1])
            check(all(sum(t) == S for t in trips) and len(set(trips)) == len(trips),
                  f"{name}: listed triples are distinct with sum {S}, R = {lam / S}", log)
        ai = model(lam)
        E = pari.ellinit(ai)
        rk = pari.ellrank(E)
        tor = pari.elltors(E)
        log.append(f"     {name}: lam = {lam}, model {ai}, conductor {pari.ellglobalred(E)[0]}, "
                   f"ellrank = [{rk[0]}, {rk[1]}, {rk[2]}], torsion {tor[1]}, root number {pari.ellrootno(E)}")
        check(int(rk[0]) == int(rk[1]) == claimed[name], f"{name}: PARI r1 = r2 = {claimed[name]} (proven by PARI's bounds)", log)
        check(int(tor[0]) == 6, f"{name}: torsion Z/6", log)
        # rank of the subgroup generated by the fibre's points (numerical height regulator, informative)
        pts = [topari(plane_to_E(lam, t)) for t in trips]
        for v in pts:
            check(int(pari.ellisoncurve(E, v)) == 1, "fibre point on E", [])
        H = pari.ellheightmatrix(E, pts)
        ev = [float(e) for e in pari.qfjacobi(H)[0]]
        rkH = sum(1 for e in ev if e > 1e-12 * max(ev))
        log.append(f"     {name}: eigenvalues of the height matrix: " + ", ".join(f"{e:.3e}" for e in ev))
        log.append(f"     {name}: numerical rank of the height matrix of the {len(pts)} fibre points = {rkH}")
    log.append("ALL PARI CHECKS PASSED")
    finish(log, OUT)
except Fail:
    finish(log, OUT)
    sys.exit(1)
