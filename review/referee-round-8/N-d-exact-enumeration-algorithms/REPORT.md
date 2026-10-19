<!-- Round 8 N-d referee report: returned text saved verbatim; the reviewer could not write files -->

Writing REPORT.md was refused, so the full report is below. I reran every computation I could with my own code: an independent C enumeration to S = 6000, exact rational group law, sympy and PARI/GP 2.17.2. Every number I could recompute in the note is correct, and I found no fatal error. The two major issues are both in the statistics of Section 6.3. My code is in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/N-d-exact-enumeration-algorithms/scratch/` (enum.c, analyse.py, grp.py, mult.py, ranks.py, alg.py, iso.c, prop4.py, fits.py, boot.py).

---

# Referee report for *Integers*

**Manuscript:** "Triples with Equal Sum and Equal Reciprocal Sum" (22 pp.)
**Referee brief:** Section 6 (the enumeration and its completeness, the counts, the fits and their uncertainties, the holdout, the heuristic and Question E), plus every computation anywhere in the note. I rewrote and reran these computations myself.
**Placeholders** (author contributions, AI-use statement, Zenodo DOI, preprint identifier) are treated as known. I did not consult the code deposit. Everything below rests on the PDF and on my own code.

## 1. Summary

The note studies unordered pairs (and classes) of triples of positive integers that share both their sum S and their reciprocal sum R. It identifies them with positive rational points on the cubic pencil C_Λ: e1e2 = Λe3 (Bremner–Guy–Nowakowski), and shows that reciprocation is translation by a 2-torsion point. It determines the torsion subgroups and which torsion points are positive (Theorem 1, Lemma 4), and proves three lower bounds:
- N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X, from the isosceles family;
- N(X) ≫ X(log X)², from the dual family;
- an upper bound n(S) ≪ S^{2+ε}.

Through Schinzel's method it gets classes of every size, and through Browning–Sofos it bounds the dual family by O(X(log X)⁵).

Section 6 reports an exhaustive enumeration up to S = 6000 and fits growth laws to the counts. It ends by asking whether N(X) = X^{1+o(1)} (Question E), with a heuristic about which subvarieties of the pairs variety could prevent this.

## 2. Significance

The arithmetic part is modest but sound and honestly credited. Most of the geometry is attributed to [3], [1], [16]. The new pieces are:
- the positive-torsion classification;
- the counting function and its bounds;
- the enumeration itself.

The enumeration is a real contribution: it is correct, and I reproduced it exactly. It would be a useful dataset for an OEIS-style record. Section 6.3, the fits, is the weakest part. Its numbers are right, but its uncertainty statements understate how little the data constrain the growth law (M1, M2). Question E is a reasonable open question. The heuristic in 6.4 is clearly labelled as heuristic.

## 3. Correctness, and what I recomputed

All of the following was done with my own code:
- a multithreaded C enumerator, which hashes the double of e2/e3 and then confirms every collision by exact cross-multiplication;
- Python with exact `Fraction` arithmetic;
- sympy;
- PARI/GP 2.17.2 through cypari2.

### 3.1 Enumeration, Section 6.1 and Table 2 (pp. 15–17)

I enumerated all admissible 2 ≤ a ≤ b ≤ c with a + b + c = S ≤ 6000 and grouped them by exact R. This was independent of the authors' programs and took 4.6 min wall time on 4 threads.

| claim | paper | mine |
|---|---|---|
| admissible triples, S ≤ 4800 | 3 067 197 199 | 3 067 197 199 |
| admissible triples, S ≤ 6000 | 5 992 496 499 | 5 992 496 499 |
| every row of Table 2 (N, N_cl, primitive classes, largest size, local exponent) | as printed | **identical in every entry**, including 2.524, 2.069, …, 1.603, 1.585 |
| class sizes ≤ 4800 | 96 981 / 1627 / 122 / 11 / 1 | identical; these also sum to N_cl = 98 742 and give N = 102 719 |
| no class of size 7 up to 6000 | yes | yes (maximum is 6) |
| sums 19 ≤ S ≤ 600 with a primitive class | 507 of 582 | 507 of 582 |
| primitive pairs ≤ 4800 | 46 254 | 46 254 |
| dual primitive pairs | 7626 (16.5%); 32.9% for S ≤ 200 | 7626 (16.49%); 32.93% |
| non-dual primitive pairs ≤ 600 / ≤ 400 | 1330 / 669 | 1330 / 669 |
| N(X)/X²: 0.0094 at 400, 0.0040 at 6000 | — | 0.00935, 0.00405 |

- **Table 1 (p. 16):** every member of every row, every S and every Λ is confirmed. The size-4 class at 408 is 3× the class at 136 together with (65, 70, 273), as stated.
- **Lemma 1:** I brute-forced all triples with a ≥ 1 for S ≤ 300. No coincidence involves a triple with R ≥ 1, so restricting the enumeration to admissible triples loses nothing.
- **Hash argument (p. 15):** sound. e3 ≤ (S/3)³ < 2^53, so correct rounding of e2/e3 sends equal rationals to equal doubles. The exact check then separates distinct rationals that share a double. 64-bit cross-multiplication already suffices, since e2·e3′ < 10^17; 128-bit is harmless.

### 3.2 Torsion-type pairs (p. 16, Lemma 4, Theorem 1)

I implemented the chord–tangent law on the plane cubic with flex O = (1 : −1 : 0) in exact arithmetic.

- **Torsion-type pairs:** I scanned all Λ of the primitive pairs up to 4800 for Z/12 curves. Only C_{169/16} (r = −4) carries non-dual pairs on a curve with r < 0, and these are exactly the four pairs listed at S = 845, 1183, 2145 and 3003. For each, the partner is P + T for a torsion point T of order 4 or 12, as claimed.
- **Non-dual pairs on r > 0 curves:** these do occur, on C_{169/9}, C_{361/36}, C_{1369/144} and C_{1521/100}. Consistently with Lemma 4, they are not of torsion type.
- **Torsion orders in Theorem 1(iv):** confirmed on C_{27/2}, where (1:4:4) and (4:1:4) have order 6 and (4:4:1) has order 2. Also confirmed on C_{49/4}, where the orderings (1:4:2) and (4:1:2), whose last coordinate is the middle term, have order 4 and the other four have order 12.
- **Multiplication test (pp. 16–17):** none of the 669 non-dual primitive pairs with S ≤ 400 satisfies P′ = ±mP + T or P = ±mP′ + T with m ∈ {2, 3} and T in the full torsion group. Confirmed.
- **Theorem 4 example (p. 15):** 3P = (162833463 : 723926268 : 287876366) and P + T2 = (9 : 4 : 2) on C_{155/12}. Confirmed.

### 3.3 Ranks, torsion, conductors, root numbers (pp. 15–16)

I worked on the minimal model of E_Λ. `ellrank` bounds coincide in every case.

| Λ | conductor | root number | torsion | rank |
|---|---|---|---|---|
| 27/2 | 90 | +1 | Z/2×Z/6 | 0 |
| 155/12 | 6250530 | +1 | Z/6 | 2 |
| 68/5 | 82110 | +1 | Z/6 | 2 |
| 1849/120 | 1715185290 | −1 | Z/6 | 3 |
| 230/21 | 41388270 | −1 | Z/6 | 3 |
| 169/16 | — | — | Z/12 | 1 |
| 49/4 | — | — | Z/12 | — |

All values match the paper. I did not redo the authors' explicit 2-isogeny Selmer-set sizes (4/1, 4/4, 8/4, 16/2, 8/2). Their product relation 2^r = |α(Γ)||ᾱ(Γ̄)|/4 is consistent with the ranks.

### 3.4 Algebra (Proposition 2, Section 1, Section 4), checked in sympy

- The maps C_Λ ↔ E_Λ send each curve to the other, and both compositions are the identity modulo the curve equation.
- Δ = 2^12 Λ²(Λ−1)³(Λ−9).
- The substitution into the Tate normal form satisfies it identically (p. 3).
- (1:4:4) ↦ (−6, 45) at Λ = 27/2.
- MacLeod's identity R/r = (Λ−1)/4 holds (p. 5).
- The six dual cubic forms span a 5-dimensional space (p. 14).
- The heat constant (S + R − 2)/12 = χ/6 + Σ(m_i² − 1)/(12m_i) is correct (p. 2).

### 3.5 Section 4 numerics

- **Isosceles family:** there are 506 pairs D_{u,v} with S ≤ 4800, against c_iso·4800 = 505.66. Of these, 27 lie in classes of size ≥ 3.
- **Copies of the isosceles pairs:** their count minus c_iso X log X equals −0.2852X at 4800 and −0.2860X to −0.2863X for 10^4 ≤ X ≤ 4×10^7, which matches the paper's −0.286X. The count is 0.6077X at 4800.
- **Constants and counting steps:** the factor 18c_iso ≈ 1.90 is right. I also re-derived the constants c_iso = 3 log 2/(2π²), c_A = 3/(32π⁴) and 3/(128π⁴), and the steps of the box and Möbius counting. I found no error.

### 3.6 Proposition 4 (p. 17)

- The identity (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′ is verified algebraically.
- I recounted n(S) through the factorisation for every S ≤ 100 (the authors went to 160), using p < p′, all signed divisors and integrality of the roots. It matches the enumeration exactly.

### 3.7 Lines search (p. 20)

There are 189 lines ax + by + cz = 0 with coprime |a|, |b|, |c| ≤ 7 that meet the open positive triangle, up to permutation and sign. Confirmed. I could not rerun the family test itself, because it is described only by reference to the deposit.

### 3.8 Fits, Section 6.3 (p. 18), reproduced

I reproduced the Poisson maximum-likelihood fit of n(s) = c(log s)^q on [600, 4800] and the least-squares fit to the cumulative counts.

| quantity | paper | mine |
|---|---|---|
| q, all pairs (per sum / cumulative) | 4.49 / 4.56 | 4.489 / 4.557 |
| q, primitive pairs (per sum / cumulative) | 3.53 / 3.63 | 3.532 / 3.625 |
| q, dual pairs (primitive / all) | 2.56 / 3.33 | 2.560 / 3.332 |
| q, non-dual pairs (primitive / all) | 3.73 / 4.80 | 3.728 / 4.798 |
| q on windows [1200,4800] / [600,2400] / [2400,4800] | 4.44 / 4.64 / 4.39 | identical |
| power-law exponent β | 0.587 | 0.5868 |
| log-likelihood difference ΔLL | 9.5 | 9.48 |
| Pearson dispersion | 6.8 | 6.76 |
| ΔLL / dispersion | 1.4 | 1.40 |
| block-bootstrap spread of q | 0.06 | 0.055 |

- **Holdout, 4801–6000:** the observed count is 42 960. The log-power law predicts 43 066, so the observed count is 0.25% below it, which is 0.20 SD. The power law predicts 43 961, so it overshoots by 1001. That is 2.33% of the observed count, or 2.28% of the prediction, and 1.86 SD.

**Verdict on the computations:** every number in the note that I could recompute is correct. I found no computational error.

## 4. FATAL

None.

## 5. MAJOR

**M1 (pp. 18–19, also p. 1 and p. 19 §6.4). The stated uncertainties of the fits and of the holdout are too small, and the claim that the holdout "separates [the laws] a little" does not survive a fuller error budget.**

1. **The holdout yardstick leaves out parameter uncertainty.** The paper measures the holdout discrepancy against √(φ · count) = 540, which is Poisson noise only. It ignores the uncertainty of the fitted trend being extrapolated. I propagated the quasi-Poisson covariance, dispersion × inverse Fisher information, to the 4801–6000 total:
   - standard error of q: **0.133**, which is 2.4× the reported block-bootstrap "spread" of 0.06;
   - standard error of the extrapolated total: **593 (1.38%)** for the log-power law and **625 (1.42%)** for the power law. Each is larger than the 540 used.

   With both sources combined (about 830), the power law's miss of 1001 is about **1.2 SD**, not 1.9. The holdout therefore does not separate the two laws. The phrases "separate them a little" (p. 18) and "slightly less well on the sums 4801 to 6000" (p. 19) should go.

2. **The bootstrap "spread" is not informative, and the authors half-admit it.** The divisor structure (Lemma 5) means n(s) depends strongly on the arithmetic of s. Refitting the same model on residue classes of s within the same window gives very different exponents:

   | sums used | q |
   |---|---|
   | gcd(s, 6) = 1 | 4.06 |
   | s odd | 4.29 |
   | s even | 4.61 |
   | 6 ∣ s | 4.97 |

   That range is about 0.9, fifteen times the quoted spread of 0.06. The Pearson residuals also have lag-1 autocorrelation −0.33, so the independence that underlies both the quasi-likelihood comparison and the holdout SD fails. The 50-sum block bootstrap scrambles exactly this structure. A number that small next to "q = 4.49" invites a reader to read q as known to ±0.06, whatever the disclaimer says.

3. **The two laws are locally the same model on this range, so no test on [600, 6000] can separate them.** The log-slope of (log s)^q is q/log s. It equals β = 0.587 at log s = q/β ≈ 7.65, that is s ≈ 2100, the geometric centre of the fitting window. The two fits are tangent there and differ only through the curvature term −q/(log s)², and over log s ∈ [6.4, 8.7] that difference is a few per cent in the counts. This should be stated in place of the likelihood and holdout comparisons. It makes the authors' own conclusion ("a finite range bounds the limiting exponent from neither side") precise, instead of leaving it as a caveat attached to statistics that seem to say more.

*What resolves M1:*
- Report q with an honest range: the window-to-window and residue-class variation, or a quasi-Poisson SE together with the residue-class fits.
- Either drop the "spread" or give it alongside these.
- Recompute the holdout yardstick including parameter uncertainty, or drop the SD language and just report the two percentages.
- Add the tangency remark.
- Delete "separate them a little" and "slightly less well".

**M2 (p. 18). The per-sum model is misspecified, and that distorts the exponent comparisons that are used as evidence.**

By Lemma 5, n(s) = Σ_{d|s} n_prim(s/d). So the expected count is not a smooth function of s: it carries an arithmetic factor of about Σ_{d|s} d^{-1}(…). A single smooth trend fitted to n(s) estimates a weighted mixture over residue classes. The 4.06–4.97 spread above shows how strongly this mixture depends on which sums are in the window.

The statement "Scaling accounts for the difference of about one" (4.49 against 3.53) is correct at the level of heuristic asymptotics. Within this misspecified per-sum model, however, it is partly a coincidence. The paper's own dual-family test (fitted 2.56 against an expected 4) already shows that the fitted q do not estimate asymptotic exponents.

*What resolves M2:* fit the smooth objects only:
- the primitive cumulative count A(y);
- N(X), as in the cumulative fit;
- or n_prim(s), which has no divisor sum.

Present the all-pairs per-sum q, if at all, only as a descriptive number with the residue-class caveat. Alternatively, cut 6.3 back to the local-exponent column of Table 2, the ratio N(X)/X², and the dual-family cautionary example. On this data those are the informative content.

## 6. MINOR

- **m1 (p. 16):** For 4801 ≤ S ≤ 6000 the cross-check between programs is at two checkpoints only (S = 5400 and 6000), and the "third enumeration" is not described at all. My independent run confirms every S, but the paper should:
  - say what the third program does;
  - publish per-S counts, or a checksum of the per-S (n(S), classes) vector, so that the next reader can verify it the same way.
- **m2 (p. 15):** The hash argument relies on IEEE-754 correctly rounded division. The text should say that no fast-math or contraction flags were used, and on which platform and compiler.
- **m3 (p. 18):** "matched to within 0.25%" uses the prediction as the base, while "exceeded by 2.33%" uses the observed count; relative to the prediction it is 2.28%. Use one base for both.
- **m4 (p. 18):** "The enumeration is complete, so there is no sampling error" sits awkwardly next to a Poisson or quasi-likelihood framework that presupposes a stochastic model. Say explicitly that the Poisson model is a working device for weighting, not a model of the data.
- **m5 (p. 18):** "with q = 4.5 fitted" should be q = 4.49, or say that it is rounded.
- **m6 (p. 20):** The lines search ("grouped the lines by the discriminant of the branch values of Λ restricted to them and tested each candidate pair exactly") cannot be reproduced from the text. Give the test criterion explicitly: when two restrictions of Λ to lines are Möbius-equivalent, and how equivalence was decided. Also state that the search is exhaustive in its box.
- **m7 (p. 15):** The rank verification by "an independent 2-isogeny descent in exact arithmetic" depends on code in the deposit. Either list the generators that fill the Selmer images, perhaps in a short table in the deposit README cited here, or state that the descent output is in the deposit.
- **m8 (pp. 19–20):** "We have not searched for one" (a d = 2, m = 3 surface). Since Question E turns on it, add one sentence on why a search is non-trivial, or what a cheap test would be. For example: look for a quadratic-form parametrisation through the observed non-dual pairs, or test whether the non-dual primitive pairs cluster on low-degree surfaces by fitting.
- **m9 (p. 4):** In "Equivalently (with Theorem B)", the equivalence A(y) = y^{1+o(1)} ⇔ N(X) = X^{1+o(1)} uses only A ≤ N, Equation (2) and partial summation; Theorem B supplies only the lower half. One clause would make this clear.
- **m10 (data availability, p. 20):** The reproducibility claims cannot be refereed from the PDF:
  - "one command reruns every check";
  - "verified symbolically" (Proposition 2, p. 7; the span claim, p. 14);
  - the lines list.

  The deposit must be accessible to referees at resubmission. This is not a criticism of the placeholder itself.

## 7. Presentation

- **P1 (p. 19, Fig. 1(b)):** The caption says S ≤ 4800, but the holdout data run to 6000. Plot up to 6000 and mark 4801–6000 as held out, so the reader can see the extrapolation.
- **P2 (p. 19, Fig. 1(a)):** I checked it and it is correct: the (1,1,4)-type points sit near the vertices (orange) and the (1,4,4)-type points near the edge midpoints (dark). The caption could say which is which geometrically.
- **P3 (p. 17, Table 2):** Add a column for primitive pairs. They are used in 6.1 (46 254) and 6.3 but tabulated nowhere. Consider adding X = 5400, which is the second cross-check point.
- **P4 (p. 18):** The paragraph mixes three things: the fit procedure, the cautionary dual-family example and the holdout. After M1–M2 it would read better split as:
  1. what is measured, namely the local exponents;
  2. why smooth fits cannot decide, namely tangency and the dual-family example;
  3. the holdout percentages.
- **P5 (p. 1, abstract):** "a local growth exponent falling from about 2 near 500 to 1.58 at 6000; the limiting exponent is open" is accurate and appropriately modest. Keep it, and keep any revised 6.3 at the same level of claim.

## 8. Recommendation

**Minor revision. M1 and M2 are mandatory.**

M1 and M2 are filed as MAJOR because they are must-fix items. The fixes are confined to roughly one page of Section 6.3 and need no new mathematics. The enumeration is correct and complete as far as anything checkable in the PDF goes. I reproduced every reported count, class, rank, torsion group, conductor, root number and fit value independently. The underlying arithmetic in Sections 2–5 is also correct in every place I tested numerically or symbolically.

**Confidence:** high on correctness, since everything was recomputed independently; moderate-to-high on the recommendation.

## 9. What resolves each issue

| issue | resolution |
|---|---|
| M1 | Include parameter uncertainty in the holdout, or drop the SD language. Replace the 0.06/0.08 "spreads" with window and residue-class ranges. Add the tangency remark (q/log s = β at s ≈ 2100). Delete "separate them a little" and "slightly less well". |
| M2 | Fit only smooth objects (A(y), N(X), n_prim). Label the all-pairs per-sum q as descriptive, with the residue-class caveat, or remove it. |
| m1 | Describe the third program; publish per-S counts or a checksum. |
| m2 | State the platform and compiler, and that no fast-math was used. |
| m3 | Use one percentage base. |
| m4 | One sentence: the Poisson model is a working device for weighting. |
| m5 | 4.49, or "rounded". |
| m6 | State the line-pair test criterion and that it is exhaustive. |
| m7 | Point to the descent generators and output in the deposit. |
| m8 | One sentence on searching for a d = 2, m = 3 surface. |
| m9 | One clause on what Theorem B contributes. |
| m10 | Make the deposit available to referees. |
| P1–P5 | As stated. |
