<!-- FIX-CHECK-B (round 10), returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

FIX-CHECK-B (round 10)

Paper: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold", revised build, 48 pp. All page numbers below refer to this PDF.

Inputs used: the manuscript PDF (text extraction, plus every page rendered at 110 dpi; I looked at pp. 2, 3, 5, 16, 18–20, 23, 32, 34, 37 and 44), VERDICT-B.md, and the five B-* reports. I read nothing else from the repository and used none of the referees' scripts. My own code is in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/fixcheck-B/code/:
- consts.py recomputes Tables 4, 5 and 6.
- gaps.py recomputes Table B1 and the certificate from its decimals.
- r67.py checks Remark 6.7(a), the α_k identity and c′, Λ₂, ℓ₂,₃.

The rendered pages are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/fixcheck-B/pages/.

## Overall verdict

All seven major items are resolved; two have small residual wording issues (B1, B4).
- Every number I recomputed matches.
- Every table and figure cross-reference I checked is correct after the renumbering. There are no stale references.
- The honest framing holds throughout: eigenvalue errors are called estimates, completeness is supported but not proved, and the test presupposes a complete list.

There are four small new problems, listed under "New problems" below, and one minor item that was not applied (B-e P5). None affects a result.

## Recomputed numbers (all match the paper)

**Table 4 (p. 20)**
- N = 244, 283, 139, 2605, 7416, 387182. The fractional parts of eZ♯(1/Λ) are 0.47, 0.45, 0.81, 0.15, 0.36 and 0.87, so none is near an integer.
- δ = 1.1671e−4, 4.2731e−5, 5.8993e−4, 4.8669e−4, 2.4879e−6, 2.1414e−4. The printed values are correctly rounded down.
- The new Λ_o column (log(8/Θ)/t) is 242.6, 286.5, 46.50, 646.1, 2533.6, 41899.5. The printed 243, 287, 46.5, 647, 2540, 41900 are correct three-digit upward roundings.
- The last column (Theorem 6.2's N) agrees with Table 6.

**Table 5 (p. 20)**
- B*(t) = 7.976e−6, 7.104e−5, 0.017933, 0.016707, 1.406e−4, 0.013937, all below the printed upper bounds.
- Θ/8 = 0.001985, 0.000815875, 0.019, 0.0206875, 0.000171625, 0.020825.
- Λt = 17.63, 19.65, 12.52, 17.21, 27.95, 26.32.
- t ≤ t₂ holds in every row.
- The caption's explanation of 0.001984 and 0.01899 (decimals strictly below the exact values 0.001985 and 0.019) is correct.

**Table B1 (p. 44) and the certificate**
- I evaluated I₁(t) and every E_m(t) independently with mpmath quadrature. Every printed decimal is within one unit of its last digit (worst about 0.4 units).
- I enumerated Sig(A, M) (sizes 27, 48, 8, 8, 281, 12) and formed G_σ from the printed decimals alone, with the error rule of Appendix B. Every pairwise gap minus both errors is at least Θ in all six classes.
- Least gaps: 0.0158823219, 0.0065272983, 0.1520292969, 0.1655107997, 0.0013738512, 0.1666487025.
- Ties: two pairs in class 1, one in class 2, two each in classes 3 and 4, one in class 5, three in class 6. This is exactly what p. 19 says, and the Table 5 pairs are among them.
- The error of the decimals is at most 5.0e−6 (p. 21 says "at most 6 × 10⁻⁶"). Its largest ratio to Θ/16 is 4.8e−4 (p. 21 says below 10⁻³).

**Table 6 (p. 21): all eight rows reproduce** (k*, C*, t₁, t₃, Θ*, Λ, N, δ, binding constraint). N with three digits rounded up is correct in every row: 3.399e8 → 3.40e8, 6.818e9 → 6.82e9, 43188 → 4.32e4, 7.4356e12 → 7.44e12, 2.2809e6 → 2.29e6, 1.0841e6 → 1.09e6, 3.7538e30 → 3.76e30. In every row the minimum defining t₁ is attained at k = k*.

**Other numbers that check**
- Weyl ratio N/(AΛ/4π): 2.839, 2.860, 2.839, 2.725, 2.724, 2.718, i.e. "between 2.72 and 2.86" (2.718 rounds to 2.72).
- p. 15: πe^{3D}/A ranges over 10^196.53 to 10^29325.38, i.e. 3.4e196 to 2.4e29325, as now printed. C* ranges over 4.0e5 to 7.1e10.
- Table 3: 56.6, 1125, 6.37e5, 150.9, 640, 2.25e4 reproduce.
- Remark 6.7(a), by exact enumeration of Sig(π/2, 12): the largest first-difference index is 3. The least first differences are 1/2640 ((2,5,11)/(2,6,8)), 1/12 ((3,3,6)/(3,4,4)) and 25/12 ((2,8,8)/(3,3,12)). With these, t₁ = 2.36e−5 (printed 2.4e−5).
- The α_k moment form equals the Bernoulli closed form exactly for k ≤ 10. The μ_k closed form in A.2 is correct, by derivation and numerically.
- ℓ₂,₃ = 0.5620669; h₇ = 0.545275; c′ = 33.4447; Λ₂ = 133.029 > 133.
- B4 feasibility (p. 26): N·δ = 0.012093. Under Weyl's law r = 5.98e−5; with the 40 eigenvalues of Table 8 and Weyl's law above them r = 5.89e−5. This matches "about 6 × 10⁻⁵" and "5.9 × 10⁻⁵". Also 4.27e−5/2250 ≈ 1.9e−8.
- p. 31 "about 5.6 to 11.3": the ratios are 283/25 = 11.32, 283/37 = 7.65, 139/25 = 5.56, 2605/462 = 5.64, 7416/843 = 8.80.
- "Changes them by at most 5%": the smallest count compared is 24, and 25/24 is a 4.2% change. "Factor of at most 1.7": the maximum is 767/461 = 1.66. The quoted ranges 10² to 2×10³, 1.9 to 2.8×10⁸ and 10¹⁰ to 2×10¹¹ check.
- (λ̃_N − ϵ_N)t = 7.68 and 8.35. 2.96e−3/6.5e−11 ≈ 4.5e7.

## Major items

**B1 — RESOLVED, with one residual wording point (pp. 2–4, 17–19)**
- Theorem 6.5 (p. 18) gives the terminating certified procedure. I checked the proof:
  - (i) The equality claimed for y₀ is right: y₀ = 2(log 16ϖ/γ* + p log 4/ε² + p log 2p/e) gives e^{−y₀/2}(2p/e)^p = (γ*/16ϖ)(ε²/4)^p.
  - (ii) Termination holds because Θ_k ≥ Θ(t) > 8B*(t). Θ(t) ≤ 1/24, Λt ≥ 2 log 8, and the midpoint-rule and Lipschitz bounds are correct.
- Theorem 1.1 now has the "Moreover" clause, and the abstract mentions the procedure.
- "What is new" (p. 3) now:
  - calls Lemma 4.5 a crude auxiliary count;
  - attributes the enveloping remainders to the companion paper;
  - lists the necessity results;
  - names Proposition 6.6 as the usable statement, together with what it needs.
- References [27]–[29] are added (p. 7). I checked the description of [27] against the arXiv abstract: it bounds the systole, kissing number, λ₁, its multiplicity and the number of small eigenvalues, which matches.
- Residual: Theorem 1.1's "at every rational time t < t* … terminates" omits two hypotheses of Theorem 6.5, that A/2π is rational and that ε is computable. Add "(for A/2π rational)" or similar.

**B2 — RESOLVED (pp. 2, 34–35)**
- Corollary 8.5 is retitled "A constraint on N and δ" and stated for the pair.
- The paragraph after it shows that at δ ≤ M⁻¹ the corollary gives only N ≥ 2 (correct, since Λ₂ > 133). It says that Theorem 6.2 gives no N at a fixed δ and why, and that the fixed-δ question is open.
- The last sentence of Remark 8.6 is rewritten.
- The abstract no longer juxtaposes the two bounds.

**B3 — RESOLVED (pp. 2, 4–6, 36–37)**
- Proposition 8.8 is proved, and I checked the proof step by step:
  - Cheng's bound with R = d/2j gives λ_j ≤ 1/4 + 4π²j²/d².
  - Area(S) ≤ 2π(cosh d − 1) gives d ≥ arccosh(2g − 1).
  - The residual-finiteness construction of Γ₁ with systole > ε is correct (conjugate into the Dirichlet domain, then Φ is finite).
  - The cyclic covers of index q have genus 1 + q(g₁ − 1) and do not decrease the systole.
  - The pigeonhole with Λ′ = 1/4 + 4π²N²/arccosh(3)² is correct.
- The abstract, the introduction (pp. 4–6) and Table 1 are updated, and the novelty claimed for Theorem 1.2 is recalibrated (p. 6).
- I could not check the pinpoint "[8, Thm 2.1]" in Cheng without the source.

**B4 — RESOLVED, with one residual wording point (pp. 2, 25–28)**
- The accuracy paragraph is rewritten around the weighted hypothesis, with a correct feasibility estimate (checked above).
- "Practical size" is now "moderate size" (p. 3).
- Section 7 is down to one clause in the abstract.
- The rigorous instance is said to be not done and "within reach".
- The signature-free completeness statement is present (p. 28). Residual: it says the check "presupposes nothing about the signature beyond the class", but:
  - the competitors are the signatures of area exactly π/2, not the whole class;
  - the tail budget uses Σb₀(m_i) of the true signature.

  Numerically this is harmless: the largest Σb₀ among the competitors, 1.604 for (2,6,12) against 1.4375, changes the budget by about 0.1%. The wording should be "beyond its area and the order bound", with the budget taken as the maximum over S.

**B5 — RESOLVED (pp. 19–21, 43–44)**
- Table B1 is present and verified above.
- The certification paragraph states that t enters as an exact decimal rational enclosed in a ball, gives Arb's tolerances (2⁻²⁰⁰), and explains holomorphy (meromorphic integrands, no branch cuts, a pole yields a non-finite ball).
- The tail bounds are correct: the largest is about 1.9e^{−80} < 2e^{−80}, consistent with radii below 1e−34.

**B6 — RESOLVED (pp. 7–11)**
- The headers of Theorem 2.1, Proposition 2.3, Lemma 3.1 and Theorem 3.2 point to the internal proofs. The "[4, …]" attributions are gone from the headers.
- p. 7 names the primary home of each shared result, and Table 2 gives their places in [4].
- The "Relation to Uçar's formulas" paragraph (p. 11) cites (4.33)–(4.35) and (4.25), and states the novelty of Proposition 2.3, Theorem 3.2(i) and Lemma 3.3.

**B7 — RESOLVED (pp. 4, 22–23)**
- Remark 6.7 qualifies the explanation of the size of the constants and lists the gains: (a) exact first-difference data, with numbers that check; (b) the maximum in place of the sum; (c) enumerated geodesics; (d) the infimum over s and the exact factor in B*, plus the individual δ_k t^{k−2}.
- It names Proposition 6.6 as the class-exact route.
- The introduction (p. 4) carries the same qualification.

## Minor items listed as applied

- **B-a m1:** RESOLVED (p. 17, why Θ ≤ 8).
- **B-a m2:** RESOLVED (λ_top against λ_c, p. 27).
- **B-a m3:** RESOLVED by stating the convention (pp. 4, 29, 31, Table 9 and Fig. 2 captions); Theorem 7.1 itself is not restated.
- **B-a m5:** RESOLVED (2.5e−6 in the abstract and on p. 4).
- **B-a m6:** RESOLVED ([27]–[29], [8], erratum [35]).
- **B-a m7:** RESOLVED (Bolza benchmark, p. 27).
- **B-a m8:** this paper's version is kept; I cannot check the companion.
- **B-a m9:** placeholder.
- **B-a m12, m13:** RESOLVED.
- **B-a m14:** the year is kept as the volume year 2018; acceptable.
- **B-a P1, P3, P6:** RESOLVED (Theorem 1.1 gives the shape of N and δ; Table 1; the abstract is reordered).
- **B-b m1:** RESOLVED (p. 11).
- **B-b m2:** RESOLVED (Lemma A.1 "only to keep the paper self-contained"; [18] cited).
- **B-b m3:** RESOLVED (identification argument, exact check for k ≤ 10, Uçar (4.35)).
- **B-b m4, m5, m7, P2, P4, P5:** RESOLVED.
- **B-c m2:** RESOLVED (p. 21, verified).
- **B-c m3:** RESOLVED (c′ = 33.44…).
- **B-c m5:** RESOLVED (γ ≠ 1, p. 13).
- **B-c m6:** RESOLVED (Remark 8.7).
- **B-c P1–P5:** RESOLVED (2r₀ = d₀; Jørgensen equality in every (2,3,p); C* linear in Section 7; three digits; "area at most A").
- **B-d m1:** RESOLVED by the caption explanation.
- **B-d m2:** RESOLVED (restricted to the counts 18 and 25).
- **B-d m3:** PARTLY RESOLVED. The convention is stated and the Fig. 2 caption mentions Proposition 6.6 (139 to 7416), but it is not plotted and the caption does not lead with it.
- **B-d m4–m9:** RESOLVED (Table 8 column relabelled; Λ_o column and the substitution in Proposition 6.6; tolerance of the decision rule; meaning of "binds"; 2.5e−6; "with none omitted").
- **B-d P2:** RESOLVED (ties rewritten).
- **B-d P3:** RESOLVED (caption and text).
- **B-e m1–m4:** RESOLVED (GJ pinpoints split between [17] and [18]; Uçar Cor. 4.21(iv) via Thm 4.20; "congruent"; Buser–Courtois quoted; Hejhal "as quoted in [17, Ex. 5.8]").
- **B-e m5, m6, m9:** RESOLVED (3.4e196 and 2.4e29325 verified; "escape it" rephrased; b_K growth marked as from [4] and used in no proof; the exact t₁ formula is given).
- **B-e P1, P2, P6:** RESOLVED.
- **B-e P5: NOT RESOLVED.** "whose singular points are cone points" is still on p. 2.

## New problems introduced by the fixes (all minor)

1. **Theorem 1.1, p. 3: missing hypotheses.** The "Moreover" clause lacks Theorem 6.5's hypotheses (A/2π rational, ε computable). See B1.
2. **p. 4: overclaim about the systole.** "None of the bounds A, ε, M is read off finitely many eigenvalues: … whether one bounds the systole is Problem 1" asserts for ε what the paper says is open. It also misdescribes Problem 1, which asks whether the theorem needs a systole bound, not whether eigenvalues bound the systole. Suggested wording: "Neither A nor M is read off …; for ε we do not know (Problem 1 asks a related question)".
3. **p. 28: "beyond the class".** See B4: the check presupposes the exact area, and the budget uses the true signature's Σb₀.
4. **Table 1, p. 3, and layout.** The "proved" row omits Lemma 6.1 and Corollary 6.4, which are proved and used. Separately, the Table B1 float is placed inside the reference list (p. 44, between [4] and [5]); it would sit better on p. 43 after Appendix B.

## Checks that found nothing

- **Cross-references:** I listed every cross-reference and checked each in context. Tables 1–9 and B1, Remarks 6.3, 6.7 and 6.8, Theorem 6.5, Propositions 6.6, 8.8 and 8.9, and Appendix B all point to the right objects. There are no stale references to the old Proposition 6.5, Remark 6.6, Table 5 or Table 8.
- **Abstract, introduction and body:**
  - The ranges 10² to 10⁴ and 6e−4 to 2.5e−6 are consistent between the abstract and Table 4.
  - The ranges 4.32e4 to 7.44e12, 24 to 842 and 18 to 847 agree between pp. 4, 29–30 and Table 9.
  - The status of each result agrees between Table 1 and the body.
- **Overclaims:** apart from items 2 and 3 above, none found. Section 7 and Tables 8 and 9 consistently say estimated errors, completeness supported not proved, a complete list presupposed, and illustration only. The corruption protocol is labelled empirical.
- **Rendered pages:** no typographical, sign or figure errors on the pages I inspected. The formulas for y₀, Θ_k and Corollary 8.5, and Figs. 1 and 2, are consistent with the text.

## Follow-up (main session)

1. Theorem 1.1's "Moreover" clause now carries the hypotheses of Theorem 6.5: A/2π rational and ε computable.
2. The overclaim on p. 4 is replaced. Neither A nor M is read off finitely many eigenvalues (Theorem 1.2, Proposition 8.8). For ε it is not known, and Problem 1 asks whether the theorem needs a systole bound.
3. The completeness check presupposes nothing beyond the area and the order bound, with the budget taken over the maximum Σb₀ among the competitors (1.604 for (0;2,6,12)).
   - Recomputed: the totals move from 6.53988e-11 to 6.54019e-11 and from 5.42538e-11 to 5.42563e-11. The tails and the thresholds 15633.6 and 15758.2 are unchanged.
   - Every printed figure therefore stands.
4. Lemma 6.1 and Corollary 6.4 are added to the "proved" row of Table 1. Table B1 now sits in Appendix B, before the references.
5. B-e P5: the redundant clause on p. 2 is removed.
6. B-d m3 is left as it was: the Fig. 2 caption mentions Proposition 6.6, and the figure is not redrawn (no figure changes).

Build: 49 pp., zero undefined references, no overfull boxes. The round-10 blind check of the Paper B changes (`blind-check-B/REPORT.md`) found every item correct. Its wording points were applied before this fix check.
