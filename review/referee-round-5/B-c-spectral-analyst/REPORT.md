<!-- Saved verbatim by the main session from the final message of reviewer B-c: the harness refused the reviewer's own write. Text from the report's first heading on; the reviewer's preceding cover note was dropped. -->
# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

I found no mathematical error in Sections 2–6, and every constant of Table 3 reproduces from the printed formulas. The serious reservation is that load-bearing results are taken from an unrefereed companion manuscript; I recommend minor revision on that condition.

The harness refused to write `REPORT.md` ("Subagents should return findings as text"), so the complete report follows here. The scripts I used are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-5/B-c-spectral-analyst/scratch/code/` (mpmath, 25–50 digits):
- `consts.py`: Tables 2 and 3.
- `checks.py`: the remainders and the geometry.
- `tri.py`: the triangle check of Lemma 4.2.
- `more.py`: the last column of Table 6 and the scaling in ε.
- `scanB.py`, `scanB0.py`: the bound in Lemma 2.2.

The rendered pages are in `scratch/render/`.

Submitted to Annals of Global Analysis and Geometry. My remit is Sections 2–6, with emphasis on the constants of Theorem 6.2 and Table 3; I read Sections 7–8 only where they bear on these. I read the PDF and the rendered pages (110 dpi) of pp. 6, 7, 9–13.

## Summary

The paper proves an effective, signature-level analogue of the Buser–Courtois theorem. Let O be a closed orientable hyperbolic 2-orbifold with area at most A, systole at least ε and cone orders at most M. Then the first N eigenvalues, each known to within δ, determine the signature, and N and δ are explicit (Theorem 6.2).

The proof works at one small time t\*:
1. The cone and area terms of the Selberg trace formula have enveloping small-t expansions (Prop. 2.3).
2. The first heat invariant at which two admissible signatures differ is bounded below by an explicit rational (Lemma 3.3). Its index is at most min(⌊A/π⌋+4, M) (Theorem 3.2).
3. This gives a gap Γ(t) = ½γ\* t^{k\*−2} between the signature terms (Lemma 6.1).
4. The closed-geodesic term is pushed below the gap by a count of closed geodesics in terms of the diameter, together with a diameter bound in terms of (A, ε, M) (Section 4).
5. The tail beyond N is controlled by a Chebyshev-type count (Prop. 5.2).

Section 7 gives an a-posteriori version and runs it on ten computed spectra. Section 8 shows that the order bound cannot be dropped, using O(2,3,m), and leaves the systole question open.

Within my remit I found **no mathematical error**:
- I recomputed every entry of Tables 2 and 3, and the class-level N in Table 6, from the printed formulas. All agree to the printed digits.
- I re-derived every inequality on which t1, t2, t3, Γ\*, Λ, N and δ rest.
- I tested numerically the imported enveloping remainders and the imported bound B of Lemma 2.2; both pass.

The one serious reservation is structural (M1). Load-bearing inputs are stated without proof and taken from a companion manuscript submitted at the same time and not refereed:
- the heat trace formula;
- the closed-geodesic count and its constant;
- the enveloping remainders;
- above all, Theorem 3.2.

## Significance

The question is natural, and the paper is honest that its constants are astronomically pessimistic: N up to 3.8×10^30 and δ down to 10^−277 in Table 3. Its value is the following:
- **Effective and checkable.** Its pieces can be checked line by line, which a compactness argument cannot offer.
- **Integrality at the first difference.** Lemma 3.3 is clean, and it is the conceptual reason an explicit gap exists.
- **The order bound is necessary.** The O(2,3,m) construction shows this genuinely.
- **A usable test.** The same mechanism, run on data, gives a test that succeeds with 18–847 eigenvalues.

The tools are standard: the trace formula with a Gaussian test function, counting via Z(1/x), and a packing bound for the diameter. The novelty is in the assembly, the bookkeeping and Lemma 3.3. I consider this appropriate for AGAG, provided M1 is resolved.

## Correctness and what was recomputed

### Section 2

- **Theorem 2.1.** The normalisations of I, E_m and Hyp match the standard cocompact trace formula with elliptic terms (Hejhal; Iwaniec). g_t and ĝ_t are a correct Fourier pair.
- **Lemma 2.2, final bound.** I re-derived every step:
  - the two maxima, at x = 2√t and x = 6t, giving 2√t e^{−1/2} e^{9t/2};
  - 2 sinh(x/2) ≥ e^{x/2}(1−e^{−ℓ});
  - Σ e^{−2ℓ(γ)} ≤ 2∫ n e^{−2x} dx ≤ 2π e^{3 diam−ℓ}/Area.
- **Lemma 2.2, first bound B (imported).** I compared B with the largest value the count n_O(x) ≤ C e^x allows (Stieltjes integration).
  - Grid: ℓ ∈ [0.01, 10] and t/t_max ∈ (0, 1].
  - With the factor e^{−t/4}, the ratio of that value to B is at most 0.9999997.
  - Without e^{−t/4}, it is at most 0.99999999993.
  - So B is valid given the count, and is asymptotically sharp relative to it.
- **Monotonicity of B in ℓ.** The claim that B decreases in ℓ on the range is correct: there ℓ/(2t) ≥ 1/ℓ + 1, so the logarithmic derivative is negative.
- **α_k.** Recomputed α_0, …, α_4 = 1, −1/3, 1/15, −4/315, 1/315.
- **b_l(m) and the c_j.** I computed the Taylor coefficients φ_k(m) of Φ_m directly.
  - b_0(m) = (m²−1)/(12m), as in Lemma 5.1(ii).
  - d_2 = −1/12 for (0;4,4,4) against (0;3,4,6), as on p. 8.
  - For O(2,8,8) against O(3,3,12): d_2 = 0 and d_3 = 25/12, as on p. 13. This matches Lemma 3.3(ii): −(1/360)(1032−1782) = 25/12.
- **Prop. 2.3 (imported), numerical test.** E_m(t) was computed by quadrature at 30 digits.
  - For m ∈ {2,3,5,8,12}, t ∈ {0.002, 0.02, 0.1, 0.5} and K = 0..5: the sign is (−1)^K and the modulus is ≤ |b_K(m)| t^K in every case.
  - The same holds for (4π/Area)I(t), for t ∈ {0.01, …, 3}.
  - |b_K(m)| is strictly increasing in m for K ≤ 5 and m ≤ 14.
  - The index bookkeeping in (2) is right.

### Section 3

- **Lemma 3.3.** Correct, given Lemma 3.1, Theorem 3.2 and the triangular expansion:
  - Padding by 1 is harmless, since p_l(1) = 0 and ψ_k(1) = 0.
  - The ψ_{l+1} term reduces to P_{2l+1}.
  - The sign (−1)^l = (−1)^k is right.
  - In (i), c_1 = s/2 with s ∈ L^{−1}Z, which gives |d_1| ≥ 1/(2L).
- **a_l.** I computed a_0, …, a_11: 1/12, 1/360, 1/2520, 1/10080, 3.51e−5, 1.60e−5, 8.90e−6, 5.86e−6, 4.46e−6, 3.84e−6, 3.69e−6, 3.93e−6. The minimum over l ≤ 10 is a_10, which is γ\* in row 8 of Table 3.

### Section 4

- **(H1)–(H3).** Re-derived; correct.
- **Lemma 4.2.** Correct:
  - the defect is ≥ π/(abc);
  - |θ−α−β| ≤ π−π/M;
  - sin α sin β ≤ π²/(ab);
  - hence cosh d − 1 ≥ 2/(π² c M) ≥ 2/(π² M²).
  
  Over all hyperbolic triangles (π/a, π/b, πk/c) with a, b, c ≤ M ≤ 24, the true cosh d − 1 is at least 9.7 times this bound. So the bound is valid but loose.
- **Lemma 4.3.** Correct in both cases.
- **Theorem 4.4.** Correct:
  - the packing argument gives Δ < 4r0A/v0;
  - cosh ρ1 − 1 ≥ (cosh r0 − 1) sin²(π/M) holds;
  - arccosh(1+x) ≥ √(2x/(1+x)) holds on [10^−10, 10^2];
  - d0 ≥ min(ε/2, 0.6/M), using 0.621 ≥ 0.6;
  - D ≤ closed form on a grid of A, ε and M.
- **Table 2.** All 12 entries reproduced: 56.60, 1125.4, 6.368e5; 150.94, 3001.2, 1.698e6; 639.97, 3184.1, 1.698e6; 1132.0, 22509, 1.274e7. The claimed M³ growth holds: the ratio for M = 100 against M = 12 is 566, against (100/12)³ = 579.

### Section 5

- **Lemma 5.1(i).** The case analysis is correct: s ≥ 1/42 and n + 4g ≤ Area/π + 4.
- **Lemma 5.1(ii).** Correct.
- **Prop. 5.2.** Correct, including the index bookkeeping (indices start at 0).

### Section 6

- **Lemma 6.1.** Correct.
- **Theorem 6.2.** Every step re-derived:
  - 63 = 21 × 3, valid since t2 < ε/2.
  - B\* is increasing on (0, t2], since t2 < ε²/2.
  - The reduction of B\* ≤ Γ/8 gives exactly the printed y0, including the term p log(4/ε²).
  - Λt\* ≥ 1, since 8Z♯/Γ\* ≥ 64.
  - Tail ≤ Γ\*/8 and perturbation ≤ Γ\*/(8e), so the total error is < 3/8 of Γ\* against a margin of 5/8. With G_σ known only to Γ\*/16, the comparison is still 7/16 against 9/16.
- **Hypotheses against use.** Each hypothesis is used, and only as stated:
  - area ≤ A gives n\*, Q, Z♯ and D;
  - systole ≥ ε gives the monotonicity of B, t2 and D;
  - orders ≤ M give k\* ≤ M, L_M, |b_K(M)|, b_0(M) and D;
  - the universal bound Area ≥ π/21 gives ϖ.
  
  No unstated hypothesis is used.
- **Table 3.** All 8 rows × 10 columns agree to the printed digits, including the binding constraint. t2 ≥ 0.00455 never binds. For example:
  - row 4: t1 = 9.32e−4, t3 = 1.29e−4, Γ\* = 1.78e−7, Λ = 4.07e5, N = 3.69e5, δ = 1.73e−10;
  - row 8: t1 = 2.5e−27, Γ\* = 1.77e−272, Λ = 5.52e29, N = 3.75e30, δ = 8.65e−278.
- **Text claims checked.**
  - "About 4×10^18 at A = 10π": with k\* = 14 I get 4.19e18. Confirmed.
  - The last column of Table 6: all 18 values reproduced.
  - t3 ≈ ε²/(24D): confirmed.
  - |b_K| ≈ K!(M/π)^{2K}: the ratio drifts from 0.33 to 0.11 for M = 12, K ≤ 10, so "roughly" is fair.
  - The scaling claim in ε is not accurate as worded; see m4.

## MAJOR issues

**M1 (gap in verifiability; no error found). pp. 4–7, Table 1, Sections 2–3.** The main theorem rests on results that are stated without proof and imported from the simultaneously submitted, unrefereed companion [20]:
- Theorem 2.1;
- the first bound of Lemma 2.2 and the count n_O(x) ≤ π e^{x+3 diam}/Area;
- the positivity and monotonicity of φ_k and of |b_K(m)|;
- Prop. 2.3;
- the triangular expansion;
- Lemma 3.1;
- Theorem 3.2.

Theorem 3.2(ii) is the most load-bearing. It is what gives k\* = min(n\*, M), and the text itself shows that this changes N by 11 orders of magnitude at A = 10π. Theorem 3.2(i) fixes n\*, and Prop. 2.3 is what makes Lemma 6.1 work at all.

My tests support Prop. 2.3 and B. I cannot certify Lemma 3.1 or Theorem 3.2, which are algebraic statements about power sums of padded multisets of orders. The proof of the main theorem is correct exactly when these statements are, and the editor currently has no way to check them.

## MINOR issues

- **m1 (exposition), p. 5, after Thm 2.1.** "Standard approximation argument": no approximation is needed. ĝ_t is even, entire and decays fast in every strip, so it is directly admissible for Hejhal [22] or Iwaniec [23]. Cite the theorem number, and say in one line why the series converge absolutely (the count of Lemma 2.2 suffices).

- **m2 (exposition), p. 6, Lemma 2.2.** The constant in n_O(x) ≤ π e^{x+3 diam}/Area enters through e^{3D}, so please give the one-line reason: a non-elliptic base point, and a ball of radius x + 3 diam. My test shows B is asymptotically sharp relative to this count, so no slack is available anywhere in it.

- **m3 (gap in exposition), p. 12, after Thm 6.2: "computable in exact rational arithmetic".**
  - (a) t\* is not rational. The proof uses t\* only through t\* ≤ t1, t2, t3, so any rational t ≤ min(t1, t2, t3) works, with Γ\*, Λ, N and δ defined from it. Say so.
  - (b) The existence of K with t\*^K Q(K) ≤ Γ\*/16 is asserted, not shown. Q(K) grows factorially, and t ≤ t1 does not directly give t\*Q(k\*−1) ≤ γ\*/32. Prove existence, add a constraint, or use validated quadrature.

- **m4 (inaccurate statement), p. 13.** "N grows by a factor of about 9 per halving of ε in the range of the table, tending to 8." I recomputed this for A = 4π/3, M = 3:
  - The first halving from ε = 0.694 gives a factor of 5.46, because D does not depend on ε while ε/2 > arccosh(1 + 2/(9π²)) ≈ 0.212.
  - After that the factors are 9.01, 8.92, 8.85, …, reaching 8.50 at ε ≈ 3.4e−4.
  
  Reword, for example "below ε ≈ 0.42 (M = 3), by about 9, decreasing slowly towards 8".

- **m5 (exposition), p. 12, proof of Thm 6.2.** Justify the step "B decreasing in ℓ on the range". t ≤ t2 ≤ ℓ'²/(2(1+ℓ')) holds for every ℓ' ∈ [ε, ℓ(O)], because ℓ²/(2(1+ℓ)) is increasing in ℓ.

- **m6 (exposition), p. 11, Lemma 5.1(ii).** E_m > 0 is immediate from the positive integrand; Prop. 2.3 is not needed for it.

- **m7 (suggestion; constants only), Lemma 6.1.** The uniform gap ½γ\* t^{k\*−2} is wasteful. When the areas differ (k = 1) the gap is of order t^{−1}, and δ_1 = 1/(2L_M) sets γ\* in rows 2 and 5. Per-k thresholds would improve the constants. A one-sentence remark is enough.

- **m8 (suggestion; constants only), p. 12, perturbation step.** The inequality |e^{−at} − e^{−bt}| ≤ t|a−b|e^{−min(a,b)t}, with Σ e^{−(λ_j−δ)t} ≤ e^{δt}Z♯(t), replaces N by about Z♯(t\*). That gains a factor of about 2e log(8Z♯/Γ\*), of order 10²–10³. Optional.

- **m9 (remark), p. 9, Lemma 4.2.** The bound on d0 is loose by a factor of 10–25 on triangle configurations. Note this next to the existing remark that the rates in M are artefacts.

- **m10 (wording), p. 2, Theorem 1.1.** "An explicit function G_σ … at an explicit time t\*" is vague for a main theorem. Name G_σ (Section 2.1) and t\* (Theorem 6.2) by reference.

- **m11 (exposition), p. 12.** The completeness caveat ("first N eigenvalues, with multiplicity; a missed eigenvalue shifts every later index") belongs in the statement of Theorem 1.1 as an explicit hypothesis.

## Presentation

- **P1. Fig. 1 (p. 13).**
  - There is no legend; the curves are identified only in the text, and the two dotted curves cannot be told apart in the figure.
  - The y-axis label describes only the grey curves.
  - Specify the diameter bound used for the dashed curve.
  - The caption's criterion omits the perturbation term. It is negligible here, but say so.
- **P2. Notation clashes.**
  - Γ is both the Fuchsian group and the gap function Γ(t), Γ\*.
  - A is both the class bound and the common area in Theorem 3.2(i) and Lemma 3.3(ii). Lemma 6.1 silently uses monotonicity in the area, so rename the common area.
  - δ clashes with δ_k.
  - ε clashes with ϵ_j.
  - L_M and L_{σσ'} clash with L, the number of invariants.
- **P3. Table 3 caption.** State that ε is the rounded systole of the named examples, and that D is D(A, ε, M), not 2 diam P.
- **P4. Placement.** The correct remarks "t3 binds in rows 4, 6, 7" (p. 10) and "t2 never binds" (p. 12) should sit together, next to Table 3.
- **P5. p. 6.** Add half a sentence that Φ_m is even by pairing j with m−j.
- **P6. Rendered formulas.** Pages 6, 7 and 9–13 are typographically clean. I found no sign errors: d_2 = −1/12, d_3 = +25/12, the signs in Prop. 2.3 and X in (H3) are all confirmed independently.

## Recommendation

**Minor revision**, conditional on M1 being resolved, that is, on the companion results being verifiable.

- **Confidence is high** for Sections 4–6 and all constants (Tables 2 and 3 and the last column of Table 6 recomputed exactly).
- **Confidence is moderate** for Sections 2–3. The imported analytic statements pass my numerical tests, but I could not verify the algebraic Lemma 3.1 and Theorem 3.2.

If the companion is unavailable or fails review, the recommendation becomes **major revision**, since the proof of the main theorem would then be incomplete.

## What resolves each issue

- **M1:** do one of the following:
  - Make [20] available as an arXiv preprint with stable numbering.
  - Or give proofs or literature references for Prop. 2.3, Lemma 3.1 and Theorem 3.2.
  
  At a minimum, mark in Table 1 which imported statement feeds which constant: Theorem 3.2(i) → n\*, Theorem 3.2(ii) → k\*, Prop. 2.3 → t1, Lemma 2.2 → t2, t3, ϖ.
- **m1:** cite the admissibility conditions directly.
- **m2:** add the one-line derivation of the count.
- **m3:** allow a rational t ≤ min(t1, t2, t3); prove that the truncation order K exists, or add a constraint, or use validated quadrature.
- **m4:** reword using the recomputed factors (5.5, then about 9, decreasing towards 8).
- **m5, m6:** add one sentence each.
- **m7, m8, m9:** optional remarks.
- **m10, m11:** sharpen the statement of Theorem 1.1.
- **P1–P5:** add a legend and labels to Fig. 1, rename the clashing symbols, complete the Table 3 caption, and add the evenness remark.
