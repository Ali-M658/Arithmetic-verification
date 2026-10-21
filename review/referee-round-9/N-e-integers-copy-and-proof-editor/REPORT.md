<!-- Round 9 N-e referee report: returned text saved verbatim; the reviewer could not write files -->

# Referee report for *Integers*: "Triples with Equal Sum and Equal Reciprocal Sum"

**I could not write the report to `REPORT.md`.** The tool refused the write, so the full report is below.

Referee brief: rigour, statement-level citations, cross-references, tables, displayed formulae, house style.
Material read: `scratch/input/note.pdf` (24 pp.). I read every page as a rendered image at 100 dpi, and p. 7 also at 200 dpi. I did not assess the author contributions, the AI-use statement, the Zenodo DOI or the preprint identifier, because these are marked placeholders.

## Summary

The note studies unordered pairs of triples of positive integers with equal sum S and equal reciprocal sum R. These are exactly the pairs of hyperbolic triangle orbifolds that the first two heat invariants do not separate. Following Bremner–Guy–Nowakowski (BGN), a class of such triples is a set of positive rational points on one fibre C_Λ, with Λ = SR, of the pencil (x+y+z)(xy+yz+zx) = Λxyz.

The paper proves the following:
- Reciprocation is translation by a 2-torsion point.
- The torsion of C_Λ(Q) is Z/6, Z/12 or Z/2×Z/6 (Theorem 1). For Λ > 9 the positive torsion points are exactly the isosceles triples and the geometric progressions, and their orders are determined.
- Torsion translations preserve positivity exactly when the translating point is not positive (Lemma 4).
- Lower bounds: N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X, and N(X) ≫ X (log X)².
- Classes of every size exist, by Schinzel's method.
- The dual pairs and their copies contribute O(X (log X)⁵), via Browning–Sofos.
- n(S) ≪ S^{2+ε}.

An exhaustive enumeration up to S = 6000 is reported, and the limiting growth exponent is left as Question E.

## Significance

This is a modest but clean contribution. The positivity analysis of the torsion (Theorem 1(iv), Lemma 4) and the counting results are new as far as I can tell. The rest of the geometry is honestly credited to BGN, Beauville and Kubert. The novelty of the isosceles and dual parametric families, however, cannot currently be judged against Choudhry [11] (see M1). The enumeration is careful and, as reported below, exactly reproducible. The scope fits *Integers*.

## Correctness and what I recomputed

I re-derived every proof step by hand and found no mathematical error. Everything numerical that I could rerun reproduces exactly. Using a private venv with sympy 1.14 and PARI/GP 2.17.2 (via cypari2), plus my own C enumerator:

**Proposition 2 and the introduction**
- Both rational maps C_Λ ↔ E_Λ (read as η·((x+y)/z − Λ + 1)/(4Λ(Λ−1)), as typeset on p. 7) land on the target curve, and both compositions are the identity modulo the curve equations (Gröbner reduction, symbolic in Λ).
- Δ = 2¹²Λ²(Λ−1)³(Λ−9).
- c₄ = 16(Λ−3)(Λ³−9Λ²+3Λ−3), which is nonzero at Λ = 0, 1, 9. The fibre types I₂, I₃, I₁ and I₆ (at ∞) follow.
- The tangent at O reduces the cubic to Λ(Λ−1)z³.
- The Tate-normal-form isomorphism with c = −1/Λ is exact, and (0,0) pulls back to (4Λ, 4Λ(1−Λ)).
- The example (1:4:4) ↦ (−6, 45) at Λ = 27/2 is correct.

**Lemma 1.** The case list and both discriminants, 3(c′+3)(1−c′) and (c′+4)(24−22c′−c′²)/(6−c′), are correct.

**Proposition 3, Lemma 3 and Theorem 1.** I checked numerically on E_Λ for Λ = 155/12 and Λ = 49/4:
- Transposition x↔y acts as −P; y↔z as (1:0:−1) − P; x↔z as (0:1:−1) − P.
- The cycle (x:y:z) ↦ (z:x:y) is P + (0:1:−1).
- ι(P) = P + T₂.
- On C_{49/4}, the six orderings of (1,2,4) have orders 12, 12, 12, 4, 4, 12, with order 4 exactly when the middle term is last.
- On C_{27/2}, (1:4:4) and (4:1:4) have order 6 and (4:4:1) has order 2.

These all match Theorem 1(iv). Λ(1:r:r²) = (r+1+1/r)² is correct, as is the integer-Λ claim (only Λ = 10, via (Λ−5)² − m² = 16).

**Section 5 and Tables 1–2**
- Λ(4,9,18) = 155/12.
- 3P = (162833463 : 723926268 : 287876366), exactly as printed.
- ellrank gives coinciding bounds 0, 2, 2, 3, 3 for Λ = 27/2, 155/12, 68/5, 1849/120, 230/21.
- elltors gives Z/2×Z/6 for 27/2 and Z/6 for the others.
- Root numbers are +1, +1, +1, −1, −1, and conductors are 90, 6250530, 82110, 1715185290, 41388270.
- The a, b columns of Table 1 are correct, the α(T) = b and b̄ = a² − 4b classes appear in the stated lists, and 2^r = |α||ᾱ|/4 gives the stated ranks.
- C_{169/16} has rank 1 and torsion Z/12.
- Every member of every Table 2 class has the stated S and Λ, and every class is primitive.
- The four C_{169/16} pairs (S = 845, 1183, 2145, 3003) lie on C_{169/16}. For each, P′ − P has order 4 or 12 for some orderings and infinite order for the others.

**Theorems 2–3**
- I checked the area computation (|Ω| = (1/6) log 2), the Möbius/residue-class bookkeeping, c_iso = 0.105346, the constant c_A = 3/(32π⁴), the final 3/(128π⁴) ≈ 2.41·10⁻⁴, and the crossover log X > 438.
- There are 506 pairs D_{u,v} with S ≤ 4800, and 27 of them lie in classes of size ≥ 3.
- The count of copies at X = 4800 is 0.6077X.
- (count − c_iso X log X)/X = −0.28597, −0.28621, −0.28628 at X = 10⁴, 10⁵, 10⁶.

**Proposition 4.** The six cubic forms have rank 5 and vanish at the five points. The line, conic and Picard-rank bookkeeping is correct.

**Proposition 5.** The identity (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′ holds.

**Section 6.** I ran my own exhaustive enumeration for S ≤ 6000 (exact 128-bit verification of every hash group, no mismatches). It reproduces:
- every entry of Table 3, including the primitive-class column, the largest size and the local exponents;
- 3 067 197 199 admissible triples for S ≤ 4800 and 5 992 496 499 for S ≤ 6000;
- the class-size histogram 96 981 / 1627 / 122 / 11 / 1, with no class of size 7;
- first classes of sizes 2–6 at S = 18, 136, 408, 1849, 4600;
- 507 of the 582 sums in [19, 600] carry a primitive class;
- 46 254 primitive pairs, of which 7626 (16.49%) are dual, against 32.93% for S ≤ 200;
- 1330 non-dual primitive pairs with S ≤ 600 and 669 with S ≤ 400;
- N(6000) − N(4800) = 42 960;
- N/X² = 0.00935 and 0.00405.

The Poisson fits also reproduce: q = 4.489 (all pairs), 3.532 (primitive); 4.437, 4.642, 4.39 on the three sub-windows; 4.061, 4.289, 4.609, 4.966 on the four residue subsets; β = 0.587. The predicted excesses on (4800, 6000] are +0.25% and +2.32%. The count of 189 lines in Section 6.4 is also correct.

**Not recomputed:** the Section 6.4 line-pair search result, the m ∈ {2, 3} relation test, the dual/non-dual sub-fits (2.56, 3.33, 3.73, 4.80), and the cumulative fits.

**Citations checked against the sources:**
- Schinzel [27]: the primitive-set definition on p. 587 and the argument on p. 588.
- Browning–Sofos [8, Thm 1.1]: hypotheses X(Q) ≠ ∅ and a conic over Q; bounds c₁B(log B)^{ρ−1} ≤ N(B) ≤ c₂B(log B)^{ρ−1}, with N(B) counting points off the 16 lines.
- Dryden–Gordon–Greenwald–Webb (DGGW) [14, (5.7)], arXiv numbering.
- Nguyen Xuan Tho [24, Thm 1.1], including the curve v² = u(u² + (n²−6n−3)u + 16n), the Hilbert-symbol method, and its statement of [6].
- Bremner–Macleod [4, Lemma 2.1, §4, Thm 5.1, Cor 5.2] and the corrigendum [5].
- Ulas [31, Thm 3.1, Cor 3.4].
- Chen [10, A.5.1].
- Top–Yui [30, Table 2], whose singular fibres t = ∞, 0, 1, −8 match Λ = ∞, 1, 0, 9.
- Moreland–Zieve [23], including the counterexample (3, 10, 24).
- Sadek–El-Sissi [26], arXiv v1 and v2 (see M2).
- Zhang [34], which quotes the BGN "n ≥ 16" expectation.
- Abstracts of Cha et al. [9], van Doorn [32], MacLeod [21] and Youmbai–Zargar–Voznyy [33].
- Crossref metadata for all journal references.

**Could not verify:**
- BGN [3]: the AMS server returned a bot challenge, so the p. 117/118/119/120/130 page citations and quotations are unverified, although [24] and [34] corroborate the content.
- Mazur [22]: the Numdam PDF was unreadable, so "Ch. III, Thm (5.1), p. 156" is unverified.
- Beauville [1], Bremner–Guy [2], Bremner–Nguyen Xuan Tho [6] (theorem numbers 8, 9, 14), Kelly [19], Kubert [20] and Choudhry [11], all paywalled. Project Euclid served a challenge page for Choudhry.

## FATAL

None.

## MAJOR

**M1 (pp. 5–6; also Theorem 2 on p. 12 and Corollary 1 on p. 9). Choudhry [11] is cited but was not read, and priority is left open.**
The note says Choudhry's paper "was not accessible to us, so we cannot say whether his family is, or contains, the dual family or the isosceles family". Yet it credits him with "a three-parameter solution", which Chen [10, A.5.1] confirms. On p. 6 the note claims novelty for "the bounds of Theorem B", which are built on these two families.

*Integers* cannot publish a paper that cites a result its authors have not seen, while that result may contain one of the paper's two main parametrisations. Rocky Mountain J. Math. 41(3) (2011), 737–763 is on Project Euclid (DOI 10.1216/RMJ-2011-41-3-737) and through any library.

*Resolution:* obtain [11]. State precisely whether its three-parameter family contains D_{u,v}, the dual family, or both, and adjust the credit in Section 1.4 and around Theorem 2 and Corollary 1. If the dual family is there, Theorems 2–3 stay new as counting results, but the families must be attributed.

**M2 (p. 4, lines 3–9 of Section 1.4; p. 11, paragraph after Theorem 1). Sadek–El-Sissi is cited at statement level with numbering and hypotheses I could not match to any available version.**
The note cites "[26, Proposition 2.7 and Theorem 2.8]" for a statement about "three distinct positive **rationals** u₁ > u₂ > u₃". In arXiv v2, the version with the extra hypothesis d₁(d₂−d₃)³ ≠ d₃(d₁−d₂)³:
- the results are **Proposition 2.6 and Theorem 2.7**;
- they are stated for distinct positive **integers**;
- Theorem 2.7 has "positive integers d₁ > d₂ > d₃".

In v1 the same numbers (2.6, 2.7) are used, the hypothesis is absent, and the triples are distinct nonzero integers. Moreland–Zieve refer to "[20, Prop. 2.6] and [20, Thm. 2.7]" of v1. zbMATH's review of the Osaka version (Zbl 1317.14072) describes integer partitions. If the published Osaka J. Math. 52 (2015) version renumbers to 2.7/2.8 and works over Q, the citation is right but must say so. Otherwise both the numbering and the word "rationals" are wrong.

*Resolution:* check the published paper. Cite it with its own numbering, and add "(Proposition 2.6 and Theorem 2.7 in arXiv:1303.6705v1)" where the note discusses the first preprint and Moreland–Zieve's counterexample. Make "integers" or "rationals" match the source.

## MINOR

**m1 (p. 13, proof of Theorem 2).** The claim that the gcds (2u+v)/g and (u+2v)/g "are coprime" is not justified when g = 3. One line fixes it: if 3 divided both quotients, then 9 | 3(u+v), so u+v ≡ 0 (mod 3); together with u ≡ v this forces 3 | u, a contradiction.

**m2 (p. 4, paragraph after Proposition D).** "S^{2+ε} is the size one expects for such points in general" is not right.
- S^{2+ε} is the affine *dimension-growth* bound for a threefold in A⁴: what one can prove in general, not what one expects.
- Homogenised with S as a coordinate, the variety of pairs is a quintic hypersurface in P⁴ (p. 22). Its expected count off accumulating subvarieties is far smaller.
- N(X) ≪ X^{3+ε} is then the dimension-growth bound for a degree-5 projective threefold, known by the work of Heath-Brown and Salberger, with later uniform versions by Castryck–Cluckers–Dittmann–Nguyen.

Reword the sentence, and cite this literature so the reader sees that Proposition 5 is an elementary special case of a known bound. It would also help to note that a quintic in P⁴ has trivial canonical class (compare the Schoen remark on p. 22), since that supports the heuristic of Section 6.4.

**m3 (pp. 5–6). Missing reference.** Nguyen Duy Tan and Nguyen Xuan Tho, "An extension of Bremner and MacLeod's theorem", Rocky Mountain J. Math. 54(3) (2024), 885–893, DOI 10.1216/rmj.2024.54.885. It extends the Bremner–Macleod non-existence result that the note itself translates to C_{2N+6}, so it belongs next to [4] and [24].

**m4 (p. 5). Uncited identity.** The "classical identity" (λ/x with λ = e₁eₙ/e_{n−1}) needs a reference, or the word "classical" should be removed. The one-line proof could be given instead.

**m5 (p. 15, Proposition 4(i)).**
- "Its Picard rank over Q is 5" uses Pic(Y) = Pic(Ȳ)^{Gal}. That holds because Y(Q) ≠ ∅; say so, with a reference.
- Browning–Sofos's hypotheses are "X(Q) ≠ ∅ and X contains a conic defined over Q", not "a conic bundle over Q". State that the strict transform of a rational line through (1:0:0) is such a conic, so the hypothesis is checked in the source's own terms.

**m6 (p. 16, proof of Proposition 4(iii)).** The clause "while a pair comes from at most twelve points" plays no role in an upper bound. Only "each pair comes from at least one point and a point determines the pair" is used. Delete the clause or say why it is there.

**m7 (p. 2, Section 1.1).** The note cites "(see also the erratum [15])" without saying whether the erratum affects (5.7). State whether it does.

**m8 (p. 3).** "the elliptic modular surface of Γ₀(6), which is ±Γ₁(6) [30, Table 2]". Top–Yui's Table 2 lists Γ₀(6) for this equation. The identification Γ₀(6) = ±Γ₁(6), true because (Z/6)^× = {±1}, is the note's own remark. Move the citation so that it covers only what [30] states.

**m9 (p. 17).** "The torsion column of Table 2 also follows from Theorem 1: for Λ = 155/12, 68/5, 1849/120, 230/21". Λ = 155/12 is not in Table 2; it is the Theorem 4 curve. Separate the two.

**m10 (p. 4).** "Theorem B is needed only for the lower bound A(y) ≫ y, which the primitive isosceles pairs already give." This is confusing, because the isosceles count *is* part of Theorem B. Say instead "only Theorem 2 is needed, for A(y) ≫ y".

**m11 (pp. 3, 5, 7, 8, 9, 16; references [3], [22], [1], [2], [6]).** These are statement-level citations I could not access (see above). Please confirm against the originals:
- BGN p. 117 (reciprocal pairs, scale invariance), p. 118 (model (6), "egg"), p. 119 (quotation), §4 p. 120 (quotation and table), p. 130;
- Mazur Ch. III, Thm (5.1), p. 156 (Kubert's tables);
- Beauville, "Théorème and Tableau, p. 658";
- Bremner–Guy's invariant (x+y+z)³/xyz;
- Bremner–Nguyen Xuan Tho "Theorems 8, 9, and 14".

Direct quotations in particular must be checked against the printed page.

**m12 (p. 10, Theorem 1(iii)).** 2G = (0:1:−1) + T₂ equals (1:0:0) by Proposition 2 (A = T₂ + Q). Saying so would shorten the proof of (iv) and make the identification of "the two points of order 6" explicit.

## Presentation and house style

**P1 (p. 21, Figure 1(b)).** The dashed log-power fit lies on the heavy curve and cannot be seen for S ≳ 600, and it is not drawn below 600. Use contrast, an offset or an inset, or remove it from the figure and the caption.

**P2 (p. 17, Table 1).** The column heads say "image of α / ᾱ" while the caption says "the Selmer groups containing the images". The text explains that they coincide; make the caption say "Selmer groups (= images)".

**P3 (p. 6, Proposition 1).** "Primitive triples, no one of them proportional to a permutation of another": for primitive triples, "proportional" means "equal", so "no one a permutation of another" suffices.

**P4 (p. 14).** The theorem title "(One more logarithm; the constant is not optimised)" carries commentary. *Integers* theorem headers are normally short names; move the remark to the text.

**P5 (p. 22).** "Over the curve of values Λ = (r+1+1/r)²" should say "after the base change r ↦ (r+1+1/r)²". The set of such Λ is not a curve.

**P6 (pp. 22–23).** A "Statements and Declarations" block (funding, competing interests, data) is not part of the *Integers* template. Keep the data statement, preferably as a short paragraph or in the acknowledgements, and follow the editor's instruction on the rest.

**P7 (references).**
- [10] "Chen Shuwen" and [6], [24] "Nguyen Xuan Tho" depart from the initials-plus-surname form used elsewhere. Pick one convention consistent with *Integers* (e.g. "S. Chen") and apply it throughout. The running text alternates "Bremner and Macleod" and "MacLeod" correctly by source, but a reader will think it is a typo, so add a footnote or keep the source spellings consistently.
- [29] should read "2nd ed., Undergrad. Texts Math., Springer, Cham, 2015".
- [8] appeared online in 2018; 2019 is the print year and is fine.
- Ensure the journal abbreviations follow one standard (e.g. "Proc. Edinb. Math. Soc. (2)" vs "C. R. Acad. Sci. Paris Sér. I Math.").

**P8 (throughout).** Cross-references, equation numbers (1)–(2), table and figure numbers, and the lettered results A–E all resolve correctly. I found no broken references. All pages were read as images, and I found no typographical sign or figure errors beyond P1.

## Recommendation

**Minor revision** (confidence: high for the mathematics and numerics; moderate for the citation items I could not access).

The mathematics is correct. Every proof step checks, and every number in Tables 1–3, Section 4 and Section 6 that I recomputed is exact. What blocks acceptance is citation integrity: M1 (an unread source that may anticipate the main families) and M2 (statement-level numbering and hypotheses of [26]). Both are fixable without new mathematics, but M1 must actually be done: if Choudhry's family contains the dual or isosceles family, the credit in Sections 1.4 and 4 has to change.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Read [11] and state its relation to D_{u,v} and the dual family; revise attribution. |
| M2 | Check the Osaka version; give correct numbering and "integers" or "rationals"; map to the v1 numbering used by Moreland–Zieve. |
| m1 | Add the one-line 9 ∤ argument. |
| m2 | Reword "the size one expects"; cite the dimension-growth literature; optionally note K = 0 for the quintic. |
| m3 | Cite Nguyen Duy Tan–Nguyen Xuan Tho (2024). |
| m4 | Reference or prove the λ/x identity. |
| m5 | Justify Pic_Q via Y(Q) ≠ ∅; quote BS's hypothesis verbatim and verify it. |
| m6 | Drop or explain the "at most twelve points" clause. |
| m7 | Say whether the erratum touches (5.7). |
| m8 | Restrict [30] to Γ₀(6). |
| m9 | Remove 155/12 from the Table 2 sentence. |
| m10 | Replace "Theorem B" with "Theorem 2". |
| m11 | Verify the listed page and theorem citations and quotations against the originals. |
| m12 | Note 2G = (1:0:0). |
| P1–P8 | Editorial changes as listed. |

---
Everything is in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/N-e-integers-copy-and-proof-editor/scratch/`:
- **`code/`:** the check scripts (`sym.py`, `sym2.py`, `pari1.py`, `pari2.py`, `iso.py`, `chk3.py`, `dp.py`, `more.py`, `tab.py`, `cr.py`) and the enumerator `enum.c`.
- **`e6000.txt`:** per-S enumeration output for S ≤ 6000.
- **`dl/`:** the downloaded sources.
- **`pages/`:** the rendered page images.
