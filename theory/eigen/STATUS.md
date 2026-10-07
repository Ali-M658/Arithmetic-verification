# STATUS: theory/eigen

**Session goal.** Prove the analytic theorem that answers the referees (rounds 1–2: R1, and d M1).
Heat invariants are not finite spectral data, so why count them? Theorem E below answers this: the
first N eigenvalues, each known to accuracy δ, determine the signature. The counting of heat
invariants is what makes N and δ explicit. The first differing invariant is an integer multiple of
an explicit rational number (Lemma E1), and that gives an explicit gap between heat traces at an
explicit time.

**Audit.** **FREEZE WITH CHANGES** (`AUDIT.md`), with the changes applied.
- No FATAL findings.
- The only SERIOUS findings were two overclaims about the systole hypothesis. They are now
  withdrawn.

All seven verification scripts pass (`run.sh`).

## Tasks

| # | task | status | where |
|---|---|---|---|
| 1 | diameter bound D(A, ε, M); is M needed? | **DONE**. D explicit, O(AM³ + A/ε). M is necessary: diam ≥ log(M/2π) on the class, from O(2,3,m). The true growth in M, between log M and M³, is not determined | `diameter.tex`, `diameter.py` |
| 2 | N(x) ≤ e·Z(1/x); explicit bound on Z; tail bound | **DONE** | `counting.tex`, `counting.py` |
| 3 | explicit remainders of the cone and area expansions | **DONE**, strengthened in the audit: both expansions are enveloping for all t > 0, with sharp constants \|b_K(m)\| and \|α_{K+1}\| | `remainder.tex`, `remainder.py` |
| 4 | Theorem E with explicit N, δ | **DONE** | `theorem_e.tex`, `theorem_e.py` |
| 5 | necessity: (a) unbounded orders; (b) systole → 0 | (a) **DONE**. (b) **PARTIAL**: upper bounds along pinching families are proved; no necessity statement for the systole bound is proved (see below) | `necessity.tex`, `necessity.py` |
| 6 | Theorem 4.4 (now `thm:quantlocality`(a), §5) with D(A, ε, M) in place of the diameter | **DONE** (the constant is qualitative) | `locality.tex`, `locality.py` |
| 7 | Theorem E in practice on committed spectra | **DONE** | `practice.md`, `practice.py`, `data/practice.csv` |
| 8 | blind audit | **DONE**: 5 reviewers, verdict FREEZE WITH CHANGES | `STATEMENTS.md`, `AUDIT.md`, `audit/` |

## The statement for the paper (Section 4, `sec:eigen`, the slot in manuscript 665125e)

**Theorem E (`eig:E`).**
- **Data.** Let A > 0, ε > 0 and M ≥ 2 be an integer. Let D, t_*, Γ_*, Λ, N, δ be the explicit
  constants of `theorem_e.tex`.
- **Hypotheses.** Let O be a closed orientable hyperbolic 2-orbifold whose singular points are cone
  points, with
  - area ≤ A,
  - systole ≥ ε (least translation length over all hyperbolic elements),
  - all cone orders ≤ M.
- **Data.** Let λ̃_0, …, λ̃_{N−1} be real numbers with |λ̃_j − λ_j(O)| ≤ δ.
- **Conclusion.** σ(O) is the unique signature σ with area ≤ A and orders ≤ M that minimises
  |Σ_{j<N} e^{−λ̃_j t_*} − G_σ(t_*)|. Here G_σ(t) = I(t) + Σ_i E_{m_i}(t) is the signature part of
  the trace formula.
- **Corollary.** Two orbifolds in the class whose first N eigenvalues agree to within δ have the
  same signature.

**Ingredients, each a separate statement:**

| label | statement |
|---|---|
| eig:sep | Cone separation: d(p̃, q̃) ≥ min{ε/2, arccosh(1 + 2/(π²M²))} |
| eig:balls | Balls have area at least v_0 |
| eig:diam | diam < D = 4r_0A/v_0 ≤ (A/π)·max(4M, M²)·max(4/ε, 10M/3) |
| eig:elem | Area ≥ π/21; E_m ≤ b_0(m); I ≤ A/(4πt) |
| eig:counttail, eig:hypall, eig:count | 𝒩(x) ≤ e·Z_b(1/x); the tail bound; Hyp bounded at every t |
| eig:remcone, eig:remarea | Enveloping remainders: \|E_m − Σ_{l<K} b_l t^l\| ≤ \|b_K(m)\| t^K, \|I − (A/4π)Σ_{k≤K} α_k t^{k−1}\| ≤ (A/4π)\|α_{K+1}\| t^K, with signs, for every t > 0 |
| eig:int | Integrality: at the first differing index k of two equal-area signatures, d_k = (−1)^k a_{k−2}(P_{2k−3}(U) − P_{2k−3}(V)), with a nonzero integer factor, k ≤ ⌊Area/π⌋ + 4 and a_l = \|B_{2l+2}\|/(2(l+1)!(2l+1)). For different areas, \|d_1\| ≥ 1/(2 lcm) |
| eig:gap | \|G_σ − G_σ'\| ≥ Γ(t) = γ_* t^{k_*−2}/2 for t ≤ t_1 |

**Also for the paper:**
- **Proposition `eig:233`.** O(2,3,m) has area < π/3, systole ≥ 0.5620, and diam ≥ log(m/2π).
- **Proposition `eig:N1`.** For every N and δ, two O(2,3,m) have their first N eigenvalues within
  δ. With them, Remark `eig:Mneeded` shows that the order bound M cannot be dropped.
- **Theorem `eig:loc`.** Locality with the constant C(A, ℓ, D(A, ℓ, M)), which depends only on the
  signature and ℓ. It belongs in §5 after `thm:quantlocality`, or as a remark there.

## Size of N and δ (honest)

N and δ are explicit, finite and enormous:

| class (A, ε, M) | N | δ | binding |
|---|---|---|---|
| (π/2, 1.8626, 12) ∋ O(2,8,8), O(3,3,12) | 6.82 × 10⁹ | 4.2 × 10⁻²⁵ | t_1 |
| (π/2, 1.8626, 8) | 3.4 × 10⁸ | 3.1 × 10⁻²¹ | t_1 |
| (4π/3, 0.694, 3) ∋ the (0;3,3,3,3) family | 2.0 × 10⁷ | 3.4 × 10⁻²⁴ | t_1 |
| (4π/3, 0.694, 12) | 7.4 × 10¹² | 4.1 × 10⁻⁴¹ | t_1 |
| (2π, 0.1, 3) | 5.9 × 10⁸ | 8.9 × 10⁻³⁵ | t_1 |
| (10π, 1, 3) | 4.2 × 10¹⁸ | 1.7 × 10⁻¹⁸⁹ | t_1 |
| (10π, 1, 12) | 1.3 × 10³⁵ | 7.7 × 10⁻³⁸⁴ | t_1 |

**What binds.**
- In practice the binding constraint is t_1, set by the divergence of the cone expansion: the
  smallest possible first difference against the largest possible next term.
- The geometry, through t_3 ≈ ε²/(24D), binds only for small ε. Then N grows like
  ε⁻³ log(1/ε): checked, ratio about 8.7 per halving of ε at A = π/2, M = 7.
- log(1/δ) grows roughly like (A/π)² log(AM). This is an observation on the formulas, not a
  proved asymptotic.

**In practice (Task 7).** The nearest-signature rule of Theorem E, applied to the committed spectra:

| orbifold | observed count | a-priori count, modulo the a-posteriori error bars |
|---|---|---|
| O(2,8,8) | 3 | 21 |
| O(3,3,12) | 4 | 39 |
| (0;3,3,3,3) family, M = 3 | 3–50 | 33–694 |
| (0;3,3,3,3) family, M = 12 | 5–98 | 38–749 |

For the (0;3,3,3,3) family, the a-priori count is unavailable at systole 0.694, because the
committed 815 eigenvalues are too few. These are 10⁸–10¹² times fewer eigenvalues than the theorem
requires.

## Necessity: what is proved and what is not

- **Cone orders (proved, Proposition `eig:N1`).**
  - λ_j(O(2,3,m)) ≤ 1/4 + π²(j+1)²/h_m², with h_m = arccosh(1/(2 sin(π/m))). So
    limsup λ_j ≤ 1/4.
  - For all N and δ, among any (⌊Λ_N/δ⌋+1)^{N−1} + 1 orders m ≥ 7, two have their first N
    eigenvalues within δ. Their signatures differ.
  - Hence N and δ cannot depend on (A, ε) alone, for A ≥ π/3 and ε ≤ σ_0. Area and systole do not
    bound the cone orders.
- **Systole (not proved).**
  - Proved: along the pinching families (0;k,k,k,k), k = 3 or 4, λ_1 → 0 and
    limsup λ_j ≤ 1/4 (Proposition `eig:N2`).
  - Not proved: that (N, δ) cannot be chosen independently of ε with A and M fixed. The missing
    input is a lower bound λ_j ≥ 1/4 − o(1) for 2 ≤ j < N along two degenerating families of
    different signatures (spectral degeneration theory, not verified for orbifolds).
  - The audit showed that the first two eigenvalues already fail at a fixed systole, so the
    pinching result says nothing about the systole hypothesis. This claim has been withdrawn.
- **Limit of the O(2,3,m) eigenvalues (not proved).** That λ_j(O(2,3,m)) converges as m → ∞,
  expected to 1/4.

## Remaining items for the paper (other session)

1. **Fill the slot.** `\section{From heat invariants to eigenvalues}\label{sec:eigen}` gets an
   opening paragraph, Theorem E, and the ingredients in the order diameter → counting → remainder →
   integrality → gap → Theorem E → `eig:Mneeded`, `eig:N1`.
   - The fragments use the manuscript's macros and labels.
   - They cite the supplement's `sec:derivation` with `\sref` and Theorem 2.3, Lemmas 2.4–2.5 by
     their labels.
   - In the article class they set to 13 pages. Cut the tables, the closed forms and Proposition
     `eig:N2` to the supplement if space is short.
2. **Abstract placeholder.** Suggested clause: "Finitely many eigenvalues, known approximately,
   determine the genus and the cone orders among orbifolds of bounded area, systole bounded below
   and cone orders bounded above, with explicit (and very large) bounds; the bound on the cone
   orders cannot be dropped."
3. **Introduction slot (§1.1).** Suggested text: "Section 4 proves that the first N eigenvalues,
   each known to accuracy δ, determine the signature, with N and δ explicit in the area, a lower
   bound for the systole and an upper bound for the cone orders. The proof runs through the heat
   invariants: where two signatures first differ, the difference is an integer multiple of an
   explicit rational number, and this becomes an explicit gap between heat traces."
4. **Bibliography.** Add `jorgensen1976` (entry in `sources/README.md`). Its primary source is
   unreachable headless; the statement used is quoted from a fetched secondary source.
5. **Section 5 remark.** The sentence after `thm:quantlocality` ("the constant … depends on the
   diameter, which the signature does not determine") can now point to `eig:loc`.

## Wave 3 (2026-10-08): the material is now its own paper

Section 4 of the manuscript became `paper/eigen/manuscript.tex` (referee round 3, the split). Changes
here:

- `eigen_common.theorem_E_constants` uses k_* = min(floor(A/pi) + 4, M): with cone orders at most M
  the first difference occurs by the M-th heat invariant (`theory/msep/proof.tex`, part (i)).
  n_* = floor(A/pi) + 4 still bounds the number of cone points. The constants change where M is
  small: for (4pi/3, 0.694, 3), N = 3.7e5 and delta = 1.7e-10 (were 2.0e7, 3.4e-24); for
  (10pi, 1, 3), N = 1.1e7 (was 4.2e18). `theorem_e.py` asserts k <= min(floor(Area/pi) + 4, M).
- `practice.py` bounds the cone part of the tail by the maximum over the competitor set, so that the
  a-posteriori certificate (Theorem 7.1 of the eigen paper) does not use the unknown true signature;
  three N_apr values change by one (222 -> 223, 353 -> 354, 749 -> 750).
- The fragments `*.tex` and `STATEMENTS.md` are kept as the record of wave 2; the eigen paper is now
  the authority, and its proofs of (H1)-(H3), the commutator identity and Jorgensen's inequality
  (hyperbolic case) replace the numerical checks and the Wikipedia citation of `diameter.tex`.
