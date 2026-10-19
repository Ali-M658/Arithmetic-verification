<!-- Round 8 A-e referee report: returned text saved verbatim; the reviewer could not write files -->

I could not save REPORT.md because the tool refused the write, so the full report is below as instructed.

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (submitted to AGAG)

**Role:** referee for rigour, citations and figures. I checked each lemma and proposition line by line, each citation at statement level against its fetched source, each figure and table against its caption and the text, and the cross-references. Page numbers are those of the PDF. The marked placeholders are treated as known.

## 1. Summary

The paper studies closed orientable hyperbolic 2-orbifolds with cone points (the class Sig). It asks how many heat invariants c₁,…,c_k are needed to determine the signature, meaning the genus and the cone orders.

The geometric input has two parts:
- a closed-form heat expansion at curvature −1, derived from the Selberg trace formula, with enveloping remainders (Prop. 2.8, Prop. B.2);
- Uçar's triangular structure (Lemma 2.11): each new coefficient brings in exactly one new odd power sum of the cone orders.

Everything after that is a moment problem for signed multisets. The main results are:
- **Bounded cone orders (Thm 3.11).** If every cone order is at most M, then M invariants suffice within that class and M+1 suffice against all of Sig. Both numbers are sharp.
- **Growth (Thm 3.18, Prop. 3.19).** The worst-case count f(A) lies between about √A and about A. Lower bounds f(A) ≥ cA^α are equivalent to bounds N(k) = O(k^{1/α}) for the Prouhet–Tarry–Escott (PTE) problem.
- **Algebra of a collision (Thm 3.3, Thm 3.15).** The determinant of the recovery system has a closed Orlando–Hurwitz form, and a Descartes-rule argument bounds how much a change of genus costs.
- **Triangle orbifolds (§5).** Three invariants always suffice. Two first fail at O(2,8,8) and O(3,3,12), and this pair is isolated by the rank-0 elliptic curve C₂₇/₂.

The paper also contains a variable-curvature section (§2.4), a stability analysis (§6 and Appendix C), and numerical illustrations (§4, supplement S4–S6).

## 2. Significance

The paper is careful and candid about what is new. Its main contributions are:
- the exact, area-independent answer M+1;
- the closed-form determinant;
- the triangle-orbifold classification together with its arithmetic isolation;
- a clean reduction of the growth question to the PTE quantity N(k).

The heat-theoretic input is thin. Once Uçar's Lemma 2.11 is in place, almost everything is about odd power sums. Theorem 1.2 is, as the authors say, a reformulation in terms of an open problem and does not settle it. Whether this is enough geometric content for AGAG is the editor's call; I do not count it against correctness. The variable-curvature section is closest to the journal's scope and is also the least rigorous part (see M2 and M3).

## 3. Correctness, and what I recomputed

Unless stated otherwise, all checks below are independent and in exact arithmetic (sympy and Python fractions). **I found no mathematical error in anything a main result depends on.**

**Analysis (§2, Appendix B)**
- Lemma 2.7:
  - The closed form was checked numerically for m = 2, 3, 7, and series (4) against the Taylor coefficients of the defining sum.
  - Positivity and monotonicity of φ_k were confirmed.
- Proposition 2.8, (5), (8) and Lemma 2.9:
  - I recomputed p₀,…,p₄ and confirmed p_l(1) = 0, degree 2l+2 and the leading coefficient.
  - α₀,…,α₅ = 1, −1/3, 1/15, −4/315, 1/315, −4/3465 are correct, confirmed also by direct numerical integration of the identity term.
  - The cone series was compared with numerical integration of E_m for m = 3 and 12. The remainder has the predicted sign and is at most |b₄|t⁴.
- Formula (10) and c₂ = χ/6 + Σ(m²−1)/12m are correct.
- For the minimal pair, d₃ = 25/12, d₄ = −1775/24 and d₅ = 153025/48 are correct, and c₂ = 67/48 for both orbifolds.
- Appendix B: the beta-integral moments, the sign and modulus bookkeeping in Proposition B.2(a) and (b), and the counting argument in Lemma B.1 are all correct.
- Lemmas 2.4 and 2.5 are correct: the integration by parts, the integral bound, C_hyp, the time range, and the logarithmic derivative in ℓ. Proposition 4.2 is correct.
- Remark 4.3: the Fourier identity was checked numerically. Proposition 2.12 is correct.

**Variable curvature (§2.4)**
- At constant curvature β_{l,l+1} = (2l)!/l!·K^l (checked for l ≤ 4). The coefficient of m^{2l+1} is consistent with the leading coefficient of p_l.
- The leading coefficient of mΠ_i is correct.
- Remark 2.14(b): the K³ coefficient equals p₃(m)/m, and the Δ²K coefficient equals mΠ₄(m) (agreement to about 10⁻³⁷). The −m⁵ΔK/15120 term agrees with Schueth.
- I redid the Duhamel computation behind Proposition 2.13(iii) by hand.
- In Proposition 2.15(ii), I re-derived ω₂,…,ω₆ = 1/30, −1/140, 1/1260, −1/16632, 1/288288. As an independent check, ω₃ matches the −(1/280π)∫|∇K|² term of Gilkey's a₆ coefficient.
- The examples in Proposition 2.15(ii) and (iii) check out.

**Moment problem (§3)**
- I read line by line: Lemma 3.1, Theorems 3.2 and 3.4, Lemma 3.6, Theorem 3.7, Corollary 3.8, Lemma 3.10, Theorem 3.11(i)–(iv), Corollary 3.12, Lemma 3.14, Theorem 3.15 (the Descartes gap count), Proposition 3.16, Theorems 3.17 and 3.18, Proposition 3.19, Lemma 3.20, Lemma A.1 and Proposition A.2. All are correct.
- Theorem 3.3: det M = ς_n Π_{i<j}(m_i+m_j)/Π_i m_i was verified symbolically for n = 2,…,5. Lemma C.1 (B = YM and det B) likewise.
- Theorem 3.11:
  - The weights, the M = 3 and M = 4 examples, and the least-genus areas 2π·(2, 6, 18, 190, 442, 3998, 8838, 77054) are correct.
  - Example (iv) checks out: C = 180, ν = (10, −4), s = 2.
- An exhaustive search of 4-multisets with orders up to 130 gives 16 primitive witnesses, 8 of them with orders up to 84, and no triples. This agrees with the supplement and with Chen.
- Every explicit pair in Table S1 (L = 2–7: genus, equal-count, cone-count, and the L = 2, 3 Prouhet rows) has the stated area and shares exactly L invariants. Table 2 and Example 3.21 are confirmed.
- The real partner triple in Remark 3.22 is correct.
- amp₀,…,amp₄ = 2, 14, 498, 4062, 56230/3 and P₃ = −18c̃₁ − 120c̃₂ − 360c̃₃ are correct.
- ζ₃, ζ₄, ζ₅ = 1, 79/3, 14048/15 are correct.
- δ_thm, recomputed from Theorem C.4 for six multisets, matches Table S4 under its round-down convention.
- Remark B.4: Q₃ = 303.63, δ₁ = 4858·t₃, t₃ ≤ 7.82×10⁻¹¹, and η ≤ 2.071×10⁻¹⁹ at t₃ = 10⁻¹¹ are correct.

**Triangle orbifolds (§5, Appendices D and E)**
- Every gap value is correct: 1/840, 1/2310, 1/10296, the seven negative values at S*(p)+1, and the closed form for gap_p(3p+7), checked for p = 9,…,14.
- S*(p) was confirmed by brute force for p ≤ 14.
- There are exactly 83 hyperbolic triads with 10 ≤ S₁ ≤ 18, and the only coincidence among them is the minimal pair.
- Theorem 5.8:
  - The map ψ sends E into C₂₇/₂, verified symbolically. The discriminant is 2¹⁸3⁸5⁶, and #E(F₇) = #E(F₁₁) = 12.
  - The listed points, the flex (16, 400) with tangent y = 21x + 64, and φ(1:4:4) = (−24, 360) all check out.
  - E is isomorphic to LMFDB curve 90.c3 with u = 2 (rank 0, torsion Z/2 × Z/6).
- Appendix E: every congruence in the 2-isogeny descent is correct, giving n₁ = 4, n₁′ = 1 and rank 0.

**Stability (§6, Appendix C).** Theorems C.2–C.4 and Propositions 6.3 and 6.4 are correct, apart from one omitted step (m8).

**Figures.** I checked all eight from rendered page images:
- Fig. 2: marker positions and multiplicities are correct.
- Fig. 3: points match Table S1, and the step curves match Corollary 3.8 and Theorem 3.18(a).
- Fig. 4: the square-root axis is correct.
- Fig. 5(b): emergence times are t = ℓ²/98, consistent with ℓ²/4t ≈ 24.5.
- Fig. 7: dots and circles match Table S2.
- Fig. 8: the slopes and the δ_cert diamonds match Table S4.
- The flat-cone values quoted with Fig. 1 are correct: 1.78 at distance √t/sin(π/12), and below 0.03% beyond three times that distance.

## 4. FATAL issues

None.

## 5. MAJOR issues

**M1. Overstated claim in the abstract and on pp. 3 and 50.** The abstract says reading c₃ with a proved error "needs t of order 10⁻¹¹", and p. 3 says it works "only for t ≲ 8×10⁻¹¹ and values accurate to about 10⁻¹⁹". These numbers come from the authors' own choices:
- the three-node scheme (t₃, t₃/2, t₃/4) of Lemma B.3;
- the target δ_thm(2,8,8) = 3.80×10⁻⁷, which the paper itself calls "far from sharp" (p. 44).

With the paper's own certificate, δ_cert = 2.341×10⁻³ (Proposition S3.1, which Corollary 6.5 explicitly permits), the same lemma gives t₃ ≤ 4.8×10⁻⁷. I recomputed this; it is four orders of magnitude larger. Nothing in the paper proves a lower bound on the time scale that every method would need, so "needs" is unsupported.

**M2. Proposition 2.13 has only an outline proof (pp. 15–17).** The paper says three steps are "not carried out in full":
- Donnelly's reduction to (I − dΦ_p)⁻¹;
- the identification of the radial part of the jet;
- uniformity in ϑ of the inversion and of Laplace's method.

These are not routine; the second is exactly where the hypothesis m ≥ l − 1 enters. The machine checks cover only l ≤ 3 on rotationally symmetric germs, and the linear part for l ≤ 7. The Introduction (p. 6) nevertheless says §2.4 "identifies its coefficient". An outline should not carry the label "Proposition".

**M3. The "if" direction of Proposition 2.15(ii) is only sketched at its key computation (p. 19).** This is the basis of the claim that the counts "lose their meaning" in variable curvature. The formula for G_l(θ) is justified only by "in Fourier variables … completing the square … the displayed one". The formula is correct (I re-derived ω_n for n ≤ 6 and matched Gilkey's a₆), but the derivation belongs in the paper. The paper should also state that the O(θ³) remainder is uniform in the bump scale ε, since the argument rescales the bumps.

## 6. MINOR issues

- **m1 (p. 2).** "Lies at distance 2r sin(πj/m)" is the flat approximation. At curvature −1 the exact relation is sinh(d/2) = sinh r · sin(πj/m).
- **m2 (p. 9, ref. [5]).** The area formula is cited to Dryden–Strohmaier Thm 3.2, but that is Gauss–Bonnet. Cite "Def. 3.1 and Thm 3.2".
- **m3 (p. 6, ref. [6]).** "Proved independently by Doyle and Rossetti" does not fit the cited arXiv:1103.4372v2, which cites Dryden–Strohmaier as prior work. Either cite their 2006 preprint math.DG/0605765 for independence, or say "by a different method".
- **m4 (pp. 7, 24, ref. [28]).**
  - Steinig's theorem appears directly after the statement of Laurens's Lemma 3.2, not "before" it.
  - Laurens has no stated lemma of the form of Lemma 3.10. The sign-change idea appears inside the proof of his Lemma 3.2 (a total-positivity argument for the odd moments 3,…,2n+1) and in his Cor. 3.3. Rephrase accordingly.
- **m5 (pp. 16, 18, ref. [21]).** Schueth's equation numbers (6), (7), (13), (15), (16) are those of the arXiv version. In the published Ann. Inst. Fourier version they are (2.3), (2.4), (3.2), (3.4), (3.5).
- **m6 (p. 35, ref. [37]).** Garbin–Jorgenson's Thm 2.5 integrates over [0, ∞) with constant (1/q)·e^{−t/4}/√(16πt). On the whole line the constant against g_t is 1/(4q). Say "half-line", or note the symmetrisation.
- **m7 (pp. 7, 15, ref. [13]).** Fursaev's structural formula is his (3.26), not (2.8); (2.8) is the explicit second coefficient. Suggested pointer: "(3.26)–(3.28); (2.7)–(2.8) for the first two coefficients".
- **m8 (p. 51).** The proof of Theorem C.2(b) leaves out the Neumann-series step ‖M(Ĩ)⁻¹‖ ≤ 2·cond, which follows from cond·ζ_n·η ≤ ½.
- **m9 (p. 25).** In Theorem 3.11(iv), "m, m′ as in (ii)" must range over the orders {2,…,M, X}; part (ii) defines them over {2,…,M} only. Say so explicitly.
- **m10 (p. 39).** The proof of Lemma 5.3(ii) refers forward to parts (a) and (b) of the proof of Theorem 5.4. This is not circular, but say so, or reorder.
- **m11 (p. 18).** The proof of Proposition 2.15(i) uses Donnelly's weight-2l structure for every m. Cite [1, 40] or [2, §4] there, so it is clear the argument does not inherit the outline status of Proposition 2.13.
- **m12 (p. 14).** For K > 0, "from the polynomial dependence … on the jet" is not an argument. Cite Uçar [15, Thm 4.20], which covers every constant curvature.
- **m13 (pp. 9, 13, ref. [2]).**
  - The formula c₂ = χ/6 + Σ(m²−1)/(12m) is in DGGW Example 5.6, not Example 5.3.
  - Say that this paper's c₂ is the t⁰ coefficient of the heat trace; DGGW's own c₂ in (4.9) carries an extra factor 4π.
  - Check the DGGW erratum (Michigan Math. J. 66 (2017) 221–222) and cite it if it affects their §5.
- **m14 (p. 7, ref. [15]).** Uçar's Cor. 4.23 determines only χ(O) and χ(X_O); the cone orders come from his Cor. 4.21(iv).
- **m15 (p. 28, ref. [45]).** Croot–Mao–Yip write P(k,2) for what the paper calls N(k); say so.
- **m16 (pp. 8, 30, 41).** I could not check Borwein–Lisoněk–Percival pp. 2064, 2069 or Bremner–Guy–Nowakowski p. 117, because AMS blocks headless downloads. The BLP abstract mentions Letac but not Gloden. The authors should confirm these page-level attributions.
- **m17 (p. 50).** Explain that µ₀ = 12 is the a-priori order bound chosen to cover the competitor O(3,3,12); as written it reads like a property of O(2,8,8).

All other cited statements checked out at statement level against their sources: Dryden–Strohmaier eq. (1), p. 68, Thm 1.1 and Prop. 3.3; the Garbin–Jorgenson normalisation; Linowitz–Voight Thm A; Holtz–Tyaglov (1.37) and Thm 1.17; Melánová–Sturmfels–Winter Prop. 24; Chen's (A.685)–(A.692), Identity 9, (3.33), A.1.6/17/26/33 and §8.1; Borwein–Ingalls pp. 6–10, 25, Props. 2–3 and §6; Coppersmith et al. (5) (checked in the arXiv version); LMFDB 90.c3; Cremona §3.3 and §3.6; Uçar Thm 4.20, (4.25), Thm 3.40 and the quoted phrase; DGGW Thm 4.8, (5.13), Rem. 5.16 and Thms 5.14–5.15; Schueth's theorems and remarks; Thurston 13.3.4–13.3.7; Dryden [52]; Abreu et al.

## 7. Presentation

- **P1.** In Fig. 3, the filled diamonds mix genus pairs, equal-count pairs and cone-count pairs and cannot be told apart. Several overlap near s ≈ 7 and s ≈ 18.
- **P2.** The letter a is used for the Lagrange nodes, for a_l and for a_{l,k}. Rename the nodes.
- **P3.** Interpretive sentences ("So the growth is carried by …") sit inside the statements of Theorem 1.1(iii) and Theorem 1.2. Move them out of the theorem environments.
- **P4.** Orlando's formula (11): note that the sign (−1)^{n(n−1)/2} in Holtz–Tyaglov cancels because the zeros of χ_m are −m_i. The sign matters in Theorem 3.3 and Lemma C.1.
- **P5.** In Remark B.4 and on p. 3, the times "t₃, t₃/2, t₃/4" clash with the indexing of Lemma B.3. Use τ, τ/2, τ/4.
- **P6.** On pp. 5–6, the paragraph beginning "What the two papers share …" is hard to parse. A short list of what the companion paper reproves would be clearer.

## 8. Recommendation

**Minor revision**, close to major because of M2. My confidence is about 0.85 on correctness, and moderate on the recommendation, since that also depends on the editor's view of fit with AGAG.

Every main result is correct, and the parts I recomputed independently all agree with the paper: the expansion and its remainders, the determinant, the separation, sign-change and Descartes arguments, the growth equivalence, the strata, the descent and torsion, the stability constants, and all pairs in Table S1. Figures and tables match their captions. Citations are accurate in substance, apart from the location and wording fixes in m2–m7 and m13–m16.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Drop "needs" from the abstract. Present the time scale as a property of the Lemma B.3 scheme at target δ_thm, and also quote the δ_cert threshold, t₃ ≲ 4.8×10⁻⁷. |
| M2 | Either supply the three omitted steps, or relabel 2.13(i)–(ii) as a conjecture supported by Remark 2.14, keeping (iii) as a proposition. Adjust the wording on p. 6. |
| M3 | Write out the Fourier/Duhamel computation, including ∫₀¹(a(1−a))ⁿ da = (n!)²/(2n+1)!, and the uniformity of the O(θ³) remainder in ε. |
| m1 | Give the hyperbolic relation, or say "approximately". |
| m2–m7, m13–m16 | Fix the citations as listed. |
| m8 | Add the Neumann-series line. |
| m9 | State the range of m, m′ explicitly. |
| m10 | Note that the forward reference is not circular, or reorder. |
| m11, m12 | Add the citations given. |
| m17 | Explain the choice of µ₀. |
| P1–P6 | Make the editorial changes described. |

The scripts and downloaded sources are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/A-e-lemma-by-lemma-verifier/scratch/` (`code/`, `cites_A/`, `cites_B/`, `cites_C/`, `img/`).
