"""VC7 attack, parts (b), (c), plus cross-check of (a) against an independent NONLINEAR computation.

1. Cross-check (a) against the earlier attacker's full radial b_0..b_5 (normal coordinates, Weyl-algebra
   Duhamel; ../twisted_duhamel_output.txt): extract the degree-1 part in the jet (k0,...,k5) and compare
   with (2/(l-1)!) X^{l+1} (-Delta)^{l-1}K |_lin, where K = sum k_j r^{2j} in normal coords, -Delta = lap,
   so lap^{l-1} K(0) |_lin = 4^{l-1} ((l-1)!)^2 k_{l-1}.
   Also: Schueth Thm 3.7 linear part of b_2 is -(2/C^6) Delta_g K.
2. Pi_i(m) exactly (trace of (L_cycle + J/m)^{-i}), against 50-digit trig sums, m = 2..20,
   i = 1..7; polynomial structure in m and leading coefficient |B_2i|/(2i)! m^{2i-1}.
3. (b) against Schueth Thm 4.1 (l=2) and Remark 4.2 / Donnelly (l=1), as rational functions of m, and the
   linear part of a_l obtained by averaging (a) over j, m = 2..20.
4. (c) the examples l = 1..4 and the leading m-power.
"""
import re
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
m, X, C, u = sp.symbols('m X C u', positive=True)

# ---------------------------------------------------------------- 1
txt = open('../twisted_duhamel_output.txt').read()
ks = sp.symbols('k0:6')
loc = {f'k{i}': ks[i] for i in range(6)}
loc['X'] = X
b = {}
for line in txt.splitlines():
    mm = re.match(r'^b_(\d) = (.*)$', line)
    if mm:
        b[int(mm.group(1))] = sp.sympify(mm.group(2), locals=loc)
assert set(b) == set(range(6))
eps = sp.symbols('eps')
for l in range(1, 6):
    lin = sp.expand(sp.diff(b[l].subs({k: eps * k for k in ks}), eps).subs(eps, 0))
    pred = sp.Rational(2, sp.factorial(l - 1)) * X**(l + 1) * 4**(l - 1) * sp.factorial(l - 1)**2 * ks[l - 1]
    assert sp.expand(lin - pred) == 0, (l, lin, pred)
    print(f"earlier-attacker b_{l}: linear part = {lin}   == VC7(a): OK")
# Schueth Thm 3.7
K, DK = sp.symbols('K DK')
b2S = (12 / C**6 - 2 / C**4) * K**2 - 2 / C**6 * DK
linS = sp.expand(sp.diff(b2S.subs({K: eps * K, DK: eps * DK}), eps).subs(eps, 0))
assert sp.expand(linS - sp.Rational(2, 1) * C**-6 * (-DK)) == 0
print("Schueth Thm 3.7 linear part -2 C^-6 Delta K == VC7(a) l=2: OK")


# ---------------------------------------------------------------- 2
def Pi_exact(i, mm):
    """(1/m) sum_{j=1}^{m-1} (4 sin^2(pi j/m))^{-i}, exact: the cycle-graph Laplacian L_m has eigenvalues
    4 sin^2(pi j/m), j=0..m-1; L + J/m (J = all-ones) replaces the eigenvalue 0 by 1, so the sum is
    tr((L + J/m)^{-i}) - 1, computed in exact rational arithmetic."""
    L = sp.zeros(mm)
    for a in range(mm):
        L[a, a] += 2
        L[a, (a + 1) % mm] -= 1
        L[a, (a - 1) % mm] -= 1
    A = (L + sp.ones(mm) / mm).inv()
    val = (A**i).trace() - 1
    assert val.is_Rational, val
    return val / mm


def Pi_num(i, mm):
    return mp.fsum(1 / (4 * mp.sin(mp.pi * j / mm)**2)**i for j in range(1, mm)) / mm


Pi_tab = {}
for i in range(1, 8):
    for mm in range(2, 21):
        v = Pi_exact(i, mm)
        assert abs(mp.mpf(v.p) / v.q - Pi_num(i, mm)) < mp.mpf(10)**-40
        Pi_tab[(i, mm)] = v
print("Pi_i(m) exact (cycle-Laplacian trace) == 50-digit trig sums, i=1..7, m=2..20: OK")

Pi_poly = {}
for i in range(1, 8):
    # m*Pi_i(m) is a polynomial in m of degree 2i: interpolate on 2i+1 points, check on the rest
    pts = list(range(2, 2 * i + 3))
    poly = sp.interpolate([(mm, mm * Pi_tab[(i, mm)]) for mm in pts], m)
    for mm in range(2, 21):
        assert poly.subs(m, mm) == mm * Pi_tab[(i, mm)], (i, mm)
    assert sp.degree(poly, m) == 2 * i
    lead = sp.Poly(poly, m).LC()
    assert lead == abs(sp.bernoulli(2 * i)) / sp.factorial(2 * i), (i, lead)
    assert poly.subs(m, 1) == 0
    Pi_poly[i] = sp.expand(poly / m)
    print(f"Pi_{i}(m) = {sp.factor(Pi_poly[i])};  leading coeff |B_{2*i}|/({2*i})! = {lead}: OK "
          f"(interpolated on {len(pts)} pts, verified m=2..20)")

# ---------------------------------------------------------------- 3
a2_lin_S = -((m**5 - 1 / m) / 15120 + (m**3 - 1 / m) / 1440 + (m - 1 / m) / 180)   # coefficient of Delta K
assert sp.simplify(a2_lin_S - (-2 * Pi_poly[3])) == 0
print("(b) l=2: Schueth Thm 4.1 coefficient of Delta_g K == -2 Pi_3(m) as rational functions: OK")
a1_S = (m**3 - 1 / m) / 360 + (m - 1 / m) / 36          # Remark 4.2 (Donnelly b_1 averaged)
assert sp.simplify(a1_S - 2 * Pi_poly[2]) == 0
print("(b) l=1: Schueth Rem 4.2 / Donnelly a_1 coefficient of K == 2 Pi_2(m): OK")
a0_S = (m - 1 / m) / 12
assert sp.simplify(a0_S - Pi_poly[1]) == 0
print("    (sanity) a_0 = Pi_1(m) = (m - 1/m)/12: OK")
# full Schueth a_2 also from averaging Thm 3.7 (checks the C^-4 / C^-6 bookkeeping)
for mm in range(2, 21):
    avg = sum(((12 / C**6 - 2 / C**4) * K**2 - 2 / C**6 * DK).subs(C, sp.sqrt(4 * sp.sin(sp.pi * j / mm)**2))
              for j in range(1, mm)) / mm
    lhs_lin = sp.nsimplify(sp.N(sp.diff(avg, DK), 60), rational=True)
    assert lhs_lin == -2 * Pi_tab[(3, mm)] or abs(sp.N(sp.diff(avg, DK) + 2 * Pi_tab[(3, mm)], 50)) < 1e-40
print("(b) l=2: direct average of Thm 3.7 over j, m=2..20: coefficient of Delta K = -2 Pi_3(m): OK")
# general l: averaging (a) gives (2/(l-1)!) Pi_{l+1}(m); check the j-average numerically vs exact Pi
for l in range(1, 7):
    for mm in range(2, 21):
        avg = mp.fsum(2 / mp.factorial(l - 1) * (4 * mp.sin(mp.pi * j / mm)**2)**(-l - 1)
                      for j in range(1, mm)) / mm
        ex = sp.Rational(2, sp.factorial(l - 1)) * Pi_tab[(l + 1, mm)]
        assert abs(avg - mp.mpf(ex.p) / ex.q) < mp.mpf(10)**-35 * max(1, abs(avg))
print("(b) l=1..6, m=2..20: (1/m) sum_j (2/(l-1)!) C_j^{-2l-2} == (2/(l-1)!) Pi_{l+1}(m): OK")

# ---------------------------------------------------------------- 4
D = sp.symbols('Delta')       # stands for Delta_g acting on K
for l, claimed in [(1, 2 * Pi_poly[2]), (2, -2 * Pi_poly[3] * D), (3, Pi_poly[4] * D**2), (4, -sp.Rational(1, 3) * Pi_poly[5] * D**3)]:
    general = sp.Rational(2, sp.factorial(l - 1)) * Pi_poly[l + 1] * (-D)**(l - 1)
    assert sp.expand(general - claimed) == 0
    top = sp.Poly(sp.expand(m * general), m).degree() - 1
    assert top == 2 * l + 1
    print(f"(c) l={l}: (2/(l-1)!) Pi_{l+1} (-Delta)^{l-1} K == stated example; top power m^{top}: OK")
# leading coefficient in m of Pi_{l+1}
for l in range(1, 7):
    lc = sp.Poly(sp.expand(m * Pi_poly[l + 1]), m).LC()
    assert lc == abs(sp.bernoulli(2 * l + 2)) / sp.factorial(2 * l + 2)
print("(c) leading term of Pi_{l+1}(m) is |B_{2l+2}|/(2l+2)! m^{2l+1}, l=1..6: OK")
# (c) caveat: K^l also carries the top power (e.g. a_2: m^5/2520 K^2); so "top power" is not exclusive
print("(c) note: K^2 in Schueth a_2 also carries m^5 (coefficient 1/2520): the top power is shared, not exclusive")
print("DONE")
