#!/usr/bin/env python3
"""Exact checks of the statements that are new in the arithmetic note (paper/arith/note.tex).

Everything else in the note is traced to theory/diophantine/ or review/audit/ (paper/arith/TRACE.md).
This script checks, in exact arithmetic, what those directories do not already contain:

  1. the discriminant identity (L^2-6L-3)^2 - 64L = (L-1)^3 (L-9) behind the 2-torsion criterion;
  2. for isosceles points, L-1 = 2(u+v)^2/(uv) and L-9 = 2(u-v)^2/(uv), so (L-1)(L-9) is a square;
  3. the birational map to the BGN model at L = 27/2 sends (1:4:4) to (s, eta) = (-6, 45);
  4. the factorisation identity behind the upper bound n(S) << S^(2+eps), and an independent
     recount of n(S) for S <= 160 through that identity, compared with theory/diophantine/data/per_S.csv;
  5. the count of primitive isosceles pairs with S <= 4800 (506) and the members and Lambda of the
     first classes of each size (Table 1 of the note);
  6. with --enum: the enumeration of all classes with 4801 <= S <= 6000 by the audit enumerator
     (copied to checks/enum_classes.c), compared with review/audit/threshold/check_enum.txt at
     S = 5400 and 6000, and the number of primitive classes with S <= 6000.
  7. statements added in revision: every coincidence is admissible (brute force to S = 240 and the case
     analysis of the proof); N(X) = sum over primitive pairs D of floor(X/S_D) against per_S.csv; the isosceles
     copies with k >= 1 (0.608 X at X = 4800, secondary term -0.286 X) and the threshold log X > 437.8; the
     base group from five lines through base points (O is a flex); geometric progressions of order 12, and the
     orders 4 and 12 of their orderings;
     the orders of the three orientations of an isosceles point; positive torsion points with S <= 60; the
     Ravi identity R/r = (Lambda - 1)/4; the geometric progressions of Lemma 3.

Run from the repository root:  python3 paper/arith/checks/check_note.py [--enum]
Output: paper/arith/checks/check_note.txt. Exits nonzero on any failure.
"""
from __future__ import annotations

import csv
import re
import subprocess
import sys
import tempfile
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
OUT: list[str] = []
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global FAIL
    FAIL += not ok
    OUT.append(f"{'PASS' if ok else 'FAIL'} {name}" + (f": {detail}" if detail else ""))
    print(OUT[-1], flush=True)


# 1-2. torsion criterion --------------------------------------------------------------------
L, u, v = sp.symbols("L u v", positive=True)
check("1 (L^2-6L-3)^2-64L = (L-1)^3(L-9)", sp.expand((L**2 - 6*L - 3)**2 - 64*L - (L - 1)**3*(L - 9)) == 0)
Liso = (2*u + v)*(u + 2*v)/(u*v)  # Lambda of (u:v:v) = e1 e2 / e3
check("2 isosceles Lambda = (2u+v)(u+2v)/(uv)",
      sp.simplify((u + 2*v)*(v*v + 2*u*v)/(u*v*v) - Liso) == 0)
check("2 L-1 = 2(u+v)^2/(uv)", sp.simplify(Liso - 1 - 2*(u + v)**2/(u*v)) == 0)
check("2 L-9 = 2(u-v)^2/(uv)", sp.simplify(Liso - 9 - 2*(u - v)**2/(u*v)) == 0)

# 3. birational map at Lambda = 27/2 ------------------------------------------------------
def to_bgn(x, y, z, lam):
    e2 = x*y + y*z + z*x
    s = F(-4*e2, z*z)
    eta2 = s*(s*s + (lam*lam - 6*lam - 3)*s + 16*lam)
    return s, eta2


lam = F(27, 2)
s, eta2 = to_bgn(1, 4, 4, lam)
check("3 (1:4:4) on C_{27/2}", (1 + 4 + 4)*(4 + 16 + 4) == lam*16)
check("3 s = -4 e2/z^2 = -6 and eta^2 = 45^2 at L = 27/2", s == -6 and eta2 == 45**2, f"s={s}, eta^2={eta2}")

# 4. upper-bound identity and recount ------------------------------------------------------
p, pp, A, Ap, B, Bp = sp.symbols("p pp A Ap B Bp")
d = p - pp
eqR = (1/p + A/B) - (1/pp + Ap/Bp)  # R = 1/p + (q+r)/(qr) with A = q+r, B = qr
lhs = (d*B - p*pp*A)*(d*Bp + p*pp*Ap) + p**2*pp**2*A*Ap
check("4 (dB - pp'A)(dB' + pp'A') + p^2p'^2AA' = -d pp'BB' (R - R')",
      sp.simplify(lhs + d*B*Bp*p*pp*eqR) == 0)


def divisors(n: int) -> list[int]:
    fs = sp.factorint(n)
    out = [1]
    for q, e in fs.items():
        out = [x*q**k for x in out for k in range(e + 1)]
    return out


def qr_from(Aval: int, Bval: int, pmin: int):
    disc = Aval*Aval - 4*Bval
    if disc < 0 or isqrt(disc)**2 != disc or (Aval + isqrt(disc)) % 2:
        return None
    r = (Aval + isqrt(disc))//2
    q = Aval - r
    return (q, r) if q >= pmin else None


def hyperbolic(t) -> bool:
    return F(1, t[0]) + F(1, t[1]) + F(1, t[2]) < 1


def pairs_via_identity(S: int) -> int:
    """Pairs of distinct hyperbolic triads at sum S, found only through the factorisation."""
    found = set()
    for a in range(2, S//3 + 1):            # least entry of the first triad
        for b in range(a + 1, S//3 + 1):    # least entry of the second, b > a
            dd = a - b
            Aa, Ab = S - a, S - b
            M = a*a*b*b*Aa*Ab               # (dd*B - ab*Aa)(dd*B' + ab*Ab) = -M
            for f in divisors(M):
                for sgn in (1, -1):
                    f1, f2 = sgn*f, -M//(sgn*f)
                    if (f1 + a*b*Aa) % dd or (f2 - a*b*Ab) % dd:
                        continue
                    Bv, Bpv = (f1 + a*b*Aa)//dd, (f2 - a*b*Ab)//dd
                    if Bv <= 0 or Bpv <= 0:
                        continue
                    t1, t2 = qr_from(Aa, Bv, a), qr_from(Ab, Bpv, b)
                    if t1 and t2:
                        x, y = (a, *t1), (b, *t2)
                        if hyperbolic(x) and hyperbolic(y):
                            assert F(1, a) + F(Aa, Bv) == F(1, b) + F(Ab, Bpv)
                            found.add((x, y))
    return len(found)


with open(ROOT / "theory/diophantine/data/per_S.csv") as fh:
    per_s = {int(r["S"]): r for r in csv.DictReader(fh)}
bad = [S for S in range(10, 161) if pairs_via_identity(S) != int(per_s[S]["pairs"])]
check("4 n(S) recounted through the identity equals per_S.csv for 10 <= S <= 160", not bad, f"mismatch at {bad[:5]}")

# 5. isosceles count and Table 1 -------------------------------------------------------------
iso = 0
for uu in range(1, 200):
    for vv in range(uu + 1, 4801):
        if gcd(uu, vv) != 1:
            continue
        g = gcd(2*uu + vv, uu + 2*vv)
        if (2*uu + vv)*(uu + 2*vv)//g <= 4800:
            iso += 1
check("5 primitive isosceles pairs with S <= 4800", iso == 506, str(iso))

TABLE = {
    2: (18, F(27, 2), [(2, 8, 8), (3, 3, 12)]),
    3: (136, F(68, 5), [(15, 55, 66), (16, 40, 80), (17, 34, 85)]),
    4: (408, F(68, 5), [(45, 165, 198), (48, 120, 240), (51, 102, 255), (65, 70, 273)]),
    5: (1849, F(1849, 120), [(168, 820, 861), (172, 645, 1032), (185, 480, 1184), (215, 344, 1290), (253, 276, 1320)]),
    6: (4600, F(230, 21), [(750, 1750, 2100), (756, 1674, 2170), (800, 1400, 2400), (805, 1380, 2415),
                           (882, 1170, 2548), (920, 1104, 2576)]),
}
for k, (S, lamk, mem) in TABLE.items():
    Rs = {F(1, a) + F(1, b) + F(1, c) for a, b, c in mem}
    ok = len(mem) == k and all(sum(t) == S for t in mem) and len(Rs) == 1 and S*Rs.pop() == lamk
    check(f"5 Table 1 row k={k}: common sum, common R, Lambda", ok)
first = {}
for S in range(10, 4801):
    m = int(per_s[S]["max_fibre"])
    for k in range(2, m + 1):
        first.setdefault(k, S)
check("5 first sums of classes of sizes 2..6 from per_S.csv",
      [first.get(k) for k in range(2, 7)] == [18, 136, 408, 1849, 4600] and 7 not in first, str(first))

# 6. enumeration 4801..6000 --------------------------------------------------------------------
if "--enum" in sys.argv:
    with tempfile.TemporaryDirectory() as tmp:
        exe = Path(tmp)/"enum_classes"
        subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE/"enum_classes.c")], check=True)
        res = subprocess.run([str(exe), "4801", "6000", "6000"], check=True, capture_output=True, text=True).stdout
    base = per_s[4800]
    P_, C_, PC_ = int(base["cum_pairs"]), int(base["cum_classes"]), int(base["cum_prim_classes"])
    mx, at = 0, {}
    sizes: dict[int, int] = {}
    for line in res.splitlines():
        tok = line.split()
        if tok[0] == "S":
            P_ += int(tok[5]); C_ += int(tok[7]); mx = max(mx, int(tok[9]))
            at[int(tok[1])] = (P_, C_)
        elif tok[0] == "C":
            sizes[int(tok[2])] = sizes.get(int(tok[2]), 0) + 1
            PC_ += int(tok[3])
    ref = (ROOT/"review/audit/threshold/check_enum.txt").read_text()
    for S in (5400, 6000):
        m = re.search(rf"^\s+{S}\s+(\d+)\s+\S+\s+(\d+)", ref, re.M)
        check(f"6 cumulative pairs and classes at S = {S} agree with the G5 enumeration",
              m is not None and (int(m.group(1)), int(m.group(2))) == at[S], f"{at[S]}")
    check("6 primitive classes with S <= 6000", PC_ == 62401, str(PC_))
    check("6 no class of size 7 with S <= 6000", mx == 6, f"largest {mx}; sizes 4801..6000 {sizes}")

# 7. statements added in revision ---------------------------------------------------------------
sys.path.insert(0, str(ROOT/"theory/diophantine"))
from cubic_group import Cubic, normalize as cg_norm, lam as cg_lam, O as O_PT  # noqa: E402
import math  # noqa: E402

# 7a. admissibility: a triple of positive integers sharing S and R with another one has R < 1
groups: dict = {}
for S in range(3, 241):
    for a in range(1, S//3 + 1):
        for b in range(a, (S - a)//2 + 1):
            c = S - a - b
            groups.setdefault((S, F(1, a) + F(1, b) + F(1, c)), []).append((a, b, c))
viol = [g for (S, R), g in groups.items() if len(g) > 1 and R >= 1]
check("7a every coincidence of positive triples with S <= 240 is admissible (R < 1)", not viol, str(viol[:3]))
nonadm = sorted({t for (S, R), g in groups.items() for t in g if R >= 1 and t[0] > 1 and t[:2] != (2, 2)})
check("7a the triples with R >= 1 and a >= 2 other than (2,2,c) are (2,3,3..6), (2,4,4), (3,3,3)",
      nonadm == [(2, 3, 3), (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 4, 4), (3, 3, 3)], str(nonadm))
cc = sp.symbols("c", positive=True)
check("7a (1,b,c) against (2,2,c'): discriminant (c'+3)^2 - 4c'(c'+3) = 3(c'+3)(1-c')",
      sp.expand((cc + 3)**2 - 4*cc*(cc + 3) - 3*(cc + 3)*(1 - cc)) == 0)

# 7b. every pair is k D for a unique primitive pair D, and every copy is a pair: N(X) = sum_D floor(X/S_D)
prim = {S: int(per_s[S]["prim_pairs"]) for S in per_s}
badX = [X for X in range(10, 4801)
        if sum(prim[S]*(X//S) for S in range(10, X + 1)) != int(per_s[X]["cum_pairs"])]
check("7b N(X) = sum over primitive pairs D of floor(X/S_D), 10 <= X <= 4800", not badX, str(badX[:5]))

# 7c. isosceles family with all copies: secondary term and value at 4800; threshold of Theorem 4
c_iso = 3*math.log(2)/(2*math.pi**2)


def iso_sums(X):
    out = []
    for u in range(1, X):
        if (2*u + u + 1)*(u + 2*(u + 1)) > 3*X:
            break
        v = u + 1
        while (2*u + v)*(u + 2*v) <= 3*X:
            if gcd(u, v) == 1:
                s = (2*u + v)*(u + 2*v)//gcd(2*u + v, u + 2*v)
                if s <= X:
                    out.append(s)
            v += 1
    return out


S_iso = sorted(iso_sums(10**6))
sec = {}
for X in (4800, 10**4, 10**5, 10**6):
    cnt = sum(X//s for s in S_iso if s <= X)
    sec[X] = (cnt - c_iso*X*math.log(X))/X
check("7c isosceles copies k >= 1 at X = 4800: count/X = 0.608",
      round(sum(4800//s for s in S_iso if s <= 4800)/4800, 3) == 0.608)
check("7c isosceles copies k >= 1: count - c_iso X log X = -0.286 X to three digits, X = 1e4, 1e5, 1e6",
      all(round(sec[X], 3) == -0.286 for X in (10**4, 10**5, 10**6)), str({X: round(v, 5) for X, v in sec.items()}))
thr = 128*math.pi**4*c_iso/3
check("7c Theorem 4 exceeds Theorem 3 only for log X > 128 pi^4 c_iso/3 = 437.8", abs(thr - 437.8) < 0.05, f"{thr:.3f}")

# 7d. torsion: the base group by lines; GP points of order 12; isosceles orientations; (1:1:t) of order 2
x, y, z, Lm = sp.symbols("x y z Lambda")
Fc = (x + y + z)*(x*y + y*z + z*x) - Lm*x*y*z
tang = sp.expand(Fc.subs(x, (Lm - 1)*z - y))
check("7d the tangent x + y = (Lambda-1)z at O meets C_Lambda only at O (O is a flex)",
      sp.simplify(tang - Lm*(Lm - 1)*z**3) == 0, str(sp.factor(tang)))
lines = {"z=0": Fc.subs(z, 0), "x+y+z=0": Fc.subs(z, -x - y), "y=0": Fc.subs(y, 0),
         "y+z=0": Fc.subs(z, -y), "x+y=0": Fc.subs(y, -x)}
fac = {k: sp.factor(v) for k, v in lines.items()}
check("7d line intersections: z=0, x+y+z=0, y=0, y+z=0, x+y=0",
      fac["z=0"] == sp.factor(x*y*(x + y)) and sp.simplify(fac["x+y+z=0"] - Lm*x*y*(x + y)) == 0
      and fac["y=0"] == sp.factor(x*z*(x + z)) and sp.simplify(fac["y+z=0"] - (Lm - 1)*x*y**2) == 0
      and sp.simplify(fac["x+y=0"] - (Lm - 1)*x**2*z) == 0, str(fac))
rr = sp.symbols("r", nonzero=True)
check("7d Lambda(1:r:r^2) = (r + 1 + 1/r)^2",
      sp.simplify((1 + rr + rr**2)*(rr + rr**3 + rr**2)/rr**3 - (rr + 1 + 1/rr)**2) == 0)
T2, Q3 = (0, 0, 1), (0, 1, -1)
ok12 = True
for p_, q_ in ((2, 1), (3, 1), (3, 2), (5, 3), (1, 2), (-2, 1), (-1, 3), (4, 1), (7, 5)):
    G = (q_*q_, p_*q_, p_*p_)                       # (1 : r : r^2), r = p/q
    C = Cubic(cg_lam(G)) if all(G) else None
    ok12 &= C is not None and C.order(G) == 12 and C.add(G, G) == C.add(Q3, T2) \
        and C.add(G, T2) == cg_norm((G[1]*G[2], G[0]*G[2], G[0]*G[1]))
check("7d geometric progressions (1:r:r^2) have order 12 and 2G = Q3 - T2", ok12)
ok4 = True
for p_, q_ in ((2, 1), (3, 1), (3, 2), (5, 3), (4, 1)):
    a_, b_, c_ = q_*q_, p_*q_, p_*p_                  # a geometric progression with middle term b_
    C = Cubic(cg_lam((a_, b_, c_)))
    for P in ((a_, b_, c_), (c_, b_, a_), (b_, a_, c_), (b_, c_, a_), (a_, c_, b_), (c_, a_, b_)):
        ok4 &= C.order(P) == (4 if P[2] == b_ else 12)
check("7d orderings of a geometric progression: order 4 when the middle term is last, else 12", ok4)
ok6 = True
for u_, v_ in ((1, 4), (1, 2), (2, 3), (3, 5), (5, 2), (1, 7)):
    C = Cubic(cg_lam((u_, v_, v_)))
    ok6 &= C.order((u_, v_, v_)) == 6 and C.order((v_, u_, v_)) == 6 and C.order((v_, v_, u_)) == 2
check("7d isosceles orientations: (u:v:v), (v:u:v) of order 6, (v:v:u) of order 2", ok6)
# positive torsion points with sum <= 60 are exactly the isosceles triples and the geometric progressions
okt = True
for S in range(3, 61):
    for a in range(1, S//3 + 1):
        for b in range(a, (S - a)//2 + 1):
            c = S - a - b
            if gcd(gcd(a, b), c) != 1 or a == b == c:
                continue
            tors = Cubic(cg_lam((a, b, c))).order((a, b, c)) is not None
            okt &= tors == (a == b or b == c or b*b == a*c)
check("7d a positive primitive triple with S <= 60 is torsion iff isosceles or a geometric progression", okt)

# 7e. Ravi substitution: R/r of the triangle with sides y+z, z+x, x+y equals (Lambda - 1)/4
f_, g_, h_ = y + z, z + x, x + y
Rr = 2*f_*g_*h_/((f_ + g_ - h_)*(f_ + h_ - g_)*(g_ + h_ - f_))
check("7e R/r = (Lambda - 1)/4 under the Ravi substitution",
      sp.simplify(Rr - ((x + y + z)*(x*y + y*z + z*x)/(x*y*z) - 1)/4) == 0)

# 7f. Lemma 3: (u, vq, vr) is a geometric progression iff u/v is sqrt(qr), q^2/r or r^2/q
okgp = True
for q_ in range(1, 9):
    for r_ in range(q_, 13):
        if gcd(q_, r_) != 1:
            continue
        for u_ in range(1, 40):
            for v_ in range(1, 40):
                if gcd(u_, v_) != 1:
                    continue
                t = sorted((u_, v_*q_, v_*r_))
                gp = t[1]**2 == t[0]*t[2]
                ratio = F(u_, v_)
                cand = ratio**2 == q_*r_ or ratio == F(q_*q_, r_) or ratio == F(r_*r_, q_)
                okgp &= gp == cand
check("7f (u, vq, vr) is a geometric progression iff u/v in {sqrt(qr), q^2/r, r^2/q}", okgp)

(HERE/"check_note.txt").write_text("\n".join(OUT) + f"\n\n{len(OUT)} checks, {FAIL} failures\n")
print(f"\n{len(OUT)} checks, {FAIL} failures")
sys.exit(1 if FAIL else 0)
