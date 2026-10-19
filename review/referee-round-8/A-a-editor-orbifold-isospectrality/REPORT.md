<!-- Round 8 A-a editor report: returned text saved verbatim; the reviewer could not write files -->

Writing to REPORT.md was refused, so the full report follows.

# Handling editor's report: Annals of Global Analysis and Geometry

**Manuscript:** "How much of a hyperbolic orbifold does heat hear?" (58 pp.), with Online Resource 1 (16 pp.)
**Disclosed related manuscripts:** "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (submitted to AGAG); "Triples with equal sum and equal reciprocal sum" (Integers).
**Treated as known:** the placeholders for author contributions, the AI-use statement, the Zenodo DOIs and the preprint identifiers.

Page numbers are the printed page numbers, which equal the PDF page numbers. "S" means the supplement.

---

## 1. Summary

The paper studies closed orientable hyperbolic 2-orbifolds that have only cone points (the class Sig). It asks how many heat invariants c_1, …, c_k are needed to determine the signature (g; m_1, …, m_n). Here c_j is the coefficient of t^{j−2}, and the count is K_mult(O; C).

**Geometric input:**
- Uçar's cone coefficients at constant curvature, re-derived in closed form from the Selberg trace formula (Lemma 2.7, Prop. 2.8, App. B).
- New *enveloping* remainder bounds for the cone series and the area series (Prop. B.2, eq. (6)).
- Uçar's triangular structure (Lemma 2.11): each c_{l+2} adds exactly one new odd power sum P_{2l+1}, next to the reciprocal sum R.

From there, almost everything is about signed integer multisets whose low odd moments and reciprocal sum vanish.

**Main results:**
- **Thm 1.1 / 3.11.** If all cone orders are at most M, then M + 1 invariants suffice against all of Sig, at every area. This is sharp: Lagrange-weight constructions give pairs sharing exactly c_1, …, c_M. The proof uses Vandermonde and Descartes sign-change arguments.
- **Cor. 1.5 / 3.8.** ⌊Area/π⌋ + 4 invariants always suffice.
- **Thm 1.2 / 3.18 and Prop. 3.19.** f(A) ≳ √A. A power lower bound f ≥ cA^α holds if and only if N(k) = O(k^{1/α}), where N(k) is the least size of a degree-k Prouhet–Tarry–Escott (PTE) solution. So linear growth is equivalent to the open problem N(k) = O(k).
- **Thm 1.3.**
  - n invariants suffice for spheres with n cone points (Newton and Hurwitz algebra).
  - The recovery system has a closed-form determinant (Orlando/Hurwitz).
  - n − 1 invariants fail for n = 3, 4.
  - A change of genus costs extra invariants (a Descartes-type bound).
- **Thm 1.4 / Section 5 (triangle orbifolds).**
  - Within the triangle class, 3 invariants suffice, and 2 suffice when the order sum is at most 17.
  - O(2,8,8) and O(3,3,12) are the first collision.
  - That pair is isolated, via the rank-0 curve C_{27/2} ≅ 90.c3 and a hand 2-isogeny descent (App. E).
- **Section 2.4 (variable curvature).**
  - A structure theorem for cone terms, proved only in outline (Prop. 2.13).
  - Prop. 2.15: in variable curvature, equal c_2 extends to equal H_L. Pairs such as (2,8,8)/(3,3,12) carry metrics, flat near the cone points, whose invariants agree to all orders.
- **Section 4.** Locality, with an explicit constant for where closed geodesics enter, illustrated by finite-element spectra.
- **Section 6 / App. C.** Stability of recovering real orders from perturbed c_1, …, c_n: Lipschitz at simple orders, Hölder at multiple ones.

**What is good:**
- The paper is exceptionally careful, honest and internally consistent. Every number I recomputed was right (Section 3).
- It separates proof, computation and heuristic scrupulously.
- It credits prior work fairly: Uçar, Fursaev, Laurens, Chen, and Bremner–Guy–Nowakowski.
- Several pieces are genuinely nice and, as far as I know, new:
  - the exact area-free answer M + 1;
  - the Hurwitz/Orlando determinant;
  - the clean reduction of the growth question to PTE;
  - the arithmetic isolation of the minimal pair;
  - the flat-cone construction of Prop. 2.15(iii). It shows that the expansion "hearing" the cone orders is a constant-curvature phenomenon.

## 2. Significance and scope

**Scope.** The paper is in scope. Inverse spectral problems for orbifolds and heat invariants of singular strata are standing AGAG topics: Stanhope 2005, Rossetti–Schueth–Weilandt 2008, Abreu–Dryden–Freitas–Godinho 2008, Schueth 2026. Dryden–Gordon–Greenwald–Webb asked whether their invariant c distinguishes triangular pillows, and Thm 1.4 answers that.

**Significance is the real question.**
- Once Lemma 2.11 (Uçar's) is granted, the main counts are statements about odd power sums of integers. The proofs use Newton's identities, Vandermonde determinants, Descartes' rule, pigeonhole and Lagrange interpolation; the authors say so themselves (pp. 5, 8).
- Thm 1.2 is, by the authors' own description, a reformulation. It moves an open Diophantine problem without progress on it.
- The new geometric and analytic content is Prop. B.2, Prop. 2.15 and the outlined Prop. 2.13.
- The authors themselves show that K_mult has no direct geometric or physical meaning:
  - it counts coefficients, not times (pp. 1, 3);
  - it is destroyed by arbitrarily small changes of the metric (p. 14);
  - in variable curvature it collapses to c_2 alone (Prop. 2.15).

The revision must make the geometric case explicitly.

## 3. Correctness and what I recomputed

I found no mathematical error. Computations were exact (SymPy or rational arithmetic) unless noted.

**Heat coefficients:**
- α_0, …, α_4 = 1, −1/3, 1/15, −4/315, 1/315.
- p_0, p_1, p_2 as in (8).
- p_3 = (m²−1)(m²+3)(3m⁴+2m²+19)/30240, which matches the K³ part of Remark 2.14(b).
- The leading coefficients |B_{2l+2}|/(2(l+1)!(2l+1)) and p_l(1) = 0 hold for l ≤ 4.
- Formula (10) for c_2, c_3 is exact.
- b_0 = (m²−1)/(12m).
- The closed form of Φ_m (Lemma 2.7) matches the direct sum to 30 digits.

**Enveloping remainders (Prop. B.2(a)).** Checked numerically with mpmath by integrating E_m(t) from Thm 2.3. For m = 3 and 12, t = 0.01 and 0.003, and K = 0, …, 6, every remainder has sign (−1)^K and modulus at most |b_K| t^K.

**Minimal pair:**
- c_2 = 67/48.
- d_3, d_4, d_5 = 25/12, −1775/24, 153025/48.
- (R, P_1, P_3) = (3/4, 18, 1032 vs 1782).
- For {3,10,15,30} vs {4,5,21,28}: P_5 = 25159618 vs 21298618.

**Thm 3.3.** The determinant, including the sign ς_n, verified symbolically for n = 2, 3, 4.

**Example pairs.** Areas and the exact number of shared invariants are as stated for:
- (0;2^10) / (1;4^4)
- (1;15) / (0;3,3,5,5)
- (1;15³) / (0;3,3,5,7,7,21)
- (0;4,4,5,5,6,12,12) / (0;2,2,2,3,10⁴)
- (0;5,5,5) / (0;2,2,2,10)
- (1;3^9) / (0;2^16)
- (0;2^28,4^8) / (1;3^27)
- the Table S1 rows with L = 2 (Prouhet), L = 3, and L = 4 (cone count)
- (2;) / (0;2^8)

**Thm 3.11(ii).** I rebuilt the construction for M = 2, …, 9. The least-genus areas are 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054}, as stated (p. 26).

**Proofs checked by hand:** Lemma 3.1; Thms 3.2, 3.7, 3.11(i)/(iii), 3.15; Prop. 3.16; Lemma A.1; Thm 3.18(a)–(d) with Prop. 3.19.

**Section 5:**
- There are 83 hyperbolic triads with 10 ≤ S ≤ 18, and the only R-coincidence is at S = 18.
- S*(p) brute-forced for p = 2, …, 15.
- The gaps 1/840, 1/2310, 1/10296 are correct. (The text extraction showed "23101"; the rendered page reads 1/2310.)
- The negative gaps at S*(p) + 1 are correct, and so is the formula for gap_p(3p+7) for p = 9, …, 15.
- The collision-free sums up to 600 are exactly the 38 listed in Computation S2.1.
- Table S2 reproduced for p = 2, …, 14.

**Thm 5.8 / App. E:**
- ψ maps E into C_{27/2}, and φ∘ψ = id modulo the curve.
- The twelve listed points lie on the curves.
- The discriminant is 2^18·3^8·5^6, and #E(F_7) = #E(F_11) = 12.
- The flex tangent is y = 21x + 64.
- c_4 and c_6 are 2^4 and 2^6 times those of LMFDB 90.c3. The LMFDB record gives j = 4102915888729/9000000, rank 0, torsion Z/2 × Z/6.
- The hand descent in App. E is correct case by case (mod 5 on E; mod 3 and 9 on E′).

**Variable curvature (consistency only):**
- Remark 2.14 agrees with Prop. 2.13(ii) at the top coefficient.
- It agrees with Prop. 2.13(iii) in the linear part for l = 1, 2, 3, matching Schueth's −m⁵ΔK/15120 and the Δ²K coefficient. I checked Σcsc⁶ and Σcsc⁸ numerically.
- The value ω_2/(2π) = 1/(60π) matches Ω_1.

**Section 6 / App. B:**
- amp_0, amp_1, amp_2 = 2, 14, 498, and P_3 = −18c̃_1 − 120c̃_2 − 360c̃_3.
- δR and δP_3 in Prop. 6.3(i) are correct.
- Remark B.4: Q_3 = 303.63, δ_1 = 4858·t_3, t_3 ≤ 7.8 × 10⁻¹¹, η ≤ 2.0714 × 10⁻¹⁹. All as stated.

**References.** Eight DOIs verified against Crossref.

**Not checked:** the finite-element spectra (S4–S6), δ_cert and δ_up in Table S4, the large searches, and the citations to Uçar's thesis and to Chen's survey.

**Confidence that the main results are correct: high.**

## 4. FATAL

**None.** I found no error that breaks a main result, no undisclosed duplication, and nothing out of scope.

## 5. MAJOR

**M1. Significance and the weight of the geometric contribution (pp. 1–8; Sections 3.3–3.4, 5).**
- The main theorems are combinatorics of power sums built on Uçar's structure. The genuinely geometric content (Prop. B.2, Prop. 2.15) is peripheral to them.
- The title asks how much heat hears. By the paper's own account (p. 6), that is already answered: Dryden–Strohmaier and Doyle–Rossetti for the whole spectrum, Uçar for the full expansion. What the paper actually answers is how many expansion coefficients are needed.

*Resolve:*
- Retitle, or state the object precisely.
- Add a section on what the counts mean geometrically.
- Promote Prop. 2.15(ii)–(iii) to the main results.
- Justify why Sections 3.3–3.4 belong in AGAG.

**M2. The physical framing of the headline numbers is overstated (abstract p. 1; p. 3; Remark B.4 p. 50).**

(a) **"Needs t of order 10⁻¹¹."** This figure depends on three choices:
- one extraction scheme: Vandermonde interpolation at t_3, t_3/2, t_3/4;
- one goal: δ_1 ≤ δ_thm, which guarantees exact rounding;
- the authors' lossy threshold δ_thm(2,8,8) = 3.80 × 10⁻⁷.

The supplement's equally rigorous certificate gives δ_cert(2,8,8) = 2.341 × 10⁻³ (Table S4). With δ_1 = 4858·t_3, which I recomputed, the same Lemma B.3 needs only t_3 ≲ 4.8 × 10⁻⁷, four orders of magnitude larger. Better schemes would do better still: exploiting the alternating remainders of Prop. B.2, or fitting the closed-form E_m directly. So "needs" is not a necessity statement. It is an upper bound for one method with one constant.

(b) **"At any fixed t > 0 the heat trace determines the whole spectrum"** (p. 1; similar wording on p. 3). Read literally, this says that a single value determines the spectrum, which is false. It should say: the function Z on any interval of times determines the spectrum.

(c) **The constant-curvature caveat is buried.** The diffusion picture is correct; I checked the flat-cone values 1.78 and 2.5 × 10⁻⁴. But no result uses it. The key "cannot detect" message is that the counts lose their meaning in variable curvature (Prop. 2.15). That belongs in the abstract, not only on pp. 3 and 19.

*Resolve:*
- Recast the 10⁻¹¹ and 10⁻¹⁹ figures as method-dependent upper bounds, and quote the δ_cert-based value.
- Fix the "fixed t" sentence.
- Add the curvature caveat to the abstract.

**M3. Proposition 2.13 is proved only in outline (pp. 15–17).**
- The paper itself says that three steps are not carried out:
  - the reduction to (I − dΦ_p)⁻¹;
  - the identification of the radial jet;
  - uniformity in ϑ of the inversion and of Laplace's method.
- The support offered is computer algebra for l ≤ 3, and l ≤ 7 for the linear part.
- Uniformity as ϑ → 0 is exactly where such arguments fail. A proposition in AGAG must be proved.
- Prop. 2.15(i) (p. 18) assumes equal Ω_l, which are not spectral data.
- The paragraph after Prop. 2.15 asserts without proof that several theorems "hold for pairs in that class".

*Resolve:*
- Complete the proof of Prop. 2.13, or relabel it a conjecture supported by Remark 2.14.
- Reformulate Prop. 2.15(i).
- Remove or prove the meta-claims.

**M4. Relevance of Section 6, App. C, S3 and S5, and of the numerics in Section 4, S4 and S6 (pp. 32–36, 42–45, 50–52).**
- Section 6 is standard root-perturbation theory (Rouché, Ostrowski). By the authors' own account, its application needs trace values accurate to 10⁻¹⁹.
- The blind recovery (S5) is "easy by design": the two candidates' c_3 differ by about 10⁴ error bars.
- The spectra illustrate classical facts: locality and the Huber–McKean asymptotics. They are not certified.
- The one claimed novelty of Section 4, the constant in Prop. 4.2(a), is loose by factors of 4.4 × 10⁶ to 1.0 × 10¹⁰ on the authors' own data (p. 35).
- This material also carries most of the overlap with the companion (see O1).

*Resolve:* justify each part against the paper's thesis, or move it to the companion, keeping only what a proof here uses.

## 6. MINOR

- **m1.** The paper relies on DGGW [2] — (5.7), (5.13), Thm 4.8, Ex. 5.3/5.6, Prop. 5.5, Thms 5.14–5.15 (pp. 3, 7, 13–15) — but does not cite its Erratum (Michigan Math. J. 66 (2017) 221–222, doi:10.1307/mmj/1488510034). The authors' own Integers note does cite it. Cite it and confirm that the cited items are unaffected.
- **m2.** The abstract's claim "the pair of least area sharing two invariants" is proved only among triangle orbifolds (Thm 5.7, p. 40). It holds in all of Sig by a short argument:
  - the only non-triangle signature of area below π/2 is (0;2,2,2,3), and (0;2,2,2,4) has area exactly π/2;
  - neither shares c_2 with a triangle orbifold of the same area: Ψ_1 = 43/6 against 103/6, 79/6, 67/6, 61/6; and 33/4 against 45/4, 49/4, …

  Add this argument, or qualify the claim.
- **m3.** Whether K_mult(O(p,q,r); Sig) ≤ 3 is left open (p. 37). Attempt it with Section 3 (Thm 3.15 restricts the possible shapes), or flag it in the abstract and in Section 7.
- **m4.** On p. 32, "first differ at the third order in t" should read: at order t, in the third coefficient.
- **m5.** The (0;3,3,3,3) family members are called pairwise non-isometric on numerical evidence only (p. 33; S6). Prove it, for example from an exact formula for 4b(ϑ), or weaken the claim.
- **m6.** On p. 7, "(we could not consult Steinig's paper)": do not cite a paper you have not read. Attribute through Laurens [28] instead.
- **m7.** The Figure 3 caption (p. 31) says the open question lies between the solid and dashed curves. The diamonds already lie above the dashed curve, so the open region is between the diamonds and the solid curve.
- **m8.** Figure 1 (p. 2): the "darkest tips" are not visible at print size, as the authors concede. Replace the panels with radial profiles of 4πt𝔥_t against distance, with the flat cone for comparison.
- **m9.** Several attributions (A.685, Identity 9, the Letac/Gloden pieces) go through Chen's 2025 arXiv survey. Cite the original sources where they exist.
- **m10.** In Remark B.4 (p. 50), index the times in increasing order (t_1 = t_3/4, t_2 = t_3/2) to match Lemma B.3.
- **m11.** Add one sentence on why non-orientable orbifolds (mirrors, corner reflectors) are excluded.
- **m12.** The Integers note carries the header "#A1 INTEGERS 26 (2026)", but ref. [35] cites it as a preprint. Clarify its status.

## 7. Presentation

- **P1.** Section 1 (pp. 3–8) is hard to read. Paragraphs such as "What is elementary and what is not" (p. 5) and "What the two papers share is stated exactly" (p. 6) chain five or six clauses with cross-references. Split them, and isolate the overlap bookkeeping.
- **P2.** Symbols collide. Rename:
  - T: tanh series (p. 21), T(L) (p. 29), cylinder length (p. 19), triangle (S4);
  - C: 2 sin(ϑ/2) (p. 15), and constants in Thms 3.11 and 3.18;
  - a: a node versus a_l (p. 25 needs a disclaimer);
  - ν: a measure (p. 24) and a multiplicity difference (p. 25);
  - κ: Thms 3.4 and 3.7, and the curvature on p. 17;
  - σ: the signature and σ_i (p. 11);
  - S: an order sum and a number of sign changes;
  - M: a bound on orders and a matrix.
- **P3.** The index offsets c_j ↔ t^{j−2} ↔ b_{j−2} ↔ Ψ_{j−1} ↔ P_{2j−3} are the main source of reader error. Add them as one row of Table 1 (p. 9).
- **P4.** The mathematics in the abstract renders bold (pp. 1–2), probably a template artefact.
- **P5.** Each introductory theorem should name its body counterpart where it is stated, not only on p. 8.
- **P6.** The Figure 5(b) caption (p. 37) should explain the shading and the circles.
- **P7.** Figure 6 (p. 38) is decorative. Drop it or give it content.

## 8. Overlap with the related manuscripts

**O1. The AGAG companion on finitely many eigenvalues.** The overlap is accurately disclosed (p. 6; companion Table 1).
- **Shared proofs.** The companion's Appendix A reproves the following from this paper: the trace formula with Lemma B.1; Lemmas 2.4, 2.5, 2.7, 2.9, 2.11, 3.6; Prop. B.2; and Thm 3.11(i) with Cor. 3.8.
- **Verbatim text.** About 4.6% of the companion's text, measured by 12-word shingles, appears verbatim here. The longest shared runs are the proofs of Lemmas B.1 and 2.4, the declarations and the references.
- **Shared data, distinct figures.** Both papers use the same computed spectra of O(2,8,8), O(3,3,12) and the (0;3,3,3,3) family.
- **Consistency.** Cross-checked numbers agree: systole 2.2567 vs 2.256767; 2002 eigenvalues below 1.6 × 10⁴; [3, Lemma 4.5] and [3, §7.1] exist.

This is acceptable recycling for self-containment, not duplicate publication; the main results are disjoint. Assign at least one common referee to both, and describe the computations in full in one paper only (see M4).

**O2. The Integers note.**
- Thm 5.8 appears in both papers. Here it is proved by hand; the note proves it by machine as a corollary of its torsion classification and cites this paper.
- The enumeration up to S = 4800 is literally the same computation.
- The values quoted here from the note are consistent with it: (3 log 2/(2π²) + o(1)) X log X, X(log X)², and classes of every size.
- One paper should state Thm 5.8 as a theorem and the other should cite it. I recommend keeping the hand proof here, because it is about orbifolds.

**O3.** I found no other overlap.

## 9. Editorial decision and recommendation

- **Decision: send to review, not desk-reject.** The paper is in scope and technically careful; every claim I tested verified. It has new results, some geometric (Prop. 2.15) and some elegant (Thm 3.3, Thm 3.11(ii)–(iv), Thm 5.8). Its weaknesses are significance and framing, which specialist referees should judge.
- **Referees.**
  - A spectral geometer working on orbifolds or cone singularities, for Sections 2 and 4 and Prop. 2.13.
  - A PTE / number-theory expert, for Sections 3.4 and 5.
  - Coordinate with the companion submission.
- **Recommendation: major revision.**
  - About 75% confidence that the main results are correct as stated.
  - About 70% confidence in the recommendation.
  - Rejection on significance would be defensible if the revision cannot make the geometric case (M1).

## 10. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Retitle or restate the object as counts of coefficients. Add a section on geometric meaning. Promote Prop. 2.15. Justify Sections 3.3–3.4 for AGAG. |
| M2 | Recast 10⁻¹¹ and 10⁻¹⁹ as method-dependent upper bounds and quote the δ_cert value (t ≈ 5 × 10⁻⁷). Fix "at any fixed t". Put the curvature caveat in the abstract. |
| M3 | Complete the proof of Prop. 2.13, especially uniformity as ϑ → 0, or relabel it a conjecture. Reformulate Prop. 2.15(i) and drop the unproved meta-claims. |
| M4 | Justify or relocate Section 6, App. C, S3, S5 and the numerics of Section 4, S4, S6. |
| m1 | Cite the DGGW erratum and confirm the cited items are unaffected. |
| m2 | Add the least-area argument over all of Sig, or qualify the claim. |
| m3 | Settle K_mult(O(p,q,r); Sig) ≤ 3, or flag it as open. |
| m4–m12, P1–P7 | Edits as listed above. |
| O1–O2 | Describe the computations in one paper only. Make Thm 5.8 a theorem in one paper and a citation in the other. Clarify the note's status. Use a common referee for the two AGAG papers. |

---

Supporting material is in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/A-a-editor-orbifold-isospectrality/scratch/`:
- `code/check1.py` to `code/check7.py`: the verification scripts;
- `dl/lmfdb.json`: the LMFDB record for 90.c3;
- `img/`: the rendered pages.
