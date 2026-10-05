# Handling editor's report: "How much of a hyperbolic orbifold does heat hear?" (JGA submission, 56 pp.)

**Basis of this report:** I read the whole PDF, all nine figures (each rendered page inspected), the six tables and three appendices. Page numbers are the printed ones. As instructed, I do not count the placeholders (author contributions, AI-use statement, Zenodo DOI) as defects.

**Network access:** the Crossref, zbMATH and Semantic Scholar APIs, and fetching the Springer guidelines page, all failed from the sandbox. I verified references and the guidelines through web search instead.

## 1. Summary
The paper asks how many coefficients c_j of the small-t heat expansion Z_O(t) ~ Σ c_j t^{j−2} are needed to determine a closed orientable hyperbolic 2-orbifold, and what they can determine at all.

**Setup.** The paper starts from Uçar's constant-curvature expansion [8], restated as Prop. 2.4. A cone point of order m contributes (−1)^l p_l(m)/m at order t^l, with p_l even of degree 2l+2 (Lemma 2.5). So c_j adds one odd power sum P_{2j−3} of the orders (Lemma 2.10), and comparing two orbifolds becomes a moment problem for a signed multiset.

**Signature (Section 3).**
- Theorem A: (R, P_1, …, P_{2n−3}) determines an n-multiset of nonzero complex numbers with no m_i + m_j = 0. Hence K_mult(O; P_n) ≤ n.
- Theorem B: a linear system for the e_k, whose determinant is an Orlando/Hurwitz product.
- Theorem C: n−1 invariants are never locally injective over the reals, with integer witnesses for n = 3, 4.
- Theorem 3.6 and Corollary 3.7: K_mult(O; Sig) ≤ ⌊Area/π⌋ + 4.
- Theorem 3.10 (Prouhet–Thue–Morse): no uniform number suffices. Corollary 3.12 gives log and linear growth bounds.

**Shape (Section 4).** Every c_j depends only on the signature, so K_iso = ∞ off the triangle orbifolds. Through the trace formula, the difference between two traces is O(t^{−1/2} e^{−ℓ²/4t}), and this is attained.

**Triangle orbifolds (Section 5).** Two coefficients are equivalent to (S_1, R). They suffice when p+q+r ≤ 17. The first failure is (2,8,8)/(3,3,12). Three coefficients always suffice. The minimal pair is isolated because rank C_{27/2}(Q) = 0 and the torsion is Z/2×Z/6 (a PARI computation).

**Stability (Section 6).** Recovery is Lipschitz at simple orders and Hölder-1/k at k-fold orders, with explicit and certified thresholds.

**Experiments (Section 7).** FEM spectra of the minimal pair and of a (0;3,3,3,3) family.

**Arithmetic (Section 8, Appendices A, B).** The paper places the degeneracies on the Bremner–Guy–Nowakowski cubics. It shows N(X) ≳ X log X and X(log X)², proves that classes of every size exist, and conjectures N(X) = X^{1+o(1)}.

## 2. Significance, novelty, scope

**Good.**
- The question is natural, and the paper is honest about prior work.
- Three results are genuinely new and clean:
  - the ⌊Area/π⌋+4 bound (Cor. 3.7), with the mirror/parity argument of Thm 3.6;
  - the Prouhet construction (Thm 3.10);
  - the sharp threshold 17, with the explicit, isolated minimal pair (Thms 5.13, 5.14, 5.16). This settles the remark of DGGW [3, Rem. 5.16].
- Every number I re-derived matched exactly (§3.3).

**Overstated.**
- Thm 1.2(i)–(ii) is folklore. The paper itself says "No local invariant can see the moduli" (p. 21). For surfaces these facts are in McKean (CPAM 1972), which is not cited.
- Thm 1.2(iii) is the standard leading hyperbolic term of the trace formula.
- Thm A in the positive-real case actually used is classical (Steinig; Laurens), as the paper concedes. The complex/Orlando version and Thm B are pleasant algebra, but no geometric theorem needs them.
- Once Prop. 2.4 is granted, Sections 3, 5 and 8 are power-sum combinatorics and arithmetic.

**Scope.** JGA states that it publishes "new results at the interface of analysis, geometry, and partial differential equations". It does publish spectral geometry of hyperbolic surfaces, for example recent Steklov papers on hyperbolic surfaces and triangle tilings. Sections 2–5 are therefore in scope. Sections 6, 7, 8 and Appendix A are not:
- Section 6 is root perturbation;
- Section 7 is FEM computation;
- Section 8 and Appendix A are rational points on cubics and lattice counting.

The MSC codes 11D68, 11G05 and 11D45 signal this.

## 3. Correctness and consistency

**3.1 Promises in the abstract and introduction, checked against the body.**
- ⌊Area/π⌋+4 bound: delivered by Cor. 3.7 (p. 16).
- "Read off from c_1": delivered (c_1 = Area/4π).
- No fixed number suffices: delivered by Thm 3.10. I checked the k = 2 pair (0;4,4,4,6,6)/(0;2,2,2,3,8,8) by hand.
- Complex-multiset injectivity: delivered by Thm A. The abstract omits "nonzero".
- "n−1 never do near distinct positive reals": delivered by Thm C(2). However, Thm 1.1(iii) does not say that for integer orders necessity is shown only for n = 3, 4 and is open for n ≥ 5 (Problem 2).
- Signature locality: delivered (Thm 4.1), but classical.
- t^{−1/2}e^{−ℓ²/4t}, attained: delivered (Thms 4.9(b), 4.10(iii), Cor. 4.11). "C is explicit" hides the dependence on the diameters, which are not spectral data.
- Threshold 17, first failure at 18, isolation: delivered (Thms 5.13, 5.14, 5.16). Thm 5.16 rests on PARI.
- "Both rates are sharp": only for general (complex-root) data. For real multisets at a triple order the exponent is 1/2 (Remark 6.8; Fig. 9, dotted line).
- Certified thresholds: delivered (Thm 6.9, Prop. 6.10, Table 2).
- "Computed spectra confirm": numerics only. The paper calls them "a-posteriori agreements, not enclosures", and one recomputation "has not yet been run" (pp. 44, 53).
- Intro p. 4, blind recovery: I checked c_1 = 1/8, c_2 = 67/48 and exact c_3 = −3.335417 / −5.418750 against Table 3.
- "Answers the question left open in [3, Rem. 5.16]": overstated. DGGW make a remark, not a question.

**3.2 Cross-references.**
- All theorem, figure and table references resolve.
- Fig. 5(a) is printed on p. 26 (Section 4) but discussed only on p. 44 (Section 7). Fig. 4(b) shows Section 7.2 data inside Section 4.
- Section 1.2 omits Appendices A and B.
- Table 5 and p. 49 report S = 6000 data (N = 145679; "1.58 near S = 6000"; "0.00405 at S = 6000"). But the caption, §8.4 and Appendix C all say the enumeration covers S ≤ 4800 ("3,067,197,199 hyperbolic triads with 10 ≤ S ≤ 4800"). The S = 6000 data are therefore unexplained.

**3.3 Independent recomputation (my scratch scripts).** All of the following matched the paper exactly:
- p_0, p_1, p_2 and α_0..α_4;
- d_3 = 25/12, d_4 = −1775/24, d_5 = 153025/48;
- F^{−1} and amp = 2, 14, 498, 4062, 56230/3;
- Remark 2.11 values; (2,3,5) → 271/360;
- Thm C(3): R, P_1, P_3, P_5;
- Example 3.13, including P_3 = 10126;
- C(123,5) = 216,071,394;
- c_2(3,3,4) = 107/144;
- x*(p) and S*(p);
- Table 4 members: equal S and R, with Λ = 68/5, 68/5, 1849/120, 230/21; (4:9:18) and 3P lie on C_{155/12};
- the E model: Y² = X(X+9)(X+384), with full 2-torsion and the point (−24, 360);
- c_iso and 3/(128π⁴).

An exhaustive enumeration of the triads with S ≤ 600 (8 s of CPU) also matched:
- Table B1: 83 triads;
- Table 5 rows from S = 18 to 600: pairs 1, 92, 386, 840, 1496, 2210, 3067; classes 1, 92, 380, 822, 1468, 2158, 2977;
- every entry of Table 1;
- 2793 of the 3067 pairs are non-adjacent, the first being (5,15,15)/(7,7,21);
- 1753 primitive pairs, 423 of them dual;
- 507 of the 582 sums;
- the 38 collision-free sums: 19, 21–25, 27–30, 33, 41, 44, 46–51, 59, 65, 67, 81, 99, 115, 119, 123, 125, 173, 199, 203, 223, 235, 243, 251, 307, 329, 557.

I did not re-run the PARI ranks, the Table 2 certificates or the FEM spectra.

**3.4 References.** The Crossref, zbMATH and Semantic Scholar APIs were unreachable from the sandbox, so I verified by web search.
- Confirmed: [7], [10], [11], [12], [13] (Korobov–Bugaevskaya, Math. Comp. 85(298):717–736), [20], [37].
- Consistent with my own knowledge, no anomaly: the rest.
- Defects are listed in m11.

## 4. MAJOR issues

**M1 — The paper is three papers, and only one fits JGA** (Sections 6–8, Appendices A, B; about 22 of 56 pages; MSC 11xx).
- None of this material is used in the proofs of Theorems 1.1–1.3 (p. 42: "Neither is used in any proof"; p. 45).
- Refereeing it would need three kinds of expertise.
- *Fix:*
  - Restructure around Sections 2–5, about 25–30 pages.
  - Reduce Section 6 to Thm 6.6 and Prop 6.7, or move it to a supplement.
  - Move Section 7 and §6.5 to a supplement.
  - Submit Section 8 with Appendix A separately to a number-theory venue.

**M2 — Section 4 and Theorem 1.2 overstate their novelty.**
- Part (i)/(ii) is immediate from locality, and for surfaces it is due to McKean (1972).
- Theorems 4.6–4.10 are standard trace-formula estimates.
- The proof of Prop. 4.4 is a long route to "R^d modulo a countable modular group is uncountable".
- Remark 4.13 ignores Wolpert (Ann. Math. 1979).
- *Fix:*
  - Demote (i)/(ii) to a cited proposition.
  - Keep only the explicit constant and the t^{−1/2} sharpness, flagged as routine.
  - Cite McKean, Huber, Buser, Wolpert and Hejhal/Iwaniec.
  - Cut Section 4 to about 4 pages.

**M3 — The key formula rests on an unrefereed thesis.**
- Prop. 2.4 and Lemma 2.5 (degree 2l+2 and nonzero leading coefficient for all l) come only from Uçar's thesis [8], and Thm 3.6 and Cor. 3.7 need them for all l.
- Schueth [24] covers only p_1 and p_2, and Remark 4.12 is a computer check through order t^5.
- The paper says the trace-formula route is "not independent" because it uses DGGW's leading term. But DGGW is refereed, so this is no circularity with respect to [8].
- *Fix:* derive b_l(m) and Lemma 2.5 from the elliptic term E_m(t) of Thm 4.6, using the moments already listed on p. 25 (1–2 pages). Alternatively, cite a refereed version of Uçar's formula.

**M4 — Proofs depend on unshown computation or the repository.**
- *Locations:*
  - Remark 2.12: "The proofs are in the repository".
  - Thm 5.13 has "…33, and so on, the largest being 557" inside the theorem statement.
  - Prop. 5.15(2): "by direct check".
  - Thm 5.16: PARI `ellrank`; the 2-isogeny descent is not shown.
  - Thm 8.9: "nP ≠ O for 1 ≤ n ≤ 12 (exact chord-and-tangent computation)".
- The repository belongs to a GitHub account ("Ali-M658") that is none of the authors.
- *Fix:*
  - Prove Remark 2.12 in the paper or delete it.
  - Move the computational claim of Thm 5.13 to a remark with all 38 sums listed (I confirm the list).
  - Write out the 2-isogeny descent for Y² = X(X+9)(X+384); it is half a page.
  - Prove that P in Thm 8.9 has infinite order by Nagell–Lutz or by reduction modulo two primes.
  - Separate proved statements from observations.

**M5 — Unfinished or uncertified computation.**
- *Locations:* p. 44: "has not yet been run"; p. 53: "prepared but has not been run"; §6.5: "protocol committed before the pipeline code"; Remark 6.1: error budgets are not enclosures.
- The real inverse problem, estimating c_j from finitely many eigenvalues, is not addressed.
- *Fix:* complete the run or remove Section 7 and §6.5 to a supplement. Label the numerics as uncertified in the abstract, and drop the pre-registration language.

**M6 — Incomplete bibliography** for the novelty claims and for the software used.
- Missing:
  - McKean (1972), Huber (1959), Buser (1992), Wolpert (1979);
  - Hejhal or Iwaniec (trace formula with elliptic elements);
  - C. Gordon, "Orbifolds and their spectra"; Stanhope (2005);
  - the Prouhet–Tarry–Escott literature (Borwein; Wright; Borwein–Ingalls);
  - Guy, *Unsolved Problems in Number Theory*, D16;
  - NGSolve and cypari2.
- *Fix:* add them and recalibrate "to our knowledge the first…" and "answers the question left open".

## 5. MINOR issues
- **m1** (p. 2): K_mult, Sig and P_0 are used before Def. 2.3. *Fix:* state Thm 1.1 in words.
- **m2**: lettered theorems A–C sit inside numbered sections. *Fix:* unify the numbering.
- **m3** (Thm 1.1(iii)): *Fix:* add "over the reals; for integer orders proved only for n = 3, 4, open for n ≥ 5".
- **m4** (abstract; Thm 1.4): "both rates are sharp" / "cannot be improved". *Fix:* add "for general data" and cite Remark 6.8.
- **m5** (p. 5): "answers the question left open". *Fix:* rephrase.
- **m6** (Thm 1.2(iii)): *Fix:* say that C depends on the diameters and the systole.
- **m7** (Props. 4.3, 4.4): *Fix:* cite the classical rigidity of triangle groups, and use the countable-modular-group argument.
- **m8** (Lemma 2.6, Prop. 2.7): classical. *Fix:* cite and delete the proofs.
- **m9** (Fig. 2(a), lower panel): the "configuration that sharing c3 would force" is {±2, ±8, ±8}, i.e. U* = V*. This contradicts the disjointness established in the proof of Thm 3.6; the forced configuration is X* = ∅. *Fix:* redraw it or correct the caption.
- **m10** (Table 5, p. 49): *Fix:* explain the S = 6000 row or delete it.
- **m11** (References):
  - [4]: write "73(4, Part 2)".
  - [10]: "laguerre's" → "Laguerre's"; write "Rend. Mat. (6) 4".
  - [27]: the DOI loses its underscore; it should be 10.1007/978-1-4471-0551-0_1.
  - [29]: add LMS Lecture Note Ser. 397.
  - [35]: "singulieres" → "singulières".
  - [36]: check the pinpoint "Cor. (5.2)" (usually Theorem (8), or Invent. Math. 44 (1978)).
  - [23]: duplicated URL.
  - Title capitalisation is inconsistent across entries.
- **m12**: N(S) (per sum) and N(X) (cumulative) are told apart only by font, in Table 5 and Fig. 8(b). *Fix:* use distinct symbols.
- **m13** (p. 14): "witnesses are not isolated: there are 11 witness classes…" does not follow. *Fix:* define the term or drop the sentence.
- **m14**: padding is introduced twice (Remark 3.3, Lemma 3.4). *Fix:* introduce it once.
- **m15** (Fig. 3): "complete area classes" is undefined.
- **m16**: "pillow" is used in Figs. 1, 6 and 8 but never defined.
- **m17** (Table 2): *Fix:* give the intermediate quantities (A, v, E) of Prop. 6.10 for one row so a reader can check it.
- **m18**: *Fix:* confirm ownership and licence of the repository, which sits under a non-author account.

## 6. Presentation
- **p1 — Length.**
  - Cut or move to a supplement:
    - Lemma 2.6 and Prop. 2.7; Remarks 2.11, 2.12 and 3.2;
    - Props. 4.2–4.4; Lemmas 4.7 and 4.8;
    - Prop. 5.8; Prop. 5.15 and Table 1;
    - Sections 6.4–6.5, 7 and 8;
    - Appendices A and B, and Table B1 ("plays no role in the proofs").
  - Target: 25–30 pages.
- **p2 — Figures.**
  - Fig. 4(a) is a "stylised" decorative rendering: drop it.
  - Fig. 6 is attractive but not needed.
  - Fig. 1 may stay as a teaser.
  - Fig. 5 splits Section 7.1 and 7.2 material and sits 18 pages before its discussion. Fig. 4(b) shows Section 7.2 data in Section 4.
  - Fig. 5(a) has no t-axis tick labels, and the log scale is unstated.
  - Captions say "dark/light" for teal/orange (Figs. 2, 8(a)), which fails in greyscale. *Fix:* use marker shapes as well.
  - Fig. 1 labels the colour bar 𝔥_t while the caption says h_t.
  - Legibility is otherwise fine.
- **p3 — Density.** Statements are mixed with computational provenance. *Fix:* move provenance to Appendix C.
- **p4 — Notation.** The symbol load is very heavy. *Fix:* add a notation table and drop one-off symbols.
- **p5 — Abstract length.** About 255 words; JGA asks for 150–250. *Fix:* shorten.
- **p6 — Keywords and MSC.** Six keywords is within the JGA range. The eight MSC codes have no primary/secondary designation. *Fix:* designate primary 58J53, and drop the 11xx codes after M1.
- **p7 — Line numbers.** *Fix:* add line numbers for review.
- **p8 — Declarations.** Funding, competing interests, ethics, data availability and author contributions (placeholder) are present. The AI statement sits in Appendix C, which the policy accepts. The title page has template residue ("Corresponding author(s). E-mail(s):").
- **p9 — Tone.** The metaphorical register in the introduction should be used sparingly.

## 7. Recommendation
**Major revision**, conditional on M1. As it stands, I would not send the 56-page version to referees. **Confidence: medium.**

**Desk-reject probability: about 50%.** Reasons for desk rejection:
- about 40% of the paper is out of scope (M1);
- the geometric-analysis depth is thin, and the "shape" half is classical (M2);
- the paper depends on a thesis and on repository-only verifications (M3, M4);
- it shows visibly unfinished work (M5);
- it is long for its new content.

Reasons against:
- the question is natural, and the paper settles a remark of DGGW;
- the ⌊Area/π⌋+4 bound, the Prouhet construction and the sharp threshold 17 with its isolated pair are new and correct as far as I checked;
- the exposition is honest about prior work.

A focused 25–30-page version (Sections 2–5) would be a reasonable JGA submission. It should go to two referees: a spectral geometer, and a referee with number-theory competence for Thm 5.16.

---

*Saved by the coordinating session: this subagent could not write files, so the report came back as text and was saved verbatim.*
