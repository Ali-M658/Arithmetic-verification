# FIX-CHECK-B (round 9): "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

Materials used: `main/scratch/B-r9final.pdf` (41 pp.) and `VERDICT-B.md` only. Pages were rendered with pdftoppm (100 dpi) and searched with pdftotext. Recomputations are in `fixcheck-B/scratch/code/` (venv with mpmath 1.4.1):

- `consts.py` recomputes the constants of Theorem 6.2 and the N, δ, Λt, B_* and t_2 of Table 3/4.
- `gap.py` and `ties.py` recompute by quadrature the least gap over Sig(A,M) for all six certified classes, and count the tied pairs.

## Summary

Every item B1–B8 and b1–b11 is visible in the PDF. B7 remains open in substance, as the verdict says. I found no FATAL or MAJOR problem introduced by the changes, and no broken references (no "??"). All recomputed numbers agree with the paper:
- Table 3 (N, δ);
- Table 4 (gaps, minimising pairs, B_*, Θ/8, Λt);
- Table 5 (all 8 rows, with the new δ_1);
- the exponents 9 and 26 of Remark 8.6.

There are five small new problems, listed at the end (N1–N5).

## Major items

| id | status | where | check |
|---|---|---|---|
| B1 | RESOLVED | pp. 16–17 | The certification paragraph (p. 16) covers everything the verdict lists: enumeration from n+4g ≤ A/π+4; the identity term as (A/4π)(e^{-t/4}/t − ∫_0^∞ 4re^{-t(1/4+r²)}(e^{2πr}+1)^{-1}dr) on [0,40] with tail ∫_40^∞ 4re^{-2πr}dr; elliptic intervals [−R_1,R_2] with the stated R_1, R_2 and tails; "all below 2e^{-80}"; ball evaluation of C_*, B_*, t_2, Z♯, Λ; N = ⌊eZ♯(1/Λ)⌋+1 taken only when strictly between integers (the same floor form as Theorem 6.2, p. 15); δ rounded down; python-flint 0.9.0 / FLINT 3.6.0, 200 bits, about half a minute. Table 4 (p. 17) is new. I checked the tails: 1/(2θ_j) ≤ M/2π ≤ 1.91 for M ≤ 12, so "below 2e^{-80}" holds, and the identity tail is about e^{-251}. **Recomputed by quadrature:** all six least gaps agree with "gap ≥" to every printed digit (e.g. 0.01588232199, 0.006527298332, 0.1520292966, 0.1655107998, 0.001373851304, 0.1666487023), and so do the counts \|Sig(A,M)\| = 27, 48, 8, 8, 281, 12. **Recomputed from t and Θ:** N = 244, 283, 139, 2605, 7416, 387182; δ = 1.167e-4, 4.273e-5, 5.899e-4, 4.867e-4, 2.488e-6, 2.141e-4; Λt = 17.63, 19.64, 12.52, 17.21, 27.94, 26.32; B_*(t) = 7.98e-6, 7.10e-5, 0.01793, 0.01671, 1.406e-4, 0.01394. All of these match Tables 3–4. The thin margin of row 3 (0.0180 against 0.01899) is stated and is indeed the smallest. See N1 (ties also occur at M = 8). |
| B2 | RESOLVED | p. 3 | The "What is new" paragraph names four contributions (Prop. 5.2 with the decision rule, Lemma 4.5, Prop. 6.5, Thm 1.2 / Cor. 8.5 / Remark 8.6). It says the closed-form constants matter only to show that explicit constants exist. |
| B3 | RESOLVED | p. 14 (definition of δ_1), p. 15 (proof of Lemma 6.1), p. 30 (Remark 8.6), p. 2 (abstract) | δ_1 = 1/(2 min(L_M, M^{2n_*})), justified in the proof of Lemma 6.1 (lcm of at most 2n_* orders ≤ M). I recomputed Table 5 with the new δ_1 and every entry matches: C_*, t_1, t_3, Θ_*, Λ, N, δ, binds (e.g. N = 3.399e8, 6.818e9, 4.319e4, 4.319e4, 7.436e12, 2.281e6, 1.084e6, 3.754e30). L_M < M^{2n_*} in every row, so the table is unchanged. **Remark 8.6:** I recomputed A = π/2, ε = 1, M = 2^k, k ≤ 16. The per-doubling exponents fall from above towards 9 (N) and 26 (δ^{-1}): 9.09 and 26.09 at M = 65536, a log-factor drift. C_* gives 9.000, so "approach 9 and 26" and "C_* grows like M^9" are correct. The jump to 17.1 / 54.0 at M = 32 is where M^{2n_*} starts to bind. The orders 2n_*+1 and 2n_*+(2n_*+1)(n_*−2) check out by hand. Abstract: "grows at most polynomially in M". |
| B4 | RESOLVED | p. 15 (Theorem 6.2 statement), p. 17 (Prop. 6.5), pp. 15–16 (Remark 6.3) | The weighted hypothesis is now in both statements. Remark 6.3's arithmetic is right: errors ≤ Θ_*/4 + Θ_*/(8e) ≈ 0.296Θ_*; adding Θ_*/8 gives 0.421Θ_* < Θ_*/2; each replacement of entries ≥ Λ_o changes Z̃ by ≤ e^{-Λ_o t_*}. The "over-estimate" correction from the blind check is in. See N2 (two wording points). |
| B5 | RESOLVED | p. 20 (now Remark 6.7) | Rewritten as the verdict says. The η_T of Lemma A.1 count eigenvalues with no geodesic term; the route would remove t_3 and Lemma 4.5 but needs the small eigenvalues and the separation for compactly supported g; not pursued. The renumbering is consistent: Remark 6.6 is "Sharper constants", and p. 25 cites "Remark 6.6(c)" correctly. |
| B6 | RESOLVED (two small inconsistencies, N3 and N4) | pp. 23–24, p. 22 | The Weyl estimate is replaced by min_s e^{-Λ_c(t−s)}(A/4πs + Σb_0 + B(s)), with Λ_c the smaller list maximum (2.17e4 / 2.19e4). The paper gives the tail ≤ 5.2e-11, the budgets 6.5e-11 / 5.4e-11 and the detection threshold "below about 1.56e4", and says that the 48 / 29 eigenvalues up to 1.6e4 rest on the window agreement alone. The sentence that the ε_j of the first 40 are at rounding level is on p. 23. Inertia counts not computed is said on p. 22. My check: −ln(6.5e-11)/0.0015 = 15638 and −ln(5.4e-11)/0.0015 = 15761. |
| B7 | PARTLY RESOLVED, as the verdict intends (not resolvable here) | p. 22, p. 20 (§7 intro) | The paper says how far it is from a proved determination: 283 eigenvalues to 4.27e-5 (≈1.9e-8 relative at λ_282 ≈ 2.25e3, which agrees with Weyl: 282·8 ≈ 2256); counts robust to 1e-3 relative; ε_j < 2e-13 relative for j < 283 (consistent with Table 7 and with "ten to twenty times the floor 10^{-14}λ_j"); what is missing (index-wise enclosures, signature-independent completeness). No proved determination is given, which is still the editor's blocking point. |
| B8 | RESOLVED (answered in paper) | p. 6, Table 1 p. 7, Appendix A | Table 1, the reverse dependencies and the self-contained Appendix A are present. |

## Minor items

| id | status | where | check |
|---|---|---|---|
| b1 | RESOLVED | p. 10 | §4 is titled "Separation of cone points and the count of closed geodesics". The opening paragraph names Lemmas 4.2, 4.3 and 4.5, and says Theorem 4.4 is used in no proof of a main result. |
| b2 | RESOLVED | p. 12 | The 1/M in v_0 is intrinsic for balls about a cone point: on O(2,3,M) the cone ball has area 2π(cosh 2r_0 − 1)/M, and 2r_0 = d_0 < h_M holds (e.g. M = 7: 0.091 < 0.54). d_0's 1/M is "not expected to be" intrinsic. Small omission: Prop. 8.2 needs M ≥ 7, and the sentence does not say so. |
| b3 | RESOLVED | p. 33 | (0;3,3,3,3) and (0;2,2,6,6) are named, with partitions {3,3}\|{3,3} and {2,6}\|{2,6} ({2,2} excluded: area 0, which I checked); an eigenvalue → 0; limits (0;3,3,∞) and (0;2,6,∞); what remains. Both signatures have area 4π/3 (checked). |
| b4 | RESOLVED | pp. 30–31 | "If it holds … would give lim inf λ_1 ≥ 1/4, and so λ_j → 1/4". Condition (a) for m ≥ 13 checked: m/2π ≥ 1 + m/4π ⇔ m ≥ 4π. |
| b5 | RESOLVED | p. 5, p. 30 | G_N: one cusp, orders 2 and N, a different family from the compact O(2,3,m), in both places. |
| b6 | RESOLVED | Table 1 p. 7, Thm 3.2 p. 10 | Both read "Cor. 3.8, Thm 3.11(i)". |
| b7 | RESOLVED | p. 11 | "X ≥ −cos(α+β) > −1, since 0 < α+β ≤ π". Correct, since sin α sin β ≥ 0 and cosh d ≥ 1. |
| b8 | RESOLVED | p. 7 | Theorem 2.1 is titled "Trace formula for the heat function", and Table 1 matches. |
| b9 | RESOLVED | Table 5 caption p. 18, Table 6 caption p. 22 | Table 5 rounds to nearest and Table 6 rounds up. Checked consistent: C_* = 3.545e9 → 3.5e9 / 3.6e9; 9.454e9 → 9.5e9 / 9.5e9; 4.0098e5 → 4.0e5 / 4.1e5. |
| b10 | RESOLVED | p. 4, p. 26 | "4.4 × 10^4 to 7.5 × 10^12 (rounded up)", and the true N are 4.319e4 and 7.436e12. Related ratios check out: 6.818e9/24 = 2.84e8 and /36 = 1.89e8 ("1.9 to 2.8 × 10^8"); Fig. 2's 56 and 2.7e11 (43190/767 = 56.3; 7.436e12/28 = 2.66e11); "6 to 12" (5.65–11.8). |
| b11 | RESOLVED | p. 19 | "N = 21 is the value drawn, and (C2) holds already with N = 20 (Table 8), at t ≈ 0.056". This matches Table 8 (20, window middle 0.0556) and the Fig. 1 caption (N = 21, 100). |

## New problems introduced by the changes

- **N1 (p. 16, Table 4): ties are not limited to M = 3.** The parenthesis says that in the classes with M = 3 several pairs attain the least gap. The M = 8 class (row 1) has a tie as well:
  - (0;2,3,8)/(0;2,4,5) attains the least gap 0.01588232199, exactly as Table 4's (0;3²,8)/(0;3,4,5) does. Both pairs share a common order and have the same area difference.
  - Rows 2 and 5 have unique minimisers. Rows 3 and 4 have 2 tied pairs, and row 6 has 3.
  - Suggested wording: "in the classes with M = 3 and in the first class".
- **N2 (p. 15, Remark 6.3): two wording points.**
  - "over-estimate λ_j by up to δe^{λ_j t_*} if the other values are exact": with the other values exact, the weighted hypothesis (sum ≤ Nδ) allows up to Nδe^{λ_j t_*}. The stated bound is valid but understates the allowance by a factor N. Either write Nδ, or drop "if the other values are exact" (δe^{λ_j t_*} is the allowance when every entry errs).
  - "The three errors in it add up to less than ¼Θ_* + Θ_*/(8e)": each bound is non-strict, so this should read "at most". The conclusion is unaffected.
- **N3 (p. 24): the 29 eigenvalues for O(3,3,12) do not fit the stated interval.** The text says "alone for the 48, respectively 29, eigenvalues between 1.56 and 1.6 × 10^4".
  - The detection threshold depends on the budget: 15638 for O(2,8,8) (budget 6.5e-11) but 15761 for O(3,3,12) (budget 5.4e-11).
  - The Weyl density is A/4π = 1/8, which fits the 2000 eigenvalues below 1.6e4. At that density, [15638, 16000] holds ≈ 45 eigenvalues (48 stated) and [15761, 16000] holds ≈ 30 (29 stated).
  - So the 29 refers to [≈1.576e4, 1.6e4]. About 50 eigenvalues of O(3,3,12) lie between 1.56e4 and 1.6e4.
  - Suggested fix: "between about 1.56 (respectively 1.58) and 1.6 × 10^4". The simpler alternative, saying the window agreement alone covers [1.56e4, 1.6e4] for both, also works.
- **N4 (p. 23): the tail bound "at most 5.2 × 10^{-11}" is sensitive to the unprinted digits of Λ_c.**
  - I grid-minimised e^{-Λ_c(t−s)}(1/(8s) + 1.4375) at t = 0.0015 (B(s) is negligible). The bound is 5.80e-11 at Λ_c = 21650, 5.39e-11 at 21700 and 5.01e-11 at 21750.
  - So the stated 5.2e-11 holds only if Λ_c(O(2,8,8)) ≳ 2.1725e4. The printed "≈ 2.17 × 10^4" cannot confirm this.
  - For O(3,3,12) (Λ_c ≈ 2.19e4) the bound is ≈ 4.0e-11, consistent with its budget.
  - I cannot settle this from the PDF. Suggested fix: print Λ_c to four or five digits. The budget 6.5e-11 and the conclusions survive either way, since the margin is 4.7e-13 against about 5e-11.
- **N5: two stale or incomplete sentences after B1 and B6.**
  - p. 6: "our completeness check follows the idea of Strohmaier and Uski, without their rigorous control of the tail." After B6 the tail above Λ_c is bounded rigorously (Prop. 5.2), conditional on completeness below Λ_c. The non-rigorous parts are now the ε_j, completeness and floating-point summation. The sentence should be updated.
  - pp. 33–34: the Data and code statement attributes Tables 2 and 5–8 to programs but not the new Tables 3 and 4. certified_gap.py is described only as "certifies Proposition 6.5".

No other inconsistency found. These cross-checks all agree with the text and tables:
- the abstract and intro ranges (N of order 10²–10⁴; δ ≈ 6e-4 to 2e-6, where the smallest is 2.48e-6);
- "N = 3.9 × 10^5" against 387182;
- "C_* between 4 × 10^5 and 7 × 10^10" against 4.01e5–7.09e10;
- "2.96e-3 ≈ 4.5 × 10^7 budgets";
- the counts quoted on pp. 4 and 26 against Table 8;
- all table renumberings (Tables 3–8);
- the remark numbering (6.3, 6.6(c), 6.7).

Typography in the rendered pages is clean (pp. 2–3, 10–12, 14–20, 22–24, 26, 30–33). One cosmetic point: Table 3 mixes ε = 1.8626 with ε = 2.633915 / 0.693994, while Table 5 uses 2.6339 / 0.6939 for the same classes.

## Follow-up (main session)

- N1: the tie in the first class, (0;2,3,8)/(0;2,4,5), is now stated next to the M = 3 ties.
- N2: Remark 6.3 now says "up to Nδe^{λ_j t_*}" and "add up to at most".
- N3, N4: Λ_c is printed as 2.174e4 and 2.189e4 (from `practice_checks.py`: 21740 and 21890). The detection thresholds are given per orbifold, 1.563e4 and 1.576e4. The 48 and 29 eigenvalues are counted from these thresholds to 1.6e4 (recounted by the script).
- N5: the Strohmaier–Uski sentence is updated. The data statement now names `certified_gap.py` and `make_tables.py` for Tables 3 and 4.
- Cosmetic ε decimals: not changed.
