<!-- Round 10 blind check of the Paper B changes: returned text saved verbatim; the reviewer could not write files -->

Blind check of paper/eigen/build/manuscript.pdf, items 1–7. I read only the PDF and recomputed what I could. Scripts and renders are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/main/scratch/blind-B/ (heat.py, t1.py, b1.py, t5.py, acc.py, c85.py, ucar.py, r67.py; Uçar's thesis is in dl/ucar/).

**Summary:** I found no mathematical errors. Items 3–7 are correct. Items 1 and 2 have only minor gaps: two unstated assumptions in Theorem 6.5, and a theorem number in Cheng that I could not check against the original.

### 1. Theorem 6.5 and its proof: CORRECT, with two minor gaps
- **Part (i):** the reduction to e^{-y}y^p < (γ*/16ϖ)(ε²/4)^p is right. So is the bound e^{-y/2}y^p ≤ (2p/e)^p, whose maximum is at y = 2p. With y0 = 2(log(16ϖ/γ*) + p log(4/ε²) + p log(2p/e)), e^{-y0/2}(2p/e)^p equals the right-hand side exactly. The inequality y > y0 is strict because t < t3.
- **Part (ii):** the following all hold.
  - Θ(t) ≤ 1/24, since γ* ≤ a0 = 1/12, k* ≥ 2 and t < 1. Hence Θk ≥ Θ(t).
  - The procedure terminates, because bk → B*(t) < Θ(t)/8.
  - When it stops, each gap is at least max(Θ(t), |qσ−qσ'| − 2^{1−k}), which is at least Θk.
  - Θk ≤ 1 gives Λt ≥ 2 log 8 ≥ 1, and so 1/Λ ≤ t, as Corollary 6.4 needs.
  - The proof of 6.2 uses only that N is an integer with N > eZ♯(1/Λ), and that Ntδ ≤ Θ/(8e).
- **Computability details:** these check out.
  - I1 = e^{-t/4}/t − ∫₀^∞ h follows from r tanh πr = |r| − 2|r|/(e^{2π|r|}+1).
  - 0 ≤ h ≤ 1, and |h'| ≤ 4/(e^{2πr}+1) + h(2π+2tr) ≤ 2 + 2r(2π+2tr), using h ≤ 2r.
  - 0 < Fj ≤ 1 holds for both signs of r. The bound on |Fj'| is right.
  - The midpoint-rule error LH²/(4n) is right, and so are the tail bounds.
- **Gap (a), choosing t:** "N and δ are computable from A, ε, M" requires picking a rational t < t*. That needs a computable positive lower bound for t*, so A and ε must be computable reals. Say so in one clause.
- **Gap (b), enumerating Sig(A, M):** this means deciding s(σ) ≤ A/2π exactly. That is not decidable for an arbitrary computable real A when equality occurs. Fix: assume A/2π is rational, as it is in every example, or note that only the finitely many values s(σ) matter.
- **Wording:** "Proposition 6.6 records six runs … that did [stop]" is loose. The runs of Proposition 6.6 used the least certified lower gap, rounded down, not the Θk = min{1, max(…)} rule. Say "runs of the same certification".

### 2. Proposition 8.8: CORRECT; Cheng's numbering not verified
- **Cheng's statement:** I could not get Cheng's paper (Springer paywall, OpenAlex lists it as closed). The form quoted is the standard one: λ_m ≤ λ_1^D(V_n(k, d/2m)), with 0 = μ0 indexing. That bound comes from m+1 points spaced d/m apart on a minimising geodesic, which give disjoint balls of radius d/2m, plus the ball comparison.
- **Theorem number:** from memory, in Cheng's paper the ball comparison may be Theorem 1.1, with the λ_m bound in §2 possibly numbered as a corollary. Please confirm that "Thm 2.1" is the right label.
- **The constants:**
  - λ_1^D of a disc of radius R in H² is at most 1/4 + π²/R². This follows from f = (sinh ρ)^{-1/2}u, a sine arch, and q ≤ 1/4 in (3).
  - With R = d/2j this gives 1/4 + 4π²j²/d².
  - The area of a ball of radius d is 2π(cosh d − 1) ≥ 4π(g−1), so d ≥ arccosh(2g−1).
- **Systole > ε (residual finiteness):** correct. Φ is finite, and Γ1 is the intersection of finitely many finite-index kernels, so it is normal of finite index. The conjugation trick gives d(x0, γ'x0) ≤ 2D0 + ℓ(γ), so ℓ ≤ ε would put γ' in Φ.
- **Cyclic covers:** correct. The kernel of Γ1 → H1 → Z/q has index q, so the genus is 1 + q(g1 − 1). These genera are distinct because g1 ≥ 2, and lengths are inherited, so the systole stays > ε.
- **Pigeonhole:** correct. Λ' = 1/4 + 4π²N²/arccosh(3)², with arccosh 3 = 1.76275. There are ⌊Λ'/δ⌋+1 intervals per coordinate, and infinitely many q, so infinitely many vectors share a box. The conclusions about C(A, ε, M) and about δ/2 follow.

### 3. Corollary 8.5: CORRECT; wording only
- **Contrapositive of Proposition 8.3:** the orders 7…M give M − 6 orbifolds in C(A, ε, M). The midpoint of two eigenvalue lists is within δ/2 of both. This gives M − 6 ≤ J.
- **Constants:** ΛN ≤ c'N² for N ≥ 1, with h7 = 0.5452748 and c' = 1/4 + π²/h7² = 33.4447. Λ2 = 133.0288 > 133.
- **Vacuity claim:** for δ ≤ 1/M, ⌊Λ2/δ⌋ + 1 > Λ2·M ≥ M − 6. So N = 2 satisfies the constraint.
- **Wording:** "vacuous" is slightly overstated, since for M ≥ 8 the constraint still excludes N = 1. Say "it gives nothing beyond N ≥ 2". Also, the logarithmic form needs M ≥ 7; state it.

### 4. Accuracy paragraph in Section 7: CORRECT
- **Uniform hypothesis:** Nδ = 283 × 4.27e-5 = 0.012084. Uniform relative accuracy is 4.27e-5 / (8 × 282) = 1.89e-8, i.e. about 2e-8.
- **Weighted hypothesis:** solving Σ_{j<283} r·λj·e^{-t(1−r)λj} = Nδ with λj = 8j and t = 0.02482 gives r = 5.97e-5. Using Table 8's λ1…λ40 plus a Weyl tail gives r = 5.89e-5 for O(2,8,8) and 5.89e-5 for O(3,3,12), matching the printed 5.9e-5.
- **Tail share:** eigenvalues above 500 carry a fraction 5.5e-5 of the weighted sum, consistent with "less than 1e-4".
- **Wording:** "Our estimated errors ϵj are below 2e-13 relative for j < 283" sits next to the paper's own admission that these ϵj are rounding-level and say nothing about discretisation. Quote the second estimate instead (up to 1.2e-8 relative for the first 500). It is the meaningful number and is still far below 6e-5.

### 5. Remark 6.7: CORRECT
For A = π/2, M = 12 I recomputed the following.
- **Default constants:** n* = 4, k* = 4, δ1 = 1/55440, δ2 = 1/12, δ3 = 1/360, δ4 = 1/2520. The ratios δk/4Q(k−1) for k = 1…4 are 1.12e-6, 1.01e-3, 1.72e-6 and 6.85e-9, so t1 = 6.8e-9, attained at k = k*.
- **Class-exact data:** enumerating Sig(π/2, 12) gives 48 signatures. The largest first-difference index is 3. The least first differences are 1/2640, 1/12 and 25/12, which give t1 = 2.359e-5, i.e. 2.4e-5.
- **Other claims:** the area-12π pair (0;2⁴,7⁷), (0;4⁶,8⁴) shares c1–c3 and differs at c4, by −54/7. In every row of Table 6, t1 matches (1.1e-7, 6.8e-9, 9.3e-4, 2.7e-11, 7.8e-4, 3.3e-4, 2.5e-27), with the minimum at k = k*.

### 6. Table B1: CORRECT
- **Entries:** I recomputed all 42 entries independently with mpmath quad at 30 digits, from the Theorem 2.1 integrals. Every entry agrees within half a unit of its last digit. The largest deviations are 4.2e-9 on I1 in row 1, 3.5e-8 and 3.1e-8 in rows 4–5 (unit 1e-7), and 3.1e-6 in row 6 (unit 1e-5). The E_m entries agree to about 5e-11 or better.
- **Gaps:** I enumerated Sig(A, M) exactly; the sizes are 27, 48, 8, 8, 281 and 12. Working in exact rationals from the printed decimals, I subtracted the stated error (s/2 units of I1 plus one unit per E_m) from every pairwise gap. The least such gap is at least Θ in every row: 0.0158823, 0.0065273, 0.1520293, 0.1655107, 0.0013738 and 0.1666387. The minimising pairs match Table 5.
- **Error size:** the largest error from the decimals is 5.0e-6 (row 6), consistent with the "6e-6" claim.
- **Tables 4 and 5:** I recomputed C*, B*(t), t ≤ t2, Λt, N, δ and Λo; all match. N = 244, 283, 139, 2605, 7416 and 387182. B* = 7.98e-6, 7.10e-5, 0.01793, 0.01671, 1.41e-4 and 0.01394. Λt = 17.63, 19.64, 12.52, 17.21, 27.94 and 26.32.

### 7. Agreement with Uçar (4.33)–(4.35) at κ = −1: CORRECT
- **Source:** I fetched arXiv 1711.03405, which is the thesis itself. (4.33) is C = ΣνΣℓ 2/(4^ℓ ℓ!)·c^S_{ν−ℓ}(π/k)·κ^ν t^ν, with c^S from (4.25). (4.35) is a_ν = vol/(ν! 4^ν)·Σ C(ν,ℓ)(−4)^ℓ B_{2ℓ}(1/2) κ^ν, in the normalisation (1/4πt)Σ a_ν t^ν.
- **Comparison:** at κ = −1, for ν ≤ 8 and m = 2…12, Uçar's cone term equals the paper's b_ν(m), and a_ν/vol equals α_ν. The largest relative difference is 1e-49, i.e. exact; for example m = 3 gives 2/9, −4/27, 4/27, −8/27, 220/243.
- **Independent check:** I also derived b_l and α_k directly from the trace-formula integrals, using moments of 1/(2 sin(x/2)) and Dirichlet-eta values. These agree too.
- **Suggestion:** cite (4.25) as well, since (4.33) is not explicit without c^S.

### Wording errors and suggestions
- Theorem 6.5 should state the assumptions on A and ε noted under item 1. It should also say that the runs of Proposition 6.6 used the certified least gap rather than the Θk rule.
- Corollary 8.5: say it requires M ≥ 7, and replace "vacuous" with "yields only N ≥ 2".
- Section 7: replace the 2e-13 figure with the 1.2e-8 second estimate.
- Section 6: "within 6×10⁻⁶, less than 10⁻³ of Θ/16 in every row" reads as if the 6e-6 bound were used in every row. With 6e-6 in row 5, the ratio to Θ/16 would be 0.07. The claim holds only with each row's own error (row 5: 3.4e-8). State that it is per row.
- Uçar citation: add (4.25).
- Cheng: verify the theorem number ("Thm 2.1") against the original.

### Overall verdict
The new and changed results are mathematically sound. Every number I could recompute agrees: Table B1 to within half a unit, all certified gaps at least Θ, Tables 4, 5 and 6, t1 = 6.8e-9 → 2.4e-5, c' = 33.4447, Λ2 = 133.03, r ≈ 6e-5, and exact agreement with Uçar. The remaining points are minor: two unstated assumptions in Theorem 6.5, an unverified theorem number in Cheng, and wording. The paper can be accepted for these items once these are fixed.
