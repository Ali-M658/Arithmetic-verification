<!-- Round 9 B-c referee report: returned text saved verbatim; the reviewer could not write files -->

I could not write the report to `REPORT.md` (the write was refused), so the full report is below. My scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/B-c-eigenvalue-counting-tails/scratch/` (`consts.py`, `gaps.py`, `check2.py` to `check7.py`).

# Referee report: Sections 2, 5, 6 and Appendix A

**Manuscript:** "Finitely many eigenvalues determine the signature of a hyperbolic orbifold", submitted to *Annals of Global Analysis and Geometry*.

**Scope:**
- Section 2: the trace formula, Lemma 2.2 and Proposition 2.3.
- Section 5: Lemma 5.1 and Proposition 5.2.
- Section 6: Lemma 6.1, Theorem 6.2, Corollary 6.3, Proposition 6.4, Tables 3–4, Figure 1, Remarks 6.5–6.6.
- Appendix A.

Theorem 6.2 depends on Lemma 3.3 and Theorem 3.2 (proved in Appendix A.3) and on Lemmas 4.2, 4.3 and 4.5 (the count C\*). I checked those proofs too. The placeholders are treated as known. Page numbers are those of the PDF. I read rendered page images of pp. 7–9, 11, 13–18 and 32–34 before reporting any typographical or figure point.

## 1. Summary

The heat trace splits as Z_O(t) = G_σ(t) + Hyp(t). G_σ (the identity term plus the elliptic terms) depends only on the signature σ; Hyp ≥ 0 is the closed-geodesic term (Theorem 2.1).

The chain of results:
- **Proposition 2.3** gives enveloping (alternating-sign) remainders for the small-t expansions of the identity and elliptic terms.
- **Lemma 6.1** combines these with the integrality bound for the first differing heat invariant (Lemma 3.3). This gives a gap |G_σ − G_σ′| ≥ Θ(t) on Sig(A, M) for t ≤ t₁.
- **Lemma 2.2(ii)**, with the class-level count of Lemma 4.5, bounds Hyp.
- **Proposition 5.2**, #{λ ≤ x} ≤ e·Z(1/x), controls the spectral tail.
- **Theorem 6.2** gives explicit N and δ and a minimum-distance decision rule.
- **Corollary 6.3** replaces Lemma 6.1 by a gap computed at one moderate time.
- **Proposition 6.4** certifies such gaps in ball arithmetic for six classes. It gives N from 139 to 387 182, against 4·10⁴ to 7·10¹² from the closed form.

## 2. Significance

- Spectral determination of the signature, and finiteness under bounds on A, ε and M, are both classical (the latter by compactness). The novelty is the effectivity: explicit N and δ, a decision rule, and a geodesic count with no diameter bound.
- The closed-form constants of Theorem 6.2 are astronomically far from usable; the authors say so honestly. The useful content is Corollary 6.3 with Proposition 6.4, a computer-assisted statement about six specific classes.
- The analytic ingredients in my sections are standard: the Selberg trace formula, alternating Taylor remainders, the Chebyshev/Markov count and a Gaussian geodesic tail. They are assembled carefully, with fully explicit constants, but no step is technically new.
- The paper is a reasonable fit for AGAG.

What is good:
- The argument is complete and every constant is traceable.
- Proposition 2.3 and Appendix A.2 are clean and correct.
- The authors are scrupulous about what is proved and what is only observed.
- Every number I recomputed in Tables 3 and 4 is right.

## 3. Correctness and what I recomputed

I checked every proof line by line and found **no mathematical error**.

**Theorem 2.1 and Lemma A.1**
- The normalisation is standard and E_m(0⁺) = (m² − 1)/(12m) is correct.
- Independent check: I used the 40 eigenvalues of Table 6 and compared Σ e^{−λt} with G_σ(t) at t = 0.15 and 0.3.
  - For the true signature, Z − G_σ is small and positive, as Hyp must be: 2.4·10⁻⁴ for O(2,8,8) and 3.8·10⁻³ for O(3,3,12) at t = 0.15.
  - For every other signature of area π/2 it is 0.04 to 0.5.
- Lemma A.1 is correct but not needed (m6).

**Lemma 2.2**
- (i): the Dirichlet-domain packing argument is correct.
- (ii): I re-derived the integration by parts, the derivative identity for x·e^{x/2−x²/4t}, the bound x/(x−t) ≤ ℓ/(ℓ−t), the log-derivative of B_C, and the all-t bound with e^{17t/4 − 1/2 − ℓ}. All are correct.

**Proposition 2.3, Lemma A.2, Appendix A.2**
- The sign bookkeeping and the formula for μ_k are correct.
- Numerical checks (30 digits):
  - α₀, …, α₃ = 1, −1/3, 1/15, −4/315 are reproduced, and b₀(m) = (m² − 1)/(12m).
  - For m ∈ {2, 3, 7, 12}, five values of t from 0.001 to 3, and 0 ≤ K ≤ 6, both remainders have the claimed sign and bound in all 140 cases.
  - |b_K(m)| increases in m for K ≤ 5 and 2 ≤ m ≤ 30.

**Lemma A.3, Lemma 3.1, Lemma A.4, Theorem 3.2, Lemma 3.3**
- All correct.
- The worked values check: d₂ = −1/12 for (0;4,4,4) and (0;3,4,6), and d₃ = 25/12 for (0;2,8,8) and (0;3,3,12).
- The example (0;2⁴,7⁷) / (0;4⁶,8⁴) of Remark 6.5(a) checks: Ψ₁ = 54 and Ψ₂ = 2430 agree, and Ψ₃ differs.
- In exact arithmetic, no pair first differs beyond k = 3 for:
  - A ≤ 4π with M ≤ 10 (1561 signatures);
  - A ≤ 6π with M ≤ 6 (782 signatures);
  - A ≤ 2π with M ≤ 30 (5235 signatures).

**Lemmas 4.2, 4.3 and 4.5** (the count C\*): correct.

**Lemma 5.1 and Proposition 5.2**: correct.

**Lemma 6.1, Theorem 6.2, Corollary 6.3**: correct, including:
- B\* ≤ Θ/8 ⇔ e^{−y}·y^p ≤ (γ\*/16ϖ)(ε²/4)^p, and the formula for y₀;
- Θ\* ≤ 1/8 and Λt\* ≥ 2 log 64;
- N > e·Z_O(1/Λ);
- the final margin (1/4 + 1/(8e))·Θ < (3/8)·Θ.

**Table 4** (all eight rows at 40 digits). C\*, t₁, t₃, Θ\*, Λ, N, δ and the binding constraint all agree with the stated rounding. The minimum defining t₁ is attained at k = k\* in every row. The Section 6 text claims also check:
- N ≈ 4.19·10¹⁸ when k\* = n\* at A = 10π, M = 3;
- t₃ binds from ε = 0.44 down;
- the factor per halving of ε goes 5.239 to 4.673 over seven halvings.

**Table 3** (floating point, not certified). I enumerated Sig(A, M) independently and evaluated G_σ(t) at the stated t by mpmath quadrature. Every row reproduces:
- |Sig(A, M)| = 27, 48, 8, 8, 281, 12;
- the minimal gaps 0.0158823, 0.0065273, 0.152029, 0.165511, 0.00137385, 0.166649;
- B\*(t) ≤ Θ/8, t ≤ t₂ and Λt ≥ 1;
- N = 244, 283, 139, 2605, 7416, 387182 exactly, and δ to the stated digits.

The tightest margin is row 3: B\*(t) = 0.01793 against Θ/8 = 0.0190.

## 4. FATAL issues

None.

## 5. MAJOR issues

**M1 (p. 18, Remark 6.6; framing on pp. 2, 4, 17). The stated limitation of compactly supported test functions is incorrect.**
- Remark 6.6 says that truncating the spectral side with a test function supported below the systole needs an eigenvalue count that "again involves the closed geodesics". That is wrong.
- The paper's own Lemma A.1 counts eigenvalues with η_T, whose g is supported below the systole, so "the hyperbolic side vanishes for it". Made explicit (or via a Beurling–Selberg majorant), this gives an explicit Weyl upper bound depending only on the area, the orders and the systole.
- Such a route would need neither Lemma 4.5, nor t₃, nor the divergent small-t expansion behind t₁ (which binds in seven of the eight rows of Table 4).
- **Resolution:** correct the remark. Either sketch the geodesic-free Weyl bound, or state plainly that this route was not pursued and is expected to remove t₃ and Lemma 4.5. Adjust the framing on pp. 2, 4 and 17.

**M2 (pp. 15–16, Proposition 6.4). The computer-assisted proof is under-documented.** I reproduced every number, so the values are not in doubt, but the text should specify:
1. the exact rational times used;
2. how Sig(A, M) was enumerated, in exact arithmetic, with the cardinalities stated as checked;
3. the integration intervals, the truncation points, and the J-form of the identity term;
4. whether Λ, N and δ were computed with outward rounding (the margin slack absorbs rounding, but say so);
5. per row, the certified least gap, the pair attaining it, and the enclosure of B\*(t). In row 3 the margin is only about 6%.

**Resolution:** add a verification paragraph or table, with the deposit file names.

**M3 (pp. 6–9, Table 1, Appendix A). Overlap with the companion manuscript [31].**
- Theorem 2.1, Lemma 2.2, Proposition 2.3, the cone-polynomial lemmas, Lemma 3.1 and Theorem 3.2 are results of [31], re-proved here with "the arguments … of [31]". Lemma 3.3 is "a direct consequence" of two lemmas of [31].
- That is roughly five pages shared with a simultaneous submission. The editor should be told, and should judge whether it is acceptable.
- **Resolution:** declare the overlap precisely in the paper and the cover letter, and replace Appendix A by citations once [31] is accepted.

## 6. MINOR issues

**m1 (pp. 14–15). The tail bound is wasteful.**
- Choosing s = t/2 makes Λ ≈ (2/t)·log(…).
- Integrating the same counting bound instead gives Σ_{λ>Λ} e^{−λt} ≤ e·e^{−Λt}·(AΛ/4π + A/(4πt) + c), with c = n\*(M² − 1)/(12M) + 1.
- This cuts N in Table 3 by 30–38%:

| Row of Table 3 | N (paper) | N (integrated tail) |
|---|---|---|
| π/2, M = 8 | 244 | 161 |
| π/2, M = 12 | 283 | 184 |
| 4π/3, ε = 2.63, M = 3 | 139 | 98 |
| 4π/3, ε = 0.69, M = 3 | 2605 | 1730 |
| 4π/3, M = 12 | 7416 | 4558 |
| 2π, M = 3 | 387182 | 240053 |

- A further factor of nearly e is lost against an explicit Weyl bound.
- Section 5 (five lines) is oversold by its title "Counting eigenvalues"; merge it into Section 6.

**m2 (pp. 14–15).** The weighted hypothesis Σ_{j<N} |λ̃_j − λ_j|·e^{−t·min(λ̃_j, λ_j)} ≤ Nδ, left as a parenthetical in the proof, should be stated in Theorem 6.2 and Proposition 6.4.
- In Table 3, Λt ranges from 12.5 to 27.9, and λ_{N−1} ≈ eΛ. The accuracy needed on the upper eigenvalues is therefore relaxed enormously.
- The uniform absolute δ misrepresents the real requirement.

**m3 (p. 17, Remark 6.5(a)).** The exact rational first-difference computation is mentioned but not done. Lemma 6.1 holds verbatim with the realised per-k minima of |d_k|, and gives a theorem with no quadrature. My computation:

| Class | k_max | N (Theorem 6.2) | N (exact first differences) |
|---|---|---|---|
| (π/2, 1.8626, 8) | 2 | 3.4·10⁸ | 7.9·10⁴ |
| (π/2, 1.8626, 12) | 3 | 6.8·10⁹ | 6.3·10⁵ |
| (4π/3, 0.6939, 3) | 2 | 4.3·10⁴ | 2.9·10³ |
| (4π/3, 0.6939, 12) | 3 | 7.4·10¹² | 5.4·10⁶ |

Most of the loss comes from the worst-case k\* and δ_k, not from the heat-invariant method. This weakens the explanation on p. 2 of why the constants are enormous.

**m4 (p. 9, eq. (2); p. 14, Q(K)).** The cone and area remainders have opposite signs, so the sum in (2) and in Q(K) can be replaced by a maximum.

**m5 (p. 15, Corollary 6.3).** "0 < Θ ≤ 8" exists only to make the "+1" in Z♯ valid. Use "+Θ/8" instead and drop the hypothesis. Also define B\* in the statement of Theorem 6.2, not inside its proof.

**m6 (pp. 7, 32).** Hejhal (Vol. I) and Iwaniec (Thm 10.2) admit ĝ_t directly, so Lemma A.1 is a convenience, not a necessity. Say so.

**m7 (p. 32, Lemma A.1).** Three steps need one line each:
- a T-uniform bound |ψ̂(iy ± T)| ≤ e^{ϵ/2} at imaginary r_j;
- the spectral side for η_T is not termwise nonnegative there;
- absolute convergence for compactly supported g is part of the cited theorem.

**m8 (p. 16).** The growth claim for |b_K(M)| rests on [31] and is used only heuristically. Say that it is not used in any proof.

## 7. Presentation

**P1. Notation is overloaded:**
- δ (accuracy) and δ_k (separations);
- ε (systole bound), ϵ_j (errors), ϵ (support radius) and ϵ_X in Lemma A.1;
- Λ (Theorem 6.2) and Λ_N (Proposition 8.3);
- N (eigenvalue count) and N (number of variables in Lemma A.4);
- p = k\* − 3/2 and p ≤ q ≤ r (orders);
- λ for a line and for an eigenvalue near Lemma 4.2.

**P2 (pp. 16–17, 20). The tables disagree with each other:**
- Table 4 lists ε = 2.6339 and 0.6939; Table 3 and the text use 2.633915 and 0.693994.
- C\* is 4.0e5 and 3.5e9 in Table 4 but 4.1×10⁵ and 3.6×10⁹ in Table 5. My values are 4.0098·10⁵ and 3.5454·10⁹.
- The rounding of C\*, t₁, t₃ and Λ in Table 4 is not stated.

**P3 (p. 3).** "7 × 10¹²" should be 7.5 × 10¹².

**P4 (p. 18, Figure 1):**
- there is no legend;
- the y-axis label describes only the grey gap curves, not the bounds;
- the N = 21 and N = 100 dotted curves cannot be told apart;
- the caption's criterion requires halving a plotted curve mentally.

**P5.** Merge Section 5 into Section 6, or expand it.

**P6 (p. 15).** Display the three estimates (hyperbolic term, tail, perturbation) and the final margin in the proof of Theorem 6.2 separately.

## 8. Recommendation

**Minor revision** for the part under my review. Confidence is high on correctness and moderate on the overall verdict.

The mathematics is correct and every number in Tables 3 and 4 reproduces. M1 to M3 need no new mathematics. m1 and m3 would improve the practical constants cheaply. The editor should weigh M3 together with the other reports.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Rewrite Remark 6.6: eigenvalues can be counted without geodesics, as in Lemma A.1. Either sketch the Weyl bound or say the route was not pursued and would remove t₃ and Lemma 4.5. Adjust pp. 2, 4 and 17. |
| M2 | Add the verification details 1–5 with deposit file names. |
| M3 | Declare the overlap with [31] precisely; plan to replace Appendix A by citations once [31] is accepted. |
| m1 | Use the integrated tail bound, or note it. Merge Section 5 into Section 6. |
| m2 | State the weighted accuracy hypothesis in Theorem 6.2 and Proposition 6.4. |
| m3 | Add the exact rational first-difference version of Lemma 6.1 and Theorem 6.2, or explain the omission. |
| m4 | Replace the sum by the maximum in (2) and Q(K). |
| m5 | Use "+Θ/8" in Z♯, drop "Θ ≤ 8", and define B\* in Theorem 6.2. |
| m6 | Cite Hejhal or Iwaniec for direct admissibility of ĝ_t. |
| m7 | Add the three one-line justifications in Lemma A.1. |
| m8 | Flag the growth claim for |b_K(M)| as heuristic and unused. |
| P1–P6 | Editorial changes as described. |
