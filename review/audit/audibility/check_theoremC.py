"""Theorem C: (1) pair criterion, (2) real curves, (3) integer sharpness via scaling.

Exact arithmetic (Fractions / sympy). Real-root certification uses sympy's exact real-root
isolation (Sturm/Descartes based count_roots on rational polynomials). One mpmath block at the end is
a labelled non-proof sanity check.
"""
import random
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
from sympy import symbols, Poly, expand, Rational, oo, I as iu, sqrt, nsimplify, Matrix, prod

random.seed(11)
z = symbols("z")
out = []


def log(s):
    out.append(s)
    print(s, flush=True)


def Inv(ms, n):
    """I_n(m) = (R, P_1, ..., P_{2n-3})."""
    return (sum(F(1, 1) / x for x in ms),) + tuple(sum(F(x) ** k for x in ms) for k in range(1, 2 * n - 2, 2))


def Qodd(m, mp):
    """Odd part Q(z) - Q(-z) of Q(z) = prod(z - m_i) prod(z + m'_j), as {degree: coeff}."""
    from sympy import sympify
    Q = expand(prod([z - sympify(x) for x in m]) * prod([z + sympify(x) for x in mp]))
    D = Poly(expand(Q - Q.subs(z, -z)), z)
    return {mon[0]: c for mon, c in zip(D.monoms(), D.coeffs()) if c != 0}


def to_q(x):
    return Rational(x.numerator, x.denominator) if isinstance(x, F) else x


# ---------- (1) pair criterion ----------
# (a) collisions of I_{n-1} found by exhaustive search must have Q(z)-Q(-z) = 2 kappa z^3, kappa != 0
for n, N in ((2, 30), (3, 40), (4, 30)):
    g = defaultdict(list)
    for ms in combinations_with_replacement(range(1, N + 1), n):
        g[Inv(ms, n - 1)].append(ms)
    pairs = 0
    for cls in g.values():
        for a, b in combinations(cls, 2):
            D = Qodd([Rational(x) for x in a], [Rational(x) for x in b])
            assert set(D) == {3} and D[3] != 0, (a, b, D)
            pairs += 1
    assert pairs > 0
    log(f"(1) n={n}, orders 1..{N}: {pairs} pairs sharing I_{n-1}; each has Q(z)-Q(-z)=2kappa z^3, kappa!=0")
# (b) converse direction on random pairs: if Q(z)-Q(-z) is a multiple of z^3 then I_{n-1} agree
tested = 0
for n in range(1, 7):
    for _ in range(300):
        a = [random.randint(-6, 6) or 1 for _ in range(n)]
        b = [random.randint(-6, 6) or 1 for _ in range(n)]
        D = Qodd([Rational(x) for x in a], [Rational(x) for x in b])
        is_z3 = set(D) <= {3}
        same = Inv(a, n - 1) == Inv(b, n - 1)  # for n=1 this is (R) alone
        assert is_z3 == same, (a, b, D)
        tested += 1
log(f"(1) {tested} random signed-integer pairs, n=1..6: [Q(z)-Q(-z) in C z^3] <=> [I_(n-1) agree]")
# (c) kappa = 0 iff m' = m under the hypothesis; failure without it
a, b = [1, -1, 5], [2, -2, 5]
D = Qodd([Rational(x) for x in a], [Rational(x) for x in b])
assert D == {} and sorted(a) != sorted(b)
log("(1) without the hypothesis: m={1,-1,5}, m'={2,-2,5}: Q(z)=Q(-z) (kappa=0) but m != m'")
for n in range(1, 6):
    for _ in range(200):
        a = [random.randint(1, 9) for _ in range(n)]
        b = [random.randint(1, 9) for _ in range(n)]
        D = Qodd([Rational(x) for x in a], [Rational(x) for x in b])
        assert (D == {}) == (sorted(a) == sorted(b))
log("(1) kappa=0 <=> m'=m on 1000 random positive pairs, n=1..5")
# complex pair sharing I_2 (n=3) built exactly: m = {1, w, wbar} type check via symbolic family
# n=2: I_1 = R only; m={1+i, 1-i}, m' with same R: 1/m1+1/m2 = 1  -> m'={2,2}
D = Qodd([1 + iu, 1 - iu], [2, 2])
assert set(D) <= {3} and D.get(3, 0) != 0
log("(1) complex n=2 example {1+i,1-i} vs {2,2}: same R=1, Q(z)-Q(-z) = 2kappa z^3 with kappa != 0")


# ---------- (2) real curves: fibre of I_{n-1} is an affine line in e-space ----------
def fibre_line(ms, n):
    """Solve the n-1 equations (odd rows j=0..n-3 from P_1..P_{2n-5}, and e_{n-1}=R e_n) for
    e_1..e_{n-1} in terms of t = e_n. Returns functions of t (exact)."""
    N = 2 * n - 3
    g = [F(0)] * N
    for k in range(1, N, 2):
        g[k] = sum(F(x) ** k for x in ms) / k
    ex = [F(0)] * N
    ex[0] = F(1)
    for m_ in range(1, N):
        ex[m_] = sum(k * 2 * g[k] * ex[m_ - k] for k in range(1, m_ + 1)) / m_
    num = [F(0)] + ex[1:]
    den = [F(2)] + ex[1:]
    dinv = [F(0)] * N
    dinv[0] = F(1, 2)
    for m_ in range(1, N):
        dinv[m_] = -sum(den[i] * dinv[m_ - i] for i in range(1, m_ + 1)) * dinv[0]
    T = [sum(num[i] * dinv[m_ - i] for i in range(m_ + 1)) for m_ in range(N)] + [F(0)] * 3
    R = sum(F(1) / x for x in ms)
    rows, rhs = [], []
    for j in range(n - 2):
        row = [F(0)] * (n + 1)  # columns e_1..e_n, and constant
        if 2 * j + 1 <= n:
            row[2 * j] += 1
        for i in range(j + 1):
            idx = 2 * j - 2 * i
            if idx == 0:
                row[n] -= T[2 * i + 1]
            elif idx <= n:
                row[idx - 1] -= T[2 * i + 1]
        rows.append(row)
    row = [F(0)] * (n + 1)
    row[n - 2] += 1
    row[n - 1] -= R
    rows.append(row)
    # unknowns e_1..e_{n-1}; t = e_n moves right: A x = -(c_n t + const)
    A = Matrix([[Rational(r[c].numerator, r[c].denominator) for c in range(n - 1)] for r in rows])
    t = symbols("t")
    bvec = Matrix([-(Rational(r[n - 1].numerator, r[n - 1].denominator) * t +
                     Rational(r[n].numerator, r[n].denominator)) for r in rows])
    assert A.det() != 0
    x = A.LUsolve(bvec)
    return [expand(xx) for xx in x] + [t], t


def positive_roots(e_t, t, tt, n):
    coeffs = [ee.subs(t, tt) for ee in e_t]
    q = Poly(expand((-1) ** n * Poly([1] + coeffs, z).as_expr().subs(z, -z)), z)
    sqf = q.gcd(q.diff(z)).degree() == 0
    return coeffs, sqf, q.count_roots(0, oo)


for n in range(2, 7):
    used = []
    for trial in range(3):
        ms = sorted(random.sample(range(2, 40), n))
        e_t, t = fibre_line(ms, n)
        t0 = prod(ms)
        # at t0 we must recover ms
        pz = Poly([1] + [ee.subs(t, t0) for ee in e_t], z)
        assert pz == Poly(prod([z + x for x in ms]), z)
        # the derivative of the fibre at t0 is nonzero, so the multiset moves; find a rational step
        # (both signs) at which the fibre polynomial still has n distinct positive real roots
        for kexp in range(3, 13):
            ok = True
            for sgn in (1, -1):
                tt = t0 * (1 + sgn * Rational(1, 10 ** kexp))
                coeffs, sqf, npos = positive_roots(e_t, t, tt, n)
                ok = ok and sqf and npos == n
            if ok:
                break
        assert ok, ms
        used.append((ms, kexp))
        for sgn in (1, -1):
            tt = t0 * (1 + sgn * Rational(1, 10 ** kexp))
            coeffs, sqf, npos = positive_roots(e_t, t, tt, n)
            assert sqf and npos == n
            e = [Rational(1)] + coeffs
            P = [None] * (2 * n)
            for k in range(1, 2 * n):
                s_ = (-1) ** (k - 1) * k * (e[k] if k <= n else 0)
                for i in range(1, k):
                    s_ += (-1) ** (i - 1) * (e[i] if i <= n else 0) * P[k - i]
                P[k] = expand(s_)
            for k in range(1, 2 * n - 4, 2):
                assert P[k] == sum(Rational(x) ** k for x in ms)
            assert e[n - 1] / e[n] == sum(Rational(1, x) for x in ms)
            assert P[2 * n - 3] != sum(Rational(x) ** (2 * n - 3) for x in ms)
    log(f"(2) n={n}: multisets and certified steps 10^-k: {used}; at e_n = t0(1 +- 10^-k) the fibre polynomial "
        f"has n distinct positive real roots (exact count), shares I_(n-1), differs in P_(2n-3)")

# repeated-value points (outside C(2)'s hypothesis): informational
for ms in ([3, 3, 3], [2, 5, 5], [4, 4, 4, 4]):
    n = len(ms)
    e_t, t = fibre_line(ms, n)
    t0 = prod(ms)
    res = []
    for delta in (Rational(1, 1000), Rational(-1, 1000)):
        coeffs = [ee.subs(t, t0 * (1 + delta)) for ee in e_t]
        q = Poly(expand((-1) ** n * Poly([1] + coeffs, z).as_expr().subs(z, -z)), z)
        res.append(q.count_roots(0, oo))
    log(f"(2) informational, repeated values {ms}: positive real roots at t0(1+1/1000), t0(1-1/1000): {res}")

# ---------- (3) integer sharpness by scaling ----------
from math import lcm
for a, b in (([F(1), F(4), F(4)], [F(3, 2), F(3, 2), F(6)]),):
    assert Inv(a, 2) == Inv(b, 2) and sorted(a) != sorted(b)
    L = lcm(*[x.denominator for x in a + b])
    for s in (L, 2 * L, 3 * L):
        A = [x * s for x in a]
        B = [x * s for x in b]
        assert Inv(A, 2) == Inv(B, 2)
    log(f"(3) rational pair {[str(x) for x in a]} / {[str(x) for x in b]} scales by {L} to "
        f"{[int(x*L) for x in a]} / {[int(x*L) for x in b]} sharing I_2")
# smallest n=4 integer witnesses (orders >= 2, hyperbolic) with all orders <= 40
g = defaultdict(list)
for ms in combinations_with_replacement(range(2, 41), 4):
    if sum(F(1, x) for x in ms) < 2:
        g[Inv(ms, 3)].append(ms)
w4 = [cls for cls in g.values() if len(cls) > 1]
assert ((3, 10, 15, 30), (4, 5, 21, 28)) in [tuple(sorted(c)) for c in w4] or \
    any(set(c) >= {(3, 10, 15, 30), (4, 5, 21, 28)} for c in w4)
log(f"(3) n=4 hyperbolic witnesses with orders <= 40: {len(w4)} classes, e.g. {w4[:4]}")

# ---------- non-proof sanity check (mpmath): follow the n=4 curve through (2,3,5,7) ----------
import mpmath as mp
mp.mp.dps = 40
ms = [2, 3, 5, 7]
e_t, t = fibre_line(ms, 4)
for tt in (200, 210, 230, 260):
    coeffs = [mp.mpf(str(ee.subs(t, tt))) for ee in e_t]
    rts = mp.polyroots([1] + coeffs, maxsteps=200, extraprec=200)
    log(f"(sanity, mpmath, not a proof) e_4={tt}: m = {[mp.nstr(-r, 10) for r in rts]}")
print("ALL CHECKS PASSED")
