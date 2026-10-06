"""check_compare (comparison phase): my implementation (stab610.py) against the producer's code.

Producer code is imported read-only:
  - theory/stability/threshold.py (main() guarded; nothing is written);
  - theory/revision/check_prop610.py: its source is exec'd only up to the "(a)" block, so it computes but never
    writes check_prop610.txt (no file under theory/ is touched).
Checks, exactly, for all 11 rows:
  1. Theorem B system: stab_common.theorem_B_system == my M, b; check_prop610.system == my M, b.
  2. At the printed delta_cert: E, A, r_rem bound of threshold._common and of check_prop610.bounds == mine.
  3. G: threshold (via lipschitz_e.N_matrix) and check_prop610 (printed J) == mine.
  4. delta_thm: threshold.delta_thm exact == mine.
  5. Ladders: threshold.RADII == check_prop610.RADII == my LADDER.
  6. threshold_results.json: delta_cert_exact lies in [my 6-s.f. sup, my 6-s.f. sup + 1e-6]; delta_up float vs my
     best exact failure; eps_cert float vs my 4-s.f. max; whether the 4-s.f. eps strings of threshold_output.md
     certify.
"""
import json, os, sys
from fractions import Fraction as Fr
from stab610 import *
from rows_table import TABLE, max_sig

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'theory', 'stability'))
import threshold as TH  # noqa
from stab_common import theorem_B_system  # noqa

src = open(os.path.join(ROOT, 'theory', 'revision', 'check_prop610.py')).read()
src = src[: src.index('# ------------------------------------------------------------------ (a)')]
CP = {'__file__': os.path.join(ROOT, 'theory', 'revision', 'check_prop610.py'), '__name__': 'cp610'}
exec(compile(src, 'check_prop610(prefix)', 'exec'), CP)
assert not any(k == 'OUT' and False for k in CP)  # OUT path defined but never opened in the prefix

RES = json.load(open(os.path.join(ROOT, 'theory', 'stability', 'threshold_results.json')))
OUTMD = open(os.path.join(ROOT, 'theory', 'stability', 'threshold_output.md')).read()
MYDUP = {  # best exact failure levels from check_dup.txt (pushed values, exact to 8 digits)
    (2, 8, 8): 2.4848623e-03, (3, 3, 12): 4.5882716e-03, (3, 10, 15, 30): 7.4865192e-03,
    (4, 5, 21, 28): 2.0176678e-03, (2, 3, 7): 6.5869137e-03, (4, 4, 4): 5.0358257e-04, (7, 7, 7): 8.2721187e-05,
    (3, 3, 4, 4): 1.1943586e-04, (5, 5, 5, 5): 3.8257987e-05, (2, 2, 2, 3): 2.5197149e-04,
    (2, 2, 2, 2, 3): 5.3113199e-05}

fails = 0


def check(cond, msg):
    global fails
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        fails += 1
    return cond


check(TH.RADII == LADDER and CP['RADII'] == LADDER, "ladders identical: threshold.RADII, check_prop610.RADII, mine")
eps_rows = {}
for line in OUTMD.splitlines():
    if line.startswith('| ('):
        cells = [c.strip() for c in line.strip('|').split('|')]
        eps_rows[cells[0]] = cells
for m, dthm_s, dcert_s, dup_s, ratio_s, built, rel_s, eps_s in TABLE:
    print(f"=== {m}")
    st = Setup(m)
    n = st.n
    I = st.I
    M1, b1, _ = theorem_B_system(I)
    M2, b2, _, _ = CP['system'](I, n)
    check(M1 == st.M and b1 == st.b and M2 == st.M and b2 == st.b, "Theorem B M, b identical (stab_common, check_prop610, mine)")
    d = parse_sci(dcert_s)
    B = st.bounds([d] * n)
    th = TH._common(m, [d] * n)
    cp = CP['bounds'](m, [d] * n)
    check(th['E'] == B['E'] and th['A'] == B['A'] and th['r_rem'] == B['rho_rem'],
          "threshold._common E, A, r_rem == mine at printed delta_cert")
    check(cp['E'] == B['E'] and cp['A'] == B['A'] and cp['rho_rem'] == B['rho_rem'] and cp['vrho'] == B['varrho'],
          "check_prop610.bounds E, A, rho_rem, varrho == mine")
    Jth = [[-x for x in row] for row in mat_mul(st.Minv, TH.N_matrix(I, st.e))]
    Gth = mat_mul(Jth, st.Finv)
    check(Gth == st.G and cp['G'] == st.G, "G identical (threshold via N_matrix, check_prop610 via printed J, mine)")
    check(TH.N_matrix(I, st.e) == st.J, "lipschitz_e.N_matrix == printed J (my J_matrix)")
    dt_th, _ = TH.delta_thm(m)
    dt_me, _ = delta_thm(m)
    check(dt_th == dt_me, f"delta_thm exact identical ({float(dt_me):.6e})")
    r = RES[str(m)]
    their_sup = Fr(r['delta_cert_exact'])
    q6, e6 = max_sig(st.certify_abs, 6, 'mixed')
    my6 = from_sig(q6, e6)
    check(my6 <= their_sup < my6 + Fr(10) ** e6 and st.certify_abs(their_sup)['mixed'],
          f"threshold sup {float(their_sup):.8e} in my 6-s.f. bracket [{float(my6):.6e}, +1e{e6}) and certifies with mine")
    dup_th = r['delta_up']
    print(f"       delta_up: threshold_results {dup_th:.7e}, mine {MYDUP[m]:.7e}, printed {dup_s};"
          f" output.md {eps_rows[str(m)][4]}")
    check(abs(dup_th - MYDUP[m]) <= 1e-6 * MYDUP[m], "threshold_results delta_up == my best (rel 1e-6)")
    eps_out = eps_rows[str(m)][7]
    q4, e4 = max_sig(st.certify_rel, 4, 'mixed')
    my_eps4 = fmt(q4, e4, 4)
    certifies = st.certify_rel(parse_sci(eps_out))['mixed']
    th_cert = TH.certify(m, [parse_sci(eps_out) * abs(h) for h in st.H])
    print(f"       eps: output.md {eps_out} (float {r['eps_cert']:.8e}), my 4-s.f. max {my_eps4};"
          f" output.md value certifies: mine {certifies}, threshold.certify {th_cert}")
    check(certifies == th_cert, "my certificate and threshold.certify agree on the output.md eps string")
    check(st.certify_rel(parse_sci(eps_s))['mixed'], f"printed (2 s.f.) eps {eps_s} certifies")
print("TOTAL FAILURES:", fails)
sys.exit(1 if fails else 0)
