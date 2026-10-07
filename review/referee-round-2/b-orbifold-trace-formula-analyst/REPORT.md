<!-- Provenance: reviewer (b) could not write files; this is its returned report text, saved verbatim by the orchestrating session (preamble line about the failed write removed). -->

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (submitted to The Journal of Geometric Analysis)

Reviewer profile: analyst working on the Selberg trace formula for cofinite Fuchsian groups with torsion and on heat kernels and small-time asymptotics on hyperbolic orbisurfaces.

I did not count the marked placeholders (author contributions, AI-use statement, Zenodo DOI) as defects. I rendered every page I comment on below and looked at it as an image (pp. 2, 7, 8, 9, 13, 16, 18, 20, 23, 28, 30, 31, with zoomed renders of Figs. 1, 3 and 5).

## 1. Summary

The paper studies closed orientable hyperbolic 2-orbifolds with cone points and asks how many heat invariants c_1, c_2, ... it takes to recover the signature (genus and multiset of cone orders).

**Analytic input.**
- The Selberg trace formula is applied to the heat function (Thm 2.3, extended from the C_c^∞ class in Appendix A).
- It yields a closed-form expansion to all orders in small time. Each cone point of order m contributes b_l(m) = (−1)^l p_l(m)/m. Here p_l is an explicit even polynomial of degree 2l+2 with p_l(1) = 0, built from the closed form Φ_m(u) = (cot u − m cot mu)/(4m sin u) of the elliptic sum (Lemma 2.6, Prop. 2.7, Lemma 2.8).
- So the j-th invariant adds exactly one new odd power sum P_{2j−3} of the orders, besides the reciprocal sum R (Lemma 2.10).

**Comparing two signatures.** This becomes a symmetric (odd-power) Prouhet–Tarry–Escott (PTE) moment problem for a signed multiset. The results are:
- **Hearing the signature.**
  - ⌊Area/π⌋+4 invariants always determine the signature (Thm 3.4, Cor. 3.5).
  - No number independent of the area does (Thm 3.10).
  - The worst-case count f(A) lies between roughly √(A/6π) and A/π+4. Its polynomial growth exponent is tied, in both directions, to that of the PTE function N(k) (Thm 3.11).
- **Spheres with n cone points.**
  - n invariants suffice, by a Newton-identity argument with R replacing the top odd power sum (Thm A).
  - An explicit linear system has determinant ±∏(m_i+m_j)/e_n (Thm B).
  - n−1 invariants fail generically over the reals, and on explicit integer examples for n = 3, 4 (Thm C).
- **Triangle orbifolds.**
  - c_1, c_2 determine O(p,q,r) for p+q+r ≤ 17 and first fail at (2,8,8)/(3,3,12) (Thms 5.4–5.7, by elementary but careful interval analysis of "strata").
  - c_3 always suffices.
  - The minimal collision stays isolated under every scaling because the cubic C_{27/2} has rank 0 (Thm 5.10).
  - Exactly 38 sums in [18, 4800] are collision-free (computational).
- **What heat does not hear.**
  - Heat invariants are functions of the signature, so even infinitely many cannot fix the moduli.
  - The difference of heat traces within one signature is bounded with explicit constants (Thm 4.4), and its leading term t^{−1/2} e^{−L*²/4t} is identified (Thm 4.5).
- **Stability.**
  - Recovering the orders from perturbed c_1..c_n (known n, genus 0) is Lipschitz at simple orders and Hölder with exponent 1/k at k-fold orders, with explicit constants.
  - The constants are sharp in the senses stated (Section 6).
- **Numerics.** Finite-element spectra (Section 7 and supplement) illustrate the theory; none of it is used in a proof.

## 2. Significance and novelty

**What is good.**
- The paper is unusually careful and honest. It separates proved, computed and open statements, it states its limits of scope (Thm 1.3, Remark 6.1), and it labels computational results as such (Prop. 5.9).
- The closed form of the elliptic contribution to every order (Lemma 2.6 / Prop. 2.7) is clean. I find it more usable than the lune-coefficient route of Watson and Uçar.
- The observation that each new coefficient adds exactly one odd power sum is the key to everything that follows, and it is used well.
- Several results are, to my knowledge, new:
  - the uniform explicit count ⌊Area/π⌋+4;
  - the reduction of the growth question to N(k);
  - the exact first failure of two invariants on triangle orbifolds;
  - its isolation by a rank-0 curve.
- These answer precisely the remark of Dryden–Gordon–Greenwald–Webb that the invariant c "does not seem sufficiently strong" for hyperbolic triangular pillows.

**Where the novelty is limited.**
- The analytic part (Sections 2 and 4) is, by the authors' own account, classical in substance:
  - Thm 2.3 is the trace formula.
  - Prop. 2.7 re-derives coefficients Uçar already computed.
  - Prop. 4.1 and Cor. 4.3 are folklore.
  - Thm 4.5 is the standard leading-term argument.
- The genuinely new mathematics is mostly algebraic and arithmetic: power sums, PTE, Descartes' rule, 2-descent.
- The growth theorem (Thm 3.11) moves an open problem rather than solving it, as the paper says.
- For a geometric-analysis journal, the geometric-analytic contribution proper is therefore modest. The paper's value is in the inverse-spectral counting question and its sharp answers in the rigid case.
- It is a solid, correct and interesting contribution. Whether its centre of gravity suits JGA is for the editor (Major 2).

## 3. Correctness

### 3.1 What I recomputed, how, and the results

The scripts are listed at the top; unless stated otherwise they use sympy/mpmath with exact rationals.

1. **Trace-formula normalisation (Thm 2.3), checked against the cited sources.**
   - Dryden–Strohmaier (arXiv math/0504571v2), eq. (1): the identity term, the hyperbolic weight ln N(P_c)/(N^{1/2} − N^{−1/2}) = ℓ(γ_0)/(2 sinh(ℓ/2)), and the elliptic term (2m sin θ)^{−1} ∫ e^{−2θr} h/(1+e^{−2πr}) with θ = πl/m all match Thm 2.3. DS do not fix the Fourier convention.
   - Garbin–Jorgenson (arXiv 1603.01495v1, Remark 2.7, eq. (2.8)) state the heat-kernel version directly. Their identity, hyperbolic and elliptic terms coincide with the paper's I, Hyp and E_m.
   - Independent check: E_m(0+) = Σ_j (4m sin²θ_j)^{−1} = (m²−1)/(12m), which is the classical t⁰ cone term. The identity term gives Area/(4πt) at leading order.
2. **Lemma 2.6 and formula (4).** The closed form matches the elliptic sum numerically, and its Taylor coefficients equal (4) exactly, for m = 2, 3, 5, 12 and k ≤ 4.
3. **Cone polynomials.**
   - From (4)–(5) I get p_0, p_1, p_2 exactly as in (7).
   - I also get p_3 = m⁸/10080 + m⁶/3780 + m⁴/2160 + m²/945 − 19/10080.
   - p_l(1) = 0 and the leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)) hold for l ≤ 3.
4. **α_k.**
   - The Bernoulli-polynomial formula gives 1, −1/3, 1/15, −4/315, 1/315, −4/3465, 382/675675.
   - I recomputed these independently by expanding I(t) through the moments M_k = ∫_0^∞ r^{2k+1}/(e^{2πr}+1) dr, which I also checked by quadrature. The two agree through k = 6.
5. **All-order expansion against the actual integrals.**
   - I computed E_m(t) by 30-digit quadrature for m = 2, 3, 8, 12 at t = 0.01 and 0.05.
   - Every residual against Σ_{l≤4} b_l t^l has the size and sign of the first omitted term. For example, at m = 2, t = 0.01 the residual is −5.79e−12 against b_5 t⁵ = −5.91e−12.
   - For m = 12 at t = 0.05 the series visibly diverges, as stated.
   - The identity term matches Σ α_k t^{k−1}/(4π) to 1e−15 at t = 0.01.
6. **Formula (9) and the minimal pair.**
   - c_1, c_2, c_3 for a triad equal (9) symbolically.
   - For (2,8,8) against (3,3,12): c_2 = 67/48, d_3 = 25/12, d_4 = −1775/24, d_5 = 153025/48, all as in the text.
7. **Front end (Prop. 6.2).**
   - The diagonal of F for n = 5 is −1/2, 1/12, −1/360, 1/2520, −1/10080.
   - The P_3 row of F⁻¹ is (−18, −120, −360).
   - The amplification factors are 2, 14, 498, 4062, 56230/3.
   - All as stated.
8. **Theorem B.** For random integer orders with n = 2..5, det M = (−1)^{n(n+1)/2} ∏_{i<j}(m_i+m_j)/e_n exactly, and M⁻¹b is the true e.
9. **Theorem C(3), Examples 3.6 and 3.12, Table S1.**
   - (R, P_1, P_3, P_5) of both n = 4 witnesses check out.
   - The exact number of shared invariants and the areas are correct for all of these pairs: (1;15)/(0;3,3,5,5); (2,8,8)/(3,3,12); the n = 4 witness; (1;15,15,15)/(0;3,3,5,7,7,21); the 7-vs-8 cone pair; (0;5,5,5)/(0;2,2,2,10); the Prouhet L = 2 pair; the cone-count pairs with L = 4, 5.
10. **Remark 3.2 (partial check).**
    - An exhaustive C enumeration of 4-multisets with orders ≤ 130 and equal exact (R, P_1, P_3) gives 16 primitive witnesses.
    - These include the pencil-free pairs (16,16,74,74; 11,37,44,88) and (11,21,99,99; 9,51,51,119), as in Section S1.
    - I did not rerun the 220/440 bounds or the n = 5 search.
11. **Section 6 constants.**
    - ζ_3 = 1, ζ_4 = 79/3 and ζ_5 = 14048/15 are correct.
    - I recomputed the exact cond, r_n, Ξ_μ, Π̂_a and δ_thm for all eleven multisets in Table 1. I obtain 3.803e−7, 1.189e−7, 4.021e−11, 3.147e−11, 4.492e−7, 9.354e−7, 9.973e−8, 1.487e−9, 4.744e−10, 2.031e−9 and 2.730e−12. Rounded down, these match Table 1.
    - The largest cond is 3.5109, matching "at most 3.511".
    - I did not recompute δ_cert or δ_up.
12. **Prop. 6.6(i) and Remark 6.7.** δR = s²/(4(64−s²)) and δP_3 = 48s² for (2,8,8). The constant 498 + 42a² follows from amp_1 = 14 and amp_2 = 498.
13. **Section 5, strata.**
    - There are 83 hyperbolic triads with 10 ≤ S ≤ 18 and none with S < 10. The only coincidence of R within one sum is (2,8,8)/(3,3,12).
    - For p = 2..14 the first overlap S*(p) and first collision reproduce Table S2 exactly.
    - Symbolically I checked: the closed form of φ_p − τ_p; the identity gap_p = φ_p − τ_p for S−p even; gap_p(3p+7) = −2(p²−5p−30)/(p(p+1)(p+3)(p+4)(p+5)); and the numerator of φ_p′.
    - The first non-adjacent collision (5,15,15)/(7,7,21) is correct.
14. **Proposition 5.9.** An independent exhaustive C search over all hyperbolic triads with 18 ≤ S ≤ 4800 (exact reduced fractions, sorted per sum) returns exactly the 38 listed sums. S = 557 has 25 575 triads.
15. **Theorem 5.10.**
    - ψ maps E into C_{27/2}, and φ∘ψ is the identity.
    - Δ = 2^18 3^8 5^6.
    - The listed points lie on E. The tangent at (16,400) meets E as (x−16)³, so that point is a flex. #E(F_7) = #E(F_11) = 12.
    - The twelve listed points lie on C_{27/2}, and φ(1:4:4) = (−24, 360).
    - I brute-forced the local obstructions in the descent:
      - on E, the quartics for d_1 ∈ {±2, ±3} are never 0 or a square mod 5;
      - on E′, for d_1 ∈ {3, 5, 15} they are never a 3-adic square, with all cases mod 3⁵ decided;
      - on E′, for d_1 < 0 all coefficients are negative.
    - So the descent gives rank 0. PARI was not available, so this check is my own.
16. **References.** arXiv 2609.05061, 2506.11429, math/0411290 and 1103.4372 exist with the stated titles. Crossref confirms the Schueth, Garbin–Jorgenson, Coppersmith et al. and Wooley entries.

**Nothing I recomputed disagrees with the manuscript.**

### 3.2 Proofs the main results depend on, and whether each is complete where it appears

| Result used | Where | Status |
|---|---|---|
| Thm 2.3 (trace formula for the heat function) | §2.1 + App. A | **Complete.** It cites DS eq. (1), which DS quote from Hejhal and Iwaniec, and Garbin–Jorgenson Rem. 2.7/(2.8), which states the heat case directly (I checked GJ). Lemma A.1 is also a correct self-contained approximation argument; I checked every step: a Weyl-type bound N(λ) = O(λ) using h_T with support ≤ 2ε < ℓ; dominated convergence via Lemma 2.4; the bound \|f̂_ϱ\| ≤ ε_ϱ min(1, \|r\|^{−3}); and the imaginary r_j. It is terse (Minor 1) but has no gap. |
| Lemma 2.4 (geodesic count) | §2.1 | Complete. |
| Lemma 2.5 (hyperbolic term) | §2.1 | Complete. I re-derived both integrations by parts, the constant (2+3ℓ)/(2+ℓ), and the logarithmic derivative in ℓ. |
| Lemma 2.6, Prop. 2.7, Lemma 2.8 (elliptic and identity terms to all orders) | §2.2 | Complete. The beta integral, the domination that justifies differentiating under the integral, the alternating Taylor remainder with F_a ≥ 0, and the Liouville argument are all there. Confirmed numerically (item 5). |
| Lemma 2.10, Lemma 3.1, Thms A, B, C | §§2.3, 3.1 | Complete. |
| Lemma 3.3, Thm 3.4, Cor. 3.5 | §3.2 | Complete. The padding bookkeeping, the parity of T, \|U\|+\|V\| = 2 max(n+g−g′, n′+g′−g), and n + 4g ≤ Area/π + 4 all check. |
| Thm 3.8 (Descartes bound) | §3.3 | Complete. |
| Prop. 3.9, Thm 3.10, Thm 3.11(a)–(e), Lemma B.1, Prop. B.2 | §3.3 + App. B | Complete. The pigeonhole count, the doubling identity, hyperbolicity for n = 2, the choice of L in (c), monotonicity of N in (d), the shift construction in (e), N(2L−3) ≤ 2L², and the small-A fallbacks all check. |
| Props. 4.1, 4.2, Cor. 4.3 | §4 | Complete (rigidity via Troyanov). |
| Thms 4.4, 4.5, Cor. 4.6 | §4 | Complete. |
| Thms 5.1–5.7, Prop. 5.8 | §5.1 | Complete. All constants in the proof of Thm 5.4 match my computation. |
| Prop. 5.9 | §5.1 | Computational and labelled as such. Reproduced independently. |
| Thm 5.10 | §5.2 | Complete; reproduced. |
| Thms 6.4, 6.5, 6.8, Prop. 6.6, Rem. 6.7 | §6 | Complete. The Rouché constants and the majorant \|T̃_k − T_k\| ≤ η t_k(n) check. |
| Prop. S3.1 (δ_cert) | Supplement | A proof is given. It feeds only the δ_cert column, not a theorem. I did not rerun it. |

## 4. MAJOR issues

Neither issue is a correctness defect. Both can be fixed by rewriting rather than by new mathematics.

1. **Theorem 4.4 is presented as an "explicit" quantitative locality bound, but its constant depends on the diameter, which no spectral or topological datum controls** (Lemma 2.5, Thm 4.4; also §1.1).
   - **Why it matters.** The factor e^{3 diam} comes from the crude Dirichlet-domain count in Lemma 2.4. The admissible range t ≤ ℓ²/(2(1+ℓ)) is tiny for short systoles. The authors themselves call the constant "qualitative" and the bound "loose".
   - **Why the sharp parts are not new.** The only sharp content, the exponent ℓ²/4 and the factor t^{−1/2}, is the classical leading term of the hyperbolic sum (Huber, McKean; for orbisurfaces Dryden [9]).
   - **Resolution.** Either (a) replace diam by an explicit function of (Area, ℓ), for instance via a thick–thin argument plus Buser-type counting; or (b) tone the claim down in §1.1 and Section 4 to "an elementary explicit bound and the sharp leading term".

2. **Scope, length and focus for JGA** (37 pp. plus a 12-pp. supplement).
   - **The problem.** The paper bundles four largely independent pieces:
     - the PTE growth theory;
     - the arithmetic of triangle collisions, including a 2-descent;
     - the conditioning analysis;
     - finite-element numerics.
   - The geometric-analysis core is short and mostly classical.
   - **Resolution.** Tighten:
     - move §7 to the supplement, since nothing in it is used;
     - cut §6 down to Thm 6.5 and Prop. 6.6;
     - consider moving Thm 5.10 to the companion manuscript [24].
   - Alternatively the editor may judge the fit acceptable as it stands. I do not consider this disqualifying.

## 5. MINOR issues

1. **Thm 2.3 and App. A, sourcing.**
   - DS eq. (1) is itself only quoted, with no Fourier convention fixed.
   - Cite the precise theorem in Hejhal Vol. I [28] or Iwaniec Thm 10.2 [35]. Their admissible classes already contain h_t, which would make Lemma A.1 unnecessary. Alternatively, rely explicitly on GJ (2.8).
   - If Lemma A.1 is kept, add one line each on:
     - why the trace formula applies to h_T (g = 2cos(Tu)(ψ*ψ) is smooth, even and compactly supported);
     - eigenvalues being counted with multiplicity;
     - the step from #{|r_j − T| ≤ 1} = O(T+1) to Σ_j min(1, |r_j|^{−3}) < ∞.
2. **Proof of Thm 2.3:** "elliptic classes ρ^j" — ρ is never defined.
3. **Notation clashes.**
   - h_t is the test function in §2, while Fig. 1 uses fraktur 𝔥_t for the heat kernel.
   - O(t^N) uses N, which is also the PTE function N(k).
   - In Lemma 2.4, x denotes both the base point and the length bound.
   - Lemma 2.5 writes C(Area, ℓ, diam) but (3) writes C(A, ℓ, diam).
4. **Prop. 2.7** says "for every integer m ≥ 1", but §6, Thm 1.1(iii) and Thm C(2) evaluate b_l at real m. State once that b_l extends to real m through the polynomial p_l.
5. **Remark 2.9:** "Putting u = it/2 in Lemma 2.6 gives mΦ_m^{(2k)}(0) = …" is not a substitution that yields this identity. Rephrase as a comparison of Taylor coefficients.
6. **Lemma 2.5:** the first inequality needs only t < ℓ; the stated range t ≤ ℓ²/(2(1+ℓ)) is needed only for the monotonicity claim. Saying so slightly enlarges the domain of Thm 4.4(b).
7. **Thm 4.5(ii):** say that L* is attained because the supports of w_1, w_2 are discrete (Lemma 2.4).
8. **Thm 1.3:** δ_thm is 4–6 orders of magnitude below δ_cert. Say in the theorem's own discussion, not only after Thm 6.8, that the closed-form threshold is far from sharp.
9. **Thm 3.11(c):** note that the fallback "f(A) ≥ 3 via O(2,8,8)" needs A ≥ π/2. This is implied by A ≥ 8π, but readers will check it.
10. **§3.3, before Thm 3.8:** after "sharing exactly L iff Σ z^{2L−1} ≠ 0", add the reason: R agrees, so c_{L+1} differs exactly when P_{2L−1} does (Lemma 2.10).
11. **Prop. 5.9 wording:** the proposition says "18 ≤ S ≤ 4800" while the abstract says "between 19 and 4800". Make them consistent.
12. **Supplement abstract:** "No theorem of the paper depends on it" is true, but Table 1's δ_cert column and Remark 6.1 do rely on Prop. S3.1. Say so.
13. **Appendix C** cites repository paths such as `review/audit-2/…` and `review/round1-fixes/…`, which read as process artefacts. Rename them to neutral paths before archiving.

## 6. Presentation (including figures and captions)

The writing is compact and precise, sometimes telegraphic. Thm B, Thm 3.8, Lemma A.1 and Thm 5.10 would each benefit from two or three more sentences. The roadmap and the "limits of scope" paragraphs are helpful.

Figures, checked on rendered pages:

- **Fig. 1 (p. 2).** At 300 dpi it is consistent with the caption. The tips of largest order reach the darkest band; the order-2 and order-3 corners reach about 2 and 3. The drawn angles are not π/2, π/8, …, which "schematic" covers.
- **Fig. 2 (p. 13).** Correct: the discs and rings match X* and −X* in both panels, with the padding 1 included in (b). Panel (b) uses grey/black where (a) uses orange/teal, with no explanation. The lower row of (a) is identified only in the caption.
- **Fig. 3 (p. 16).** The solid bound ⌊2s⌋+4 and the dashed bound ⌊√((s−1)/3)⌋+2 (starting at s = 4) are plotted correctly; I checked s = 4, 13 and about 2000. The squares at s = 255 and 1023 sit below the dashed lower bound. That is legitimate, since they are particular pairs, but deserves a clause in the caption.
- **Fig. 4 (p. 18).** The λ-axis in (b) is non-linear (ticks 0, 1, 5, 10, 20, 40, …), and the caption does not say so.
- **Fig. 5 (p. 20).**
  - The caption says "tilings of the hyperboloid", but the pictures are disc-model tilings of the hyperbolic plane.
  - The boundary circle is drawn as an ellipse, about 510 × 435 px at 250 dpi (aspect ratio about 1.17).
  - Fix the aspect ratio and the wording, or explain the projection. The caption stresses "Exact tilings", so this matters.
- **Fig. 6 (p. 23).** Consistent with Table S2 and Prop. 5.8.
- **Fig. 7 (p. 28).** The slopes are visually consistent with 1, 1/2, 1/3, 1/2.
- **Fig. 8 (p. 30).** (a) is consistent with d_3 t ≈ 0.003 at t = 0.0015 and with the sign change near t ≈ 0.34. (b) shows only the seven pairs with ϑ = 0, while the text speaks of all 28 pairs; say which are drawn.
- **Captions.** Fig. 1's "darkest tip" should say "at the cone point of largest order".

The Table S1 entries I checked are correct.

## 7. Recommendation

**Minor revision.**

Every proof Theorems 1.1–1.3 rest on is present and complete where it appears. That includes the extension of the trace formula to the heat function, the convergence arguments, the elliptic expansion to all orders, and the appendix lemmas. Every quantity I recomputed agrees with the manuscript. The two major points are about framing (Thm 4.4) and the paper's breadth for JGA, not about errors.

Confidence:
- **High** on the analytic parts (my area) and on the triangle/arithmetic parts I recomputed.
- **Moderate** on what I did not rerun: the n = 5 and T_3 searches, δ_cert/δ_up, and the finite-element numerics.
- **Moderate** on journal fit, which I leave to the editor.
