# STATUS: stability of the cone orders under errors in the heat coefficients

## Verdict

**PROVED, with explicit constants. Exact recovery is certified, and the blind experiment succeeds.**

- Heat coefficients → cone orders is Lipschitz at simple orders.
- It is Hölder with exponent 1/k at a k-fold coincidence.
- The exponent is sharp, both for realisable data (k = 2) and for general data (every k).
- For integer orders there is an explicit threshold below which rounding recovers the orders
  exactly.
- From the computed spectra alone, both (2,8,8) and (3,3,12) are recovered exactly from three
  coefficients, with certificates. Two coefficients cannot separate them.

## The planned structure, checked layer by layer

| layer | plan | outcome |
|---|---|---|
| heat → I_n | linear, triangular | **confirmed.** L is universal; n enters only through the offset. The diagonal factors 12, 360, 2520 are right, but the worst-case factors are the row sums **14, 498, 4062** (MAJ-05 corrected). Relative amplification is 0.02–3.7. |
| I_n → e | Lipschitz via Theorem B, det M = c_n ∏(m_i+m_j)/∏ m_i | **confirmed and sharpened.** c_n = (−1)^{n(n+1)/2} for **every** n (Lemma S2.1; previously only n ≤ 8). M⁻¹ = B⁻¹S with B a Hurwitz matrix, det B = ±∏(m_i+m_j) (Lemma S2.2). Explicit constant in Theorem S2. Normalised ‖M⁻¹‖ is 1–3.5 on every test multiset. |
| e → orders | Lipschitz away from coincidences, Hölder 1/k near a k-fold one | **confirmed** (Lemma S3, explicit Rouché constants; Theorem S3). **Sharp** (Prop. S3.2). Refinement (Remark S3.3): for heat data of *real* multisets near a triple order the exponent is 1/2, not 1/3. 1/k is the right exponent for noisy data. |
| integers | exact below a threshold | **confirmed.** Closed form δ_thm (Theorem S4) and a sharper exact certificate δ_cert (Prop. S5), bracketed above by an explicit failure δ_up. |

**One correction to the plan's wording.** The planned row says "det M = c_n ∏(m_i+m_j)/∏ m_i,
never 0". Since ∏ m_i = e_n this is right, and c_n is now known: c_n = (−1)^{n(n+1)/2}.

## T4 thresholds (absolute error, same δ on every coefficient)

| m | δ_cert | δ_up | binding relative precision (last coefficient) |
|---|---|---|---|
| (2, 8, 8) | 2.34e-03 | 2.48e-03 | 7.0e-04 |
| (3, 3, 12) | 4.04e-03 | 4.59e-03 | 7.5e-04 |
| (3, 10, 15, 30) | 3.66e-03 | 7.49e-03 | 3.6e-07 |
| (4, 5, 21, 28) | 1.46e-03 | 2.02e-03 | 1.7e-07 |
| (2, 3, 7) | 3.66e-03 | 6.59e-03 | 2.7e-03 |
| (4, 4, 4) | 4.54e-04 | 5.04e-04 | 5.4e-04 |
| (7, 7, 7) | 8.07e-05 | 8.27e-05 | 2.4e-05 |
| (3, 3, 4, 4) | 9.60e-05 | 1.19e-04 | 7.3e-05 |
| (5, 5, 5, 5) | 3.62e-05 | 3.83e-05 | 6.3e-06 |
| (2, 2, 2, 3) | 1.86e-04 | 2.52e-04 | 7.7e-04 |
| (2, 2, 2, 2, 3) | 7.91e-06 | 5.74e-05 | 2.0e-05 |

The closed form δ_thm is 10³–10⁶ times smaller (worst-case constants). Full table in proof.md §5.

## T5 blind result

The protocol (3c1139a) was committed before the pipeline (a4a87d7) and before the result
(1fa4ff4).

| | H₁ estimate | U(H₁) | δ_cert | recovered | certified | (est − true)/U |
|---|---|---|---|---|---|---|
| A = (2,8,8) | −3.33541350 | 2.1·10⁻⁵ | 2.3·10⁻³ | (2,8,8) | yes | +0.11, −0.13, +0.15 |
| B = (3,3,12) | −5.41869532 | 1.4·10⁻⁴ | 4.0·10⁻³ | (3,3,12) | yes | +0.29, −0.33, +0.39 |

- **Two coefficients:** the two-coefficient candidate set of both specimens is exactly
  {(2,8,8), (3,3,12)}, at 1U and at 3U.
- **Three coefficients:** with H₁ added, each set contains exactly one triple.
- The H₋₁ and H₀ estimates of A and B agree to 0.2σ and 0.3σ.

## Literature (review/literature/)

| question | verdict |
|---|---|
| (a) Theorem A prior art | **NOT FOUND** for the version with R = Σ1/m_i, over ℂ and over the positive reals. **KNOWN** for the odd-power-sum version (P₁,…,P_{2n−1}) on positive reals (Melánová–Sturmfels–Winter, Exp. Math. 2022, Prop. 24; attributed on MathOverflow to Steinig 1971). **KNOWN IN EQUIVALENT FORM** over ℂ (Korobov–Bugaevskaya, Math. Comp. 85 (2016), Hankel criterion; whether it matches m_i + m_j ≠ 0 was checked by the searcher only for even n). Caveat: the positive-real case of Theorem A may follow from Steinig / Drury–Marshall / Müller et al. real-exponent injectivity. Those are instrument gaps, not read. |
| (b) stability in inverse spectral problems | Lipschitz/Hölder for finite-dimensional unknowns and log for infinite-dimensional ones are standard, with non-explicit constants. The coincidence-driven loss of stability is known (Bondarenko 2025). Integer rounding from approximate spectra has a precedent (Léna–Serio 2020, a single integer, linear). No stability estimate for heat invariants was found. **What is new here:** the explicit constants, the sharp exponent 1/k tied to the coincidence multiplicity, and an explicit threshold for a multiset recovered through a nonlinear inversion. |
| (c) Bari–Hunsicker (arXiv:1705.01412; Canad. J. Math. 72 (2020)) | The manuscript's description is **INCORRECT**. They show that heat-trace expansions can agree to all orders for non-isospectral orbifold lens spaces; no finite count of coefficients appears. MAJ-12's reading is **CORRECT** (minor precision points in the note). |
| root perturbation (for T3) | Ostrowski, Acta Math. 72 (1940), Théorème XXX, read from the primary. Bhatia–Elsner–Krause only secondary (paywalled). |

## For the manuscript (not edited here)

- Cite Korobov–Bugaevskaya 2016 next to Theorem B. It is a linear "Newton-type" system for
  odd power sums with a Hankel nondegeneracy condition.
- Cite Uçar's Cor. 4.21(iv): the full spectrum determines the multiset of cone orders,
  qualitatively.
- The stability statement is in terms of heat coefficients. The step from eigenvalues to
  coefficients is empirical (§6 of proof.md), so do not call it "stability with respect to the
  spectrum".
- Replace the Bari–Hunsicker sentences: wording in `review/literature/bari-hunsicker.md`.

## Files

- **Proof:** `proof.md`.
- **Scripts:** `stab_common.py`, `front_end.py` (T1), `lipschitz_e.py` (T2), `roots_holder.py`
  (T3), `threshold.py` (T4), and their `*_output.md`; `threshold_results.json`.
- **Blind experiment:** `blind/PROTOCOL.md`, `blind/blind_pipeline.py`, `blind/RESULT.md`,
  `blind/result.json`.
- **Adversarial review:** `attack-log.md`.
- **Reproduce:**
  `cd theory/stability && for s in front_end lipschitz_e roots_holder threshold; do python $s.py; done && python blind/blind_pipeline.py`.
  Use the miniforge Python, with sympy, mpmath, numpy and scipy. threshold.py takes about
  30–60 min, almost all of it in the counterexample search.
