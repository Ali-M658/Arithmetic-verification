<!-- Round 9 A-a editor report: returned text saved verbatim; the reviewer could not write files -->

I could not save the report to REPORT.md because the harness refused the write, so the full report follows below. Decision: send to review. Recommendation: major revision. There is no fatal issue, and I found no mathematical error in any proved statement. My checks are listed in the "Correctness" section; the scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/A-a-editor-singular-heat-asymptotics/scratch/checks/`.

# Handling editor's report: "How much of a hyperbolic orbifold does heat hear?" (AGAG submission)

Materials read: the manuscript (61 pp.), its supplement (17 pp.), and the two disclosed companions: *Finitely many eigenvalues determine the signature of a hyperbolic orbifold* (38 pp., also for AGAG) and *Triples with equal sum and equal reciprocal sum* (24 pp., for Integers). Before commenting on any figure or formula I looked at the rendered pages (Figs. 1–8; pp. 2–4, 16, 24, 32, 35, 37, 39, 42, 46). As instructed, the placeholders for author contributions, the AI-use statement, the Zenodo DOI and the preprint identifiers are treated as known and are not raised below.

## Summary

The paper works with closed orientable 2-orbifolds of curvature −1 that have only cone points. It asks for the least number k of heat invariants c₁,…,c_k (cⱼ is the coefficient of t^{j−2}) that separates the signature (g; m₁,…,m_n) of one such orbifold from every other signature in the class Sig. The main results are as follows.

- **Thm 1.1 / 3.11 (bounded orders).** Within Sig_{≤M} the answer is exactly M. Against all of Sig it is M+1, uniformly in the area, and M+1 is attained for every M. It is also at most 2d_O+2.
- **Thm 1.2 / 3.18, Prop 3.19 (growth).** Let f(A) be the worst case over area ≤ A. Then ⌊√((A/2π−1)/3)⌋+2 ≤ f(A) ≤ ⌊A/π⌋+4. Power-law lower and upper bounds on f are equivalent to the corresponding bounds on the least size N(k) of a degree-k Prouhet–Tarry–Escott (PTE) solution. In particular, linear growth of f is equivalent to the open problem N(k)=O(k).
- **Thm 1.3 / 3.2–3.4, 3.15.** n invariants determine the orders of a sphere with n cone points. The orders come from a linear system whose determinant is given in closed form via Orlando's formula. A change of genus costs extra invariants (a Descartes-rule argument).
- **Thm 1.4 / §5.** Three invariants determine a triangle orbifold. If p+q+r ≤ 17, two suffice. O(2,8,8) and O(3,3,12) form the first collision, and the pair of least area in all of Sig that shares c₁ and c₂. The pair is isolated: the curve C_{27/2} has rank 0 and torsion ℤ/2×ℤ/6.
- **Analytic side (§2, App. B).** A closed form of Uçar's constant-curvature expansion, with enveloping remainders (Prop 2.8, B.2) and the asymptotics of the cone coefficients (Lemma B.3).
- **Variable curvature (§2.4).** The linear-in-jet part of every cone coefficient in variable curvature (Prop 2.14). Constructions showing that equal c₂ allows metrics with equal H_L, and that the minimal pair carries metrics, flat near the cone points, whose invariants agree to all orders (Prop 2.16). A conjecture on the general structure of the cone terms, supported by a derivation in outline (Conj 2.13).
- **Supporting material.** A Lipschitz/Hölder stability theorem for recovering the orders (§6, App. C). Numerical illustrations from finite-element spectra (§4, supplement S4–S6).

## Significance

**What is good.** The paper is careful and honest, and I could not fault any of its arithmetic.
- It says plainly that the counts are invariants of the sequence of coefficients, not lengths of time, and that the growth theorem is a reformulation.
- It separates proved, computed and conjectured statements.
- The exact answer M+1 for bounded orders is clean and nontrivial: Chebyshev sign changes give the upper bound, and divided-difference witnesses give the lower bound.
- The link to PTE is neat and correctly calibrated.
- The isolation argument for C_{27/2} is complete and checked by hand.
- Prop 2.14 is a genuine all-order result about cone coefficients of *curved* orbifold cones. Researchers in singular heat asymptotics will want to see it next to Schueth's recent AGAG paper [25].

**Where the significance is limited.**
- Almost all of the geometric input is Uçar's: the coefficients and the triangular structure. Everything downstream of Lemma 2.11 is the algebra of odd power sums (Newton, Vandermonde, Orlando, Descartes/Chebyshev), PTE combinatorics, or the arithmetic of one elliptic curve.
- The headline growth question stays open, between √A and A. Even whether f grows like a power of A is left open.
- The variable-curvature structure result is stated as a conjecture.
- For AGAG's readership, the new analysis is Prop B.2, Lemma B.3, Prop 2.14 and Prop 2.16. That is real but modest. The paper's weight rests on the combinatorial reduction.
- Referees should judge whether the combination clears AGAG's bar. My own view is that it can, provided the framing changes (M1, M2).

**Scope.** In scope: 58J53, inverse spectral problems on orbifolds, in the line of Dryden–Gordon–Greenwald–Webb, Stanhope, Rossetti–Schueth–Weilandt and Abreu–Dryden–Freitas–Godinho, all of which AGAG has published.

**Physical framing: what short-time diffusion can and cannot detect.** The paper is mostly accurate here.
- Kac locality, the orbifold-image picture (influence radius √t/sin(π/m); I checked the 0.55, 1.8 and 1% figures), and the non-diffractive nature of orbifold cone points (Rem. 4.3) are all stated correctly.
- So is the point that the moduli enter only through e^{−ℓ²/4t} (Prop 4.2).
- Rem. B.5 shows, to its credit, that a *proved* reading of even c₃ needs trace values at t < 10⁻³ with absolute accuracy of about 10⁻⁸. That is below what a list of roughly 2850 computed eigenvalues resolves.
- But this candour undercuts the title and the opening of the Introduction. Heat at any positive time "hears" the whole spectrum, and the spectrum determines the signature (Dryden–Strohmaier, Doyle–Rossetti). What the paper counts is exact coincidences of Taylor-type coefficients of an asymptotic, factorially divergent series (Lemma B.3).
- By the paper's own §2.3 discussion, these coincidences are destroyed by arbitrarily small non-constant-curvature perturbations.
- So the paper is about heat *invariants*, not heat *diffusion*. See M1.

## Correctness, and what I recomputed

I recomputed the following independently, with exact sympy/Fraction arithmetic and mpmath quadrature. Scripts are in `scratch/checks/`.

1. **Cone polynomials and area coefficients.** I took p₀,…,p₃ from (4)–(5). They agree with (8). Their leading coefficients equal |B_{2l+2}|/(2(l+1)!(2l+1)) (Lemma 2.9), and α₀,…,α₄ = 1, −1/3, 1/15, −4/315, 1/315.
2. **The expansion and its enveloping remainders, numerically.** I integrated E_m(t) of Thm 2.3 directly for m = 3, 8, 12 and t = 10⁻³, 10⁻². The truncation remainders alternate with sign (−1)^K and are bounded by |b_K(m)|t^K, as Prop B.2(a) states. This also independently confirms b₀ and b₁ (b₁ = −p₁/m) for m = 3, 8, 12.
3. **Minimal pair.** d₃, d₄, d₅ = 25/12, −1775/24, 153025/48. Also c₁ = 1/8 and c₂ = 67/48; c₃(2,8,8) = −3.33542 and c₃(3,3,12) = −5.41875, matching Table S6.
4. **Thm 3.3 (determinant).** det M = (−1)^{n(n+1)/2} ∏_{i<j}(m_i+m_j)/∏m_i, checked exactly at five multisets with n = 3, 4, 5.
5. **Thm 3.11.** The pairs for M = 2, 3, 4, both (ii) and (iv) with X = 4. The least-g areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054} for M = 2,…,9, and the constants C.
6. **Examples.** 3.4(3), 3.9 and 3.21(i)–(ii): areas, the shared invariants, and that the next invariant differs. Also (0;2¹⁰) against (1;4⁴), and (2;) against (0;2⁸).
7. **Thm 5.5, Table S2, Theorem 5.6–5.8 and Computation S2.1 (up to S = 600).**
   - I recomputed S*(p) for p ≤ 14 and the first adjacent collisions by brute force.
   - The only collision with S ≤ 18 is the minimal pair.
   - The collision-free sums up to 600 are exactly the 38 listed (all of them are ≤ 557).
   - I checked the "least area in all of Sig" argument of Thm 5.8 by hand.
8. **Thm 5.9.**
   - ψ maps E into C_{27/2}, and φ∘ψ = id on E.
   - All eleven listed affine points are on E (with ∞, twelve rational points).
   - #E(𝔽₇) = #E(𝔽₁₁) = 12.
   - Δ = 2¹⁸3⁸5⁶ and j = 4102915888729/9000000. j, c₄ and c₆ match LMFDB 90.c3 (rank 0, torsion [2,6]; queried through the public API).
   - I verified the hand 2-isogeny descent of Appendix E line by line: the mod-5 argument on E, and the mod-3/mod-9 arguments on E′.
9. **Variable curvature.**
   - I recomputed the Duhamel integral in Prop 2.14 (−2l·l!·4^l t^l C^{−2l−2}) and the normalisation λ_l = 2/(l−1)!.
   - The top coefficient (2l)!/l!·K^l of Conj 2.13(ii) is consistent with Lemma 2.9.
   - The K³ and Δ²K terms of Rem 2.15(b) agree with p₃ and with Prop 2.14 (checked at m = 2).
   - ω₂ = 1/30 in Prop 2.16 reproduces Ω₁ = (1/60π)∫K².
10. **Constants.**
    - amp₀,…,amp₄ = 2, 14, 498, 4062, 56230/3, and the row P₃ = −18c̃₁ − 120c̃₂ − 360c̃₃ (Prop 6.1).
    - Lemma 2.5's constant C_hyp and its range.
    - The Remark B.5 numbers: δ₁ ≈ 4.9×10³τ, τ ≈ 7.8×10⁻¹¹ and η ≤ 2.07×10⁻¹⁹.
11. **Proofs checked by hand.**
    - Lemma 2.4, Lemma 2.7, Lemma 3.1, Thm 3.2, Thm 3.7, Cor 3.8, Lemma 3.10, Thm 3.11(i)–(iv), Lemma 3.14, Thm 3.15, Prop 3.16, Prop 3.19, Thm 3.18(a)–(d), Lemma A.1, Prop A.2, Cor 5.1, Prop 5.2, Lemma 5.4, Prop D.1 and Prop 6.4.
    - The formula in Remark 4.3, including the pole location ±2πi/m.
    - The reference metadata for 14 entries via Crossref/arXiv. All are correct, including [25], whose published title differs from its arXiv title.

I found no mathematical error in any proved statement.

Not verified by me:
- the finite-element spectra and the supplement's searches. They are labelled as non-proofs and nothing depends on them.
- the outline behind Conjecture 2.13.
- Prop S3.1 and the Table S4 values.

## FATAL

None.

## MAJOR

**M1 (pp. 1–3, title, abstract and §1). The framing promises more than the paper delivers.**
- The title and the first paragraphs present the problem as what short-time heat *diffusion* detects. The paper then concedes (p. 3, Rem. B.5 on pp. 52–53, and Cor. 6.5) three things:
  - the counts are about exact equalities of coefficients;
  - the heat trace on any interval determines everything;
  - the proved recovery of c₃ needs data far beyond computed spectra.
- These are not quantities a diffusion experiment, or the trace at accessible times, can see.
- Asks:
  - Retitle the paper, e.g. "How many heat invariants determine the signature of a hyperbolic orbifold?".
  - Reduce the diffusion narrative to a short, accurate paragraph.
  - Shorten the abstract to the results, without the third sentence's caveats.
- This is a significance and accuracy issue, not a matter of style.

**M2 (pp. 5–8, 13–14). What exactly is new should be stated sharply, and the analytic novelty separated from the combinatorics.**
- The paper does acknowledge Uçar for Lemma 2.11 and for the coefficients.
- But a reader of the Introduction has to work hard to find which statements need anything beyond Uçar plus classical power-sum algebra.
- Asks:
  - Put one short list at the start of §1.2: (a) new geometric/analytic results (Prop B.2, Lemma B.3, Prop 2.14, Prop 2.16); (b) new results about power sums (Thm 3.11(ii)–(iv), Thm 3.15, Prop 3.16, Thm 3.18/Prop 3.19); (c) arithmetic (Thm 5.9).
  - State openly that Thm 1.2 settles no growth exponent.
- Referees will then be able to judge significance for AGAG directly.

**M3 (pp. 15–18). An unproved conjecture is carried with a page-long "derivation in outline".**
- The authors themselves list three steps that are not carried out:
  - Donnelly's dependence on dΦ_p;
  - the radial reduction up to quadratic non-radial terms;
  - uniformity in ϑ.
- A journal article should not carry an outline proof in the main text.
- Asks: either complete these steps, which would turn Conj 2.13 into a theorem and substantially raise the paper's value for AGAG's singular-asymptotics readership, or reduce it to a stated conjecture. In the second case, give the evidence (Rem 2.15) and move the outline to the supplement.
- Separately, the K∆K coefficients of Rem 2.15(b) below the top one rest on a single machine computation (p. 18). Either check them independently or label them as unconfirmed.

**M4 (pp. 6–8; companion pp. 6 and 32–36; note p. 17). Overlap with the disclosed manuscripts needs editorial handling.**
- The disclosure is clear and accurate, and the dependence structure is acyclic for main results.
- However, the AGAG companion reproduces this paper's proofs nearly verbatim in its Appendix A: Lemma B.1 ↔ A.1, Lemma 2.7 ↔ A.2, Prop B.2 ↔ Prop 2.3, and Lemmas 2.4–2.5 ↔ 2.2.
- It also restates Lemma 3.6, Cor 3.8 and Thm 3.11(i), and shares all computed spectra and the code deposit.
- By a word-shingle comparison that excludes formulas, about 4% of the companion's prose coincides with this paper. This is concentrated in those proofs.
- Two simultaneous AGAG submissions with duplicated proofs and mutual forward references to unpublished work (Rem 2.6 and B.5 here; the companion's Table 1) must be handled by one editor, and both referees must receive both papers.
- Asks: either keep the proofs in one place, with the other citing them, or justify why merging is undesirable.
- The Integers note proves the same isolation statement as Thm 5.9 by machine. This is fine as disclosed, but the note cites it as "[17, Theorem 5.8], proved there by a 2-isogeny descent by hand" (note p. 17). In this manuscript that statement is Thm 5.9 / Appendix E, so the cross-reference must be corrected.

**M5 (p. 36). The "cone timescale" is stated heuristically but can be proved, and it is exactly the statement that would make the physical discussion rigorous.**
- By Remark 4.3, E_m(t) = ∫g_t(u)k_m(u)du, with k_m analytic in |Im u| < 2π/m.
- The standard optimal-truncation argument (Cauchy estimates for the Taylor remainder of k_m on a strip, integrated against the Gaussian) gives a remainder of size O(e^{−(π/m)²(1−ε)/t}) at the optimal order l ≈ π²/(m²t).
- That proves the paper's heuristic e^{−π²/(µ²t)}, which is currently stated only heuristically.
- With Prop 4.2 this yields a proved two-scale picture: cone remainder e^{−π²/(µ²t)} against geodesic term e^{−ℓ²/4t}.
- Asks: prove it, or remove the heuristic claims from §1 and §4.

## MINOR

- **m1 (p. 34, Prop 4.2).** "the classes of γ and γ⁻¹ are counted separately". When Γ has 2-torsion, γ can be conjugate to γ⁻¹; the companion's Lemma 2.2 says so explicitly. Harmonise the definition of w_O and of n_O(x) in Lemma 2.4. This matters for the multiplicity-2 fit reported in S4.
- **m2 (p. 29).** "the 2026 paper [48]": [48] is an arXiv preprint, so call it a preprint.
- **m3 (p. 39, Prop 5.2 proof).** In "which leaves {2,2,2,2,x} and {2,2,2,3,x} with 3 ≤ x ≤ 5", the range applies only to the second family, and the values "1 + 6/x" belong to the first. Say so.
- **m4 (pp. 15–16).** With ∆ = −div grad, (−∆)^{l−1}K is the iterated *Euclidean-sign* Laplacian. One sentence noting this would prevent sign errors (I checked that Prop 2.14 is consistent).
- **m5 (pp. 19–20, Prop 2.16(ii)).** The Jacobian with respect to the L scales should be displayed. The argument also controls Ω₁,…,Ω_L while only Ω₁,…,Ω_{L−2} are needed; say this or trim it.
- **m6 (p. 20, Prop 2.16(iii)).** "Constant curvature is essential" overstates what is shown. Flat cone points contribute only to c₂, which is classical, so the all-orders coincidence is a property of this special family of metrics. Rephrase as "the counts are not stable outside constant curvature".
- **m7 (p. 41, Thm 5.8).** The "least area in all of Sig" assertion deserves its own label (it is used in the abstract) and an explicit statement that it is unique.
- **m8 (p. 26).** The minimality of the areas 12π and 36π (M = 3, 4) rests on a search. Mark it as such in the text where it is stated, not only in S7.
- **m9 (p. 25, Thm 3.11(ii)).** Define C by a formula (lcm of the denominators, then possibly doubled) rather than "least positive integer for which…". I recomputed C for M ≤ 9.
- **m10 (Lemma 3.14(c), p. 28).** "W being the side of that genus" is ambiguous when the genera are equal. Make it precise.
- **m11 (pp. 7–8, literature).** The authors might add Mazzeo–Rowlett's heat-trace anomaly on polygons and Sher's work on conic degeneration as context for curved-cone coefficients. This is optional.

## Presentation

- **P1.** The prose is extremely dense. Sentences routinely carry three to five parenthetical qualifications; see the abstract and pp. 5–7, especially "What is elementary and what is not". Break them up. Results should be stated before their caveats.
- **P2.** Fig. 1 (p. 3) is "stylised, not isometric" and lifts triangles to a surface in space. A plain Poincaré-disc rendering would show the same heat-kernel data without suggesting a geometry the orbifold does not have. Figs. 2–8 match their captions and the text; I checked these against the rendered pages.
- **P3.** Each main theorem appears twice (§1.1 and §§3–5), under different numbers. Give "(= Theorem 3.11)" tags at the §1 statements.
- **P4.** The indexing convention (c_j is the coefficient of t^{j−2}, so c_{l+2} ↔ b_l) is easy to misread. Repeat it at Lemma 3.6 and in Thm 1.1.
- **P5.** Computational asides in the main text (Rem 3.5, Rem 3.22, the end of §3.4, and §4's numerics) could be grouped so that the proved line of argument reads continuously.

## Overlap with the related manuscripts

- **Eigenvalue manuscript (AGAG).** It shares the trace-formula preliminaries and the heat-invariant structure, reproved verbatim in its Appendix A, together with the computed spectra and the code deposit. Its main results are disjoint from those here: the effective eigenvalue count, the diameter bound, the closed-geodesic count and the cusp-like behaviour. The cross-references in its Table 1 point to the correct items here. Neither paper's main proofs depend on the other. Action: see M4.
- **Integers note.** It overlaps only in Thm 5.9: the same rank and torsion statement for C_{27/2}, proved by machine in the note and by hand here. It also overlaps in the triad enumeration up to S = 4800. The citations here of the note's Theorems B and C match the note's statements. The note mis-cites Theorem 5.8 for Theorem 5.9 (M4). No result here depends on the note.
- **Verdict.** There is no duplicate publication of main results, and the disclosure is adequate. The duplicated proofs between the two AGAG submissions should be resolved before acceptance.

## Editorial decision and recommendation

- **Decision:** send to review, not a desk rejection.
- **Reasons:** the paper is in scope, technically sound as far as I could check (a substantial part), and contains a clean exact result (M+1), an honest reduction to PTE, and a new all-order statement about curved cone coefficients.
- **Referees:** I will seek two. One should come from spectral geometry of orbifolds or singular heat asymptotics, with Section 2.4 and Conj 2.13 in focus. The other should come from Diophantine and PTE combinatorics, with §3.4 and §5 in focus. Both should receive the companion AGAG manuscript.
- **My recommendation:** major revision. **Confidence:** moderate–high on correctness, moderate on significance.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | New title and abstract centred on heat *invariants*; one accurate paragraph on what diffusion at accessible times detects. |
| M2 | An explicit novelty list split into analytic, combinatorial and arithmetic results; a clear statement that Thm 1.2 settles no exponent. |
| M3 | Prove Conj 2.13 (complete the three steps), or demote it to a stated conjecture with evidence and move the outline to the supplement; independently confirm or flag the K∆K coefficients. |
| M4 | De-duplicate the proofs between the two AGAG submissions (cite instead of reproving), or argue for or against merging; fix the note's cross-reference to Thm 5.9 / App. E. |
| M5 | Prove the optimal-truncation bound e^{−π²(1−ε)/(µ²t)} from Remark 4.3, or delete the heuristic timescale claims. |
| m1 | Harmonise how γ and γ⁻¹ are counted in Prop 4.2 and Lemma 2.4 with the companion's Lemma 2.2. |
| m2 | Describe [48] as a preprint. |
| m3 | Make clear which range and which values belong to which family in the Prop 5.2 proof. |
| m4 | Add one sentence on the sign convention of (−∆)^{l−1}K. |
| m5 | Display the scale Jacobian in Prop 2.16(ii) and trim the unneeded Ω's, or say why they are there. |
| m6 | Rephrase "constant curvature is essential". |
| m7 | Give the least-area statement of Thm 5.8 its own label and state uniqueness. |
| m8 | Mark the 12π/36π minimality as computational in the main text. |
| m9 | Define C in Thm 3.11(ii) by a formula. |
| m10 | Make "W" in Lemma 3.14(c) precise. |
| m11 | Optionally add the suggested references. |
| P1–P5 | Copy-editing for sentence length, Fig. 1 redrawn, cross-tags between §1 and §§3–5, the indexing reminder, and grouping of the computational asides. |
