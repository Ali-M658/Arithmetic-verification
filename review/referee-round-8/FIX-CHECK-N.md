# FIX-CHECK-N (round 8): "Triples with Equal Sum and Equal Reciprocal Sum" (Integers layout, 24 pp.)

Inputs used: `fixcheck-N/scratch/input/note.pdf` and `VERDICT-N.md` only. Pages were rendered at 110 dpi and checked where the text extraction was ambiguous. Arithmetic checks were run in `scratch/py/` (sympy/fractions). In this layout Proposition 4.5 is **Proposition 4**, Theorem 3.4 is **Theorem 1**, Proposition 2.3 is **Proposition 2**, and Section 6.3 is **6.3**.

Summary: **N1–N8 are present and correct**. N3 is done as far as the text can go, but the underlying item is still open. There is **no mathematical error** in any new material, and every proof I re-derived holds. There are **a few new small issues**: one misplaced citation (LMFDB → [18]), one incommensurable comparison in 6.3, one possibly overstated comparison to [8], and some reference hygiene.

## FATAL / MAJOR

| id | verdict | notes |
|---|---|---|
| N1 | DONE | The abstract ("arbitrarily large classes"), Theorem C ("Arbitrarily large classes"), the Section 5 title and Theorem 4 all match the statement "size at least k". Nothing about the authors' own result still says "every size". The phrase survives only for Kelly (p. 4 l. 185, p. 16 §5): "Classes of every size for equal sums and equal products". A strict referee may ask whether Kelly's result is exact size or at least k, and whether Kelly really predates Schinzel's solution of D16 for triples. The wording should match what [20] proves. |
| N2 | DONE | Bremner–MacLeod is cited and compared on p. 5–6. I checked the substitution: with x = b+c etc., Σ a/(b+c) = (Λ−6)/2, so Λ = 2N+6. ✓. Odd N gives 4 \| Λ. ✓ MacLeod's R/r = (Λ−1)/4 also checks. ✓ The corrigendum [5] is cited (Table 2 only). "New" is softened to "we have not found in the literature" (p. 3), and the integer case is stated: only Λ = 10, orderings of (1:1:2), (1:2:2). I verified this: (Λ−5)²−m² = 16 has only Λ = 10 (Λ = 9 is excluded), and r + 1/r ∈ ℤ forces r = ±1. ✓ Two caveats. (a) BM 2014 predates Nguyen Xuan Tho 2021, yet the text calls BM's odd-N theorem "the case 4 \| Λ of the theorem of Nguyen Xuan Tho restricted to that subregion". That is mathematically right but reverses priority; "which the later theorem of NXT extends to the whole positive triangle" would be fairer. (b) The bib spells it "A. Macleod" in [4] and [5] but "MacLeod" in the text and in [22] (a different MacLeod, A. J.). The PDF alone cannot confirm "their elliptic curve is E_{2N+6}". |
| N3 | PARTIAL (text DONE; substance open) | Pages 5–6 say Choudhry [12] was not accessible and that the authors cannot say whether his family is or contains the dual or isosceles family. They credit the classical identity λ/x with λ = e₁eₙ/eₙ₋₁. I checked it: the sum is λe_{n−1}/e_n = e₁ and the reciprocal sum is e₁/λ. ✓ The text separates "individual coincidences in [11]" from "a parametric family in [12]". This is honest and adequate as text. The comparison is still unmade, though, and a referee who knows [12] could object that the dual family is in it. This must be settled before submission (SUBMISSION-CHECKLIST item). The general-n identity is called "classical" but is cited only for triples (BGN p. 117); either cite a source or drop "classical". |
| N4 | DONE (one caution) | The new paragraph is after Proposition D (p. 4). The dimension count is right: a degree-5 affine threefold in 𝔸⁴ gives B^{2+ε}. Caution: [8] (BHBS 2006) proves dimension growth only for degree ≥ 6 (as far as I recall), and the relevant hypersurface e₂e₃′ = e₂′e₃ has degree 5. "Compare [8] for such bounds" is not a claim that [8] applies, but a strict referee will want that said explicitly, or a citation of the later degree ≥ 4 result (Salberger). |
| N5 | DONE (one new soft spot) | The 6.3 changes are all present: the Poisson model is "a device for weighting the counts, not a model of them"; there are window variations (4.44/4.64/4.39); residue-class exponents 4.06/4.29/4.61/4.97 "because n(s) is a divisor sum"; and the remark that the cumulative and primitive counts are smoother. Tangency at s ≈ 2100 checks: e^{4.49/0.587} = 2099. ✓ The holdout appears as two percentages of the exact count 42 960, and the section ends "These describe a finite range; they are not predictions". "Separate them a little", "slightly less well", the quasi-likelihood figure and the spreads are all gone. **New soft spot (p. 20):** "differences smaller than the variation of the fits above" compares holdout percentage errors (0.25 % vs 2.33 %) with the spread of the fitted q. These quantities are incommensurable, and the power law's holdout error is ~9× the log-power law's. Suggest deleting the clause or saying "neither is decisive". Also, "about as well as a power law" (p. 20 l. 1) now has no quantitative support after the quasi-likelihood figure was removed. That is acceptable as descriptive wording, but "about as well" could become "comparably, by eye". |
| N6 | DONE | After Theorem B (p. 3): 3/(128π⁴) = 2.406·10⁻⁴ ✓, and the crossover log X > 437.8 ✓ (stated as 438). The upper bound O(X(log X)⁵) (Proposition 4) is followed by "probably of that order". That hedge agrees with p. 16 ("to be expected … we do not claim it"). Minor: in "it is proved for pairs only, since dual pairs can lie in one class (Theorem 3)", the parenthetical reads as if Theorem 3 proves that dual pairs share classes. Move "(Theorem 3)" next to "The second bound". |
| N7 | DONE | Proposition 4 with proof (pp. 15–16). I re-checked it: (1) the six cubics vanish at the five points; (2) no three of the points are collinear; (3) the independence computation (coefficients of a²b, ab², b²c, bc², a²c) is correct; (4) dimension 10−5 = 5; (5) Galois swaps E₄ and E₅, so ρ = 5; (6) H−E₁ has −K-degree 2, so it is a conic bundle; (7) 16 lines = 5 + 10 + the conic e₂ = 0 (e₂ does vanish at (1:ω:ω²)); (8) the non-real lines have only one real point; (9) positive triples avoid all of them; (10) the gcd/height comparison and the multiplicity of 12 hold; (11) partial summation gives (log X)⁵. This is consistent with the abstract, Theorem B's comment and §6.4. Minor: the multiplicity "at most twelve" is irrelevant to the upper bound (only "at least one point per pair" is used), so it could be dropped or marked as such. |
| N8 | DONE | The clause is added (p. 4): "the last hypothesis is absent from the first preprint version, whose corresponding statements Moreland and Zieve showed to be false, with the counterexample (3, 10, 24) [24]". The numbering is Proposition 2.7 / Theorem 2.8, as the verdict says. Minor: (a) "the first preprint version" is not in the bibliography; add its arXiv number. (b) "three distinct positive rationals u₁>u₂>u₃ with product N with u₁(u₂−u₃)³ ≠ …" has a double "with". (c) M and N are reused here for sum and product (N also names Bremner–MacLeod's and MacLeod's integers), which clashes with 𝒩(X). |

## MINOR

| id | verdict | notes |
|---|---|---|
| n1 | DONE | Remark 1 now has a complete proof (lines, charges, the three-line and two-line cases). I re-derived it, including the second case: (a+b)² = ab is impossible for a and b of the same sign. ✓ The proportional exclusion is illustrated. §6.4 says "By Remark 1, d = 1 occurs, for forms in two variables, only through scaling", which is consistent. |
| n2 | DONE | "(the pairs at S = 18 and S = 20 are smaller)" is present. I verified by enumeration: S = 20 is {(4,8,8),(5,5,10)}, and S = 26 is Chen's pair. The 408 chain is completed by (51,102,255), all at Λ = 68/5. ✓ |
| n3 | DONE | Browning–Elsholtz [7] and Elsholtz–Tao [17] are cited (p. 5). |
| n4 | DONE | Softened (p. 3), and the integer case is stated and correct (see N2). |
| n5 | DONE (no change needed) | The p. 2 formula renders as Σ(m_i²−1)/(12m_i), which gives (S+R−2)/12. ✓ |
| n6 | DONE | Schoen [29] is cited generally, with "we do not use this" and no locator. |
| n7 | DONE (one new citation error) | The integral model a = p²−6pq−3q², b = 16pq³ checks against E_Λ, and all ten a and b values in Table 1 check. 2^r = \|α\|·\|ᾱ\|/4 gives 0, 2, 2, 3, 3. ✓ The vanishing of the relevant Sha parts is stated. **New error (p. 17):** "the curve 90.c3 of the LMFDB [18, Theorem 5.8]". Reference [18] is the authors' companion manuscript, not the LMFDB, and the LMFDB has no bibliography entry. This should read "the curve 90.c3 of the LMFDB [new ref]; this is also [18, Theorem 5.8]". The second mention of [18, Theorem 5.8] in the same paragraph then duplicates it. The PDF cannot confirm the label 90.c3. |
| n8 | DONE | e₂, e₃ ≤ (S/3)³ ≤ 8·10⁹ < 2⁵³ (p. 18). Correct by AM–GM, and e₂ ≤ S²/3 ≤ (S/3)³ for S ≥ 9. |
| n9 | DONE | "Theorem B is needed only for the lower bound A(y) ≫ y, which the primitive isosceles pairs already give" (p. 4). The label is correct in this layout, and the logic is right for both directions. |
| n10 | DONE | Lemma 6 keeps a short 2 × 3 multiplicity argument, which is correct, and Proposition 4(iii) covers the count. |
| n11 | DONE | See N8. |
| n12 | DONE | Theorem 1(iv) proof: "distinct as t ≠ ±1 (t = 1 gives Λ = 9, and t = −1 gives Λ = 1)". ✓ Lemma 3 is "used only for its formulas". Optional: the six orderings of (1,r,r²) are distinct for the same reason (r = ±1 gives Λ ∈ {9,1}), which the proof leaves implicit. The final order list G, −G, 7G, 3G, 9G, 5G shows it anyway. |
| n13 | DONE | The check_note.py program is named. The μ = 1/Λ model is integral, with ord Δ = 6 and ord c₄ = 0, giving I₆. I checked c₄ ≠ 0 at Λ = 0, 1, 9 and ord Δ = 2, 3, 1. ✓ The Tate-normal-form isomorphism on p. 3 checks symbolically: Tate = E_Λ/(64Λ⁶). ✓ |
| n14 | DONE | Proposition 2 states the fibre types on the blown-up rational elliptic surface. |
| n15 | DONE | The four values 6721, 1449, 1329601, 8569 check, are non-squares, and no Λ is a square. ✓ Small inconsistency: the Table 2 caption still says rank and torsion are "from ellrank and elltors", while §5 now proves both. Suggest "(proved in Section 5)". |
| n16 | DONE | Smoothness is proved via the genus-one component. The argument is correct: a cubic with a genus-one component is that component and is smooth. |
| n17 | DONE | "By Lemma 3 and Proposition 3" appears in Theorem 1(iii) and (iv). |
| n18 | DONE | Lemma 3 says "six orderings of the triple x and the six orderings of its dual". "Asymptotically by a factor 18c_iso log X ≈ 1.9 log X" ✓. q = 4.49 is used consistently in the text and Figure 1(b). There is one percentage base (N(6000)−N(4800) = 42 960). Poisson is described as a device. |
| n19 | DONE | The companion-colour remark is gone. Nit: the text says "dark blue-green" but the caption says "(dark)". |
| n20 | DONE | p. 21: "such a search ranges over surfaces in a threefold, not over lines in the plane, and we know no practical test". |
| n21 | DONE | Theorem 1(i): "… Z/2×Z/6; the cases (ii) and (iii) below exclude each other". The abstract says "the dual pairs and their multiples". |
| n22 | n/a | Declined items; nothing to check. |

## Numerical spot checks (all pass)

- **Table 2 classes.** All Λ values are as listed: 68/5 (136 and 408), 1849/120, 230/21. Size 4 = 3 × (size 3) plus (65,70,273). ✓
- **The four C_{169/16} pairs.** Sums are 845, 1183, 2145 and 3003, all with Λ = 169/16 (r = −4). ✓
- **Theorem 4.** (4:9:18) and 3P lie on C_{155/12}, and ι(P) = (9:4:2). ✓
- **Class counts.** 96 981 + 1627 + 122 + 11 + 1 = 98 742 = 𝒩_cl(4800). The pair count 96 981 + 3·1627 + 6·122 + 10·11 + 15 = 102 719 = 𝒩(4800). ✓
- **Primitive pairs.** 7626 + 4 + 38 624 = 46 254, with 16.5 % dual and 83.5 % of the third kind. ✓
- **Table 3 local exponents.** I recomputed them at 600, 1000, 2000, 4000 and 6000 (6000: 1.58454 → 1.585 in Table 3 and 1.58 in the text). 𝒩/X² is 0.0094 → 0.0040. ✓
- **Isosceles constant.** c_iso = 0.105346, and c_iso·4800 = 505.7. ✓
- **Proposition 5 identity.** It equals −δ times the cleared-denominator relation. ✓
- **Theorem 3 constants.** c_A = 3/(32π⁴) and the final 3/(128π⁴) re-derived. ✓
- **Proposition 2 example.** (1:4:4) ↦ (−6, 45) on E_{27/2}. ✓

## New items a strict referee would flag

1. **LMFDB citation (p. 17).** "[18, Theorem 5.8]" is attached to "the LMFDB" (see n7). This is a misattribution, and the LMFDB is missing from the references.
2. **Holdout comparison (p. 20).** "Differences smaller than the variation of the fits above" compares percentages with exponent spreads (see N5).
3. **Dimension growth and [8] (p. 4).** [8] does not cover degree 5; say so or cite the degree ≥ 4 result (see N4).
4. **Priority wording for Bremner–MacLeod 2014 vs Nguyen Xuan Tho 2021 (p. 5–6), and "Macleod"/"MacLeod" in the bib.**
5. **"Classes of every size" attributed to Kelly (pp. 4, 16).** Check against [20] and match the "at least k" wording, and confirm the priority relative to Schinzel.
6. **Unread and uncited sources.** Choudhry [12] is still unread (N3). The general-n "classical identity" has no source. The "first preprint version" of Sadek–El-Sissi is uncited.
7. **Theorem B comment (p. 3).** The parenthetical "(Theorem 3)" is misplaced (see N6).
8. **Table 2 caption.** It still credits ellrank/elltors, while §5 now proves rank and torsion (see n15).
9. **Placeholders remain.** These are the Zenodo DOI, author contributions, the AI-use statement and the [18] preprint identifier. They are not new, but they block submission.

## Resolutions after this check (round 8)

- LMFDB: the label 90.c3 and its attribution removed from §5 (the rank-0 statement rests on the descent of Table 1).
- §6.3: the clause comparing percentages with the variation of the fits removed.
- Reference to Browning–Heath-Brown–Salberger removed (their bounds need degree ≥ 6); the sentence now says only that S^{2+ε} is the size expected for such points and that a power saving needs input special to this threefold.
- Bremner–Macleod: spelled as in their paper; their odd-N theorem is now described as the case 4 | Λ, on that subregion, of the later theorem of Nguyen Xuan Tho.
- N3 (Choudhry): unchanged; recorded as an action for the authors in the submission checklist.
- Not changed: Kelly (1989) is credited as in its abstract and precedes Schinzel (1996); the general n-tuple identity is proved in its sentence; Table 2's caption still names the PARI routines that produced the column, which §5 now also derives.
