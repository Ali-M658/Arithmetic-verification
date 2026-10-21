# VERDICT-B (round 9): "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (AGAG)

Inputs: the five reports of Panel B (README.md). Length remarks are excluded.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| B-a editor (effective geometric analysis) | send to review; major revision | high (correctness), medium (recommendation) |
| B-b (moduli, compactness) | minor revision | high |
| B-c (eigenvalue counting, tails) | minor revision | high (correctness), moderate (verdict) |
| B-d (ball arithmetic, certification) | minor revision | high |
| B-e (logical dependencies, citations) | minor revision | high (theorems), medium-high (recommendation) |

No FATAL item. Every table entry and every certified number was reproduced independently by B-a, B-c, B-d and B-e.

**Stop condition: not met.** Every referee recommends minor revision and the editor sends the paper to review, but confirmed MAJOR items remain before the fixes (B1–B6), and the editor's M2 (one proved determination) is not resolvable here. Round 9 is the fourth and last round for this paper; see "What blocks" below.

## FATAL and MAJOR items

| id | item (reviewers) | status | resolution |
|---|---|---|---|
| B1 | The computer-assisted proof of Prop. 6.4 (now 6.5) is not reviewable from the paper: enumeration, integral representation and tails, rounding of N and δ, minimising pairs, certified margins (B-a M5, B-c M2, B-d M1, B-e M1, m9) | CONFIRMED | The certification paragraph now gives the enumeration (from n + 4g ≤ A/π + 4), the identity-term form I = (A/4π)(e^{−t/4}/t − ∫…) with the interval [0,40] and its tail bound, the elliptic intervals [−R_1,R_2] with R_2 = ⌊80/2θ_j⌋+1, R_1 = ⌊80/(2π−2θ_j)⌋+1 and their tail bounds, ball evaluation of C_*, B_*, t_2, Z♯, Λ, N decided strictly between integers, δ rounded down, versions (python-flint 0.9.0, FLINT 3.6.0, 200 bits), run time. New generated Table 4 (`certified_gap_detail.csv`): minimising pair, certified gap lower bound, B_* ≤, Θ/8 ≥, Λt ≥ per class; the thin row-3 margin (0.0180 vs 0.01899) is stated. `theory/eigen/certified_gap.py` now writes and asserts these |
| B2 | Contribution beyond the companion and standard estimates not stated (B-a M1) | CONFIRMED (presentation) | New paragraph "What is new" after Theorem 1.1: four contributions; the closed-form constants matter only to show explicit constants exist |
| B3 | The dependence on M is misdescribed; δ_1 can use min(L_M, M^{2n_*}) (B-a M3, B-b m3) | CONFIRMED | δ_1 = 1/(2 min(L_M, M^{2n_*})), justified in the proof of Lemma 6.1 (the lcm of at most 2n_* orders ≤ M); Table 4 unchanged (L_M < M^{2n_*} in every row, asserted). New Remark 8.6: for fixed A, ε, N = O(M^{2n_*+1} log M), δ^{−1} = O(M^{2n_*+(2n_*+1)(n_*−2)} log M), computed exponents 9 and 26 at A = π/2, ε = 1 (C_* ~ M^9); abstract: "at most polynomially in M". `theorem_e.py` round-9 block |
| B4 | Physical framing: weighted accuracy, omissions above a level (B-a M4, B-c m2) | CONFIRMED | Weighted hypothesis moved into the statement of Theorem 6.2 and Prop. 6.5; new Remark 6.3 (accuracy and omissions high in the list) with proof: the proof's errors leave slack Θ_*/8, so K arbitrary replacements of entries ≥ Λ_o are tolerated when K e^{−Λ_o t_*} ≤ Θ_*/8 |
| B5 | Remark 6.6 wrong: eigenvalues can be counted without closed geodesics (B-c M1) | CONFIRMED | Remark rewritten: the η_T of Lemma A.1 count eigenvalues with no geodesic term; the route would remove t_3 and Lemma 4.5 but needs the small eigenvalues and the separation for compactly supported g; not pursued |
| B6 | Completeness rests on a Weyl estimate; inertia counts; ε_j at rounding level (B-d M2, M3) | CONFIRMED in part | The Weyl estimate replaced by the rigorous bound min_s e^{−Λ_c(t−s)}(A/4πs + Σb_0 + B(s)), Λ_c the smaller of the largest computed Neumann and Dirichlet eigenvalues (2.17e4 and 2.19e4; a first version used the overall maximum 2.38e4, corrected after the blind check): tail at most 5.2e-11, budget 6.5e-11 and 5.4e-11, detection of one missing eigenvalue below about 1.56e4; the 48 and 29 eigenvalues between 1.56e4 and the cut 1.6e4 rest on the window agreement alone, as now stated (`practice_checks.py`, round 9; consistent with the reviewer's 3.5e-11 at 2.2e4). Sentence that for the first 40 eigenvalues the ε_j are at rounding level and the conclusions rest on the robustness check. Inertia counts not computed (the paper says so) |
| B7 | The examples prove nothing although a rigorous instance looks within reach (B-a M2, B-d M4) | CONFIRMED; NOT RESOLVABLE here | The paper now says concretely how far it is: 283 eigenvalues to 4.27e-5 (about 2e-8 relative at λ_282 ≈ 2.25e3), counts robust to 1e-3 relative, estimated errors 1e-11 relative; what is missing is guaranteed index-wise enclosures for a weighted Laplacian on a polygon with geodesic sides and a completeness proof independent of the signature. Section 7 was already labelled an illustration |
| B8 | Overlap with the companion (B-c M3) | ANSWERED IN PAPER (Table 1, the reverse dependencies, Appendix A kept for self-containment, round 8) |

## MINOR items (deduplicated)

| id | item | resolution |
|---|---|---|
| b1 | Section 4 title; Theorem 4.4 unused (B-b m1, B-a m7) | retitled "Separation of cone points and the count of closed geodesics", with an opening paragraph naming the results used later |
| b2 | v_0's 1/M intrinsic (B-b m2) | corrected: intrinsic for balls about a cone point (O(2,3,M) cone ball of area 2π(cosh 2r_0 − 1)/M); d_0's not expected to be |
| b3 | Problem 1(b) candidate pair (B-b m4) | (0;3,3,3,3) and (0;2,2,6,6) named, partitions, small eigenvalue, limits (0;3,3,∞) and (0;2,6,∞), what remains |
| b4 | Garbin–Jorgenson condition (b) and the λ_j → 1/4 claim conditional (B-b m5, B-e m4) | now "If it holds … would give" |
| b5 | Hecke groups mislabelled (B-e m3) | corrected from the fetched Garbin–Jorgenson text: G_N has a cusp and orders 2, N; a different family from O(2,3,m) (intro and §8) |
| b6 | citation of Thm 3.11(i) harmonised (B-b m6) | done |
| b7 | (H3) clause (B-e m1) | "X ≥ −cos(α+β) > −1, since 0 < α+β ≤ π" |
| b8 | "extension to the heat function" (B-e m5) | theorem title reworded |
| b9 | C_* rounding in two tables (B-a m1, B-d m1, B-e m6, B-c P2) | stated in both captions (constants table to nearest, inputs table up) |
| b10 | 7×10^12 → 7.5×10^12, 4×10^4 → 4.4×10^4 (B-a m2, B-c P3, B-e P3) | done, "rounded up" |
| b11 | Fig. 1 N = 20 sentence (B-d m2) | reworded: N = 21 drawn; (C2) holds with N = 20 at t ≈ 0.056 |
| b12 | not done: B-a m3, m4 (Dai–Wei: not verifiable here), m5, m6, m8–m10, P1–P5; B-b m7, m8, P1–P5; B-c m1 (integrated tail, would change every N), m3 (exact first differences), m4–m8, P1, P4–P6; B-d m3–m10, P1–P5; B-e m2, m7–m10, P1–P5 | judged not worthwhile this round or not verifiable; no correctness issue |

## Mathematical changes (each with its check)

1. δ_1 with min(L_M, M^{2n_*}); Remark 8.6 (polynomial growth) — `theory/eigen/theorem_e.py` (round-9 block), `eigen_common.theorem_E_constants`.
2. Remark 6.3 (omissions) — proof in the text.
3. Table 4 (certificate details) — `theory/eigen/certified_gap.py`, `data/certified_gap_detail.csv`.
4. Rigorous completeness budget — `theory/eigen/practice_checks.py` (round 9).
5. v_0 remark, (H3), Problem 1 candidate pair — text; blind check.

Blind check: `blind-check-B/REPORT.md`: all eight items correct in substance; it found that Remark 6.3's first sentence holds only for over-estimates (corrected), that several pairs attain the least gap in the M = 3 rows (stated), that two tail bounds slightly exceed e^{-80} (now "below 2e^{-80}"), that Λ_c must be the smaller list maximum (corrected, numbers recomputed), and that "10^{-11} relative" was unsupported (now "below 2×10^{-13} for j < 283", computed from the data).

## What blocks this paper after four rounds

- **B7 (a proved determination).** The editor asks for at least one rigorous determination of a signature from computed eigenvalues. That needs guaranteed eigenvalue enclosures by index for weighted Laplacians on polygons with geodesic sides and a signature-independent completeness proof: new numerical analysis, not revision. Further review rounds would report the same gap.
- **Significance.** The editor and B-e note that the closed-form theorem is of no practical use and the usable content is computer-assisted; the paper now says this itself (B2), but the judgement is the journal's.
