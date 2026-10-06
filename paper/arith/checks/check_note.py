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

(HERE/"check_note.txt").write_text("\n".join(OUT) + f"\n\n{len(OUT)} checks, {FAIL} failures\n")
print(f"\n{len(OUT)} checks, {FAIL} failures")
sys.exit(1 if FAIL else 0)
