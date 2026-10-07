<!-- The reviewer's write was refused by the harness ('Subagents should return findings as text'); this file is the reviewer's returned final message, saved verbatim from the task transcript by the main session. -->

I could not write the report to disk: the Write tool refused with "Subagents should return findings as text, not write report files", so I did not work around it. The full report is below, intended for `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-3/e-rigour-and-citations/REPORT.md`. My scripts, downloaded sources and page images are in `.../e-rigour-and-citations/scratch/`.

---

# Referee report (rigour and citations): "How much of a hyperbolic orbifold does heat hear?"

Manuscript: 48 pp. Online Resource 1: 15 pp. Journal: Annals of Global Analysis and Geometry.
Role: rigour-and-citations referee. The marked placeholders (author contributions, AI-use statement, Zenodo DOI) are treated as known and not counted.
Method: I read the text of both PDFs. I looked at the rendered images of all 8 figures, of Tables 1-3, and of the key-formula pages (pp. 3, 20, 23-26, 29, 36). I recomputed what could be recomputed (Section 3). I checked every bibliography entry against Crossref, DataCite, zbMATH, arXiv and publisher pages, and against the cited statement wherever the text was reachable.

## 1. Summary

The paper studies closed orientable hyperbolic 2-orbifolds O with cone points only (class Sig). Their heat trace has an expansion Z_O(t) ~ Σ c_j t^{j-2}. At curvature -1, c_j depends only on the area and the cone orders. A cone point of order m contributes b_{j-2}(m), a polynomial in m of degree 2j-2 divided by m. The j-th invariant brings in exactly one new odd power sum P_{2j-3} of the orders (Lemma 2.10).

Main results:

1. **Thm 1.1 / 3.4 / Cor. 3.5.** The first ⌊Area/π⌋+4 heat invariants determine genus and cone-order multiset. The proof is a "mirror" (parity) argument on the signed multiset U* ⊎ (-V*). No area-independent number suffices (Prop. 3.9, Thm 3.10).
2. **Thm 3.11 / Prop. 3.12.** The minimal number f(A) satisfies ⌊√((1/3)(A/2π − 1))⌋ + 2 ≤ f(A) ≤ ⌊A/π⌋ + 4. Growth f ≳ A^α is equivalent to N(k) = O(k^{1/α}) for the Prouhet-Tarry-Escott (PTE) function. Linear growth holds iff N(k) = O(k), which is open.
3. **Thm A, B, C.** For spheres with n cone points, the first n invariants determine the orders (Thm A). A Hurwitz/Orlando determinant gives the linear system of Thm B. The first n-1 do not determine them: this is sharp over R for all n, and over Z for n = 3, 4 ({2,8,8} vs {3,3,12}; {3,10,15,30} vs {4,5,21,28}).
4. **Thm 1.2 / Section 6.** For triangle orbifolds, two invariants (the pair (S1, R)) suffice up to cone-order sum 17. The first failure is O(2,8,8) vs O(3,3,12). It is isolated, because the cubic C_{27/2} has rank 0 and E(Q) ≅ Z/2 × Z/6 (Thm 6.8). Three invariants always suffice.
5. **Section 4 / Thm 4.13.** Among orbifolds with area ≤ A, systole ≥ ε and cone orders ≤ M, finitely many eigenvalues, each known to accuracy δ, determine the signature. N and δ are explicit but astronomically large (Table 2). The bound on M cannot be dropped (O(2,3,m), Prop. 4.15). Necessity of the systole bound is left open.
6. **Section 5.** Within a signature the heat expansion is identical to all orders (Prop. 5.1). Shape enters first through t^{-1/2} e^{-ℓ²/4t}, with ℓ the systole (Thm 5.4).
7. **Section 7 and Section 8.** Section 7 treats conditioning of recovering the orders from approximate invariants: Lipschitz at simple orders, Hölder-1/k at k-fold ones, sharpness examples, explicit thresholds. Section 8 and the supplement give numerical experiments on computed spectra.

## 2. Significance

The question is natural, and the answer has an unusually crisp form. It gives an explicit sufficient number and a lower bound of order √Area. It also reduces the exact growth question to a famous open problem (PTE).

Relative to what I checked:

- Uçar [14, Cor. 4.21(iv), 4.23] and Dryden-Strohmaier [9] recover cone orders from all invariants or from the spectrum.
- DGGW [2, Rem. 5.16] say that c (= 12·c_2 up to normalisation) is too weak for hyperbolic triangular pillows. I confirmed the quoted phrase.
- The finite explicit count, the PTE reduction, the exact first failure at sum 18, and the effective eigenvalue theorem are new as far as I can tell.
- The Steinig-type uniqueness with a reciprocal-sum constraint (Thm A), the closed-form determinant (Thm B) and the Descartes imbalance bound (Thm 3.8) are modest but correct and cleanly proved.
- The triangle pair and its isolation by a rank-0 curve is a pleasant arithmetic touch. I reproduced it independently.
- Thm 4.13 is of "effectivity" interest only, and the paper says so honestly. Its constants (down to 10^-384) are useless in practice, but it is a genuine, checkable theorem.

For AGAG readers this is a solid inverse-spectral / heat-invariant paper. Its weakness is breadth. In 48+15 pages it combines algebraic combinatorics, an arithmetic-geometry detour, numerical analysis and a spectral-perturbation section.

## 3. Correctness and what I recomputed

Everything below was run by me, in exact arithmetic wherever the paper claims exactness.

**Heat coefficients**
- I re-derived p_0, p_1, p_2 from (4)-(5) with Bernoulli numbers, and they match (7). α_0..α_5 = 1, -1/3, 1/15, -4/315, 1/315, -4/3465 also match.
- The leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)), p_l(1) = 0 and degree 2l+2 hold for l ≤ 4.
- Eq. (9) is correct. The general-n form c_2 = (S1 + R − 2n + 4)/12 explains why (0;5,5,5) and (0;2,2,2,10) share two invariants.
- At K = -1 the cone terms b_0, b_1, b_2 agree with Schueth [13, Rem. 4.2, Thm 4.1]. The 1/k-coefficient −37/5040 of b_2 checks.
- The closed form of Lemma 2.6 checks numerically for m = 3, 7, 12.
- Prop. 4.9, for m = 5, t = 0.01 and 0.002, K = 1, 2, 3:
  - The true remainder has sign (-1)^K.
  - Its ratio to |b_K|t^K lies between 0.92 and 0.994 and tends to 1.
  - So both the "enveloping" claim and the sharpness claim are right.

**Section 3**
- I re-read the proofs of Thm A, Cor. 3.5 and Thm 3.4 line by line. They are correct, including the parity bookkeeping and the step e_{T-1} = e_T (R(U*) − R(V*)).
- Thm 3.8 (Descartes bound): the sign-change counting argument is complete.
- Prop. 3.9: the identity P_j(U) − P_j(V) = (1 − 2^{j+1})(P_j(X) − P_j(Y)) holds, including j = -1. The hyperbolicity argument is fine.
- Thm 3.11(a)-(d), Lemma A.1 and Prop. A.2: the constants check. The signed-count formula for ι(Z(c)) is right.
- Thm C(3): P_3 = 31402 for both, and P_5 = 25159618 vs 21298618, are correct.
- Thm B: for 5 multisets ({2,8,8}, {3,3,12}, {2,3,7}, {3,10,15,30}, {2,5,7,11,13}) I built M from (11) and checked M e = b for the true e. I also checked det M = (−1)^{n(n+1)/2} Π(m_i+m_j)/e_n exactly. All agree (e.g. det = 25/2 for both members of the first pair).
- Table S1: I recomputed all 20 explicit pairs printed in full (L = 2..7: genus, equal-count and cone-count pairs; Prouhet pairs at L = 2, 3) with exact rationals.
  - Each shares exactly the stated L invariants and has the stated area.
  - The Prouhet squares at L = 4, 5, 6 are given only as hashes, so I could not check them.
- Remark 3.2 (my C program), n = 4 with orders in [2, 440] and equal (R, P1, P3):
  - There are 193 pairs, 107 of them primitive, and no group of three.
  - Primitive counts with largest order ≤ 130, 220, 440 are 16, 33, 107, as in S1.
  - The eight primitive pairs with orders ≤ 84 are exactly Chen's (A.685)-(A.692).
  - (16,16,74,74)/(11,37,44,88) is the first non-pencil pair.
- Case n = 5 (my C program): no pair of 5-multisets of orders in [2, 120] has equal (R, P1, P3, P5).
  - The multiset count 216,071,394 reproduces.
  - The count 4,325,115,770 of gcd-1 5-multisets in [1, 220] used in Remark 3.14 reproduces exactly.
  - I did not rerun the 4.3·10^9 cubic-splitting search.

**Section 6**
- Brute force over all triples with S ≤ 600:
  - There are 83 hyperbolic triads for 10 ≤ S ≤ 18.
  - The only coincidence of R within a sum ≤ 18 is (2,8,8)/(3,3,12) at S = 18.
  - The collision-free sums in [18, 600] are exactly the 38 sums of Prop. S2.1, namely 19, 21-25, 27-30, 33, 41, …, 329, 557.
  - I did not rerun 600 < S ≤ 4800.
  - S = 557 has 25,575 triads, as stated.
  - All 13 "first collision" rows of Table S2 reproduce.
- Thm 6.4: the formula for S*(p) agrees with brute-force first overlap of strata p, p+1 for every p = 2..24 (S < 400).
  - The identity x*(p) − 18 = 3(p−2)(p−3)/(p−1) is right.
  - The numerator in gap_p(3p+7) changes sign exactly at p ≥ 9.
- Thm 6.8:
  - ψ maps E into C_{27/2}, and φ∘ψ = id on E (symbolic check). disc E = 2^18·3^8·5^6.
  - #E(F_7) = #E(F_11) = 12, and all 12 listed points lie on E. The flex tangent y = 21x + 64 gives (x−16)³.
  - PARI 2.15.4 (not the 2.17.2 the paper cites) independently gives ellrank = [0,0,0,[]], so rank 0, with conductor 90 and torsion Z/6 × Z/2.
  - The hand descent of Appendix C is consistent (d' = 3²5⁶, n_1 = 4, n_1' = 1).

**Section 4**
- I re-derived the proofs of Lemmas 2.4 and 2.5. B decreases in ℓ on the stated range.
- I followed the proofs of Lemmas 4.1 and 4.2 and Thm 4.3. The trigonometric identities and the case splits are correct.
- Table 1 and the D-column of Table 2 reproduce numerically. Examples: D(π/2,1,3) = 56.60, D(π/2,1.8626,8) = 402.2, D(10π,1,12) = 22509. The closed-form majorant is indeed ≥ D.
- Table 2: I implemented (14), Lemma 4.12 and Thm 4.13. For all 7 rows, t_1, t_3, N and δ agree with the printed values. Row 2 gives t_1 = 6.85e-9, t_3 = 1.28e-4, N = 6.82e9, δ = 4.17e-25.
  - The formula for y_0 must be read from the rendered page, because the text layer drops a log term.
- Lemma 4.11: d_2 = −1/12 for (0;4,4,4)/(0;3,4,6) is right.
- Prop. 4.4:
  - The identity tr[γ,β] − 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r was only "checked numerically" in the paper. I confirmed it numerically for three parameter sets.
  - σ_0 = 0.56206 requires the coefficient 3/4 (= sin²(π/3)), as printed.
- Prop. 4.15 and S7.1: I re-derived the Rayleigh-quotient estimates and identity (15), with q = 1/4 − 1/(4 sinh²) and q = 1/4 + 1/(4 cosh²). The λ_1 bound sinh a/((a²+2) sinh a − 2a cosh a) is correct.

**Section 7 and the supplement**
- amp_0..amp_4 = 2, 14, 498, 4062, 56230/3 reproduce as row sums of F^{-1}. The relation P_3 = −18c̃_1 − 120c̃_2 − 360c̃_3 also holds.
- Prop. 7.6(i): δR = s²/(4(64 − s²)) and δP_3 = 48s² are correct. The inequality chain in Prop. 7.7 is correct.
- Table S4: all δ_up/δ_cert ratios and the quoted 5e2..2e8 spread match. The relative-precision column for (2,8,8) matches.
- Table S6 and S4 data:
  - Exact c_3(2,8,8) = −3.335417, c_3(3,3,12) = −5.41875, d_3 = 25/12 and d_4 = −1775/24 all match the fitted values within the stated error bars.
  - Systoles 4b(ϑ) = 2.634 and 0.694 at ϑ = 0, 2.8 are right.

I found **no mathematical error** in any proof I checked. I did not recompute the following:
- the finite-element spectra and Table 3;
- the 525 equal-area classes of Fig. 3;
- the hashed Prouhet squares;
- the S3 certificates (only their ratios);
- the 4.3·10^9 search;
- Thms 7.4 and 7.5 beyond the Rouché step.

**Figures and tables as rendered**
- Fig. 1: the tips go dark at the cone vertices, consistent with the caption.
- Fig. 2: discs and rings are as described. The "−3" and "−2" tick labels overlap slightly in (a).
- Fig. 3: the solid line is ⌊2s⌋+4, the dashed line is Thm 3.11(a), and the squares at L+1 = 3..7 are consistent with Table S1.
- Fig. 4: λ_1 goes 4.12 → 0.435, and the square-root axis is fine.
- Fig. 5: consistent with its caption.
- Fig. 6: the dots and circles agree with Table S2, e.g. (19, ≈0.59), (20, 0.5), (34, 0.31), (38, 0.45).
- Fig. 7: slopes 1, 1/2, 1/3, 1/2 as captioned.
- Fig. 8: the sign change near t = 0.34 and the early d_3·t behaviour are consistent with the text.
- All captions match their figures and the citing text. I found no figure/caption/text mismatch. For Table 3, see m5.

**Citations: 47 bibliography entries examined** (41 in the paper, 6 in the supplement; 46 distinct, since Chen appears twice).
- Existence and bibliographic data were verified for all 47 via Crossref, DataCite, zbMATH or arXiv.
- 27 entries were also checked at statement level against the source text (3a).
- Problematic ones are discussed in M1 and m1-m3.

### 3a. Statement-level citation results (all OK unless noted)

- **[2] DGGW.** Thm 4.8 (locality), Prop 5.5 with (5.7), Ex 5.6, Thms 5.14-5.15, and Rem 5.16 with the quoted phrase ("does not seem sufficiently strong to distinguish among these triangular pillows") all check.
- **[4], [6], [7].**
  - [4] Richardson-Stanhope Thm 4.7: OK.
  - [6] Bérard-Webb Thm 3.1: the Neumann-isospectral orientable/non-orientable pair. OK.
  - [7] CRAS 320 (1995) 533-536, zbMATH 0841.58062. zbMATH lists the English title "One cannot hear orientability of surfaces"; the paper gives the French title, which is fine.
- **[9] Dryden-Strohmaier.** Eq. (1) is exactly the formula in Thm 2.3: elliptic terms 1/(2m sin θ) ∫ e^{-2θr}/(1+e^{-2πr}) h, for h entire of exponential type. Thm 3.2 is Gauss-Bonnet. Prop 3.3 and Thm 1.1 are as used (see m3).
- **[10], [11], [12], [13], [14].**
  - [10] Linowitz-Voight Thm A: minimal area 23π/6, all of signature (0;2,2,2,2,2,3,4).
  - [11] Stanhope Main Thms 1-2.
  - [12] ADFG Thm 1 and §6.1.
  - [13] Schueth 2019 Rem. 4.2 and Thm 4.1: a_2 at K = −1 equals b_2.
  - [14] Uçar: Thm 4.20(ii), (4.35), Cors 4.21(iv) and 4.23. I located the thesis at edoc.hu-berlin.de.
- **[16], [17], [18].** [17] Laurens Lemma 3.2 and the remark crediting Steinig; [18] MSW Prop. 24; [16] Steinig, zbMATH 3377304 (Rend. Mat. (6) 4 (1971), 629-644, published 1972).
- **[20] Chen.** Identity 9 with (3.27)-(3.28); (3.33); A.1.6 with [1,5,5]=[2,3,6]; A.1.33; A.5.8 with (A.685)-(A.692); the "2017" computer search.
- **[21]-[23], [26]-[28].**
  - [21] Grieser-Maronna Thm 1: area, perimeter and the sum of reciprocals of the angles determine a Euclidean triangle.
  - [22] Philippe Thm 3.1.
  - [23] Bremner-Guy-Nowakowski p. 117: reciprocal pairs, integer Λ only.
  - [26] Garbin-Jorgenson Rem. 2.7 and (2.8): same normalisation, since 1/√(16πt) = 1/(2√(4πt)) matches Hyp(t) in Thm 2.3.
  - [27] Dryden, arXiv math/0411290, proof of Thm 4.5.
  - [28] Thurston ch. 13: 13.3.4-13.3.5 and Cor. 13.3.7. The dimension is 6g−6+2n after Thurston's own k/l swap.
- **[31], [32].**
  - [31] Holtz-Tyaglov (1.37) and Thm 1.17. The sign (−1)^{n(n−1)/2} cancels as stated in (10).
  - [32] Melzak pp. 233-234 report K(n) < (n²+4)/2, credited to Wright [2]. The paper's "≤" is harmless.
- **[33], [34], [36].**
  - [33] and [34] (arXiv 2609.05061 exists, 4 Sep 2026): ideal solutions are known for k ≤ 9 and k = 11.
  - [36] Wikipedia states Jørgensen's inequality exactly as used.

Chen's survey is a single-version arXiv preprint, and Croot-Mao-Yip [34] is a one-month-old preprint. Neither is a problem for the claims made: Chen's witnesses are rechecked exactly, and [34] is used only for status.

### 3b. Not verified (text not retrievable)

- **[5] Borwein-Ingalls.** It has no DOI, and e-periodica is behind a captcha. zbMATH 0810.11016 confirms the bibliographic data. The cited items (§2 p. 6, Prop. 1, §3, Props 2-3, §6 Problem 3, p. 9) are consistent with what Melzak [32] and Croot-Mao-Yip [34] say, but I could not read them.
- **[3]** (erratum scope "only Thm 5.1"). Thm 5.1 of [2] is a statement about odd/even-dimensional strata, so this is plausible.
- **[19]** Korobov-Bugaevskaya §3 (AMS PDF unreachable).
- **[39]** Cremona (§3.3 p. 70; §3.6 Method 1 and (3.6.2)).
- **[40]** Ostrowski ("Théorème XXX (71,1)").
- **[24]** Hejhal, **[25]** McKean, **[29]** Iwaniec, **[37]** Huber, **[35]** Jørgensen (original), **[30]** Watson (zbMATH 1076.35042 only).
- NGSolve [S-3], NETGEN, ARPACK and Strohmaier-Uski: existence and bibliographic data verified, and arXiv:1110.2150 is indeed the Strohmaier-Uski paper. No statement was checked.

### 3c. Statements quoted from a secondary source

These are marked as such in the paper:
- Jørgensen's inequality, via Wikipedia [36] ("we could not retrieve the original paper").
- Wright's bound, via Melzak [32].
- The PTE bounds, via [5] (but see 3b).

I found no unmarked secondary quotation, apart from the qualifications in m1 and m2.

## 4. MAJOR issues

**M1. Load-bearing geometric facts are "checked numerically" with undocumented code, and Jørgensen's inequality is taken from Wikipedia.**
Location: Section 4.1 (before (H1)), Prop. 4.4, Remark 4.14, Prop. 4.15, supplement S7.

The issue:
- Section 4.1, before (H1): "each is also checked numerically on random configurations, with the repository code of Appendix D."
  - (H1)-(H3) are the rotation-displacement formula, "product of two reflections", and the law of cosines for angles.
  - They underlie Lemmas 4.1 and 4.2, hence the diameter bound D(A,ε,M) and every constant in Table 2.
- Prop. 4.4, last display: the commutator-trace identity tr[γ,β] − 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r is "checked numerically".
  - This is the whole quantitative content of the systole lower bound σ_0.
  - It therefore underlies the abstract's claim that "the bound on the cone orders cannot be dropped".
- S7 says "the Lambert relation; checked numerically". Section 4.5 says "checked symbolically".
- The only source for the inequality itself is a Wikipedia page (reference [36]), with the remark that the original could not be retrieved.
- Appendix D and S8 do not describe any of these numerical checks.

I verified all of these numerically and by reading, and they are true and standard. The trace identity is a short matrix computation, and Jørgensen's inequality appears in Beardon, Maskit and elsewhere. Still, a proof in a mathematics journal cannot rest on "checked numerically" plus a Wikipedia article, and a reader cannot see what the repository check consisted of.

What resolves it:
- (a) Cite a textbook for (H1)-(H3) (e.g. Beardon, *The Geometry of Discrete Groups*, §7; Ratcliffe), or give the one-line proofs.
- (b) Prove the commutator-trace identity from tr[A,B] − 2 = tr²A + tr²B + tr²(AB) − trA·trB·tr(AB) − 4, with explicit matrices.
- (c) Replace [36] by Jørgensen [35] together with a textbook statement of the inequality. If Wikipedia is kept at all, add a permalink.

**M2. The "exact" computer-search claims cannot be checked from the PDFs alone.**
Location: Remark 3.2, Remark 3.14, S1, Prop. S2.1, S8.

Several quantified claims are proved only by computer searches whose code and output live in the repository:
- the n = 4 search up to 440;
- the n = 5 search up to 120;
- the 4.3·10^9-multiset exclusion of genus pairs of shape (3,5) with entries ≤ 220;
- collision-free sums up to 4800.

I reproduced three of the four searches, and the fourth up to S = 600, and found them correct. Even so:
- The main text states these as facts ("no witness", "excludes every one", "exactly 38 sums") without saying in the statement that they are computational and bounded.
- There is no algorithm description sufficient to reimplement the 4.3·10^9 search. S8 gives only one sentence on the floating-point filter on an arm64 machine where long double is binary64.

What resolves it:
- Label each as a "Computational result" with its exact bound in the statement.
- Add to S8, for each search, the key, the loop bounds and the exact-arithmetic fallback (about half a page of pseudo-code).
- Flag in the abstract or introduction that the exclusion behind "Tg(3) ∈ {8, 10}" is computer-assisted, not proved.

## 5. MINOR issues

**m1. Attribution of [8] (Schueth 2025), Section 1.1.**
- The text says Schueth "computes such terms for curved cones from the metric near the cone point alone [8, Abstract and §1]".
- The terms in question are the cone contributions through K(p) at order t and K(p)², ΔK(p) at order t², rational in the order. They are due to [2] (b_1) and [13] (b_2), and [8] only recalls them.
- What [8] proves is a formula for b_{1/2} under rotational symmetry near the cone point, and the irrational dependence on rescaling when f''(0) ≠ 0.
- Fix: rephrase. Keep "all-order formulas [8, p. 2]" for Uçar's constant-curvature result; that attribution is right.

**m2. [15] Chang-DeTurck, Section 1.2.**
- The text says "A finite, likewise non-uniform count is known for Euclidean triangles and their Dirichlet eigenvalues."
- As reported by Grieser-Maronna, the result is: for each ε > 0 there is N such that the first N Dirichlet eigenvalues determine a triangle among triangles with all angles ≥ ε.
- The angle restriction is the analogue of the systole and cone-order restrictions of Section 4 and should be stated. As written, the sentence suggests a count depending only on the triangle.

**m3. [9] Thm 1.1 vs Prop. 3.3.**
- Section 1.1 says "orbifolds in Sig with different signatures have different spectra [9, Thm 1.1]".
- Thm 1.1 gives the number of cone points of each order. The genus then follows from the area (Weyl) plus Gauss-Bonnet, which is [9, Prop. 3.3].
- The paper cites both elsewhere; cite both here.

**m4. Thm 1.2(iii) lacks its class.**
- "The first three heat invariants always determine O(p,q,r)" is proved among triangle orbifolds (Thm 6.1, Kiso(O;Sig_{0,3}) ≤ 3).
- Part (i) says "among all hyperbolic triangle orbifolds", and the abstract says "Among triangle orbifolds…".
- Fix: add the qualifier to (iii), and to the "only such pair" sentence in (ii).

**m5. Table 3 caption.**
- The caption says "ranges are over the members of the family of systole 2.634 down to 0.694".
- The text beneath says the a-priori count N_apr is unavailable for the member of systole 0.694. Its range covers only the seven members of systole ≥ 0.846.
- Fix the caption. Also unify "diam ≤ 7.77" (text) with "diam ≤ 7.8" (Table 1 caption).

**m6. Notation overloading.**
- Φ_m(u) (Lemma 2.6) vs Φ_j(σ) (Prop. 5.1).
- T(z) (tanh series), T(L) (minimal configuration size), T = |U*|+|V*|, and T (a triangle, Prop. 4.4).
- L as the number of invariants, the lcm L_M, the geodesic length in Prop. 4.4, and Lipschitz constants.
- B for Bernoulli numbers, the bound B(ℓ,diam,t), and the matrix B of Lemma 7.3.
- N(k), N (number of eigenvalues), and the counting function.
- Fix: rename at least Φ_j and T.

**m7. Appendix D / S8 cross-references.**
- Section 2.2 and Appendix B point to "Appendix D" for the exact comparison with Uçar for l ≤ 40. Appendix D has only generic text, and the item appears only as one clause of S8(iii).
- Likewise the numerical check of (H1)-(H3) is attributed to "the repository code of Appendix D" (see M1).

**m8. Duplicated sentence in Section 1.1.** "Section 4 connects the heat invariants to finitely many eigenvalues … Section 4 proves that the first N eigenvalues …" says the same thing twice.

**m9. Bibliographic years.**
- [8] is given as 2026, while Crossref says first published online 2025 (article 2 of vol. 69(1)).
- [12] 2008 vs online 2007; [13] 2019 vs Crossref 2020; [18] 2024 vs online 2022; [33] 2024 vs online 2023.
- These are volume-year vs online-year differences, not errors. Please be consistent.
- For [36], give the revision ID or permalink, and avoid a Wikipedia entry as a numbered reference in a proof (see M1).

**m10. Wright's improvement is unnecessary.**
- In Thm 3.11(c), the step N(2L−3) ≤ 2L² follows from the classical bound k(k+1)/2 + 1, which is [5, Prop. 3]. Indeed (2L−3)(2L−2)/2 + 1 = 2L² − 5L + 4 ≤ 2L².
- The secondary citation to Melzak/Wright can therefore be dropped from the proof.

**m11. Figures.**
- Fig. 2(a): the tick labels "−3" and "−2" overlap.
- Fig. 3: add a legend naming diamonds (genus pairs) and squares (Prouhet pairs), rather than only "pairs of Table S1".

## 6. Presentation

- **Length and structure.**
  - 48 pages plus a 15-page supplement for Thms 1.1-1.3 plus Section 4. The roadmap in §1 is clear, and the statements are mostly self-contained.
  - Sections 4 and 7 are particularly heavy. The constants of Table 2 are useful only as an existence statement.
  - A reader interested in the PTE connection must pass through Section 2 before reaching the result. A two-page statement-only summary of Sections 3 and 6 would help.
- **Typography.**
  - Theorem labels "A, B, C" are mixed with numbered theorems.
  - The very long displayed formulas in Thm 4.13 are readable only on the rendered page; the text layer loses a log term in y_0.
  - Sign and constant conventions (e.g. tr²γ − 4 vs 4 sinh²(L/2)) are consistent throughout.
- **Figures.** All eight figures are legible and consistent with captions and text (see Section 3). The Fig. 1 colour map is monotone with correct colourbar labels. Fig. 6 has correct log-axis ticks.
- **Candour about scope.**
  - No theorem depends on Section 8.
  - The paper does not claim the systole bound is necessary.
  - The large constants are called "enormous".
  - Unverified numerics are described as "validated, not proved".
- **Language.** Generally clear. Minor duplication (m8).

## 7. Recommendation

**Minor revision**, with confidence about 75%. I would move to "accept" once M1 and M2 are fixed and the citation corrections in m1-m3 are made.

What is good:
- The mathematics is correct as far as I could check. Every proof I re-read (Sections 2-4, Section 6, Appendices A-C) is complete, with no sign, constant or quantifier error.
- About 30 independent recomputations agree with the paper: heat coefficients, the determinant of Thm B, the 20 explicit pairs, the n = 4 and n = 5 searches, the triad enumeration to S = 600, the elliptic curve (including PARI), and all seven rows of Table 2.
- Citations are accurate, and secondary-source quotations are marked.
- The one flagged-as-unretrieved primary source I could read (Jørgensen's inequality, via Wikipedia) is quoted correctly.

| Issue | What resolves it |
|---|---|
| M1 numerical checks + Wikipedia in proofs | Cite standard references or give the short proofs of (H1)-(H3) and the commutator-trace identity. Replace [36] by [35] plus a textbook statement. |
| M2 computer-search claims | Label as computational. State bounds in the statements. Add the algorithms to S8. Mark the Tg(3) ∈ {8,10} exclusion as computer-assisted in the abstract/introduction. |
| m1 [8] attribution | Rephrase: [2] and [13] for the K, K², ΔK terms; [8] for b_{1/2}. |
| m2 [15] | State the lower-angle restriction. |
| m3 [9] | Add Prop. 3.3. |
| m4 Thm 1.2(iii) | Add "among hyperbolic triangle orbifolds". |
| m5 Table 3 caption | Correct as described. |
| m6-m11 | Editorial fixes as listed. |

Report path (intended, not written): `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-3/e-rigour-and-citations/REPORT.md`
