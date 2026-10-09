# VC7 adversarial check: linear part of b_l(Phi) and of a_l(p)

I worked from the statement in the task brief only. Inside `theory/varcurv/` I read only `SOURCES.md` and the earlier
attacker's `attack/ATTACK-REPORT.md`, `attack/twisted_duhamel_output.txt` and `attack/nonradial_test_output.txt`.
I opened none of the forbidden files. I fetched nothing.

**Overall verdict: (a) CONFIRMED, (b) CONFIRMED, (c) CONFIRMED.** One wording caveat for (c) is given below. I found
no counterexample.

## Method (independent of the earlier attacker)

The earlier attacker used normal coordinates, a Weyl-algebra Duhamel expansion and radial jets. I used a
different route: a first-order perturbation of the flat rotation in **isothermal coordinates**.

- **Setup.** Write g = e^{2 eps psi}|dx|^2 with psi invariant under Phi = R_phi. Then
  Delta_g = -e^{-2 eps psi} lap = Delta_0 + eps V + O(eps^2), with V = 2 psi lap.
- **Duhamel term.** The first-order term is
  K_1(t,x,y) = -int_0^t ds int dz K0(t-s,x,z) 2 psi(z) lap_z K0(s,z,y).
  K is the kernel with respect to Lebesgue measure. The kernel with respect to dvol_g is
  H(x,y) = K(x,y) e^{-2 eps psi(y)}. Because psi(Phi q) = psi(q), the identity
  int H(t,q,Phi q) dvol(q) = int K(t,q,Phi q) dq holds exactly.
  So the linear part of sum_l b_l t^l is L(psi)(t) = int dq K_1(t,q,Phi q).
- **Jet dictionary at linear order.**
  - K = e^{-2psi}(-lap psi), so the linear part of K is -lap psi.
  - -Delta_g = e^{-2psi} lap, so the linear part of (-Delta_g)^{l-1}K(p) is -lap^l psi(0).
- **Normal vs isothermal coordinates.** The two coordinate systems differ by x_iso = x_norm + (jet) * O(|x|^3).
  So the Taylor coefficients of K in the two systems differ only by terms of degree >= 2 in the jet. The same holds
  for the coordinate expression of (-Delta_g)^{l-1}K(p), which is an invariant. The linear part therefore does not
  depend on the coordinate choice.
  Cross-check: route C below compares my isothermal result with the earlier attacker's normal-coordinate result,
  and they agree.
- **Phi is linear.** Phi is an isometry fixing p, so it is linear in normal coordinates. Its isotropy group is
  compact, so one can also choose isothermal coordinates in which Phi is the rotation R_phi.
- **dpsi(0) = 0 automatically.** The degree-1 part of psi would have to be fixed by a rotation through
  phi in (0, 2pi), and no such rotation fixes a nonzero vector.

### Route A: generating function, all l (`vc7_conformal_genfun.py`)

- **Setup.** Take psi = exp(a.z) with a = (a1, a2) symbolic. Then L is a 4-dimensional Gaussian integral, and I
  kept cos phi and sin phi symbolic.
- **Intermediate results (exact).**
  - det M = 4 lam^2 mu^2 (1-c)^2.
  - The exponent is (a.a) t/C^2, which does not depend on s.
  - The s-integrand is (a.a) e^{(a.a)t/C^2}/C^4, which is constant in s.
- **Closed form.** L(t) = -(2/C^2) x e^x, with x = (a.a) t / C^2.
- **Reading off b_l.** The degree-2l part of psi is (a.z)^{2l}/(2l)!, and its lap^l is (a.a)^l. So the coefficient
  of t^l is (2/(l-1)!) C^{-2l-2} (-lap^l psi(0)). This is exactly VC7(a), for every l.
  - It was asserted coefficient by coefficient for l = 0..8.
  - The l = 0 coefficient is 0, which is correct: b_0 = C^{-2} has no linear part.
- **Non-radial jets and half-integer powers.** L depends on a only through a.a.
  - Every homogeneous polynomial of degree n is spanned by the powers (a.z)^n. By linearity (polarisation),
    L(P) = c_n lap^{n/2} P(0) for every such P.
  - Hence non-radial (frequency != 0) parts of the jet never enter the linear part.
  - Odd degrees give 0, so there are no half-integer powers t^{n/2} at linear order.
  - The structural reason is that L is invariant under all of SO(2), because every rotation commutes with Phi.
    So L annihilates every component z^a zbar^b with a != b, even when that component is Z_m-invariant.

### Route B: explicit polynomials, Wick moments (`vc7_explicit_monomials.py`)

Route B uses the same functional but a different evaluation: an explicit polynomial psi, lap_z K0 obtained by direct
differentiation, Gaussian moments from the covariance (2M)^{-1}, and an explicit s-integral. The angle phi takes
exact values pi, 2pi/3, 4pi/3, pi/2 and pi/3, plus a generic rational parametrisation of the angle. 37 exact
asserts pass:

- **Radial.** psi = r^{2l} for l = 1..4 at all five angles, and a mixed radial jet: L equals the VC7(a) prediction.
- **Non-radial, Phi-invariant psi: L = 0 every time.** The cases tested:
  - Re z^2, r^2 Im z^2, Re z^4, r^2 Re z^4, r^4 Re z^2 and r^6 Re z^2 at m = 2. The last two have the weights of
    l = 3 and l = 4.
  - Re z^3 and r^2 Im z^3 at m = 3. These are odd degree, so this is the half-integer-power test.
  - Re z^6 and r^2 Re z^6 at m = 3, and Re z^3 + r^2 Re z^3 at angle 4pi/3.
  - Re z^4 + r^2 Im z^4 at m = 4, and Re z^6 at m = 6.
- **Mixed.** r^4 + 11 Re z^4 - 3 r^2 Re z^2 at m = 2 gives exactly the radial answer.
- **Generic phi.** r^4 gives L = -2 t^2 (1+u^2)^3/u^6 = -128 t^2/C^6, using C^2 = 4u^2/(1+u^2). This matches
  (2/1!) C^{-6} (-lap^2 r^4) with lap^2 r^4 = 64. Re z^4 gives 0.

### Route C: cross-check against an independent nonlinear computation (`vc7_cone_checks.py`, part 1)

- **Earlier attacker's b_1..b_5.** I took their full radial b_1..b_5 (normal coordinates, K = sum k_j r^{2j}) and
  extracted the degree-1 part. It is exactly 2 X^2 k0, 8 X^3 k1, 64 X^4 k2, 768 X^5 k3 and 12288 X^6 k4, with
  X = C^{-2}.
  - VC7(a) predicts 2 * 4^{l-1} (l-1)! X^{l+1} k_{l-1}, which matches all five.
  - All C^{-2i} terms with i <= l in their b_l are of degree >= 2 in the jet. This confirms the clause "no C^{-2i}
    terms with i <= l".
- **Schueth Thm 3.7.** The linear part of b_2 is -(2/C^6) Delta_g K, which equals (2/1!) C^{-6} (-Delta_g) K.

### (b), (c) checks (`vc7_cone_checks.py`, parts 2-4)

- **Pi_i(m) values.** For i = 1..7 and m = 2..20, I computed Pi_i(m) exactly as tr((L_cycle + J/m)^{-i}) - 1,
  divided by m. These values match the trigonometric sums to 50 digits.
- **Pi_i(m) polynomial form.** m Pi_i(m) is a polynomial of degree 2i that vanishes at m = 1, with leading
  coefficient |B_2i|/(2i)!. I interpolated it on 2i+1 points and verified it on all of m = 2..20.
- **(b), l = 2.** Schueth Thm 4.1's coefficient of Delta_g K equals -2 Pi_3(m) identically as a rational function of
  m. Here Pi_3 = (m^2-1)(2m^4+23m^2+191)/(60480 m). A direct j-average of Thm 3.7 gives the same result for
  m = 2..20.
- **(b), l = 1.** Schueth Rem. 4.2 (Donnelly) gives the coefficient of K in a_1 as
  (m^3-1/m)/360 + (m-1/m)/36. This equals 2 Pi_2(m) identically.
- **(b), l = 1..6, m = 2..20.** The j-average of (a) equals (2/(l-1)!) Pi_{l+1}(m).
  - m = 2 (phi = pi) is not special, and m < l is allowed. Route A is a single analytic formula in 0 < C <= 2,
    so (b) needs no lower bound on m.
  - This contrasts with the earlier attacker's result: at l = 4, m = 2, the traceless Hessian enters b_4(pi), but
    only **quadratically** (7/480 h2^2). That is consistent with VC7, which is a statement about the linear part.
- **(c).** The four stated examples (l = 1..4) are exactly (2/(l-1)!) Pi_{l+1}(m) (-Delta)^{l-1} K, with top power
  m^{2l+1}. The leading coefficient |B_{2l+2}|/(2l+2)! is checked for l = 1..6.
  - (-Delta_g)^{l-1}K is the only monomial of weight 2l that contains the (2l-2)-jet of K. So its coefficient in
    a_l is exactly the linear part from (b).

## Answers to the suggested gap hunts

- **Normal vs isothermal coordinates.** The linear part does not depend on the choice (argument above). The isothermal
  result (A/B) agrees with the normal-coordinate result (C).
- **Is (-Delta)^{l-1}K the only SO(2)-invariant linear jet invariant of weight 2l?** Yes. A linear SO(2)-invariant
  of the degree-(2l-2) jet must pair with the frequency-0 component, which is one-dimensional (r^{2l-2}).
  - For Z_m there are more linear invariants: the Re and Im parts of the frequency-km components of the jet.
  - VC7 claims they have coefficient 0. Route A proves this, because L is SO(2)-invariant, and route B checks it
    on examples.
- **m = 2.** Nothing special happens at m = 2.
- **Orientation-reversing symmetries.** These are outside the hypothesis, which requires dPhi to be a rotation with
  phi in (0, 2pi). A reflection fixes a curve, not an isolated point, and its contribution has a t^{-1/2} boundary
  structure. **Not tested**, and VC7 does not cover it.
- **Half-integer powers.** None appear at linear order (route A, and route B's odd-degree cases).
- **Sign.** With Delta_g = -div grad: K_lin = -lap psi, and route A's l = 1 coefficient -2(a.a)/C^4 equals
  2 K_lin/C^4, which matches Donnelly's b_1. Route C confirms the sign against Schueth and the earlier code. The sign
  is correct.

## Caveat on (c) (wording, not a counterexample)

"(-Delta_g)^{l-1}K occurs with the TOP power of m" is correct. But the top power m^{2l+1} is not exclusive to the
highest derivative. For example, the K^2 term in Schueth's a_2 carries m^5/2520, and the earlier attacker's b_4 has
K^4, K^2 DK and other terms at X^5. If (c) is meant to say that only the highest derivative carries m^{2l+1}, it would
be false; as written it is true.

## Rigor notes and what I did not test

- **Formal Duhamel step.** The first-order term uses a global polynomial (or exponential) psi. I justify this through
  locality (DGGW 4.1, as quoted in SOURCES.md) and the fact that the b_l are universal polynomials in the jet. A
  cutoff changes the result only by O(t^infinity). I did not write out the analytic estimate.
- **Scope of the l = 0..8 check.** Route A holds for all l in closed form. The explicit-coefficient assertion covers
  l = 0..8, and route B covers l <= 4 with non-radial terms up to weight 8. I did not run explicit route-B
  non-radial monomials at l = 5, 6. Route A covers them.
- **Not tested.**
  - The nonlinear parts of b_l or a_l (outside VC7).
  - Orientation-reversing or dihedral corner points.
  - Non-orbifold cone angles.

## Files

- `vc7_conformal_genfun.py` / `_output.txt`: route A (closed form, all l; asserts for l = 0..8)
- `vc7_explicit_monomials.py` / `_output.txt`: route B (37 exact asserts; about 10 min of CPU)
- `vc7_cone_checks.py` / `_output.txt`: route C, Pi_i, (b), (c) (24 checks)
