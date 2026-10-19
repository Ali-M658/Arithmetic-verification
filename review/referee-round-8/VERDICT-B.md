# VERDICT-B (round 8): "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (AGAG)

Inputs: the five reports of Panel B (README.md). Length remarks are excluded.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| B-a editor (inverse spectral problems) | send to review; major revision | high (correctness), moderate (recommendation) |
| B-b (Fuchsian groups, signatures) | minor revision | high |
| B-c (Selberg zeta, explicit constants) | minor revision | high |
| B-d (validated eigenvalue numerics) | major revision | high |
| B-e (statements and citations) | minor revision | high (proofs), moderate (acceptability) |

No FATAL item; every proof checked and every table recomputed agrees.

**Stop condition: not met** (B-d recommends major revision, and confirmed MAJOR items remain before the fixes).

## FATAL and MAJOR items

| id | item (reviewers) | status | resolution |
|---|---|---|---|
| B1 | The practically sized N (Corollary 6.3) rest on an uncertified gap; δ and the time are not reported (B-a M1, B-c M1, B-d M2, B-e M1) | CONFIRMED (the abstract said "computed, not certified") | Certified in ball arithmetic: `theory/eigen/certified_gap.py` (Arb via python-flint) encloses every integral of G_σ(t) at one rational time per class, with explicit tail bounds, and decides Θ, B_* ≤ Θ/8, t ≤ t_2 and Λt ≥ 1. New Proposition 6.4 with Table 3 (A, ε, M, |Sig|, t, Θ, N, δ, N of Theorem 6.2): N = 244, 283, 139, 2605, 7416, 387182 (= ⌊e Z♯(1/Λ)⌋ + 1) with δ from 5.9e-4 to 2.5e-6. Abstract and introduction now state proved N with their δ |
| B2 | Section 7 certifies nothing; Theorem 1.2 promoted as a headline (B-d M1, B-a M4) | CONFIRMED (presentation) | The introduction's Theorem 1.2 is now a paragraph describing Theorem 7.1; Section 7 opens by saying that its applications are illustrations on orbifolds of known signature, none a proved determination. Theorem 7.1 itself is a proved statement about lists that satisfy its hypotheses |
| B3 | "A finite procedure that decides" is effective only in principle; the cost remark (B-d M3) | CONFIRMED | "in principle": up to about 4e30 eigenvalues to accuracies down to 1e-277 for Table 2, far beyond computation; the practical statements are Proposition 6.4 and Section 7. The cost remark now names the number of eigenvalues and δ as the dominant cost |
| B4 | The closed-geodesic bound is about 1e7 times too large, which drives the comparison claims of Section 7.2 (B-d M4) | CONFIRMED by computation (`practice_checks.py`: H = 6.8e-3 at t = 0.0562 against 2.8e-10, ratio 2.4e7) | Section 7.2 states the overestimate and that its comparisons concern the bound, not the spectra; Remark 6.5(c) already notes the exact-sum improvement |
| B5 | Completeness is heuristic, and the scan protocol is untested beyond 24 corruptions (B-d M5, B-a M3) | ANSWERED IN PAPER in substance (items (iv)–(v), "completeness supported, not proved") | The protocol is now labelled empirical, tested on the 24 corruptions only. Inertia counts were not computed (the paper says so) |
| B6 | Physical framing: which inputs are spectral; absolute accuracies; omissions (B-a M3) | CONFIRMED (presentation) | New paragraph in the introduction: none of A, ε, M is read off finitely many eigenvalues (Theorem 1.3; Problem 1; no known bound for the area); accuracies absolute; the sum does not depend on the order of the list, but an omitted eigenvalue λ lowers it by e^{-λt}, which no budget covers |
| B7 | Overlap with the companion; reverse dependencies (B-a M2, B-b M3, B-c M2) | ANSWERED IN PAPER (Table 1 and the appendix declare the shared results; no main proof depends on the companion) | Reverse dependencies stated after Table 1; "nothing else here is taken from it" now excepts the shared spectra. The appendix is kept for self-containment, not cut |
| B8 | The constants of Theorem 6.2 say nothing about the least N (B-a M5) | CONFIRMED (presentation) | Introduction: "The formulas of Theorem 6.2 say nothing about the size of the least admissible N, which we do not know" |
| B9 | The order dependence of Section 4 is an artefact; Jørgensen for elliptic pairs; Dryden–Parlier (B-b M1) | CONFIRMED that an order-free route is plausible; not a correctness issue | Remark after Theorem 4.4: the elliptic Jørgensen identity and bound (attained in (2,3,7); `check_eigen_supporting.py` §5), Beardon §5.4, Dryden–Parlier cited; why not pursued: C_* enters only through log C_* in t_3, and t_1 binds in all but one row |
| B10 | Theorem 4.4 is not used in the logical chain, though the text said so (B-b M2, B-e m8, m1) | CONFIRMED | Text corrected: used in no proof of a main result; finiteness rests on Mumford–Bers; the instances use 2 diam P; kept as an explicit bound and for comparison with Proposition 8.2. Stanhope's isospectral diameter bound credited |

## MINOR items (deduplicated)

| id | item | resolution |
|---|---|---|
| b1 | "(C2) stronger criterion" (B-a m1) | "a second criterion, (C2), which implies the first" |
| b2 | two N conventions (B-a m2, B-d P2, B-e P3) | stated where the test is introduced |
| b3 | Figure 1 N = 21 vs 20 (B-a m3, B-d m1) | the text says N = 21 at the figure's grid and N = 20 on the finer grid; both true |
| b4 | legends in Figures 1, 2 (B-a m4, P5; B-d P1; B-e P4) | not done: no labels inside figures; the captions and text give the coding |
| b5 | Garbin–Jorgenson condition (b) granted (B-a m5); m ≥ 13 (B-b m7) | "granting this, and only for m → ∞" |
| b6 | ε ≤ 0.42 threshold; growth wording (B-a m6, B-e m10) | t_3 binds from 0.44; factors 5.24 falling below 4.7 (asserted in `theorem_e.py`) |
| b7 | grid optima; time used (B-a m7, B-e m9) | Table 3 gives the time |
| b8 | Jørgensen reproof (B-a m8, B-b m9) | kept (self-contained proof of the hyperbolic case) |
| b9 | systole margin wording (B-a m9) | "in all ten cases" |
| b10 | empirical labels (B-a m10) | the protocol labelled empirical |
| b11 | note's status (B-a m11) | template header defaults (see VERDICT-A a11) |
| b12 | bi-Lipschitz in dimension two (B-a m12) | stated |
| b13 | "analogue of their conjecture" (B-a m13) | "an analogue, in a loose sense" |
| b14 | Remark 6.5(a) as an observation; where it fails (B-a m14) | labelled an observation; fails at area 12π with orders up to 8: (0;2^4,7^7) and (0;4^6,8^4) share c_1..c_3 (asserted in `theorem_e.py`; the first wording, orders at most 3, was wrong and was caught by the blind check) |
| b15 | "oriented" with order-2 elements (B-b m2, B-c m4) | corrected |
| b16 | 10^29326 (B-b m4, B-d m6) | "about 3×10^196 and 2×10^29325" (asserted in `theorem_e.py`) |
| b17 | B_C monotone for fixed t (B-c m2) | stated |
| b18 | "or vanishes" (B-c m5) | removed |
| b19 | B_* defined in a statement (B-c m6) | in Corollary 6.3 |
| b20 | over-estimate wording (B-c m7) | "every term" |
| b21 | growth of |b_K(M)| (B-c m8) | "K^{-1/2} K!(M/π)^{2K} up to a constant", citing the companion's Lemma B.3 |
| b22 | Area lower bound for C (B-d m2) | "replaced by a lower bound such as π/21" |
| b23 | rounding and quadrature not in E_N (B-d m3) | stated |
| b24 | "geometric middle" (B-d m7); N_obs single t (B-d m8); factor 6–12 against the Sig(A,M) column (B-d m10) | fixed |
| b25 | Garbin–Jorgenson Thm 6.5 (B-e m2); LMPT "effectively" (B-e m4); Stanhope isolated singularities (B-e m5); "nothing else here" (B-e m7); 1 ≤ j ≤ 40 (B-e P2) | fixed |
| b26 | not done: B-b m1, m3, m5, m6, m8, m10; B-c m1 (answered by Remark 6.5(a)), m3, m9; B-d m4, m5, m11, m12; B-e m3, m6, m11; renamings (B-a P1, B-c P1, B-d P3) | judged not worthwhile this round, or not verifiable; no correctness issue |

## Mathematical changes (each with its check)

1. Proposition 6.4 (certified instances) — `theory/eigen/certified_gap.py`, `data/certified_gap.csv`.
2. The elliptic Jørgensen identity and bound — `theory/revision/check_eigen_supporting.py` §5.
3. The ε-threshold, growth factors and exponent range — `theory/eigen/theorem_e.py` (round-8 block).
4. The closed-geodesic overestimate — `theory/eigen/practice_checks.py`.

Blind check: `blind-check-B/REPORT.md`.
