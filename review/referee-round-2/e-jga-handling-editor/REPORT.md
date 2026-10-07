<!-- Provenance: reviewer (e) could not write files; this is its returned report text, saved verbatim by the orchestrating session (preamble line about the failed write removed). -->

# Handling-editor report: "How much of a hyperbolic orbifold does heat hear?"

**Submission to:** The Journal of Geometric Analysis (JGA).

**Materials read:**
- the manuscript (37 pp.);
- the electronic supplement (12 pp.);
- the companion note the authors disclosed, "Triples with equal sum and equal reciprocal sum" (12 pp.).

I rendered every manuscript page to an image. Figures and the formula-heavy pages (3, 7, 11, 24, 26, 27) were checked on the rendered page, not only in extracted text. The marked placeholders (author contributions, AI-use statement, Zenodo DOI) were not counted as defects.

## 1. Summary

The paper studies closed orientable hyperbolic 2-orbifolds with cone points. It asks how many heat-trace coefficients c_1, c_2, … are needed to recover the signature, meaning the genus and the multiset of cone orders.

The basic observation is classical at curvature −1:
- c_1 is the area;
- each later c_j adds exactly one new odd power sum Σ m_i^{2j−3} on top of the reciprocal sum R.

So comparing two signatures becomes a signed odd-moment problem: a symmetric Prouhet–Tarry–Escott (PTE) system with an extra reciprocal-sum condition.

**Results on the signature (Theorem 1.1)**
- The first ⌊Area/π⌋+4 invariants always determine the signature (Theorem 3.4 and Corollary 3.5, a parity or mirror argument).
- No bound independent of the area works (Theorem 3.10).
- The worst-case count f(A) lies between about √(A/6π) and A/π + 4.
- f has power-law growth with exponent α exactly when N(k) = O(k^{1/α}), where N(k) is the PTE function; in particular f is linear exactly when N(k) = O(k), which is an open problem (Theorem 3.11).
- For spheres with n cone points, n invariants suffice (Theorem A, an R-variant of the Newton/Steinig uniqueness, with an Orlando/Hurwitz determinant in Theorem B).
- n−1 invariants fail: over the reals for every n ≥ 2, and on explicit integer witnesses for n = 3, 4 (Theorem C).

**Triangle orbifolds (Theorem 1.2, Section 5)**
- The first two invariants are equivalent to (S_1, R), the cone-order sum and the reciprocal sum.
- They separate every triangle orbifold with cone-order sum S ≤ 17. They first fail at S = 18, on O(2,8,8) and O(3,3,12), which a stratification of triads by least order explains.
- The authors list the 38 collision-free sums up to 4800; this is a computational result.
- The minimal pair and all its multiples are isolated, because C_{27/2} is a rank-0 elliptic curve with torsion Z/2 × Z/6.
- Three invariants always suffice.

**Section 4: what heat does not hear**
- Every c_j depends only on the signature, so no finite number of invariants determines an orbifold up to isometry whenever there are moduli.
- The authors give an explicit but loose bound on the difference of two heat traces of the same signature, and show that the order t^{−1/2}e^{−ℓ²/4t} is attained.

**Section 6: stability**
- For spheres with known n, recovering the orders from perturbed c_1, …, c_n is Lipschitz at simple orders and Hölder of exponent 1/k at k-fold orders.
- They give explicit thresholds, and an exact-arithmetic certificate in the supplement.

**Section 7 and supplement: numerics**
- High-order finite-element spectra of O(2,8,8) and O(3,3,12) recover d_3 and d_4, and a blind recovery of the cone orders succeeds.
- A one-parameter family of signature (0;3,3,3,3) has a moving spectrum and fixed heat invariants.

## 2. Significance and novelty (including fit to JGA)

**What is good**
- The question is natural: a quantitative version of which finite part of the heat expansion hears the cone data.
- The answers are clean and, as far as I checked, correct.
- The authors are candid about what is classical (Remark 2.11, the start of Section 4, and the "three limits of scope" paragraph).
- The mirror/parity argument of Theorem 3.4 is short and elegant.
- The triangle-orbifold analysis is complete. It gives an exact first failure with a structural explanation (tangency only at p = 2, 4) and an arithmetic isolation result.
- The reduction of the growth question to N(k) works in both directions, and is presented honestly as relocating the problem rather than solving it.
- Reproducibility is exemplary: computations are in exact arithmetic and each one is tied to a script.

**Novelty claims checked against the literature**
- I searched arXiv (heat invariants and orbifolds, orbisurfaces, triangle orbifolds and the spectrum, PTE and spectral problems). Nothing I found anticipates:
  - the explicit uniform count ⌊Area/π⌋+4;
  - the first failure at S = 18;
  - the rank-0 isolation.
- Uçar's thesis (arXiv:1711.03405) recovers the cone data from the full sequence of invariants. Dryden–Gordon–Greenwald–Webb only remark that their invariant c "does not seem sufficiently strong". The authors' positioning against both is accurate.
- Reference [44] (Croot–Mao–Yip, arXiv:2609.05061) exists and says what it is cited for.
- I checked six references on Crossref ([16], [17], [23], [31], [38], [43]); their metadata is correct.

**Depth**
- Once the classical coefficient structure is granted, every main theorem reduces to elementary algebra:
  - Newton's identities and Descartes' rule of signs;
  - inequalities on reciprocal sums plus a finite check;
  - a standard 2-isogeny descent;
  - Rouché/Ostrowski root perturbation.
- The analytic content is either classical or re-derived:
  - the trace formula for the heat function, and Appendix A;
  - all the heat coefficients, which Uçar already computed;
  - Section 4.
- The most interesting open question, how f(A) grows, is left as a gap between √A and A.

**Fit to JGA**
- The primary MSC class 58J53 and the inverse-spectral framing are within JGA's scope.
- The new mathematics, however, is mainly algebraic, combinatorial and arithmetic. Fit is acceptable but not strong.
- Overall this is a correct, careful contribution of moderate depth. It would be publishable in a substantially shorter form.

## 3. Correctness (spot-checks and recomputations)

All recomputations below used exact rational arithmetic unless noted.

1. **Lemma 2.6, Proposition 2.7, Lemma 2.8 and equation (7).**
   - I recomputed p_l for l ≤ 7 from formulas (4)–(5); p_0, p_1, p_2 match (7).
   - p_l(1) = 0 for every l checked.
   - The leading coefficient is |B_{2l+2}|/(2(l+1)!(2l+1)) in every case.
   - p_l > 0 at the sample points m > 1 that I tested.
   - α_0, …, α_5 = 1, −1/3, 1/15, −4/315, 1/315, −4/3465.
2. **Equation (9).** The formulas for c_2 and c_3 are exact at (2,3,7) and (4,5,9).
3. **D(t) = Z_{(2,8,8)} − Z_{(3,3,12)}.**
   - d_1 = d_2 = 0, d_3 = 25/12, d_4 = −1775/24, d_5 = 153025/48.
   - c_1 = 1/8 and c_2 = 67/48, as stated.
4. **Theorem C(3).**
   - n = 3: (R, P_1) = (3/4, 18) on both sides, with P_3 = 1032 and 1782.
   - n = 4: (8/15, 58, 31402) on both sides, with P_5 = 25159618 and 21298618.
   - For n = 4, c_1–c_3 agree and c_4 differs by 10725/7. Area/2π = 22/15.
5. **Remark 3.2.**
   - The pencil splitting has e_1 = 0 on both sides, e_3 = −1650 and e_4 = 12600 on both sides.
   - The smallest witness without a pencil splitting shares (R, P_1, P_3) = (45/296, 180, 818640).
6. **Examples 3.6 and 3.12, and the small rows of Table S1.** Each pair shares exactly the stated number of invariants. Where the paper gives the area, it matches.

   | Pair | Recomputed |
   |---|---|
   | (1;15) and (0;3,3,5,5) | s = 14/15, Ψ_1 = 224/15 on both sides |
   | (1;15,15,15) and (0;3,3,5,7,7,21) | s = 14/5 |
   | (0;4,4,5,5,6,12,12) and (0;2,2,2,3,10,10,10,10) | s = 113/30 |
   | (0;5,5,5) and (0;2,2,2,10) | s = 2/5 |
   | Prouhet L = 2 pair | s = 12/5 |
   | Cone-count pairs, L = 4, 5 | shared counts as stated |
   | Genus pair, L = 4 | s ≈ 6.9999 |

7. **Theorem B.** I built M from (11). det M equals (−1)^{n(n+1)/2} ∏(m_i+m_j)/e_n exactly for (2,3,7), (3,10,15,30) and (2,2,2,2,3).
8. **Section 5.1.**
   - Table S3 lists exactly 83 triads.
   - S*(p) matches a direct overlap computation for 2 ≤ p ≤ 15.
   - x*(p), the odd-parity gaps 1/840, 1/2310, 1/10296, the values at S*(p)+1, and the closed form of gap_p(3p+7) are all correct.
   - The first collisions in Table S2 (p ≤ 14) are reproduced.
   - The first non-adjacent collision is at S = 35, between strata 5 and 7.
9. **Proposition 5.9.** An independent C program reproduces exactly the 38 collision-free sums in [18, 4800].
10. **Companion note, Table 2.** My enumeration reproduces the counts at S = 18 and 100–600 (for example 3067 / 2977 / 1714 at S = 600). It also confirms that 507 of the 582 sums 19–600 carry a primitive class.
11. **Theorem 5.10.**
    - ψ maps E: y² = x(x+9)(x+384) into C_{27/2}, and φ(1:4:4) = (−24, 360).
    - disc E = 2^18·3^8·5^6, and #E(F_7) = #E(F_11) = 12.
    - All eleven listed points lie on E with the orders the paper states.
    - d' = 3²5⁶, and the mod-5 step of the descent is correct.
    - PARI/GP (cypari2, installed in a local virtual environment) gives torsion Z/6 × Z/2, ellrank [0,0], analytic rank 0 with L(E,1) ≈ 1.3376, and conductor 90. Rank 0 is therefore also unconditional (Kolyvagin and Gross–Zagier), and E appears in Cremona's tables.
12. **Section 6 constants.**
    - The absolute row sums of F^{-1} are 2, 14, 498, 4062, 56230/3.
    - The P_3 row of F^{-1} is (−18, −120, −360).
    - ζ_3 = 1, ζ_4 = 79/3, ζ_5 = 14048/15.
    - Proposition 6.6(i) and the identity and constant 498 + 42a² in Remark 6.7 are correct.
13. **Proofs read line by line.**
    - Lemmas 2.4–2.5: the integration by parts, the bound 2tℓ/(ℓ−t), the constant C in (3), and the logarithmic derivative.
    - Theorem A, Theorem 3.4, Corollary 3.5, Lemma B.1, Proposition 3.9, and Theorem 3.11(a)–(e), including the thresholds 16π and 12π.
    - Theorem 5.1, and the real partner triple in Remark 3.13 (its sum 11 and product about 7.36 check).

**Verdict.** I found no mathematical error, and every number I recomputed matches.

**Not re-derived:**
- the thresholds in Table 1;
- the blind recovery;
- the finite-element error budget.

All three are labelled as a-posteriori and not used in any proof.

## 4. MAJOR issues

**M1. The length is not earned (the whole paper).**
- The paper is 37 pages plus a 12-page supplement, but at most about 15 pages are new mathematics.
- Material that re-derives or illustrates known results:
  - Section 2.2 (pp. 8–10);
  - Theorem 2.3 with Lemmas 2.4–2.5 and Appendix A;
  - Section 4 (pp. 17–20);
  - Section 6 (pp. 25–28);
  - Section 7 (pp. 28–29).

*Why it matters:* JGA has no hard limit, but long papers must justify their length.

*Resolution:*
- Replace the derivation in Section 2.2 by a citation to Uçar [11, Thm 4.20] plus the comparison in Remark 2.9. Keep (5) and Lemma 2.8.
- Move the proof of Lemma 2.6 and Appendix A to the supplement.
- Compress Section 4 to about one page.
- Move Section 7 to the supplement.
- Treat Section 6 as in M3.
- Target about 22–25 pages.

**M2. The significance case is thin (Section 1.1, Theorem 1.1(ii)).**
- The growth result is a gap between √A and A plus a reduction to N(k).
- Theorem A is a small variant of the Newton/Steinig uniqueness, and Theorem 1.2(iii) is Theorem A for n = 3.
- Corollary 3.5 is a short parity argument.

*Resolution:*
- The Introduction should name the genuinely new results:
  - Theorem 3.4 and Corollary 3.5;
  - Theorem 3.11(b)–(e);
  - the S = 18 threshold;
  - Theorem 5.10.
- Ideally, add one result with real analytic content, for example:
  - recovery when (g, n) is unknown (currently excluded on p. 4);
  - eigenvalue-level stability.
- Otherwise, accept a shorter and more focused paper.

**M3. Section 6 has limited value in its present form (pp. 25–28, Table 1).**
- Errors are modelled on the coefficients, not the eigenvalues.
- The constants are evaluated at the unknown true orders, which Remark 6.1 concedes.
- The closed-form threshold δ_thm is 3 to 7 orders of magnitude below the certificate δ_cert. For example, 3.8e−7 against 2.3e−3 for (2,8,8), and 2.7e−12 against 7.9e−6 for (2,2,2,2,3).
- The Hölder exponent 1/k is the familiar behaviour of coalescing roots.

*Resolution:*
- State Theorem 1.3 qualitatively, with the exponents and their sharpness (Proposition 6.6, Remark 6.7).
- Keep Lemma 6.3.
- Move Theorems 6.4, 6.5, 6.8 and Table 1 to the supplement, or give only δ_cert.

**M4. Overlap with, and division of material against, the companion note (Sections 1.1, 5.1–5.2).**

The submission does not depend on the note, and it stands on its own. The arithmetic of (S, R)-coincidences is nevertheless shared between the two papers:
- **Same curve.** Both use the Bremner–Guy–Nowakowski curve C_Λ and its reciprocal-pair structure. Both treat Λ = 27/2; the note's Remark 2.4 gives Z/2 × Z/6 torsion there.
- **Same conclusion stated twice.** The caption of the note's Figure 1(a) asserts the conclusion of Theorem 5.10 without proof.
- **Same enumeration.** Both papers use the same enumeration up to S ≤ 4800. Proposition 5.9 is purely arithmetic.
- **Same derivation of (S, R).** The note's Section 1.1 repeats the derivation that two invariants are equivalent to (S, R).

*Resolution:*
- Keep in the manuscript only what the spectral statements need: Theorems 5.4–5.7, and Theorem 5.10 with a shortened proof.
- For Theorem 5.10, say "conductor 90, rank 0 by [Cremona/LMFDB]; torsion by reduction mod 7 and 11", and move the hand descent to the supplement.
- Move Proposition 5.9 and Table S2 to the note or to the supplement.
- Have the note cite Theorem 5.10 instead of restating it.
- Post the note to arXiv so that [24] can be cited.

**M5. Too many figures, and several have defects.**
- Figures 2, 3 and 6 carry the argument.
- Figures 1, 4(a) and 5 are decorative ("schematic, not isometric", tilings).
- Figures 7 and 8 illustrate numerics from the supplement.

*Resolution:* Keep Figures 2, 3, 6 and perhaps 7. Move or drop the others, and fix the defects listed in m1–m6.

## 5. MINOR issues

**Figures**
- **m1. Figure 5 (p. 20).** Each "disc" is rendered as an ellipse; I measured a width-to-height ratio of 424:360 ≈ 1.18 in both panels. Either the Poincaré disc was drawn with unequal axes, which distorts the angles and contradicts "Exact tilings", or the projection is not explained. The caption also says "hyperboloid" while the picture shows a disc model. *Fix:* use equal axes and name the model.
- **m2. Figure 3 (p. 16).** The split two-colour disc at s = 1/4, K_mult = 3 is not explained. The text on the 525 equal-area classes is hard to parse. *Fix:* explain the disc in the caption and simplify the text.
- **m3. Figure 4(b) (p. 18).** The vertical axis is nonlinear (ticks 0, 1, 5, 10, 20, 40, …) but its scale is not stated. The grid lines at ϑ ≈ 0.8 and 1.6 are unexplained. *Fix:* state the scale and explain or remove the lines.
- **m4. Figure 8(a) (p. 30).** Three grey "divergent expansion" curves appear with no truncation orders given. *Fix:* label them.
- **m5. Figure 2 (p. 13).** The colour code differs between panel (a) (orange/teal) and panel (b) (grey/black) and is never explained. *Fix:* use one scheme and state that it distinguishes U* from −V*.
- **m6. Figure 1 (p. 2).**
  - The caption does not say how h_t(x,x) was computed.
  - Each panel shows a single triangle, which is half of the orbifold.
  - The colouring is quantitative, but the shape is "schematic, not isometric".

  *Fix:* clarify the caption, or move the figure to the supplement.

**Text and statements**
- **m7. Definition of Sig (p. 3).** Mirror orbifolds are excluded by appeal to isospectrality [5], but K_mult is about finitely many coefficients, not isospectrality. The relevant fact is that reflector edges create a t^{−1/2} term. More importantly, non-orientable orbifolds without mirrors share all heat invariants with the orientable orbifold of the same Euler characteristic and the same cone orders (crosscap number 2g). So the genus is heard only within the orientable class. *Fix:* say so explicitly.
- **m8. Abstract and Proposition 5.9.** "Two suffice again at exactly 38 sums between 19 and 4800" is ambiguous. *Fix:* rephrase precisely.
- **m9. Page 3.** The letter s in "s-multisets" clashes with the later use of s = Area/2π. *Fix:* rename one of them.
- **m10. Theorem 5.10 (pp. 24–25).** The two-page hand descent is for a curve that is in Cremona's tables. *Fix:* cite the tables and the analytic rank, and move the descent to the supplement.
- **m11. Proposition 4.2.** Triangle rigidity is classical; Troyanov's theorem is heavier than needed. *Fix:* cite the classical fact instead.
- **m12. Table 1 and Table S4.** The two tables duplicate each other. *Fix:* keep one.
- **m13. Appendix C.**
  - Paths such as `review/audit-2/…` and `review/round1-fixes/…` are internal workflow names. *Fix:* cite a clean, versioned archive.
  - The n = 4 search and the T_3 search are only logged, not rerun. *Fix:* state their run times.
- **m14. Table S1, row "6 Prouhet".** "1023 − 0.00 × 10^0" is a formatting glitch. *Fix:* correct the formatting.
- **m15. Theorem 1.1(i).** *Fix:* replace "read off from c_1" with "computable from c_1 = Area/4π".
- **m16. Page 5, "no earlier result locates…".** *Fix:* soften to "we are not aware of", and point to Chang–DeTurck and Grieser–Maronna as the nearest analogues.
- **m17. Reference [38].** Crossref gives online publication on 8 Dec 2025 (vol. 69, art. 2). *Fix:* date it consistently.

## 6. Presentation

**Writing and structure**
- The writing is crisp and precise at the sentence level, the statements are carefully scoped, and the roadmap on p. 4 helps.
- The problem is the overall structure. A reader looking for the new results first passes through:
  - re-derived coefficients (Section 2);
  - classical material (Section 4);
  - long and impractical stability constants (Section 6);
  - numerics that are not used in any proof (Section 7).
- Section 5 mixes the spectral statements with arithmetic that belongs in the companion note.

**Length.** At 37 pages plus a 12-page supplement, the paper does not earn its length. About 22–25 pages would hold everything new.

**Figures and captions**
- The captions are commendably short (two sentences each), but several leave a symbol or a colour unexplained (m2–m5).
- Figures 1, 4(a) and 5 are ornamental, and Figure 5 appears to have a distorted aspect ratio (m1).
- Three of the eight figures are essential.

**Overlap with the companion note**
- The overlap is moderate and honestly disclosed: the manuscript says on p. 5 that no proof depends on the note.
- It is not a duplicate publication of a main result.
- The shared material is:
  - the C_Λ and Bremner–Guy–Nowakowski framework;
  - the Λ = 27/2 isolation, which the note's figure caption also asserts;
  - the S ≤ 4800 enumeration behind Proposition 5.9;
  - the (S, R) equivalence.
- The division between the two papers should be made explicit (M4).

## 7. Recommendation

**Recommendation: major revision.** Confidence: moderate (about 65%).

The mathematics is correct wherever I checked, the computations reproduce exactly, and the question is natural.

The revision must:
- cut the paper substantially toward its new results;
- sharpen the significance case for a JGA audience;
- settle the division of material with the companion note;
- prune and fix the figures.

If the revised paper still reads mainly as elementary power-sum algebra around re-derived classical analysis, I would lean towards rejection and suggest a more specialised journal.

**Desk decision: send to review.** Desk-reject probability: 35%.

Reasons to send it out:
- It is in scope (58J53, inverse spectral problems on orbifolds).
- The results are correct, explicit and, as far as I can tell, new.
- The exposition is professional.
- The disclosed overlap is not duplicate publication.

Reasons the desk-reject probability is not low:
- The depth is moderate relative to the length.
- The novelty is mainly algebraic and arithmetic.
- About a third of the manuscript re-derives or illustrates classical facts.

Ask the referees to judge whether Theorems 3.4, 3.11 and 5.4–5.10 meet JGA's bar, and whether Sections 2.2, 4, 6 and 7 should be cut as in M1 and M3.

Suggested referees:
- one in inverse spectral geometry of orbifolds;
- one in PTE and Diophantine problems.

Tell the authors that a substantially shorter version is expected.
