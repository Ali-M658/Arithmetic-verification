<!-- Round 9 blind check A: returned text saved verbatim; the reviewer could not write files -->

# Blind check A (round 9): report

I could not write REPORT.md: writing the file was refused, so the full report is here.

Materials used: `main/scratch/A-r9fix.pdf` and `A-r9fix-supp.pdf`. For literature I fetched with headless curl: Croot–Mao–Yip (arXiv:2609.05061), Schueth (arXiv:1812.06119, which is [25]) and Dryden–Gordon–Greenwald–Webb (arXiv:0805.3148, which is [2]).

Scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/blind-check-A/scratch/`, with a venv holding mpmath, sympy and numpy:
- `item1.py`, `item1hp.py`: optimal truncation, numerical.
- `item4.py`: least-area enumeration and the five-order case list.
- `item56.py`: Prop. 2.14 integrals, the values of Π_i against Schueth, and ω_n.
- `item7.py`: the numbers of Lemma B.5 and Remark B.6.
- `item8.py`: the constants C, ν and s, and the example pairs.

## Summary

| # | Item | Verdict |
|---|---|---|
| 1 | Prop. B.4 and the paragraph after it | CORRECT |
| 2 | Prop. 5.2: disjointness and the corrected case list | CORRECT |
| 3 | Cor. 5.3, Problem 5 | CORRECT (one trivial step left implicit in the converse of the scaling equivalence) |
| 4 | Thm 5.9: unique pair of least area | CORRECT |
| 5 | Prop. 2.14 and Remark 2.15 | Prop. 2.14 is CORRECT and accurately conditional. INCOMPLETE elsewhere: three places still assert the l ≥ 3 value, or something that depends on it, without the condition. |
| 6 | Prop. 2.17(ii) and (iii) | (iii) is CORRECT. In (ii) the Jacobian, the definition of E and the scaling step are CORRECT, but (ii) is INCOMPLETE as stated: for L ≥ 4 it depends on the unproved parametric form, while the statement is unconditional. |
| 7 | Remark B.6 numbers | CORRECT, all reproduced |
| 8 | Thm 3.11(ii), C = Dq and related claims | CORRECT |
| 9 | Thm 3.15, Thm 1.3(ii), Remark 3.22 | CORRECT |
| 10 | Cor. 6.5 (δ_thm) and the paragraph after it | CORRECT |
| 11 | Supplement: Bolza covering; "Changing the shape" | CORRECT (one minor unstated step, σ² = id) |
| 12 | N(k) paragraph | CORRECT (I did not verify the attribution to [4, Props 2–3]; the bound itself is) |

---

## 1. Proposition B.4 (Optimal truncation of the cone series): CORRECT

I checked the proof step by step.

**The bound on |b_K|.**
- |b_K(m)| = 4^{-K} Σ_k (2k)!/(k!(K−k)!) φ_k is a sum of positive terms.
- With (2k)! ≤ 4^k (k!)² and φ_k ≤ C A_m x^k, this is at most C A_m Σ_k 4^{k−K} k!/(K−k)! x^k.
- Put j = K−k and use (K−j)! ≤ K!. The sum is at most K! x^K Σ_j (4x)^{-j}/j! = e^{1/(4x)} K! x^K.

**The bound on |b_K| t^K.**
- Put s = xt ≤ 1. Then K = ⌊1/s⌋ ≥ 1, s ≤ 1/K, and |b_K| t^K = |b_K| x^{-K} s^K.
- K! s^K ≤ K! K^{-K} ≤ e√K e^{-K}, by the valid bound n! ≤ e n^{n+1/2} e^{-n}.
- √K ≤ s^{-1/2} = (π/m) t^{-1/2}, and e^{-K} < e^{1−1/s}.
- Together these give e^{2+1/(4x)} C A_m (π/m) t^{-1/2} e^{-π²/(m²t)}, with 1/(4x) = π²/(4m²). This is exactly the stated bound.

**The first inequality (Prop. B.2(a)).**
- Re-derived: ρ_K has sign (−1)^K and modulus at most |g_K| t^K.
- The decomposition E_m − Σ_{l<K} b_l t^l = e^{−t/4}ρ_K + Σ_k g_k t^k [e^{−t/4} − Σ_{i<K−k}(−t/4)^i/i!] is an identity.
- Every term has sign (−1)^K.
- The moduli sum to Σ|g_k| 4^{k−K}/(K−k)! = |b_K|, because all terms of b_K have the same sign.

**Numerical test.**
- E_m(t) was computed by quadrature of the trace-formula integral at 60 digits, rechecked at 130 digits.
- b_l comes from (4)–(5), with (4) checked against direct Taylor coefficients of Φ_m to 1e−62, and p_0, p_1, p_2 agreeing with (8).
- C = sup_k φ_k/(A_m x^k) over k ≤ 300: 1.000 for m=2 (the supremum is the limit), 1.209 for m=3, 1.388 for m=4, 1.578 for m=8, 1.615 for m=12. For m ≥ 3 the supremum is attained at k=0.

| m | t | K | true error | \|b_K\| t^K | bound of B.4 |
|---|---|---|---|---|---|
| 2 | 0.5 | 4 | 1.19e−3 | 2.12e−3 | 3.48e−2 |
| 2 | 0.05 | 49 | 4.24e−23 | 8.44e−23 | 5.67e−21 |
| 2 | 0.01 | 246 | 7.86e−109 | 1.57e−108 | 2.38e−106 |
| 3 | 0.1 | 10 | 2.51e−6 | 4.81e−6 | 1.24e−4 |
| 3 | 0.005 | 219 | 7.30e−97 | 1.46e−96 | 1.79e−94 |
| 4 | 0.01 | 61 | 2.61e−28 | 5.20e−28 | 3.44e−26 |
| 8 | 0.02 | 7 | 1.43e−4 | 2.73e−4 | 6.27e−3 |
| 8 | 0.001 | 154 | 3.13e−68 | 6.25e−68 | 6.65e−66 |
| 12 | 0.05 | 1 | 0.151 | 0.257 | 2.22 |
| 12 | 0.001 | 68 | 7.49e−31 | 1.49e−30 | 1.06e−28 |

- Both inequalities hold in every case. The true error is about half of |b_K| t^K.
- The enveloping property holds for every truncation order up to K+2: the remainder has sign (−1)^K and modulus at most |b_K| t^K.
- At 60 digits two cases (m=3 at t=0.005, m=8 at t=0.001) failed only because the precision was too low. At 130 digits they pass.
- |b_K(m)| is strictly increasing in m for m = 2..15 and K ≤ 30.

**Several cone points.** Take K = ⌊π²/(µ²t)⌋ and t ≤ π²/µ². For every order m ≤ µ, the error is at most |b_K(m)| t^K ≤ |b_K(µ)| t^K (monotonicity in B.2(a)), and B.4 applies at m = µ. So the total is at most n|b_K(µ)| t^K = O(t^{−1/2} e^{−π²/(µ²t)}). Correct. The condition t ≤ π²/µ² is implicit in "for t below the scale (π/µ)²".

## 2. Proposition 5.2 (Rivals of a triangle orbifold): CORRECT

**Areas.** Equal area < 2π, together with area ≥ 2π(2g−2+n'/2), forces 4g+n' < 6. That leaves g=0 with n' ≤ 5, or (1;m). The case n'=3 is excluded by Cor. 5.1.

**(1;m).** d = 0, so m = p+q+r and m³ = p³+q³+r³ < (p+q+r)³, a contradiction.

**Five orders.** d = 2, so U = {1,1,p,q,r} and R(m') = R+2 > 2. I enumerated all 5-multisets with entries below 60 and R > 2. They are exactly {2,2,2,2,x} for every x ≥ 2 and {2,2,2,3,x} for x = 3, 4, 5. By hand, {2,2,3,3,x} and {2,2,2,4,x} would need x < 3 or x < 4 respectively, and larger patterns fail too.

The values of (P1(m')−2)(R(m')−2), computed exactly:
- First family: 1 + 6/x (4, 3, 5/2, ...), all at most 4.
- Second family: 10/6, 11/12 and 12/30 for x = 3, 4, 5, as stated.

All are below 9 ≤ (p+q+r)R (AM–HM). The corrected list and values are right.

**Four orders.** d = 1, so U = {1,p,q,r} and V = m'. Then 4/a ≥ R(m') = 1+R > 1 gives a ∈ {2,3}. (pdftotext garbles this as "a4 > 1"; the rendered page reads 4/a > 1.)

**Disjointness.** |U|+|V| = 8. A common order between {a,b,c,d} and {p,q,r} would give |U*|+|V*| ≤ 6 < 2·3+2. That contradicts Thm 3.7 with L = 3, which applies because the signatures differ and H_3 is equal.
- I re-derived Thm 3.7: for κ ≤ 2L, Lemma 3.1 kills e_j for odd j ≤ κ−3, and e_{κ−1} = e_κ ΣX^{−1} = 0. So Q is even and U* = V* = ∅. Correct.

## 3. Corollary 5.3 and Problem 5: CORRECT

**K_mult ≤ 4.** A rival sharing c1..c4 has, by Prop. 5.2, signature (0;a,b,c,d). Then max(n+g−g', n'+g'−g) = max(3,4) = 4 ≤ L = 4, so Thm 3.7 forces equal signatures. Correct.

**Equivalence with the Diophantine system.**
- Take a solution with p,q,r,a,b,c,d ≥ 2. R(a,b,c,d) = 1+R(p,q,r) < 2, so (0;a,b,c,d) is hyperbolic once R(p,q,r) < 1.
- The paddings U = {1,p,q,r} and V = {a,b,c,d} satisfy (14) with |U| = |V| and g = g' = 0. By the converse in Lemma 3.6 the two orbifolds share H_3, so K_mult ≥ 4.
- Conversely, if there is no solution, Prop. 5.2 gives K_mult ≤ 3.

**Automatic hyperbolicity (Problem 5).** R(p,q,r) ≥ 1 would need Σ1/a ≥ 2, so a=b=c=d=2 and R(p,q,r) = 1. The triads with R = 1 are (2,3,6), (2,4,4) and (3,3,3), with sums 11, 10 and 9, so 1+p+q+r ∈ {10,11,12} ≠ 8. Correct.

**Scaling equivalence.**
- Forward: multiplying by k ≥ 2 makes every entry ≥ 2 and keeps R, P1, P3 equal (homogeneity). The gcd of the eight entries is k, because 1 is an entry, and k lies on one side. Correct.
- Converse: one step is implicit. If the side containing the gcd g contained it twice, dividing gives {1,1,x,y}. Its reciprocal sum exceeds 2 ≥ R(a,b,c,d), so this is impossible; the other side cannot contain g by disjointness (Thm 3.2).
- The remark "covers only solutions with entries at most 220" is right (440/2).

## 4. Theorem 5.9 (minimal degeneracy), uniqueness of least area: CORRECT

**The proof.**
- An area of at most π/2 forces g = 0 and n ≤ 4. With n = 4 it leaves only (0;2,2,2,3), of area π/3, and (0;2,2,2,4), of area π/2. Genus 1 has area ≥ π.
- A triangle sharing c1, c2 with these would need (S, R) = (8, 5/6) or (9, 3/4). Then SR = 20/3 or 27/4, both below 9, so this is impossible.
- Triangle against triangle: a collision needs equal (S, R). One triad has least order ≥ 3, because R is injective on stratum 2. Majorisation by (3,3,S−6) gives R ≤ 2/3 + 1/(S−6) ≤ 3/4, with equality only at S = 18, where Thm 5.7 gives only the minimal pair.

**Independent enumeration.**
- I enumerated every signature in Sig with area ≤ π/2 and orders ≤ 3000: 6032 signatures, of which the only four-point ones are (2,2,2,3) and (2,2,2,4) and none has five points.
- I grouped them by exact (χ, c2). The only pair with different signatures and equal c1, c2 is {(0;2,8,8), (0;3,3,12)}, at area π/2.
- The order bound is harmless: for large orders only the families (2,3,r) and (2,4,r) have area below π/2. Equal S would need r = r'+1 with 1/(r'(r'+1)) = 1/12, so r' = 3, outside the family.

## 5. Proposition 2.14 and Remark 2.15: statement CORRECT and accurately conditional; surrounding text INCOMPLETE

**The structural part.** The linear part has the form λ_l (−Δ)^{l−1}K for every l. This rests on Donnelly's theorem, SO(2)-invariance and Schur on Sym^{2l−2}(R²), and holds unconditionally. Correct.

**The value λ_l = 2/(l−1)! Π_{l+1}, checked symbolically (sympy):**
- 2t ∫ |x|^{2l} e^{−C²|x|²/4t}/(4πt) (1/t − C²|x|²/4t²) dx = −2l·l!·4^l t^l C^{−2l−2} for l = 1..6.
- Δ^l |x|^{2l} = 4^l (l!)², so λ_l(ϑ) = 2/(l−1)! C^{−2l−2}.
- Averaging over j gives 2/(l−1)! Π_{l+1}(m).
- The only conditional step is exchanging the ε-derivative with the t-expansion. That is exactly what Remark 2.15 isolates.

**l ≤ 2 without the assumption:**
- l=1: DGGW (4.4) in dimension 2 gives b_1(Φ) = 2K/C_S², with Schueth's C_S = 2−2cos ϑ = (the paper's C)². That is 2K C^{−4} = λ_1 K. Exact check: 2Π_2(m) = (m⁴+10m²−11)/(360m) = p_1(m)/m for m = 2..8.
- l=2: Schueth, Thm 4.1 (arXiv:1812.06119; Δ_g = −div grad, the same convention). The ΔK coefficient is −[(m⁵−1/m)/15120 + (m³−1/m)/1440 + (m−1/m)/180]. Exact check: 2Π_3(m) equals that bracket for m = 2..8, so λ_2(−Δ)K matches.
- So the unconditional claim for l ≤ 2 is justified by the cited sources.
- Also: Π_4(m) equals the Δ²K coefficient of Remark 2.16(b) exactly for m = 2..8.

**Still asserted without the condition:**
1. The Introduction ("What is elementary…" and "The analysis") says Section 2.4 "proves the part of the cone terms linear in the curvature (Proposition 2.14)". There is no "for l ≤ 2, or granting Remark 2.15".
2. The paragraph after Prop. 2.14 says that to first order the cone terms at order t^l "add up to 2/(l−1)! Σ_i (−Δ)^{l−1}K(p_i) Π_{l+1}(m_i) plus terms of degree at least two". This is stated for every l. For l ≥ 3 it holds only granting Remark 2.15.
3. The statement of Prop. 2.17(ii) and its echoes depend on the same unproved assumption for L ≥ 4 (item 6). The echoes are the Introduction ("for each L, two signatures with equal c2 carry metrics…") and the paragraph after the proof of Prop. 2.17 in Section 2.4.

## 6. Proposition 2.17(ii)–(iii): (iii) CORRECT; (ii) INCOMPLETE as stated (correct for L ≤ 3, conditional for L ≥ 4)

**(ii), checked step by step:**
- **Only if.** c2 = χ/6 + Σ(m²−1)/(12m) for every metric, and χ/6 + Σ(m²−1)/(12m) = (2−2g)/6 + Σ(m−1)²/(12m). Both identities verified. Example: (0;2⁸) and (0;3,3,3) both give 2/3, with χ = −2 and χ = 0.
- **Restriction to Ω_1..Ω_{L−2}.** Correct: H_L involves c1 (adjusted by the cylinder), c2 (fixed by hypothesis) and c_3..c_L = Ω_1..Ω_{L−2} plus cone terms.
- **Nit.** "Put L' = L−2 ≥ 1" is false for L = 2. That case is trivial, since nothing needs adjusting.
- **Jacobian.** ∂F_l/∂ε_k = −2l G_l ε_k^{−2l−1}, so det = Π_l(−2l G_l) · det(ε_k^{−2l−1}). This is nonzero for distinct ε_k > 0, by the generalised Vandermonde/Rolle argument. Correct.
- **Definition of E and the scaling step.**
  - Shrinking all bumps by s multiplies the Ω_l-change by s^{−2l} (weight count: u_{l+1} has weight 2l+2 and dA has weight −2).
  - Bumps on O with image w0 + Σ_s^{−1}E and on O' with image w0 make c_{l+2}(O) − c_{l+2}(O') = E_l − E_l = 0. Here Σ_s^{−1}E = diag(s², …, s^{2L'}) E → 0, so it stays in the ball around w0.
  - The cylinder changes only the area. Correct.
- **ω_n.** Verified symbolically for l = 1..11: (i) the closed form ω_n = (−1)^n n(n−1) n!/(2n+1)! equals the three-term expression; (ii) the ξ-integral identity ∫|ξ|²|ξ−ζ|² e^{−t|ξ−sζ|²}dξ = (π/t)(2/t² + (2s−1)²|ζ|²/t + s²(1−s)²|ζ|⁴); (iii) the Beta integrals. I also redid the expansion of the second Duhamel term to the t^l coefficient (π/2)ω_{l+1}|ζ|^{2l+2}. At l = 1 it gives θ²/(60π)∫(Δψ)², the classical (1/60π)∫K².
- **The gap.** g_l ≠ 0 for l ≥ 2 is computed "granting the parametric form" (Remark 2.15 says so). So (ii) is proved for L ≤ 3 only. For L ≥ 4 it rests on an assumption the paper does not prove. Yet the statement of Prop. 2.17(ii) and the Introduction claim it for every L ≥ 2 without qualification.
  - Suggested fix: add "for L ≥ 4 granting Remark 2.15" to (ii) and to the Introduction. Alternatively, cite a source for the quadratic part of the heat invariants, or for smooth parameter dependence of the expansion on closed manifolds (both are standard in the literature).

**(iii), the gluing:**
- The exponents (1/m_i − 1) and α0 − 1 sum to −2, so the metric is smooth at ∞. It has a flat orbifold cone point of order m_i at each z_i and a cone of angle 2πα0 at z0. Gauss–Bonnet balances.
- Cutting a small round neighbourhood of z0 gives isometric collars on both sides, since cones of equal angle and radius are isometric.
- A genus-g piece with a cone collar of angle 2πα0 > 0 exists: a rotationally symmetric interpolation to a cylinder, then any cap of genus g.
- The underlying surface has genus g. All cj with j ≥ 3 come from the common piece, because flat regions and flat cone points contribute nothing for l ≥ 1. c2 agrees because χ and Σ(m − 1/m) agree. c1 is matched by the cylinders.
- O(2,8,8) and O(3,3,12) qualify: Σ(1−1/m) = 9/4 and Σ(m−1/m) = 18 − 3/4 for both.

## 7. Remark B.6 (How short the times must be): CORRECT, all numbers reproduced

**Inputs**, as stated in the remark and Lemma B.5:
- n = N = 3, times τ/4, τ/2, τ, µ0 = 12, A0 = π/2, D = 4.897, ℓ0 = 2.2567.
- 2·arccosh(cot²(π/8)) = 4.89690, so D = 4.897 is an upper bound.
- Q_3 = max(|α_3|/2, 3|b_2(12)|) = max(2/315, 174889/576) = 303.627.
- B0 is negligible: e^{−ℓ0²/4t} underflows at these times.

**Row bounds.**
- δ_{1,j}/τ = (1.9e−16·(τ/1e−9)², 1.0e−6·(τ/1e−9), 1138.6). So δ1 ≈ 1.14×10³ τ. Exactly, row 3 gives (1/12 + 1 + 8/3)·Q_3·τ = 3.75·Q_3·τ.
- δ1 ≤ δ_thm = 3.80e−7 holds for τ < 3.337×10⁻¹⁰ ("about 3.3×10⁻¹⁰").
- At τ = 10⁻¹¹ it holds for η ≤ 4.608×10⁻¹⁹ ("4.6×10⁻¹⁹").

**Uniform bound** (also in the remark).
- ‖V⁻¹‖∞ · τ · Q_3 τ² = 16 Q_3 τ = 4858 τ ("4.9×10³ τ").
- τ < 7.822×10⁻¹¹ ("7.8×10⁻¹¹").
- η ≤ 2.071×10⁻¹⁹ ("2.07×10⁻¹⁹").

**N = 8 times τ, …, τ/128 with row bounds j ≤ 3.**
- δ_thm: τ_max = 3.597×10⁻³ ("3.6×10⁻³"); η_max at τ_max/2 = 5.00×10⁻¹³ ("5.0×10⁻¹³").
- δ_cert = 2.341e−3: τ_max = 1.54×10⁻² ("1.5×10⁻²"); η_max = 1.32×10⁻⁸ ("1.3×10⁻⁸").
- The smallest time is then 6.0×10⁻⁵, below 10⁻⁴. All correct.

I took δ_thm(2,8,8) and δ_cert as given; I did not recompute them.

## 8. Theorem 3.11(ii) and the constants: CORRECT

**C = Dq is the least C.** Valid C are exactly the multiples of D, because ν(a) = C a w_a must be integers. On those, s scales linearly, so the least C making s even is D times the denominator of s_D/2.

**Computed values** (exact rationals):

| M | C (brute force) | Dq | D | q | s at C = D |
|---|---|---|---|---|---|
| 2 | 6 | 6 | 3 | 2 | 1 |
| 3 | 120 | 120 | 120 | 1 | −2 |
| 4 | 2520 | 2520 | 2520 | 1 | 2 |
| 5 | 362880 | 362880 | 362880 | 1 | −10 |

- Brute force over all positive integers C, not only multiples of D, gives the same values for M = 2, 3, 4.
- The values also agree for M up to 9.

**Related identities, all verified for M ≤ 9:**
- a w_a = (−1)^{M−a} 2a³/((M−a)!(M+a)!).
- ν ∝ (−1)^{M−a} a³ binom(2M, M−a).
- s = Σν + C w_1 in (ii).

**Examples in the text:**
- (ν(2), ν(3)) = (−16, 9), with s = −2.
- (28, −27, 8).
- The least-g areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054} for M = 2..9.
- The pairs (1;3⁹) against (0;2¹⁶), and (0;2²⁸,4⁸) against (1;3²⁷). Exact c1..c5 show they share exactly c1..c_{M−1}, with differences (−1)^M C a_{M−2} = −1/3 and +1.

**(iv) with M = 2, X = 4.**
- w = (1/45, −1/36, 1/180), C = 180 (= Dq with D = 90 and q = 2), ν = (10, −4), s = 2.
- s = Σν − C w_1 holds; Σν + C w_1 does not. So the statement that in (iv) s = Σν(a) − C w_1 is correct.
- (0;2¹⁰) and (1;4⁴) share exactly c1 = 3/2 and c2 = 3/4, with c3 differing by 1/2 = C a_1.

## 9. Descartes bound, Theorem 1.3(ii), Remark 3.22: CORRECT

**Thm 3.15.**
- κ ≥ 2L+2 > 2L−1, so the vanishing odd indices k = 1, 3, …, 2L−3 and k = κ−1 are distinct. That leaves at most (κ−2L)/2 nonzero odd-degree coefficients.
- Gap counting: an even gap contributes 0 or 2 (≤ d−d') to V⁺+V⁻ and 0 to V⁺−V⁻. An odd gap contributes 1 and ±1. Hence V⁺+V⁻ ≤ κ.
- All roots are real and nonzero, so Descartes gives equalities and ι = V⁺−V⁻.
- Each odd gap has exactly one odd-degree endpoint, and each such coefficient bounds at most two gaps. So |ι| ≤ κ−2L. Then ι = 2(g'−g), and the equality case (|ι| = 2, sizes {L, L+2}) follows.

**Thm 1.3(ii).** |U|+|V| = n + n' + |d| with d = R' − R, and |U*|+|V*| ≤ |U|+|V|. This gives n + n' + |R−R'| ≥ 2L + 2|g−g'|. Checked on Example 3.9, where 6 = 6 is attained, and on the genus pair of Example 3.21(i), where 10 ≥ 8.

**Remark 3.22.**
- (ΣV)(Σ1/V) ≥ 25 by AM–HM for five positive entries.
- The e3 coefficient is indeed 3 − 3P1(V)R(V), since P3 = e1³ − 3e1e2 + 3e3 with e2 = R e3. So it is nonzero.

## 10. Corollary 6.5 (A-posteriori use) for δ_thm, and the paragraph after it: CORRECT

**The corollary.**
- |c_j(m) − c_j(m*)| ≤ δ1 + δ2 ≤ δ_thm(m*), so by Thm 6.2 at m* the rounded recovery from c(m) returns m*.
- From exact data, M(I_n(m)) is invertible: det = ±Π(m_i+m_j)/e_n ≠ 0 for positive orders, and e(m) solves the system (Thm 3.3). So the recovered roots are m and rounding returns m. Hence m = m*.

**The paragraph after it.** Prop. S3.1 is stated in the supplement as "every data vector with |c̃_j − c_j(m)| ≤ δ_j is recovered exactly after rounding if …". Applied at m* with radii δ1+δ2, the same argument goes through. The surrounding caveats (δ1 must be proved; Lemma B.5 needs very short times; the blind recovery is validated, not proved) are accurate.

## 11. Supplement: Bolza benchmark and "Changing the shape": CORRECT

**Bolza.**
- Bolza is the regular octagon with angles π/4 and opposite sides paired. The rotation R by π/4 conjugates the pairing g_i to g_{i+1}, so ⟨R⟩ ≅ Z/8 acts by isometries.
- Fixed points: the centre (stabiliser Z8) and the single vertex class (all eight corners are identified, and R rotates the total angle 2π by π/4, so the stabiliser is Z8). R permutes the four edge-midpoint classes cyclically and R⁴ fixes each, so one orbit with stabiliser Z2.
- Riemann–Hurwitz: −2 = 8(2−2h) − (7 + 7 + 4·1), so h = 0. The quotient is (0;2,8,8) with χ = 2 − 9/4 = −1/4 = −2/8. As stated.

**Changing the shape.**
- An orientation-reversing isometry σ fixing the four cone points has a fixed set that is one circle: a quotient with two boundary circles would be an annulus, whose double is a torus, and the fixed set is nonempty. So the quotient is a quadrilateral with geodesic sides and angles π/3.
- Four points on a circle with a given cross-ratio are Möbius-equivalent to a rectangle configuration with the same cross-ratio. That configuration is symmetric under z ↦ z̄ and z ↦ −z̄.
- Uniqueness of the hyperbolic orbifold metric in its conformal class makes these anticonformal maps isometries. The converse inclusion is clear.
- One step is unstated: that σ is an involution. It holds because σ² is an orientation-preserving finite-order isometry of the sphere fixing four points, hence the identity. This is minor.

## 12. Prior work, the N(k) paragraph: CORRECT

Checked against Croot–Mao–Yip, arXiv:2609.05061v1 (4 Sep 2026), §1:
- They define P(k,m) as the least s with distinct solution sets for equal power sums j = 1..k, and W(k,m) as the same with pairwise unequal (k+1)-th power sums. So N(k) as defined in the paper (no condition at exponent k+1) is P(k,2).
- They state P(k,2) ≥ k+1. They state "Using a pigeonhole principle argument one can easily see that P(k,m) ≤ k(k+1)/2 + 1", and that "the pigeonhole principle does not readily yield an upper bound on W(k,2)".
- They state "The best-known upper bound is W(k,m) ≤ k(k+1)/2 + 1, due to Wooley [22, Theorem 13.1]".
- Wright introduced the variant with unequal (k+1)-th power sums. P(k,2) = k+1 is known for 2 ≤ k ≤ 9 and k = 11.
- All of these match the paper's paragraph.

**N(k) ≤ W(k,2).** Immediate: a W-solution is a P-solution of the same size. So Wright's and Wooley's bounds hold a fortiori for N(k).

**The pigeonhole bound itself** (re-derived):
- Multisets of size n in [1,Q] number at least Q^n/n!. The vectors (P1..Pk) number at most n^k Q^{k(k+1)/2}.
- So n = k(k+1)/2 + 1 suffices for large Q.
- The odd-exponent version in Lemma A.1, with n = (L−1)²+1 and Q > n! n^{L−1}, is also correct.

**Not checked.** I could not fetch Borwein–Ingalls [4], so the citation "[4, Props. 2–3]" for the pigeonhole bound is unverified as an attribution.
