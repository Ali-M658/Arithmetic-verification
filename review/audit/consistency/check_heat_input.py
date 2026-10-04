"""P8 part 1: every group's stated heat input is the same function as the one derived from
Ucar (4.25), (4.33), (4.35), Thm 4.20.  Exact arithmetic, l <= 8, m <= 30.
Run from repo root:  python3 review/audit/consistency/check_heat_input.py
Exits nonzero on any failure."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import sympy as sp
import mpmath as mp
import heat
from heat import B, Bhalf, cS, beta, b, alpha, alpha_unit, p_sym, lead_claimed, m_sym

LMAX, MMAX = 8, 30
out = []
def log(s=""):
    print(s); out.append(s)

def fact(n): return Fr(sp.factorial(n))
def binom(a, k): return Fr(sp.binomial(a, k))

# ---------------------------------------------------------------- derived table
log("== 1. Derived from Ucar ==")
log("smooth: a_nu/vol = kappa^nu * alpha_unit(nu),  alpha_unit = " +
    ", ".join(str(alpha_unit(n)) for n in range(9)))
for l in range(4):
    log(f"p_{l}(m) = m*beta_{l}(m) = {p_sym(l).as_expr()}")

# structural facts claimed by AU.0, SG.1, ST.0, DV.0/Thm 2
for l in range(LMAX + 1):
    P = p_sym(l)
    assert P.degree() == 2 * l + 2, l
    coeffs = P.all_coeffs()[::-1]
    assert all(coeffs[i] == 0 for i in range(1, len(coeffs), 2)), f"p_{l} not even"
    assert P.eval(1) == 0, f"p_{l}(1) != 0"
    lc = P.LC()
    assert Fr(lc.p, lc.q) == lead_claimed(l), (l, lc, lead_claimed(l))
    for m in range(2, MMAX + 1):
        assert Fr(P.eval(m).p, P.eval(m).q) == m * beta(l, m)
        assert beta(l, m) > 0  # DV Lemma 1(b), CU.1 'none vanishes'
log("p_l even, deg 2l+2, p_l(1)=0, leading |B_{2l+2}|/(2(l+1)!(2l+1)), beta_l(m)>0: OK for l<=8, m<=30")

# ---------------------------------------------------------------- group formulas
log("\n== 2. Group-by-group heat input ==")
ok_groups = []

# PC (paper): b_0 = (m^2-1)/(12m) via def:cone = (1/4m) sum csc^2 ; eq:b1 ; chi/6
def power_sums_u(m, kmax):
    """Exact power sums p_1..p_kmax of the roots u_j = 1/(1-zeta_j), zeta_j the nontrivial m-th
    roots of unity.  They are the roots of Q(u) = (u-1)^m - u^m (degree m-1)."""
    # coefficients of Q, highest degree first
    coeffs = [Fr(0)] * (m + 1)   # index = power
    for i in range(m + 1):
        coeffs[i] += binom(m, i) * Fr(-1) ** (m - i)
    coeffs[m] -= 1
    d = m - 1
    lead = coeffs[d]
    e = [Fr(1)] + [Fr((-1) ** k) * coeffs[d - k] / lead for k in range(1, d + 1)]  # elementary symm. fns
    p = [Fr(0)] * (kmax + 1)
    for k in range(1, kmax + 1):
        s = Fr((-1) ** (k - 1) * k) * (e[k] if k <= d else 0)
        for i in range(1, k):
            s += Fr((-1) ** (i - 1)) * (e[i] if i <= d else 0) * p[k - i]
        p[k] = s
    return p
# csc^2(j pi/m) = 4/|1-zeta|^2 = -4 zeta/(1-zeta)^2 = -4(u^2-u),  csc^4 = 16(u^2-u)^2
for m in range(2, MMAX + 1):
    pu = power_sums_u(m, 4)
    csc2 = -4 * (pu[2] - pu[1])
    csc4 = 16 * (pu[4] - 2 * pu[3] + pu[2])
    assert csc2 == Fr(m * m - 1, 3), (m, csc2)                            # prop:csc
    assert csc2 / (4 * m) == beta(0, m) == Fr(m * m - 1, 12 * m)          # def:cone, cor:conevals
    assert csc2 - (m - 1) == Fr((m - 1) * (m - 2), 3)                     # lem:cot (cot^2 = csc^2 - 1)
    # DGGW (5.9): (1/m) sum R1212/(8 sin^4) with R1212 = K
    assert csc4 / (8 * m) == beta(1, m), (m, csc4 / (8 * m), beta(1, m))
# numerical spot check that the u-substitution is right
mp.mp.dps = 40
for m in (5, 11):
    assert abs(mp.fsum(1 / mp.sin(j * mp.pi / m) ** 4 for j in range(1, m)) - mp.mpf(16) * (lambda pu: pu[4] - 2 * pu[3] + pu[2])(power_sums_u(m, 4)).numerator / (lambda pu: pu[4] - 2 * pu[3] + pu[2])(power_sums_u(m, 4)).denominator) < mp.mpf(10) ** -30
log("PC def:cone / prop:csc / lem:cot exact (m<=30); DGGW (5.5),(5.9) cone terms == Ucar beta_0, beta_1 (with R1212=K)")
for m in range(2, MMAX + 1):
    for K in (-1, 0, 1):
        eqb1 = (Fr(1, 360) * (Fr(m) ** 3 - Fr(1, m)) + Fr(1, 36) * (m - Fr(1, m))) * K
        assert eqb1 == Fr(K) * beta(1, m)
assert alpha(1, -1) * 2 == Fr(-2, 3)  # (Area/4pi)*alpha_1 = chi/(2kappa)*kappa/3 = chi/6 for both signs
for kap in (-1, 1):
    # smooth t^0 term = (chi/(2 kappa)) * alpha(1,kappa) must be chi/6 independent of kappa
    assert Fr(1, 2 * kap) * alpha(1, kap) == Fr(1, 6)
log("PC eq:b1 (carries K^1) == Ucar for K in {-1,0,1}; smooth t^0 term chi/6 for kappa=+-1: OK")
ok_groups.append(("paper-core", "b_0=(m^2-1)/(12m) [csc^2 average]; b_1 = [(m^3-1/m)/360+(m-1/m)/36]K; smooth t^0 = chi/6", "K^l (l=1 only; K=-1 used)", "same"))

# DF: only c_1 = Area/4pi = -chi/2 = (1-R)/2 for pillows (kappa=-1)
for (p, q, r) in [(2, 3, 7), (2, 8, 8), (3, 3, 12), (3, 3, 4), (7, 7, 7)]:
    R = Fr(1, p) + Fr(1, q) + Fr(1, r)
    chi = R - 1
    assert heat.c(1, 0, [p, q, r]) == -chi / 2 == (1 - R) / 2
ok_groups.append(("definitions", "c_1=Area/4pi=-chi/2=(1-R)/2; c_j at t^{j-2}; no explicit b_l", "-", "same"))

# AU: b_l = K^l p_l(m)/m, K=-1, p_l even deg 2l+2, p_l(1)=0, leading coeff as claimed (checked above)
for l in range(LMAX + 1):
    for m in range(2, MMAX + 1):
        P = p_sym(l).eval(m)
        assert Fr(-1) ** l * Fr(P.p, P.q) / m == b(l, m, -1)
ok_groups.append(("audibility", "b_l=K^l p_l(m)/m, K=-1; t^{-1} coeff multiple of 2pi(n-2-R)", "K^l", "same"))

# SG: (H2) b_l(k)=K^l sum 2/(4^i i!) c^S_{l-i}(pi/k) -- literal transcription; lem:sigdata (-1)^l k^{-1} p_l(k)
def sg_b(l, k, K):
    return Fr(K) ** l * sum((Fr(2) / (Fr(4) ** i * fact(i)) * cS(l - i, k) for i in range(l + 1)), Fr(0))
for l in range(LMAX + 1):
    for m in range(2, MMAX + 1):
        assert sg_b(l, m, -1) == b(l, m, -1) == Fr(-1) ** l * Fr(p_sym(l).eval(m).p, p_sym(l).eval(m).q) / m
ok_groups.append(("signatures", "(H2) K^l sum 2/(4^i i!) c^S_{l-i}(pi/k); statements.tex: (-1)^l k^{-1} p_l(k); (H3) c_{l+2}=alpha_l Area + C_l", "K^l in (H2), (-1)^l in statements.tex", "same (alpha_l of SG = alpha_{l+1}^{LO}/(4pi): index/normalisation differs from LO)"))

# LO: alpha_k = (-1)^k/(k! 4^k) sum binom(k,l)(-4)^l B_{2l}(1/2) ; beta_k(m) = coefficient of t^k in C at kappa=-1
for k in range(LMAX + 2):
    lo_alpha = Fr((-1) ** k) / (fact(k) * Fr(4) ** k) * sum((binom(k, l) * Fr(-4) ** l * Bhalf(2 * l) for l in range(k + 1)), Fr(0))
    assert lo_alpha == alpha(k, -1)
# Phi_j check: c_j = alpha_{j-1} Area/4pi + sum beta_{j-2}
for (g, ms) in [(0, [2, 3, 7]), (1, [15]), (2, []), (0, [3, 3, 5, 5]), (1, [2, 2, 3])]:
    s = 2 * g - 2 + sum((1 - Fr(1, m) for m in ms), Fr(0))
    for j in range(1, 8):
        phi = alpha(j - 1, -1) * s / 2 + (sum((b(j - 2, m, -1) for m in ms), Fr(0)) if j >= 2 else 0)
        assert phi == heat.c(j, g, ms)
ok_groups.append(("locality", "alpha_k explicit (Ucar 4.35 at kappa=-1), beta_k = coeff of C (4.33) at kappa=-1; Phi_j", "kappa=-1 built in", "same"))

# ST: alpha = 1, -1/3, 1/15, -4/315, 1/315 ; b_nu = (-1)^nu p_nu/m ; H_{-1}=(n-2-R)/2
assert [alpha(j, -1) for j in range(5)] == [1, Fr(-1, 3), Fr(1, 15), Fr(-4, 315), Fr(1, 315)]
for ms in ([2, 8, 8], [3, 10, 15, 30], [2, 2, 2, 2, 3]):
    n = len(ms); R = sum((Fr(1, m) for m in ms), Fr(0))
    hc = heat.heat_coeffs(0, ms, -1, n)
    assert hc[-1] == (n - 2 - R) / 2
    for nu in range(0, n - 1):
        assert hc[nu] == (n - 2 - R) / 2 * alpha(nu + 1, -1) + sum((Fr(-1) ** nu * Fr(p_sym(nu).eval(m).p, p_sym(nu).eval(m).q) / m for m in ms), Fr(0))
ok_groups.append(("stability", "H_{-1}=(n-2-R)/2; H_nu=(Area/4pi)alpha_{nu+1}+sum b_nu; b_nu=(-1)^nu p_nu/m; alpha=1,-1/3,1/15,-4/315,1/315", "(-1)^nu", "same"))

# TH, DI: no analytic input beyond (S_1,R) from c_1, c_2 -- check c_1,c_2 <-> (R,S_1) for pillows
ok_groups.append(("threshold", "none (uses sigma=(S_1,R) from paper)", "-", "n/a"))
ok_groups.append(("diophantine", "none (uses a_0, a_1 language = two coefficients)", "-", "n/a; see indexing finding"))

# CU: flat (K=0) Kokotov; spherical a_0 = chi/6 + sum (m^2-1)/(12m); higher coeffs K^l
for m in range(2, MMAX + 1):
    beta_cone = 2 * sp.pi / m
    kok = sp.Rational(1, 12) * (2 * sp.pi / beta_cone - beta_cone / (2 * sp.pi))
    assert sp.nsimplify(kok) == sp.Rational(m * m - 1, 12 * m) == sp.Rational(beta(0, m).numerator, beta(0, m).denominator)
    for l in range(1, LMAX + 1):
        assert b(l, m, 0) == 0
flat = {"T2": [], "(2,2,2,2)": [2, 2, 2, 2], "(3,3,3)": [3, 3, 3], "(2,4,4)": [2, 4, 4], "(2,3,6)": [2, 3, 6]}
c0_claim = [Fr(0), Fr(1, 2), Fr(2, 3), Fr(3, 4), Fr(5, 6)]
dggw_c = [0, 6, 8, 9, 10]   # DGGW Thm 5.15 proof: c = 12 x degree-zero term
for (name, ms), cl, dc in zip(flat.items(), c0_claim, dggw_c):
    g = 1 if name == "T2" else 0
    chi = 2 - 2 * g - sum((1 - Fr(1, m) for m in ms), Fr(0))
    assert chi == 0
    c0 = sum((beta(0, m) for m in ms), Fr(0))
    assert c0 == cl and 12 * c0 == dc
log("CU flat c_0 = 0,1/2,2/3,3/4,5/6 and DGGW c = 0,6,8,9,10: OK; Kokotov (F) == b_0; K=0 kills l>=1")
ok_groups.append(("curvature", "Kokotov (F) at K=0; a_0=chi/6+sum(m^2-1)/(12m) at K=+1; b_l = K^l(...) ", "K^l, K in {0,+1,-1}", "same"))

# DV: Lemma 1(a): c_l(pi/k) = (-1)^l (2l+2)! / (4k (l+1)! (2l+1)) g_{2l+2}(k),
#     G_k(t) = (t/2)/sinh(t/2) [ (kt/2)coth(kt/2) - (t/2)coth(t/2) ]
def xcothx(scale, N):   # series coefficients of (s t/2) coth(s t/2) in t up to t^N
    return [Fr(0) if n % 2 else B(n) * Fr(scale) ** n / fact(n) for n in range(N + 1)]   # x coth x = sum B_{2n} (2x)^{2n}/(2n)!
def xcschx(N):          # (t/2)/sinh(t/2) = sum (2-2^{2n}) B_{2n} (t/2)^{2n}/(2n)!
    return [Fr(0) if n % 2 else (2 - Fr(2) ** n) * B(n) * Fr(1, 2) ** n / fact(n) for n in range(N + 1)]
NN = 2 * LMAX + 2
A0 = xcschx(NN)
for k in range(2, MMAX + 1):
    br = [a - bb for a, bb in zip(xcothx(k, NN), xcothx(1, NN))]
    g = [sum((A0[i] * br[n - i] for i in range(n + 1)), Fr(0)) for n in range(NN + 1)]
    for l in range(LMAX + 1):
        lhs = Fr((-1) ** l) * fact(2 * l + 2) / (4 * k * fact(l + 1) * (2 * l + 1)) * g[2 * l + 2]
        assert lhs == cS(l, k), (k, l)
        assert Fr(-1) ** l * g[2 * l + 2] > 0
log("DV Lemma 1(a) generating-function form == Ucar (4.25), and (b) sign, for l<=8, k<=30: OK")
# DV Theorem 3: a_l = C s_{l+1} K^{l+1} + K^l sum beta_l, C=|chi|/2 ; s_k not defined in the register:
# the only reading consistent with Ucar is s_k = alpha_unit(k)  (a_k/vol at kappa=+1).
for k in range(0, 41):
    assert alpha_unit(k) > 0   # Cor 4 needs s_k > 0
for (g, ms, K) in [(0, [2, 8, 8], -1), (0, [3, 3, 12], -1), (2, [5], -1), (0, [2, 3, 5], 1), (0, [7, 7], 1)]:
    chi = 2 - 2 * g - sum((1 - Fr(1, m) for m in ms), Fr(0))
    C = abs(chi) / 2
    hc = heat.heat_coeffs(g, ms, K, LMAX + 2)
    for l in range(LMAX + 1):
        a_l = C * alpha_unit(l + 1) * Fr(K) ** (l + 1) + Fr(K) ** l * sum((beta(l, m) for m in ms), Fr(0))
        assert a_l == hc[l]
log("DV Theorem 3 a_l formula == assembled coefficient (K=+-1) with s_k := Ucar a_k/vol at kappa=1 > 0 (k<=40)")
ok_groups.append(("divergence", "b_l=K^l beta_l (beta from 4.25/4.33); Lemma 1(a) via G_k; a_l = C s_{l+1}K^{l+1}+K^l sum beta_l", "K^l, K=+-1", "same (s_k undefined in the statement)"))

# DV Theorem 2 sanity (asymptotic, high precision): p_l/(lambda_l m^{2l+2}) -> sigma_m
mp.mp.dps = 60
for m in (2, 3, 7):
    sig = (mp.pi / m) / mp.sin(mp.pi / m)
    errs, sc = [], []
    for l in (10, 20, 40, 80):
        bl = mp.mpf(beta(l, m).numerator) / beta(l, m).denominator
        lam = mp.mpf(lead_claimed(l).numerator) / lead_claimed(l).denominator
        r = bl * m / (lam * mp.mpf(m) ** (2 * l + 2))
        errs.append(abs(r - sig))
        A = mp.factorial(2 * l) / (mp.factorial(l) * m * mp.sin(mp.pi / m)) * (mp.mpf(m) / (2 * mp.pi)) ** (2 * l + 1)
        sc.append(abs(bl / A - 1 - mp.pi ** 2 / (2 * m * m * (2 * l - 1))) * l * l)
    assert errs[0] > errs[1] > errs[2] > errs[3], (m, errs)          # ratio -> sigma_m (rate 1/l)
    assert max(sc) < 5 and sc[3] < 2 * sc[2] + 1e-12, (m, sc)          # remainder is O(l^-2)
log("DV Theorem 2: p_l/(lambda_l m^{2l+2}) -> sigma_m; b_l/A_l - 1 - pi^2/(2m^2(2l-1)) = O(l^-2) (l=10..80, m=2,3,7): OK")

# ---------------------------------------------------------------- spherical sign check
# Independent check of the K^l convention at K=+1 from the exact spectrum (CU Lemma 2).
log("\n== 3. Spherical (K=+1) sign check from the spectrum of S^2/G (CU Lemma 2), high-precision ==")
mp.mp.dps = 80
def N_l(l, orders, Gord):
    return Fr(2 * l + 1, Gord) + Fr(1, 2) * sum((2 * (l // m) + 1 - Fr(2 * l + 1, m) for m in orders), Fr(0))
for orders, Gord in [((2, 3, 5), 60), ((2, 3, 4), 24), ((2, 3, 3), 12), ((5, 5), 5), ((2, 2, 7), 14)]:
    Ns = [N_l(l, orders, Gord) for l in range(4000)]
    assert Ns[0] == 1 and all(x.denominator == 1 and x >= 0 for x in Ns)
    Ns = [int(x) for x in Ns]
    hc = heat.heat_coeffs(0, list(orders), 1, 10)   # t^-1 .. t^8
    t = mp.mpf('0.0001')
    Z = mp.fsum(Ns[l] * mp.e ** (-l * (l + 1) * t) for l in range(4000))
    for K in (2, 4, 6, 8):
        pred = sum(mp.mpf(hc[p].numerator) / hc[p].denominator * t ** p for p in range(-1, K))
        nxt = mp.mpf(hc[K].numerator) / hc[K].denominator
        # (Z - sum_{p<K} c_p t^p)/t^K -> c_K : confirms every coefficient below t^K, signs included
        assert abs((Z - pred) / t ** K - nxt) < mp.mpf('0.02') * abs(nxt), (orders, K)
    log(f"S^2/G orders {orders}: spectrum reproduces t^-1..t^8 coefficients (K=+1); a_0={hc[0]}, a_1={hc[1]}")
# with the opposite sign on the l=1 cone term the t^1 coefficient would be wrong:
hc = heat.heat_coeffs(0, [2, 3, 5], 1, 3)
assert hc[0] == Fr(271, 360)   # PC.2 reference value
wrong = hc[1] - 2 * sum((beta(1, m) for m in (2, 3, 5)), Fr(0))
assert wrong != hc[1]

log("\n== 4. Summary table ==")
for row in ok_groups:
    log(" | ".join(row))

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_heat_input.txt"), "w") as f:
    f.write("\n".join(out) + "\nALL HEAT-INPUT CHECKS PASSED\n")
print("ALL HEAT-INPUT CHECKS PASSED")
