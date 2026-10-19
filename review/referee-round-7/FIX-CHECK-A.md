<!-- FIX-CHECK A (round 7): returned text saved verbatim; the reviewer could not write files -->

Of the 12 MAJOR items, 10 are DONE and 2 are PARTIAL (A2 and A11). None is MISSING or WRONG. The minor items are mostly done, with seven PARTIAL. There are no "??" cross-references, but one reference is wrong: p. 5 cites "Theorem 1.1(ii)–(iv)", and Theorem 1.1 has only (i)–(iii). Nothing in either PDF comments on length or suggests cuts. The only AI, path or history problem is one revision-history sentence in the supplement (S-p. 15).

I rendered both PDFs at 110 dpi (300 dpi for Fig. 3 and 200 dpi for Remark B.4) and checked Figs 1–8, the abstract, pp. 3, 5, 15, 50 and supplement p. 16 against the text. I also recomputed the worked examples: Theorem 3.4(3), Example 3.21, the ν(a) closed form and the M = 3, 4 pairs, Proposition 2.12's scaling, Table S2 against Theorem 5.4, the Fig. 3 step curves and the Fig. 8 slopes. All of them check.

## MAJOR items

| id | where (page) and passage | verdict | reason |
|---|---|---|---|
| A1 | Abstract (p. 1): "They describe diffusion only in the limit t → 0: at any fixed t > 0 the heat trace determines the whole spectrum, and reading even c3 … needs t of order 10⁻¹¹." §1 (p. 2): "depends … only on the geometry in a fixed neighbourhood of the point (Kac's principle)". §1 (p. 3): "Short-time diffusion therefore detects the signature through these coefficients only in the limit t → 0 … t ≲ 8 × 10⁻¹¹ and values accurate to about 10⁻¹⁹. The counts below are invariants of the sequence of coefficients, not durations of an experiment." The moduli enter "only through terms of order e^{−ℓ²/4t}" (p. 3). | DONE | Every requested element is there; the title is unchanged. |
| A2 | p. 5, "What is elementary and what is not" (new / classical / Uçar's / Fursaev's), repeated in §1.2 (pp. 7–8). §5 (p. 38): "Kmult(O(p,q,r); Sig) ≤ ⌊2(1−R)⌋+4 ≤ 5 … and ≤ 4 when R > 1/2". | PARTIAL | The verdict's evidence asks for a table (result / new or not / method / where), but the paper has prose only. The p. 5 sentence "the exact area-free answer M + 1 of Theorem 1.1(ii)–(iv)" is a wrong reference (should be Theorem 3.11(ii)–(iv), as on p. 8). The §5 bound is correct. |
| A3 | p. 6: "What the two papers share is stated exactly: … this paper is the primary place of those results and of the description of the computations." p. 8: "Theorem 5.8 is proved here, by hand … the note reproves it by machine … The enumeration … up to sum 4800 … is the same computation as the note's". | DONE | Small wording point: "and cites it here" should read "and cites this paper". |
| A4 | Proposition 2.12 (p. 14), with its proof and the paragraph after it: "not claimed for an unknown curvature … not stable under changes of the metric". | DONE | I checked c_j(O) = \|K\|^{j−2} c_j(O₁), \|K\| = −χ/(2c₁) and the χ^{j−2} criterion; all correct. One wording error is listed under flag (a) below. |
| A5 | p. 7 and p. 15: "Fursaev wrote the n-th cone coefficient as Σ αc_k(α)G_nk … and computed the first two [13, (2.8), (3.26)–(3.28)]". p. 15: "The proof below is an outline: three steps are not carried out in full here, namely …", naming all three. "The main results of the paper do not use the proposition." Proposition 2.13(i) requires m ≥ max(2, l−1). | DONE | (ii) is restated as reading the identity of (i) as a Laurent polynomial in m. The β values check: (2l)!/l!·K^l gives 2K and 12K². |
| A6 | Lemma B.3 (p. 49): "integer cone orders at most μ₀". Remark B.4 (p. 50): "ℓ₀ and … D are geometric inputs, not spectral ones, so δ₁ is proved relative to them … D = 4.897, twice the longest side arccosh(cot² π/8) = 2.4485 … ℓ₀ = 2.2567 … certified in interval arithmetic … 7.8 × 10⁻¹¹ … 2.07 × 10⁻¹⁹". | DONE | The numbers are consistent with each other (3.80e−7 / 4.9e3 ≈ 7.8e−11). The supplement contradicts the "interval arithmetic" claim; see flag (a). |
| A7 | p. 7: "follows from Steinig's uniqueness theorem, which Laurens states as follows … (we could not consult Steinig's paper) … Theorem 3.2 adds complex multisets with multiplicity". p. 24 (Lemma 3.10): "the following classical sign-change argument, the mechanism behind Descartes' rule of signs; Laurens gives the same argument for power sums [28, Lemma 3.2, Cor. 3.3]". | DONE | Minor: "the conclusion of Theorem 3.2 follows" holds only among positive distinct reals, which the next sentence implies. |
| A8 | Remark 4.3 (p. 35): "… is Garbin and Jorgenson's [37, Thm 2.5, Rem. 2.6]". | DONE | |
| A9 | p. 32: "what is new here is that constant (Proposition 4.2(a), Remark 2.6) and the reading of the cone timescale … The computed spectra then illustrate these proved statements". p. 35: "the fit of d3, d4 is a test of the computation, not of these exactly known coefficients". | DONE | |
| A10 | Remark 2.6 (p. 11) uses C∗ from [3, Lemma 4.5]. p. 34: "4.4 × 10⁶ to 1.0 × 10¹⁰ … 4.0 × 10³ to 8.8 × 10⁴ with the computed diameter (not a bound), and from 4.1 × 10⁵ to 1.9 × 10⁶ with the diameter-free count". S6 (S-p. 14) gives the same three ranges. | DONE | |
| A11 | p. 43 (proof of Theorem 6.2): "M = Y⁻¹B with det B = ±∏(m_i+m_j) (Lemma C.1), so the system is singular exactly where Hur_{n−1}(χ_m) = 0, and M⁻¹ = B⁻¹Y". p. 51: "a one-sided bound". p. 5: "vanishes exactly where a Hurwitz determinant does". | PARTIAL | The overstatement is gone and "as well conditioned as" no longer appears. The verdict's "identify B" (a submatrix of the order-(n+1) Hurwitz matrix up to column signs) is not stated in Lemma C.1. |
| A12 | Lemma 3.14 (pp. 26–27), parts (a)–(c) with proof. Definition 3.13 is now only a definition. Proposition 3.19's proof cites Lemma 3.14(a) and (c). | DONE | |

## Minor and presentation items

| id | where (page) and passage | verdict | reason |
|---|---|---|---|
| a1 | p. 35 and S-p. 11: "near t ≈ 0.36 … (between the sampled times 0.341 and 0.360)" | DONE | Fig. 5(a) crosses zero there. |
| a2 | S-p. 12: "within the displacement bound d(x₀,γx₀) ≤ ℓ + 2r of the proof of Lemma 2.4" | PARTIAL | r is undefined, and Lemma 2.4's proof uses 2 diam, not 2r. |
| a3 | p. 38: "Two strata overlap at S if the convex hulls … meet." Table S2 caption (S-p. 8): "in this table it vanishes only for p = 2 and p = 4" | DONE | |
| a4 | p. 35: "Heuristically, and without use in any proof … (we checked these numerically …)" and "truncating the cone series" | PARTIAL | p. 3 still states as fact: "its coefficients grow like l!(m/π)^{2l}". |
| a5 | p. 33: "at ϑ = 0, where a = b, the systole is attained by two closed geodesics and λ₁ appears to be double" | DONE | |
| a6 | p. 37: "O(5,5,5) and the sphere (0;2,2,2,10), of cone-order sums 15 and 16, share c₁ and c₂" | DONE | Rechecked. |
| a7 | S-p. 14: "differ by up to 0.78" | DONE | |
| a8 | p. 10: "the class of test functions for which [5] state it" | PARTIAL | That fix is in. But p. 48 still has "with 2ϵ < ℓ" (it is used there, so not wrong), and "ψ̂ real and even" is not stated. |
| a9 | pp. 6, 19: "for each L … metrics, depending on L"; p. 18: "bumps in disjoint discs add"; "exact flat cone" | DONE | |
| a10 | pp. 13–14: "for K > 0 from the polynomial dependence of the coefficients on the jet of the curvature" | DONE | |
| a11 | Proposition 2.13(i): m ≥ max(2, l−1) | DONE | |
| a12 | Remark 2.14 (p. 17): "The following rest on exact computer algebra" | DONE | |
| a13 | Lemma B.3: "integer cone orders at most μ₀" | DONE | |
| a15 | p. 25: "a w_a = (−1)^{M−a} 2a³/((M−a)!(M+a)!) … proportional to (−1)^{M−a} a³ binom(2M, M−a)" | DONE | M = 3, 4 values recomputed. |
| a16 | Theorem 3.15 (p. 27): "if moreover … \|Z\| = 2L+2" | DONE | |
| a17 | Corollary 3.12(a): "L ≥ 2" | DONE | |
| a18 | Proposition 3.19 (p. 29): "f(A) = o(A) if and only if N(k)/k → ∞", with proof | DONE | |
| a19 | p. 29: "the set of areas of signatures is well ordered …" | DONE | |
| a20 | Theorem 1.1(iii) and Corollary 3.12(a): "⌈(L−1)/2⌉" | DONE | |
| a21 | p. 19–20: "Most of what follows comes from one fact … the bounds on the cone orders and on the genus rest instead on sign changes" | DONE | |
| a22 | "pencil of quartics" is gone; "pencil splitting" is defined in S1 (S-p. 1) | DONE | |
| a26 | p. 7: "[20, Thm 1, Thm 6.2]" with hypotheses; Proctor–Stanhope [17]; p. 12: Schueth's "can occur"; DGGW χ ≥ 0 class; "[5, Thm 1.1]" for the counts | DONE | Kuosa–Meyrignac–Chen does not appear anywhere. |
| a27 | "To our knowledge" remains (pp. 7 and 28) | PARTIAL | The intended fix is unclear. W(k) does not appear. |
| a28 | p. 16: "[21, Cor. 2.4, Lemma 3.4, (13)]" | DONE | |
| a29 | p. 36: "each circle is drawn at the first sampled time past the threshold, so it can lie above ten times the budget" | DONE | Matches the figure. |
| a30 | Fig. 8 caption (p. 44): "up to permutation" | DONE | The axis title ‖m̃ − m‖_∞ is consistent with it. |
| a31 | (0;3,3,3) "χ = 0" (p. 18); Corollary 6.5 conditional on a "proved bound" (p. 45); unknown-curvature sentence (p. 14) | DONE | I could not identify the "constants 1/3 and 8π" item. |
| a33 | Theorems A–C are now 3.x; no "Theorem A/B/C" remains | DONE | The companions' cross-references are not checkable from these PDFs. |
| a34 | Proposition 2.13's cut-off is now ζ | PARTIAL | The proof of (iii) (p. 17) still uses the cut-off χ₀. The bump ψ (versus ψ_k), the isometry Φ (versus Φ_m and Φ(e,I)) and the integer C (versus C = 2 sin ϑ/2, C_hyp, C∗) are unchanged. |
| a35 | All eight captions are at most two sentences; the colour key is in the text at Fig. 2 (p. 23); there are no in-figure legends | DONE | Checked on the renders. |
| a36 | One "Table 1 lists" (p. 8); the table does not split a sentence | DONE | |
| a37 | Lemma 5.3 proof (p. 38): "R⁻_{S,p} ≤ max(stratum p+1) is gap_p(S) ≤ 0" | PARTIAL | The "is gap ≤ 0" phrasing is still there. "The bound 6" no longer appears. |
| a38 | [9] "Dowker, S." against [10] and [14] "Dowker, J.S."; [14] "11(11), 137–140" | PARTIAL | The initials are inconsistent for the same author, and the CQG letter pages are L137–L140. Whether [6] and [52] have since been published cannot be checked from the PDFs. |
| a39 | Definition of "enveloping" (p. 6); forward dependence on Lemma 3.6 addressed (p. 15) | DONE | |
| not changed | a14 (p. 25: "we claim no minimality for other M"), a23–a25, a32 (Kac's principle on p. 2 is still uncited), a40 | consistent with the verdict | |

## Flags

**(a) New statements that look wrong or overstated**
1. **Wrong reference, p. 5:** "Theorem 1.1(ii)–(iv)" should be Theorem 3.11(ii)–(iv).
2. **Wording error, p. 14:** "So an equality of c₁ or of c₃ … is destroyed by arbitrarily small such changes." "Such changes" keep the area, so they cannot change c₁; the statement holds only for c₃.
3. **Contradiction about ℓ₀:**
   - Remark B.4 (p. 50) says ℓ₀ = 2.2567 is "certified in interval arithmetic by the complete enumeration of … the companion".
   - Supplement S4 (S-p. 12) calls the same enumeration "in floating point".
4. **Divergence asserted, growth heuristic:**
   - p. 35: "The usable window is short because the cone series diverges."
   - S-p. 11: "the series diverges, by (6) and the growth of the cone coefficients stated there."
   - The growth "stated there" is explicitly heuristic, and (6) is only an upper bound. A one-line lower bound from Lemma 2.7's positivity would make divergence rigorous.
5. **"No proof here depends on it", p. 6:** Remark 2.6 and the certified ℓ₀ of Remark B.4 do rest on the companion ([3, Lemma 4.5], [3, §7.1]). Both are remarks, so this is borderline.
6. **Undefined symbol, S-p. 12:** the "ℓ + 2r" bound (same as a2).

**(b) Broken cross-references:** no "??" in either PDF. The only wrong reference is item (a)1.

**(c) Comments on length or suggested cuts:** none.

**(d) AI tools, internal paths, review history:**
- The AI-use, author-contribution, Zenodo DOI and preprint-identifier placeholders are as allowed. The AI placeholder carries a "Use of AI tools. See the paragraph …" pointer (p. 46).
- No referee or round history appears anywhere.
- **Flag:** S-p. 15: "(An earlier version of the search used a floating-point filter instead; it is superseded by this exact test, with the same conclusion.)" This is revision history.
- **Note, likely acceptable:** S-p. 16 lists program file names (e.g. `check_heat_supporting.py`, `locality_ratio.py`). They are names, not paths. `gen_f4_area_classes.py` for Figure 3 is a leftover of old numbering and clashes with "each figure: Fk.py". The main paper's data statement gives the public GitHub URL.

Working files are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/fixcheck-A/scratch/ (renders in img/, extracted text in txt/).
