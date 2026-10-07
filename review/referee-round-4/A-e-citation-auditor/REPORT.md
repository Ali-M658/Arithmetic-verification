<!-- Saved verbatim by the main session from the reviewer's returned text: the harness refused the reviewer's own write. Fetched sources (scratch/lit), scripts and page renders are in its git-ignored scratch/. -->

# Referee report (rigour and citations)

**Manuscript:** "How much of a hyperbolic orbifold does heat hear?" (39 pp.), with electronic supplement "Online Resource 1" (14 pp.)
**Journal:** Annals of Global Analysis and Geometry
**Role:** rigour-and-citations referee. I checked citations against their sources, bibliographic data, internal cross-references, figures against captions, and every place where a proof leans on a computation or on material outside the paper.

As instructed, I treat the marked placeholders (author contributions, AI-use statement, Zenodo DOI) as known. I did not open the code repository named in the data statement, by design. Page numbers are those of the manuscript PDF (S-pages are supplement pages). Every typographical, sign or figure point below was checked on page images rendered at 110 dpi, and Figure 6 was also checked at 300 dpi.

---

## Summary

The paper studies closed orientable hyperbolic 2-orbifolds with cone points. It asks how many small-time heat invariants c_1, ..., c_k determine the signature (genus and cone orders). The main results are:

1. **Thm 1.1(i), Cor 3.5.** The first ⌊Area/π⌋+4 heat invariants always suffice. No area-independent number suffices (Thm 3.12).
2. **Thm 1.1(ii), Thm 3.13, Prop 3.14.** The worst-case number f(A) lies between about √(A/6π) and A/π. Its growth exponent is tied to the Prouhet–Tarry–Escott function N(k): f is linear iff N(k)=O(k).
3. **Thm 1.1(iii), Thm 3.7.** With cone orders bounded by M, M invariants suffice and are optimal; against all of Sig, M + ⌈½ log(2⌊A/π⌋+8)⌉ suffice.
4. **Thm A, B, C.** n invariants determine the orders of a sphere with n cone points. There is a closed form for the determinant of the recovery system (Orlando), and n−1 invariants fail for n = 3, 4 and over the reals.
5. **Thm 1.2, §5.** For triangle orbifolds, two invariants suffice up to cone-order sum 17. They first fail on O(2,8,8), O(3,3,12). This pair is isolated for every scaling k because the cubic C_{27/2} ≅ E: y² = x(x+9)(x+384) has rank 0. Three invariants always suffice.
6. **Thm 1.3, §6.** Stability (Lipschitz / Hölder 1/k) of recovering orders from perturbed heat invariants, with explicit thresholds.
7. **§4 and §7.** The shape (moduli) enters only through t^{-1/2}e^{-ℓ²/4t}. Numerical experiments on computed spectra.

The arguments are short and mostly elementary once the closed-form cone coefficients (Lemma 2.6, Prop 2.7) are in place. Everything I recomputed was correct (list below). The citations are, with a handful of exceptions listed as minor issues, accurate at statement level. The paper is unusually careful about separating proved statements from computational ones.

## Significance

**What is good.**
- The reduction "heat invariants ↔ odd power sums plus a reciprocal sum" (Lemma 2.10, Lemma 3.3) is clean.
- It yields an explicit, area-dependent bound (Cor 3.5), which I have not seen before for this class.
- The PTE equivalence (Thm 3.13(d), Prop 3.14) is a genuine and somewhat surprising link.
- The bounded-order theorem (Thm 3.7) correctly locates the growth in large cone orders.
- The triangle case is sharp and complete:
  - the first failure at sum 18 is proved by hand (Thms 5.4–5.7);
  - the isolation of the minimal pair is proved by a hand 2-isogeny descent (App. C).
- Theorem 1.2 makes precise the remark of Dryden–Gordon–Greenwald–Webb [2, Rem. 5.16] that the invariant c "does not seem sufficiently strong to distinguish among" hyperbolic triangular pillows. That is a natural question for this journal's readership.

**Limitations (stated honestly by the authors).**
- The results concern heat invariants, not spectra. Orbifolds in Sig with different signatures are already known to have different spectra [10, Thm 1.1, Prop 3.3], and the whole sequence of heat invariants already determines the cone orders [14, Cor 4.21(iv), 4.23].
- The novelty is therefore quantitative: how many invariants, and with what growth. Much of the mathematical content is number theory of power sums.

I consider the paper publishable in AGAG after revision. The editor should weigh M2 below.

## Correctness and what was recomputed or checked

### Recomputed by me
Exact rational arithmetic in Python/SymPy, and PARI/GP 2.17.2 through cypari2, all in my own scratch folder.

**Cone coefficients and the heat expansion**
- **p_0 … p_3 from (4)–(5):** recomputed. (7) is correct. p_l(1)=0 holds. The leading coefficient is |B_{2l+2}|/(2(l+1)!(2l+1)) (Lemma 2.8).
- **Smooth coefficients α_0 … α_4:** equal 1, −1/3, 1/15, −4/315, 1/315 (p. 9).
- **Lemma 2.6:** the closed form of Φ_m, and its Taylor coefficients against (4), checked numerically for m = 2, 3, 7.
- **Agreement with the literature:** b_1 = −p_1/m agrees with DGGW (5.10) at R_{1212} = −1, and b_2 = p_2/m agrees with Schueth [9, Thm 4.1] (coefficient −37/5040 of 1/k).
- **(9):** c_1, c_2, c_3 checked for (2,8,8) and (2,3,7).

**The minimal pair O(2,8,8), O(3,3,12)**
- c(2,8,8) and c(3,3,12) for j ≤ 5: c_1 = 1/8, c_2 = 67/48 for both.
- d_3 = 25/12, d_4 = −1775/24, d_5 = 153025/48 (p. 31). Table S6 estimates are consistent with c_3 = −1601/480 and −867/160.

**Theorem C(3) and Example 3.6**
- Theorem C(3): R, P_1, P_3 and P_5 of both witnesses are correct (P_5: 65568 ≠ 249318 for n = 3; 25159618 ≠ 21298618 for n = 4).
- Example 3.6: areas 2π·14/15 and Ψ_1 = 224/15 on both sides.

**Theorem 3.7(ii)**
- M = 3: C = 120, ν = (−16, 9), s = −2.
- M = 4: C = 2520, ν = (28, −27, 8), s = 2.
- The pairs (1;3⁹)/(0;2¹⁶) (area 12π) and (0;2²⁸,4⁸)/(1;3²⁷) (area 36π) share exactly M−1 invariants.
- c_M differences are −1/3 and 1, equal to (−1)^M C a_{M−2}.
- (0;2⁵)/(1;2) share exactly c_1.

**Every pair in Table S1 (all 20 rows, parsed from the PDF)**
- The number of shared invariants equals the stated L in every row.
- The area values match: e.g. genus L=4 41149074301/5878522650; genus L=6 12 − 7.85·10⁻³¹; equal-count L=7 18 − 5.73·10⁻⁴²; cone-count L=6 ≈ 26.55911353.
- The size counts |U*|+|V*| = 14, 18, 24, 40 and 16, 20, 26, 40 in Example 3.16(iii) and the T(L) table (p. 19) match.

**PTE pieces of Lemma 3.15 / Table S1** (all satisfy the stated power-sum identities; correct degree)
- ±{7,11,18}/±{3,14,17}
- ±{2,16,21,25}/±{5,14,23,24}
- ±{18,245,…}/±{103,189,…}
- the size-12 set of [36, (5)]
- the two 7-sets and Letac's two 9-sets.

**Remark 3.2 (n = 4 search)**
- Exhaustive search to 130: 16 primitive witnesses. To 220: 33 primitive. Both match S-p. 2.
- No triple shares (R, P_1, P_3).
- The 8 primitive witnesses with orders ≤ 84 are exactly Chen (A.685)–(A.692).

**Remark 3.17:** the partner triple of {1,1,1,1,7} is {0.26636, 4.28304, 6.45060} (S-p. 2).

**Section 5**
- **Theorem 5.4:** x*(p) for p ≤ 9, S*(p), gap_p(3p+7) = −2(p²−5p−30)/(p(p+1)(p+3)(p+4)(p+5)), and all odd-parity gaps quoted in the proof (1/840, 1/2310, 1/10296; −7/936, …, −17/4680) are correct.
- **Lemma 5.3:** the bound 1/3 + 60/224 = 101/168 < 7/10 holds.
- **Table S3:** the 83 triads and their R values are correct; the only coincidence is (2,8,8)/(3,3,12).
- **Table S2:** all 13 first collisions are correct (enumeration to S ≤ 600).
- **Proposition S2.1:** the collision-free sums ≤ 600 are exactly the 38 listed. I did not extend to 4800.

**Theorem 5.8 and Appendix C**
- ψ maps E into C_{27/2}: C(ψ) ≡ 0 modulo E, symbolically.
- The 12 points map as stated; φ(1:4:4) = (−24, 360).
- (16,400) is a flex: x³+393x²+3456x − (21x+64)² = (x−16)³.
- Δ = 2¹⁸3⁸5⁶; #E(F_7) = #E(F_11) = 12.
- PARI: ellrank → [0,0]; elltors → Z/6 × Z/2. ellanalyticrank → 0 with L(E,1) ≈ 1.3376 ≠ 0, conductor 90. This is an unconditional confirmation via Kolyvagin; the authors may wish to mention it.
- I re-did every congruence in the hand descent of Appendix C (the classes ±2, ±3 mod 5 on E; d_1 = 3, 5, 15 mod 3 and mod 9 on E′, including 5w²−w+2 ≡ 6 for w ∈ {1,4,7}). It is correct.

**Section 6**
- **Prop 6.2:** amp_0…amp_4 = 2, 14, 498, 4062, 56230/3; row P_3 = −18c̃_1 − 120c̃_2 − 360c̃_3; the diagonal of F is as stated.
- **Thm 6.4:** ζ_3 = 1, ζ_4 = 79/3, ζ_5 = 14048/15. These are correct only when j ≤ n−2; with j ≤ n−1 one gets 49/3, 2336/5, … (see m14).
- **Thm B:** det M checked exactly, including the sign ς_n, for (2,8,8), (3,3,12), (2,3,7), (3,10,15,30), (2,3,5,7,11); the true e solves (11).
- **Prop 6.6(i):** δR = s²/(4(64−s²)), δP_3 = 48s².
- **Prop 6.7:** the constant 498 + 42a² is correct.
- **Table S4:** the ratios δ_up/δ_cert and the range 5·10²–2·10⁸ for δ_up/δ_thm are consistent.

**Appendix B:** Euler's beta integral and the moment formula ∫₀^∞ r^{2k+1}/(e^{2πr}+1) dr = (1−2^{−2k−1})(−1)^k B_{2k+2}/(4(k+1)) checked numerically.

**Proofs checked line by line:**
- Lemma 2.4; Lemma 2.5, including the logarithmic derivative of B and the constant C;
- Theorems A, B, C(1), 3.4; Cor 3.5; Theorem 3.7(i),(iii), including the inequality 2M + (k−3)(k+1) > 0;
- Prop 3.11; Lemma A.1; Prop A.2; Theorem 3.13(a)–(d); Prop 3.14;
- Lemma 5.2–Theorem 5.7.

I found no mathematical error.

**Figure geometry** (Fig. 4, §4, S6): sinh a sinh b = cos(π/3) = 1/2 gives systoles 4b = 2.634 at ϑ = 0 and 0.694 at ϑ = 2.8, as stated.

### Citations checked against the source (statement level unless noted)
Sources: arXiv full texts, publisher/Crossref/DataCite metadata, zbMATH, Project Euclid / Numdam / edoc.hu-berlin.de full texts, and the Cremona and Thurston online texts. All are saved in scratch/lit.

| Ref | Cited for | Result |
|---|---|---|
| [1] Donnelly | locality; heat invariants are spectral | Bibliographic data checked (Crossref, zbMATH). Content not fetched (paywalled). |
| [2] DGGW (arXiv 0805.3148, journal numbering checked against it) | Thm 4.8 (locality / expansion); Thm 5.1; Ex. 5.3, Prop 5.5, (5.7); Ex. 5.6, (5.10); Thms 5.14–5.15 (c = 12 × degree-0 term determines type for χ ≥ 0); Rem 5.16 quote | All correct, quote verbatim. Pages 205–238 confirmed (zbMATH). |
| [3] Erratum, MMJ 66 (2017) 221–222 | quote "implicit assumption that Iso^max(N) is nontrivial", affects Thm 5.1 only | Bibliographic data correct. **Text not accessible to me** (Project Euclid blocks headless access). Plausible, since DGGW's proof of Thm 5.1 uses Iso^max(N). See m6. |
| [4] Richardson–Stanhope | Thm 4.7 | Correct. |
| [5] Borwein–Ingalls (checked on the authors' preprint P98; journal page numbers could not be checked, since e-periodica is captcha-protected) | §2 definition of N(k); Props 2–3; §3 odd symmetric; §6 Problem 3 and quote "has been made for many years"; Letac 9-sets; size-7 sets; Wright report | Content correct, quote verbatim. Bounds attributed to Wright alone; BI attribute them to Wright **and Melzak** (m3). "[5, Prop. 1 and §3]" does not state the cited lemma (m4). Zbl 0810.11016, pp. 3–27 confirmed. |
| [6] Bérard–Webb MZ (arXiv 2008.12498) | Thm 3.1 | Correct. |
| [7] Bérard–Webb CRAS | announcement | Title, volume and pages confirmed (zbMATH; also cited verbatim in [4] and [6]). |
| [8] Schueth AGAG 2026 (arXiv 2511.22255) | Abstract (b_{1/2}), §1 (germ locality), p. 2 (discussion of all-order formulas) | Correct. Article no. 2, vol. 69(1) confirmed. |
| [9] Schueth AIF (arXiv 1812.06119) | Thm 4.1 (a_2), Rem 4.2 (a_0, a_1, "already computed in [8], 5.6") | Correct, and recomputed. |
| [10] Dryden–Strohmaier (arXiv math/0504571) | eq. (1) trace formula and the class of h; trace formula taken from Hejhal/Iwaniec; elliptic classes ρ^j; Thm 1.1; Prop 3.3; Thm 3.2 (Gauss–Bonnet) | Correct. Note DS record an independent proof by Doyle–Rossetti (m7). |
| [11] Linowitz–Voight | Thm A and following sentence (signature (0;2,2,2,2,2,3,4)) | Correct. |
| [12] Stanhope | Main Thms 1–2 | Correct. |
| [13] Abreu–Dryden–Freitas–Godinho | Thm 1, §6.1 | Correct. |
| [14] Uçar thesis (edoc full text) | Cors 4.21(iv), 4.23; Thm 4.20(ii), (4.25), (4.33)–(4.35) | Correct. |
| [14] Uçar thesis, second use | Thm 4.10, Cor 4.18, cited for "spectrum of a triangle orbifold = union of Neumann and Dirichlet spectra" | **Inaccurate** (m1). |
| [15] Chang–DeTurck | finite count among triangles with angles ≥ ε | Matches the paraphrase in [21]. zbMATH Zbl 0721.58053 says N depends only on λ_1, λ_2. Primary not accessible (m5). DOI given is the JSTOR alias (m10). |
| [16] Steinig | uniqueness | Bibliographic data correct, Zbl 0238.10007. Content via [17], which states Steinig's result. |
| [17] Laurens | Lemma 3.2 and the remark after it | Correct. |
| [18] Melánová–Sturmfels–Winter | Prop 24 | Correct. |
| [19] Korobov–Bugaevskaya | §3 | Bibliographic data correct. Content not accessible. |
| [20] Chen survey arXiv 2506.11429v1 | §A.5.8 (A.685)–(A.692), "computer search … 2017"; Identity 9 with m = 3, (3.27)–(3.28); (3.33); A.1.6, A.1.17, A.1.26, A.1.33 p. 224 | All correct. The L = 6 pieces are due to Wróblewski (2009) per Chen; credit could be given. |
| [21] Grieser–Maronna | Thm 1 (first three heat invariants suffice for Euclidean triangles) | Correct. |
| [22] Philippe, Sémin. TSG 28 | Thm 3.1 | Correct. This is a survey; the original is Geom. Dedicata 149 (2010) 155–160 (m8). |
| [23] Bremner–Guy–Nowakowski | p. 117 (curve, reciprocal pairs) | Bibliographic data correct. Text not accessible (AMS blocks headless access). The reciprocal symmetry for every Λ I verified directly. |
| [24], [29] Hejhal, Iwaniec | source of trace formula | Consistent with DS's own references [7], [8]. |
| [25] McKean | classical t^{-1/2}e^{-ℓ²/4t} | Bibliographic data correct. There is a Correction, CPAM 27 (1974) 134 (m9). |
| [26] Garbin–Jorgenson (arXiv 1603.01495) | Rems 2.6–2.7, (2.8), normalization of ĝ | Correct. Pages 84–128 confirmed. |
| [27] Dryden arXiv math/0411290 | proof of Thm 4.5 | Correct. |
| [28] Thurston, Ch. 13 | 13.3.4–13.3.5 (χ, Gauss–Bonnet); Cor 13.3.7 (dim Teich = −3χ(X_O) + 2k + l = 6g−6+2n) | Correct, but "hyperbolic exactly when χ < 0" is 13.3.6 (m2). |
| [30] Watson | lune expansion | Zbl 1076.35042 confirmed. |
| [31] Holtz–Tyaglov (arXiv 0912.4703) | (1.37), Thm 1.17 | Correct. Sign checked: with zeros −m_i the two signs (−1)^{n(n−1)/2} cancel, giving (10). |
| [32] Wright 1935 | improved N(k) bounds | Bibliographic data correct. As reported in [5], together with Melzak (m3). |
| [33]–[35] Hua, Dorwart–Brown, Borwein | background | Bibliographic data correct. |
| [36] Coppersmith et al. | (5), ideal solutions known for k ≤ 9, 11 | Correct. |
| [37] Croot–Mao–Yip arXiv 2609.05061v1 | §1, same facts | Correct. |
| [38] Borwein–Lisoněk–Percival | pp. 2064, 2069 | Bibliographic data correct. Text not accessible. I verified the size-10 set is an ideal symmetric solution. |
| [39] Huber | classical | Bibliographic data correct. |
| [40] PARI/GP 2.17.2 | release 5 March 2025 | Correct (pari-announce archive). |
| [41] Cremona | §3.3 p. 70 (reduction injective on torsion at odd good primes); §3.6 Method 1, (3.6.2) | Correct. |
| [42] Ostrowski | Thm XXX, (71,1) | Not verified. The memoir is in two parts, Acta Math. 72, 99–155 and 157–257 (m9). |
| [43] Crameri v8.0.1 | colour maps | DataCite record correct. |
| Supplement [1]–[6] | Chen; NETGEN; NGSolve; ARPACK; Strohmaier–Uski + Correction | Bibliographic data correct; Strohmaier–Uski §7.1 is on the Bolza surface. |

**Bibliographic data.** Every DOI resolves to the cited work, with authors, year, volume and pages matching Crossref, DataCite or zbMATH. The only exception is the JSTOR alias DOI of [15].

**Internal cross-references.** All references to numbered items exist and point to the right statement. Specifically:
- Thm 1.1 ↔ Cor 3.5, Thm 3.12, Thm 3.13, Thm 3.7, Cor 3.8, Thm A, Thm C;
- Thm 1.2(i)–(iv) ↔ Thms 5.6, 5.7, 5.1, 5.8;
- Thm 1.3 ↔ Thms 6.5, 6.8, Props 6.6, 6.7;
- Problems 1–4; Supplement Sections S1–S7 and Tables S1–S6.

Every supplement section cited for a computation exists and describes it.

---

## MAJOR issues

**M1. Theorem 1.3 (p. 4) states more than §6 proves.**
The theorem says: "for data that are heat invariants of positive real orders it is ½, and attained, at a double order and when all n ≥ 3 orders are equal."
- The natural reading is that for realizable data the Hölder exponent is ½ in general.
- Section 6 proves less (p. 29, after Thm 6.5): "for data coming from real orders it is ½ at a double order (Prop 6.6(i)) and when all the orders are equal (Prop 6.7); other configurations are not settled". The proof of Prop 6.7 adds "mixed clusters are not settled".
- A headline theorem must not admit a reading that is not proved. The same sentence appears in substance in the Introduction.

**M2. Scope, length and balance, for the editor.**
The core results (Cor 3.5, Thm 3.7, Thm 3.13/Prop 3.14, Thms A–C, §5) occupy about 20 pages. Around them are substantial blocks whose role is illustrative or computational:
- Remark 3.17 with a 4.3·10⁹-case modular search;
- Fig. 3's 525 complete area classes;
- Prop S2.1 to 4800;
- the stability theory with certificates (§6, S3), which the authors say they use only a posteriori;
- §4, which records "classical" facts (p. 20);
- §7 and S4–S6, numerical spectra which "nothing here is used in a proof" (p. 30).

For an AGAG reader, the geometric-analytic content is Theorem 2.3/Prop 2.7 (a re-derivation of Uçar's coefficients) and §4. The rest is power-sum and Diophantine analysis.

I do not object to any of it on correctness grounds; everything I checked is right. But the paper would be stronger, and easier to referee, if §6 and §7 were shortened substantially or moved to the supplement, and if the number-theoretic side were tightened. The editor should decide whether the balance fits the journal.

## MINOR issues

**Citation accuracy**

- **m1 (p. 31, §7, first line).** "[14, Thm 4.10, Cor. 4.18]" is cited for "the Neumann and Dirichlet spectra of the triangles, whose union is the spectrum of the orbifold". The sources do not support this:
  - Uçar's Thm 4.10 concerns the spherical setting M = S²(r) with Z_k/D_k quotients and a lune Ω.
  - Cor 4.18 gives heat invariants of constant-curvature surfaces with totally geodesic boundary.
  - Neither states the decomposition for hyperbolic triangle orbifolds. The fact is elementary and is proved in S4 (S-p. 9).
- **m2 (p. 7, Def 2.1).** "[28, 13.3.4–13.3.5]" supports the formula for χ and Area = −2πχ. "Carries a hyperbolic metric exactly when χ(O) < 0" is Thurston's Theorem 13.3.6.
- **m3 (p. 17).** "Wright [32] improved the upper bound to ½(k²−4) … as reported in [5, p. 7]." Borwein–Ingalls write "Slightly stronger upper bounds are discussed in [22] and [15]", i.e. Wright **and Melzak** (Canad. Math. Bull. 4 (1961) 233–237). Credit both or cite precisely. In the preprint version the even-k bound is misprinted as "12(k²−4)"; please confirm against the journal page.
- **m4 (p. 5).** "two n-multisets … have equal P_1, P_3, …, P_{2n−1} exactly when they agree after deleting pairs {a, −a} [5, Prop. 1 and §3]". BI's Prop 1 is the equivalence of the three formulations of the PTE problem; §3 defines ideal symmetric solutions. Neither states this lemma. It is immediate from Lemma 3.1 and the argument of Theorem A; say so rather than citing [5].
- **m5 (p. 5–6).** The description of [15] ("among triangles whose angles are all at least ε, with a number depending on ε") follows Grieser–Maronna [21, §4]. zbMATH Zbl 0721.58053 summarises Chang–DeTurck as "N depends only on the first two eigenvalues". Please state the theorem from the primary source, with its number.
- **m6 (p. 2).** The erratum quotation [3] could not be verified by me (paywall). Please double-check the wording. Also note that [4, Thm 4.7], used on p. 3, rests on the same Iso^max/b_0-positivity mechanism as [2, Thm 5.1]: Richardson–Stanhope's Cor 4.8 is "equivalent to [5, Theorem 5.1]". Add a sentence on why [4] is unaffected; for instance, [4] postdates the erratum, and its Lemma 4.3 places γ in Iso^max of a primary stratum.
- **m7 (pp. 5–6).** Dryden–Strohmaier [10, p. 2] record that Doyle and Rossetti proved Theorem 1.1 of [10] independently (arXiv math/0605765). Cite it in the prior-work paragraph.
- **m8 (p. 6).** [22] is a seminar survey. Its Thm 3.1 is announced there as the main result of E. Philippe, *Sur la rigidité des groupes de triangles (r,p,q)*, Geom. Dedicata 149 (2010) 155–160. Cite the original.
- **m9 (references).**
  - [25] McKean has a Correction, Comm. Pure Appl. Math. 27 (1974) 134 (Zbl 0317.30018); cite it with [25].
  - [42] Ostrowski's memoir appears in Acta Math. 72 in two parts, pp. 99–155 and 157–257. You cite only the second; confirm that Théorème XXX and (71,1) are there. I could not verify this statement.
- **m10 (references).** [15]: the DOI 10.2307/2047071 is a JSTOR alias that redirects to the publisher DOI 10.1090/S0002-9939-1989-0953738-7. Use the latter and add the issue, 105(4).
- **m11 (p. 3).** "We know of no result on whether the whole spectrum hears it for closed hyperbolic orbifolds". Richardson–Stanhope [4, p. 1] state explicitly that detecting orientability in the closed setting "is still unresolved"; cite them here.
- **m12 (p. 17).** The status "No bound o(k²) is known" is supported by a 1994 quotation. Add a recent source ([20] or [36]) confirming the problem is still open in 2026.
- **m13 (p. 18; Table S1).** Credit the original discoverers of pieces taken from Chen's survey. In particular the A.1.33 sets [23,163,…] and [43,161,…] are due to Wróblewski (2009) per [20, p. 224]. Letac and Gloden are credited, so be consistent.

**Statement precision and notation**

- **m14 (p. 28, before Thm 6.4).** In the definition of ζ_n the range of j is implicit. The stated values ζ_4 = 79/3 and ζ_5 = 14048/15 hold only for j ≤ n−2 (rows of M). With j ≤ n−1 one gets 2336/5 and 699984/35. State the range.
- **m15 (pp. 3, 14, 17).** Theorem 1.1(iii), Theorem 3.7(iii) and Corollary 3.8 use "log" without a base. The proof of 3.7(iii) uses log(1+y) ≥ 2y/(2+y), so it is natural log; say so.
- **m16 (notation clashes).**
  - h_t (test function, p. 7) vs 𝔥_t (heat kernel, p. 4). Typographically distinct, but easily confused.
  - g (genus) vs g_t, g (Fourier transforms) in §2.1 and App. B.
  - κ: size in the proof of Thm 3.4; constant in Thm C(1); curvature in Uçar's notation.
  - c: the DGGW invariant (p. 5); the constant in Thm 1.1(ii); the shift in Prop A.2.
  - C: class; constant; C(A, ℓ, diam); the integer in Thm 3.7(ii).
  - M: order bound vs the matrix M(I).
  - Please disambiguate the worst of these.
- **m17 (p. 16, Def. of f_g, f_n).** Say explicitly that f_n is maximised only over genus-0 O while f_g is maximised over all O. This is stated but easy to misread. Also state the analogue of f(A) ≥ L+1 ⇔ A ≥ A_min used in the proof of 3.13(d) for f_g and f_n.
- **m18 (p. 12, Remark 3.2; S-p. 2).** "193 witnesses ≤ 440" and the pencil counts "17/49" (≤ 130 / ≤ 220) count different things. My exhaustive count to 220 gives 53 witnesses (33 primitive), as against 49 from pencil splittings. One sentence distinguishing "all witnesses" from "pencil-split witnesses" would avoid confusion.

**Reproducibility and outside material**

- **m19 (p. 32; S-pp. 1, 6, 9).** The repository https://github.com/Ali-M658/Arithmetic-verification is under an account that does not correspond to any listed author. I did not inspect it, by instruction.
  - The paper is careful that no proof depends on it. Still, Fig. 3's dots, Prop S2.1 (S ≤ 4800), Remark 3.2's counts to 440, the n = 5 search, and Remark 3.17's search exist only there.
  - The archival Zenodo copy (placeholder) is essential. The repository's ownership or affiliation should be stated.
- **m20 (S5, S-p. 12).** The "blind" protocol is anchored to a commit hash and a date (3c1139a, 1 Oct 2026). Without the archival copy this cannot be checked. Tie it to the Zenodo record.

## Presentation (figures and captions)

Each figure was checked against its caption and against the text on page images.

**Fig. 1 (p. 2).** One triangle of O(2,8,8) and of O(3,3,12), coloured by 4πt𝔥_t(x,x) at t = 0.02, log colour bar 1–12.
- In (a) the two sharp tips (order 8) are the darkest and the right-angle corner (order 2) is orange. In (b) the order-12 tip is darkest and the two order-3 corners are orange. This is consistent with the claim that the value tends to the order m at a cone point.
- Wording conflict: the caption says "in schematic shapes" and p. 4 says "in a stylised shape". But p. 4 also says the value "is drawn at the point with the same Poincaré-disc coordinates", which would make the shape the true Poincaré-disc picture, not a schematic. The two statements conflict; clarify which.

**Fig. 2 (p. 14).** Checked mark by mark.
- (a), upper row: discs at X* = {2,8,8,−3,−3,−12} and rings at −X* are drawn correctly, coloured by orbifold. Lower row: orbifold against itself.
- (b): U* = {15, 1} (with the padding 1, d = 1) and −V* = {−3,−3,−5,−5}, with rings at −X*, correct.
- Caption and text agree.

**Fig. 3 (p. 19).**
- Solid step curve = ⌊2s⌋+4 (Cor 3.5): 4 for s < ½, 28 near s = 12. Dashed curve = ⌊√((s−1)/3)⌋+2 from s = 4: 3 at s = 4, 7 near s = 100.
- Open squares at s = 2.4, ≈15, ≈63, ≈255, ≈1023, at K = 3…7 = L+1, matching the Table S1 "Prouhet" rows.
- Diamonds at the Table S1 / Example 3.16 areas with K = L+1.
- Consistent. But the caption does not define the dots, diamonds, squares, the split disc, or which step curve is which. That is all in the body text. Make the caption self-contained.

**Fig. 4 (p. 22).**
- (b): λ_1 (heavy) falls from about 4.12 to 0.43; square-root axis; thin verticals at ϑ = 0.8, 1.6 (and 0, 2.8 at the frame), matching the text on p. 21.
- (a): schematic, as stated.
- Consistent.

**Fig. 5 (p. 23).** The coloured triangle plus its pale mirror image form one copy of each orbifold; the elliptical rim matches the oblique orthographic view described in the text. Consistent. I could not count the 2m triangles at each vertex at this resolution.

**Fig. 6 (p. 26; 300 dpi crop).**
- Dots (first overlap) at S = 19, 23, 26, 29 (p = 3, 5, 6, 7). Circles (first collision) at (20, 0.5), (38, 0.452), (34, 0.310), (62, 0.221), (117, 0.244) (p = 4, 3, 6, 7, 5). The split disc at (18, ¾) is p = 2.
- These match Table S2 and my own enumeration.
- Only adjacent pairs p = 2…7 can be marked, because band 9 is not drawn, so band 8 has no marker. The caption should say this and mention the split disc.

**Fig. 7 (p. 30).**
- Measured slopes: about 1 for (2,3,7) (thin solid), about ½ for (2,8,8) (heavy), about ⅓ for (4,4,4) worst case (dashed), and about ½ for the dotted realizable-data curve.
- Diamonds sit near δ_cert = 3.7·10⁻³, 2.3·10⁻³ and 4.5·10⁻⁴; the horizontal line is at ½. All consistent with Table S4 and the text on p. 29.
- But the caption ("The slopes are the exponents of Theorem 6.5") is incomplete: the dotted curve's slope ½ comes from Prop 6.7, not Thm 6.5. The line styles, diamonds and horizontal line are not identified in the caption.

**Fig. 8 (p. 31).**
- (a): the light grey d_3 t reaches 0.08 near t = 0.04. The mid-grey d_3t + d_4t² peaks at about 0.015 near t = 0.014 and vanishes near 0.028. The dark grey cubic truncation shoots up near 0.03. D (heavy) follows the dashed elliptic term to about 0.1 and changes sign near 0.3 (S-p. 11 says 0.34).
- (b): emergence circles from t ≈ 0.005 (ℓ = 0.694) to t ≈ 0.05 (ℓ = 2.21), consistent with ℓ²/4t* ≈ 24.5.
- Consistent. The caption omits the grey truncations, circles and shading, which are explained only in the text.

**Tables.**
- The T(L) table (p. 19), Tables S1–S4 and S6 are consistent with my computations.
- Table S4's "rounded up/down" convention is stated.
- Table S3 is exactly right.

**Other presentation points.**
- The abstract is dense. Its long, compressed sentences assume material defined later (e.g. "rank-0 elliptic curve", "Prouhet–Tarry–Escott function").
- The roadmap (p. 4) should say where each part of Theorem 1.1 is proved; currently only "Sections 2–3".

## Recommendation

**Minor revision** (bordering on major only through the editorial question M2).

**Confidence:** high for correctness of what I recomputed (listed above). Medium-high for the citations overall:
- I verified at statement level 31 of the 43 references in the paper.
- I verified bibliographic data for all 43 and for the six supplement references.
- References [3], [19], [23], [38], [42] and the primary text of [15], [32] could not be read headlessly (paywall, Cloudflare or captcha).

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Rephrase Thm 1.3 (and the Introduction) to say that for realizable data the exponent ½ is proved at a double order and when all n ≥ 3 orders are equal, and is open for other configurations, as on p. 29. |
| M2 | Shorten §6 and §7 (move the certificate discussion and most numerics to the supplement), or justify their place in the main text. Possibly trim §4 to the new quantitative part (Thm 4.4). Editor's call. |
| m1 | Replace "[14, Thm 4.10, Cor. 4.18]" by the elementary argument of S4 (or a correct reference). |
| m2 | Cite [28, Thm 13.3.6] for "hyperbolic iff χ < 0". |
| m3 | Credit Wright and Melzak as in [5]; confirm the even-k bound against the printed journal page. |
| m4 | Replace "[5, Prop. 1 and §3]" by "(Lemma 3.1; cf. [5, §3])" or give the two-line proof. |
| m5 | State Chang–DeTurck's theorem from the paper itself, with theorem number. |
| m6 | Verify the erratum quotation; add one sentence on why [4, Thm 4.7] is unaffected by the erratum. |
| m7 | Cite Doyle–Rossetti alongside [10]. |
| m8 | Cite Philippe, Geom. Dedicata 149 (2010) 155–160, for the length-spectrum rigidity. |
| m9 | Add McKean's Correction; give Ostrowski's two-part page range and confirm the location of Théorème XXX. |
| m10 | Use DOI 10.1090/S0002-9939-1989-0953738-7 and the issue number for [15]. |
| m11 | Cite [4, §1] for the open status of hearing orientability in the closed setting. |
| m12 | Add a recent reference for the open status of N(k) = o(k²). |
| m13 | Credit Wróblewski (2009) and other original finders as reported in [20]. |
| m14 | Write "max over 0 ≤ j ≤ n−2" in the definition of ζ_n. |
| m15 | State that log is the natural logarithm. |
| m16 | Rename the clashing symbols (at least κ, c, C, M). |
| m17 | One sentence each in §3.4 on the maximisation classes of f_g, f_n and the analogue of A_min used in 3.13(d). |
| m18 | Distinguish "all witnesses" from "pencil-split witnesses" in Remark 3.2/S1, and give the total count to 220. |
| m19 | State the repository's ownership or affiliation; deposit the archival copy (Zenodo) before acceptance. |
| m20 | Reference the archived record for the pre-registered protocol of S5. |
| Fig. 1 | Resolve "schematic/stylised" vs "same Poincaré-disc coordinates". |
| Figs. 3, 6, 7, 8 | Make captions self-contained: identify all marks and line styles; for Fig. 6 note that only p = 2…7 are marked; for Fig. 7 attribute the dotted slope to Prop 6.7. |
