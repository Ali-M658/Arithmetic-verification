# G5-bis blind review, group `threshold-sharpness`

| id | statement | grade |
|---|---|---|
| TH.1a | Theorem 5.13 (the threshold): S <= 17 determined by the first two heat invariants, 17 sharp | **NONE** |
| TH.1b | Proposition (collision-free sums, computational): exactly 38 sums in [18, 4800] | **NONE** |
| TH.1b-M | Method claims: scaling lemma, 3962 covered / 783 remaining, first pairs at 18, 20, 26 | **NONE** (one counting convention to state, see below) |
| TH.2 | Sharpness wording (abstract, Thm 1.4, after Thm 6.6) | **MINOR** |
| TH.3 | Remark 6.8 addition, real-multiset restriction of the Prop. 6.7(ii) witnesses | **NONE** (one hypothesis to make explicit) |

No FATAL and no SERIOUS findings.

## Contamination

None. I read only `review/audit-2/REVIEWER-BRIEF.md`, `review/audit/G5-VERDICT.md`,
`review/audit-2/statements/threshold-sharpness.md`, `review/audit/statements/threshold.md` and
`review/audit/statements/stability.md`. I opened no file under `theory/`, `paper/`, `review/audit/threshold/`,
`review/audit/stability/` or `review/referee-sim/`. The bundle does not include the Method paragraph of the
Proposition. I checked the Method claims as the lead quoted them in the task message: 3962 sums covered by
scaling, 783 remaining, and the first pairs.

## Instrument gaps

None. No external input is needed (bundle: "None external"). No source was fetched. See `fetches.md`.

## Files

- `check_collisionfree.c`: exact C search (64-bit gcd, `__int128` re-check on every hash hit, no floating point).
  Its output is `collisions_18_4800.txt`, one line per S: S, number of hyperbolic triads, collision flag, first
  pair found. Run: `nice -n 10 ./cf 18 4800 collisions_18_4800.txt`, 33.7 s CPU, one process
  (`memory_pressure` 45% free beforehand).
- `check_collisionfree.py` / `.txt`: an independent `Fraction` certification of (A) and (B).
- `check_sharpness.py` / `.txt`: sympy and Fraction checks for (C).

Both Python scripts end with `ALL CHECKS PASSED`, exit 0, and raise `AssertionError` (exit 1) on failure.
Total CPU used is about 5 minutes.

---

## TH.1a. Theorem 5.13 (the threshold): grade NONE

**Inputs.** The invariants are taken from the context.

- ST.0, for n = 3: H₋₁ = Area/4π = (1 − R)/2, and H₀ = (Area/4π)·α₁ + Σ b₀(mᵢ), with α₁ = −1/3 and
  b₀(m) = (m² − 1)/(12m) (PC.6, PC.7).
- The separation theorem PC.14/TH.4 (Corollary 2) is previously audited.

**Derivation.**

1. *The two invariants are equivalent to (R, S₁).* From the formulas above,
   H₀ = −(1 − R)/6 + (S₁ − R)/12 = (S₁ + R − 2)/12. So R = 1 − 2H₋₁ and S₁ = 12H₀ + 2 − R. The map
   (R, S₁) ↦ (H₋₁, H₀) is an affine bijection (checked exactly for every triad with S ≤ 59).
   So two triangle orbifolds share their first two invariants if and only if they have the same S₁ and the same R.
2. *Larger sums need no search.* Suppose O(p, q, r) has S = p + q + r ≤ 17, and O(p′, q′, r′) is any hyperbolic
   triangle orbifold, of any sum, with the same (H₋₁, H₀). Then p′ + q′ + r′ = S₁ = S ≤ 17 by step 1.
   So the competitor lies in the finite set of triads of the same sum. The comparison with all hyperbolic
   triangle orbifolds therefore reduces to injectivity of R on each fixed sum S ≤ 17. This bound is the
   whole answer to "how do you bound the larger sums": S₁ itself is an invariant.
3. *Injectivity for S ≤ 17* is the interval-separation theorem (Corollary 2 of the threshold context).
   - Lemma `lem:chamber`: R is strictly monotone within each least-order stratum.
   - Theorem `thm:separation`: the stratum intervals are pairwise disjoint for S ≤ 17.
   - Direct check: there are exactly 65 hyperbolic triads with S ≤ 17. The least sum is 10, attained only by
     (3, 3, 4). Their (H₋₁, H₀) are pairwise distinct.
   - Cross-check, not part of the proof: none of the 65 shares (H₋₁, H₀) with any triad of sum ≤ 300.
4. *Sharpness.* At S = 18 there is exactly one collision fibre, {(2,8,8), (3,3,12)}, with R = 3/4 (exact
   enumeration). So O(2,8,8) has sum 18 and is not determined by two invariants, and the uniform bound 17
   cannot be raised. The phrase "the first failure occurs at cone-order sum 18" is exact.
5. *K_iso ≤ 2.* This follows from steps 1–3: the orbifold O(p, q, r) is determined up to isometry by the
   multiset {p, q, r}.

**Counterexample hunt.**

- Smallest sums: S = 10, …, 17 contain 65 triads, and all are injective.
- Boundary: S = 18 has exactly one fibre of size 2.
- p = 2 truncation: triads (2, q, r) need q + r ≥ 9.
- Competitors of larger sum: excluded by step 2, and cross-checked up to S = 300.
- Nothing found.

**Wording.** No change is required. Optionally, add one clause to the proof stating that the first two
invariants determine S₁ (eq:s1inv), so that the comparison with larger sums is explicit.

---

## TH.1b. Proposition (collision-free sums): grade NONE

**Reading the printed list.** 19, 21–25, 27–30, 33, 41, 44, 46–51, 59, 65, 67, 81, 99, 115, 119, 123, 125, 173,
199, 203, 223, 235, 243, 251, 307, 329, 557.

- The ranges 21–25, 27–30 and 46–51 contribute 5, 4 and 6 sums, a total of 15.
- With the 23 isolated sums this gives **38**, all distinct (asserted in the script).

**Search.** For each 18 ≤ S ≤ 4800, the C program enumerates 2 ≤ p ≤ q ≤ r with p + q + r = S, keeps
qr + rp + pq < pqr, reduces R = e₂/e₃ by gcd, and hashes the reduced pair.

- e₃ ≤ 1600³ < 2³⁷, so 64-bit arithmetic is exact.
- Every hash hit with equal reduced fraction is re-verified by `__int128` cross-multiplication.
- The search stops at the first collision of each S, but all triads are still counted.

**Results.**

1. The collision-free sums in [18, 4800] are **exactly the 38 printed**. The largest is 557, and the C count of
   hyperbolic triads at S = 557 is **25,575**, as claimed.
2. Each of the other **4745** sums in [18, 4800] has a collision. The C program records one witness pair per sum.
   Python re-verifies every pair with `Fraction`: distinct, hyperbolic, same sum, equal R.
3. Independent `Fraction` enumeration (full fibres, no hashing) for every S ≤ 700 gives:
   - the same classification;
   - the same triad count for every S, including 25,575 at 557.

   This independently certifies all 38 collision-free sums. The C certificates cover the collision sums.

**Method claims (as quoted by the lead).**

- *Scaling: "if d | S and d carries a collision, so does S".* This is exactly right. If (p, q, r) ≠ (p′, q′, r′)
  have sum d and equal R, then for k = S/d ≥ 1 the triads (kp, kq, kr) and (kp′, kq′, kr′):
  - have entries ≥ 2k ≥ 2 and keep their order;
  - are hyperbolic, since R/k ≤ R < 1;
  - have sum S and equal reciprocal sum R/k;
  - are distinct.

  No extra hypothesis is needed. A colliding d satisfies d ≥ 18 automatically. The script asserts that every
  covered sum indeed has a collision.
- *3962 covered by scaling, 783 remaining.* Define "covered" as having a proper divisor 18 ≤ d < S that carries a
  collision. Then:
  - **3962** sums are covered;
  - **821** are not covered. Of these, **783** carry a (primitive) collision and 38 are collision-free.

  So 3962 + 783 + 38 = 4783 = #[18, 4800]. The printed "783 remaining" is correct if "remaining" means
  "not covered by scaling and carrying a collision, so certified by a direct witness". It is not the number of
  uncovered sums, which is 821. The Method should say which is meant.
- *First pairs.* These are confirmed as the unique collision fibre at their sum:
  - S = 18: (2,8,8) ~ (3,3,12);
  - S = 20: (4,8,8) ~ (5,5,10);
  - S = 26: (4,10,12) ~ (5,6,15).

  Sums 18, 20 and 26 are the first three collision sums. The next are 31, 32 and 34.

**Wording.** The Proposition needs no change. The Method needs a change only if "remaining" is ambiguous in
the text: "…3962 sums are covered by scaling; for each of the remaining 821 sums except the 38 listed, an explicit
colliding pair (783 sums) is exhibited."

---

## TH.2. Sharpness wording: grade MINOR

**Inputs.**

- Theorem S3 (ST.8): Hölder exponent 1/k_a, given a localization radius.
- Prop. S3.2 (ST.9): (i) the double-order family; (ii) the witnesses q_s = ((z − a)ᵏ − sᵏ) g(z).
- Remark S3.3 (ST.10).
- The front end (ST.0–ST.2) and b₁ from PC.8.

I re-derived the front-end rows exactly from those definitions, with α₁ = −1/3 and α₂ = 1/15:

- R = −2H₋₁ + c;
- P₁ = 2H₋₁ + 12H₀ + c;
- P₃ = −18H₋₁ − 120H₀ − 360H₁ + c.

These match ST.2.

**(i) 1/k is sharp for arbitrary data at a k-fold order, k ≥ 2.**

- *Construction.* Take q_s = ((z − a)ᵏ − sᵏ) g(z), with g real monic of degree n − k, g(a) ≠ 0, a ≠ 0, g(0) ≠ 0.
  Its coefficients are polynomials in sᵏ, so e(q_s) − e(m) = O(sᵏ). The data I = (R, P₁, P₃, …):
  - the P's come from e by Newton's identities;
  - R = e_{n−1}/e_n, with e_n ≠ 0.
  So I(q_s) − I(m) = O(sᵏ), and through the linear map L also δ := ‖H(q_s) − H(m)‖_∞ ≤ C sᵏ.
  Directly: Σ_j (a + sωʲ)^e − k aᵉ keeps only the binomial terms with k | i, so it is O(sᵏ) for
  e = −1, 1, 3, …. This is checked for k ≤ 6.
- *Recovery.* For small s the matrix M(I(q_s)) is invertible (Lemma S2.1: det ∝ ∏(zᵢ + zⱼ)/e_n ≠ 0 near
  positive a). The recovery map therefore returns q_s itself, whose roots a + sωʲ lie at distance exactly s
  from a.
- *Conclusion.* The displacement satisfies d = s ≥ (δ/C)^{1/k}. No exponent > 1/k is possible, and Theorem S3
  gives 1/k. So **1/k is sharp for arbitrary (real-coefficient, hence real-data) vectors.** For complex data
  vectors this holds a fortiori.

**(ii) Data that are heat invariants of a real multiset.**

- *Double order, any n ≥ 2.* The family (a+s, a−s, c₃, …, c_n) has every invariant even and smooth in s, so
  δ ≤ Cs², while the orders move by s. So no exponent > 1/2 is possible. Theorem S3 with k = 2 gives 1/2.
  The exponent is **1/2 and sharp**.
  - For n = 2 the data are (R, P₁) only. The same family gives ΔP₁ = 0 and ΔR = 2s²/(a(a² − s²)).
  - So "all orders equal" with n = k = 2 is the double-order case, and the exponent is 1/2 there too.
- *All orders equal, n = k ≥ 3: upper bound d ≤ Cδ^{1/2}.*
  - Write the real multiset as a + dᵢ. Then
    (P₃ − 3a²P₁)(a + d) − (P₃ − 3a²P₁)(a) = Σ(3a dᵢ² + dᵢ³) = 2aΣdᵢ² + Σdᵢ²(a + dᵢ).
  - So **Σ(3a dᵢ² + dᵢ³) ≥ 2aΣdᵢ² holds termwise iff every dᵢ ≥ −a**, that is, all orders a + dᵢ ≥ 0.
  - Hence max|dᵢ|² ≤ Σdᵢ² ≤ |ΔP₃ − 3a²ΔP₁|/(2a).
  - By the front-end rows, ΔP₃ − 3a²ΔP₁ = (−18 − 6a²)ΔH₋₁ + (−120 − 36a²)ΔH₀ − 360ΔH₁. So
    |ΔP₃ − 3a²ΔP₁| ≤ (498 + 42a²)δ, and

    **max|dᵢ| ≤ ((498 + 42a²) δ / (2a))^{1/2}.**

  - This needs only H₋₁, H₀, H₁, which are available exactly when n ≥ 3.
  - Exact probes: 3000 real multisets near (a, …, a), n = 3..6, a ∈ {2, …, 12}, all dᵢ ≥ −a. The largest
    observed value of max|d|²/bound is 0.594, so there are no violations.
  - The hypothesis dᵢ ≥ −a is genuinely needed for the global form. A multiset near (3, …, 3) with one
    entry −6.902 violates the bound (in the script). Locally it is automatic, because Theorem S3 puts
    every root within O(δ^{1/n}) of a.
  - Remark S3.3 states the hypothesis as |dᵢ| ≤ a. That is sufficient; dᵢ ≥ −a is the sharp form.
- *Attainment.* For the family (a+s, a−s, a, …, a) I computed exactly, for n = 2..7:
  - ΔP₁ = 0;
  - ΔP₃ = 6as²;
  - ΔR = 2s²/(a(a² − s²));
  - every ΔP_{2r−1} is even in s and O(s²).

  So δ ≤ Cs² while d = s, and **1/2 is attained**.
- *1/k is not attained for k = n ≥ 3 with real data.* The bound gives d/δ^{1/k} ≤ Cδ^{1/2 − 1/k} → 0.

**(iii) The witnesses for k ≥ 3 are not real.** For k ≥ 3, ω = e^{2πi/k} is non-real, so a + sω is non-real for
s ≠ 0.

- If the data I(q_s) were H(m′) for some multiset m′ (real or not, with e_n ≠ 0), then e(m′) would solve the
  same linear system M(I)e = b(I).
- Since det M(I) ≠ 0 there, e(m′) = e(q_s), and m′ would be the root multiset of q_s, which is not real.
- Explicit instance, n = k = 3, a = 4, s = 1/10: (R, P₁, P₃) determine e uniquely, since RP₁ ≠ 1. The
  discriminant of q_s is −27/10⁶ < 0.
- For k = 2 the witness is real (a ± s), which is consistent with (ii).

**Which cases are not settled, and a remark.** As printed, the unsettled cases are real data at a k-fold order
with 3 ≤ k < n (mixed clusters). In my view these can be settled in the same way, giving exponent 1/2. The
sketch:

1. For each cluster a of multiplicity k_a, take the parameters p_j = Σ_{i∈a} dᵢʲ, j = 1..k_a. For each simple
   order, take its displacement ε.
2. Then ΔI = Aθ + O(s^{3} + |ε|²), where A is the confluent Jacobian of m ↦ (1/m, m, m³, …, m^{2n−3}).
3. det A ≠ 0 for distinct positive values. det[g(mᵢ)] for g = (−m⁻², 1, 3m², …) equals a constant times
   ∏mᵢ⁻² ∏_{i<j}(mⱼ² − mᵢ²). Dividing out the within-cluster factors leaves ∏(mᵢ + mⱼ)·(cross factors) ≠ 0.
   This is checked symbolically for the patterns (3,1), (2,2), (4,1), (3,2), (3,1,1), (2,1,1) and (5): every
   determinant is a product of powers of x, (x − y) and (x + y).
4. Hence p₂ = Σdᵢ² ≤ C(δ + s³ + |ε|²) and |ε| ≤ C(δ + s³). Since s → 0 by Theorem S3, s² = O(δ).
5. The family (a+s, a−s, a, …, others) attains the rate.

So for real orders the exponent appears to be 1/2 at **every** multiple order. This is a strengthening the
authors may adopt or ignore; the printed "not settled" is not false.

**Is the abstract sentence correct as worded?** "the exponent 1/k is sharp for arbitrary data, while for the
coefficients of real orders it is 1/2 when all the orders are equal."

- For n = k ≥ 3 it is **correct**, by (ii).
- For n = k = 2 it is **correct**: this is the double-order case.
- Defects (MINOR):
  - (a) It is literally wrong for n = 1, where the single order is simple and recovery is Lipschitz. It needs
    "n ≥ 2".
  - (b) It omits the double-order case with other orders present, which Theorem 1.4 states.
  - (c) It omits "sharp".
  - (d) "real orders" should be "positive real orders", or the global form needs dᵢ ≥ −a. Locally this is
    automatic.

**Required wording changes.**

- Abstract: "…the exponent 1/k is sharp for arbitrary data, while for the coefficients of positive real orders
  the sharp exponent is 1/2 at a double order and when all n ≥ 2 orders are equal."
- Theorem 1.4: "For data that are the heat invariants of positive real orders it is ½, and sharp, at a double
  order (any n), and at an order of multiplicity k = n ≥ 3, that is, when all the orders are equal."
- After Theorem 6.6: no change is needed. Optionally replace "other configurations are not settled" by the
  confluent-Jacobian argument above.
- Remark S3.3: write "for real dᵢ ≥ −a (in particular |dᵢ| ≤ a)".

---

## TH.3. Remark 6.8 addition: grade NONE

- "The argument applies verbatim to (a, …, a) with any n ≥ 3 entries." This is **true**: the identity and
  inequality are termwise and independent of n, and P₁, P₃ are in the data exactly when n ≥ 3.
- "δP₁ = 0, δP₃ = 6as², all other data changes O(s²)": **verified exactly** for n = 2..7 (ΔR = 2s²/(a(a² − s²))).
- "shows that ½ is attained": **true**.
- The composed sentence (the witnesses for k ≥ 3 have non-real roots, and their data are not the heat invariants
  of any real multiset): **true**. The proof is in (iii); it needs det M(I(q_s)) ≠ 0, which holds for small s
  under the G5 hypotheses a ≠ 0, g(0) ≠ 0, ∏(zᵢ + zⱼ) ≠ 0.

**Recommended (not required).** Carry the hypothesis "real dᵢ ≥ −a" (or "|dᵢ| ≤ a") explicitly into the remark
when it is extended to n ≥ 3, and the G5 hypotheses into Proposition 6.7(ii).
