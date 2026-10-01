# Attack log: adversarial review of T2–T4

## Protocol

**What the reviewer was given.** The review was independent. The reviewer received only the
T2–T4 statements and proofs, i.e. `proof.md` §1–§5 with the T4 table as it stood then. That
input is kept as `attack/statements-under-attack.md`. The reviewer did not see:

- the scripts in this directory;
- their outputs;
- the audibility files.

**What the reviewer built.** Everything was reimplemented from scratch, in `attack/`:

- The cone polynomials were rederived from the Selberg trace formula (elliptic and identity
  terms; `cone.py`), not taken from the stated tables. The resulting L reproduces the stated
  rows of L⁻¹ and the row sums ℓ_r.
- The Theorem B system, the recovery map and both certificates of Proposition S5 were
  implemented independently.

**The instruction.** Break every claim, both by reading and numerically, including with
adversarial (not random) perturbations.

## Findings

| # | severity | finding | resolution |
|---|---|---|---|
| — | FATAL | none | — |
| — | SERIOUS | none | — |
| 1 | MINOR | Printed thresholds were rounded to nearest. The exact certificate **fails** at the printed 2.342e−3 for (2,8,8) and 1.462e−3 for (4,5,21,28); the exact certified maxima are 2.34171e−3 and 1.46177e−3. Conversely, δ_up for (3,3,12) printed as 4.588e−3 is below the constructed failure at 4.58827e−3. | **Fixed.** δ_thm and δ_cert are now printed rounded down, δ_up rounded up (`threshold.py` `fmt_down`/`fmt_up`). Every printed δ_cert is re-certified exactly (`threshold_output.md`). |
| 2 | MINOR | ζ_n had no range for j. Taken literally it is infinite. With j ≤ n−2: ζ₃ = 1, ζ₄ = 79/3, ζ₅ = 14048/15. | **Fixed** in proof.md. The code already used j ≤ n−2. |
| 3 | MINOR | The claim "δ_cert within a factor ≤ 2 of δ_up" fails for (3,10,15,30), where the ratio is 2.046. | **Fixed** before the review returned. The text now says 1.03–2.05 for n ≤ 4 and 7.3 for the n = 5 case. |
| 4 | MINOR | The constructed failure has a root with real part exactly a ± 1/2. That is a rounding tie, and under round-half-even it does not fail. | **Fixed.** δ_up is stated as an infimum: failures occur at every level above it. The reviewer confirmed failures just above δ_up. |
| 5 | MINOR | The conclusion of Theorem S3 needs the radius hypothesis for every distinct order. | **Fixed** in the statement. |
| 6 | MINOR | Prop. S3.2(i), (3,3,4,4): the ratio 2.0446 is for splitting the 3s; splitting the 4s gives 1.3593. | **Fixed** (both stated). |
| 7 | MINOR | In Theorem S2(a), "‖Ŝ‖_∞ = max(…)" is only an inequality when n = 2. | **Fixed** (≤). |

## Verified: no defect found

| claim | what was tried | result |
|---|---|---|
| Lemma S2.1, c_n = (−1)^{n(n+1)/2} | exact at rational multisets for n = 2..10, including coincident orders; symbolic in m for n = 2..5; det N and D_I e = −M⁻¹N exact for n ≤ 6 | holds; sign bookkeeping in the proof checked line by line |
| Lemma S2.2 | B is the map d ↦ W_D; B = S·M; det B, exact for n = 2..10 | holds |
| Theorem S2 | proof read for the majorant chain, residual and δM bounds, Hadamard bound; σ values reproduced (49/3, 76/3, 6628/15); part (b) attacked at every sign vertex, random points and by differential evolution, on 14 multisets with n = 3..6, including two small orders with one large one | holds; worst observed 0.065 of the bound; for n ≥ 5 the bound is loose (10⁻⁵ to 10⁻⁷ of it) |
| Lemma S3 | adversarial e-perturbations at the largest allowed ε, k = 1..6 | the count is always exactly k; worst k-th root at 0.981 r_a |
| Theorem S3 | data-space perturbations at the largest admissible δ, 80-digit arithmetic | counts exact; worst distance 0.08 r_a |
| Prop. S3.2 | double orders: ratios 2.73850, 4.46296, 2.04460 reproduced; ΔR, ΔP₁, ΔP₃ for (2,8,8) checked symbolically. k-fold orders: recovery returns q_s exactly | ratios constant in s: 4.939, 4.933, 2.201 (k = 3), 2.241 (k = 4) |
| Remark S3.3 | 20,000 real perturbations | holds; worst ratio 0.99975 (approached as d → −a). The hypothesis \|d_i\| ≤ a is redundant for positive orders. |
| Theorem S4 | δ_thm reproduced exactly: 3.803e−7, 1.189e−7, 4.021e−11, 3.147e−11 | holds |
| Prop. S5, soundness | adversarial search inside \|δH\| ≤ δ_cert at (2,8,8), (3,3,12), (3,10,15,30), (4,5,21,28): every box vertex, 4000 random points, differential evolution, dense grid, 60-digit recheck | **no failure.** Worst deviation of a rounded real part (failure at 0.5): 0.4846, 0.4672, 0.2412, 0.2483 |
| Prop. S5, tightness | empirical failure thresholds | 2.484862e−3, 4.588272e−3, 7.486520e−3, 2.017668e−3, matching δ_up. No cheaper failure exists below δ_up. |

**Physics of the dangerous direction.** At a double order the cheap perturbation does not
split the pair into a complex pair. Those directions move real parts by less than 0.03. The
dangerous perturbation keeps all roots real and pushes one root of the pair to a − 1/2. For
(2,8,8) at the failure threshold the roots are 2.027, 7.49999994 and 8.448.

## Files

`attack/` holds the reviewer's independent code and outputs:

- `cone.py`, `common.py`, `fast.py`;
- `t_front.py`, `t_lemmas.py`, `t_symbolic.py`, `t_s2b.py`, `t_s3.py`, `t_s3thm.py`,
  `t_sharp.py`, `t_misc.py`;
- `cert.py`, `t_cert_exact.py`, `dthm.py`, `attack.py`;
- the `*_output.txt` files.

The scripts were written for the reviewer's working directory. Their file paths are local to
it.
