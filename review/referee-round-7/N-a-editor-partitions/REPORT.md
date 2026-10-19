<!-- N-a editor (partitions), round 7: returned text saved verbatim; the reviewer could not write files -->

# Editor's report: "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

The write to `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/N-a-editor-partitions/REPORT.md` was refused, so the full report is below.

**Decision: send to review. Recommendation: major revision.** I found no mathematical error. Every proof I checked is right, and the data I could rerun (to S = 3000) matches exactly. The problems are four. Most of the torsion theorem is classical once the curve family is recognised as a modular one. The literature on equal sums with negative exponents is missing. The explicit constants in the lower bounds are artefacts of the proof. The curve-fitting section treats divisor structure as noise.

Handling editor (partitions; multiplicative problems and divisor-sum averages). The note has 19 pages. I read all of them as rendered images (pdftoppm, 110 dpi) and also in extracted text. As the brief says, the placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifier) are treated as known and not counted as defects.

## Summary

The note studies pairs, and more generally classes, of distinct triples of positive integers with the same sum S and the same reciprocal sum R. The motivation is that these are exactly the pairs of hyperbolic triangle orbifolds O(a,b,c) that share their first two heat invariants.

- **Lemma 1.** Every triple in a coincidence has R < 1.
- **Reduction to a cubic pencil.** Λ = SR does not change under scaling, so a class is a set of positive rational points on one cubic C_Λ : (x+y+z)(xy+yz+zx) = Λxyz. This is the Bremner–Guy–Nowakowski (BGN) curve, here taken over all rational Λ, and it is identified with Beauville's pencil with singular fibres I6, I3, I2, I1.
- **Proposition 3.** Taking reciprocals is translation by a point T2 of order 2. This gives a "dual family" (Corollary 1): every triple that is not a geometric progression yields a pair.
- **Theorem A (torsion).**
  - The torsion of C_Λ(Q) is Z/6, Z/12 or Z/2×Z/6, with explicit criteria.
  - For Λ > 9, the positive torsion points are exactly the isosceles triples and the geometric progressions, with their orders given.
- **Theorem B (lower bounds).**
  - N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X, from the isosceles part of the dual family.
  - N(X) ≥ (3/(128π⁴) + o(1)) X (log X)², from the full dual family.
- **Theorem C.** Classes of every size exist, by Schinzel's argument. The authors explicitly disclaim novelty here.
- **Proposition D.** n(S) ≪ S^{2+ε}.
- **Enumeration and Question E.** An exhaustive enumeration up to S = 6000 shows a local growth exponent falling from about 2 to 1.58, with curve fits. The paper asks whether N(X) = X^{1+o(1)}.

**What is good:**
- The mathematics is correct as far as I could check, and I checked a lot of it (see below).
- The note is honest about what is borrowed (Schinzel, BGN, Beauville).
- The proofs are short and complete, and the computations reproduce exactly.
- The torsion result has a pleasant feature with no analogue in the equal-product problem: geometric progressions are positive torsion points of order 4 and 12, and Z/12 actually occurs (for example on C_{49/4}).
- The problem is natural and squarely within the scope of Integers.

## Significance

- **Fit.** Good. This is elementary Diophantine analysis, elliptic-curve arithmetic and lattice-point counting, which is typical Integers material.
- **Novelty.**
  - Theorem C is Schinzel's argument, as the authors say.
  - Theorem A(i)–(iii) is classical once the pencil is recognised as the universal elliptic curve with a rational 6-torsion point (see M1).
  - Genuinely new:
    - Theorem A(iv), on the positive torsion points and their orders;
    - the counting function N(X), with its X log X and X(log X)² lower bounds;
    - the enumeration;
    - the observation that classes are common.
- **Strength.**
  - The lower bounds come from explicit rational families, by routine counting.
  - Proposition D gains only a factor S^{1−ε} over the trivial S³ bound and stays at the scale of the number of triples, as the authors concede.
  - The gap between X(log X)² and X^{3+ε} is enormous, and Question E is untouched.
- **Overall.** A correct, careful, modest note. That is enough for Integers, provided the novelty claims are recalibrated (M1, M2) and the quantitative statements are made honest (M3, M4).

## Correctness, and what I recomputed

All computations were my own code in `scratch/`: a C enumerator, Python with exact fractions, and PARI/GP 2.17.2 through cypari2 in a local virtual environment. I did not use the authors' repository.

**Checked by hand:**
- **Lemma 1 (p. 5).** All cases, including both discriminants.
- **Proposition 2 (pp. 5–6).**
  - The Weierstrass model: a² − 4b = (Λ−1)³(Λ−9), so Δ = 2¹²Λ²(Λ−1)³(Λ−9).
  - The invariant c4 is nonzero at Λ = 0, 1, 9.
  - The worked example: (1:4:4) at Λ = 27/2 maps to (−6, 45), which lies on the curve.
  - All five line intersections and the group of base points.
  - O is a flex.
- **Lemma 2.** The egg argument.
- **Proposition 3** and **Corollary 1.**
- **Theorem 1(iii).** Λ(1:r:r²) = (r+1+1/r)², and 2G = (0:1:−1) + T2.
- **Theorem 2.**
  - Area of the region Ω = (log 2)/6.
  - The residue-class bookkeeping, giving c_iso = 0.10534.
  - The partial summation.
- **Lemma 4** and **Theorem 3.**
  - The box inequality, which needs β ≤ α².
  - The error term O(M³√y log y) = o(y).
  - c_A = 3/(32π⁴), hence the final constant 3/(128π⁴).
  - 128π⁴c_iso/3 = 437.8.
- **Proposition 4.** The identity (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′.
- **Triangle substitution.** R/r = (Λ−1)/4.
- **Heat coefficient.** c2 = (S+R−2)/12, using the classical cone term (m²−1)/(12m).

**Exhaustive enumeration:**
- **Table 2 rows.** X = 18, 100, 200, 300, 400, 500, 600, 1000, 2000 and 3000 reproduce exactly in all four count columns (pairs, classes, primitive classes, largest class).
- **Local exponents** at X = 600, 1000, 2000, 3000, 4000 and 6000 follow from the tabulated N.
- **Lemma 1 numerically.** Allowing entries equal to 1, no coincidence with R ≥ 1 occurs up to S = 300.
- **Counts in the text, all confirmed:**
  - 1753 primitive pairs up to S = 600, of which 423 are dual.
  - The dual share is 32.9% for S ≤ 200.
  - 507 of the sums 19 to 600 carry a primitive class.
  - S = 36 has two classes.
  - The first classes of sizes 3, 4 and 5 are at S = 136, 408 and 1849, with exactly the members listed in Table 1.
  - The S = 4600 class has exactly six members (I did not check that it is the first class of size 6).
- **Internal consistency at 4800.**
  - Classes: 96981 + 1627 + 122 + 11 + 1 = 98742 = N_cl(4800).
  - Pairs: 96981 + 3·1627 + 6·122 + 10·11 + 15 = 102719 = N(4800).
- **Isosceles family.**
  - 506 pairs D_{u,v} with S ≤ 4800, against c_iso·4800 = 505.66.
  - 27 of them lie in classes of size at least 3.
  - The count of all multiples kD_{u,v} at X = 4800 is 0.6077X.
  - (c_iso X log X − count)/X = 0.2852, 0.2860, 0.2862, 0.2863, 0.2863, 0.2863 at X = 4800, 10⁴, 10⁵, 10⁶, 10⁷, 4·10⁷. This confirms "−0.286X to three digits".

**PARI/GP:**
- **Table 1 and C_{155/12}.** All Table 1 members lie on the curve. ellrank's lower and upper bounds coincide:

  | Λ | rank | torsion | root number |
  |---|---|---|---|
  | 27/2 | 0 | Z/2×Z/6 | +1 |
  | 68/5 | 2 | Z/6 | +1 |
  | 1849/120 | 3 | Z/6 | −1 |
  | 230/21 | 3 | Z/6 | −1 |
  | 155/12 | 2 | Z/6 | +1 |

- **Z/12 example.** C_{49/4} has torsion Z/12. The orderings of (1,2,4) have orders 12, 12, 12, 4, 4, 12. In particular 3G = (1:4:2) and 9G = (4:1:2) have order 4, exactly as Theorem 1(iv) says.
- **C_{27/2}.** (1:4:4) and (4:1:4) have order 6, and (4:4:1) has order 2.
- **The point P = (4:9:18) on C_{155/12}.**
  - It has infinite order.
  - 3P = (162833463 : 723926268 : 287876366).
  - P + T2 = (9:4:2).
- **Non-dual pairs.**
  - For all 1330 non-dual primitive pairs with S ≤ 600, both P′−P and P′+P have infinite order.
  - None of the 669 with S ≤ 400 satisfies a relation P′ = ±mP + T with m ∈ {2,3}.

**Not verified:**
- Table 2 rows 4000, 4800 and 6000.
- "No class of size 7 up to 6000".
- The individual Selmer groups (the arithmetic 2^{r+2} = |Sel||Sel| is consistent with the ranks).
- The search over 189 lines.
- The bootstrap and likelihood figures.

**No mathematical error found.**

## FATAL

None.

## MAJOR

**M1 (pp. 1, 3, 5–9). The modular interpretation is missing, and with it most of the novelty of Theorem A(i)–(iii).**

The pencil (x+y)(y+z)(z+x) + t·xyz = 0 is Beauville's elliptic modular surface for Γ0(6), which equals ±Γ1(6) in PSL2(Z). Top and Yui list it under exactly that name: J. Top and N. Yui, *Explicit equations of some elliptic modular surfaces*, Rocky Mountain J. Math. 37 (2007) 663–687, Table 2; arXiv:math/0307230. So C_Λ is the universal elliptic curve with a rational point of order 6, and the six base points are that Z/6.

The extra torsion is then governed by the genus-0 covers X1(12) → X1(6) (degree 4) and X1(2,6) → X1(6) (degree 2). This is classical; see Kubert, Proc. London Math. Soc. (3) 33 (1976) 193–237, Table 3. The paper's own formulas show it:
- The degree-4 map r ↦ (r+1+1/r)² factors through Λ = w². That is Top–Yui's Γ0(12) cover t = 1 − s², since t = 1 − Λ (p. 5).
- The condition "(Λ−1)(Λ−9) is a square" is the degree-2 cover giving full 2-torsion.

The elementary proofs can stay. But the abstract ("We determine the torsion") and §1.4 present this as new.

**Fix:**
1. Identify C_Λ as the universal curve over X1(6), citing Beauville [1], Top–Yui and Kubert.
2. Label (i)–(iii) as classical in elementary form.
3. Claim (iv) and the positive-locus description as new.
4. Revise the abstract.

**M2 (p. 4, §1.4). The literature is incomplete.**

The problem is the three-term case of equal sums of like powers with exponents −1 and 1. Four gaps:

- **(a) Negative-exponent equal sums.**
  - A. Choudhry, *Equal sums of like powers, both positive and negative*, Rocky Mountain J. Math. 41 (2011) 737–763, appears from its title to treat exactly such systems. I could not retrieve the full text without a browser. The authors must check whether it contains parametric solutions coinciding with Corollary 1 or Theorem 2.
  - The same check is needed for Chen's survey of the Prouhet–Tarry–Escott problem (arXiv:2506.11429). The authors cite it in the disclosed heat manuscript but not here.
- **(b) The four-variable analogue.** Y. Zhang, arXiv:1608.03382, should be cited alongside [4].
- **(c) The partition reading.** n(S) counts pairs of partitions of S into three parts with equal reciprocal sums. The equal-product papers cited ([5], [10], [21]) use the word "partitions" throughout. The reciprocal-sum side has its own line:
  - Graham (1963), on partitions with prescribed reciprocal sum;
  - van Doorn, arXiv:2502.02200 and arXiv:2502.01409 (2025).

  A title or subtitle mentioning partitions into three parts would help readers find the note.
- **(d) A triangle reformulation that should be stated.** Using the substitution the paper itself gives on p. 4, (a,b,c) = (y+z, z+x, x+y), a coincidence is exactly a pair of integer triangles with the same even perimeter 2S and the same ratio R/r of circumradius to inradius. The triangle literature on R/r (MacLeod [11] and papers citing it) should be searched.

**Fix:**
1. Read and cite Choudhry and Chen, and state precisely what they contain about this system.
2. Add Zhang, Graham and van Doorn.
3. State the triangle equivalence.
4. Narrow the "As far as we know … are new" sentence.

**M3 (pp. 3, 11–12, 15). The quantitative results are weak, and the explicit constants are artefacts of the proof.**

- **Theorem 3's constant 3/(128π⁴) has no intrinsic meaning.**
  - A factor 2 is lost in ⌊X/S_D⌋ ≥ X/(2S_D). Restricting to S_D ≤ X/log X loses nothing in the main term.
  - A factor 8/6 is lost by taking M = y^{1/8}, when any M = y^{1/6−δ} works.
  - Further losses come from the multiplicity bound 6 and from keeping only boxes.
- **The comparison is meaningless.** "The second bound exceeds the first only when log X > 438" (pp. 3 and 12) therefore says nothing about the problem.
- **The data point the other way.** The authors' own fit for primitive dual pairs (q ≈ 2.56 per sum, p. 16) suggests that the dual family alone grows like about y(log y)^{2.5}, well above the proven y log y. The loss is the gcd cancellation ignored after Lemma 4. Finding the true order of the dual-family count is a concrete counting problem for one explicit rational surface. It is within reach and would materially strengthen the note.
- **Proposition D** is at the trivial scale: at most S^ε solutions for each of the O(S²) pairs (p, p′). It does not merit headline status.

**Fix:**
1. State the second bound of Theorem B as ≫ X(log X)², or optimise the constant.
2. Drop the 438 comparison.
3. Demote Proposition D to a remark, or improve it.
4. Preferably, determine the order of the dual-family count, gcd cancellation included.

**M4 (pp. 15–16, §6.3). The per-sum fits are misspecified.**

By Lemma 3 applied sum by sum, n(S) = Σ_{d|S} n_prim(S/d). So n is a Dirichlet convolution with 1, and its fluctuations follow the divisors of S. I measured this on 600 ≤ S ≤ 1500. The ratio of n(S) to its 51-term moving average:
- has correlation 0.67 with σ(S)/S (σ the sum of divisors);
- averages 1.49 on multiples of 6;
- averages 1.12 on even S not divisible by 6;
- averages 0.66 on S coprime to 6.

So the reported "overdispersion 6.8" is mostly deterministic structure. A Poisson likelihood and a block bootstrap over consecutive sums treat it as noise. As a result:
- the quoted errors (±0.06 and the like) do not measure sampling noise;
- the likelihood comparison ("lower by 9.5 … scaled difference 1.4") cannot be interpreted.

**Fix:**
1. Fit primitive counts and recover all-pair counts by convolution, equivalently using Σ n(s)s^{−w} = ζ(w)·Σ n_prim(s)s^{−w}.
2. Otherwise drop the error bars and the model comparison and keep the exact counts of Table 2, which are the solid part.

## MINOR

- **m1 (p. 2).** [8] has an erratum: Michigan Math. J. 66 (2017) 221–222. Check and cite it. I expect no effect, since the cone term is classical and I reproduced (S+R−2)/12 independently.
- **m2 (p. 5, Proposition 1).** "Pairwise non-proportional" must mean as unordered triples. Otherwise (1,4,4) and (4,1,4) satisfy the hypothesis but rescale to the same triple, and the claim "they are distinct" fails.
- **m3 (p. 6, Proposition 2).** State where the birational maps are undefined. Also state that O ↦ ∞ and T2 ↦ (0,0); Section 3 relies on the latter when matching BGN's "(0,0)".
- **m4 (p. 8).** The paragraph on how permutations and ι act is used as a lemma in the proof of Theorem 1(iv) (p. 9: "By the description … above"). Make it a numbered lemma with proof.
- **m5 (p. 8).** Mazur's theorem is not needed. Theorem 1 already gives the torsion subgroup, so it suffices that P′ ∓ P is not one of its at most 12 elements.
- **m6 (pp. 9–10, Remark 1).** This is an imprecise sketch, yet it is used on p. 16 ("Remark 1 rules out d = 1"). Prove it as a lemma or remove both uses.
- **m7 (p. 11).** The secondary constant −0.286 is reported empirically; I confirm 0.2860–0.2863. It can be computed in closed form (it involves γ, ζ′(2)/ζ(2) and the shape of Ω). Derive it, or call it numerical.
- **m8 (p. 13).** Give the integral model and the isogeny φ explicitly, so the Selmer orders can be checked.
- **m9 (p. 14).** Say why only m ∈ {2,3} is tested, and what a positive instance would have meant.
- **m10 (p. 17).** Define the 189 lines precisely (normalisation, what "up to permutation and sign" identifies). Explain "one Vieta involution on each line through a vertex".
- **m11 (pp. 17–18).**
  - Say which hypotheses of Schoen's Proposition 7.1 hold here; the singular fibres coincide over all four points.
  - Check whether this threefold is among the rigid Calabi–Yau self-fibre products of Beauville surfaces studied by Schoen and by Verrill (J. Number Theory 81 (2000) 310–334).
  - Frame Question E in the Batyrev–Manin / Lang–Vojta picture. For a Calabi–Yau threefold with the O(1) height, a(L) = 0, so one expects few points outside accumulating subvarieties: rational surfaces and curves, and positive-rank fibres. This is what the heuristic on pp. 16–17 is reaching for.
- **m12 (p. 4).** The attributed "expectation of Bremner, Guy, and Nowakowski" concerns the four-variable equation. Give a page reference.
- **m13 (pp. 3, 16).** N(X) includes all scaled copies. Also state Question E for the primitive count A(y): N(X) = X^{1+o(1)} if and only if A(y) = y^{1+o(1)}.

## Presentation

- **P1. Notation clashes.**
  - R is the reciprocal sum, also the third intersection point in the proof of Proposition 3 (p. 7), and implicitly the circumradius (p. 4).
  - s is both the Weierstrass coordinate and the summation variable in n(s).
  - T denotes torsion points.
  - N is both MacLeod's integer and the counting function N(X).
- **P2. Double numbering.** Theorems A–E alongside Theorems 1–4 and Propositions 1–4 make cross-references heavy. Use one scheme.
- **P3. Proofs and data interleaved.** "We checked how they differ for small sums" (p. 8) sits inside the structural discussion. Move it to Section 6 or a marked remark.
- **P4. Figure 1 (p. 17, checked on the rendered page).**
  - The caption does not say which colour marks which permutations.
  - In panel (b) the dashed fit lies under the heavy curve and cannot be seen.
  - The split marker is explained only in the text.
  - Panel (a) itself is correct.
- **P5. §6.1.** The provenance of the three programs belongs in the data statement. The grouping method and the exactness argument are sound.
- **P6. Heuristic labels.** Label heuristic material uniformly, so readers can separate proved from conjectural statements.
- **Typesetting.** No typographical, sign or figure errors on the rendered pages. The "withsum" and the garbled abstract fractions appear only in extracted text, not in the PDF.

## Overlap with the disclosed manuscripts

**Heat manuscript ("How much of a hyperbolic orbifold does heat hear?").**
- **What overlaps.**
  - Its Theorem 5.8 and §5.2 re-prove that C_{27/2} has rank 0 and torsion Z/2×Z/6. They use the model y² = x(x+9)(x+384) and a hand 2-isogeny descent.
  - They also repeat this note's set-up: scale invariance, the curve C_Λ, and BGN's reciprocal pairs.
  - Its enumeration up to 4800 is described as "the same computation".
  - The note acknowledges this on p. 13.
- **Consistency.** The two papers agree.
  - The models are related by s = x/4, η = y/8; for example (−24, 360) ↔ (−6, 45).
  - Both use the same c2 formula.
  - Its list of collision-free sums matches my enumeration: 38 such sums up to 1000, the first being 19 and 21–25, the last being 557.
  - It quotes Theorems B and C correctly. However, it quotes only the X(log X)² bound, which by the note's own remark is the weaker one for every practical X. It should quote both.
- **Verdict.** The overlap is disclosed and modest, not duplicate publication of a main result. Editorially:
  - the enumeration should have one canonical home, presumably this note;
  - the rank-0 result for C_{27/2} should be proved in one paper and cited in the other.

**Eigenvalue manuscript.** It cites the note only for context. There is no overlap of results.

## Editorial decision and recommendation

- **Decision: send to review, not a desk reject.** The paper fits Integers, it is correct, and it is reproducible. Its weaknesses are framing, literature and strength, not validity.
- **Recommendation: major revision.**
  - Confidence in the correctness assessment: about 0.9. I checked almost every proof step and reproduced the data and curve invariants up to S = 3000.
  - Confidence in the recommendation: about 0.7. If Choudhry (2011) or Chen's survey already contains the dual or isosceles families, the novelty would rest on Theorem A(iv), the counting set-up and the data. A referee could then justifiably recommend rejection, even at Integers. Otherwise a revision addressing M1–M4 is likely acceptable.
- **Referees.**
  - One in elliptic curves and Diophantine equations, for M1, M2(a) and the Selmer computations.
  - One in analytic or combinatorial number theory, for M3, M4 and the counting proofs.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Identify C_Λ as the universal curve over X1(6) (Beauville; Top–Yui 2007, Table 2). Cite Kubert 1976 for the Z/12 and Z/2×Z/6 subfamilies, and note that Λ = w² is the Γ0(12) cover. Mark (i)–(iii) as classical, claim (iv) as new, and revise the abstract. |
| M2 | Read and cite Choudhry (2011) and Chen's survey, and state exactly what they contain. Add Zhang (arXiv:1608.03382), Graham (1963) and van Doorn (2025). State the equal-perimeter, equal-R/r triangle equivalence. Narrow the novelty sentence. |
| M3 | Restate Theorem 3 as ≫ X(log X)², or optimise the constant. Delete the 438 comparisons (pp. 3, 12). Demote or improve Proposition D. Preferably determine the order of the dual-family count. |
| M4 | Re-model through primitive counts and n = 1 * n_prim, or drop the error bars and likelihood comparison and keep the exact counts. |
| m1–m13 | Make the specific corrections listed above (erratum; unordered triples; map domains; numbered lemma; drop Mazur; Remark 1; secondary constant; isogeny model; m ∈ {2,3}; line search; Schoen, Verrill and Batyrev–Manin; BGN page; primitive version of Question E). |
| P1–P6 | Fix the notation, numbering, figure caption and labelling as listed. |
| Overlap | Make this note the canonical source for the enumeration. Prove the C_{27/2} rank-0 result in one paper and cite it in the other. Quote both bounds of Theorem B in the heat manuscript. |

Everything is in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/N-a-editor-partitions/scratch/`:
- `code/` holds the computations: `enum.c`, `enum2.c`, `dump.c`, `curves.py`, `cfun.py`, `tors.py`, `iso.py`, and the outputs `enum3000.txt`, `perS.txt`, `prim600.txt`.
- `pages/` holds the rendered pages.
- `lit/` holds the fetched literature.
