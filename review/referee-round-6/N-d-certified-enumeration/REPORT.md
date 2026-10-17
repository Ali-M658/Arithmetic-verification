<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Referee report: "Triples with equal sum and equal reciprocal sum" (Integers)

Coverage: all of Section 6, Tables 1 and 2, Figure 1, and every computational statement elsewhere. I wrote my own code for everything below. None of the authors' code or data was used.

(Saving this to REPORT.md was refused, so the complete report is given here. My code and outputs are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/N-d-certified-enumeration/scratch/code/` and `.../scratch/out/`.)

## Summary

The note counts unordered pairs of admissible triples (R = 1/a+1/b+1/c < 1) that share both their sum S and their reciprocal sum R. The geometry is the Bremner–Guy–Nowakowski pencil C_Λ: e1e2 = Λe3. The proved results are:

- Lower bounds: N(X) ≥ N_cl(X) ≥ (c_iso+o(1)) X log X, from the isosceles family, and N(X) ≥ (3/(128π⁴)+o(1)) X(log X)², from a conic bundle of dual pairs.
- An upper bound N(X) ≪ X^{3+ε}.
- Classes of every size, by Schinzel's argument.

The computational part is an exhaustive enumeration up to S = 4800, extended to S = 6000. It produces Tables 1 and 2, growth fits n(s) = c(log s)^q, and Conjecture 1, N(X) = X^{1+o(1)}.

My independent enumeration reproduces **every** integer in Tables 1 and 2 and every count in the text. The weak points are in how the growth evidence is reported:

- The bootstrap uncertainties appear to come from a resampling scheme that destroys the trend.
- The paper's own sentence on model uncertainty contradicts its reported numbers.
- A pure power law fits the data as well as the log-power model.
- Figure 1(b) does not plot what its caption says.
- The heuristic support for the specific exponent 1 in Conjecture 1 is thin.

## Significance

This is a natural reciprocal-sum analogue of Guy's problem D16, and it has a genuine spectral-geometric motivation. The proved theorems are modest:

- The lower bounds come from explicit torsion and dual families.
- The upper bound is at the scale of the number of triples.
- Theorem 5 is Schinzel's argument, used verbatim, as the authors acknowledge.

The data set is the most original contribution. It is large, correct, and useful as a reference. As a combined note (clean geometry, certified tables, an honestly labelled conjecture) it fits Integers, provided the growth section is repaired.

## Correctness and what was recomputed

**Enumerator.** I wrote my own C++ program. For each S it lists every triple 2 ≤ a ≤ b ≤ c with a+b+c = S and e2 < e3. It sorts by the double e2/e3 and then groups exactly, using 128-bit cross-multiplication within each run of equal doubles. Seven processes ran it on an 8-core machine.

- I checked it class by class against a separate exact `Fraction` brute force for S ≤ 300. Pairs, classes and primitive classes agree: 840 / 822 / 507.
- Over the full run, no two distinct rationals ever shared a double. The authors' hashing argument (equal rationals give the same correctly rounded double when e2, e3 < 2^53) is valid.

**Table 2: reproduced exactly in every entry, S = 18 to 6000.**

- All five integer columns (pairs, classes, primitive classes, largest class, and the S column itself) agree in every row.
- All local exponents agree to three decimals, for example 2.524, 1.993, 1.603 and 1.585 (exact value 1.58454).
- The rounding "1.58" in the abstract and the text is correct.
- The triple count up to 4800 is 3 067 197 199, as stated. Up to 6000 it is 5 992 496 499; the paper does not state this.
- N(S)/S² is 0.00935 at S = 400 and 0.00405 at S = 6000, as stated.

**Text of Section 6.1: all reproduced.**

- Class sizes up to 4800: 96 981 / 1627 / 122 / 11 / 1.
- 46 254 primitive pairs up to 4800, of which 16.49% are dual. Up to S = 200 the dual share is 32.93%.
- 669 non-dual primitive pairs with S ≤ 400.
- 507 of the 582 sums 19 ≤ S ≤ 600 carry a primitive class.

**Table 1: reproduced exactly.**

- The members and sums of the first class of each size k = 2, …, 6, at S = 18, 136, 408, 1849 and 4600, agree.
- No class of size 7 occurs up to 6000, nor up to 7500 (see below).
- Ranks, from PARI 2.17.2 `ellrank` via cypari2 in a virtual environment: Λ = 68/5 gives [2,2], 1849/120 gives [3,3], 230/21 gives [3,3], and 155/12 gives [2,2].
- For C_{27/2}, `ellrank` gives [0,0] and the torsion is Z/2×Z/6.
- I did not redo the 2-isogeny descents.

**Section 3 claims: reproduced.**

- 1753 primitive pairs with S ≤ 600, of which 423 are dual and 1330 non-dual.
- For each of the 1330, neither P′−P nor P′+P has order ≤ 12. I used exact Weierstrass arithmetic on the paper's model E_Λ, through the paper's birational map.
- For each of the 669 non-dual pairs with S ≤ 400, none satisfies P′ = ±mP+T or P = ±mP′+T for m ∈ {2,3}.
- Remark 2: there are 40 305 primitive positive triples with sum ≤ 120 other than (1,1,1). Among them, 2212 are torsion points (orders 2, 6 and 12), and every one is isosceles or a geometric progression.

**Proposition 3, Proposition 4 and Theorem 5: verified.**

- The maps are mutually inverse and land on E_Λ: checked exactly on 1850 random rational points.
- The discriminant 2^12 Λ²(Λ−1)³(Λ−9) and the identity in Remark 1 were checked symbolically.
- The images of (0:1:−1) and (1:0:−1) have order 3.
- (1:4:4) ↦ (−6, 45) at Λ = 27/2.
- ι(P) = P + (0,0) on 500 random points.
- Λ(4,9,18) = 155/12, P has no order ≤ 12, and 3P = (162833463 : 723926268 : 287876366) exactly.

**Theorem 3 and its numerics: verified.**

- The area and counting constant: c_iso = 3 log 2/(2π²) = 0.105346.
- A_iso(4800) = 506, against c_iso · 4800 = 505.66.
- The copies kD_{u,v} with k ≥ 4 satisfy (count − c_iso X log X)/X = −0.4793, −0.4793, −0.4794, −0.4794 at X = 10⁴, 10⁵, 10⁷ and 4×10⁷. So "−0.479X to three digits" holds.

**Theorem 4 and Proposition 5.** I rechecked the constants (c_A = 3/(32π⁴), final constant 3/(128π⁴)), the box inequality and the multiplicity-6 argument by hand. They are correct. The identity (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′ was checked algebraically; I did not redo the "recount for S ≤ 160".

**Section 6.3 fits.** I computed exact Poisson MLEs by IRLS on 600 ≤ s ≤ 4800.

| Series | My q | Reported q |
|---|---|---|
| all pairs | 4.4887 | 4.48 |
| primitive | 3.5320 | 3.54 |
| dual, primitive | 2.5596 | 2.56 |
| dual, all | 3.3316 | 3.33 |
| non-dual, all | 4.7981 | 4.79 |
| cumulative least squares, all | 4.557 | 4.56 |
| cumulative least squares, primitive | 3.625 | 3.63 |
| window [1200, 4800] | 4.4369 | 4.43 |
| window [600, 2400] | 4.6421 | 4.63 |
| window [2400, 4800] | 4.3900 | 4.37 |

The point estimates agree to within 0.02, but see m3 on rounding. The bootstrap uncertainties do not agree; see M1.

**Extension beyond the paper.** I ran the enumeration to S = 7500: 11 707 026 874 triples, with no double collisions between distinct rationals.

| S | N | N_cl | primitive classes | largest class | local exponent |
|---|---|---|---|---|---|
| 6500 | 164 697 | 158 322 | 69 824 | 6 | 1.5739 |
| 7000 | 184 293 | 177 217 | 77 366 | 6 | 1.5665 |
| 7500 | 204 899 | 197 031 | 85 410 | 6 | 1.5612 |

Class sizes up to 7500 are 193 593 / 3158 / 247 / 29 / 4, with none of size ≥ 7. The local exponent keeps falling slowly, consistent with the paper's description.

## FATAL

None. Every theorem I checked is correct, and every reported count was reproduced exactly by an independent program.

## MAJOR

**M1 (p. 13, §6.3: "q = 4.48 ± 0.44 per sum and 4.56 ± 0.71 cumulatively; primitive 3.54 ± 0.37 and 3.63 ± 0.57"; also the ± values for the dual and non-dual fits).** The reported bootstrap standard deviations cannot be reproduced by a valid block bootstrap.

- Resampling blocks of 50 sums together with their s-values, then refitting, gives sd 0.061 for all pairs and 0.079 for primitive pairs (400 resamples).
- Resampling blocks of multiplicative residuals around the fitted trend gives 0.057 and 0.092.
- The quasi-Poisson standard error is 0.051 × √6.76 = 0.13. The Pearson dispersion is 6.76.
- One scheme does reproduce the paper's numbers: resampling blocks of the count series and laying them back on the original s-grid gives sd 0.458 and 0.374. But that scheme destroys the trend: the mean of the resampled q is −0.03.

So the reported "± 0.44" appears to measure the spread of a trend-free null distribution, not sampling noise in q. The authors must state the scheme exactly and, if this is what they did, replace it.

The error also shows inside the paper. Section 6.3 says "The model uncertainty is larger" than the bootstrap. Yet the paper's own model-dependence figures are a method spread of ≤ 0.1 and a window spread of 4.37 to 4.63. Both are smaller than ±0.44, so the sentence contradicts the numbers next to it. With a correct bootstrap (about 0.06 to 0.13) the sentence becomes true, and model uncertainty dominates.

**M2 (pp. 3, 13; Conjecture 1, §§6.3–6.4): the evidence offered does not single out the exponent 1.**

- The fitted model n(s) = c(log s)^q assumes the conclusion, namely exponent 1 up to logarithms.
- On the same window, a pure power law n(s) = c s^β fits essentially as well. Poisson MLE gives β = 0.587. The negative log-likelihoods differ by 9.5, which is about 2.8 in quasi-deviance after the dispersion of 6.76, so the difference is not decisive.
- That power law gives a cumulative exponent of about 1.59, matching the observed local exponents. My extension shows 1.561 at S = 7500, still drifting down slowly.
- Section 6.4 itself names a scenario the data cannot exclude: a quadratic rational surface would give X^{3/2}. The authors say they have not searched for one.

Required:

1. Report the power-law competitor and the model comparison, with a dispersion-adjusted criterion.
2. Correct "does not exclude a limiting exponent anywhere between 1 and about 1.58" (p. 13). A finite-range local exponent is not an upper bound for the limit either, so the true range left open is 1 to 3.
3. Either give a real heuristic for exponent exactly 1 (for example, a count of the contribution of rational curves of each degree, or a Manin-type heuristic for the Calabi–Yau fibre square), or downgrade Conjecture 1 to a question.

The abstract's "We conjecture N(X) = X^{1+o(1)}" should then be qualified accordingly.

## MINOR

**m1 (p. 14, Figure 1(b) and its caption; p. 13, "with the isosceles lower bound of Theorem 3").** The thin curve is not the lower bound of Theorem 3. It is the count of all admissible copies kD_{u,v} with k ≥ 1, divided by S.

- It takes the value 1/18 = 0.056 at S = 18, rises to 0.10 at S = 20, falls to 0.059 at S = 34, and jumps to 0.139 at S = 36. These match the rendered curve exactly.
- It reaches 0.63 at S = 6000.
- Theorem 3's quantity uses only k ≥ 4. It is 0 until S = 72 and equals 0.44 at S = 6000.

Either plot the bound or relabel the curve. Also, panel (b) stops at S ≈ 4800 although Table 2 runs to 6000; say so, or extend the panel.

**m2 (p. 7, Remark 2: "A positive isosceles point therefore has order 6").** This depends on which coordinates are equal. The arrangement (v:v:u) is fixed by the transposition x↔y, which fixes O = (1:−1:0), so it is a point of order 2. Example: (2:2:1) on C_10 maps to (−32, 0). Only (u:v:v) and (v:u:v) have order 6. Restate the claim for the arrangement (u:v:v).

**m3 (p. 13, rounding of fit results).** Exact MLEs are 4.4887, 3.5320, 4.7981, 4.4369, 4.6421 and 4.3900. These round to 4.49, 3.53, 4.80, 4.44, 4.64 and 4.39; the paper prints 4.48, 3.54, 4.79, 4.43, 4.63 and 4.37. This is probably optimizer tolerance. Use an exact GLM fit and round once. Also state whether "non-dual pairs 4.79" refers to all pairs or primitive pairs: the primitive non-dual value is 3.73.

**m4 (p. 6, Remark 1: "For rational Λ there is more").** The list is incomplete. The geometric-progression curves Λ = (1+r+r²)²/r² carry Z/12. PARI gives Z/12 for Λ = 49/4 and Λ = 169/9, and geometric-progression points have order 4 or 12 there; I found 21 points of order 12 in the Remark 2 range. Mention this, since Remark 2 relies on geometric progressions being torsion.

**m5 (p. 14, "Among the 189 lines … coefficients of absolute value at most 7").** 189 is the count up to sign *and* permutation of coordinates. Without the permutation identification there are 1026 such lines. Say so. Also state how the Möbius reparametrisation was searched for (degree, height, method), so that the negative result can be reproduced.

**m6 (p. 11, §6.1, certification).** The range 4801–6000 is fully cross-checked only at S = 5400 and S = 6000, and only for cumulative counts. State precisely which column of each Table 2 row was confirmed by how many independent programs. Give the triple count to 6000 (5 992 496 499) and per-S checksums in the archive. My recomputation agrees everywhere, so this concerns documentation only.

**m7 (pp. 3, 12–13, Proposition 5).** Say plainly that n(S) ≪ S^{2+ε} is at the scale of the number of triples (about S²/12). The data show n(s) growing like s^{0.6}, so the stated "upper bound" says little about growth. The phrase "far apart" undersells how wide the gap is.

**m8 (abstract; pp. 3 and 13: "falling from 2.5").** The value 2.524 at S = 100 rests on N(50) = 16 pairs and is a small-number start-up effect. The local exponent is 1.993 at S = 500 and falls monotonically after that. Quote the range from S ≥ 500.

**m9 (p. 11, Table 1).** Give the rank of C_{27/2} as 0 (PARI `ellrank` gives [0,0]; torsion Z/2×Z/6) instead of the bare citation "[8]".

## Presentation

**P1 (abstract and Table 2 caption).** "Both conventions" is opaque. Say "pairs and classes".

**P2 (p. 2).** Typo: "withsum".

**P3 (p. 13).** The bootstrap, the "exact partial sums of the model", and the cumulative baseline (from s = 1 or from s = 600?) need one precise sentence each, so the fits can be reproduced.

**P4 (p. 12).** Table 2 uses S for the upper limit X of N(X). Use X, or say that the notation is reused.

**P5 (p. 11).** It would help to add the counts to 6000 (class sizes 137 520 / 2287 / 173 / 23 / 2) next to the 4800 counts.

## Recommendation

**Major revision.** Confidence: high on the computational findings, since everything was recomputed independently; medium on the weight given to M2.

## What resolves each issue

| Issue | What resolves it |
|---|---|
| M1 | Specify the bootstrap. Use a valid scheme (pairs bootstrap with s-values kept, or residual block bootstrap); expect sd ≈ 0.06–0.13. Rewrite the "model uncertainty is larger" sentence consistently. |
| M2 | Report the power-law fit (β ≈ 0.59) and a dispersion-adjusted comparison. Fix the "between 1 and 1.58" sentence. Supply a heuristic for exponent 1, or turn Conjecture 1 into a question. Adjust the abstract to match. |
| m1 | Plot the k ≥ 4 bound, or relabel the curve as "all admissible isosceles copies". Extend panel (b) to 6000 or state its range. |
| m2 | Restrict the order-6 claim to the arrangement (u:v:v), and note that (v:v:u) has order 2. |
| m3 | Refit by exact GLM, round once, and say which non-dual series is meant. |
| m4 | Add Z/12 on the geometric-progression family. |
| m5 | Say "up to sign and permutation" and describe the Möbius search. |
| m6 | Give a per-column certification statement, the triple count to 6000, and checksums. |
| m7 | Add one sentence on the scale of Proposition 5. |
| m8 | Quote the exponent range from S ≥ 500. |
| m9 | Write rank 0 in Table 1. |
| P1–P5 | Make the wording edits listed above. |
