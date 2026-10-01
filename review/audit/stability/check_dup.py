"""P3: test the printed delta_up values.  For each row, build exact rational data within
(1+1e-3)*delta_up of H(m) whose exact recovery has a root with real part exactly a +- 1/2 (a tie),
and a second data vector (still within the tolerance) whose recovery rounds to the wrong multiset.
The optimiser is numerical (floats); every reported datum is rebuilt and evaluated exactly.
Run from repo root: python3 review/audit/stability/check_dup.py"""
import sys, os, json, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s5_lib import *
import numpy as np
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

TABLE = [((2, 8, 8), '2.485e-03', '8-1/2'), ((3, 3, 12), '4.589e-03', '3+1/2'),
         ((3, 10, 15, 30), '7.488e-03', '10+1/2'), ((4, 5, 21, 28), '2.018e-03', '5-1/2'),
         ((2, 3, 7), '6.587e-03', '3-1/2'), ((4, 4, 4), '5.036e-04', '4+1/2'), ((7, 7, 7), '8.273e-05', '7-1/2'),
         ((3, 3, 4, 4), '1.195e-04', '4-1/2'), ((5, 5, 5, 5), '3.826e-05', '5-1/2'), ((2, 2, 2, 3), '2.520e-04', '3-1/2'),
         ((2, 2, 2, 2, 3), '5.743e-05', '2+1/2')]

def Hf_factory(n):
    L = np.array([[float(x) for x in r] for r in L_matrix(n)])
    h = np.array([float(x) for x in h0(n)])
    K = 2 * n - 3
    def Hf(coef):  # coef high->low, monic, real; Newton identities in floats (search heuristic only)
        e = [(-1) ** j * coef[j] for j in range(n + 1)]
        p = [float(n)] + [0.0] * K
        for k in range(1, K + 1):
            acc = 0.0
            for i in range(1, min(k, n + 1)):
                acc += (-1) ** (i - 1) * e[i] * p[k - i]
            if k <= n:
                acc += (-1) ** (k - 1) * k * e[k]
            p[k] = acc
        R = e[n - 1] / e[n]
        return L @ np.array([R] + [p[2 * l - 1] for l in range(1, n)]) + h
    return Hf

def minimax(fun_vec, x0):
    """min_x max_nu |fun_vec(x)_nu| via the epigraph form (SLSQP), then Nelder-Mead polish."""
    t0 = float(np.max(np.abs(fun_vec(x0))))
    z0 = np.concatenate([x0, [t0]])
    cons = [{'type': 'ineq', 'fun': lambda z: z[-1] - fun_vec(z[:-1])},
            {'type': 'ineq', 'fun': lambda z: z[-1] + fun_vec(z[:-1])}]
    best = (t0, x0)
    try:
        r = minimize(lambda z: z[-1], z0, method='SLSQP', constraints=cons, options=dict(maxiter=500, ftol=1e-16))
        v = float(np.max(np.abs(fun_vec(r.x[:-1]))))
        if v < best[0]:
            best = (v, r.x[:-1])
    except Exception:
        pass
    obj = lambda x: float(np.max(np.abs(fun_vec(x))))
    r = minimize(obj, best[1], method='Nelder-Mead', options=dict(xatol=1e-13, fatol=1e-18, maxiter=6000, maxfev=6000))
    if r.fun < best[0]:
        best = (r.fun, r.x)
    return best

def exact_dev(coef, Hm):
    H, I, e = heat_from_poly(coef)
    return max(abs(x - y) for x, y in zip(H, Hm)), H

def polymul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c

def rat(x, D=10 ** 12):
    return F(round(x * D), D)

results = []
fail = []
for m, p_up, where in TABLE:
    n = len(m)
    Hm = heat_direct(m)
    Hf = Hf_factory(n)
    Hmf = np.array([float(x) for x in Hm])
    tol = F(p_up) * (1 + F(1, 1000))
    best = None
    for a, k in multiset(m):
        for sgn in (-1, 1):
            c = F(a) + sgn * HALF
            others = list(m); others.remove(a)
            # shape 1: (z - c) g(z), g monic of degree n-1, parametrised by its coefficients
            starts = [np.poly(others)]
            # shape 2: ((z-c)^2 + y^2) g(z), g of degree n-2 (remove a and one further order)
            starts2 = []
            for b in set(others):
                o2 = list(others); o2.remove(b)
                for y0 in (0.05, 0.3, 0.8):
                    starts2.append((np.poly(o2) if o2 else np.array([1.0]), y0))
            cf = float(c)
            cands = []
            for g0 in starts:
                sc = np.where(np.abs(g0[1:]) > 0, np.abs(g0[1:]), 1.0)
                f1 = lambda y, g0=g0, sc=sc: Hf(np.polymul([1, -cf], np.concatenate([[1.0], g0[1:] + sc * y]))) - Hmf
                v, y = minimax(f1, np.zeros(len(g0) - 1))
                cands.append(('real', v, g0[1:] + sc * y))
            for g0, y0 in starts2:
                sc = np.where(np.abs(g0[1:]) > 0, np.abs(g0[1:]), 1.0)
                def f2(w, g0=g0, sc=sc):
                    g = np.concatenate([[1.0], g0[1:] + sc * w[1:]])
                    return Hf(np.polymul([1, -2 * cf, cf * cf + w[0] ** 2], g)) - Hmf
                v, w = minimax(f2, np.concatenate([[y0], np.zeros(len(g0) - 1)]))
                cands.append(('pair', v, np.concatenate([[w[0]], g0[1:] + sc * w[1:]])))
            for shape, fv, x in cands:
                if shape == 'real':
                    coef = polymul([F(1), -c], [F(1)] + [rat(v) for v in x])
                else:
                    y = rat(x[0])
                    coef = polymul([F(1), -2 * c, c * c + y * y], [F(1)] + [rat(v) for v in x[1:]])
                if any(z == 0 for z in [coef[-1]]):
                    continue
                dev, H = exact_dev(coef, Hm)
                if best is None or dev < best[0]:
                    best = (dev, shape, a, c, coef, x)
    dev, shape, a, c, coef, x = best
    n_ = n
    # exact recovery of the tie polynomial
    et, It = recover_e(heat_from_poly(coef)[0], n)
    rec = [F(1)] + [(-1) ** j * et[j] for j in range(1, n + 1)]
    assert rec == coef, 'recovery is not q~ itself'
    ok, info = rounds_to(rec, m)
    tie = (not ok) and info[0] == 'undecided'
    # push the root across: c' = c + sgn*tau (real shape) or real part shifted (pair shape)
    wrong = None
    for sgn, tau in itertools.product((1, -1), [F(1, 10 ** p) for p in (9, 8, 7, 6)]):
        c2 = c + sgn * tau
        if shape == 'real':
            coef2 = polymul([F(1), -c2], [F(1)] + [rat(v) for v in x])
        else:
            y = rat(x[0])
            coef2 = polymul([F(1), -2 * c2, c2 * c2 + y * y], [F(1)] + [rat(v) for v in x[1:]])
        dev2, H2 = exact_dev(coef2, Hm)
        et2, _ = recover_e(H2, n)
        rec2 = [F(1)] + [(-1) ** j * et2[j] for j in range(1, n + 1)]
        ok2, info2 = rounds_to(rec2, m)
        if dev2 <= tol and not ok2 and info2[0] == 'count':
            wrong = (sgn * tau, dev2, info2)
    within = dev <= tol
    # informational: smallest delta at which some corner of the box |dH_nu| <= delta fails (exact)
    Linv = inv(L_matrix(n))
    def corner_fails(d):
        for sg in itertools.product([-1, 1], repeat=n):
            et_, _ = recover_e([h + s_ * d for h, s_ in zip(Hm, sg)], n, Linv)
            ok_, _ = rounds_to([F(1)] + [(-1) ** j * et_[j] for j in range(1, n + 1)], m)
            if not ok_:
                return True
        return False
    cf_lo, cf_hi = F(0), tol
    corner_thr = None
    if corner_fails(cf_hi):
        for _ in range(26):
            mid = (cf_lo + cf_hi) / 2
            if corner_fails(mid):
                cf_hi = mid
            else:
                cf_lo = mid
        corner_thr = cf_hi
    ratio = dev / F(p_up)
    row = dict(m=m, printed_up=p_up, where_printed=where, where_found='%s%s1/2' % (a, '+' if c > a else '-'), shape=shape,
               dev_exact='%.6e' % float(dev), ratio_to_printed=float(ratio), within_tol=within, tie=tie,
               corner_fail_threshold=None if corner_thr is None else '%.4e' % float(corner_thr),
               wrong=None if wrong is None else dict(tau=str(wrong[0]), dev='%.6e' % float(wrong[1]), detail=str(wrong[2])))
    results.append(row)
    log('%-16s printed d_up %s at %s | built %s-shape at %s, exact ||dH|| = %.6e (= %.6f x printed), within (1+1e-3) d_up: %s, tie: %s, wrong rounding built: %s | smallest failing box corner ~ %s'
        % (str(m), p_up, where, shape, row['where_found'], float(dev), float(ratio), within, tie,
           'yes (tau=%s, ||dH||=%s)' % (row['wrong']['tau'], row['wrong']['dev']) if wrong else 'no', row['corner_fail_threshold']))
    if not (within and tie and wrong):
        fail.append(m)

json.dump(results, open(os.path.join(HERE, 'check_dup.json'), 'w'), indent=1, default=str)
open(os.path.join(HERE, 'check_dup.txt'), 'w').write('\n'.join(out) + '\n' +
     ('ALL CHECKS PASSED\n' if not fail else 'NOT CONSTRUCTED FOR: %s\n' % fail))
if fail:
    print('NOT CONSTRUCTED FOR', fail); sys.exit(1)
print('ALL CHECKS PASSED')
