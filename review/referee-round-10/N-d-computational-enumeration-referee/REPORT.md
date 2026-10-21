<!-- Round 10, N-d, returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

I could not write the report to `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/N-d-computational-enumeration-referee/REPORT.md`: the write was refused ("Subagents should return findings as text"). The full report is below.

# Referee report: "Triples with Equal Sum and Equal Reciprocal Sum" (submitted to *Integers*)

**Referee remit:** Section 6 (enumeration, upper bound, growth, the evidence for Question E) and every computation in it. I also cover the numerical statements elsewhere that rest on the enumeration: Table 2, the isosceles counts after Theorem 2, and the statements of Question E on p. 4. Page numbers are those of the submitted PDF (25 pp.). I read the rendered pages for every figure and typographical remark below. The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifier) are treated as known.

## Summary

The note studies unordered triples of positive integers that share their sum S and reciprocal sum R with another triple. It does this through the cubic pencil C_Λ: (x+y+z)(xy+yz+zx) = Λxyz.

Section 6 does the following:
- reports an exhaustive enumeration of all admissible triples with S ≤ 4800, extended to S ≤ 6000;
- tabulates the cumulative number of pairs N(X), of classes and of primitive classes, with local growth exponents (Table 3);
- classifies the primitive pairs up to 4800 as dual, torsion-translate or "third kind";
- proves n(S) ≪ S^{2+ε} (Proposition 5);
- fits two-parameter growth laws (log-power and power) to the per-sum counts and compares them on two forward holdouts;
- closes with a heuristic for what a positive answer to Question E (N(X) = X^{1+o(1)}) would require.

## Significance (for Section 6)

The enumeration is a real contribution. It is complete, exact and large (5.99 × 10^9 triples), and as far as I know it is new. Table 3 and the class-size statistics will be the reference data for this problem.

The dual / torsion / infinite-order classification of the 46 254 primitive pairs is informative and well designed. It shows that the families the paper can prove things about (the dual pairs) are a shrinking minority, about 15.5% of primitive pairs at the top of the range.

The paper is also unusually candid that curve fits do not estimate asymptotic exponents, and the dual-family example on p. 21 is the right one to make that point. The weak part is the use of the two holdouts as "evidence for a positive answer to Question E". My recomputations show that this claim cannot stand (M1).

## Correctness, and what I recomputed

I wrote my own code from the definitions in the paper and did not look at the authors' deposit:

- **Enumerator (C++).** For each S it lists all 2 ≤ a ≤ b ≤ c with a+b+c = S and e2 < e3, reduces e2/e3 by its gcd, and groups by the exact reduced fraction using an integer sort. It does not hash floating-point values. Every class is re-verified by 128-bit cross-multiplication.
- **Classifier (Python, exact arithmetic with `fractions`).** It maps each triple to E_Λ through the map of Proposition 2, asserting that the image lies on E_Λ. It decides "dual" by proportionality to a permutation of (bc, ca, ab). It decides "differs by torsion" by testing whether 12(P − P′) = O or 12(P + P′) = O on E_Λ. This test is valid because every torsion group in Theorem 1 has exponent dividing 12.
- **Fitter.** Poisson maximum likelihood and least squares for the growth laws.

The full run to S = 6000 took about 10 minutes on 6 cores. Results:

| Quantity (page) | Paper | Mine |
|---|---|---|
| admissible triples, S ≤ 4800 / S ≤ 6000 (p. 19) | 3 067 197 199 / 5 992 496 499 | identical |
| Table 3: every entry of every row, all five columns plus local exponents (p. 19) | — | identical, X = 18 … 6000 |
| N(5400), cross-check point (p. 19) | stated as reproduced | 123 559 pairs, 118 769 classes |
| class sizes to 4800: 96 981 / 1627 / 122 / 11 / 1 (p. 19) | — | identical. To 6000: 137 520 / 2287 / 173 / 23 / 2; no size 7 |
| first classes of size 3, 4, 5, 6 at S = 136, 408, 1849, 4600, with members and Λ (Table 2, p. 18) | — | identical; all members confirmed to share Λ |
| 507 of the 582 sums 19 ≤ S ≤ 600 carry a primitive class (p. 19) | — | identical |
| 46 254 primitive pairs ≤ 4800: 7626 dual (16.5%), 4 torsion-type, 38 624 third kind (p. 20) | — | identical |
| dual share 32.9% for S ≤ 200; 1330 non-dual primitive pairs ≤ 600 (p. 20) | — | identical (82/249; 1330) |
| the four torsion-type pairs, all on C_{169/16}, at S = 845, 1183, 2145, 3003 (p. 20) | — | identical; no others ≤ 4800 |
| 669 third-kind pairs ≤ 400, none with P′ = ±mP + T or P = ±mP′ + T, m ∈ {2, 3} (p. 20) | — | identical (669, 0) |
| A(1000), A(2000), A(4000), A(4800) and their local exponents (p. 21) | 4141, 12 512, 35 567, 46 254; 1.64, 1.60, 1.51, 1.48 | identical (1.641, 1.595, 1.507, 1.481) |
| N(X)/X² at 400 and 6000 (p. 20) | 0.0094, 0.0040 | 0.00935, 0.00405 |
| per-sum q, all / primitive (p. 21) | 4.49 / 3.53 | 4.489 / 3.532 |
| cumulative q, all / primitive (p. 21) | 4.56 / 3.63 | 4.557 / 3.625 |
| q on windows [1200,4800], [600,2400], [2400,4800] (p. 21) | 4.44, 4.64, 4.39 | 4.437, 4.642, 4.390 |
| q on gcd(s,6)=1, odd, even, 6 \| s (p. 21) | 4.06, 4.29, 4.61, 4.97 | 4.061, 4.289, 4.609, 4.966 |
| dual q, primitive / all; non-dual q, primitive / all (p. 21) | 2.56 / 3.33; 3.73 / 4.80 | 2.560 / 3.332; 3.728 / 4.798 |
| power-law β; crossover point (p. 21) | 0.587; s ≈ 2100 | 0.5868; s = 2098 |
| holdout 4801–6000, log-power / power (p. 21) | +0.25% / +2.33% | +0.248% / +2.331% |
| holdout 3601–4800, fit on [600,3600] (p. 21) | +0.21% / +2.32% | +0.209% / +2.319% |
| N(6000) − N(4800) (p. 21) | 42 960 | 42 960 |
| 506 pairs D_{u,v} with S ≤ 4800; 27 of them in classes of size ≥ 3 (p. 14) | — | identical |
| copies of D_{u,v}: c_iso X log X − 0.286X for 10^4 ≤ X ≤ 4·10^7; 0.608X at 4800 (p. 14) | — | (count − c_iso X log X)/X = −0.2860, −0.2862, −0.2863, −0.2863, −0.2863 at X = 10^4, 10^5, 10^6, 10^7, 4·10^7; 0.6077 at 4800 |
| 189 lines with \|a\|, \|b\|, \|c\| ≤ 7 meeting the positive triangle, up to permutation and sign (p. 23) | — | 189 |

I also checked:
- The identity in the proof of Proposition 5, by hand. Expanding, it is equivalent to 1/p′ − 1/p = A/B − A′/B′. The proof is correct.
- The torsion arithmetic of Table 1/Table 2: (Λ−1)(Λ−9)q² equals 6721, 1449, 1329601 and 8569, and none is a square. I also checked a and b in Table 1 for Λ = 27/2 and 155/12.

I did **not** rerun:
- the ranks and Selmer groups (no PARI in my sandbox);
- the bidegree-(1,1) search over the 189 lines;
- the "recount through the identity for S ≤ 160" check.

**Every number in Section 6 that I could check is correct, to the digits printed.** There is no computational error.

## FATAL

None.

## MAJOR

**M1 (pp. 21–22, §6.3 last third and §6.4 first paragraph; echoed on p. 4). The holdouts are not evidence for a positive answer to Question E, weak or otherwise.**

The paper says (p. 22): "in both holdouts it predicts within about 0.2%, while the power law over-predicts by about 2.3% … this is weak, non-asymptotic evidence for a positive answer to Question E". The holdouts only measure how concave log n is against log s over a 25% forward extension. They cannot tell an asymptotic exponent of 1 from one above 1. I tested this in three ways.

1. **Laws with asymptotic exponent above 1 fit almost equally well.** I fitted the family n(s) = c·s^{b0}·(log s)^q, with b0 fixed and (c, q) fitted exactly as in the paper (Poisson ML on [600, 4800]). Under this law N(X) has asymptotic exponent 1 + b0.

   | b0 | q | deviance on [600, 4800] | holdout 4801–6000 | holdout 3601–4800 |
   |---|---|---|---|---|
   | 0 (paper's law) | 4.49 | 26 479.2 | +0.25% | +0.21% |
   | 0.1 | 3.73 | 26 480.9 | +0.61% | +0.57% |
   | 0.2 | 2.96 | 26 483.3 | +0.98% | +0.92% |
   | 0.3 | 2.20 | 26 486.3 | +1.34% | +1.28% |
   | 0.5 | 0.67 | 26 494.0 | +2.08% | +2.00% |
   | 0.587 (power law) | ≈0 | 26 498.1 | +2.40% | +2.32% |

   - The deviance moves by less than 2 between b0 = 0 and b0 = 0.1, against a residual deviance of 26 479 on 4199 degrees of freedom. The data are overdispersed by a factor of about 6.3, so the in-sample difference between the paper's two laws, 19, corresponds to about 3 on a χ² scale.
   - A law with N(X) ≍ X^{1.1}(log X)^{4.7} misses the forward window by 0.6%. A law with N(X) ≍ X^{1.2}(log X)^{4} misses it by 1%.
   - The holdout error grows smoothly and monotonically with b0. Nothing singles out b0 = 0.

2. **The criterion prefers laws that are provably false.** The free three-parameter fit c·s^β·(log s)^q on [600, 4800] gives β = −0.25, q = 6.39. On [600, 6000] it gives β = −0.17, q = 5.80.
   - A negative β means N(X) = o(X) asymptotically, which contradicts Theorems 2 and 3.
   - Extrapolating along b0 < 0 would also improve the holdout error, which is already −0.65% at the free optimum.
   - So the window is pre-asymptotic, and the local curvature it shows is stronger than any law consistent with the proven lower bounds can keep up. A criterion that ranks provably false laws highest cannot be cited as evidence about the limit.

3. **Neither two-parameter law is stable across windows.** On sliding windows of width 2400:
   - The log-power exponent q falls steadily for all pairs: 4.56, 4.43, 4.37, 4.39, 4.29, 4.22 from [600, 3000] to [3600, 6000].
   - For primitive pairs it falls from 3.73 to 3.09.
   - The power-law β falls from 0.622 to 0.500.
   - For the one family whose asymptotics are known (the dual pairs, ≍ y(log y)^{≤4} by Proposition 4), the primitive per-sum q is 2.70, 2.60, 2.29, 1.80, 3.11, 2.46 on the same windows. It is not even monotone.

   This extends the paper's own warning on p. 21 and shows that the fitted (log s)^q laws are not stable objects.

The rest of the section is careful. It says that "a finite range bounds the limiting exponent from neither side", that the data "cannot locate" the exponent (p. 4), and that the A(X) figures "are not predictions" (p. 21). The single sentence claiming evidence for E contradicts all of these, and that sentence is the one a reader will quote.

*What resolves it:*
- Delete "weak, non-asymptotic evidence for a positive answer to Question E" and the matching framing in §6.4.
- Say only what the holdouts show: on [600, 6000] the local exponent keeps falling, and a law with this much curvature extrapolates better over a short forward window than a fixed power does.
- State that laws with asymptotic exponent 1.1–1.3 do almost as well. The b0 table above, or a sentence summarising it, would make the point.
- Make the abstract, p. 4 and p. 22 say the same thing. At present p. 4 says the data "cannot locate" the exponent while p. 22 says they are evidence for E.

**M2 (pp. 20–21, §6.3). The fitted exponents are printed with spurious precision and no stated uncertainty.**

- q is printed to three significant figures (4.49, 4.56, 3.53, 3.63, 2.56, 3.33, 3.73, 4.80) and β to three decimals (0.587).
- The paper's own residue-class split moves q from 4.06 to 4.97, and its windows move it by 0.25. I find a further downward drift of 0.34 across sliding windows, and a range of 1.3 for the dual-family q.
- The cumulative least-squares fit on log(N(S) − N(599)) has residuals that are almost perfectly autocorrelated, so it is not independent confirmation of the per-sum fit. Its agreement with the per-sum fit (4.56 vs 4.49) is not a second piece of evidence.
- The Poisson device is acknowledged as a weighting device, but the overdispersion (deviance/dof ≈ 6.3) should be reported. It is what makes deviance comparisons between the two laws uninformative.

*What resolves it:*
- Report q as a range together with its drift across windows; a short table of sliding-window q and β, or a plot of local exponents, would do it.
- Round to what the data support, roughly one decimal for q.
- Say explicitly that the cumulative fit is not independent of the per-sum fit.
- Keep the dual-family comparison (fitted 2.56 against an expected 4), which is the most informative sentence in §6.3, and add that its fitted q is not even stable across windows.

## MINOR

**m1 (p. 19, §6.1). Floating-point grouping: the possibility of collisions is not addressed.**
- Distinct reduced fractions e2/e3 with e3 up to 8·10^9 can in principle differ by about 10^{-20}, far below one ulp of R ∈ (0, 1). So two different rationals can share a correctly rounded double.
- The text says candidate matches are confirmed exactly and classes re-verified. It does not say what happens when a bucket mixes two rationals. Such a bucket has to be split into sub-classes, not just rejected, or the counts are wrong.
- In 41 sums sampled at 4000 ≤ S ≤ 6000 (step 50) I found no such collision. My enumerator groups by exact fractions anyway and reproduces every count, so the published numbers are right.
- Please state how mixed buckets are handled and how many occurred.
- Also, "128-bit cross-multiplication" is more than needed: e2·e3′ < 1.2·10^7 · 8·10^9 < 2^63. This is harmless.

**m2 (p. 19). How independent are the programs, and what was checked for 4801 ≤ S ≤ 6000?**
- "Two independent programs" is not explained: do they differ in algorithm, in language, or in arithmetic?
- For 4801 ≤ S ≤ 6000, the primitive-class column and the class sizes come from one program, checked against the third only at two cumulative points.
- My independent run confirms all of them, so nothing is wrong. The paper should still say what kind of independence it claims, and which program supplies which column of Table 3 above 4800 (for example in a table note).

**m3 (pp. 19, 21). Question E is about A(X), but A(X) is not in Table 3.**
- Question E is stated for N, and the paper says it is equivalent to A(X) = X^{1+o(1)} (p. 4). Yet A appears only in the text, only to 4800, and A(500) and A(2400), which the local exponents need, are not given.
- Add an A(X) column to Table 3, to 6000, and add the row X = 5400, which the text uses as a cross-check.
- My values: A(500) = 1328, A(2400) = 16 565, A(6000) = 63 876, with local exponent log₂(A(6000)/A(3000)) = 1.461. N(5400) = 123 559, Ncl(5400) = 118 769, primitive classes 53 626.

**m4 (p. 20). The m ∈ {2, 3} test needs a rationale or a better replacement.**
- The two triples of a pair have the same sum S, so their naive heights agree to within a bounded factor.
- A relation P′ = ±mP + T with m ≥ 2 would force ĥ(P′) ≈ m²ĥ(P). Such a relation can only occur when the height-difference constant of C_Λ is comparable to log S. That is possible, since H(Λ) ≈ S³, but it is not likely.
- So the null result is close to expected, and the paper should say so.
- A more informative test is whether P and P′ are independent, i.e. whether the regulator of ⟨P, P′⟩ is non-zero. That would distinguish rank-1 curves carrying two multiples of one generator from curves of rank ≥ 2.
- Please also state how torsion was decided. A 12(P ± P′) = O test, as I used, is the natural one.

**m5 (pp. 20–23). The data carry structural information on Question E that is not reported.** I suggest adding the following; none of it is required for acceptance.
- **Coincidences are spread over many curves.** Up to 4800 the 46 254 primitive pairs lie on 36 107 distinct curves C_Λ, and 28 827 of those Λ carry exactly one primitive pair. To 6000: 63 876 pairs on 50 001 curves, with at most 24 pairs on one curve (Λ = 676/55). So the growth of N comes mainly from the number of curves that carry a small coincidence, not from many points on few curves. Question E is then about how often a fibre of small height has two small positive points.
- **The dual share stops falling.** By window of S, the dual share of primitive pairs is 32.9% (≤ 200), 22.7%, 18.7%, 16.7%, 16.1%, 15.3%, and 15.4% (4800–6000).
- Why the stable share matters: the dual family is provably between y·log y and y(log y)^4. A stable share means the third-kind pairs, about which nothing is proved, grow at a comparable rate in this range. That observation is more directly relevant to E than any curve fit.

**m6 (pp. 22–23, §6.4 heuristic). The heuristic covers only one mechanism.**
- The heuristic considers only rational surfaces parametrised by forms of degree d in m variables.
- But the variety of pairs is a quintic hypersurface in P⁴, whose canonical class is trivial; the paper itself cites Schoen's Calabi–Yau threefolds. Every pair lies on a fibre C_Λ × C_Λ, an abelian surface, over the Λ-line.
- On such a variety the generic expectation off special subvarieties is very small. The growth is carried entirely by accumulating subvarieties: the dual surface, and the positive-rank fibres that hold 83.5% of the pairs.
- "A positive answer would require that the variety contain no such surface" therefore states one necessary condition from one mechanism. The fibration over Λ, which is where most pairs actually live (m5), is a second mechanism that the heuristic does not address.
- The section title "What Question E Would Require" promises more than the section delivers. Either retitle it or add the fibration viewpoint in a sentence or two.

**m7 (p. 20). The four torsion-type pairs.**
- By Lemma 4, every positive point of C_{169/16} yields such pairs. Say so.
- Note that, since C_{169/16} has rank 1 and heights grow quadratically in the multiple, this mechanism contributes only O(log X) pairs per curve.
- The reader then knows that the second kind is negligible for Question E, rather than merely unexplored.

**m8 (p. 14, Section 4, but numerical).** The secondary term "−0.286X to three digits" is right: I get −0.2863 for all X from 10^5 to 4·10^7. It is a computable constant, ∫(A_iso(y) − c_iso·y)y^{-2}dy plus the floor correction, and could be stated as such rather than as a numerical fit.

## Presentation (Section 6 and Figure 1)

- **P1 (p. 19).** Table 3 floats to the top of p. 19, above the heading of Section 6, so the reader meets it before the section that defines it. Anchor it after §6.1.
- **P2 (p. 22, Figure 1(b); checked on the rendered page).**
  - The plot stops at S = 4800, although data to 6000 exist and the holdout is the section's main argument.
  - The dashed fit is drawn only over its own training window, where it cannot be told apart from the heavy curve.
  - The power-law competitor is not shown.
  - A panel of the ratio data/model − 1 against s, for both laws, with the training/holdout boundary marked, would show what the text claims, or its limits (M1).
  - The caption should give q and the fitting window.
- **P3 (p. 21).** "These describe a finite range; they are not predictions" sits a few lines after two holdout predictions. Reword so the two passages do not seem to contradict each other.
- **P4 (p. 20).** "We sorted the 46 254 primitive pairs accordingly": "classified" is meant.
- **P5 (p. 21).** The paragraph moves between per-sum and cumulative fits, all and primitive pairs, dual and non-dual, windows and residue classes, all as running text. A small table would make the numbers easier to compare. If M2 is followed, most of them can go.
- **P6 (p. 19).** "(and 8 · 10^9 for S ≤ 6000)" makes the 2^53 argument parenthetical for the range that matters most. State the bound once for S ≤ 6000.

## Recommendation

**Minor revision** (as far as Section 6 is concerned). Confidence: high on the computations, which I reproduced independently and exactly, and moderately high on the statistical points, which I backed with my own fits.

- The enumeration, the tables, the classification and Proposition 5 are correct. Every number I could check matches mine to the printed digit.
- The only substantive defect is interpretive: the holdouts are presented as evidence for a positive answer to Question E (M1), and the fitted exponents are printed with spurious precision (M2). Both are fixed by rewording and by reporting the instability that is already in the data. No new mathematics is needed.
- I would not accept the paper with the sentence on p. 22 as it stands.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Remove the "evidence for a positive answer to Question E" claim (p. 22). Say what the holdouts show (local concavity, a falling local exponent) and that laws with asymptotic exponent 1.1–1.3 do almost as well. Make p. 4, p. 22 and the abstract consistent. |
| M2 | Report q and β as window-dependent ranges with their drift, at about one decimal. Note the overdispersion and that the cumulative fit is not independent. Keep the dual-family caution and extend it. |
| m1 | State how mixed double-precision buckets are split, and how many occurred. |
| m2 | Describe how the programs are independent; say which program supplies which Table 3 column for S > 4800. |
| m3 | Add an A(X) column and the X = 5400 row to Table 3, to 6000. |
| m4 | Justify the m ∈ {2, 3} test or replace it by an independence (regulator) test; state the torsion test used. |
| m5 | Optional: report the pairs-per-Λ distribution and the dual share by window. |
| m6 | Add the fibration over Λ to the §6.4 heuristic, or retitle the section. |
| m7 | Say that the torsion-type pairs come from the rank-1 curve C_{169/16} and contribute O(log X). |
| m8 | Optional: identify −0.286 as an explicit constant. |
| P1–P6 | Editorial, as listed. |

---

My code and outputs are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/N-d-computational-enumeration-referee/scratch/`:
- `code/enum.cpp`: exact enumerator
- `code/classify.py`: exact group-law classifier
- `code/fits.py`, `code/alt.py`, `code/dualfit.py`: fits and holdouts
- `code/iso.c`: isosceles copies
- `code/coll.cpp`: double-collision check
- `code/summary.py`: Table 3 summary
- `run/per_all.txt`: per-sum counts to 6000
- `run/side_all.txt`: all primitive pairs and all classes of size at least 3
