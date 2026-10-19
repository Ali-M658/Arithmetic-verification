<!-- N-d referee (points of bounded height), round 7: returned text saved verbatim; the reviewer could not write files -->

I couldn't save the report: writing `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/N-d-points-of-bounded-height/REPORT.md` was refused (subagents may not write report files). The full report follows.

My enumeration code and outputs are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/N-d-points-of-bounded-height/scratch/code` and `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/N-d-points-of-bounded-height/scratch/out`.

---

# Referee report for Integers: "Triples with Equal Sum and Equal Reciprocal Sum"

**Scope of this report.** Sections 4 and 6 (the lower bounds and their constants, the enumeration, the upper bound, the growth fits and their uncertainties, Question E), plus every computation in the note. I recomputed independently wherever I could. The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifier) are taken as known. Page numbers are those printed on the rendered PDF, which I read as images.

## Summary

The note studies unordered pairs of positive-integer triples with equal sum S and equal reciprocal sum R. Such pairs are positive rational points on one fibre C_Λ, Λ = SR, of the Beauville pencil (x+y+z)(xy+yz+zx) = Λxyz. Reciprocation acts on C_Λ as translation by the 2-torsion point T₂.

The parts I was assigned contain:

- an exact formula N(X) = Σ_D ⌊X/S_D⌋ over primitive pairs (Lemma 3);
- a lower bound c_iso X log X from the isosceles family D_{u,v} (Theorem 2);
- a lower bound (3/(128π⁴)) X (log X)² from the "dual family" x ↦ (e₂x, e₁(bc,ca,ab)) (Lemma 4, Theorem 3);
- an upper bound n(S) ≪ S^{2+ε} (Proposition 4);
- an exhaustive enumeration to S = 6000 (Table 2);
- Poisson and log-power fits of growth with block-bootstrap errors (§6.3);
- the question whether N(X) = X^{1+o(1)} (Question E, §6.4).

## Significance

The arithmetic content of Sections 4 and 6 is modest but appropriate for Integers. The enumeration is careful and is a real contribution. However, the main structural observation that the note is missing changes how Sections 4 and 6.4 should be written.

The dual family is the set of rational points of bounded anticanonical height on a smooth quartic del Pezzo surface with Picard rank 5 over Q. That surface has a conic bundle with a rational section. Manin-type results for such surfaces (Frei–Loughran–Sofos 2018; Browning–Sofos 2019) therefore give the true order of the dual family up to constants, namely y(log y)⁴ primitive pairs. The positivity condition still needs to be checked for the lower bound (see M1). This order is much larger than the note's (log)² result, and it contradicts the statement on p. 16 that the order of the dual family "is not known".

## Correctness, and what I recomputed

**1. Exhaustive enumeration (my own C program, written independently of the authors' code).**

- Method: for each S, sort the admissible triples by the correctly rounded double of e₂/e₃ (radix sort), then group exactly inside runs of equal keys by integer cross-multiplication.
- Run: all S ≤ 6000, in 8 processes, about 2 minutes.
- Every number in Table 2 is reproduced exactly: all 13 rows, all six columns, including every local exponent.
- Also reproduced:
  - the triple totals 3 067 197 199 (S ≤ 4800) and 5 992 496 499 (S ≤ 6000);
  - the class-size histogram up to 4800: 96 981 / 1627 / 122 / 11 / 1;
  - no class of size 7 up to 6000;
  - the first classes of sizes 3–6 at S = 136, 408, 1849, 4600, with exactly the members and Λ listed in Table 1;
  - 507 of the 582 sums 19 ≤ S ≤ 600 carry a primitive class;
  - 46 254 primitive pairs up to 4800, of which 16.5% are dual (32.9% up to 200);
  - 1753 primitive pairs up to 600, of which 423 are dual;
  - 669 non-dual primitive pairs up to 400;
  - 506 isosceles pairs D_{u,v} with S ≤ 4800, of which 27 lie in classes of size ≥ 3;
  - N(X)/X² = 0.00935 at X = 400 and 0.00405 at X = 6000.

**2. Lemma 1.** I enumerated all triples (including a = 1) with S ≤ 250 and grouped them by exact R. No coincidence involves a triple with R ≥ 1.

**3. Proposition 4 identity.** I checked (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′ algebraically. I then recounted n(S) by running through the factorizations of the right-hand side, for 18 ≤ S ≤ 120. This matches the enumeration exactly.

**4. Theorem 2.**
- I rederived |Ω| = (log 2)/6, the residue-class bookkeeping (#U/8) and c_iso = 3 log 2/(2π²) = 0.10534.
- Direct counts of A_iso(y): 506 at 4800 (c_iso·4800 = 505.7) and 4 213 811 at 4·10⁷ (c_iso·X = 4 213 830).
- The number of copies kD_{u,v} minus c_iso X log X, divided by X, is −0.2852, −0.2860, −0.2862 and −0.2863 for X = 4800, 10⁴, 10⁵ and 4·10⁷. The count at 4800 is 0.6077X. The text's figures (−0.286 and 0.608) are confirmed.

**5. Theorem 3.** I checked every inequality and the constant chain:
- (1/6)·(3/(2π²))·(3/π²)·(1/8) = 3/(32π⁴);
- the final constant 3/(128π⁴);
- the crossover log X > 128π⁴c_iso/3 ≈ 437.8.

The proof is correct, but the constant is needlessly weak (m1).

**6. Statistics in §6.3.** I recomputed these with my own Poisson IRLS fitting.

Per-sum log-power exponent q (Poisson maximum likelihood on 600 ≤ s ≤ 4800):

| Subset | All pairs | Primitive pairs |
|---|---|---|
| All coincidences | 4.489 | 3.532 |
| Dual pairs | 3.332 | 2.560 |
| Non-dual pairs | 4.798 | 3.728 |

Other quantities:
- Cumulative fits: q = 4.557 (all pairs) and 3.625 (primitive).
- Pure power law: β = 0.587.
- Log-likelihood difference between the two laws: 9.48. Pearson dispersion: 6.76. Scaled difference: 1.40.
- Window dependence: q = 4.437, 4.642 and 4.390 on [1200,4800], [600,2400] and [2400,4800].
- The authors' block-50 bootstrap gives standard deviations 0.055 / 0.075 (all pairs) and 0.076 / 0.109 (primitive), matching their ±0.06 / 0.08 / 0.08 / 0.11.

Every number in §6.3 is reproduced. My objection is to what those numbers are taken to mean (M2).

**7. PARI/GP 2.17.2 (cypari2) checks.**
- (1:4:4) maps to (s, η) = (−6, 45) on E_{27/2}.
- ellrank gives ranks 0, 2, 3, 3, 2 for Λ = 27/2, 68/5, 1849/120, 230/21, 155/12. Lower and upper bounds coincide in each case.
- Torsion is Z/2×Z/6 for 27/2 and Z/6 for the others.
- Root numbers are +1, +1, −1, −1, +1.
- 3P for P = (4:9:18) on C_{155/12} is (162833463 : 723926268 : 287876366), as stated.
- On C_{49/4}, the orderings of (1,2,4) have orders 12, 4, 12, 12, 12, 4, with order 4 exactly when the middle term is last. On C_{27/2}, (1:4:4) has order 6 and (4:4:1) and (1:1:4) have order 2. This agrees with Theorem 1(iv).
- For all 1330 non-dual primitive pairs with S ≤ 600, neither P′ − P nor P′ + P is torsion.
- For all 669 non-dual primitive pairs with S ≤ 400, no relation P′ = ±mP + T or P = ±mP′ + T holds with m ∈ {2, 3}.
- The MacLeod substitution identity on p. 4 checks symbolically.

**Not reproduced:**
- the 2-isogeny Selmer orders. Their products are consistent with the stated ranks, and ellrank agrees, but ellrank is the authors' own tool, so this is not an independent check;
- the search over 189 lines (§6.4), which is not specified precisely enough to rerun (m9).

**Verdict on correctness.** I found no mathematical error in Sections 4 and 6, and no wrong number anywhere in the note.

## FATAL

None.

## MAJOR

**M1 (pp. 11–12, 16–18; abstract; Theorem B). The dual family is a quartic del Pezzo surface, and its order of growth is known. Theorem 3 is far from the truth, and "its exact order is not known" (p. 16) is not correct as stated.**

The six entries of the dual pair, e₂(a,b,c) and e₁(bc,ca,ab), are cubic forms. All of them vanish at the three coordinate vertices and at (1:ω:ω²) and (1:ω²:ω). They satisfy one linear relation: (sum of the first three) = (sum of the last three) = e₁e₂.

I checked symbolically that they span the full 5-dimensional space of plane cubics through these five points. No three of the points are collinear. So x ↦ D(x) is the anticanonical map of X = Bl₅P², a smooth quartic del Pezzo surface in P⁴.

Two further facts follow:

- **The height on X is the reduced sum.** For primitive x, the reduced pair is exactly the image point with coprime coordinates. For positive points, S_D is within a factor 3 of its largest coordinate. So S_{D(x)} is, up to a bounded factor, the anticanonical height of x on X. This is exactly the "cancellation of a common factor" that the authors mention and then discard after Theorem 3.
- **X has Picard rank 5 and a conic bundle with a rational section.** Over Q there are three rational blown-up points and one conjugate pair, so the Picard rank is ρ = 5. The pencil of lines through (1:0:0) — the authors' own "conic bundle" of Lemma 4 — is a conic bundle on X, and the exceptional curve over (1:0:0) is a rational section of it. Its degenerate fibres all split: z = 0, y = 0, and the degree-2 point y² + yz + z² = 0. So ρ = 2 + δ₀ = 5, consistent with the count above.
- **Lines carry no positive points.** The 16 lines are the 5 exceptional curves, the 10 lines through two of the points, and the conic e₂ = 0 through all five. None of them contains a positive point.

Two theorems now apply:

- **Browning–Sofos** (arXiv:1609.09057, Math. Ann. 2019, Thm 1.1): c₁B(log B)^{ρ−1} ≤ N_U(B) ≤ c₂B(log B)^{ρ−1} for any quartic del Pezzo surface over Q with a rational point and a conic over Q.
- **Frei–Loughran–Sofos** (arXiv:1609.04330, Proc. LMS 2018, Thms 1.1 and 1.6) already gives the lower bound when ρ ≥ 4, for any nonempty Zariski-open set.

Consequences:

- **Upper bound (unconditional).** The number of primitive dual pairs with S_D ≤ y is O(y(log y)⁴). By Lemma 3, the dual family contributes O(X(log X)⁵) to N(X).
- **Lower bound.** The same order, y(log y)⁴, should hold for positive points. Positivity is an open real condition, and Manin–Peyre predicts a positive proportion. The section-bearing conic-bundle setting is the easiest case of the FLS method, and FLS Thm 4.1 already carries a real region D at the infinite place. The authors must either verify the positive-region lower bound (preferably) or state it as conditional.

If the lower bound holds, then N(X) ≫ X(log X)⁵. That replaces the second half of Theorem B and makes the comparison "exceeds the first bound only when log X > 438" moot.

This also matters for §6.3. The note itself observes that the dual primitive pairs fit q = 2.56 ± 0.20, meaning A_dual(y) ≈ y(log y)^{2.56}. My recomputed local exponent of A_dual is 1.35 at 6000, which matches y(log y)³ rather than y(log y)⁴. But the proven order is y(log y)⁴. So on a subfamily whose answer is known, the fitted log-power is seven quoted standard errors below the truth. This is the cleanest possible demonstration that the fitted q values are not estimates of asymptotic exponents (see M2).

The Manin picture also fits Question E well. For X(log X)^k, the local exponent on [X/2, X] is 1 + k·log(log X / log(X/2))/log 2. With k = 5 this gives 1.80, 1.72, 1.65 and 1.60 at X = 750, 1500, 3000 and 6000. Table 2 (with N(375) and N(750) recomputed) gives 1.85, 1.74, 1.66 and 1.585.

The isosceles family of Theorem 2 is one fibre (q = r = 1) of the conic bundle. It is a conic on X, which explains why it gives exactly c·y.

*What resolves M1:*
- Identify the dual surface as the anticanonical quartic del Pezzo Bl₅P², and cite Browning–Sofos and Frei–Loughran–Sofos (plus de la Bretèche–Browning 2011 for context).
- Replace Theorem 3 by the resulting bound N(X) ≫ X(log X)⁵, either proved for positive points or clearly labelled conditional. Add the unconditional upper bound O(X(log X)⁵) for the dual-family contribution.
- Rewrite the remark after Theorem 3, the heuristic in §6.4 ("its exact order is not known"), Theorem B and the abstract to match.
- Restate the novelty sentence on p. 4.
- Consider reformulating Question E in Manin language: is N(X) ≍ X(log X)^κ, and is the count off the twelve "trivial" surfaces dominated by further rational (del Pezzo or conic-bundle) surfaces inside Schoen's threefold?

**M2 (pp. 15–16, §6.3; abstract). The error bars are not meaningful, the model comparison is underspecified, and the available out-of-sample check is not used.**

All my figures below reproduce the authors' point estimates first.

(a) **There is no sampling.** The data are a complete enumeration, and n(s) is a deterministic function of s. The phrase "the bootstrap measures sampling noise only" has no referent. The ± values describe how sensitive the fitted curve is to an arbitrary resampling scheme. They are not uncertainty in any parameter that has a limit. M1 shows this concretely: on the dual family the fit returns 2.56 ± 0.20 where the true exponent is 4.

(b) **The block-50 choice gives the smallest error of the schemes I tried.** For all pairs, per-sum fit:

| Uncertainty scheme | SD of q |
|---|---|
| Block bootstrap, block length 50 (authors) | 0.055 |
| Block length 10 | 0.075 |
| Block length 1 | 0.114 |
| Quasi-Poisson model-based standard error | 0.133 |
| Jackknife deleting one residue class mod 12 | 0.134 |

The authors' own window-to-window spread (4.39 to 4.64, plus 4.38 on [3000, 6000]) is about 4–5 times the quoted ±0.06.

(c) **The residuals are arithmetic and long-range, not local.**
- The ratio n(s)/fitted correlates 0.73 with σ(s)/s.
- It averages 1.25 on even s, 0.75 on odd s, and 1.57 on s ≡ 0 (mod 6).
- The Pearson residuals at s and 2s correlate at 0.88.
- The autocorrelation is −0.33 at lag 1, +0.30 at lag 6 and +0.35 at lag 12.

All of this is Lemma 3 at work: n = 1 * a, a Dirichlet convolution of the primitive-pair counts a(m) with the constant function 1. A bootstrap over blocks of consecutive sums does not represent this dependence. The phrase "well described by c(log s)^q" sits poorly with a Pearson dispersion of 6.8 driven by this structure.

(d) **The model comparison needs a stated criterion.** "Scaled difference 1.4 does not separate the two laws" needs a named rule. If this is QAIC, then ΔQAIC = 2.8. A Vuong statistic (ignoring dependence) gives z = 1.27 for all pairs, but 1.98 for primitive pairs and 2.25 for non-dual primitive pairs. So "equally consistent" (p. 16) is not uniform across subsets.

(e) **The 4800–6000 data are an unused holdout.** Both laws were fitted on [600, 4800], and the data extend to 6000.
- Predicted N(6000) − N(4800): 43 066 from the log-power law (+0.25%) and 43 961 from the power law (+2.3%). The actual value is 42 960.
- With dispersion 6.8, the power law misses by about 1.9 Poisson-scaled SD, the log-power law by about 0.2.
- The fitted power law predicts a local exponent of 1.602 at 6000. The data give 1.585, and the log-power law gives 1.587.

This is the most informative test the note's data allow, and it mildly favours log-power growth. The text's "equally with X^{1.59}" (p. 16) should be revised accordingly.

*What resolves M2:*
- Drop the ± values, or relabel them explicitly as descriptive sensitivity rather than statistical uncertainty.
- Report the window sensitivity and the 4800–6000 holdout in a small table.
- Fit primitive counts (dispersion 2.1) and obtain N through Lemma 3, rather than fitting the convolution n(s) directly. Alternatively, include the arithmetic factor explicitly.
- Name the model-selection criterion.
- State plainly, with the dual family as the example (M1), that fitted log-powers at this range do not estimate asymptotic exponents.

## MINOR

**m1 (p. 12, Theorem 3).** Even within the authors' own method, the constant can be improved by a factor of 4.

- **Floor function.** ⌊X/S_D⌋ ≥ X/(2S_D) loses a factor 2. Restricting to S_D ≤ X/K with K = log X gives ⌊X/S_D⌋ ≥ (1 − 1/K)X/S_D and recovers the full c_A/2.
- **Lattice error.** The bound U + V ≤ (2M+1)√y is wasteful. In fact V ≤ √(y/8) and U = √(βy/(4α³)) ≤ √(y/32), because β ≤ α²/4. So each box has error O(√y log y), and M = y^{1/4}/(log y)² is admissible instead of y^{1/8}.

Together these give N(X) ≥ (3/(32π⁴) + o(1)) X(log X)², and the crossover becomes log X ≈ 109 instead of 438. Counting the full hyperbolic region (αu+βv)(u+αv) ≤ y instead of a box gains roughly a further factor 3–4. This is superseded if M1 is adopted. If Theorem 3 is kept, do not advertise an artefact constant.

**m2 (p. 11).** The secondary term −0.286X is reported only numerically ("to three digits"). Either derive it (it is X·c_iso·γ_iso minus the mean of the fractional parts {X/S_D}) or call it an empirical observation. It is correct to four digits: −0.2863 for X ≥ 10⁵.

**m3 (p. 15, Proposition 4).** The divisor bound is used in its worst case. Since τ(p²p′²AA′) ≤ τ(p²)τ(p′²)τ(S−p)τ(S−p′), and the sum over (p, p′) factorises, Cauchy–Schwarz gives n(S) ≪ S²(log S)^C. Worth a sentence. The remark "we do not know a bound o(S²)" stands.

**m4 (p. 3, Theorem B; p. 11).** Only N, not N_cl, inherits the (log X)² bound, because dual pairs can share a class. Say so explicitly, and say whether N_cl ≫ X(log X)^{1+δ} is known.

**m5 (abstract; p. 3; p. 15).** "Falling from 2.0 at 500" picks its starting point. The column is not monotone (1.954 at 400, 1.993 at 500). Say "from about 2 near X = 300–500".

**m6 (p. 16).** The cumulative fit is least squares on a cumulative series, whose residuals are autocorrelated by construction. State that it is a descriptive check, not an independent estimate.

**m7 (p. 14, §6.1).** The hashing description does not say what happens when distinct rationals share a double, that is, when a run of equal keys contains more than one class. My implementation sub-groups exactly within runs. Please state that yours does the same; I assume it does, since the counts agree.

**m8 (p. 17, Figure 1).** For (a), the caption should say which colour marks (1,4,4) and which marks (1,1,4). For (b), extend the plot to S = 6000 and shade the fit window [600, 4800], so that the holdout of M2(e) is visible.

**m9 (p. 17, §6.4).** The line search ("189 lines … coefficients of absolute value at most 7, counted up to permutation … and sign") cannot be reproduced from the text. Give the normalisation precisely, give the list or its location in the archive, and state the test used for "Λ agrees after a Möbius change of parameter".

**m10 (p. 13).** Two independent checks of the ranks would be better than one: the isogeny descent already given, plus Magma or an analytic-rank check. At present ellrank and the descent share their inputs.

## Presentation

**P1 (p. 15, Table 2).** Add columns for primitive pairs and dual primitive pairs. The text quotes 46 254 and 16.5% from data that are not in the table.

**P2 (p. 16, §6.3).** The fits for six subsets, the bootstrap SDs, three windows and the power-law comparison are all packed into running text. A compact table would be clearer, including the holdout of M2(e).

**P3 (p. 16).** "These are measured exponents on a finite range, not predictions" is the right sentiment. Move it before the numbers.

**P4.** The rendered pages are clean. I found no typographical, sign or figure errors in Sections 4 and 6 after reading the page images.

## What is good

- The mathematics in Sections 4 and 6 is correct and carefully written.
- Lemma 3 is the right organising identity.
- The Möbius and residue-class count in Theorem 2 is clean.
- The enumeration is unusually well cross-checked, and every one of its numbers survives an independent reimplementation.
- The authors are commendably candid that the data do not determine the exponent.

## Recommendation

**Major revision.** Confidence: high on the correctness findings; moderately high on the applicability of the del Pezzo results, where only the positivity step needs checking.

The paper is sound but presently under-informed on its central counting question:

- the second lower bound, a headline result, is superseded by known Manin-type theorems once the dual family is recognised as a quartic del Pezzo surface (M1);
- the statistical presentation overstates precision and omits the available holdout test (M2).

Both are fixable without new heavy computation.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Identify the dual surface as an anticanonical quartic del Pezzo surface (ρ = 5, conic bundle with a section). Cite Browning–Sofos and Frei–Loughran–Sofos. State N(X) ≫ X(log X)⁵ (proved for positive points, or conditional) and the dual-family upper bound O(X(log X)⁵). Revise Theorem B, the abstract, p. 4, the remarks on p. 12, §6.4, and possibly Question E. |
| M2 | Remove or relabel the ± values. Report window sensitivity and the 4800–6000 holdout. Model primitive counts and use Lemma 3. Name the comparison criterion. Use the dual family as the cautionary example. |
| m1 | Tighten the constant (factor 4), or drop Theorem 3 in favour of M1. |
| m2 | Derive the −0.286 term or label it empirical. |
| m3 | Add the averaged divisor bound. |
| m4 | Clarify what is known for N_cl. |
| m5 | Rephrase "from 2.0 at 500". |
| m6 | Label the cumulative fit as descriptive. |
| m7 | State how equal-double runs are sub-grouped. |
| m8 | Fix Figure 1 colours, range and window shading. |
| m9 | Specify the line search reproducibly. |
| m10 | Add a second independent rank check. |
| P1–P3 | Add the table columns, move the fits into a table, and move the caveat sentence. |
