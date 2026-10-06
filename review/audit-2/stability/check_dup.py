"""check_dup: exact verification of the delta_up failure points (ST.13 construction).

Reads dup_candidates.json (numerical minimisers from search_dup.py; floats are only starting data). For every
candidate:
  1. rebuild q~ exactly: the float parameters are converted exactly to rationals (Fraction(float)), c = a + s/2 is
     exact, and the complex shape uses w = y^2 (rational);
  2. compute the data H(q~) exactly (Newton, R = e_{n-1}/e_n, H = F I + h0) and delta = max |H(q~) - H(m)|;
  3. Theorem B: the exact solve M(I~)^{-1} b(I~) returns e(q~) (recovery returns q~ itself);
  4. tie: q~ has a root (pair) with real part exactly a + s/2 (by construction; checked by exact evaluation);
  5. failure beyond the tie: push the root (pair) outward to c' = c + s*10^-12; the exact data H(q~') are within
     delta' of H(m) with delta' - delta < 10^-9 * delta, the exact solve returns q~', and the exact Routh-Hurwitz
     strip counts show that rounding the real parts of its roots does NOT return m.
Then, per row: best exact upper bound (rounded up, 4 s.f.), the location, and comparison with the printed delta_up.
"""
import json, sys
from fractions import Fraction as Fr
from stab610 import *
from rows_table import TABLE

fails = 0


def check(cond, msg):
    global fails
    if not cond:
        fails += 1
        print("   FAIL:", msg)
    return cond


def polymul(p, q):
    r = [Fr(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i + j] += x * y
    return r


def build(m, a, s, shape, params, push=Fr(0)):
    n = len(m)
    mu = Fr(max(m))
    c = Fr(a) + Fr(s, 2) + s * push
    P = [Fr(x) for x in params]
    if shape == 'R':
        g = [Fr(1)] + [P[k - 1] * mu ** k for k in range(1, n)]
        q = polymul([Fr(1), -c], g)
    else:
        w = P[0] ** 2
        g = [Fr(1)] + [P[k] * mu ** k for k in range(1, n - 1)]
        q = polymul([Fr(1), -2 * c, c * c + w], g)
    e = [(-1) ** j * q[j] for j in range(n + 1)]
    return q, e, g, c


def data_delta(m, e):
    I = invariants_from_e(e)
    H = H_from_I(I)
    Hm = H_of_m(m)
    return I, max(abs(x - y) for x, y in zip(H, Hm))


def rounded_multiset_count(coef, lo, hi):
    """exact counts of roots of coef (desc) in each strip (k-1/2, k+1/2) for integers lo..hi; None if a tie."""
    out = {}
    for k in range(lo, hi + 1):
        cnt = strip_count(coef, Fr(k) - Fr(1, 2), Fr(k) + Fr(1, 2))
        if cnt is None:
            return None
        if cnt:
            out[k] = cnt
    return out


cands = json.load(open('dup_candidates.json'))
try:
    deep = json.load(open('dup_candidates_deep.json'))
except FileNotFoundError:
    deep = {}
for key, d in deep.items():
    cands.setdefault(key, {})
    for k, v in d.items():
        cands[key][k + '|deep'] = v
PUSH = Fr(1, 10 ** 20)
summary = []
for m, dthm_s, dcert_s, dup_s, ratio_s, built, rel_s, eps_s in TABLE:
    key = str(m)
    if key not in cands:
        print(f"=== {m}: no candidates (search not run)")
        check(False, f"no candidates for {m}")
        continue
    n = len(m)
    print(f"=== {m}  (printed delta_up {dup_s}, built at {built}, ratio {ratio_s})")
    best = None
    for k, cd in sorted(cands[key].items()):
        a, s, shape = cd['a'], cd['s'], cd['shape']
        q, e, g, c = build(m, a, s, shape, cd['params'])
        I, dlt = data_delta(m, e)
        # 3. Theorem B exact solve
        ok3 = check(solve_e(I) == e, f"exact solve does not return q~ for {k}")
        # 4. exact tie: (z - c) divides q~ (R) or (z-c)^2 + w divides q~ (C), and real part c
        val = sum(q[j] * c ** (n - j) for j in range(n + 1))
        if shape == 'R':
            ok4 = check(val == 0, f"q~(c) != 0 for {k}")
        else:
            ok4 = True  # the quadratic factor is explicit; its roots are c +- i sqrt(w)
        # 5. push the tied root (pair) by 10^-20 in each direction; the point is a valid failure if recovery
        #    fails for at least one direction (the tie may belong to the order a or to its neighbour a + s).
        mm = {}
        for x in m:
            mm[x] = mm.get(x, 0) + 1
        tag = f"a={a} c={a}{'+' if s > 0 else '-'}1/2 {shape}" + (" [deep]" if k.endswith('deep') else "")
        ok5 = False
        pushed = None
        notes = []
        for direction in (1, -1):
            q2, e2, g2, c2 = build(m, a, s, shape, cd['params'], push=direction * PUSH)
            I2, dlt2 = data_delta(m, e2)
            solved = solve_e(I2) == e2
            check(solved, f"exact solve (pushed) does not return q~' for {k}")
            gm = rounded_multiset_count(g, -int(max(m)) - 3, int(max(m)) + 3)
            if gm is None or sum(gm.values()) != len(g) - 1:
                notes.append("g has a root on a half-integer line")
                continue
            rnd = dict(gm)
            side = a + s if (c2 - c) * s > 0 else a  # outward rounds to a+s, inward to a
            rnd[side] = rnd.get(side, 0) + (1 if shape == 'R' else 2)
            fails_rec = not recovers(e2, m)
            check(fails_rec == (rnd != mm), f"Routh count and rounded multiset disagree for {k}")
            small = dlt2 - dlt < dlt * Fr(1, 10 ** 9)
            check(small, f"push 1e-20 changed delta by more than 1e-9 relative for {k}")
            gdesc = ", ".join(f"{kk}x{v}" if v > 1 else f"{kk}" for kk, v in sorted(gm.items()))
            notes.append(f"push {'out' if direction > 0 else 'in'}: g roots round to [{gdesc}], tied root(s) to {side},"
                         f" recovery {'FAILS' if fails_rec else 'succeeds'}")
            if fails_rec and solved and small:
                ok5 = True
                pushed = dlt2 if pushed is None else min(pushed, dlt2)
        print(f"  {tag}: exact delta = {float(dlt):.7e}; solve==q~ {ok3}, tie {ok4}, valid failure {ok5}; " + "; ".join(notes))
        if ok5:
            dlt2 = pushed
        if ok3 and ok5 and (best is None or dlt2 < best[0]):
            best = (dlt2, tag)
    if not check(best is not None, f"no valid failure point for {m}"):
        continue
    q4, e4 = sig_round(best[0], 4, 'up')
    bstr = fmt(q4, e4, 4)
    printed = parse_sci(dup_s)
    valid = printed >= best[0]
    ratio = best[0] / parse_sci(dcert_s)
    print(f"  BEST exact failure level (pushed, an upper bound for the threshold): {float(best[0]):.7e} -> {bstr}"
          f" at {best[1]}; printed {dup_s}: {'VALID (>= best)' if valid else 'NOT reproduced (< best found)'};"
          f" ratio best/delta_cert = {float(ratio):.3f} (printed {ratio_s})")
    summary.append((m, dup_s, bstr, best[1], valid, float(ratio), ratio_s))

print()
print("SUMMARY  m | printed delta_up | best exact upper bound (4 s.f. up) | where | printed valid | ratio best/cert (printed)")
for row in summary:
    m, ds, bs, where, valid, ratio, rs = row
    print(f"  {m} | {ds} | {bs} | {where} | {valid} | {ratio:.2f} ({rs})")
print("TOTAL FAILURES:", fails)
sys.exit(1 if fails else 0)
