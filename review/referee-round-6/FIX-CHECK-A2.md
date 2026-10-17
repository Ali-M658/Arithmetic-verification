# FIX-CHECK-A2: revision check of Paper A against VERDICT-A (referee round 6)

Inputs used: `fix-check-A2/scratch/input/` only (A-manuscript.pdf 55 pp., A-supplement.pdf 16 pp., VERDICT-A.md, B-manuscript.pdf, N-note-integers.pdf). Pages were rendered (pdftoppm) and read wherever a formula, figure or sign is at issue. "p." means the page of A-manuscript; "S p." means the page of A-supplement.

Recomputed for this check (Python, mpmath/sympy):
- **(6) / A1 counterexample:** for (2;2) at t = 0.05, the remainder after c1, c2 is 1.07754e-3, which is larger than c3·t = 1.04167e-3. The statement on p.11 is correct.
- **Prop. 2.11:** the Duhamel constant gives λ_l = 2/(l−1)!. At constant curvature β_{l,l+1} = (2l)!/l!·K^l, which agrees with β_{1,2} = 2K, β_{2,3} = 12K², β_{3,4} = 120K³ and with Lemma 2.8.
- **Theorem B:** det M = ς_n ∏(m_i+m_j)/∏m_i holds exactly for random integer m, n = 2..6.
- **Theorem 5.8:** ψ maps E into C_{27/2} and φ∘ψ = id on the torsion points. φ(1:4:4) = (−24, 360), disc(E) = 2^18·3^8·5^6, and the tangent at (16, 400) meets E with multiplicity 3.
- **Remark B.4:** with times t3/4, t3/2, t3, δ1 ≈ 4.86×10³·t3, and η ≤ 2.07×10⁻¹⁹ at t3 = 10⁻¹¹. Both agree with the text.
- **Table S6:** the recovery from the printed estimates gives roots 2, 8 ± 0.0050i and 2.99154, 3.00851, 11.99995.
- **Closed-geodesic term of O(3,3,12):** ℓ = 1.862604. Per oriented class the term is 3.9×10⁻¹³ at t = 0.03, so with the two orientations it is 7.8×10⁻¹³ at t = 0.03, 2.6×10⁻¹⁵ at t = 0.025 and 2.5×10⁻⁴ at t = 0.1.
- **Small checks:** Prop. 2.13(ii) example, Examples 3.6 and 3.17(i)–(ii), the Theorem 3.8 examples, amp₀..amp₂ = 2, 14, 498, the formulas of Prop. 6.3(i)/6.4, d3 and d4, c1..c3 of the minimal pair, the Table S2 columns, the 83 triads of Table S3, and the δup/δthm range 5×10²–2×10⁸. All agree.

## 1. MAJOR items

| id | status | evidence (new PDF) |
|---|---|---|
| A1 | RESOLVED | p.5: the two series have enveloping remainders, "for the heat trace, where the two remainders have opposite signs, this gives the explicit bound (6), not an enveloping series". p.11: (6) now has the bound t^K·max(Area/4π·\|α_{K+1}\|, Σ\|b_K(m_i)\|) and says the truncation holds α_0..α_K and b_0..b_{K−1}. It also states that the trace is not enveloped, with the (2;2), t = 0.05 example (recomputed above). p.46 Prop. B.2 gives the opposite signs and "in particular (6) holds". |
| A2 | RESOLVED | p.11: Schueth is now cited correctly. Her note (without proof) says integrality plays no role, the coefficients are rational in the angle, and a different form arises only when the cone is not smooth to second order [22, p. 2]. The physics computations are cited as [13, (3.26)–(3.28)] (Fursaev, PLB 334) and [14] (Dowker, CQG 11), also on p.6. Fursaev–Solodukhin is not cited; this is optional. |
| A3 | RESOLVED | pp.14–15, proof of Prop. 2.11. It has a "Rotation invariance" paragraph (frame rotation ρ fixes dΦ_p), a "Pole order" paragraph (deg P ≤ 2l, computation of X_l) and a "Radial reduction" paragraph (weight ≥ 2m+4 > 2l for m ≥ l−1). Part (iii) now uses the compactly supported ψ = χ0\|x\|^{2l}, so the trace-class step is justified and the cut-off costs O(t^∞). p.17, Prop. 2.13(ii): the bumps lie in the flat disc D1 and change neither the cone terms nor Ω0 (Gauss–Bonnet); one θ is fixed with G_l(θ) ≠ 0 for all l ≤ L; shrinking keeps the bumps in D1. p.16 Remark 2.12: rests on computer algebra and is used nowhere else. |
| A4 | RESOLVED | p.28: the open squares are "the genus pairs of the proof of Theorem 3.14(c) built from the Prouhet–Thue–Morse solutions, with c = −1/2 and c′ = 1/2, for L = 2..6". The p.29 caption reads "lower bounds from constructed pairs (diamonds and squares)". Table S1 (S pp.3, 6) defines T_e, U0, V0, A′, B′, prints the L = 2, 3 rows in full, and gives SHA-256 checksums plus the CSV for L ≥ 4. The squares on p.29 sit at s ≈ 2.4, 15, 63, 255, 1023, as in Table S1. |
| A5 | RESOLVED | Abstract p.1: "within a distance of order √t of a smooth point, and within about √t/sin(π/m) of a cone point of order m". p.2 adds the chart-image fact 2r sin(πj/m). p.3 says the paper "counts coefficients of an asymptotic expansion, not lengths of time" and gives the two scales, (π/12)² ≈ 0.07 against ℓ²/4 ≈ 0.87. The wave-trace picture is now Remark 4.3 (p.32). The Fig. 1 caption no longer says "within a distance of about √t". |
| A6 | PARTLY | Resolved parts: pp.4–5 now lead with the area-free results (Theorem 1.1, Corollary 1.5) and call Theorem 1.2 "a reformulation". Thm 1.1(ii) says "M+1 cannot be lowered uniformly in the area … some pair, of large enough area". Theorem 3.4 is called "the analogue … of the classical bound N(k) ≥ k+1" (pp.5, 7). **Not done:** Lemma 3.7 (p.22) is still uncited; it is only called "the mechanism behind Descartes' rule of signs". Add a citation to a standard source for the sign-change lemma (e.g. Pólya–Szegő, *Problems and Theorems in Analysis II*, Part V; check the exact problem number against the record). |
| A7 | RESOLVED | Lemma B.3 (p.47) gives a proved δ1 from finitely many trace values under a-priori bounds. Remark B.4 (p.47) shows how demanding this is; its numbers were recomputed above. Corollary 6.5 (p.41) requires "a proved bound … an estimated δ1 gives no conclusion". The approximate-data claim is no longer in the abstract, and the introduction (p.5) cites Lemma B.3. |
| A8 | RESOLVED | p.6: "the classical form of locality, due in substance to Selberg, Huber and McKean, with an explicit constant". p.29: the fact that heat invariants do not see the moduli "is classical in substance [38, 51]". p.30 says Prop. 4.2(b) "is classical in substance". The phrase "Three analytic results carry the counts" is gone. |
| A9 | RESOLVED | The constants and proof of Theorem 6.2 are in App. C (Lemma C.1, Thms C.2–C.4, pp.47–49). The former Prop. S2.2 is now Prop. D.1 (App. D, p.49). The descent is in App. E (pp.49–50). The supplement abstract (S p.1) points to them. |
| A10 | RESOLVED | p.6 says exactly what is shared with B. pp.7–8: the S ≤ 4800 enumeration "is the same computation as the note's, restricted to that range", and "Theorem 5.8 is proved here because it is the isolation statement of Theorem 1.4(iii)". p.37: the note's two results are cited "by arguments used nowhere here", and "No proof in this paper depends on these statements". Caveat: the verdict's reason "the note cites it" does not hold (see §3, item X3). |

## 2. MINOR and presentation items

| id | status | evidence (new PDF) |
|---|---|---|
| a1 | RESOLVED | p.11: (6) with the max bound and the exact list of included terms. |
| a2 | RESOLVED | p.13: the K^l rule "follows from Proposition 2.7 by the weight argument in the proof of Proposition 2.13(i)". p.17, proof of (i): b_l(p) is a weight-2l polynomial, the constant is fixed by Prop. 2.7, and [15] is cited only "in agreement". |
| a3 | RESOLVED | p.16, last paragraph of Prop. 2.13. It lists which conclusions survive (Thms A, 3.4, 3.11, 3.8(i)/(iii), Cor. 3.5) "for the given L", with Area read as −2πχ, under Ω_l(O) = Ω_l(O′). It adds that c1 does not determine χ and that the number in Cor. 3.5 is "not computable from c1". |
| a4 | RESOLVED | p.13: "for closed orientable orbifolds with χ ≥ 0, those of curvature 0 and +1, the single invariant c2 already determines the orbifold type [2, (5.13), Thms 5.14–5.15]". |
| a5 | RESOLVED | p.9 Lemma 2.4: n_O counts "hyperbolic conjugacy classes, primitive or not". p.30: w_O counts "the classes of γ and γ⁻¹ … separately". |
| a6 | RESOLVED | p.45: the trace formula's admissibility conditions are cited [38, 39], then "for completeness, here is the standard approximation argument". |
| a7 | RESOLVED | p.12 Remark 2.9 gives Uçar's normalisation of c_{S_k} explicitly. |
| a8 | RESOLVED | p.16 Remark 2.12(c): "The coefficients of K∆K in (b) below the top one rest on this single computation". |
| a9 | RESOLVED | S p.15, S7(ii): "every prime used exceeds every entry of V, so it divides no denominator of R(V)". It also skips p when 3(1 − e1R) ≡ 0. |
| a10 | PARTLY | p.32 states one window: t ≤ 0.025 at 4×10⁻¹⁴, with the geodesic term "not subtracted". S p.11 agrees: 3.4×10⁻¹⁴ on [0.0015, 0.025], fit window [0.0015, 0.012]. **The values near t = 0.03 disagree with each other** (see §3, item N4). |
| a11 | PARTLY | Fixed: S p.10 now calls the second difference "a second estimate … neither is a bound". **Still present:** "conservative" on S p.12 (Limitations: "agrees within the conservative error estimate") and S p.14 (S6: "8.3 × 10⁻⁹ conservative"). Replace with "the second estimate" in both places. |
| a12 | RESOLVED | p.43 qualifies "one command": "except two long computer searches and the finite-element solves". S7 (S p.15) gives the versions (SciPy 1.18.1, NGSolve/NETGEN 6.2.2607, PARI/GP 2.17.2) and names the programs and files, including those behind Table S1. S5 (S p.12) describes the dated protocol (1 October 2026). |
| a13 | RESOLVED | p.7: the weights are recovered "from the spectra on functions and on 1-forms, or from the spectrum on functions and the Euler characteristic [20, Thm 1 and §6.1]". |
| a14 | PARTLY | p.28 lists the sources only collectively: [4], [50] (Borwein–Lisoněk–Percival), [49, (5)], and [31] A.1.17/26/33 with discoverers. The S1 recipes and Table S1 do not attribute each piece. For example, the L = 6 genus piece ±{18, 245, 331, 471, 508} / ±{103, 189, 366, 452, 515} is not tied to [50]. Add a source to each recipe in S1. |
| a15 | RESOLVED | p.7: Chen's Identity 9 is "stated there for integer sets". p.20 Thm C(1): "an odd symmetric system in the sense of [4, §3]". p.42 Problem 4: "In the notation of [31] … type (−1, 1, 3, …, 2n−5)". |
| a16 | PARTLY | Fixed: "wrote in 1994" is gone, and [10] and [14] read "Dowker, J.S.". **Remaining:** (i) [23] (p.52) lists the editor as "Gier, J."; it should be "de Gier, J.". (ii) [9] reads "Dowker, S." while [10] and [14] read "Dowker, J.S." for the same author; keep "S." only if the CMP 182 record has it. (iii) [14] gives pages "137–140"; this is a CQG letter, so they should be "L137–L140". |
| a17 | RESOLVED | p.6: "the computed spectra of Section 4 and of the supplement". |
| a18 | RESOLVED | p.8 Table 1 has entries for T(L) ("before Prop. 3.15"), a_l ("from Thm 3.8(ii)") and T_g(L) ("Rem. 3.18"). |
| a19 | NOT RESOLVED | p.7: "only finitely many signatures have a given area (Corollary 3.5)". Corollary 3.5 (p.21) bounds only n + 4g, not the orders, and no finiteness line was added. The proof of Prop. 3.15 (p.27) also relies on "the set of areas of signatures is well ordered" without proof. Fix: add to the proof of Cor. 3.5 one line: "with n, g bounded, Σ 1/m_i = n + 2g − 2 − Area/2π is fixed, and an equation Σ_{i≤n} 1/m_i = r has finitely many solutions in integers ≥ 2 (order m_1 ≤ … ≤ m_n; then m_k ≤ (n−k+1)/r_k, with r_k the reciprocal sum still required), so only finitely many signatures have a given area, and the areas below any bound form a finite set". The same line also covers a32. |
| a20 | RESOLVED | p.41: "Its worst-case error, on the vertical axis, is the largest recovery error in the distance dist above". The axis on p.42 reads ‖m̃ − m‖_∞, which agrees with dist for matched multisets. The slopes 1, 1/2, 1/3, 1/2 match the figure. |
| a21 | PARTLY | "Schematic, not isometric" is said in the text (p.30) but not in the Fig. 4 caption (p.31). Suggested caption: "(a) Four members of the family (0; 3, 3, 3, 3), drawn schematically, with their shortest closed geodesics; …". This keeps two sentences. |
| a22 | RESOLVED | p.33: "ten times the error budget (a different threshold from the 10³ times the noise used for the ratio test in Section S6 …)". Style: this parenthesis is directly followed by a second one, "(the shaded region …)"; merge them or turn one into a clause. |
| a23 | RESOLVED | p.36: 101/168 = R⁻_{18,3} "attained at (3, 7, 8)", with the reason it is the maximum (parity monotonicity, R⁻_{19,3} = 7/12). (2, 5, S−7) is justified by "(as S − 7 ≥ 5)". |
| a24 | RESOLVED | p.16: (0; 2⁸) and (0; 3, 3, 3), "with χ = −2 and χ = 0: in variable curvature c2 does not determine χ". Both have c2 = 2/3, checked. |
| a25 | RESOLVED | The moments are now the fraktur 𝔪_n (p.45). ϱ no longer appears in App. B; it is used only for reciprocal sums (Lemma 3.16, Prop. A.2). In the proof of Prop. 2.11, κ denotes only the constant curvature. Table 1 and the global use of a and C are kept, as decided. |
| a26 | RESOLVED | Figs 3, 5 and 8 each have a two-sentence caption with a short first sentence (pp.29, 34, 42). |
| a27 | RESOLVED | p.13: "Section 3 is used only in Proposition 2.13, through Lemma 3.3, and only for its consequences". |
| a28 | RESOLVED | p.14 Prop. 2.11(i): "For m ≤ l − 2 nothing is claimed (Problem 5)". |
| a29 | RESOLVED | p.16 (i): "the direction from H_L(O) = H_L(O′) to (13) fails". |
| a30 | RESOLVED | p.3: f(A) is defined for A ≥ π/21. |
| a31 | RESOLVED | p.26: k+1 ≤ N(k) ≤ k(k+1)/2 + 1 [4, Props 2–3], Wright and Melzak, Problem 3 of [4, §6], [45, §1] (2026) and [31, §8.1]. |
| a32 | NOT RESOLVED | S p.6: the area classes were "enumerated exactly … with no bound on the orders", but neither the algorithm nor the a-priori bound on the orders at fixed area is given. Add the bound from a19, i.e. n + 4g ≤ 2s + 4 and the successive bound on m_k from the remaining reciprocal sum, together with a sentence on how the enumeration uses it. |
| a33 | RESOLVED | p.37 Thm 5.7: "every other collision has R < 3/4, hence area larger than π/2", with a proof by convexity and majorisation by (3, 3, S−6) (checked). The script is named in S7 (S p.16). |
| a34 | RESOLVED | p.5 and Thm 6.2 (p.40): "closed formulas except for one matrix norm, cond, which Theorem C.2(a) bounds explicitly". |
| a35 | RESOLVED | p.32 Remark 4.3 cites Duistermaat–Guillemin [55], Hillairet [56] and Ford–Wunsch [57]. |
| a36 | RESOLVED | p.44, proof of 3.14(b): "Kmult ≥ 3 by Theorem C(3)". |
| a37 | RESOLVED | p.26: "so that f(A) ≥ L+1 for A ≥ A_min(L)". |
| a38 | RESOLVED | p.20 Lemma 3.3: the criterion is (13) alone, and d with the paddings is a consequence ("Then d = …"). |
| a39 | RESOLVED | p.24 Def. 3.10: "Newton's identities force Z = −Z, which the absence of pairs {z, −z} excludes". |
| a40 | RESOLVED | p.25, proof of Thm 3.11: the gap count is spelled out (checked: at most (κ−2L)/2 nonzero odd coefficients, hence at most κ−2L mixed-parity gaps). |
| a41 | RESOLVED | p.19 Thm B: ς_n = (−1)^{n(n+1)/2}, with the Hurwitz normalisation [42, (1.37)] on p.18. Verified numerically for n = 2..6. |
| a42 | RESOLVED | p.26: "If β ≥ 1". p.44: C ≥ N(1) is not used, and Lemma A.1 is stated with n = (L−1)²+1 (pigeonhole checked). |
| a43 | RESOLVED | p.4 Thm 1.1(ii): "M + 1 cannot be lowered uniformly in the area". |
| a44 | RESOLVED | p.28: the pieces are classified (ideal or symmetric PTE solution, a pair with equal odd power sums, or the 7-element set for L = 4). |
| a45 | RESOLVED | S pp.3–6: exact s is printed for L ≤ 5 and is in the data file for L ≥ 6; SHA-256 checksums are given for the Prouhet cone lists. |
| a46 | RESOLVED | p.29 Remark 3.18: "the bound concerns the five-element side alone". |
| a47 | RESOLVED | p.28: Table 2 is numbered and captioned. |
| a48 | RESOLVED | p.30: non-isometry follows from λ1 differing by ≥ 0.15 ("a numerical, not a proved, statement"). The systoles 4b(ϑ) come "by a complete enumeration … in floating point". |
| a49 | RESOLVED | p.32 now says the agreement "tests the computed spectra against the trace formula, while the coefficients d3, d4 are tested by the fit". The phrase "tests every order" is gone. |
| a50 | RESOLVED | pp.32–33: "Heuristically, and without use in any proof …; we checked these numerically for m ≤ 12 and l ≤ 15, but do not prove them … What is proved is the bound (6)". |
| a51 | PARTLY | p.34 states K_mult(O(p,q,r); Sig) ≤ 3 as open ("we do not know"). The search that the disposition promised is not reported in the paper or in S7. Either add it (its range and its result) or drop "with the search" from the plan. |
| a52 | RESOLVED | p.39: ψ is a morphism (its coordinates never vanish together; ψ(∞) = (1 : −1 : 0)), and "φ∘ψ is the identity of E" (verified). |
| a53 | RESOLVED | S pp.7–8, Prop. S3.1: "entry τ_{2i+1} in row j, column e_{2j−2i}". The Table S4 caption reads "a real root, or a non-real complex pair, of real part a ± 1/2". |
| a54 | RESOLVED | S p.11: "For small t the orbifold with the smaller P3 has the larger heat trace (D(t) changes sign near t = 0.34)". |
| a55 | RESOLVED | S p.7 and p.37: it is now "Computation S2.1 … a computer enumeration and not a proof". |
| a56 | RESOLVED | p.40 Thm 6.2: "for n = 2 the statement is algebraic only". p.41 Prop. 6.4: "For n = 1, an algebraic case with no hyperbolic orbifold". |
| a57 | RESOLVED | Text only, p.37: dots and circles are drawn for p = 2..7, and they coincide only for p = 2 and 4. The Fig. 7 caption is two sentences, and the plot (p.38) has only axis titles and ticks. The p = 5 circle (S = 117) is inside the frame. |
| a58 | RESOLVED | p.38: φ is displayed. |
| a59 | RESOLVED | p.33: "the cap of points at hyperbolic distance at most 2.4 from a vertex, whose boundary circle appears as an ellipse". |
| a60 | RESOLVED | p.33: key₂ is defined in a display. |
| a61 | NOT APPLICABLE (reason holds only in part) | No change, as decided. The map linking the numberings is in the Organisation paragraph on **p.8**, not p.7. The stated reason, that renumbering "would break the cross-citations from Paper B and the note", does not hold as worded. B cites only Thm 2.3, Lemma B.1, Lemmas 2.4–2.6, 2.8, 2.10, 3.3, Cor. 3.5, Thm 3.8 and Prop. B.2, none of them 1.x, and the note cites no numbered result of A. The p.8 map is enough reason on its own; adjust the reason in the response letter. |
| a62 | NOT APPLICABLE (reason holds) | Every figure is kept and the captions are clarified (Fig. 1 "stylised"; Fig. 4 and Fig. 6 captions shortened). Each figure has only axis titles, ticks and panel letters (pp.2, 22, 29, 31, 34, 35, 38, 42). |
| a63 | RESOLVED | "explores … learns" and "heard late" are gone. Remaining are the abstract's "heat … feels the geometry" and "Other singular data heard by heat" (p.6), which are acceptable. |
| a64 | PARTLY | P5 (table of pieces) is done through the S1 recipes and Table S1. P2, P4 and P7 are unchanged as decided. For P3, Example 3.6 (p.21) still ends with the vague "a handle costs no more invariants than a cone point". Suggested replacement: "the change of genus costs nothing beyond the bound of Theorem 3.4: here 2L + 2\|g − g′\| = 2L + 2 = 6". |

The verdict's "Plan" asked for the A9 proofs to move into appendices. This is done (Apps C, D, E), and the supplement abstract points to them.

## 3. Cross-paper consistency

**B → A (B's Table 1, p.6, and bracketed locators).** Every locator points to the right result in the current A:
- B Thm 2.1 → [30, Thm 2.3, Lemma B.1]: matches.
- B Lemma 2.2 → A Lemmas 2.4, 2.5: matches.
- φ_k → A Lemma 2.6: matches.
- B Prop. 2.3 → A Prop. B.2: matches, including the 4π/Area normalisation and the signs (−1)^K, (−1)^{K+1}.
- Cone polynomials and the triangular basis → A Lemmas 2.8, 2.10: matches.
- B Lemma 3.1 → A Lemma 3.3: matches, including "d ∈ Z".
- B Thm 3.2 → A Cor. 3.5 and Thm 3.8(i): matches.
- B p.5, "Lemma 3.3 … direct consequence of [30, Lemmas 2.10 and 3.3]": matches.
- B p.18, "the convergence in h and p is tabulated in the supplement of [30]": matches Table S5.

B's (2) uses the sum bound Area/4π·|α_{K+1}| + Σ|b_K|. It is weaker than A's max bound (6) but correct, so there is no conflict. B could cite the sharper bound; this is optional.

**Numbers shared by A and B:**
- Systoles: 2.256767 and 1.862604 in B Table 4, against 2.2568 and 1.8626 in S p.12 and Remark B.4. They agree.
- Family systoles: 2.633915 to 0.693994 in B, against "2.634 to 0.694" in S p.14. They agree.
- Diameter: 2.448 in B, against D = 2.448 in Remark B.4. They agree.
- Eigenvalue counts: 2845/2854 and 2002/2001 below 1.6×10⁴, and about 5800 / 4357–4451, against "about 2850", "2002 and 2001" and "0.8 times the least sector maximum" in S p.10 and A p.6. They agree.
- Second estimate: 1.2×10⁻⁸ for the first 500 in both. They agree.
- A's description of B (p.6: N and δ explicit in area, systole bound and order bound; B adds a diameter bound, eigenvalue counting and cusp-like high orders) matches B.

**X1 (inconsistency).** p.6 says "the companion restates, **without proof** and with their places here, the results of Sections 2 and 3 it uses". B says the opposite on p.5 ("Appendix A proves them, so that this paper is self-contained"), in the Table 1 caption ("each proved in Appendix A") and on p.28 (App. A: "every proof this paper relies on is in it. The arguments are those of [30]"). Suggested correction for A p.6: "the companion restates the results of Sections 2 and 3 it uses, with their places here, and reproves them in its Appendix A by the arguments of this paper".

**A ↔ note.**
- The note's theorem letters are cited correctly: on p.37, "[35, Thms B and C]" are the note's Theorem B (lower bounds) and Theorem C (classes of every size).
- The constant 3/(128π⁴) and the form X(log X)² match the note's Theorem B.
- "Enumerates the collisions up to sum 6000" (p.7) and "the same computation … which extends it to S ≤ 6000" (p.37) match the note's §6.1 (two programs to 4800, a third to 6000).
- The note's 2-isogeny Selmer orders for C_{27/2} (4 and 1) match A's App. E (Selmer groups {±1, ±6} and {1}).
- Both papers say "nothing here depends on it".
- A's Theorems A–C share their letters with the note's Theorems A–E. Every citation is unambiguous because it carries the [35] locator, so no change is needed.

**X2 (overstatement).** p.37 says the note proves "that classes of every size occur infinitely often [35, Thms B and C]". The note's Theorem C says only that "for every k there are infinitely many primitive classes of size **at least** k". Suggested correction: "… and that for every k infinitely many classes have at least k members [35, Thms B and C]".

**X3 (verdict premise and missing cross-reference).** VERDICT-A A10 keeps Theorem 5.8 in A partly because "the note cites it". The note does not cite it. Note §5 (p.13) proves the same statement independently: "C_{27/2} has rank 0 … So {(2,8,8),(3,3,12)} and its multiples are the only coincidences with Λ = 27/2". This is not an error, but the overlap is undeclared on both sides. Either add to the note, after that sentence, "(this is also [9, Theorem 5.8], proved there by a hand descent)", or add to A p.8 "the note gives an independent descent". Also correct the reason in the response letter.

## 4. New problems (not in the verdict, or introduced by the fixes)

No "??", broken references or table/text count mismatches were found in A, the supplement, B or the note.

| # | where | problem | suggested correction |
|---|---|---|---|
| N1 | A p.6 | Says B restates the shared results "without proof"; B proves them (X1). | Text given under X1. |
| N2 | A p.37 | Overstates the note's Theorem C (X2). | Text given under X2. |
| N3 | Note §5 / A p.8 | Theorem 5.8 is proved in both papers without a cross-reference (X3). | Add the cross-reference given under X3. |
| N4 | A p.32 vs S p.11 | Three statements about t near 0.03 disagree. (i) A p.32: "up to t = 0.03 the difference grows to 4 × 10⁻¹³, the size of the closed-geodesic term of O(3,3,12)". (ii) S p.11 (Result): "at most 4.0 × 10⁻¹³ for t ≤ 0.03 … about 7.8 × 10⁻¹³ at t = 0.03". (iii) S p.11 (ii): each trace agrees with I + E "to 7.1 × 10⁻¹³" on [0.0015, 0.03], while the geodesic term (not subtracted) "reach[es]" 7.8 × 10⁻¹³ at t = 0.03. The geodesic term is 7.8 × 10⁻¹³ at t = 0.03 (both orientations; recomputed), 2.9 × 10⁻¹³ at t = 0.029 and 6.5 × 10⁻¹³ at t = 0.0298. So the bounds 4.0e-13 and 7.1e-13 "for t ≤ 0.03" can only hold if the sampled grid stops before 0.03, and the two grids must then differ. | State the last sampled time. A p.32: "(at the last sampled time, t ≈ 0.029, the difference is 4 × 10⁻¹³, the size of the closed-geodesic term of O(3,3,12) there, which is not subtracted)". S p.11: change both "for t ≤ 0.03" to the actual largest sampled t, or quote the deviation at t = 0.03 (≈ 7.8 × 10⁻¹³). |
| N5 | A p.33 | "beyond t ≈ 0.1 the closed geodesics take over". At t = 0.1 the geodesic part of D is about −2.5 × 10⁻⁴, against D ≈ 0.047 (0.5%). It becomes comparable only near t ≈ 0.3 and reverses the sign of D near t ≈ 0.34 (S p.12). | "beyond t ≈ 0.1 the closed geodesics become visible, and near t ≈ 0.34 they reverse the sign of D". |
| N6 | A p.32 | Remark 4.3 (new, from A5) sits between "The sharp part, the exponent and the factor t^{−1/2}, is classical …" and "The constant of (a) is not: …". "is not" has lost its antecedent. | Either move Remark 4.3 after that paragraph, or begin it with "The constant C_hyp of Proposition 4.2(a) is not sharp: …". |
| N7 | A p.7 / p.21 / p.27 | Finiteness of signatures of a given area is attributed to Cor. 3.5, which does not prove it; the proof of Prop. 3.15 relies on "well ordered" (a19). | Add the one-line Egyptian-fraction bound given under a19. |
| N8 | A refs | [23] "Gier, J."; [14] pages without the letter prefix; [9] initials differ from [10] and [14] (a16). | "de Gier, J."; "L137–L140"; check the [9] record. |
| N9 | A p.33 | Two consecutive parentheticals (a22). | Merge them. |
| N10 | S pp.12, 14 | "conservative" remains (a11). B p.18 also says "within the conservative error estimate"; align B if A is changed. | Replace with "the second estimate". |

## 5. Summary

The revision deals with the substance of every MAJOR item.
- **A1:** the bracketing claim is gone, and (6) now has the correct max bound with an explicit counterexample, which I recomputed.
- **A2:** the Schueth statement is corrected and the physics references are added.
- **A3:** the variable-curvature proofs are now complete.
- **A4, A5:** the Figure 3 squares, and the √t/sin(π/m) and wave-trace framing, are corrected.
- **A7–A10:** done (the proved δ1 of Lemma B.3, the classical attributions, the proofs moved to Appendices C–E, the overlap statements).
- **A6 is only PARTLY resolved,** because Lemma 3.7 is still uncited.

I checked the new mathematics independently and it holds:
- the Duhamel constant and the top coefficient in Prop. 2.11;
- the Theorem B determinant;
- the maps, discriminant and flex of Theorem 5.8;
- the Remark B.4 numbers;
- the least-area statement of Theorem 5.7.

Of the 64 minor rows:
- 53 are RESOLVED;
- 2 are NOT APPLICABLE as intended (a61, a62), though the stated reason for a61 is wrong in detail: no 1.x numbers are cited from outside;
- 7 are PARTLY resolved: a10 (inconsistent values near t = 0.03), a11 ("conservative" remains), a14 (no per-piece attribution), a16 (de Gier, Dowker initials, page prefix), a21 (caption lacks "schematic"), a51 (search not reported), a64 (Example 3.6 wording);
- 2 are NOT RESOLVED: a19 and a32 (finiteness of signatures of a given area and the a-priori bound on the orders for the area-class enumeration). One added line fixes both.

All of B's locators into A are correct, and all shared numbers agree (systoles, diameter, eigenvalue counts, error estimates, the note's constants and Selmer orders). Two cross-paper statements need correcting. First, A says B restates the shared results "without proof", but B proves them in its Appendix A. Second, A overstates the note's Theorem C ("every size" for "at least k"). A third point is a missing link rather than an error: the note reproves Theorem 5.8 without citing A, which is also why the verdict's reason "the note cites it" is false. The other new problems are small:
- the inconsistent values near t = 0.03 between p.32 and S4;
- "closed geodesics take over at t ≈ 0.1" (their share there is 0.5%);
- Remark 4.3 cutting off the antecedent of "The constant of (a) is not";
- the bibliography details.
