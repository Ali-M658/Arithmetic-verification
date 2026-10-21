<!-- Round 10, B-e, returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

I could not save REPORT.md: the tool refused to let a subagent write report files. The full report is below.

# Referee report (AGAG): rigour, citations and figures

**Manuscript:** "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (41 pp.)
**Remit:** check every claim against its proof or source, trace each main result's dependencies, and check every table and figure against its caption and cross-references.
**Known placeholders, not counted as defects:** author contributions, AI-use statement, Zenodo DOIs, preprint identifiers (including those of the companion paper [4] and the note [32]).

## Summary

The paper takes a closed orientable hyperbolic 2-orbifold in the class C(A, ε, M): area at most A, systole at least ε, cone orders at most M. It shows that the first N eigenvalues, each known to within δ, determine the signature, with N and δ given by explicit formulas (Theorem 6.2 / Theorem 1.1).

The ingredients are:
- the Selberg trace formula for the heat function (Thm 2.1, App. A.1);
- enveloping remainders for the cone and area terms (Prop. 2.3);
- an integrality lower bound for the first heat invariant at which two signatures differ (Lemma 3.3), with the index of that invariant bounded by min(⌊A/π⌋+4, M) (Thm 3.2);
- a count of closed geodesics in terms of A, ε and M only, with no diameter bound (Lemma 4.5);
- a spectral tail bound read off the heat trace (Prop. 5.2).

The closed-form constants are astronomically large (Table 5). A second route uses Corollary 6.4: the gap between signature terms is computed in ball arithmetic at one moderate time. This gives certified N between 139 and 7416 for the classes of the worked examples (Prop. 6.5, Tables 3–4).

The paper also shows that the order bound cannot be dropped. The triangle orbifolds O(2,3,m) have a uniform explicit systole bound (Prop. 8.2) and acquire many eigenvalues near 1/4 (Prop. 8.3). It follows that N must grow at least like log M / log log M (Cor. 8.5), against the polynomial upper bound of Remark 8.6. Section 7 runs an a-posteriori version of the test on ten computed spectra, and is explicitly labelled as non-rigorous.

**Verdict on the remit.** I found no mathematical error. Every number I recomputed matches, including the whole certificate of Proposition 6.5. Every citation I could reach supports the statement attributed to it, with three small exceptions (m1–m3). The remaining issues are minor or presentational.

## Significance

The result is an honest effectivization of a compactness argument. The authors say plainly (pp. 2–3, 17–18) that the closed-form constants only show that explicit constants exist.

The parts with real content are:
- the tail-plus-gap mechanism;
- the geodesic count without a diameter bound;
- the certified practical instances (Prop. 6.5);
- the necessity of the order bound, with a quantitative lower bound on how N must grow with M.

The mathematics is modest in depth but careful, complete and self-contained; Appendix A reproves everything taken from the companion paper. It suits AGAG's inverse-spectral readership.

The weakest points for significance are that the practical statement (Prop. 6.5) rests on a computer-assisted certificate, and that Section 7 is only illustrative. The paper states both candidly.

## Correctness: what I checked and recomputed

All computations used my own code (mpmath 1.3.0 at 30–40 digits, plus sympy) in a virtual environment inside the scratch folder. I did not have the authors' deposit.

### Proofs checked line by line

**Section 2**
- Lemma 2.2(i) and (ii):
  - the integration by parts and the bound x/(x−t) ≤ ℓ/(ℓ−t);
  - the "every t" bound, with maxima at x = 2√t and x = 6t and constant e^{17t/4−1/2};
  - the monotonicity of B_C in ℓ: the logarithmic derivative is correct, and the bracket is ≥ 0 exactly when t ≤ ℓ²/(2(1+ℓ)).
- Equation (2) from Prop. 2.3: the index bookkeeping (α_1..α_K, b_0..b_{K−1}) is right.

**Section 3**
- Lemma 3.3 (i) and (ii), including the sign (−1)^k and the index 2k−3.
- Theorem 3.2 (i) and (ii), proved in App. A.3:
  - parity of κ;
  - |U|+|V| = 2 max(n+g−g′, n′+g′−g) ≤ 2(⌊A/π⌋+4);
  - the Newton identities / Lemma A.4 argument;
  - the Vandermonde step.

**Section 4**
- Lemma 4.1 (H1)–(H3).
- Lemma 4.2:
  - the defect bound π/(abc);
  - |θ−α−β| ≤ π − π/M;
  - the conclusion cosh d − 1 ≥ 2/(π²M²).
- Lemma 4.3.
- Theorem 4.4 and its closed form. This includes arccosh(1+x) ≥ √(2x/(1+x)), which I proved via f(y) = y²cosh y − 2cosh y + 2 ≥ 0, and the bound 0.6 at M = 2.
- Lemma 4.5.

**Sections 5–7**
- Lemma 5.1: all minimal-s cases (1/42, 1/20, 1/12, 1/10, 1/6, 1/2).
- Prop. 5.2 and Lemma 6.1.
- Theorem 6.2:
  - y_0 is exactly what B_* ≤ Θ/8 requires: with y = ε²/4t, that inequality is e^{−y}y^p ≤ (γ_*/16ϖ)(ε²/4)^p;
  - Θ_* ≤ 1/24;
  - Λt_* ≥ 2 log 64;
  - the 3/8 versus 5/8 margin.
- Remark 6.3: the arithmetic 1/4 + 1/(8e) + 1/8 < 1/2 holds.
- Corollary 6.4 and Theorem 7.1.

**Section 8**
- Lemma 8.1 (Jørgensen's inequality, hyperbolic case):
  - the matrix B_{n+1};
  - the recursion x_{n+1} = −x_n(1+x_n)(u−u^{−1})²;
  - p_n/q_n = x_{n−1}/(1+x_{n−1});
  - the conjugation argument giving C_n → A.
- The trace identity for a rotation and a hyperbolic element.
- Prop. 8.2:
  - the side lengths via (H3): cosh d(v_2,v_3) = 2cos(π/m)/√3 and cosh d(v_2,v_m) = 1/(2 sin(π/m));
  - the 2s_m bound;
  - ℓ_{2,3} = 0.56206.
- Prop. 8.3 and identity (3); I rederived q = 1/2 − w′²/4w².
- Cor. 8.5 and Remark 8.4, including the case A < π/3.
- Remark 8.6: the exponents 9 and 26 at n_* = 4.
- Prop. 8.7: the Rayleigh quotient for λ_1 and the λ_j bound.

**Appendix A**
- Lemma A.1: the η_T window count, the bound ψ̂ ≥ cos(εr) ≥ 1/2, and the dominated convergence.

### Recomputed numbers (all agree with the manuscript)

**Heat-invariant data and Prop. 2.3**
- α_0..α_4 = 1, −1/3, 1/15, −4/315, 1/315.
- a_0..a_3 = 1/12, 1/360, 1/2520, 1/10080.
- b_0(m) = (m²−1)/(12m).
- p_l(1) = 0, and p_l is even of degree 2l+2.
- The closed form in Lemma A.2 agrees with a direct Taylor expansion of Φ_m.
- d_3 = 25/12 for (0;2,8,8) against (0;3,3,12); d_2 = −1/12 for (0;4,4,4) against (0;3,4,6).
- Prop. 2.3 (a) and (b): I checked the signs and the modulus bounds numerically for m ∈ {2,3,7,12}, K ≤ 4 and t ∈ [0.01, 2]. All passed.

**Tables 2, 5 and the C_* values of Table 6**
- Every entry of Tables 2 and 5 is reproduced, with the stated rounding conventions.
- The minimum defining t_1 is attained at k = k_* in every row, as Remark 6.6(a) says.
- The C_* columns of Table 6 (rounded up) are reproduced.

**Tables 3 and 4: an independent recomputation of the Prop. 6.5 certificate**
- |Sig(A,M)| = 27, 48, 8, 8, 281, 12.
- Least gaps: 0.01588232, 0.006527298, 0.1520292, 0.1655107, 0.001373851, 0.1666487.
- The minimising pairs are the listed pairs, or pairs with the same difference of orders, as the text says.
- B_*(t) = 7.98e−6, 7.10e−5, 0.01793, 0.01671, 1.406e−4, 0.01394.
- Λt = 17.63, 19.64, 12.52, 17.21, 27.94, 26.32.
- N = 244, 283, 139, 2605, 7416, 387182 (exact matches).
- δ = 1.167e−4, 4.273e−5, 5.899e−4, 4.867e−4, 2.488e−6, 2.141e−4.
- My check is not certified, but it confirms every input and output of the certificate.

**Secondary claims**
- p. 13: πe^{3D}/A spans 10^{196.5} to 10^{29325.4}.
- p. 18:
  - N ≈ 4.19e18 at A = 10π with k_* = n_*;
  - t_3 binds from ε = 0.44;
  - the factors per halving of ε are 5.239 down to 4.673.
- Remark 8.6: the exponents per doubling of M tend to 9.1 (N) and 26.1 (1/δ); C_* grows like M^9.
- Remark 6.6(a), by exhaustive enumeration:
  - no two signatures share c_1–c_3 for A ≤ 4π with M ≤ 10, for A ≤ 6π with M ≤ 6, or for A ≤ 2π with M ≤ 30;
  - (0;2⁴,7⁷) and (0;4⁶,8⁴) share Ψ_1 and Ψ_2 but not Ψ_3.

**Table 7 against the trace formula**
- At t = 0.1 I compared 1 + Σ_{j≤40} e^{−λ̃_j t} with G_σ(t):
  - O(2,8,8): residual 4.20e−6; the two systole classes predict 4.2e−6;
  - O(3,3,12): residual 2.59e−4; predicted 2.5e−4.
- So the table is transcribed correctly and is consistent with the stated systoles.
- The p. 25 figures "6.8e−3 against 2.8e−10" are reproduced: H = 6.75e−3, and the two classes give 2.76e−10.

**Completeness check on p. 23**
- The nearest other signature term at t = 0.0015 is 2.969e−3 away.
- The stated thresholds are consistent: e^{−15630·0.0015} = 6.6e−11, e^{−15760·0.0015} = 5.4e−11, e^{−9800·0.0025} = 2.3e−11.

**Geometry**
- 2·diam P: 4.897 and 4.317.
- Family systoles 4b: 2.633915 and 0.69404.
- The O(2,3,7) search value 0.983986, and the modular orbifold systole 1.9248.
- Fig. 3(b) rescaled λ_1: 1.35 at m = 7 and 1.16 at m = 4096, matching the "6–16%" in the text.
- Garbin–Jorgenson's condition (a) holds for m ≥ 13.

**Comparison factors stated in the text**
- Fig. 2 caption, "56 to 2.7e11": 43188/767 and 7435635783983/28.
- "10² to 2×10³", "1.9 to 2.8×10⁸" and "6 to 12" all check.
- (λ̃_N − ϵ_N)t = 7.68 and 8.35.
- The Fig. 1 grid times are 0.0501 and 0.0562.

### Citations checked at statement level against the sources

| Ref | Claimed | Verdict |
|---|---|---|
| [1] Dryden–Strohmaier | Thm 1.1, Prop. 3.3; eq. (1), with each elliptic class R_c^l (1 ≤ l ≤ m−1) counted once, weight 1/(2m sin θ); Thm 3.2 | Verified (arXiv math/0504571). The normalisation matches Thm 2.1. |
| [2] Uçar | Cor. 4.21, Thm 4.20, Thm 3.40 | Verified, but pinpoint should be refined (m2) |
| [3] Linowitz–Voight | Thm A | Verified: signature (0;2⁵,3,4), area 23π/6 |
| [7] Doyle–Rossetti | Thm 1 | Verified |
| [13] Stanhope | Main Thms 1–2 | Verified |
| [14], [15], [38], [47], [48], [10] | as stated | Verified |
| [16] Garbin–Jorgenson | §2 (a)/(b), Cor. 5.5, Thm 5.7, Ex. 5.8 | Verified against arXiv 1603.01494v1 |
| [21] Ji | as stated | Verified from abstract |
| [24] Strohmaier–Uski | §7 | Verified |
| [26] Linowitz–McReynolds–Pollack–Thompson | as stated | Verified |
| [30] Dryden–Gordon–Greenwald–Webb | Thm 4.8 | Verified |
| [19] Judge | as stated | Verified from abstract |
| [5] Mumford | compactness | Verified from abstract; "Cor. 3" pinpoint not seen |
| [31] Chang–DeTurck | as stated | See m3 |
| [6], [8], [17] (Thm 6.5, Rem. 2.7/(2.8)), [18] p. 579, [22] p. 67, [28] Lemma 6.6.4, [33], [36] | — | Not reachable headlessly; not verified (m4) |

The bibliographic metadata of all 50 references match Crossref or DataCite.

## FATAL

None.

## MAJOR

None. The two things that most limit what a reader can check are the dependence of Section 7's evidence on the companion paper (m7) and the computer-assisted certificate (m8). Given how the paper hedges both, I list them as minor.

## MINOR

**m1 (pp. 5, 30–31): Garbin–Jorgenson pinpoints.**
- I verified [16]'s numbering only against the 2016 arXiv version. Please confirm it matches the published L'Enseignement version.
- I could not reach [17] (Kodai) to check Thm 6.5 or Rem. 2.7/(2.8). Its abstract places small eigenfunctions and eigenvalues in the companion article, i.e. [16]. Please re-check which paper is the right source for the pointwise counting statement.
- [16, Ex. 5.8] itself misdescribes G_N as having elliptic points of orders 2, 3 and N. The manuscript's version (orders 2 and N, one cusp) is correct; consider noting the misprint.

**m2 (p. 2): Uçar pinpoint.** The relevant result is [2, Cor. 4.21(iv)], which Uçar phrases as "κ together with the spectrum". "The heat invariants alone" is justified only through Thm 4.20. Cite (iv), and add "via [2, Thm 4.20]".

**m3 (p. 6): [31] is understated.** Chang–DeTurck conclude that the triangles are *congruent*. Replace "isospectral" with "congruent".

**m4 (pp. 2, 5, 32): citations I could not verify.**
- Pinpoints: [8, (1.1)] and the conjecture at pp. 523–524; [5, Cor. 3]; [6]; [18, p. 579]; [22, p. 67]; [28, Lemma 6.6.4]; [33, 13.3.4–6].
- Buser–Courtois is the closest prior work, and Problem 1 is framed as an analogue of their conjecture. Quote their hypothesis (injectivity radius) and the conjecture exactly.
- If Hejhal was not consulted directly, write "as quoted in [16, Ex. 5.8]".

**m5 (pp. 1, 3, 13): rounding in the prose.**
- The smallest δ is 2.48e−6, so "about 2×10⁻⁶" should read 2.5×10⁻⁶ (abstract and p. 3).
- On p. 13, 10^{29325.4} is about 2.5×10^{29325}. Harmonise this with the "3×10^{196}" quoted elsewhere, which is actually 3.4×10^{196}.

**m6 (p. 5): "the orbifolds of Theorem 1.2 escape it" is inaccurate.**
- O(2,3,m) lies in C(π/3, ℓ_{2,3}, m), where Theorem 4.4 gives D of order m³, far above log(m/2π).
- So the family does not violate Theorem 4.4. What it escapes is any diameter bound that depends on (A, ε) alone.
- Rephrase, as p. 12 already does.

**m7 (pp. 23, 25): convergence evidence sits in the companion's supplement.**
- The evidence for the eigenvalue error estimates (h^{13} to h^{19}, geometric in p) is only in the supplement of [4], which I could not see.
- Include, in this paper's supplement or deposit, the convergence data for the eigenvalues used: at least λ_1–λ_40 of Table 7, plus a sample near λ_c.

**m8 (p. 16): the certificate.**
- Prop. 6.5 is computer-assisted, and I could not run certified_gap.py.
- My independent, uncertified recomputation reproduces Tables 3–4 exactly.
- The archived code, data and enclosure radii should be available to the editor before acceptance.
- The tail bounds on p. 16 are correct (1/(2θ_min) ≤ 1.91 for M ≤ 12).

**m9 (p. 18): an unproved growth claim, and a dropped factor.**
- |b_K(M)| ~ K^{−1/2} K! (M/π)^{2K} is cited to [4, Lemma B.3] and is not reproved here. Label it heuristic, or give the short argument from the poles of Φ_M at ±π/M.
- "t_1 ≈ δ_k/Q(k−1)" drops the factor 4 in the definition of t_1.

## Presentation, figures and cross-references

All tables match their captions, and all internal cross-references point to the right places.

- **P1 (Fig. 1, p. 19):** only the N = 21 window is shaded. For N = 100 the corresponding window (about 0.025–0.055) is larger and unshaded. Add "for N = 21" to the caption.
- **P2 (Fig. 2, p. 27):** the marker key is only in the running text. Put it in the caption or a legend. Also note the index offset: diamonds count N+1 eigenvalues, while squares and N_obs count N. The plotted values agree with Table 8.
- **P3 (Fig. 3):** consistent with the text; no change needed.
- **P4: overloaded notation.**
  - ϵ_j versus ε.
  - ℓ as systole and as interval length in the proof of Prop. 8.3.
  - a as the coefficients a_l, as the quadrilateral parameter, as the cut point in Prop. 8.3, and as a matrix entry in Lemma 8.1.
  - A as area bound and as a matrix in Lemma 8.1.
  - δ versus δ_k.
  - Λ, Λ_N, Λ_c, Λ_o.
- **P5 (p. 2):** "whose singular points are cone points" is redundant for closed orientable 2-orbifolds.
- **P6 (Table 8):** write "0.084" as 0.0840 for consistency.

## What is good

- Every proof I traced is complete.
- Each main result (Thm 6.2, Prop. 6.5, Thm 1.2 / Cor. 8.5) depends only on results proved in this paper. The diameter bound is used in no main proof, as the paper states.
- The paper is unusually candid about the limits of its claims:
  - Section 7 is presented as an illustration;
  - the errors ϵ_j are presented as estimates;
  - completeness is described as supported, not proved;
  - the growth rates are described as properties of the formulas;
  - the λ_j → 1/4 statement is made conditional on Garbin–Jorgenson's condition (b).
- Every constant in Tables 2–6 and the Prop. 6.5 certificate can be reproduced from the printed formulas.
- Prior work is attributed accurately, and in the case of the Hecke groups more accurately than in the cited source.

## Recommendation

**Minor revision.** Confidence is 4/5 overall: high for correctness, moderate for the paywalled pinpoint citations in m4.

## What resolves each issue

| Issue | Resolution |
|---|---|
| m1 | Confirm [16] numbering in the published version; re-check [17, Thm 6.5] against [16]; optionally note the G_N misprint. |
| m2 | Cite [2, Cor. 4.21(iv)] via Thm 4.20. |
| m3 | Change "isospectral" to "congruent". |
| m4 | Quote [8] exactly; mark the Hejhal page as quoted via [16]; confirm the other pinpoints. |
| m5 | Change 2×10⁻⁶ to 2.5×10⁻⁶; harmonise the rounding on p. 13. |
| m6 | Rephrase "escape it". |
| m7 | Add the eigenvalue convergence data to this paper's supplement or deposit. |
| m8 | Make the certificate code, data and radii available to the editor. |
| m9 | Mark the b_K growth as heuristic or prove it; restore the factor 4 in t_1. |
| P1–P6 | Caption and notation edits as listed. |

Code and intermediate files are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/B-e-citation-and-claims-auditor/scratch/: code/consts.py, code/gaps.py, code/extra.py, code/checks2.py, code/checks3.py, code/k3.py and code/cr.py; fetched sources in src/; rendered pages in pages/ and hi/.
