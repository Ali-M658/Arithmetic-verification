# G5 referee report: STABILITY group (ST.0–ST.14)

Scope: re-derivation from the statements in `review/audit/statements/stability.md` and the fetched
sources only. Every check is a script in this folder. Each runs from the repo root and exits
nonzero on failure. Arithmetic is exact (`fractions.Fraction`, sympy rationals). Floats are used
only as search heuristics: the optimiser in `check_dup.py`, the football transcription sanity
check in `check_frontend.py`, and the Ostrowski sanity check. Every value reported from those
searches was then re-evaluated exactly.

| script | covers | output |
|---|---|---|
| `stab_lib.py`, `s5_lib.py` | shared library: Uçar coefficients, L, Theorem B system, Routh–Hurwitz counts; the Prop. S5 certificate and δ_thm | — |
| `check_frontend.py` | ST.0, ST.1, ST.2 | `check_frontend.txt` |
| `check_det.py` | ST.0 (homogeneity), ST.3, ST.4 | `check_det.txt` |
| `check_s2.py` | ST.5 | `check_s2.txt` |
| `check_ostrowski.py` | ST.6 | `check_ostrowski.txt`, page images `ostrowski_p53.png`, `ostrowski_p55.png` |
| `check_s3.py` | ST.7–ST.11 | `check_s3.txt` |
| `check_s5.py` | ST.12, ST.13, ST.14: δ_thm, δ_cert, relative columns, ε_cert | `check_s5.txt`, `check_s5.json` |
| `check_dup.py` | ST.13/ST.14: δ_up constructions | `check_dup.txt`, `check_dup.json`, `check_dup.log` |
| `check_probe.py` | P3 soundness probe | `check_probe.txt` |

## Summary

| item | result | grade |
|---|---|---|
| ST.0 setting | Uçar (4.25)+(4.33)+(4.35) give exactly the stated H₋₁, b_ν, α_j. The weighted homogeneity M(Î)=D_r⁻¹M(I)D_c holds | NONE |
| ST.1 Prop. S1 | L, h₀ and the diagonal formula are correct. H = L·I + h₀ holds identically | NONE |
| ST.2 front-end tables | every entry of L⁻¹, the diagonal and ℓ_r up to P₁₃ match. κ_r for (2,8,8) is 0.33/0.94/1.33 | NONE |
| ST.3 Lemma S2.1 | c_n = (−1)^{n(n+1)/2} is proved for all n (below) and checked exactly for n = 2..10 | NONE |
| ST.4 Lemma S2.2 | B = S·M, det B, det S and M⁻¹ = B⁻¹S are proved and checked. W_D is mis-normalised (off by a factor z) | MINOR |
| ST.5 Thm S2 | all constants and every inequality in the chain are valid | NONE |
| ST.6 Ostrowski | page, equation and constant (2n−1) are right. γ must be the largest root modulus of **both** polynomials, and the ε formula silently re-indexes the printed (69,3)–(69,4) | MINOR |
| ST.7 Lemma S3 | proved: the 3ⁿ and 2^{1−k} constants, \|z\| ≤ 3/2 and the hypothesis on r all check | NONE |
| ST.8 Thm S3 | proved, and tested at the edge of all hypotheses | NONE |
| ST.9 Prop. S3.2 | (i) ΔR, ΔP₁, ΔP₃ and all four ratios are confirmed. (ii) is correct but lacks the non-degeneracy hypotheses | MINOR |
| ST.10 Rem. S3.3 | identity and inequality proved | NONE |
| ST.11 Thm S4 | proved. All 11 printed δ_thm reproduce exactly (rounded down) | NONE |
| ST.12 Prop. S5 | the certificate is valid (proof below). There is a stray cross-reference, and two hypotheses are left implicit | MINOR |
| ST.13 δ_up / rounding | ties built within (1+10⁻³)δ_up for all 11 rows. For (2,2,2,2,3) the printed δ_up is 8% above a failure I built exactly. The "fails at 2.342e−3 / 1.462e−3" claims are confirmed | MINOR |
| ST.14 results table | all 11 δ_thm, δ_cert and ε_cert values re-certified exactly at the printed values, and every printed δ_cert equals my 4-s.f. maximum. Probe: 22,184 exact samples, 0 failures | NONE (one δ_up/δ_cert ratio, see ST.13) |
| source register | `holtz_tyaglov_1005.2843.txt` is a hep-ph paper by M. Rauch. The Holtz–Tyaglov paper is arXiv:0912.4703 | MINOR (citation; must fix) |

No FATAL or SERIOUS findings.

---

## ST.0 Setting and the recovery map

**Derivation.** Uçar Thm 4.20 and (4.35): a_ν(O) = vol·α_ν, where
α_ν = (ν!4^ν)⁻¹ Σ_ℓ C(ν,ℓ)(−4)^ℓ B_{2ℓ}(1/2) κ^ν. With κ = −1 this gives 1, −1/3, 1/15, −4/315, 1/315, −4/3465.

Thm 4.20(ii) and (4.33): a cone point of order k contributes C = Σ_ν b_ν t^ν, where
b_ν(k) = Σ_{ℓ≤ν} 2/(4^ℓ ℓ!)·c^S_{ν−ℓ}(π/k)·κ^ν. Here c^S_ℓ(π/k) from (4.25) is 1/k times an even polynomial in k of
degree 2ℓ+2 that vanishes at k = 1, because of the factor (k^{2j}−1). Therefore
b_ν = (−1)^ν p_ν(m)/m with p_ν even, of degree 2ν+2, and p_ν(1) = 0, as stated.

- b₀ = (m²−1)/(12m).
- π_{1,·} = (−11/360, 1/36, 1/360).
- π_{2,·} = (−37/5040, 1/180, 1/720, 1/2520).

Area/(4π) = (n−2−R)/2 follows from Gauss–Bonnet.

**Transcription check.** As an independent check on the reading of (4.25)/(4.33), I compared with
κ = +1 against the exact spectrum of the football S²/Z_k: eigenvalues l(l+1), with multiplicity
2⌊l/k⌋+1. The difference from the expansion through t⁴ is O(t⁵) for k = 2, 3, 5: residual/t⁵ is stable
to below 1% between t = 4·10⁻⁴ and 2·10⁻⁴.

**Homogeneity.** The entry M_{jk} = −T_{2j+1−k} has weight 2j+1−k, and the last row has weights
n−1−k. Therefore M(Î) = D_r⁻¹ M(I) D_c, and ê solves M(Î)ê = b(Î). This was checked exactly for n = 2..7.

**Not checked.** I could not check the Selberg cross-check of α_j up to j = 11, because the script
it refers to is outside my remit. **Grade: NONE.**

## ST.1 Proposition S1

**Proof.** Σ_i b_ν(m_i) = (−1)^ν Σ_k π_{ν,k} Σ_i m_i^{2k−1}. The k = 0 term is π_{ν,0}·R, and the k ≥ 1
terms are π_{ν,k}·P_{2k−1}. Adding (Area/4π)α_{ν+1} = ((n−2)/2 − R/2)α_{ν+1} gives exactly the stated L and h₀.

- Row ν+1 involves P up to P_{2ν+1}. So L is lower triangular, and it is independent of n.
- The diagonal is (−1)^ν π_{ν,ν+1}. Only the ℓ = 0 term of (4.33), i.e. 2c^S_ν, reaches degree k^{2ν+1}. Its
  leading part comes from the j = ν+1 term of (4.25), with B₀(1/2) = 1:
  2·(1/(4k))·(−1)^ν/((ν+1)!(2ν+1))·B_{2ν+2}k^{2ν+2}.
- Multiplying by κ^ν = (−1)^ν gives b_ν ~ B_{2ν+2}m^{2ν+1}/(2(ν+1)!(2ν+1)). Since sign B_{2ν+2} = (−1)^ν, this
  gives π_{ν,ν+1} = |B_{2ν+2}|/(2(ν+1)!(2ν+1)), as claimed.

The identity H = L·I + h₀ was checked exactly against direct evaluation of Uçar's formulas: 6 integer
and 6 rational random multisets for each n = 2..8. The diagonal formula was checked for ν ≤ 6. **Grade: NONE.**

## ST.2 Front-end tables

I computed L⁻¹ exactly for n = 8.

- The rows R, P₁, P₃, P₅, P₇ match the table, including −70/3.
- The diagonal 1/|L_rr| = 2, 12, 360, 2520, 10080, 28512, 43243200/691, 112320 matches.
- The row sums ℓ_r = 2, 14, 498, 4062, 56230/3, 303654/5, 104899830/691, 10805786/35 match.
- The ratios ℓ/diag are 7/6, 83/60 and 677/420, i.e. 1.17, 1.38 and 1.61, as stated.

The worst case ℓ_r·δ is attained by the sign pattern of row r.

κ_r on the 11 table multisets lies in [0.024, 3.699]. For (2,8,8) it is (0.333, 0.944, 1.328) → 0.33, 0.94, 1.33.
I cannot see the full list of multisets in `front_end_output.md`, so I checked the "0.02–3.7"
claim only on the table rows, where it holds. The maximum, 3.699, sits right at the stated edge.
**Grade: NONE.**

## ST.3 Lemma S2.1 and ST.4 Lemma S2.2

**Proof of S2.2.** Write X_D := E_f O_D − E_D O_f = ½(f(−z)D(z) − f(z)D(−z)).

1. *X_D is odd in z, of degree ≤ 2n−1.* So X_D = z·W(z²), with deg_w W ≤ n−1. The statement calls X_D itself "a
   polynomial in w = z²". It should be W_D := (E_f O_D − E_D O_f)/z (**MINOR**).
2. *B is the matrix of D ↦ W_D.* Because [z^{2k+1}] gives +e_{2k+1−j} for odd j and −e_{2k+1−j} for even j,
   B_{k,j} = (−1)^{j+1}e_{2k+1−j}.
3. *Rows k ≤ n−2 of S·M.* Row j of the homogeneous part of M is [z^{2j+1}](O_D − T·E_D). Because
   E_f·T = O_f (Theorem B's T = O_f/E_f), [z^{2k+1}] E_f(O_D − T E_D) = [z^{2k+1}] X_D. This is (S·M)_k for k ≤ n−2.
4. *Last row of S·M.* The top coefficient of X_D is e_n d_{n−1} − e_{n−1} d_n for n even, and minus that for n
   odd. In both cases it is (−1)ⁿ e_n(d_{n−1} − R d_n) = (S·M)_{n−1}.

So B = S·M. det S = (−1)ⁿe_n, because S is lower triangular with diagonal (1, …, 1, (−1)ⁿe_n).

**det B, divisibility.** det B is a symmetric polynomial in m, homogeneous of weight
Σ(2k+1) − Σj = n(n−1)/2. Suppose m_i = −m_j. Then f(z) = (1+m_i z)(1−m_i z)k(z), and D = z²k(z) is a non-zero
element of the kernel: D(0) = 0, deg D = n, and f(−z)D(z) = f(z)D(−z). So every (m_i+m_j) divides det B.
Hence det B = c′_n ∏_{i<j}(m_i+m_j).

**det B, the constant.** Set m_n = 0. Then the last row of B_n becomes (0, …, 0, (−1)^{n+1}e′_{n−1}), and the
complementary minor is exactly B_{n−1}(e′). So c′_n e′_{n−1}∏′ = (−1)^{n+1}e′_{n−1}c′_{n−1}∏′, i.e.
c′_n = (−1)^{n+1}c′_{n−1}. With c′_1 = 1 this gives c′_n = (−1)^{n(n+1)/2+n−2} = (−1)^{n(n−1)/2}.

**Proof of S2.1.** det M = det B/det S = (−1)^{n(n−1)/2+n}∏/e_n = (−1)^{n(n+1)/2}∏/e_n. The proof needs no
appeal to Orlando's formula.

**Exact checks** (`check_det.txt`):

- For n = 2..10, on 9 multisets each (random rationals, all-ones, 1..n, and (2,…,2,3)), I checked: M e = b;
  det M = c_n∏/e_n; S·M = B; det B; det S; M⁻¹ = B⁻¹S; and that B represents D ↦ W_D.
- det B = (−1)^{n(n−1)/2}∏(m_i+m_j) was also checked as a polynomial identity in sympy for n ≤ 5.

The observed signs are c_n = −, +, +, −, −, +, +, −, − for n = 2..10.

**Grades.** S2.1: NONE. S2.2: MINOR. **Fix:** define W_D := (E_f O_D − E_D O_f)/z. Optionally include the
three-line m_n → 0 induction for the constant.

## ST.5 Theorem S2

**Proof.** Work in scale-free variables.

1. *Majorants for U and δU.* Û = Σ_i artanh(m̂_i z) has coefficients P̂_k/k ≤ n/k, so Û ≪ n·artanh w. The
   perturbation δÛ has |δÛ_k| ≤ η/k, so δÛ ≪ ηβ with β := artanh w.
2. *Majorant for tanh.* |[x^j] tanh^{(k)}| ≤ [x^j] tan^{(k)}, so
   T̃ − T̂ = Σ_{k≥1} tanh^{(k)}(Û)δÛ^k/k! ≪ tan(nβ + ηβ) − tan(nβ).
3. *Using η ≤ 1.* (ηβ)^k ≪ ηβ^k, so the right side is ≪ η(tan((n+1)β) − tan(nβ)).
4. *Mean value.* tan((n+1)β) − tan(nβ) = ∫₀¹ β sec²(nβ+tβ) dt ≪ β sec²((n+1)β), because sec² has non-negative
   coefficients. Hence |δT_k| ≤ σ_k(n)η.
5. *Residual.* Let M̃ = M + δM. Then M̃(ẽ − ê) = δb − δM·ê. Its row j is Σ_{i≤j} δT_{2i+1} ê_{2j−2i}, and its last
   row is δR̂·ê_n. So the residual is bounded by ρ_n η. Also ‖δM‖_∞ ≤ ζ_n η: the rows use only i < j with
   2 ≤ 2j−2i ≤ n, and the last row has |δR̂| ≤ η.
6. *Neumann series.* If β = κζ_nη ≤ 1/2, then ‖M̃⁻¹‖ ≤ κ/(1−β) ≤ 2κ. This gives (b).

**Proof of (a).** M⁻¹ = B⁻¹S. Every column of B(ê) has 2-norm ≥ 1: an odd column contains ê₀ = 1, and an even
column j ≤ n contains ê₁ ≥ m̂_max = 1. So by Hadamard every cofactor is ≤ Λ, and ‖B⁻¹‖_∞ ≤ nΛ/|det B|.
The second bound uses ê_k ≤ C(n,k), so Σ_k ê_k² ≤ C(2n,n), and Σ_{k even} C(n,k) = 2^{n−1}.

**Exact checks.**

- σ₁ = 1 and σ₃ = 1/3+(n+1)² for n = 2..8.
- The listed examples: n = 3 gives (1, 49/3); n = 4 gives (1, 76/3, 6628/15); ζ₃ = 1, ζ₄ = 79/3, ζ₅ = 14048/15.
- 1,039 coefficient checks of |δT_k| ≤ σ_kη, including η = 1 and box corners. The maximum ratio is 1, attained at
  k = 1, where δT₁ = δP̂₁.
- 400 exact perturbations at the edge β = 1/2, covering repeated orders, order 1, and ratios up to 10⁶. The
  maximum observed ratio to the bound in (b) is 0.59.
- The chain in (a) was verified exactly via squared norms. **Grade: NONE.**

## ST.6 Ostrowski input

**Verified against the PDF.** I rendered pp. 210 and 212 (the OCR text is too garbled to rely on).

- p. 212 contains (71,1), |y_ν − x_ν| ≤ (2n−1)ε ≤ (2n−1)Mδ^{1/n} < 4nTδ^{1/n}.
- p. 212 also contains Théorème XXX, which refers to ε of (69,4), and the sentence "…satisfont, comme fonctions
  des coefficients, à une condition de Lipschitz d'ordre 1/n".
- p. 210 has "Soit γ = Max(|x_ν|, |y_ν|)" and (69,4): ε = (Σ_{ν=0}^{n−1}|a_ν − b_ν|γ^ν)^{1/n}.

**Discrepancies.**

1. *γ must range over both root sets.* The paper writes "γ is the largest root modulus", but in Ostrowski γ is
   the maximum over the roots of f **and** g. The distinction matters: f = z², g = z² − z gives ε = 0 if γ is
   taken over the roots of f alone, yet a root moves by 1 (`check_ostrowski.py`).
2. *Silent re-indexing.* The printed (69,3)–(69,4) carry the index ν = 0..n−1 on y^ν, which does not match the
   (69,1) convention f = Σ a_ν z^{n−ν}. The paper's Σ_{ν=1}^{n}|a_ν−b_ν|γ^{n−ν} is the consistent reading, but it
   is a re-indexing, not a quotation.

**Grade: MINOR. Fix:** "where γ = max(|x_ν|, |y_ν|) over the roots of both f and g (Ostrowski's (69,4), indices
adapted to (69,1))".

## ST.7 Lemma S3

**Proof.**

1. *Perturbation on the circle.* On |z−a| = r ≤ 1/2 with a ≤ 1, |z| ≤ 3/2. So
   |q̃ − q| ≤ εΣ_{j=1}^n(3/2)^{n−j} = 2ε((3/2)ⁿ−1) < 3ⁿ2^{1−n}ε (strict for ε > 0).
2. *Lower bound for q.* For r ≤ g_a/2 we have |z−b| ≥ |a−b| − r ≥ |a−b|/2. So |q| ≥ r^k Q_a 2^{−(n−k)}.
3. *Rouché.* r^kQ_a ≥ 2^{1−k}3ⁿε gives |q| > |q̃−q| on the circle, hence exactly k zeros in the open disc.
4. *Disjointness.* The discs for distinct a are disjoint, since r_a + r_b ≤ |a−b|.

So 3ⁿ and 2^{1−k} are correct (with room to spare), and the condition r ≤ min(g_a,1)/2 is exactly what the
proof uses.

**Exact check.** I counted roots exactly in discs, using a Möbius map to the half-plane followed by the Routh
array. In 1,408 cluster/perturbation pairs, the count is k both at r = r_a(ε) (rounded up rationally) and at
r = min(g_a,1)/2. The pairs covered: n ≤ 5, multiplicities up to 5, ε from 10⁻³ to 10⁻¹², and adversarial ±ε
signs. **Grade: NONE.**

## ST.8 Theorem S3

**Proof.**

- With η := max(μ|δR|, |δP_{2l−1}|/μ^{2l−1}) ≤ λ_μδ, the hypotheses give η ≤ 1 and β ≤ 1/2.
- Theorem S2(b) then gives |ẽ_k − ê_k| ≤ ε := 2κρ_nλ_μδ.
- Lemma S3 applies with r̂ = r_a/μ, since r̂^kQ̂_a = 2^{2−k}3ⁿκρλδ = 2^{1−k}3ⁿε. Scaling back by μ gives the
  conclusion.
- The matching distance is ≤ max_a r_a, because the cluster discs are disjoint and contain k_a roots each.

**Exact check.** I tested 120 random multisets (repeated orders, order 1, ratios up to 400) at the **largest** δ
allowed by all three hypotheses, with the binding hypothesis attained with equality, and 4 random corners each.
Exact disc counts confirm k_a roots within r_a for all 1,152 clusters.

*Observation:* at δ = min(1/λ, 1/(2κζλ)) the radius hypothesis already fails for every cluster, so the radius
condition is always the binding one. **Grade: NONE.**

## ST.9 Proposition S3.2

**(i)** H(m(s)) is symmetric under s ↦ −s, so it is even. For (2,8,8), exactly:

- ΔR = 16/(64−s²) − 1/4 = s²/(4(64−s²)), which equals the printed 2s²/(8(64−s²));
- ΔP₁ = 0;
- ΔP₃ = 48s².

The limits of s/‖ΔH‖^{1/2} = (max_ν|[s²]ΔH_ν|)^{−1/2}, computed exactly with L, are:

| multiset | split | my limit | printed |
|---|---|---|---|
| (2,8,8) | the 8s | 2.7385014 | 2.7385 |
| (3,3,12) | the 3s | 4.4629623 | 4.4630 |
| (3,3,4,4) | the 3s | 2.0445998 | 2.0446 |
| (3,3,4,4) | the 4s | 1.3592693 | 1.3593 |

The O(s) term vanishes in every case.

**(ii)** I confirmed ΔH = O(s^k) with vanishing lower-order terms. The limits are:

| k | case | limit |
|---|---|---|
| 3 | (4,4,4) | 4.93886 |
| 3 | (7,7,7) | 4.93311 |
| 3 | (2,2,2,3) | 2.20128 |
| 4 | (5,5,5,5) | 2.24054 |

Exact recovery returns q_s at s = 1/1000 (Theorem B).

**Gap.** For general g, the statement needs:

- a ≠ 0 and g(0) ≠ 0, so that e_n ≠ 0 and R = e_{n−1}/e_n is defined;
- ∏(z_i+z_j) ≠ 0 at s = 0, so that M is invertible (Lemma S2.1). This fails, for example, if g(−a) = 0.

These hold for orders that are positive reals. **Grade: MINOR. Fix:** add "with the roots of g in the open right
half-plane (e.g. positive orders)".

## ST.10 Remark S3.3

Σ[(a+d)³ − 3a²(a+d) − (a³ − 3a³)] = Σ(3ad² + d³), checked symbolically. Since d ≥ −a, d³ ≥ −ad², so the sum is
≥ 2aΣd², and max|d_i|² ≤ Σd_i² ≤ |Δ|/(2a). This was also checked on 3,000 exact samples. **Grade: NONE.**

## ST.11 Theorem S4

**Proof.** At δ = δ_thm the third term gives r_a^k ≤ μ^k·2^{2−k}·2^{k−1}/(2μ)^k = 2^{−k}, i.e. r_a ≤ 1/2. Moreover
μ·min(ĝ_a,1)/2 = min(g_a, μ)/2 ≥ 1/2 for integers. So Theorem S3 applies, each cluster lies in the open disc of
radius 1/2, and the real parts are strictly within 1/2 of a, so there is no tie.

**Exact check.** All 368 corners of the δ_thm boxes of 36 integer multisets round to m. The multisets cover orders
1, repeats, and ratios up to 1000. The 11 printed δ_thm values are reproduced: my exact value rounded down to
3 s.f. equals the printed value in every row (see the P3 table). **Grade: NONE.**

## ST.12 Proposition S5: validity of the certificate

1. *Step 1* is immediate.
2. *Step 2.* tanh(U+V) − tanh U − sech²U·V = Σ_{k≥2} tanh^{(k)}(U)V^k/k!. Because U(0) = 0 and U has non-negative
   coefficients (P_k > 0), and |[x^j] tanh^{(k)}| ≤ [x^j] tan^{(k)}, this is ≪ Σ_{k≥2} tan^{(k)}(U)|V|^k/k!
   = tan(U+|V|) − tan U − sec²U·|V|. The linear term is bounded coefficientwise by |sech²U| ∗ |δU|.
3. *Steps 3–5.* Put Δ = ẽ − e and r = δb − δM·e. Then Δ = M⁻¹r − M⁻¹δM·Δ, so (I−A)|Δ| ≤ |M⁻¹||r|.
   - If (I−A)v = 𝟙 with v > 0, then Av = v − 𝟙 < v. By Collatz–Wielandt, ρ(A) ≤ max_i (Av)_i/v_i < 1, so
     (I−A)⁻¹ ≥ 0 and |Δ| ≤ E.
   - The same bound gives ρ(M⁻¹δM) ≤ ρ(A) < 1, so M̃ is invertible.
   - The positive-vector test is therefore a valid certificate.
4. *Test (i).* |q̃ − q| ≤ Σ_j E_j|z|^{n−j} ≤ Σ_j E_j(a+r)^{n−j} on |z−a| = r. Also
   |q| ≥ r^{k_a}∏(|a−b|−r)^{k_b} when r < |a−b|, which holds for integer orders and r ≤ 1/2. Strict inequality
   gives exactly k_a roots in the open disc. Since Σk_a = n, the real parts all lie in (a−1/2, a+1/2).
5. *Test (ii).* The linear part of r is J·δI, with J = ∂(b − M e)/∂I at fixed e. So M⁻¹J L⁻¹δH = G·δH exactly,
   with G = (D_I e)L⁻¹. The remainder is ϱ = M⁻¹r_rem − M⁻¹δM·Δ, so |ϱ| ≤ |M⁻¹||r_rem| + A·E. On the circle,
   |p_c(z)| ≤ Σ_l|p_c^{(l)}(a)/l!|r^l.

**Exact checks of the implementation.**

- G agrees with exact difference quotients (O(h) convergence).
- E bounds the true |ẽ−e|, and ϱ bounds the true remainder, on 180 exact samples.

**Defects (all MINOR).**

- (a) "G = (D_I e)L⁻¹ is exact (Lemma S2.1)": the relevant input is Theorem B plus implicit differentiation,
  G = M⁻¹J L⁻¹. Lemma S2.1 only gives invertibility.
- (b) The radius set for test (ii) is not stated. I used the same list as test (i), and that reproduces every
  printed value.
- (c) The proposition needs integer orders, or r < min gap, for the product lower bound and for disjointness.
  State it.
- (d) "valid because U ≥ 0" should say "U has non-negative Taylor coefficients and U(0) = 0".

## ST.13 δ_up and rounding conventions

The ST.13 adversarial claims hold exactly: the test **fails** at 2.342e−3 for (2,8,8) and at 1.462e−3 for
(4,5,21,28), and it certifies at the printed values 2.341e−3 and 1.461e−3.

δ_up results are in the P3 table. In each row I built a real polynomial q̃ = (z − c)g(z), with c = a ± 1/2 and
rational coefficients, whose exact data are within (1+10⁻³)δ_up of H(m). Exact recovery returns q̃ itself, so the
outcome is a tie: Routh–Hurwitz finds a root on Re z = c. Shifting c by |τ| ≤ 10⁻⁶ (in one of the two directions) gives data, still
within tolerance, that round to the wrong multiset.

**Finding.** For (2,2,2,2,3) the printed δ_up = 5.743e−05 is not the infimum over its own shape family. I found
an exact tie at ‖ΔH‖_∞ = 5.3113e−05, 7.5% lower, with the root at 2+1/2 as printed. The smallest failing corner
of the box is also ≈ 5.3113e−05. So δ_up/δ_cert is ≤ 6.72, not 7.26.

All other rows agree with the printed δ_up to within 0.06%. The printed δ_up remains a valid upper bound.
**Grade: MINOR. Fix:** reprint δ_up = 5.312e−05 (rounded up) and ratio 6.72 for (2,2,2,2,3), or state that δ_up
is only an upper bound from a local search.

## ST.14 Results table

All checks are in `check_s5.txt`.

- **δ_thm:** every printed value equals the exact value rounded down to 3 s.f. The three rows whose exact value
  would round to nearest *up* are printed correctly rounded down: (3,3,12) 1.189e−7 → 1.18e−7,
  (4,5,21,28) 3.147e−11 → 3.14e−11, (2,2,2,2,3) 2.730e−12 → 2.72e−12.
- **δ_cert:** every printed value certifies exactly, with the same δ on every coefficient. Test (ii) succeeds;
  test (i) alone fails at the printed value in every row. My largest certified value at 4 s.f. equals the printed
  value in all 11 rows, and the next 4-s.f. value fails in all 11 rows.
- **Relative columns δ_cert/|H_ν|:** consistent with rounding down to 2 s.f. Several differ from round-to-nearest,
  e.g. 1.6e−3 vs 1.7e−3 for (2,8,8), ν = 0. The header should say "rounded down".
- **ε_cert:** every printed value certifies with ρ_ν = ε|H_ν|, and my 2-s.f. maximum equals the printed value in
  all rows.
- **Soundness probe** (`check_probe.txt`): for each row, all 2ⁿ corners plus 2,000 uniform exact rational points of
  the printed δ_cert box went through the full recovery map. That is 22,184 vectors with 0 failures. The real
  parts were isolated exactly by Routh–Hurwitz counts on the lines Re z = a ± 1/2. The probe can detect failures:
  at the (1+10⁻³)δ_up box, 1–3 corners per row fail.

**Grade: NONE**, apart from the δ_up entry for (2,2,2,2,3) (ST.13) and the "rounded down" note for the relative
columns.

---

## P3 verdict

The Proposition S5 certificate is mathematically valid. My independent implementation reproduces **every**
printed δ_cert exactly, as the maximal 4-s.f. certified value. The printed δ_thm and ε_cert also reproduce.
Every δ_up is a genuine upper bound: a tie was built within (1+10⁻³)δ_up in every row. One δ_up, for (2,2,2,2,3),
is not tight.

| m | printed δ_thm | my δ_thm (exact, 6 s.f.) | printed δ_cert | certified at printed value? | my max certified (4 s.f., down) | printed δ_up | failure constructed? (‖ΔH‖_∞ exact, location) |
|---|---|---|---|---|---|---|---|
| (2,8,8) | 3.80e-07 | 3.80281e-07 | 2.341e-03 | yes (ii) | 2.341e-03 | 2.485e-03 | yes: tie 2.48486e-03 at 8−1/2; wrong rounding at 2.48494e-03 |
| (3,3,12) | 1.18e-07 | 1.18928e-07 | 4.040e-03 | yes (ii) | 4.040e-03 | 4.589e-03 | yes: tie 4.58827e-03 at 3+1/2; wrong at 4.58835e-03 |
| (3,10,15,30) | 4.02e-11 | 4.02102e-11 | 3.660e-03 | yes (ii) | 3.660e-03 | 7.488e-03 | yes: tie 7.48652e-03 at 10+1/2; wrong at 7.48898e-03 |
| (4,5,21,28) | 3.14e-11 | 3.14738e-11 | 1.461e-03 | yes (ii) | 1.461e-03 | 2.018e-03 | yes: tie 2.01767e-03 at 4.5 (= 5−1/2); wrong at 2.01857e-03 |
| (2,3,7) | 4.49e-07 | 4.49202e-07 | 3.658e-03 | yes (ii) | 3.658e-03 | 6.587e-03 | yes: tie 6.58691e-03 at 2.5 (= 3−1/2); wrong at 6.58698e-03 |
| (4,4,4) | 9.35e-07 | 9.35405e-07 | 4.539e-04 | yes (ii) | 4.539e-04 | 5.036e-04 | yes: tie 5.03583e-04 at 4+1/2; wrong at 5.03779e-04 |
| (7,7,7) | 9.97e-08 | 9.97349e-08 | 8.068e-05 | yes (ii) | 8.068e-05 | 8.273e-05 | yes: tie 8.27212e-05 at 7−1/2; wrong at 8.27592e-05 |
| (3,3,4,4) | 1.48e-09 | 1.48692e-09 | 9.597e-05 | yes (ii) | 9.597e-05 | 1.195e-04 | yes: tie 1.19436e-04 at 4−1/2; wrong at 1.19471e-04 |
| (5,5,5,5) | 4.74e-10 | 4.74370e-10 | 3.617e-05 | yes (ii) | 3.617e-05 | 3.826e-05 | yes: tie 3.82580e-05 at 5−1/2; wrong at 3.82776e-05 |
| (2,2,2,3) | 2.03e-09 | 2.03106e-09 | 1.858e-04 | yes (ii) | 1.858e-04 | 2.520e-04 | yes: tie 2.51972e-04 at 2.5 (= 3−1/2); wrong at 2.52051e-04 |
| (2,2,2,2,3) | 2.72e-12 | 2.72978e-12 | 7.908e-06 | yes (ii) | 7.908e-06 | 5.743e-05 | yes, **below printed**: tie 5.31132e-05 at 2+1/2; wrong at 5.32225e-05 |

"yes (ii)" means the coherent test (ii) succeeds. Test (i) alone does not certify the printed value in any row.
The radii used were r = 1/2 for every order, except order 5 in (4,5,21,28) (19/40), 3 in (2,3,7) (17/40), 3 in
(3,3,4,4) (19/40), 3 in (2,2,2,3) (19/40) and 3 in (2,2,2,2,3) (17/40).
