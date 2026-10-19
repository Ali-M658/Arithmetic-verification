<!-- Round 8 N-e referee report: returned text saved verbatim; the reviewer could not write files -->

The tool refused to write the report file, so the full report is below. In short: no fatal errors, and every result and number I could recheck is correct. I recommend minor revision, with two must-fix items. The first is that the O(X(log X)⁵) bound stated in the abstract is proved only in sketch. The second is that the Sadek–El-Sissi citation does not match the source I could reach.

# Referee report (rigour and citations): "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

Reviewed from `scratch/input/note.pdf` (22 pages). Page numbers below are the printed page numbers. As instructed, I treated the author-contribution and AI-use statements, the Zenodo DOIs and the preprint identifiers as known. Before reporting anything typographical, I looked at the rendered pages at 110 and 220 dpi.

## Summary

The note studies unordered triples of positive integers with equal sum S and equal reciprocal sum R. It first shows that coincidences force R < 1 (Lemma 1). It then places each class of such triples on one curve C_Λ of the Beauville Γ1(6) pencil, where Λ = SR, and shows that reciprocation is translation by a 2-torsion point (Proposition 3). From these it derives:

- the torsion of C_Λ(Q) and which positive points are torsion (Theorem 1);
- which torsion translations preserve positivity (Lemma 4);
- two lower bounds: N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X from the isosceles family (Theorem 2), and N(X) ≥ (3/(128π⁴) + o(1)) X (log X)² from the dual family (Theorem 3);
- classes of every size, by Schinzel's argument on C_{155/12} (Theorem 4);
- the upper bound n(S) ≪ S^{2+ε} (Proposition 4);
- an O(X (log X)⁵) bound for the dual-family contribution, via Browning–Sofos.

It also gives an exhaustive enumeration to S = 6000 and states one open question (Question E).

## Significance

The arithmetic is modest. The torsion classification is classical, and the authors say so. Theorem 4 is Schinzel's argument transplanted, and the authors claim no novelty for it. Proposition 4 gains only S^{1−ε} over the trivial bound. The genuinely new content is:

- the positivity analysis of torsion (Theorem 1(iv) and Lemma 4);
- the two counting lower bounds with explicit constants;
- the del Pezzo/conic-bundle view of the dual family;
- an exact, well-documented enumeration.

The text is careful about what is and is not claimed. This is a reasonable Integers note.

What is good: the proofs I checked are correct and complete apart from the gaps listed below. Every number I could recompute agrees with the text to the last digit. Citations are, with one exception (M2), accurate at statement and page level wherever I could reach the source.

## Correctness and what I recomputed

All scripts are in `scratch/code/`, and the downloaded sources are in `scratch/src/`.

**Symbolic checks (sympy):**
- Proposition 2: the identity (x+y)(y+z)(z+x) = e1e2 − e3 holds.
- The map (s, η) sends C_Λ into E_Λ.
- The inverse map as printed (with η((x+y)/z − Λ + 1)/(4Λ(Λ−1))) lands on C_Λ. Both compositions are the identity modulo the curve equations.
- Δ = 2¹²Λ²(Λ−1)³(Λ−9), and c4 ≠ 0 at Λ = 0, 1, 9 (c4 = 144, 256, 2304).
- (1:4:4) maps to (−6, 45) at Λ = 27/2.
- The tangent at O is x + y = (Λ−1)z, and restricting the curve to it gives Λ(Λ−1)z³.
- The Tate-normal-form substitution with c = −1/Λ (p. 3) transforms the Tate equation exactly into E_Λ. The point (0,0) of the Tate model corresponds to (0:1:0), as stated.
- A Gröbner basis confirms that the plane cubic C_Λ is singular exactly for Λ ∈ {0, 1, 9} (see m1).
- The six cubic forms of p. 14 vanish at the five stated points and span a space of dimension exactly 5.

**Hand-checked proof steps:**
- Base-point group law (p. 7).
- Lemma 1, including both discriminants on p. 6.
- Proposition 1.
- Lemma 2.
- Proposition 3, including the root-product and collinearity steps.
- Lemma 3 (automorphism argument and fixed points).
- Theorem 1(i)–(iv), including every order assignment.
- Lemma 4.
- Corollary 1 and Lemma 6.
- Theorem 2: the area log 2/6, the Möbius sum restricted to 3 ∤ d, and c_iso = 0.105345…
- Theorem 3: the box inequality W ≤ y; the error O(M³√y log y) = O(y^{7/8} log y); c_A = 3/(32π⁴); and the final constant 3/(128π⁴).
- Proposition 4: the identity (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′ and the divisor argument.
- The R/r identity R/r = (Λ − 1)/4 (p. 5).

**Group-law checks (exact rational arithmetic on E_Λ):**
- On C_{155/12}, 3P = (162833463 : 723926268 : 287876366), and P + T2 = (9 : 4 : 2).
- 2G = (0:1:−1) + T2 for G = (1:r:r²) with r = 2, −4 and 3/2.
- The orderings of a geometric progression have order 4 exactly when the middle term is the last coordinate, and order 12 otherwise.
- On C_{27/2}, (u:v:v) and (v:u:v) have order 6 and (v:v:u) has order 2.
- The pairs at S = 845, 1183, 2145 and 3003 all lie on C_{169/16}, and their differences are torsion of orders 4 and 12 only.

**PARI/GP 2.17.2 (cypari2 in a local venv):**
- ellrank gives coinciding bounds 0, 2, 2, 3, 3 for Λ = 27/2, 155/12, 68/5, 1849/120, 230/21. It also gives rank 1 for 169/16.
- elltors gives Z/2×Z/6 for 27/2, and Z/12 for 169/16 and 49/4.
- The conductors are 90, 6250530, 82110, 1715185290 and 41388270, and the root numbers are +1, +1, +1, −1, −1. All agree with p. 15.

**Independent exact enumeration** (my own C program; it groups by double, then splits exactly with 128-bit cross-multiplication):
- Every row of Table 2 up to X = 3000 matches: N, N_cl, primitive classes, largest size, and the local exponents (2.524, 2.069, 2.007, 1.954, 1.993, 1.868, 1.790, 1.713, 1.663).
- From the published rows: 1.624 (4000), 1.603 needs N(2400), and 1.585 (6000) is consistent.
- The first classes of sizes 3, 4 and 5 are at S = 136, 408 and 1849.
- 507 of the 582 sums 19 ≤ S ≤ 600 carry a primitive class.
- There are 1330 non-dual primitive pairs with S ≤ 600, and 669 with S ≤ 400.
- The dual share is 32.9% for S ≤ 200.
- Up to S = 3000, the only non-dual primitive pairs on curves with r < 0 are those at 845, 1183 and 2145. That is consistent with "four … at 845, 1183, 2145, 3003".
- All Table 1 classes have a common S and Λ and gcd 1.
- The size-4 class is 3 × (the size-3 class) ∪ {(65, 70, 273)}.
- The size-histogram totals on p. 16 reproduce N(4800) = 102719 and N_cl(4800) = 98742 exactly.
- 7626/46254 = 16.5% and 38624/46254 = 83.5%.

**Other counts:**
- Admissible triples, by closed form: 748,123,249 (S ≤ 3000), 3,067,197,199 (S ≤ 4800) and 5,992,496,499 (S ≤ 6000), as stated.
- Isosceles family: 506 pairs D_{u,v} with S ≤ 4800 (c_iso · 4800 = 505.66). The copies number 2917 = 0.6077X at X = 4800.
- The count of copies minus c_iso X log X, divided by X, is −0.2860, −0.2862, −0.2863, −0.2863 and −0.2863 at X = 10⁴, 10⁵, 10⁶, 10⁷ and 4·10⁷. That confirms "−0.286X to three digits".
- 189 lines ax + by + cz = 0 with coprime |a|, |b|, |c| ≤ 7 meet the open positive triangle up to permutation and sign.
- N(6000) − N(4800) = 42960, and N/X² = 0.0094 at 400 and 0.0040 at 6000.

**Not recomputed:**
- The fits in Section 6.3; I enumerated only to 3000.
- The 2-isogeny image sizes on p. 15. PARI's ranks agree with them, and the formula 2^r = |α(Γ)||ᾱ(Γ̄)|/4 reproduces the stated ranks.
- The first class of size 6 being first (I confirmed it is a class).
- The "27 of them lie in classes of size ≥ 3".

**Citations checked against the source text:**
- Browning–Sofos [5, Thm 1.1]: hypotheses X(Q) ≠ ∅ and a conic over Q; standard height on P⁴; exponent ρ − 1.
- Top–Yui [26, Table 2]: X0(6), Γ0(6), (x+y)(y+z)(z+x) + txyz. The fibres I6, I3, I2, I1 at t = ∞, 0, 1, −8 match Λ = ∞, 1, 0, 9 under t = 1 − Λ.
- Mazur [18]: Ch. III §5, Theorem (5.1) on p. 156, with the remark on p. 156 that Kubert [16, Ch. IV] tabulates the parametrisations.
- Schinzel [23]: primitive-set definition p. 587; argument p. 588; the curve x1 + x2 + x3 = x1x2x3 = 6.
- Ulas [27]: Thm 3.1 (n ≥ 4) and Cor 3.4 (i = −1, 1, 2).
- Dryden–Gordon–Greenwald–Webb [11, (5.7)]: χ(O)/6 + Σ(m_i² − 1)/(12m_i) (arXiv version).
- Nguyen Xuan Tho [20, Thm 1.1]: no positive solution when 4 | n. His curve is exactly E_n, and his introduction confirms the families 4m², 4m² + 4 of [4].
- Chen Shuwen [7, App. A.5.1]: the listed solutions and chains, and Choudhry's 3-parameter family.
- Zhang [30]: quotes BGN, "it seems likely that for n ≥ 16 …".
- MacLeod [17], Moreland–Zieve [19], van Doorn [28], Youmbai–Zargar–Voznyy [29]: abstracts consistent with the use made of them.
- Crossref metadata (volume, issue, pages, year) for [2], [3], [4], [5], [6], [8], [10], [11], [12], [14], [15], [16], [24], [26], [27], [29], [31]: all correct.

**Could not access:**
- Bremner–Guy–Nowakowski [3]: AMS sits behind a challenge page.
- Beauville [1].
- The published Osaka version of Sadek–El-Sissi [22] (Project Euclid blocked); see M2.
- Schoen [24].
- The erratum [12].
- Kelly [15].
- Bremner–Nguyen Xuan Tho [4] theorem numbers.

I did not reach these, so the page-level quotations of [3] (pp. 117, 118, 119, 120, 130) and the item numbers in [1], [4] and [24] remain unconfirmed by me (m9).

## FATAL

None. I found no false statement among the main results, and no error in any proof a main result depends on.

## MAJOR

**M1 (p. 14, also abstract p. 1 and p. 19). The O(X(log X)⁵) bound for the dual family is advertised in the abstract but proved only in sketch.** The paragraph after Theorem 3 makes several assertions that each need a line of proof or a precise reference.

- (a) "Span the five-dimensional space of plane cubics through them (we checked this symbolically)." This is true; I confirmed rank 5. The proof is one line: one linear relation, Σ e2·x_i = Σ e1·(x_j x_k), and five independent conditions imposed by five points with no three collinear. Give it instead of "checked symbolically".
- (b) The identification of D with the anticanonical embedding needs to be explicit. Y lies in the hyperplane {Σ first three = Σ last three} of P⁵. Dropping one coordinate gives P⁴ coordinates whose primitive integer vector is the reduced pair. The standard height in [5] is therefore comparable to max entry ≤ S_D. As written, "each primitive dual pair comes from a point of height at most its sum" depends on an unstated choice of coordinates.
- (c) "The image avoids the sixteen lines of Y, which carry no positive points" is asserted without proof. The 16 lines are:
  - the 5 exceptional curves;
  - the 10 strict transforms of lines through two of the points: z = 0 and its permutations; the two conjugate lines through a coordinate point and (1:ω:ω²) or (1:ω²:ω), whose only real point is the coordinate point; and x + y + z = 0;
  - the conic through all five points, which is e2 = 0.

  Each visibly misses the positive orthant. I checked this, but the paper must say it.
- (d) Theorem 1.1 of [5] assumes X(Q) ≠ ∅ and a conic defined over Q. State that both hold. The first is trivial; the second holds via the pencil of lines through (1:0:0).
- (e) State the finite-to-one passage from points of Y to unordered primitive dual pairs (at most 12 orderings per pair), and the Picard-rank computation (Galois-invariant part spanned by H, E1, E2, E3, E4 + E5).

None of this is in doubt, but an abstract-level result needs a stated lemma with proof. Fix: promote the paragraph to a Proposition with items (a)–(e) as its proof.

**M2 (p. 4 and p. 10). Statement-level citation of Sadek–El-Sissi [22] does not match the source I could reach, and omits a known correction.**

- In arXiv:1303.6705v2, whose journal_ref is the cited Osaka paper:
  - The isosceles result is Proposition 2.5, and that matches the note.
  - The positive-rank result is Proposition 2.6, and the torsion trichotomy is Theorem 2.7. The note cites "Proposition 2.7 and Theorem 2.8".
  - The hypothesis is three distinct positive integers d1 > d2 > d3 with sum M and product N. The note says "three distinct positive rationals u1 > u2 > u3".
- Moreland–Zieve [19], cited in the same paragraph, state (p. 3) that [22, Prop. 2.6, Thm. 2.7] as first posted are false. Their counterexample is (a, b, c) = (3, 10, 24), and the proof of [22, Thm. 3.1] is affected. The extra hypothesis d1(d2 − d3)³ ≠ d3(d1 − d2)³, which the note does quote, was added in v2 precisely to exclude this: 24·7³ = 3·14³.

Fix:
- Check the numbering and hypotheses against the published Osaka version. If the published text says integers, say integers.
- Add a half-sentence noting the correction in [19], so that readers of [22, v1] are not misled.
- Make the corresponding numbering change in the remark after Theorem 1 (p. 10).

## MINOR

- **m1 (pp. 6–7, Proposition 2).** "For every other Λ the curve C_Λ is smooth of genus one" is not proved. The discriminant computed is that of E_Λ, and "as rational maps between smooth projective curves they extend to isomorphisms" presupposes that C_Λ is smooth. The flex and chord–tangent arguments on p. 7, and Lemmas 2–4, also need it. The statement is true: a Gröbner-basis check gives singular members exactly at Λ ∈ {0, 1, 9} in the chart z = 1, and none at infinity. One sentence fixes it. Either compute the gradient, or argue as follows: a reducible plane cubic has only rational components, so C_Λ is irreducible; an irreducible plane cubic birational to a genus-one curve has geometric genus equal to arithmetic genus 1, hence is smooth.
- **m2 (p. 7, Proof of Proposition 2).** "The maps and both compositions are verified symbolically, as is the discriminant." Either give the two or three displayed identities, or point to the deposit script by name. I confirmed all of them.
- **m3 (p. 10, Theorem 1(iii) proof).** "(0:1:−1) − G = G + T2 by Proposition 3" also uses Lemma 3, for the action of the transposition of x and z. Cite both.
- **m4 (p. 11, Remark 1).** It is labelled a sketch but asserts a theorem ("Then x′ is a permutation of x"). I reconstructed the pole-matching argument and believe it. However, "every other family by forms of one degree has degree at least 2" is not a precise statement. Either give the complete argument, which is short (group entries by the pole of their linear form; compare residues and the S-identity form by form), or state it explicitly as a heuristic. It is used only in the heuristic of Section 6.4.
- **m5 (p. 15).** "{(2,8,8), (3,3,12)} and its multiples are the only coincidences with Λ = 27/2" is a theorem-level statement. Its proof is a PARI rank computation, a 2-isogeny descent summarised only by the sizes of the image sets, and a companion paper [13, Thm 5.8] whose identifier is a placeholder. For a self-contained proof, give the descent for C_{27/2} explicitly (conductor 90, so it is short), or cite the curve's entry in Cremona's tables or the LMFDB by label. I confirmed rank 0 and torsion Z/2 × Z/6.
- **m6 (p. 3).** "The description of the positive torsion points is new." Bremner–Guy–Nowakowski already record permutations as torsion translates of ±P ([3, §4], as the note says on p. 8). Unless the authors have checked the later literature on this pencil, "we have not found it in the literature" is safer.
- **m7 (p. 5, Chen [7]).** Besides S = 18, the isosceles pair {(4,8,8), (5,5,10)} at S = 20 is also smaller than Chen's "smallest" S = 26 pair; say "the pairs at S = 18 and 20 are smaller". Chen's chain (A.652), {45,165,198}, {48,120,240}, {65,70,273}, is not a complete class: Table 1 shows the class at S = 408 also contains (51, 102, 255). That is worth a clause. I checked that Chen's chain (A.653) at S = 573 is a complete class of size 3.
- **m8 (p. 18, Section 6.3).** The fit statistics (quasi-likelihood difference 1.4, Pearson dispersion 6.8, "0.2 and 1.9 standard deviations", the block-resampled spreads) cannot be checked from the paper. They need the per-sum counts n(s) for s ≤ 6000.
  - Name the deposit file that contains n(s) and the script that reproduces each number in this subsection.
  - "Separate them a little" is an interpretation of one out-of-sample cumulative count; state the numbers without the gloss. The text elsewhere already concedes that a finite range bounds the exponent from neither side.
- **m9 (pp. 3, 5, 7, 8, 20).** Page-level quotations from [3] (pp. 117, 118, 119, 120, 130), "Théorème and Tableau, p. 658" of [1], "Theorems 8, 9, and 14" of [4] and "Proposition 7.1" of [24] could not be verified by this referee (sources behind access controls). Please re-check them against the printed versions.
  - For [24], confirm that the cited proposition covers the self-fibre product E ×_{P¹} E, whose singular fibres coincide. Schoen's general setting assumes the singular fibres are in general position, and the self-product case is treated separately in that paper.
  - For [12], say in a few words what the erratum corrects and whether (5.7) is affected. In the arXiv version of [11], (5.7) is exactly as quoted.
- **m10 (p. 19, Figure 1 caption and p. 18 last line).** "The colours of O(2,8,8) and O(3,3,12) in the companion manuscript" is meaningless to a reader of this note; delete it.
- **m11 (references).**
  - [25] should say "2nd ed." (Springer, Cham, 2015).
  - Integers style omits issue numbers in parentheses after volumes, e.g. "Math. Comp. 61 (1993), 117–130". Harmonise if the editor requires it.
  - Check whether [17], [19], [28] and [30] have since been published.
  - Give the arXiv identifier of [22] next to the journal reference if the numbering differs (M2).

## Presentation

- **P1 (p. 3).** The sentence from "With a point of order 6" to "Mazur records [18, p. 156]" runs to nine lines and carries four separate claims. Split it.
- **P2 (p. 4).** The displayed chain after Question E is set inline and breaks across lines. Display it.
- **P3 (pp. 20–21).** "Statements and Declarations" is not part of the Integers template. Keep the data statement; the rest is for the editor.
- **P4.** Theorems A–C and Proposition D/Question E duplicate numbered results; this is acceptable. Make sure "Theorem 1" and "Theorem A" use identical hypotheses. They currently do.
- **P5.** Typography on the rendered pages is clean. I found no sign, sub/superscript or figure errors. Figure 1(b) matches the text: N(4800)/4800 ≈ 21.4 and copies ≈ 0.61 at 4800. In Figure 1(a), the dark points sit near the edge midpoints, (1,4,4)/9, and the orange points near the vertices, (1,1,4)/6, as expected.

## Recommendation

**Minor revision.** Confidence: high (about 0.85) that every main result is correct as stated. I re-derived the proofs of Lemma 1, Propositions 1–4, Lemmas 2–6, Theorems 1–4 and Corollary 1, and independently reproduced every enumeration figure up to S = 3000 and every curve invariant.

The two MAJOR items are must-fix but short:
- M1 is a proof that exists only as a sketch, for a result stated in the abstract.
- M2 is a statement-level citation mismatch, plus a missing pointer to a published correction.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | A Proposition (dual pairs ↔ points of the quartic del Pezzo Y) with the proof items (a)–(e): independence and relation of the six cubics; the P⁴ coordinates and height comparison; the explicit list of 16 lines and why none meets the positive locus; the hypotheses of [5, Thm 1.1]; the finite-to-one correspondence. |
| M2 | Numbering and hypotheses (integers vs rationals) checked against the published [22], and a clause citing Moreland–Zieve's correction; same fix in the remark after Theorem 1. |
| m1 | One sentence proving C_Λ smooth for Λ ∉ {0, 1, 9}. |
| m2 | Display the verified identities, or name the deposit script. |
| m3 | Cite Lemma 3 alongside Proposition 3. |
| m4 | Full short proof, or relabel Remark 1 as heuristic and drop the imprecise final sentence. |
| m5 | Explicit descent for C_{27/2}, or a Cremona/LMFDB label. |
| m6 | Soften "new". |
| m7 | Mention S = 20; note that Chen's S = 408 chain is an incomplete class. |
| m8 | Name the n(s) data file and the scripts; remove the interpretive gloss. |
| m9 | Re-verify the page and item numbers in [1], [3], [4], [24]; one phrase on what [12] corrects. |
| m10 | Delete the companion-colour remark. |
| m11 | Bibliographic tidying as listed. |
| P1–P3 | Editorial. |

All work files are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/N-e-integers-proof-reader/scratch/:
- code/ — scripts (enum.c, prop2.py, ec.py, ranks.py, iso.py, misc.py)
- src/ — fetched sources
- out600.txt, out3000.txt — enumeration output
- nondual3000.txt — non-dual primitive pairs to S = 3000
- pages/ — rendered page images
- venv/ — cypari2 virtual environment
