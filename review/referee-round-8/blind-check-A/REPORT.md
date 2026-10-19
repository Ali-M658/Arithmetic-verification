<!-- Round 8 blind check A: returned text saved verbatim; the reviewer could not write files -->

Writing to `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/blind-check-A/REPORT.md` was refused, so the full report is below.

# Blind check A: report

**Summary.** I found no mathematical errors in any of the eight items.
- Items 1, 3, 4, 5, 6 and 7: **VERIFIED**.
- Item 2: **VERIFIED**, except that two thresholds are rounded up.
- Item 8: **VERIFIED with minor PROBLEMs**. Two numbers in the introduction are not in Remark B.5, and one of them is slightly too strong.

**How I checked.** I read the two PDFs as text and rendered pp. 15–20 and 51–54 as images to read formulas. All computations are my own code in `scratch/code/`, run in a venv I created at `scratch/venv` (mpmath, sympy, numpy). I rebuilt the heat coefficients α_k, φ_k, p_l and b_l from (4) and (5) in exact rational arithmetic (`heat.py`), and checked them against (8).

## 1. Lemma B.3 (growth of the cone coefficients) — VERIFIED

**Proof.** Each step is correct:
- **Principal parts.** The residues of Φ_m at ±π/m are ∓1/(4m sin(π/m)). The principal parts add up to A_m Σ(mu/π)^{2k}, with A_m = 1/(2π sin(π/m)).
- **Remainder.** It is holomorphic in |u| < 2π/m: the next poles of cot(mu) are at ±2π/m, the poles of 1/sin u are at jπ with π ≥ 2π/m, and u = 0 is removable.
- **Cauchy estimate.** It gives φ_k = A_m (m/π)^{2k}(1 + O(ρ^{-2k})) for ρ < 2.
- **Dominated convergence.** The ratio of the term k = l − j to the term k = l is at most (C/c)·x^{-j}/j! times a factor that is ≤ 1 and tends to 0, where x = (m/π)². The bound (C/c)·x^{-j}/j! is summable. With 4^{-l}(2l)!/l! ~ l!/√(πl), this gives the stated asymptotic.

**Numerics (`item1.py`).**
- **Taylor coefficients.** I expanded the defining sum Σ_j (4m sin θ_j sin(θ_j − u))^{-1} directly (60 digits). It matches (4) to 1e-56 for m = 2, 3, 7, 12, and the odd coefficients vanish.
- **Closed form and residues.** The closed form of Lemma 2.7 and the residues check numerically.
- **Rate for φ_k.** φ_k/(A_m(m/π)^{2k}) − 1 is about 2e-37 at k = 60. The decay rate tends to 1/2 (that is, ρ → 2) for m ≥ 3. For m = 2 the rate is 1/3, because the remainder extends further. Both fit "for every ρ < 2".
- **Asymptotic for b_l.** |b_l| divided by the asymptotic is 1.0031, 1.00094, 0.99984, 0.99946 and 0.99933 at l = 160 for m = 2, 3, 5, 8, 12. The error is O(1/l).
- **Proposition B.2.** I computed E_m(t) and the area integral by quadrature for m = 2, 8, 12. For K = 0..6 every truncation remainder has the stated sign and is at most the next term.

## 2. Lemma B.4 and Remark B.5 — VERIFIED (two thresholds rounded up)

**Proof of Lemma B.4.** It is complete:
- (6) with K = N − 1 bounds the expansion error.
- For genus 0, Area/4π < (n−2)/2.
- |b_{N−1}| increases with the order m (Proposition B.2(a)).
- B is monotone in the systole and the diameter, and proportional to 1/Area.
- The error identity for c̃ − c is correct, and the uniform bound follows from the row bounds.

**Inputs.** arccosh(cot²(π/8)) = 2.4485, so D = 4.897. A0 = π/2 is the area of O(2,8,8), and π/21 is the area of O(2,3,7). I took ℓ0 = 2.2567 as given.

**Recomputation (80–120 digits).** Q_3 = 303.63 and Q_8 = 2.7485e11.

| Claim in Remark B.5 | My value |
|---|---|
| N = 3: δ1 ≈ 4.9e3·τ | 4858.03·τ |
| δ1 unchanged for every ℓ0 ≥ 0.01 | confirmed (B0 is negligible) |
| τ below about 7.8e-11 | 7.822e-11 |
| at τ = 1e-11: η ≤ 2.07e-19 | 2.0714e-19 |
| N = 8: δthm met for τ ≤ 3.6e-3 | exact threshold **3.5968e-3** |
| at τ/2: η ≤ 5.0e-13 | 5.008e-13 |
| δcert met for τ ≤ 1.5e-2 | 1.5400e-2 |
| at τ/2: η ≤ 1.3e-8 | **1.2886e-8** |
| smallest time below 1e-4 | 5.86e-5 |

**Scan statement.** I minimised δ1 over N = 3..16, over T on a fine log grid up to 0.7819, and over four node families: geometric, Chebyshev–Gauss, Chebyshev–Lobatto, and Chebyshev in log t.

| a | best δ1 | meets δcert? | meets δthm? |
|---|---|---|---|
| 1e-3 | 1.27 | no | no |
| 9e-4 | 0.62 | no | no |
| 8e-4 | 0.25 | no | no |
| 7e-4 | 0.071 | no | no |
| 6e-4 | 0.013 | no | no |
| 5e-4 | 1.1e-3 | yes | no |
| 4e-4 | 4.8e-5 | yes | no |
| 3e-4 | 8.59e-7 | yes | no |
| 2.8e-4 | 3.3e-7 | yes | yes |
| 2.4e-4 | 3.9e-8 | yes | yes |

So all three scan claims hold. The actual crossings in these families are about 5.3e-4 for δcert and about 2.9e-4 for δthm.

**Rounding.** "τ ≤ 3.6×10⁻³" and "η ≤ 1.3×10⁻⁸" are rounded up from 3.597e-3 and 1.289e-8. Read literally, the endpoint values fail by 0.5% and 0.9%. Suggest "3.59×10⁻³" and "1.28×10⁻⁸", or add "about".

## 3. Conjecture 2.13 and Proposition 2.14 — VERIFIED

**Proof of Proposition 2.14.** Each step is correct:
- **Invariance.** Rotating the frame commutes with dΦ_p, so the polynomial is SO(2)-invariant. This also holds on the R_ϑ-invariant jets, which form an SO(2)-stable subspace.
- **Weight.** The weight is 2l, so the linear part involves only ∇^{2l−2}K.
- **Ricci identities.** The antisymmetric parts are at least quadratic in the jet.
- **Invariant forms.** Sym^{2l−2}(R²) splits into frequencies 2l−2, …, 0, each once. So the only invariant linear form is the full trace, which is (−Δ)^{l−1}K.
- **Duhamel step.** d/dε tr(R e^{−tΔ_ε}) = 2t·tr(R ψ Δ0 e^{−tΔ0}). I re-derived this, using cyclicity and that ψ is radial.

**Symbolic checks (sympy, l = 1..7).**
- The Gaussian integral equals −2l·l!·4^l·t^l·C^{−2l−2} exactly.
- The linear part of (−Δ)^{l−1}K(0) is −4^l(l!)²ε.
- So λ_l = 2/(l−1)!·C^{−2l−2}.
- At l = 1, 2Π_2(m) = p_1(m)/m exactly for m = 2..8.
- Π_4 reproduces the Δ²K coefficient in Remark 2.15(b).
- The normalisation of Conjecture 2.13(ii) is internally consistent: it gives (2l)!/l!·K^l at constant curvature, the stated linear part, β_{1,2} = 2K and β_{2,3} = 12K² − 2ΔK.

**Minor gap, not an error.** The proof takes the ε-derivative of the t^l coefficient to be the t^l coefficient of the ε-derivative of the trace. That interchange is standard but not stated.

**Separation from the conjecture.** It is clean. Proposition 2.14 does not depend on Conjecture 2.13 and holds for every m ≥ 2. The three unproved steps of the outline are named, and the paper says no result uses the conjecture. The introduction and the end of §2.4 are hedged.

## 4. Proposition 2.16(ii) — VERIFIED

Checked in sympy:
- The Gaussian moment (π/t)(2/t² + (2s−1)²|ζ|²/t + s²(1−s)²|ζ|⁴) is exact.
- The completed square is exact.
- The first Duhamel term is of order t⁻¹ only.
- The t^l coefficient of the second term equals ω_{l+1}/(2π) exactly for l = 1..8.

**General l.** Using I_l/I_{l+1} = 2(2l+3)/(l+1), the bracket reduces to (−1)^n n(n−1)n!/(2n+1)! with n = l + 1, for all l.

**Normalisation.** At l = 1 the formula gives (1/4π)∫K²/15 dA to order θ², the classical u_2. This independently confirms the (2π)^{-4} trace normalisation.

**Analyticity.** G_l is analytic because K_θ is entire in θ. G_l′(0) = 0 because the linear part of u_{l+1} is a multiple of Δ^l K, which integrates to zero. The remaining steps of the "if" argument also check.

## 5. Proposition 5.2, the search statement and Problem 5 — VERIFIED

**Case analysis.**
- **Area.** The area condition leaves genus 0 with at most five cone points, or (1;1). Three cone points are excluded by Corollary 5.1.
- **(1; m).** Here d = 0, so U = {p,q,r} and V = {m}. Then m = p+q+r, and m³ = p³+q³+r³ < (p+q+r)³ is a contradiction.
- **Five points.** Only {2,2,2,2,x} (any x) and {2,2,2,3,x} with 3 ≤ x ≤ 5 remain. Their products are 1 + 6/x, 10/6, 11/12 and 12/30, all below 9, against AM–HM.
  - Wording nit: "3 ≤ x ≤ 5" applies only to the second family, but 1 + 6/x ≤ 4 covers the first for every x.
- **Four points.** R(m′) = 1 + R > 1 forces a ∈ {2,3}. The converse comes from Lemma 3.6.

**Problem 5.** Allowing any positive integers p, q, r is harmless. Any solution forces p, q, r ≥ 2 and R < 1, so the stated equivalence holds.

**My search.** I solved for e2 and e3 exactly in integers and tested whether the cubic splits over positive integers. I sanity-checked the root-finder on known triples.

| Range searched | Cases | Solutions | Paper's range |
|---|---|---|---|
| {2,2,c,d}, d ≤ 10000 | 49,995,000 | none | d ≤ 1000 |
| b ≥ 3, d ≤ 100000 | 600,093 | none | d ≤ 20000 |

## 6. Theorem 5.8, last sentence — VERIFIED

**Proof.**
- Area ≤ π/2 forces genus 0 and at most four cone points.
- With four cone points only (0;2,2,2,3) (area π/3) and (0;2,2,2,4) (area π/2) qualify.
- A triangle sharing c1, c2 with one of these would need (S, R) = (8, 5/6) or (9, 3/4). Both have SR < 9, so neither exists.
- Two triangles that collide have R ≤ 3/4, with equality only at S = 18 (by majorisation).

**Brute force.** I enumerated all signatures with area ≤ π/2 (orders up to 3000) and grouped them by (area, c2). The only pair is O(2,8,8), O(3,3,12). It is still the only pair with area ≤ 3π/4 (orders up to 600).

## 7. Theorem C.2(b), Lemma C.1 and Theorem C.3 — VERIFIED

**Lemma C.1.** I built M and b with the paper's row and column indexing. On (2,8,8), (3,3,12), (2,3,7), (2,2,2,3), (3,10,15,30), (2,3,5,7,11) and (2,2,3,4,4,9), exactly:
- Me = b;
- B = YM;
- det B = (−1)^{n(n−1)/2}Π(m_i + m_j);
- det M = (−1)^{n(n+1)/2}Π(m_i + m_j)/e_n.

The column indexing is consistent. I also recomputed ζ_3 = 1, ζ_4 = 79/3 and ζ_5 = 14048/15.

**Theorem C.2(b).**
- The residual bound r_n is exactly what the entries give.
- The majorant |δT_k| ≤ η t_k(n) is valid.
- The Neumann step is correct: ‖X‖ ≤ cond·ζ_n·η ≤ 1/2, so ‖M(Ĩ)⁻¹‖ ≤ 2·cond.
- In 200 random perturbations per multiset (n = 3, 4), the error never exceeded the bound 2·cond·r_n·η (worst ratio 0.999).

**Theorem C.3.**
- sep_a and Π̂_a are both scaled, and the radius condition r_a ≤ µ·min(sep_a, 1)/2 is consistent with that. Taking sep = +∞ for a single distinct order gives min = 1.
- The Rouché inequalities give exactly the stated r_a.
- In Theorem C.4, the sep condition is automatic for integer orders.

## 8. Abstract and introduction against Remark B.5 — VERIFIED with minor PROBLEMs

The abstract, p. 3 ("t ≳ 10⁻³", against the remark's 1.5e-3) and p. 6 are consistent with Remark B.5.

Two problems with the p. 3 sentence "times reaching down to about 5×10⁻⁴ or below, with values accurate to 10⁻⁸ or better":

- **(a) The 5×10⁻⁴ figure is not in Remark B.5.** The remark only says no scan meets δcert for a ≥ 10⁻³. My scan puts the true crossing near 5.3e-4, so the number is right, but the remark should state it, or the introduction should say "below 10⁻³".
- **(b) "Accurate to 10⁻⁸ or better" is slightly too strong.** The remark gives only one example, η ≤ 1.3e-8. The largest admissible η for δcert in my scan (`item2c.py`) is:

  | a | largest admissible η |
  |---|---|
  | 4e-4 | 2.4e-11 |
  | 1e-4 | 1.7e-8 |
  | 1e-5 | 6.2e-8 |
  | 1e-6 | 5.8e-8 |

  So about 6×10⁻⁸ can suffice. "A few ×10⁻⁸" would be accurate. Also, time sets that reach only about 5×10⁻⁴ need far better accuracy, around 1e-11. For δthm the admissible η never exceeds about 1.2e-12.

Neither point affects any proof.

All scripts and scan outputs are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/blind-check-A/scratch/code/`.
