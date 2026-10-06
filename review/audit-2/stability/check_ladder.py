"""check_ladder: the radius ladder of Prop. S5 read as {k/40 : k = 20, 19, ..., 1} U {1/100, 1/1000} (22 radii).

Shows (a) the reading: 1/2 = 20/40, step 19/40 - 20/40 = -1/40 reaches 1/40 after 19 steps (arithmetic); a geometric
reading with ratio 19/20 never reaches 1/40 exactly; (b) sensitivity: the certified sup (6 s.f., test (ii)) with
the printed ladder vs a 10x finer ladder {k/400 : k = 200..1} U {1/1000}; (c) the first passing radius per order at
the printed delta_cert.
"""
import sys
from fractions import Fraction as Fr
from stab610 import *
from rows_table import TABLE, max_sig

assert LADDER[0] == Fr(1, 2) and LADDER[1] == Fr(19, 40) and LADDER[19] == Fr(1, 40) and len(LADDER) == 22
assert all(LADDER[i] - LADDER[i + 1] == Fr(1, 40) for i in range(19))
k = 0
x = Fr(1, 2)
while x > Fr(1, 40) and k < 200:
    x *= Fr(19, 20); k += 1
assert x != Fr(1, 40)
print("(a) ladder =", [str(r) for r in LADDER])
print("    geometric reading 1/2*(19/20)^k never equals 1/40 (first k below:", k, ")")
FINE = [Fr(k, 400) for k in range(200, 0, -1)] + [Fr(1, 1000)]
fails = 0
for m, dthm_s, dcert_s, *_ in TABLE:
    st = Setup(m)
    q, e = max_sig(st.certify_abs, 6, 'mixed')
    qf, ef = max_sig(lambda d: st.certify_abs(d, FINE), 6, 'mixed')
    r = st.certify_abs(parse_sci(dcert_s))
    radii = {a: str(v[1]) for a, v in r['per'].items()}
    gain = from_sig(qf, ef) / from_sig(q, e) - 1
    print(f"(b,c) {m}: sup printed ladder {fmt(q, e, 6)}, fine ladder {fmt(qf, ef, 6)} (gain {float(gain):.2%});"
          f" first passing radius (ii) per order at {dcert_s}: {radii}")
    if from_sig(qf, ef) < from_sig(q, e):
        fails += 1
        print("   FAIL: finer ladder gives smaller sup")
print("TOTAL FAILURES:", fails)
sys.exit(1 if fails else 0)
