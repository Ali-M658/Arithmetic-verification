<!-- Round 10, B-b, returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

The write to REPORT.md was refused (subagents may not write report files), so the full report is below.

# Referee report: Sections 2, 3 and Appendix A

**Manuscript:** "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (submitted to AGAG; 41 pp.)
**Referee remit:** Sections 2 (pp. 7–9) and 3 (pp. 9–10), and Appendix A (pp. 34–37). I checked every proof in these parts line by line and recomputed every number I could. I did not referee Sections 4–8, except where they use Sections 2–3 (Lemma 6.1, Table 3). I treated the marked placeholders (author contributions, AI-use statement, Zenodo DOIs, preprint identifiers) as known.

## Summary

Sections 2–3 and Appendix A provide the analytic and algebraic input for the main theorem:

- **Theorem 2.1:** the Selberg trace formula for the heat function on a cocompact Fuchsian group with elliptic elements. Lemma A.1 justifies it by approximating with compactly supported test functions.
- **Lemma 2.2:** (i) a diameter-based count of closed geodesics; (ii) explicit bounds on the hyperbolic term Hyp(t), assuming n_O(x) ≤ Ce^x.
- **Proposition 2.3:** remainders for the small-t expansions of the elliptic terms E_m(t) and the identity term I(t). These remainders have a definite sign and are bounded by the first omitted term, **for every t > 0**. This gives the heat invariants (1) and the remainder bound (2).
- **Lemmas A.2–A.3:** the "cone polynomials" p_l. They are even, have rational coefficients, have degree 2l + 2 with an explicit leading coefficient, and expand triangularly in ψ_k(x) = x^{2k−1} − x^{−1}.
- **Section 3:**
  - Lemma 3.1 characterises equality of c_1, …, c_L through power sums of the padded order multisets.
  - Theorem 3.2 bounds the index of the first differing invariant: (i) by ⌊A/π⌋ + 4, via a parity/Newton-identity argument; (ii) by M, via a Vandermonde argument.
  - Lemma 3.3 (new here) shows that the first difference is an integer multiple of an explicit rational, which gives the gap used in Lemma 6.1.

## Significance (of the parts under review)

The material is a careful, explicit re-derivation of the constant-curvature orbisurface heat invariants, plus the quantitative information that an effective theorem needs: remainders valid at all t > 0, and integrality at the first difference.

- **What is new and useful:** Proposition 2.3, Lemma 3.3 and, unless it already appears in Uçar or [4], the parity argument of Theorem 3.2(i). They are clean and elementary, and suited to effective work.
- **What is not new:** the coefficients themselves. I checked that the cone contributions b_l(m) in (1) coincide **exactly** with Uçar's closed form ([2], arXiv:1711.03405, eqs. (4.25), (4.33)–(4.34) at κ = −1) for l = 0, …, 5. For example:
  - b_1(m) = −(m²−1)(m²+11)/(360m);
  - b_2(m) = (m²−1)(2m⁴+9m²+37)/(5040m).

  The α_k are Uçar's (4.35). Theorem 3.2(ii) is a short Vandermonde consequence of the triangular structure that drives Uçar's induction.
- **Overall:** the significance of Sections 2–3 rests on the effective remainders and on Lemma 3.3, not on the expansion. The text should say so plainly (M1).

## Correctness and what I recomputed

**Verdict on the parts under review: I found no mathematical error.** Every proof in Sections 2–3 and Appendix A is correct as written, up to the presentational gaps listed under MINOR and Presentation. In detail:

### Theorem 2.1 / Lemma A.1 (pp. 7, 34–35)

- **Normalisation.** I compared it with Dryden–Strohmaier [1, eq. (1)] (fetched from arXiv:math/0504571) and Garbin–Jorgenson [17, Rem. 2.7, (2.8)] (arXiv:1603.01495). The identity, hyperbolic (ℓ(γ₀)g(ℓ)/2 sinh(ℓ/2), classes γ and γ⁻¹ counted separately) and elliptic (1/(2m sin(πj/m)) ∫ e^{−2πjr/m}/(1+e^{−2πr}) ĝ) terms all agree.
- **E_m(0+) = (m²−1)/(12m).** Checked via Σ csc²(πj/m) = (m²−1)/3. Numerically, E_5(10⁻⁴) = 0.39995 against b_0(5) = 0.4.
- **Lemma A.1, eigenvalue count.**
  - η_T = ĝ for g = 2cos(Tu)(ψ*ψ), with support in [−2ϵ, 2ϵ], so Hyp vanishes.
  - η_T ≥ 1/4 on |r−T| ≤ 1, which gives #{λ_j ≤ x} = O(x).
  - The imaginary r_j are handled through |ψ̂(is ± T)| ≤ e^{ϵ/2}.
- **Lemma A.1, convergence.** The domination uses Lemma 2.2(i), which does not depend on the trace formula, so there is no circularity. The |f̂_X| ≤ ϵ_X min(1, |r|⁻³) argument and the Σ_j min(1, |r_j|⁻³) < ∞ step are correct.

### Lemma 2.2 (p. 8)

- **(i):** correct. The Dirichlet domain lies in B̄(x̃₀, diam), and choosing representatives is injective on conjugacy classes. The remark about classes coinciding with their inverses when Γ has order-2 elements is correct and welcome.
- **(ii), main bound.** I re-derived B_C line by line:
  - On the stated range, (log φ)′ < 0 for x ≥ ℓ. In fact t(2−ℓ) < ℓ² suffices.
  - The integration by parts against n_O, with the boundary term vanishing.
  - The identity x e^{x/2−x²/4t} = −(2tx/(x−t)) d/dx e^{x/2−x²/4t}.
  - The bound x/(x−t) ≤ ℓ/(ℓ−t).
- **(ii), monotonicity.** I expanded the logarithmic derivative of B_C in ℓ: 1/ℓ + 1/2 − ℓ/(2t) − e^{−ℓ}/(1−e^{−ℓ}) − 2t/(ℓ²−t²). This equals the expression printed, and the bracket is nonnegative exactly when t ≤ ℓ²/(2(1+ℓ)).
- **(ii), the all-t bound.** The factorisation is correct, with maxima at x = 2√t (value 2√t e^{−1/2}) and x = 6t (value e^{9t/2}). The prefactor is 2C e^{17t/4 − 1/2 − ℓ}/(√π(1−e^{−ℓ})).

### Section 2.2 and Lemma A.2 (pp. 8–9, 35)

- **Closed form.** Φ_m(u) = (cot u − m cot mu)/(4m sin u) is correct (cotangent partial-fraction identity; residues and limits at Im x → ±∞ checked).
- **Bernoulli expansion.** From (x/2)coth(x/2) at x = 2iu, the series is Σ 4ⁿ|B₂ₙ|(m²ⁿ−1)u^{2n−1}/(2n)!.
- **Numerical check.** I compared the formula for m φ_k(m) with the Taylor coefficients of Φ_m computed directly from the defining sum, for m = 2, 3, 5, 7 and k ≤ 4. Agreement is to 10⁻⁴⁰.

### Lemma A.3 (p. 36)

- **Exact recomputation of p_0, …, p_5.** All are even, have rational coefficients, satisfy p_l(1) = 0 and have degree 2l + 2.
- **Leading coefficients.** a_l = |B_{2l+2}|/(2(l+1)!(2l+1)) is confirmed: 1/12, 1/360, 1/2520, 1/10080, 1/28512, 691/43243200.
- **Triangular expansion in ψ_k.** Correct, using Σ_k a_{l,k} = 0.

### Proposition 2.3 (p. 9; proof pp. 35–36)

- **Moment step.** Euler's integral ∫ e^{−ar}/(1+e^{−2πr}) e^{sr} dr = [2 sin((a−s)/2)]⁻¹ and the moment identity Σ_j 𝔪_{2k}(2θ_j)/(2m sin θ_j) = (2k)! φ_k/4^k are correct. The decomposition of E_m − Σ_{l<K} b_l t^l into same-sign pieces is correct, and the moduli sum to exactly |b_K| t^K.
- **Part (b).** The μ_k formula is correct; I checked it by quadrature for k ≤ 3. The moment recursion for α_k equals the Bernoulli closed form for k ≤ 6 (exact rational arithmetic): 1, −1/3, 1/15, −4/315, 1/315, −4/3465, 382/675675. This also matches Uçar (4.35).
- **Numerical test of the enveloping claims.** I tested (a) and (b) with 30-digit quadrature at t ∈ {0.01, 0.05, 0.2, 0.5, 1, 2, 5}, K = 0, …, 5 and m ∈ {2, 3, 7, 12}. There were **no failures**: both the sign (−1)^K (cone), respectively (−1)^{K+1} (area), and the modulus bound hold in every case.
- **Monotonicity.** |b_K(m)| is strictly increasing in m for K ≤ 5 and 2 ≤ m ≤ 40.
- **Formulas (1) and (2):** the indices are consistent.

### Section 3 and Appendix A.3 (pp. 9–10, 36–37)

- **Paper proofs.**
  - Lemma 3.1 is correct, including the padding and d ∈ ℤ.
  - Lemma A.4 is correct: every partition of an odd j has an odd part.
  - Theorem 3.2(i) is correct, including |V*|−|U*| = 2(g−g′), the vanishing of e_{κ−1} via R(U*) = R(V*), and |U|+|V| = 2 max(n+g−g′, n′+g′−g) ≤ 2(⌊A/π⌋+4).
  - Theorem 3.2(ii) is correct: det(y_a^k − 1) is the Vandermonde determinant once the column y_1 = 1 is added.
  - Lemma 3.3 is correct.
- **Brute-force check.** I enumerated all hyperbolic signatures with area ≤ 2πS and orders ≤ M, for (S, M) = (1, 8), (2, 6), (2, 12), (4, 5): up to 2746 signatures and 8280 equal-area pairs. Using exact rational heat invariants from (1), I checked for every equal-area pair:
  - the first differing index satisfies k ≤ min(⌊A/π⌋+4, M);
  - d_k = (−1)^k a_{k−2}(P_{2k−3}(U) − P_{2k−3}(V)) holds exactly;
  - |d_k| ≥ a_{k−2}.

  For 20,000 random pairs of unequal area, |d_1| ≥ 1/(2L_{σσ′}) held. **There were no violations.**
- **Examples.** (0;4,4,4) against (0;3,4,6) gives d_2 = −1/12, as stated (p. 10). O(2,8,8) against O(3,3,12) share c_1 and c_2 (p. 6), and d_3 = 25/12, which agrees with the Lemma 3.3 formula.
- **Table 3.** I recomputed |Sig(A, M)| = 27, 48, 8, 281, 12 for the classes of Table 3 (p. 17). All agree.

The scripts are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/B-b-orbifold-trace-formula-analyst/scratch/code/ (sec2.py, env.py, sec3.py, ucar_cmp.py, kstar.py).

## FATAL

None in the parts under review.

## MAJOR

**M1. Overlap with, and dependence on, the unavailable companion [4]; the novelty of Sections 2–3 is not stated precisely (pp. 6–10, 34–37).**

- **Overlap.** By Table 1 (p. 7), Theorem 2.1, Lemma 2.2, the positivity of φ_k, Proposition 2.3, the cone polynomials, Lemma 3.1 and Theorem 3.2 are all results of [4]. Appendix A reproduces "the arguments … of [4]" (p. 34).
- **[4] cannot be inspected.** It was submitted at the same time and its identifier is a placeholder, so the editor and referees cannot judge the extent of the overlap. The two papers also depend on each other: [4] uses Lemma 4.5 and Section 7.1 of this paper (p. 6). Several headers attribute results proved here to [4] instead: "[4, Lemma B.1]" in Theorem 2.1, "[4, Prop. B.2]" in Proposition 2.3.
- **Relation to Uçar.** The coefficients in (1) are exactly Uçar's closed forms (verified for l ≤ 5; see above). The paper says only that the coefficients "are known in closed form [2, Thm 4.20]" (p. 5) and that the triangular expansion is "the mechanism of Uçar's induction" (p. 9). It never states that (1) agrees with Uçar.
- **Consequence.** As written, a reader cannot tell what in Sections 2–3 is (a) classical, (b) Uçar's, (c) in [4], and (d) new here.

**What resolves it:**

- Supply [4] to the editor as a confidential supplement.
- State, result by result, which paper is the primary home of each shared statement.
- Replace the "[4, …]" attributions in theorem headers by the internal proofs, with a single pointer to [4].
- Add one sentence noting that (1) coincides with Uçar's formulas (4.33)–(4.35) at κ = −1 (cone point of order m, curvature −1).
- Say explicitly that the new content here is the all-t enveloping remainder (Prop. 2.3), Lemma 3.3 and, if it is not in [4], Theorem 3.2(i).

**M2. Lemma 3.3 is used in Theorem 6.2 with worst-case data that the paper's own finite enumeration shows are far from attained (pp. 10, 14).**

Lemma 6.1 uses the first-difference index k* = min(⌊A/π⌋+4, M) and the lower bounds δ_1 = 1/(2 min(L_M, M^{2n*})) and δ_k = a_{k−2}. Through Θ(t) = ½γ* t^{k*−2} and t_1, these drive the "enormous" constants of Table 5.

For every class of Table 3, I computed the true first-difference index and the true least |d_k| over Sig(A, M). This is the same enumeration the authors already do for Proposition 6.5.

| Class (A, M) | k* | True max first-difference k | Least \|d_1\| | δ_1 |
|---|---|---|---|---|
| (π/2, 8) | 4 | 2 | 1.19e−3 | 5.95e−4 |
| (π/2, 12) | 4 | 3 | 3.79e−4 | 1.80e−5 |
| (4π/3, 3) | 3 | 2 | | |
| (4π/3, 12) | 5 | 3 | 1.80e−4 | 1.80e−5 |
| (2π, 3) | 3 | 2 | | |

Substituting the exact data into the paper's own formulas for t_1 and Θ(t_1) changes them as follows:

| Class (A, M) | t_1 (paper) | t_1 (exact data) | Θ(t_1) (paper) | Θ(t_1) (exact data) |
|---|---|---|---|---|
| (π/2, 12) | 6.8e−9 | 2.4e−5 | 4e−22 | 4e−9 |
| (4π/3, 12) | 2.7e−11 | 8.9e−6 | 2e−37 | 8e−10 |
| (π/2, 8) | 1.1e−7 | 1.1e−4 | 3e−18 | 6e−4 |

This is not an error. But the paper attributes the size of the constants of Theorem 6.2 to "heat invariants … valid only at very small times" (pp. 1, 3). A large part of the size is instead an artefact of the crude a-priori k* and γ*.

**What resolves it:** state a class-exact variant of Lemma 6.1 / Theorem 6.2. Replace k* and γ* by the exact maximum first-difference index and the exact least |d_k| over the finite set Sig(A, M), which are computable exactly in rational arithmetic from (1). Report the resulting closed-form N and δ next to Table 5. This would sit naturally between Theorem 6.2 and Proposition 6.5 and makes better use of Lemma 3.3. Alternatively, qualify the explanation of the size of the constants.

## MINOR

- **m1 (p. 9, eq. (2)).** By Proposition 2.3 the area remainder has sign (−1)^{K+1} and every cone remainder has sign (−1)^K. The two therefore partly cancel, and (2) holds with the sum replaced by the maximum: |G_σ − Σ| ≤ t^K max{(Area/4π)|α_{K+1}|, Σ_i |b_K(m_i)|}. This improves Q(K) in Section 6 by up to a factor 2 at no cost. State it, or remark on why the weaker form is kept.
- **m2 (pp. 7, 34–35, Lemma A.1).** The approximation argument is correct but unnecessary. Two sources already give the heat function directly:
  - Hejhal [34] and Iwaniec [35, Thm 10.2] admit test functions h even and holomorphic in |Im r| ≤ ½ + ε with h(r) ≪ (1+|r|)^{−2−ε}, which covers h = e^{−t(1/4+r²)}.
  - Garbin–Jorgenson [17, (2.7)–(2.8)] state exactly the heat-trace identity of Theorem 2.1 for compact orbisurfaces.

  Either cite these and drop Lemma A.1, or say that it is included only for self-containedness. "Classical" is then accurate without the reduction.
- **m3 (p. 36, proof of Prop. 2.3(b)).** The step from the moment recursion for α_k to the Bernoulli-polynomial closed form of p. 9 is asserted ("following from …") but not derived. I confirmed it for k ≤ 6 only. Give the generating-function argument, or cite Uçar [2, (4.35)], where exactly this formula appears. Note that only the moment form is used in proofs.
- **m4 (p. 37, end of Theorem 3.2(i)).** Make the final contradiction explicit: 2L + 2 ≤ κ ≤ |U| + |V| ≤ 2⌊A/π⌋ + 8. Also state the two facts used: n + g − g′ ≤ n + 4g needs g′ ≥ 0 and g ≥ 0, and passing to ⌊A/π⌋ uses integrality.
- **m5 (p. 10, Lemma 3.3(i)).** State the convention L_{σσ′} = 1 when neither signature has cone points.
- **m6 (pp. 9–10).** Theorem 3.2(i) is never close to sharp in the computed range: across all classes I enumerated, the first difference never occurs beyond k = 3. A sentence to this effect, perhaps with the observed maximum, would inform the reader. This is related to M2.
- **m7 (p. 9).** "[2, Thm 3.40]" is Uçar's theorem for polygons. The orbisurface statement is [2, Cor. 4.21(iv)], and the cone coefficients are [2, (4.33)–(4.34)]. Cite those.

## Presentation

- **P1 (pp. 7–10, 34–37): symbol overloads.** Each of these causes real friction when checking proofs:
  - ε (the systole bound) against ϵ (the support radius in Lemma A.1, ϵ_X, and the error budgets ϵ_j).
  - ℓ (systole, lengths, and the free lower bound in Lemma 2.2(ii)) against l (the index of b_l and p_l).
  - L (the number of invariants in H_L and Lemma 3.1) against L_{σσ′} and L_M (lcm's).
  - φ (the auxiliary function in the proof of Lemma 2.2) against ϕ_k(m) against ϕ (an angle in Lemma 4.1).
  - A (the area of the given signature in Theorem 3.2(i) and Lemma 3.3(ii)) against A (the class bound).
  - x (the polynomial variable) against x (the Taylor variable in the proof of Prop. 2.3).
  - K (the remainder order) against K (bi-Lipschitz, p. 3) against K (replaced entries, Remark 6.3).
- **P2 (p. 9).** The coefficients a_{l,k} appear in Section 2 before they are defined; they are defined only in Lemma A.3. Define them where they are first used.
- **P3 (pp. 7, 9).** Theorem 2.1's header cites "[4, Lemma B.1]" and Proposition 2.3's cites "[4, Prop. B.2]". Cite the internal Lemma A.1 and the proof in A.2 (see M1).
- **P4 (p. 8).** In Lemma 2.2(ii), add a sentence that the range t ≤ ℓ²/(2(1+ℓ)) is chosen for the monotonicity of B_C. For the bound itself, t(2−ℓ) < ℓ² suffices.
- **P5 (p. 36).** In the A.3 preamble, "for finite multisets m, m′ of positive reals" silently extends b_l to non-integer arguments through p_l. Say so.

I read the rendered pages 7–10 and 34–37. I found no typographical, sign or formula errors in the displayed mathematics. In particular, Proposition 2.3(b) correctly has 4π/Area, and α_2 = 1/15 is printed correctly. The text-extraction artefacts I first saw were not present in the PDF.

## Recommendation

**Minor revision**, as far as Sections 2, 3 and Appendix A are concerned. Confidence is high for these sections; I have not refereed Sections 4–8.

The mathematics in my remit is correct, carefully written and independently confirmed: exact symbolic checks, 30-digit numerical tests of every enveloping claim, an exhaustive enumeration check of Section 3, and a coefficient-level match with Uçar's thesis. Two things stand in the way of acceptance:

- M1 must be resolved: the editor needs [4], and the paper must state precisely what is new relative to [4] and Uçar.
- I strongly recommend M2, which would make Lemma 3.3 do much more work.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Provide [4] to the editor. Give a per-result primary-home statement. Replace the [4]-attributions with internal references. Add a sentence that (1) equals Uçar's (4.33)–(4.35) at κ = −1. Give an explicit novelty statement for Prop. 2.3, Lemma 3.3 and Thm 3.2(i). |
| M2 | Add a class-exact version of Lemma 6.1 / Thm 6.2 (exact first-difference index and exact least \|d_k\| over Sig(A, M)) with its constants beside Table 5, or qualify the explanation of the size of the constants (pp. 1, 3). |
| m1 | Replace the sum by the maximum in (2) and Q(K), or justify keeping the sum. |
| m2 | Cite Iwaniec Thm 10.2 / Hejhal / [17, (2.8)] for the heat function, and drop Lemma A.1 or mark it as included for self-containedness. |
| m3 | Derive the closed form of α_k, or cite Uçar (4.35). |
| m4 | Write out the final inequality chain in the proof of Theorem 3.2(i). |
| m5 | State the lcm convention for signatures without cone points. |
| m6 | Add a remark on the observed first-difference indices. |
| m7 | Correct the Uçar citations. |
| P1–P5 | Disambiguate the notation, define a_{l,k} where first used, use internal citations, and add the two clarifying sentences (P4, P5). |
