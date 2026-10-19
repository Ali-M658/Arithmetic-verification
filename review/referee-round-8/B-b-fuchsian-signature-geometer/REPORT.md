<!-- Round 8 B-b referee report: returned text saved verbatim; the reviewer could not write files -->

I couldn't save the report to `review/referee-round-8/B-b-fuchsian-signature-geometer/REPORT.md` because the write was refused, so the full text is below. My check scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/B-b-fuchsian-signature-geometer/scratch/code/` (`sec3.py`, `sec4.py`, `sec8.py`, `env.py`, `jorg.py`).

---

# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

Journal: Annals of Global Analysis and Geometry
Referee B-b: geometry of Fuchsian groups and their signatures.

My assignment covered Sections 3, 4 and 8, every geometric hypothesis of the main theorems (including the count of closed geodesics), and the appendix results these sections depend on: Lemma 2.2, Proposition 2.3, and Appendix A (Lemmas A.2–A.4, the proofs of Lemma 3.1 and Theorem 3.2). Page numbers are those of the PDF (36 pp.). I read the rendered pages of everything cited below. The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) are treated as known.

## Summary

The paper shows that for closed orientable hyperbolic 2-orbifolds with area ≤ A, systole ≥ ε and cone orders ≤ M, the first N eigenvalues, each known to within δ, determine the signature, with N and δ given by explicit formulas.

The parts I refereed supply the following:

- **Section 3:** the arithmetic of the first heat invariant at which two signatures differ (Lemma 3.3). This rests on Theorem 3.2 (taken from the companion paper and proved in Appendix A).
- **Section 4:** a separation of cone points (Lemma 4.2), a lower bound for the area of balls (Lemma 4.3), a diameter bound (Theorem 4.4), and a count of closed geodesics in terms of A, ε and M alone (Lemma 4.5). The count C\* from Lemma 4.5 is the one Theorem 6.2 actually uses.
- **Section 8:** the order bound is shown to be necessary. The family O(2,3,m) has a systole bound uniform in m (Proposition 8.2, via Jørgensen's inequality), explicit upper bounds for its eigenvalues (Proposition 8.3), and a pigeonhole argument (Remark 8.4, Corollary 8.5). Section 8 also has a collar construction on a pinching family (Proposition 8.6) and an open problem on the systole hypothesis.

## Significance

- **The geometric part is careful, correct and, in places, neat.** Three arguments stand out:
  - Lemma 4.2 produces a group element γ = s₁s₃ from three reflections.
  - Lemma 4.5 replaces the diameter-based count e^{3D} (between 10^196 and 10^29326 on the classes of Table 3) by a packing count C\* between 4×10^5 and 7×10^10.
  - Proposition 8.2 gives a systole bound for O(2,3,m) that is uniform in m, which places the whole family in one class C(π/3, ℓ₂,₃, ·).

  Theorem 3.2(ii), which says the first difference occurs at index ≤ M, is a clean Vandermonde argument.
- **Novelty in my sections is modest.**
  - Sections 2–3 are taken from the companion paper [31] (Table 1).
  - Section 4 is a standard thick–thin and packing argument, with order dependence that is far from sharp (M1).
  - Theorem 1.3 adds two things to Garbin–Jorgenson's elliptic degeneration: the uniform systole constant and the explicit pigeonhole. Both are honest but small additions.

  For AGAG the geometric content is publishable as support for the main theorem. It would not carry a paper on its own.

## Correctness, and what I recomputed

I checked every proof in my assignment line by line. **I found no mathematical error.** Details:

1. **Lemma 4.1 (H1)–(H3).** I re-derived all three, including the hyperboloid normals in (H3) and the sign argument placing w on the side x₂ > 0. They are correct.
2. **Lemma 4.2.** I re-derived the identity cosh d − 1 = 2cos((θ+α+β)/2)·cos((θ−α−β)/2)/(sin α sin β) from cos θ = X. The defect bound π/(abc), the bound |θ−α−β| ≤ π − π/M and the final 2/(π²cM) ≥ 2/(π²M²) are all correct. The hyperbolic case (X > 1, so ε ≤ 2h ≤ 2d) and the exclusion of X = 1 (no parabolic elements) are correct.
3. **Lemma 4.3.**
   - The two-case argument is correct.
   - The case "cone point within r₀" uses Lemma 4.2 for the orbit of p̃.
   - The other case uses (H1) with sin(πj/k) ≥ sin(π/M) and centre distance ≥ r₀.
4. **Theorem 4.4.**
   - The proof is correct, including the strict inequality ∆ < 4r₀A/v₀.
   - The closed form is valid. I verified cosh ρ₁ − 1 ≥ (cosh r₀ − 1)sin²(π/M) from sinh ρ₁ = sinh r₀ sin(π/M).
   - I checked numerically that arccosh(1+x) ≥ √(2x/(1+x)) on x ∈ [10⁻⁸, 10⁴].
   - The constant 0.6 is valid: M·arccosh(1+2/(π²M²)) ≥ 0.634 for all M ≥ 2.
   - **Table 2 (p. 12):** all 15 entries reproduced to the printed digits (56.6, 1125, 6.37×10⁵; 150.9, 3001, 1.70×10⁶; 640, 3184, 1.70×10⁶; 1132, 2.25×10⁴, 1.27×10⁷).
5. **Lemma 4.5.**
   - The covering of O by 5r₀-balls about the points b(y) is correct.
   - So is the 2ρ₁-separation of the orbit points γb̃ over distinct cosets of Γ_b̃.
   - So is the bound #{γ : d(b̃,γb̃) ≤ R} ≤ M(cosh(R+ρ₁)−1)/(cosh ρ₁−1).
   - So is the estimate d(b̃,γb̃) ≤ x + 10r₀.
   - I reproduced C\* for every row of Table 3 (1.32e8, 3.55e9, 4.01e5, 4.01e5, 9.45e9, 8.06e7, 3.01e6, 7.09e10) and the C\* columns of Table 4 (3.5e9, 4.0e5, 9.5e9).
   - I recomputed log₁₀(πe^{3D}/A) as 196.5 and 29325.4 at the ends of the range (see m4).
6. **Lemma 2.2.**
   - (i) is correct: the Dirichlet domain lies in B̄(x̃₀, diam) and the packing argument holds.
   - (ii) I re-derived the integration by parts, including the atoms at the lengths. I also re-derived the bound x/(x−t) ≤ ℓ/(ℓ−t), the identity x e^{x/2−x²/4t} = −(2tx/(x−t)) d/dx e^{x/2−x²/4t}, and the logarithmic derivative of B_C, whose bracket ℓ/(2t) − (1+ℓ)/ℓ is ≥ 0 exactly when t ≤ ℓ²/(2(1+ℓ)).
   - The bound valid for all t (maxima at x = 2√t and x = 6t, giving e^{17t/4−1/2−ℓ}) is correct.
7. **Proposition 2.3 and Lemmas A.2–A.3.**
   - The closed form Φ_m(u) = (cot u − m cot mu)/(4m sin u) is correct.
   - So is the series for mφ_k(m), which I checked against a Taylor expansion of the defining sum for m = 3 and m = 7.
   - b₀(m) = (m²−1)/(12m) holds for 2 ≤ m < 20, and a₀,…,a₄ = 1/12, 1/360, 1/2520, 1/10080, 1/28512.
   - α₀,…,α₄ = 1, −1/3, 1/15, −4/315, 1/315.
   - I checked the enveloping property (sign (−1)^K, or (−1)^{K+1} for the area term, with modulus ≤ the next term) by mpmath quadrature at t ∈ {0.01, 0.2} for E₃, E₇ and at t ∈ {0.05, 0.3, 1} for the identity term, K = 0,…,3. **It held in all 28 cases.**
8. **Lemma 3.1, Lemma A.4, Theorem 3.2, Lemma 3.3.**
   - I re-derived the padding identities, including |V\*|−|U\*| = 2(g−g′) and |U|+|V| = 2max(n+g−g′, n′+g′−g).
   - I re-derived the evenness argument for ∏(z−x) and the Vandermonde determinant in (ii).
   - The first-difference formula d_k = (−1)^k a_{k−2}(P_{2k−3}(U) − P_{2k−3}(V)) is correct.
   - **Independent enumeration in exact rational arithmetic.** I computed c₁,…,c₈ for every hyperbolic signature in these classes:
     - A ≤ 4π, M ≤ 10: 1562 signatures, 3503 equal-area pairs.
     - A ≤ 2π, M ≤ 30: 5235 signatures, 4306 pairs.
     - A ≤ 6π, M ≤ 6: 782 signatures, 4103 pairs.
     - A = π/2 and A = 4π/3 with M ≤ 12.
   - In every pair, d_k/((−1)^k a_{k−2}) is a nonzero integer and k ≤ min(⌊A/π⌋+4, M). The largest first index is 3, which confirms Remark 6.4(a).
   - The examples check out: d₂ = −1/12 for (0;4,4,4) vs (0;3,4,6), and d₃ = 25/12 for (0;2,8,8) vs (0;3,3,12) (as in Fig. 1). The six signatures of area π/2 with orders ≤ 12 are as stated.
9. **Lemma 8.1.**
   - I re-derived B_{n+1} and x_{n+1} = −x_n(1+x_n)(u−u⁻¹)².
   - The non-vanishing of the x_n is correct, including the parabolic commutator when exactly one fixed point is shared.
   - The conjugation by A^{−k_n} that forces C_n → A is correct.
   - I checked the trace identity tr[γ,β] − 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r (bc = −sin²(φ/2)cosh² r) numerically with explicit matrices. The point h(i) is at distance exactly r from the axis.
10. **Proposition 8.2.**
    - The triangle side lengths are correct: cosh s_m = 2cos(π/m)/√3 and cosh h_m = 1/(2 sin(π/m)).
    - The cone ball is embedded (P = Stab(v_m)·(T ∪ sT); the boundary is at distance h_m because the angle at v₂ is π/2).
    - The connectedness argument for the axis is correct, as is the estimate d(x, v₃) ≤ 2s_m (d(v_m,v₃) − h_m ≤ s_m by the triangle inequality).
    - **Recomputed constants:** ℓ₂,₃ = 0.5620668712, s_∞ = 0.5493061, cosh 2s_∞ = 5/3, h₇ = 0.5452748, and h_m ≥ log(m/2π).
11. **Proposition 8.3, Remark 8.4, Corollary 8.5.**
    - Formula (3) is correct, including q = 1/4 − 1/(4 sinh²ρ) and q = 1/4 + 1/(4 cosh²ρ).
    - The min–max argument with disjoint arches is correct.
    - The pigeonhole count (⌊Λ_N/δ⌋+1)^{N−1} is correct. The case analysis for A < π/3 is correct.
    - The growth (N−1)log(c′N²/δ+1) ≥ log(M−6) is correct.
    - Garbin–Jorgenson condition (a) holds exactly from m ≥ 13: m/2π ≥ 1 + m/4π fails at m = 12.
12. **Section 8.2.**
    - The Lambert-quadrilateral relation sinh a sinh b = cos(π/k) is correct.
    - The embedded collar is correct.
    - The λ₁ Rayleigh quotient is correct: ∫₀^a ρ² cosh ρ dρ = (a²+2) sinh a − 2a cosh a.
    - The λ_j bound with arches on [a/2, a) is correct.
    - The 4b values give exactly the eight systole bounds of Table 4 when rounded down at the sixth decimal (margins 5.5×10⁻⁸ to 9.3×10⁻⁷; the smallest is O(3,3,12), consistent with "at least 5×10⁻⁸").
    - The closed forms 2arccosh(1+cos(π/4)) = 2.2567679 and 2arccosh(1/2+cos(π/12)) = 1.8626041 match Table 4.
    - The (1;3) Gauss–Bonnet remark is correct.

**Geometric hypotheses of the main theorems.** Area, systole and order bound are all used where they should be:

- The area enters through the finiteness of Sig(A,M), the bound n + 4g ≤ A/π + 4, and |Y| ≤ A/v₀.
- The systole enters through Lemma 2.2(ii) and Lemmas 4.2, 4.3 and 4.5.
- The order bound enters through k\* ≤ M, L_M, |b_K(M)| and d₀.

The absence of parabolic elements is used correctly in Lemma 4.2 (X ≠ 1) and Lemma 8.1. The count n_O(x) ≤ C\*e^x feeding Theorem 6.2 is proved from A, ε and M alone, as the abstract claims.

## FATAL

None.

## MAJOR

**M1 (pp. 10–12, Section 4; p. 23, Lemma 8.1): the dependence on M in Section 4 is an artefact, and the classical tool that removes it is already in the paper.**

Lemma 4.2 gives d₀ = min(ε/2, arccosh(1 + 2/(π²M²))), which is about 0.64/M. Jørgensen's inequality, applied to two elliptic generators f, g of orders p, q with distinct fixed points (a non-elementary pair once max(p,q) ≥ 3), gives

  4 sin²(π/p) · (1 + sin²(π/q) · sinh² d) ≥ 1.

I checked numerically that tr[f,g] − 2 = 4 sin²(π/p) sin²(π/q) sinh² d. So for p ≥ 7:

  sinh² d ≥ (1 − 4sin²(π/p)) / (4 sin²(π/p) sin²(π/q)).

This bound has three relevant features:

- It is attained by the triangle group (2,3,7): it gives exactly h₇ = 0.545275 for q = 2 and d(v₃,v₇) = 0.620672 for q = 3.
- It grows like log(pq): it is 1.09 for p = q = 7 and 6.9 for p = q = 100, against the paper's 0.091 and 0.0064.
- Applied to the vertex w, it also excludes the near-degenerate triangles with a high-order third vertex that drive the 1/M in the proof of Lemma 4.2.

Two consequences follow.

- A separation bound for cone points that does not depend on M looks within reach.
- With it, cone balls of radius about log M and area bounded below would give v₀ and the diameter bound with roughly A·log M growth instead of the AM³ claimed on p. 11. That would match the lower bound diam O(2,3,m) ≥ log(m/2π) of Proposition 8.2.

The authors write "we expect the factors 1/M … not to be intrinsic, but do not prove it" (p. 11). For a paper whose stated point is explicit constants, this needs more. Either prove the M-free separation, or state the expected growth as a precise conjecture and explain why the Jørgensen route fails.

The paper should in any case cite the relevant literature:

- Beardon [36], §5.4 (Jørgensen's inequality in general, which makes the self-contained proof of the hyperbolic case in Lemma 8.1 unnecessary) and the chapter on elliptic elements and distances between fixed points.
- Dryden–Parlier, "Collars and partitions of hyperbolic cone-surfaces", Geom. Dedicata 127 (2007), doi:10.1007/s10711-007-9172-6 (arXiv:math/0405129). It gives embedded collars and cone neighbourhoods for cone angles < π, which is exactly the content of Lemmas 4.2–4.3.

This is not a correctness issue: C\* enters Theorem 6.2 only through log C\* in t₃, and t₁ binds in seven of the eight rows of Table 3. It is a positioning and sharpness issue for Section 4.

*Resolution:* add the Jørgensen elliptic bound, and either a proof of an M-independent d₀ (and the resulting v₀, D, C\*) or an explicit statement of why it is not pursued. Cite Beardon §5.4 and Dryden–Parlier.

**M2 (pp. 4, 11–12): Theorem 4.4 is not used anywhere in the logical chain, yet the text says it is.**

- p. 12 states: "Theorem 4.4 is used for the finiteness statement of Section 1 and, through Lemma 2.2(i), for instances whose diameter is bounded directly (Section 7)."
  - The finiteness argument of Section 1 (p. 3) uses Mumford–Bers compactness, not Theorem 4.4.
  - The instances of Section 7 use the proved bound 2 diam P with Lemma 2.2(i), not Theorem 4.4.
- On p. 4, the diameter bound is offered as input to the Proctor–Stanhope finiteness of diffeomorphism types in isospectral families. At curvature −1, however, the spectrum already determines the signature [1], [6], so that conclusion is immediate for the paper's class.

So the section titled "The diameter" proves a theorem whose only role is Table 2 and a comparison (πe^{3D}/A versus C\*).

*Resolution:* either correct the sentences on pp. 4 and 12 to say plainly that Theorem 4.4 is a side result (kept for comparison and for the instance-level discussion), or demote it to a remark. If M1 is carried out, Theorem 4.4 becomes meaningful again as a sharp-in-order statement next to Proposition 8.2.

**M3 (pp. 5–6, 8–9, 30–32): overlap with the companion paper.**

All of Section 3 except Lemma 3.3 is taken from [31] (Table 1). Appendix A reproves it, along with the trace formula, Proposition 2.3 and the cone polynomials. Lemma 3.3 is itself "a direct consequence of [31, Lemmas 2.11 and 3.6]".

The appendix makes the paper self-contained, which I value, and every reproduced proof is correct. The editor should nevertheless decide whether this much shared material (Theorem 2.1, Lemma 2.2, Proposition 2.3, Lemmas 3.1, A.2–A.4, Theorem 3.2) is acceptable when both papers are submitted simultaneously.

*Resolution:* an editorial decision. Scientifically, I would keep Appendix A but shorten Sections 2–3 to statements with pointers.

## MINOR

- **m1 (p. 10, Lemma 4.2 statement).** p̃ and q̃ are not introduced in the statement ("distinct elliptic points satisfy d(p̃, q̃) ≥ …"). Write "for distinct elliptic points p̃, q̃ ∈ H²".
- **m2 (p. 7, Lemma 2.2).** "Oriented" closed geodesics: when there are cone points of order 2, a hyperbolic class can be conjugate to its inverse (γ = e₁e₂ with e₁, e₂ involutions). Then the "two orientations" are one class. The counting and the trace formula are unaffected, but the parenthetical should say "hyperbolic conjugacy classes" without implying that each geodesic is counted twice.
- **m3 (p. 9, Lemma 3.3(ii)).** A is reused for the common area of σ, σ′, while elsewhere A is the class bound. Lemma 6.1 applies the lemma to signatures of area ≤ A. Use a different letter, or say "area at most A" and note that ⌊Area/π⌋ ≤ ⌊A/π⌋.
- **m4 (p. 12).** "between about 10^196 and 10^29326": the recomputed values are 10^196.5 and 10^29325.4, so the upper end is about 3×10^29325. Write "about 10^196 and 10^29325", or give a × 10^b.
- **m5 (p. 25, remark after Proposition 8.2).** The search values fit 2 arccosh((1 + 2cos(2π/m))/2): 0.983987 at m = 7 (as noted) and 1.921313 at m = 100 (the printed 1.9213). The data therefore suggest that this closed form is the systole of O(2,3,m) for all m ≥ 7, increasing to the modular value 2 arccosh(3/2). Say so, as a conjecture or with a reference. If it can be proved (e.g. by trace arithmetic in Z[2cos(π/m)]), it replaces the crude ℓ₂,₃ = 0.562 by about 0.984 in Theorem 1.3.
- **m6 (p. 25, Proposition 8.2 proof).** "P is star-shaped about v_m": add that the 2m tiles at v_m have angle π/m each and fill a neighbourhood of v_m. Also add that the folding f is well defined because T is a strict fundamental domain of the reflection group W.
- **m7 (p. 26).** Garbin–Jorgenson condition (a) is verified only for m ≥ 13 (it fails at m = 12 with this inequality). Say explicitly that the limit statement concerns m → ∞, so the finitely many m < 13 do not matter.
- **m8 (pp. 28–29, Problem 1 discussion).** "So a negative answer to (b) would follow from two degenerating families …": as written, this already presupposes the lower bound λ_j ≥ 1/4 − o(1) for orbifolds, which the next paragraph says is missing. Move the caveat into that sentence ("would follow, given an orbifold version of …").
- **m9 (p. 23, Lemma 8.1).** The proof of the hyperbolic case is correct but reproves a textbook result (Jørgensen [42]; Beardon [36], Thm 5.4.1). A citation suffices unless the authors want the elliptic case for M1.
- **m10 (p. 4).** In the Buser–Courtois paragraph, the claim that Theorem 1.1 is "an effective counterpart" should acknowledge that it concerns the signature, which is a much coarser invariant than the isospectral class treated in [7]. The sentence partly says this; make it explicit there and not only in Problem 1.

## Presentation

- **P1.** Lemma 4.1 is the only numbered lemma without a title; the proof of (H3) is a single dense paragraph. Split (H1)–(H3) into separate proofs.
- **P2.** Section 8 alternates proved statements with numerical observations: the word search on p. 25, the monotonicity in m on p. 26, and the "6% to 16%" observation on p. 27. Each is labelled, which is good. Grouping them in one "Numerical observations" paragraph would make the boundary between theorem and experiment unmistakable.
- **P3.** Lemma 4.5 is the result Theorem 6.2 needs, yet it is placed after the diameter theorem it supersedes. Consider putting Lemmas 4.2, 4.3 and 4.5 first and Theorem 4.4 last, or in a remark (see M2).
- **P4.** In my sections the figures are consistent with the text: Fig. 3(a)/(b) levels and bounds, and the shading of Fig. 1 against the d₃ = 25/12 slope.

## What is good

**The geometric arguments are correct throughout.** The constants are reproducible from the stated formulas: I reproduced Tables 2–4 in the parts I checked, as well as ℓ₂,₃, h_m, the systoles and the 4b values. The authors consistently separate what is proved from what is observed or computed. Specific strengths:

- the reflection trick in Lemma 4.2;
- the diameter-free count in Lemma 4.5;
- the uniform systole for O(2,3,m) via Jørgensen in Proposition 8.2;
- the clean lower bound log M / log log M in Corollary 8.5.

## Recommendation

**Minor revision** for Sections 3, 4 and 8 and the appendix results they depend on. Confidence is high on correctness (every proof checked; Lemma 3.3 / Theorem 3.2 checked independently on more than 11,000 equal-area pairs). Confidence is moderate on the significance of the geometric part, which is a careful but standard support for the main theorem. M1 is the substantive request. It does not affect the validity of any stated result, but for a paper about explicit constants the order dependence should be either removed or explained.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Jørgensen elliptic bound added; M-free d₀ (and v₀, D, C\*) proved or the obstruction explained; Beardon §5.4 and Dryden–Parlier (2007) cited. |
| M2 | Sentences on pp. 4 and 12 corrected; Theorem 4.4 either justified or demoted to a remark. |
| M3 | Editorial decision on overlap with [31]; optionally shorten Sections 2–3 to statements. |
| m1, m3 | Notation fixed in Lemmas 4.2 and 3.3. |
| m2 | "Oriented" removed or qualified (order-2 points). |
| m4 | Exponent corrected to 10^29325. |
| m5 | Closed-form conjecture for the systole of O(2,3,m) stated. |
| m6, m7 | One-line justifications added in the proof of Proposition 8.2 and in the Garbin–Jorgenson paragraph. |
| m8 | Caveat moved into the "would follow" sentence. |
| m9 | Lemma 8.1 replaced by a citation (or extended to the elliptic case). |
| m10 | Scope of the comparison with Buser–Courtois made explicit. |
| P1–P3 | Restructuring as indicated. |
