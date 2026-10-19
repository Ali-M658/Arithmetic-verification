# FIX-CHECK-A (round 8): "How much of a hyperbolic orbifold does heat hear?"

Inputs used: `fixcheck-A/scratch/input/` only (manuscript.pdf, 61 pp.; supplement.pdf, 17 pp.; VERDICT-A.md).
Page numbers are the printed page numbers of the PDFs. The repository checks that VERDICT-A cites
(`check_heat_supporting.py` §9 and others) were not available, so only what the PDFs say was checked. Where it
mattered, the mathematics was recomputed by hand: Prop. 2.14's λ_l, ω_{l+1} for l = 1, 2, Lemma B.3's principal
parts and asymptotics, Prop. 5.2's case analysis, and Thm 5.8's area ≤ π/2 cases.

Summary: 9 of the 11 major items are DONE and 2 are PARTIAL (A4, A10). Among the minor items, 20 are DONE, 3 are
PARTIAL (a4, a6, a27), a3 is DONE with a leftover wording, and 4 were declined in VERDICT-A itself (a7, a8, a11
in part, a29). The revision has no broken cross-references. Every new label in the text resolves: Conjecture 2.13,
Propositions 2.14, 2.16 and 5.2, Lemmas B.3 and B.4, Remark B.5 and Problems 5–6. No stale "Proposition 2.13/2.15",
"Remark B.4" or "Lemma B.3" (old meaning) remains in either PDF.

## FATAL / MAJOR items

| id | status | check |
|---|---|---|
| A1 | DONE | Lemma B.4 (p. 52) now takes N ≥ n times with row bounds δ_{1,j}. Remark B.5 (pp. 52–53) gives: the three-time numbers (τ, τ/2, τ/4; δ1 ≈ 4.9e3 τ; τ < 7.8e-11); the N = 8 numbers (δ_thm: τ ≤ 3.6e-3, η ≤ 5.0e-13 at τ/2; δ_cert: τ ≤ 1.5e-2, η ≤ 1.3e-8); and the scan (N ≤ 16 in [a, T]: no δ_cert for a ≥ 1e-3, no δ_thm for a ≥ 3e-4). These match VERDICT-A. The abstract, the introduction (p. 3) and Corollary 6.5 (p. 46) all say the proved recoveries need times shorter than computed spectra resolve. One small overstatement: the introduction says "values accurate to a few times 10^-8 or better", but the best configuration in Remark B.5 allows η ≤ 1.3e-8. "About 10^-8 or better" would match. |
| A2 | DONE | Conjecture 2.13 (p. 16) contains (i) and (ii). The three steps not carried out are named and the derivation is labelled "in outline". The text says "No result of the paper uses the conjecture"; no proof cites it. Proposition 2.14 (pp. 17–18) has a complete proof: Donnelly invariance, Ricci identities, invariant linear forms on Sym^{2l−2}, and Duhamel with ψ = ζ0\|x\|^{2l}. I recomputed the Gaussian integral (−2l·l!·4^l t^l C^{−2l−2}), (−1)^{l−1}Δ_0^l\|x\|^{2l}(0) = −4^l (l!)^2, and λ_l = 2/(l−1)! · C^{−2l−2}. They agree with the statement, with β_{1,2} = 2K and β_{2,3}'s −2ΔK, and at l = 1 with 2Π_2(m) = p_1(m)/m. The introduction (pp. 6–7), the closing paragraph of §2.4 (p. 20), Remark 2.15 and Problem 6 are consistent with the split. |
| A3 | DONE | Prop. 2.16(ii) proof (pp. 19–20) now gives the trace identity for f a(D) f b(D), the completed square, the Gaussian moment and the s-integrals, and ω_{l+1} as an explicit sum with its closed form. I checked that the sum equals (−1)^n n(n−1) n!/(2n+1)! for n = 2, 3 and that it gives 1/(60π)∫K² at l = 1. Analyticity of G_l and the vanishing first derivative are stated with reasons. The exact scaling ε^{−2l}G_l(θ) is stated ("no uniformity in ε is needed"). |
| A4 | PARTIAL | The sentence after Theorem C.4 (p. 54) is present. It says Table S4 uses the exact cond, the closed form is smaller by large factors, and the certificate used is Prop. S3.1. Two problems remain. (1) The relabelling did not reach the two places that still call δ_thm closed-form. Supplement Table S4's caption (p. 9) says "the closed form δ_thm of Theorem C.4". §6, p. 46 says "The closed form δ_thm is far from sharp … on the eleven multisets of Table S4". Both now contradict p. 54. Both should say "δ_thm of Theorem C.4 (with the exact cond)". (2) The new sentence sits between the statement of Theorem C.4 and its proof. It should go after the proof, or into a remark. |
| A5 | DONE | Proposition 5.2 (p. 39) is proved. I checked each case: the area bound gives g = 0, n′ ≤ 5 or (1;1); (1;m) is impossible because m³ < (p+q+r)³; for five orders, (p+q+r)R ∈ {1+6/x, 10/6, 11/12, 12/30} < 9; for four orders, 4/a > 1. The search statement and its supplement entry (S7) are present, and Problem 5 (p. 47) is added. The abstract says "Among triangle orbifolds three invariants always suffice; against all orbifolds the question reduces to one Diophantine system in four orders". Nits: (i) in the proof, "{2,2,2,2,x} and {2,2,2,3,x} with 3 ≤ x ≤ 5" reads as if the range also applies to the first family, where x is unrestricted; the computation 1 + 6/x covers it anyway. (ii) Problem 5 says "positive integers p, q, r". The equivalence with K_mult ≤ 3 holds because equal reciprocal sums force p, q, r ≥ 2 and R < 1, but this is not said. |
| A6 | DONE | A sentence on what a count measures geometrically and on constant curvature is on p. 3 ("Geometrically, a count measures …; Proposition 2.16 shows …"). The variable-curvature caveat is in the abstract. The title is unchanged, as declared. |
| A7 | DONE | Abstract and introduction (p. 3) say "on any interval of (positive) times". No "fixed t" wording remains. |
| A8 | DONE | The last sentence of the abstract is the constant-curvature caveat, as quoted in VERDICT-A. |
| A9 | DONE | The introduction (p. 5) says the stability theorem tells "how accurately the invariants must be known for the counts to be usable, the quantitative side of what heat diffusion can detect". |
| A10 | PARTIAL (formatting only) | Karlin–Studden [5], de Boor [6] and Pólya–Szegő Part V [7] are cited at Lemma 3.10, Theorem 3.11(ii) and Theorem 3.15. The "what is new" paragraphs (pp. 5–6 and p. 8) are rewritten to credit them. New error: reference [6] prints as "Boor, C.: Divided differences" and should be "de Boor, C." (a BibTeX name-particle problem). |
| A11 | DONE | Lemma B.3 (p. 51) is proved. I checked the principal parts at ±π/m, which sum to A_m Σ(mu/π)^{2k}; the remainder is holomorphic in \|u\| < 2π/m (including the m = 2 boundary case under the ρ < 2 Cauchy estimate); dominated convergence works with middle factor ~ (4l)^{−j} → 0; and 4^{−l}(2l)!/l! ~ l!/√(πl). The result \|b_l(m)\| ~ A_m(πl)^{−1/2} l!(m/π)^{2l} is quoted identically in the introduction (p. 3) and §4 (p. 36). Optimal truncation is still labelled "Heuristically" (p. 36). |

## Minor items

| id | status | check |
|---|---|---|
| a1 | DONE | The erratum [44] is cited where (5.7) is used (p. 14). |
| a2 | DONE | Theorem 5.8 (p. 41) now covers all of Sig. I checked the proof: area ≤ π/2 forces g = 0, n ≤ 4; with n = 4 only (0;2,2,2,3) (area π/3) and (0;2,2,2,4) (area π/2) remain; the triangle partners need (S, R) = (8, 5/6) or (9, 3/4), and SR < 9 rules them out. The abstract claim "the pair of least area in the whole class" is supported. |
| a3 | DONE (one leftover) | §4 intro (p. 33) now says "first differ in the third coefficient, at order t". The leftover is p. 36: "starting at the third order because the two orbifolds share c1, c2". This means the third coefficient, but it is the same ambiguity; say "at the third coefficient (order t)". |
| a4 | PARTIAL | The manuscript is correct (p. 34: "(a numerical, not a proved, statement)"). The supplement was not changed, although VERDICT-A says it was. S6 (p. 14) still says "Their systoles are 4b(ϑ) … (evaluated numerically from the exact formula), so the members are pairwise non-isometric", with no "numerical" qualifier. It also contradicts the manuscript on method. The manuscript says the systoles come from "a complete enumeration of short closed geodesics in floating point"; the supplement says "from the exact formula". If 4b(ϑ) is a proved formula, non-isometry is proved and the manuscript undersells it; if not, the supplement overstates it. |
| a5 | DONE | Laurens is cited "after his Lemma 3.2", and the sign-change argument is attributed to the proofs of his Lemma 3.2 and Corollary 3.3 (pp. 8, 25). Steinig is cited only through Laurens. |
| a6 | PARTIAL | The Fig. 3 caption now reads: "The open growth question lies between the constructed pairs, above the proved dashed lower bound, and the solid upper bound." In the figure, the open squares at s ≈ 60, 250 and 1000 lie below the dashed curve. So the region is not bounded below by "the constructed pairs" there. Suggested wording: "lies above the larger of the dashed lower bound and the constructed pairs, and below the solid upper bound." |
| a7 | NOT DONE (declined in VERDICT-A) | The figure is unchanged; the text gives radial values (p. 2: about 0.55 for m = 12 at that distance). Acceptable as a declined minor item. |
| a8 | NOT DONE (declined) | The Letac and Gloden solutions are still cited through Borwein–Ingalls [4], Borwein–Lisoněk–Percival [53] and Chen [33] (p. 31). Acceptable. |
| a9 | DONE | Remark B.5 uses τ, τ/2, τ/4. |
| a10 | DONE | p. 9: non-orientable orbifolds are not treated, with [2, (5.8)]. |
| a11 | DONE (as far as the PDFs show) | The note [37] is cited as a preprint (identifier is a placeholder). The note's own header cannot be checked from these inputs. |
| a12 | DONE | Lemma C.1 now indexes the columns of B and M by 1 ≤ j ≤ n and those of Y by 0 ≤ i ≤ n−1 (p. 53); "sep = +∞ if a is the only distinct order". |
| a13 | DONE | p. 14: "for K > 0 from Uçar's theorem, which covers every constant curvature". |
| a14 | DONE (small imprecision) | p. 20: "flat cone points contribute only to c2, which is then fixed by χ and Σ(m_i − 1/m_i)". In variable curvature c2 = χ/6 + Σ(m_i−1)²/(12m_i), which also depends on Σ(1 − 1/m_i), that is on the genus once χ is fixed. Within (iii) the genus is common, so this is harmless; adding "and the genus" would make it exact. |
| a15 | DONE | Row-wise bounds δ_{1,j} are in Lemma B.4. Remark B.5 still says "about" for the scan thresholds, which is acceptable for scan output; the three-time number gives "(to three digits)". |
| a16 | DONE | Corollary 6.5: "Let m be the integer orders of a sphere with n cone points". |
| a17 | DONE | Proof of Prop. 3.19 (pp. 30–31): area ≥ 2π(2g − 2 + n/2) bounds n + 4g ≤ A/π + 4, and the well-ordering argument is written out. |
| a18 | DONE | Supplement S7(ii) (p. 15) gives the Gauss's-lemma soundness argument, with p > max V, p ∤ 3(1 − e1R(V)) and a control run. The argument is correct. |
| a19 | DONE | Cor. 4.1(b) cites [38, Ch. 13]. Prop. 4.2(b) states the range t ≤ L′²/(2(1+L′)). |
| a20 | DONE | Proof of Lemma 5.4(ii) (p. 40; VERDICT-A calls it 5.3(ii), the old number) says that steps (a) and (b) of the proof of Theorem 5.5 do not use the lemma. |
| a21 | DONE | p. 38: "at a smaller order sum, though not at a smaller area", with O(5,5,5) and (0;2,2,2,10) of area 4π/5. |
| a22 | DONE (statement level) | Doyle–Rossetti is now "proved by a different method" (p. 6). Also present: DS Def. 3.1 (p. 9); Fursaev (3.26)–(3.28) and (2.7)–(2.8) (pp. 7, 12, 15); DGGW Ex. 5.6 and the t^0 coefficient (pp. 13–14); Uçar Cor. 4.21(iv) (p. 7); Garbin–Jorgenson "integrate over the half-line" (p. 36). These could not be checked against the sources here. |
| a23 | DONE | Schueth [24] is cited as (2.3), (2.4), (3.2), (3.4), (3.5) (pp. 16–17, 19). |
| a24 | DONE | p. 2: "at curvature −1, sinh(d/2) = sinh r sin(πj/m)". |
| a25 | DONE | Theorem C.2(b) proof: M(Ĩ) = M(I)(I + X) with ‖X‖∞ ≤ cond·ζ_n·η ≤ 1/2, then Neumann series and ‖M(Ĩ)^{−1}‖ ≤ 2 cond. The step is correct. |
| a26 | DONE | Theorem 3.11(iv): "m, m′ are formed from the orders in {2, …, M, X}"; X ∈ m′; the orders of m are at most M. |
| a27 | PARTIAL (new inconsistency) | Remark B.5 now explains μ0 = 12 as "the largest order of the competitor O(3,3,12), so that the a-priori class contains both". But the same remark takes ℓ0 = 2.2567, the certified systole bound of O(2,8,8). O(3,3,12) has systole 1.8626 (supplement S4, p. 12), so the a-priori class with this ℓ0 excludes the competitor. "Contains both" is therefore false. Fix: take ℓ0 ≤ 1.8626 (with D ≥ 4.897 still covering O(3,3,12), whose longest side is ≈ 2.16). For N = 3 the remark already says the numbers are the same for every ℓ0 ≥ 0.01. For N = 8, B0 at t ≤ 1.5e-2 with ℓ0 = 1.86 is about e^{−58}, so the numbers should survive, but this should be stated. Alternatively, drop "contains both" and say why μ0 = 12 was chosen. |
| a28 | DONE | Supplement S4 (ii) and Limitations: "a missing eigenvalue paired with a spurious one nearby would not [be detected] … completeness is supported, not proved". The two-window recomputation (p. 12) and the companion's ranges (below 1.6e4; 0.8 times the least sector maximum, pp. 10, 14) are stated. |
| a29 | NOT DONE (declined) | These items were declined as a group in VERDICT-A. Nothing in the PDFs shows any of them was done, and there was no claim that it was. |

## New items a strict referee would flag

1. **Placeholders in the submission**: the AI-use statement (p. 48), the Zenodo DOI (p. 48), the author contributions (p. 48), and the preprint identifiers of [3] and [37] (manuscript) and [5] (supplement). These must be filled before submission.
2. **"Closed form δ_thm"** on p. 46 and in the Table S4 caption contradicts the new sentence after Theorem C.4 (see A4).
3. **A-priori class in Remark B.5**: ℓ0 = 2.2567 excludes O(3,3,12) (systole 1.8626), contrary to "contains both" (see a27).
4. **Supplement S6 non-isometry**: the claim is stated flatly, and the systole method differs from the manuscript's description (see a4).
5. **Reference [6]** prints as "Boor, C." instead of "de Boor, C.".
6. **Figure 3 caption** wording: the open region is described wrongly where the Prouhet squares lie below the dashed bound (see a6).
7. **Placement**: the remark on cond and Table S4 sits between the statement and the proof of Theorem C.4.
8. **Introduction, p. 3**: "accurate to a few times 10^-8 or better" slightly overstates the tolerance Remark B.5 shows (1.3e-8).
9. **Problem 5 and the proof of Prop. 5.2**: the minor precision points listed under A5 (the range of p, q, r; the range of x).
10. **"Third order", p. 36**: the leftover wording listed under a3.

Nothing else new was found. The new mathematics was checked line by line and is correct: Proposition 2.14, Proposition 2.16(ii), Lemma B.3, Lemma B.4, Proposition 5.2, the extension of Theorem 5.8 and Theorem C.2(b). The numbers quoted in Remark B.5, Table S4, §4 and the supplement are consistent with one another, apart from the a27 systole point.

## Resolutions after this check (round 8)

- A4: the Table S4 captions (supplement, generated by `paper/jga/tools/make_tables.py`) and §6 now say "the threshold δ_thm, evaluated with the exact matrix norm"; the sentence on cond moved below the proof of Theorem C.4.
- A10: the de Boor entry prints as "de Boor, C." (`{de Boor}` in references.bib).
- a4: supplement S6 now says the systoles come from the enumeration of closed geodesics, equal 4b(ϑ) to 1e-30 (a numerical identification), and that non-isometry is a numerical statement.
- a6: the Figure 4 caption now says the open question lies between the upper bound and, at each s, the higher of the constructed and the proved lower bounds.
- a27: Remark B.5 no longer claims that the class contains both orbifolds; μ0 = 12 is the largest order of the competitor.
- a3: the leftover "third order" on p. 36 is now "the third coefficient".
- Not changed: "a few times 1e-8" (the blind check found admissible η up to about 6e-8 in its scan); the placeholders are the four permitted kinds.
