<!-- Round 8 N-a editor report: returned text saved verbatim; the reviewer could not write files -->

Writing to REPORT.md was refused, so the full report is below.

# Handling editor's report: "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

Handling editor: additive combinatorics and sums of unit fractions.
Materials: the submission (22 pp.) and the two disclosed related manuscripts by the same six authors ("How much of a hyperbolic orbifold does heat hear?", 58 pp.; "Finitely many eigenvalues determine the signature of a hyperbolic orbifold", 36 pp.). As instructed, I treat the placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) as known. Page numbers are the printed ones, which are the same as the PDF page numbers. I checked every typographical or figure point below against rendered page images at 80–300 dpi.

---

## 1. Summary

The note studies unordered triples of positive integers that share both the sum S = e1 and the reciprocal sum R = e2/e3 with another triple. It shows that such triples have R < 1 (Lemma 1). They therefore correspond to pairs of hyperbolic triangle orbifolds that the first two heat invariants cannot tell apart. Since Λ = SR = e1e2/e3 is scale-invariant, a class of such triples is a finite set of positive rational points on one member of the pencil C_Λ : (x+y+z)(xy+yz+zx) = Λxyz. This is the Bremner–Guy–Nowakowski (BGN) curve, which is Beauville's Γ1(6) pencil.

The results:
- **Theorem 1 (Theorem A).** For rational Λ the torsion of C_Λ(Q) is Z/6, Z/12 or Z/2×Z/6, with explicit criteria. For Λ > 9 a positive point is torsion exactly when it is isosceles or a geometric progression. Lemma 4 says which torsion translations preserve positivity. Reciprocation is translation by the 2-torsion point T2 (Proposition 3, after BGN). This gives the "dual family" of Corollary 1.
- **Theorems 2 and 3 (Theorem B).** N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X, from the isosceles family. N(X) ≥ (3/(128π⁴) + o(1)) X (log X)², from the dual family viewed as a conic bundle.
- **Theorem 4 (Theorem C).** Classes of every size, by Schinzel's argument on C_{155/12}. No novelty is claimed for the method.
- **Proposition 4 (Proposition D).** n(S) ≪ S^{2+ε}, hence N(X) ≪ X^{3+ε}.
- **Section 4 remark.** The dual family is a quartic del Pezzo surface of Picard rank 5, so by Browning–Sofos it contributes O(X (log X)⁵).
- **Section 6.** An exhaustive enumeration to S = 6000 (about 6 × 10⁹ admissible triples), Tables 1–2, curve fits, and the open Question E: is N(X) = X^{1+o(1)}?

## 2. Significance and fit

**Fit.** The note fits Integers well. It is an elementary-to-intermediate Diophantine counting problem in the line of Guy's D16 and Schinzel's note, uses elliptic curves only at a classical level, and comes with a complete and reproducible computation.

**Significance is modest, and I want to be plain about it.**
- The genuinely new mathematics is:
  - the positivity analysis of torsion (Theorem 1(iv), Lemma 4);
  - the two lower bounds (elementary lattice-point counts over explicit families);
  - the observation that the dual family is a quartic del Pezzo surface, so Browning–Sofos bounds its contribution.
- Theorem 1(i)–(iii) is classical (Kubert/Mazur and the Tate normal form), as the authors say.
- Theorem C is Schinzel's argument applied verbatim, as the authors say.
- Proposition D is at the scale of the number of triples (see M3). The paper's central question, the growth exponent of N(X), is left wide open between 1 and 3.
- The enumeration is careful and, as far as I could recheck it, exactly right. It is the most solid contribution, and it is valuable as a reference dataset.

In short, this is a competent, honest and well-credited note with modest theorems. That is within the range Integers publishes. It is not a paper that settles anything.

**Novelty search.** I searched OpenAlex, arXiv, Crossref and OEIS for: equal sum / equal reciprocal sum; (x+y+z)(1/x+1/y+1/z) = n; sums of reciprocals with equal sums; triangle orbifolds and heat invariants; the sum sequence 18, 20, 26, 31, 32, 34, ...; and the pairs themselves.
- I found no prior counting result for N(X) or N_cl(X). The enumeration and the two counting theorems appear new.
- The search turned up one clearly relevant omission, Bremner–MacLeod 2014 (M1).
- It also confirmed the one acknowledged gap: the authors have not read Choudhry 2011 (M2).

## 3. Correctness and what I recomputed

I found no mathematical error. Everything below was recomputed independently in my scratch folder: my own C enumerator with exact rational keys, sympy, and PARI/GP 2.17.2 through cypari2 in a private venv.

**Symbolic checks**
- The Weierstrass model E_Λ: η² = s(s² + (Λ²−6Λ−3)s + 16Λ) and the map s = −4e2/z², η = 4Λ(Λ−1)(x−y)/(x+y−(Λ−1)z) (Proposition 2, p. 6). The numerator of η² − cubic(s) reduces to 0 modulo the equation of C_Λ.
- The discriminant 2¹²Λ²(Λ−1)³(Λ−9). The c4 values at Λ = 0, 1, 9 are non-zero. The fibre types are I2, I3, I1, and I6 at ∞.
- The change of variables to the Tate normal form with c = −1/Λ (p. 3). The Tate equation equals (E_Λ equation)/(64Λ⁶) identically, and (0:1:0) ↦ (0,0) (sign of η checked).
- The worked example (1:4:4) ↦ (s, η) = (−6, 45) at Λ = 27/2 (p. 6).

**Group law** (my own chord-and-tangent on the plane cubic, origin O = (1:−1:0)):
- On C_{27/2}: T2 has order 2; (1:0:0) has order 6; (0:1:−1) has order 3; (1:1:4) has order 2; (4:1:1) and (1:4:4) have order 6. This matches Theorem 1(iv).
- On C_{49/4}: (1:2:4), (2:1:4), (2:4:1), (4:2:1) have order 12, and (1:4:2), (4:1:2) have order 4. This confirms "order 4 iff the middle term is the last coordinate".
- On C_{169/16}: (1:−4:16) has order 12.
- On C_{155/12}: 3P = (162833463 : 723926268 : 287876366) and P + T2 = (9:4:2), as on p. 15.
- The pair {(165,240,440), (182,208,455)} on C_{169/16} differs by torsion points of orders 4 and 12 for suitable orderings (Lemma 4 example, p. 11).

**Proofs re-derived by hand**
- Lemma 1: both discriminants on pp. 5–6 are correct.
- Lemma 2: the egg argument.
- Lemma 3: the transposition argument via α² = 1 and fixed points.
- Proposition 3 and Corollary 1.
- Theorem 1(ii)–(iv).
- Lemma 4.
- Lemma 6.
- The constant c_iso in Theorem 2: |Ω| = (log 2)/6, the residue-class Möbius count (6/π²)t²|Ω|·#U/8, and the U1/U3 weights 3/4 + 3/4.
- The constant 3/(32π⁴) in Theorem 3 and its error terms (O(M³√y log y) = O(y^{7/8} log y)).
- The identity in Proposition 4: (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′. It is correct.
- The del Pezzo claims: the six cubics vanish at the five points; no three of the points are collinear; the Picard rank over Q is 5.
- Browning–Sofos, Math. Ann. 373 (2019), Theorem 1.1 (read from arXiv:1609.09057). Its hypotheses are X(Q) ≠ ∅ and a conic over Q, and it gives c1 B(log B)^{ρ−1} ≤ N(B) ≤ c2 B(log B)^{ρ−1}. The note uses it correctly, including the caveat that positivity is not part of that theorem.

**Enumeration** (exact rational keys, independent of the authors' code):

| Quantity | Result |
|---|---|
| Table 2, every column, X = 18, 100, 200, 300, 400, 500, 600, 1000, 2000, 3000 | all agree exactly |
| Local exponents at 600, 1000 and 6000 (from the table counts) | agree |
| Admissible-triple totals 3 067 197 199 (S ≤ 4800) and 5 992 496 499 (S ≤ 6000), by closed form | agree |
| "582 sums 19 ≤ S ≤ 600, 507 carry a primitive class" | confirmed |
| Dual share 32.9% for S ≤ 200 | confirmed (82/249) |
| "All 1330 non-dual primitive pairs with S ≤ 600" | confirmed (1753 − 423) |
| First classes of sizes 3, 4, 5, 6 at S = 136, 408, 1849, 4600, Table 1 members | exactly as listed |
| Class sizes at S ≤ 4800 (96 981 / 1627 / 122 / 11 / 1) | consistent with N(4800) and N_cl(4800): 96 981 + 3·1627 + 6·122 + 10·11 + 15 = 102 719 |
| 7626 + 4 + 38 624 | = 46 254; 16.5% and 83.5% correct |
| 506 pairs D_{u,v} with S ≤ 4800 (c_iso·4800 = 505.66) | confirmed |
| Copies of kD_{u,v}: 0.608X at 4800; second-order term −0.2852, −0.2860, −0.2862, −0.2863 at X = 4800, 10⁴, 10⁵, 10⁶ | consistent with "−0.286X to three digits" |
| Heat manuscript's "38 collision-free sums, the last 557" | consistent (38 such sums up to 700, last 557) |

**PARI/GP (ellrank, elltors, ellglobalred, ellrootno)**

| Curve | Rank | Torsion | Conductor | Root number |
|---|---|---|---|---|
| C_{27/2} | 0 | Z/2×Z/6 | 90 | +1 |
| C_{68/5} | 2 | Z/6 | 82110 | +1 |
| C_{1849/120} | 3 | Z/6 | 1715185290 | −1 |
| C_{230/21} | 3 | Z/6 | 41388270 | −1 |
| C_{155/12} | 2 | Z/6 | 6250530 | +1 |
| C_{169/16} | 1 | Z/12 | — | — |
| C_{49/4} | 0 | Z/12 | — | — |

ellrank returned r1 = r2 for every curve, so the ranks are unconditional. The 2-isogeny arithmetic 2^r = |α(Γ)|·|ᾱ(Γ̄)|/4 on p. 15 matches these ranks.

**Not checked**
- I could not verify the verbatim BGN quotations (pp. 7, 8, 120). The AMS site blocks headless access.
- I could not verify the Sadek–El-Sissi statements (p. 10) or Choudhry 2011 (Project Euclid also blocks headless access).
- I did not recheck the regression and resampling numbers of §6.3, the 189-line search of §6.4, or the "none of the 669 pairs satisfy P′ = ±mP + T" test.

## 4. FATAL

None. I found no error that invalidates a stated result.

## 5. MAJOR

**M1 (pp. 4–5, §1.4). A directly relevant prior paper on the same pencil is missing: A. Bremner and A. Macleod, "An unusual cubic representation problem", Ann. Math. Inform. 43 (2014), 29–41.**
- It studies N = a/(b+c) + b/(c+a) + c/(a+b), the "fruit puzzle".
- Its curve is E_N: y² = x³ + (4N² + 12N − 3)x² + 32(N+3)x. This is exactly the note's E_Λ with Λ = 2N + 6: then Λ² − 6Λ − 3 = 4N² + 12N − 3 and 16Λ = 32(N+3). Equivalently, (x, y, z) = (b+c, c+a, a+b) gives (x+y+z)(1/x+1/y+1/z) = 2N + 6.
- It treats the torsion (Z/6 except one N), uses the "egg" and odd multiples, and works out which points are strictly positive.
- It proves that strictly positive solutions do not exist for N odd, that is for 4 | Λ, on the triangle-inequality sub-region of the positive triangle. This anticipates the Nguyen Xuan Tho theorem cited on p. 5, which is the same statement on the whole positive region.
- It famously shows that positive points on these curves can be astronomically large, which is relevant to the remark on p. 15 that classes from one point are "far out".

The note already discusses MacLeod's R/r triangles, the mirror substitution (a,b,c) = (y+z, z+x, x+y) giving Λ = 4N + 1, so it must also discuss Bremner–MacLeod. The positivity statements of Lemma 2 and Lemma 4 should be compared with theirs. The "new" label on the positive-torsion description in Theorem A (p. 3) needs to be checked against their Remarks 2.2–2.5. Theirs concern integer N, so I expect the rational-Λ statement to survive, but the authors must say so.

**M2 (p. 5). The authors cite Choudhry 2011 without having read it.** They write "we have not been able to consult Choudhry's paper, and do not know whether his family contains the dual or the isosceles family". This is not acceptable in a submitted research paper.
- Choudhry's three-parameter solution of the (k = −1, 1) type is exactly the object of Corollary 1 and Theorem 2.
- The novelty sentence at the end of §1.4 ("individual coincidences and a parametric family are in [7, 8]") cannot be judged until the authors have compared the families explicitly.
- The paper is in Rocky Mountain J. Math. and is obtainable through any library or by writing to the author.

Required: state precisely whether Choudhry's family contains, equals, or is disjoint from the isosceles family D_{u,v} and the dual family D(x), and adjust the credits.

**M3 (pp. 4, 17). Proposition D is placed too modestly and too vaguely.**
- n(S) ≪ S^{2+ε} is exactly the dimension-growth scale for integer points in a box of side S on a hypersurface in A⁴. The pairs at fixed sum are cut out by one equation in (p, b, p′, b′).
- Correspondingly, N(X) ≪ X^{3+ε} is dimension growth for the threefold of pairs.
- The text says only that the bound "gains a factor S^{1−ε}" over the trivial bound and "remains at the scale of the number of triples". The reader is not told why this is the natural barrier or what kind of input could beat it: the elliptic fibration, or determinant-method bounds for points off special subvarieties.
- With Theorem B the exponent is pinned only between 1 and 3, and the note's main question is open.

At a minimum, the authors should explain that Proposition 4 is the generic bound and what an improvement would need. Better, they should make a serious attempt at n(S) = o(S²) or N(X) ≪ X^{3−δ}. Two possible routes:
- the determinant method applied to the open part of the variety of pairs, after removing the trivial planes x′ = πx;
- a uniform bound on class sizes. Class sizes are numbers of points of height ≪ S on one elliptic curve, and rank bounds give them as ≪ S^{o(1)}-type quantities.

A uniform upper bound on class size alone, even S^{1/3+ε} from Bombieri–Pila, would be a natural companion to Theorem C. As it stands, Proposition D adds little.

**M4 (§6.3, pp. 18–19; abstract p. 1; §6.4 p. 19). The quantitative reading of the numerical growth data is weaker than its presentation suggests.**
- The two-parameter "log-power" and "power" fits are compared over 600 ≤ S ≤ 4800 and then tested on 4801–6000. That test window has a log-ratio of only 0.22, and the two models differ by about 2.5% there. The block-resampling "spreads" are, as the authors admit, not uncertainties. The quasi-likelihood difference of 1.4 separates nothing.
- The authors themselves note that the fitted q for the dual family (2.56) is far from its expected 4. This is strong evidence that the fitted q are not estimates of anything asymptotic.

I do not object to reporting the data; Table 2 is valuable. But the inferential apparatus (Poisson ML, Pearson dispersion, quasi-likelihood, resampling) gives the appearance of evidence about an asymptotic exponent where none exists. Please restrict §6.3 to descriptive statements. Consider replacing the statistical comparison with a theoretical heuristic. Section 6.4 already observes that the variety of pairs is a quintic hypersurface in P⁴ whose resolution is Calabi–Yau (Schoen). For a quintic threefold in P⁴ the usual heuristics predict y^{o(1)} rational points of height ≤ y off accumulating subvarieties. That is genuine support for Question E: A(y) would be dominated by rational curves and surfaces such as the isosceles curve and the dual del Pezzo, plus the special fibres. It is more informative than curve fitting.

## 6. MINOR

- **m1 (p. 11, Remark 1).** "No linear families; a sketch" is a statement in a numbered remark with only a sketch of proof. The pole-matching argument is plausible but not complete; for example, the "charges" and the affine case are not written out. Either give a proof, or mark it explicitly as heuristic and drop the claim "every other family by forms of one degree has degree at least 2" from §6.4 (p. 19), which relies on it.
- **m2 (p. 5).** Chen's survey calls {4,10,12}, {5,6,15} (S = 26) and {6,14,14}, {7,9,18} (S = 34) the "smallest solutions". The note remarks only that the S = 18 pair is smaller. Also state that {(4,8,8), (5,5,10)} at S = 20 precedes them, so Chen's claim is wrong; I confirmed S = 18, 20, 26 are the first three sums. Also note that Chen's three-term chain {45,165,198}, {48,120,240}, {65,70,273} is not a full class: it misses (51,102,255) (Table 1, p. 16).
- **m3 (p. 5).** For context in the unit-fraction literature, add a sentence relating the problem to counts of triples with a prescribed reciprocal sum alone: Browning–Elsholtz on representations of m/n as a sum of unit fractions, and Elsholtz–Tao on Erdős–Straus. The novelty here is the joint constraint with the sum, and the reader in this area will ask about it.
- **m4 (p. 3).** "the description of the positive torsion points is new" should be softened to "new for rational Λ" after M1. For integer Λ, BGN's table and Bremner–MacLeod's remarks already contain it, since only Λ = 10 has extra torsion there and no integer Λ > 9 is of the form (r + 1 + 1/r)².
- **m5 (p. 2).** The note cites DGGW [11, (5.7)] for the constant heat term (S + R − 2)/12. The disclosed heat manuscript cites [DGGW, (5.13)] and Remark 5.16 for the triangle case. Please make the two citations consistent, or explain why they differ. The formula itself is right: χ/6 + Σ(m_i² − 1)/(12m_i) with χ = R − 1 gives (S + R − 2)/12.
- **m6 (p. 20).** Give the exact statement of Schoen [24, Proposition 7.1] that is used. It should say that the self-fibre product of this semistable surface, with all singular fibres coinciding, has a projective small resolution that is Calabi–Yau. It is also worth noting that the self-fibre product of the Beauville Γ1(6) surface is a well-studied rigid Calabi–Yau threefold, which strengthens the heuristic in M4.
- **m7 (p. 15).** The 2-isogeny descents "in exact arithmetic" are asserted, not shown. Since the ranks enter only Table 1 and the rank-0 statement for C_{27/2}, which the companion proves by hand, either point to the deposit file by name or say plainly that the ranks are machine results. They agree with my PARI run.
- **m8 (p. 15).** The conductors are given without the curve models. Give an LMFDB label or minimal model for at least C_{27/2} (90.c3, as in the companion manuscript) so a reader can check.
- **m9 (p. 16).** The double-hashing argument is fine (e2, e3 < 2⁵³, and division is correctly rounded). Say "e2, e3 ≤ 8·10⁹ < 2⁵³ for S ≤ 6000" so the reader need not work it out.
- **m10 (p. 17, Table 2).** The text uses X = 5400 as a checkpoint, but Table 2 omits it. Also, local exponents for X = 100, 200, 400, 500, 4800 need N(X/2) at 50, 100, 200, 250, 2400; give these, or note that they are in the deposit.
- **m11 (p. 4, Question E).** "Equivalently (with Theorem B)": only the lower bound A(y) ≫ y from Theorem 2 is needed. Say so.
- **m12 (pp. 13–14).** In Theorem 3 the multiplicity bound "at most 6 tuples" uses that the member of D proportional to x determines x up to scaling, and that v = gcd of the other two entries. Write that sentence in the proof of Lemma 6. It is now compressed into "The remaining two entries ... determine (q, r, v)".
- **m13 (p. 10).** The statements attributed to Sadek–El-Sissi (Proposition 2.7, Theorem 2.8) are long and conditional. Please check them against the published version; I could not access it.

## 7. Presentation

- **P1 (throughout). Symbol overloading:**
  - A is used for the point (1:0:0) (p. 7), the counting function A(y) (pp. 4, 13), and b + c (p. 17).
  - R is used for the reciprocal sum and the circumradius (p. 5).
  - r is used for the geometric-progression ratio (Theorem 1), the inradius (p. 5), and the second parameter in Lemma 6 (q ≤ r).
  - c is used for a triple entry and the Tate parameter c = −1/Λ (p. 3).
  - N is used for the counting function and MacLeod's R/r = N (p. 5).
  - U is used for a box side (p. 13) and for unions of residue classes (p. 12).

  Rename the clashes; for example, use ρ for the geometric-progression ratio, and use different letters for the residue classes and the box.
- **P2 (pp. 3–5).** §1.3–1.4 interleave results, credits and literature in long, heavily qualified sentences. The reader has to reach p. 5 to learn what is claimed as new. Move the novelty statement ("As far as we know ...", p. 5) to directly after Theorem B, and separate the literature on (i) equal sums and products, (ii) the curves C_Λ, and (iii) equal sums of like powers with negative exponents.
- **P3 (p. 19, Figure 1(b)).** The dashed log-power fit is drawn in grey over the heavy black curve and is barely distinguishable at print resolution (checked at 300 dpi). Use a contrasting dash or offset. The axis label N(S)/S should be N(X)/X, or the caption should say that S is the cumulative bound.
- **P4 (p. 19, Figure 1(a)).** This panel is correct. I checked that the orange points (1,1,4) sit toward the vertices and the dark points (1,4,4) toward the edge midpoints in the chart x + y + z = 1, with the egg inside the triangle. The caption should say that the three unbounded branches pass through the base points at the triangle's vertices.
- **P5 (p. 6).** "the maps ... together with (x − y)/z = ..." is hard to parse as typeset. Display the inverse map on its own line.
- **P6 (p. 1, abstract).** The sentence "and by a theorem of Browning and Sofos they contribute O(X(log X)⁵)" should say "the dual pairs and their multiples contribute". As written, "the pairs coming from reciprocation" could be read as all coincidences.

## 8. Overlap with the disclosed manuscripts

- **Heat-invariants manuscript.**
  - It overlaps the note in one theorem. Its Theorem 5.8, the isolation of the minimal pair (C_{27/2}(Q) ≅ Z/2×Z/6, rank 0), is proved there by hand with a 2-isogeny descent in Appendix E. The note restates the same fact on p. 15 as a by-product of its machine rank computations and explicitly cites [13, Theorem 5.8].
  - The two papers share the enumeration to S = 4800, which the heat manuscript says openly is "the same computation". The heat manuscript also summarises the note's Theorems B and C and states that none of its proofs depend on them.
  - The statements are mutually consistent: the minimal pair, 18 and R = 3/4, the second collision at S = 20, Λ = 27/2, conductor 90, and the 38 collision-free sums ending at 557, which I confirmed.
  - The overlap is properly disclosed, symmetric in its cross-references, and small relative to either paper. I see no duplicate-publication problem, provided neither paper claims the C_{27/2} result as its own new contribution. The note currently does not; it says "this is also [13, Theorem 5.8]".
- **Eigenvalue manuscript.** It uses O(2,8,8) and O(3,3,12) only as a test example and cites the note for the arithmetic. There is no substantive overlap.
- **Placeholder cross-reference.** Reference [13] is a placeholder preprint. Before acceptance it must resolve to a public identifier, because the note relies on it for priority on the C_{27/2} statement.

## 9. Editorial decision and recommendation

- **Editorial decision: send to review** (not desk-reject). The note is in scope, correct as far as I could check (and I checked a great deal), honest about what it does not prove, carefully credited apart from M1 and M2, and fully reproducible. Its significance is modest but real: the counting function and the lower bounds are new, and the dataset is useful.
- **My recommendation: major revision.** The weight is on literature and positioning, not on correctness:
  - M1: the missing Bremner–MacLeod paper on the same pencil.
  - M2: the unread Choudhry paper that may contain the families.
  - M3: a placement of Proposition D, and ideally an improvement of it.
  - M4: the over-interpreted statistics.

  If M1 and M2 are resolved without damaging the novelty claims, I expect a short second round and eventual acceptance in Integers.
- **Confidence:** high in correctness (most numerical and symbolic claims were recomputed independently). Medium in the recommendation, because the outcome of M2 is unknown.

**For the referees:** I suggest one referee in Diophantine geometry / elliptic curves (to check Theorem 1, Lemma 4 and the del Pezzo remark against Browning–Sofos and Bremner–MacLeod) and one in elementary or analytic number theory (Theorems 2–3, Proposition 4, M3).

## 10. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Cite and discuss Bremner–MacLeod 2014. State the identification E_N(BM) = E_{2N+6} and the triangle-region positivity. Compare with Lemma 2, Lemma 4 and Theorem 1(iv). Note that their N-odd result is the triangle-region case of Nguyen Xuan Tho's 4 \| n. Adjust the "new" claims accordingly. |
| M2 | Obtain Choudhry 2011. State precisely how his three-parameter family relates to D_{u,v} and D(x). Revise the novelty sentence at the end of §1.4. |
| M3 | Explain that Proposition 4 is the dimension-growth bound and what is needed to beat it. Preferably add either a power saving or a uniform class-size bound. |
| M4 | Reduce §6.3 to descriptive statements. Remove or demote the inferential statistics. Add the Calabi–Yau/quintic heuristic as the main support for Question E. |
| m1 | Prove Remark 1 or mark it as heuristic and stop relying on it in §6.4. |
| m2 | Correct the statement about Chen's "smallest solutions" (S = 20 precedes S = 26), and note that his 408 chain is a class of four. |
| m3 | Add the Browning–Elsholtz / Elsholtz–Tao context. |
| m4 | Soften "new" to "new for rational Λ" once M1 is done. |
| m5 | Reconcile the DGGW equation numbers with the companion manuscript. |
| m6 | Quote the exact Schoen statement; mention rigidity. |
| m7, m8 | Name the deposit files for the descents; give LMFDB labels or minimal models. |
| m9 | One clause on the size of e2, e3. |
| m10 | Add the X = 5400 row and the N(X/2) values, or point to the deposit. |
| m11 | Say "with Theorem 2" instead of "with Theorem B". |
| m12 | One explanatory sentence in Lemma 6. |
| m13 | Check the Sadek–El-Sissi statements against the published version. |
| P1–P6 | Rename overloaded symbols; restructure §1.3–1.4; fix the figure contrast, axis label and caption; display the inverse map; reword the abstract sentence. |
| [13] | Replace the placeholder with a public preprint identifier before acceptance. |

---

All my working files are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/N-a-editor-additive-combinatorics/scratch/`:
- `code/` holds my scripts and the run to S = 3000 (`run3000.txt`).
- `lit/` holds the papers I fetched (Bremner–MacLeod, Browning–Sofos, Chen's survey, Nguyen Xuan Tho).
- The PARI/GP install is the venv in `venv/`.
