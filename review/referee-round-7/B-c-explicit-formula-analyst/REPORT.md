<!-- Referee B-c: returned text saved verbatim; the reviewer could not write files -->

I couldn't save the report: writing `REPORT.md` was refused, so the full report is below instead. In short, every proof that Theorems 1.1 and 6.2 rely on in my sections is correct, and every table in scope reproduces. There is one MAJOR issue (M1), about how the paper explains its own constants. My recommendation is minor revision.

# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

Submitted to *Annals of Global Analysis and Geometry*.
Referee B-c: explicit formulas, test functions in the Selberg trace formula, trace-formula verification of computed spectra.
Scope: Sections 2, 3, 5 and 6, and Appendix A. Lemma 4.5 and Lemmas 4.2–4.3 behind it are also checked, because Theorem 6.2 depends on them. Section 7 is touched only where Section 6 refers to it (Fig. 1, Table 6, last column).

The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) are treated as known and not commented on. Every typographical or sign point below was checked against rendered page images (pdftoppm, 110 dpi).

---

## Summary

The paper proves an effective version of a classical consequence of compactness. In the class C(A, ε, M), the first N eigenvalues, each known to within δ, determine the signature, and N and δ are closed-form expressions in A, ε and M (Theorems 1.1 and 6.2).

The mechanism is the following.

1. Write the heat trace by the Selberg trace formula as G_σ(t) + Hyp(t) (Theorem 2.1).
2. Expand G_σ in heat invariants with enveloping remainders (Proposition 2.3).
3. Show that the first heat invariant at which two signatures differ does so by an explicitly bounded amount: an integer multiple of a_{k−2}, or of 1/(2L) for the area (Lemma 3.3). Its index is at most min(⌊A/π⌋+4, M) (Theorem 3.2).
4. Bound Hyp(t) using a diameter-free count of closed geodesics (Lemma 4.5 with Lemma 2.2(ii)).
5. Control the spectral tail through the heat trace at an earlier time (Proposition 5.2).

The resulting constants are astronomically large (Table 3: N up to 3.8 × 10^30, δ down to 8.7 × 10^−278). Separately, the paper gives an a-posteriori test (Section 7), which is outside my brief.

## Significance

The question is natural, and an effective, checkable statement is worth having. In my sections the paper's real contributions are:

- the clean integrality statement at the first difference (Lemma 3.3);
- a careful, fully enveloping treatment of the cone and area remainders, valid for every t > 0 (Proposition 2.3), not merely asymptotic;
- the assembly into a proof whose every constant can be recomputed.

The sections I reviewed contain no deep new analytic idea. They combine a classical trace formula, the companion paper's heat-invariant algebra and elementary tail bounds.

The headline numbers of Theorem 6.2 are, as I show in M1, an artefact of one choice in the proof (Lemma 6.1). They are not intrinsic to the method. The paper's own discussion attributes them to the wrong cause. This bears on how the result should be presented, not on its correctness.

## Correctness, and what I recomputed

**Verdict on correctness: every proof in Sections 2, 3, 5, 6 and Appendix A that Theorems 1.1 and 6.2 depend on is correct.** I found no gap, no sign error and no wrong constant. I checked each step by hand and the following by independent code. The scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/B-c-explicit-formula-analyst/scratch/`: `heat.py`, `check_num.py`, `table3.py`, `kover.py`, `computed_gap.py` and `test71.py`. They were written from the manuscript alone and use sympy and mpmath.

**Trace formula (Theorem 2.1, Lemma A.1)**

- The normalisation of all three terms agrees with Dryden–Strohmaier [1, eq. (1)] and with Garbin–Jorgenson [15, (2.8)]. I fetched both from arXiv: math/0504571v2 and 1603.01495v1.
- E_m(t) → (m²−1)/(12m) follows from the beta integral, which I verified.
- As an independent end-to-end check, I took the 40 eigenvalues of Table 5 for each of O(2,8,8) and O(3,3,12) and compared them with G_σ(t) evaluated by 30-digit quadrature.
  - At t = 0.06 they agree to 7 × 10^−9 for O(2,8,8). That is the size of the Weyl tail beyond λ_40.
  - They agree to 1.0 × 10^−6 for O(3,3,12), which is consistent with Hyp(0.06) at systole 1.8626.
  - For t ≥ 0.08 the residual grows exactly as the geodesic term should.
  - So the normalisation, including the "each nontrivial stabiliser element once" convention for the elliptic terms, is right.
- In Lemma A.1, the approximation argument is sound:
  - the a-priori count #{λ_j ≤ x} = O(x) comes from η_T with support in [−2ϵ, 2ϵ];
  - the bound |f̂_X(r)| ≤ ϵ_X min(1, |r|^−3) holds;
  - the imaginary r_j are handled by ∫|f_X| e^{|u|/2}.

  I checked that η_T(iy) is real and bounded uniformly in T: by evenness and realness of ψ, η_T(iy) = 2 Re ψ̂(iy−T)².

**Lemma 2.2**

- In (i), the Dirichlet-domain packing argument is correct.
- In (ii), I rederived B_C(ℓ, t) step by step, including:
  - the integration by parts against −φ′ ≥ 0;
  - the identity x e^{x/2−x²/4t} = −(2tx/(x−t)) (d/dx) e^{x/2−x²/4t};
  - the logarithmic derivative in ℓ, which is negative exactly on t ≤ ℓ²/(2(1+ℓ));
  - the global bound, with maxima at x = 2√t and x = 6t.

  The constant 2C e^{17t/4−1/2−ℓ}/(√π(1−e^{−ℓ})) is right.

**Proposition 2.3 and Lemmas A.2–A.3**

- Symbolically:
  - the closed form of Φ_m;
  - the Bernoulli expansion;
  - the formula for m φ_k(m), checked against direct series of the defining sum for m = 2, 3, 7, 12 and k ≤ 3, with exact agreement;
  - p_l for l ≤ 5: even, degree 2l+2, p_l(1) = 0, leading coefficient a_l = |B_{2l+2}|/(2(l+1)!(2l+1));
  - b_0(m) = (m²−1)/(12m);
  - α_0, …, α_5 = 1, −1/3, 1/15, −4/315, 1/315, −4/3465, which agree for k ≤ 9 with the moment formula built from μ_k = (1−2^{−2k−1})(−1)^k B_{2k+2}/(k+1);
  - μ_0, …, μ_3, checked against quadrature.
- Numerically, at 30 digits I checked the enveloping property. For m ∈ {2, 3, 8, 12}, t ∈ {10^−3, 10^−2, 0.05, 0.3, 1, 3} and K ≤ 6, the remainders have sign (−1)^K and modulus at most |b_K(m)| t^K, with zero failures. The area term, sign (−1)^{K+1} and modulus at most |α_{K+1}| t^K, also has zero failures.

**Lemma 3.1, Theorem 3.2, Lemma 3.3, Lemma A.4**

- I checked each proof line by line: the paddings, the even-polynomial argument with e_{κ−1} = e_κ Σ 1/x, the bound κ ≤ 2(⌊A/π⌋+4), and the Vandermonde determinant in (ii).
- By brute force over all hyperbolic signatures in Sig(π/2, 12) (48 signatures), Sig(4π/3, 3) (8), Sig(4π/3, 12) (281) and Sig(2π, 6) (90), with exact rational heat invariants:
  - every pair first differs at an index k ≤ min(n_*, M);
  - |d_k| ≥ δ_k in every case, with no violations;
  - the example (0;4,4,4)/(0;3,4,6) with d_2 = −1/12 is confirmed;
  - d_3 = 25/12 for (0;2,8,8)/(0;3,3,12) is confirmed.

**Section 5**

- Lemma 5.1 (the case analysis and the bounds on E_m and I) is correct; see m4 for the unstated non-hyperbolic cases.
- Proposition 5.2 is correct.

**Lemma 6.1 and Theorem 6.2**

- I checked every inequality:
  - the choice of p = k_* − 3/2 and of y_0. The rendered page 13 has y_0 = 2(log(16ϖ/γ_*) + p log(4/ε²) + p log(2p/e)), which is exactly what e^{−y/2} y^p ≤ (2p/e)^p requires;
  - the monotonicity of B_* on (0, t_2];
  - Hyp ≤ Θ_*/8 ≤ 1;
  - Λt_* ≥ 1 and N > e Z_O(1/Λ);
  - the tail bound Θ_*/8 and the perturbation bound Θ_*/(8e).
- The final margin 3/8 against 5/8 is correct.
- The remark that t_* may be replaced by a smaller t is correct, because y ≥ y_0 persists.

**Table 3**

All eight rows are reproduced to the printed two digits: C_*, t_1, t_3, Θ_*, Λ, N, δ and the binding constraint. This uses Lemmas 4.2–4.5 as printed, which I also checked.

**Remaining numerical claims of Section 6**

- The last column of Table 6 (6.8 × 10^9, 4.3 × 10^4, 7.4 × 10^12) is reproduced.
- The claim "at A = 10π [the bound k_* ≤ M] changes N from about 4 × 10^18 to 1.1 × 10^6" is reproduced: 4.19 × 10^18 and 1.08 × 10^6.
- For A = 4π/3 and M = 3:
  - t_3 binds exactly for ε ≤ 0.42;
  - N grows by a factor of 5.24, 5.13, 5.01, 4.90 and 4.81 per halving, so "about 5 … decreasing towards 4" holds;
  - C_* grows by a factor tending to 16, so "C_* of order ε^−4" holds.
- The growth "|b_K(M)| roughly like K!(M/π)^{2K}" holds up to a factor decaying like K^{−1/2}.

**Fig. 1 and Table 6 (triangle orbifolds), from Table 5 alone**

I ran Theorem 7.1 on the 40 tabulated eigenvalues and errors, with s/t on a 240-point grid. The results reproduce Table 6:

- O(2,8,8): (C1, Δ) = 18, (C2, Δ) = 20, (C1, C_*) = 24.
- O(3,3,12): 25, 29 and 36.
- No wrong signature is ever singled out.
- The shaded window of Fig. 1 (around t ≈ 0.05–0.056) is consistent with this.

---

## FATAL

None.

## MAJOR

**M1 (pp. 14–15, p. 21, and the abstract on p. 1). The size of the a-priori constants is an artefact of Lemma 6.1, and Section 7.2 attributes the gap to the wrong cause.**

What the paper says:

- p. 21: "Nearly the whole gap to Theorem 6.2, a factor of … 2 × 10^8 for the triangle orbifolds and 10^10 to 2 × 10^11 for the family at M = 12, comes from the use of the data: Theorem 6.2 must allow for the worst signature of the class and is governed by the divergence of the cone expansion, through t_1."
- The abstract says only "The constants are very large."

What actually happens is this. Theorem 6.2 replaces the true gap min_{σ≠σ′} |G_σ(t) − G_σ′(t)| over the finite set Sig(A, M) by the heat-invariant lower bound Θ(t) = ½ γ_* t^{k_*−2}. That bound is valid only for t ≤ t_1, and t_1 is 10^−7 to 10^−27 in Table 3. Nothing about the data enters this step.

To test this, I replaced Θ(t) by the computed gap over all of Sig(A, M), evaluated by quadrature at a single moderate time t. Everything else in Theorem 6.2 was kept exactly as printed: the class-level count C_* of Lemma 4.5, the bound B_C of Lemma 2.2(ii), Z^♯, Λ, N and δ. No spectral data is used, so the result is still an a-priori statement about the whole class.

| class C(A, ε, M) | t | computed gap | B_C(ε, t) | N, data-free | δ | N, Thm 6.2 | test N (C1, C_*) |
|---|---|---|---|---|---|---|---|
| π/2, 1.8626, 12 (48 signatures) | 0.0254 | 3.9e−3 | 5.1e−5 | **290** | 2.4e−5 | 6.8e9 | 24 / 36 |
| 4π/3, 2.6339, 3 (8 signatures) | 0.0805 | 0.153 | 2.0e−3 | **148** | 5.9e−4 | 4.3e4 | 24 |
| 4π/3, 0.6939, 3 (8 signatures) | 0.0064 | 0.165 | 1.7e−2 | **2448** | 4.9e−4 | 4.3e4 | 461 |

Source: `computed_gap.py`. The table uses mpmath at 20 digits on a time grid. It is not certified, but the margins are many orders of magnitude.

So for the triangle class, a factor of about 2 × 10^7 of the 2.8 × 10^8 gap disappears without any data. What remains, a factor of about 8–12, is the contribution of the data. At M = 3 and small systole the data matter relatively more, a factor of about 5, but there too most of the gap comes from Lemma 6.1.

The sentence on p. 21 is therefore wrong as stated: the gap does not come from "the use of the data". The paragraph "How large are N and δ" (pp. 14–15) and the abstract leave the reader thinking that astronomically large constants are what effectivity costs. In fact they are the cost of using a closed-form lower bound for the gap rather than a computed one.

This matters for the paper's own stated purpose ("Effectivity is the point", p. 4). The decision rule of Theorem 1.1 already requires evaluating G_σ(t_*) for every σ ∈ Sig(A, M) to accuracy Θ_*/16 (p. 14). A procedure that evaluates the G_σ anyway can just as well evaluate their gaps at a moderate time.

*What resolves it:*

- (a) Correct the sentence on p. 21 and the corresponding discussion on pp. 14–15. State that the a-priori constants come from the heat-invariant gap bound of Lemma 6.1 (t_1), not from the absence of data.
- (b) Add a remark, or better a corollary: for any finite Sig(A, M), Theorem 6.2 holds with Θ(t) replaced by any certified lower bound for min |G_σ(t) − G_σ′(t)|, at any t ≤ t_2 with B_*(t) ≤ Θ/8. Give the resulting N and δ for at least the rows of Table 3 that can be computed, or for the classes of Table 6. Theorem 2.1 makes this a finite computation of explicit integrals. The proof of Theorem 6.2 carries over verbatim.
- (c) Rephrase "The constants are very large" in the abstract accordingly, or qualify it as "the closed-form constants".

## MINOR

**m1 (p. 14, Table 3; pp. 8–9, Lemma 3.3). t_1 is set by an index k_* that does not occur in the classes enumerated.** In every row of Table 3, the minimum defining t_1 is attained at k = k_*. In the classes I enumerated exhaustively, no pair of signatures first differs beyond k = 3:

- Sig(π/2, 12), where k_* = 4;
- Sig(4π/3, 12), where k_* = 5;
- Sig(2π, 6), where k_* = 6.

Using the exact maximal first-difference index of the class lowers N from 6.8 × 10^9 to 2.4 × 10^7 for (π/2, 1.8626, 12), and from 7.4 × 10^12 to 8.4 × 10^7 for (4π/3, 0.6939, 12).

The least nonzero |d_1| is also much larger than δ_1 = 1/(2L_M): it is 1/2640 against 1/55440 in Sig(π/2, 12). Remark 6.3(a) says the δ_k are worst cases, but it says nothing about k_*.

*Fix:* report in Table 3 which k binds t_1. Extend Remark 6.3(a) to say that both k_* and the δ_k can be replaced by their exact values for the finite set Sig(A, M). State whether Theorem 3.2's bound is ever attained.

**m2 (p. 14, "We do not prove that such a K exists for every class"). This caveat can be removed at small cost.** Add the constraint t ≤ γ_*/(32 Q(k_*−1)) to t_1. Then (2) with K = k_*−1 gives

|G_σ(t) − Σ_{j≤k_*} c_j(σ) t^{j−2}| ≤ t^{k_*−1} Q(k_*−1) ≤ Θ(t)/16

uniformly on Sig(A, M). The decision rule then compares Σ e^{−λ̃_j t} with an explicit polynomial in t with rational coefficients, and no quadrature with an unstated rigorous error bound is needed. For the classes of Table 3 this tightens t by a factor of at most 8γ_*/δ_{k_*}. Alternatively, cite or describe the validated quadrature you have in mind: as written, the "finite procedure" (p. 4) rests on an unspecified ingredient.

**m3 (p. 12, end of the proof of Lemma 4.5).** "≤ K e^x": K is undefined. It should be C_* e^x, with C_* = (A/v_0) M e^{10r_0+ρ_1}/(2(cosh ρ_1 − 1)). The bound is correct as computed.

**m4 (p. 12, Lemma 5.1(i)).** The case analysis omits g = 0 with n ≤ 2, and g = 1 with n = 0. Say that these are not hyperbolic.

**m5 (p. 2 and p. 13).** Sig(A, M) should be defined explicitly as the set of *hyperbolic* signatures, with area in (0, A], since Lemma 3.3 and Theorem 3.2 are stated for hyperbolic signatures. Also state in Theorem 6.2 that the minimiser ranges over signatures of all areas ≤ A. Lemma 6.1 correctly covers k = 1 for this, but a reader could think only area A is meant, as in Theorem 7.1.

**m6 (p. 6 and Table 1).** Theorem 2.1 is attributed to "[30, Thm 2.3, Lemma B.1]". The formula is classical (Selberg, Hejhal [33], Iwaniec [34], Dryden–Strohmaier [1]). Only the extension to the heat function by approximation is the companion paper's. Attribute accordingly.

**m7 (pp. 15–16, Remark 6.4).** Since this is my specialty, I would like the remark sharpened rather than left as "not worked out".

- With g supported in (−ℓ, ℓ), the geodesic term vanishes in Theorem 7.1 as well, so H(t) disappears from E_N.
- The price is that ĝ is not positive and not monotone, so the tail needs a two-sided bound from the eigenvalue count. The positive choice ĝ = |ψ̂|² helps one side.
- The signature terms Σ_i E_{m_i}[h] for a dilated family g_a(u) = a^{−1} g(u/a) have a small-a expansion with the same heat-invariant structure, so the separation step is not obviously better.

Either sketch these points, or say that you do not know whether the compactly supported route improves Theorem 6.2.

**m8 (p. 3, Theorem 1.2, and p. 16, Theorem 7.1).** Theorem 1.2 says "first N+1 eigenvalues" and uses λ̃_N in E_N. Theorem 6.2 uses N eigenvalues. Section 7.1 (p. 20) explains this, but Theorems 1.1 and 1.2 should state it once, side by side, because Table 6 compares the two counts directly.

## PRESENTATION

**P1 (throughout my sections). Symbol overloads that will cost readers time:**

- δ is the accuracy of Theorem 6.2; δ_k are the separations; δ appears again in Proposition 8.3.
- N is the eigenvalue count, and also the number of variables x_1, …, x_N in Lemma A.4.
- m is a cone order, and 𝔪_n(a) are the moments in the proof of Proposition 2.3.
- ε is the systole bound, ϵ is the support radius in Lemma A.1, and ϵ_j are the eigenvalue errors.
- p is k_* − 3/2, p_l are the cone polynomials, and P is a polygon.
- L is a padding length in Lemma 3.1, L_M and L_σσ′ are lcms, L is a length in Remark 6.3(c), and L is a translation length in Section 8.
- K is the expansion order, and the undefined K of m3.

**P2 (p. 15, Fig. 1).**

- There is no legend. The five competitors are not identified, except that the darkest is (0;3,3,12).
- The figure does not say which dotted curve is N = 21 and which is N = 100.
- The y-axis label covers only the gaps, though bounds are also plotted.
- The caption should say why N = 21 is shown when Table 6 gives 20: the s-grid kt/20 is coarser than the 240-point grid of Section 7.1.

**P3 (p. 14, Table 3).** Add the t_2 column, or a sentence noting that t_2 never binds (it is ≥ 4.5 × 10^−3), and add the binding k of t_1 (see m1).

**P4 (pp. 13–14, proof of Theorem 6.2).** Two steps are compressed and should be spelled out:

- "Hence Hyp(s) ≤ Θ_*/8 for s ≤ t_*" uses that B_* increases on (0, t_2] and that t_* ≤ t_2.
- "As Λt_* ≥ 1" uses 8Z^♯(t_*/2)/Θ_* ≥ e^{1/2}.

**P5 (p. 7, Section 2.2).** Φ_m is defined "for an integer m ≥ 1", but Proposition 2.3 and everything after use m ≥ 2. Unify these.

**P6 (Table 1 and Appendix A, editorial).** Sections 2–3 and about three pages of Appendix A reproduce results and proofs of the simultaneously submitted companion paper [30], openly and in order to make this paper self-contained. The editor should have [30] in hand to judge the overlap.

---

## Recommendation

**Minor revision** for the part under my review. Confidence is high on correctness: every step was checked and the constants were recomputed independently. Confidence is moderate on the overall recommendation, which depends on the other referees' sections and on the editor's view of the overlap with [30].

The mathematics in Sections 2, 3, 5, 6 and Appendix A is correct and carefully done. The tables in my scope reproduce exactly. The one substantive problem, M1, is interpretive, but it concerns the paper's central comparison and must be fixed. I would also strongly encourage adding the computed-gap corollary, which would turn Theorem 6.2 from a curiosity with 10^−278 accuracies into a usable a-priori statement.

## What resolves each issue

| issue | resolution |
|---|---|
| M1 | Correct p. 21 and pp. 14–15 on the source of the gap. Add a remark or corollary allowing a certified computed gap in place of Θ(t), with numbers. Qualify "very large" in the abstract. |
| m1 | Report the binding k of t_1. Extend Remark 6.3(a) to cover k_* and \|d_1\|. Say whether Theorem 3.2 is ever attained. |
| m2 | Add t ≤ γ_*/(32 Q(k_*−1)) so the rule uses the truncated expansion, or specify the validated quadrature. |
| m3 | Replace K by C_* on p. 12. |
| m4 | Mention the non-hyperbolic cases in Lemma 5.1(i). |
| m5 | Define Sig(A, M) as the hyperbolic signatures of area in (0, A]. Say so in Theorem 6.2. |
| m6 | Attribute Theorem 2.1 to the classical sources. Credit [30] only for the extension to the heat function. |
| m7 | Sharpen Remark 6.4 as described, or state plainly that this is open. |
| m8 | Put the N versus N+1 conventions side by side in Theorems 1.1 and 1.2. |
| P1–P6 | Rename the overloaded symbols. Add a legend and caption detail to Fig. 1. Add a t_2 column and the binding k to Table 3. Expand the two compressed steps. Unify m ≥ 2. Give the editor the companion paper. |
