<!-- Round 8 blind check B: returned text saved verbatim; the reviewer could not write files -->

Items 1, 2, 3, 4 and 6 check out. Item 5 has one real error: Remark 6.5(a) states something impossible. Item 1 also has a small off-by-one in N that does not affect correctness. Writing `REPORT.md` was refused, so the full report is below. My code is in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/blind-check-B/scratch/code/`, run with the virtual environment in that same scratch folder (python-flint 0.9.0 for Arb ball arithmetic, plus mpmath). I wrote every formula again from the PDF and read the rendered pages where formulas mattered; I read no other file on the disk.

---

## Item 1. Proposition 6.4 and Table 3: VERIFIED, with an off-by-one in N

**What I recomputed** (`sig.py`, `certify.py`, `consts.py`):
- **Sig(A, M):** enumerated from 0 < s(σ) ≤ A/2π with orders from 2 to M. The counts 27, 48, 8, 281, 12 match Table 3.
- **G_σ(t) in ball arithmetic** (Arb `acb.integral`, 160-bit):
  - Identity term: I(t) = (Area/4π)·e^{−t/4}·(1/t − J(t)), with J(t) = 4∫₀^∞ r e^{−tr²}/(e^{2πr}+1) dr. Integrated on [0, 40] plus an explicit tail bound.
  - Elliptic terms E_m(t): integrated on [−400, 400] with tails bounded by e^{−aR}/a + e^{−(2π−a)R}/(2π−a).
  - Cross-checks: E_m(10⁻³) minus b₀ + b₁t + b₂t² has sign (−1)³ and modulus at most |b₃|t³ for m = 2, 3, 7, 12. I(10⁻³) agrees with the α_k expansion. E₇(0.0034221) agrees with an independent mpmath quadrature to 20 digits. Every gap ball has radius at most 3e−32.

| class (A, ε, M) | certified least gap (pair) | stated Θ | B*(t) vs Θ/8 | t ≤ t₂ | Λt | N: formula / stated | δ: formula / stated |
|---|---|---|---|---|---|---|---|
| π/2, 1.8626, 8 | 0.0158823 ((0;3,3,8)/(0;3,4,5)) | 0.01588 ✓ | 7.98e−6 ≤ 1.99e−3 ✓ | ✓ | 17.6 | 244 / 245 | 1.167e−4 / 1.16e−4 |
| π/2, 1.8626, 12 | 0.0065273 ((0;2,4,10)/(0;2,5,7)) | 0.006527 ✓ | 7.10e−5 ≤ 8.16e−4 ✓ | ✓ | 19.6 | 283 / 284 | 4.273e−5 / 4.25e−5 |
| 4π/3, 2.633915, 3 | 0.152029 ((0;2,2,2,2,3)/(0;3,3,3,3)) | 0.1520 ✓ | 1.79e−2 ≤ 1.90e−2 ✓ | ✓ | 12.5 | 139 / 140 | 5.90e−4 / 5.85e−4 |
| 4π/3, 0.693994, 3 | 0.165511 (same pair) | 0.1655 ✓ | 1.67e−2 ≤ 2.07e−2 ✓ | ✓ | 17.2 | 2605 / 2606 | 4.867e−4 / 4.86e−4 |
| 4π/3, 0.693994, 12 | 0.00137385 ((0;4,8,8)/(0;5,5,10)) | 0.001373 ✓ | 1.41e−4 ≤ 1.72e−4 ✓ | ✓ | 27.9 | 7416 / 7417 | 2.488e−6 / 2.48e−6 |
| 2π, 0.1, 3 | 0.166649 ((0;2⁶)/(0;2,2,3,3,3)) | 0.1666 ✓ | 1.39e−2 ≤ 2.08e−2 ✓ | ✓ | 26.3 | 387182 / 387183 | 2.141e−4 / 2.14e−4 |

- **Hypotheses of Corollary 6.3:** they all hold. Every stated Θ is a valid rounded-down lower bound for the least gap, Θ ≤ 8, and all inequalities are decided in ball arithmetic.
- **Off-by-one in N:** the formula N = ⌊e Z♯(1/Λ)⌋ + 1 gives exactly one less than Table 3 in every row. The floors are certain (e Z♯ = 243.47, 282.45, 138.81, 2604.15, 7415.36, 387181.87). The table seems to use ⌈·⌉ + 1, and its δ equals Θ/(8eNt) for the stated N.
- **Why this is harmless:** the proof only needs N ≥ e Z_O(1/Λ) and N·t·δ ≤ Θ/(8e), and both still hold with N + 1. So the proposition is correct. But the table does not literally follow "the formulas of Theorem 6.2": either change the formula or say that a larger N is allowed. The intro's N values (Item 6) carry the same +1.
- **Last column of Table 3** matches my recomputed Table 4.
- **Proof of Corollary 6.3:** I re-derived it. B* increases on (0, t₂], so Hyp(1/Λ) ≤ Θ/8 ≤ 1, and the margin Θ/8 + Θ/(8e) < 3Θ/8 holds.

## Item 2. Remark after Theorem 4.4: VERIFIED

- **Trace identity:** tr[f, g] − 2 = 4 sin²(π/p) sin²(π/q) sinh² d agrees to 15 digits with explicit SL(2, R) matrices for four (p, q, d) cases. It is positive, so Jørgensen's inequality gives 4 sin²(π/p)(1 + sin²(π/q) sinh² d) ≥ 1, as stated.
- **Range of the bound:** it constrains d only when p ≥ 7, since 4 sin²(π/6) = 1 and 4 sin²(π/7) = 0.753.
- **Attainment in (2, 3, 7):** with p = 7, q = 2 and cosh d = 1/(2 sin(π/7)), the left side is exactly 1, and tr(fg) = −1, so fg has order 3 and f, g generate the (2,3,7) group. (Equality in fact holds for every (2, 3, m), m ≥ 7; this is not an error.)

## Item 3. Ranges on p. 12 and the growth paragraph: VERIFIED

- **Table 4:** every entry (k*, C*, t₁, t₃, Θ*, Λ, N, δ, binding constraint) agrees at 50 digits.
- **Table 2:** agrees with the exact D = 4r₀A/v₀ (56.6, 1125, 6.37e5; 150.9, 3001, 1.70e6; 640, 3184, 1.70e6; 1132, 2.25e4, 1.27e7).
- **C\* range:** 4.0e5 to 7.1e10, as stated.
- **π e^{3D}/A range:** log₁₀ runs from 196.53 to 29325.38 over the Table 4 classes, i.e. about 3.4e196 to 2.4e29325, matching the text. The manuscript says "classes of Table 4", not Table 2 as in the task; over the Table 2 classes (M = 100) the value would be far larger, so "Table 4" is the right reference.
- **Growth paragraph (A = 4π/3, M = 3):**
  - t₃ < t₁ exactly for ε < 0.44446, so "t₃ binds from ε = 0.44 down" is correct.
  - N at ε = 0.42·2^{−k}, k = 0…7: 49199, 257757, 1321596, 6619137, 32448767, 156150368, 739652443, 3456764994.
  - The factor per halving goes 5.239, 5.127, 5.008, 4.902, 4.812, 4.737, 4.674, so it falls from 5.24 to below 4.7 over seven halvings. The next factor is 4.62, consistent with a slow approach to 4.

## Item 4. Section 7.2, closed-geodesic bound for O(2,8,8): VERIFIED

- **The bound H:** C = π e^{3·4.897}/(π/2) = 4.80e6. At t = 0.0562 (inside the range t ≤ 0.782) the first bound of Lemma 2.2(ii) gives H = 6.772e−3, matching 6.8e−3.
- **The hyperbolic term:** the systole is 2 arccosh(1 + cos π/4) = 2.2567679. Two classes give 2 × 1.386e−10 = 2.77e−10, matching 2.8e−10.
- **The ratio** is 2.44e7. "About 2×10⁷" is acceptable, though 2.4×10⁷ would be more accurate.
- **"Two classes" checked from the data:** using the 40 eigenvalues of Table 6 (the omitted tail is below 1e−17 for t ≥ 0.12), (Z(t) − G_{(0;2,8,8)}(t)) divided by the one-class term is 2.005, 2.019 and 2.077 at t = 0.12, 0.15 and 0.2. This tends to 2, which supports multiplicity 2 at the systole.

## Item 5. Corollary 6.3, Remark 6.5(a), Theorem 7.1 with π/21

- **Corollary 6.3: VERIFIED.** With B* defined in the statement it is self-contained, and its hypotheses are exactly what the proof of Theorem 6.2 uses.
- **Remark 6.5(a): PROBLEM.** The remark says the companion paper gives pairs of area 12π with orders at most 3 that share their first three heat invariants. No such pair can exist:
  - **Excluded by the paper's own Theorem 3.2(ii)** with M = 3. Directly, Lemma 3.1 would require equal Ψ₁ and Ψ₂, and the 2×2 matrix [[3/2, 8/3], [15/2, 26/3]] has determinant −7 ≠ 0.
  - **Exhaustive check:** none of the 15 signatures of area 12π with orders ≤ 3 share c₁, c₂, c₃ (all c's computed exactly). Up to area 40π there is no such pair either.
  - **What actually exists at area 12π with orders ≤ 3:** the only coincidence is (0; 2¹⁶) and (1; 3⁹). They share only c₁ = 3 and c₂ = 1, then differ at c₃ (−4/5 vs −17/15, d₃ = 1/3, consistent with Lemma 3.3(ii)). This pair first differs at k = 3, so it does not show that "no pair first differs beyond k = 3" fails at larger area.
  - **A correct example:** (0; 2⁴, 7⁷) and (0; 4⁶, 8⁴), both of area 12π with orders ≤ 8. They share c₁, c₂, c₃ = 3, 7/2, −161/20 and differ at c₄ (d₄ = −54/7, P₅ difference −19440). With orders ≤ 6 there is no such pair up to area 12π.
  - **Fix:** either say "share their first two heat invariants", or cite a pair with larger orders such as the one above.
  - The other claim in the remark, that the minimum defining t₁ is attained at k = k* in every row of Table 4, is confirmed.
- **Theorem 7.1 with the area replaced by π/21: VERIFIED.** Lemma 5.1(i) gives Area ≥ π/21 ((2,3,7) has s = 1/42; I re-checked the case analysis), so π e^{3Δ}/(π/21) is a valid count constant. For O(2,8,8) at t = 0.0562 it raises H by a factor of 10.5, to 7.1e−2.

## Item 6. Introduction: VERIFIED (consistent with Tables 2–4 and 7)

- **"N of order 10² to 10⁴, accuracies 10⁻⁴ to 10⁻⁶":** Table 3 gives N = 140 to 7417 and δ from 5.85e−4 to 2.48e−6 for the example classes. The ε = 0.1 row (N = 3.9e5) is not an example class. "10⁻⁴" slightly overstates the accuracy needed at the coarse end, which is the safe direction.
- **"N = 24 to 842" for (C1), "18 to 847" with the instance diameter bound, against "4×10⁴ to 7×10¹²":** matches Table 7 and my Table 4 (4.3e4, 6.8e9, 7.4e12).
- **"Up to about 4×10³⁰ eigenvalues to accuracies down to 10⁻²⁷⁷":** I get N = 3.75e30 and δ = 8.7e−278 for A = 10π, ε = 1, M = 12. That δ is strictly a little below 10⁻²⁷⁷, which "about" covers.
- **The paragraph on what finite spectral data can detect** matches the body:
  - Orders are not bounded by the data: Theorem 1.2 and Corollary 8.5.
  - The systole question is left open as Problem 1.
  - Every δ in Table 4 is at most 1.5e−9.
  - An omitted eigenvalue lowers Σe^{−λt} by e^{−λt}.
  - Section 7(iv) reports a wrong acceptance in 19 of 24 corrupted lists.
- **The demoted a-posteriori test** is consistently described as consistency checks with estimated errors and lists assumed complete.
