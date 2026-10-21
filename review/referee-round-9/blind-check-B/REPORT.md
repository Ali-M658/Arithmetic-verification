<!-- Round 9 blind check B: returned text saved verbatim; the reviewer could not write files -->

I could not write REPORT.md: the harness refused the file write. The full report is below. Overall, the substance of all 8 items holds, but I found one real error in Remark 6.3 (item 3) and several small inaccuracies.

Only the PDF and the Garbin–Jorgenson preprint (arXiv:1603.01494v1, fetched with curl) were used. My code is in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/blind-check-B/scratch/code/ (mpmath at 30 to 60 digits; the virtual environment is in the sibling scratch/venv):
- consts.py: φ_k, b_l, α_k, a_l, C_*, and every constant of Theorem 6.2.
- table5.py: Table 5.
- growth.py: Remark 8.6.
- sig.py: enumeration of Sig(A, M).
- gaps.py: G_σ(t), the least gaps, and Tables 3 and 4.

I computed φ_k(m) two independent ways: from the Taylor series of Φ_m, and from the closed form of Lemma A.2. They agree to 15 digits. The values α_0..α_3 = 1, −1/3, 1/15, −4/315 and a_0 = 1/12, a_1 = 1/360 also check out.

## Verdicts
| Item | Verdict |
|---|---|
| 1. New δ_1 and "table unchanged" | **CORRECT** |
| 2. Remark 8.6 | **CORRECT** |
| 3. Remark 6.3 | Slack Θ_*/8, the K-replacement claim and the error-budget arithmetic are **CORRECT**. The first sentence ("wrong by up to δe^{λ_j t_*}") is **INCORRECT** for underestimates. |
| 4. Proposition 6.5 and Tables 3–4 | **CORRECT**: every number reproduced. Two small inaccuracies: tied least-gap pairs, and "all tail bounds below e^{−80}" is false. |
| 5. Factor 1/M in v_0; the (H3) step | **CORRECT** |
| 6. Section 8: Hecke groups, GJ Ex. 5.8, the conditional limit, the candidate pair | **CORRECT** |
| 7. Completeness budget | **CORRECT**, with caveats: "1.8×10⁸" should be 1.74×10⁸, and "about 10⁻¹¹ relative" is unsupported |
| 8. Remark 6.7 | **CORRECT** (an accurate description) |

## 1. δ_1 = 1/(2 min(L_M, M^{2n_*})): CORRECT
**The justification in the proof of Lemma 6.1.**
- In case (i), d_1 lies in (1/(2L_{σσ'}))ℤ and is nonzero.
- L_{σσ'} divides L_M.
- Each signature has area at most A, so n + 4g ≤ A/π + 4, which gives n ≤ n_* for each one.
- The lcm is therefore taken over at most 2n_* integers, each at most M, so it is at most M^{2n_*}.
- The rest of the gap argument is complete: t ≤ δ_k/(4Q(k−1)), t ≤ 1 and k ≤ k_* give the bound ≥ ½δ_k t^{k−2} ≥ Θ(t).

**L_M against M^{2n_*} in the rows of Table 5:**

| (A, M) | L_M | M^{2n_*} |
|---|---|---|
| (π/2, 8) | 840 | 1.68e7 |
| (π/2, 12) | 27720 | 4.3e8 |
| (4π/3, 3) | 6 | 5.9e4 |
| (4π/3, 12) | 27720 | 6.2e10 |
| (2π, 3) | 6 | 5.3e5 |
| (10π, 3) | 6 | 2.3e13 |
| (10π, 12) | 27720 | 1.6e30 |

So δ_1 equals the old value 1/(2L_M) in every row.

**Table 5 recomputed from the formulas.** Every row matches with the stated rounding:
- C_*: 1.32e8, 3.55e9, 4.01e5, 4.01e5, 9.45e9, 8.06e7, 3.01e6, 7.09e10.
- t_1: 1.14e−7 and 6.85e−9 (k = 4); 9.32e−4; 2.7e−11 (k = 5); 2.5e−27 (k = 12).
- Θ_*: 2.59e−18, 4.23e−22, 1.29e−6, 1.77e−37, 4.83e−8, 4.58e−7, 1.77e−272.
- N: 3.40e8, 6.82e9, 4.32e4, 7.44e12, 2.28e6, 1.08e6, 3.75e30.
- δ: 3.07e−21, 4.17e−25, 1.48e−9, 4.06e−41, 2.8e−11, 5.89e−11, 8.65e−278.
- The binding constraint matches: t_3 in the row with ε = 0.1, t_1 elsewhere.
- The minimum defining t_1 is at k = k_* in every row, as Remark 6.6(a) says.
- The last column of Table 3 also matches.

## 2. Remark 8.6: CORRECT
**The asymptotic bounds** (fixed A and ε, M → ∞):
- Q(K) ≤ cM^{2K+1}, since p_K has degree 2K+2.
- For large M, γ_* = δ_1 = ½M^{−2n_*}. The k = 1 term of t_1 is of order M^{−2n_*−1} and the k ≥ 2 terms are at least cM^{−2n_*+1}. So t_1 ≥ cM^{−2n_*−1}.
  - From M = 32 on, L_M > M^8 and the minimum for t_1 is at k = 1.
  - The ratio t_1(64)/t_1(128) = 511.6 ≈ 2⁹.
- d_0 ≈ 2/(πM), ρ_1 ≈ 1/M² and v_0 ≈ π/M⁴, so C_* ≈ AM⁹/π.
  - Computed doubling exponents of C_*: 8.92, 8.96, 8.98, 8.99.
- The bounds y_0 = O(log M), t_3 ≥ c/log M, the Θ_* bound, Λ and N = O(M^{2n_*+1} log M), and the δ^{−1} bound all follow.
- N t_* = 102.3, 118.8, 135.3, 151.8 for M = 64, 128, 256, 512: linear in log M, as claimed.

**Doubling exponents at A = π/2, ε = 1:**

| M → 2M | N | δ^{−1} |
|---|---|---|
| 64→128 | 9.252 | 26.250 |
| 128→256 | 9.214 | 26.213 |
| 256→512 | 9.187 | 26.186 |
| 512→1024 | 9.166 | 26.165 |

These approach 9 and 26 from above (the excess is the log factor), as claimed.
- Raw values: at M = 64, N = 4.92e18 and δ^{−1} = 5.80e51; at M = 512, N = 9.79e26 and δ^{−1} = 2.59e75.
- The jump at M = 16→32 (exponents 17.1 and 54.0) is where δ_1 switches from the lcm term to the power term. It is harmless.
- "L_M = e^{(1+o(1))M}" is correct.

## 3. Remark 6.3
**The error budget in the proof of Theorem 6.2: CORRECT.**
- B_* is increasing on (0, t_2], because t_2 < ε²/2.
- The factor bound 1 + 2t/(ε − t) ≤ 3 holds because t ≤ t_2 < ε/2.
- The derivation of y_0 = 2(log(16ϖ/γ_*) + p log(4/ε²) + p log(2p/e)) is right, using max_y y^p e^{−y/2} = (2p/e)^p.
- The tail equals exactly Θ_*/8.
- Θ_* ≤ 1/8 holds because δ_1 ≤ 1/4.
- The three terms sum to 1/4 + 1/(8e) = 0.2960, which is less than 3/8.

**The slack: CORRECT.** 1/4 + 1/(8e) + 1/8 = 0.4210 < 1/2.

**K replacements: CORRECT.**
- If both the old and new values are at least Λ_o, Z̃ changes by less than e^{−Λ_o t_*}.
- Omission plus append, a duplicate, and a spurious value are each one replacement.
- Λ_o = t_*^{−1} log(8/Θ_*) gives e^{−Λ_o t_*} = Θ_*/8 exactly.

**The first sentence: INCORRECT as stated.** The hypothesis weights each error by e^{−t_* min(λ̃_j, λ_j)}. So "wrong by up to δe^{λ_j t_*}" holds only for overestimates (where the true allowance is even Nδe^{λ_j t_*}). A rigorous counterexample for underestimates:
- Take C(4π/3, 2.6339, 3). It is nonempty, since O_ϑ with ϑ = 0 belongs to it.
- Its constants are t_* = 9.3217e−4, δ = 1.4788e−9, N = 43188 and Θ_* = 1.29e−6.
- Let x = 32972, the root of δe^{x t_*} = x.
- Proposition 5.2 gives #{λ ≤ x} ≤ eZ♯(1/x) = 29881 < N − 1. So λ_{N−1} > x, and hence λ_{N−1} ≤ δe^{λ_{N−1} t_*}.
- Setting λ̃_{N−1} = 0, with every other value exact, is therefore "within δe^{λ_j t_*}".
- But the weighted sum is then λ_{N−1} > 3.3e4, far above Nδ = 6.4e−5.
- And Z̃ shifts by about 1, roughly 7.7e5 Θ_*, which nothing in the proof covers.
- **Fix:** write δe^{t_* min(λ_j, λ̃_j)}, or restrict the sentence to upward errors.

## 4. Proposition 6.5 and Tables 3–4: CORRECT (two small inaccuracies)
**Method.**
- My independent enumeration of Sig(A, M) gives 27, 48, 8, 8, 281, 12, matching |Sig| in Table 3.
- I computed G_σ with mpmath quadrature at 30 digits.
- The identity-term form, (Area/4π)(e^{−t/4}/t − ∫_0^∞ 4r e^{−t(1/4+r²)}/(e^{2πr}+1) dr), agrees with direct integration of r tanh(πr)ĝ to 20 digits.

**Recomputed values per row.** In every row: gap ≥ the table's lower bound, B_* ≤ its upper bound, Θ/8 and Λt ≥ their lower bounds, t ≤ t_2, and N and δ match Table 3 exactly.

| Row | Least-gap pair (mine) | Gap | B_* | Θ/8 | Λt | N | δ |
|---|---|---|---|---|---|---|---|
| π/2, M = 8 | (0;3,3,8)/(0;3,4,5) | 0.01588232199 | 7.976e−6 | 0.001985 | 17.631 | 244 | 1.1671e−4 |
| π/2, M = 12 | (0;2,4,10)/(0;2,5,7) | 0.006527298332 | 7.104e−5 | 8.159e−4 | 19.645 | 283 | 4.2731e−5 |
| 4π/3, ε = 2.633915, M = 3 | (0;2⁴,3)/(0;3⁴) | 0.1520292966 | 0.017933 | 0.019 | 12.518 | 139 | 5.8993e−4 |
| 4π/3, ε = 0.693994, M = 3 | (0;2⁵)/(0;2,3³) | 0.1655107998 | 0.016707 | 0.020688 | 17.214 | 2605 | 4.8669e−4 |
| 4π/3, ε = 0.693994, M = 12 | (0;5,5,10)/(0;4,8,8) | 0.001373851304 | 1.406e−4 | 1.716e−4 | 27.945 | 7416 | 2.4878e−6 |
| 2π, ε = 0.1, M = 3 | (0;2⁵)/(0;2,3³) | 0.1666487023 | 0.013937 | 0.020825 | 26.322 | 387182 | 2.1414e−4 |

- The smallest margin is in row 3, as the text says.
- eZ♯(1/Λ) is at least 0.146 away from an integer in every row.

**Inaccuracy 1: ties.** G_σ is linear in the area and the order multiset. So every equal-area pair whose multisets differ by {3,3,3} against {2,2,2,2} has the same gap 3E_3 − 4E_2. Examples: (0;3⁴)/(0;2⁴,3), (0;2,3³)/(0;2⁵), and (0;2²,3³)/(0;2⁶).
- In rows 3, 4 and 6 the least gap is attained by several pairs.
- Table 4's pairs are valid minimisers, but "the pair" is not unique. This is worth a footnote.

**Inaccuracy 2: "all below e^{−80}" is false.**
- The elliptic tail bounds themselves are valid.
- But for m ≤ 12, 10 of the 66 pairs (m, j) exceed e^{−80}.
- The worst is m = 12, j = 1 or 11 (R = 153), at 1.71·e^{−80}; next is m = 8, at 1.14·e^{−80}.
- This is numerically irrelevant (about 3e−35). Writing "below 2e^{−80}" would fix it.
- The identity tail is ∫_40^∞ 4re^{−2πr} dr = 1.8e−108.

## 5. Section 4: CORRECT
**The factor 1/M in v_0 is intrinsic.**
- 2r_0 = d_0 ≤ ℓ_{2,3}/2 = 0.281 < h_7 = 0.543 ≤ h_M.
- So the 2r_0-ball about the order-M cone point lies inside the embedded cone of Proposition 8.2, and its area is exactly (2π/M)(cosh 2r_0 − 1).
- Minor points: the claim implicitly needs M ≥ 7, and for large M the binding term of v_0 is the second one, not the 1/M term.

**The (H3) step.**
- sin α sin β > 0 and cosh d ≥ 1 give X ≥ −cos(α+β).
- 0 < α+β ≤ π gives X > −1. Together with X < 1, the trichotomy says the lines meet.
- The wrong side is excluded because its angles would sum to 2π − (α+β) ≥ π.
- The step is correct.

## 6. Section 8: CORRECT
**Garbin–Jorgenson Example 5.8 (arXiv:1603.01494).**
- It treats G_N = ⟨z ↦ −1/z, z ↦ z + 2cos(π/N)⟩ and says their Theorem 5.7 quantifies an accumulation attributed to Selberg (p. 579 of [He 83]). So the citation "[18, p. 579], [16, Ex. 5.8]" is accurate.
- GJ themselves write that G_N\H has "one cusp and three elliptic points of order 2, 3, and N". That is wrong: G_N has signature (0;2,N,∞).
- The manuscript's corrected description ("one cusp and elliptic points of orders 2 and N", "different from the compact O(2,3,m)") is the correct one.

**Condition (a).**
- GJ's condition (a) reads: the cone C_{q,ε} = {ρ < arccosh(1+εq/2π)} embeds for every ε < 1/2. The manuscript quotes it correctly.
- For m ≥ 13: 1/(2 sin(π/m)) ≥ m/(2π) ≥ 1 + m/(4π), and the last step holds exactly when m ≥ 4π ≈ 12.57.
- Condition (b) is correctly flagged as unverified.

**The conditional λ_j → 1/4.**
- GJ Corollary 5.5 gives lim N_{M_q,0}(T) = N_{M_∞,0}(T) for T ≤ 1/4 not an eigenvalue of the limit, for compact or non-compact M_q.
- PSL(2,ℤ)\H² has no eigenvalue in (0, 1/4) (λ_1 ≈ 91.14). So lim inf λ_1 ≥ 1/4.
- With the upper bound 1/4 + π²(j+1)²/h_m² → 1/4, this gives λ_j → 1/4.
- The statement is now properly conditional.

**The pair after Problem 1.**
- (0;3,3,3,3), (1;3) and (0;2,2,6,6) all have s = 2/3, so all have area 4π/3.
- On (1;3), a disc with one cone point of order 3 has χ^orb = 1/3, so its area would be −2π/3 < 0.
- A disc with cone points of orders 2, 2 has χ^orb = 0, so its area would be 0 and a geodesic boundary is impossible. Hence (0;2,2,6,6) admits only the partition {2,6}|{2,6} (χ = −1/3 on each side, area 2π/3 each).
- The limits are (0;3,3,∞) and (0;2,6,∞), each of area 2π/3 (two copies of each), and (0;3,∞,∞) of area 4π/3. All correct.
- Small eigenvalue: both halves have area bounded below, so the ±1 test function gives λ_1 → 0. Correct.

## 7. Completeness budget: CORRECT (with caveats)
**The tail bound.** I computed min over 0 < s < t of e^{−Λ_c(t−s)}(A/(4πs) + 23/16 + B(s)) at t = 0.0015, A = π/2. Here Σb_0 = 23/16 for both orbifolds, and I used ℓ from Table 6 with either the diameter count C or C_* = 3.6e9.

| Λ_c | Bound |
|---|---|
| 2.375e4 | 2.72e−12 |
| 2.38e4 | 2.53e−12 |
| 2.385e4 | 2.36e−12 |

- The minimum is at s ≈ 4.2e−5, where B(s) < 1e−8900.
- So the bound is below 3e−12 for both orbifolds whenever Λ_c ≥ 23690.

**It follows from the paper's counting proposition.** Proposition 5.2, Lemma 5.1(ii), Theorem 2.1 and Lemma 2.2(ii) give exactly this bound.
- Caveat: Λ_c must be the level below which the union of the Neumann and Dirichlet lists is complete, i.e. the smaller of the two maxima, not "the largest computed value". The text should state this.

**The threshold.** ln(1/1.7e−11)/0.0015 = 16532, so 1.65e4 is correct. Including the observed discrepancy 4.7e−13 gives 16514, still 1.65e4.

**The gap to other signatures.**
- I recomputed the six signatures of area π/2 with orders ≤ 12: (2,8,8), (3,3,12), (2,6,12), (3,4,6), (4,4,4), (2,2,2,4).
- At t = 0.0015 the least gap is 2.96855e−3, between (0;2,8,8) and (0;3,3,12). Every other gap is at least 0.163.
- But 2.96e−3 / 1.7e−11 = **1.74e8**, not "about 1.8×10⁸".

**How far a proved instance is.**
- 283 eigenvalues to 4.27e−5 is confirmed (Table 3, row 2).
- λ_282 ≈ 2.25e3 is consistent with Weyl (≈ 8·282).
- 4.27e−5 / 2250 = 1.90e−8, so "about 2×10⁻⁸ relative" is correct.
- "Our estimated errors are about 10⁻¹¹ relative" is not supported by the PDF, and looks inconsistent with it:
  - Table 7 gives ε_j/λ_j ≈ 1.2–1.6e−13 for j ≤ 40.
  - Section 7.1 gives a maximum of 7.4e−8 relative.
  - It may hold near j ≈ 282, but I cannot verify that. The authors should state the actual range of ε_j/λ_j for j < 283.

## 8. Remark 6.7: CORRECT (accurate)
In Lemma A.1:
- η_T = ĝ for g = 2cos(Tu)(ψ*ψ)(u), supported in [−2ϵ, 2ϵ] with 2ϵ below the systole, so the geodesic term vanishes.
- η_T ≥ cos²1 > 1/4 on the window |r − T| ≤ 1.
- The identity term is O(T+1), with constants depending on the area and on ϵ (hence the systole).
- Each elliptic term is O(1) uniformly in T. By the beta integral it is at most (m²−1)/(6m), so it depends on the order.

So "count the eigenvalues in windows with no geodesic term" is accurate, and the Weyl-type bound "depending only on area, orders and systole" is an accurate conditional description.

The one missing input is a uniform bound for the imaginary r_j. For them η_T(iy) = 2 Re ψ̂(iy − T)² can be negative, and their number must itself be bounded. The remark flags exactly this ("needs an explicit treatment of the small eigenvalues"), so it does not overstate.
