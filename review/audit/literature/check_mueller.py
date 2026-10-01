#!/usr/bin/env python3
"""
P7 check: does Mueller-Feliu-Regensburger-Conradi-Shiu-Dickenstein (arXiv:1311.5493,
Found. Comput. Math. 16 (2016) 69-97) give the positive-real case of Theorem A?

Theorem A map:  I_n(m) = (R, P_1, P_3, ..., P_{2n-3}),  R = sum 1/m_i,  P_k = sum m_i^k.

Their setting (Def. 1.1): f_kappa(x) = A diag(kappa) x^B on the open positive orthant R^n_+,
and Thm 1.4 / Cor 2.8 characterise injectivity *for all kappa in R^r_+*:
    (i) f_kappa injective for all kappa  <=>  (ii) ker B = 0 and sigma(ker A) cap sigma(im B) = {0}.
Thm 1.5 (bnd): if all nonzero products det(A_[n],J) det(B_J,[n]) have one sign (and one is
nonzero), then A x^B = y has at most one positive solution.

Checks (exact arithmetic, sympy Rationals; every check is an assert; nonzero exit on failure):
  1. Direct encoding (variables m_1..m_n, monomials m_i^e, e in E={-1,1,3,..,2n-3}):
     ker B = 0 and an explicit nonzero w = Bv lies in ker A  =>  Cor. 2.8(ii) fails.
     The (bnd) minor products take both signs.  (Consistent with: the kappa=1 map is
     symmetric, so not injective on ordered tuples.)
  2. Elementary-symmetric encoding (variables e_1..e_n > 0; R = e_{n-1} e_n^{-1}, P_k = Newton
     polynomial in e): the kappa=1 map is NOT injective on R^n_+ -- exact witnesses
     e(b) from the complex multisets {ib, -ib, c_1, ..., c_{n-2}}; and (jac) of Thm 1.4 fails
     at kappa = 1 (explicit kernel vector of the Jacobian).  So no injectivity theorem on the
     full e-orthant (theirs or any other) can yield Theorem A; the relevant domain is the
     real-rooted region, which their framework does not treat.
  3. Restricted injectivity w.r.t. S cannot encode 'modulo permutation': for every nonzero d
     there are x, y in R^n_+ with x - y = d and y not a permutation of x (so S must be R^n).
  4. Steinig/Laurens route: for exponents a = (-1,1,3,..,2n-3) the kernel
     K(s)_k = a_k s^{a_k - 1} has all square minors of constant, nonzero sign on ordered
     positive points (sampled exactly), and the run-count lemma (at most n sign runs of the
     merged partial-sum step function) holds exhaustively on small configurations.
  5. Consistency: I_3, I_4 injective on integer multisets with small entries (exhaustive).
"""
import itertools, random, sys
from fractions import Fraction
import sympy as sp

random.seed(20261001)
FAIL = []
def check(cond, msg):
    if not cond:
        FAIL.append(msg); print("FAIL:", msg)
    assert cond, msg

# ---------------------------------------------------------------- 1. direct encoding
def direct_encoding(n):
    E = [-1] + list(range(1, 2*n-2, 2))          # -1, 1, 3, ..., 2n-3  (n exponents)
    cols = [(i, e) for e in E for i in range(n)]  # monomial x_i^e
    r = len(cols)
    A = sp.zeros(n, r); B = sp.zeros(r, n)
    for j, (i, e) in enumerate(cols):
        A[E.index(e), j] = 1
        B[j, i] = e
    return E, cols, A, B

print("== 1. direct encoding")
for n in range(2, 7):
    E, cols, A, B = direct_encoding(n)
    check(B.rank() == n, f"n={n}: ker B != 0")
    v = sp.Matrix([1, -1] + [0]*(n-2))
    w = B*v
    check(any(x != 0 for x in w) and all(x == 0 for x in A*w),
          f"n={n}: Bv not a nonzero element of ker A")
    # kappa = 1 map is not injective: swap of two coordinates
    x = [sp.Rational(k+2, 1) for k in range(n)]
    y = [x[1], x[0]] + x[2:]
    fx = [sum(xi**e for xi in x) for e in E]; fy = [sum(yi**e for yi in y) for e in E]
    check(fx == fy and x != y, f"n={n}: swap witness failed")
    print(f"  n={n}: r={len(cols)}, rank B={B.rank()}, w=Bv in ker A (w!=0): Cor 2.8(ii) fails")
    if n <= 4:   # Theorem 1.5 (bnd) minor products
        signs = set()
        for J in itertools.combinations(range(len(cols)), n):
            p = A[:, list(J)].det() * B[list(J), :].det()
            if p != 0: signs.add(sp.sign(p))
        check(signs == {1, -1}, f"n={n}: (bnd) products not of both signs: {signs}")
        print(f"  n={n}: Thm 1.5 (bnd) minor products take both signs -> hypothesis fails")

# ---------------------------------------------------------------- 2. e-encoding
print("== 2. elementary-symmetric encoding")
def newton_power_sums(n, K):
    """P_1..P_K as polynomials in e_1..e_n (Newton identities)."""
    e = sp.symbols(f"e1:{n+1}", positive=True)
    E_ = [sp.Integer(1)] + list(e) + [sp.Integer(0)]*(K+1)
    P = [None]*(K+1)
    for k in range(1, K+1):
        s = (-1)**(k-1) * k * E_[k]
        for i in range(1, k):
            s += (-1)**(i-1) * E_[i] * P[k-i]
        P[k] = sp.expand(s)
    return e, P

def elem(ms):
    z = sp.symbols('z')
    poly = sp.Poly(sp.expand(sp.prod([1 + m*z for m in ms])), z)
    co = poly.all_coeffs()[::-1]
    return [sp.nsimplify(sp.expand(c)) for c in co[1:]]

for n in range(3, 7):
    e, P = newton_power_sums(n, 2*n-3)
    Phi = [e[n-2]/e[n-1]] + [P[k] for k in range(1, 2*n-2, 2)]
    # generalized-polynomial form A x^B: collect monomials
    mons = []
    rows = []
    for comp in Phi:
        num, den = sp.fraction(sp.together(comp))
        terms = sp.Poly(sp.expand(num), *e).terms()
        dmon = sp.Poly(den, *e).monoms()[0] if den != 1 else (0,)*n
        row = {}
        for mon, c in terms:
            ex = tuple(a - b for a, b in zip(mon, dmon))
            if ex not in mons: mons.append(ex)
            row[ex] = c
        rows.append(row)
    A = sp.Matrix([[row.get(m, 0) for m in mons] for row in rows])
    B = sp.Matrix([list(m) for m in mons])
    check(B.rank() == n, f"e-encoding n={n}: ker B != 0")
    check(any(c < 0 for c in A) and any(c > 0 for c in A), f"n={n}: coefficients not mixed-sign")
    # non-injectivity on the positive e-orthant, exact
    cs = [sp.Integer(k+2) for k in range(n-2)]
    vals = []
    for b in (sp.Integer(1), sp.Integer(2), sp.Rational(1, 3)):
        ms = [sp.I*b, -sp.I*b] + cs
        ev = elem(ms)
        check(all(x.is_real and x > 0 for x in ev), f"n={n}: e(b) not positive")
        sub = dict(zip(e, ev))
        vals.append((tuple(ev), tuple(sp.simplify(c.subs(sub)) for c in Phi)))
    check(len({v[0] for v in vals}) == 3 and len({v[1] for v in vals}) == 1,
          f"n={n}: e-orthant non-injectivity witness failed")
    # (jac) fails at kappa = 1: J(e(b)) * de/db = 0
    bb = sp.symbols('b', positive=True)
    ecurve = elem([sp.I*bb, -sp.I*bb] + cs)
    J = sp.Matrix([[sp.diff(c, x) for x in e] for c in Phi])
    tangent = sp.Matrix([sp.diff(x, bb) for x in ecurve]).subs(bb, 1)
    Jb = J.subs(dict(zip(e, [x.subs(bb, 1) for x in ecurve])))
    check(all(sp.simplify(x) == 0 for x in Jb*tangent) and any(x != 0 for x in tangent),
          f"n={n}: Jacobian kernel witness failed")
    print(f"  n={n}: r={len(mons)} monomials, A mixed-sign; Phi(e(1))=Phi(e(2))=Phi(e(1/3)) with "
          f"e(1)={vals[0][0]}, e(2)={vals[1][0]}; (jac) fails at kappa=1")

# ---------------------------------------------------------------- 3. restricted injectivity
print("== 3. S cannot encode 'modulo permutation'")
def is_perm(x, y): return sorted(x) == sorted(y)
for n in range(2, 7):
    for _ in range(300):
        d = [Fraction(random.randint(-5, 5), random.randint(1, 4)) for _ in range(n)]
        if all(t == 0 for t in d): continue
        T = 1 + sum(abs(t) for t in d)          # spread x so that x - d is never a permutation
        x = [T * 10**k for k in range(n)]
        x = [Fraction(v) * 3 for v in x]
        y = [xi - di for xi, di in zip(x, d)]
        check(all(v > 0 for v in y) and not is_perm(x, y), f"n={n}: construction failed for d={d}")
print("  every sampled nonzero difference d is realised by a non-permutation pair: S must be R^n")

# ---------------------------------------------------------------- 4. Steinig/Laurens route
print("== 4. Steinig/Laurens route for exponents -1,1,3,...,2n-3")
for n in range(2, 7):
    a = [-1] + list(range(1, 2*n-2, 2))
    for msize in range(1, n+1):
        for K in itertools.combinations(range(n), msize):
            sgn = None
            for _ in range(40):
                s = sorted({Fraction(random.randint(1, 400), random.randint(1, 60)) for _ in range(msize)})
                if len(s) < msize: continue
                M = sp.Matrix([[sp.Rational(a[k]) * sp.Rational(si.numerator, si.denominator)**(a[k]-1)
                                for k in K] for si in s])
                dv = M.det()
                check(dv != 0, f"n={n}, K={K}: vanishing minor at {s}")
                sg = sp.sign(dv)
                check(sgn is None or sg == sgn, f"n={n}, K={K}: minor sign changes")
                sgn = sg
    print(f"  n={n}: all square minors of the kernel a_k s^(a_k-1) nonzero, constant sign (sampled)")

def runs(mult_x, mult_y):
    """number of maximal intervals of constant nonzero sign of the step function phi"""
    pts = sorted(set(mult_x) | set(mult_y), reverse=True)
    alpha, prev, count = 0, 0, 0
    for p in pts:
        alpha += mult_x.count(p) - mult_y.count(p)
        sg = (alpha > 0) - (alpha < 0)
        if sg != 0 and sg != prev: count += 1
        prev = sg
    assert alpha == 0
    return count
for n in range(1, 6):
    pool = range(1, 7)
    ms = list(itertools.combinations_with_replacement(pool, n))
    mx = 0
    for X in ms:
        for Y in ms:
            mx = max(mx, runs(list(X), list(Y)))
    check(mx <= n, f"run-count lemma fails for n={n}: {mx}")
    print(f"  n={n}: max sign runs over all pairs of {n}-multisets from 1..6 = {mx} <= n")

# ---------------------------------------------------------------- 5. integer consistency
print("== 5. exhaustive injectivity on small integer multisets")
def inv(ms):
    n = len(ms)
    return (sum(Fraction(1, m) for m in ms),) + tuple(sum(m**k for m in ms) for k in range(1, 2*n-2, 2))
for n, top in ((3, 40), (4, 22)):
    seen = {}
    cnt = 0
    for ms in itertools.combinations_with_replacement(range(1, top+1), n):
        key = inv(ms); cnt += 1
        check(key not in seen, f"collision {ms} vs {seen.get(key)}")
        seen[key] = ms
    print(f"  n={n}, entries 1..{top}: {cnt} multisets, I_n injective")

if FAIL:
    print("FAILURES:", FAIL); sys.exit(1)
print("ALL CHECKS PASSED")
