<!-- Saved verbatim by the main session from the final message of reviewer A-d: the harness refused the reviewer's own write. Text from the report's first heading on; the reviewer's preceding cover note was dropped. -->
# Referee report: "How much of a hyperbolic orbifold does heat hear?" (Annals of Global Analysis and Geometry)

Referee remit: Appendices A and B; Sections 4, 5 and 6; and every proof that Theorem 1.1, Theorems 1.2–1.4 and Corollary 1.5 depend on, including Sections 2.1–2.4, 3.1–3.4 and supplement Sections S2, S3 and S7. I read the PDF and supplement as text and also read rendered page images of pp. 2–3, 8, 12, 18, 22, 24, 26, 28–30, 32, 35 and 39, plus high-resolution crops of Figures 1, 7 and Theorem 5.8. My scripts use exact rational arithmetic (sympy/fractions), with mpmath at 40 digits for the integrals.

## Summary

The paper studies closed orientable hyperbolic 2-orbifolds with cone points. It asks for the least number K_mult of heat invariants c_1, c_2, ... that separates the signature (genus and cone orders) of a given orbifold from all other signatures, and how the worst case f(A) grows with the area A.

The analytic input comes from the Selberg trace formula:
- Appendix B derives the full constant-curvature heat expansion (Proposition 2.7).
- The truncations come with enveloping (alternating-sign) remainders (Proposition B.2).
- The hyperbolic term is bounded explicitly (Lemmas 2.4–2.5).
- Lemma 2.10 records the triangular structure: each new coefficient adds one new odd power sum of the cone orders.

Everything else is a moment problem for signed multisets:
- a mirror-symmetry argument (Theorem 3.4), which gives the area bound ⌊A/π⌋+4 (Corollary 3.5);
- a sign-change/Descartes argument, which gives the exact area-free answer M+1 for cone orders at most M (Theorem 3.8) and the genus cost (Theorem 3.11);
- a reduction of the growth of f to the Prouhet–Tarry–Escott (PTE) function N(k) (Theorem 3.14, Proposition 3.15).

For triangle orbifolds (Section 5):
- three invariants always suffice;
- O(2,8,8) and O(3,3,12) form the minimal collision;
- this pair is isolated because C_{27/2} is a rank-0 elliptic curve with 12 rational points.

Section 6 gives Lipschitz/Hölder stability of the algebraic inverse map (c_1..c_n) → orders, with explicit thresholds. Section 4 records what the heat trace hears only beyond all orders.

## Significance

The question is natural and the answer is clean:
- M+1 invariants suffice, independently of the area, when orders are at most M;
- without that bound the count grows at least like √A and at most linearly;
- power-law growth f ≍ A^α is equivalent to N(k) = O(k^{1/α}).

The equivalence with an open Diophantine problem is a genuine contribution, not a decoration: Proposition 3.15 pins f to the inverse of the minimal configuration size T(L), which sits within constant factors of N.

The triangle-orbifold section makes precise a remark of Dryden–Gordon–Greenwald–Webb, and the elliptic-curve isolation is pleasing. The stability section is careful about what is proved (heat-invariant data, true orders) versus what is only illustrated.

The variable-curvature Section 2.4 is the weakest part (M1 below). The mathematics in my remit is otherwise correct as far as I could check, and it is unusually reproducible.

## Correctness and what was recomputed

Every item below agreed with the paper unless flagged.

1. **Closed form and coefficients (Lemma 2.6, Proposition 2.7, Lemma 2.8, (8)).**
   - Checked the Taylor coefficients of Φ_m against (4) numerically (m = 5, k ≤ 3), and the closed form Φ_m = (cot u − m cot mu)/(4m sin u).
   - Built p_l from (4)–(5) for l ≤ 4. Each is even of degree 2l+2, with p_l(1) = 0 and leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)).
   - p_0, p_1, p_2 agree with (8).
   - α_0..α_5 = 1, −1/3, 1/15, −4/315, 1/315, −4/3465, both from the formula of Proposition 2.7 and from the μ_k recursion of Appendix B.
2. **Triangle coefficients and the minimal pair.**
   - (10) holds.
   - c_1 = 1/8 and c_2 = 67/48 for both orbifolds.
   - c_3 = −1601/480 and −867/160.
   - d_3 = 25/12, d_4 = −1775/24, d_5 = 153025/48 (and d_6 = −150503225/864).
   - Table S6 is reproduced: solving the triangle system at the printed estimates gives the roots 2, 8 ± 0.00502i and 2.99154, 3.00851, 11.99995.
3. **Enveloping remainders (Proposition B.2, (6)).** I computed E_m(t) and (4π/Area)·I(t) by quadrature at 40 digits for m ∈ {2,3,8,12}, t ∈ {0.002, 0.01, 0.05, 0.3} and K = 0..7. Every truncation remainder has the claimed sign (−1)^K (respectively (−1)^{K+1}) and modulus at most |b_K(m)| t^K (respectively |α_{K+1}| t^K).
   - |b_K(m)| increases in m.
   - |b_l(m)| / (l^{−1/2} l! (m/π)^{2l}) converges (about 0.105 for m = 3 and 0.233 for m = 8), which confirms the growth law stated in Section 4.
4. **Analytic steps checked by hand.**
   - Trace formula for the heat function (Theorem 2.3 with Lemma B.1): the Fejér-type η_T counting argument, the dominated convergence and the imaginary-r_j terms.
   - Lemma 2.4: the Dirichlet-domain packing.
   - Lemma 2.5: both integrations by parts, the bound x/(x−t) ≤ ℓ/(ℓ−t), the formula for C_hyp at the endpoint t = ℓ²/(2(1+ℓ)), and the logarithmic derivative in ℓ.
   - Theorem 4.2: the reduction to the first differing length.
5. **Theorem B and Lemma S3.1.** I built M, b, B and Y explicitly for n = 2..6 at random rational multisets and at (2,8,8,3)-prefixes.
   - The true e solves Me = b.
   - det M = (−1)^{n(n+1)/2} ∏_{i<j}(m_i+m_j)/∏m_i, exactly.
   - B = YM and det B = (−1)^{n(n−1)/2} ∏_{i<j}(m_i+m_j).
6. **Proposition 6.1 and Section 6 constants.**
   - F^{−1} has rows (−2), (2,12), (−18,−120,−360), ..., giving amp_0..amp_4 = 2, 14, 498, 4062, 56230/3. P_3 = −18c̃_1 − 120c̃_2 − 360c̃_3 is confirmed.
   - ζ_3 = 1, ζ_4 = 79/3, ζ_5 = 14048/15.
   - I recomputed δ_thm of Theorem S3.4 for all eleven multisets of Table S4. All agree to the stated rounding (e.g. 3.80e−7, 1.19e−7, 4.02e−11, 2.73e−12 versus printed 2.72e−12, "rounded down"). The exact cond is ≤ 3.511, as stated.
   - I checked by hand the Rouché bookkeeping of Theorem S3.3, the Neumann-series step of S3.2(b) and the v > 0 spectral-radius argument of Proposition S3.5.
   - Proposition 6.3(i) values and the proof of Proposition 6.4 are correct.
7. **Section 3.**
   - Proofs checked line by line: Theorem A (support argument), Theorem C(1)–(2), Lemma 3.3 (padding identities), Theorem 3.4, Corollary 3.5, Lemma 3.7, Theorem 3.8(i)–(iv) (Lagrange weights, signs, area bookkeeping), Corollary 3.9, Theorem 3.11 (Descartes count), Proposition 3.12 (including hyperbolicity for n = 2), Lemma 3.16, Lemma A.1 (pigeonhole), Proposition A.2, Theorem 3.14(a)–(d), Proposition 3.15, and the o(A) equivalence (using monotonicity of A_min in L).
   - Exact recomputations:
     - The power sums of Theorem C(3): P_3 = 1032 / 1782; P_5 = 25159618 / 21298618.
     - Examples 3.6, 3.17 and the pairs in Theorems 1.2(ii) and 3.8. These are (0;2^10)/(1;4^4), (2;)/(0;2^8), (1;3^9)/(0;2^16), (0;2^28,4^8)/(1;3^27), (0;5,5,5)/(0;2,2,2,10) and (0;2^5)/(1;2).
     - The least-g areas of Theorem 3.8(ii) for M = 2..9 are 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054}; each pair shares exactly M−1 invariants.
     - Theorem 3.8(iv) for (M,X) = (2,4), (3,5), (4,7): exactly M shared, with C = 180, 40320, 19958400. For X = M+1 it reduces to (ii) with sides exchanged.
     - The sign of c_M − c'_M in (ii) for M = 3: it is −1/3 = (−1)^3·120·a_1.
   - Table S1: I parsed all 20 printed signature pairs and recomputed the area and the exact number of shared invariants. All match the stated L. |U\*|+|V\*| = 14, 18, 24, 40 (equal count) and 16, 20, 26, 40 (genus) match Example 3.17(iii) and the table of upper bounds. The four exact areas printed for L = 4, 5 match.
   - The real partner triple of {1,1,1,1,7} in Remark 3.18 is reproduced (0.26636, 4.28304, 6.45060).
8. **Section 5.**
   - Enumerated all hyperbolic triads with sum S ≤ 600. There are 83 with 10 ≤ S ≤ 18, and the only coincidence of R among them is (2,8,8), (3,3,12).
   - The collision-free sums up to 600 are exactly the 38 sums of Proposition S2.1 (the last is 557).
   - The first adjacent-stratum collisions for p = 2..14 agree with Table S2.
   - Brute-force overlap of adjacent strata for p < 60 agrees with S\*(p) of Theorem 5.4 with no exception.
   - gap_p(3p+7) formula holds for p < 200.
   - gap values: 1/840, 1/2310, 1/10296, and the seven negative values in step (d).
   - The only zero gaps for p < 400 are (2,18) and (4,20) (Proposition S2.2).
   - x\*(p) − 18 = 3(p−2)(p−3)/(p−1).
9. **Theorem 5.8.**
   - ψ maps E into C_{27/2} (exact reduction modulo the curve equation), and φ∘ψ = id with φ exactly as printed.
   - Δ = 2^18·3^8·5^6.
   - The flex: x³+393x²+3456x − (21x+64)² = (x−16)³.
   - #E(F_7) = #E(F_11) = 12.
   - The eleven affine points lie on E and have orders 2, 2, 2, 3, 3, 6 × 6 (the six non-flex points have order 6).
   - The twelve points of C_{27/2} are as listed, and ψ of the torsion points gives them.
   - The hand 2-isogeny descent of S7 was checked step by step: the quadratic non-residue arguments mod 5 on E, and mod 3 and mod 9 on E′ (including 5w²−w+2 ≡ 6 mod 9 for w ∈ {1,4,7}). Rank 0 follows.
10. **Section 2.4 consistency checks** (not proofs):
    - The K³ term of 2.11(iv) equals p_3(m)/m, with p_3 = (m²−1)(m²+3)(3m⁴+2m²+19)/30240.
    - The Δ²K term equals Π_4(m) exactly, i.e. 2.11(iii) at l = 3.
    - The top coefficients of 2.11(iv) reproduce β_{3,4} = 120K³ − 42KΔK + Δ²K.
    - 4^l l! [v^{2l}](J^{−1})′ at K = −1 gives (2l)!/l!·K^l.
    - The linear term of 2.11(iii) at l = 2 reproduces Schueth's −m⁵ΔK/15120.
    - The flat-metric construction of 2.12(iii) checks out: Gauss–Bonnet for α_0, regularity at ∞, and equal Σ(m − 1/m) ⇒ equal c_2.
    - 2.12(ii) is verified on the example (0;2^8)/(0;3,3,3).

**Not recomputed:**
- The numerical spectra (S4–S6), Figures 4–5 data and the 525 complete area classes (Figure 3 dots).
- The n = 4/n = 5 searches and the Remark 3.18 search.
- Proposition 2.11(i)–(ii) beyond the consistency checks in item 10.
- Rank 0 via PARI/GP: an LMFDB lookup failed, so I rely on my own check of the hand descent.

## MAJOR issues

**M1. Section 2.4, Propositions 2.11 and 2.12 (pp. 11–14): stated as propositions but supported only by sketches and by a computation that cannot be reproduced. This is a gap in rigour, not an error.**
- **Proposition 2.11(i).** The key step "following the substitution of Schueth's proof … to all orders shows that (2 sin ϑ/2)^{2l+2}B_l is bounded" is asserted, not proved.
- **The hypothesis m ≥ l−1 in 2.11(i).** The step that removes non-radial jet terms ("its non-radial part has Taylor degree at least m and, for m ≥ l−1, cannot enter a rotation-invariant polynomial of weight 2l") is incomplete as written. A linear non-radial term can never be rotation-invariant. The real reason is that an invariant needs at least two non-radial factors, of total weight ≥ 2(m+2) > 2l. That is precisely where m ≥ l−1 comes from (compare Problem 5(b)), and it should be said.
- **Proposition 2.11(ii)–(iii).** These rest on a "Duhamel expansion" whose computation is not given.
- **Proposition 2.11(iv).** This is "an exact computation" that is confirmed "by an independent computation". Neither is in the paper or supplement, and S8 does not list it.
- **Proposition 2.12(ii).** This uses the second-order coefficient ω_n = (−1)^n n(n−1) n!/(2n+1)! without derivation or reference. Only its non-vanishing is needed, and that should be referenced to a standard source on quadratic parts of heat invariants.
- **Proposition 2.12(i).** This needs b_l(p) to be a universal polynomial in ∇^jK(p), which is 2.11(i) again.

All my consistency checks (item 10) passed, so I have no reason to doubt the statements. No main theorem depends on Section 2.4. However, the introduction (p. 3) and Section 2.4's own conclusions present it as established.

*Resolution:* Supply complete proofs, or a derivation of (iv) in the supplement with the computation listed in S8. Alternatively, mark 2.11(i)–(iv) and 2.12(ii) explicitly as results whose proofs are sketched (or as conjectural), and keep "Proposition" only for 2.12(iii). The sketch of 2.12(iii) is essentially complete and correct, and it is what the introduction uses.

**M2. The link from heat-trace data to heat-invariant data is asserted, not established (p. 40, last paragraph of Appendix B; p. 36, after Corollary 6.5; p. 33, opening of Section 6). This affects the scope of the stability claims, not their correctness.**

Theorem 6.2 and Corollary 6.5 are stated and proved for data that are approximate heat invariants; that part is correct. The paper then says that "(6) is the link between a heat trace and the heat invariants that Section 6 takes as data" and that δ_1 can be obtained "for instance from (6)". As stated, this is not usable, for three reasons:
- The remainder in (6) contains Σ_i|b_K(m_i)|, a function of the unknown orders. A bound needs an a priori upper bound μ_max on the cone orders. Proposition B.2(a) (monotonicity in m) makes that sufficient, but the assumption is not stated. It is exactly the quantity Section 6 is trying to recover.
- The hyperbolic term needs a priori bounds ℓ ≥ ℓ_0 and diam ≤ D.
- Extracting (c_1, ..., c_n) from finitely many samples Z(t_i) needs an extrapolation step, for example Lagrange/Vandermonde in t. Its conditioning grows rapidly with n and with the sampling window, which must lie below (π/μ_max)². No constant is given. The blind recovery of Section S5 uses heuristic least-squares error bars instead.

From an inverse-problems point of view, the theorem as proved is about the algebraic map c ↦ m. The paper should not suggest a quantitative statement from heat-trace data that it does not prove.

*Resolution:* Either
- (a) add a lemma: given Z(t_i) to accuracy ε at prescribed t_i, together with a priori bounds μ_max, ℓ_0, D and n, the invariants c_1..c_n are determined to explicit accuracy δ_1(ε, t_i, μ_max, ℓ_0, D). This follows from (6), Lemma 2.5 and an explicit Vandermonde inverse bound; or
- (b) rephrase the three passages to say that converting heat-trace data into heat-invariant data requires a priori bounds on the largest order, the systole and the diameter, plus an extrapolation step not analysed here.

## MINOR issues

- **m1. p. 30, Lemma 5.3(ii) proof (mathematical inaccuracy).** "For S ≥ 3p+3 the stratum p+1 contains its hyperbolic spread triad" is false at (p,S) = (2,9): (3,3,3) is not hyperbolic and stratum 3 is empty. Stratum 2 is also empty at S = 9, 10. The equivalence in (ii) survives, because gap_2(9) = 1/12 > 0 and gap_2(10) > 0, but the sentence should exclude this case or assume both strata nonempty.
- **m2. Terminology of "overlap" (pp. 30–31; Proposition S2.2; Figure 7 caption).** "Overlap" is defined as "convex hulls meet", which includes touching, and Theorem 5.4 counts S = 18 (p = 2) and S = 20 (p = 4) as overlaps. Page 31 then says the strata "touch without overlapping only for p = 2 and p = 4". Make the two uses consistent, e.g. "overlap (possibly only touching)".
- **m3. Proposition S2.2 proof (odd S−p case, supplement p. 7).** "positive at the last odd-parity sum below its zero and negative at the next … so it vanishes at no such sum" is circular as written. The clean argument is:
  - for p ≥ 9, the odd sums 3p+3 and 3p+5 lie below x\*(p);
  - gap_p(3p+7) ≠ 0, since p² − 5p − 30 has no integer root;
  - decrease from there on;
  - for p ≤ 8, a finite check.

  My computation confirms the statement for p < 400.
- **m4. p. 19, after Theorem 3.8.** "An exhaustive search finds no pair of smaller area with orders at most M sharing c_1, ..., c_{M−1} for M = 3, 4" is a search-only statement. It is neither described nor listed among "Statements that rest on computer search alone" in S8, against the paper's own stated policy.
- **m5. Theorem 6.2, p. 34 ("given by explicit formulas in m").** δ_0(m) and C_a(m) in Theorem S3.3 involve cond = ‖M(Î)^{−1}‖_∞. That is computable but is not a closed formula. Theorem S3.2(a) gives an explicit bound. State which one is meant, or define the constants with the bound of S3.2(a).
- **m6. Lemma A.1 (p. 37).** "with n ≤ (L−1)²+1, and with n ≤ N(2L−3)" reads as one pair satisfying both bounds. These are two separate constructions; rephrase as "… and also such multisets with n ≤ N(2L−3)".
- **m7. Proposition 3.15 (p. 22).** A_min(L) is defined as an infimum, and the proof uses "a pair of area A_min". Note that the infimum is attained, since the set of areas 2π(2g−2+Σ(1−1/m_i)) is well-ordered, or phrase the proof with areas A ↓ A_min.
- **m8. Section 4, Theorem 4.2(b) (p. 26).** "L\* = ℓ if ℓ_1 ≠ ℓ_2" is right. It is also worth saying that the leading coefficient is then ±w_i(ℓ)/(2 sinh(ℓ/2)) with w_i(ℓ) > 0, so the sign of the difference is determined. (Optional.)
- **m9. Corollary 6.5 / Section S5.** The certificate is applied with heuristic error bars for δ_1. The text says "validated, not certified", which is correct. Corollary 6.5 itself should carry the same caveat about δ_1 in its statement, not only in the paragraph after it.

## Presentation (figures, captions, notation, exposition)

I checked the rendered page images.
- **Figure 2** matches X\* and −X\* exactly in both panels (padding 1 in black in (b)).
- **Figure 7.** Dots at S\* = 19, 23, 26, 29 and circles at 38, 117, 34, 62 sit where Table S2 places them, and the split disc is at (18, 3/4).
- **Figure 8.** Slopes ≈ 1, 1/2, 1/3, 1/2.
- **Figure 5(a).** The truncation d_3t + d_4t² crosses zero near t = d_3/|d_4| ≈ 0.028, as drawn.
- **Figure 3.** The step curves match ⌊2s⌋+4 and ⌊√((s−1)/3)⌋+2.
- **Formulas.** The formulas of Theorem 1.1, Lemma 2.5, Proposition 2.11, Proposition 3.15, Theorem 5.4 and Theorem 5.8 render correctly. Several apparent errors in the extracted text, e.g. "23101" on p. 30 and the φ map, are artefacts of pdftotext; the rendered pages are correct.

Points to fix:
- **P1. Figure 1, p. 2.** At print size the order-12 cusp in panel (b) looks no darker than the order-3 corners. The near-black value is visible only under strong zoom, because the cusp is a few pixels wide. The text claims the darkest tips are the cone points of largest order. Enlarge or inset the cusps, or say in the caption that the extreme values occupy a region of size about √t at the tip.
- **P2. Figure 3 caption and text, p. 24.** The constructed pairs are "drawn at K_mult = L+1". For those orbifolds this is a lower bound (another partner could share more invariants). Write "K_mult ≥ L+1", or say that the diamonds and squares are lower bounds.
- **P3. Figure 8, p. 35.** The "worst-case error" is the maximum over the 2^n vertices of the error box, not over the box. Call it that, or justify why vertices suffice.
- **P4. Table 1 and Section 2.4.** Notation clash: B_l is the fixed-point coefficient in Section 2.4, B_{2l} are Bernoulli numbers, and B(ℓ, diam, t) is the bound of Lemma 2.5. The fraktur m_n(a) for moments in Appendix B sits next to m for cone orders. Consider renaming.
- **P5. Appendix B.** The final sentence of the proof of Proposition B.2(b), "These moduli are those of the terms of α_{K+1}", is correct but terse. One line matching the three groups of terms to the terms of α_{K+1} in the displayed formula would help.

## Recommendation

**Minor revision**, conditional on M1 and M2 being addressed by proof or by explicit restatement of status and scope.

I found no mathematical error in any result on which Theorem 1.1, Theorems 1.2–1.4 or Corollary 1.5 depends. Every value and constant I could recompute agrees with the paper:
- the heat coefficients and their enveloping remainders;
- the Hurwitz determinant;
- the amplification constants and δ_thm;
- the explicit pairs;
- the strata thresholds;
- the elliptic curve.

The two major points concern rigour and scope outside the main theorems: Section 2.4 is supported only by sketches, and the stability section implies a statement from heat-trace data that it does not prove.

Confidence:
- high for Appendices A and B, Sections 3, 5 and 6, and supplement S3/S7;
- moderate for Section 2.4, which I could only consistency-check;
- the numerical Sections 4/S4–S6 are, as the authors say, illustrations, and I did not re-run them.

## What resolves each issue

- **M1:** full proofs of Proposition 2.11(i)–(iv) and 2.12(ii), with the (iv) computation documented and listed in S8, the quadratic non-radial argument for m ≥ l−1 added, and a reference for ω_n ≠ 0. Alternatively, relabel these as sketched/conjectural statements, keeping 2.12(iii) (which is fine) as the result the introduction relies on.
- **M2:** a quantitative lemma from samples of Z(t) to (c_1..c_n) under stated a priori bounds (μ_max, ℓ_0, D, n), or rewording of the three passages so that no unproved heat-trace stability is implied.
- **m1:** exclude (p,S) = (2,9) in Lemma 5.3(ii), or assume both strata nonempty.
- **m2:** unify "overlap" and "touch".
- **m3:** replace the odd-parity argument in Proposition S2.2 with the explicit p ≥ 9 / p ≤ 8 argument.
- **m4:** describe the M = 3, 4 minimal-area search and list it in S8.
- **m5:** define δ_0 and C_a through the explicit bound of S3.2(a), or call them computable rather than explicit.
- **m6:** rephrase Lemma A.1.
- **m7:** note that A_min is attained (well-ordering), or adjust the proof.
- **m8:** optional sentence on the sign in Theorem 4.2(b).
- **m9:** put the δ_1 caveat into the statement of Corollary 6.5.
- **P1–P5:** figure and notation edits as listed.
