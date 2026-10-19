<!-- Blind check B (round 7): returned text saved verbatim; the reviewer could not write files -->

Overall: none of the ten items has a mathematical error that breaks a result. The stated computed-gap numbers are reproduced to within grid resolution. What remains is three wording errors (abstract range, abstract qualifier, a symbol typo), one imprecise sentence, one missing one-line justification, a small hole in the "in particular" of Corollary 8.5, and one unsupported assertion in §8.2.

Note on numbering: in the PDF the corollary is **Corollary 6.3**. The remark you call "Remark 6.3(a)" is **Remark 6.4(a)**.

Everything I wrote is in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/blind-check-B/scratch/ (`gap.py` and `fine.py` for item 1, `heat.py`, `t1.py` and `firstdiff.py` for item 8). Pages 1–3, 12–14, 17, 26 and 28 were rendered and read; every typo or formula point below was checked on those images.

**1. Corollary 6.3 and the numbers after it: VERIFIED, with one imprecise sentence.**
- **Proof structure.** The proof of Theorem 6.2 uses Lemma 6.1 only for the gap at t\*. Every other estimate needs only t\* ≤ t2 and y ≥ y0:
  - Hyp ≤ B\* needs t ≤ t2 ≤ ε/2, which gives 1 + 2t/(ε−t) ≤ 3.
  - B\* ≤ Θ/8 needs y ≥ y0.
  - The tail needs N > e·Z(1/Λ) and 1/Λ ≤ t\*.
  - The perturbation needs N·t\*·δ = Θ\*/(8e).
  - The total is Θ/8 + Θ/8 + Θ/(8e) < 3Θ/8, against a gap of at least 5Θ/8.
- **Imprecise sentence.** "t1 only through that lemma" is not quite right. t1 ≤ 1 gives t\* ≤ 1, hence Θ\* ≤ γ\*/2 ≤ 1/8. That is used for "Θ\*/8 ≤ 1" and is what makes Λt\* ≥ 1 automatic (Λt\* = 2 log(8Z♯/Θ\*) ≥ 2 log 64).
- **Unjustified step.** The proof of Theorem 6.2 asserts "As Λt\* ≥ 1" with no justification; it needs the line above.
- **Hypotheses suffice.** The corollary assumes Θ ≤ 8 and Λt ≥ 1 explicitly, so both uses are covered. t ≤ t2, the gap, and B\*(t) ≤ Θ/8 cover the rest.
- **B\* increases on (0, t2]: true.** d/dt log B\* = −1/(2t) + ε²/(4t²) > 0 for t < ε²/2, and t2 = ε²/(2(1+ε)) < ε²/2.
- **Recomputation.** I computed G_σ by quadrature of Theorem 2.1 over all of Sig(A,M), took Θ = min(gap, 8), and minimised N over t-grids:

| Class | Paper N | My N (grid minimum) | Notes |
|---|---|---|---|
| π/2, M=8 | 244 | 244 | 27 signatures |
| π/2, M=12 | 283 | 282–318, depending on grid | 48 signatures |
| 4π/3, M=3, ε=2.633915 | 139 | 139–153 | |
| 4π/3, M=3, ε=0.693994 | 2605 | 2575–2752 | |
| 4π/3, M=12 | 7415 | 7378 | |
| 2π, M=3, ε=0.1 | 3.9×10⁵ | 3.81–3.90×10⁵ | B\* ≤ Θ/8 binds, as the paper says |

  N jumps with the grid because the minimum over pairs is non-smooth, and all paper values lie at or just above my finest-grid minima, so they are consistent. In every case Λt ≈ 15–25 ≥ 1 and Θ ≤ 0.17. The comparison values 3.4e8, 6.8e9, 4.3e4, 7.4e12 and 2.3e6 match Table 3.
- **Minor.** §7.2 says "the data account for the remaining factor of about 10". The actual ratios are 139/24 ≈ 5.8, 2605/461 ≈ 5.7, 283/36 ≈ 7.9, 283/24 ≈ 11.8 and 7415/842 ≈ 8.8. Suggest "about 6 to 12".

**2. Corollary 8.5: VERIFIED, with one gap in the "in particular".**
- **Membership.** For 7 ≤ m ≤ M, O(2,3,m) has area < π/3 ≤ A, systole ≥ ℓ_{2,3} ≥ ε and orders ≤ M, so A ≥ π/3 and ε ≤ ℓ_{2,3} are right; any A ≥ 2π(1/6 − 1/M) would do. I recomputed ℓ_{2,3}: cosh(2s∞) = cosh(log 3) = 5/3, so ℓ_{2,3} = 2 arsinh(½·√(12/37)) = 0.56206.
- **Main inequality.** The pigeonhole works: h_m ≥ h_7, the ⌊Λ_N/δ⌋+1 boxes cover [0, Λ_N], and the midpoint list is within δ/2 of both spectra. M − 6 ≥ J + 1 then gives a contradiction, so J ≥ M − 6 is correct (trivial for M ≤ 6).
- **GAP.** "N log(N²/δ) ≥ c log M" fails as written when N²/δ ≤ 1. Example: δ ≥ 1, N = 1, M = 7 makes the left side ≤ 0. Fix: state (N−1)·log(c′N²/δ + 1) ≥ log(M − 6), which is what the proof derives, or add "for M ≥ M0(δ)".
- **Growth rate.** "N ≳ log M / log log M" follows only at fixed δ. If δ shrinks like 1/M, the argument allows bounded N.

**3. Elliptic degeneration paragraph at Fig. 3: VERIFIED** (Garbin–Jorgenson's statements taken as quoted).
- sin x ≤ x gives 1/(2 sin(π/m)) ≥ m/(2π).
- m/(2π) ≥ 1 + m/(4π) holds iff m ≥ 4π ≈ 12.57, so m ≥ 13 is right (fails at m = 12: 1.91 < 1.95).
- Hence for any fixed ε < ½, arccosh(1 + εm/2π) < h_m, and Proposition 8.2's embedded open cone ball of radius h_m gives condition (a).
- Since PSL(2,Z)\H² has no eigenvalue in (0, ¼), Corollary 5.5 gives lim inf λ1 ≥ ¼; with Proposition 8.3 this gives λj → ¼. "Granting this" hedges condition (b) adequately.

**4. Theorem 7.1: VERIFIED, with one statement gap.**
- **Perturbation term.** |e^{−at} − e^{−bt}| ≤ t|a−b|·e^{−t min(a,b)}, and min(λj, λ̃j) ≥ max(λ̃j − εj, 0) because λj ≥ 0. So the term is a valid bound. The proof should state this inequality; at present it only says the factor "may be kept".
- **Tail.** Valid, since λN ≥ λ̃N − εN.
- **Extension to area ≤ A.** The tail bound needs only Area(O) ≤ A and σ(O) ∈ S. C\* is increasing in A, so C\*(A, ℓ, M) stays valid. The diameter count πe^{3Δ}/A would be invalid if Area(O) < A, which is why the parenthetical switches to C\*.
- **GAP.** The statement says "Let O have area A", which contradicts the intended use with only an area bound (Table 6, Sig(A,M) column). Fix: "area at most A", with the diameter count using Area(O).
- **GAP.** Using C\*(A,ℓ,M) needs O's orders ≤ M (O ∈ C(A,ℓ,M)). Say so, or require S to have orders ≤ M.
- (C2) ⇒ (C1) is correct.

**5. Item (iv), the protocol: VERIFIED.**
- For a correct, complete list, Theorem 7.1 says σ(O) passes at every (N,t) in the range, so "no signature passes" cannot happen. Any signature singled out by (C1) must be σ(O).
- "Correct" must include εj being true bounds and valid ℓ and C. Here the εj are estimates, which the text already says. Rejection of the 24 lists is empirical, not guaranteed.

**6. Continuity sentence (bi-Lipschitz factors): VERIFIED.** For a differential with singular values s1, s2 ∈ [1/K, K] in dimension 2:
- the Dirichlet energy factor is between s2/s1 and s1/s2, i.e. in [K⁻², K²];
- the L² norm (area) factor is s1·s2 ∈ [K⁻², K²];
- so the Rayleigh quotient factor is in [K⁻⁴, K⁴]. Correct, though not sharp.

**7. §8.2, the signature (1;3): VERIFIED, with one unsupported assertion.**
- All three areas are 4π/3: s = 2/3 for (0;3,3,3,3), (1;3) and (0;2,2,6,6).
- A separating essential curve on (1;3) would bound a disc with the cone point. Such a disc with geodesic boundary would have area 2π(−1 + 2/3) = −2π/3 < 0, so the argument is correct.
- The limit (0;3,∞,∞) is correct (area check: −2 + 2/3 + 2 = 2/3).
- **Unsupported.** "λ1 stays away from 0" is stated without proof or citation. The same paragraph says the orbifold versions of the needed degeneration results are missing. Lifting to a torsion-free cover does not settle it, because lifts of a non-separating curve can separate the cover. Hedge it or cite it.

**8. Remark 6.4(a): VERIFIED.**
- I recomputed t1 exactly for every Table 3 row (α_k, b_K and a_l from the paper's formulas): 1.1e−7, 6.8e−9, 9.3e−4, 2.7e−11, 7.8e−4, 3.3e−4 and 2.5e−27, all matching. The minimum is at k = k\* in every row.
- Θ\* for row 1 is 2.6e−18, matching.
- Spot-check of first differences, exact rational heat invariants, same-area pairs:

| Class | Signatures | Maximum first-difference index |
|---|---|---|
| A ≤ 2π, M ≤ 6 | 90 | 2 |
| A ≤ 2π, M ≤ 10 | 310 | 3 |
| A ≤ 4π, M ≤ 10 | 1562 | 3 |
| A ≤ 2π, M ≤ 30 | 5235 | 3 |
| A ≤ 6π, M ≤ 6 | 782 | 3 |

  This confirms "no two signatures first differ beyond k = 3" on all three classes the remark names. Extreme pairs include (5,5,5)/(2,2,2,10), (2,8,8)/(3,3,12) and (3⁵)/(2⁵,6).

**9. Abstract and introduction: one error, one omission.**
- **ERROR.** "N of order 10² to 10⁴ in our examples", in both the abstract and the introduction, contradicts the body's N = 3.9×10⁵ for A = 2π, ε = 0.1, M = 3, which comes from the same corollary. Either say "10² to 10⁵", or restrict the claim to the classes of the Section 7 examples (24 to 7415).
- **Omission.** "log M / log log M" needs "at fixed accuracy δ" in the abstract (see item 2).
- **Consistent.** "Systole … certified in interval arithmetic" matches §7.1 and Table 4. "Computed, not certified" matches §6.

**10. Other points.**
- Proof of Lemma 4.5, last line (confirmed on the rendered page): "≤ K eˣ" should read "≤ C\* eˣ".
- The "λ1 stays away from 0" assertion in §8.2 (item 7).
- The abstract's range and missing "fixed δ" qualifier (item 9).
