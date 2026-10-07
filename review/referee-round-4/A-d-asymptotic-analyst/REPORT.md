<!-- Saved verbatim by the main session from the reviewer's returned text: the harness refused the reviewer's own write. Check scripts (check1.py..check8.py) and rendered pages are in its git-ignored scratch/. -->

# Referee report: "How much of a hyperbolic orbifold does heat hear?"

**Journal:** Annals of Global Analysis and Geometry
**Referee profile:** analyst (small-time heat expansions, trace formulas, explicit remainders, asymptotic versus convergent series, perturbation and stability estimates)
**Specific charge:** the heat-expansion appendix line by line (derivation, remainder and enveloping bounds), the stability section, and every proof that a main result depends on.
**Material read:** the 39-page manuscript and the 14-page supplement, as PDFs. I rendered and read page images at 110 dpi for pp. 2-4, 7-9, 11-12, 14, 17, 19, 22-23, 26-31, 33-34 of the manuscript, and also used `pdftotext -layout` for both files. The placeholders (author contributions, AI-use statement, Zenodo DOI) are treated as known and are not counted against the paper.

---

## Summary

The paper studies closed orientable hyperbolic 2-orbifolds whose singular points are cone points. It asks how many small-time heat invariants c_1, ..., c_k are needed to determine the signature (g; m_1, ..., m_n).

- **Analytic input.** From the Selberg trace formula (Thm 2.3, extended to the heat function in Lemma B.1) the paper derives a closed all-order formula for the cone contributions (Lemma 2.6, Prop. 2.7, eqs. (4)-(6)). The derivation goes through Phi_m(u) = (cot u - m cot mu)/(4m sin u). The j-th invariant adds exactly one new odd power sum P_{2j-3} (Lemma 2.10).
- **Main results.**
  - Theorem 1.1: floor(Area/pi) + 4 invariants always suffice. No area-independent number suffices. The worst-case count f(A) lies between c sqrt(A) and A/pi + 4, and linear growth is equivalent to N(k) = O(k) for the Prouhet-Tarry-Escott function. With cone orders at most M, M invariants suffice and M is sharp.
  - Theorem 1.2: triangle orbifolds. Two invariants suffice up to cone-order sum 17. The first failure is O(2,8,8)/O(3,3,12), which is isolated via a rank-0 elliptic curve. Three invariants always suffice.
  - Theorem 1.3: stability of recovering the cone orders of a sphere from perturbed c_1, ..., c_n. Recovery is Lipschitz at simple orders and Hoelder 1/k at k-fold orders, with an explicit rounding threshold delta_thm.
- **Further material.** Section 4 locates the moduli-dependence in the geodesic term t^{-1/2} e^{-l^2/4t} (Thm 4.4). Section 7 and supplement S4-S6 compare the theory with finite-element spectra.

## Significance

- **Questions and connection.** The questions are natural and the answers are clean. The link between "how many heat invariants" and the Prouhet-Tarry-Escott problem (Thm 3.13, Prop. 3.14) is a genuinely new and attractive observation.
- **Bounded orders.** The bounded-order theorem (Thm 3.7) is the right structural explanation of the growth: large counts come from large cone orders, because the cone series has radius pi/m in u.
- **Triangle orbifolds.** The triangle-orbifold analysis answers precisely the remark in Dryden-Gordon-Greenwald-Webb [2, Rem. 5.16].
- **Analytic contribution.** This part is modest but tidy. It is a self-contained derivation of the full constant-curvature cone expansion in closed form, and an explicit, honest stability analysis of the algebraic inverse problem.
- **Fit to the journal.** The paper fits AGAG's scope (inverse spectral problems on orbifolds; cf. [8], [12], [13] published there).
- **Limitations, which the authors state.** These are statements about heat invariants, not spectra; the stability theory is for errors in the invariants, not in a measured trace.

## Correctness and what was recomputed

All scripts are in `scratch/` (`check1.py` to `check8.py`). They use sympy 1.14 (exact rational arithmetic) and mpmath 1.3 (30-40 digits), in a venv in `scratch/.venv`.

**1. Lemma 2.6 and eq. (4), p. 8.**
- I checked the closed form against the defining sum at u = 1/(10m), m = 2..9, to 40 digits.
- I checked the Taylor coefficients of the closed form against formula (4) exactly, for k <= 6 and m = 2..9.
- I re-derived the proof step by step: the partial-fraction identity, the residue cancellation in the Liouville argument, the Bernoulli expansion of cot u - m cot mu, and the sign convention sgn B_2n = (-1)^{n+1}. All are correct.

**2. Eq. (5), (7) and Lemma 2.8, p. 9.**
- p_0, p_1, p_2 reproduce (7) exactly.
- I also computed p_3 = m^8/10080 + m^6/3780 + m^4/2160 + m^2/945 - 19/10080.
- For l <= 7, deg p_l = 2l + 2, p_l(1) = 0, and the leading coefficient is |B_{2l+2}|/(2(l+1)!(2l+1)), exactly as stated. The displayed coefficient computation in the proof of Lemma 2.8 is correct.

**3. Smooth coefficients alpha_k, p. 9 and App. B, p. 34.**
- I re-derived alpha_k independently from I(t), using r tanh(pi r) = |r| - 2|r|/(e^{2pi|r|} + 1) and the moments mu_k = (1 - 2^{-2k-1})|B_{2k+2}|/(4(k+1)). The mu_k were also checked by quadrature for k <= 3.
- The result agrees exactly with the closed formula in Prop. 2.7 for k < 10: alpha_0..alpha_5 = 1, -1/3, 1/15, -4/315, 1/315, -4/3465.

**4. Appendix B line by line, p. 34.**
- The Euler beta integral: integral of F_a(r) e^{sr} dr = 1/(2 sin((a - s)/2)) for a - 2pi < s < a. The domination argument for differentiating under the integral is correct.
- The identity Sum_j m_{2k}(2 theta_j)/(2m sin theta_j) = d^{2k}/ds^{2k} Phi_m(s/2) at s = 0, which equals (2k)! phi_k/4^k. Correct.
- Multiplying by e^{-t/4} gives (5) with the stated signs. Correct.
- Lemma B.1 was checked step by step, and every step holds:
  - psi-hat >= cos(eps r) >= 1/2 for |r| <= 1;
  - h_T is the Fourier transform of 2 cos(Tu)(psi * psi), supported in [-2eps, 2eps] with 2eps < l;
  - the identity, elliptic and imaginary-r_j terms are O(T + 1), O(1), O(1);
  - #{lambda_j <= x} = O(x);
  - |f-hat_rho(r)| <= eps_rho min(1, |r|^{-3}), with Sum_j min(1, |r_j|^{-3}) < infinity;
  - dominated convergence on the geodesic side via Lemma 2.4.
- The elliptic term of Thm 2.3 matches Dryden-Strohmaier's eq. (1) in normalization. I fetched arXiv:math/0504571v2 and compared: the elliptic weight is 1/(2m sin theta) times the integral of e^{-2 theta r}/(1 + e^{-2 pi r}) h(r) dr, with theta = pi l/m. The geodesic weight is ln N(P_c)/(N^{1/2} - N^{-1/2}).

**5. Prop. 2.7 checked numerically against the trace formula itself.**
- I integrated E_m(t) of Thm 2.3 by quadrature (40 digits) for m = 2, 3, 8, 12 and t = 0.001, 0.005, 0.02, and subtracted the partial sums of Sum b_l(m) t^l for K = 1..6. The remainders decrease as predicted where the series is useful. For m = 12, t = 0.02 they start growing after K = 4, as expected from a divergent series.
- I did the same for I(t) at t = 0.001, 0.01, 0.05.
- **Enveloping property (not stated in the paper, but implied by its proof).** For G_m(t) = e^{t/4} E_m(t) and g_k = (-1)^k (2k)! phi_k(m)/(k! 4^k), the ratio (G_m - Sum_{k<K} g_k t^k)/(g_K t^K) lies in (0,1) for every K = 1..7 and m = 2, 3, 8, 12 at t = 0.005. See M1.
- I computed the coefficients of D(t) = Z_{(2,8,8)} - Z_{(3,3,12)} exactly. The results are d_3 = 25/12, d_4 = -1775/24, d_5 = 153025/48, c_2 = 67/48 for both, c_3 = -1601/480 and -867/160. All match p. 31, supplement S4 and Table S6.
- I also computed the exact elliptic difference D_ell(t) at t = 0.0015 ... 0.4. Its shape agrees with Fig. 8(a): maximum about 0.048 near t = 0.12, still about 0.043 at t = 0.4.
- **Growth of the cone coefficients.** |b_l(m)| / (l! (m/pi)^{2l}) times sqrt(l) tends to about 0.234 (m = 8) and 0.346 (m = 12) for l = 5..30. So "growing roughly like l!(m/pi)^{2l}" (pp. 5, 31) is right up to a factor l^{-1/2}.

**6. Lemma 2.4, Lemma 2.5 and constant (3), pp. 7-8.**
- I re-derived the counting bound: injectivity of class to translate via the Dirichlet domain at a free point, and the hyperbolic disc area 2 pi(cosh R - 1).
- I re-derived the bound on Hyp: 2 sinh(x/2) >= e^{x/2}(1 - e^{-l}) for x >= l; (log phi)' < 0 on the range; Stieltjes integration by parts with n_O(l-) = 0; the integral bounded by (2tl/(l - t)) e^{l/2 - l^2/4t}; and 1 + 2t/(l - t) <= (2 + 3l)/(2 + l) on the range.
- The logarithmic derivative of B in l is -1/2 - (l/2t - (1+l)/l) - e^{-l}/(1 - e^{-l}) - 2t/(l^2 - t^2), as printed, and is negative on the range.
- B(l, diam, t) and C(A, l, diam) are exactly as in (3). The monotonicity argument used in Thm 4.4(a) is valid.

**7. Thm 4.4(b), p. 21.**
- The leading term and the o(1) argument are correct. Starting the Lemma 2.5 argument at L' > L_* produces a boundary term -phi(L') n(L'-) <= 0, which only helps.
- I checked the geometry of the Fig. 4 family. With sinh a sinh b = cos(pi/3) = 1/2 (Lambert quadrilateral), the systole 4b equals 2.634 at theta = 0 and 0.694 at theta = 2.8, as stated on p. 21.

**8. Section 6, stability, pp. 27-30.**
- **Prop. 6.2.** I rebuilt F exactly. Row 2 of F^{-1} is (-18, -120, -360), matching the printed formula for P_3. The absolute row sums are amp_0..amp_5 = 2, 14, 498, 4062, 56230/3, 303654/5; the printed values go to amp_4.
- **Theorem B.** det M = (-1)^{n(n+1)/2} Prod(m_i + m_j)/e_n, and M e = b is solved by the true e. Both checked exactly on random integer multisets, n = 2..5.
- **zeta_n.** zeta_3 = 1, zeta_4 = 79/3, zeta_5 = 14048/15, recomputed exactly.
- **Theorem 6.4.** Checked step by step:
  - coefficientwise majorants U-hat <= n artanh w, |dU-hat| <= eta artanh w;
  - |T-tilde_k - T_k| <= eta t_k(n), via the tan majorant and the mean value theorem for sec^2;
  - the residual and perturbation bounds, and the Neumann-series factor 2.
  - Part (a) holds; Hadamard actually gives the exponent (n-1)/2 (see m5).
- **Theorem 6.5.** I re-derived the Rouche estimate: |q| >= r^{k_a} Pi-hat_a 2^{-(n-k_a)}, and |q-tilde - q| < 2^{1-n} 3^n eps for |z| <= 3/2. The inequality is strict even at r = r_a, so there is no boundary problem.
- **Theorem 6.8.** The third term is equivalent to r_a <= 1/2.
- **Table S4, delta_thm column.** I recomputed delta_thm(m) from the definitions for all eleven multisets. Every value agrees with the table to the printed digits; the printed values are rounded down. For example, (2,8,8) gives 3.803e-7 and (2,2,2,2,3) gives 2.730e-12. The largest exact cond is 3.5109, for (2,2,2,2,3), confirming "at most 3.511" (p. 28).
- **Props. 6.6(i) and 6.7.** The formulas dR = s^2/(4(64 - s^2)), dP_3 = 48 s^2 and Sum d_i^2(3a + d_i) >= 2a Sum d_i^2 were re-derived.
- **Supplement S3.** The sech^2 U series for (2,2,2,2,3) (p. 8) is correct: 1 - 121z^2 + 9328z^4 - 601472z^6.
- **Table S6.** Re-running the Theorem B recovery on the printed estimates reproduces the roots: 2, 8 +/- 0.00502i for A, and 2.99154, 3.00851, 11.99995 for B.

**9. Examples and constructions on which the main theorems rest (exact arithmetic).**
- Shared-invariant counts and areas:
  - Thm C(3): 2 and 3 shared invariants;
  - Ex. 3.6: 2;
  - Ex. 3.16(i)-(ii): 3;
  - Thm 3.7(ii) pairs for M = 3, 4: M - 1;
  - (0;5,5,5)/(0;2,2,2,10): 2;
  - (0;2^5)/(1;2): 1;
  - the Table S1 "cone count, L = 4" pair: 4.
- The P_5 values in Thm C(3) are correct.
- Thm 3.7(ii) checked for M = 3..7: the construction shares exactly M - 1 invariants, and c_M(g;m) - c_M(g';m') = (-1)^M C a_{M-2} (= -1/3, 1, -36, 700, -99504).
- Exhaustive enumeration of hyperbolic triads with S <= 60:
  - the only collision with S <= 18 is (2,8,8)/(3,3,12);
  - the next collisions are at S = 20, 26, 31;
  - there is no triple collision;
  - the first collision of non-adjacent strata is (5,15,15)/(7,7,21) at S = 35;
  - for k <= 6 the only triads with key_2 = (18k, 3/(4k)) are the two scaled ones.
- Thm 5.8 checked:
  - psi maps E into C_{27/2} (exact remainder 0) and phi o psi = id;
  - the twelve points lie on C_{27/2};
  - phi(1:4:4) = (-24, 360);
  - #E(F_7) = #E(F_11) = 12;
  - disc = 2^18 3^8 5^6;
  - the tangent y = 21x + 64 meets E at x = 16 with multiplicity 3.
  - I did not re-run the 2-descent of App. C by machine; I read it and found no error.
- By hand I checked the proofs of:
  - Thm A, Thm C(1)-(2), Lemma 2.10, Lemma 3.3, Thm 3.4, Cor. 3.5, Thm 3.7(i) and (iii), Cor. 3.8;
  - Thm 3.13(a)-(d), Prop. 3.14, Lemma A.1, Prop. A.2, Prop. 3.11;
  - Prop. 4.1, Cor. 4.3, and Thms 5.4-5.7 (the formula for phi_p - tau_p and the listed gaps).
  - In Thm 3.7(iii) the inequality chain (2L-3) log((L+1)/M) >= 2(2M+2k-3)(k+1)/(2M+k+1) > 2k >= lambda is correct.
  - I found no mathematical error.

**Overall.** In the parts I was charged with, every formula I recomputed is correct, and every proof I traced is complete. The issues below concern what the analytic part does *not* yet say. They do not concern errors.

---

## MAJOR issues

**M1. The expansion is stated only as "∼"; there is no remainder, so no theorem connects heat-trace data to the heat invariants that Theorem 1.3 takes as input.**
(Prop. 2.7, p. 9; App. B, p. 34; Thm 1.3 and the sentence before it, p. 4; Sec. 1.1, p. 5; Sec. 7, p. 31; supplement S4-S5.)

- **What the paper does.** It motivates Theorem 1.3 with "A measured heat trace is never exact" (p. 4). It interprets its counts through the claim that "the expansion describes the heat trace only for t small compared with (pi/m)^2" (p. 5). It speaks of "two timescales" in Sec. 7, and recovers c_1, c_2, c_3 from computed traces by polynomial least squares with heuristic error bars (S4, S5).
- **What is missing.**
  - Prop. 2.7 gives no quantitative remainder.
  - Remark 6.1 and the sentence after Thm 1.3 acknowledge that the errors are in the invariants. However, none of the quantitative statements about traces is backed by a bound.
  - For a paper whose abstract says its results are "statements about short-time diffusion", this is the one analytic step a reader in this journal expects.
- **The remedy is nearly free, because the proof in Appendix B already yields an enveloping remainder.**
  - Write G_m(t) = e^{t/4} E_m(t) and g_k(m) = (-1)^k (2k)! phi_k(m)/(k! 4^k). Here phi_k(m) > 0 by (4).
  - Two facts give the bound: F_{2 theta_j} > 0 with positive weights 1/(2m sin theta_j), and the Taylor remainder of e^{-x} has sign (-1)^K with modulus at most x^K/K!.
  - Hence, for every K >= 0 and t > 0, G_m(t) - Sum_{k<K} g_k(m) t^k = theta g_K(m) t^K for some theta in [0,1].
  - The same holds for (4 pi/Area) t e^{t/4} I(t) with the positive moments mu_k.
  - I checked the enveloping property numerically (item 5 above).
  - Combined with Lemma 2.5, this gives a fully explicit two-sided bound for Z_O(t) minus its truncated expansion, valid for all t <= l^2/(2(1+l)).
- **Two consequences should be stated.**
  1. **Optimal truncation.** Since |b_l(m)| ~ C_m l^{-1/2} l! (m/pi)^{2l} (item 5), the optimally truncated error is of size about exp(-pi^2/(mu^2 t)), with mu the largest order. This turns the heuristic on p. 5 into a statement.
  2. **Geometric input.** Any rigorous extraction of c_1..c_n from Z on a window [t_0, t_1] requires an a-priori lower bound for the systole and an upper bound for the diameter, because the geodesic remainder (Lemma 2.5) depends on them and the invariants do not determine them. This structural limitation should be said explicitly next to Theorem 1.3. It is exactly why the blind recovery (S5) "validates but does not certify".
- **What would close the gap.** Ideally, a short lemma: if |Z_measured - Z| <= eps on [t_0, t_1], then |c-tilde_j - c_j| <= (explicit), with the stated geometric bounds. That lemma would make Theorem 1.3 applicable to trace data. Short of that, the motivation on p. 4 and the language of Sec. 7 should be toned down.

**M2. The a-posteriori use of Theorem 6.8 is asserted (Remark 6.1, p. 27; S5, p. 12 of the supplement) but not stated or proved as a result.**

- **The problem.** The constants of Theorems 6.4-6.8 (cond, r_n, Pi-hat_a, Xi_mu, delta_thm) are evaluated at the true, unknown orders. Remark 6.1 says one "recovers a candidate and checks the hypotheses of Theorem 6.8 there". As written, Theorem 6.8 applied at the candidate m* only says that data near c(m*) round to m*. That is not the needed conclusion, which is m_true = m*.
- **The argument that works.** Exact data c(m_true) are recovered exactly. This holds by Theorem A and Theorem B, since det M = ς_n Prod(m_i + m_j)/e_n is nonzero for positive orders. Hence, if |c(m_true) - c(m*)| <= delta_thm(m*), Theorem 6.8 applied at m* to the data c(m_true) forces m_true = m*.
- **The required hypothesis** is therefore delta_thm(m*) >= (distance from the data to c(m*)) + (a bound on the distance from the data to the true invariants). This is what S5 does ("radii equal to the distance ... plus the error bars"). Remark 6.1's phrase "with delta covering the distance from the data to its exact invariants" is ambiguous on exactly this point.
- **Request.** State and prove this as a corollary (a few lines). It is what Theorem 1.3 means by "used a posteriori". The same corollary should be noted for the certificate of Proposition S3.1.

**M3. The statement of Theorem 1.3 (p. 4) is broader than what Section 6 proves.**

- **The problem.** "for data that are heat invariants of positive real orders it is 1/2, and attained, at a double order and when all n >= 3 orders are equal". This can be read as asserting exponent 1/2 for all realisable data. Section 6 says explicitly that only the double-order case (Thm 6.5 together with Prop. 6.6(i)) and the all-equal case (Prop. 6.7) are settled, and that "other configurations are not settled" (p. 29; also "mixed clusters are not settled", p. 30).
- **Request.** Since this is a headline theorem, the statement must match. Suggested wording: "...; for data that are heat invariants of positive real orders, the exponent is 1/2 at a double order and when all n >= 3 orders are equal, and is attained there; other configurations are open."

## MINOR issues

- **m1 (p. 31, Sec. 7; supplement p. 11, "Prediction").** "D(t) = Sum_{j>=3} d_j t^{j-2}" must be "∼". The authors themselves say two lines later that the series diverges, with coefficients growing like l!(144/pi^2)^l, and Fig. 8(a) shows the truncations failing. The same applies to any other place where the expansion is written with "=" (I found only these two).
- **m2 (p. 31; supplement S4(ii), p. 10).**
  - "each trace agrees with I + E to 7 x 10^{-13} for 0.0015 <= t <= 0.03" and "the computed D agrees with the exact difference of the elliptic terms to 4 x 10^{-13}" both include t = 0.03.
  - At t = 0.03 the shortest closed geodesic of O(3,3,12) (l = 1.8626, two orientations, as found in S4) contributes Hyp ≈ 7.8 x 10^{-13}. At t = 0.025 it contributes 2.6 x 10^{-15}. For O(2,8,8), at t = 0.03 it contributes 1 x 10^{-18}.
  - So at the end of the window the term the comparison omits is as large as the agreement claimed, and about twice the 4 x 10^{-13} claimed for D. This is within the stated error budget (1.5 x 10^{-11}), so nothing is wrong. However, the comparison should be with I + E + Hyp, or the window should stop at t = 0.025, and the "less than 10^{-12}" remark should be made quantitative.
- **m3 (p. 5 and p. 31).** "coefficients grow roughly like l!(m/pi)^{2l}": the precise behaviour is C_m l^{-1/2} l! (m/pi)^{2l} (item 5). It follows in two lines from the simple poles of Phi_m at u = ±pi/m. State it, and the resulting optimal-truncation scale (see M1).
- **m4 (Lemma 2.5, p. 8; Thm 4.4(b) proof, p. 22).**
  - Lemma 2.5: say explicitly that the integration by parts uses n_O(l-) = 0.
  - Thm 4.4(b): when the argument is rerun from L' > L_*, the boundary term -phi(L') n(L'-) is nonpositive and may be dropped. Both points are easy but silent.
- **m5 (Thm 6.4(a) and proof, p. 28).**
  - The parenthetical "(whose columns contain ê_0 = 1 or ê_1 >= 1)" plays no role in an upper bound via Hadamard's inequality; delete or explain it.
  - The column-norm bound used is Sum_l ê_l^2 <= Sum_l C(n,l)^2 = C(2n,n). Say so.
  - The cofactors are (n-1) x (n-1), so the exponent n/2 can be (n-1)/2.
- **m6 (Thm 6.5, p. 29).** Give the range of r in the definition of Xi_mu explicitly (1 <= r <= n-1) and the range of j in delta (j <= n).
- **m7 (Thm 1.1(iii), p. 3; Thm 3.7(iii), p. 14; Cor. 3.8, p. 15).**
  - "log" is the natural logarithm (|U| <= e^lambda in the proof); say so.
  - Cor. 3.8(b) speaks of the "largest cone order" of O, which is undefined when n = 0. Add "if O has a cone point" or a convention.
- **m8 (Lemma B.1, p. 34).**
  - "the finitely many imaginary r_j contribute O(1)": note that h_T(iy) = 2 Re(psi-hat(iy - T)^2) is real and bounded, so the counting inequality concerns only the nonnegative terms from real r_j. State that eigenvalues are counted with multiplicity.
  - Theorem 2.3 asserts absolute convergence of all series; this follows from the counting estimate and Lemma 2.4, so reference them there.
- **m9 (App. B, p. 34).** Once the remainder of M1 is stated, Proposition 2.7 should cite it. Without it, the sentence "|e^{-x} - ...| <= x^K/K! gives ∼" hides that the proof gives more.
- **m10 (Remark 6.1, p. 27).** Also make explicit that cond, r_n and Pi-hat_a are evaluated at the true orders (they are, by definition) and are therefore not known in practice. This is the reason for M2.
- **m11 (p. 3, non-orientable paragraph).** The claim that a cone-point orbifold on a non-orientable surface shares every heat invariant with its orientable counterpart is correct. However, the justification ("heat invariants are local") should add one line: in the trace formula for the non-orientable group, the extra glide-reflection classes contribute only terms of order e^{-c/t}. Otherwise a reader may wonder why orientation-reversing elements do not contribute.
- **m12 (Prop. 6.7, p. 29).** The proof uses only c_1, c_2, c_3 (amp_1 = 14, amp_2 = 498). Say that this is why n >= 3 is needed, and that the bound holds for every delta, with no smallness assumption. Both points are true but implicit.

## Presentation (figures and captions included)

- **Writing.** The paper is unusually well written, compact and careful about attribution. In particular the precedent discussion in Sections 1.1-1.2 is careful.
- **Notation.** Notation is consistent. The heat kernel is in fraktur in Fig. 1 and on p. 4, distinct from the spectral function h_t of Thm 2.3. That is good, but worth one sentence, since both are called h.
- **Fig. 1 (p. 2).** Colours are consistent with the claim that 4 pi t (heat kernel)(x,x) approaches the order at a cone point: the tips of order 8, 8 (a) and 12 (b) are darkest, and the orders 2 and 3 are orange. Fine.
- **Fig. 2 (p. 14).** I checked discs and rings against X* for both pairs; they are correct.
- **Fig. 3 (p. 19).**
  - The step curves agree with Cor. 3.5, i.e. floor(2s) + 4, and with Thm 3.13(a), i.e. floor(sqrt((s-1)/3)) + 2 from s = 4.
  - The Prouhet squares sit at s = 12/5, about 15, 63, 255, 1023 with K_mult = L + 1, as in Table S1.
  - The caption should define the markers (dots, filled diamonds, open squares, split disc) and the two step curves. At present only the text does.
- **Fig. 6 (p. 26).** I verified the dots and circles against Table S2: S* = 18, 19, 20, 23, 26, 29, and first collisions at 18, 38, 20, 117, 34, 62 for p = 2..7. Fine. The caption could say that the split disc is the minimal pair.
- **Fig. 7 (p. 30).**
  - The slopes I read off are 1, 1/2, 1/3 and 1/2, as stated.
  - The diamonds sit at about 4.5e-4, 2.3e-3 and 3.7e-3, consistent with delta_cert in Table S4.
  - The caption does not say which line is which (solid (2,3,7), heavy (2,8,8), dashed (4,4,4), dotted realisable data near (4,4,4)), nor what the diamonds and the horizontal line are. Move this from the text into the caption.
- **Fig. 8 (p. 31).**
  - Panel (a) agrees with my computation of the elliptic difference.
  - The caption should identify the heavy curve (computed D), the dashed curve (cone-point term) and the three grey truncations.
  - In (b), it should identify the shaded error budget and the circles.
  - The t-axis label appears only under (b); add it under (a) or share the axis explicitly.
- **Section 7.** Section 7 is very compressed and relies on S4-S6 for every number. Given M1, it would profit from one displayed inequality (the remainder) against which Fig. 8(a) can be read.
- **Typography.** I found no typographical, sign or figure error on the rendered pages I read. The extracted text garbles fractions, but the page images are correct.

## Recommendation

**Minor revision.**

- **Confidence.** High for Sections 2, 4 and 6, Appendices A-B and the stability material, all of which I recomputed. Moderate-to-high for the number-theoretic Sections 3 and 5, where I verified every example and construction exactly and traced the proofs, but did not machine-check the 2-descent of Appendix C or the large searches. Those are, correctly, not used in proofs.
- **Why minor.** The three "major" items are major in importance for how the analytic results are framed, not in the amount of work. M1 needs one proposition with a half-page proof, already implicit in Appendix B, plus optionally an extraction lemma or a softened motivation. M2 needs one corollary. M3 needs one sentence. I found no mathematical error.

## What resolves each issue

- **M1:** Add, after Prop. 2.7, a proposition with the explicit enveloping remainder for e^{t/4}E_m and for the identity term (proof: positivity of F_a and of the moment weights, plus the alternating Taylor remainder of e^{-x}). Combine it with Lemma 2.5 into an explicit bound for |Z_O(t) - truncation|. Then do one of two things: either state a lemma bounding errors in c_1..c_n by an error bound on Z over a window, given a systole lower bound and a diameter upper bound; or reword p. 4 ("A measured heat trace...") and Sec. 7 so that Theorem 1.3 is not presented as applying to trace data. State the optimal-truncation scale exp(-pi^2/(mu^2 t)) in place of the heuristic on p. 5.
- **M2:** State and prove the a-posteriori corollary: exact recovery at the true orders, plus |c(m_true) - c(m*)| <= delta_thm(m*), implies m_true = m*. State the required hypothesis on the data error. Reference it in Remark 6.1, Thm 1.3, S3 and S5.
- **M3:** Reword the last sentence of Thm 1.3 as suggested, matching p. 29-30.
- **m1:** Replace "=" by "∼" on p. 31 and in S4 "Prediction".
- **m2:** Compare with I + E + Hyp, or end the window at t = 0.025, and quote the size of Hyp at the window end.
- **m3:** State |b_l(m)| ~ C_m l^{-1/2} l! (m/pi)^{2l} with the two-line derivation.
- **m4:** Add the two one-line justifications (n_O(l-) = 0; the sign of the boundary term).
- **m5:** Delete or explain the parenthetical, state the column-norm bound, and optionally improve the exponent to (n-1)/2.
- **m6:** Add the index ranges in Thm 6.5.
- **m7:** Specify natural log; add the n >= 1 proviso in Cor. 3.8(b).
- **m8:** Add the remark on h_T(iy) and multiplicities, and the reference for absolute convergence in Thm 2.3.
- **m9:** Cite the new remainder proposition in the proof of Prop. 2.7.
- **m10:** One sentence in Remark 6.1.
- **m11:** One sentence on glide reflections contributing O(e^{-c/t}).
- **m12:** One sentence in Prop. 6.7.
- **Presentation:** Expand the captions of Figs. 3, 7 and 8 as described, and add the t-axis to Fig. 8(a).
