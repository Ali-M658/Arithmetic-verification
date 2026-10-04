# Referee report, gate G5: curvature (CU.*) and divergence (DV.*)

Scope: the statements in `review/audit/statements/curvature-divergence.md` only, re-derived from
the fetched sources in `review/audit/sources/` (plus two papers fetched for DV.5, see `fetches.md`).
I have not read the manuscript's proofs.

Scripts (run from the repo root, each exits nonzero on any failed `assert`):

| script | output | content |
|---|---|---|
| `check_lemma1.py` | `check_lemma1.txt` | DV.1 (a),(b) exact; G_2 closed form; DV.2 leading coefficient; s_nu > 0 and an independent derivation of s_nu |
| `check_curvature.py` | `check_curvature.txt` | CU.2 against Molien; full spectral expansion of S^2/G against Uçar at every order to t^24; classification lists; a_0 injectivity; flat class; Part 4; Part 3 witnesses |
| `check_divergence.py` | `check_divergence.txt` | DV.1(c) rates, DV.2, DV.3 limits and the two stated stress tests, DV.4 peeling from a tail (exact subtraction), DV.5 radius |

`heatlib.py` implements Uçar (4.25), (4.33), (4.35) in exact rationals (Bernoulli numbers from sympy).
mpmath appears only in blocks labelled "asymptotic sanity".

## Summary

| id | grade | one-line reason | in paper? |
|---|---|---|---|
| CU.0 | NONE | Conventions correct; Thurston 13.3.6 quoted correctly | yes |
| CU.1 | MINOR | Conclusion correct, but the deficiency-space sentence misreads Kokotov p. 9, and DGGW Thm 4.8 does not by itself give vanishing or the exponential remainder | yes, with the reworded justification |
| CU.2 | MINOR | Correct (agrees with Molien's formula for every finite subgroup of SO(3)); classical, not new | as a remark or one-line lemma, with no claim that it is new |
| CU.3 (1) | MINOR | Correct. The flat class is complete and the c_0 values are right; this is DGGW Thm 5.15 | yes, presented as DGGW's result |
| CU.3 (2) | MINOR | Correct, and I prove a_0 injective below. It is DGGW Thm 5.15 / Prop 5.22 and Uçar Cor 4.21(iv). "for every n" should read n >= 2 | as a cited remark, not a new proposition |
| CU.3 (3) | NONE | Witnesses verified exactly; rests on Theorem A and C(2) | yes |
| CU.3 (4) | MINOR | Correct. "have the same area" should say "after rescaling"; the Friedrichs extension must be named | optional remark (not load-bearing) |
| CU.3 strength | NONE | The priority statement is accurate and appropriately modest | yes |
| DV.0 | NONE | Notation and Stirling form correct | yes |
| DV.1 | NONE | (a), (b), (c) all proved; the rates are sharp (k >= 3: Θ(4^-l); k = 2: exactly -3·9^-(l+1) at leading order) | yes |
| DV.2 | MINOR | Correct, including the constant and σ_m ∈ (1, π/2]. The second form is a consequence of the first, not equivalent to it | yes |
| DV.3 | MINOR | Correct, including n = 0 and multiplicities. The 1000×49+50 test reproduces. In the genus-10⁴ test the smooth part dominates up to l = 8, not l = 5. The O(1/l) remark applies to the first limit only | yes |
| DV.4 | MINOR | Valid: limits see only tails. K is in fact recoverable from the tail, so the hypothesis "and K" can be dropped. The "strengthening" is modest | yes, as a corollary/remark |
| DV.5 | MINOR | Radius, Pringsheim and sign are right for n >= 1. It needs "n >= 1" (for n = 0 with K = -1 every a_l/K^l < 0, and the radius is π²). Both citations check out | as a remark (not load-bearing) |

No FATAL or SERIOUS findings.

Items that should not appear in the paper as new results:

- **CU.3 Parts 1–2.** These are DGGW Theorem 5.15 (restricted to good orbifolds), DGGW Proposition 5.22 and Uçar Cor. 4.21(iv). The strength paragraph already says this. The paper should present them as a cited table entry or remark, not as a numbered proposition with its own proof. The only new ingredient is the exponential remainder in the flat case, and that is Kokotov's Theorem 1.
- **CU.2 (Lemma 2).** This is Frobenius/Molien reciprocity for SO(3) characters. It is not load-bearing for any claim here, because the spherical expansion is already Uçar (4.33)–(4.35). It is useful as an independent check (I used it as one), so keep it at most as a remark or an appendix check.
- **CU.3 Part 4** and **DV.5** are not load-bearing. They are fine as remarks.

---

## CU.0 Conventions — NONE

- **χ formula.** Thurston 13.3.4 (sources/thurston_ch13.txt l. 503), with no corner reflectors.
- **Existence of a metric.** Thurston Theorem 13.3.6 (l. 526) says: a closed 2-orbifold has an elliptic, parabolic or hyperbolic structure iff it is good. The structure is hyperbolic iff χ < 0 and parabolic iff χ = 0. So "constant curvature of sign sgn χ exists iff good" is an exact restatement.
- **Area.** If O is elliptic or hyperbolic, area = 2π|χ| (13.3.5, l. 520). This matches "area fixed by χ when K = ±1".
- **Scale invariance.** Under g → c²g, the eigenvalues scale as λ → λ/c². Hence Z(t) → Z(t/c²), so the t^0 coefficient is unchanged. By DGGW (5.7) it equals χ/6 + Σ(m²−1)/(12m), which is topological. So Parts 1, 2 and 4 are indeed independent of normalisation.

## CU.1 Flat-cone input — MINOR

**Independent proof.**

1. **Kokotov's statements.** Kokotov Prop. 1 (sources/kokotov_0906.0717.txt l. 278, eq. (7)) gives
   ∫_{C_β(R)} H_β = Area/(4πt) + (1/12)(2π/β − β/2π) + O(e^{−ε/t}). Thm 1 (l. 478, eq. (13)) globalises this for the Friedrichs extension on a compact polyhedral surface.
   - I re-derived the residue in his (10) exactly: Res_{γ=0} cot(πγ/β)/sin²(γ/2) = (2/3)(β/2π − 2π/β). This gives the constant (1/12)(2π/β − β/2π), which equals (m²−1)/(12m) at β = 2π/m (`check_curvature.py`).
   - It agrees with DGGW Prop. 5.5 / (5.7) and with the classical sum Σ_{j<m} 1/(4 sin²(jπ/m)) = (m²−1)/12 (high-precision sanity check only).
2. **The orbifold Laplacian is Kokotov's Friedrichs extension.** Kokotov p. 8–9 says the deficiency space M is spanned by χV^k_± with 0 ≤ k < β/2π.
   - For β = 2π/m ≤ π, only k = 0 occurs. So M = span{χ·1, χ·log r} and d = 1.
   - Every self-adjoint extension of Δ_min is Δ_N with N a line in M.
   - The orbifold Laplacian is self-adjoint, extends Δ on C_c^∞(X∖P), and its domain contains the smooth orbifold function χ (a cutoff that is constant near P). Hence N = span{χ}, which is exactly Kokotov's Friedrichs choice ("N spanned by χV^k_+", p. 9).
   - Equivalently, points have zero capacity in dimension 2, so the form domain of both operators is the orbifold H¹.
3. **Vanishing at K = 0.** That every t^l coefficient with l ≥ 1 vanishes follows from (F). Independently, it follows from Uçar Thm 4.20, which is stated for every κ ∈ ℝ and gives cone contributions Σ_ν(...)κ^ν t^ν and smooth contributions ∝ κ^ν.
4. **Positivity for K ≠ 0.** Positivity of β_l is DV.1(b), proved below.

**Problems.**

- *"for β ≤ 2π only the bounded mode enters his deficiency space (p. 9)."* This is inaccurate. Both k = 0 modes, 1 and log r, are in M. The Friedrichs extension is the choice that keeps the bounded one. The conclusion stands.
- *"The same follows from DGGW Thm 4.8, whose coefficients are integrals of curvature polynomials."* DGGW Thm 4.8 (dggw l. 1034) asserts only the form of the expansion, with remainder O(t^N). The curvature-polynomial structure is Donnelly's theorem (an accepted standing gap), quoted in Uçar's proof of Thm 4.20. DGGW never gives the O(e^{−ε/t}) remainder.

**Fix.** Replace the sentence with: "Kokotov's deficiency space at a vertex of angle β ≤ 2π is span{χ, χ log r} (k = 0 only). The orbifold Laplacian's domain contains χ, so it is the extension N = span{χ}, which is Kokotov's Friedrichs extension." Cite Uçar Thm 4.20 (κ = 0) for the vanishing of the l ≥ 1 coefficients, and say the exponential remainder is Kokotov's.

## CU.2 Lemma 2 — MINOR (correct, classical)

**Independent proof.**

- Let χ_l be the character of the degree-l harmonics. Then χ_l(rotation by θ) = Σ_{k=−l}^{l} e^{ikθ}, and N_l = |G|^{-1} Σ_g χ_l(g).
- Each non-identity g fixes exactly two poles. The poles fall into G-orbits, one per cone point i, each of size |G|/m_i, with stabiliser C_{m_i}. Counting pairs (g, pole) therefore gives
  Σ_{g≠1} χ_l(g) = ½ Σ_i (|G|/m_i) Σ_{j=1}^{m_i−1} χ_l(2πj/m_i).
- Finally, (1/m) Σ_{j=0}^{m−1} χ_l(2πj/m) = #{|k| ≤ l : m | k} = 2⌊l/m⌋ + 1. Removing the j = 0 term gives the bracket in the lemma.

**Checks.**

- The formula equals Molien's count, computed with exact cosines, for C_2..C_8, D_2..D_8, T, O and I and for l ≤ 40.
- The spectrum it defines reproduces Uçar's expansion exactly at every order. I computed the full small-t expansion of Σ N_l e^{−l(l+1)t} via Hurwitz-zeta values: P_m has mean 0, and ζ(−n, a) = −B_{n+1}(a)/(n+1). It equals (χ/2)s_{l+1} + Σ_i β_l(m_i) for every l ≤ 24 and every m = 2..13.
- This is an independent confirmation of Uçar (4.25)/(4.33)/(4.35) at K = +1, including m = 2, where the rotation by π is its own inverse ("l = 1 = m−1").

**Fix.** State the lemma as a standard consequence of Frobenius reciprocity/Molien. Do not list it under "what is added here"; keep it as a cross-check.

## CU.3 Proposition (curvature comparison)

### Part 1 (K = 0) — MINOR

**Classification.** Closed orientable 2-orbifolds with χ = 0:
- genus 1 with no cones gives T²;
- genus 0 needs Σ(1 − 1/m_i) = 2. Since each term is ≥ 1/2, n ≤ 4. n = 4 forces (2,2,2,2). n = 3 gives 1/a + 1/b + 1/c = 1, i.e. (3,3,3), (2,4,4), (2,3,6). n ≤ 2 gives Σ < 2.

This matches Thurston's parabolic list for X_O = S², T² (thurston l. 545–548). Enumeration confirms it (orders < 200).

**Heat expansion.** Each is a flat polyhedral surface with β_i = 2π/m_i. By CU.1 its expansion is A/(4πt) + Σ(m_i² − 1)/(12m_i) + O(e^{−ε/t}), giving c_0 = 0, 1/2, 2/3, 3/4, 5/6 (exact). These are distinct, so the t^0 coefficient determines the orbifold. The t^{−1} coefficient is A/4π, with A free on every member, so one coefficient never suffices. Hence K_mult = 2.

**Issue.** None mathematically. This is DGGW Thm 5.15 restricted to K = 0 (c = 0, 6, 8, 9, 10 in DGGW's normalisation c = 12·a_0).

### Part 2 (K = +1) — MINOR

**Classification.** The list matches Thurston's elliptic list for X_O = S², and its bad list S²(n), S²(n_1, n_2) with n_1 < n_2 (thurston l. 536–541). The exclusion is justified exactly as stated: by 13.3.6, bad orbifolds carry no constant-curvature metric.

**a_0 is injective (proof).**
- a_0(S²(n,n)) = (n² + 1)/(6n) and a_0(S²(2,2,n)) = (n² + 1)/(12n) + 1/4. Both are strictly increasing in n ≥ 1, and n = 1 gives S² and S²(2,2) respectively.
- **Cross-family collision.** Suppose (n² + 1)/(6n) = (p² + 1)/(12p) + 1/4. This is equivalent to p(2n² − 3n + 2) = n(p² + 1).
  - Since gcd(p, p² + 1) = 1, p | n.
  - Reducing mod n, n | 2p.
  - So n = p or n = 2p. n = p gives p² − 3p + 1 = 0, which has no integer root. n = 2p gives 6p(p − 1) = 0, so p = 1 and the orbifold is S²(2,2) itself.
- **Platonic cases.** The three platonic values are 43/72, 97/144 and a_0(2,3,5). Each is < 1, and DGGW Table 1 lists the first two. None lies on either family: n ≤ 12 is checked exactly, and for n > 12 both families exceed 1.
- Exact verification for n < 3000 is in `check_curvature.py`.

**Sharpness.** χ(S²(2,2,n)) = χ(S²(2n,2n)) = 1/n is correct (exact). At n = 1 the two orbifolds coincide, so "for every n" should read "for every n ≥ 2".

**Higher coefficients.** "The higher coefficients are nonzero" holds: with K = 1, every t^l coefficient is (χ/2)s_{l+1} + Σβ_l > 0, by DV.1(b) and s_ν > 0.

**Issues.**
- (i) "for every n" should be n ≥ 2.
- (ii) Prior art. Part 2 is the orientable case of DGGW Prop 5.22 and of Thm 5.15, and it is Uçar Cor 4.21(iv). It should not be framed as a proposition of this paper.

### Part 3 (K = −1, genus 0) — NONE

- {2,8,8} and {3,3,12} agree at t^{−1} and t^0 and differ at t^1. So K_mult ≥ 3 for n = 3.
- {3,10,15,30} and {4,5,21,28} agree at t^{−1}, t^0 and t^1 and differ at t^2. So K_mult ≥ 4 for n = 4.
- Both are exact, using Uçar (4.25)/(4.33)/(4.35) with K = −1. Together with Theorem A (black box), equality holds.
- The C(2) and "open for n ≥ 5" statements are restatements of other groups' results. Not audited here.

### Part 4 (flat cone surfaces) — MINOR

**Proof.** By Kokotov Thm 1, the only heat invariants of a closed flat cone surface (Friedrichs extension) are the area and (1/12)Σ(2π/β_k − β_k/2π).
- A flat sphere with three cone points has Σβ_i = 2π (Gauss–Bonnet), so it is a doubled triangle with angles πα_i, where Σα_i = 1. Its invariants are the area and (1/12)(Σ1/α_i − 1).
- On the open simplex, f = Σ1/α_i is strictly convex. Its unique minimum is 9, attained at the equilateral triangle, and f → ∞ at the boundary.
- So for c > 9 the level set {f = c} is a closed curve. Modulo S_3 it is still a 1-parameter family of distinct angle multisets. Cone-angle multisets are isometry invariants, so these surfaces are pairwise non-isometric.
- After rescaling to a common area, they share every heat coefficient.

**Example.** (1/4, 1/4, 1/2) and (1/5, 2/5, 2/5) both have f = 10 and t^0 coefficient 3/4 (exact). The level set f = 10 projects onto α_1 ∈ [1/5, 1/2], and these two triangles are its endpoints.

**Issues.**
- (i) "have the same area" should read "rescaled to the same area": they are shapes.
- (ii) Name the self-adjoint extension (Friedrichs). For non-orbifold cone angles in (0, 2π) other extensions exist and change the heat expansion. Kokotov stresses this after (14).
- (iii) Not load-bearing. The Euclidean-polygon analogue is Uçar Cor 3.41: at zero curvature the heat invariants give only Σ1/γ_i. That should be cited next to it.

### Strength paragraph — NONE

It is accurate. DGGW Thm 5.15 (dggw l. 2253) is indeed strictly stronger: it covers bad orbifolds and separates the class from smooth closed surfaces. Prop 5.22 covers non-orientable spherical orbifolds.

---

## DV.0 Notation — NONE

(2l)!/l! = l!·binom(2l, l) = l!·4^l(πl)^{−1/2}(1 + O(1/l)). Substituting gives
A_l(m) = l!(m²/π²)^l / (2π sin(π/m)√(πl)) · (1 + O(1/l)), as stated.

β_l is exactly Uçar's (4.33) coefficient divided by κ^l. The smooth coefficient of t^l is (vol/4π)κ^{l+1}s_{l+1}, where s_ν is the factor of vol·κ^ν in (4.35). With vol = 2π|χ| this is C K^{l+1} s_{l+1}, C = |χ|/2.

## DV.1 Lemma 1 — NONE

**(a)** By (3.69) at x = 1/2, (t/2)/sinh(t/2) = t e^{t/2}/(e^t − 1) = Σ B_{2i}(1/2) t^{2i}/(2i)!. Also y coth y = Σ B_{2j}(2y)^{2j}/(2j)!. Hence the bracket equals Σ_j B_{2j}(k^{2j} − 1)t^{2j}/(2j)!, and
g_{2l+2}(k) = Σ_j binom(2l+2, 2j)(k^{2j} − 1)B_{2j}B_{2l+2−2j}(1/2)/(2l+2)!.
Comparing with (4.25) gives (a). This is checked exactly against an independent sympy Taylor expansion of G_k (k = 2..6, l ≤ 9) and against the Bernoulli form for l ≤ 56.

**(b)** Put H(x) := −G_k(ix) = (x/2)/sin(x/2) · [(x/2)cot(x/2) − (kx/2)cot(kx/2)]. Then [x^{2l+2}]H = (−1)^l g_{2l+2}.
- (x/2)/sin(x/2) has positive Taylor coefficients, with constant term 1.
- y cot y = 1 − Σ_{j≥1} 2ζ(2j)y^{2j}/π^{2j}, so the bracket is Σ_{j≥1} 2ζ(2j)(k^{2j} − 1)(x/2π)^{2j}, with all coefficients > 0 for every real k > 1.

A product of two such series has every coefficient of x^{2l+2} (l ≥ 0) strictly positive. The prefactor in (a) is positive, so c_l > 0, and β_l, a positive combination of the c's, is > 0. This holds for all l and all real k > 1, not only for integers. It is checked exactly for k = 2..30, 49, 50, 97 and l ≤ 120.

**(c)** H is meromorphic, with poles only at:
- x = 2πn/k (from cot(kx/2)) with k ∤ n, and
- x = 2πn (from 1/sin(x/2)).

At x = 2πn with k | n the two cot residues cancel (both equal 2πn).

The nearest poles are ±x_0 = ±2π/k. Near them the principal part of H is σ_k·x_0/(x_0 − x) at x_0 and σ_k·x_0/(x_0 + x) at −x_0: the residue of (kx/2)cot(kx/2) at x_0 is x_0, and φ(x_0) = (π/k)/sin(π/k) = σ_k. So [x^{2l+2}]H = 2σ_k(k/2π)^{2l+2} + (contribution of the next poles). The rates follow:

- **k ≥ 3.** The next poles are ±4π/k (k ∤ 2), and 4π/k < 2π. Their weight is φ(4π/k) = (2π/k)/sin(2π/k) ≠ 0, so the relative error is exactly [φ(4π/k)/σ_k]·4^{−(l+1)}(1 + o(1)), i.e. Θ(4^{−l}). This is consistent with O((2ρ)^{−2l}) for any ρ < 1, and in fact holds with ρ = 1.
- **k = 2.** H = (x/2)² sec(x/2), equivalently G_2 = (t/2)² sech(t/2) (exact). Its poles are x = ±(2n+1)π, i.e. t = ±(2n+1)πi. The relative error is −3·9^{−(l+1)}(1 + o(1)) = O(9^{−l}), as claimed.

Numerically, the ratio of the observed error to these predictions → 1 (`check_divergence.txt`).

## DV.2 Theorem 2 — MINOR

**Proof.**
- By (a) and (c), c_j = ½A_j(m)(1 + O(4^{−j})), uniformly in j, and c_j > 0.
- Then β_l = 2c_l + ½c_{l−1} + Σ_{i≥2} 2c_{l−i}/(4^i i!).
- A_{l−1}/A_l = 2π²/(m²(2l−1)), so ½c_{l−1}/(2c_l) = π²/(2m²(2l−1))·(1 + O(4^{−l})).
- For the tail: c_j ≤ C'A_j for all j, and A_{l−i}/A_l = Π_{r=l−i+1}^{l} 2π²/(m²(2r−1)). Each factor is ≤ π²/2, and the first two factors give O(l^{−2}). So Σ_{i≥2} = O(l^{−2})·A_l. This proves the expansion with the constant π²/(2m²(2l−1)).
- Numerically, l²·(remainder) is bounded and tends to π⁴/(32m⁴), the i = 2 term A_{l−2}/(32A_l). For m = 2 it is 0.1938 at l = 120, against the limit 0.1903.

**Leading coefficient.** p_l = mβ_l is an even polynomial in m of degree 2l+2. Its leading coefficient comes from j = l+1, i = 0: 2·(−1)^l B_{2l+2}/(4(l+1)!(2l+1)) = λ_l, since sgn B_{2l+2} = (−1)^l. This is exact for l ≤ 15.

**Limit.** Using |B_{2n}| = 2(2n)!ζ(2n)/(2π)^{2n}, one gets mA_l/(λ_l m^{2l+2}) = σ_m/ζ(2l+2) → σ_m. Moreover x/sin x is increasing on (0, π/2], > 1 for x > 0, and equals π/2 at x = π/2. So σ_m ∈ (1, π/2], with the maximum at m = 2.

**Issues.**
- (i) "Equivalently": the second display follows from the first but does not imply it (it loses the 1/l term). Write "In particular".
- (ii) "the full polynomial exceeds its leading term by the factor σ_m" holds only asymptotically (ζ(2l+2) → 1). Add "asymptotically, as l → ∞".

## DV.3 Theorem 3 — MINOR

**Proof.**
- **The form of a_l.** By Uçar Thm 4.20/(4.35) and area = 2π|χ|, a_l/K^l = CK s_{l+1} + Σ_i β_l(m_i), with C = |χ|/2. Two checks:
  - s_ν is positive and, from the S² spectrum via Euler–Maclaurin at the half-integers, satisfies s_ν = 2ν!/(√(πν) π^{2ν})(1 + O(1/ν)). Exact identity for ν < 150.
  - So C s_{l+1}/A_l(M) = (4 sin(π/M)/π)·C(l+1)M^{−2l}(1 + o(1)), which is the O(Cl M^{−2l}) term.
- **Other cone orders.** For m_i < M, β_l(m_i)/A_l(M) = (m_i/M)^{2l}·sin(π/M)/sin(π/m_i)·(1 + o(1)).
- **The top order.** The μ copies of M give μA_l(M)(1 + O(1/l)) by DV.2.
- **The limits.** A_l/A_{l−1} = M²(2l−1)/(2π²), which gives the three limits. With cones, the first statistic converges at rate O(l^{−2}); for {3,3,12}, l²(e_1 − 144) is bounded.
- **n = 0.** The first statistic is (2l+1)/(2l−1)(1 + O(l^{−2})) → 1, with (e_1 − 1)·l → 1, and the second statistic → 1/π². Both are as claimed.

**Stress tests (both re-run).**

- **1000×49 + one 50 (K = −1, genus 0).** At l = 150, √e_1 = 49.298 and √(π²e_2) = 49.216. Both round to 49, **as stated**. √e_1 first rounds to 50 at l = 172.
- **Genus 10⁴ + one cone of order 2 (K = −1).** This was computed exactly, and independently a second time from the closed form G_2 = (t/2)² sech(t/2) together with Euler–Maclaurin for s. The smooth part dominates, with the opposite sign, for **l = 0, …, 8**; the cone term takes over at l = 9. The statement "for l ≤ 5" is true but understates the range. Read as a threshold, it is wrong. **Fix:** "for l ≤ 8 (the cone dominates from l = 9)".

**Counterexample hunt.** None found. Cases run:
- m = 2 only;
- repeated largest orders (2,2,7,7,7) and five 2's on genus 2;
- S²(2,2,400) and S²(400,400);
- genus 1 + {2};
- genus ≥ 2 with no cones;
- 1000×49 + 50.

In every case with n ≥ 1, a_l/K^l > 0 from some l_0 ≤ 20 on (exact), and the estimators converge to M² and μ. With n = 0, a_l/K^l has the sign of K for every l (exact).

**Issues.**
- (i) The sentence "There the convergence is only O(1/l)" is true of the first statistic only. The second statistic |a_l|/(l|a_{l−1}|) converges at rate O(1/l) in every case, because of (2l−1)/(2l). Say "the first limit converges at rate O(1/l) instead of O(l^{−2})".
- (ii) The non-uniformity paragraph is correct and useful: the limits give no effective bound on l.
- (iii) The genus-10⁴ threshold should be l ≤ 8, not l ≤ 5 (see above).

## DV.4 Corollary 4 (peeling) — MINOR

**Proof.** Everything used is a limit, and limits depend only on tails.
1. From (a_l)_{l≥L}, Theorem 3 gives M (an integer, read from the limit M² ≥ 4) and μ.
2. Subtract μK^l β_l(M) for every l ≥ L. This is exact, since β_l(M) is a known closed form, (4.25)/(4.33). The remainder is again of Theorem 3's form, with one fewer distinct order.
3. Iterate. Termination is decided by the first limit: it is 1 iff n = 0, and ≥ 4 otherwise.
4. When n = 0, the remainder is C s_{l+1} K^{l+1} with s > 0, so C = a_l/(K^{l+1}s_{l+1}) for any l ≥ L. Then χ = 2KC (χ has sign K and C > 0), area = 2π|χ|, and genus = (2 − χ − Σ(1 − 1/m_i))/2.

**Finitely many removed, infinitely many used.** This is legitimate: "determine" here is a statement about infinite tails, and nothing below L enters. It is not effective from finitely many terms; DV.3's non-uniformity shows that no finite window works uniformly.

**Exact demonstration.** Using only the coefficients with l ∈ [L, L+W] (L = 30 or 40), the procedure recovers the multiset, χ and genus. The remainder is checked exactly to be a constant multiple of K^{l+1}s_{l+1}. The cases:
- {2,8,8}, {3,3,12}, {3,10,15,30};
- genus 3 + {2,2,7,7,7};
- genus 2 and genus 1 + {2};
- S²(2,3,5), S²(9,9), S²(2,2,9) and S².

**Improvement.** K need not be assumed (within K ∈ {±1}). For n ≥ 1, sgn a_l = K^l for large l. For n = 0, sgn a_l = K^{l+1} for all l. The first limit tells which case applies.

**Novelty.** The statement is correct, and the comparison with Uçar is fair. Uçar's Thm 3.40 proof (ucar l. 8697 ff.) first uses the volume and curvature (Cor 3.38), then extracts W_ν by induction from ν = 0. But this is a remark-level strengthening (heat-invariant tails versus the full spectrum), and it should be presented as such.

**Fix.** Drop "and K" or note that it is recoverable. Say explicitly that the determination is non-effective.

## DV.5 Borel reading — MINOR

**Proof.**
- **Radius.** By DV.3, |a_l/l!|^{1/l} → M²/π², so the radius is π²/M². Numerically (a_l/l!)^{1/l}·π²/M² → 1 slowly, and a_l/(l a_{l−1})·π²/M² → K.
- **Singularity.** In w = Kζ the coefficients are a_l/(K^l l!), which are > 0 for l ≥ l_0 when n ≥ 1. Removing a polynomial does not move singularities. By Pringsheim, w = π²/M² is singular, i.e. ζ = Kπ²/M²: on the negative axis for K = −1 and the positive axis for K = +1.
- **Citations.** Both check out:
  - Dunne (fetched; eqs. (21)–(25) and the sentence after (21)): the H² diagonal expansion has Borel poles on the negative axis at distance π² (in his Γ(n+1/2)-weighted transform, which has the same radius).
  - Li–Li–Tang Example 2.30: the S² singularities are {k²π²}.

**Issue.** The statement needs "n ≥ 1". For n = 0 the radius is π², not π²/M². With K = −1, every a_l/K^l is < 0 (exact, l ≤ 200), so "All a_l/K^l > 0 for large l" fails. Pringsheim still applies to −B and gives ζ = Kπ². Not load-bearing.

**Fix.** Add "(n ≥ 1; for n = 0 replace M by 1 and apply Pringsheim to −B when K = −1)".
