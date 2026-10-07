<!-- Provenance: reviewer (d) could not write files; this is its returned report text, saved verbatim by the orchestrating session (its run was interrupted by a connection error and resumed once to return the report). -->

# Referee report

**Manuscript:** "How much of a hyperbolic orbifold does heat hear?" (37 pp.), with electronic supplementary material (12 pp.)
**Journal:** The Journal of Geometric Analysis

## 1. Summary

The paper studies closed orientable hyperbolic 2-orbifolds whose only singular points are cone points (the class Sig). It asks how many of the small-time heat-trace coefficients c_1, c_2, … are needed to determine the signature (g; m_1, …, m_n).

**Analytic input.** The analytic input is classical: the Selberg trace formula with elliptic terms, applied to the heat kernel.
- Each c_j equals α_{j−1}·Area/4π plus a sum over cone points of an explicit rational function b_{j−2}(m). The authors re-derive these coefficients in closed form for every order (Lemma 2.6, Proposition 2.7).
- They observe that c_j brings in exactly one new odd power sum, P_{2j−3}, of the cone orders. The area term brings in the reciprocal sum R (Lemma 2.10, eq. (8)).
- From here on the problem is algebraic. Comparing two orbifolds becomes a vanishing-moment problem for the signed multiset m ⊎ (−m′), padded with 1s.

**Main results.**
- **Signature from finitely many invariants (Theorem 1.1, Section 3).**
  - The first ⌊Area/π⌋+4 heat invariants determine the signature (Corollary 3.5, via the separation Theorem 3.4). No number independent of the area suffices (Theorem 3.10).
  - The least sufficient number f(A) satisfies roughly √(A/6π) ≲ f(A) ≤ A/π+4.
  - Polynomial growth of f with exponent α is equivalent to N(k) = O(k^{1/α}), where N is the Prouhet–Tarry–Escott function (Theorem 3.11).
- **Spheres with n cone points.** n invariants suffice (Theorem A). n−1 do not: there are integer counterexamples for n = 3, 4, and real local non-injectivity for all n (Theorem C). A closed-form determinant (Theorem B) controls the linear system that recovers the elementary symmetric functions.
- **Triangle orbifolds (Section 5).** Two invariants are equivalent to (S_1, R).
  - Elementary stratum and interval estimates prove that two invariants separate all triads of cone-order sum ≤ 17. The first collision is O(2,8,8) and O(3,3,12) at sum 18 (Theorems 5.4–5.7).
  - Three invariants always suffice (Theorem 5.1).
  - The minimal pair and its multiples are isolated, because C_{27/2} is a rank-0 elliptic curve with torsion Z/2 × Z/6 (Theorem 5.10).
  - The collision-free sums up to 4800 are listed (Proposition 5.9, computational).
- **What heat cannot hear (Section 4).** Heat invariants are functions of the signature, so K_iso = ∞ off the triangle orbifolds. For two traces of the same signature, the paper gives an explicit bound on their difference and shows that the exponent e^{−ℓ²/4t} and the factor t^{−1/2} are attained (Theorems 4.4–4.5).
- **Stability (Section 6).** Recovering the cone orders of a sphere from perturbed c_1, …, c_n is Lipschitz at simple orders and Hölder-1/k at k-fold orders. Explicit rounding thresholds are given, sharpened by an exact-arithmetic certificate that lives in the supplement.
- **Numerics (Section 7 and supplement).** Finite-element spectra of the minimal pair and of a one-parameter (0;3,3,3,3) family illustrate the results.

## 2. Significance and novelty

**Strengths.** The paper is careful and, within its scope, clean. To my knowledge the following are new:
- an explicit uniform count, ⌊Area/π⌋+4;
- the exact location of the first failure of two invariants on triangle orbifolds, proved by hand rather than by search;
- the isolation of the minimal pair through the rank of an explicit elliptic curve;
- a two-sided reduction of the growth question to N(k).

Theorem 5.10 turns DGGW's remark that c "does not seem sufficiently strong" (their Rem. 5.16) into a precise statement. The proofs are short and essentially complete. The authors are frank about what is classical, what is computational and what is open.

**Concerns about significance for JGA.**
- **Little new analysis.**
  - The analytic part is the trace formula plus a re-derivation of known coefficients. Uçar computed all orders; DGGW and Schueth computed the low orders.
  - Section 4 is a direct consequence of the trace formula. Its constant is admitted to be "qualitative" and "loose".
  - After Lemma 2.10, Sections 3 and 5 are algebra and elementary number theory: Newton's identities, Descartes' rule, Prouhet–Tarry–Escott (PTE) and a 2-descent.
- **Theorem 1.1(ii) only relocates the question.** Once heat invariants are identified with odd power sums, the PTE equivalence is close to a restatement. The authors say so themselves.
- **The stability theory has little spectral meaning.** Theorem 1.3 measures errors in the heat invariants. These are asymptotic coefficients that finitely many eigenvalues do not determine; in the paper they are estimated by fits with heuristic error bars.

The authors should argue explicitly why geometric analysts should care. The editor may weigh whether a venue at the interface of spectral geometry and number theory, or of experimental mathematics, fits better. This is a judgment about scope, not about correctness.

## 3. Correctness

I recomputed independently everything I could, using my own code: exact rationals, sympy, mpmath, PARI/GP via cypari2, and two C programs. I did not use the authors' repository.

### Section 2: heat coefficients

| Check | Method | Result |
|---|---|---|
| Lemma 2.6 | Defining sum vs closed form vs (4), m = 3, 5, 12, first four Taylor coefficients, 40-digit arithmetic | Agree to 1e−40 |
| Lemma 2.8 and (7), l ≤ 3 | p_0…p_3 computed exactly | As stated, including p_l(1) = 0, degree 2l+2, leading coefficient \|B_{2l+2}\|/(2(l+1)!(2l+1)) |
| α_0…α_4 | Exact computation | 1, −1/3, 1/15, −4/315, 1/315 |
| Series vs trace formula | Numerical quadrature of the identity term I(t) and elliptic term E_m(t) at t = 0.005 | I(t) agrees to 15 digits. E_3 agrees to 1e−11. E_8 and E_12 differ by 4e−7 and 3e−5, consistent with truncating a divergent series |
| b_0, b_1, b_2 at K = −1 | Compared with Schueth's Thm 4.1 / Rem. 4.2 | Agree |
| Formula (9) | Exact, several triads | Confirmed |
| Section 7 data | Exact | c_1 = 1/8 and c_2 = 67/48 for both orbifolds; d_3 = 25/12, d_4 = −1775/24, d_5 = 153025/48. Exact c_3 values (−1601/480, −867/160) lie inside the Table S6 error bars. The fitted coefficients deviate by 0.42 and 0.52 error bars, as claimed |

I checked the proofs of Lemmas 2.4, 2.5 and A.1 line by line and found no error. In Lemma 2.5 this covers the integration by parts, 1 + 2t/(ℓ−t) = (2+3ℓ)/(2+ℓ) at the end of the range, and the log-derivative in ℓ. In Lemma A.1 it covers the a-priori count #{λ_j ≤ x} = O(x) from a test function with no hyperbolic terms, and dominated convergence.

### Section 3

**Proofs checked, no error found.**
- Lemma 3.1, Theorem A, Lemma 3.3, Theorem 3.4, Corollary 3.5.
- Theorem 3.8 (the sign-change and gap counting).
- Proposition 3.9, including P_j(U) − P_j(V) = (1 − 2^{j+1})(P_j(X) − P_j(Y)), valid also for j = −1.
- Lemma B.1 (the pigeonhole exponent count), Proposition B.2, and Theorem 3.11(a)–(e) with its constants, for example N(2L−3) ≤ 2L².

**Theorem B.** I built M from (11) symbolically for random rational multisets with n = 2, 3, 4, 5. In each case det M = ς_n ∏(m_i+m_j)/∏m_i, and the true e solves the system.

**Theorem C(3).** Both 4-multisets have R = 8/15, P_1 = 58, P_3 = 31402. Their P_5 values are 25159618 and 21298618. For the triangle pair, P_3 = 1032 and 1782. All confirmed.

**Examples and Table S1.** For each pair below I computed the exact areas and the exact number L of shared invariants. All agree with the paper.
- (1;15) and (0;3,3,5,5): s = 14/15, L = 2.
- (1;15,15,15) and (0;3,3,5,7,7,21): s = 14/5, L = 3.
- (0;3,10,15,30) and (0;4,5,21,28): s = 22/15, L = 3.
- (0;4,4,5,5,6,12,12) and (0;2,2,2,3,10,10,10,10): s = 113/30, L = 3.
- (0;5,5,5) and (0;2,2,2,10): s = 2/5, L = 2.
- (1;2,14,35) and (0;6,7,7,10,21): s = 12/5, L = 2.
- Table S1: the cone-count rows with L = 4, 5, 6, 7, the equal-count row with L = 4, and the genus rows with L = 4, 5.

**Remark 3.2.** I searched all 12,082,785 four-multisets with orders in [2,130], keyed on the exact triple (P_1, P_3, R). I found exactly 16 primitive witnesses (19 pairs in all). Both witnesses without a pencil splitting, (16,16,74,74; 11,37,44,88) and (11,21,99,99; 9,51,51,119), are among them. This is consistent with "16, of which 14" in S1.

**Search sizes.** The stated sizes are correct:
- C(123,5) = 216,071,394;
- the number of gcd-1 five-multisets in [1,220] is 4,325,115,770 (by Möbius inversion).

I did not rerun the searches up to 440 or for n = 5.

### Section 5

**Small sums.** There are exactly 83 hyperbolic triads with 10 ≤ S ≤ 18. R values are pairwise distinct within every sum ≤ 17. The only coincidence at S = 18 is (2,8,8) and (3,3,12). This confirms Theorems 1.2(i)–(ii), 5.6 and 5.7.

**Theorem 5.4 algebra.** All of the following are confirmed exactly:
- the factorisation of φ_p − τ_p;
- gap_p(3p+7) for p = 2..11;
- the odd-parity gaps 1/840, 1/2310 and 1/10296;
- all seven values at S*(p)+1;
- R⁻_{18,3} = 101/168 and R⁺_{18,4} = 3/5.

**Overlaps and Table S2.** By enumeration, the first overlap equals S*(p) for 2 ≤ p ≤ 14 and persists up to S = 400. Every row of Table S2 is reproduced, including the colliding pairs. The first non-adjacent collision is (5,15,15) and (7,7,21) at S = 35.

**Proposition 5.9.** My exact C search over 18 ≤ S ≤ 4800 returns exactly the 38 listed sums. S = 557 has 25,575 triads. Of the other sums, 3962 have a collision obtained by scaling from a divisor, and 783 need an explicit pair. All as stated.

**Theorem 5.10.** Checked with sympy and PARI:
- ψ maps E into C_{27/2}, and φ∘ψ = id on E. The minus sign inside φ's second coordinate is essential, and it is printed correctly.
- disc E = 2^18·3^8·5^6.
- φ(1:4:4) = (−24, 360), φ(1:0:0) = (216, 5400), and the images of all twelve listed points are as stated.
- The torsion subgroup is Z/6 × Z/2, with #E(F_7) = #E(F_11) = 12, and the point orders are as stated.
- d′ = 3²·5⁶.
- PARI's `ellrank` returns provable rank 0.
- No other positive primitive points with coordinates ≤ 120.

The theorem is correct.

**Systoles.** Enumerating reflection-group words gives the shortest lengths 2.2568, 2.8816, 3.0571 for (2,8,8) and 1.8626, 2.9807, 3.4027 for (3,3,12), as in S4. For the family of Figure 4, 4·arsinh(√(½e^{−ϑ})) gives 2.634 at ϑ = 0 and 0.694 at ϑ = 2.8, as stated.

### Section 6

**Constants.** I rebuilt **F** exactly. Its absolute row sums amp_0…amp_4 are 2, 14, 498, 4062, 56230/3. The P_3 row is (−18, −120, −360). The values ζ_3 = 1, ζ_4 = 79/3, ζ_5 = 14048/15 are correct.

**Table 1.** All eleven δ_thm entries are reproduced from the definitions: 3.803e−7, 1.189e−7, 4.49e−7, 9.35e−7, 9.97e−8, 4.02e−11, 3.15e−11, 1.49e−9, 4.74e−10, 2.03e−9, 2.73e−12. The maximum of cond is 3.511, as stated. I did not recompute δ_cert or δ_up.

**Proofs checked, no error found.**
- Theorem 6.4(b) (Neumann-series bound).
- Theorem 6.5 (the Rouché constant 2^{1−n}3^n ε).
- Theorem 6.8.
- Proposition 6.6(i): δR = s²/(4(64−s²)), δP_3 = 48s².
- Remark 6.7: Σ d_i²(3a+d_i), and 498 + 42a² = amp_2 + 3a²·amp_1.
- The logic of Proposition S3.1 (Perron-vector argument, Neumann bound, Rouché).

**Theorem 4.4 constant.** For the (0;3,3,3,3) family, C exceeds the attained leading constant by factors between about 20 (ℓ = 0.69, diam = 1) and about 10^5 (ℓ = 2.63, diam = 3).

### Citation spot-checks

I checked 23 items against the sources: arXiv versions, Borwein's preprint, Cremona's online book, and the zbMATH review for Troyanov.

**Verified, with numbers and content matching:**
- Dryden–Strohmaier [7]: Thm 1.1, Prop. 3.3, Thm 3.2, p. 68 (cone point ↔ elliptic classes 1 ≤ l ≤ m−1), and the source of the trace formula.
- DGGW [2]:
  - Rem. 5.16, quotation exact.
  - Prop. 5.5, (5.7), (5.10), Thm 4.8, Thm 5.1.
  - The scope of the erratum (only Thm 5.1, per zbMATH).
- Schueth [39]: Thm 4.1 and Rem. 4.2. Her a_0, a_1, a_2 at K = −1 equal the manuscript's b_0, b_1, b_2.
- Abreu–Dryden–Freitas–Godinho [12]: Thm 1 and §6.1.
- Garbin–Jorgenson [31]: Rem. 2.7, (2.8).
- Holtz–Tyaglov [40]: Thm 1.17. The source's sign (−1)^{n(n−1)/2} cancels against the roots −m_i of χ_m, so (10) is correct.
- Dryden [9]: Thm 4.5 (proof reads the systole off e^{−ω²/4t}) and Thm 5.1 (genus ≥ 1).
- Doyle–Rossetti [10]: Thm 1.
- Richardson–Stanhope [5]: Thm 4.7.
- Wooley [42]: Thm 13.1, exact-degree version.
- Coppersmith et al. [43]: p. 2, Letac's two size-9 solutions, and "k ≤ 9, k = 11" read as degree.
- Croot–Mao–Yip [44]: §1.
- Chen [45]: A.1.6, A.1.33, A.685, (3.33).
- Laurens [16]: Lemma 3.2 and the following remark crediting Steinig.
- Melánová–Sturmfels–Winter [17]: Prop. 24.
- Grieser–Maronna [22]: Thm 1.
- [26], [27]: the exponent 1/(2l−1).
- Philippe [19]: Thm A.
- Troyanov [46]: Thm A (via the zbMATH review).
- Borwein–Ingalls [6]: definition of N(k), Props 1–3, §3, §6 Problems 3–4 (preprint).
- Cremona [48]: §3.6 Method 1, (3.6.2), and §3.3 p. 70.

**Imprecise (minor):**
- (a) [7] does not state the normalisation of g. It is stated in [31, Rem. 2.6] and [9].
- (b) [2, Thm 5.14] covers only footballs and teardrops. Thm 5.15 requires *orientable* orbifolds, but Section 1.1 omits "orientable".
- (c) "[2, §5.6]" is Example 5.6, not a section.
- (d) [2, Prop. 5.22] says the spectrum determines a spherical orbifold, not the t⁰ coefficient. Remark 2.11 cites it as if it concerned the coefficient.
- (e) [38, p. 2] (arXiv v1) discusses Uçar's all-order formulas but says nothing about Watson's lunes or corrections to them.
- (f) The same-signature fact cited as [33, Thm A] is in the sentence after Thm A.
- (g) The journal page numbers [6, p. 6] and [6, p. 9] could not be confirmed from the preprint.
- (h) The following could not be checked with permitted sources: [21, Thm 3.1], [41], [23, p. 117], [11] and [34].

No citation was wrong in substance.

## 4. MAJOR issues

**M1. Fit and geometric-analytic contribution (Sections 1, 2, 4).**
- *Problem.* The new content is essentially algebraic and arithmetic. Section 2 re-derives known coefficients; Remark 2.9 concedes agreement with Uçar for all orders. Section 4's bound is far from sharp. JGA readers will look for new analysis.
- *Resolution:* do one of the following.
  - **Strengthen the analysis.** For example:
    - a version of Theorem 4.4 whose constant depends only on the signature and the systole, removing e^{3·diam};
    - a result linking finitely many eigenvalues to c_1, …, c_n;
    - a non-constant-curvature setting, where the moduli enter the coefficients.
  - **Shorten instead.** State the case for the journal explicitly, and replace the re-derivation in Section 2 by a citation and comparison.

**M2. Length and focus (Sections 6–7, Table 1, Figures 7–8, S3–S6).**
- *Problem.* The paper runs to 37 + 12 pages. Several features of Section 6 weaken its case for the main text:
  - The error model of Section 6 (errors in c_j, Remark 6.1) is not connected to any spectral measurement.
  - The constants depend on the unknown orders, so the results can only be applied a posteriori.
  - The numerical sections are, by the authors' own account, neither certified nor used in any proof.

  These parts dilute a paper whose core is Sections 3 and 5.
- *Resolution:*
  - Move most of Section 7 and Figures 7–8 to the supplement.
  - Present Theorem 1.3 more modestly in the introduction, or supply a bound linking the c_j errors to measurable spectral data, for example finitely many eigenvalues together with an a-priori Weyl remainder.

**M3. Main-text results depend on a proof only in the supplement (Table 1, Remark 6.1, end of Section 6).**
- *Problem.* The δ_cert column and the a-posteriori certification rest on Proposition S3.1. It is stated and proved only in the supplement, and its statement is dense while its proof is one paragraph.
- *Resolution:* move it, with a fuller proof, into an appendix, or drop δ_cert, δ_up and the diamonds of Figure 7 from the main text.

**M4. Figure 5 does not show what its caption claims (p. 20).**
- *Problem.* The caption says "Exact tilings of the hyperboloid". What is drawn is the Poincaré disc model, and its boundary is an ellipse. At 300 dpi both panels measure 635 × 539 px, an aspect ratio of 1.18. The pictures are therefore stretched anisotropically: not conformal, angles not π/p, π/q, π/r, and not "exact". The figure exists to compare the shapes of two triangles of equal area, so this misrepresents exactly what it is meant to show.
- *Resolution:* regenerate the figure at equal aspect ratio and label it "Poincaré disc model".

## 5. MINOR issues

1. **Abstract.** It packs about fifteen results into one paragraph. Trim it to the main three or four.
2. **p. 3, scope note on orientability.** The note on mirrors and orientability concerns the spectrum. For heat invariants the orientable restriction is essential. A locally orientable but non-orientable orbifold (cone points on a non-orientable surface) with the same χ and cone orders has identical heat invariants to all orders, by the mechanism of Proposition 4.1. State this; it clarifies what "genus" means in Theorem 1.1.
3. **Section 1.1, [2, Thms 5.14–5.15].** Add "orientable" (Thm 5.15) and note that Thm 5.14 covers only footballs and teardrops.
4. **Proof of Theorem 2.3.** "the normalization of [7, eq. (1)]": [7] does not state it. Cite [31, Rem. 2.6] or [9].
5. **p. 9.** "[2, §5.6]" should read "[2, Example 5.6]".
6. **Remark 2.11.** [2, Prop. 5.22] concerns the spectrum, not the t⁰ coefficient; separate the citations.
7. **Section 2.2.** "see also [38, p. 2]": say what this supports. That page is about Uçar's formulas, not Watson's lunes.
8. **Section 1.1 end.** Write "[33, Thm A and the sentence following it]".
9. **Theorem 4.4.** "same signature and area A" is redundant, since equal signature implies equal area.
10. **Remark 6.7.** The proof of Theorem 1.3 relies on it. Make it a Proposition with a proof.
11. **Proof of Theorem 3.11(e), genus part.** The case where every entry of W is 1 after scaling (W empty, g_0 = 2) is not covered by "below 2π(|W|−2) if g_0 = 0 and at most 4π if g_0 = 1". The bound still holds (area 4π < 2π|Z|), but say so.
12. **Lemma 5.2.** The exception (S,p) = (9,3) is vacuous because that stratum is empty. Rephrase.
13. **Theorem 5.5 proof.** State explicitly that gap_3(18) = 1/840 > 0 separates strata 3 and 4.
14. **Section 7, "Two timescales".** The aside "(a function of t, not the diameter)" reads oddly. Remove it.
15. **Section 7, "Error budget".** The same value, 2.9 × 10⁻¹¹, is given both as the maximal relative eigenvalue error and as the bound on the error in D(t). Please confirm this is not a transcription slip.
16. **Section 7 vs Figure 8(b).** The text says "all 28 pairs", but the figure shows only the 7 pairs with ϑ = 0. Say so in the caption.
17. **Data statement and Appendix C.**
    - The repository belongs to an account unrelated to the authors ("Ali-M658/Arithmetic-verification"). Please explain.
    - Appendix C exposes internal working paths ("review/audit-2/…", "review/round1-fixes/…"). Use neutral, stable paths.
    - (The Zenodo placeholder is treated as known.)
18. **Table S1.** The entry "1023 − 0.00 × 10⁰" is a formatting artefact. Give the actual deviation or a bound.
19. **Remark 3.13.** State the size of the exhausted search (about 4.3 × 10⁹ multisets) in the main text.
20. **[23, p. 117].** This is the first page of the article. Give the precise location of the reciprocal-pair remark.
21. **Typography.** Some displays are very dense, notably ζ_n and r_n on p. 26 and Proposition S3.1. Split the auxiliary series into separate displays.

## 6. Presentation (figures and captions, figure by figure)

**General.** The prose is precise but heavily compressed; many paragraphs read as condensed lists of checked facts. A gentler lead-in to Sections 3.3, 5.1 and 6 would help. Notation is consistent. I examined rendered pages at 110 dpi, with 300 dpi crops of Figures 1, 5 and 6.

**Figure 1 (p. 2).** The colouring is 4πt h_t(x,x) on a logarithmic scale from 1 to 12.
- *Accurate:* at 300 dpi the order-8 and order-12 tips reach the dark end of the scale, the order-2 corner sits near 2, and the order-3 corners near 3. The caption is honest.
- *Fix:* say that each panel shows one triangle, i.e. half of the orbifold.
- *Fix:* explain how values computed on the true metric were transferred to the "schematic, not isometric" domain.

**Figure 2 (p. 13).**
- *Accurate:* every disc and ring matches X* = {2,8,8,−3,−3,−12} and {1,15,−3,−3,−5,−5}.
- *Fix:* panel (a) uses orange and teal, panel (b) uses grey and black, and there is no legend. State the meaning (U* versus −V*) or unify the scheme.

**Figure 3 (p. 16).**
- *Accurate:*
  - the solid curve is ⌊2s⌋+4, reaching 28 at s ≈ 12;
  - the dashed curve is ⌊√((s−1)/3)⌋+2, starting at 3 for s = 4;
  - the squares sit at s = 2.4, 15, 63, 255, 1023 with heights 3–7;
  - the diamonds are consistent with Table S1.
- *Fix:* the split-colour dot at s = 1/4 is unexplained.
- *Fix:* for 5 ≲ s ≲ 35 the diamonds give better lower bounds than the dashed curve, so "the open question lies between" the two curves needs qualifying.
- *Fix:* the dashed bound holds only for s ≥ 4.
- *Unverified:* I could not check the 525 complete classes.

**Figure 4 (p. 18).**
- *Accurate:* the λ_1 endpoints are consistent with the caption.
- *Fix, panel (a):* the four renderings show no cone points, and the caption does not say which four ϑ values are drawn.
- *Fix, panel (b):* the vertical axis is nonlinear (ticks 0, 1, 5, 10, 20, 40, …, apparently a square-root scale) and the scale is not stated.
- *Fix, panel (b):* the connecting lines cross, so they are not sorted by index. The rule for matching branches across only eight samples is not explained.
- *Fix, panel (b):* the thin vertical lines at ϑ = 0.8 and 1.6 are unexplained.

**Figure 5 (p. 20).**
- *Wrong:* see M4. The disc is stretched (aspect ratio 1.18) and mislabelled "hyperboloid".
- *Accurate:* the vertex valences are right (16 edges at the order-8 vertices, 24 at the order-12 vertex), and the stated area π/4 is correct.

**Figure 6 (p. 23).**
- *Accurate:*
  - first-overlap dots at S = 19, 23, 26, 29, and the coincident dot and circle at S = 20, R = 1/2;
  - collision circles at S = 34, 38, 62, 117 at the correct values of R;
  - the split disc at (18, 3/4).

  All are consistent with Table S2 and Proposition 5.8. Only the adjacent pairs among p = 2..8 are marked, which is consistent.
- *Fix:* the dotted connectors are not mentioned in the caption.
- *Fix:* state that both axes are logarithmic.

**Figure 7 (p. 28).**
- *Accurate:* the slopes are 1, ½, ⅓, ½ as captioned. The diamonds lie at δ_cert = 3.66e−3, 2.34e−3 and 4.54e−4. The thin line is at 1/2.
- *Fix:* neither the paper nor the supplement explains how the "worst-case error" curves were computed. Describe the maximisation, or call it an adversarial perturbation.

**Figure 8 (p. 30).**
- *Accurate, panel (a):* D(t) starts near d_3·t ≈ 0.003, leaves the cone term near t ≈ 0.1, and changes sign near 0.33, all consistent with S4.
- *Fix, panel (a):* three grey truncations are drawn with unstated orders.
- *Accurate, panel (b):* the circles match ℓ²/4t* ≈ 24.5, for example t* ≈ 0.0049 at ℓ = 0.694 and ≈ 0.050 at ℓ = 2.21.
- *Fix, panel (b):* "where both first exceed ten times it" is ambiguous.
- *Fix, panel (b):* only 7 of the 28 pairs are shown.

**Tables.** The δ_thm column of Table 1 is reproduced exactly, and so are Tables S2 and S3.

## 7. Recommendation

**Major revision.**

**What holds up.** As far as I could check (and I checked extensively) the mathematics is correct. Every formula, example, table entry and computational claim I recomputed agreed, including Proposition 5.9 up to 4800 and the rank-0 curve of Theorem 5.10. The citations are accurate apart from minor imprecisions.

**Why not accept as is:**
- limited geometric-analytic novelty and unclear fit for JGA (M1);
- excessive length, including a stability and numerics component with weak spectral meaning (M2);
- a main-text table that rests on a proof found only in the supplement (M3);
- a figure whose caption misstates what is drawn (M4).

All of these can be fixed by restructuring and rewriting; no new mathematics is needed. A shortened version that makes a convincing case for its geometric-analytic interest could be acceptable.

**Confidence:** high in the correctness assessment; moderate in the recommendation, which depends mainly on the editor's view of scope.
