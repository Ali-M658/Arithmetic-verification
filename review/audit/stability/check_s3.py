"""ST.7 Lemma S3, ST.8 Theorem S3, ST.9 Proposition S3.2, ST.10 Remark S3.3.
Root counts in discs are exact: Moebius map of the disc to the left half-plane + Routh array.
Run from repo root: python3 review/audit/stability/check_s3.py"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s5_lib import *
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

def polymul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c

def polyadd(a, b):
    L = max(len(a), len(b)); a = [F(0)] * (L - len(a)) + a; b = [F(0)] * (L - len(b)) + b
    return [x + y for x, y in zip(a, b)]

def disc_count(coef, a, r):
    """exact number of roots of coef (high->low) in the open disc |z-a| < r; None if a root lies on the circle."""
    n = len(coef) - 1
    # p(w) = coef(a + r w)
    p = poly_shift(coef, F(a))
    p = [c * F(r) ** (n - i) for i, c in enumerate(p)]
    # w = (1+s)/(1-s):  Q(s) = sum_i p_i (1+s)^{n-i} (1-s)^i ; |w|<1 <=> Re s < 0
    Q = [F(0)] * (n + 1)
    for i, c in enumerate(p):
        term = [c]
        for _ in range(n - i):
            term = polymul(term, [F(1), F(1)])
        for _ in range(i):
            term = polymul(term, [F(-1), F(1)])
        Q = polyadd(Q, term)
    while Q and Q[0] == 0:
        Q.pop(0)
    dropped = n - (len(Q) - 1)  # roots at w = -1 (on the circle)
    if dropped:
        return None
    rh = rhp_count(Q)
    if rh is None:
        return None
    return (len(Q) - 1) - rh

def kth_root_up(x, k):
    """rational y >= x^{1/k} (x >= 0), within relative 1e-12."""
    if x == 0:
        return F(0)
    y = F(float(x) ** (1.0 / k)).limit_denominator(10 ** 15)
    while y ** k < x:
        y *= F(1000000000001, 10 ** 12)
    return y

# ---------------------------------------------------------------- Lemma S3
random.seed(5)
tested = 0
for trial in range(600):
    n = random.choice([2, 3, 4, 5])
    kind = trial % 3
    if kind == 0:
        base = [F(random.randint(1, 40), 40) for _ in range(n)]
    elif kind == 1:
        a0 = F(random.randint(1, 40), 40); k0 = random.randint(2, n)
        base = [a0] * k0 + [F(random.randint(1, 40), 40) for _ in range(n - k0)]
    else:
        base = [F(1)] + [F(random.randint(1, 1000), 1000) for _ in range(n - 1)]
    mx = max(base); base = [x / mx for x in base]  # scale-free, max = 1
    coef = poly_from_roots(base)
    eps = F(1, 10 ** random.randint(3, 12))
    sgn = [random.choice([-1, 1]) for _ in range(n)]
    pert = [F(0)] + [s * eps if trial % 2 else eps * F(random.randint(-100, 100), 100) for s in sgn]
    qt = [c + d for c, d in zip(coef, pert)]
    for a, k in multiset(base):
        others = [(b, kb) for b, kb in multiset(base) if b != a]
        g = min([abs(a - b) for b, _ in others], default=None)
        Q = F(1)
        for b, kb in others:
            Q *= abs(a - b) ** kb
        cap = min(g, F(1)) / 2 if g is not None else F(1, 2)
        r = kth_root_up(F(2) ** (1 - k) * 3 ** n * eps / Q, k)
        if r > cap:
            continue
        assert r ** k * Q >= F(2) ** (1 - k) * 3 ** n * eps
        c = disc_count(qt, a, r)
        assert c == k, (base, a, k, eps, r, c)
        # and also at the edge r = cap
        c2 = disc_count(qt, a, cap)
        assert c2 == k
        tested += 1
log('Lemma S3: exact disc counts equal k at r = r_a(eps) and r = min(g,1)/2 on %d (cluster, perturbation) pairs' % tested)

# |z| <= 3/2 and sum_{j>=1} (3/2)^{n-j} < 3^n 2^{1-n}
for n in range(1, 30):
    assert sum(F(3, 2) ** (n - j) for j in range(1, n + 1)) < F(3) ** n * F(2) ** (1 - n)
log('sum_{j=1}^n (3/2)^{n-j} = 2((3/2)^n - 1) < 3^n 2^{1-n}: OK; with |a-b|-r >= |a-b|/2 this gives the 2^{1-k} 3^n constant')

# ---------------------------------------------------------------- Theorem S3 (edge of hypotheses)
random.seed(9)
tested = 0
for trial in range(120):
    n = random.choice([2, 3, 4])
    kind = trial % 3
    if kind == 0:
        m = sorted(random.sample(range(2, 20), n))
    elif kind == 1:
        a0 = random.randint(2, 9); m = [a0] * n if trial % 2 else [a0] * (n - 1) + [a0 + random.randint(1, 5)]
    else:
        m = [1] + [random.choice([2, 3, 50, 400]) for _ in range(n - 1)]
    m = [F(x) for x in m]
    dthm, P = theorem_s4([int(x) for x in m])
    mu = max(m)
    lam, kap, zet, rho = P['lam'], P['kappa'], P['zeta'], P['rho']
    delta = min(1 / lam, 1 / (2 * kap * zet * lam))  # edge of both hypotheses
    # largest delta for which the radius hypothesis holds for every order (edge of all hypotheses)
    for a, k in multiset(m):
        Qh = F(1); gh = None
        for b, kb in multiset(m):
            if b != a:
                Qh *= abs(a - b) ** kb / mu ** kb
                gh = abs(a - b) / mu if gh is None else min(gh, abs(a - b) / mu)
        cap_hat = (min(gh, F(1)) if gh is not None else F(1)) / 2
        delta = min(delta, cap_hat ** k * Qh / (F(2) ** (2 - k) * 3 ** n * kap * rho * lam))
    H = heat_direct(m)
    Linv = inv(L_matrix(n))
    for corner in range(4):
        sg = [random.choice([-1, 1]) for _ in range(n)]
        Ht = [h + s * delta for h, s in zip(H, sg)]
        et, _ = recover_e(Ht, n, Linv)
        qt = [F(1)] + [(-1) ** j * et[j] for j in range(1, n + 1)]
        mh = [x / mu for x in m]
        for a, k in multiset(m):
            Qh = F(1); gh = None
            for b, kb in multiset(m):
                if b != a:
                    Qh *= abs(a - b) ** kb / mu ** kb
                    gh = abs(a - b) / mu if gh is None else min(gh, abs(a - b) / mu)
            capm = mu * (min(gh, F(1)) if gh is not None else F(1)) / 2
            assert (capm / mu) ** k * Qh >= F(2) ** (2 - k) * 3 ** n * kap * rho * lam * delta
            ra = min(capm, mu * kth_root_up(F(2) ** (2 - k) * 3 ** n * kap * rho * lam * delta / Qh, k))
            c = disc_count(qt, a, ra)
            assert c == k, (m, a, ra, c)
            tested += 1
log('Theorem S3: at the largest delta allowed by all three hypotheses (binding one attained with equality), exact disc counts confirm k_a roots within r_a on %d clusters' % tested)

# ---------------------------------------------------------------- Theorem S4: corners of the delta_thm box
import itertools
random.seed(13)
cases = [[1, 2], [1, 1, 5], [2, 2], [2, 3], [1, 2, 1000], [2, 2, 2], [3, 3, 3, 3], [2, 5, 400, 401], [1, 1, 1, 2],
         [6, 7, 8, 9], [2, 3, 3, 1000]]
for _ in range(25):
    n = random.choice([2, 3, 4])
    cases.append([random.choice([1, 2, 3, 4, 7, 12, 30, 200]) for _ in range(n)])
done = 0
for m in cases:
    n = len(m)
    d, _ = theorem_s4(m)
    H = heat_direct(m); Linv = inv(L_matrix(n))
    for sg in itertools.product([-1, 1], repeat=n):
        et, _ = recover_e([h + s_ * d for h, s_ in zip(H, sg)], n, Linv)
        ok, info = rounds_to([F(1)] + [(-1) ** j * et[j] for j in range(1, n + 1)], m)
        assert ok, (m, sg, info)
        done += 1
log('Theorem S4: all %d corners of the delta_thm boxes of %d multisets (orders 1, repeats, ratios up to 1000) round to m' % (done, len(cases)))

# ---------------------------------------------------------------- Proposition S3.2 (i)
s = sp.Symbol('s')
def sym_I(ms):
    n = len(ms)
    return [sum(1 / x for x in ms)] + [sum(x ** (2 * l - 1) for x in ms) for l in range(1, n)]
def Lsym(n):
    return sp.Matrix(n, n, lambda i, j: sp.Rational(L_matrix(n)[i][j].numerator, L_matrix(n)[i][j].denominator))
I0 = sym_I([8 + s, 8 - s, 2]); I00 = sym_I([8, 8, 2])
dI = [sp.simplify(x - y) for x, y in zip(I0, I00)]
assert sp.simplify(dI[0] - 2 * s ** 2 / (8 * (64 - s ** 2))) == 0
assert dI[1] == 0 and sp.expand(dI[2] - 48 * s ** 2) == 0
log('S3.2(i) (2,8,8): dR = 2s^2/(8(64-s^2)) = s^2/(4(64-s^2)), dP1 = 0, dP3 = 48 s^2: confirmed exactly')

def limit_ratio(ms_s, ms0, k):
    n = len(ms0)
    dIs = sp.Matrix([sp.simplify(x - y) for x, y in zip(sym_I(ms_s), sym_I(ms0))])
    dH = Lsym(n) * dIs
    lead = []
    for comp in dH:
        ser = sp.series(comp, s, 0, k + 1).removeO()
        for j in range(1, k):
            assert sp.expand(ser).coeff(s, j) == 0
        lead.append(abs(sp.expand(ser).coeff(s, k)))
    c = max(lead)
    return sp.N(c ** sp.Rational(-1, k), 12), c

claims = [([8 + s, 8 - s, 2], [8, 8, 2], '2.7385'), ([3 + s, 3 - s, 12], [3, 3, 12], '4.4630'),
          ([3 + s, 3 - s, 4, 4], [3, 3, 4, 4], '2.0446'), ([3, 3, 4 + s, 4 - s], [3, 3, 4, 4], '1.3593')]
for ms_s, ms0, cl in claims:
    v, c = limit_ratio(ms_s, ms0, 2)
    log('  S3.2(i) %s: limit s/||dH||^(1/2) = %s (claimed %s)' % (ms0, sp.N(v, 8), cl))
    assert abs(v - sp.Float(cl)) < sp.Float('0.00005') + 1e-12 or sp.floor(v * 10 ** 4) / 10 ** 4 == sp.Float(cl)

# ---------------------------------------------------------------- Proposition S3.2 (ii)
z = sp.Symbol('z')
def heat_of_poly_sym(qpoly, n):
    P = sp.Poly(qpoly, z)
    co = P.all_coeffs()
    e = [sp.Integer(1)] + [(-1) ** j * co[j] for j in range(1, n + 1)]
    K = 2 * n - 3
    p = [sp.Integer(n)] + [0] * K
    for kk in range(1, K + 1):
        acc = 0
        for i in range(1, kk):
            if i <= n:
                acc += (-1) ** (i - 1) * e[i] * p[kk - i]
        if kk <= n:
            acc += (-1) ** (kk - 1) * kk * e[kk]
        p[kk] = sp.expand(acc)
    I = [e[n - 1] / e[n]] + [p[2 * l - 1] for l in range(1, n)]
    return Lsym(n) * sp.Matrix(I)

for a, k, gl in [(4, 3, []), (7, 3, []), (2, 3, [3]), (5, 4, [])]:
    gpoly = sp.prod([z - c for c in gl]) if gl else sp.Integer(1)
    n = k + len(gl)
    qs = sp.expand(((z - a) ** k - s ** k) * gpoly)
    q0 = sp.expand(((z - a) ** k) * gpoly)
    dH = heat_of_poly_sym(qs, n) - heat_of_poly_sym(q0, n)
    lead = []
    for comp in dH:
        ser = sp.expand(sp.series(sp.simplify(comp), s, 0, k + 1).removeO())
        for j in range(1, k):
            assert ser.coeff(s, j) == 0
        lead.append(abs(ser.coeff(s, k)))
    c = max(lead)
    lim = sp.N(c ** sp.Rational(-1, k), 10)
    # exact recovery at a rational s: Theorem B returns q_s
    sv = F(1, 1000)
    co = sp.Poly(qs.subs(s, sp.Rational(1, 1000)), z).all_coeffs()
    coefF = [F(int(sp.fraction(x)[0]), int(sp.fraction(x)[1])) for x in co]
    Hs, Is, es = heat_from_poly(coefF)
    et, _ = recover_e(Hs, n)
    assert et == es
    log('  S3.2(ii) a=%d k=%d g=%s: dH = O(s^%d), limit s/||dH||^(1/%d) = %s; exact recovery returns q_s at s=1/1000'
        % (a, k, gl, k, k, lim))

# ---------------------------------------------------------------- Remark S3.3
d1, d2, d3, A = sp.symbols('d1 d2 d3 a', real=True)
f = lambda x: x ** 3 - 3 * A ** 2 * x
lhs = sum(f(A + d) for d in (d1, d2, d3)) - 3 * f(A)
assert sp.expand(lhs - (3 * A * (d1 ** 2 + d2 ** 2 + d3 ** 2) + d1 ** 3 + d2 ** 3 + d3 ** 3)) == 0
random.seed(4)
for _ in range(3000):
    a = F(random.randint(1, 50))
    d = [a * F(random.randint(-10 ** 6, 10 ** 6), 10 ** 6) for _ in range(3)]
    D = sum(3 * a * x * x + x ** 3 for x in d)
    assert D >= 2 * a * sum(x * x for x in d)
    assert max(x * x for x in d) <= D / (2 * a)
log('Remark S3.3: identity verified symbolically; inequality on 3000 exact samples with |d_i| <= a')

open(os.path.join(HERE, 'check_s3.txt'), 'w').write('\n'.join(out) + '\nALL CHECKS PASSED\n')
print('ALL CHECKS PASSED')
