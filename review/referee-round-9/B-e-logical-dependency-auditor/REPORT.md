<!-- Round 9 B-e referee report: returned text saved verbatim; the reviewer could not write files -->

The write to REPORT.md was refused (subagents may not write report files), so the full report is below. My scratch code and data are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/B-e-logical-dependency-auditor/scratch/ (code/, cites/, pages/).

# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

**Journal:** Annals of Global Analysis and Geometry.
**Role:** referee for rigour, citations and figures. I traced logical dependencies, checked citations at statement level, and checked tables, figures and cross-references.

## Summary

Fix an area bound A, a systole bound ε and an order bound M. The paper proves that within the class C(A, ε, M) of closed orientable hyperbolic 2-orbifolds, the first N eigenvalues, each known to within δ, determine the signature. N and δ are explicit (Theorem 1.1 / Theorem 6.2).

The argument has four parts:
- **Selberg trace formula** for the heat function (Theorem 2.1).
- **Enveloping remainders** for the identity and elliptic terms (Proposition 2.3).
- **Integrality of the first differing heat invariant** (Lemma 3.3, resting on Theorem 3.2).
- **A count of closed geodesics** that depends on A, ε and M only (Lemma 4.5, via cone-point separation, Lemma 4.2).

The closed-form constants are astronomically large (Table 4). Proposition 6.4 replaces the heat-invariant gap with a gap certified in ball arithmetic at a moderate time, giving N between 139 and 7416 for five classes, plus N = 387182 for a sixth (Table 3). Theorem 1.2 / Proposition 8.3 shows the order bound cannot be dropped: the triangle orbifolds O(2,3,m) have systole bounded below uniformly in m, yet their low eigenvalues cluster. Corollary 8.5 deduces that N must grow at least like log M / log log M.

Section 7 is an a-posteriori test, Theorem 7.1, run on computed spectra. The authors say clearly that these runs are consistency checks, not determinations.

## Significance

The paper makes effective a compactness statement that is standard: signature rigidity follows from Dryden–Strohmaier and Doyle–Rossetti, and finiteness from compactness. The bounds of Theorem 6.2 are of no practical use (up to 4×10^30 eigenvalues at accuracy 10^−277). The genuinely usable statement is Proposition 6.4, which is computer-assisted.

Theorem 1.2 is the conceptually most interesting result. It shows the order hypothesis is necessary, and that holds even at fixed area and systole. The paper is honest throughout about what is proved and what is observed.

The contribution is modest but correct and carefully executed. It fits the journal's scope. My assessment of significance is "solid, not striking".

## Correctness, and what I recomputed

I traced every proof that Theorem 6.2 and Theorem 1.2 depend on. The dependency chain is:

1. Theorem 2.1, with Lemma A.1 for the heat function.
2. Lemma 2.2.
3. Proposition 2.3, with Lemmas A.2 and A.3.
4. Lemma 3.1, Theorem 3.2 (with Lemma A.4) and Lemma 3.3.
5. Lemmas 4.1–4.3 and 4.5.
6. Lemma 5.1 and Proposition 5.2.
7. Lemma 6.1 and Theorem 6.2.
8. Corollary 6.3 and Proposition 6.4.
9. For Theorem 1.2: Lemma 8.1, Proposition 8.2, Proposition 8.3 and Corollary 8.5.

I found no logical gap in this chain. I checked each step by hand. In particular:
- The integration by parts and the monotonicity in ℓ in Lemma 2.2(ii), including the constant 17t/4.
- The sign and modulus bookkeeping in the proof of Proposition 2.3.
- The triangular expansion in Lemma 3.3: d_k = (−1)^k a_{k−2}(P_{2k−3}(U) − P_{2k−3}(V)).
- The Vandermonde argument in Theorem 3.2(ii).
- The parity argument in Theorem 3.2(i), including |V*| − |U*| = 2(g − g′) and κ ≤ 2(⌊A/π⌋ + 4).
- The Gauss–Bonnet defect bound in Lemma 4.2.
- The packing count in Lemma 4.5.
- The derivation of y_0 and t_3 in Theorem 6.2, including the inequality e^{−y} y^p ≤ (γ*/16ϖ)(ε²/4)^p.
- The 3Θ*/8 margin in Theorem 6.2.
- Jørgensen's recursion in Lemma 8.1, including the case where some x_n vanishes.
- The trace identity tr[γ,β] − 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r.
- The identity (3) for the Rayleigh quotient, and the collar quotients in Proposition 8.6.

I also recomputed the following independently, using my own mpmath/scipy code.

- **Proposition 2.3 (numerical):** I evaluated E_m(t) and I(t) by quadrature for m = 2, 3, 7, 12, t = 0.01, 0.1, 0.5, 2 and K = 0, …, 5. The sign (−1)^K (resp. (−1)^{K+1}) and the bound |b_K(m)| t^K (resp. |α_{K+1}| t^K) hold in all cases.
- **Cone-term coefficients:** φ_k from Lemma A.2 agrees with the Taylor coefficients of Φ_m. a_l, p_l(1) = 0, α_0, …, α_4 and b_0(m) = (m² − 1)/(12m) are all confirmed.
- **Table 2:** every entry reproduced, and every entry lies below the closed form of Theorem 4.4.
- **Table 4:** every entry reproduced (C*, t_1, t_3, Θ*, Λ, N, δ, binding constraint). The minimum defining t_1 is attained at k = k* in every row, as Remark 6.5(a) states. The values C* ∈ [4×10^5, 7×10^10] and πe^{3D}/A ∈ [3×10^196, 2×10^29325] on p. 13 are confirmed.
- **Table 3:** I recomputed Θ in floating point as the minimum gap over Sig(A, M). I enumerated |Sig(A, M)| = 27, 48, 8, 8, 281, 12. The minimum gaps are 0.0158823, 0.0065273, 0.152029, 0.165511, 0.00137385, 0.166649. Each lies just above the tabulated Θ, as it should. B*(t) ≤ Θ/8, t ≤ t_2 and Λt ≥ 1 all hold. N and δ agree exactly with the table. This independently corroborates Proposition 6.4, but only in floating point.
- **Claims on p. 17:**
  - Without the order bound, N at A = 10π is 4.19×10^18, against 1.08×10^6 with it.
  - For A = 4π/3 and M = 3, t_3 starts to bind between ε = 0.45 and 0.44.
  - The growth factors per halving run 5.24, 5.13, …, 4.67.

  All three are confirmed.
- **Figure 1:**
  - The six signatures of area π/2 with orders ≤ 12 are (0;2,6,12), (0;2,8,8), (0;3,3,12), (0;3,4,6), (0;4,4,4) and (0;2,2,2,4).
  - The small-t limits of the gaps against (0;2,8,8) are 0.75, 0.5, 5/12 and 1/6, plus d_3 t = (25/12)t for (0;3,3,12). They match the plotted curves.
- **Worked examples in the text:**
  - Lemma 3.3: d_2 = −1/12 for (0;4,4,4) against (0;3,4,6).
  - Remark 6.5: (0;2^4,7^7) and (0;4^6,8^4) both have area 12π, agree in P_1, P_3 and R after padding, and differ in P_5.
- **Table 5:**
  - The closed-form systoles of the triangle orbifolds agree with the table (2.2567679, 1.8626041).
  - For the family, 4b = 2.633916 to 0.693995, so each tabulated ℓ is the value rounded down.
  - 2 diam P (largest vertex distance) agrees after rounding up in all ten cases.
  - The margins are ≥ 5×10^−8.
- **Table 7 (triangle rows):** I reran Theorem 7.1 using only the 40 eigenvalues and error estimates printed in Table 6. I used the same set S, ℓ, Δ = 2 diam P and the same s-grid. I get:

  | Orbifold | (C1), Δ | (C2), Δ | (C1), C* |
  |---|---|---|---|
  | O(2,8,8) | 18 | 20 | 24 |
  | O(3,3,12) | 25 | 29 | 36 |

  These are exactly the published counts. No wrong signature was singled out at any N or t.
- **Figure 2 and text ratios:** the ratios 56 and 2.7×10^11 are confirmed (43188/767; 7.436×10^12/28). So are the factor of at most 1.7, "about 10² to 2×10³", "1.9 to 2.8×10^8" and "about 6 to 12" on p. 24.
- **Section 8:**
  - ℓ_{2,3} = 0.56206.
  - 2 arccosh((1 + 2cos(2π/7))/2) = 0.983986.
  - 2 arccosh(3/2) = 1.92485.
  - At m = 4096, h_m² (λ_1 − 1/4)/π² = 1.16, the 16% quoted on p. 29.

**Citations.** I checked these against the sources (arXiv versions, and the HU edoc copy of Uçar's thesis): [1], [2], [3], [6], [12], [13], [14], [15], [16], [23], [25], [26], [29], [33], [38], [47], [48]. Statement-level discrepancies are listed under MINOR. The following could not be accessed and are unverified: [4, Cor. 3], [5], [7, (1.1) and pp. 523–524], [21, p. 67], [30, Thm 1], [36, §5.4], and the published (as opposed to arXiv) numbering of [1], [15] and [16].

## FATAL

None.

## MAJOR

**M1 (pp. 15–16, Proposition 6.4: a computer-assisted result whose certificate cannot be checked from the paper).**
Proposition 6.4 is the only result of practical size, and it is stated as a theorem. Its proof is the sentence "we certified it" plus a pointer to the deposit. The paper does not give what a reader would need to check or reproduce the certificate:
- the rational times;
- the truncation points R;
- the enclosures of the G_σ(t), or at least the pair (σ, σ′) realising each minimal gap together with its enclosure;
- the margin between the certified gap and the rounded Θ. This margin is about 2×10^−6 in row 1, so it matters.

The description of the tail bounds is also inconsistent with the integrals of Theorem 2.1. The identity integrand r tanh(πr) ĝ_t(r) has Gaussian, not exponential, decay, so its tail cannot be bounded by ∫_R^∞ 4r e^{−2πr} dr. That bound fits only the J(t) form of the proof of Proposition 2.3(b), where I(t) = (Area/4π) e^{−t/4}(1/t − J(t)). Presumably that form is what is integrated, but the text does not say so.

My floating-point recomputation reproduces every entry of Table 3. So I do not doubt the result, but as written it is not verifiable from the paper.

*What resolves it:*
- State which representation of each integral is enclosed, with the explicit tail bound for each.
- Add a short table, or an appendix line per row, giving the rational t, R, the minimising pair and the certified lower bound of its gap.
- State that the deposit's certificate script is the proof, and say how to run it.

## MINOR

**m1 (p. 11, proof of (H3)).** "X ≥ −cos(α+β) ≥ −1, with equality only if α = β = π/2 and d = 0" is wrong.
- At α = β = π/2, −cos(α+β) = +1, not −1.
- d = 0 contradicts p ≠ q.

In fact −cos(α+β) > −1 strictly for 0 < α + β ≤ π, so X > −1 always. Since that is all the proof needs, the conclusion survives. Replace the clause with "and −cos(α+β) > −1 since 0 < α + β ≤ π".

**m2 (p. 7, [1, Thm 3.2]).** In Dryden–Strohmaier, Thm 3.2 is the orbifold Gauss–Bonnet theorem ∫K dA = 2πχ(O). The area formula needs Def. 3.1 (the orbifold χ) as well. Cite "[1, Def. 3.1, Thm 3.2]". The Thurston citation [33, 13.3.4–13.3.6] is correct.

**m3 (pp. 5 and 28, "Hecke triangle groups", [15, Ex. 5.8], [17, p. 579]).**
- In Garbin–Jorgenson's Example 5.8 the groups G_N have genus 0, one cusp and elliptic points of orders 2, 3 and N. That is not the Hecke group: the Hecke group ⟨−1/z, z + 2cos(π/N)⟩ has signature (0; 2, N; 1).
- The manuscript inherits the label on p. 5 ("for Hecke triangle groups this accumulation is attributed to Selberg") and uses it on p. 28 ("their own Example 5.8, the Hecke groups, as the triangles converge to the triangle of PSL(2,Z)").

Either the example concerns the (2,3,N) family, which is exactly the family of Section 8.1, or it concerns Hecke groups, which have a cusp for every N. The two do not degenerate in the same way. The authors should say which family [15, Ex. 5.8] and [17, p. 579] actually treat, and stop calling the (2,3,m) triangles Hecke groups.

**m4 (p. 28, conditional claim).** The deduction "so λ_j(O(2,3,m)) → 1/4 for every j ≥ 1" rests on "granting" Garbin–Jorgenson's condition (b), which the paper does not verify. It also uses [15, Cor. 5.5], which concerns counting functions at levels T that are not eigenvalues of the limit; eigenvalue-wise convergence appears only in the prose after Cor. 5.5. Phrase the claim explicitly as conditional ("if (b) holds, then …") and cite the location precisely.

**m5 (p. 7 and Appendix A.1, "the extension to the heat function of [31, Lemma B.1]").**
- The heat function ĝ_t is admissible in the classical trace formula: it is even, holomorphic in |Im r| ≤ 1/2 + ε, and decays faster than (1 + |r|)^{−2−ε} (Hejhal [34], Iwaniec [35]).
- Lemma A.1 is correct, but calling it an extension overstates it. Say instead that it reduces the claim to the C_c^∞ version stated in [1].
- In [1], eq. (1) does not fix the Fourier normalisation. The one used here, ĝ(r) = ∫ g(u) e^{iru} du, agrees with [16, Rem. 2.6–2.7]. Say so, and note that the general-h form in [16] is (2.9) while the heat form is (2.8).

**m6 (pp. 17 and 20, C* printed twice with different values).** Table 4 gives C*(π/2, ·, 12) = 3.5e9 and C*(4π/3, ·, 3) = 4.0e5. Table 5 gives 3.6×10^9 and 4.1×10^5 for the same quantities. They are the same quantities because d_0, and hence C*, does not depend on ε at these M. The exact values are 3.545×10^9 and 4.010×10^5, so Table 5 rounds up and Table 4 rounds to nearest. State the rounding convention in Table 5's caption, or unify the two tables.

**m7 (p. 4, [2]).**
- [2, Thm 3.40] is a theorem about polygon angles. The induction the paper calls "Uçar's induction" sits in its proof and is transferred to orbifolds in §4.3 of the thesis. Cite "[2, proof of Thm 3.40 and §4.3]".
- [2, Cor. 4.21]: the relevant part is (iv) (trivial mirror locus, κ ≠ 0 known). Cite it as such.

**m8 (p. 5, [6, Thm 1]).** Doyle–Rossetti's Thm 1 gives the area and the number of cone points of each order. The genus then follows by Gauss–Bonnet, which is not stated there. The sentence "the spectrum determines the signature [1], [6, Thm 1]" is acceptable, but "determines the number of cone points of each order" (p. 5, line 4) is the precise content.

**m9 (references).**
- Errata exist and should be cited alongside the originals: for [23] (Comm. Math. Phys. 359 (2018) 427, doi 10.1007/s00220-018-3094-z) and for [29] (Michigan Math. J. 66 (2017) 221–222, doi 10.1307/mmj/1488510034).
- [12, Main Thm 2] needs a lower bound on *sectional* curvature, not just Ricci. The text on p. 5 says "a lower curvature bound", which is acceptable, but Main Thm 1 assumes only Ricci, so the two theorems differ.

**m10 (p. 21, convergence data).** The paper says the h- and p-convergence of the eigenvalues "is tabulated in the supplement of [31]", an unpublished companion with a placeholder identifier. Section 7 is not a proof, so this is not a logical dependency. Still, the data supporting Tables 6 and 7 should be in this paper's own deposit, or referenced to it.

## Presentation

- **P1 (Figure 2, p. 25).** The plot has no legend. Markers (diamond/square/circle, open/filled, two colours) are explained only in the running text. Add an in-figure legend, or a caption that names every marker.
- **P2 (Theorem 1.1, p. 2).** The theorem uses t*, N and δ, which are defined only in Theorem 6.2. That is acceptable, but give one sentence on the form of N and δ, e.g. N ≈ (eA/2πt*) log(8Z♯/Θ*).
- **P3 (p. 3 vs Table 4).** The range "4×10^4 to 7×10^12" uses nearest rounding (7.44×10^12), while Table 4 prints 7.5e12 (rounded up). This is harmless, but use one convention throughout.
- **P4 (p. 15).** "with Arb's certified integration … on a finite interval beyond which each tail is bounded …": see M1. Say which integrand is meant.
- **P5 (Lemma 2.2(ii)).** The monotonicity of B_C in ℓ is proved but never used in any later proof, since Theorem 6.2 applies the bound at ℓ = ε directly. Either use it, or drop it or mark it as a remark.
- **Strengths.** Cross-references and numbering are correct throughout; I found no broken or mismatched reference. Every table caption matches its content and the text. Every figure I checked against its caption and the data (Figures 1–3) is consistent. The rendered mathematics on the pages I inspected (7–9, 11–17, 19, 25–30) has no sign errors.

## Recommendation

**Minor revision.**

- Confidence that the main theorems are correct: **high.** I checked every step of the proofs of Theorems 6.2 and 1.2 and independently reproduced Tables 2–5 and the triangle rows of Table 7.
- Confidence in the recommendation itself: **medium-high.** M1 must be fixed, but it is a matter of documentation rather than correctness.
- A note on significance for the editor: the paper's practical content is a computer-assisted proposition plus a necessity example. Whether that clears the journal's bar is the editor's call. I would not reject on rigour grounds.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Give per-row certificate data (rational t, R, minimising pair, certified gap lower bound), state the integral representation and tail bounds actually enclosed, and point to the runnable certificate. |
| m1 | Replace the equality clause in the proof of (H3) with "−cos(α+β) > −1". |
| m2 | Cite [1, Def. 3.1, Thm 3.2] for the area formula. |
| m3 | Identify the family in [15, Ex. 5.8] and [17, p. 579] correctly; do not call the (2,3,m) triangle groups Hecke groups. |
| m4 | State the λ_j → 1/4 claim conditionally, with a precise location in [15]. |
| m5 | Reword "extension to the heat function"; record the Fourier convention and [16, (2.8)–(2.9)]. |
| m6 | Unify or state the rounding of C* in Tables 4 and 5. |
| m7 | Cite [2, proof of Thm 3.40, §4.3] and [2, Cor. 4.21(iv)]. |
| m8 | Adjust the statement attributed to [6, Thm 1]. |
| m9 | Add the two errata; note the sectional-curvature hypothesis of [12, Main Thm 2]. |
| m10 | Put the convergence data in this paper's deposit. |
| P1–P5 | As stated above. |
