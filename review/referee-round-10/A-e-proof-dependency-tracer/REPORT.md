<!-- Round 10, A-e, returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

# Referee report (rigour, citations, figures): "How much of a hyperbolic orbifold does heat hear?" (AGAG)

I could not save the report to /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/A-e-proof-dependency-tracer/REPORT.md, because subagents are not allowed to write report files. The full report follows.

Page numbers are those of the manuscript PDF (65 pp.); "S-p." means a supplement page. I rendered every page with pdftoppm (110–160 dpi) and looked at every figure before reporting on it.

My own scripts and the downloaded sources are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/A-e-proof-dependency-tracer/scratch/:
- `code/` holds the scripts c1–c8.py.
- `citeA/`, `citeB/` and `citeC/` hold the fetched sources.

## Summary

The paper studies closed orientable hyperbolic 2-orbifolds with cone points. It asks how many heat invariants c1, c2, … are needed to determine the signature. The analytic input is the Selberg trace formula and Uçar's triangular structure of the cone coefficients (Lemma 2.11). After that, each coefficient adds one new odd power sum of the orders.

The main results are:
- **Theorem 1.1 / 3.11.** With all cone orders at most M, M invariants suffice within Sig≤M and M+1 suffice against all of Sig. Both bounds are sharp; the witnesses come from Lagrange weights at the nodes a².
- **Corollary 1.5.** ⌊A/π⌋+4 invariants always suffice.
- **Theorem 1.2 / 3.18 / Proposition 3.19.** The maximal count f(A) lies between about √A and about A. Growth like A^α is equivalent to N(k) = O(k^{1/α}), where N(k) = P(k,2) is the Prouhet–Tarry–Escott quantity.
- **Theorem 1.3.** The recovery system has determinant ±∏(mi+mj)/∏mi, and a change of genus costs invariants (proved with Descartes' rule).
- **Theorem 1.4 / Section 5, triangle orbifolds.**
  - Three invariants suffice, and two suffice when the order sum is at most 17.
  - O(2,8,8), O(3,3,12) is the unique least-area pair in all of Sig sharing c1, c2.
  - The pair is isolated by the rank-0 curve C_{27/2} ≅ LMFDB 90.c3.
- **Section 2.4, variable curvature.** The part of the cone term linear in the curvature (Proposition 2.14), and extension and obstruction results (Proposition 2.17).
- **Section 6 and Appendices B, C.** A stability theorem with explicit remainders.

## Significance

What is good:
- The exact, area-free answer M+1 (Theorem 3.11(ii)–(iv)) is clean, sharp and new.
- The Descartes bound on the imbalance (Theorem 3.15) is neat.
- The reduction of the growth question to the PTE problem is correct in both directions, and the paper is honest that it settles no exponent.
- Theorems 5.9–5.10 fully answer the question left open in DGGW Rem. 5.16, with a hand-checkable 2-isogeny descent.
- Propositions 2.14 and 2.17 show cleanly that the counts are a constant-curvature phenomenon.
- The bookkeeping (remainders, signs, constants) is unusually careful.

The reason for doubt is about substance, not correctness:
- After Section 2.3 the work is the algebra of odd power sums: Newton's identities, Vandermonde, Chebyshev sign changes, Descartes' rule.
- Theorem 1.2 is a reformulation. Its unconditional content is √A ≲ f(A) ≤ ⌊A/π⌋+4.
- The geometric novelty sits mainly in Section 2.4 and Appendices B and E (see M1).

## Correctness, and what I recomputed

I traced every main result to its proof and to the external statements it uses. **I found no mathematical error in any main result or in any number I recomputed.** All computations below were exact (sympy and Python fractions) unless marked as quadrature.

**Section 2: heat coefficients and the trace formula**
- p0–p3 in (8). This includes p3 = (m²−1)(m²+3)(3m⁴+2m²+19)/30240.
- The leading coefficients in Lemma 2.9, for l ≤ 5, and α0–α5.
- The closed form of Lemma 2.7.
- Proposition 2.8, checked against the trace formula itself.
  - I computed the elliptic term E_m(t) by mpmath quadrature for m = 3 and m = 8. The remainder has the sign (−1)^K that Proposition B.2(a) claims.
  - I(t) agrees with the α-series.
- Remark 4.3: k_m reproduces E_m(t) to 25 digits.
- Lemma B.3: the asymptotic ratio is 1.0165, 1.0078 and 1.0038 at l = 10, 20 and 40.
- Lemmas 2.4–2.5: I checked the integration by parts, C_hyp and the monotonicity in ℓ by hand.

**Variable curvature (Section 2.4)**
- Proposition 2.14: I recomputed the Gaussian integral (−2l·l!·4^l t^l C^{−2l−2}) and obtained λ_l = 2/(l−1)!·Π_{l+1}. This equals p1/m at l = 1 and Schueth's −m⁵ΔK/15120 term at l = 2.
- Remark 2.16(b): the Δ²K term equals Π4(m) and the K³ term equals p3(m)/m. The top coefficients are consistent with β3,4.
- Proposition 2.17(ii):
  - I checked the formula ω_n = (−1)^n n(n−1)n!/(2n+1)! for n ≤ 8.
  - I also checked the 2D Gaussian identity used in the proof, u2 = K²/15, and the examples in (ii)–(iii).

**Section 3: counting results**
- Theorem 3.3: det M = ς_n∏(mi+mj)/∏mi, verified symbolically for n = 2…5.
- Theorem 3.11:
  - C = 6, 120, 2520, 362880.
  - The least-g areas are 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054}.
  - (ν(2), ν(3), ν(4)) = (28, −27, 8), and the example in (iv) checks out.
  - The M = 3 and M = 4 pairs share exactly 2 and 3 invariants.
- Exact shared counts and areas agree for Example 3.9, Theorem 3.4(3) (P3, P5) and Example 3.21(i)–(ii). In Table S1 they agree for the genus pairs L ≤ 4, the equal-count pairs L ≤ 4, the cone-count pairs L ≤ 5 and the Prouhet pair L = 2. Table 2's upper bounds agree with these pairs.
- By hand I checked:
  - Theorems 3.2, 3.7, 3.15 and 3.18(a)–(d);
  - Lemmas 3.6, 3.10, 3.14 and A.1;
  - Propositions 3.16, 3.19 and A.2, including the index bookkeeping L_i = ⌊(k_i+3)/2⌋.

**Section 5: triangle orbifolds**
- I enumerated all hyperbolic triads with S ≤ 600. This reproduces:
  - the 83 triads of Table S3 and the unique collision at S = 18;
  - Table S2 exactly, for p ≤ 14;
  - the first non-adjacent collision, (5,15,15)/(7,7,21) at S = 35;
  - the 38 collision-free sums of Computation S2.1, last one 557.

  The enumeration only goes to 600, not to the stated 4800.
- Theorem 5.6 and Proposition D.1: x*(p), S*(p), every quoted gap value, and gap_p(3p+7).
- Theorem 5.10:
  - ψ maps E into C_{27/2}, and φ∘ψ = id.
  - The discriminant is 2^18·3^8·5^6, and #E(F7) = #E(F11) = 12.
  - All twelve points lie on the curve, and the flex tangent meets it in (x−16)³.
  - The LMFDB API confirms 90.c3: rank 0, torsion [2,6], the same j-invariant, and c4, c6 matching with u = 2.
- Appendix F: the descent is correct line by line, including the mod-5 and mod-9 steps.
- Proposition 5.2 system: my own search ({2,2,c,d} with d ≤ 400; b ≥ 3 with d ≤ 5000) finds no solution.

**Section 6 and Appendix B: stability**
- amp0–amp4 = 2, 14, 498, 4062, 56230/3, and the row for P3.
- ζ3, ζ4, ζ5 = 1, 79/3, 14048/15.
- Propositions 6.3(i) and 6.4.
- The c3 values in Table S6, and d3, d4, d5.
- Remark B.6 for N = 3 (times τ, τ/2, τ/4): 4.9·10³τ, 1.14·10³τ, 7.8·10⁻¹¹, 3.3·10⁻¹⁰, 2.07·10⁻¹⁹, and arccosh(cot²(π/8)) = 2.4485.
- The ratios in Table S4.

**Citations.** I fetched and checked these at statement level: [2], [4], [5], [9], [10], [11], [17], [19], [20], [22], [24], [25], [26], [29], [30], [31], [34], [36], [37], [39], [40], [46], [52], [61], [63], plus [33] and Crossref metadata for the recent DOIs. All are accurate in substance. The discrepancies are listed under minor issues.

## FATAL

None.

## MAJOR

**M1. Geometric substance and focus (pp. 5–9, 21–33).**
- By the paper's own account (pp. 5–6), Theorems 1.1, 1.3(i) and Corollary 1.5 follow from Newton's identities and a Vandermonde determinant once Lemma 2.11 is in place.
- Theorem 1.2 relocates an open problem rather than solving it.
- For AGAG, the introduction should say in two or three sentences what geometric insight the counts give beyond Uçar's Cor. 4.21(iv). Candidates are the localisation of growth in large cone orders (Corollary 3.12) and the failure in variable curvature (Proposition 2.17).
- The variable-curvature dichotomy deserves a place in the list of main results; at present it is mixed in with numerical illustrations.

This does not affect correctness, but it is the strongest reason an editor could decline.

**M2. Results in the main text that rest on the unrefereed, unavailable companion [3].**
- Remark 2.6 (p. 12) imports the diameter-free count n_O(x) ≤ C*·e^x from [3, Lemma 4.5]. The introduction (pp. 6–7) and p. 34 then present "that constant (Proposition 4.2(a), Remark 2.6)" as new here.
- Remark B.6 (p. 54) quantifies the "proved" recovery of c3 cited in the abstract and on p. 2. It uses ℓ0 = 2.2567, "certified … by the complete enumeration of closed geodesics of the companion [3, §7.1]".
- [3] carries a placeholder identifier, so neither input can be checked.

Fix: either
- (a) include the count with a proof, and a self-contained systole certificate; or
- (b) mark Remark 2.6, the diameter-free form of Proposition 4.2(a) and the ℓ0 of Remark B.6 as conditional on [3], and remove them from the "new" lists on pp. 6–7 and 34.

Remark B.6 already states that its numbers hold for every ℓ0 ≥ 0.01. So option (b) costs nothing if a crude certified bound, such as one obtained by hand, is supplied.

## MINOR

**m1. p. 11, proof of Theorem 2.3.** [9, eq. (1)] states the trace formula for h entire, even and of uniform exponential type, with g = ĥ compactly supported. It does not state it "for h = ĝ with g ∈ C_c^∞ even". Add "(equivalently, by Paley–Wiener)" here, as is already done on p. 51. In addition:
- [9] writes R_c^l, not ρ^j.
- "[9, p. 68]" is p. 3 of arXiv math/0504571; check it against the journal pagination.
- [9] does not write out the area formula (2). It follows from Def. 3.1 with Thm 3.2 and K = −1; say so.

**m2. p. 7.** Neither [9, Thm 1.1] nor [9, Prop. 3.3] states literally that different signatures give different spectra. Thm 1.1 gives the number of cone points of each order, and Prop. 3.3 gives the underlying surface. The claim is their conjunction; say so.

**m3. p. 21, (11).** Holtz–Tyaglov Thm 1.17 reads Δ_{n−1}(p) = (−1)^{n(n−1)/2} a0^{n−1}∏(z_i+z_j). For the monic χ_m, whose roots are −m_i, the signs cancel, so (11) is correct. Add a line saying so. The arXiv id of [46] is 0912.4703.

**m4. p. 14, the erratum [45].** The secondary evidence I found (Gittins et al. [23], restating DGGW Thm 5.1 with "primary" strata) indicates that the added hypothesis concerns strata whose Iso^max is **empty**, not "trivial". I could not open the erratum itself, which is behind a bot wall. Please check the wording against [45].

**m5. Citation wording.**
- p. 30: [52] says ideal solutions "are known for n ≤ 10 and n = 12", counting by size. "Only" is the authors' addition, and the conversion from size to degree should be explicit.
- p. 30: [5, §1] states the pigeonhole bound and Wooley's bound for general m, as P(k,m) and W(k,m).
- p. 30: [4] writes Problem 3 as "N(k) ≤ o(k²)". Its remark about no progress "for many years" covers Problems 3 and 4.
- p. 4 / p. 30: [4] defines solutions as "sets" in §1 (pp. 3–4); p. 6 defines only N(k).
- p. 8: the Steinig attribution in [31] comes right after the *statement* of Lemma 3.2, before its proof. Laurens frames his argument as total positivity rather than Descartes' rule.
- p. 8: [34]. Identity 9 is (3.27), and (3.28) is the case m = 3, so the citation is fine. Chen calls (A.685)–(A.692) the *smallest* solutions found by a 2017 search, not a complete list up to 84. Keep the completeness claim attached to the authors' own search (Remark 3.5).
- p. 8: [20, Main Thms 1–2] have different hypotheses. Thm 1 assumes a lower Ricci bound. Thm 2 assumes a lower sectional curvature bound and isolated singularities. Both assume compact orientable orbifolds. The sentence merges them.
- p. 9: [29, Thm 1] literally says area, perimeter and the reciprocal sum of the angles. Identifying these with the first three heat invariants is the paper's preceding text, which is fine but should be said.
- p. 7: [11, Thm A]. Say that its pairs have signature (0; 2,2,2,2,2,3,4), so they lie in Sig. That is exactly what the sentence needs.

**m6. p. 4, Theorem 1.2(ii).** For α ≤ 1/2 both equivalences hold trivially (N(k) ≤ k(k+1)/2+1). Their content is in 1/2 < α ≤ 1; state this.

**m7. p. 32, Table 2 caption.** It says the upper bounds are sizes of pairs in Example 3.21. The L = 2 entry, 6, comes from O(2,8,8)/O(3,3,12) or Example 3.9; Example 3.21 starts at L = 3.

**m8. pp. 29–31.** Theorem 3.18(b) uses 6πC (Proposition 3.16 with n ≤ N(2L−3)). Proposition 3.19 uses 4N(2L−3) (the genus construction of Theorem 3.18(c)). Both are correct, but one sentence naming which construction gives which constant would spare the reader a reconstruction.

**m9. p. 5, Theorem 1.3(i), last sentence.** It speaks of non-injectivity "as functions of real orders". It should carry, in the statement itself, the caveat from p. 13 that b_l at non-integer m is an algebraic device.

**m10. p. 16.** Conjecture 2.13 rests on an outline (S7) with two steps not carried out, and it is used nowhere. Consider moving it with S7 to Section 7, keeping Proposition 2.14 in place.

**m11. pp. 57–58, Appendix E, Step 4.** The rotation-invariant cap used to identify c_k = B_k creates a second fixed point of Rot_ϑ at the antipode. State that its contribution is a separate, distant term, and that the cap can be chosen uniformly in |ε| ≤ 1.

**m12.** The computer searches are correctly labelled as unused in proofs: Remarks 3.5 and 3.22, the search after Corollary 5.3, and Computation S2.1. I reproduced S2.1 up to S = 600 and part of the Proposition 5.2 search. No change needed.

## Presentation (figures, tables, cross-references)

I checked every figure and table against its caption and the text that cites it. The cross-references resolve correctly.

- **P1. Fig. 1 (p. 3).** The colour bar runs to 12, but the panels never visibly exceed about 4. Cap the bar or add an inset at the order-12 vertex. The text figures are correct: 0.546 and 1.786.
- **P2. Fig. 2 (p. 25).** Correct as drawn and captioned.
- **P3. Fig. 3 (p. 33).** The diamonds lump genus, equal-count and cone-count pairs together; use three marker shapes. Otherwise the plot matches:
  - the step functions ⌊2s⌋+4 (solid) and ⌊√((s−1)/3)⌋+2 (dashed) are as stated;
  - the squares sit at 2.4, 15, 63, 255 and 1023;
  - the dot counts agree with S-p. 6.

  Move the remark "drawn at L+1, a lower bound" into the caption.
- **P4. Fig. 5(a) (p. 38).** The three truncations are not labelled, and the cubic one is nearly as dark as the heavy D curve. Label them d3t, +d4t² and +d5t³.
- **P5. Figs. 4, 6, 7, 8.** These agree with the text and the tables:
  - Fig. 4: λ1 runs from 4.122 to 0.435, and the systole is 4b(ϑ) with 2.634 at ϑ = 0.
  - Fig. 6: triangle area π/4.
  - Fig. 7: dots and circles agree with Table S2.
  - Fig. 8: slopes 1, ½, ⅓, ½, and the diamonds agree with δcert.
- **P6. Table S1, L ≥ 4 Prouhet rows.** These rows exist only as hashes in the deposit, so I could not check them. Say explicitly that their shared counts are machine checks of the deposited CSV.
- **P7. Abstract (pp. 1–2).** The clause "the proved recoveries of even c3 from values of the trace given below use times shorter than computed spectra resolve" is very hard to parse. The same caveat recurs on pp. 2, 5, 45, 47, 48 and 54; state it clearly once, in Section 6.
- **P8. Remark 2.10 (p. 13).** The identity mΦ_m^{(2k)}(0) = 2·4^k k! m c_{S_k}(π/m) needs a line of derivation or a pointer to the S8 check.

## Recommendation

**Minor revision**, with moderate confidence (about 70%).

- On correctness I would accept. I found no error in any proof or in any figure I recomputed, and the citations are accurate in substance.
- The revision should resolve M2, which is a rigour issue and quickly fixed, and answer M1 in the introduction.
- If the editor weighs M1 heavily for AGAG's scope, a major revision with a refocused introduction is defensible.
- I would not reject.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | A paragraph on the geometric meaning of the counts; promote Proposition 2.17 and Corollary 3.12 among the main results. |
| M2 | Prove or explicitly condition Remark 2.6 and the diameter-free Proposition 4.2(a). Replace ℓ0 from [3] by a self-contained certified bound, noting that any ℓ0 ≥ 0.01 suffices. |
| m1, m2 | Reword the citations of [9]. |
| m3 | One line on the sign in (11); correct the arXiv id of [46]. |
| m4 | Check "trivial" vs "empty" Iso^max against [45]. |
| m5 | Reword the citations of [52], [5], [4], [31], [34], [20], [29], [11]. |
| m6 | Restrict or annotate Theorem 1.2(ii) to 1/2 < α ≤ 1. |
| m7 | Correct the Table 2 caption. |
| m8 | One sentence in Proposition 3.19. |
| m9 | Add the caveat to the statement of Theorem 1.3(i). |
| m10 | Move Conjecture 2.13 and S7 to Section 7. |
| m11 | Two sentences in Appendix E. |
| P1–P8 | Figure labels, captions and abstract wording as stated. |
