"""check_cert: re-certify every printed delta_thm, delta_cert, eps_cert (ST.14 / SB.4) with the Prop. 6.10 formulas.

For each of the 11 rows:
  - delta_cert (printed, rounded down): must pass; report which test ((i), (ii), per order) and radius;
    the next 4-s.f. value must fail (printed value is the 4-s.f. maximum); exact 4-s.f. and 6-s.f. maxima for
    test (i) alone, test (ii) alone, and per-order mixing.
  - delta_thm: recomputed from Theorem S4 / S3 constants; printed must equal the 3-s.f. round-down; must pass.
  - eps_cert (uniform relative): printed must pass; next 2-s.f. value must fail (reported).
  - delta_cert/|H_nu| column: recomputed (floor and nearest at 2 s.f.).
Ladder: r in {k/40 : k = 20, 19, ..., 1} U {1/100, 1/1000} (22 radii).
"""
import sys
from fractions import Fraction as Fr
from stab610 import *

from rows_table import TABLE, passes, max_sig

fails = 0


def check(cond, msg):
    global fails
    if not cond:
        fails += 1
        print("   FAIL:", msg)
    return cond


def desc(res):
    return ", ".join(f"a={a}: (i) r={x[0]} (ii) r={x[1]}" for a, x in sorted(res['per'].items()))


summary = []
for m, dthm_s, dcert_s, dup_s, ratio_s, built, rel_s, eps_s in TABLE:
    st = Setup(m)
    n = st.n
    print(f"=== m = {m}, n = {n}")
    # ---- delta_cert
    dc = parse_sci(dcert_s)
    r = st.certify_abs(dc)
    ok = check(r['spec'] and r['mixed'], f"printed delta_cert {dcert_s} does not certify")
    which = 'ii' if r['ii'] else ('i' if r['i'] else ('mixed' if r['mixed'] else 'NONE'))
    print(f"  delta_cert printed {dcert_s}: rho(A)<1 {r['spec']}, test (i) {r['i']}, test (ii) {r['ii']}, "
          f"mixed {r['mixed']} -> certified by {which}; {desc(r)}")
    rn = st.certify_abs(next_up(dcert_s))
    check(not rn['mixed'], f"next value above {dcert_s} also certifies (printed not the 4-s.f. max)")
    print(f"  next 4-s.f. value {float(next_up(dcert_s)):.4e}: certifies (any test) = {rn['mixed']}; {desc(rn) if rn['spec'] else 'rho(A)<1 fails'}")
    maxes = {}
    for mode in ('i', 'ii', 'mixed'):
        r4 = max_sig(st.certify_abs, 4, mode)
        r6 = max_sig(st.certify_abs, 6, mode)
        maxes[mode] = (fmt(*r4, 4) if r4 else 'never', fmt(*r6, 6) if r6 else 'never')
    print(f"  4-s.f. max: test (i) {maxes['i'][0]}, test (ii) {maxes['ii'][0]}, mixed {maxes['mixed'][0]};"
          f" 6-s.f.: (i) {maxes['i'][1]}, (ii) {maxes['ii'][1]}, mixed {maxes['mixed'][1]}")
    check(maxes['mixed'][0] == dcert_s, f"4-s.f. maximum {maxes['mixed'][0]} != printed {dcert_s}")
    # ---- delta_thm
    dt, info = delta_thm(m)
    q, e = sig_round(dt, 3, 'down')
    dt_floor = fmt(q, e, 3)
    print(f"  delta_thm (Thm S4) = {float(dt):.6e} exact = {dt}" if len(str(dt)) < 80 else
          f"  delta_thm (Thm S4) = {float(dt):.6e}")
    print(f"    kappa = {float(info['kappa']):.6g}, zeta_n = {info['zeta']}, rho_n = {float(info['rho_n']):.6g},"
          f" lambda_mu = {info['lam']}; binding term index {info['terms'].index(min(info['terms']))}"
          f" of {[f'{float(t):.3e}' for t in info['terms']]}")
    check(dt_floor == dthm_s, f"delta_thm 3-s.f. round-down {dt_floor} != printed {dthm_s}")
    rt = st.certify_abs(parse_sci(dthm_s))
    check(rt['spec'] and rt['mixed'], "printed delta_thm does not pass the certificate")
    print(f"  delta_thm printed {dthm_s} (round-down of exact: {dt_floor}): certificate (i) {rt['i']}, (ii) {rt['ii']}")
    # ---- relative precision column
    rel_floor = []
    rel_near = []
    for h in st.H:
        x = dc / abs(h)
        rel_floor.append(fmt(*sig_round(x, 2, 'down'), 2))
        rel_near.append(fmt(*sig_round(x, 2, 'near'), 2))
    print(f"  delta_cert/|H_nu| floor: {rel_floor}  nearest: {rel_near}  printed: {rel_s}")
    sup6 = parse_sci(maxes['mixed'][1])  # unrounded certified sup, 6 s.f. (round-down, still certified)
    rel_sup = [fmt(*sig_round(sup6 / abs(h), 2, 'down'), 2) for h in st.H]
    check(rel_sup == rel_s, "relative precision column != floor(sup delta / |H|)")
    if rel_floor != rel_s:
        print(f"    NOTE: with the PRINTED delta_cert the round-down is {rel_floor}; the printed column equals the"
              f" round-down of (certified sup {maxes['mixed'][1]})/|H_nu| = {rel_sup}")
    # ---- eps_cert
    ec = parse_sci(eps_s)
    re_ = st.certify_rel(ec)
    check(re_['spec'] and re_['mixed'], f"printed eps_cert {eps_s} does not certify")
    which_e = 'ii' if re_['ii'] else ('i' if re_['i'] else ('mixed' if re_['mixed'] else 'NONE'))
    ren = st.certify_rel(next_up(eps_s))
    qe, ee = max_sig(st.certify_rel, 2, 'mixed')
    qe4, ee4 = max_sig(st.certify_rel, 4, 'mixed')
    eps_max = fmt(qe, ee, 2)
    print(f"  eps_cert printed {eps_s}: certified by {which_e}; next 2-s.f. {float(next_up(eps_s)):.1e} certifies"
          f" = {ren['mixed']}; 2-s.f. max {eps_max}, 4-s.f. max {fmt(qe4, ee4, 4)}")
    check(eps_max == eps_s, f"eps_cert 2-s.f. maximum {eps_max} != printed {eps_s}")
    summary.append((m, dcert_s, which, maxes, dthm_s, dt_floor, eps_s, eps_max, which_e))

print()
print("SUMMARY  m | delta_cert printed | test | 4sf max (i)/(ii)/mixed | delta_thm printed/recomputed | eps printed/max | eps test")
for m, dcs, w, mx, dts, dtf, es, em, we in summary:
    print(f"  {m} | {dcs} | {w} | {mx['i'][0]} / {mx['ii'][0]} / {mx['mixed'][0]} | {dts} / {dtf} | {es} / {em} | {we}")
print("TOTAL FAILURES:", fails)
sys.exit(1 if fails else 0)
