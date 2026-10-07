<!-- Provenance: reviewer (a) could not write files; this is its returned report text, saved verbatim by the orchestrating session (preamble line about the failed write removed). -->

# Referee report

**Manuscript:** "How much of a hyperbolic orbifold does heat hear?" (submitted to *The Journal of Geometric Analysis*), with its electronic supplementary material.

I treat the marked placeholders (author contributions, AI-use statement, Zenodo DOI) as known and do not count them as defects.

## 1. Summary

The paper studies the small-time heat invariants c_1, c_2, ... of closed orientable hyperbolic 2-orbifolds whose only singularities are cone points. It starts from the Selberg trace formula applied to the heat function, and re-derives in closed form the expansion found by Uçar: c_1 = Area/4π, and c_j adds Σ_i b_{j−2}(m_i), where b_l(m) = (−1)^l p_l(m)/m and p_l is an explicit even polynomial of degree 2l+2. A triangular change of basis shows that agreement of c_1, ..., c_L is the same as agreement of the area, of the reciprocal sum R, and of the odd power sums P_1, ..., P_{2L−3} of the cone orders. Comparing two orbifolds then becomes a symmetric (odd-power) Prouhet–Tarry–Escott problem for the signed multiset U* ⊎ (−V*).

The main results are as follows.

- **Theorem 1.1.** ⌊Area/π⌋+4 invariants always determine the genus and the cone orders, and no bound independent of the area exists. The worst-case count f(A) satisfies √A ≲ f(A) ≤ A/π+4, and f grows like A^α exactly when N(k) = O(k^{1/α}). Among spheres with n cone points, n invariants suffice, and n−1 do not (integer witnesses for n = 3, 4).
- **Theorem 1.2.** Among triangle orbifolds, c_1 and c_2 (equivalently, the DGGW invariant c) separate everything with order sum ≤ 17. They first fail on O(2,8,8) and O(3,3,12). This pair is isolated, through the rank-0 curve C_{27/2}, and c_3 always separates.
- **Section 4.** Heat invariants are functions of the signature. The authors give an explicit bound on the difference of the heat traces within one signature, of order t^{−1/2}e^{−ℓ²/4t}, and show that the leading term is attained.
- **Theorem 1.3 (Section 6).** For spheres with known n, the algebraic map from (c_1, ..., c_n) to the orders is Lipschitz at simple orders and Hölder-1/k at k-fold orders, with explicit thresholds for exact recovery after rounding.
- **Section 7 and the supplement.** FEM spectra of the minimal pair and of a (0;3,3,3,3) family illustrate the results, including a "blind" recovery.

## 2. Significance and novelty

I state my bias openly. I am not yet persuaded that "how many heat invariants are needed" matters for inverse spectral geometry, and the manuscript does too little to persuade me.

**What one actually has is the spectrum.** By Dryden–Strohmaier the spectrum determines the signature and the length spectrum, and by Doyle–Rossetti isospectral hyperbolic 2-orbifolds are even representation-equivalent. So in dimension 2 the full spectrum already gives everything that the heat invariants could give, and more.

**The heat invariants are not finite spectral data.** Not one c_j can be computed exactly from finitely many eigenvalues. Hence "the first k heat invariants" is not a natural notion of partial spectral information. Section 7 shows this: c_3 is obtained by a heuristic polynomial fit. The error model of Theorem 1.3, with errors in the heat invariants rather than in eigenvalues, has no clear operational meaning for someone holding a spectrum.

**Once Proposition 2.7 is in hand, the geometry is gone.** The question becomes the algebra of power sums. The cone contribution is a fixed function of the order only because the curvature is constant. In variable curvature (Schueth [38]) each cone point contributes curvature jets, and none of the counting results obviously survives. Every 2-dimensional isospectral construction (Sunada, transplantation, Linowitz–Voight [33]) produces pairs inside one signature. There the heat invariants are blind, so none of the collisions found here can ever be isospectral. The paper never says what its collisions mean spectrally.

That said, there is real content, and I want to be fair about it.

- **The explicit area bound ⌊Area/π⌋+4 (Corollary 3.5).** Its proof via the clean "mirror" argument of Theorem 3.4 is short. It is the first explicit count of this kind that I know of.
- **The two-sided link to the PTE function N(k) (Theorem 3.11).** It is a neat reformulation, honestly described as relocating the growth question.
- **The triangle-orbifold analysis (Theorem 1.2).** It is the most satisfying part of the paper. It gives a sharp threshold (sum 17), an exact first failure, and an arithmetic reason for the isolation of the minimal pair. It answers the DGGW remark on the invariant c.
- **The integer witnesses for n = 4 (Theorem C(3)), and Theorem C(1).** These are pleasant.

Much of the rest is classical or a repackaging.

- Theorem A is the symmetric PTE / Newton-identity argument with P_{2n−1} replaced by R.
- Theorem 3.4 follows from it immediately.
- Proposition 2.7 is Uçar's expansion, re-derived.
- Section 4 is Selberg–Huber–McKean. Its constant contains e^{3·diam}, which the authors themselves call qualitative and loose.
- Section 6 is a standard combination of a Hurwitz-type linear solve with Ostrowski/Rouché root perturbation.
- The cubics C_Λ come from Bremner–Guy–Nowakowski.

**On fit with JGA.** The geometric-analysis input is one classical formula. Most of the 37 + 12 pages are combinatorial number theory, root perturbation and numerics.

## 3. Correctness

I checked the mathematics independently, as far as my time allowed. I found **no mathematical error**. Everything I recomputed agrees with the manuscript.

**Heat expansion (Lemma 2.6, Proposition 2.7, Lemma 2.8, (7), (9)).**
- I computed p_l symbolically from (4)–(5) for l ≤ 7. p_0, p_1, p_2 agree with (7).
- p_l(1) = 0 and the leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)) hold for l ≤ 4.
- α_0..α_5 = 1, −1/3, 1/15, −4/315, 1/315, −4/3465, as stated.
- The closed form for Φ_12 checks numerically, and its Taylor coefficients equal φ_k(12) for k ≤ 4.
- **Independent test of the sign convention (−1)^l.** I evaluated the elliptic integral E_m(t) of Theorem 2.3 by 30-digit quadrature for m = 3, 8, 12 at t = 0.01 and 0.002. The differences from Σ_{l≤5} b_l t^l are of the size of the omitted t^6 term, for example 1.1×10⁻¹⁵ for m = 3, t = 0.002. The expansion is correct, signs included.
- c_2 reproduces the DGGW formula.
- For O(2,8,8) and O(3,3,12):
  - c_1 = 1/8;
  - c_2 = 67/48;
  - c_3 = −1601/480 and −867/160;
  - d_3, d_4, d_5 = 25/12, −1775/24, 153025/48, all as stated.

**Theorem B.** I checked two things for six multisets with n = 3 to 6:
- Me = b holds;
- det M = (−1)^{n(n+1)/2} Π_{i<j}(m_i+m_j)/Π m_i holds exactly.

**Theorem C(3).** R, P_1, P_3 and P_5 match: 3/4, 18, 1032/1782, and 8/15, 58, 31402, 25159618/21298618.

**Remark 3.2.** My own exhaustive exact C search over pairs of 4-multisets with equal (R, P_1, P_3) found:
- orders ≤ 130: 19 pairs, 16 primitive;
- orders ≤ 220: 53 pairs, 33 primitive.

Both agree with the supplement's 16 and 33.

**Section 6.**
- F⁻¹ has absolute row sums 2, 14, 498, 4062, 56230/3, and the P_3 row is (−18, −120, −360).
- ζ_3, ζ_4, ζ_5 = 1, 79/3, 14048/15.
- Proposition 6.6(i) and Remark 6.7 are correct.
- I re-evaluated δ_thm(2,8,8) from Theorem 6.8. With cond = 1, r_3 = 107/6 and Ξ_µ = 16, I get 3.8028×10⁻⁷, as in Table 1.
- Re-running the recovery chain on the Table S6 estimates gives exactly the reported roots: 2 and 8 ± 0.00502i; and 2.99154, 3.00851, 11.99995.

**Section 5.**
- Table S3 has 83 triads.
- **Table S2.** By brute force, every entry (p ≤ 14) is reproduced.
- **Theorem 5.4.** "Overlap iff S ≥ S*(p)" holds for p ≤ 30 and S < 400.
- All the exact gap values in its proof are correct.
- **Proposition 5.8.** Tangencies occur exactly at (2,18) and (4,20).
- **Proposition 5.9.** My own exact C enumeration over all sums up to 4800 (scaling from divisors, otherwise a full sort of R) found collision-free sums exactly at S ≤ 17 and the 38 listed sums, with S = 557 having 25 575 triads.

**Theorem 5.10.** With PARI/GP (cypari2):
- E: y² = x(x+9)(x+384) has discriminant 2¹⁸3⁸5⁶ and conductor 90.
- ellrank gives [0,0], so the rank is provably 0, and the analytic rank is 0.
- E(Q)_tors ≅ Z/6×Z/2, and #E(F_7) = #E(F_11) = 12.

Symbolically, ψ maps E into C_{27/2} and φ∘ψ = id. The 12 rational points map to the 12 listed points, and the positive ones are the permutations of (1:4:4) and (1:1:4).

**Table S1.** From the heat invariants directly, I recomputed exactly all 20 explicitly printed pairs: genus, equal-count and cone-count pairs for L = 2..7, and Prouhet pairs for L = 2, 3. The shared count is exactly the claimed L, and the areas match the column s. I also checked the following:
- Example 3.6;
- (0;5,5,5) against (0;2,2,2,10);
- Example 3.12(ii);
- the partner triple of {1,1,1,1,7};
- the search sizes 216,071,394 and 4,325,115,770.

**Proofs read line by line.** These were Theorems A, B, C, 3.4, 3.8, 3.11 with Appendix B, Corollary 3.5, Proposition 3.9, Lemmas 2.4, 2.5 (including the constant (3)) and A.1, and Theorems 4.4 and 4.5. I found them correct but sometimes too compressed (M4).

**The family of Figure 4.** The systoles 4b run from 2.634 to 0.694, and ρ_1ρ_2 at adjacent cone points has translation length 4b, so the systole claim is consistent.

**Not recomputed:**
- the FEM spectra;
- the 525 classes of Figure 3;
- δ_cert, δ_up and the other δ_thm rows;
- the n = 5 search;
- the T_3 search.

## 4. MAJOR issues

**M1. The question needs a justification for inverse spectral geometry (Introduction, §1.1, Remark 4.7).**

*Why it matters.*
- The spectrum already determines the signature, and the heat invariants cannot be computed from any finite part of it.
- Within a signature, where every 2-dimensional isospectral pair lives, the heat invariants are blind.
- So the title's question has a classical answer, "the signature" (Proposition 4.1). The new content is a count.

*What would resolve it.* A section that does the following:
- states what the count tells someone who holds a spectrum;
- reformulates in terms of the t = 0 wave-trace singularity, as opposed to the length-spectrum singularities;
- states that no exhibited pair is isospectral, and why;
- discusses variable curvature (Schueth [38]) or unknown K < 0, where local invariants are all one has.

Otherwise, reposition the paper as a paper on odd-power PTE systems, and retitle it.

**M2. Orientability of the underlying surface (definition of Sig, Theorem 1.1(i)).**

*Why it matters.*
- Non-orientable underlying surfaces with cone points are locally orientable, so the cited Richardson–Stanhope result does not exclude them.
- They have the same heat expansion, with χ = 2 − k for k cross-caps.
- Heat invariants therefore cannot tell whether the underlying surface is orientable.
- Bérard–Webb ("One cannot hear orientability of surfaces", C. R. Acad. Sci. Paris 320 (1995); Math. Z. 300 (2022)) show by Sunada-type methods that orientability is not in general a spectral invariant at all.
- The restriction "among all closed orientable ..." therefore hides a real phenomenon.

*What would resolve it.* Either extend Theorem 1.1 and Section 3 to all locally orientable orbifolds, determining (χ, cone orders), which looks nearly free from Lemma 3.3. Or justify the restriction with a discussion of Bérard–Webb.

**M3. Focus and length (Sections 4, 6, 7, supplement).**

*Why it matters.*
- Section 4 is classical by the authors' own account, and Theorem 4.4's constant e^{3·diam} is "qualitative".
- Section 6 uses an artificial error model, with constants evaluated at the unknown true orders.
- Table 1's δ_cert rests on Proposition S3.1, which is proved only in the supplement.
- Section 7 and Sections S4–S6 are illustrations with heuristic error bars. Eigenvalues above 1.6×10⁴ are untested, and the double-window recomputation "has not been run".
- The core results are buried.

*What would resolve it.*
- Reduce Section 4 to a remark, or make Theorem 4.4's constants depend only on the signature and the systole.
- Cut Section 6 to the qualitative statement.
- Prove Proposition S3.1 in the paper, or drop δ_cert from the main text.
- Move Section 7 to the supplement.

**M4. Several proofs are too compressed to check without redoing them.** The statements are all correct (I verified them numerically), but the following need to be written out.
- **Theorem B, determinant.** The sign collection, the "dense set" argument, and ∂T_k/∂P_l need a displayed computation. A cleaner route may be to prove det B via Lemma 6.3 and deduce det M.
- **Theorem 3.8.** The Descartes sign-change bookkeeping needs to be spelled out. It is the only genuinely new inequality in §3.3.
- **Theorem C(2).** Display the rank-(n−1) matrix.
- **Lemma 2.5.** Treat the boundary term at ℓ in the integration by parts.
- **Proposition 6.6(ii).** "Invertibility persists for small s" needs its quantitative input.

**M5. State the growth result at its true strength (abstract, Theorems 1.1(ii) and 3.11).** The equivalence "f(A) ≥ cA^α iff N(k) ≤ Ck^{1/α}" is correct. But it is a dictionary between two quantities neither of which is known up to the exponent, and the unconditional content is only √A ≲ f ≲ A.

*What would resolve it.* Say in the abstract that the exponent is undetermined, between 1/2 and 1. Comment on the constructed pairs, which lie above the dashed pigeonhole bound in Figure 3.

## 5. MINOR issues

1. **Abstract and Theorem 1.1(iii).** "For spheres with n cone points, n invariants suffice" should say "among spheres with the same n". By Theorem 3.10, Kmult(O; Sig_0) can exceed n.
2. **Theorem 5.1 and Theorem 1.2.** K_iso on Sig_{0,3} takes the values 1, 2 and 3. For instance, O(2,3,7), which has the largest R < 1, is determined by c_1 alone. Give the distribution.
3. **Proposition 4.2.** Troyanov's theorem is unnecessary: a hyperbolic triangle is determined by its angles.
4. **Remark 2.11.** If the curvature is unknown, c_1 gives Area·K and an extra unknown enters. Comment on this.
5. **Remark 2.9.** "Compared exactly for l ≤ 40" needs a pointer to the code.
6. **Table 1 caption.** Flag that δ_cert relies on a result proved in the ESM.
7. **Theorem 1.3.** Separate the upper bound (Theorem 6.5 / Remark 6.7) from the lower bound (Proposition 6.6(i)) in the "1/2, and sharp" sentence.
8. **Appendix C.**
   - Internal-looking paths (`review/audit-2/...`, `review/round1-fixes/...`, `theory/revision/...`) should be cleaned out.
   - The repository account (`Ali-M658`) matches none of the authors; make the Zenodo archive the reference of record.
   - For the T_3 floating-point filter, state the arithmetic format, the rounding mode and the platform. Its rigour can depend on the platform, for example on the width of `long double`.
9. **Table S1 (supplement p. 5).**
   - The Prouhet L = 6 area prints as "1023 − 0.00 × 10⁰", because the deficit underflowed the formatting.
   - "Writes out every pair" is not true for the Prouhet pairs with L ≥ 4, which are given only by hash and CSV.
10. **Figure 3 and Example 3.12.** Identify which Table S1 rows are the diamonds at s ≈ 18–32.
11. **Theorem 4.4.** diam is not a spectral quantity; say so.
12. **Lemma 2.4.** Make explicit that n_O counts non-primitive classes too.
13. **Corollary 4.3.** Add the one line explaining why there are uncountably many isometry classes.
14. **§5 and Theorem 5.10.** Put the reason "c_2 gives (S_1, R) since S_1 ∈ Z and 0 < R < 1" next to Theorem 5.10.
15. **§1.1.** "Uniformly over all ..." is inaccurate, since the count depends on the area. Say "explicit in the area".
16. **Notation.** "Kmult" is opaque; consider K_sig.
17. **Theorem 3.10.** Mention the handle-adding argument already in the statement.

## 6. Presentation (including figures and captions)

The prose is crisp but often too dense. Theorem 1.1 is assembled from five places, so the reader needs a "result / where proved / what is new" table. I checked the figures on rendered page images.

- **Figure 1.**
  - Each panel shows one triangle (the half that is doubled); say so.
  - The order-12 tip of (b) is visibly only dark brown and does not reach the darkest colour, contrary to the caption. Add an inset or mark the tip values.
  - The figure uses 𝔥_t while the text uses h_t; unify.
- **Figure 2.**
  - Correct: I checked (a), and in (b) U* = {1,15} with the 1 coming from padding, and V* = {3,3,5,5}.
  - The colour coding differs between (a) and (b). Unify it, and explain the disc at 1.
- **Figure 3.**
  - Correct: the bounds start at s = 4, the solid line is ⌊2s⌋+4, and the dashed line jumps at s = 13.
  - Note that the dashed curve is a non-constructive guarantee, not a record.
- **Figure 4.**
  - The non-linear λ-axis is unexplained.
  - The vertical lines at ϑ = 0.8 and 1.6 are unexplained.
  - The ϑ values of the four drawn shapes are not given.
- **Figure 5.** The boundary is drawn as an ellipse (aspect ratio about 1.2), and the caption says "hyperboloid". Either say this is an oblique view, or fix it to a Poincaré disc. The triangle area π/4 is correct.
- **Figure 6.** Correct: the overlap dots at 19, 20, 23, 26, 29 and the collision circles at 20, 34, 38, 62, 117 agree with Table S2. State that both axes are logarithmic.
- **Figure 7.** The slopes and the diamond positions are consistent with Table 1.
- **Figure 8.** Fine. In (b), state that there are seven curves.
- **Tables 1 and S4.** Consistent: δ_up/δ_cert is 1.03–2.05, and 6.72 for n = 5.

## 7. Recommendation

**Major revision.**

I could not fault any mathematical statement. Every formula, example, search count and arithmetic claim I recomputed is correct, including Proposition 5.9 up to 4800 and the rank-0, Z/2×Z/6 structure of C_{27/2}. The triangle-orbifold theorem and the explicit area bound are genuine contributions.

However, the paper does not yet show that counting heat invariants matters for inverse spectral geometry (M1). It hides the orientability question behind a class restriction (M2). And it wraps a modest core in long classical, numerical and error-model material (M3). A revision that addresses M1–M3 and makes the key proofs checkable (M4) could be acceptable. Without a convincing answer to M1, I would advise the authors to take the paper to a journal with a more arithmetic-combinatorial readership.

**Confidence:**
- high on correctness, since I recomputed most of the checkable claims;
- moderate on the recommendation, which rests on a judgement of significance for JGA.
