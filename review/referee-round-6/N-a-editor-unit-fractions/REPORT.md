<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Editor's report: "Triples with equal sum and equal reciprocal sum" (submitted to *Integers*)

## Summary

The note studies unordered triples of positive integers {a, b, c} with R = 1/a + 1/b + 1/c < 1 ("admissible") that share both their sum S and their reciprocal sum R with another such triple. The motivation is spectral: these are the pairs of hyperbolic triangle orbifolds that the first two heat invariants do not distinguish. The smallest case is {(2,8,8), (3,3,12)}.

The note does five things.

1. **The curves.** Following Bremner–Guy–Nowakowski (BGN), it recalls that a class of coincident triples is a finite set of positive rational points on one member C_Λ : e1e2 = Λe3 of the Γ1(6) Beauville pencil, now for rational Λ = SR (Props. 2–3, Lemma 1).
2. **Reciprocation and the dual family.** It shows that reciprocation is translation by the 2-torsion point (0:0:1) (Prop. 4). This gives an explicit "dual" partner for every triple that is not a geometric progression (Cor. 1).
3. **Lower bounds.** N(X) is the number of coincident pairs with sum at most X, and N_cl(X) the number of classes. The note proves N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X from the isosceles family (Thm 3), and N(X) ≥ (3/(128π⁴) + o(1)) X (log X)² from a conic-bundle subfamily of the dual family (Thm 4).
4. **Classes of every size and an upper bound.** Schinzel's equal-sum/equal-product argument, transplanted to C_{155/12}, gives classes of every size (Thm 5). No novelty is claimed for the method. An elementary divisor-counting bound gives n(S) ≪ S^{2+ε} and N(X) ≪ X^{3+ε} (Prop. 5).
5. **Enumeration and conjecture.** An exhaustive enumeration up to S = 6000 (Tables 1–2), log-power fits and a heuristic section lead to the conjecture N(X) = X^{1+o(1)}.

The note is careful, honest about what is borrowed, and (as far as I could check) correct. The question is whether the new content (two elementary counting lower bounds, a weak upper bound, and data) is enough for *Integers* as it stands.

## Significance

**What is good.**
- The counting question is natural and, as far as I can find, new. Bremner–Guy–Nowakowski, Nguyen Xuan Tho and Bremner–Nguyen Xuan Tho all ask *which* Λ occur, not *how often* coincidences occur.
- Prop. 4 gives a clean plane-model proof that reciprocation is a 2-torsion translation. It turns BGN's remark into a usable tool (Cor. 1), and Cor. 1 drives the lower bounds.
- The lower bounds are proved completely, with explicit constants that I could reproduce.
- The enumeration is large, exact and cross-checked. I reproduced it independently in full (see below).
- Attribution is scrupulous: BGN, Beauville and Schinzel are credited exactly where their work is used.
- *Integers* is the right venue: the subject is the reciprocal-sum analogue of Guy's D16, and the tools are elementary.

**Why the significance is limited.**
- The mathematical depth is modest. Theorems 3 and 4 count lattice points in explicit rational families. Theorem 5 is Schinzel's argument verbatim, which the authors say themselves. Proposition 5 is a one-line divisor bound.
- Theorem 4's extra logarithm is purely asymptotic. Its constant, 3/(128π⁴) ≈ 2.41 × 10⁻⁴, beats Theorem 3's bound c_iso X log X only when log X > 438, that is X > 10^190.
- The upper bound X^{3+ε} sits essentially at the trivial scale. The number of admissible triples with sum ≤ X is ≍ X³, so Prop. 5 does not even show that coincidences are rare, i.e. that N(X) = o(X³), or that almost all triples have no partner. The data make that statement look obvious and it is the first thing a reader would want.
- The true exponent is left between 1 and 3. The conjecture rests on about 1.6 decades of data (see M3).

This is an acceptable *Integers* note if the literature is completed and the upper-bound side is strengthened or the claims are recalibrated. In its current form it is a borderline paper.

## Correctness and what was recomputed

**Checked from rendered pages.** I read every page as rendered at 110 dpi. In particular I checked:
- p. 2: the heat-coefficient formula, which correctly has (m_i² − 1)/(12 m_i);
- p. 3 and p. 5: the Beauville row;
- pp. 8–10: the counting displays;
- pp. 11–12: Tables 1 and 2;
- p. 14: Figure 1.

All computations below are my own. I used C, Python/sympy, and PARI/GP 2.17.2 via cypari2 in a scratch virtual environment.

**Recomputed and confirmed.**
- **§1.1:** χ/6 + Σ(m_i² − 1)/(12 m_i) = (S + R − 2)/12 with χ = R − 1, and area 2π(1 − R).
- **Prop. 3:**
  - (x+y)(y+z)(z+x) = e1e2 − e3.
  - Both birational maps C_Λ ↔ E_Λ were checked symbolically: the image of each lies on the target, and the round trip at Λ = 27/2 works.
  - (Λ² − 6Λ − 3)² − 64Λ = (Λ−1)³(Λ−9), hence Δ = 2¹²Λ²(Λ−1)³(Λ−9). The fibre types I2, I3, I1 at Λ = 0, 1, 9 (c4 ≠ 0 there) and I6 at ∞ are consistent.
  - (1:4:4) ↦ (s, η) = (−6, 45).
  - With O = (1:−1:0), I implemented the exact chord-and-tangent law on the plane cubic. The base points (0:0:1), (0:1:−1), (1:0:−1), (1:0:0), (0:1:0) have orders 2, 3, 3, 6, 6.
- **Lemma 1:** the argument is sound.
- **Prop. 4:**
  - P + T2 = ι(P) holds on C_{27/2}, C_{155/12} and C_{68/5}.
  - The three transpositions act as P ↦ Q − P with Q = O, (1:0:−1), (0:1:−1), and the cyclic shift is translation by (1:0:−1). This confirms the unproved paragraph on p. 7.
- **Remark 1:** Λ − 1 = 2(u+v)²/(uv) and Λ − 9 = 2(u−v)²/(uv) for (u:v:v).
- **Remark 2:**
  - (1:4:4) has order 6 with 2P = (1:0:−1).
  - Among the **40 305** primitive triples ≠ (1,1,1) with sum ≤ 120 (count confirmed), every torsion point is isosceles or a geometric progression. I checked this with PARI `ellorder` after mapping to E_Λ: 2212 torsion points, no exceptions.
- **Cor. 1:** (1,4,4) ↦ {(2,8,8), (12,3,3)}.
- **§3, p. 7:** I confirm **1753** primitive pairs with S ≤ 600, of which **423** are dual. For each of the other 1330, both P′ − P and P′ + P have infinite order (PARI `ellorder` = 0). The share of dual pairs at S ≤ 200 is 82/249 = 32.9%.
- **Theorem 3:**
  - Algebra, primitivity and g ∈ {1, 3} all check.
  - |Ω| = (1/6) log 2 and c_iso = 3 log 2/(2π²) = 0.105346.
  - A_iso(4800) = 506, against 505.7.
  - A_iso(10⁷) = 1 053 444, against c_iso · 10⁷ = 1 053 457.
  - The count of copies kD_{u,v} with k ≥ 4, minus c_iso X log X, divided by X, is −0.4793, −0.4793, −0.4794, −0.4794, −0.4794 at X = 10⁴, 10⁵, 10⁶, 10⁷, 4 × 10⁷. This confirms "−0.479X to three digits".
- **Lemma 3 / Theorem 4:**
  - The displayed pair, the multiplicity 6 and the geometric-progression exceptions all check.
  - The box estimate Q ≤ y uses β/α ≤ α, which holds.
  - The error terms and the constants 3/(2π²) · 3/π² · (1/6) · (1/8) = 3/(32π⁴), and then (c_A/2)(1/2) = 3/(128π⁴), are all correct.
- **Theorem 5:**
  - P = (4:9:18) lies on C_{155/12}, and nP ≠ O for n ≤ 12.
  - 3P = (162833463 : 723926268 : 287876366), exactly as printed.
  - Odd multiples are positive and even ones are not (checked to 5P).
- **Ranks (PARI `ellrank` on the minimal models; r1 = r2 in every case):**

  | Λ | Conductor | Torsion | Rank |
  |---|---|---|---|
  | 27/2 | 90 | Z/2 × Z/6 | 0 |
  | 68/5 | 82110 | Z/6 | 2 |
  | 1849/120 | — | Z/6 | 3 |
  | 230/21 | — | Z/6 | 3 |
  | 155/12 | — | Z/6 | 2 |

  All as claimed. The Λ = 27/2 row agrees with LMFDB 90.c3 as stated in the companion.
- **Table 1:** every listed class has the stated sum, a common R, Λ = SR as printed, and gcd 1. My enumeration finds the same first classes of sizes 2–6 at S = 18, 136, 408, 1849, 4600, with identical members, and no class of size 7 up to S = 6000.
- **Prop. 5:** the identity (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′ follows from the equation, and the argument is correct.
- **§6.1:** the total 3 067 197 199 of admissible triples with S ≤ 4800 is confirmed both by a closed formula and by my enumeration. The "correctly rounded double" hashing argument is valid since e2, e3 < 2⁵³.
- **Table 2 and the counts of §6.1:** I re-enumerated all admissible triples with S ≤ 6000 independently, using C with exact 128-bit comparison. Every entry of Table 2 is reproduced exactly:
  - pairs, classes, primitive classes and largest class size in all 13 rows;
  - the local exponents, e.g. 2.5236, 2.0689, 1.9935 (so "1.993" at S = 500 is correctly rounded), 1.6026 and 1.5845.
  
  The counts in the text are reproduced too:
  - the class-size histogram to 4800 (96 981 / 1627 / 122 / 11 / 1);
  - 46 254 primitive pairs at 4800, of which 7626 (16.5%) are dual;
  - 507 of the 582 sums 19 ≤ S ≤ 600 carry a primitive class;
  - N(S)/S² = 0.00935 at S = 400 and 0.00405 at S = 6000.
  
  The same run gives exactly 38 collision-free sums in 18 ≤ S ≤ 4800, the last being 557, as claimed in the companion's Prop. S2.1.
- **Cited literature claims:** a brute-force search (a ≤ b ≤ 700) found no triple with e1e2/e3 = n for any n ≡ 0 (mod 4) in 12 ≤ n ≤ 60, consistent with the cited theorem of Nguyen Xuan Tho.

**Not checked.**
- The "independent 2-isogeny descents".
- The search over "189 lines" in §6.4.
- The bootstrap fits of §6.3.
- The "669 non-dual pairs, m ∈ {2, 3}" statement.

None of these is load-bearing for a theorem.

**Conclusion on correctness.** I found no mathematical error in any theorem, proposition, lemma or reported number that I checked.

## FATAL

None. No main statement is false, no proof has a gap that cannot be closed, and the work is not a duplicate of published work.

## MAJOR

**M1 (Significance of the bounds; Thm 1, Thm 4 p. 9–10, Prop. 1/Prop. 5 p. 12).** The results do not locate the growth of N(X) to within a power. The note proves X log X and X(log X)² below and X^{3+ε} above, so the exponent is somewhere in [1, 3].
- **The upper bound is too weak to say anything.** Since there are ≍ X³ admissible triples with sum ≤ X, Proposition 5 does not imply that a vanishing proportion of triples have a partner. That is, it does not give n(S) = o(S²) or N(X) = o(X³), which the data (N(S)/S² falling from 0.0094 to 0.0040) make look true and which is the obvious first theorem on the upper side.
- **Theorem 4 is presented as "one more logarithm" without its fine print.** Its bound exceeds Theorem 3's only for X > 10^190. That should be said, and the abstract should not lead with it.
- **Requested:**
  - Either prove a non-trivial upper bound: N(X) ≪ X^{3−δ}, or at least n(S) = o(S²). One possible route: in the proof of Prop. 5, use that both discriminants A² − 4B and A′² − 4B′ must be squares, and average the divisor function over (p, p′).
  - Or prove an asymptotic, not just a lower bound, for the dual family, which carries 16–33% of the pairs.
  - Failing either, recalibrate the claims in the abstract and introduction, so that the note presents itself as a study of explicit families plus data.

**M2 (Literature and novelty; §1.4 p. 3–4, §6.4 p. 14).** The novelty claim ("As far as we know, the counting function N(X), the bounds … and the enumeration are new") needs a fuller search. The following are directly relevant and are not cited:
- **(a) Equal sums of power sums including exponent −1.**
  - A. Choudhry, "Equal sums of like powers, both positive and negative", *Rocky Mountain J. Math.* 41(3) (2011) 737–763. From its title this treats systems Σx_i^k = Σy_i^k for positive and negative k. I could not retrieve the full text, so the authors must check whether k ∈ {1, −1} with three terms, or a parametric solution of it, appears there.
  - M. Ulas, "A note on Diophantine systems involving three symmetric polynomials" (arXiv:1305.6241). Its abstract states that for each k there are at least k n-tuples with equal sums of i-th powers for i = −1, 1, 2. This is a "classes of every size" result for a system containing the reciprocal sum, and is directly comparable to Theorem 2/Theorem 5.
  - M. Ulas, "On some Diophantine systems involving symmetric polynomials", *Math. Comp.* (arXiv:1305.6237).
- **(b) The equal-sum/equal-product side, the comparison the authors themselves draw.**
  - G. Moreland and M. E. Zieve, "Some Diophantine equations related to positive-rank elliptic curves" (arXiv:1304.1442).
  - B. Cha et al., "An investigation on partitions with equal products", *Int. J. Number Theory* (2018). This is the nearest *counting-type* study of the analogue (see also OEIS A316945–A316946, A334911).
- **(c) The same pencil in another guise.** For the Ravi substitution a = y+z, b = z+x, c = x+y, a triangle's ratio R/r of circumradius to inradius equals (x+y)(y+z)(z+x)/(4xyz) = (Λ − 1)/4. So integer triangles with R/r = N are exactly the positive points of C_{4N+1}. See A. J. MacLeod, "Integer triangles with R/r = N" (arXiv:math/0502475), and the recent Halbeisen–Hungerbühler–Zargar paper in *Indag. Math.* (2026) on rational circumradius-to-exradius ratios. These belong in §2.
- **(d) The threefold of §6.4.**
  - The self-fibre product of Beauville's semistable Γ1(6) surface is a well-studied rigid Calabi–Yau threefold, and its L-function has been computed. See H. Verrill, "The L-series of certain rigid Calabi–Yau threefolds", *J. Number Theory* 81 (2000) 310–334; M.-H. Saito and N. Yui, *J. Math. Kyoto Univ.* 41 (2001); and C. Meyer's book on modular Calabi–Yau threefolds. Citing Schoen alone undersells what is known.
  - It is also worth saying explicitly that the variety of pairs is the quintic threefold {e1(x) = e1(x′), e2(x)e3(x′) = e2(x′)e3(x)} ⊂ P⁴ (a hyperplane section of P⁵). That makes the Calabi–Yau nature, and the relevance of Batyrev–Manin-type heuristics with accumulating rational curves and surfaces, transparent. It is the natural frame for Conjecture 1.
- **Also:** please check whether Guy's *Unsolved Problems in Number Theory* records the reciprocal-sum analogue of D16.

**M3 (Evidence for Conjecture 1; §1.3 p. 3, §6.3–6.4 p. 13–14).** The data cover 600 ≤ S ≤ 6000, about 1.6 decades.
- **The fits cannot tell the competing laws apart.** On [600, 4800], (log s)^{4.48} grows by a factor of 3.53 and s^{0.60} by a factor of 3.48. So the fitted n(s) = c(log s)^q is numerically indistinguishable from n(s) ≍ s^{0.6}, i.e. from N(X) ≍ X^{1.6}.
- **The heuristic of §6.4 does not discriminate either.** It only shows what *kind* of subvariety would violate the conjecture, and the authors have "not searched for one".
- **Requested:**
  - Either downgrade Conjecture 1 to a question;
  - or give a real heuristic for the exponent 1, e.g. a Batyrev–Manin-type count on the quintic Calabi–Yau threefold (M2(d)) with an argument that the accumulating subvarieties are conics and conic bundles only;
  - and state in the abstract that the local exponent is still 1.58 at X = 6000.

**M4 (Self-containment and dependence on an unpublished companion; p. 2, Table 1 p. 11).** The note says nothing depends on [8], but two things do.
- **The smallest coincidence.** The introduction asserts that {(2,8,8), (3,3,12)} is the smallest coincidence and points to [8].
- **Table 1, row k = 2.** The rank entry is "[8]".

Both are trivially self-supportable:
- minimality follows from the note's own enumeration (or a two-line strata argument);
- C_{27/2} is LMFDB curve 90.c3, which has rank 0 and torsion Z/2 × Z/6 (I confirmed this with PARI: conductor 90, r1 = r2 = 0).

Replace the citations of an unrefereed manuscript by these. The rank column is in any case not used by any proof. Either say why it is reported (e.g., to contrast torsion-generated and rank-generated classes, Remark 2) or drop it.

## MINOR

- **m1 (p. 3 §1.3; p. 5 Prop. 3).** "the row Γ_0^0(6) of his table" should read Γ1(6) unless the authors can show that Beauville prints Γ_0^0(6). The elliptic modular surface of a Beauville family has Euler number 12, which equals the index of ±Γ1(6) in PSL2(Z) and matches the fibre configuration I6, I3, I2, I1. Γ_0^0(6) = Γ0(6) ∩ Γ^0(6) is conjugate to Γ0(36), of index 72.
- **m2 (p. 7, Remark 2).** "order 3 would make it a base point" uses the fact that E_Λ(Q) has a unique subgroup of order 3. Say why: Z/3 × Z/3 is impossible over Q, either by the Weil pairing (μ3 ⊄ Q) or by Mazur.
- **m3 (p. 7, paragraph after Cor. 1).** The description of transpositions as P ↦ Q − P and of cyclic shifts as translations by 3-torsion is stated without proof. It is true (I verified it), but give the one-line reason. A linear automorphism of C_Λ fixing O is ±1; x ↔ y fixes O and acts as −1; the rest follows by composing with the 3-cycle. Alternatively, cite BGN's table.
- **m4 (p. 7, Remark 3).** The partial-fraction argument is a sketch. In the affine one-parameter case an entry can be constant, so it has no pole. The mismatched cases then also include a constant entry against two constants. The same AM–HM contradiction applies, but the proof should list the cases or be relabelled as a sketch.
- **m5 (p. 9, Thm 3 proof).** The partial-summation display starts the integral at 18 and silently absorbs the k ≤ 3 terms into O(X). Say so.
- **m6 (pp. 9–10, Thm 4).** State the crossover (X > 10^190) right after the theorem (see M1).
- **m7 (p. 14, Fig. 1(b) and p. 13 last sentence of §6.3).** The thin curve is described as "the isosceles lower bound of Theorem 3". It is not: the curve plotted is the count of *all admissible* copies kD_{u,v}, k ≥ 1.
  - The k ≥ 4 count used in Theorem 3 is 0 at S = 18 and 0.438·S at S = 6000.
  - The plotted thin curve starts at 1/18 ≈ 0.056 (the single pair (2,8,8), (3,3,12)) and ends near 0.63, which matches my count of 3781 admissible isosceles copies with S ≤ 6000.
  
  Fix the caption and text, or plot the Theorem 3 quantity.
- **m8 (p. 14, Fig. 1(a)).** The caption does not say which colour marks the permutations of (1,4,4) and which those of (1,1,4).
- **m9 (p. 12, Table 2).** The first column is the cumulative bound S, but the headings write N(S), N_cl(S). With n(S) defined per sum, this invites confusion; use X. "Largest class" should read "largest class size so far".
- **m10 (p. 13, §6.3).** Fraktur 𝔮 versus a in the next paragraph: one symbol should be used for the same exponent. Also say explicitly that "per sum" means a fit to n(s) and "cumulatively" means a fit to N.
- **m11 (p. 4, §1.4).** Sadek–El-Sissi is cited for "a mild condition". State the condition.
- **m12 (p. 10, §5).** "an independent 2-isogeny descent gives the same rank". If these descents are not printed or archived, say where they are.
- **m13 (p. 11, §6.1).** "Two independent programs … agree on every count up to S = 4800. A third enumeration gives … up to 6000." Give the run time and memory, and state which program produced which published number. The Data statement partly does this.

## Presentation

- **P1 (p. 1, Abstract).** It is too long and technical for an *Integers* abstract.
  - "gives the counts in both conventions" is undefined there.
  - The displayed asymptotics lead with the X(log X)² term, which is the weaker statement for every practical X.
  
  Shorten it. State the bounds as orders of growth and say the conjecture is an extrapolation.
- **P2 (p. 14–15, "Statements and Declarations").** The Funding / Competing interests / Data / Author contributions / AI-use block is publisher-style rather than *Integers* style. *Integers* uses a plain Acknowledgements paragraph. Move the data-availability sentence there, and drop the list of internal script names (`make_tables.py`, `F9.py`, …); the archive's README is the place for them. (The placeholders themselves are noted and not held against the paper.)
- **P3 (p. 3).** Theorem 1 and Proposition 1 duplicate Theorems 3–4 and Proposition 5 under different numbers. In a note of this size, state the results once, or label the introduction statements as Theorem A/B.
- **P4 (§6.4).** Separate proved statements, computations and heuristics typographically, e.g. label the heuristic paragraphs "Heuristic".
- **P5 (p. 2).** The motivation paragraph is good, but the heat-kernel constant-term formula should cite the exact proposition in Dryden–Gordon–Greenwald–Webb, not only the display number.
- **P6.** The authors' affiliations (several school addresses) are fine. The note would benefit from naming one corresponding author.

## Overlap with the related manuscripts

**Related manuscript 1, "How much of a hyperbolic orbifold does heat hear?" (47 pp. + 19 pp. supplement).**
- **Overlap.**
  - Its §5.2 contains the reduction "collision ⇒ positive rational points on C_Λ", the scale invariance of Λ, and the reciprocal-pair remark: the content of the note's Prop. 2 and the first lines of §3, stated without the note's proofs.
  - It proves the isolation theorem for C_{27/2} (its Thm 5.8, with a hand 2-isogeny descent in Supplement S7).
  - It reports results computed from **the same enumeration** to S = 4800: the 38 collision-free sums of its Proposition S2.1, which my run reproduces.
  - It quotes the note's Theorems 1.1–1.2 (X(log X)² lower bound; classes of every size) in its §5.1.
- **Dependence.**
  - The note depends on manuscript 1 only for the minimality of the S = 18 pair and the rank-0 entry of Table 1. Both are removable (M4).
  - Manuscript 1 cites the note for results it does not need.
  - The two manuscripts cite each other's unpublished theorems. That is acceptable only if each is self-contained, which after M4 the note will be.
- **Duplication.** There is no duplication of theorems. The arithmetic content (counting, Thms 3–5, Prop. 5, Tables 1–2) appears only in the note. The shared enumeration should be described in full in one place, naturally the note, and only cited in manuscript 1.

**Related manuscript 2, "Finitely many eigenvalues determine the signature of a hyperbolic orbifold".** It concerns effective spectral recovery and shares only the example O(2,8,8), O(3,3,12) and a pointer to the note. There is no overlap of results and no dependence in either direction.

**Verdict on overlap.** Acceptable, with the clean-up in M4.

## Editorial decision (send to review / desk-reject) and recommendation (accept / minor / major / reject) with confidence

**Decision: SEND TO REVIEW.**
- The note is in scope for *Integers*. It studies the reciprocal-sum analogue of Guy D16, uses elementary and elliptic-curve tools of the kind the journal publishes, and is correct in every statement and every number I checked.
- It is honest about what is borrowed and adds a genuinely new counting question with complete proofs of two lower bounds.
- None of the reasons for desk rejection applies: there is no error, no duplicate publication, no out-of-scope material, and no unsupported main theorem.
- The weaknesses are of significance and context, not of correctness, and they are exactly what referees should weigh.

**Recommendation to the authors at this stage: MAJOR REVISION.**
- The paper should not be accepted until the literature is completed (M2) and the self-containment issues are fixed (M4).
- It also needs one of the following: a non-trivial upper bound (at least N(X) = o(X³)) or a sharper result on the dual family (M1); or a clear recalibration of its claims, together with a more honest status for Conjecture 1 (M3).
- I would send it to one referee from combinatorial/elementary number theory (equal-sum problems) and one from arithmetic of elliptic surfaces.

**Confidence.**
- *Correctness of the main statements* (proofs read; constants, key numbers and the full Table 2 recomputed independently): high.
- *Significance judgement*: moderate. A referee who knows of a counting result for the equal-sum/equal-product analogue, or finds the k ∈ {1, −1} system in Choudhry 2011, could move this either way.

## What resolves each issue

- **M1:** Prove N(X) ≪ X^{3−δ} or n(S) = o(S²), or an asymptotic for the dual-family count. Otherwise rewrite the abstract and introduction to present the bounds as family counts, and state the 10^190 crossover of Theorem 4.
- **M2:** Cite and discuss Choudhry (2011), both Ulas papers, Moreland–Zieve, Cha et al. (2018) with the OEIS entries, MacLeod (R/r = N) with the Ravi identity R/r = (Λ − 1)/4, and Verrill (2000), Saito–Yui (2001) and Meyer for the Γ1(6) self-fibre product. Add the quintic-threefold description, check Guy's UPINT, and re-state the novelty claim after this search.
- **M3:** Recast Conjecture 1 as a question, or supply a heuristic that predicts exponent 1. Report that the log-power and power-law fits are indistinguishable on the window, and add the "local exponent 1.58 and falling" caveat to the abstract.
- **M4:** Prove minimality of the S = 18 pair inside the note (from the enumeration or a strata argument). Replace "[8]" in Table 1 by "0 (LMFDB 90.c3)", and justify or drop the rank column.
- **m1:** Change Γ_0^0(6) to Γ1(6), or quote Beauville's notation exactly with a remark.
- **m2–m4:** Add the missing one-line justifications, and the case list in Remark 3.
- **m5–m6:** Add one sentence each.
- **m7:** Correct the Fig. 1(b) caption and the end of §6.3, or replot the k ≥ 4 quantity.
- **m8–m10:** Fix the caption and notation.
- **m11–m13:** State the Sadek–El-Sissi condition, and say where the descents and run details are archived.
- **P1–P6:** Shorten the abstract and remove "both conventions". Convert the declarations block to *Integers* style. Remove duplicated theorem numbering. Label the heuristics. Make the citation precise. Name a corresponding author.
