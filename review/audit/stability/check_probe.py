"""P3 soundness probe: for every table row, >= 2000 exact rational data vectors uniform in the
certified box |H~_nu - H_nu(m)| <= delta_cert (printed value), all 2^n corners included.  Each is run
through the recovery map (front end, exact linear solve, exact polynomial, exact Routh-Hurwitz
strip counts = certified isolation of the real parts, rounding) and must return m.
Informational power check: corners of the box at the printed delta_up.
Run from repo root: python3 review/audit/stability/check_probe.py [samples_per_row]"""
import sys, os, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s5_lib import *

HERE = os.path.dirname(os.path.abspath(__file__))
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

TABLE = [((2, 8, 8), '2.341e-03', '2.485e-03'), ((3, 3, 12), '4.040e-03', '4.589e-03'),
         ((3, 10, 15, 30), '3.660e-03', '7.488e-03'), ((4, 5, 21, 28), '1.461e-03', '2.018e-03'),
         ((2, 3, 7), '3.658e-03', '6.587e-03'), ((4, 4, 4), '4.539e-04', '5.036e-04'),
         ((7, 7, 7), '8.068e-05', '8.273e-05'), ((3, 3, 4, 4), '9.597e-05', '1.195e-04'),
         ((5, 5, 5, 5), '3.617e-05', '3.826e-05'), ((2, 2, 2, 3), '1.858e-04', '2.520e-04'),
         ((2, 2, 2, 2, 3), '7.908e-06', '5.743e-05')]

def recover_and_round(Ht, m, Linv):
    n = len(m)
    et, _ = recover_e(Ht, n, Linv)
    coef = [F(1)] + [(-1) ** j * et[j] for j in range(1, n + 1)]
    return rounds_to(coef, m)

bad = []
random.seed(20261001)
D = 10 ** 9
for m, pc, pu in TABLE:
    n = len(m)
    H = heat_direct(m)
    Linv = inv(L_matrix(n))
    d = F(pc)
    pts = [list(s) for s in itertools.product([-1, 1], repeat=n)]
    pts = [[F(x) for x in p] for p in pts]
    while len(pts) < NS + 2 ** n:
        pts.append([F(random.randint(-D, D), D) for _ in range(n)])
    nfail = 0
    for p in pts:
        Ht = [h + d * x for h, x in zip(H, p)]
        ok, info = recover_and_round(Ht, m, Linv)
        if not ok:
            nfail += 1
            bad.append((m, p, info))
    # power check (informational): corners of the delta_up box
    du = F(pu) * (1 + F(1, 1000))
    cfail = 0
    for p in itertools.product([-1, 1], repeat=n):
        ok, info = recover_and_round([h + du * x for h, x in zip(H, p)], m, Linv)
        cfail += (not ok)
    log('%-16s delta_cert=%s: %d samples (%d corners + %d uniform) -> %d failures | info: %d/%d corners of the (1+1e-3)delta_up box fail'
        % (str(m), pc, len(pts), 2 ** n, len(pts) - 2 ** n, nfail, cfail, 2 ** n))

open(os.path.join(HERE, 'check_probe.txt'), 'w').write('\n'.join(out) + '\n' +
     ('ALL CHECKS PASSED\n' if not bad else 'FAILURES: %s\n' % bad[:20]))
if bad:
    print('FAILURES', bad[:20]); sys.exit(1)
print('ALL CHECKS PASSED')
