"""Exact verification for theory/msep/proof.tex (bounded cone orders: M heat invariants suffice).

Statement checked (proof.tex, Theorem msep): for M >= 2, two closed orientable hyperbolic 2-orbifolds
whose cone orders are all at most M and which share c_1, ..., c_M have the same signature; and M is
optimal: an explicit pair with orders at most M and different signatures shares c_1, ..., c_{M-1}.

Checks, all in exact rational arithmetic (fractions.Fraction; sympy only for an independent rank):
  1. rank of A_L(M) = (psi_k(a))_{1<=k<=L-1, 2<=a<=M}, psi_k(x) = x^(2k-1) - 1/x, equals
     min(L-1, M-1) for 1 <= L <= M+1 and 2 <= M <= MMAX, by our own Fraction elimination and by sympy;
  2. the same for the padded system of the brief, B_L(M) = (x^j)_{j in {-1,1,3,..,2L-3}, 1<=x<=M},
     rank min(L, M), so both formulations give the threshold L = M;
  3. det of the (M-1)x(M-1) matrix (a^2k - 1)_{1<=k<=M-1, 2<=a<=M} equals the Vandermonde determinant
     of (1, 2^2, ..., M^2) (the identity used in the proof);
  4. the kernel vector w_a = 1/prod_{b != a, 1<=b<=M} (a^2 - b^2) (Lagrange weights) kills the rows
     k = 0..M-2 of the Vandermonde matrix, and nu(a) = a w_a kills A_{M-1}(M);
  5. for each M the explicit sharp pair of proof.tex (integer scaling C, genera g, g'): orders in
     [2, M], hyperbolic, different signatures, c_1..c_{M-1} equal and c_M different, recomputed from
     the cone coefficients b_l of Proposition 2.7 (theory/eigen/eigen_common.py), and the
     difference c_M - c_M' = (-1)^M C a_{M-2} with a_l the leading coefficient of p_l;
  6. independent brute force for M = 2, 3, 4: every signature with orders <= M and area at most a
     bound; no two distinct signatures share c_1..c_M, and the largest number of shared coefficients
     among distinct signatures is M - 1 once the bound reaches the sharp pair's area (and the minimal
     area of such a pair is reported).
Run: python3 verify.py [MMAX]   (default MMAX = 24; about a minute). Exit status 0 iff all checks pass.
"""
import itertools
import os
import sys
from fractions import Fraction as Fr
from math import gcd, prod

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "eigen"))
from eigen_common import alpha, b_cone, check, lead_coef  # noqa: E402

MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 24
check(MMAX >= 18, "the brief asks for M up to at least 18")


def rank_fraction(rows):
    """Rank over Q by Gaussian elimination on Fractions."""
    A = [list(map(Fr, r)) for r in rows]
    if not A:
        return 0
    n, m = len(A), len(A[0])
    r = 0
    for c in range(m):
        piv = next((i for i in range(r, n) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(n):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(m)]
        r += 1
        if r == n:
            break
    return r


def det_fraction(rows):
    A = [list(map(Fr, r)) for r in rows]
    n = len(A)
    d = Fr(1)
    for c in range(n):
        piv = next((i for i in range(c, n) if A[i][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            d = -d
        d *= A[c][c]
        for i in range(c + 1, n):
            f = A[i][c] / A[c][c]
            A[i] = [A[i][j] - f * A[c][j] for j in range(n)]
    return d


def psi(k, x):
    x = Fr(x)
    return x ** (2 * k - 1) - 1 / x


def A_mat(L, M):
    return [[psi(k, a) for a in range(2, M + 1)] for k in range(1, L)]


def B_mat(L, M):
    js = [-1] + list(range(1, 2 * L - 2, 2))
    return [[Fr(x) ** j for x in range(1, M + 1)] for j in js]


# ---------------------------------------------------------------- 1-3. ranks and the determinant
import sympy  # noqa: E402

n_rank = 0
for M in range(2, MMAX + 1):
    for L in range(1, M + 2):
        rA = rank_fraction(A_mat(L, M))
        check(rA == min(L - 1, M - 1), f"rank A_{L}({M}) = {rA}")
        rB = rank_fraction(B_mat(L, M))
        check(rB == min(L, M), f"rank B_{L}({M}) = {rB}")
        n_rank += 2
    # sympy, independently, at the two lengths that matter: L = M (full rank) and L = M - 1
    for L in (M - 1, M):
        if L >= 2:
            S = sympy.Matrix([[sympy.Rational(v.numerator, v.denominator) for v in row] for row in A_mat(L, M)])
            check(S.rank() == min(L - 1, M - 1), f"sympy rank A_{L}({M})")
    V = [[Fr(a * a) ** k - 1 for a in range(2, M + 1)] for k in range(1, M)]
    vdm = prod(Fr(y2 - y1) for y1, y2 in itertools.combinations([a * a for a in range(1, M + 1)], 2))
    check(det_fraction(V) == vdm, f"det identity at M = {M}")
print(f"1-3. ranks: {n_rank} exact ranks (A_L(M): min(L-1, M-1); B_L(M): min(L, M)) for 2 <= M <= {MMAX}, "
      f"1 <= L <= M+1; sympy agrees at L = M-1, M; det(a^2k - 1) = Vandermonde(1, 4, ..., M^2) for every M")


# ---------------------------------------------------------------- 4-5. kernel and the sharp pairs
def lagrange_w(M):
    return {a: Fr(1, prod(a * a - b * b for b in range(1, M + 1) if b != a)) for a in range(1, M + 1)}


def heat_mult(g, mult, L):
    """(c_1..c_L) for genus g and cone orders with multiplicities mult = {order: count}."""
    s = Fr(2 * g - 2) + sum(c * (1 - Fr(1, a)) for a, c in mult.items())
    c1 = s / 2
    out = [c1]
    for j in range(2, L + 1):
        out.append(alpha(j - 1) * c1 + sum(c * b_cone(j - 2, a) for a, c in mult.items()))
    return out, s


def sharp_pair(M):
    """proof.tex, part (ii): nu(a) = C a w_a with the least positive integer C making nu integral
    and s = sum nu(a)(1 - 1/a) an even integer; genera g = 2 + max(0, -s/2), g' = g + s/2."""
    w = lagrange_w(M)
    nu0 = {a: a * w[a] for a in range(2, M + 1)}
    den = 1
    for v in nu0.values():
        den = den * v.denominator // gcd(den, v.denominator)
    C = den
    nu = {a: int(C * v) for a, v in nu0.items()}
    s = sum(Fr(v) * (1 - Fr(1, a)) for a, v in nu.items())
    # least multiple k with s*k an even integer
    k = 1
    while not ((s * k).denominator == 1 and (s * k).numerator % 2 == 0):
        k += 1
    C *= k
    nu = {a: v * k for a, v in nu.items()}
    s = s * k
    m = {a: v for a, v in nu.items() if v > 0}
    mp_ = {a: -v for a, v in nu.items() if v < 0}
    # least genera with g' - g = s/2 for which the (common) area is positive
    g = max(0, -int(s) // 2)
    while Fr(2 * g - 2) + sum(c * (1 - Fr(1, a)) for a, c in m.items()) <= 0:
        g += 1
    gp = g + int(s) // 2
    return C, nu, int(s), (g, m), (gp, mp_)


rows = []
for M in range(2, MMAX + 1):
    w = lagrange_w(M)
    for kk in range(0, M - 1):
        check(sum(w[a] * Fr(a * a) ** kk for a in range(1, M + 1)) == 0, f"Lagrange weights, M={M}, k={kk}")
    check(all(w[a] != 0 for a in w), "weights nonzero")
    check(all((w[a] > 0) == ((M - a) % 2 == 0) for a in w), "sign of w_a is (-1)^(M-a)")
    nu0 = [a * w[a] for a in range(2, M + 1)]
    for row in A_mat(M - 1, M):
        check(sum(r * v for r, v in zip(row, nu0)) == 0, f"kernel of A_(M-1)({M})")
    C, nu, s, (g, m), (gp, mp_) = sharp_pair(M)
    check(all(2 <= a <= M for a in list(m) + list(mp_)), "orders in [2, M]")
    check(m != mp_ or g != gp, "different signatures")
    H1, s1 = heat_mult(g, m, M)
    H2, s2 = heat_mult(gp, mp_, M)
    check(s1 == s2 and s1 > 0, f"equal positive area at M = {M}: both hyperbolic")
    check(H1[:M - 1] == H2[:M - 1], f"c_1..c_(M-1) agree at M = {M}")
    check(H1[M - 1] != H2[M - 1], f"c_M differs at M = {M}")
    check(H1[M - 1] - H2[M - 1] == (-1) ** M * C * lead_coef(M - 2), f"Delta c_M = (-1)^M C a_(M-2) at M = {M}")
    rows.append((M, C, s, g, gp, sum(m.values()), sum(mp_.values()), s1))
print("4-5. Lagrange kernel and sharp pairs (orders <= M, different signatures, equal c_1..c_(M-1), c_M differs):")
print("   M  genera  cone points    Area/2pi        nu on {2..M}")
for (M, C, s, g, gp, n1, n2, s1) in rows[:6]:
    _, nu, _, _, _ = sharp_pair(M)
    print(f"  {M:2d}  ({g},{gp})   {n1:>6} vs {n2:<6} {float(s1):12.6g}   {[nu[a] for a in range(2, M + 1)]}")
for (M, C, s, g, gp, n1, n2, s1) in rows[6:]:
    print(f"  {M:2d}  ({g},{gp})   {n1:.3g} vs {n2:.3g} cone points, Area/2pi = {float(s1):.4g}")


# ---------------------------------------------------------------- 6. brute force, small M
def all_sigs(M, smax):
    """Every hyperbolic signature (g; multiset in [2, M]) with Area/2pi = s <= smax (Fractions)."""
    out = []
    g = 0
    while 2 * g - 2 <= smax:
        nmax = int((smax - (2 * g - 2)) * 2)
        for n in range(0, max(nmax, 0) + 1):
            for orders in itertools.combinations_with_replacement(range(2, M + 1), n):
                s = Fr(2 * g - 2) + sum(1 - Fr(1, a) for a in orders)
                if 0 < s <= smax:
                    out.append((g, orders, s))
        g += 1
    return out


def heat_key(g, orders, L):
    mult = {}
    for a in orders:
        mult[a] = mult.get(a, 0) + 1
    return tuple(heat_mult(g, mult, L)[0])


print("6. brute force (all signatures with orders <= M and Area/2pi <= bound):")
SHARP_AREA = {M: s1 for (M, C, s, g, gp, n1, n2, s1) in rows}
for M, smax in ((2, Fr(6)), (3, Fr(9)), (4, SHARP_AREA[4])):
    sigs = all_sigs(M, smax)
    keyM = {}
    for g, o, s in sigs:
        keyM.setdefault(heat_key(g, o, M), []).append((g, o))
    check(all(len(v) == 1 for v in keyM.values()), f"c_1..c_M separate all signatures, M = {M}")
    keyM1 = {}
    for g, o, s in sigs:
        keyM1.setdefault(heat_key(g, o, M - 1), []).append((g, o, s))
    clash = [v for v in keyM1.values() if len(v) > 1]
    smin = min((min(x[2] for x in v) for v in clash), default=None)
    print(f"   M = {M}: {len(sigs)} signatures with Area/2pi <= {smax}; c_1..c_{M} injective; "
          + (f"pairs sharing c_1..c_{M - 1}: {len(clash)} classes, least Area/2pi = {smin}" if clash else
             f"no pair shares c_1..c_{M - 1} below this bound"))
    if M == 2:
        check(smin == Fr(1, 2), "M = 2: (1;2) and (0;2,2,2,2,2) share c_1")
    if M == 3:
        check(clash and smin == 6, "M = 3: least area of a pair sharing c_1, c_2 is 12 pi, (1;3^9)/(0;2^16)")
        ex = [v for v in clash if any(x[0] == 1 and x[1] == (3,) * 9 for x in v)]
        check(ex and any(x[0] == 0 and x[1] == (2,) * 16 for x in ex[0]), "M = 3 example")
    if M == 4:
        check(clash and smin <= SHARP_AREA[4], "M = 4: a pair sharing c_1..c_3 exists by the sharp pair's area")


# ---------------------------------------------------------------- 7. part (iii): arbitrary competitors
def multisets_with_sum(sigma, lo=2):
    """All sorted tuples m_1 <= ... <= m_n, m_i >= lo, with sum(1 - 1/m_i) = sigma (complete)."""
    out = []

    def rec(sig, r, lo, pre):
        if r == 1:
            rest = 1 - sig
            if rest > 0 and rest.numerator == 1 and rest.denominator >= lo:
                out.append(pre + (rest.denominator,))
            return
        if not (Fr(r, 2) <= sig < r):
            return
        a = lo
        while a <= Fr(r) / (r - sig):
            rec(sig - (1 - Fr(1, a)), r - 1, a, pre + (a,))
            a += 1
    if sigma == 0:
        return [()]
    for n in range(int(sigma) + 1, int(2 * sigma) + 1):
        rec(sigma, n, lo, ())
    return out


def area_class(s):
    """Every signature (g; m) with 2g - 2 + sum(1 - 1/m_i) = s, no bound on the orders."""
    cls, g = [], 0
    while 2 * g - 2 <= s:
        cls += [(g, m) for m in multisets_with_sum(s + 2 - 2 * g)]
        g += 1
    return cls


import math  # noqa: E402

KCAP = 9
svals = sorted({Fr(2 * g - 2) + sum(1 - Fr(1, a) for a in o)
                for g in range(0, 2) for n in range(0, 6) for o in itertools.combinations_with_replacement(range(2, 5), n)
                if 0 < Fr(2 * g - 2) + sum(1 - Fr(1, a) for a in o) <= 2})
n_or, worst, nsig = 0, {}, 0
for sv in svals:
    cls = area_class(sv)
    nsig += len(cls)
    keys = {sig: heat_key(sig[0], sig[1], KCAP) for sig in cls}
    A_over_pi = 2 * sv
    for sig in cls:
        M = max(sig[1], default=2)
        if M > 4:
            continue
        others = [o for o in cls if o != sig]
        K = next(k for k in range(1, KCAP + 1) if all(keys[o][:k] != keys[sig][:k] for o in others))
        bound = M + math.ceil(math.log(2 * math.floor(A_over_pi) + 8) / 2)
        check(K <= bound, f"(iii) at {sig}: K = {K} > {bound}")
        worst[M] = max(worst.get(M, 0), K)
        # the order bound: a competitor sharing c_1..c_L, L >= 2, has orders <= M (2 floor(A/pi) + 8)^(1/(2L-3))
        for o in others:
            L = next(k for k in range(1, KCAP + 1) if keys[o][:k] != keys[sig][:k]) - 1
            if L >= 2:
                check(max(o[1], default=1) <= M * (2 * math.floor(A_over_pi) + 8) ** (1 / (2 * L - 3)) + 1e-9,
                      f"order bound fails for {sig} against {o}")
                n_or += 1
print(f"7. part (iii): {len(svals)} complete area classes (Area/2pi <= 2, {nsig} signatures, no bound on the "
      f"orders); for every O with orders <= M (M = 2, 3, 4) the exact K_mult(O; Sig) is at most "
      f"M + ceil(log(2 floor(A/pi) + 8)/2); largest observed {worst}; order bound checked on {n_or} pairs "
      f"sharing at least two invariants")
# the arithmetic of part (iii): with k = ceil(lambda/2) and L = M + k, every order of a competitor sharing
# c_1..c_L is <= L, i.e. (L+1)^(2L-3) > N M^(2L-3) for N = 2 floor(A/pi) + 8, checked in integers
n_ar = 0
for N in list(range(8, 400, 2)) + [2 * q + 8 for q in (10 ** 3, 10 ** 6, 10 ** 12, 10 ** 30)]:
    k = math.ceil(math.log(N) / 2)
    for M in range(2, 200):
        L = M + k
        check((L + 1) ** (2 * L - 3) > N * M ** (2 * L - 3), f"(iii) arithmetic at N={N}, M={M}")
        n_ar += 1
print(f"8. part (iii) arithmetic: (L+1)^(2L-3) > N M^(2L-3) for L = M + ceil(log(N)/2) in {n_ar} cases")
print("all checks passed")
