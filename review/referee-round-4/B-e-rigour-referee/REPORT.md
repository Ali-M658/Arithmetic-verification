<!-- Saved verbatim by the main session from the reviewer's returned text: the harness refused the reviewer's own write. Scripts (scratch/code/), fetched sources (scratch/refs/) and page images (scratch/pages/) are in its git-ignored scratch/. -->

# Referee report (rigour and citations)

**Manuscript:** "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (P. Gang, A. Agadi, A. Veluri, J. Wang, J. Barreto, A. Chouthaiwale), 23 pp., submitted to *Annals of Global Analysis and Geometry*.

As instructed, I treat the three marked placeholders (author contributions, AI-use statement, Zenodo DOI; p. 21) as known and do not count them against the paper. I read every proof to the end. Before reporting anything typographical or about a figure, I checked it on rendered page images (110 dpi throughout; Fig. 2 also at 300 dpi). I wrote my own scripts to recompute the constants. I did not access the authors' repository.

---

## Summary

The paper looks at closed orientable hyperbolic 2-orbifolds with cone points only. It shows effectively that in the class C(A, ε, M) (area ≤ A, systole ≥ ε, cone orders ≤ M), the first N eigenvalues, each known to within δ, determine the signature. N and δ are given by explicit formulas (Theorem 1.1 / Theorem 6.2).

The argument runs as follows:
- **Heat trace (§2).** The heat-function trace formula (Thm 2.1, App. A) gives explicit enveloping remainders for the area and cone terms (Props 2.6, 2.7).
- **Heat invariants (§3).** The signature's heat invariants have this structure:
  - integrality of the first difference (Lemma 3.5);
  - separation by the ⌊A/π⌋+4-th invariant (Thm 3.3);
  - separation by the M-th invariant when orders are ≤ M (Thm 3.4).
- **Diameter (§4).** An explicit diameter bound in terms of A, ε and M (Thm 4.4).
- **Counting (§5).** Eigenvalue counting and tail bounds.
- **A-posteriori certificate (Thm 1.2 / 7.1).** This is applied to computed spectra of O(2,8,8), O(3,3,12) and a family O_ϑ of signature (0;3,3,3,3).
- **Necessity of the order bound (§8.1).** The family O(2,3,m) shows the bound on orders cannot be dropped (Thm 1.3, Props 8.2–8.3, Remark 8.4). Along the way the paper gives a self-contained proof of the hyperbolic case of Jørgensen's inequality (Lemma 8.1).
- **The systole bound (§8.2).** Whether it is needed is left open (Problem 1).

## Significance

The qualitative statement follows from Dryden–Strohmaier plus compactness, as the authors say on p. 2. The contribution is effectivity and the a-posteriori certificate, together with the clean negative result on unbounded orders.

The a-priori constants are astronomically large (N up to 3.8×10^30, δ down to 10^-278 in Table 2), so Theorem 1.1 is of conceptual rather than practical value. The authors say this plainly, which I appreciate. The parts I find genuinely nice are:
- the Vandermonde argument giving the M-th invariant (Thm 3.4);
- the parity / odd-power-sum argument (Thm 3.3);
- the fully enveloped (signed) remainders for the cone and area expansions (Props 2.6, 2.7);
- the cusp-like behaviour of O(2,3,m) (Prop 8.3 / Remark 8.4).

The paper is carefully written, unusually self-contained, and its proofs are complete to a degree I rarely see. For AGAG the topic is appropriate. The novelty is moderate.

## Correctness, and what was recomputed or checked

I checked every proof line by line. **I found no mathematical error in any theorem, proposition or lemma.** The problems I found concern:
- the status of the computational claims of §7;
- one misstatement of results in the abstract and introduction;
- one cited secondary description I could not confirm;
- presentation.

Details below.

### Proofs verified by hand (all correct as written)

**§2.**
- **Lemma 2.2:** the triangle-inequality step and the packing count.
- **Lemma 2.3:**
  - the integration by parts;
  - the bound x/(x−t) ≤ ℓ/(ℓ−t);
  - the logarithmic derivative in ℓ, whose bracket is nonnegative iff t ≤ ℓ²/(2(1+ℓ));
  - the second bound via the factorisation x e^{-x/2-x²/4t} = (x e^{-x²/8t})(e^{3x/2-x²/8t})e^{-2x}, with maxima at 2√t and 6t. Keeping e^{-t/4} gives exactly e^{17t/4-1/2-ℓ}.
- **Lemma 2.4:**
  - the cot identity;
  - the Bernoulli expansion of cot u − m cot mu;
  - the coefficient formula (2);
  - Φ_m(π/2m) ≤ m/4.
- **Lemma 2.5:** the Euler beta integral and the domination for differentiation.
- **Props 2.6 and 2.7:**
  - the decomposition of E_m − Σ b_l t^l and of (4π/Area) I − Σ α_k t^{k−1};
  - the sign of every term;
  - that the moduli sum exactly to |b_K| t^K and |α_{K+1}| t^K.
- **Lemma 2.8:** the leading coefficient.

**§3.**
- **Lemma 3.1:**
  - the triangular system via p_l(x)/x = Σ a_{l,k} ψ_k(x), using p_l even with p_l(1) = 0;
  - the padding identities;
  - |U|+|V| = n+n′+|d| = 2 max(n+g−g′, n′+g′−g).
- **Theorem 3.3:**
  - κ even;
  - e_j(X) = 0 for odd j ≤ κ−3;
  - e_{κ−1} = e_κ Σx^{-1} = 0, so X = −X.
- **Theorem 3.4:** the Vandermonde reduction.
- **Lemma 3.5:** both parts.

**§4.**
- **(H1)–(H3):** including the hyperboloid normals n_1, n_3 and ⟨n_1, n_3⟩ = −X.
- **Lemma 4.2:**
  - the defect ≥ π/(abc);
  - cos((θ−α−β)/2) ≥ sin(π/2M) ≥ 1/M;
  - hence cosh d − 1 ≥ 2/(π²cM).
- **Lemma 4.3.**
- **Theorem 4.4**, including the closed form. arccosh(1+x) ≥ √(2x/(1+x)) gives 2/(πM·1.025) ≥ 0.6/M for M ≥ 2.

**§5–6.**
- **Lemma 5.1(i):** the case analysis; the minimum s = 1/42 gives Area ≥ π/21.
- **Prop 5.2.**
- **Lemma 6.1.**
- **Theorem 6.2:**
  - B ≤ ϖ e^{3D} t^{-1/2} e^{-ε²/4t}, with 63 = 3·21 from Area ≥ π/21;
  - B_* is monotone on (0, t_2];
  - the reduction to e^{-y}y^p ≤ (γ_*/16ϖe^{3D})(ε²/4)^p and the formula for y_0;
  - Λt_* ≥ 1;
  - the tail bound equals Γ_*/8 exactly;
  - Γ_*/8 + Γ_*/8 + Γ_*/(8e) < 3Γ_*/8.

**§7.** Theorem 7.1 (the inequality itself).

**§8.**
- **Lemma 8.1:**
  - the recursion x_{n+1} = −x_n(1+x_n)(u−u^{-1})²;
  - the non-vanishing argument;
  - the fixed-point normalisation C_n → A.
- **Trace identities after Lemma 8.1.**
- **Prop 8.2:**
  - the side lengths: cosh d(v_2,v_3) = 2cos(π/m)/√3 and cosh d(v_2,v_m) = 1/(2 sin(π/m));
  - d(x, v_3) ≤ 2s_m;
  - the application of Lemma 8.1.
- **Formula (5):** both values of q.
- **Prop 8.3 and Remark 8.4:** the pigeonhole count.
- **Prop 8.5:** ∫_{−a}^{a} ρ² cosh ρ dρ = 2[(a²+2) sinh a − 2a cosh a] gives the stated λ_1 bound.

**Appendix A.** Lemma A.1, including the O(T+1) local count and the dominated-convergence steps.

### Recomputed exactly or in high precision (scripts in `scratch/code/`; sympy rationals, mpmath at 50 digits)

| Item | Result |
|---|---|
| α_0..α_3 = 1, −1/3, 1/15, −4/315; μ_0 = 1/12 | reproduced |
| b_0(m) = (m²−1)/(12m) | reproduced, m = 2..7 |
| Lemma 2.4 closed form and series (2) vs. the defining sum Φ_m(u) | agreement to 10^-25 or better (m = 2, 3, 7, 12) |
| φ_k(m) ≤ (m/4)(2m/π)^{2k} | holds, k < 10, m ≤ 14 |
| Lemma 2.8: p_l even, degree 2l+2, p_l(1) = 0, leading coefficient a_l | verified exactly, l ≤ 6 |
| Props 2.6 / 2.7: sign and modulus of the remainder vs. numerical quadrature of E_m(t) and I(t) | all correct, K = 0..4, m ∈ {2, 5}, t ∈ {0.05, 0.1, 0.5, 1, 2} |
| Lemma 3.5 example: (0;4,4,4) vs (0;3,4,6) | d_2 = −1/12 ✓ |
| Fig. 1 text: (0;2,8,8) vs (0;3,3,12) | c_2 equal, d_3 = 25/12 ✓ |
| Table 1 (all 12 entries) | reproduced from D = 4r_0A/v_0 |
| Table 2 (all 8 rows, all columns: k_*, D, t_1, t_3, N, δ, binding constraint) | reproduced, with one rounding exception (m8) |
| p. 13: "N from about 4×10^18 to 1.1×10^7" | 4.19×10^18 with k_* = 14 ✓ |
| Table 3, last column | N(4π/3, ε, 3) = 4.32×10^4 at ε = 2.634, 2.41×10^5 at 0.846, 3.69×10^5 at 0.694; N(·, 12) = 7.44×10^12 for every ε (t_1 binds), which explains the single entry ✓ |
| Ratio claim "10^2 to 10^11" (p. 15, Fig. 2 caption) | consistent (≈ 3.5×10^2 to 2×10^11) |
| \|S\| in Table 3 | enumerated: area π/2, M = 12 gives the 6 signatures {(2,6,12), (2,8,8), (3,3,12), (3,4,6), (4,4,4), (2,2,2,4)}; area 4π/3 gives 3 (M = 3) and 10 (M = 12) ✓ |
| σ_* (Prop 8.2) | 0.5620668711… ✓ (statement's 0.56206… correct) |
| Fig. 1 grey curves (direct quadrature of G_{σ0} − G_σ) | at t = 0.001: 0.75, 0.50, 0.42, 0.16 and 0.0020 (darkest); at t = 0.05 the nearest gap is 0.039; consistent with the plot |
| Systoles behind the class parameters (enumeration of words in triangle groups, not a proof) | ℓ(O(3,3,12)) = 1.86260, the 1.8626 of Tables 2/3; ℓ(O(2,8,8)) = 2.25677; control ℓ(O(2,3,7)) = 0.98399 (known value). For the most symmetric O_ϑ (regular quadrilateral, angles π/3, cosh side = 3), the product of the two order-3 rotations at adjacent vertices has cosh(ℓ/2) = 2, i.e. ℓ = 2.634, the paper's value for ϑ = 0 |
| Diameter claims, Table 1 caption | twice the longest side: 4.896 for O(2,8,8) (side cosh⁻¹ cot²(π/8)), 4.31 for O(3,3,12); consistent with "below 4.9 and 4.4". I did not check 7.8 for O_ϑ |

### Citations checked

| Ref. | How checked | Result |
|---|---|---|
| [1] Dryden–Strohmaier, CMB 52 (2009) | Crossref; full text of arXiv:math/0504571v2 | eq. (1) is the trace formula for h entire of uniform exponential type. The hyperbolic term ln N(P_c)/(N(P)^{1/2}−N(P)^{-1/2}) g matches ℓ(γ_0)g(ℓ)/(2 sinh(ℓ/2)). The elliptic term (2m sin θ)^{-1}∫e^{-2θr}h/(1+e^{-2πr}) with θ = πl/m matches E_m exactly. Thm 1.1 (orders), Thm 3.2 (Gauss–Bonnet) and Prop 3.3 (same underlying space) say what they are cited for. **Correct.** |
| [2] Linowitz–Voight, Math. Z. 281 | Crossref; arXiv:1408.2001 | Thm A: minimal-area isospectral non-isometric pairs. The text after Thm A notes all three pairs have signature (0;2,2,2,2,2,3,4), so they share a signature. **Correct** (the "same signature" is in the sentence after Thm A). |
| [3] Mumford, PAMS 28 | Crossref | Metadata correct. Full text not obtainable (AMS and Harvard DASH refused headless access), so **"Cor. 3" not verified at statement level**. |
| [4] Bers, Israel J. Math. 12 | Crossref | Metadata correct; content not verified (paywalled). |
| [5] Donnelly, Math. Ann. 224 | Crossref | Metadata correct. The role as source of local heat invariants is confirmed indirectly by DGGW Remark 4.10 and Uçar's proof of Thm 4.20. |
| [6] DGGW, Michigan Math. J. 56 | Crossref; arXiv:0805.3148 | Thm 4.8 (local expansion) ✓. Ex. 5.6 gives the cone contribution (m²−1)/(12m) = b_0 ✓ and the degree-one term. **Correct.** |
| [7] Uçar, thesis HU Berlin 2017 | DataCite; full PDF from edoc | Thm 4.20 and (4.35) exist (pp. 137–138). From (4.35) at κ = −1 I get a_1 = −A/3 and a_2 = A/15, i.e. α_1 = −1/3 and α_2 = 1/15 after normalisation. **Correct.** |
| [8] Stanhope, AGAG 27(4) | Crossref; Semantic Scholar abstract; arXiv | Bounds isotropy types of isospectral orbifolds. **Correct.** |
| [9] Chang–DeTurck, PAMS 105 | DOI 10.2307/2047071 resolves (via JSTOR) to 10.1090/S0002-9939-1989-0953738-7; original text blocked | Grieser–Maronna (arXiv:1208.3163) describe it as the paper does (N depending on a lower angle bound ε). Another secondary source (arXiv:1911.06758) describes it as N(T) depending on the triangle. **Not verified at source**; see m14. |
| [10] Thurston notes, Ch. 13 | full chapter from library.slmath.org | 13.3.4 is χ(O) = χ(X_O) − Σ(1−1/m_i) (with mirror terms), 13.3.5 is Gauss–Bonnet. **Correct.** |
| [11] Hejhal LNM 548; [12] Iwaniec GSM 53 | Crossref / standard | Metadata correct; cited only as sources of DS (1). |
| [13] Garbin–Jorgenson, Kodai 43 | Crossref; arXiv:1603.01495v1 | Remark 2.7, (2.8) is precisely the heat-trace formula with the same identity, hyperbolic and elliptic terms. **Correct** (checked on the arXiv numbering). |
| [14] Schueth, AIF 69(7) | Crossref; arXiv:1812.06119 | Thm 4.1 gives the cone-point a_2. With K ≡ −1 it equals my exact b_2(k) for k = 2..7. **Correct.** |
| [15] Beardon | Crossref | Metadata correct (series and volume missing, m15). |
| [16] Jørgensen, AJM 98(3) 739–749 | Crossref | Metadata correct; see m12. |
| [17]–[21] | Crossref / DataCite / doi.org | All resolve and match (Crameri v8.0.1, 2023; Nat. Commun. 11, 5444; NETGEN CVS 1(1) 41–52; ARPACK SIAM 1998). |

All internal cross-references (theorem, lemma, equation, table, figure and section numbers) were checked against their targets. All resolve correctly.

---

## MAJOR issues

**M1. The "a-posteriori certificate" is not a certificate as applied: its inputs are neither established nor described in the paper.**
Pages affected: abstract; p. 3 after Thm 1.2; §7 pp. 15–16; Table 3; Fig. 2.

Theorem 7.1 is a correct conditional statement. Its conclusion, however, is only as rigorous as four inputs, and none of them is established or adequately described:
- **(a) Enclosures.** The eigenvalue error bounds ϵ_j are not established.
  - The paper says only "computed with high-order finite elements and error estimates" (p. 15).
  - Conforming FEM gives upper bounds via min–max. Two-sided enclosures need a guaranteed lower-bound method (e.g. Liu-type, Carstensen–Gedicke, Lehmann–Goerisch or Kato–Temple bounds) and control of floating-point error.
  - The paper does not say which method was used, whether the ϵ_j are rigorous, or what their size is. No ϵ_j appears anywhere.
- **(b) Completeness.** Completeness of the list up to λ̃_N ("complete below 1.6×10^4", "complete up to λ ≈ 2440–2560") is asserted without method.
  - Shift-invert Arnoldi (ARPACK) can miss eigenvalues, especially multiple ones, and the symmetric O_ϑ will have them.
  - The theorem needs the λ_j "counted with multiplicity in increasing order". The authors stress this themselves on p. 13.
- **(c) Systole lower bound.** The lower bound ℓ is a hypothesis of Theorem 7.1. For O_ϑ (2.634 … 0.694) and the triangle orbifolds it is stated without derivation.
  - I confirmed 1.8626, 2.2568 and the ϑ = 0 value 2.634 by independent computation (table above), but numerically, not by proof.
  - For the other seven members, ϑ is not even defined (m10), so a reader cannot reconstruct the orbifolds, let alone their systoles.
- **(d) Diameter upper bound.** The diameter bound Δ for O_ϑ ("at most 7.8", Table 1 caption) has no stated justification. "Twice the longest side" (p. 15) is asserted without proof even for triangles.

As it stands, the words "certifies", "certified" and "the certificate succeeds" (abstract, p. 3, p. 15, Fig. 2 caption) claim more than the paper shows. The validation lives in an external repository, which a reader of the journal cannot be expected to audit and to which the paper is not anchored by any stated method.

**M2. The abstract and introduction misstate the outcome of §7.**
- p. 3 says: "On the computed spectra of O(2,8,8), O(3,3,12) and eight orbifolds of signature (0;3,3,3,3) … the certificate succeeds with 21 to 750 eigenvalues". The abstract says the certificate "certifies the signature of a computed spectrum from 21 to 750 eigenvalues in our examples".
- But p. 15 says that for the member of systole 0.694 the certificate needs more than the 815 computed eigenvalues, so it does **not** succeed. Table 3's N_apr range is "over the seven of systole at least 0.846".
- So on the paper's own evidence the certificate succeeds on 9 of the 10 examples, not all of them. Saying the failure is "a limit of the data, not of the method" is reasonable, but the headline claims must match it.

## MINOR issues

- **m1 (Thm 1.1 vs Thm 6.2; pp. 2, 13).** Theorem 6.2 assumes λ̃_j ≥ 0, which its proof uses: |e^{-at} − e^{-bt}| ≤ t|a−b| needs a, b ≥ 0. Theorem 1.1 omits this hypothesis. Either add it or note that replacing λ̃_j by max(λ̃_j, 0) only reduces the error.
- **m2 (Thm 6.2, p. 13).** In δ = min{1/t_*, Γ_*/(8eNt_*)}, the first entry is redundant (Γ_* ≤ 1/4) and plays no role in the proof. Remove it or explain it.
- **m3 (Thm 1.2 vs Thm 7.1; pp. 3, 14).** Theorem 7.1 requires S to consist of hyperbolic signatures of area A and the λ̃_j to be nonnegative; Theorem 1.2 says neither. Make the two statements agree.
- **m4 (Thm 7.1, p. 14).** "min over 0 < s ≤ t": H is piecewise-defined and may jump at s = ℓ²/(2(1+ℓ)), so the minimum need not be attained. Write inf. (The bound is unaffected.)
- **m5 (Lemma 2.3 and Thm 7.1, pp. 5, 14).** Lemma 2.3 is stated for "ℓ the systole". Theorems 6.2 and 7.1 apply it with a lower bound ℓ ≤ systole, which needs:
  - monotonicity of B in ℓ, proved only on t ≤ ℓ²/(2(1+ℓ)) (fine, since that range increases with ℓ);
  - monotonicity of the second bound (obvious, but unstated).
  State the lemma for "systole at least ℓ".
- **m6 (§4, p. 11, after Thm 4.4).** "in no row of Table 2 is it the binding constraint through t_1" has no meaning: D does not enter t_1. Probably intended: "D matters only through t_3, which binds in rows 4, 6, 7". Rephrase.
- **m7 (Remark 8.4, p. 18, last sentence).** "by the case analysis of Lemma 5.1, only finitely many triples occur" for A < π/3 does not follow from that case analysis. Every (2,3,m) has area < π/3. Finiteness comes from s ≤ A/2π < 1/6 bounding r in each family ((2,3,r) needs 1/r ≥ 1/6 − A/2π, etc.). Give this one-line argument.
- **m8 (Table 2, row 2, p. 13).** t_1 = 6.85×10^-9 rounds to **6.8**×10^-9, not 6.9×10^-9. All other entries of Tables 1–2 reproduce exactly to the printed precision.
- **m9 (pp. 14, 20).** On p. 14 the ε^{-3} log(1/ε) growth is flagged "observations on the formulas, not proved asymptotics". On p. 20 it is stated flatly ("grows like ε^{-3} log 1/ε"). Make them consistent; it is in fact easy to prove from D ≍ A/ε, y_0 ≍ 6D and N ≍ t_*^{-1} log(…).
- **m10 (§7, p. 15).** The parameter ϑ of the family O_ϑ is never defined: only ϑ = 0 and ϑ = 2.8 appear, together with "two mirror symmetries". Define the quadrilaterals explicitly (e.g. by a side-length or Fenchel–Nielsen parameter) and list the eight ϑ and systoles. Otherwise Table 3 and Fig. 2 cannot be reproduced from the paper.
- **m11 (Table 3 and Fig. 2, pp. 15–16).** The triangle orbifolds' systoles are never stated (O(2,8,8): 2.2568; O(3,3,12): 1.8626 by my computation), yet Fig. 2 places them "at their own systoles". Also, Table 3's "N of Theorem 6.2 for the same class" for O(2,8,8) uses ε = 1.8626, the systole of O(3,3,12), not its own. This is harmless, since t_1 binds, but should be said.
- **m12 (§8.1, p. 16).** "We could not obtain the text of [16]" is not acceptable in a journal article: Jørgensen 1976 is in AJM/JSTOR. Moreover the needed inequality (non-elementary discrete ⟨A,B⟩ ⇒ |tr²A−4| + |tr[A,B]−2| ≥ 1), with proof, is, to my knowledge, in the authors' own reference [15] (Beardon, §5.4). Either cite the textbook proof (checking that ⟨γ, β⟩ in Prop 8.2 is non-elementary, which the hypotheses of Lemma 8.1 give), or keep the self-contained proof without that sentence.
- **m13 (§8.2, p. 20).** "the number of eigenvalues that pinching drives to 0 is bounded in terms of A" is stated without proof or citation. For surfaces this is Schoen–Wolpert–Yau / Buser / Otal–Rosas. For orbifolds give a reference or an argument (e.g. via a manifold cover).
- **m14 ([9], p. 3).** The description "N depending on ϵ, among triangles with all angles at least ϵ" matches Grieser–Maronna's account, but another secondary source describes Chang–DeTurck's N as depending on the triangle T (through its first two eigenvalues). I could not access the original. Please check the precise statement and quote the theorem number. Also use the AMS DOI 10.1090/S0002-9939-1989-0953738-7 and give the issue number (4).
- **m15 (Bibliography).**
  - [15] lacks the series (Graduate Texts in Mathematics, vol. 91).
  - [10] should give the stable URL (library.slmath.org/books/gt3m).
  - [13] Kodai: give pages as published; the theorem numbering I checked is that of arXiv:1603.01495, so please confirm "Rem. 2.7, (2.8)" in the published version.
  - [3]: I could not verify "Cor. 3" at source; please double-check the numbering.
- **m16 (Notation clashes).**
  - Γ (group) vs Γ(t), Γ_* (gap).
  - L is used as an index in Lemma 3.1 and in Lemma 3.5(ii) ("for L = k−1"), but as the lcm in Lemma 3.5(i), inside the same lemma.
  - N is the number of variables in Lemma 3.2 and the eigenvalue count elsewhere.
  - K is the Taylor index and the pigeonhole count (Prop 8.3).
  - ℓ is the systole, the integration variable bound, and the interval length in Prop 8.3.
  - s is s(σ), the Fourier variable (Lemma 2.5), and the Fermi coordinate (Prop 8.5).
  - A is the area bound and the matrix in Lemma 8.1.
  - "C_l = Σ b_l" is introduced inline in the proof of Lemma 3.5 and never defined.
  - Sig_{≤M} is defined (p. 8) and never used. Sig is a class of orbifolds while Sig(A,M) is a set of signatures.
- **m17 (Prop 8.5 statement, pp. 19–20).** The range of j in the λ_j bound (j ≥ 1) is not stated. Also, in the intermediate-value remark, say why λ_1(O_{k,b}) is continuous in b.
- **m18 (Intro, p. 2).** In the compactness sketch, "each λ_j is continuous there" needs a reference (continuity of eigenvalues on Teichmüller/moduli space of orbifolds).

## Presentation (figures and captions included)

The writing is terse but precise. Proofs are complete; cross-references are correct; the statements in §1 match those in the body apart from m1, m3 and M2. Each figure is checked against its caption below.

**Figure 1 (p. 14).** Checked against the caption, the text and my own quadrature of the gaps.
- The five grey gap curves are correct in their limits as t → 0: 0.75, 0.50, 0.42, 0.17, and 25t/12 for the darkest. At t = 1 the two lowest curves (0.025 and 0.029) cross the ordering, as in the plot.
- **(i)** The caption says the signature is decided where half the gap exceeds "both errors". The text and Theorem 7.1 require it to exceed their **sum**. Fix the caption.
- **(ii)** The caption does not say what the line styles are (solid grey and black: gaps; dashed: geodesic bound; dotted: N = 21 and N = 100 errors; shading: N = 21 window), nor that M = 12. That information is only in the text.
- **(iii)** The two dotted curves are not labelled with their N.

**Figure 2 (p. 16).** Checked against the caption, the text and Table 3 at 300 dpi.
- Values agree with Table 3:
  - squares: 7.4×10^12 (filled), 4.3×10^4 to 3.7×10^5 (open), 6.8×10^9 (triangles);
  - diamonds: 33/38 to 694/750, 21 and 39;
  - circles: 3 to 50 and 5 to 98, 3 and 4.
- The triangle orbifolds sit at 1.86 (orange) and 2.26 (teal), consistent with my systole computations.
- Problems:
  - **(i)** The open diamonds (N_apr, M = 3) are completely hidden under the filled diamonds. Only a doubled grey line betrays them, so one of the six plotted series is invisible.
  - **(ii)** There is no legend; the marker code is only in the text.
  - **(iii)** Neither caption nor text says which colour is which triangle orbifold.
  - **(iv)** The caption's "10^2 to 10^11" is correct but compares different classes for M = 3 and M = 12; say so.

**Figure 3 (p. 19).** Checked against the caption and the text (pp. 18–19).
- λ_1(7) ≈ 44.9 and λ_1(4096) ≈ 0.47 are consistent with the text.
- Each plotted λ_j lies below the j-th bound. I checked m = 1000 by hand: bound 1.44 for j = 1 vs λ_1 ≈ 0.5.
- Problems:
  - **(i)** The text says the bounds are "thin dashed"; they render dotted. The caption does not identify them.
  - **(ii)** The "line 1/4" in panel (a) coincides with the lower frame of the axes and is invisible.
  - **(iii)** Panel (b)'s horizontal reference lines are at j² = 1, 4, …, 36, which is not stated. The text says the rescaled quantities "approach j² slowly". In the plot, only j = 1 visibly decreases; j = 2..6 sit on plateaus clearly above j² (≈ 4.6, 10, 17.5, 26, 37) over 10² ≤ m ≤ 4096. Either weaken the sentence or show the trend (e.g. plot the differences from j²).
  - **(iv)** Interleaving: in (a) the bound for j lies just below λ_{j+1}. This is correct but confusing; distinguishing the bounds by shade would help.

**Tables.**
- Table 1: verified, except for "at most 7.8" (no method given).
- Table 2: verified, except m8.
- Table 3: the last column is verified. N_obs and N_apr depend on unpublished data (M1). Its caption is accurate (ranges, "seven of systole at least 0.846").

**Other.**
- The data statement points to a repository whose owner is not among the authors (github.com/Ali-M658/…). The editor may wish the archived (Zenodo) version to be the primary reference.
- The companion manuscript is cited as "in preparation". The authors state that no proof depends on it, and I confirm that none does.

## Recommendation

**Major revision.**

The mathematical core is correct and complete in every detail I checked:
- Theorems 1.1/6.2, 1.3, 3.3, 3.4, 4.4, 7.1 (as a conditional statement);
- Lemma 8.1;
- Appendix A;
- every constant in Tables 1 and 2.

That is to the authors' credit, and with M1–M2 fixed I would expect to recommend acceptance. The revision is needed because:
- the abstract and introduction advertise a "certificate" whose inputs (enclosures, completeness, systole and diameter bounds) are not established in the paper (M1);
- the headline statement of its success is inconsistent with §7 itself (M2).

Neither can be waved through by a rigour referee. The required changes are textual, plus a methods description; no new mathematics is needed unless the authors choose to make the certificate rigorous.

**Confidence:**
- High in the mathematical verification: line-by-line, with exact recomputation.
- High in the identification of M1–M2.
- Moderate on the citations I could only check through secondary sources ([3], [4], [9]).

## What resolves each issue

- **M1.** Either:
  - (a) add a short methods section (or appendix) that states how the ϵ_j were obtained, and with what guarantee (method, reference, interval or rounding control); how completeness of the list was ensured (e.g. a guaranteed lower bound on the (N+1)-st eigenvalue, or a Weyl-type count with explicit error, or a matching Neumann/Dirichlet count per symmetry class); a proof or explicit computation of the systole lower bounds and diameter upper bounds used (including a proof that twice the longest side bounds the diameter of a doubled polygon); and a table of the ϵ_j actually used; or
  - (b) if the enclosures are not rigorous, replace "certifies/certificate succeeds" in the abstract, §1 and §7 by "would certify, given rigorous enclosures; numerically, …", and present Table 3 / Fig. 2 as numerical illustrations of Theorem 7.1.
- **M2.** Change the abstract and p. 3 to say that the certificate succeeds on O(2,8,8), O(3,3,12) and seven of the eight O_ϑ (all with systole ≥ 0.846), and fails for the eighth for lack of computed eigenvalues.
- **m1.** Add λ̃_j ≥ 0 to Theorem 1.1, or add the max(λ̃_j, 0) remark.
- **m2.** Delete 1/t_* from δ or explain it.
- **m3.** Align the hypotheses of Theorem 1.2 with Theorem 7.1.
- **m4.** Replace min by inf in E_N.
- **m5.** Restate Lemma 2.3 for "systole at least ℓ" and note monotonicity of both bounds.
- **m6.** Rewrite the sentence after Theorem 4.4.
- **m7.** Add the one-line finiteness argument in Remark 8.4.
- **m8.** Correct to 6.8×10^-9.
- **m9.** Either prove the ε^{-3} log(1/ε) rate or hedge it on p. 20 as on p. 14.
- **m10.** Define ϑ and the quadrilaterals; tabulate ϑ, systole and diameter bound for the eight members.
- **m11.** State the two triangle-orbifold systoles, and the ε used for them in Table 3.
- **m12.** Delete "we could not obtain the text of [16]"; cite Beardon §5.4 (or [16]) and keep or shorten the proof.
- **m13.** Cite or prove the bound on the number of small eigenvalues for orbifolds.
- **m14.** Verify and quote the exact statement of Chang–DeTurck; use the AMS DOI and the issue number.
- **m15.** Complete [3] (check Cor. 3), [10], [13] and [15] as indicated.
- **m16.** Rename the clashing symbols (e.g. gap function 𝒢(t), lcm ℒ, pigeonhole count K′); define C_l; delete Sig_{≤M} or use it.
- **m17.** State j ≥ 1 in Prop 8.5; add a word on continuity of λ_1 in b.
- **m18.** Add a reference for continuity of eigenvalues on moduli space.
- **Figures.**
  - Fig. 1: fix "both" → "the sum of"; add a line-style key, M = 12 and N labels.
  - Fig. 2: make the open diamonds visible (offset or different marker); add a legend; name the colours.
  - Fig. 3: identify the dotted bounds and the j² lines in the caption; draw the 1/4 line visibly; revise or support the "approaches j²" sentence.
