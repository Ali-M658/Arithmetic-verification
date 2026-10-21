<!-- Round 9 N-a editor report: returned text saved verbatim; the reviewer could not write files -->

I could not save the report to `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/N-a-editor-elementary-number-theory/REPORT.md`: the write was refused because subagents may not write report files. The full report is below. My scripts and outputs are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/N-a-editor-elementary-number-theory/scratch/` (`code/`, `lit/`, `pages/`, `venv/`).

# Editor's report: "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

Handling editor: elementary and combinatorial number theory. I read every page from the rendered PDF images (pdftoppm, 110 dpi) and from the extracted text. Page numbers below are the PDF page numbers, which are also the printed ones.

## Summary

The note studies unordered triples of positive integers that share their sum S = e1 and their reciprocal sum R = e2/e3 with another triple. Lemma 1 shows such triples are admissible (R < 1), so they correspond to pairs of hyperbolic triangle orbifolds that the first two heat invariants do not distinguish. Proposition 1 places a class on the cubic C_Λ: (x+y+z)(xy+yz+zx) = Λxyz with Λ = SR, which is the curve of Bremner, Guy and Nowakowski taken over rational Λ. The main contents are:

- **Proposition 2.** The model E_Λ and the identification with the Γ1(6) pencil.
- **Proposition 3.** Reciprocation acts as translation by a point of order 2.
- **Theorem 1.** The torsion is Z/6, Z/12 or Z/2×Z/6. For Λ > 9 the positive torsion points are exactly the isosceles triples and the geometric progressions.
- **Lemma 4.** Which torsion translations preserve positivity.
- **Lower bounds.** N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X from the isosceles family (Theorem 2), and N(X) ≫ X(log X)² from the dual family (Theorem 3).
- **Proposition 4.** An upper bound O(X(log X)^5) for the contribution of the dual family, via a quartic del Pezzo surface and Browning–Sofos.
- **Theorem 4.** Arbitrarily large classes, by Schinzel's method.
- **Proposition 5.** The upper bound n(S) ≪ S^{2+ε}.
- **Computation.** An exhaustive enumeration up to S = 6000, descriptive fits, and Question E: is N(X) = X^{1+o(1)}?

**What is good.**
- The note is careful and honest. It credits Bremner–Guy–Nowakowski, Beauville, Kubert, Mazur and Schinzel where credit is due, and it labels its heuristics as heuristics.
- Every statement I checked is correct (see below).
- The computations are exact, reproducible and cross-checked.
- The positivity analysis is new as far as I can tell, small but clean: the egg argument for rational Λ, positive torsion, and the translations that preserve positivity. Geometric progressions as positive torsion points of order 4 or 12 are a nice contrast with the equal-product problem.
- The exhaustive data set is a real service.

**Limitations.** The note does not answer its own central question. The growth exponent of N(X) is only confined to [1, 3]. The lower bounds come from explicit families. The upper bound (Proposition 5) beats the trivial bound by only S^{1−ε}. Theorem 4 is immediate once one has a positive point of infinite order.

## Significance and fit

The fit for Integers is good. The topic is classical Diophantine material in the Guy D16 tradition (equal sums and equal products; Schinzel; Kelly; Zhang–Cai; Sadek–El-Sissi), and the elliptic-curve input is at the level this journal routinely publishes.

The significance is modest but real:
- the first counting results for this coincidence problem;
- the positivity and torsion description over all rational Λ;
- a reliable data set;
- a clearly posed open question.

None of the theorems is deep. Theorem 1(i)–(iii) is the Kubert/Mazur classification in plane coordinates. Theorems 2 and 3 are lattice-point counts on explicit families. Theorem 4 is Schinzel's argument. The O(X(log X)^5) bound is a black-box application of Browning–Sofos.

Whether the paper is publishable therefore depends on two things: the novelty of the families against the one prior parametric work the authors admit they have not read (M1), and an honest placement of the counting results (M2). I see no correctness obstacle.

## Correctness: what I recomputed

All of the following were run in scratch/code: sympy, a C enumerator written by me independently, and PARI/GP 2.17.2 via cypari2 in a scratch venv.

1. **Lemma 1** (p. 6). I checked the case analysis by hand, including both discriminants, 3(c′+3)(1−c′) and (c′+4)(24−22c′−c′²)/(6−c′). Correct.
2. **Proposition 2** (p. 7).
   - Both maps are correct: forward image on E_Λ, inverse image on C_Λ, and round trips at (1:4:4), (2:8:8) and (4:9:18).
   - (1:4:4) at Λ = 27/2 maps to (−6, 45), as stated.
   - The discriminant is 2^{12}Λ²(Λ−1)³(Λ−9), as stated.
   - The fibre types follow from c4 = 16(A²−3B) ≠ 0 at Λ = 0, 1, 9, giving I2, I3, I1, and I6 at ∞.
   - The isomorphism to Tate normal form on p. 3 (c = −1/Λ) holds; the two equations differ by the factor c⁶/64.
3. **Proposition 3** and the tangent and flex computations (pp. 7–9). Checked by hand. Correct.
4. **Theorem 1(iv)** (p. 10), checked by exact group law on E_Λ:
   - On C_{49/4}, (1,2,4), (2,1,4), (2,4,1) and (4,2,1) have order 12, and (1,4,2) and (4,1,2) have order 4 (middle term last).
   - On C_{27/2}, (4,4,1) and (1,1,4) have order 2, and the other orderings have order 6.
   - For integer Λ > 9, Z/2×Z/6 forces (n−5)²−16 to be a square, so n = 10, and Z/12 is impossible. This confirms the claim on p. 3.
5. **Lemma 4 example** (p. 11). On C_{169/16}, (165,240,440) and (182,455,208) differ by a point of order 4. PARI gives C_{169/16} rank 1 and torsion Z/12; C_{49/4} has torsion Z/12.
6. **Theorem 2** (pp. 12–13).
   - The area |Ω| = (log 2)/6 and c_iso = 3 log 2/(2π²) = 0.10534 are correct.
   - There are 506 pairs D_{u,v} with S ≤ 4800.
   - (copies − c_iso X log X)/X = −0.2852, −0.2860, −0.2862, −0.2863, −0.2863, −0.2863 at X = 4800, 10⁴, 10⁵, 10⁶, 10⁷ and 4×10⁷. The copy count at 4800 is 0.6077X. All as stated.
7. **Theorem 3** (p. 14). I rederived c_A = 3/(32π⁴) and the final constant 3/(128π⁴). The box inequality W ≤ (2βV)(2αV) = y holds because β/α ≤ α. The error terms are o(y). The crossover log X > 438 is correct (437.8).
8. **Proposition 4** (p. 15).
   - The five base points, the linear independence of five of the six cubic forms, ρ = 5, the 16 lines, and the positivity of D(x) off the lines are all correct.
   - The Browning–Sofos hypotheses (arXiv 1609.09057v4, Thm 1.1: X(Q) ≠ ∅ and a conic over Q) are met.
9. **Proposition 5** (p. 19). I verified the identity (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′ algebraically.
10. **Theorem 4** (p. 16). Λ(4,9,18) = 155/12. 3P = (162833463 : 723926268 : 287876366) and P + T2 = (9:4:2), exactly as printed.
11. **Table 1 and Section 5** (p. 17). PARI ellrank gives coinciding bounds for all five curves, with the stated ranks 0, 2, 2, 3, 3.
    - Conductors: 90, 6250530, 82110, 1715185290 and 41388270.
    - Root numbers: +1, +1, +1, −1, −1.
    - Torsion: Z/2×Z/6 for 27/2 and Z/6 for the other four.
    - The a and b columns match a = p²−6pq−3q² and b = 16pq³.
    - The non-square checks 6721, 1449, 1329601 and 8569 are correct.
    - Consistency 2^r = |α|·|ᾱ|/4 holds row by row.
12. **Table 2** (p. 18). Every member has the stated sum and Λ. My enumeration confirms that the classes at S = 136 and 408 are complete and are as printed.
13. **Table 3** (p. 19). My independent exact enumeration reproduces every entry for X = 18, 100, 200, …, 600, 1000, 2000 and 3000: pairs, classes, primitive classes and largest size. For example N(3000) = 48574, N_cl = 46755, primitive = 22657.
    - I also reproduced the triple counts 3 067 197 199 (S ≤ 4800) and 5 992 496 499 (S ≤ 6000), and that 507 of the sums 19 ≤ S ≤ 600 carry a primitive class (p. 18).
    - The primitive-pair statistics are reproduced: 32.9% of primitive pairs with S ≤ 200 are dual (82/249), and there are 1330 non-dual primitive pairs with S ≤ 600.
    - The class-size counts on p. 18 are internally consistent with N(4800) and N_cl(4800).
14. **Section 6.4** (pp. 21–22). The count of 189 lines (coprime |a|, |b|, |c| ≤ 7, meeting the positive triangle, up to permutation and sign) is correct.
15. **Consistency with the companion manuscript.** It records 38 collision-free sums in 18 ≤ S ≤ 4800, the last being 557. My enumeration finds exactly 38 up to S = 1000, the last being 557, so the two agree.

I found no mathematical error.

## FATAL

None.

## MAJOR

**M1. Choudhry's three-parameter solution was not consulted, and it bears on novelty and on Question E** (p. 5, lines on [10, App. A.5.1] and [11]; p. 6 novelty paragraph; p. 21 Heuristic).

The authors write that Choudhry, "Equal sums of like powers, both positive and negative", RMJM 41 (2011) 737–763, "was not accessible to us". I confirmed in Chen's survey (arXiv:2506.11429, App. A.5.1) that Choudhry gave a three-parameter solution of exactly this system (k = −1, 1, three terms). Semantic Scholar lists the article as open access (bronze) on Project Euclid. It is freely readable in a browser; only headless access is blocked.

This is not a bibliographic nicety:
1. If Choudhry's family is the dual family, the "classical identity" on p. 5 has a citable source, and the novelty claim must be adjusted.
2. If his family is new relative to the dual and isosceles families, the counting picture changes.
3. If it is parametrised by quadratic forms in three homogeneous variables and has positive points on an open set, the authors' own heuristic (p. 21: "would give about X^{3/2}") predicts N(X) ≫ X^{3/2}. That would answer Question E negatively and change the paper's main message.

The note cannot go to acceptance while the one known parametric prior work on its exact equation is unread. Separately, the "classical identity" λ/x with λ = e1·en/e_{n−1} (p. 5) is called classical without a citation; give one.

*Resolves:* obtain and read [11]. State precisely whether Choudhry's family is, contains, or is contained in the dual family or the isosceles family. Give its degree and number of variables, and the resulting contribution to N(X) (heuristic or proved). Revise Section 1.4, the novelty paragraph on p. 6 and Section 6.4 accordingly. Cite a source for the λ/x identity.

**M2. The upper-bound side is close to trivial and is not placed in the dimension-growth literature** (p. 4, paragraph after Proposition D; pp. 19–20, Proposition 5; p. 21).

Proposition 5 gains S^{1−ε} over the trivial S³ and stays at the scale of the number of triples. The text asserts that "S^{2+ε} is the size one expects for such points in general" and that "a power saving would need input special to this threefold", but cites nothing for either claim.

These are statements about counting integer points on hypersurfaces, and there is a substantial literature: Pila; Heath-Brown (Annals 2002); Browning–Heath-Brown–Salberger (Duke 2006); Salberger's proof of dimension growth; Castryck–Cluckers–Dittmann–Nguyen (2020). The pairs at sum S include the trivial linear components x′ = πx, which by themselves give about S² points, so general dimension-growth bounds cannot by themselves give o(S²). Points off those planes are exactly where determinant-method results are designed to save.

The authors should either:
- show what the existing uniform results give for the non-trivial points, even a bound n(S) ≪ S^{2−δ}, or N(X) ≪ X^{3−δ} by slicing; or
- explain precisely why they do not apply.

Without this, the exponent window [1, 3] in Theorem B, Proposition D and Section 6.4 looks wider than the state of the art may allow, and the paper's counting contribution is hard to assess.

*Resolves:* a short paragraph with references, and either an improved upper bound or a precise statement of the obstruction. Rephrase "the size one expects" with a citation.

## MINOR

- **m1** (p. 17). "this is also [17, Theorem 5.8], proved there by a 2-isogeny descent by hand". In the disclosed manuscript [17], Theorem 5.8 is the minimal-degeneracy statement. The isolation of the pair on C_{27/2} (rank 0, torsion Z/2×Z/6) is Theorem 5.9, with the descent in its Appendix E. Correct the citation.
- **m2** (p. 2). "the smallest is {(2,8,8),(3,3,12)}" is asserted without proof or reference. Cite [17, Thm 5.8], or give the two-line argument; in the note it currently rests only on the enumeration in Table 3.
- **m3** (p. 11, Lemma 4). "the base points, together with all twelve torsion points when the torsion is Z/12 with … r < 0" reads as if twelve points were added to the six. Write: "the base points; and, when the torsion is Z/12 with r < 0, all twelve torsion points".
- **m4** (p. 13). "has area ½ log 4": write log 2. In the Möbius step, say explicitly that coprime pairs are equidistributed among the eight non-zero classes mod 3; that is what produces #U/8.
- **m5** (pp. 4, 16). Guy's problem D16 is invoked twice, but *Unsolved Problems in Number Theory* is not in the references. Add it.
- **m6** (p. 15, Prop. 4(i)). Browning–Sofos require Y(Q) ≠ ∅. Name the rational point, for example D(1:1:2) or any positive point, instead of only asserting "a rational point".
- **m7** (p. 12). Remark 1 has a full proof and is used in Section 6.4. Make it a Proposition. Likewise, move "the constant is not optimised" out of the name of Theorem 3 (p. 14) and into the text.
- **m8** (p. 3). The isomorphism to Tate normal form is buried in a long sentence. Display it. (I verified it: the equations agree up to the factor c⁶/64.)
- **m9** (p. 17, Table 1 caption). "the Selmer groups containing the images" followed by text saying the images fill them is confusing. State in the caption that the listed sets are both the Selmer groups and the images.
- **m10** (p. 20, §6.3). The fitted exponents (q = 4.49, 4.56, 3.53, …; β = 0.587) come with no uncertainty, and "Poisson maximum likelihood" is applied to deterministic counts. Either give ranges, as you partly do across windows, or reduce this to one or two sentences. Their only role is to show that the data cannot locate the exponent.
- **m11** (p. 5). Chen's chain (A.653), {44,253,276}, {45,198,330}, {66,78,429} at S = 573, is not mentioned. I checked that it is a complete class. Mention it alongside (A.652) for completeness.
- **m12** (p. 7, proof of Prop. 2). "The maps and both compositions are verified symbolically … by the program check_note.py". Either print the two composition identities, which are short, or say explicitly that this step is computer-verified.

## Presentation

- **P1** (pp. 4–6). Section 1.4 is a single paragraph of about 60 lines, mixing equal products, PTE, unit fractions, the representation problem for e1e2/e3 = n, and triangle geometry. Split it into topical paragraphs.
- **P2.** Each result carries two labels (Theorem A = Theorem 1, B = Theorems 2 and 3, C = 4, D = Proposition 5). Together with the many internal cross-references, this makes the note hard to navigate. Consider stating the results once, in the Introduction, and proving them later under the same numbers.
- **P3.** Program names and provenance (p. 7, and §6.1 on pp. 17–18) belong in the data statement. Proofs should not depend on file names.
- **P4** (p. 1). The abstract is overloaded with numerics (1.58, 6000, "near 500") and internal structure. Two or three sentences on the results would serve readers better.
- **P5** (p. 1). The running head "#A1 INTEGERS 26 (2026)", the empty "DOI:", and "Received/Revised/Accepted" are journal fields. Leave them blank for the production office.
- **P6.** The figures are fine. In Fig. 1(a) the egg and the two orbits are legible and the colours are distinguishable; in Fig. 1(b) the log-log axes and legend match the caption. No typographical, sign or figure errors were found on the rendered pages.
- **Placeholders** (author contributions, AI-use statement, Zenodo DOI, preprint identifier of [17]) are treated as known and not counted against the paper.

## Overlap with the disclosed related manuscripts

- **"How much of a hyperbolic orbifold does heat hear?" ([17]).** The overlap is limited and properly disclosed in both directions.
  - [17] proves the minimality of the pair (2,8,8)/(3,3,12) (Thm 5.8) and the isolation on C_{27/2}, with a hand descent (Thm 5.9, App. E). The note reproves the latter by machine as a corollary of Theorem 1 and Table 1, and cites [17] (with the wrong theorem number; see m1).
  - The enumeration up to S = 4800 is the same computation in both papers; [17] says so explicitly.
  - [17] quotes the note's Theorems B and C without relying on them.
  - The heat-invariant motivation on p. 2 is one paragraph and is not duplicated.
  - Numbers stated in both papers agree (I checked the collision-free sums and the 83 triads with S ≤ 18).
  - None of the note's main results (positivity and torsion, the counting bounds, the del Pezzo upper bound, large classes, Proposition 5, Question E) appears in [17].
- **"Finitely many eigenvalues determine the signature".** The only shared content is (2,8,8)/(3,3,12) used as a numerical test case. There is no mathematical overlap.
- **Salami slicing.** I see none. The arithmetic of the coincidences is a coherent, separable topic.

## Editorial decision and recommendation

- **Editorial decision:** send to review. The submission is in scope, correct as far as I could check (extensively), and of a standard Integers publishes. It does not merit a desk rejection.
- **Recommendation:** major revision, confidence moderate-high (about 0.75).
  - The label reflects M1. Until Choudhry [11] is read, neither the novelty of the families nor the plausibility of Question E can be judged, and the answer could change the paper's conclusion.
  - If [11] turns out to be the dual family, or another family of degree at least 3, then M1 reduces to a citation fix. With M2 addressed by a referenced paragraph and the minor items fixed, I would expect to accept after a minor round.
  - If [11] gives a quadratic family in three variables, Question E as posed has to go and Section 6.4 must be rewritten. That would be a substantial revision, though not necessarily a rejection.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Read Choudhry 2011 (open on Project Euclid). State the relation of his three-parameter family to the dual and isosceles families, with its degree and number of variables and its contribution to N(X). Update pp. 5–6 and §6.4. Cite a source for the λ/x identity. |
| M2 | Add references to dimension-growth and determinant-method results. Either derive a power saving for non-trivial pairs, or explain precisely why the known uniform bounds do not apply. Replace "the size one expects" with a cited statement. |
| m1 | Change [17, Theorem 5.8] to [17, Theorem 5.9] (and App. E) on p. 17. |
| m2 | Cite [17, Thm 5.8], or prove the minimality of the S = 18 pair on p. 2. |
| m3 | Reword the last sentence of Lemma 4. |
| m4 | Write log 2; state the equidistribution of coprime pairs mod 3. |
| m5 | Add Guy, UPNT (D16). |
| m6 | Name a rational point of Y. |
| m7 | Make Remark 1 a Proposition; rename Theorem 3. |
| m8 | Display the Tate-normal-form isomorphism. |
| m9 | Fix the Table 1 caption. |
| m10 | Give uncertainty ranges for the fits, or condense §6.3. |
| m11 | Mention Chen's chain at S = 573. |
| m12 | Print the composition identities, or flag the step as computer-verified. |
| P1–P5 | Split §1.4; use single numbering for results; move provenance to the data statement; shorten the abstract; leave the journal fields blank. |
