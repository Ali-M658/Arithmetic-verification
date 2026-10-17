<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (Annals of Global Analysis and Geometry)

I was not allowed to write `REPORT.md`, so this message is the complete report. My working scripts and outputs are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/B-e-mathscinet-reviewer/scratch/`.

Referee scope: rigour, citations, figures and tables. I read the whole manuscript (29 pp.) and looked at every page that contains a figure, table or display I comment on, rendered at 110 dpi, with 300–400 dpi crops of Figures 1 and 3. The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) are treated as known and are not counted as defects.

## Summary

Let Sig be the class of closed orientable hyperbolic 2-orbifolds whose singular points are cone points. Let C(A, ε, M) be the subclass with area at most A, systole at least ε and cone orders at most M. The main result (Thm 1.1 = Thm 6.2) says that explicit N and δ exist with the following property: the first N eigenvalues, each known to within δ, determine the signature, namely as the unique minimiser over Sig(A, M) of |Σ_{j<N} e^{-λ̃_j t*} − G_σ(t*)|. Here G_σ is the identity-plus-elliptic part of the Selberg trace formula for the heat kernel.

The proof has five ingredients:
- An integrality lower bound for the first heat invariant at which two signatures differ (Lemma 3.3), with the index of that invariant bounded by min(⌊A/π⌋+4, M) (Thm 3.2).
- Enveloping remainders for the cone and area expansions (Prop. 2.3), which turn this into a gap Γ(t) between signature terms (Lemma 6.1).
- An explicit diameter bound D(A, ε, M) (Thm 4.4), proved here from a separation lemma for elliptic points (Lemma 4.2) and a packing argument.
- A bound for the closed-geodesic term (Lemma 2.2).
- A counting bound for the tail (Prop. 5.2).

Thm 1.3 / Prop. 8.2–8.3 / Rem. 8.4 show that the order bound cannot be dropped. The orbifolds O(2,3,m) lie in C(π/3, 0.5620, m) and have λ_j ≤ 1/4 + π²(j+1)²/h_m². A pigeonhole argument then gives pairs of different signatures whose first N eigenvalues agree to within δ.

Section 7 turns the mechanism into an a-posteriori test (Thm 7.1) and runs it on computed spectra of O(2,8,8), O(3,3,12) and eight members of a (0;3,3,3,3) family. The paper states plainly that the eigenvalue errors are estimates, completeness is not proved and the systoles are floating-point values.

## Significance

The question is natural: how much of a finite, inexact piece of the spectrum fixes the topology of a hyperbolic orbisurface? The answer is clean, effective and honest about its constants. These are astronomically large: N up to 3.8 × 10³⁰ and δ down to 10⁻²⁷⁸ (Table 3). The effective content of Thm 1.1 is therefore one of principle. The non-effective version follows from compactness, as the authors themselves say on p. 2.

The comparison with Buser–Courtois should be kept in proportion. For surfaces without cone points the signature is the genus, so Thm 1.1 says only that finitely many approximate eigenvalues determine the area. That is far weaker than the Buser–Courtois statement that finitely many eigenvalues determine the whole spectrum. The new content is in the cone points, with orders and genus together.

The most interesting new mathematical statement is the necessity of the order bound (Thm 1.3). It is short and correct, and it complements the Garbin–Jorgenson elliptic-degeneration results well. The diameter bound (Thm 4.4) and its separation lemma (Lemma 4.2) are a small, neat, self-contained contribution. The a-posteriori section is a careful, unusually candid numerical illustration.

Overall the paper is of moderate significance, within scope for AGAG. What is good: the logic is tight, the constants are reproducible, the hypotheses are discussed seriously (Section 8 and Problem 1), and the numerical claims are stated with appropriate caveats almost everywhere.

## Correctness and what was recomputed

I checked by hand every proof given in the paper:
- Lemma 3.3, including the example d₂ = −1/12 for (0;4,4,4) and (0;3,4,6).
- Lemma 4.1 (H1)–(H3).
- Lemma 4.2, including the defect bound π/(abc), cos((θ−α−β)/2) ≥ 1/M and the final cosh d − 1 ≥ 2/(π²M²).
- Lemma 4.3.
- Theorem 4.4 and its closed form.
- Lemma 5.1. The case analysis is correct and Area ≥ π/21 is attained at (2,3,7).
- Proposition 5.2 and Lemma 6.1.
- Theorem 6.2. This covers the derivation of ϖ (63 = 21·3), the condition e^{−y}y^p ≤ γ*(ε²/4)^p/(16ϖe^{3D}) and its sufficient condition y ≥ y₀ via e^{−y/2}y^p ≤ (2p/e)^p, monotonicity of B* on (0, t₂], Λt* ≥ 1 and the 3Γ*/8 margin.
- Theorem 7.1, including the claim that (C2) implies (C1).
- Lemma 8.1, Proposition 8.2, Proposition 8.3, Remark 8.4 and Proposition 8.5.

I found no error in any proof given in the paper. The last bound of Lemma 2.2 (the one proved here) is correct: the maxima at x = 2√t and x = 6t, and the Stieltjes step Σ e^{−2ℓ(γ)} = 2∫ n_O(x)e^{−2x}dx, check out. The monotonicity of B in ℓ on t ≤ ℓ²/(2(1+ℓ)) also holds: the logarithmic derivative is ≤ −1/2 there.

I verified the following symbolically (sympy) or numerically (mpmath at 40–60 digits, scipy):
1. **Lemma 8.1 and the trace identities.** I checked tr[A,B] − 2 = −bc(u − u⁻¹)², the matrix B_{n+1} and the recursion x_{n+1} = −x_n(1+x_n)(u−u⁻¹)². For β = hkh⁻¹ I checked the off-diagonal entries ±sin(φ/2)cosh r, so bc = −sin²(φ/2)cosh²r. I also checked σ* = 2 arsinh √(3/37) = 0.5620669 and h₇ = 0.545275. Finally, h_m ≥ log(m/2π) holds for 7 ≤ m < 5000.
2. **Section 2.2 coefficients.**
   - α₀,…,α₃ = 1, −1/3, 1/15, −4/315.
   - b₀(m) = (m²−1)/(12m).
   - φ_k(m) is a positive combination of m^{2n−1} − m⁻¹ (k ≤ 4).
   - p_l is even, of degree 2l+2, with p_l(1) = 0 and leading coefficient a_l = |B_{2l+2}|/(2(l+1)!(2l+1)) (l ≤ 4).
   - |b_K(m)| is increasing in m (K ≤ 5, m ≤ 13).
   - |b_K(12)| ≈ c_K K!(12/π)^{2K} with c_K decreasing slowly from 0.35 to 0.10 (K ≤ 11), consistent with "roughly" on p. 13.
3. **Proposition 2.3**, the companion result that sets t₁. I tested the enveloping property (sign (−1)^K, modulus ≤ |b_K|t^K) against direct quadrature of E_m(t) for m ∈ {2,3,7,12}, t ∈ {0.01, 0.05, 0.2}, K ≤ 5. I tested part (b) for t ∈ {0.01,…,3}, K ≤ 6. No violation.
4. **Theorem 3.2.**
   - Part (ii) follows from Lemma 3.1 in three lines: equal R and equal P_{2k−1}, k ≤ M−1, form a nonsingular Vandermonde system in the squares of the M possible values 1,…,M. I recommend including that argument.
   - Part (i): I brute-forced all hyperbolic signatures with area ≤ 3π and orders ≤ 24 (4553 area classes). The first index of difference never exceeds ⌊A/π⌋+4; the maximum observed is 3, e.g. (2,8,8) vs (3,3,12).
5. **Table 2.** All 12 entries are reproduced from the exact form 4r₀A/v₀; the table does not use the cruder closed form, which is 1.06–2.6 times larger. The threshold ε < 0.42 (p. 14) is 0.42362.
6. **Table 3.** All 8 rows are reproduced in every column (k*, D, t₁, t₃, Γ*, Λ, N, δ, binding constraint), as are the claim t₂ ≥ 0.0045 and the claim "N from about 4 × 10¹⁸ to 1.1 × 10⁷" at A = 10π, M = 3 (I get 4.19 × 10¹⁸). The growth "factor of about 9 per halving of ε, slowly decreasing towards 8" is reproduced: 9.03, 8.94, 8.86, 8.79, 8.73, 8.67, 8.62.
7. **Table 4.**
   - The systoles ℓ were confirmed independently by enumerating the orientation-preserving reflection groups in SO(2,1), floating point, cut-off cosh 9. I get O(2,8,8) 2.2567679, O(3,3,12) 1.8626041, family 4b = 2.6339158 … 0.6939946 (and 4b is indeed the shortest), O(2,3,7) 0.9839866 and O(2,3,100) 1.921313. These agree with p. 22.
   - 2 diam P: closed forms reproduced, e.g. cosh⁻¹(cot²(π/8)) = 2.4483.
   - The D columns are reproduced.
   - Nc agrees with Weyl's law.
8. **Table 6.**
   - The "N, Thm 6.2" column is reproduced (all 18 rows), as are |S| = 6, 3 and 10.
   - Using only Table 5 and Theorem 7.1 as written (∆ = 2 diam P, my own quadrature for G_σ), I reproduced the triangle counts exactly: (C1) 18 and (C2) 20 for O(2,8,8), and (C1) 25 and (C2) 29 for O(3,3,12). At every time where a single signature passed, it was the true one.
   - The completeness ablation in item (iv) on p. 15 ("wrong signature in 19 of these 24 cases, mostly at a smaller N") is reproduced exactly: 19/24, with wrong conclusions at N = 9–17 for O(2,8,8) and 12–26 for O(3,3,12).
   - The class-level times are consistent with t ≈ ℓ²/(12D), e.g. 0.00383 vs 0.00375 for ϑ = 0.
9. **Ratios quoted in the text.** "20–50 at M = 3", "10⁶", "10⁷–3 × 10⁸" (p. 19) and "5 × 10² to 3 × 10¹¹" (Fig. 2) are all correct from Table 6.
10. **Figures.** I compared Figures 1–3 against the tables and text. Details are under Presentation.

Not recomputed:
- The eigenvalues themselves (Table 5, Fig. 3).
- The estimates column of Table 6 and N_obs.
- The diameters computed by optimisation.

**Citations checked against the sources** (arXiv versions where the published one was not accessible):

| Reference | Cited for | Result |
|---|---|---|
| [1] Dryden–Strohmaier | Thm 1.1, Prop. 3.3 (spectrum determines cone orders and topology), Thm 3.2 (Gauss–Bonnet, used for the area formula), eq. (1) (trace formula) | ✓ |
| [5] Doyle–Rossetti | Thm 1 | ✓ (v2, 10 Apr 2014) |
| [2] Linowitz–Voight | Thm A | ✓ (isospectral pairs of signature (0;2,2,2,2,2,3,4)) |
| [6] Buser–Courtois (GDZ scan) | (1.1), injectivity radius ≥ ε; conjecture on pp. 523–524 | ✓ |
| [11] Stanhope | Main Thms 1–2 | ✓ |
| [12] Proctor–Stanhope | abstract | ✓ |
| [14] Garbin–Jorgenson, Ens. Math. | Cor. 5.5, Thm 5.3 | ✓ in arXiv 1603.01494 numbering; see m4 |
| [15] Garbin–Jorgenson, Kodai | Rem. 2.7, (2.8); Thm 6.5 | (2.8) has exactly the normalisation of Thm 2.1, including 1/(2q sin(nπ/q)) and √(16πt); Thm 6.5 is a pointwise statement C_{M_q,0}(x,T), as the text says |
| [21] Strohmaier–Uski | §7 | ✓; see m3 |
| [25] DGGW | Thm 4.8 | ✓ |
| [26] Uçar | Thm 4.20 (closed form of the area coefficients matches α_k), Thm 3.40 | ✓ |
| [34] Dryden–Parlier | Thm 3.1, cone angles < π | ✓ |

Crossref confirms authors, titles, volumes, issues, pages and years for all 33 DOIs given. The DataCite record for [26] is correct. The Zenodo DOI for [42] is not in Crossref; it is a DataCite DOI and was not checked further.

I could not obtain the following, so their statement-level citations are unverified: [3] Mumford, Cor. 3 (AMS site blocked headless access); [27] Chang–DeTurck, Thm 1; [23] Buser, Lemma 6.6.4; [30] Thurston 13.3.4–13.3.6; [16]–[20], [39]–[41] at page level.

## FATAL

None. I found no false statement among the main results, and every proof given in the paper checks.

## MAJOR

**M1 (Sections 2–3, Table 1; affects Thm 1.1/6.2, Lemma 6.1, Table 3, Theorem 7.1, Table 6). The main theorem rests on unrefereed results of the companion manuscript [28], stated without proof.** The following load-bearing statements are imported:
- Theorem 2.1 (trace formula for the heat function, with absolute convergence).
- Lemma 2.2, its first two statements: the count n_O(x) ≤ πe^{x+3 diam}/Area and the bound B(ℓ, diam, t), which sets t₂, t₃ and H in Theorem 7.1.
- Proposition 2.3 (enveloping remainders for all K, all t > 0 and all m, plus monotonicity of |b_K| in m), which sets t₁ and hence every binding entry "t₁" in Table 3.
- Lemma 3.1.
- Theorem 3.2(i), which is what gives k* = ⌊A/π⌋+4 < M in rows 1, 2 and 5 of Table 3 and in every M = 12 row of Table 6. Without it, k* = M and the numbers change completely.

My numerical tests (items 3 and 4 above) support all of these, and Thm 3.2(ii) follows from Lemma 3.1 by a Vandermonde argument. But a numerical check is not a proof, and [28] is cited only by placeholder. AGAG cannot accept a theorem whose proof depends on an unpublished, unrefereed manuscript that the referees were not given.

**M2 (p. 6, Lemma 2.2; p. 7, Prop. 2.3). The constants in the two imported analytic estimates cannot be checked from the paper, and they drive every number in Tables 3 and 6.** In particular:
- the factor 1 + 2t/(ℓ − t);
- the range t ≤ ℓ²/(2(1+ℓ));
- the claim that |b_K(m)| increases strictly in m for every K.

The second Hyp bound in Lemma 2.2 is proved in full here and is correct, which makes the absence of the other two proofs more conspicuous. All three proofs are short (Stieltjes integration against the counting bound, and a contour or Bernstein-type argument for the alternating remainders), and they should be in this paper.

## MINOR

**m1 (abstract; pp. 3, 18–19, §7.2; Table 6). The eigenvalue counting convention is inconsistent.**
- In Theorem 7.1 "the test with N" uses λ̃₀,…,λ̃_N, that is N+1 eigenvalues. Figure 1's discussion (p. 14) counts this way: "21 eigenvalues … (N = 20)".
- The abstract, p. 3 and §7.2 ("with 18 and 25 eigenvalues", "18 to 847", "855 to 2900", "about 800 eigenvalues") report N itself as the number of eigenvalues.

Either report N+1 throughout or say once that the counts are values of N. In Theorem 6.2, by contrast, N is the number of eigenvalues used.

**m2 (p. 19, line 2). "The tail then needs (λ̃_N − ϵ_N)t of about 11"** is not borne out by the paper's own data:
- O(2,8,8): λ̃₁₈ · 0.0565 = 7.7 (Table 5/6).
- O(3,3,12): λ̃₂₅ · 0.0412 = 8.3.
- For the family, Weyl's law λ_N ≈ 3N gives about 9.8 (ϑ = 2.8, M = 3) and 10.5 (M = 12).

Say "about 8–11".

**m3 (p. 5, l. 2). "Our completeness check is that of Strohmaier and Uski."** Strohmaier–Uski (§7) bound the length-spectrum contribution and call their check rigorous up to a level. Here the tail beyond the computed range is a Weyl-law estimate, the ϵ_j are estimates and floating-point summation is not controlled, all as §7.1 says. Write "follows the idea of" and keep the caveat next to the citation.

**m4 (p. 4). "[14, Thm 5.3]: the number of eigenvalues below a fixed level above 1/4 grows like the logarithm of the orders."** In the arXiv version of [14] (p. 16), Q is defined as log(∏q_γ) and Theorem 5.3 states N ~ c_w(T) log Q. Read literally that is log log of the orders, which contradicts this paper's own Prop. 8.3: #{λ_j < T} ≥ h_m√(T − 1/4)/π − 1 ~ (√(T − 1/4)/π) log m. Check the published version, cite precisely, and note that Prop. 8.3 gives the log m lower bound independently. Also give [16] a page: Garbin–Jorgenson attribute the Hecke-triangle accumulation to Selberg via p. 579 of Hejhal Vol. 2.

**m5 (p. 24, l. 3). "Related by quasi-isometries with constants near 1, as in Section 1."** Section 1 (p. 3) correctly uses bi-Lipschitz maps. Quasi-isometries with additive constants do not control eigenvalues. Replace with "bi-Lipschitz".

**m6 (abstract; p. 3; §7.2). The word "decides" is stronger than what is established.** Section 7 itself establishes only that "the criterion of Theorem 7.1 holds with the estimated errors, for lists assumed complete" (p. 16). Item (iv) on p. 15, which I reproduced, shows that a single missing or duplicated eigenvalue produces a wrong but confident answer in 19 of 24 cases. The abstract also quotes Weyl-surrogate extrapolations ("estimated to need 4.4 × 10³ to 4.1 × 10⁵") whose error the paper puts at up to 8%. One of them (ϑ = 1.6, M = 3: 4412) is known to be low, because the criterion still fails at N = 4423. Use "the criterion of Theorem 7.1 holds" in the abstract, or move the estimates out of it.

**m7 (p. 17, Completeness). The completeness evidence for the triangles is circular in a way that should be stated, and partly removable.** The trace comparison at t = 0.0015 is against G_σ of the true signature. At that time the competing signatures differ from G_{σ(O)} by at least about d₃t ≈ 3 × 10⁻³, far more than the budget of 1.5 × 10⁻¹¹. Comparing against all σ ∈ S would turn the check into a joint test of "complete list and signature σ" that only the true σ passes. A missing-plus-spurious pair is still invisible to it. The authors should also state the perturbation bound used in the budget. The unweighted t Σϵ_j of Theorem 7.1 would be about 10⁻³ there, so the budget must use |e^{−at} − e^{−bt}| ≤ t|a−b|e^{−t min(a,b)}. That sharper bound would also be worth adopting in E_N.

**m8 (§7.1; data statement). Reproducibility details are missing from the paper.**
- Software versions of NGSolve and ARPACK are not given.
- With the class-level D, the factor e^{3D} is e^{3375} to e^{9003}, which overflows double precision. State how H is evaluated (log-space or multiprecision).
- The data statement names no script for Figures 1–3 or for the O(2,3,m) spectra behind Fig. 3.

**m9 (p. 2, l. 3). [3, Cor. 3] for Mumford's compactness theorem is unverified by me.** Please check the numbering: the result is usually quoted as the main theorem of that note.

**m10 (p. 8, Lemma 3.3 proof).** "C_l = Σ b_l" is used once and never defined. Also, the header of Theorem 3.2 cites "[28, Cor. 3.5, Thm 3.8]" while Table 1 cites "Theorem 3.8(i)".

**m11 (bibliography).**
- [33] lacks the series number (GTM 91).
- [23] lacks DOI and series number.
- [10]: the third author is customarily "Petersen V, P.".

## Presentation

**P1 (Figs 1–3; house style: at most two short sentences).** All three captions have the right number of sentences, but the sentences are not short: about 45 words (Fig. 1), about 40 (Fig. 2) and about 50 (Fig. 3, where two panel descriptions are joined by a semicolon). Move the explanatory material to the text.

**P2 (Fig. 3, p. 24).** The panel labels "(a)" and "(b)" are drawn inside the figure, against the house style of no labels inside figures. Either typeset them as part of the caption or split the figure. As rendered, the dashed bound for λ_j lies just below the curve of λ_{j+1} in panel (a), which invites misreading. The caption should say that the bound for λ_j is the dashed curve of the same shade, or panel (b) should show the level (j+1)² that corresponds to the bound.

**P3 (Fig. 2, p. 20).**
- The markers are deliberately offset horizontally ("slightly to the left/right of their systole"), so the abscissa is not the systole. State the offset or avoid it, for example by using shape alone.
- N_obs (circles) is plotted, but it appears in no table and is defined only after the figure. Add an N_obs column to Table 6.
- The colour key for the two triangle orbifolds is given only in the text.

**P4 (Fig. 1, p. 14).**
- "The sum of the two errors" can be read as the two dotted curves (21 and 100 eigenvalues). Say "the closed-geodesic bound plus the tail-and-perturbation term".
- The text says the dashed curve uses "the true systole", whereas Table 4's ℓ is a rounded-down floating-point value.
- The figure itself is consistent with the text. The shaded window is 0.050–0.057. There, both error curves lie about 0.8 decades below the (0;3,3,12) gap, so their sum is below half the gap. The (0;3,3,12) curve starts at about (25/12)t, and there are five competitors.

**P5 (notation).** Several symbols carry two or more meanings:

| Symbol | Meanings |
|---|---|
| Γ | Fuchsian group; gap function Γ(t), Γ* |
| Λ | spectral cut-off; Λ_N in Prop. 8.3 |
| p | polynomials p_l; exponent k* − 3/2 in Thm 6.2; points p̃; FEM order |
| A | class area bound; common area in Lemma 3.3(ii) |
| D | diameter bound; Dirichlet label in Table 5 |
| Q | Q(K); quadrilateral Q_{k,b} |
| δ | accuracy; δ_k |
| ε / ϵ_j | systole bound / error estimates |
| Sig | class of orbifolds; Sig(A, M), a set of signatures |

At least the gap function, the exponent p and the area in Lemma 3.3(ii) should be renamed.

**P6 (Tables).** All six tables are internally consistent wherever I could check them (items 5–8 above). Table 2 should say that it uses the exact form 4r₀A/v₀, not the closed form of Thm 4.4, which is up to 2.6 times larger. Table 3 should note that its ε values are the Table 4 systole bounds rounded down to four decimals.

## Recommendation

**Major revision.** Confidence: high on the correctness checks above; moderate on the recommendation itself, which depends on the editor's policy for companion papers.

The mathematics that is actually proved here is correct, and every table I could recompute is reproduced exactly. That includes the a-posteriori counts for the triangle orbifolds and the 19/24 completeness ablation. The numerical claims are, with the exceptions in m1, m2, m6 and m7, stated honestly as estimates and not enclosures, with completeness supported but not proved.

The obstacle to acceptance is M1–M2: the core analytic inputs of Theorem 1.1 are imported from an unrefereed companion. If the editor makes [28] available and the authors either include short proofs of Lemma 2.2 (first two statements), Prop. 2.3 and Thm 3.2, or the companion is accepted first, I would expect to recommend acceptance after minor changes.

## What resolves each issue

- **M1:** Include proofs, in an appendix, of Theorem 2.1 (admissibility of the heat function), Lemma 2.2 (count and first bound), Proposition 2.3, Lemma 3.1 and Theorem 3.2. Alternatively, supply [28] to the referees and make acceptance conditional on it. For Thm 3.2(ii), add the three-line Vandermonde argument from Lemma 3.1.
- **M2:** Prove the counting bound, the bound B and its range, and the enveloping and monotonicity statements of Prop. 2.3 in this paper. If only one is added, add Prop. 2.3, which governs t₁.
- **m1:** Fix one counting convention (N or N+1) and use it in the abstract, p. 3, §7.2 and the Table 6 caption.
- **m2:** Replace "about 11" with "about 8–11", or quote the actual values.
- **m3:** Reword to "follows the idea of [21, §7]" and keep the non-rigour caveat beside the citation.
- **m4:** Verify [14, Thm 5.3] in the published version, state precisely what is cited, add the remark about Prop. 8.3, and add the page for [16] (p. 579).
- **m5:** Replace "quasi-isometries" with "bi-Lipschitz maps".
- **m6:** Rephrase "decides" in the abstract, and move the Weyl-surrogate estimates out of the abstract or flag them there as extrapolations.
- **m7:** Run the completeness trace check against every σ ∈ S, report the margins, and state the perturbation bound used. Consider the weighted bound in E_N.
- **m8:** Give software versions, explain how e^{3D} is handled, and name the scripts for Figures 1–3 and the O(2,3,m) spectra.
- **m9:** Check and correct the numbering in [3].
- **m10:** Define C_l (or remove it), and make the Theorem 3.2 citation match Table 1.
- **m11:** Complete the bibliographic data for [33], [23] and [10].
- **P1–P4:** Shorten the captions, remove the in-figure panel labels in Fig. 3, explain or remove the marker offsets in Fig. 2, tabulate N_obs, and clarify "two errors" and "true systole" in Fig. 1.
- **P5:** Rename the overloaded symbols listed above.
- **P6:** Add the two caption clarifications for Tables 2 and 3.
