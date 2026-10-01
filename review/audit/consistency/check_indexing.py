"""P8 part 2: coefficient indexing across groups, and every cross-group number recomputed
exactly from the coefficients derived in heat.py (Ucar 4.25/4.33/4.35).
Run from repo root:  python3 review/audit/consistency/check_indexing.py   (exit != 0 on failure)"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import sympy as sp
import heat
from heat import alpha, beta, b, p_sym

out = []
def log(s=""):
    print(s); out.append(s)
def R_(ms): return sum((Fr(1, m) for m in ms), Fr(0))
def P_(ms, k): return sum((Fr(m) ** k for m in ms), Fr(0))

# =========================================================== A. index dictionary
log("== A. Index dictionary (power of t  ->  name in each group) ==")
table = [
    ("t^-1", "c_1", "H_{-1}", "a_0^{sm}/(4pi) [PC.3, Ucar a_0]", "-", "-", "1st"),
    ("t^0",  "c_2", "H_0",    "a_0 [PC.2, DV], a_1^{sm}/(4pi)+sum b_0", "C_0 (+alpha_0 Area)", "a_0 (DV)", "2nd"),
    ("t^1",  "c_3", "H_1",    "'third coefficient' [PC.7-8]", "C_1 (+alpha_1 Area)", "a_1 (DV)", "3rd"),
    ("t^l",  "c_{l+2}", "H_l", "a_l (PC eq:a0conv style)", "C_l", "a_l", "(l+2)-th"),
]
for row in table:
    log(" | ".join(row))
# executable form of the dictionary
for ms in ([2, 8, 8], [3, 3, 12], [2, 3, 7], [3, 10, 15, 30]):
    n = len(ms)
    hc = heat.heat_coeffs(0, ms, -1, 6)
    for j in range(1, 7):
        assert heat.c(j, 0, ms) == hc[j - 2]           # c_j <-> H_{j-2} <-> t^{j-2}
    # c_1 = H_{-1} = Area/4pi = -chi/2 = (n-2-R)/2 ; for pillows (1-R)/2
    assert hc[-1] == (n - 2 - R_(ms)) / 2 == -(2 - n + R_(ms)) / 2
    # c_2 = H_0 = a_0 = (P_1 + R - 2n + 4)/12 ; n=3: (S_1+R-2)/12 (paper eq:s1inv, stability H_0)
    assert hc[0] == (P_(ms, 1) + R_(ms) - 2 * n + 4) / 12
    if n == 3:
        assert hc[0] == (P_(ms, 1) + R_(ms) - 2) / 12
        # c_3 = t^1: smooth (1-R)/2 * alpha_2 + eq:a2red
        assert hc[1] == (1 - R_(ms)) / 2 * Fr(1, 15) - P_(ms, 3) / 360 - P_(ms, 1) / 36 + Fr(11, 360) * R_(ms)
log("c_j = H_{j-2} = coefficient of t^{j-2}; c_1=(n-2-R)/2; c_2=a_0=H_0=(P_1+R-2n+4)/12 [(S_1+R-2)/12 at n=3]; c_3 = (1-R)/30 + eq:a2red: OK")

# =========================================================== B. quoted numbers
log("\n== B. Quoted numbers recomputed ==")
h288 = heat.heat_coeffs(0, [2, 8, 8], -1, 3)
h3312 = heat.heat_coeffs(0, [3, 3, 12], -1, 3)
assert h288[0] == Fr(67, 48) and h3312[0] == Fr(67, 48)
assert h288[1] == Fr(-1601, 480) and h3312[1] == Fr(-867, 160)
assert h288[-1] == h3312[-1] == Fr(1, 8)
log(f"(2,8,8): c1={h288[-1]}, a_0={h288[0]}, a_1={h288[1]};  (3,3,12): c1={h3312[-1]}, a_0={h3312[0]}, a_1={h3312[1]}  [DV quotes -1601/480, -867/160, 67/48: OK]")
# P_3 weight -1/360 (paper eq:a2red) == stability L_{22} == -(lead coeff of p_1)
assert Fr(-1) * Fr(p_sym(1).LC().p, p_sym(1).LC().q) == Fr(-1, 360)
for m in range(2, 31):
    assert b(1, m, -1) == -Fr(m) ** 3 / 360 - Fr(m) / 36 + Fr(11, 360) / m
log("eq:a2red sum b_1 = -P_3/360 - S_1/36 + 11R/360 (K=-1): OK")
# reference (2,3,5), rem:bugfix
h235 = heat.heat_coeffs(0, [2, 3, 5], 1, 2)
R235 = R_([2, 3, 5])
assert h235[0] == Fr(271, 360) and 12 * h235[0] + 2 - R235 == 10 and 12 * (h235[0] - 2) + R235 < 0
log("PC.2 (2,3,5) a_0 = 271/360 (spherical, K=+1); S_1 = 12a_0+2-R = 10; rem:bugfix wrong formula negative: OK")
# PC.16: a_0(3,3,4)=107/144, minimal over all pillows (S_1>=10; a_0 >= (S+9/S-2)/12 increasing)
assert heat.c(2, 0, [3, 3, 4]) == Fr(107, 144)
best = min(((P_([p, q, r], 1) + R_([p, q, r]) - 2) / 12, (p, q, r))
           for S in range(10, 40) for p in range(2, S) for q in range(p, S) for r in [S - p - q]
           if r >= q and R_([p, q, r]) < 1)
assert best == (Fr(107, 144), (3, 3, 4))
log("PC.16 min a_0 over pillows = 107/144 at (3,3,4): OK")

# =========================================================== C. stability front end
log("\n== C. Stability front end L, L^{-1} (from derived coefficients) ==")
NMAX = 8
def pi_coef(nu, k):
    c = p_sym(nu).as_dict().get((2 * k,), 0)
    return Fr(sp.Rational(c).p, sp.Rational(c).q)
L = [[Fr(0)] * NMAX for _ in range(NMAX)]
L[0][0] = Fr(-1, 2)
for nu in range(NMAX - 1):
    L[nu + 1][0] = -alpha(nu + 1, -1) / 2 + Fr(-1) ** nu * pi_coef(nu, 0)
    for k in range(1, nu + 2):
        L[nu + 1][k] = Fr(-1) ** nu * pi_coef(nu, k)
# L.I + h0 reproduces the heat coefficients
for ms in ([2, 8, 8], [3, 10, 15, 30], [2, 2, 2, 2, 3], [4, 5, 21, 28], [2, 3, 7, 7, 9, 11, 13]):
    n = len(ms)
    I = [R_(ms)] + [P_(ms, 2 * k - 1) for k in range(1, n)]
    h0 = [Fr(n - 2, 2) * alpha(j, -1) for j in range(n)]
    hc = heat.heat_coeffs(0, ms, -1, n)
    for r in range(n):
        assert sum((L[r][k] * I[k] for k in range(n)), Fr(0)) + h0[r] == hc[r - 1]
M_L = sp.Matrix(NMAX, NMAX, lambda i, j: sp.Rational(L[i][j].numerator, L[i][j].denominator))
Linv = M_L.inv()
claimed_rows = [[-2], [2, 12], [-18, -120, -360], [30, 252, 1260, 2520], [sp.Rational(-70, 3), -240, -1680, -6720, -10080]]
for r, row in enumerate(claimed_rows):
    assert [Linv[r, c] for c in range(r + 1)] == [sp.Rational(x) for x in row], (r, [Linv[r, c] for c in range(r + 1)])
diag_claim = [2, 12, 360, 2520, 10080, 28512, sp.Rational(43243200, 691), 112320]
rows_claim = [2, 14, 498, 4062, sp.Rational(56230, 3), sp.Rational(303654, 5), sp.Rational(104899830, 691), sp.Rational(10805786, 35)]
for r in range(NMAX):
    assert abs(1 / M_L[r, r]) == diag_claim[r] == abs(Linv[r, r])
    assert sum(abs(Linv[r, c]) for c in range(NMAX)) == rows_claim[r], (r, sum(abs(Linv[r, c]) for c in range(NMAX)))
    assert Fr(abs(M_L[r, r]).p, abs(M_L[r, r]).q) == (heat.lead_claimed(r - 1) if r >= 1 else Fr(1, 2))
log("L^{-1} rows (R..P_7), diagonal 2,12,360,2520,10080,28512,43243200/691,112320 and row sums 2,14,498,4062,56230/3,303654/5,104899830/691,10805786/35: OK")
assert [round(float(rows_claim[i] / diag_claim[i]), 2) for i in (1, 2, 3)] == [1.17, 1.38, 1.61]
# kappa_r for (2,8,8)
H = [h288[-1], h288[0], h288[1]]
I288 = [R_([2, 8, 8]), P_([2, 8, 8], 1), P_([2, 8, 8], 3)]
kap = [sum(abs(Fr(sp.Rational(Linv[r, c]).p, sp.Rational(Linv[r, c]).q)) * abs(H[c]) for c in range(r + 1)) / abs(I288[r]) for r in range(3)]
assert [round(float(x), 2) for x in kap] == [0.33, 0.94, 1.33]
log("ST.2 kappa_r(2,8,8) = 0.33, 0.94, 1.33 and amplification ratios 1.17,1.38,1.61: OK")

# ST.14 relative precisions delta_cert/|H_nu| against derived H
st14 = {
    (2, 8, 8): (2.341e-3, [1.8e-2, 1.6e-3, 7.0e-4]),
    (3, 3, 12): (4.040e-3, [3.2e-2, 2.8e-3, 7.4e-4]),
    (3, 10, 15, 30): (3.660e-3, [4.9e-3, 8.0e-4, 4.1e-5, 3.6e-7]),
    (4, 5, 21, 28): (1.461e-3, [1.9e-3, 3.2e-4, 1.6e-5, 1.7e-7]),
    (2, 3, 7): (3.658e-3, [3.0e-1, 4.0e-3, 2.7e-3]),
    (4, 4, 4): (4.539e-4, [3.6e-3, 5.0e-4, 5.4e-4]),
    (7, 7, 7): (8.068e-5, [2.8e-4, 4.9e-5, 2.3e-5]),
    (3, 3, 4, 4): (9.597e-5, [2.3e-4, 1.0e-4, 1.1e-4, 7.2e-5]),
    (5, 5, 5, 5): (3.617e-5, [6.0e-5, 2.5e-5, 1.9e-5, 6.2e-6]),
    (2, 2, 2, 3): (1.858e-4, [2.2e-3, 3.2e-4, 5.6e-4, 7.7e-4]),
    (2, 2, 2, 2, 3): (7.908e-6, [2.3e-5, 1.2e-5, 2.1e-5, 2.9e-5, 1.9e-5]),
}
def two_sf(x, mode):
    e = math.floor(math.log10(x)) - 1
    v = x / 10 ** e
    v = math.floor(v + 1e-9) if mode == "down" else round(v)
    return v * 10 ** e
st14_note = []
for ms, (dc, rel) in st14.items():
    hc = heat.heat_coeffs(0, list(ms), -1, len(ms))
    got = [dc / abs(float(hc[nu])) for nu in range(-1, len(ms) - 1)]
    for g, r in zip(got, rel):
        ok = any(math.isclose(two_sf(g, md), r, rel_tol=1e-6) for md in ("down", "near"))
        assert ok, (ms, got, rel)
        if not math.isclose(two_sf(g, "down"), r, rel_tol=1e-6):
            st14_note.append((ms, g, r))
log(f"ST.14 relative-precision columns reproduced from derived H_nu (2 s.f.) for all 11 rows: OK"
    + (f"; entries rounded to nearest rather than down: {[(m, round(g, 6), r) for m, g, r in st14_note]}" if st14_note else ""))

# =========================================================== D. Theorem B c_n vs Lemma S2.1; Jacobians
log("\n== D. Theorem B determinant constant vs Lemma S2.1; S2.2; Jacobians ==")
def esym(ms):
    e = [Fr(1)]
    for m in ms:
        e = [(e[k] if k < len(e) else 0) + (m * e[k - 1] if k >= 1 else 0) for k in range(len(e) + 1)]
    return e
def thmB_matrix(ms):
    n = len(ms); e = esym(ms)
    E = [e[k] if k % 2 == 0 else Fr(0) for k in range(n + 1)]
    O = [e[k] if k % 2 == 1 else Fr(0) for k in range(n + 1)]
    NT = 2 * n + 2
    E += [Fr(0)] * (NT - len(E)); O += [Fr(0)] * (NT - len(O))
    T = [Fr(0)] * NT                                   # T = O/E as power series
    for k in range(NT):
        T[k] = O[k] - sum((T[i] * E[k - i] for i in range(k)), Fr(0))
    # check T = tanh(sum_{k odd} P_k z^k / k) -- i.e. built from heat invariants only
    z = sp.Symbol('z')
    ser = sp.series(sp.tanh(sum(sp.Rational(int(P_(ms, k)), k) * z ** k for k in range(1, NT, 2))), z, 0, NT).removeO()
    for k in range(NT):
        cf = sp.Rational(ser.coeff(z, k))
        assert Fr(cf.p, cf.q) == T[k]
    M = [[Fr(0)] * n for _ in range(n)]
    rhs = [Fr(0)] * n
    for j in range(n - 1):
        if 2 * j + 1 <= n:
            M[j][2 * j + 1 - 1] += 1
        for i in range(j + 1):
            idx = 2 * j - 2 * i
            if idx == 0:
                rhs[j] += T[2 * i + 1]
            elif idx <= n:
                M[j][idx - 1] -= T[2 * i + 1]
    M[n - 1][n - 2] += 1
    M[n - 1][n - 1] -= R_(ms)
    return M, rhs, e
def det(Mx):
    return sp.Matrix(len(Mx), len(Mx), lambda i, j: sp.Rational(Mx[i][j].numerator, Mx[i][j].denominator)).det()
random.seed(1)
cn_thmB = {3: 1, 4: 1, 5: -1, 6: -1, 7: 1, 8: 1}
for n in range(2, 9):
    for trial in range(3):
        ms = [random.randint(2, 40) for _ in range(n)]
        M, rhs, e = thmB_matrix(ms)
        # true e solves the system
        for row, bb in zip(M, rhs):
            assert sum((row[k] * e[k + 1] for k in range(n)), Fr(0)) == bb
        prod = 1
        for i in range(n):
            for j in range(i + 1, n):
                prod *= ms[i] + ms[j]
        cn = det(M) / (sp.Integer(prod) / sp.Integer(int(e[n])))
        assert cn == (-1) ** (n * (n + 1) // 2), (n, cn)
        if n in cn_thmB:
            assert cn == cn_thmB[n]
        # Lemma S2.2: B = S M, det B = (-1)^{n(n-1)/2} prod
        ee = lambda i: e[i] if 0 <= i <= n else Fr(0)
        Bm = [[Fr(-1) ** (j + 1) * ee(2 * k + 1 - j) for j in range(1, n + 1)] for k in range(n)]
        Sm = [[Fr(0)] * n for _ in range(n)]
        for k in range(n - 1):
            for i in range(k + 1):
                Sm[k][i] = ee(2 * (k - i))
        Sm[n - 1][n - 1] = Fr(-1) ** n * e[n]
        SM = [[sum((Sm[r][t] * M[t][c] for t in range(n)), Fr(0)) for c in range(n)] for r in range(n)]
        assert SM == Bm, n
        assert det(Bm) == (-1) ** (n * (n - 1) // 2) * prod
log("Theorem B system built from tanh(sum P_k z^k/k); true e solves it; det M = c_n prod(m_i+m_j)/e_n with c_n = (-1)^{n(n+1)/2} for n=2..8;"
    " equals Theorem B's list (+1,+1,-1,-1,+1,+1 for n=3..8) and Lemma S2.1; S2.2 B=SM and det B: OK")
# AU Remark 2 Jacobian, c_n = -prod_{r<n}(2r-1)   (a different 'c_n')
for n in range(2, 7):
    xs = sp.symbols(f'x1:{n + 1}')
    Ivec = [sum(1 / x for x in xs)] + [sum(x ** (2 * k - 1) for x in xs) for k in range(1, n)]
    J = sp.Matrix(n, n, lambda i, j: sp.diff(Ivec[i], xs[j]))
    for trial in range(3):
        vals = {x: sp.Integer(random.randint(2, 50)) for x in xs}
        V = sp.prod([vals[xs[j]] - vals[xs[i]] for i in range(n) for j in range(i + 1, n)])
        Pp = sp.prod([vals[xs[i]] + vals[xs[j]] for i in range(n) for j in range(i + 1, n)])
        D = J.subs(vals).det()
        cn = -sp.prod([2 * r - 1 for r in range(1, n)])
        assert D == cn * V * Pp / sp.prod([v ** 2 for v in vals.values()]), n
p_, q_, r_ = sp.symbols('p q r', positive=True)
F = sp.Matrix([p_ + q_ + r_, 1 / p_ + 1 / q_ + 1 / r_, p_ ** 3 + q_ ** 3 + r_ ** 3])
Jd = sp.simplify(F.jacobian([p_, q_, r_]).det())
assert sp.simplify(Jd - (-3 * (p_ - q_) * (p_ - r_) * (q_ - r_) * (p_ + q_) * (p_ + r_) * (q_ + r_) / (p_ ** 2 * q_ ** 2 * r_ ** 2))) == 0
log("AU Remark 2 Jacobian with c_n=-prod(2r-1) (n<=6) and PC.10 det DF = -3(p-q)(p-r)(q-r)(p+q)(p+r)(q+r)/(pqr)^2: OK (mutually consistent)")

# =========================================================== E. stability constants sigma, zeta ; ST.9/ST.10 identities
w, s_, a_, d_ = sp.symbols('w s a d')
def sigma(k, n):
    return sp.series(sp.atanh(w) * sp.sec((n + 1) * sp.atanh(w)) ** 2, w, 0, k + 1).removeO().coeff(w, k)
assert sigma(1, 3) == 1 and sigma(3, 3) == sp.Rational(49, 3)
assert [sigma(1, 4), sigma(3, 4), sigma(5, 4)] == [1, sp.Rational(76, 3), sp.Rational(6628, 15)]
def zeta(n):
    best = sp.Integer(1)
    for j in range(0, n - 1):
        sm = sum((sigma(2 * i + 1, n) for i in range(j) if 2 <= 2 * j - 2 * i <= n), sp.Integer(0))
        best = max(best, sm)
    return best
assert [zeta(3), zeta(4), zeta(5)] == [1, sp.Rational(79, 3), sp.Rational(14048, 15)]
dR = (sp.Rational(1, 2) + 1 / (8 + s_) + 1 / (8 - s_)) - sp.Rational(3, 4)
assert sp.simplify(dR - 2 * s_ ** 2 / (8 * (64 - s_ ** 2))) == 0
assert sp.expand((8 + s_) ** 3 + (8 - s_) ** 3 + 8 - 1032) == 48 * s_ ** 2
assert sp.expand(((a_ + d_) ** 3 - 3 * a_ ** 2 * (a_ + d_)) - (a_ ** 3 - 3 * a_ ** 3) - (3 * a_ * d_ ** 2 + d_ ** 3)) == 0
log("ST.5 sigma_k, zeta_n values; ST.9 Delta R, Delta P_3 for (2,8+s,8-s); ST.10 identity: OK")

# =========================================================== F. witnesses and examples across groups
log("\n== F. Cross-group witnesses ==")
A3, B3 = [2, 8, 8], [3, 3, 12]
A4, B4 = [3, 10, 15, 30], [4, 5, 21, 28]
for (U, V, n, last) in [(A3, B3, 3, (1032, 1782)), (A4, B4, 4, (25159618, 21298618))]:
    hu, hv = heat.heat_coeffs(0, U, -1, n + 1), heat.heat_coeffs(0, V, -1, n + 1)
    assert all(hu[p] == hv[p] for p in range(-1, n - 2))       # share first n-1 coefficients
    assert hu[n - 2] != hv[n - 2]                               # differ at the n-th
    assert (P_(U, 2 * n - 3), P_(V, 2 * n - 3)) == last
    assert sum((1 - Fr(1, m) for m in U), Fr(0)) > 2 and sum((1 - Fr(1, m) for m in V), Fr(0)) > 2
z = sp.Symbol('z')
for U, V, claim in [(A3, B3, 500 * z ** 3), (A4, B4, 1544400 * z ** 3)]:
    pz = sp.prod([z + m for m in U]); pp = sp.prod([z + m for m in V])
    Phi = sp.expand(pz * pp.subs(z, -z) - pp * pz.subs(z, -z))
    Q = sp.prod([z - m for m in U]) * sp.prod([z + m for m in V])
    n = len(U)
    assert Phi == claim and sp.expand(Phi - (-1) ** (n + 1) * (Q - Q.subs(z, -z))) == 0
assert R_(A4) == Fr(8, 15) and P_(A4, 1) == 58 and P_(A4, 3) == 31402 == P_(B4, 3)
log("n=3 pair shares c_1,c_2, differs at c_3; n=4 pair shares c_1..c_3, differs at c_4; P values, Phi=500z^3, 1544400z^3: OK")
# ex:siggenus with genus via derived coefficients
e1 = heat.heat_coeffs(1, [15], -1, 4), heat.heat_coeffs(0, [3, 3, 5, 5], -1, 4)
e2 = heat.heat_coeffs(1, [15, 15, 15], -1, 5), heat.heat_coeffs(0, [3, 3, 5, 7, 7, 21], -1, 5)
assert e1[0][-1] == e1[1][-1] and e1[0][0] == e1[1][0] and e1[0][1] != e1[1][1]
assert all(e2[0][p] == e2[1][p] for p in (-1, 0, 1)) and e2[0][2] != e2[1][2]
log("ex:siggenus: (1;15)~(0;3,3,5,5) share exactly 2; (1;15,15,15)~(0;3,3,5,7,7,21) share exactly 3: OK")
# SG Lemma 4 mirror identity for these
for (g, m), (g2, m2), L in [((1, [15]), (0, [3, 3, 5, 5]), 2), ((1, [15, 15, 15]), (0, [3, 3, 5, 7, 7, 21]), 3)]:
    Nn = max(len(m), len(m2)) + 2
    mN = m + [1] * (Nn - len(m)); m2N = m2 + [1] * (Nn - len(m2))
    X = mN + [-x for x in m2N]
    target = 2 * (g - g2)
    assert sum((Fr(1, x) for x in X), Fr(0)) == target
    for j in range(1, 2 * L - 2, 2):
        assert sum((Fr(x) ** j for x in X), Fr(0)) == target
log("SG Lemma 4 mirror identity s_{-1}(X)=s_j(X)=2(g-g') for the two examples: OK")

# DI.11 indexing: size-3 fibre shares (c_1,c_2) = (t^-1, t^0) but NOT the paper's/divergence's a_1 (t^1)
fib3 = [[15, 55, 66], [16, 40, 80], [17, 34, 85]]
hs = [heat.heat_coeffs(0, f, -1, 3) for f in fib3]
assert len({h[-1] for h in hs}) == 1 and len({h[0] for h in hs}) == 1
assert len({h[1] for h in hs}) == 3
log("DI.11 'sharing a_0 and a_1': the size-3 fibre shares t^-1 and t^0 only; its t^1 coefficients (paper/DV a_1) are distinct "
    f"{[str(h[1]) for h in hs]} -> DI uses Ucar's a_nu indexing (a_0 = area term), the paper/DV use a_l = t^l. INCONSISTENT LABEL.")

# DF.7(a)/AU.0: c_j carries P_{2j-3} with nonzero weight, and nothing higher
for j in range(2, 10):
    l = j - 2
    P = p_sym(l)
    assert P.degree() == 2 * j - 2 and P.LC() != 0     # b_l ~ m^{2l+1} = m^{2j-3}
log("c_j (j>=2) involves R, P_1, ..., P_{2j-3} with nonzero top weight (j<=9): OK")

# PC.15 / TH.0 numbers
tau = lambda p: Fr(p - 1, p * (p + 1))
phi = lambda p, S: Fr(4, S - p) - Fr(1, S - 2 * p - 2)
assert tau(2) == tau(3) == Fr(1, 6) and tau(4) == Fr(3, 20)
assert phi(2, 17) == Fr(29, 165) and phi(2, 18) == Fr(1, 6) and phi(3, 12) == Fr(7, 36) and phi(3, 17) == Fr(11, 63)
assert min(phi(4, S) for S in (15, 16, 17)) == phi(4, 15) == Fr(9, 55)
Rm = lambda S, p: Fr(1, p) + Fr(1, (S - p) // 2) + Fr(1, S - p - (S - p) // 2)
Rp = lambda S, p: Fr(2, p) + Fr(1, S - 2 * p)
assert (Rm(18, 3), Rp(18, 4), Rm(18, 4), Rp(18, 5), Rm(18, 5), Rp(18, 6)) == (Fr(101, 168), Fr(3, 5), Fr(15, 28), Fr(21, 40), Fr(107, 210), Fr(1, 2))
assert Rm(18, 2) == Rp(18, 3) == Fr(3, 4)
for p in range(2, 40):   # gap >= -tau + phi  identity behind TH.0
    for S in range(3 * p + 3, 3 * p + 60):
        assert Fr(1, p) + Fr(4, S - p) - Rp(S, p + 1) == phi(p, S) - tau(p)
log("PC.15 / TH.0 tau_p, phi_p, endpoint values at S=18: OK")

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_indexing.txt"), "w") as f:
    f.write("\n".join(out) + "\nALL INDEXING CHECKS PASSED\n")
print("ALL INDEXING CHECKS PASSED")
