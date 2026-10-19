<!-- Round 8 B-e referee report: returned text saved verbatim; the reviewer could not write files -->

Writing to REPORT.md was refused, so the full report follows here instead.

# Referee report (AGAG): rigour, citations and figures

**Manuscript.** "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (36 pp.)

**Remit.** I checked every statement against its proof and hypotheses, every external result at statement level against its source, every table and figure against its caption and the text, and the numbering. I read the pages as rendered images (pdftoppm at 110, 200 and 300 dpi). I treated the placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) as known.

## Summary
The paper proves an effective version of the following fact: the spectrum of a closed orientable hyperbolic 2-orbifold determines its signature. Fix a class C(A, ε, M), meaning area at most A, systole at least ε and cone orders at most M. Theorem 6.2 gives explicit N and δ: the first N eigenvalues, each known to within δ, determine the signature. The decision rule is to pick the σ in Sig(A, M) that minimises |Σ_{j<N} e^{−λ̃_j t*} − G_σ(t*)|.

The proof combines four ingredients:
1. An enveloping remainder for the small-t expansion of the identity and cone terms (Prop. 2.3).
2. An integrality lower bound for the first heat invariant at which two signatures differ (Lemma 3.3). That index is at most min(⌊A/π⌋+4, M) (Thm 3.2).
3. A count of closed geodesics from A, ε and M alone (Lemma 4.5). It uses separation of cone points (Lemma 4.2) and a packing argument.
4. A heat-trace tail bound (Prop. 5.2).

The paper also shows that the order bound cannot be dropped:
- **Theorem 1.3 and Prop. 8.2–8.3:** O(2,3,m) has systole ≥ 0.56206 uniformly in m, and λ_j ≤ 1/4 + π²(j+1)²/h_m².
- **Corollary 8.5:** N must grow at least like log M / log log M.

Finally, it gives an a-posteriori test (Theorem 7.1), run on ten computed spectra. These runs are honestly labelled as consistency checks.

## Significance
The qualitative statement follows from compactness, as the authors say. The contribution is that every constant is explicit, together with the obstruction of Theorem 1.3, which is sharp in kind.

The a-priori constants are astronomically large: Table 3 has N up to 4 × 10³⁰. The practically meaningful numbers, N ≈ 10²–10⁴ from Corollary 6.3, rest on a gap that is computed, not certified.

This is a solid, careful, modest contribution to inverse spectral geometry of orbifolds, within AGAG's scope. Its value is a complete, checkable effective chain of argument.

## Correctness and what I recomputed
I found no mathematical error in any proof that a main result depends on.

### Proofs checked line by line
- **Lemma 2.2(i)–(ii):**
  - the integration by parts and the bound B_C;
  - monotonicity of B_C in ℓ (the bracket is ≥ 0 exactly when t ≤ ℓ²/(2(1+ℓ)));
  - the bound valid for all t (maxima at 2√t and 6t, giving e^{17t/4−1/2−ℓ}).
- **Lemma 4.1 (H1–H3).**
- **Lemma 4.2:** the defect argument and the bound cosh d − 1 ≥ 2/(π²cM).
- **Lemmas 4.3 and 4.5, and Theorem 4.4** together with its closed form.
- **Lemma 5.1**, all cases (minimum area π/21; n + 4g ≤ A/π + 4).
- **Prop. 5.2.**
- **Lemma 6.1 and Theorem 6.2:** the y₀/t₃ derivation, Θ* ≤ 1/8, Λt* ≥ 2 log 64, and the 3/8 and 5/8 margins.
- **Corollary 6.3 and Theorem 7.1**, including the implication (C2) ⇒ (C1).
- **Lemma 8.1 (Jørgensen):** the recursion x_{n+1} = −x_n(1+x_n)(u−u⁻¹)², the case analysis, and the conjugates C_n → A.
- **The trace identity:** bc = −sin²(φ/2) cosh² r.
- **Prop. 8.2:** the law of cosines, the folding argument, and ℓ_{2,3} = 2 arsinh(½(37/12)^{−1/2}) = 0.562066.
- **Props 8.3 and 8.6:** identity (3), the Rayleigh quotients, and the collar quotient.
- **Corollary 8.5 and Remark 8.4.**
- **Appendix A:**
  - Lemma A.1, including the O(x) eigenvalue count and the case of imaginary r_j;
  - Lemmas A.2–A.4;
  - the proof of Prop. 2.3 (signs and moduli sum exactly to |b_K| t^K and |α_{K+1}| t^K);
  - Theorem 3.2 (|V|−|U| = 2(g−g′), the parity argument via Newton's identities, and the Vandermonde step).
- **Lemma 3.3**, including d₂ = −1/12 for (0;4,4,4) against (0;3,4,6), and d₃ = 25/12 for O(2,8,8) against O(3,3,12).

### Numerical checks (mpmath, 50–60 digits)
- α₀..α₃ come out as 1, −1/3, 1/15, −4/315.
- The closed form for φ_k in Lemma A.2 matches the Taylor coefficients of Φ_m to 10⁻⁵⁷.
- b₀(m) = (m²−1)/(12m) holds, and the leading coefficients a_l are correct.
- The sign and modulus claims of Prop. 2.3 hold by quadrature for m = 2, 3, 8, t ∈ {0.01, 0.2, 1} and K = 0..4.

### Tables, figures and in-text numbers
- **Table 2:** all entries reproduce.
- **Table 3:** every entry reproduces (C*, t₁, t₃, Θ*, Λ, N, δ, binding constraint), and the minimum is at k = k* in every row.
- **In-text numbers that reproduce:**
  - N ≈ 4.19 × 10¹⁸ for the k* = n* comparison at A = 10π, M = 3;
  - πe^{3D}/A ranges from 10^196.5 to 10^29325;
  - t₃ starts to bind at ε ≈ 0.42;
  - Fig. 2's ratios 56 and 2.66 × 10¹¹;
  - the gap ratios on p. 22.
- **Corollary 6.3, recomputed independently** (my own quadrature and signature enumeration, coarser grid):

  | Class | Paper | My value |
  |---|---|---|
  | 1 | 244 | 245 |
  | 2 | 283 | 286 |
  | 3 | 139 | 150 |
  | 4 | 2605 | 2684 |
  | 5 | 7415 | 7434 |
  | 6 | 3.9 × 10⁵ | 3.83 × 10⁵ |

  The differences are consistent with the different time grids.
- **Table 6:** the |S| values 6, 3 and 10 are confirmed by enumeration.
- **Remark 6.4(a):** confirmed exactly. No two signatures share c₁–c₃ in the three stated classes (1562, 5235 and 782 signatures).
- **Table 4:** the closed-form systoles and 2 diam P agree with my values. I did not rerun the finite-element computations.
- **Fig. 1:** the curve levels at t = 10⁻³ are 0.75, 0.50, 0.42, 0.17 and 2.1 × 10⁻³. These match the predicted 9/12, 6/12, 5/12, 2/12 and 25t/12. The shaded grid times are consistent.
- **Fig. 3 and p. 27:** the bounds dominate the plotted values, and "16% above j²" at m = 4096 checks.

### Citations fetched and checked
- **Dryden–Strohmaier [1]:** Thm 1.1, Prop. 3.3, Thm 3.2 and eq. (1) are as cited. The normalisation is identical to Theorem 2.1.
- **Uçar [2]:** Thm 4.20 (eq. 4.35 gives α_k exactly), Cor. 4.21(iv) and Thm 3.40 are as cited.
- **Linowitz–Voight [3]:** Thm A holds; the isospectral pairs share the signature (0;2⁵,3,4).
- **Doyle–Rossetti [6]:** Thm 1 is as cited (v2, 2014).
- **Dryden [9]** is as cited.
- **Stanhope [12] and Proctor–Stanhope [13]:** see m1 and m5.
- **Garbin–Jorgenson [15] and [16]** (arXiv v1 numbering):
  - in [15], §2 conditions (a) and (b), Cor. 5.5, Thm 5.7 and Ex. 5.8 (which itself cites Hejhal p. 579) are as cited;
  - in [16], Rem. 2.7 and eq. (2.8) use the same normalisation, and Thm 6.5 is cited but described inaccurately (see m2);
  - the m ≥ 13 condition on p. 26 is verified.
- **Strohmaier–Uski [23] §7**, **DGGW [29] Thm 4.8**, **Thurston [33] 13.3.4–13.3.6** and **BMM [45]** are as cited.
- **Checked via abstracts:** Judge [18], Chang–DeTurck [30], Mumford [4] (the statement, not the corollary number), Ji [20] and HJL [43].
- **Crossref metadata** agrees for all DOIs.

**Not verified against the source text** (paywalled or blocked): Buser–Courtois [7] ((1.1) and pp. 523–524), Bers [5], Wolpert [21, p. 67], Buser [27, Lemma 6.6.4], Hejhal [17, p. 579] (corroborated by [15]), Beardon [36] and "Cor. 3" of [4].

## FATAL
None.

## MAJOR
**M1 (pp. 1–2, 14, 22).** The usable constants (N = 139–7415) come from Corollary 6.3, and they are "computed, not certified". What is actually proved is:
- Theorem 6.2, with N between 4 × 10⁴ and 4 × 10³⁰;
- a lower bound of order log M / log log M;
- an a-posteriori test with unproved inputs.

So "N of order 10² to 10⁴" in the abstract is not a theorem.

Fixing this is cheap. G_σ(t) is a finite sum of explicit one-dimensional integrals, and Sig(A, M) has 8–281 elements in these classes. One interval-arithmetic quadrature (mpmath.iv or Arb) at one time per class would make Corollary 6.3 a proved statement.

- **Resolution:** certify the gap and state the resulting N as a proposition for at least C(π/2, 1.8626, 12) and C(4π/3, 0.693994, 3). Otherwise, reword the abstract.

## MINOR
- **m1 (p. 4, [12], [13]).** The text says "Theorem 4.4 supplies such a diameter bound", which suggests it fills a gap in the isospectral setting. It does not. Proctor–Stanhope deduce their isospectral result from Stanhope's isospectral diameter bound ([12]; Prop. 7.4 in the arXiv version, as quoted in [13]).
  - **Resolution:** credit [12], and say that what Theorem 4.4 adds is explicitness, in terms of (A, ε, M) rather than the spectrum.
- **m2 (p. 5, [16, Thm 6.5]).** "Spectral counting functions pointwise" is inaccurate. GJ Thm 6.5 concerns the local counting function C(x, T) = Σ_{λ_n ≤ T} φ_n(x)², for x away from the cusps and T < 1/4 not an eigenvalue of the limit.
  - **Resolution:** restate it that way.
- **m3 (p. 5, pp. 26–27, [15]).**
  - The proof of GJ Thm 5.7 rests on their Remark 5.6, which is partly heuristic.
  - GJ Ex. 5.8 misdescribes the Hecke groups: it says orders 2, 3, N, but G_N is the (2, N, ∞) triangle group.
  - Its limit geometry differs from that of O(2,3,m), so the analogy used for condition (b) carries little weight. "Granting this" is appropriate.
  - **Resolution:** note these points, and confirm that the published numbering matches what is cited (I could check only arXiv v1).
- **m4 (p. 5, [25]).** LMPT Thm 1.1 concerns arithmetic 2-manifolds, not orbifolds, and has absolute constants that are effectively computable but not explicit.
  - **Resolution:** change "explicitly" to "effectively".
- **m5 (p. 4, [12, Main Thm 2]).** The bound on the number of singular points requires isolated singularities.
  - **Resolution:** add that hypothesis (it holds in this setting).
- **m6 (pp. 6, 9).** Table 1 cites "[31] Thm 3.11(i)", but the header of Theorem 3.2 cites "Thm 3.11".
  - **Resolution:** harmonise the two.
- **m7 (p. 6).** "Nothing else here is taken from it [31]" conflicts with the eigenvalue data and convergence supplement, which do come from [31] (pp. 6, 20, Table 5).
  - **Resolution:** rephrase.
- **m8 (p. 12).** "Theorem 4.4 is used for the finiteness statement of Section 1" is wrong: Section 1's finiteness argument uses Mumford–Bers.
  - **Resolution:** clarify or delete.
- **m9 (p. 14).** The values in Corollary 6.3 depend on the time grid.
  - **Resolution:** state the grid.
- **m10 (p. 15).** "Factor ≈ 5 per halving, slowly decreasing towards 4": the factors I compute are 4.94, 5.13, 5.01, 4.90, 4.81, 4.74, so they first rise and then fall.
  - **Resolution:** adjust the wording.
- **m11.** Give locators for [7, (1.1), pp. 523–524], [4, Cor. 3] and [21, p. 67], and for the hyperboloid-model citation to [36], which I could not locate in Beardon.

## Presentation
- **P1 (p. 2).** Theorem 1.1 defers N, δ and t* entirely to Theorem 6.2. Add one line on their orders.
- **P2 (p. 19).** The text says Table 5 covers "j ≤ 40", but the table covers 1 ≤ j ≤ 40.
- **P3.** The two N conventions differ: in Theorem 6.2, N is the number of eigenvalues used; in Theorem 7.1, it is the last index. Warn at Theorem 1.2 so the abstract's "24 to 842" is not misread.
- **P4.** In Fig. 2, the open and filled markers are hard to tell apart in greyscale; use different shapes for M = 3 and M = 12.

## Recommendation
**Minor revision.**
- I have high confidence that the proofs are correct.
- I have moderate confidence in overall acceptability.

The mathematics checks out essentially step by step, and every table entry I recomputed reproduces. The citation issues (m1–m5) are imprecise descriptions that affect no proof.

M1 is not a correctness defect, but it is the single change that would most raise the paper's value, and it is cheap. If the editor accepts the transparently uncertified practical constants, M1 can be treated as minor.

## What resolves each issue
| Issue | Fix |
|---|---|
| M1 | Certify the gap in Corollary 6.3 for one or two classes and state it as a proposition, or reword the abstract |
| m1 | Credit Stanhope's isospectral diameter bound |
| m2 | Restate [16, Thm 6.5] as convergence of the local counting function |
| m3 | Note the status of [15]; check published numbering |
| m4 | "effectively"; manifolds only |
| m5 | Add "with isolated singularities" |
| m6 | Harmonise the citations to [31] |
| m7 | Rephrase "nothing else here is taken from it" |
| m8 | Fix the Section 1 reference |
| m9 | State the time grid |
| m10 | Correct the growth-factor wording |
| m11 | Add locators |
| P1–P4 | Editorial |

The verification scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/B-e-statement-citation-auditor/scratch/code/` (consts.py, prop23.py, tables.py, extra.py, cor63.py, firstdiff.py). The fetched sources are in `.../scratch/src/`.
