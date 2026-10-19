<!-- Editor A-a: returned text saved verbatim; the reviewer could not write files -->

I couldn't save the report to `REPORT.md` (the write was refused), so the full report follows. **Decision: send to review. Recommendation: major revision.** I am moderately confident (about 0.6) that this is the right outcome, and fairly confident (about 0.85) that the mathematics is correct. No fatal issue found.

# Editor's report: "How much of a hyperbolic orbifold does heat hear?" (Annals of Global Analysis and Geometry)

I read the manuscript (55 pp.), the supplement (16 pp.) and both disclosed manuscripts:
- the AGAG companion "Finitely many eigenvalues determine the signature of a hyperbolic orbifold";
- the *Integers* note "Triples with equal sum and equal reciprocal sum".

Every figure and every page cited below was checked on page images rendered with pdftoppm. The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) are treated as known.

## 1. Summary

**Setting.** The paper studies closed orientable hyperbolic 2-orbifolds with cone points, of curvature −1. It asks for the least number of heat invariants c₁…c_k that separates an orbifold's genus and cone orders (its signature) from every orbifold with a different signature. Call this number K_mult.

**Geometric input.**
- The closed-form small-time expansion of the heat trace (Prop. 2.7). The authors re-derive it from the Selberg trace formula in Appendix B, with remainders that bracket the true value, and it agrees with Uçar's coefficients.
- The resulting triangular structure (Lemma 2.10, credited to Uçar): each new coefficient c_{l+2} adds exactly one new odd power sum P_{2l+1} of the cone orders, alongside the reciprocal sum R.

Everything after that is about signed multisets of cone orders whose low odd moments vanish.

**Main results.**
- **Theorem 1.1 / 3.8 (bounded orders).** If every cone order is at most M:
  - M invariants suffice within that class, and M+1 suffice against all orbifolds, at every area;
  - both numbers are sharp, by explicit Lagrange-weight constructions and a sign-change (Descartes-type) argument.
- **Theorem 1.2 / 3.14 and Prop. 3.15 (growth).**
  - The worst case f(A) over area ≤ A lies between about √(A/6π) and A/π + 4.
  - Growth like A^α is *equivalent* to N(k) = O(k^{1/α}), where N(k) is the least size of a Prouhet–Tarry–Escott (PTE) solution of degree k.
  - In particular, linear growth is equivalent to the open problem N(k) = O(k).
- **Theorem 1.3 (Theorems A–C and 3.11, spheres with n cone points).**
  - n invariants suffice.
  - Recovery reduces to a linear system whose determinant is the Orlando/Hurwitz form ∏(m_i+m_j)/∏m_i.
  - Changing the genus costs extra invariants, by Descartes' rule of signs.
- **Theorem 1.4 (§5, triangle orbifolds).**
  - Three invariants always suffice, and two suffice when p+q+r ≤ 17.
  - O(2,8,8) and O(3,3,12) form the unique minimal collision.
  - Their scalings are isolated because the curve C_{27/2} is a rank-0 elliptic curve (LMFDB 90.c3).

**Side results.**
- §2.4, variable curvature:
  - the coefficient of the new top power, and the part linear in the curvature jet, for every order (Prop. 2.11);
  - constant curvature is shown to be essential (Prop. 2.13).
- §4: the shape (moduli) enters only at order e^{−ℓ²/4t}, with an explicit constant.
- §6 and Appendix C: a stability theory for recovering the orders.
- Supplement S4–S6: finite-element spectra.

## 2. Significance

**What is good.**
- The question is natural for AGAG readers. It sits next to work by Dryden–Gordon–Greenwald–Webb, Stanhope, Rossetti–Schueth–Weilandt and Schueth.
- The answer "M+1, sharp, at every area" is clean.
- The PTE equivalence is a genuinely nice observation: it explains why the growth question is hard.
- The triangle-orbifold section is complete, and its account of the number 17 through strata is good.
- Prop. 2.11 is new and is the most geometric-analytic piece of the paper. It should interest people working on cone and corner heat coefficients.
- The paper is unusually honest about what is proved and what is only computed.

**What limits it.**
- After Lemma 2.10, everything is algebra on odd power sums. The tools are Newton's identities, a Vandermonde determinant, Descartes' rule, pigeonhole, and a rank-0 descent.
- Theorem 1.2 settles nothing about growth. It is a reformulation plus elementary √A and linear bounds, as the authors themselves say on p. 5.
- K_mult only makes sense in exactly constant curvature (Prop. 2.13).
- K_mult has no operational meaning for diffusion. By the paper's own Remark B.4, recovering c₃ of O(2,8,8) with a proved error needs t ≲ 7.8×10⁻¹¹ and trace values accurate to about 10⁻¹⁹.

A strict referee could argue the geometric novelty is below AGAG's bar. I do not think that is clear enough to desk-reject.

## 3. Correctness, and what I recomputed

The code is in `scratch/code/`. Computations are in exact arithmetic unless noted. I found no error.

1. **Cone polynomials (Lemma 2.6, Lemma 2.8, eqs. (4), (5), (8)).**
   - Rebuilt p₀…p₃ from the formulas; they match the printed ones.
   - p_l(1) = 0, and the leading coefficient is |B_{2l+2}|/(2(l+1)!(2l+1)), for l ≤ 5.
   - The area coefficients α₀…α₅ = 1, −1/3, 1/15, −4/315, 1/315, −4/3465.
   - The closed form for Φ_m holds.
2. **Expansion and remainders (Prop. 2.7, Prop. B.2).**
   - Computed the elliptic term E_m(t) by quadrature of the trace-formula integral for m = 2, 3, 8, 12 at t = 0.002.
   - It matches Σ b_l t^l. The remainder has sign (−1)^K and is at most |b_K| t^K for K = 1, 2, 3.
   - The claim on p. 11 about the signature (2;2) at t = 0.05 holds: the remainder is 1.034 times c₃t.
3. **Remark 4.3.** The Fourier identity and E_m = ∫ g_t k_m were confirmed numerically.
4. **Minimal pair.**
   - c₂ = 67/48 for both orbifolds.
   - The coefficients of the difference of the two heat traces are d₃ = 25/12, d₄ = −1775/24, d₅ = 153025/48.
   - Table S6's estimates of c₃ match the exact values −3.335417 and −5.41875 within their error bars.
5. **Prop. 2.11.**
   - The constant-curvature value of the top coefficient, (2l)!/l! K^l, is consistent with Lemma 2.8.
   - The linear part matches Dryden–Gordon–Greenwald–Webb's b₁.
   - The sign is consistent with u₂ = (K² − ΔK)/15.
6. **Theorem B.** The determinant equals ς_n∏(m_i+m_j)/∏m_i at (2,3,7) (value 75/7) and at (2,3,7,11) (value 35100/11).
7. **Explicit pairs.** Area and exact number of shared invariants were recomputed for:
   - Theorem C(3) and Example 3.6;
   - Example 3.17(i)–(ii);
   - (0;2¹⁰) vs (1;4⁴), and Theorem 3.8 with M = 3, 4;
   - the Table S1 rows with small orders, and (2;) vs (0;2⁸).

   All are as stated.
8. **Theorem 3.8(ii).** For M = 2…9 the least-genus pairs have areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054} and share exactly M−1 invariants.
9. **§5, by exhaustive enumeration of hyperbolic triads with sum S ≤ 600.**
   - No collision for S ≤ 17, and a unique collision at S = 18.
   - The first-overlap sums S*(p) for p ≤ 14.
   - All "first collision" entries of Table S2, and the 83 triads of Table S3.
   - The list of 38 collision-free sums exactly.

   I also checked Lemma 5.2, Theorem 5.4 and Theorem 5.7 by hand.
10. **Theorem 5.8.**
    - The map ψ sends E into C_{27/2}, and φ∘ψ = id on the 12 points.
    - The discriminant is 2¹⁸3⁸5⁶, and #E(F₇) = #E(F₁₁) = 12.
    - (16, 400) is a flex: the tangent y = 21x + 64 meets E with multiplicity 3 there.
    - The j-invariant and c₄ (scaled by 2⁴) match LMFDB 90.c3: rank 0, torsion Z/2×Z/6, checked via the LMFDB API.
    - I redid the hand 2-isogeny descent of Appendix E; it is correct.
11. **Lemmas 2.4, 2.5, B.3 and Remark B.4.**
    - Re-derived the constant C_hyp in (3).
    - Reproduced δ₁ ≈ 4.9×10³ t₃ and the thresholds 7.8×10⁻¹¹ and 2×10⁻¹⁹.
12. **Prop. 6.1, 6.3(i), 6.4.** P₃ = −18c̃₁ − 120c̃₂ − 360c̃₃; amplification factors 2, 14, 498; δR and δP₃ for (2,8,8).
13. **Literature.**
    - Croot–Mao–Yip (arXiv:2609.05061) give the best known PTE bound as k(k+1)/2 + 1 (Wooley). So "no o(k²) bound is known" stands.
    - Schueth's AGAG paper (arXiv:2511.22255) treats the coefficient b_{1/2} for non-smooth cones and does not anticipate Prop. 2.11.
    - 14 DOIs checked against Crossref; the bibliographic data agree.

**Not re-run:** the finite-element spectra, the n = 4 and n = 5 searches, the size-8 search, the 525 area classes, and the Table S1 rows with huge orders. No proof depends on them.

## 4. FATAL

None found.

## 5. MAJOR

**M1. The physical framing overstates what is "heard"** (title; abstract p. 1; §1 pp. 2–3; §6; Appendix B pp. 46–47).
- The theorems count coefficients of a divergent asymptotic series. Heat at any fixed t > 0 hears the whole spectrum, and therefore the signature (Dryden–Strohmaier).
- The coefficients can only be reached by extrapolating to t → 0. Lemma B.3 and Remark B.4 show this needs t ~ 10⁻¹¹ and 19-digit trace values already for c₃ of O(2,8,8).
- The coefficients grow like l!(m/π)^{2l} (p. 33). Requiring "M+1" or "√A many" invariants therefore corresponds to no realisable diffusion experiment.
- The caveat on p. 3 ("counts coefficients … not lengths of time") is right, but the title and abstract lead with the opposite picture.
- *Fix:*
  - Retitle around "heat invariants".
  - Say in the abstract and §1 that K_mult is an algebraic invariant of the coefficient sequence.
  - Bring Remark B.4's numbers forward.
  - State explicitly what short-time diffusion can and cannot detect: the signature through the coefficients; the moduli only at e^{−ℓ²/4t}; everything at fixed t.

**M2. Significance relative to the geometric input** (pp. 5–7, §§3, 5, 6).
- After Lemma 2.10 (Uçar), every result is about odd power sums:
  - Theorem A is Newton's identities;
  - Theorem 3.4 is "proved in the same way" as the classical bound N(k) ≥ k+1;
  - Theorem 1.1(i) is a Vandermonde determinant;
  - Theorem 1.2 is a reformulation;
  - §5 is inequalities on strata plus one rank-0 curve.
- The genuinely new parts for AGAG are Theorem 1.1(ii)–(iv), Prop. 2.11 and the Hurwitz form in Theorem B.
- *Fix:*
  - Add a two- or three-sentence contribution statement.
  - Either strengthen the analytic side — e.g. decide K_mult(O(p,q,r); Sig) (see m2), or go beyond the radial case in Prop. 2.11 (Problem 5(b)).
  - Or move the non-essential algebra to the supplement: §6, Appendix C, Theorem C(2).

**M3. Overlap with the disclosed manuscripts** (pp. 5, 7, 37; companion pp. 5–6 and its Table 1; note pp. 13–14).
- (a) The AGAG companion restates and reproves in its Appendix A: Theorem 2.3, Lemma B.1, Lemmas 2.4–2.6, Prop. B.2, Lemmas 2.8 and 2.10, Lemma 3.3, Corollary 3.5 and Theorem 3.8(i).
- (b) Both AGAG manuscripts describe the same finite-element spectra: method, error budgets and completeness tests.
- (c) Theorem 5.8 is proved twice, by the same 2-isogeny descent: here (Appendix E) and in the *Integers* note (§5). The S ≤ 4800 enumeration is also reported in both.
- *Fix:*
  - Put the proofs of the shared preliminaries in one paper and have the companion cite them.
  - Describe the finite-element computations once.
  - Prove Theorem 5.8 in the arithmetic note and cite it here.
  - Otherwise the journal must explicitly accept the duplication, with a common referee for both AGAG submissions.

**M4. Rigidity of K_mult** (pp. 3, 13, 16–18).
- Prop. 2.13 shows that away from constant curvature the counts carry no information.
- (i) A physical drum does not know its curvature is −1. With unknown constant curvature K < 0, c₁ no longer fixes the area alone. "One more unknown" (p. 13) does not say how Theorems 1.1 and 1.2 change.
- (ii) Collisions are exact equalities, so K_mult is unstable under perturbation of the metric. This should be said.
- *Fix:* a proposition on unknown constant curvature (c₂ is scale-invariant; say how the c_j scale), and an explicit stability remark.

## 6. MINOR

- **m1 (p. 3 vs p. 33).** The l!(m/π)^{2l} growth is stated as fact in the introduction but called heuristic and unproved on p. 33. It is easy to prove: Φ_m has simple poles at ±π/m and positive Taylor coefficients, and the k = l term dominates b_l. Prove it, or label it heuristic in both places.
- **m2 (p. 34).** "Against all of Sig, Theorem 1.1(ii) gives the bound r+1 for O(p,q,r)" is much weaker than what the paper already has.
  - Corollary 1.5 gives K_mult(O(p,q,r); Sig) ≤ ⌊2(1−R)⌋ + 4 ≤ 5, and ≤ 4 when R > 1/2, because the area is below 2π.
  - The open question is therefore 3 versus 4 or 5, and might be settled by a finite search over each triangle's (finite) equal-area class.
- **m3 (pp. 6–7).** The classical corner literature is missing:
  - Kac (1966); McKean–Singer (1967);
  - van den Berg–Srisatkunarajah (1990). Their corner term (π²−γ²)/(24πγ) at γ = π/m is exactly half of (m²−1)/(12m), as it must be for a double;
  - Mazzeo–Rowlett (2015); Lu–Rowlett (2016);
  - the work on hearing local orientability of orbifolds.

  Uçar's W_ν on p. 12 is the higher-order version of the van den Berg–Srisatkunarajah term, and saying so would orient readers.
- **m4 (p. 26).** For "no bound o(k²) is known", cite the primary sources (Wooley, Hua), not only the 1994 survey and a 2026 preprint.
- **m5 (p. 13).** The sentence on unknown curvature K is too terse (see M4(i)).
- **m6 (p. 16, Prop. 2.13(ii)).** The example (0;3,3,3) has χ = 0. Say that the constructed metrics have curvature K₀ only near the cone points, so χ is not tied to the area.
- **m7 (pp. 4, 26).** The constants 1/3 and 8π in Theorem 1.2(i) are artefacts of the construction (Lemma A.1 plus doubling); say so.
- **m8 (p. 30).** For "pairwise non-isometric", say whether the argument is λ₁ or the systoles. Both are floating-point, so neither is a proof.
- **m9 (p. 41, Corollary 6.5).** State in the corollary itself that it is rigorous only given a proved data error δ₁, and that Lemma B.3's δ₁ is unattainable in practice.
- **m10 (p. 25, Theorem 3.13).** The smaller genus of the constructed pairs is at most 2, so adding handles gives any g ≥ 2. Make the statement precise.

## 7. Presentation

- **P1 (pp. 7–8).** Table 1 splits the sentence ending "…is the same computation [Table 1] as the note's". "Table 1 lists the notation" is stated twice (pp. 3 and 8).
- **P2 (pp. 18–20 vs 47–49).** Theorems A, B, C in §3 clash with Theorems C.2–C.4 and Lemma C.1 in Appendix C; "Theorem C(3)" and "Theorem C.3" are different objects. Renumber.
- **P3 (throughout).** Overloaded symbols:
  - C: a comparison class, the constant in Theorem 3.8, 2 sin(ϑ/2), the constant in Theorem 3.14(b), and C_hyp;
  - T: T(L), the tanh series T(z), and T(ϑ);
  - a: a_l, a_{l,k}, and "a" as a node;
  - α_k vs a_k.
- **P4 (p. 42, Fig. 8).** No legend, and the caption does not identify the curves (only the text on p. 41 does).
- **P5 (p. 2, Fig. 1; p. 31, Fig. 4(a)).** Both are stylised. Fig. 4(a) draws smooth barrels with the cone points unmarked; mark them or drop the panel.
- **P6 (§1).** Each result is stated two or three times. A single "result / new? / method / where" table would make the novelty claims checkable.
- **P7.** There are many forward references to the supplement. Prop. S3.1 is used in Corollary 6.5 and belongs in the paper.

## 8. Overlap with the related manuscripts

**AGAG companion.**
- What is shared:
  - nine groups of this paper's results, listed in the companion's Table 1 and reproved in its Appendix A;
  - the same finite-element spectra (the companion uses only eigenvalues below about 1.6×10⁴).
- The questions differ. The companion's diameter bound, eigenvalue counting and the O(2,3,m) cusp behaviour are not here.
- The statements of the shared results are consistent.
- Verdict: disclosed and honestly bounded, but the duplication should be removed (M3).

***Integers* note.**
- What is shared:
  - the minimal pair;
  - Theorem 5.8, proved in both;
  - the triad enumeration (S ≤ 4800 here, ≤ 6000 there).
- The statements are consistent: torsion Z/2×Z/6, Selmer groups of orders 4 and 1, and collision counts agreeing with my enumeration.
- Verdict: prove Theorem 5.8 in one place.

No undisclosed overlap was found within the materials provided.

## 9. Editorial decision and recommendation

**Decision: send to review.**
- The paper is in scope, correct as far as I could check (extensively), and has new content of interest: the sharp M+1, Prop. 2.11, the PTE equivalence and the minimal triangle pair.
- The concerns — framing, significance, overlap — are for referees and revision, not for a desk rejection.
- Referees should be:
  - (1) a spectral geometer working on heat coefficients of singular spaces;
  - (2) a number theorist familiar with PTE and elliptic curves.
- The companion AGAG submission should go to at least one of the same referees, and the *Integers* note should be made available to them.

**Recommendation: major revision.**
- Confidence about 0.6 in this outcome; about 0.85 that the mathematics is correct.
- A rejection on significance grounds (M2) would not be unreasonable.
- Acceptance requires M1–M4 to be resolved substantively.

## 10. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Retitle around "heat invariants"; state what short-time diffusion can and cannot detect; bring Remark B.4 forward. |
| M2 | Add a contribution statement; strengthen the analysis (decide K_mult of triangle orbifolds against Sig, or extend Prop. 2.11), or move §6, Appendix C and Theorem C(2) to the supplement. |
| M3 | One location each for the shared proofs, the finite-element method and Theorem 5.8; otherwise explicit journal acceptance with a common referee. |
| M4 | A proposition on unknown constant curvature and a remark on the instability of K_mult. |
| m1 | Prove the l!(m/π)^{2l} growth or label it heuristic in both places. |
| m2 | Replace "r+1" by ≤ ⌊2(1−R)⌋ + 4 ≤ 5; restate the open question as 3 versus 4 or 5. |
| m3, m4 | Add the classical corner literature and the primary PTE sources. |
| m5–m10 | Wording fixes as indicated. |
| P1–P7 | Fix the float placement and theorem numbering; disambiguate symbols; add a legend to Fig. 8; mark or drop Fig. 4(a); add a novelty table; bring Prop. S3.1 into the paper. |
