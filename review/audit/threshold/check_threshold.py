#!/usr/bin/env python3
"""Referee check of the threshold results TH.0-TH.6 and the paper-core threshold items
PC.11-PC.16 (G5 audit).  Exact arithmetic throughout.  Exits nonzero on any failure.

Part 1  symbolic proof of Theorem 1 for all p (closed-form gap, odd cubic, 3p+7 branch)
Part 2  p <= 8 case analysis: every odd-D sum in [x*(p), S*(p)) with its exact gap,
        and the location of the odd-parity root D_o(p)
Part 3  brute force: overlap per the definition (convex hulls of the actual stratum value
        sets, every triad enumerated, no monotonicity assumed) for every p and every
        3p+3 <= S <= SMAX; compare with S >= S*(p); also TH.0 endpoint formulas
Part 4  Proposition 3 (1) symbolically and by brute force; (2) for p >= 9 symbolically
        (window at S* is 1+1) and by brute force at S* for 2 <= p <= PMAX
Part 5  PC.11-PC.16 numerical claims
"""
import sys
from fractions import Fraction as Fr
import sympy as sp

SMAX = 700
FAIL = []


def check(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


p, D, S = sp.symbols("p D S")
# ------------------------------------------------------------------ Part 1
print("== Part 1: Theorem 1, symbolic")
gap_even = 1 / p + 4 / D - 2 / (p + 1) - 1 / (D - p - 2)          # D = S - p even
closed = -(D - 2 * p - 2) * (D * (p - 1) - 2 * p * (p + 2)) / (D * p * (p + 1) * (D - p - 2))
check(sp.simplify(gap_even - closed) == 0,
      "even D: gap = -(D-2p-2)(D(p-1)-2p(p+2)) / (D p (p+1)(D-p-2))")
xstar = 3 * p * (p + 1) / (p - 1)
check(sp.simplify(p + 2 * p * (p + 2) / (p - 1) - xstar) == 0 and sp.simplify(xstar - (3 * p + 6 + 6 / (p - 1))) == 0,
      "even zero D = 2p(p+2)/(p-1)  <=>  S = x*(p) = 3p(p+1)/(p-1) = 3p+6+6/(p-1)")
tau = (p - 1) / (p * (p + 1))
phi = 4 / (S - p) - 1 / (S - 2 * p - 2)
check(sp.simplify((phi - tau) - gap_even.subs(D, S - p)) == 0, "even gap = phi_p(S) - tau_p")
# odd D: 1/((D-1)/2) + 1/((D+1)/2) = 4D/(D^2-1)
gap_odd = 1 / p + 4 * D / (D ** 2 - 1) - 2 / (p + 1) - 1 / (D - p - 2)
g = sp.expand(-(p - 1) * (D ** 2 - 1) * (D - p - 2) + p * (p + 1) * (3 * D ** 2 - 4 * (p + 2) * D + 1))
check(sp.simplify(gap_odd * p * (p + 1) * (D ** 2 - 1) * (D - p - 2) - g) == 0,
      "odd D: gap * p(p+1)(D^2-1)(D-p-2) = g(D), cubic with leading coeff -(p-1)")
check(sp.simplify(gap_odd - gap_even - 4 / (D * (D ** 2 - 1))) == 0, "odd gap = even-formula + 4/(D(D^2-1)) > 0 (lem:bound strict)")
def gint(pp, DD):
    return -(pp - 1) * (DD * DD - 1) * (DD - pp - 2) + pp * (pp + 1) * (3 * DD * DD - 4 * (pp + 2) * DD + 1)


check(all(gint(a, b) == g.subs({p: a, D: b}) for a in (2, 5, 9, 17) for b in (3, 11, 40)), "integer evaluator of g agrees with symbolic g")
vals = {"1": (1, -4 * p * (p + 1) ** 2), "-1": (-1, 4 * p * (p + 1) * (p + 3)),
        "p+2": (p + 2, -p * (p + 1) ** 2 * (p + 3)), "2p+3": (2 * p + 3, 8 * (p + 1) ** 2),
        "2p+6": (2 * p + 6, 2 * (p ** 2 + 26 * p + 70)), "2p+7": (2 * p + 7, -8 * (p ** 2 - 5 * p - 30))}
for nm, (at, exp) in vals.items():
    check(sp.expand(g.subs(D, at) - exp) == 0, f"g({nm}) = {exp}")
print("   => for p>=2: g(-1)>0>g(1), g(p+2)<0<g(2p+3): one root in each of (-1,1), (p+2,2p+3);")
print("      the third (largest) root D_o(p) lies in (2p+3, oo); on D >= 2p+3, g>0 before D_o and g<0 after.")
print("      p^2-5p-30 has roots (5+-sqrt145)/2, 8.52 > ...: g(2p+7)>0 for 2<=p<=8, <0 for p>=9.")
check(all((pp ** 2 - 5 * pp - 30 < 0) == (pp <= 8) for pp in range(2, 10000)), "sign of p^2-5p-30: negative iff p<=8 (p>=2)")
check(sp.integer_nthroot(145, 2)[1] is False, "discriminant 145 of p^2-5p-30 is not a square -> g(2p+7) != 0 for every integer p")
check(all(gint(pp, 2 * pp + 6) > 0 and gint(pp, 2 * pp + 7) < 0 for pp in range(9, 100000)),
      "p>=9 (all 9..99999, and symbolically above): D_o in (2p+6, 2p+7), so 3p+7 is the first odd-D overlap and no odd integer zero")
# even branch for p>=9: x* in (3p+6, 3p+7); first even-D sum >= x* is 3p+8
check(all(3 * pp + 6 < Fr(3 * pp * (pp + 1), pp - 1) < 3 * pp + 7 for pp in range(8, 2000)), "p>=8: 3p+6 < x* < 3p+7")


def Sstar(pp):
    return 18 if pp == 2 else 19 if pp == 3 else 3 * pp + 8 if pp <= 8 else 3 * pp + 7


def gap_exact(pp, SS):
    DD = SS - pp
    a, b = DD // 2, DD - DD // 2
    return Fr(1, pp) + Fr(1, a) + Fr(1, b) - Fr(2, pp + 1) - Fr(1, SS - 2 * pp - 2)


def xs(pp):
    return Fr(3 * pp * (pp + 1), pp - 1)


# "least S >= x* with S = p mod 2, except p >= 9 where 3p+7 comes first"
for pp in range(2, 2000):
    cand = next(SS for SS in range(3 * pp + 3, 10 * pp + 50) if SS >= xs(pp) and (SS - pp) % 2 == 0)
    exp = 3 * pp + 7 if pp >= 9 else cand
    assert exp == Sstar(pp), pp
check(True, "S*(p) equals the parity description for 2<=p<1999 (with the 3p+7 exception for p>=9)")

# ------------------------------------------------------------------ Part 2
print("== Part 2: p <= 8 case analysis (exact)")
for pp in range(2, 9):
    gp = g.subs(p, pp)
    # first odd D >= 2p+3 with g <= 0
    Do_first = next(DD for DD in range(2 * pp + 3, 400, 1) if DD % 2 == 1 and gint(pp, DD) <= 0)
    zero_odd = [DD for DD in range(2 * pp + 3, 400) if DD % 2 == 1 and gint(pp, DD) == 0]
    roots = [r for r in sp.Poly(gp, D).nroots() if abs(sp.im(r)) < 1e-12 and sp.re(r) > 2 * pp + 3]
    odd_in = [SS for SS in range(3 * pp + 3, Sstar(pp)) if SS >= xs(pp) and (SS - pp) % 2 == 1]
    line = f"   p={pp}: x*={xs(pp)}, S*={Sstar(pp)}, D_o~{[sp.N(r, 8) for r in roots]}, first odd-D overlap S={Do_first + pp}; odd sums in [x*,S*): " + \
        ", ".join(f"S={SS} gap={gap_exact(pp, SS)}" for SS in odd_in)
    print(line)
    check(not zero_odd, f"p={pp}: no odd D with gap 0")
    check(all(gap_exact(pp, SS) > 0 for SS in odd_in), f"p={pp}: every odd-D sum in [x*,S*) has gap>0")
    check(Do_first + pp in (Sstar(pp) + 1, Sstar(pp)) and Do_first + pp >= Sstar(pp),
          f"p={pp}: first odd-D overlap at S={Do_first + pp} in {{S*, S*+1}} -> overlap set is exactly S>=S*")

# ------------------------------------------------------------------ Part 3 brute force
print(f"== Part 3: brute force for all S <= {SMAX}")


def R3(a, b, c):
    return Fr(a * b + b * c + c * a, a * b * c)


def stratum_list(SS, pp):
    out = []
    for q in range(pp, (SS - pp) // 2 + 1):
        r = SS - pp - q
        e2, e3 = pp * q + q * r + r * pp, pp * q * r
        if e2 < e3:
            out.append((e2, e3, (pp, q, r)))
    return out


ext = {}  # (S,p) -> (min R, max R) over the actual hyperbolic triads
ok_mono = ok_max = ok_min = ok_nonempty = ok_p2spread = ok_l2_ = True
for SS in range(6, SMAX + 1):
    allvals = set(); nvals = 0
    for pp in range(2, SS // 3 + 1):
        lst = stratum_list(SS, pp)
        expect = (SS >= 11) if pp == 2 else (SS >= 3 * pp and (SS, pp) != (9, 3))
        ok_nonempty &= bool(lst) == expect
        if not lst:
            continue
        # strict decrease in q (cross-multiplication)
        ok_mono &= all(lst[i][0] * lst[i + 1][1] > lst[i + 1][0] * lst[i][1] for i in range(len(lst) - 1))
        Rs = [Fr(e2, e3) for e2, e3, _ in lst]
        lo, hi = min(Rs), max(Rs)
        ext[(SS, pp)] = (lo, hi)
        DD = SS - pp
        ok_min &= lo == Fr(1, pp) + Fr(1, DD // 2) + Fr(1, DD - DD // 2)
        if pp >= 3:
            ok_max &= hi == Fr(2, pp) + Fr(1, SS - 2 * pp)
        else:
            ok_p2spread &= hi < 1 and lst[0][2] != (2, 2, SS - 4)
        for R_ in Rs:
            allvals.add(R_); nvals += 1
    ext[("distinct", SS)] = (len(allvals) == nvals)
check(ok_mono, "lem:chamber: R strictly decreasing in q on every stratum (S<=%d)" % SMAX)
check(ok_min, "R^- = 1/p + 1/floor(D/2) + 1/ceil(D/2) attained on every nonempty stratum")
check(ok_max, "R^+ = 2/p + 1/(S-2p) attained for p>=3 (spread triad hyperbolic)")
check(ok_nonempty, "TH.0 nonemptiness: p=2 iff S>=11; p>=3 iff S>=3p except (9,3)")
check(ok_p2spread, "p=2: spread triad (2,2,S-4) never hyperbolic; stratum-2 maximum < 1")


def overlap_bf(SS, pp):
    A = ext.get((SS, pp)); B = ext.get((SS, pp + 1))
    if not A or not B:
        return False
    return A[0] <= B[1] and B[0] <= A[1]


ok_thm1 = ok_lem1 = True
bad = []
PMAX = (SMAX - 3) // 3
for pp in range(2, PMAX + 1):
    for SS in range(3 * pp + 3, SMAX + 1):
        ob = overlap_bf(SS, pp)
        if ob != (SS >= Sstar(pp)):
            ok_thm1 = False; bad.append((pp, SS))
        if ob != (gap_exact(pp, SS) <= 0):
            ok_lem1 = False
check(ok_lem1, f"Lemma 1 (overlap iff gap<=0) for all 2<=p<={PMAX}, 3p+3<=S<={SMAX}")
check(ok_thm1, f"Theorem 1 (overlap iff S>=S*(p)) brute force for all 2<=p<={PMAX}, 3p+3<=S<={SMAX} {bad[:5]}")
# Lemma 2: if all adjacent gaps > 0 then all strata pairwise disjoint (as value sets) and sigma injective
ok_l2 = True
for SS in range(10, SMAX + 1):
    ps = [pp for pp in range(2, SS // 3 + 1) if (SS, pp) in ext]
    if all(gap_exact(pp, SS) > 0 for pp in ps if pp + 1 in ps):
        ok_l2 &= ext[("distinct", SS)]
check(ok_l2, "Lemma 2 (adjacent separation => injective at S) for S<=%d" % SMAX)

# ------------------------------------------------------------------ Part 4 Proposition 3
print("== Part 4: Proposition 3")
# (1) even D: zero iff D = 2p(p+2)/(p-1) in Z and even; odd D: no integer zero (Part 1/2)
even_tangent = [pp for pp in range(2, 100000) if (2 * pp * (pp + 2)) % (pp - 1) == 0 and (2 * pp * (pp + 2) // (pp - 1)) % 2 == 0]
check(even_tangent == [2, 4], f"(p-1) | 2p(p+2) iff (p-1)|6 iff p in {{2,3,4,7}}; even quotient only for p in {even_tangent}")
check([pp for pp in range(2, 100000) if (2 * pp * (pp + 2)) % (pp - 1) == 0] == [2, 3, 4, 7], "integrality set {2,3,4,7}")
tang_bf = [(pp, SS) for pp in range(2, PMAX + 1) for SS in range(3 * pp + 3, SMAX + 1) if gap_exact(pp, SS) == 0]
check(tang_bf == [(2, 18), (4, 20)], f"brute force tangencies (gap=0, S>=3p+3, S<={SMAX}): {tang_bf}")
print("   note: the other even root D=2p+2 (S=3p+2) is spurious: there (p+1,p+1,p) is the balanced triad of stratum p itself.")
# (2) p >= 9 symbolic: window at S* = 3p+7 is exactly {balanced_p} + {spread_{p+1}}
w1 = sp.simplify(1 / p + 1 / (p + 2) + 1 / (p + 5) - (2 / (p + 1) + 1 / (p + 5)))
w2 = sp.simplify(1 / p + 1 / (p + 3) + 1 / (p + 4) - (1 / (p + 1) + 1 / (p + 2) + 1 / (p + 4)))
check(sp.factor(w1) == sp.factor(2 / (p * (p + 1) * (p + 2))), f"S=3p+7: R(p,p+2,p+5) - R^+_(p+1) = {sp.factor(w1)} > 0")
check(sp.simplify(w2 - (1 / (p * (p + 1)) - 1 / ((p + 2) * (p + 3)))) == 0,
      f"S=3p+7: R^-_p - R(p+1,p+2,p+4) = 1/(p(p+1)) - 1/((p+2)(p+3)) > 0")


def window(SS, pp):
    A0 = [(Fr(a, b), t) for a, b, t in stratum_list(SS, pp)]
    B0 = [(Fr(a, b), t) for a, b, t in stratum_list(SS, pp + 1)]
    lo = min(x[0] for x in A0); hi = max(x[0] for x in B0)
    A = [x for x in A0 if lo <= x[0] <= hi]
    B = [x for x in B0 if lo <= x[0] <= hi]
    coll = sorted({a[0] for a in A} & {b[0] for b in B})
    return A, B, coll


ok_p2 = True
for pp in range(2, PMAX + 1):
    SS = Sstar(pp)
    if SS > SMAX:
        break
    A, B, coll = window(SS, pp)
    if pp >= 9:
        ok_p2 &= (len(A), len(B)) == (1, 1)
    if pp in (2, 4):
        ok_p2 &= len(coll) == 1
    else:
        ok_p2 &= len(coll) == 0
    if pp <= 8:
        print(f"   p={pp} S*={SS}: window {len(A)}+{len(B)}: A={[a[1] for a in A]} B={[b[1] for b in B]} collisions={len(coll)}")
check(ok_p2, f"Prop 3(2): no adjacent collision at S*(p) for p not in {{2,4}}, 2<=p<={PMAX}; window 1+1 for p>=9")

# ------------------------------------------------------------------ Part 5 PC.11-PC.16 claims
print("== Part 5: paper-core numerical claims")
phi_ = lambda pp, SS: Fr(4, SS - pp) - Fr(1, SS - 2 * pp - 2)
tau_ = lambda pp: Fr(pp - 1, pp * (pp + 1))
check((tau_(2), tau_(3), tau_(4)) == (Fr(1, 6), Fr(1, 6), Fr(3, 20)), "tau_2=tau_3=1/6, tau_4=3/20")
check(phi_(2, 17) == Fr(29, 165) and phi_(2, 18) == Fr(1, 6), "phi_2(17)=29/165, phi_2(18)=1/6")
check(phi_(3, 12) == Fr(7, 36) and phi_(3, 17) == Fr(11, 63), "phi_3(12)=7/36, phi_3(17)=11/63")
check(min(phi_(4, s) for s in (15, 16, 17)) == phi_(4, 15) == Fr(9, 55) > Fr(3, 20), "min phi_4(15..17)=phi_4(15)=9/55>3/20")
check(all(phi_(2, s) > phi_(2, s + 1) for s in range(10, 40)) and phi_(2, 9) < phi_(2, 10), "phi_2 peaks at S=10, decreasing after")
check(phi_(3, 12) < phi_(3, 13) > phi_(3, 14) and all(phi_(3, s) > phi_(3, s + 1) for s in range(13, 40))
      and all(phi_(3, s) < phi_(3, s + 1) for s in range(9, 13)), "phi_3 unimodal, peak at S=13")
check(all(phi_(2, s) > Fr(1, 6) for s in range(11, 18)) and all(phi_(3, s) > Fr(1, 6) for s in range(12, 18))
      and all(phi_(4, s) > Fr(3, 20) for s in range(15, 18)), "phi_p(S) > tau_p on the stated ranges")
Rm = lambda SS, pp: Fr(1, pp) + Fr(1, (SS - pp) // 2) + Fr(1, SS - pp - (SS - pp) // 2)
Rp = lambda SS, pp: Fr(2, pp) + Fr(1, SS - 2 * pp)
check(Rm(18, 3) == Fr(101, 168) > Fr(3, 5) == Rp(18, 4), "R^-_{18,3}=101/168 > 3/5=R^+_{18,4}")
check(Rm(18, 4) == Fr(15, 28) > Fr(21, 40) == Rp(18, 5), "R^-_{18,4}=15/28 > 21/40=R^+_{18,5}")
check(Rm(18, 5) == Fr(107, 210) > Fr(1, 2) == Rp(18, 6), "R^-_{18,5}=107/210 > 1/2=R^+_{18,6}")
check(Rm(18, 2) == Rp(18, 3) == Fr(3, 4), "R^-_{18,2}=R^+_{18,3}=3/4")
# lem:bound
ok = True
for SS in range(10, 300):
    for pp in range(2, SS // 3 + 1):
        lb = Fr(1, pp) + Fr(4, SS - pp)
        ok &= Rm(SS, pp) >= lb and ((Rm(SS, pp) == lb) == ((SS - pp) % 2 == 0))
check(ok, "lem:bound R^- >= 1/p + 4/(S-p), equality iff S-p even (S<300)")
# R^+ non-increasing in p for p <= S/3
check(all(Rp(SS, pp) >= Rp(SS, pp + 1) for SS in range(9, 400) for pp in range(2, SS // 3) if 3 * (pp + 1) <= SS),
      "R^+_{S,p} non-increasing in p for p+1 <= S/3")
# PC.14 small-sum facts
hyp = [(a, b, c) for a in range(2, 30) for b in range(a, 30) for c in range(b, 30) if a * b + b * c + c * a < a * b * c]
check(min(sum(x) for x in hyp) == 10 and [x for x in hyp if sum(x) == 10] == [(3, 3, 4)], "S1>=10, equality only (3,3,4)")
check(min(sum(x) for x in hyp if x[0] == 2) == 11 and min(x[1] + x[2] for x in hyp if x[0] == 2) == 9
      and min(x[1] + x[2] for x in hyp if x[0] == 3) == 7 and min(sum(x) for x in hyp if x[0] >= 4) == 12, "p=2: q+r>=9,S>=11; p=3: q+r>=7; p>=4: S>=12")
# PC.13 Schur convexity: integer majorization check at fixed S
ok = True
for SS in range(10, 120):
    trs = [x for x in hyp if sum(x) == SS] if SS < 30 else [(a, b, SS - a - b) for a in range(2, SS // 3 + 1) for b in range(a, (SS - a) // 2 + 1) if a * b + b * (SS - a - b) + (SS - a - b) * a < a * b * (SS - a - b)]
    bal = (SS // 3, (SS + 1) // 3, (SS + 2) // 3)
    Rb = R3(*bal)
    ok &= all(R3(*x) >= Rb for x in trs) and bal in [tuple(sorted(x)) for x in trs]
check(ok, "prop:min: the balanced triple minimises R at each S in [10,120) and is hyperbolic")

print()
if FAIL:
    print(f"{len(FAIL)} FAILURE(S):", *FAIL, sep="\n  ")
    sys.exit(1)
print("ALL THRESHOLD CHECKS PASSED")
