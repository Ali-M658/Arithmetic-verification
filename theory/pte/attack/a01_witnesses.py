"""Attack item 1: recompute every witness of data/witnesses.json from sig1/sig2 with own b_l."""
import json, sys, os
from fractions import Fraction as F
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
from mylib import b, area, shared, sig_to_config, config_level, has_pm_pair, iota, primitive, psum, p_poly

HERE = os.path.dirname(os.path.abspath(__file__))
W = json.load(open(os.path.join(HERE, '..', 'data', 'witnesses.json')))

# --- sanity of own b_l against an independent source (Schueth Rem 4.2 / Thm 4.1, K=-1) ---
for k in [1, 2, 3, 5, 7, 12, 101]:
    k = F(k)
    assert b(0, k) == (k - 1 / k) / 12
    assert b(1, k) == -((k ** 3 - 1 / k) / 360 + (k - 1 / k) / 36)
    assert b(2, k) == (k ** 5 - 1 / k) / 2520 + (k ** 3 - 1 / k) / 720 + (k - 1 / k) / 180
for l in range(10):
    assert b(l, 1) == 0
    assert all(p % 2 == 0 for p in p_poly(l)) and max(p_poly(l)) == 2 * l + 2
# known pair from [Sig] must share exactly 2
assert shared((1, [15]), (0, [3, 3, 5, 5])) == 2
print("b_l sanity: matches Schueth a0,a1,a2 at K=-1; b_l(1)=0; p_l even of degree 2l+2")

bad = []
rows = []
for w in W:
    kind, L = w['kind'], w['L']
    s1 = (w['sig1']['g'], w['sig1']['orders'])
    s2 = (w['sig2']['g'], w['sig2']['orders'])
    tag = f"{kind} L={L}"
    def chk(cond, msg):
        if not cond:
            bad.append(f"{tag}: {msg}")
    chk(all(isinstance(x, int) and x >= 2 for x in s1[1] + s2[1]), "orders not integers >=2")
    chk((s1[0], sorted(s1[1])) != (s2[0], sorted(s2[1])), "signatures equal")
    A1, A2 = area(s1), area(s2)
    chk(A1 == A2, "areas differ")
    chk(A1 > 0, "not hyperbolic")
    chk(A1 == F(w['area_over_2pi']), f"area {A1} != claimed {w['area_over_2pi']}")
    sh = shared(s1, s2, lmax=L + 3)
    chk(sh == L, f"shares {sh}, claimed {L}")
    chk(w['shares_exactly'] == L, "shares_exactly field != L")
    chk([len(s1[1]), len(s2[1])] == w['cone_counts'], f"cone counts {[len(s1[1]), len(s2[1])]} vs {w['cone_counts']}")
    U, V, Z = sig_to_config(s1, s2)
    T = len(Z)
    chk(T == w['T'], f"T={T} vs claimed {w['T']}")
    io = iota(Z)
    chk(abs(io) == abs(w['iota']), f"iota {io} vs {w['iota']}")
    chk(io == len(U) - len(V), "iota identity")
    chk(len(V) - len(U) == 2 * (s1[0] - s2[0]), "|V*|-|U*| != 2(g-g')")
    # configuration checks, independently
    chk(not has_pm_pair(Z), "Z has a +- pair")
    lev = config_level(Z, Lmax=L + 3)
    chk(lev == L, f"config level {lev} != L")
    chk(T % 2 == 0 and T >= 2 * L + 2, "T parity / Theorem S")
    chk(abs(io) <= T - 2 * L, "Theorem 2.1 violated")
    P = primitive(Z)
    chk(P == sorted(w['Z']) or P == sorted(-z for z in w['Z']), "json Z != primitive form of config")
    # stored Z must itself be a config with the same level
    chk(config_level(w['Z'], Lmax=L + 3) == L and not has_pm_pair(w['Z']), "stored Z not an exact L-config")
    if kind == 'genus':
        chk(s1[0] != s2[0] and min(s1[0], s2[0]) == 0 and io != 0, "genus pair kind")
    elif kind == 'balanced':
        chk(s1[0] == s2[0] == 0 and len(s1[1]) == len(s2[1]) and io == 0, "balanced kind")
    elif kind == 'cone':
        chk(s1[0] == s2[0] == 0 and len(s1[1]) != len(s2[1]) and io == 0, "cone kind")
        chk(1 in w['Z'] or -1 in w['Z'], "cone pair without padding 1")
    rows.append((kind, L, T, io, [len(s1[1]), len(s2[1])], (s1[0], s2[0]), A1))
    print(f"{tag:12s} T={T:3d} iota={io:+d} cones={len(s1[1])}/{len(s2[1])} genera={s1[0]}/{s2[0]} "
          f"shares={sh} area/2pi~{float(A1):.10f}")

# --- claims of proof.md section 0 / 5 tables ---
A = {(r[0], r[1]): r[6] for r in rows}
claims_exact = {('genus', 2): F(14, 15), ('genus', 3): F(14, 5), ('balanced', 2): F(1, 4),
                ('balanced', 3): F(22, 15), ('cone', 2): F(2, 5), ('cone', 3): F(113, 30),
                ('cone', 4): F(2651846, 320229)}
for k, v in claims_exact.items():
    if A[k] != v:
        bad.append(f"{k}: area {A[k]} != table {v}")
# "approx" values: least area A_L over any pair, and the table f(A)>=L+1 for A/2pi >= value
thr = {2: F(1, 4), 3: F(22, 15), 4: F(5), 5: F(7), 6: F(10), 7: F(18)}
for L, t in thr.items():
    AL = min(A[(k, L)] for k in ('genus', 'balanced', 'cone'))
    print(f"L={L}: least area/2pi = {float(AL):.15f}  (<= table value {t}: {AL <= t})")
    if not AL <= t:
        bad.append(f"L={L}: least area {AL} exceeds table threshold {t}")
# section 0 table columns
genusT = {2: 6, 3: 10, 4: 16, 5: 20, 6: 26, 7: 40}  # proof.md section 0 (version of 6 Oct 00:45)
conecc = {2: (3, 4), 3: (7, 8), 4: (11, 12), 5: (22, 23), 6: (29, 30), 7: (35, 36)}
for r in rows:
    k, L, T, io, cc = r[0], r[1], r[2], r[3], r[4]
    if k == 'genus' and T != genusT[L]:
        bad.append(f"sec0 genus T L={L}")
    if k == 'cone' and tuple(sorted(cc)) != conecc[L]:
        bad.append(f"sec0 cone counts L={L}: {cc}")
# section 5 approx genus areas: 7.9998, 9.0000, 12.000, 19.000
for L, v, tol in [(4, 6.9999, 1e-4), (5, 9.0, 1e-4), (6, 12.0, 1e-3), (7, 19.0, 1e-3)]:
    if abs(float(A[('genus', L)]) - v) > tol:
        bad.append(f"genus L={L} area {float(A[('genus', L)])} vs {v}")
for L, v in [(4, 5.0), (5, 7.0), (6, 10.0), (7, 18.0)]:
    print(f"balanced L={L}: area/2pi - {v} = {float(A[('balanced', L)] - v):.3e}")

# section 5, L=4 genus recipe: {+-7,+-11,+-18} vs {+-3,+-14,+-17} shifted by -11/2 leaves a (3,5) piece
X = [F(t) for t in (7, -7, 11, -11, 18, -18)]; Y = [F(t) for t in (3, -3, 14, -14, 17, -17)]
assert all(psum(X, j) == psum(Y, j) for j in range(1, 6)) and psum(X, 6) != psum(Y, 6)
from mylib import cancel_pm
c = F(-11, 2)
piece = cancel_pm([x + c for x in X] + [-(y + c) for y in Y])
npos = sum(1 for z in piece if z > 0)
assert len(piece) == 8 and sorted([npos, 8 - npos]) == [3, 5]
assert all(psum(piece, j) == 0 for j in (1, 3, 5)) and psum(piece, -1) != 0
print("sec 5 L=4 recipe: size-6 solution is =_5; shift by -11/2 cancels two pairs -> (3,5) piece with s1=s3=s5=0, s_-1!=0: OK")

print()
if bad:
    print("FAILURES:")
    for x in bad:
        print("  ", x)
    sys.exit(1)
print(f"ALL {len(W)} WITNESSES PASS (own b_l, own config checks)")
