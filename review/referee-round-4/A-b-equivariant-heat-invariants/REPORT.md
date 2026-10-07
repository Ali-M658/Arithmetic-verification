<!-- Saved verbatim by the main session from the reviewer's returned text: the harness refused the reviewer's own write. Scripts and outputs are in its git-ignored scratch/. -->

# Referee report

**Manuscript:** "How much of a hyperbolic orbifold does heat hear?" (39 pp.), with Online Resource 1 (14 pp.)
**Journal:** Annals of Global Analysis and Geometry
**Referee's angle:** heat invariants of orbifolds (Donnelly; Dryden–Gordon–Greenwald–Webb; Stanhope; Sutton; Uçar; Schueth). The question I asked first of each result: does it follow quickly from known equivariant expansions or known results on orbisurfaces, and is the novelty claim calibrated against that literature?

---

## Summary

The paper works with closed orientable 2-orbifolds of curvature −1 that have only cone points (the class Sig). It asks how many heat invariants c_1,…,c_k (where Z(t) ~ Σ c_j t^{j−2}) are needed to determine the signature (g; m_1,…,m_n).

- **Section 2: the expansion.** The heat expansion at K = −1 is re-derived from the Selberg trace formula (Prop. 2.7, App. B), with the cone polynomials p_l in closed form (Lemmas 2.6, 2.8). It is observed that c_{j} adds exactly one new odd power sum P_{2j−3} of the cone orders, through Ψ_k = P_{2k−1} − R (Lemma 2.10).
- **Section 3: hearing the signature.** Comparing two orbifolds reduces to an odd-power Prouhet–Tarry–Escott (PTE) system. Newton's identities give the following:
  - separation and the bound ⌊Area/π⌋+4 (Thm 3.4, Cor 3.5, Thm 1.1(i));
  - a sharp bound M for cone orders ≤ M (Thm 3.7);
  - growth √A ≲ f(A) ≲ A, with linear growth equivalent to N(k)=O(k) for the PTE function (Thm 3.13, Prop 3.14);
  - a Descartes-rule bound on genus changes (Thm 3.10).
- **Section 4.** Within a signature, every heat invariant agrees, and the shape enters at order t^{−1/2}e^{−ℓ²/4t} (classical; quantified in Thm 4.4).
- **Section 5: triangle orbifolds.** Two invariants suffice for p+q+r ≤ 17. The first failure is O(2,8,8)/O(3,3,12), and this pair is isolated because the cubic C_{27/2} has rank 0 (Thm 5.8, with a hand 2-descent in App. C). Three invariants always suffice.
- **Section 6.** Stability of recovering the orders from perturbed c_1,…,c_n (Thms 6.4–6.8).
- **Section 7 and supplement.** FEM spectra of the minimal pair and of a (0;3,3,3,3) family.

## Significance

**What is good.**
- The paper is unusually careful. Every claim I tested was correct (see the next section).
- Proofs are complete and short.
- Computer-dependent statements are clearly separated from proofs (Appendix D).
- Prior work is cited with pinpoint locations, and the authors flag what they do not prove.

Three things are genuinely attractive:
1. The clean reformulation: the first L heat invariants agree exactly when an "L-configuration" (Def. 3.9) exists.
2. The growth equivalence with the PTE function N(k), which turns an open number-theory problem into an exact statement about heat invariants.
3. The sharp bounded-order result (Thm 3.7), which explains that the area dependence is really a dependence on the largest cone order.

The triangle-orbifold analysis answers precisely the doubt raised in Dryden–Gordon–Greenwald–Webb, Rem. 5.16 (I verified the quotation in arXiv:0805.3148, p. 31).

**Calibration.** From the heat-invariant point of view, the new spectral-geometric content is thin.
- The only analytic input is the constant-curvature expansion, which is due to Uçar (thesis, Thm 4.20 with (4.33)–(4.35)).
- The determination of the cone orders from the full sequence is Uçar's Cor. 4.21(iv) / 4.23 (I checked the thesis).
- The mechanism of Lemma 2.10 is already in Uçar's proof of his Thm 3.40, which he invokes for Cor. 4.21: the top-degree coefficient W_ν of the ν-th corner/cone term is nonzero, which determines the sequence Σ(π^{2ν+2} − γ_i^{2ν+2})/(πγ_i^{2ν+1}) inductively. For γ = π/m this is, up to constants, Ψ_{ν+1} = P_{2ν+1} − R.

What remains new is the finite-count analysis. That analysis is elementary algebra and number theory about odd power sums of rationals (Newton identities, Descartes' rule, PTE, an elliptic curve, a modular sieve), plus a numerical-analysis section and FEM experiments. Theorem 1.1(i) itself is a few lines once Lemma 2.10 is available.

The result is correct and of some interest to AGAG readers. However, the manuscript's centre of gravity is outside global analysis, and at 39 + 14 pages it is long for what the heat-invariant side contributes.

## Correctness and what was recomputed

All of this was done in my own scratch folder, with exact arithmetic (sympy, Python fractions) unless stated, mpmath at 40 digits for analysis, PARI/GP (cypari2) and one C program. **I found no mathematical error.**

**1. Heat coefficients (Section 2).**
- I generated p_l for l < 10 from (4)–(5) and confirmed Lemma 2.8 for every one of them: degree 2l+2, leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)), p_l(1) = 0. Positivity for m > 1 holds because all coefficients in the variable m²−1 are nonnegative.
- I checked the closed form of Lemma 2.6 numerically (m = 2, 3, 5, 8), and the Taylor coefficients of Φ_m against (4) for k ≤ 4.
- **Independent derivation of b_l(m).** I took the moments m_{2k}(a), i.e. the derivatives of 1/(2 sin((a−s)/2)) (Euler's beta integral), and summed them over the elliptic classes directly. This does not use Lemma 2.6. Agreement with (5) was to relative 2·10^{−40} for m ∈ {2,3,4,7,8,12}, l ≤ 5.
- **Quadrature of E_m(t).** Direct quadrature of E_m(t) in Thm 2.3 at t = 0.002 matches the 5-term series: error 1·10^{−13} for m = 3 and 4·10^{−9} for m = 8, consistent with the divergence noted on p. 5.
- **Smooth term.** α_0,…,α_5 = 1, −1/3, 1/15, −4/315, 1/315, −4/3465 (McKean's values), and I(t) by quadrature matches the series.
- (7) and c_2 = χ/6 + Σ(m²−1)/(12m) are confirmed. These agree with the classical cone term (1/12)(2π/γ − γ/2π) at γ = 2π/m.
- **Minimal pair.** c_1,…,c_5 of O(2,8,8) and O(3,3,12) give d_3 = 25/12, d_4 = −1775/24, d_5 = 153025/48 (p. 31). c_3 = −1601/480 and −867/160 are consistent with Table S6.

**2. Proofs checked line by line:** Lemmas 2.4, 2.5 (including the constant C and the monotonicity), B.1, App. B; Theorem A; Lemma 3.3; Theorem 3.4; Cor. 3.5; Theorem 3.7(i)–(iii) (including the inequality 2M+(k−3)(k+1) > 0); Theorem 3.10; Props 3.11, 3.14, A.1, A.2; Theorem 3.13(a)–(d); Theorem 4.4; Theorems 6.5, 6.8; Props 6.6, 6.7.

**3. Explicit pairs.** I computed the exact number of shared invariants by two independent routes: (area, Ψ_k), and the cone coefficients b_l directly. Every pair agrees with the paper:
- Theorem C(3), including P_5 = 25159618 ≠ 21298618;
- Example 3.6; Example 3.16(i), (ii);
- (0;5,5,5)/(0;2,2,2,10);
- the M = 3, 4 pairs after Theorem 3.7, including c_M(g;m) − c_M(g';m') = (−1)^M C a_{M−2} (−1/3 and 1);
- Table S1 rows for L = 2, 3 (genus, cone count, Prouhet), L = 4 (genus, equal count, cone count), L = 5 (genus, equal count, cone count), and L = 6, 7 (cone count). All have equal area and share exactly L invariants.

**4. Algebra of Sections 3 and 6.**
- Theorem B: M e = b is solved by the true e, and det M = (−1)^{n(n+1)/2} ∏_{i<j}(m_i+m_j)/∏m_i, both symbolically for n = 2, 3, 4.
- Lemma 6.3: B = YM and det B, symbolically for n = 2, 3, 4.
- ζ_3, ζ_4, ζ_5 = 1, 79/3, 14048/15.
- amp_0..amp_4 = 2, 14, 498, 4062, 56230/3, and the row P_3 = −18c̃_1 −120c̃_2 −360c̃_3.
- δ_thm of Table S4 for (2,8,8), (3,3,12), (2,3,7), (4,4,4), (7,7,7): 3.80e−7, 1.189e−7, 4.49e−7, 9.35e−7, 9.97e−8, as printed.

**5. Theorem 5.8.**
- ψ maps E into C_{27/2} and φ∘ψ = id_E (exact, modulo the equation of E).
- disc(E) = 2^18 3^8 5^6; conductor 90.
- E(Q)_tors ≅ Z/6 × Z/2 (PARI elltors); #E(F_7) = #E(F_11) = 12.
- y = 21x+64 meets E in (x−16)^3.
- The twelve listed points of C_{27/2} lie on it, and the six positive ones map to (−24,±360), (−9,0), (−384,0), (−144,±2160).
- PARI ellrank gives [0,0]; ellanalyticrank gives 0.
- I also checked d' = 393² − 4·3456 = 3²5^6 in App. C.

**6. Triangle orbifolds.**
- **Enumeration to S ≤ 600.** I enumerated all hyperbolic triads with S ≤ 600 and confirmed:
  - Table S3 (83 triads with 10 ≤ S ≤ 18);
  - Table S2 (first overlaps and first collisions for p ≤ 14);
  - S*(p) of Theorem 5.4 for every p with S*(p) ≤ 600;
  - Theorems 5.5–5.7;
  - the first non-adjacent collision (5,15,15)/(7,7,21) at S = 35.
- The identities in the proof of Theorem 5.4 (φ_p − τ_p, the numerator of φ_p', gap_p(3p+7), x*(p) − 18) were checked symbolically.
- **Proposition S2.1 in full.** A C program over all 3.1·10^9 triads with 18 ≤ S ≤ 4800 (exact 128-bit comparison) returns exactly the 38 collision-free sums listed.

**7. Searches (partial reproduction).**
- **n = 4 witnesses.** All 4-multisets with orders ≤ 84 give exactly 8 primitive witnesses, as stated in Remark 3.2.
- **Remark 3.17 at a smaller bound.** All 1,036,667 five-multisets with gcd 1 and entries ≤ 40 give no partner cubic that splits over Q. Two cubics, for (1,1,1,5,20) and (3,4,5,6,30), have exactly one rational root, which is a nice illustration of why the modular test is needed.
- The partner triple of {1,1,1,1,7} is {0.2664, 4.2830, 6.4506}, as in S1.

**8. Figures.**
- Fig. 2: point positions.
- Fig. 6: dots at S*(p) and circles at the first collisions, for the adjacent pairs p = 2..7.
- Fig. 8(a): I computed the exact elliptic difference D(t) = 0.0156, 0.0313, 0.0467 at t = 0.01, 0.03, 0.1, and the truncations; both match the plotted curves.
- Fig. 4: systoles 4b(0) = 2.634 and 4b(2.8) = 0.694 from sinh a sinh b = 1/2.

**Not recomputed:** the FEM spectra (S4–S6); the exact K_mult on the 525 area classes (dots of Fig. 3); the n = 4 search to 440 and the n = 5 search; the full Remark 3.17 search to 220; δ_cert of Prop. S3.1.

## MAJOR issues

**M1. The novelty claims about heat invariants are not calibrated against Uçar (pp. 5–6 §1.2; p. 10 Lemma 2.10; p. 3 Theorem 1.1(i)).**
- §1.2 credits Uçar [14] only for the coefficients and for recovery "from the whole sequence".
- The structural fact on which the whole paper rests is "each coefficient switches on one more odd power sum, with nonzero top coefficient" (Lemma 2.10, p. 10, and "The mechanism is the same throughout", p. 4). That fact is the engine of Uçar's proof of Thm 3.40 and hence of Cor. 4.21(iv): the top-degree term W_ν is nonzero because B_{2ν} ≠ 0, and the sums Σ(m_i^{2ν+1} − 1/m_i) are determined inductively.
- Theorem A (p. 11) is, as the authors partly acknowledge, the Newton-identity uniqueness for odd power sums plus the reciprocal sum.
- Theorem 5.1 / Theorem 1.2(iii) is the n = 3 case of Theorem A.

So what is genuinely new is that a *finite, explicit* number suffices, together with the analysis of that number. The introduction and abstract should say this plainly:
- Lemma 2.10 should be attributed to the mechanism of Uçar's Thm 3.40.
- The phrase "to our knowledge … the first explicit such number" (p. 5) should be accompanied by the remark that it follows in a few lines from Uçar's triangular structure and Newton's identities.
- The section should state up front that, after Section 2, no further heat-kernel input is used.

**M2. Scope, length and focus (whole manuscript, supplement, companion papers).**
Of the 39 pages, the heat-kernel input occupies about 4 (pp. 6–10 and App. B). The rest consists of:
- PTE combinatorics (pp. 15–20);
- triangle arithmetic, including an elliptic curve with a hand 2-descent (pp. 23–27, App. C);
- conditioning of polynomial root recovery (pp. 27–30);
- FEM numerics (pp. 30–32);
- a 14-page supplement with integer cone orders of up to 40 digits (Table S1).

Section 4 (pp. 20–22) records classical facts at length:
- Prop. 4.1 and Cor. 4.3 are immediate from Prop. 2.7 and Teichmüller theory;
- Prop. 4.2 is textbook;
- Theorem 4.4 is McKean/Huber with an explicit but, by the authors' own account, loose constant (p. 22, S6).

For an AGAG readership I ask for a focused version:
- condense Section 4 to a remark with references;
- move most of Section 6 and Section 7 to the supplement, or justify them in spectral terms (see M3);
- shorten §3.4 and Table S1.

In addition, p. 26 states that a companion manuscript ("Triples with equal sum and equal reciprocal sum") is devoted to "the arithmetic of these degeneracies" and cites Theorem 5.8. The editor should obtain both companion manuscripts (that one, and the one on finitely many eigenvalues, p. 5) to rule out overlapping publication of §5.2 / App. C and of the stability material.

**M3. Section 6 and Theorem 1.3 are weakly motivated, and Theorem 1.3 overstates one point (p. 4 Theorem 1.3; pp. 27–30).**
- **Unobservable error model.** The error model perturbs c_1,…,c_n directly. Heat invariants are not observable quantities, and no map from spectral data with controlled error to heat invariants with controlled error is given. Section 7/S4 extracts them by heuristic fits whose error bars are "heuristic and not standard errors" (S4, p. 12 of the supplement).
- **Loose threshold.** The rigorous threshold δ_thm is off by factors 5·10² to 2·10⁸ (p. 30). The useful certificate δ_cert lives in the supplement, and "no result here depends on it".
- **Generic content.** Most of the content (Rouché, Hadamard, Hurwitz conditioning) is generic numerical algebra, not spectral geometry.
- **Overstatement.** Theorem 1.3 says "for data that are heat invariants of positive real orders it is 1/2, and attained, at a double order and when all n ≥ 3 orders are equal". This reads as a general statement for realisable data. What is proved is the exponent 1/2 only at a double order (Prop. 6.6(i), with the general k = 2 bound) and in the all-equal case (Prop. 6.7). Other clusters are explicitly "not settled" (p. 29).

Please either (a) connect Section 6 to spectral data, for example via the eigenvalue companion or via an explicit bound on how heat invariants are recovered from finitely many eigenvalues, or (b) reduce it to a short proposition and rephrase Theorem 1.3 to state exactly the configurations proved.

**M4. The dependence on the normalisation K = −1 should be addressed or stated as a limitation (p. 1 Abstract; p. 3 Theorem 1.1; p. 5 §1.1; p. 10 end of §2.3).**
- Every count in the paper presupposes that the curvature is known to be exactly −1. Uçar's Cor. 4.21(iv) also assumes κ known, and the authors note on p. 10 that "an unknown K is one more unknown, tied to χ by K Area = 2πχ" but do not pursue it.
- In the spectral problem one is normally given only the spectrum. Whether Theorem 1.1(i) survives, perhaps with one more invariant, when the competitor class is all closed orientable orbisurfaces of constant negative curvature (arbitrary scale) is a natural and probably short question that the paper should answer.
- §1.1 motivates heat invariants as "what is available when the geometry is known only locally" and discusses variable curvature (Schueth). None of the counts apply there, because c_j then involves ∫ curvature polynomials and K(p), ΔK(p) at the cone points. The title and abstract should make the constant-curvature, known-K setting explicit.

## MINOR issues

- **m1** (p. 3 Thm 1.1(iii); p. 14 Thm 3.7(iii); p. 15 Cor. 3.8(b),(c); p. 17 discussion). "log" is not specified. The proof (p. 15) uses log(1+y) ≥ 2y/(2+y) and λ ≥ log 8 > 2, so it is the natural logarithm. Say so.
- **m2** (p. 3, §1 after Thm 1.1). The non-orientable remark treats only an even number k = 2g of crosscaps. For odd k the "genus" is a half-integer, |U|+|V| can be odd, and the parity step of Theorem 3.4 (κ even) fails. State whether Theorem 1.1(i) extends to all locally orientable closed hyperbolic 2-orbifolds without mirrors, or restrict the remark explicitly.
- **m3** (p. 3 mirrors; p. 5 "orbifolds in Sig with different signatures have different spectra"). Cite Doyle–Rossetti, "Laplace-isospectral hyperbolic 2-orbifolds are representation-equivalent" (arXiv:1103.4372). Via the Selberg trace formula, it shows that the spectrum determines the area, the total mirror length and the number of cone points of each order, mirrors included. This is the most directly relevant spectral result for hyperbolic 2-orbifolds and is not cited.
- **m4** (pp. 5–6, literature). Also missing:
  - Proctor–Stanhope, Differ. Geom. Appl. 2009 (spectral finiteness of 2-orbifold diffeomorphism types);
  - Rossetti–Schueth–Weilandt, AGAG 2008 (isospectral orbifolds with different maximal isotropy orders: what the spectrum does not hear about singular strata);
  - Gittins–Gordon–Khalile–Membrillo Solis–Sandoval–Stanhope, Michigan Math. J. 2023 (heat invariants of the Hodge Laplacians of orbifolds and the singular set);
  - for cone points of arbitrary angle and curved corners: Nursultanov–Rowlett–Sher (MATRIX 2019; Ann. Math. Québec 2024), Aldana–Kirsten–Rowlett (Ann. Math. Québec 2025), Suleymanova (arXiv 2017).

  These locate the paper within the "which orbifold data do heat invariants hear" line that the introduction invokes.
- **m5** (p. 10 §2.3, "So each power of the curvature switches on one more odd power sum"). Attribute this to Uçar, as in M1.
- **m6** (p. 23 Theorem 5.1, p. 4 Theorem 1.2(iii)). This is the n = 3 case of Theorem A, a three-line Newton-identity computation. Present it as a corollary or remark, not a theorem.
- **m7** (p. 21 Prop. 4.1, Prop. 4.2, Cor. 4.3). Standard; condense (see M2).
- **m8** (p. 4, Theorem 1.3, last sentence). Rephrase as in M3.
- **m9** (p. 18, heuristic paragraph after the T(L) table). The degree-sum heuristic is not made precise, and the authors immediately say it "predicts little". Delete it or state it as a precise expectation.
- **m10** (pp. 7, 10–13, 15, 28: notation clashes).
  - h_t (Selberg test function, p. 7) versus 𝔥_t (heat kernel, p. 4 and Fig. 1).
  - κ is |U*|+|V*| (p. 13), a constant in Theorem C(1) (p. 12) and Uçar's curvature (p. 9).
  - C is the integer of Thm 3.7(ii), the constant C(A,ℓ,diam) of Lemma 2.5 and the constant in N(k) ≤ Ck^β.
  - T is T(L), 𝒯 (Theorem B) and Teich.

  Please disambiguate.
- **m11** (p. 13 Cor. 3.5). "so the cone count is determined without being known in advance" is unclear. What is meant is that the bound n ≤ A/π + 4 uses only c_1. Rephrase.
- **m12** (p. 31 §7). State in the main text, not only in S4 "Limitations", that the eigenvalue errors are agreements between discretisations, not enclosures. Also state that the statement "no eigenvalue below about 1.6·10⁴ is missing" is conditional on those error bars.
- **m13** (p. 36 App. D; p. 19 Fig. 3). The exact K_mult values on the 525 complete area classes (Fig. 3 dots) are a computer result used to draw a figure but are listed nowhere. Add a table, or at least the maximisers, to the supplement.
- **m14** (p. 5 and p. 12). Steinig [16] (Rend. Mat. 1971) is hard to access. Since Theorem A is said to be "of the type of" Steinig's theorem, state precisely what Steinig proves, so the reader can judge the difference.
- **m15** (p. 32 Data availability). The repository is under an individual GitHub account whose name is not an author's. Apart from the Zenodo placeholder (treated as known), state who maintains it.

## Presentation (figures and captions included)

Writing quality is high and dense, sometimes too dense: definitions are often introduced inside sentences (e.g. f_g, f_n on p. 17; T(L), A_min(L) on p. 17). The roadmap on p. 4 is helpful. Specific points:

- **P1, Fig. 1 (p. 2) and text (p. 4).** The caption says "in schematic shapes". The text says the value "computed on the true hyperbolic triangle, is drawn at the point with the same Poincaré-disc coordinates", which would draw the true triangle, not a schematic one. Explain what map was used. Also define 𝔥_t in the caption.
- **P2, Fig. 2 (p. 14).** The colour key (teal/orange for the two orbifolds in (a); black for U* including the padding 1 and grey for −V* in (b)) is only in the text on p. 13. Put it in the caption. I checked that the point positions are correct.
- **P3, Fig. 3 (p. 19).**
  - The dashed lower bound comes from non-constructive (pigeonhole) pairs that are not plotted. Say so in the caption, since otherwise the Prouhet squares at s ≈ 255 and 1023, far below the dashed curve, look inconsistent with a lower bound on the maximum.
  - Explain the half-filled disc.
- **P4, Fig. 6 (p. 26).** Correct as drawn: I recomputed all dots and circles. The caption should say that dots and circles refer to the adjacent pairs (p, p+1), p = 2,…,7 (there is no dot for p = 8, since stratum 9 is not drawn) and identify the split disc.
- **P5, Fig. 7 (p. 30).**
  - There is no legend, and the caption does not say which curve is (2,3,7), (2,8,8) or (4,4,4), nor what the dotted curve, the diamonds and the horizontal line are. This is only on p. 29.
  - The caption says "The slopes are the exponents of Theorem 6.5", but the dotted slope 1/2 is Prop. 6.7.
- **P6, Fig. 8 (p. 31).** The caption does not identify the heavy, dashed and grey curves in (a), or the circles, dotted lines and shading in (b); these are in the text and in S6. Make the caption self-contained. The (a) panel agrees with my quadrature of the elliptic difference.
- **P7, Fig. 4 (p. 22).** Fine. State in the caption that λ_j is on a square-root scale and that the heavy curve is λ_1.
- **P8.** The abstract is long and spends a third of its length on triangle-orbifold arithmetic. In line with M1/M4, it should state the K = −1 normalisation and that the heat input is Uçar's expansion.

## Recommendation

**Major revision.** Confidence: high on correctness (extensive independent recomputation, no errors found); moderate on the significance assessment for this journal.

The mathematics is correct and carefully done. The reasons for "major" are not errors:
1. The heat-invariant novelty is overstated relative to Uçar's thesis (M1).
2. The paper's bulk lies outside global analysis and needs focusing, with a check for overlap with the two companion manuscripts (M2).
3. The stability section is weakly motivated and slightly overstated (M3).
4. The essential K = −1 normalisation is neither analysed nor flagged (M4).

A focused version of perhaps 25 pages, centred on Theorems 1.1, 3.7, 3.13 and the triangle first-failure, with honest attribution, would be a reasonable AGAG paper.

## What resolves each issue

- **M1:**
  - Attribute the triangular mechanism (Lemma 2.10) to Uçar's proof of Thm 3.40 / Cor. 4.21.
  - In §1.2 and the abstract, state that the new contribution is the explicit finite count and its growth analysis, obtained from Uçar's expansion by elementary algebra.
  - Downgrade Theorem 5.1 and qualify Theorem A as classical in substance.
- **M2:**
  - Condense Section 4 to about one page of remarks.
  - Move most of Sections 6–7 and the large-integer parts of §3.4 / Table S1 to the supplement.
  - Shorten App. C, for example by citing ellrank plus a one-paragraph descent sketch, unless the authors argue it is essential.
  - Supply both companion manuscripts to the editor, with a statement of what each contains that this one does not.
- **M3:** Either (a) give a result linking finitely many eigenvalues (with error) to heat-invariant error, making Theorem 1.3 a spectral statement, or (b) shorten Section 6 to the qualitative Lipschitz/Hölder statement. In both cases, rephrase Theorem 1.3's last sentence to "1/2 at a double order and when all n ≥ 3 orders are equal; other realisable configurations open".
- **M4:** Add a proposition or remark on the case where the curvature is unknown but constant and negative: how many extra invariants are needed to fix K, and does ⌊A/π⌋+5 (say) suffice? State the K = −1, constant-curvature hypothesis in the title or abstract and in §1.1.
- **m1:** Write "ln" or state "natural logarithm" at first use.
- **m2:** Add the odd-crosscap discussion, or restrict the statement explicitly.
- **m3, m4:** Add the listed references with one sentence each on their relation.
- **m5:** Attribution sentence after Lemma 2.10.
- **m6:** Make Theorem 5.1 a corollary of Theorem A.
- **m7:** Condense (with M2).
- **m8:** As in M3.
- **m9:** Delete or make precise.
- **m10:** Rename, for example k_* for |U*|+|V*|, c_M for the integer C, a different letter for the Selberg test function.
- **m11:** Rephrase.
- **m12:** One sentence in §7.
- **m13:** Supplementary table of the 525 class maxima, or at least of the classes where K_mult ≥ 3.
- **m14:** State Steinig's theorem.
- **m15:** Maintainer statement.
- **P1–P8:** Self-contained captions with line and colour keys. Explain the Fig. 1 drawing map, the Fig. 3 dashed bound and squares, and the Fig. 6 pair indexing. Shorten the abstract.
