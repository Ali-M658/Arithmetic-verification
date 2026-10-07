<!-- Returned text of the blind reviewer for Group 2 (remainders), saved verbatim by the main session: the reviewer could not write report files. Its scripts and outputs are in this directory. -->

# Blind referee report: Group 2 (remainders)

**Overall verdict:** all three statements (eig:remcone, eig:remarea, eig:Grem) are correct as stated, with no FATAL or SERIOUS issues and no index errors. The factor e^{t/4} in both remainder constants can be dropped, and then the bounds are exactly sharp.

**What I read:** only `theory/eigen/STATEMENTS.md` (Sections A, B and C/Group 2) and `theory/eigen/sources/`, which has nothing for this group. Everything was re-derived from thm:IEH, lem:Phi, prop:heatinput and the quoted supplement derivation.

**Scripts:** every check raises on failure, and all pass.
- `exact_checks.py`, with output in `exact_checks.out`: exact Fraction/sympy checks.
- `quad_checks.py`, with output in `quad_A.out`, `quad_B.out` and `quad_C.out`: 50-digit mpmath quadrature of E_m(t) and I(t), taken directly from the integrals of thm:IEH.

## Grades

| statement | grade |
|---|---|
| eig:remcone, remainder bound | NONE (true; e^{t/4} is superfluous) |
| eig:remcone, other parts: b_l identity, φ_k ≥ 0 and increasing, Cauchy bound, value at π/(2m), m/4, \|g_k\| bound | NONE |
| eig:remarea, including the μ_k formula | NONE (true; e^{t/4} is superfluous) |
| (eig:Grem), constants and indexing | NONE |
| presentation | MINOR (optional sharpening, below) |

## Derivations in brief

### Cone part (eig:remcone)
- **Expansion.** e^{t/4}E_m = Σ_j c_j ∫F_{2θ_j} e^{-tr²} dr, with c_j > 0 and F > 0.
  - For x ≥ 0 the Taylor tail of e^{-x} has sign (−1)^K and absolute value at most x^K/K!.
  - With the supplement moment identity this gives e^{t/4}E_m = Σ_{k<K} g_k t^k + R_K, where |R_K| ≤ |g_K| t^K and sgn R_K = (−1)^K.
- **The b_l identity.** It equals eq:bl exactly, so Σ_{l<K} b_l t^l is the degree-<K truncation of e^{−t/4}·Σ g_k t^k.
- **Remainder.** E_m − Σ_{l<K} b_l t^l = e^{−t/4}R_K + Σ_{k<K} g_k t^k [e^{−t/4} − T_{K−k−1}(t/4)].
  - The bracket is at most (t/4)^{K−k}/(K−k)! with no exponential factor.
  - So the stated bound holds even without e^{t/4}. The stated version is weaker, hence true.
- **Positivity and monotonicity.** By eq:phik, mφ_k is a positive combination of the terms (m^{2n}−1).
  - (m^{2n}−1)/m is strictly increasing in m.
  - So φ_k(1) = 0 and φ_k > 0 is strictly increasing for m > 1, which makes Q_cone monotone in m.
- **Cauchy bound.**
  - The nearest poles of Φ_m are at ±π/m.
  - Its series has nonnegative coefficients, so φ_k ρ^{2k} ≤ Φ_m(ρ) for 0 < ρ < π/m.
  - At ρ = π/(2m), cot(mρ) = 0, which gives cos(π/2m)/(4m sin²(π/2m)).
  - The bound ≤ m/4 is equivalent to x² cos x / sin² x ≤ π²/4 on (0, π/4]. The left side is ≤ 1 there.
  - The |g_k| bound follows by multiplying by (2k)!/(k!4^k).

### Area part (eig:remarea)
- **Splitting the integral.** For r > 0, tanh(πr) = 1 − 2/(e^{2πr}+1). So ∫ r tanh(πr) e^{−tr²} dr = 1/t − 4∫_0^∞ r e^{−tr²}/(e^{2πr}+1) dr.
- **μ_k.** The eta integral gives μ_k = 4(1−2^{−2k−1})(2k+1)! ζ(2k+2)/(2π)^{2k+2} = (1−2^{−2k−1})|B_{2k+2}|/(k+1), as stated.
- **Three remainder pieces:**
  - the tail of e^{−t/4}/t, at most t^K/(4^{K+1}(K+1)!);
  - the moment tail, at most μ_K t^K/K!;
  - the cross terms, at most μ_k 4^{k−K} t^K/(k!(K−k)!).
- **Result.** Again valid without e^{t/4}. The α_k derived this way equal the manuscript α_k exactly, and α_0 = 1.

### (eig:Grem)
- **Polynomial.** c_1 = α_0·A/4π. So Σ_{j=1}^{K+1} c_j t^{j−2} = (A/4π) Σ_{k=0}^{K} α_k t^{k−1} + Σ_i Σ_{l<K} b_l t^l.
- **Remainder.** These are exactly the two truncations, and both carry t^K.
- **Constants.** Q is increasing in t, so Q(·,t) ≤ Q(·,t_0) for t ≤ t_0.
- **Indexing.** remarea sums K+1 terms (k = 0..K) while remcone sums l < K. Both match j = 1..K+1, so there is no off-by-one.

## Sharper result (optional, MINOR)
The signs line up: g_k has sign (−1)^k and the Taylor tail with K−k terms has sign (−1)^{K−k}. So every piece of the cone remainder, and every term of b_K, has sign (−1)^K. The area part works the same way with sign (−1)^{K+1}. Hence:

- **Exact limits at t → 0.** Q_cone(m,K,0+) = |b_K(m)| and Q_area(K,0+) = |α_{K+1}|.
  - Both were checked in Fractions for m = 2..20 and K < 14.
  - So the bounds are asymptotically sharp: the quadrature gives a maximum ratio of 0.99995 at t = 1e−4.
- **Valid for all t > 0:**
  - |E_m − Σ_{l<K} b_l t^l| ≤ |b_K| t^K, with sign (−1)^K;
  - |I/(A/4π) − Σ_{k≤K} α_k t^{k−1}| ≤ |α_{K+1}| t^K, with sign (−1)^{K+1}.
  - So both expansions are enveloping.
  - Suggested fix: state Q_cone = |b_K| and Q_area = |α_{K+1}|. They are simpler, independent of t and sharp, and (eig:Grem) improves the same way.
  - If the current form is kept, at least note that e^{t/4} can be replaced by 1. At t_0 = 1, as used in Group 3, this only costs a constant of about e^{1/4}.
- **Cauchy bound is loose but true.** The choice ρ = π/(2m) loses a factor of about 4^k.
  - Exactly, φ_k (π/m)^{2k} tends to a constant: 0.159 for m = 2, 0.271 for m = 5, 1.017 for m = 20.
  - Taking ρ close to π/m would be near-optimal.
- **No sharpness claims to check.** STATEMENTS.md makes none for Group 2.

## What the code checked

### exact_checks.py (all pass)

| # | check | range |
|---|---|---|
| 1 | b_l identity equals eq:bl | l ≤ 14; m = 1..25, 3/2, 7/3 |
| 2 | Taylor coefficients of the lem:Phi closed form (sympy) equal eq:phik | m = 2..8, k < 8 |
| 3 | φ_k(1) = 0; φ_k > 0 and strictly increasing | m = 2..60, k ≤ 14 |
| 4 | α_k derived from μ_k equals the manuscript α_k; μ_k equals the zeta closed form | k ≤ 15 and k < 14 |
| 5 | Q_cone(m,K,0) = \|b_K\|, Q_area(K,0) = \|α_{K+1}\|, and the sign patterns | m = 2..20, K < 14 |
| 6 | (eig:Grem) polynomial identity (symbolic) | K = 0..6, 4 signatures |
| 7 | Cauchy bound, value at π/(2m) (closed form against the direct sum), m/4 bound, \|g_k\| bound | m = 2..40, k = 0..40 |

### quad_checks.py
Sanity checks pass: the t = 0 Euler beta integral to 1e−40, and the direct I(t) against the tanh-split form. Ratios are measured against the stated bound.

| test | range | cases | max ratio: t ≤ 1e−2 / 0.05–0.5 / t ≥ 1 |
|---|---|---|---|
| Cone: stated bound, \|b_K\| t^K bound, sign (−1)^K | m = 2..20, K = 0..8, 10 values of t from 1e−4 to 3 | 1710 | 0.99995 / 0.976 / 0.650 |
| Area: stated bound, \|α_{K+1}\| t^K bound, sign (−1)^{K+1} | K = 0..8, same t grid | 90 | 0.99998 / 0.990 / 0.831 |
| (eig:Grem) | 8 signatures, every t ≤ t_0 on the grid, K = 0..8 | 3960 | all pass |

The eight signatures are (0;2,3,7), (0;2,2,2,3), (2;), (1;2), (2;5,5), (0;20,20,20), (0;2,3,20) and (3;2,2,2,2). No counterexample was found, including for t > 1 and the largest K.

## Issues and fixes
1. **MINOR (optional):** e^{t/4} in Q_cone and Q_area is unnecessary, because the Taylor tail of e^{−x} for x ≥ 0 needs no exponential factor. Fix: replace it by 1, or better use Q_cone = |b_K(m)| and Q_area = |α_{K+1}|, which are sharp and valid for all t.
2. **MINOR (cosmetic):** "φ_k(m) ≥ 0 is increasing" can be strengthened to "> 0 and strictly increasing for m > 1, with φ_k(1) = 0".
3. **No index errors** in K, k, l or j.
