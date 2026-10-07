# Theorem E in practice

Script: `practice.py` (reads `numerics/data/` and `numerics/moduli/data/` and writes nothing there).
Per-time data: `data/practice.csv`, one row per (orbifold, M, t).

## The question

Theorem E (`theorem_e.tex`) says that the first N eigenvalues, each known to accuracy δ, determine
the signature in the class C(A, ε, M). The decision rule is: at one time t, pick the signature σ
whose signature part of the heat trace, G_σ(t) = I(t) + Σ E_{m_i}(t), is nearest to
Z̃_N(t) = Σ_{j<N} e^{−λ_j t}. Here we apply the same rule to the committed spectra and ask how many
eigenvalues it actually needs.

**Competitors.** All signatures with the same area as the true one and cone orders ≤ M:

- Area π/2: (2,8,8), (3,3,12), (2,6,12), (3,4,6), (4,4,4), (2,2,2,4) for M = 12, plus (2,5,20) for M = 30.
- Area 4π/3, M = 3: (0;3,3,3,3), (0;2,2,2,2,3), (1;3).
- Area 4π/3, M = 12: 10 signatures.

All genus 0 unless shown.

**Gap.** gap(t) = min over σ ≠ σ₀ of |G_σ(t) − G_σ₀(t)|, computed by 30-digit quadrature of the
trace-formula integrals.

**Two counts at each t:**

- **N_obs(t)** is the least N such that |Z̃_{N'}(t) − G_σ₀(t)| < gap(t)/2 for every N' from N up to
  the end of the complete range. This is the margin Theorem E's proof needs. At N_obs the
  rule returns σ₀; the script asserts this. The count is judged against the data, so it uses the
  true hyperbolic term implicitly.
- **N_apr(t)** is the least N with HypB(t) + TailB(N,t) + PertB(N,t) < gap(t)/2. This is Theorem E's
  own a-priori criterion, with the actual constants of the orbifold:
  - **HypB** is Lemma 2.5 with the true systole and a committed diameter upper bound: 2 × the
    longest side for the triangles, `diam_O_upper_bound` for the family. Past its range, Proposition C2.
  - **TailB** is Theorem C's tail bound, min over s of e^{−λ_N (t−s)} (A/4πs + Σ b₀ + HypB(s)).
  - **PertB** is Σ_{j<N} t·err_j, with the committed a-posteriori eigenvalue error estimates.

  N_apr is rigorous modulo those error bars and the completeness of the computed spectrum below λ_N.
- **N_theory** is Theorem E's N for C(Area, systole, M).

**Complete ranges:**

- Triangles: λ ≤ 16000 (manuscript §7: no eigenvalue below about 1.6×10⁴ is missing), about 2000
  eigenvalues.
- (0;3,3,3,3) family: the 120 committed eigenvalues of each of the 8 symmetry sectors, merged.
  The union is complete below the least sector maximum, giving 815–856 eigenvalues up to λ ≈ 2440–2560.
  The merge reproduces the committed first-400 orbifold lists, which the script asserts.

## Results (best over the t-grid 0.002–1)

| orbifold | systole | M | competitors | N_obs (t) | N_apr (t) | N_theory | δ_theory |
|---|---|---|---|---|---|---|---|
| O(2,8,8) | 2.2568 | 12 | 6 | 3 (0.3) | 21 (0.05) | 6.8×10⁹ | 4.2×10⁻²⁵ |
| O(2,8,8) | 2.2568 | 30 | 7 | 3 (0.3) | 21 (0.05) | 1.6×10¹⁶ | 1.6×10⁻⁴⁵ |
| O(3,3,12) | 1.8626 | 12 | 6 | 4 (0.2) | 39 (0.03) | 6.8×10⁹ | 4.2×10⁻²⁵ |
| O(3,3,12) | 1.8626 | 30 | 7 | 4 (0.2) | 39 (0.03) | 1.6×10¹⁶ | 1.6×10⁻⁴⁵ |
| (0;3,3,3,3), ϑ=0.0 | 2.634 | 3 | 3 | 3 (0.5) | 33 (0.075) | 2.0×10⁷ | 3.4×10⁻²⁴ |
| ϑ=0.4 | 2.203 | 3 | 3 | 4 (0.3) | 52 (0.05) | 2.0×10⁷ | 3.4×10⁻²⁴ |
| ϑ=0.8 | 1.831 | 3 | 3 | 4 (0.3) | 90 (0.03) | 2.0×10⁷ | 3.4×10⁻²⁴ |
| ϑ=1.2 | 1.516 | 3 | 3 | 5 (0.2) | 145 (0.02) | 2.0×10⁷ | 3.4×10⁻²⁴ |
| ϑ=1.6 | 1.250 | 3 | 3 | 13 (0.1) | 201 (0.015) | 2.0×10⁷ | 3.4×10⁻²⁴ |
| ϑ=2.0 | 1.029 | 3 | 3 | 17 (0.075) | 321 (0.01) | 2.0×10⁷ | 3.4×10⁻²⁴ |
| ϑ=2.4 | 0.846 | 3 | 3 | 27 (0.05) | 694 (0.005) | 2.0×10⁷ | 3.4×10⁻²⁴ |
| ϑ=2.8 | 0.694 | 3 | 3 | 50 (0.03) | — | 2.0×10⁷ | 3.4×10⁻²⁴ |
| (0;3,3,3,3), ϑ=0.0 | 2.634 | 12 | 10 | 5 (0.3) | 38 (0.075) | 7.4×10¹² | 4.1×10⁻⁴¹ |
| ϑ=0.4 | 2.203 | 12 | 10 | 5 (0.3) | 58 (0.05) | 7.4×10¹² | 4.1×10⁻⁴¹ |
| ϑ=0.8 | 1.831 | 12 | 10 | 7 (0.2) | 103 (0.03) | 7.4×10¹² | 4.1×10⁻⁴¹ |
| ϑ=1.2 | 1.516 | 12 | 10 | 9 (0.15) | 159 (0.02) | 7.4×10¹² | 4.1×10⁻⁴¹ |
| ϑ=1.6 | 1.250 | 12 | 10 | 15 (0.1) | 222 (0.015) | 7.4×10¹² | 4.1×10⁻⁴¹ |
| ϑ=2.0 | 1.029 | 12 | 10 | 33 (0.05) | 353 (0.01) | 7.4×10¹² | 4.1×10⁻⁴¹ |
| ϑ=2.4 | 0.846 | 12 | 10 | 61 (0.03) | 749 (0.005) | 7.4×10¹² | 4.1×10⁻⁴¹ |
| ϑ=2.8 | 0.694 | 12 | 10 | 98 (0.02) | — | 7.4×10¹² | 4.1×10⁻⁴¹ |

The theoretical constants use the systole of each member. They do not change across the family
because t_* = t_1 there, so the systole does not bind.

For ϑ = 2.8 the a-priori criterion needs t ≤ 0.003, since its Hyp bound carries e^{3·7.77}. At
that t it needs more eigenvalues than the 815 committed ones. This is a limit of the data, not of
the method.

## Reading

1. **Rule versus theorem: about 10⁸–10¹² fewer eigenvalues.** For the pair of the paper, the rule
   picks O(2,8,8) from 3 eigenvalues and O(3,3,12) from 4. The a-priori criterion certifies the
   choice, modulo the numerical error bars, from 21 and 39 eigenvalues. Theorem E's worst-case N
   for their class is 6.8×10⁹. In the (0;3,3,3,3) family the counts are 3–98 (observed) and 33–749
   (a priori), against 2×10⁷ (M = 3) or 7×10¹² (M = 12).
2. **Where the theorem loses.** Theorem E needs one t at which every pair in the class is
   separated by more than the worst-case remainder. Its gap is the smallest possible first
   difference a_{k−2}, against the largest possible next term n_* Q_cone(M, K). In practice:
   - in the classes checked by theorem_e.py (Lemma E2), the true gaps are 10¹³–10⁴² times larger than Γ;
   - the decision can be made at t = 0.03–0.5, where the asymptotic expansion is useless but the
     exact G_σ(t) is computable;
   - Lemma 2.5 with the actual diameter, not D(A, ε, M), is enough.
3. **What controls the practical count.** The hyperbolic term, through the systole. As the systole
   falls from 2.63 to 0.69, the a-priori count rises from 33 to more than 815, and the observed
   count from 3 to 50. The usable t shrinks roughly like ℓ², and the count grows like 1/t (Weyl).
   This is the behaviour of Theorem E's t_3. In these examples it is masked by t_1 in the
   worst-case constants.
4. **The nearest competitor.**
   - For O(2,8,8) and O(3,3,12) it is always the other one at t ≤ 0.3. At t ≥ 0.5, (2,6,12) is
     nearest to (2,8,8).
   - In the family it is (0;2,2,2,2,3) for M = 3, which differs already at c₂ (d₂ = 1/6), and
     (0;2,3,4,4) for M = 12.
   - The gap of the paper's pair at t = 0.002 is 0.00389 ≈ d₃t = (25/12)t. This is the first
     difference at the third heat invariant, the mechanism of Lemma E1.
