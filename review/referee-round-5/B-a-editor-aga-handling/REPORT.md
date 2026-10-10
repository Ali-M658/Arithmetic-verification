<!-- Saved verbatim by the main session from the final message of reviewer B-a: the harness refused the reviewer's own write. Text from the report's first heading on; the reviewer's preceding cover note was dropped. -->
# Handling-editor report: Annals of Global Analysis and Geometry

**Submission:** "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (Gang, Agadi, Veluri, Wang, Barreto, Chouthaiwale), 26 pp.
**Disclosed related manuscripts (not under review):** (A) "How much of a hyperbolic orbifold does heat hear?" with its supplement; (N) "Triples with equal sum and equal reciprocal sum".
**Reader:** handling editor (editorial board; my own work is on determinants of Laplacians and compactness of isospectral sets on surfaces, the Osgood–Phillips–Sarnak and Brooks–Perry–Petersen line).

As instructed, the placeholders (author contributions, AI-use statement, Zenodo DOI) are treated as known, and nothing in this report concerns the length of the manuscript. Every typographical, figure and sign remark below was checked against rendered page images (pdftoppm, 90 dpi), not only against extracted text.

---

## 1. Summary

The paper studies closed orientable hyperbolic 2-orbifolds whose singular points are cone points. Such an orbifold has a signature σ = (g; m_1, …, m_n). The full Laplace spectrum is known to determine σ (Dryden–Strohmaier). The paper asks whether finitely many eigenvalues, each known only approximately, are enough, and with how many eigenvalues and what accuracy.

- **Theorem 1.1 / Theorem 6.2 (p. 2, pp. 11–12).** Take the class C(A, ε, M): area ≤ A, systole ≥ ε, cone orders ≤ M. The paper gives explicit N and δ. If the first N eigenvalues are known to within δ, then the signature is the unique σ ∈ Sig(A, M) that minimises |Σ_{j<N} e^{−λ̃_j t\*} − G_σ(t\*)| at an explicit time t\*. Here G_σ is the identity-plus-elliptic part of the Selberg trace formula for the heat kernel.
- **Proof route.** The argument has four steps:
  1. The first heat invariant at which two signatures differ is controlled by integrality (Lemma 3.3), and it occurs by index min(⌊A/π⌋+4, M). This rests on the companion paper.
  2. Enveloping remainders turn this into a lower bound Γ(t) on |G_σ − G_σ'| for t ≤ t_1 (Lemma 6.1).
  3. A new diameter bound D(A, ε, M) (Theorem 4.4) controls the closed-geodesic term through a crude lattice-point count. This needs a separation lemma for elliptic points (Lemma 4.2) and a lower bound on ball areas (Lemma 4.3).
  4. A Weyl/heat-type counting bound controls the eigenvalues beyond the N-th (Proposition 5.2).
- **Theorem 1.2 / Theorem 7.1 (pp. 3, 13–14).** An a-posteriori version, with an explicit error budget E_N(t). It is run on computed spectra of O(2,8,8), O(3,3,12) and eight orbifolds of signature (0;3,3,3,3). The criterion holds with 18 to 847 eigenvalues, against 4×10^4 to 7×10^12 from Theorem 6.2 (Table 6).
- **Theorem 1.3 / Propositions 8.2–8.3, Remark 8.4 (pp. 3, 19–21).** The bound on the orders cannot be removed. The triangle orbifolds O(2,3,m) have area < π/3, a uniform systole bound σ\* = 0.56206 (proved through Jørgensen's inequality, Lemma 8.1), and cone balls of radius h_m ~ log m. Their eigenvalues satisfy λ_j ≤ 1/4 + π²(j+1)²/h_m², and a pigeonhole argument then gives pairs of different signatures with nearly equal first N eigenvalues.
- **Section 8.2.** A pinching construction (Proposition 8.5) and **Problem 1**: is the systole bound needed? This is a signature-level analogue of the Buser–Courtois conjecture.

The authors are unusually candid about the limits of the work: the constants are astronomically large, the rates in ε and M come from the method, and the numerical inputs are estimates rather than enclosures.

## 2. Significance

**What is good.**
- The question is natural and squarely within AGAG's scope: global analysis, inverse spectral geometry on orbifolds, MSC 58J53/58J50.
- Theorem 1.3 is a clean and quotable statement. On orbifolds, unlike surfaces, a systole bound and an area bound do not give compactness of the relevant class. The O(2,3,m) family stays thick, yet its cone points become cusp-like. This makes the order bound in Theorem 1.1 genuinely necessary, not a convenience of the proof. The proof is short and self-contained, and the uniform systole bound through Jørgensen's inequality is neat.
- The diameter bound of Theorem 4.4 for C(A, ε, M) is elementary but new as stated. Lemma 4.2, which separates elliptic points through products of reflections, is a nice argument.
- Problem 1 is well posed. The authors explain correctly why the pigeonhole mechanism of Proposition 8.3 is unavailable for it.
- The paper separates proved statements from numerical observations with care. Phrases such as "observations on our formulas, not proved asymptotics" and "demonstrations … not determinations" are exactly what a reader needs.

**Limitations on significance.**
- Without constants, Theorem 1.1 follows from compactness, as the authors explain on p. 2. The added value is that N and δ are explicit. The explicit values, however, are N up to 3.8×10^30 and δ down to 8.7×10^−278 (Table 3, p. 12). By the authors' own account (p. 10, end of §4.2), every rate in ε and M is an artefact of the method.
- What effectivity really buys is decidability. Theorem 6.2 gives a finite procedure that certifiably decides the signature from finitely many certified approximate eigenvalues. The manuscript should say this plainly, because it is the strongest argument for publication (see M2).
- The analytic machinery is standard in this area: the Selberg trace formula, heat expansion with explicit remainders, a geodesic count from a diameter bound, and Weyl-type tails. The heat-invariant algebra that makes Lemma 3.3 work comes from the companion paper. The independent mathematical novelty of the submission lies in:
  - Section 4 (the diameter bound);
  - the assembly in Section 6;
  - Section 8 (the order counterexample and the pinching discussion).
- That is a modest but real contribution for AGAG. It is comparable in weight to orbifold spectral papers AGAG has published, for example Stanhope (2005), Rossetti–Schueth–Weilandt (2008) and Abreu–Dryden–Freitas–Godinho (2008). Remarkably, the submission cites none of these (see M2).

## 3. Correctness, and what was recomputed or checked

I read every proof in the submission. I recomputed the following myself (sympy/mpmath at 40 digits, numpy), using only the formulas printed in the PDF.

**Recomputed and confirmed.**
1. **Table 3 (p. 12): all eight rows.** I recomputed k\*, D, t_1, t_3, Γ\*, Λ, N, δ and the binding constraint from the definitions of Theorem 6.2. They used:
   - n\* = ⌊A/π⌋+4 and k\* = min(n\*, M);
   - L_M, δ_1 = 1/(2L_M), δ_k = a_{k−2}, Q(K), t_1, t_2, p, ϖ, y_0, t_3, Z♯, Λ, N = ⌊eZ♯(1/Λ)⌋+1 and δ = Γ\*/(8eNt\*).

   Every entry agrees to the printed precision. Two examples: row 1 gives t_1 = 1.14e−7, t_3 = 3.54e−4, Γ\* = 2.59e−18, N = 3.4e8, δ = 3.07e−21. Row 8 gives Γ\* = 1.77e−272, N = 3.75e30, δ = 8.65e−278. The binding constraint (t_1 or t_3) and the remark "t_2 ≥ 0.0045 never binds" also agree.
2. **Table 2 (p. 10): all entries of D(A, ε, M) = 4r_0A/v_0.** All agree (56.6, 1125, 6.37×10^5; 150.9, 3001, 1.70×10^6; 640, 3184; 1132, 2.25×10^4, 1.27×10^7).
3. **The claim on p. 13** that without k\* ≤ M the value of N at A = 10π, M = 3 would be about 4×10^18. Recomputed: 4.19×10^18. Confirmed.
4. **Coefficients.**
   - α_0, …, α_4 = 1, −1/3, 1/15, −4/315, 1/315.
   - a_0, …, a_3 = 1/12, 1/360, 1/2520, 1/10080.
   - b_0(m) = (m²−1)/(12m).
   - The closed form for mφ_k(m), checked against a direct Taylor expansion of Φ_8 (0.65625, 2.953125, 17.82421875).
5. **Lemma 3.3 examples.** d_2 = −1/12 for (0;4,4,4) versus (0;3,4,6), and d_3 = +25/12 for (2,8,8) versus (3,3,12), sign included. Both agree with p. 8 and p. 13.
6. **|S| in Table 6.** Signatures of area π/2 with orders ≤ 12: exactly six, namely (2,6,12), (2,8,8), (3,3,12), (3,4,6), (4,4,4), (0;2,2,2,4). Signatures of area 4π/3 with orders ≤ 3: exactly three, namely (0;3,3,3,3), (0;2,2,2,2,3), (1;3).
7. **Table 4 inputs.**
   - diam P = 2.448 for O(2,8,8) (cosh = cot²(π/8)) and 2.158 for O(3,3,12).
   - Family systoles 4b: 2.634 at ϑ = 0 and 0.694 at ϑ = 2.8, from sinh a sinh b = 1/2.
8. **σ\* = 0.562066871…** (Proposition 8.2). Also the trace identity tr[γ,β] − 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r, checked numerically, including the claim that the rotation centre lies at distance r from the axis.
9. **Algebra checked by hand.**
   - Lemma 2.2, third bound: the two maxima, the integration by parts and the constant 2√π e^{3 diam}.
   - Lemma 4.2: (H3) gives cosh d − 1 = 2cos((θ+α+β)/2)cos((θ−α−β)/2)/(sin α sin β). The defect is ≥ π/(abc), and the final bound is ≥ 2/(π²M²).
   - Lemma 4.3 and the closed form of Theorem 4.4 (v_0 ≥ πr_0²/max(M, M²/4), d_0 ≥ min(ε/2, 0.6/M)).
   - Lemma 5.1, the case analysis giving Area ≥ π/21.
   - Theorem 6.2: the derivation of y_0 from B\*(t) ≤ Γ(t)/8. The identity (ε/2)(ε²/4)^{p−1/2} = (ε²/4)^p is what makes the exponent p = k\*−3/2 come out. Also the tail and perturbation budget 3Γ\*/8 < 5Γ\*/8.
   - Theorem 7.1, including that (C2) implies (C1).
   - Identity (3) for both w = sinh ρ and w = cosh ρ, with the stated q.
   - The matrix recurrence in Lemma 8.1.
   - The λ_1 bound of Proposition 8.5: ∫_{−a}^{a} ρ² cosh ρ dρ = 2[(a²+2) sinh a − 2a cosh a], with only the collar retained in ∫f².
   - Remark 8.4's computation for A < π/3.
10. **Ratios quoted in §7.2 and in the caption of Fig. 2**, computed from Table 6: 5×10^2 to 3×10^11; "20–50" at M = 3; ~10^6; 10^7 to 3×10^8. All consistent.
11. **Cross-document consistency.** I compared against the companion's supplement (S4, S6) the following: λ_1 = 3.838887 and 3.499847, the first Dirichlet values 73.663812 and 72.365158, the counts 2002/2001, the 1.6×10^4 completeness threshold (e^{−0.0015λ} = 1.5×10^−11 at λ = 1.661×10^4), the family systoles, and λ_1 of O(2,3,7) = 44.89. All consistent.
12. **Bibliography spot-check** through Crossref: Garbin–Jorgenson (×2), Buser–Courtois, Linowitz–Voight, Dryden–Strohmaier and Booker–Strömbergsson–Venkatesh resolve correctly.

**Not recomputed.** I did not recompute Table 6, Table 5 or the eigenvalues behind Figs. 1–3; that would need the authors' data. I judged those parts only for internal consistency and consistency with the companion supplement.

**Verdict on correctness.** I found no mathematical error in what the submission proves itself. The correctness of Sections 2–3 rests on the companion paper (M1). There is one small unproved assertion (m1).

## 4. MAJOR issues

**M1. The submission cannot be refereed or published on its own: its foundations are in an unrefereed companion manuscript (Sections 2–3, Table 1, pp. 4–7).**
- The following are stated "without proof" and cited to [20]:
  - the heat trace formula (Theorem 2.1);
  - the geodesic count and the bound on the hyperbolic term (Lemma 2.2, first two statements);
  - the enveloping remainders (Proposition 2.3), which drive Lemma 6.1;
  - the structure of the heat data (Lemma 3.1);
  - the separation and bounded-order theorems (Theorem 3.2).
- Theorem 3.2(ii) is the main theorem of the companion paper (A, Theorem 3.8(i)). Lemma 6.1, hence Theorem 6.2, hence Theorem 1.1, cannot be checked without A. Reference [20] is listed as "Companion manuscript, submitted (2026)", with no preprint identifier.
- In the PDF, cross-references such as "[20, Lemmas 2.4 and 2.5]", "Prop. B.2" and "Lemma 2.10" are typeset as live hyperlinks into the companion's internal numbering (cyan, pp. 5–7). Those links will dangle in any published version.
- *Editorial consequence.* A referee must receive A (and its supplement) as confidential supporting material. Acceptance of this submission can only be conditional on A being publicly citable (at minimum on arXiv, with a fixed version number), so that each cited statement has a stable, checkable source.

**M2. The paper is not positioned against the AGAG-relevant literature on spectral finiteness and isotropy bounds for orbifolds, and the case for significance needs to be stated.**
- *(a) Missing literature, some of it published in AGAG and some cited by the authors' own companion paper:*
  - E. Dryden, "Isospectral finiteness of hyperbolic orbisurfaces" (arXiv math/0411290): the orbifold analogue of McKean's finiteness theorem, directly relevant to "What effectivity adds" (p. 2) and to Problem 1.
  - E. Stanhope, "Spectral bounds on orbifold isotropy", AGAG 27 (2005) 355–375: the full spectrum, with a curvature bound, bounds the isotropy orders. This is the exact counterpoint to Theorem 1.3, which shows that no finite part of the spectrum does so.
  - E. Proctor and E. Stanhope, "Spectral and geometric bounds on 2-orbifold diffeomorphism type", Differential Geom. Appl. 28 (2010) 12–18. They show that bounds on curvature, volume and diameter allow only finitely many 2-orbifold diffeomorphism types, and that isospectral families of 2-orbifolds contain finitely many types. This sits next to Theorem 4.4 (diameter from A, ε, M) and Proposition 8.2 (diam O(2,3,m) ≥ h_m → ∞, so the O(2,3,m) family evades exactly the diameter hypothesis).
  - J. P. Rossetti, D. Schueth and M. Weilandt, AGAG 34 (2008), on isospectral orbifolds with different maximal isotropy orders.
  - Doyle–Rossetti, the independent proof that the spectrum determines the signature, which the companion paper cites.
  - The compactness tradition the "What effectivity adds" argument belongs to: McKean's finiteness theorem, Osgood–Phillips–Sarnak, Brooks–Perry–Petersen.

  AGAG readers will expect at least a paragraph on these.
- *(b) The area hypothesis is never discussed.* Section 8, "The hypotheses", treats the order bound (§8.1) and the systole bound (§8.2) but says nothing on whether the area bound is needed. Results on prescribing finite parts of the spectrum suggest that when the topology may vary it cannot be dropped: Colin de Verdière for variable metrics, and a recent preprint (Mukherjee, arXiv:2603.21240, 2026) for constant curvature −1 with varying topology. This should be said, proved, or posed as an open question.
- *(c) State the real gain from effectivity.* The value of Theorem 6.2 is that it gives a finite, certifiable decision procedure from finitely many certified approximate eigenvalues. The size of N and δ is not the point. The introduction (pp. 2–3) currently says the numbers are "enormous" and "the same mechanism … gives a test that a computed spectrum can pass", which undersells the decidability statement and oversells the test (see M3).

**M3. Theorem 7.1 is presented as a "test" but, as run, it checks the computed spectra for consistency with known signatures. Two of its hypotheses look unnecessary, and one of its inputs is circular (pp. 3, 14–17).**
- *(a) Circular completeness.* Input (iv), completeness, is certified on p. 15 by comparing the computed heat trace with I + E for the true signature ("agrees with I + E to 4.7×10^−13 at t = 0.0015"). For the family it is likewise compared with I + 4E_3. So completeness is established using the very signature term the test is meant to identify. For a genuine determination of an unknown signature, completeness must be certified independently of σ, for example through counts that agree across discretisations (the authors already use this above 9.8×10^3 for the family) or a signature-free Weyl bound. As written, the paper's statement "with guaranteed eigenvalue enclosures and a proved completeness, the same computation would decide the signature rigorously" (p. 14) hides this dependence.
- *(b) The exact-area hypothesis seems to be an artefact.* Item (i) on p. 14 says "finitely many eigenvalues do not determine the area". Inside C(A, ε, M), however, Theorem 1.1 itself determines the signature, and hence the area 2πs(σ), from finitely many eigenvalues.
  - In Theorem 7.1 the area enters E_N only through A/(4πs), where an upper bound suffices.
  - It enters H only through 1/Area(O), where Area ≥ π/21 or min over S suffices.
  - Signatures of different area are separated at order t^{−1} with |d_1| ≥ 1/(2L) (Lemma 3.3(i)).

  The test should therefore extend to S = Sig(A, M), with area at most A, at negligible extra cost. Then the ten examples would determine the area as well, which would materially strengthen §7. If the authors see an obstruction, it should be stated.
- *(c) The decisive input is the instance diameter.* The instance-level diameter bound 2 diam P presupposes the geometry; the authors say so frankly on p. 17. With the class-level bound, the criterion fails within the computed range for both triangle orbifolds and for most of the family (Table 6, column "(C1), D(A, ℓ, M)").

  So the paper's headline numerical claim (abstract, p. 1; p. 3: "holds for all ten with 18 to 847 eigenvalues") is a claim about a test that uses the geometry, the area and (for completeness) the signature. The abstract and introduction should foreground the class-level column of Table 6, which uses only (A, ℓ, M). That column is the honest analogue of Theorem 6.2: 855–2900 eigenvalues where it succeeds, and estimates of 5.6×10^3 to 4.1×10^5 where it does not.

**M4. The numerical-methods description omits two limitations that the companion's supplement records for the same spectra (§7.1, p. 15).**
- *(a) Single-window solver for the triangle spectra.* The supplement of A (Section S4, "Limitations") states three things about these spectra:
  - each eigenvalue was taken from a single shift-invert window;
  - the experiment of Section S6 showed this can miss an eigenvalue at a window boundary;
  - "a recomputation of all four spectra with the double-window solver … has not been run".

  The submission says only "overlapping spectral windows … for O_ϑ every eigenvalue is covered by two windows". Since the authors themselves call completeness "not a technicality" (p. 14, (iv)), this limitation must be disclosed here.
- *(b) Conservative error estimate not reported.* The supplement carries a conservative estimate |λ(0.05,10) − λ(0.07,10)|, up to 1.2×10^−8 relative for the first 500 eigenvalues against 2.9×10^−11 for the estimate used. The submission does not mention it. My own order-of-magnitude check suggests the perturbation term t Σ ε_j is many orders below the gaps at the reported times, so Table 6 should be insensitive to this choice. The authors should say so, ideally with Table 6 recomputed under the conservative ε_j.
- *(c) Compensating errors.* A single-time trace test (t = 0.0015) cannot rule out compensating errors, for example an omitted eigenvalue together with a duplicated nearby one, or a lost multiplicity offset by a spurious value. The companion's supplement uses an interval of times [0.0015, 0.03]. Also see m3.

## 5. MINOR issues

- **m1 (p. 12, paragraph after the proof of Theorem 6.2).** The decision rule is said to be "computable in exact rational arithmetic" by truncating (2) at any K with t\*^K Q(K) ≤ Γ\*/16. The cone series diverges, so such a K is not automatic. The constraint t\* ≤ t_1 only controls K ≤ k\*−1, and t\*^{k\*−1}Q(k\*−1) ≤ δ_{k\*}t\*^{k\*−2}/4 need not be ≤ γ\*t\*^{k\*−2}/32. Either prove that a K exists (for instance from Q(K+1)/Q(K) ≍ K(M/π)² and t\* ≪ (π/M)²) and give one, or evaluate G_σ(t\*) with a rigorous quadrature bound.
- **m2 (p. 3, Theorem 1.3; pp. 20–21, Remark 8.4).** "No N and δ depending only on A and ε have the property of Theorem 1.1." The property of Theorem 1.1 is stated relative to Sig(A, M), and with M removed that set is infinite. State precisely what fails: the "in particular" clause, that two orbifolds of C(A, ε, ∞) whose first N eigenvalues agree to within δ have the same signature. That is what Remark 8.4 proves.
- **m3 (p. 15, "Completeness").** "No eigenvalue below 1.6×10^4 is missing or spurious" follows from a single-time comparison, so it excludes one missing or one spurious eigenvalue but not compensating pairs. Rephrase, or report the comparison over a range of t.
- **m4 (p. 20).** The body text contains a repository path, "(theory/eigen/systole_233.py; floating point, not interval arithmetic)". Script paths belong in the data statement, not in the mathematical text. Also state explicitly that the word search giving 0.98399 … 1.9213 is used in no proof.
- **m5 (p. 4, "Results shared with the companion paper").** "Lemma 3.3 and Sections 4–8 are not contained in [20]." Lemma 3.3(ii) is in substance the computation in the proof of [20, Theorem 3.8(ii),(iv)]: at the first differing coefficient, d = (−1)^l a_l × (difference of an odd power sum). Describe it as "a direct consequence of [20, Lemmas 2.10, 3.3]".
- **m6 (p. 2).** The continuity of λ_j on the compact set of orbifolds of fixed signature is justified in a parenthesis ("quasi-isometries with constants near 1"). For orbifolds the maps must respect the cone structure. Give a reference or a two-line argument. The same parenthesis is reused on p. 22.
- **m7 (p. 2).** Cite Doyle–Rossetti next to Dryden–Strohmaier for "the whole spectrum determines the signature", as the companion paper does.
- **m8 (p. 13).** "N grows by a factor of about 9 per halving of ε … roughly like ε^{−3} log(1/ε)" is presented as an observation. It follows directly from the printed formulas: t_3 ≈ ε²/(24D) with D ≍ A/ε in that regime, and N ≍ (eA/2πt\*) log(8Z♯/Γ\*). Derive it in one line rather than "observe" it.
- **m9 (p. 21, Proposition 8.5).** In the proof, say that the λ_1 bound keeps only the collar in ∫f². As written, the reader cannot see why the bound does not depend on k or on the area 2π(2 − 4/k).
- **m10 (p. 14, Theorem 7.1).** H(s) switches between the two bounds of Lemma 2.2 at s = ℓ²/(2(1+ℓ)). Taking the minimum where both are valid is free and might help the class-level column.
- **m11 (p. 16).** Explain what "the least sector maximum" is (defined only in the companion's supplement).
- **m12 (Data statement, p. 23).** The development repository's owner handle and name ("Ali-M658/Arithmetic-verification") do not obviously match the stated maintainer or the subject of the paper. Since the Zenodo deposit is declared the record of reference, make sure the paper points readers only to it, or explain the repository name.
- **m13 (References).** Check the issue number of Buser–Courtois (Math. Ann. 287, given as "(3)"; Crossref lists issue 1) and the publication year of Garbin–Jorgenson in L'Enseignement (Crossref gives 2019 online for vol. 64 (2018)).

## 6. Presentation (figures, captions, notation, exposition)

- **P1. Notation clashes.** Several symbols mean different things in nearby places, and a reader has to track this:
  - **Γ:** the Fuchsian group; stabilisers Γ_x̃; the gap function Γ(t); Γ\* = Γ(t\*) on p. 11; and Γ\* the reflection group, with Γ_m, on p. 19.
  - **Epsilon:** ε for the systole bound and ϵ_j for the eigenvalue errors. Both glyphs appear in the same paragraphs of §7, and in Table 4 the systole bound is called ℓ.
  - **δ:** the eigenvalue accuracy and the separation constants δ_k, δ_1.
  - **ℓ:** the systole, the length ℓ(γ), and the interval length in the proof of Proposition 8.3.
  - **β:** the constant max Σ b_0 in Theorem 7.1, a rotation in §8.1, and a line in §8.2.
  - **p:** k\* − 3/2 in Theorem 6.2, the finite-element order in §7.1, and a point.
  - **N and D:** the eigenvalue count and the diameter bound, but also the Neumann and Dirichlet labels in Table 5.
  - **Sig vs Sig(A, M):** a class of orbifolds versus a set of signatures.

  Please disambiguate, for instance with 𝔊 or g\* for the gap, ε_sys versus η_j, and B_N/B_D for the boundary labels.
- **P2. Fig. 1 (p. 13).** The figure has no legend, and the caption does not identify the dashed curve (geodesic bound), the two dotted curves (N = 21 and N = 100) or the shaded window. These are explained only in the body text. The caption should be self-contained and name the darkest grey curve, (0;3,3,12).
- **P3. Fig. 2 (p. 19).** The caption mentions "a reference count" without defining N_obs. It also does not give the encoding: open versus filled markers for M = 3 versus 12, horizontal offsets, diamonds, squares and circles, and the two coloured triangle orbifolds. All of this sits in a paragraph on p. 17. The class-level column of Table 6, arguably the most informative comparison (M3(c)), is not plotted. Please add a legend and plot that column.
- **P4. Fig. 3 (p. 22).** In panel (b), the faint dashed horizontal lines at 1, 4, 9, 16, 25, 36 are not explained in the caption. They could be j² (the "interval of length h_m" reference in the text, p. 21) or the rescaled proved bounds (j+1)², and the two sets coincide as sets of levels. The reader cannot tell which. The caption also says the proved upper bounds "tend to 1/4", which describes panel (a) only. Please label both panels' reference curves.
- **P5. Figure fonts.** Axis labels in all three figures use font encodings without Unicode mapping. Extracted text reads "jG¾0(t) ¡ G¾(t)j" and "¸j". They render correctly, but they are not searchable or accessible. Please fix in production.
- **P6. Exposition.**
  - The second sentence of §1 ("once three quantities are bounded: the area, from below the systole …, and from above the cone orders") is a garden-path sentence.
  - "The criterion of an a-posteriori test, run at one time" in the abstract is opaque.
  - The proof of Lemma 2.2 (p. 6) sets a multi-level fraction inline and is hard to read.
  - §7.1 uses "trace test", "sector maximum" and "Weyl value 4πN/A" before or without defining them.
- **P7. Tables.** Table 4: explain the "–" entries in the "D, M = 3" column (orders 8 and 12 exceed 3). Table 6: the column header "(C1), D(A, ℓ, M)" mixes a count with "> N_c; estimate" entries. Add a footnote that the second number is the Weyl-based estimate of §7.1.
- **P8. Strengths of the presentation.** Theorem 1.2's list of five inputs and their status (p. 14) is a model of how to state numerical hypotheses. Table 1, which maps imported results to their sources, is helpful. The authors consistently label observations as observations.

## 7. Overlap with the disclosed related manuscripts

**Companion paper A ("How much of a hyperbolic orbifold does heat hear?") and its supplement.**
- *Declared reuse of statements.* Sections 2–3 of the submission restate, without proof, results that A proves (Table 1: A's Theorem 2.3, Lemmas 2.4–2.6, 2.8, 2.10, 3.3, Corollary 3.5, Theorem 3.8(i), Lemma B.1, Proposition B.2). The restatements match A's statements (checked). This reuse is disclosed and appropriate, but see M1.
- *Lemma 3.3.* Claimed as new. As noted in m5, its content is essentially present in A's proof of Theorem 3.8(ii),(iv).
- *Same numerical data.* The spectra of O(2,8,8), O(3,3,12) and the (0;3,3,3,3) family are those of A's supplement, Sections S4 and S6. This is disclosed on p. 4. The methods paragraph of §7.1 is a close paraphrase of A's supplement, with the same solver, levels, error estimate, convergence rates, completeness threshold and budget. Text-similarity screening will flag it, so a sentence saying the description follows [20, Supplement S4, S6] would pre-empt that. The submission omits two limitations that A's supplement records for the same data (M4).
- *Adjacent results.* A's Theorem 4.2(a) uses the same hyperbolic-term bound to compare traces within one signature. A's Appendix B ends by noting that heat-trace data determine the heat invariants up to an error explicit in the systole and diameter, which is the bridge this submission builds. A's Section 6 and Corollary 6.5 give an "a-posteriori use" with approximate heat invariants as data, where this submission uses approximate eigenvalues. These are adjacent but distinct.
- *What is not in A.* Sections 4, 5, 6 (the assembly), 7 (the test) and 8 (the order counterexample, Jørgensen systole bound, pinching, Problem 1) have no counterpart in A; I searched A and its supplement for diameter bounds, O(2,3,m), cusps, Jørgensen, Buser–Courtois and Mumford.
- *Assessment.* There is no duplicate publication. This submission is a separate paper with its own theorems, but it depends on A (M1). The division of labour is defensible: A is about heat invariants, and this submission is about eigenvalues.

**Arithmetic note N ("Triples with equal sum and equal reciprocal sum").** It shares only the motivating pair (2,8,8)/(3,3,12) and the fact that the first two heat invariants of a triangle orbifold are equivalent to (S, R). There is no technical overlap with the submission. The submission does not cite N, which is appropriate.

**Consistency across the three manuscripts.** All the shared numbers I compared agree: d_3 = 25/12, λ_1 values, the 2002/2001 and 4357–4451 counts, the 1.6×10^4 threshold, systoles 2.634→0.694, and λ_1(O(2,3,7)) = 44.89. The only discrepancies are the omissions in M4.

## 8. Desk-reject probability

**25%.** This estimate takes no account of length.

**Reasons it would go out to review (lowering the probability):**
- The scope fit is strong. Inverse spectral geometry of orbifolds via the Selberg and heat traces is AGAG territory, and AGAG has published the closest related work (Stanhope 2005; Rossetti–Schueth–Weilandt 2008; Abreu–Dryden–Freitas–Godinho 2008).
- The mathematics I could check is correct and carefully written.
- Theorem 1.3 and Problem 1 are clean contributions of independent interest.
- The constants are reproducible from the printed formulas.
- The authors are candid about every limitation.

**Reasons it might be desk-rejected (raising the probability):**
1. *Dependence on an unrefereed companion (M1).* This is the largest single risk. Some editors will not send out a paper whose central lemma (Lemma 6.1) rests on unpublished, unrefereed theorems.
2. *Perceived significance (M2).* An editor may see Theorem 1.1 as a routine effectivisation of a compactness argument with constants that have no practical meaning. In that view, the numerical section shows consistency checks on orbifolds whose geometry is known (M3), not a usable test.
3. *Missing AGAG-relevant literature (M2(a)).* This signals to an AGAG editor that the paper has not yet been placed in the journal's conversation.

On balance I would send it out, so the probability is well below 50%. It is not low, because (1) and (2) are the kind of thing a busy board member acts on at the desk.

## 9. Recommendation

**Send for review. Provisional recommendation: major revision.** Confidence is moderate (about 0.6). It would rise to minor revision once M1 is resolved (A publicly available and refereed in parallel) and M2–M4 are addressed. It would drop toward reject if A's results used in Sections 2–3 fail review.

Suggested referee profile: one referee in spectral geometry of hyperbolic orbifolds and the trace formula, who should also receive A. A second referee in computational spectral theory on hyperbolic surfaces, in the Strohmaier–Uski direction, for §7.

## 10. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Provide A (and supplement) to referees. Make A publicly citable with a fixed version (arXiv identifier) and cite each imported statement by that version. Remove the live hyperlinks into A's internal numbering. Acceptance is conditional on A being publicly available. |
| M2 | Add a related-work paragraph: Dryden (isospectral finiteness), Stanhope (AGAG 2005), Proctor–Stanhope (2010), Rossetti–Schueth–Weilandt (AGAG 2008), Doyle–Rossetti, McKean / OPS / BPP. Relate Theorem 4.4 and Proposition 8.2 to Proctor–Stanhope's diameter hypothesis. Address the necessity of the area bound (proof, citation, or open question) in §8. Restate the significance of Theorem 6.2 as a certified finite decision procedure. |
| M3 | Either extend Theorem 7.1 to S = Sig(A, M), with area at most A, and rerun Table 6, or explain why exact area is needed. Certify completeness independently of the signature, or state plainly that completeness was checked against the true signature. Foreground the class-level column of Table 6 in the abstract and introduction. |
| M4 | Disclose the single-window computation of the triangle spectra and the unrun double-window recomputation. Report Table 6 under the conservative ε_j, or state the sensitivity. Report the completeness comparison over a range of t. |
| m1 | Prove that a suitable K exists and give one, or replace the truncation by a rigorous quadrature bound. |
| m2 | Restate Theorem 1.3 and Remark 8.4 with the "two orbifolds … same signature" form, over a class without an order bound. |
| m3 | Rephrase the completeness conclusion, or use several values of t. |
| m4 | Move the script path to the data statement, and say the word search is used in no proof. |
| m5 | Reword the novelty claim for Lemma 3.3. |
| m6 | Add a reference or short argument for continuity of λ_j on orbifold moduli. |
| m7 | Cite Doyle–Rossetti. |
| m8 | Derive the ε^{−3} log(1/ε) behaviour from the formulas. |
| m9 | One sentence in the proof of Proposition 8.5. |
| m10 | Optional improvement of H(s). |
| m11 | Define "sector maximum". |
| m12 | Clarify the repository reference. |
| m13 | Correct the bibliographic details. |
| P1 | Rename the clashing symbols. |
| P2–P4 | Make captions self-contained, add legends, identify the reference lines in Fig. 3(b), and plot the class-level counts in Fig. 2. |
| P5 | Embed figure fonts with Unicode maps. |
| P6–P7 | Make the listed sentence- and table-level fixes. |

---

Files are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-5/B-a-editor-aga-handling/scratch/`:
- `scripts/consts.py`: recomputes Tables 2 and 3
- `scripts/consts_nok.py`: checks the 4×10^18 claim
- `renders/B-*.png`: page images of the submission
- `txt/`: text extracted from the four PDFs
