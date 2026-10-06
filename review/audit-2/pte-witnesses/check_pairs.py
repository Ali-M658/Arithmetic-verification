"""PW.4 (and the numbers of PW.0/PW.1/PW.2 that depend on the 18 pairs).

For each claimed pair W00..W17 (parsed verbatim from review/audit-2/statements/pte-witnesses.md):
  - both signatures: genus g >= 0, all orders integers >= 2, chi < 0  (hyperbolicity test:
    Area/2pi = 2g-2+sum(1-1/m_i) > 0; every closed orientable 2-orbifold with chi<0 is good and
    carries a hyperbolic metric);
  - exact Area/2pi equal for both and equal to the printed value;
  - distinct signatures;
  - c_1..c_{L+1} computed from first principles (heatlib): c_1..c_L equal, c_{L+1} different;
  - the [Sig] Lemma 4 / Lemma 2 criterion gives the same L;
  - T = |U*|+|V*| (Lemma 4 padding by 1s + cancellation), iota = |U*|-|V*|, cone counts.
Then the derived table numbers (least areas, margins below the integers, T vs 4L-2, Area/2pi vs T/2-2).
Exits nonzero on any failure.
"""
import re, sys
from fractions import Fraction as F
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from heatlib import is_hyperbolic, s_area, shared, criterion_L, config, P, R

BUNDLE = __file__.rsplit('/', 1)[0] + '/../statements/pte-witnesses.md'
txt = open(BUNDLE).read()
blocks = re.findall(r"\*\*(W\d\d)\*\* kind=(\w+), L=(\d+), claimed shares exactly (\d+), T=(\d+), iota=(-?\d+), "
                    r"cone counts (\d+) vs (\d+), Area/2pi = ([\d/]+)\n- O  = \(g=(\d+); ([\d, ]+)\)\n- O' = \(g=(\d+); ([\d, ]+)\)",
                    txt)
assert len(blocks) == 18, len(blocks)
W = {}
fail = []
def chk(cond, msg):
    if not cond:
        fail.append(msg)
        print("  FAIL:", msg)
for (wid, kind, L, Lx, T, iota, n1c, n2c, area, g1, m1, g2, m2) in blocks:
    L, Lx, T, iota, n1c, n2c, g1, g2 = map(int, (L, Lx, T, iota, n1c, n2c, g1, g2))
    m1 = sorted(int(x) for x in m1.split(','))
    m2 = sorted(int(x) for x in m2.split(','))
    area = F(area)
    print(f"{wid} kind={kind} L={L}: O=(g={g1}; {len(m1)} cones, max {max(m1)}), O'=(g={g2}; {len(m2)} cones, max {max(m2)})")
    chk(L == Lx, f"{wid} L mismatch")
    h1, h2 = is_hyperbolic(g1, m1), is_hyperbolic(g2, m2)
    chk(h1 and h2, f"{wid} not hyperbolic")
    s1, s2 = s_area(g1, m1), s_area(g2, m2)
    chk(s1 == s2, f"{wid} areas differ {s1} {s2}")
    chk(s1 == area, f"{wid} printed area {area} != computed {s1}")
    chk((g1, m1) != (g2, m2), f"{wid} equal signatures")
    chk(m1 != m2, f"{wid} equal cone multisets (only genus differs)")
    k, c1, c2 = shared(g1, m1, g2, m2, L + 2)
    chk(k == L, f"{wid} shares {k} coefficients (by direct c_j), claimed exactly {L}")
    kc = criterion_L(g1, m1, g2, m2, L + 2)
    chk(kc == k, f"{wid} criterion gives {kc}, direct gives {k}")
    U, V = config(g1, m1, g2, m2)
    Tc = len(U) + len(V)
    io = len(U) - len(V)
    chk(Tc == T, f"{wid} T computed {Tc} claimed {T}")
    chk(abs(io) == abs(iota), f"{wid} |iota| computed {abs(io)} claimed {abs(iota)}")
    chk(io == 2 * (g2 - g1), f"{wid} iota != 2(g'-g)")
    chk((len(m1), len(m2)) == (n1c, n2c), f"{wid} cone counts {len(m1)},{len(m2)} vs claimed {n1c},{n2c}")
    ones = (U.count(1), V.count(1))
    # independent check of the configuration conditions on Z = U* + (-V*)
    Z = [F(u) for u in U] + [F(-v) for v in V]
    for j in [-1] + list(range(1, 2 * L - 2, 2)):
        chk(sum(z ** j for z in Z) == 0, f"{wid} s_{j}(Z) != 0")
    chk(sum(z ** (2 * L - 1) for z in Z) != 0, f"{wid} s_(2L-1)(Z) == 0")
    chk(not (set(U) & set(V)), f"{wid} U*,V* not disjoint")
    W[wid] = dict(kind=kind, L=L, T=Tc, iota=io, s=s1, n=(len(m1), len(m2)), g=(g1, g2), ones=ones)
    print(f"   Area/2pi = {float(s1):.12f} (exact match printed), shares exactly {k} (direct) = {kc} (criterion);"
          f" T={Tc}, iota={io}, padding ones in (U*,V*) = {ones}, distinct multisets: {m1 != m2}")
    dlt = c1[L] - c2[L]
    print(f"   c_{L+1}(O) - c_{L+1}(O') != 0: numerator has {len(str(abs(dlt.numerator)))} digits, sign {'+' if dlt > 0 else '-'}")

print()
print("Derived numbers of PW.0 / PW.1 / PW.2")
LEAST = {}
for L in range(2, 8):
    rows = {w: d for w, d in W.items() if d['L'] == L}
    least = min(rows.items(), key=lambda kv: kv[1]['s'])
    bal = [d for d in rows.values() if d['kind'] == 'balanced'][0]
    gen = [d for d in rows.values() if d['kind'] == 'genus'][0]
    cone = [d for d in rows.values() if d['kind'] == 'cone'][0]
    s = least[1]['s']
    ceil = -((-s.numerator) // s.denominator)
    print(f"L={L}: least area among the three listed pairs: {least[0]} Area/2pi={s} ~ {float(s):.15f};"
          f" next integer {ceil}, margin {ceil - s} ~ {float(ceil - s):.3e}")
    print(f"      genus pair T={gen['T']} (cone counts {gen['n']}, genera {gen['g']});"
          f" cone pair counts {cone['n']} T={cone['T']}, ones {cone['ones']};"
          f" balanced T={bal['T']}, 4L-2={4*L-2}, T/2-2={F(bal['T'],2)-2}, Area/2pi={float(bal['s']):.6f}, 2L-3={2*L-3}")
    LEAST[L] = (least[0], s)

# Checks of the printed headline table PW.0
table = {2: (F(1, 4), 6, (3, 4)), 3: (F(22, 15), 10, (7, 8)), 4: (5, 16, (11, 12)), 5: (7, 20, (22, 23)),
         6: (10, 26, (29, 30)), 7: (18, 40, (35, 36))}
for L, (ar, tg, cc) in table.items():
    wid, s = LEAST[L]
    if L <= 3:
        chk(s == ar, f"table L={L} least area {s} != {ar}")
    else:
        chk(ar - F(1, 10**3) < s < ar, f"table L={L}: {s} not in (ar-0.001, ar)")
    gen = [d for d in W.values() if d['L'] == L and d['kind'] == 'genus'][0]
    cone = [d for d in W.values() if d['L'] == L and d['kind'] == 'cone'][0]
    chk(gen['T'] == tg, f"table L={L} genus T")
    chk(sorted(cone['n']) == list(cc), f"table L={L} cone counts")
    chk(cone['g'] == (0, 0), f"table L={L} cone pair not genus 0")
    chk(4 ** (L - 1) - 1 == [3, 15, 63, 255, 1023, 4095][L - 2], "TM bound")

# PW.1: 'previously 2pi*14/5' pair and the [1,5,5]=[2,3,6] input
chk(s_area(1, [15, 15, 15]) == F(14, 5) == s_area(0, [3, 3, 5, 7, 7, 21]), "14/5 pair area")
chk(sum([1, 5, 5]) == sum([2, 3, 6]) and sum(x**3 for x in [1, 5, 5]) == sum(x**3 for x in [2, 3, 6]), "[1,5,5]=[2,3,6]")
print("[1,5,5] vs [2,3,6]: s1", sum([1,5,5]), sum([2,3,6]), " s2", sum(x*x for x in [1,5,5]), sum(x*x for x in [2,3,6]),
      " s3", sum(x**3 for x in [1,5,5]), sum(x**3 for x in [2,3,6]))
# genus 1 vs genus 0 configuration sizes
chk([W[w]['T'] for w in ['W02', 'W03', 'W04', 'W05']] == [16, 20, 26, 40], "genus sizes 16,20,26,40")
chk([W[w]['g'] for w in ['W02', 'W03', 'W04', 'W05']] == [(0, 1)] * 4, "genus 1 vs 0")
chk([2 ** (2 * L - 1) for L in range(4, 8)] == [128, 512, 2048, 8192], "2^(2L-1)")
# balanced pairs: equal cone counts and genus 0
for w in ['W08', 'W09', 'W10', 'W11']:
    chk(W[w]['g'] == (0, 0) and W[w]['n'][0] == W[w]['n'][1], f"{w} not genus-0 equal-count")
# PS Lemma 1.2(5) bound Area/2pi < T/2 - 2 for balanced genus-0 pairs
for w in ['W06', 'W07', 'W08', 'W09', 'W10', 'W11']:
    chk(W[w]['s'] < F(W[w]['T'], 2) - 2, f"{w} Area/2pi >= T/2-2")
print()
if fail:
    print("FAILURES:", len(fail))
    for f_ in fail:
        print(" ", f_)
    sys.exit(1)
print("ALL OK")
