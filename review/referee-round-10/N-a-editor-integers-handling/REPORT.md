<!-- Round 10, N-a (editor), returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

I couldn't save the report to `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/N-a-editor-integers-handling/REPORT.md` because the harness blocked the write (subagents may not write report files). The full report follows. My scripts and the publisher's copy of Choudhry 2011 (from the Wayback Machine) are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/N-a-editor-integers-handling/scratch/` (`code/`, `lit/`).

# Handling editor's report: "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

## Summary

The note studies unordered triples of positive integers that share both their sum S and their reciprocal sum R with another triple. Lemma 1 shows that both members of such a pair have R < 1. Following Bremner, Guy and Nowakowski (BGN), a class of such triples is a set of positive rational points on one cubic C_Λ: (x+y+z)(xy+yz+zx) = Λxyz with Λ = SR. The results are:

- **Theorem 1 / Theorem A (torsion).** Torsion of C_Λ(Q) for rational Λ, which is classical via Mazur and Kubert. The new part is a determination of which torsion points are positive (isosceles triples and geometric progressions) and which torsion translations preserve positivity (Lemma 4).
- **Theorem 2 (isosceles family).** N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X.
- **Theorem 3 (dual family).** N(X) ≥ (3/(128π⁴) + o(1)) X (log X)².
- **Proposition 4.** Through Browning–Sofos on a quartic del Pezzo surface, the dual pairs and their multiples contribute O(X (log X)⁵).
- **Theorem 4 / Theorem C.** Classes of every size, by Schinzel's argument; the authors claim no novelty for the method.
- **Proposition 5.** n(S) ≪ S^{2+ε}.
- **Section 6.** An exhaustive enumeration up to S = 6000, curve-fitting of growth laws, and an open Question E (is N(X) = X^{1+o(1)}?).

## Significance

What is good:
- The note is careful and honest about attribution. It repeatedly disclaims novelty where none is claimed (Theorem C, Sections 2–3).
- Every proof I checked is correct.
- The computational work is exact and reproducible, and all the numbers I could check agree.
- Theorem 1(iv) with Lemma 4 (positivity of torsion) is a clean small addition to BGN.
- The del Pezzo upper bound is a sensible use of Browning–Sofos.

The weaknesses are at the level of significance:
- **The lower bounds come from explicit parametric families.** Both lower bounds count points of parametric families that are already in the literature: Choudhry's first solution, and the reciprocal pairing of BGN. Counting them is routine lattice-point work.
- **Both bounds are far from the truth.** For the dual family itself the note proves (log X)² against an expected (log X)⁵.
- **The upper bound is weak.** The only general upper bound, N(X) ≪ X^{3+ε}, is a divisor-bound argument that gains S^{1−ε} over the trivial bound. The data suggest an exponent of about 1.6.
- **The central counting question is untouched.** No bound of the form n(S) = o(S²) is proved.

The paper is a competent, well-organised account of a natural problem, with modest new theorems. That is within the range Integers publishes, but only with the literature positioning corrected (M1, M2).

## Correctness and what I recomputed

I recomputed independently. I used my own C enumeration, exact rational arithmetic in Python, sympy, and PARI/GP 2.17 through cypari2.

- **Table 3, up to X = 2000.** All entries agree exactly (pairs, classes, primitive classes, largest size, local exponents at 1000, 2000, 4000 and 6000). This includes N = 1, 92, 386, 840, 1496, 2210, 3067, 7641, 25042.
- **Section 6.1.**
  - The number of admissible triples with S ≤ 4800 is 3 067 197 199 (closed form).
  - 507 of the 582 sums 19 ≤ S ≤ 600 carry a primitive class.
  - The class-size distribution sums correctly to N_cl(4800) and N(4800).
  - 7626 + 4 + 38624 = 46254.
  - The pairs below S = 34 are exactly those at S = 18, 20, 26, 31, 32 and 34.
- **Table 2.**
  - The first classes of sizes 3, 4 and 5 are at S = 136, 408 and 1849, with the stated members.
  - The size-4 class is 3 × (size-3 class) plus (65, 70, 273).
- **Ranks, torsion, conductors and root numbers of all five curves in Tables 1–2** are confirmed by PARI. For example, C_{155/12} has rank 2, torsion Z/6, conductor 6250530 and root number +1. C_{169/16} has rank 1 and torsion Z/12; C_{49/4} has torsion Z/12.
- **Table 1.** The integral models a = p² − 6pq − 3q² and b = 16pq³ are checked, and so is the arithmetic 2^r = |α||ᾱ|/4.
- **Proposition 2.** The Weierstrass model and the example (1:4:4) ↦ (−6, 45) are checked. The stated change of variables to the Tate normal form with c = −1/Λ is an isomorphism: the equations agree up to the factor 1/(64Λ⁶).
- **Group law.**
  - Proposition 3: ι(P) = P + T₂.
  - Theorem 1(iv): (1:4:2) and (4:1:2) have order 4, and (2:1:4) has order 12 on C_{49/4}.
  - Theorem 4: 3P = (162833463 : 723926268 : 287876366) on C_{155/12}.
  - The four torsion-type pairs on C_{169/16} differ by points of order 4 and 12.
- **Proposition 5.** The identity (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′ holds symbolically.
- **Lemma 1, Theorem 2 and Theorem 3, checked by hand.**
  - Lemma 1: the discriminants are correct.
  - Theorem 2: c_iso = 3 log 2/(2π²); the residue-class Möbius computation gives the factors 3/4 and 1/4; there are 506 pairs D_{u,v} with S ≤ 4800; the copy count at 4800 is 2917 = 0.608X.
  - Theorem 3: the constants c_A = 3/(32π⁴) and 3/(128π⁴), and the crossover at log X ≈ 438.
- **Proposition 4.** The five base points are in general position. The six cubics vanish there. The Picard rank over Q is 5. The hypotheses of Browning–Sofos Theorem 1.1 (arXiv 1609.09057v4) are a rational point and a conic defined over Q, as stated.
- **Literature identities on p. 6.** MacLeod's R/r = (Λ − 1)/4 and Bremner–Macleod's Λ = 2N + 6 are correct.
- **Choudhry 2011.** I read the paper itself (RMJM 41(3), 737–763, archived publisher PDF; pp. 738, 745–748, 752–753). The family (35) is the third intersection of C_Λ with the line (34) through x and (x₂, x₃, x₁). Numerically, P + σP + Y = O, and none of about 2000 random positive x gives a positive y.

I found no error that invalidates any stated result.

## FATAL

None.

## MAJOR

**M1 (p. 5, lines on Choudhry; also pp. 9–10 and 13): the treatment of Choudhry [11, §4.1] is partly inaccurate.**

The identification of (35) is correct. Choudhry's (34), y_i = (x_{i+1} − x_i)t + x_i, is the line through x and its cyclic shift. The third root gives −(2P + τ), which is never positive. The note's claim that the three-parameter family contains no pair of positive triples is therefore right. In fact it understates the case: 2P + τ always lies on the identity component, so for Λ > 9 the third point is never positive, whatever x is.

However, the sentence "and the isosceles family below does not appear in that section" is wrong.
- Choudhry's first solution in §4.1 (p. 748) is y_i = m/x_i with m = Σx_i / Σx_i⁻¹, for every s ≥ 2.
- He states explicitly that "a solution in positive integers is obtained on appropriate scaling".
- Specialised to x = (u, v, v), this is exactly D_{u,v}. Theorem 2 itself calls D_{u,v} "the dual pair of (u, v, v)", and the smallest pair is Choudhry's first solution with x = (1, 4, 4).
- So both families the note counts (Theorems 2 and 3) are sub-families of a solution published in 2011.
- Choudhry's p. 738 also records Shuwen's identities. These are themselves dual pairs; for example, {4, 10, 12} and {5, 6, 15} are reciprocal up to scale.

Corollary 1 is stated without citation. The abstract says "the dual pairs, which come from reciprocation" with no attribution.

*Resolution:* delete or correct the sentence. Attribute Corollary 1 (and hence the families of Theorems 2–3) to Choudhry [11, §4.1, p. 748] in the statement, not only in §1.4. State the novelty precisely: the counting, not the families. Optionally give the stronger "never positive" form of the remark on (35).

**M2 (pp. 4–5 and 17): Choudhry §5.1 is omitted, and it bears on Theorem C and on the Ulas comparison.**

Choudhry [11, §5.1, (52)–(55), pp. 752–753] gives, for s = 3 and every t, parametric chains of t integer triples with equal sums for the exponents r = −1, 1, 2. A fortiori these are chains for (−1, 1). They have Σx⁻¹ = 0, so they lie on the singular fibre Λ = 0 and are necessarily of mixed sign. His Section 2 (p. 745) also proves that positive solutions exist for any exponent set when s is large.

The note cites Ulas (2013) for n ≥ 4 and exponents −1, 1, 2 as if nothing existed for triples. It also presents Theorem C without saying that arbitrarily long chains of integer triples for exponents −1, 1 were already known. The genuinely new content of Theorem C is positivity, together with an explicit curve of positive rank.

*Resolution:* cite §5.1 and Section 2 of [11], and restate the novelty of Theorem C accordingly.

**M3 (significance; pp. 3–4 and 13–16): the main bounds are far from the truth, and the gap is not narrowed where it plausibly could be.**

The dual family is the set of rational points of a quartic del Pezzo surface Y. Y is the blow-up of P² in three rational points and a conjugate pair, so it is Q-rational and has ρ = 5. The note proves only (log X)² for its contribution, against its own upper bound of (log X)⁵. The positive points are a nonempty real-open subset. The authors should either:
- prove the matching lower bound X (log X)⁵ for the positive points (for example by a direct count on P² with the cubic-form height, or by checking whether the lower-bound arguments of Browning–Sofos or Frei–Loughran–Sofos allow a real-open condition), or
- explain concretely why this fails.

On the upper side, Proposition 5 stays at S^{2+ε}. The note correctly identifies that the six planes x′ = σ(x) must be removed, but makes no attempt to do so. A referee for this journal may reasonably expect at least one of these two gaps to be narrowed. If neither is, the paper rests on Theorem 1(iv), Lemma 4, a routine count and an enumeration.

*Resolution:* narrow one gap. Failing that, recast the contribution modestly in the abstract and introduction as structure plus data, so that the claims match what is proved.

**M4 (Section 6.3 and the first paragraph of 6.4, pp. 20–22): the curve-fitting is presented as evidence it cannot provide.**

The material includes Poisson maximum-likelihood fits of c(log s)^q, window and residue-class variants of q, holdout comparisons between two hand-picked two-parameter laws, and the claim of "weak, non-asymptotic evidence for a positive answer to Question E". The authors concede that a finite range bounds the exponent from neither side. The fitted q varies from 4.06 to 4.97 with the residue class, and the primitive-pair local exponent is still about 1.48 at 4800. The section therefore supports no mathematical conclusion.

*Resolution:* keep the exact counts in Table 3 and the facts that are actually informative (the falling local exponents of N and A). Drop the fitted exponents and the phrase "evidence for a positive answer", or move them to the deposit. Present Question E without suggesting that the data favour it.

## MINOR

- **m1 (p. 5).** Chen's survey [10, A.5.1] describes {4,10,12},{5,6,15} and {6,14,14},{7,9,18} as "smallest solutions". The note shows implicitly that this is false (pairs exist at S = 18, 20, 31, 32, which I confirmed). Say so plainly. Also mention Chen's other chain (A.653), {44,253,276},{45,198,330},{66,78,429} at S = 573, which is a complete class (I checked), and the scaled chains (A.654)–(A.655).
- **m2 (p. 6).** "a parametric family in [11]" should read "two parametric families in [11], the first of which contains Corollary 1 and Theorems 2–3".
- **m3 (p. 14, Theorem 2).** "≥ c_iso X log X + O(X)" should be written as "≥ c_iso X log X − O(X)".
- **m4 (p. 15).** The theorem title "One more logarithm; the constant is not optimised" is informal. Move the qualification into the text.
- **m5 (p. 7, Proposition 1).** "Conversely" follows an if-and-only-if statement and is not a converse. Reword.
- **m6 (pp. 17–18, Table 1).** The table lists the Selmer groups. The text says that images of explicit rational points fill them, but the points are given only in the deposit. Print, for each curve, the points (or their x-coordinates) whose images generate. Note too that Theorem 4 needs only Theorem 1(iv), not the ranks, so the ranks are illustrative. Say so, to avoid the impression that Theorem C depends on a computation.
- **m7 (p. 19).** "e₂, e₃ ≤ (S/3)³" holds, but the sharper e₂ ≤ S²/3 makes clear that only e₃ is the binding quantity.
- **m8 (p. 4).** "(Proposition 4), probably of that order" is speculation in the statement of results. Remove it or move it to Section 4.
- **m9 (p. 4, Question E paragraph).** The equivalence argument is correct but compressed; spell out the partial summation in one more line.
- **m10 (p. 2).** The heat-trace formula is cited as [14, (5.7)]. The companion manuscript cites the same source as [2, (5.13)] for "c" in the triangle case. Both may be right, but check that the equation numbers refer to the published version.
- **m11 (p. 12).** The phrase "for suitable orderings, by a torsion point of order 4 or 12" should say which ordering gives which order. I find order 4 for one ordering and order 12 for two others.

## Presentation

- **P1.** §1.4 (pp. 4–6) is a single paragraph of about one and a half pages, mixing equal-product curves, Moreland–Zieve, Ulas, Chen, Choudhry, unit fractions, Nguyen Xuan Tho, MacLeod and Bremner–Macleod. Split it by topic: the equal-product analogue; equal sums with negative exponents (Chen, Choudhry, Ulas); the curves C_Λ (BGN, Nguyen Xuan Tho, MacLeod, Bremner–Macleod).
- **P2.** §1.3 places technical material (the Tate normal-form substitution, Beauville, Top–Yui, Kubert page references) before the statement of the results. Move it to Section 2.
- **P3.** Notation is overloaded:
  - c is a triple entry, the Tate parameter and a fit constant;
  - r is the ratio of a geometric progression, an entry in Lemma 6 and a rank;
  - q is a denominator of Λ (p. 17), an entry in Lemma 6 and a fit exponent;
  - p is the least entry in Proposition 5 and a numerator of Λ.

  Rename to avoid the collisions.
- **P4.** The abstract carries hedged numerical detail ("falling from about 2 near 500 to 1.58 at 6000") and a list of methods. State the theorems and the open question.
- **P5.** Figure 1(a), the real locus of C_{27/2}, is referred to only in passing at the end of §6.3. Either use it, for example in Lemma 2 to illustrate the egg, or drop it.
- **P6.** Rendered pages 1–25 show no typographical, sign or figure-label errors. The apparent "withsum" in a text extraction of p. 2 does not occur in the rendered PDF.
- **P7.** The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifier) are noted as known.

## Overlap with the disclosed manuscripts

**"How much of a hyperbolic orbifold does heat hear?" (65 pp.)**
- Its Theorem 5.10 proves, by a 2-isogeny descent by hand, that C_{27/2}(Q) ≅ Z/2 × Z/6 and that the minimal pair is isolated. The note derives the same statement in two lines from Theorem 1(ii) and a machine rank computation, and cites [17, Theorem 5.10] (p. 18).
- Both manuscripts use the same enumeration up to S ≤ 4800; the heat paper says so explicitly. The heat paper's count of 38 collision-free sums, the last being 557, is consistent with my enumeration.
- The heat paper summarises the note's Theorems B and C and states that no proof there depends on them.
- The descriptions are mutually consistent, including the model y² = x³ + 393x² + 3456x.

**"Finitely many eigenvalues determine the signature" (41 pp.)** cites the note only for context and has no mathematical overlap.

**Verdict.** The overlap is small, disclosed and acceptable. To avoid double publication of the one shared result, the note should present the Λ = 27/2 isolation explicitly as a corollary of its Theorem 1, as it now does, and not as a separate result.

## Editorial decision and recommendation

- **Editorial decision:** send to review (not desk-reject). The note is in scope for Integers, it is correct as far as I could check (extensively), and the enumeration is reproducible.
- **My recommendation:** major revision.
  - The literature positioning against Choudhry 2011 must be corrected (M1, M2).
  - The growth-fitting material must be reframed (M4).
  - The authors should either strengthen one of the bounds or scale down the claims (M3).
- **Confidence:**
  - correctness of what I checked: high;
  - the M1/M2 findings: high, since they are read directly from the published Choudhry paper;
  - the significance judgement: moderate. Referees in classical Diophantine analysis may value the organised account and the data more than I do.

Guidance for referees: please assess novelty against BGN (1993) and Choudhry (2011, §§4.1 and 5.1) specifically, and assess whether the dual-family order X (log X)⁵ is within reach.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Correct the "isosceles family does not appear" sentence. Cite Choudhry §4.1 (p. 748) in Corollary 1 and Theorem 2. Restate the novelty as the counting. |
| M2 | Cite Choudhry §5.1 (arbitrary-length integer chains of triples for −1, 1, 2) and §2 (positive solutions for large s). Restate Theorem C's novelty as positivity. |
| M3 | Prove X (log X)⁵ for the positive dual pairs, or n(S) = o(S²) or N(X) ≪ X^{3−δ}. Otherwise rewrite the abstract and introduction so the claims match the results. |
| M4 | Remove the fitted-exponent narrative and the "evidence for Question E" language, keeping the exact counts. |
| m1–m11 | Textual fixes as listed. |
| P1–P5 | Restructure §1.3–1.4, fix the notation, trim the abstract, and use or drop Figure 1(a). |
