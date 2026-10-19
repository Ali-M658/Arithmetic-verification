<!-- N-e referee (rigour and citations), round 7: returned text saved verbatim; the reviewer could not write files -->

# Referee report (rigour and citations): "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

The tool refused to write `REPORT.md`, so the full report is below. My working code is in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/N-e-proof-reader/scratch/code/`.

**Recommendation: minor revision.** I found no mathematical errors. Every proof checks out, and every number I could recompute matches exactly. There are two major issues, both cheap to fix:
- **M1:** the Mazur result cited in Theorem 1(i) is the wrong statement and does not support the step.
- **M2:** the code repository is not public.

The 19 pages were rendered with pdftoppm and read as images. The marked placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifier of [9]) are treated as known.

## Summary

The note studies unordered triples of positive integers that have the same sum S and the same reciprocal sum R. It works through the cubic pencil C_Λ: e1e2 = Λe3. Its results are:

- **Theorem 1 (A):** the torsion of C_Λ(Q) is Z/6, Z/12 or Z/2×Z/6, with exact criteria for each. For Λ > 9, the positive torsion points are the triples with two equal entries and the geometric progressions.
- **Theorems 2–3 (B):** N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X, and N(X) ≥ (3/(128π⁴) + o(1)) X(log X)².
- **Theorem 4 (C):** classes of every size exist, by Schinzel's method on C_{155/12}.
- **Proposition 4 (D):** n(S) ≪ S^{2+ε}.
- **Enumeration:** exact counts to S = 6000, with growth fits and a heuristic Section 6.4.

## Significance

This is a modest, honest contribution of the right size for Integers. The geometry of Sections 2–3 is mostly classical, and the note credits Bremner–Guy–Nowakowski [3] and Beauville [1] for it. The new parts are:
- the complete torsion classification for rational Λ, including the positive torsion points;
- the two counting lower bounds and the upper bound;
- a carefully cross-checked enumeration.

Attribution is careful: Section 5 says "we claim no novelty for the method", and Section 6.4 is labelled heuristic. Question E is natural, and the authors say plainly that the data cannot decide it. The literature section is unusually precise about what each cited paper actually states.

## Correctness: what I recomputed or verified

I worked independently in Python, sympy, and PARI/GP 2.17.2 (via cypari2, in a virtual environment inside scratch).

### Proofs checked line by line

All of the following are correct:

- **Lemma 1:** all cases, and both discriminants, 3(c′+3)(1−c′) and (c′+4)(24−22c′−c′²)/(6−c′).
- **Proposition 1.**
- **Proposition 2**, checked symbolically:
  - the identity (x+y)(y+z)(z+x) = e1e2 − e3;
  - the forward map C_Λ → E_Λ and the inverse composition;
  - Δ = 2¹²Λ²(Λ−1)³(Λ−9), and c4 ≠ 0 at Λ = 0, 1, 9;
  - the tangent x+y = (Λ−1)z at O, the five line sections, and that the base-point group is Z/6.
- **Lemma 2** and **Proposition 3:** the root product p0p1, and that O, R, ι(P) are collinear.
- **Corollary 1**, and the permutation analysis on p. 8:
  - π(O) for each transposition;
  - cyclic permutations are translations by a point of order 3.
- **Theorem 1(i)–(iv)**, including the bookkeeping 3G, 5G, 7G, 9G.
- **Remark 1:** I completed the sketch, including the second mismatched case, and it holds.
- **Lemma 3.**
- **Theorem 2:**
  - |Ω| = (log 2)/6;
  - the mod-3 Möbius bookkeeping, Σ_{3∤d} μ(d)/d² = (6/π²)(9/8);
  - c_iso = 0.105345….
- **Lemma 4.**
- **Theorem 3:**
  - W(u, v) ≤ (2βV)(2αV) = y;
  - the box count and the error term O(M³√y log y);
  - c_A = 3/(32π⁴), and the final constant 3/(128π⁴).
- **Proposition 4:** the identity (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′, checked in sympy.
- **Theorem 4.**

### Numbers reproduced exactly

- **Points:**
  - (1:4:4) ↦ (−6, 45) on E_{27/2};
  - 3P = (162833463 : 723926268 : 287876366) and P + T2 = (9:4:2) on C_{155/12}, checked in PARI on E_Λ.
- **Orders of torsion points:**
  - On C_{49/4}, the six orderings of (1, 2, 4) have orders 12, 12, 12, 4, 4, 12. Order 4 occurs exactly when the middle term is last.
  - On C_{27/2}, (1:4:4) and (4:1:4) have order 6, and (4:4:1) and (1:1:4) have order 2.
- **Table 1:**
  - Ranks, torsion and root numbers for all five curves (the ellrank bounds coincide), plus C_{49/4} with Z/12.
  - Each listed class is complete at its sum, checked by scanning every least entry at S = 18, 136, 408, 1849, 4600.
- **Table 2, all rows with X ≤ 1000:** reproduced from my own exhaustive enumeration (27,568,860 admissible triples).
- **Other counts:**
  - 1753 primitive pairs with S ≤ 600, of which 423 are dual;
  - 32.9% dual for S ≤ 200;
  - 507 of the 582 sums carry a primitive class;
  - the two classes at S = 36;
  - 669 non-dual primitive pairs with S ≤ 400;
  - first classes of sizes 2, 3, 4 at S = 18, 136, 408;
  - the size-4 class equals 3 × (the size-3 class) ∪ {(65, 70, 273)}.
- **Non-dual pairs:** for all 1330 non-dual primitive pairs with S ≤ 600, both P′ − P and P′ + P have infinite order. For the 669 with S ≤ 400, no relation P′ = ±mP + T or P = ±mP′ + T holds with m ∈ {2, 3}.
- **Triple totals:** 3,067,197,199 (S ≤ 4800) and 5,992,496,499 (S ≤ 6000), confirmed by a closed form.
- **Class sizes:** 96981 + 1627 + 122 + 11 + 1 = 98742 = N_cl(4800), and the corresponding pair total is 102719 = N(4800).
- **Isosceles family:**
  - 506 pairs D_{u,v} with S ≤ 4800, against c_iso · 4800 = 505.66;
  - 27 of them lie in classes of size at least 3;
  - the count of copies is 0.6077X at X = 4800;
  - c_iso X log X − (count) = 0.2860X, 0.2862X, 0.2863X at X = 10⁴, 10⁵, 10⁶.
- **Constants and exponents:**
  - 128π⁴c_iso/3 = 437.8 and 18c_iso = 1.896;
  - local exponent at 6000 is 1.5846;
  - N/X² = 0.00935 at 400 and 0.00405 at 6000.

### Not verified

- The Selmer orders. Their arithmetic is consistent: 2^{r+2} = |Sel_φ||Sel_φ̂| gives ranks 0, 2, 3, 3, 2, matching ellrank.
- The 189-line search.
- Counts above S = 1000, other than the totals listed above.
- The statistical fits.

### Citations checked at statement level against fetched sources

| Ref | Source checked | Finding |
|---|---|---|
| [8] Dryden et al. | arXiv 0805.3148 | (5.7) is χ/6 + Σ(m_i² − 1)/(12m_i), which gives (S+R−2)/12. Correct. |
| [17] Schinzel | Serdica PDF | D16; "primitive set" defined on p. 587; rescaling by the common denominator d to sum 6d on p. 588. Correct. |
| [14] Nguyen Xuan Tho | journal PDF | Theorem 1.1 (4 \| n ⇒ no positive solution). Hilbert symbols on v² = u(u² + (n²−6n−3)u + 16n), which is E_n. His description of [4] matches the note. Correct. |
| [20] Ulas | arXiv 1305.6241 | Content is correct, but it is Corollary 3.4 (with Theorem 3.1, n ≥ 4). See m2. |
| [2] Bremner–Guy | open PDF | Studies (x+y+z)³/xyz. Correct. |
| [10] Kelly | zbMATH review | r disjoint 3-part partitions with equal products, so classes of every size before Schinzel. Priority correct. |
| [5], [13], [21] | abstracts | Described correctly. |
| [11] MacLeod | — | I verified R/r = 2abc/∏(a+b−c) = (Λ−1)/4. Correct. |
| [12] Mazur | Numdam | Wrong statement cited (M1). |
| [16] Sadek–El-Sissi | arXiv 1303.6705v2, zbMATH | Numbering and hypotheses differ (m1). |
| All entries | Crossref | Volumes, issues and pages agree, including [4] 14(5) 1229–1246, [6], [7] article 5444. |

Not retrievable headlessly:
- **[3]**: AMS bot wall. The quotations on pp. 6–7 are therefore unverified by me, but they are consistent with the mathematics: for integer n, Theorem 1 gives Z/2×Z/6 only at n = 10. Tho reproduces BGN's model and its positivity criterion.
- **[1], [18] Proposition 7.1, [4] Theorems 8, 9, 14**: paywalled. My computed fibre types (I6, I3, I2, I1 at Λ = ∞, 1, 0, 9) are consistent with the attribution to Beauville.

## FATAL

None.

## MAJOR

**M1 (p. 8, Theorem 1(i)): the Mazur citation is the wrong statement and does not support the step.**
- In [12], Chapter III §5 on p. 156, Theorem (5.1) is the list of 15 torsion groups. Corollary (5.2) says only that a rational point has order at most 10, or exactly 12.
- Theorem 1(i) needs "the only groups containing Z/6 are Z/6, Z/12 and Z/2×Z/6". Corollary (5.2) does not give this, because it does not exclude Z/2×Z/12, in which every element has order at most 12.
- The other use on p. 8 (excluding differences of order at most 12) is covered by Corollary (5.2) and can stay.
- **Fix:** in Theorem 1(i), cite [12, Chapter III, Theorem (5.1), p. 156].

**M2 (p. 18): the code and data are not available.**
- `https://github.com/pa1aash/equal-sum-reciprocal-triples` returns HTTP 404, and the Zenodo DOI is a placeholder.
- Several claims rest only on that code:
  - the exact-arithmetic Selmer orders;
  - "no class of size 7 up to 6000";
  - Table 2 above X = 1000;
  - the 189-line search;
  - the 84% / 16.5% shares;
  - all of the fits.
- **Fix:** make the repository public or archived before acceptance.

## MINOR

**m1 (pp. 4, 9): the theorem numbers and hypotheses attributed to [16] do not match the source.**
- In arXiv v2:
  - positive rank is Proposition 2.6;
  - the torsion trichotomy is Theorem 2.7;
  - Proposition 2.5 (isosceles points of order 6) matches.
- The note cites "Proposition 2.7 and Theorem 2.8".
- The note says "three distinct positive rationals". Sadek–El-Sissi assume integers d1 > d2 > d3 with integer M and N.
- The rational version, with the same condition a1(a2−a3)³ ≠ a3(a1−a2)³, appears in Kelly [10] according to the zbMATH review.
- **Fix:** check the numbers against the Osaka version, say "integers", and optionally credit Kelly.

**m2 (p. 4): [20] needs a statement locator.** Cite [20, Corollary 3.4].

**m3 (p. 13): [19] (Silverman–Tate) has no Selmer groups.** Its Chapter III formula is 2^r = |α(Γ)||ᾱ(Γ̄)|/4. Add the clause "the images of explicit points fill the Selmer groups, so image = Selmer", and cite the section that contains the formula.

**m4 (p. 8): the transposition argument only rules out α = 1.** Add: "π² = id ⇒ α² = 1, and α is defined over Q, so α = ±1." This covers j = 0 and j = 1728.

**m5 (p. 5, Proposition 1): "pairwise non-proportional" is ambiguous for unordered triples.** (1,4,4) and (4,1,4) are non-proportional as vectors but are the same triple. Say "no x_i is proportional to a permutation of x_j".

**m6 (pp. 9–10): Remark 1 is labelled a sketch, but p. 16 relies on it** ("Remark 1 rules out d = 1"). The full proof is about eight lines:
- match poles and charges line by line;
- the mixed case {aℓ, bℓ, m} against {cℓ, m′m, m″m} fails by (a+b)² = ab, and also by m′+m″ = 1 = 1/m′ + 1/m″.

Give the proof, or make it a lemma.

**m7 (p. 17): "A positive answer to Question E therefore implies…" is an unproved implication.**
- The X^{m/d} count is heuristic.
- A surface with a single positive real point need not contribute any lattice points; what is needed is a Zariski-dense set or a non-empty open positive region.
- **Fix:** write "would, heuristically, require", and state the open-set condition.

**m8 (p. 3 vs p. 15): the local exponent has two definitions.** Page 3 calls it "d log N / d log X". Table 2 defines it as log₂(N(X)/N(X/2)). Use one definition.

**m9: an erratum to [8] exists** (Michigan Math. J. 66 (2017), 221–222). Confirm it does not touch (5.7).

**m10 (p. 8): Theorem 1(i) is worded confusingly.** "is the group of base points Z/6, or Z/12, or Z/2×Z/6" reads as if all three were the group of base points. Reword to "is Z/6 (the base points), Z/12, or Z/2×Z/6".

**m11 (pp. 6–7): recheck the verbatim quotations and page numbers from [3]** against the published version. I could not access it.

## Presentation

**P1 (p. 17, Figure 1).**
- The figure complies with the house rules: it contains only panel letters, axis titles and tick labels, and the caption is two sentences.
- No caption or text identifies which colour marks (1,4,4) and which marks (1,1,4); p. 16 says only "two colours".
- The half-coloured disc at S = 18 is explained only in Section 6.3.
- From the geometry, dark is the (1,4,4) type and orange is the (1,1,4) type.
- **Fix:** add "dark: (1,4,4); light: (1,1,4)" to caption sentence (a).

**P2 (p. 18): the "Statements and Declarations" block is Springer-style, not Integers style.** Fold it into a short unnumbered section.

**P3 (p. 8): the computational sentence ("Among the 1753 primitive pairs … Mazur") interrupts the proof structure.** Move it to Section 6.1, next to the check on the 669 pairs.

**P4 (p. 15): Table 2 column header.** Change "largest class" to "largest class size".

**P5: cross-references and numbering are all correct.**
- Theorems A–C, Proposition D and Question E map correctly to Theorems 1–4, Proposition 4 and Section 6.4.
- Lemmas 1–4, Corollary 1, Remark 1, equations (1)–(2), Tables 1–2 and Figure 1 are all consistent.
- The references are alphabetical.

## Recommendation

**Minor revision.**
- **Confidence in the mathematics: high.** Every proof was checked, and every reachable number was reproduced.
- **Confidence in the citation checks: moderate for [1], [3], [4] and [18]**, which I could not retrieve.

M1 is major in kind but needs one corrected reference. M2 is a condition for acceptance.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Cite Mazur Theorem (5.1) in Theorem 1(i). |
| M2 | Publish the repository or Zenodo deposit. |
| m1 | Correct the [16] numbers, say "integers", optionally credit Kelly. |
| m2 | Cite [20, Corollary 3.4]. |
| m3 | Add the image = Selmer clause and a section reference in [19]. |
| m4 | Add the α² = 1, Q-rationality sentence. |
| m5 | Define non-proportionality for unordered triples. |
| m6 | Replace the sketch with the full proof. |
| m7 | Weaken "implies" and add the open-set condition. |
| m8 | Use one definition of the local exponent. |
| m9 | Check the erratum to [8]. |
| m10 | Reword Theorem 1(i). |
| m11 | Recheck the quotations from [3]. |
| P1–P4 | Colour key in the caption; front-matter style; move the p. 8 computation; Table 2 header. |
