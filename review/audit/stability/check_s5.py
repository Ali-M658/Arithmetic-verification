"""P3: Proposition S5 certificate re-implemented from its statement; re-certify every printed
delta_cert exactly; largest certified value (4 s.f., rounded down); delta_thm from Theorem S4;
relative columns; rounding-convention claims of ST.13.
Run from repo root: python3 review/audit/stability/check_s5.py"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s5_lib import *

HERE = os.path.dirname(os.path.abspath(__file__))
out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

# m, delta_thm, delta_cert, delta_up, failure-at, rel columns, eps_cert   (ST.14, verbatim)
TABLE = [
    ((2, 8, 8), '3.80e-07', '2.341e-03', '2.485e-03', '8-1/2', ['1.8e-02', '1.6e-03', '7.0e-04'], '1.9e-03'),
    ((3, 3, 12), '1.18e-07', '4.040e-03', '4.589e-03', '3+1/2', ['3.2e-02', '2.8e-03', '7.4e-04'], '4.4e-03'),
    ((3, 10, 15, 30), '4.02e-11', '3.660e-03', '7.488e-03', '10+1/2', ['4.9e-03', '8.0e-04', '4.1e-05', '3.6e-07'], '8.7e-04'),
    ((4, 5, 21, 28), '3.14e-11', '1.461e-03', '2.018e-03', '5-1/2', ['1.9e-03', '3.2e-04', '1.6e-05', '1.7e-07'], '4.6e-04'),
    ((2, 3, 7), '4.49e-07', '3.658e-03', '6.587e-03', '3-1/2', ['3.0e-01', '4.0e-03', '2.7e-03'], '5.0e-03'),
    ((4, 4, 4), '9.35e-07', '4.539e-04', '5.036e-04', '4+1/2', ['3.6e-03', '5.0e-04', '5.4e-04'], '8.2e-04'),
    ((7, 7, 7), '9.97e-08', '8.068e-05', '8.273e-05', '7-1/2', ['2.8e-04', '4.9e-05', '2.3e-05'], '1.2e-04'),
    ((3, 3, 4, 4), '1.48e-09', '9.597e-05', '1.195e-04', '4-1/2', ['2.3e-04', '1.0e-04', '1.1e-04', '7.2e-05'], '1.1e-04'),
    ((5, 5, 5, 5), '4.74e-10', '3.617e-05', '3.826e-05', '5-1/2', ['6.0e-05', '2.5e-05', '1.9e-05', '6.2e-06'], '3.1e-05'),
    ((2, 2, 2, 3), '2.03e-09', '1.858e-04', '2.520e-04', '3-1/2', ['2.2e-03', '3.2e-04', '5.6e-04', '7.7e-04'], '4.3e-04'),
    ((2, 2, 2, 2, 3), '2.72e-12', '7.908e-06', '5.743e-05', '2+1/2', ['2.3e-05', '1.2e-05', '2.1e-05', '2.9e-05', '1.9e-05'], '1.4e-05'),
]

failures = []

# ---------------------------------------------------------------- 0. validate G = (D_I e) L^{-1}
for m in [(2, 8, 8), (3, 10, 15, 30), (2, 2, 2, 2, 3)]:
    C = Cert(m)
    n = C.n
    random.seed(7)
    u = [F(random.randint(-5, 5), random.randint(1, 3)) for _ in range(n)]
    errs = []
    for h in (F(1, 10 ** 6), F(1, 10 ** 9)):
        It = [x + h * y for x, y in zip(C.I, u)]
        Mt, bt = M_b(It, n)
        et = solve(Mt, bt)
        fd = [(x - y) / h for x, y in zip(et, C.e[1:])]
        lin = matvec(C.DIe, u)
        errs.append(max(abs(x - y) for x, y in zip(fd, lin)))
    assert errs[1] < errs[0] / 100, errs  # O(h) convergence: D_I e is the exact derivative
log('G = (D_I e) L^-1 validated against exact difference quotients (O(h) convergence)')

# ---------------------------------------------------------------- 1. sanity: E really bounds |e~ - e|
random.seed(11)
for m in [(2, 8, 8), (4, 4, 4), (3, 3, 4, 4)]:
    C = Cert(m); n = C.n
    d = F(TABLE[[t[0] for t in TABLE].index(m)][2])
    bd = C.bounds([d] * n)
    for trial in range(60):
        dH = [d * random.choice([-1, 1]) if trial % 2 == 0 else d * F(random.randint(-1000, 1000), 1000) for _ in range(n)]
        Ht = [x + y for x, y in zip(C.H, dH)]
        et, It = recover_e(Ht, n, C.Linv)
        Delta = [x - y for x, y in zip(et[1:], C.e[1:])]
        assert all(abs(x) <= y for x, y in zip(Delta, bd['E'])), (m, Delta, bd['E'])
        lin = matvec(C.G, dH)
        assert all(abs(x - y) <= z for x, y, z in zip(Delta, lin, bd['varrho']))
log('E bounds |e~-e| and varrho bounds the nonlinear remainder on 180 exact samples')

# ---------------------------------------------------------------- 2. per-row results
def max_certified(C, start):
    lo = F(start)
    assert C.certified(lo)
    hi = lo * 2
    while C.certified(hi):
        lo, hi = hi, hi * 2
    for _ in range(40):
        mid = (lo + hi) / 2
        if C.certified(mid):
            lo = mid
        else:
            hi = mid
    best = round_down_sig(lo, 4)
    while not C.certified(best):  # guard against non-monotone behaviour near the edge
        best = round_down_sig(best - F(1, 10 ** 30), 4)
    nxt = round_up_sig(best + best / 10 ** 6, 4)
    return best, lo, hi, nxt, C.certified(nxt)

def fmt(x, s=4):
    return ('%.' + str(s - 1) + 'e') % float(x)

rows = []
for (m, p_thm, p_cert, p_up, fat, p_rel, p_eps) in TABLE:
    C = Cert(m); n = C.n
    # Theorem S4
    dthm, parts = theorem_s4(m)
    thm_rd = round_down_sig(dthm, 3)
    thm_ok = thm_rd == F(p_thm)
    # certificate at the printed value
    pc = F(p_cert)
    oi, oii, det_ = C.test([pc] * n)
    certified = oi or oii
    # largest certified (4 s.f., rounded down)
    best, lo, hi, nxt, nxt_ok = max_certified(C, pc if certified else F(1, 10 ** 12))
    # relative columns
    rel = [pc / abs(h) for h in C.H]
    rel_ok = all(round_down_sig(r, 2) == F(s) or F(fmt(r, 2)) == F(s) for r, s in zip(rel, p_rel))
    # eps_cert: rho_nu = eps |H_nu|
    pe = F(p_eps)
    ti, tii, _ = C.test([pe * abs(h) for h in C.H])
    eps_ok = ti or tii
    # eps max
    lo_e, hi_e = (pe, pe * 2) if eps_ok else (F(0), pe)
    while (lambda t: t[0] or t[1])(C.test([hi_e * abs(h) for h in C.H])[:2]):
        lo_e, hi_e = hi_e, hi_e * 2
    for _ in range(30):
        mid = (lo_e + hi_e) / 2
        tt = C.test([mid * abs(h) for h in C.H])
        if tt[0] or tt[1]:
            lo_e = mid
        else:
            hi_e = mid
    row = dict(m=m, n=n, p_thm=p_thm, my_thm=fmt(dthm, 3), my_thm_exact=str(dthm), thm_rounddown=fmt(thm_rd, 3), thm_ok=thm_ok,
               p_cert=p_cert, cert_test_i=oi, cert_test_ii=oii, certified=certified,
               radii={str(a): [str(x) for x in v] for a, v in det_.items()} if isinstance(det_, dict) else det_,
               my_max=fmt(best, 4), next_up=fmt(nxt, 4), next_up_certified=nxt_ok,
               rel=[fmt(r, 2) for r in rel], rel_ok=rel_ok, p_eps=p_eps, eps_certified=eps_ok,
               my_eps_max=fmt(round_down_sig(lo_e, 2), 2),
               zeta=str(parts['zeta']), kappa=fmt(parts['kappa'], 6), rho=fmt(parts['rho'], 6), lam=fmt(parts['lam'], 6))
    rows.append(row)
    log('%-16s thm: printed %s mine %s (exact rounds down to %s) %s | cert @%s: (i)=%s (ii)=%s -> %s | my max %s (next %s certified=%s) | rel %s %s | eps %s certified=%s (my max %s)'
        % (str(m), p_thm, row['my_thm'], row['thm_rounddown'], 'OK' if thm_ok else 'MISMATCH', p_cert, oi, oii,
           'CERTIFIED' if certified else 'NOT CERTIFIED', row['my_max'], row['next_up'], nxt_ok,
           row['rel'], 'OK' if rel_ok else 'MISMATCH', p_eps, eps_ok, row['my_eps_max']))
    if not thm_ok:
        failures.append(('delta_thm', m))
    if not certified:
        failures.append(('delta_cert not certified', m))
    if not rel_ok:
        failures.append(('relative column', m))
    if not eps_ok:
        failures.append(('eps_cert not certified', m))

# ---------------------------------------------------------------- 3. ST.13: up-rounded values must fail
for m, v in [((2, 8, 8), '2.342e-3'), ((4, 5, 21, 28), '1.462e-3')]:
    C = Cert(m)
    ok = C.certified(F(v))
    log('ST.13 claim: test fails at %s for %s: %s' % (v, m, 'confirmed' if not ok else 'NOT confirmed (certifies)'))
    if ok:
        failures.append(('ST.13 claim', m))

json.dump(rows, open(os.path.join(HERE, 'check_s5.json'), 'w'), indent=1)
open(os.path.join(HERE, 'check_s5.txt'), 'w').write('\n'.join(out) + '\n' +
     ('ALL CHECKS PASSED\n' if not failures else 'FAILURES: %s\n' % failures))
if failures:
    print('FAILURES:', failures)
    sys.exit(1)
print('ALL CHECKS PASSED')
