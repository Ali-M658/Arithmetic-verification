# Adversarial check of theory/varcurv/statements.tex (VC1-VC6, Lemma VC5a)

Input read: `statements.tex` only. No other file in `theory/varcurv/` was opened.
Sources fetched with curl and read with PyMuPDF: Schueth arXiv:1812.06119, Schueth arXiv:2511.22255,
Dryden-Gordon-Greenwald-Webb arXiv:0805.3148, Ucar arXiv:1711.03405, and Vassilevich hep-th/0306138
(for Gilkey's a_6, eq. (4.29)).

## Independent method (used for VC1, VC2, VC3, VC4)

`twisted_duhamel.py` does not use Schueth's distance-function substitution. It works like this:

- In Cartesian normal coordinates, Delta_g = Delta_0 - a(r^2) E - b(r^2) Theta^2, where
  a = (f'/f - 1/r)/r, b = f^-2 - r^-2, E = x.grad and Theta = x1 d2 - x2 d1.
- Rescaling x = sqrt(t) y gives t Delta_g = Delta_0 + sum_k t^k V_k.
- Then I(t) = Tr(e^{-L_t} R_phi^*). This is expanded with the Duhamel series. Each e^{-sDelta_0} is moved to
  the right using the Heisenberg conjugation y -> y + 2 s d, in an exact Weyl-algebra implementation.
- What remains are traces Tr(y^a d^b e^{-Delta_0} R^*), which are Gaussian moments with weight
  exp(-C^2|y|^2/4).
- cos(phi) and sin(phi) are kept symbolic. The script asserts that odd powers of sin(phi) cancel, then substitutes
  cos(phi) = 1 - C^2/2.

All arithmetic is exact (sympy Rationals). The computation reached b_5, with K = k0 + k1 r^2 + ... + k5 r^10.
Output: `twisted_duhamel_output.txt`.

Calibration (all exact):
- b_0 = 1/C^2 and b_1 = 2K/C^4 (Donnelly, as quoted in Schueth Rem. 3.2).
- b_2 reproduces Schueth Thm 3.7 exactly: (12/C^6 - 2/C^4)K^2 - (2/C^6) Delta K.
- Averaging b_2 reproduces Schueth Thm 4.1 exactly.
- At constant curvature, (1/m) sum_j b_l(2 pi j/m) equals Ucar (4.33)-(4.34) (with c^S_l from (4.25)) for
  l = 0..5 and m = 2..15.

## Verdicts

### VC1 (structure): CONFIRMED by independent computation for l <= 5 (radial); non-radial clause confirmed at l = 3 and its threshold shown to be sharp

- b_l(phi) is a polynomial in X = C^-2 with powers 2..l+1 for l = 1..5. It is exactly X for l = 0. No C^0
  term and no positive powers of C appear, as an identity in phi.
- Unclaimed side observation: beta_{l,1} = 0 for 1 <= l <= 5. The lowest power is always C^-4.
- The m*Pi_i formulas for i = 1..4 hold exactly for m = 1..21. Pi_i is computed exactly as
  tr((L_cycle + J/m)^{-i}) - 1, and also agrees numerically to 50 digits.
- For i <= 7, m*Pi_i is an even polynomial of degree 2i that vanishes at m = 1, with leading coefficient
  |B_2i|/(2i)!. This was checked by interpolation plus 6 extra points.
- **Non-radial attack** (`nonradial_test.py`, output `nonradial_test_output.txt`):
  - Setup: geodesic polar coordinates with K(r, theta) containing frequency-2, 4 and 6 parts (h2, g2, g4, q2, q4, q6),
    f_rr = -K f, and Delta_g - Delta_0 = -A E - B Theta^2 + (f_theta/f^3) Theta. The same Duhamel/Weyl
    machinery was used.
  - b_1(pi), b_2(pi) and b_3(pi) do not depend on the non-radial parameters.
  - At m = 2 and m = 4 (frequency-4 jet), a_3 equals the VC3 formula evaluated on K, Delta_g K and
    Delta_g^2 K.
  - At l = 4, m = 2, however, b_4(pi) = (7/480) h2^2 + (radial part), where h2 is the traceless Hessian of K. The
    radial part was cross-checked against b_4 at X = 1/4.
  - So the hypothesis m >= max(2, l-1) is genuinely needed: at m = l-2 the radial-part reduction fails. This
    agrees with the frequency/weight argument (a non-radial Z_m-invariant needs weight >= 2(m+2)).
- Not tested: an l = 4, m = 3 non-radial jet. The weight count makes it trivially safe there.

### VC2 (top coefficient): CONFIRMED (radial); (i) holds for all l by the argument below

- The formula 4^l l! [v^2l](f^-1)'(v) equals the C^{-2(l+1)} coefficient of my independently computed b_l for
  l = 1..5. For the computation I used Lagrange inversion: [v^2l](f^-1)' = [r^2l](r/f)^{2l+1}.
- (ii) holds for l = 1..12: the formula gives (2l)!/l! kappa^l. Multiplied by |B_{2l+2}|/(2l+2)!, it equals
  Ucar's coefficient of k^{2l+1}, coming from (4.25) and (4.33). The sign is (-1)^l B_{2l+2} = |B_{2l+2}|.
- (i): the coefficient of k_{l-1} is exactly 2 * 4^{l-1} (l-1)!, which equals 2 (div grad)^{l-1}K(p)/(l-1)! at
  linear order. I asserted this for l = 1..8. It holds for all l, because the linear part of
  [r^2l](r/f)^{2l+1} is (2l+1) k_{l-1}/(2l(2l+1)). There is no sign-convention error: (-Delta_g) = div grad.
- (iii): beta_{1,2}, beta_{2,3}, beta_{3,4} and beta_{4,5} all hold exactly, using the radial invariants:
  - Delta K = -4k1
  - Delta^2 K = -8k0k1/3 + 64k2
  - Delta^3 K = 16k0^2k1/15 + 128k0k2 + 128k1^2/5 - 2304k3

  For reference, here is the full b_4 (`b4_invariants_output.txt`):
  b_4 = (1680K^4 - 904K^2 DK + 98/3 K D2K + 124/3 DK^2 - 1/3 D3K) X^5
      + (-600K^4 + 280K^2 DK - 20/3 K D2K - 10 DK^2) X^4 + (52K^4 - 52/3 K^2 DK + 1/3 DK^2) X^3 - 2/3 K^4 X^2.
- (iv): this follows from the leading coefficient of mPi_{l+1}. It also reproduces the m^5 coefficient of
  Schueth Thm 4.1 exactly: 1/2520 K^2 - 1/15120 Delta K = (1/30240)(12K^2 - 2 Delta K).
- Not tested: the general u-averaged rho_u formula for non-radial germs. It only has to agree on radial
  jets / m >= l-1, which is the domain where it is used.

### VC3 (t^3 cone coefficient): CONFIRMED by independent computation

- My b_3 is exactly the claimed expression:
  X^4(120k0^3 + 496k0k1/3 + 64k2) + X^3(-32k0^3 - 32k0k1) + (4/3)X^2 k0^3.
  This is equivalent to (120X^4 - 32X^3 + 4/3 X^2)K^3 + (-42X^4 + 8X^3) K Delta K + X^4 Delta^2 K.
- A(m), B(m) and D(m) agree as rational functions. They also agree by direct exact averaging for m = 2..15.
- A(m) equals Ucar's kappa^3 coefficient for m = 2..30.
- It also holds for non-radial Z_2 and Z_4 jets (see VC1).
- Scripts: `twisted_duhamel.py`, `vc_checks.py`, `nonradial_test.py`.

### VC4 (extension): CONFIRMED (finite parts checked exactly); one redundancy

- Pi_i lies in span{m^{2k-1} - 1/m : k <= i}, and the coefficient of psi_i is |B_2i|/(2i)! (for i <= 6).
- At constant curvature, a_l(p) = sum_{k<=l+1} e_{lk} kappa^l psi_k(m), with
  e_{l,l+1} = (2l)!/l! |B_{2l+2}|/(2l+2)! != 0 (for l <= 5). This gives the triangular structure.
- I brute-forced the "iff" on 495 genus-0 signatures (m_i <= 9, n <= 4), for kappa = +-1 and L = 2..7. The
  J-version was checked for L = 2..5 with a generic common jet.
- The cone term at t^l uses only k_j with j <= l-1, i.e. derivatives of K of order <= 2l-2. This is seen in
  b_1..b_5: k_{l-1} appears and k_l does not.
- kappa = 0 failure: all b_l vanish for l >= 1 on a flat germ (checked l = 1..5). The VC6 pairs have equal
  chi^orb and Psi_1 but different Psi_2, which gives a counterexample to the "only if" direction for every
  L >= 3, provided VC6 holds.
- Remark (not an error): S_0 = chi^orb/6 by orbifold Gauss-Bonnet (DGGW (5.7)). So the hypothesis S_0(g) = S_0(g')
  already forces chi^orb(O) = chi^orb(O'), and that condition in the "iff" is redundant.

### VC5 (finite-order obstruction): CONFIRMED in part

- Necessity: a_0 = chi^orb/6 + sum (m^2-1)/(12m), which is DGGW (5.7) together with Gauss-Bonnet. This is
  metric-independent, and per cone point it reduces to (m-1)^2/(12m) (checked exactly).
- The example works: both sides have a_0 = 2/3.
- Sufficiency is an existence argument, so it cannot be verified by computation. I looked for an obstruction
  and found none:
  - S_1 = (1/60pi) int K^2 dA >= pi chi^2/(15 Area) is only a lower bound. S_1 can be raised without limit on
    either orbifold, so it cannot block an equality.
  - For S_1..S_L, disjoint conformal bumps add exactly, since local integrals over disjoint supports add.
  - Their lambda^2 parts are proportional to F_{l+1} omega^{2l+2}. These vectors are Vandermonde-independent
    for distinct frequencies.
  - Placing bumps on g or on g' gives both signs, so any difference vector can be reached. Area can be fixed
    independently, for example with a flat cylinder or a bump with nonzero mean.
- No half-power or log terms occur for isolated cone points (DGGW Thm 4.8).

### VC6 (all-order obstruction): CONFIRMED in part (all checkable ingredients hold; construction sound)

- Hypotheses hold for (2,8,8)/(3,3,12) and (5,5,5)/(2,2,2,10). They also hold symbolically for the family
  (2k,8k,8k)/(3k,3k,12k). There are many more pairs, e.g. (2,15,20)/(3,4,30).
- At infinity the metric is |w|^{alpha_0 - 1} |h(w) dw| with h(0) = 1. This is an exact flat cone of angle
  2 pi alpha_0, with alpha_0 = sum(1 - 1/m_i) - 1. The values are 5/4 and 7/5, equal within each pair.
- So the same smooth rotationally symmetric cap can be glued into both. A cap exists for any alpha_0 > 0;
  when alpha_0 > 1 it has negative total curvature.
- Flat cone points contribute nothing at t^l for l >= 1 (b_l = 0 on flat germs, l = 1..5). This is also exact
  for flat R^2/Z_m.
- So a_l = S_l(cap) for l >= 1. a_0 matches because chi^orb and Psi_1 match. a_{-1} matches by homothety
  of the flat part before cutting.
- Handles for gamma >= 1 can be glued identically in a flat region.
- No hidden obstruction: every heat invariant of a closed orbifold with isolated cone points is a local
  integral or a cone term (DGGW Thm 4.8), with no half-powers or logs. Schueth 2511.22255 shows such terms
  only when f''(0) != 0, i.e. not for orbifold points.

### Lemma VC5a: values F_n CONFIRMED; SIGN CONVENTION BROKEN as typed for odd n

- `vc5a_formfactor.py` derives the lambda^2 form factor from scratch. It uses the second-order Duhamel term
  in Fourier space for Delta_g = e^{-2 sigma} P, where P = -(d1^2 + d2^2) >= 0.
- Its t^{n-1} coefficient is lambda^2 G_n int psi P^n psi with G_n = F_n/(2 pi) for n = 2..9, and
  F_n = (-1)^n n(n-1) n!/(2n+1)!:
  - F_2 = 1/30, which agrees with Berger's u_2 = K^2/15 - Delta K/15
  - F_3 = -1/140, which agrees with Gilkey a_6 (Vassilevich (4.29)), where the 2D integrated quadratic part
    is -(1/70) int |grad K|^2
  - F_4 = 1/1260 and F_5 = -1/16632
- Consistency checks: the t^-1 term equals the area term, and the t^0 quadratic part is 0 (Gauss-Bonnet).
- **Discrepancy:** the lemma writes (-Delta_0)^{l+1}, and the file's convention is Delta = -div grad. With that
  reading, (-Delta_0)^n = (-P)^n and the lemma has the wrong sign for every odd n (even l).
- Example, n = 3 (t^2): the true value is -lambda^2/(280 pi) int psi P^3 psi <= 0. The lemma as typed gives
  +lambda^2/(280 pi) int psi P^3 psi.
- The lemma is correct if -Delta_0 means the nonnegative flat Laplacian, i.e. Delta_0 = d1^2 + d2^2. That is
  the opposite of the header convention.
- Fix: write P^{l+1} with P = -div grad (equivalently Delta_0^{l+1} in the header convention). Then the
  quadratic part alternates in sign: S_1 is positive and S_2 is negative.
- Impact on VC5 is presumably harmless, since the spanning argument uses both signs. Any proof step that relies
  on the sign of an S_l change should be rechecked.

## Files (all in theory/varcurv/attack/)
- `twisted_duhamel.py` produces `twisted_duhamel_output.txt` (b_0..b_5 and radial invariants D1..D5)
- `vc_checks.py` produces `vc_checks_output.txt` (VC1, VC2, VC3, Schueth, Ucar)
- `vc456_checks.py` produces `vc456_checks_output.txt` (VC4, VC5 a_0, VC6 arithmetic and geometry)
- `nonradial_test.py` produces `nonradial_test_output.txt` (non-radial Z_2/Z_4 jets; m >= l-1 sharpness)
- `vc5a_formfactor.py` produces `vc5a_formfactor_output.txt` (F_n derivation, Berger, Gilkey/Vassilevich)
- `b4_invariants_output.txt` (b_4 in K, Delta K, Delta^2 K, Delta^3 K)
