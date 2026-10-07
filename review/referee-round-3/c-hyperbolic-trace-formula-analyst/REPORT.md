<!-- The reviewer's write was refused by the harness ('Subagents should return findings as text'); this file is the reviewer's returned final message, saved verbatim from the task transcript by the main session. -->

I could not write REPORT.md. The Write tool refused ("Subagents should return findings as text, not write report files"), so the full report is below. The intended path was `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-3/c-hyperbolic-trace-formula-analyst/REPORT.md`. My scripts and page renders are in the `scratch/` folder next to it.

---

# Referee report (trace-formula / heat-kernel analyst): "How much of a hyperbolic orbifold does heat hear?"

Submitted to Annals of Global Analysis and Geometry. Files read: manuscript.pdf (48 pp.) and supplement.pdf (15 pp.) only. Placeholders (author contributions, AI-use statement, Zenodo DOI) are treated as known and not counted.

## 1. Summary

The paper studies closed orientable hyperbolic 2-orbifolds O with cone points. The signature is σ = (g; m_1..m_n). The heat invariants c_j(O) come from the small-time expansion of the heat trace. At curvature −1 they depend only on the signature. The area enters through coefficients α_k. Each cone point enters through an explicit even polynomial p_l(m)/m of degree 2l+2. The j-th invariant brings in one new odd power sum P_{2j−3} of the cone orders, together with R = Σ 1/m_i.

Main claims:

1. **Counting theorem.** Comparing two signatures amounts to a signed multiset Z = U ⊎ (−V) with vanishing odd moments and vanishing reciprocal sum. If |Z| ≤ 2L the multiset is symmetric, so U = V. Hence the first ⌊Area/π⌋+4 invariants determine genus and cone orders (Thm 3.4, Cor 3.5, Thm 1.1(i)). No area-independent number suffices.
2. **Growth.** The minimal number f(A) lies between c√A and A/π + 4. Linear growth holds iff the Prouhet–Tarry–Escott function satisfies N(k) = O(k). More generally f ≥ cA^α iff N(k) ≤ Ck^{1/α} (Thm 3.11, Prop 3.12).
3. **Spheres.** For a sphere with n cone points, n invariants fix the orders (Thm A). n−1 do not, for n = 3, 4 on integers and for all n on reals (Thm C).
4. **Triangle orbifolds.** Two invariants suffice up to cone-order sum 17. The first failure is O(2,8,8) versus O(3,3,12). The isolation of this pair is the statement that the cubic C_{27/2} is an elliptic curve of rank 0 and torsion Z/2 × Z/6, with no other positive rational points (Thms 6.1–6.8). Three invariants always suffice.
5. **Theorem 4.13 (the theorem I was asked to check).** Fix A, ε, M. Among orbifolds with area ≤ A, systole ≥ ε and cone orders ≤ M, the first N eigenvalues, each known to within δ, determine the signature. The explicit N and δ come from:
   - an explicit diameter bound D(A, ε, M) (Lemmas 4.1–4.2, Thm 4.3);
   - an explicit bound on the hyperbolic term of the trace formula (Lemma 2.5, Prop 4.7, Thm 4.8);
   - enveloping remainder estimates for the cone and area expansions (Props 4.9–4.10);
   - an integrality-and-gap argument at the first index where two signatures differ (Lemmas 4.11–4.12).

   The dependence on M cannot be dropped (Props 4.4, 4.15, Rem 4.14). Whether the systole bound is needed is left open.
6. **Stability.** Section 7 and Thm 1.3 give Lipschitz and Hölder stability of the orders in the data, with a certified rounding threshold.
7. **Supporting material.** Section 5 shows that heat does not see the moduli, and Section 8 gives numerical experiments.

## 2. Significance

The literature I checked (Donnelly, Dryden–Gordon–Greenwald–Webb, Dryden–Strohmaier, Uçar, Schueth, Abreu et al.) is correctly positioned. I confirmed by Crossref and arXiv that the Dryden–Strohmaier theorem is as quoted. It says the spectrum determines the length spectrum and the number of singular points of each order. The cited arXiv items exist: Chen's survey 2506.11429, Croot–Mao–Yip 2609.05061 (submitted 2026-09-04), and Dryden's math/0411290.

**What is new.**
- *The explicit counting theorem.* The reduction to a symmetric signed power-sum problem, the Descartes imbalance bound, and the identification of the growth problem with the PTE function N(k). The "iff N(k) = O(k)" characterisation is a genuinely interesting link between inverse spectral geometry and additive number theory. I found no precedent.
- *The sharp triangle result.* Two invariants up to sum 17, with exact first failure at sum 18. It is elementary but neat, and the rank-0 isolation (verified below) is a nice touch.
- *Theorem 4.13.* A fully explicit finite-spectral-data version of Dryden–Strohmaier. Their theorem gives qualitative determination by the whole spectrum, and the finiteness of Sig(A,M) is classical. What is new is effectivity: a computable N and δ, with a trace-formula proof that avoids collars and thick–thin decompositions. The necessity of the bound on M is a real statement, because the cone-ball Rayleigh-quotient argument is clean.

**Weaknesses of significance.**
- The effective constants are astronomically large (Table 2: N up to 10^35, δ down to 10^−384). The authors admit this and show that 3–50 eigenvalues suffice on test cases.
- The theorem therefore certifies existence of a finite computable rule, not a usable one. Its value to the readership is conceptual.
- The paper bundles at least four separable contributions: PTE/counting, triangle orbifolds with an elliptic curve, finite-eigenvalue determination, and stability plus numerics. For AGAG the geometric-analytic core (Sections 2, 4, 5) is the natural fit. The arithmetic parts (Section 6, the searches of Remarks 3.2/3.14, Section 7) are more at home elsewhere.

## 3. Correctness and what I recomputed

I checked the proofs on which the main results depend line by line, and re-ran the numbers with my own code. I found no mathematical error in any proof I checked.

**Proofs read line by line and found correct** (algebra by hand, plus the numerical checks listed):

- **Lemmas 2.4 and 2.5.** I rechecked the Dirichlet-domain counting, the integration-by-parts chain, the x/(x−t) trick, and the constant (2+3ℓ)/(2+ℓ). I confirmed the claimed monotonicity of B in ℓ numerically: 600 values of ℓ times 60 values of t over the whole admissible range, no counterexample.
- **Lemma 2.6** (closed form of Φ_m, via Liouville). Verified at m = 2, 3, 7, 12 to 1e−39.
- **Prop 2.7 and Appendix B** (derivation from the trace formula, Euler beta integral, moment identity). The first values of α_k and p_l in (7) check symbolically, and (4)–(6) check numerically.
- **Lemma B.1** (admissibility of the heat function). The cut-off argument and the O(x) counting bound are correct and self-contained.
- **Lemmas 2.8, 3.1, Thm A, Lemma 3.3, Thm 3.4, Cor 3.5, Prop 3.9, Thm 3.8 (Descartes), Lemma A.1, Prop A.2, Thm 3.11(a)–(d), Prop 3.12.** The mirror argument is sound.
- **Lemma 4.1.** I re-derived the case analysis X > 1 / X < 1, the defect ≥ π/(abc), the half-angle cosine bound, and the final bound 2/(π²cM).
- **Lemma 4.2 and Thm 4.3** (packing argument) and the closed form, including d_0 ≥ min(ε/2, 0.6/M). The quoted justification "arccosh(1+x) ≥ 2x/(1+x)" is garbled. What is true, and what I checked, is arccosh(1+x) ≥ √(2x/(1+x)).
- **Prop 4.4.** The folding, the cone ball and the reduction r < 2s_∞ are right.
  - The commutator identity tr[γ,β] − 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r holds to 3e−14 on 2000 random configurations.
  - σ_0 = 0.56206 is reproduced.
  - Word enumeration of (2,3,m) gives systoles 0.98 (m=7), 1.27, 1.66, 1.91 and 1.925, consistent with the lower bound σ_0.
- **Lemma 4.5, Props 4.6–4.7, Thm 4.8.** The constants 21, 63 and 42/√π all reproduce.
- **Props 4.9 and 4.10** (enveloping remainders). I checked the all-same-sign structure of the proof. Numerically, for m ∈ {2,3,5,12}, t ∈ {0.001, 0.01, 0.1, 1, 3} and K = 0..7, at 50-digit quadrature, I checked both the sign (−1)^K and the bound |b_K|t^K, and the I(t) analogue with α_{K+1}. There were no failures, including at t of order 1.
- **Lemmas 4.11 and 4.12.** I re-derived d_k = (−1)^k a_{k−2}(P_{2k−3}(U) − P_{2k−3}(V)). Exhaustive test: I enumerated all 14,945 signatures with genus ≤ 2, orders ≤ 30 and Area ≤ 3π, and computed exact heat invariants for all 28,290 pairs of distinct signatures with equal area. In every pair the first differing index satisfies k ≤ ⌊Area/π⌋+4, and |d_k| ≥ a_{k−2}.
- **Proof of Theorem 4.13.**
  - The B*(t) ≤ Γ(t)/8 algebra for y_0, the tail bound via Prop 4.6, the perturbation estimate and the 3/8 versus 5/8 margin are all correct.
  - I recomputed t_1, t_3, N, δ of Table 2 from the printed definitions, using the exact D of Thm 4.3. All seven rows reproduce: t_1 = 1.14e−7, 6.8e−9, 5.5e−6, 2.7e−11, 4.0e−7, 1.5e−15, 1.0e−31; t_3 and N and δ also match to the printed digits.
  - Table 1 (values of D) also reproduces.
- **Prop 4.15, Rem 4.14, Prop S7.1.** I re-derived identity (15) for f = w^{−1/2}u (q = w''/(2w) − w'²/(4w²)). The Rayleigh-quotient bound, the pigeonhole count, and the exact quotient sinh a/((a²+2) sinh a − 2a cosh a) are correct.
- **Theorems 6.5–6.7.** I brute-forced all hyperbolic triads with sum ≤ 300 (keys (S,R) as exact rationals).
  - The first collision is sum 18, with the unique pair (2,8,8)/(3,3,12).
  - The collision-free sums ≥ 18 begin 19, 21–25.
  - The first non-adjacent collision, (5,15,15)/(7,7,21), appears at sum 35, as stated.
- **Thm 6.8.** I recomputed the 2-isogeny descent of Appendix C by brute-force local solubility at 2, 3, 5 and the real place. The Selmer groups have sizes 4 (for E) and 1 (for E′), so the rank is 0. #E(F_7) = #E(F_11) = #E(F_13) = 12. The map ψ lands in C_{27/2}, checked symbolically. The printed formula for φ is correct as typeset (page 36).
- **Exact heat invariants.** Example 3.6, Example 3.13 and Thm C(3) reproduce exactly:
  - (3,3,5,5)/(1;15) share exactly 2.
  - (3,10,15,30)/(4,5,21,28) share exactly 3.
  - (1;15,15,15)/(0;3,3,5,7,7,21) share exactly 3.
  - (4,4,5,5,6,12,12)/(2,2,2,3,10,10,10,10) share exactly 3.
  - For O(2,8,8) versus O(3,3,12): c_2 = 67/48 and d_3, d_4, d_5 = 25/12, −1775/24, 153025/48.

**Only skimmed.**
- Theorem B and Lemma 7.3 (the Hurwitz determinant identity), and Section 7 (Thms 7.4–7.8). I checked the front-end constants amp_r, Prop 7.6(i), and the one-line argument of Prop 7.7 (exponent 1/2). I did not check the Rouché-based Thm 7.5/7.8 line by line.
- The strata inequalities of Lemma 6.3 and Thm 6.4. I confirmed their consequences by brute force but not each algebraic step.
- The searches of Remarks 3.2/3.14 and Table S1.
- All finite-element and numerical results (Section 8, S4–S6, Table 3). These cannot be reproduced from the PDFs, so I treat Table 3 as illustrative.
- Thm C(2), and the proof of Thm 3.11(c), which I checked structurally only.

## 4. MAJOR issues

**M1. Proof steps resting on numerical checks, a secondary source, or code (bearing on a headline claim).**

*Location:* Sect 4.1, facts (H1)–(H3): "each also checked numerically on random configurations, with the repository code". Prop 4.4 proof: "(the second identity ... is checked numerically)". The Jørgensen inequality, cited via ref. [36], the Wikipedia article, with "we could not retrieve the original paper".

*Issue:* The abstract states that "the bound on the cone orders cannot be dropped". That claim passes through Prop 4.4, whose systole lower bound σ_0 uses Jørgensen's inequality and an unproved commutator-trace identity. H1–H3 underlie Lemma 4.1, hence Lemma 4.2, Thm 4.3 and every constant in Thm 4.13. A journal proof should not rest on "checked numerically", on repository code, or on Wikipedia. I verified all of these (identity to 3e−14, H3 algebra by hand, and Jørgensen's inequality is correct as stated), so this is a gap of citation and exposition rather than of truth. By the standard I was asked to apply, an unproved "standard" step is a gap.

*Resolution:*
- Cite Jørgensen (1976) directly, plus a textbook statement (for example Beardon, *The Geometry of Discrete Groups*, section 5.4, or Maskit). Remove [36].
- Include the two-line derivation of tr[γ,β] − 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r (conjugate so the axis is the imaginary axis).
- Give references or one-line proofs for H1 (rotation displacement), H2 and H3 (law of cosines for angles), and delete the appeals to code.

**M2. Overstatement risk and thin quantitative content of Theorem 4.13.**

*Location:* abstract, Section 1.1, Section 4, Table 2.

*Issue:*
- "Finitely many eigenvalues, each known approximately, determine the genus and cone orders" is correct. But the N, δ delivered are 10^8–10^35 eigenvalues at accuracy 10^−21–10^−384, even for a handful of candidate signatures. By Table 3 the same rule works with N_obs = 3–4 eigenvalues on the motivating pair.
- The cause is a design choice of the proof. The gap is manufactured from the divergent small-t expansion, which forces t* ~ δ_k/Q(k−1), and Q(K) grows like K!(M/π)^{2K}.
- Since Sig(A,M) is finite and explicit and G_σ(t) is computable exactly, a cheaper and equally rigorous a-posteriori criterion exists. Choose any t at which the Thm 4.8 hyperbolic-term bound is below a quarter of min over pairs of |G_σ − G_σ′|, and then use N from Thm 4.8 and δ from the same perturbation estimate. Section 4.6 effectively does this on data. The a priori theorem would then become a corollary.
- I could not find an explicit statement of what Thm 4.13 adds beyond Dryden–Strohmaier plus finiteness of Sig(A,M).

*Resolution:* Add the a-posteriori version, or state clearly in the abstract and introduction that the constants are far from practical. Add one paragraph saying exactly what Thm 4.13 adds over the non-effective route. Qualify "far fewer eigenvalues suffice" (Section 4.6) as based on a few specimens.

**M3. Scope and length.**

*Location:* whole paper, 48 + 15 pages.

*Issue:* The paper is effectively three or four papers:
- PTE and counting (Sections 3, A);
- triangle orbifolds and an elliptic curve (Section 6, C);
- finite-eigenvalue determination (Sections 4, B);
- stability (Section 7), plus numerics (Section 8, S4–S6).

Cross-dependencies are heavy (Section 4 uses Lemmas 2.5–2.10, 3.3, 3.4 and Cor 3.5; Section 5 uses Thm 4.3). A reviewer cannot verify all of it with equal care, and the AGAG readership will not equally care about all of it. Section 8 and the supplement's finite-element work support no theorem.

*Resolution:* Either split the paper (for example: counting/PTE with triangles; finite eigenvalues with moduli), or move Sections 7 and 8 to the supplement. At minimum, state in the introduction which results depend on which sections.

## 5. MINOR issues

- **m1 (notation clashes).**
  - σ_0 means the signature of O in the proof of Thm 4.13 and the constant 0.56206 in Prop 4.4 and Rem 4.14.
  - Φ_m(u) (Lemma 2.6) clashes with Φ_j(σ) (Prop 5.1).
  - Γ is the group, Γ(t) the gap, Γ_* its value.
  - Λ is the cut-off in Thm 4.13 and the Bremner–Guy–Nowakowski invariant in Section 6.2.
  - N is the number of eigenvalues, N(k) the PTE function, and script 𝒩 the counting function.
  - D is the diameter bound, and D(t) a trace difference in Section 8.
  - p is the exponent k*−3/2 in Thm 4.13, a prime in Lemma 4.11, and p_l the cone polynomial.
  - a_l (Section 4.4) and a_{l,k} (Lemma 2.10) collide.
  - ϖ and ϖ_r (proof of Thm B) are both used.
- **m2.** Lemma 4.11(ii) proves divisibility of P_{2k−3}(U) − P_{2k−3}(V) by all primes p with (p−1) | 2(k−2). The gap uses only |d_k| ≥ a_{k−2}. Either use the divisibility (the gain is a factor of at most a few thousand at k* = 14, so it is cosmetic) or drop the sentence.
- **m3.** Theorem 4.13 tacitly assumes the observer holds the first N eigenvalues in order, complete and with multiplicity. Section S4 admits that the authors' own single-window slicing can miss an eigenvalue. State this completeness hypothesis explicitly in Thm 4.13 and Section 4.6.
- **m4.** The diameter detour is not needed for the proof. Its only use is the closed-geodesic counting bound of Lemma 2.4, which the embedded-ball volumes of Lemma 4.2 could supply directly. The diameter bound is not binding in any row of Table 2 (t* = t_1 throughout; in the (2π, 0.1, 3) row t_1 = 4.0e−7 and t_3 = 4.3e−7 are close). Say so, or remove the detour. The gap between D = O(AM³) and the lower bound log M is acknowledged.
- **m5.** Citation quality. [27] (Dryden, 2004) is an unpublished preprint, [34] is an arXiv preprint about five weeks old, and Section 1.2 cites a "companion manuscript in preparation" for the isolation. Uçar's thesis [14] is the main source for the closed-form comparison (Remark 2.9), although no proof depends on it. Prefer published sources where they exist.
- **m6.** Garbled formula in the proof of Thm 4.3: it should read arccosh(1+x) ≥ √(2x/(1+x)).
- **m7.** Table 3: the column "competitors" counts 6 for O(2,8,8). That is the number of all signatures of area π/2 with orders ≤ 12, including the orbifold itself. I verified the list: (2,8,8), (3,3,12), (2,6,12), (3,4,6), (4,4,4), (0;2,2,2,4). The wording "competitors" suggests 5.
- **m8.** Equation (14) mixes a sum from j = 1 to K+1 with remainders indexed by K. It is correct (I checked the indexing against Props 4.9–4.10) but needs one more line.
- **m9.** The exponent N−1 in M = (⌊Λ_N/δ⌋+1)^{N−1}+7 (Rem 4.14 and Prop 4.15) is hard to read on the page image. Write it as a displayed formula.
- **m10.** The claim "log(1/δ) grows roughly like (A/π)² log(AM)" is flagged as an observation. Drop it or label it clearly as heuristic.
- **m11.** The abstract's "three always suffice" and "sum 17" are proved for triangle orbifolds only (Thm 1.2, 6.5–6.7), not for general signatures. The abstract is clear on this, but the roadmap could repeat it.

## 6. Presentation

- **Length and structure.** The paper is long and dense (Section 4 alone is about 12 pages). The roadmap and introduction are good, and theorem numbering is clean. Section 4 is well organised: elementary bounds, remainders, integrality and gap, main theorem, necessity, hypotheses.
- **Figures** (page images viewed for Figs 3, 8 and the Section 4 pages).
  - Fig. 1 is useful but schematic, as the caption says.
  - Fig. 2 is clear.
  - Fig. 3 (log s axis, 525 classes) is readable, but the caption does not say that the solid line is the Cor 3.5 staircase.
  - Fig. 8 is readable.
  - Fig. 7 has the legend "slopes 1, 1/2, 1/3, 1/2", which I could not tie to the three curves without the text.
- **Typography.** I found no sign errors in the formulas I checked on the page images: Lemma 2.5 (p. 7), Prop 4.4 (p. 20), Props 4.7 and 4.9–4.10 (pp. 21–23), Thm 4.13 (p. 25), Prop 4.15 (p. 27), Thm 6.8 (p. 36). The text-layer garbles noted above (m6, m9) are the only formula-presentation problems I found.
- **Bibliography.** A Wikipedia entry with a "fetched" date is out of place (M1).
- **Supplement.** Clear and appropriately scoped. Section S7 correctly explains why pinching does not bear on the systole bound.

## 7. Recommendation

**Minor revision** (confidence about 70%).

I could not find an error in any proof I verified. The headline results are correct as stated: the counting theorem, the PTE growth equivalence, the sum-18 triangle threshold with rank-0 isolation, and Thm 4.13. The paper is honest about its limits. The remaining reasons not to accept as-is are rigor of exposition (M1), framing (M2) and scope (M3).

| Issue | What resolves it |
|---|---|
| M1 | Cite Jørgensen and a textbook; prove the commutator identity; prove or cite H1–H3; remove the code and Wikipedia references. |
| M2 | Add the a-posteriori (explicit pairwise gap) version of Thm 4.13, or reframe the claim and state what it adds over Dryden–Strohmaier plus finiteness. |
| M3 | Split the paper or move Sections 7–8 to the supplement; state dependencies. |
| m1–m11 | Editorial, as listed. |

My confidence that Theorem 4.13 and its supporting lemmas are correct as stated is high (about 90%), based on the line-by-line reading and the recomputations above. The residual uncertainty is mainly Section 7 and the unreproducible numerics, which I only skimmed.

Report path (could not be written): `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-3/c-hyperbolic-trace-formula-analyst/REPORT.md`
