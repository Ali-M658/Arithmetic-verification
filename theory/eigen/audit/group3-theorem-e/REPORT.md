<!-- Returned text of the blind reviewer for Group 3 (Theorem E), saved verbatim by the main session: the reviewer could not write report files. Its scripts and run logs are in this directory. -->

# Group 3 referee report: Theorem E

**Verdict:** Lemma eig:int, Lemma eig:gap and Theorem E (with its corollary) are correct as stated, and their explicit N and δ are valid. Remark eig:Mneeded is false if read literally and needs rewording. One growth-rate claim in the Group 4 text and one notation clash need small fixes. Nothing is FATAL or SERIOUS.

I read only `STATEMENTS.md` and `sources/`. I reimplemented the heat invariants exactly and independently in `heat.py`, from eq. (phik), (bl) and the α_k formula. Groups 1 and 2 were taken as given; I checked only that they are applied within their hypotheses.

| Statement | Grade |
|---|---|
| Lemma eig:int | NONE |
| Lemma eig:gap | NONE |
| Theorem eig:E, with the corollary | NONE (one MINOR notation point) |
| Remark eig:Mneeded | MINOR (wording) |
| Group 4 text about Theorem E's N | MINOR (growth rate wrong) |

## Lemma eig:int: NONE

**Derivation, part (i).** If the areas differ, d_1 = (χ' − χ)/2. This is a nonzero rational whose denominator divides L, so |d_1| ≥ 1/(2L). In the class, L divides L_M.

**Derivation, part (ii).** If the areas are equal:
- **Formula and sign.** By lem:sigdata and lem:triangular, d_k = (−1)^k a_{k−2} (Ψ_{k−1}(m) − Ψ_{k−1}(m')). The leading coefficient is a_{k−2} by lem:conepoly, and the sign is correct.
- **Paddings.** ψ_j(1) = 0, so padding by 1s changes nothing. The paddings make R(U) = R(V), which turns the difference into the nonzero integer P_{2k−3}(U) − P_{2k−3}(V).
- **Fermat divisibility.** If (p−1) divides 2k−4, then x^{2k−3} ≡ x mod p for every integer x. The difference is then ≡ P_1(U) − P_1(V) = 0 mod p. This step uses k ≥ 3, which the statement assumes.
- **Range.** I derived it independently from thm:sigsep with L = k−1: 2k ≤ |U*| + |V*| ≤ 2 max(n+4g, …) ≤ 2(⌊Area/π⌋ + 4).

**Code checks.**
- `check_basics.py` confirms the implementation:
  - b_0 = (m²−1)/12m and α_0, α_1 = 1, −1/3.
  - p_l has exact degree 2l+2 with leading coefficient a_l, for l ≤ 11.
  - The triangular identity holds exactly. a_0..a_4 = 1/12, 1/360, 1/2520, 1/10080, 1/28512.
- `check_int.py` is exhaustive over all 5553 signatures with Area ≤ 6π and orders ≤ 10, using exact arithmetic:
  - 30,920 equal-area pairs, including every lexicographically adjacent pair. Adjacent pairs attain the deepest first difference in each area class.
  - The range, formula, nonzero integrality, divisibility and |d_k| ≥ a_{k−2} hold every time. First-difference indices were k = 2 (29,609 pairs) and k = 3 (1,311 pairs).
  - Different areas: 218,757 pairs, with minimum |d_1|·2L = 1, so (i) is sharp.
- `check_int_deep.py 30 5` searched for deep coincidences among 283,179 signatures with orders ≤ 30 and tested 14,564 pairs with k ≥ 3:
  - k = 4 occurs 33 times, for example (0;3,10,15,30) against (0;4,5,21,28), with P_5 difference 3,861,000 (divisible by 30, as required).
  - Every pair passes. No pair reaches k = ⌊Area/π⌋ + 4, which is expected since the bound is not sharp.

## Lemma eig:gap: NONE

**Derivation.** Take K = k−1 and apply eig:Grem with t_0 = 1 and t ≤ t_1 ≤ 1 to both signatures:
- Each orbifold has Area ≤ A and n ≤ n_*. By the stated monotonicity in m, Q_cone(m_i) ≤ Q_cone(M). So each remainder is at most t^{k−1} Q(k−1).
- The terms j < k cancel, so |ΔG| ≥ t^{k−2}(|d_k| − 2t Q(k−1)) ≥ δ_k t^{k−2}/2.
- Then t^{k−2} ≥ t^{k_*−2}. This holds for k = 1 too, where Q(0) uses Q_cone(m,0,·) = b_0(m) and Q_area(0,·) = 1/3.

**Quadrature test.** I computed G_σ from the trace-formula integrals (thm:IEH) at 60–110 digits, at t_1/10, t_1, t_* and 10·t_1, over all pairs in each class:

| Class | Signatures | Minimum gap / Γ(t) |
|---|---|---|
| π/2, ε = 1.86, M = 12 | 48 | about 3.4e13 |
| π/2, ε = 0.05, M = 7 | 20 | about 5e15 |
| 3π, ε = 0.3, M = 3 (k_* = 7) | 21 | about 7e41 |

In the first class the closest pair is (0;2,8,8) against (0;3,3,12), with k = 3 and d_3 = 25/12. The lemma is very loose but correct.

The Group 2 remainder bound eig:Grem also held in every case. One apparent failure at 60 digits (K = 6, t ≈ 3e−9) was a precision artifact and passes at 110 digits.

## Theorem eig:E: NONE

**Derivation.** I rebuilt the proof as three error terms, each at most Γ_*/8:
1. **Hyperbolic term.** The bound uses lem:hypbound within its hypotheses:
   - t_* ≤ t_2 ≤ ℓ²/(2(1+ℓ)).
   - B increases with diameter and decreases with ℓ, and diam < D.
   - 1/Area ≤ 21/π.
   - 1 + 2t/(ε−t) ≤ 3, since t_2 < ε/2.
   
   This gives B_*(t) = ϖ e^{3D} t^{−1/2} e^{−ε²/4t} with ϖ = 63·…, which matches. The claim B_*(t_*) ≤ Γ_*/8 is equivalent to y − p log y ≥ c, which holds for every y ≥ y_0 because p log y ≤ y/2 + p log(2p/e). No monotonicity is needed; max(y_0, 1) covers c < 0.
2. **Tail.** B_* increases on (0, ε²/2), and t_2 < ε²/2. So Hyp(s) ≤ Γ_*/8 ≤ 1 for s ≤ t_*, which justifies the "+1" in Z_b. Also 1/Λ < t_*.
   - eig:counttail with s = t_*/2 gives a tail of exactly Γ_*/8.
   - N = ⌊e·Z_b(1/Λ)⌋ + 1 > e·Z_O(1/Λ), so λ_j > Λ for every j ≥ N. The index bookkeeping is right.
3. **Perturbation.** min(λ̃_j, λ_j)·t_* ≥ −δ t_* ≥ −1, using λ_j ≥ 0 and δ ≤ 1/t_*. So negative approximations are handled, and the total is at most e·N·t_*·δ ≤ Γ_*/8.

**Conclusion.** The total error is 3Γ_*/8, and every other signature is at least 5Γ_*/8 away, so the minimiser is unique.
- σ(O) is in Sig(A,M).
- The competitor set needs no geometric hypothesis, because G_σ depends only on σ.
- The corollary holds: apply the theorem to both orbifolds with the same data λ̃ = λ(O').

**Code checks.**
- `theorem_e.py` checks every inequality of the chain for eight classes:
  - (π/2, 1.86, 12), (π/2, 0.5, 7), (π/2, 0.05, 7), (2π, 1, 4)
  - (3π, 0.3, 3), (π/3, 0.56206, 7), (4π, 5, 2)
  - (π/2, 3, 2), whose signature set is empty, so it passes vacuously.
  
  In (π/2, 0.05, 7), t_3 is the binding constraint.
- With quadrature, the decision rule recovers every signature in all three test classes under an adversarial error of ±3Γ_*/8.
- `check_perturb.py` ran 20,000 synthetic spectra, including negative λ̃ and δ = 1/t. The worst ratio to e·N·t·δ was 1 − 1/e ≈ 0.632.

**Recomputed constants for A = π/2, ε = 1.86, M = 12:**
- D = 1125.4413 and γ_* = 1/55440.
- Q(0..3) = 4.014, 20.81, 406.3, 14514.
- t_1 = 6.835169e−9, attained at k = 4. t_2 = 0.6048, y_0 = 6793.0, t_3 = 1.273e−4, so t_* = t_1.
- Γ_* = 4.2135e−22 and Λ = 2.0106e10.
- **N = 6,831,617,376 and δ = 4.149e−25.**
- The chain holds with huge slack: log B_*(t_*) ≈ −1.27e8 against log(Γ_*/8) ≈ −51.3.

For (π/2, 0.05, 7), where t_3 binds: N = 426,681,329 and δ = 1.97e−21.

**MINOR (notation).** Z_b is defined in eig:count with H(t) and redefined in eig:E with +1. The +1 version is valid only for s ≤ t_*. Fix: rename it, and add one line on why Hyp(s) ≤ 1 at s = t_*/2 and s = 1/Λ.

## Remark eig:Mneeded: MINOR

1. **False if read literally.** "For every N and δ > 0 two of these orbifolds [O(2,3,m), 7 ≤ m ≤ M] have their first N eigenvalues within δ" contradicts Theorem E when M is fixed. eig:N1 needs M ≥ ⌈Λ_N/δ⌉^{N−1} + 7. Fix: "for every N, δ there is M such that …".
2. **Conclusion too general.** "Area and systole alone do not bound the cone orders; no N, δ depending on A, ε alone exist" is true only for A ≥ π/3 and ε ≤ σ_0. For A < π/3 the area alone bounds the orders: (2,3,m) has area 2π(1/6 − 1/m) ≤ A only when m ≤ 12π/(π − 3A), and the other triangles of area < π/3 are finitely many. Fix: add "for A ≥ π/3 and ε ≤ σ_0".

## Group 4 text about Theorem E: MINOR

The Group 4 paragraph says Theorem E's N grows "roughly like 1/ε²". The actual rate is ε^{−3} up to a log factor. For small ε, D grows like 1/ε, and y_0 contains 6D, so t_3 shrinks like ε³.

Numerically (A = π/2, M = 7), N = 8.6e8, 7.6e9, 6.6e10, 5.7e11, 5.0e12 for ε = 0.04, 0.02, 0.01, 0.005, 0.0025. That is about ×8.7 each time ε halves. Fix: say "roughly like ε^{−3}".

Files in this directory: heat.py, check_basics.py, check_int.py, check_int_deep.py, theorem_e.py, check_perturb.py, run_A0.5pi_e1.86_M12.txt, run_A0.5pi_e0.05_M7.txt, run_A3pi_e0.3_M3.txt.

**Overall verdict:** eig:int, eig:gap and Theorem E are correct with valid explicit N and δ; only MINOR fixes are needed (Remark eig:Mneeded wording, the ε^{−3} growth claim, and the Z_b notation clash).
