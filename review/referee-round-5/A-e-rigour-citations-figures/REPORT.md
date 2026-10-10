<!-- Saved verbatim by the main session from the final message of reviewer A-e: the harness refused the reviewer's own write. Text from the report's first heading on; the reviewer's preceding cover note was dropped. -->
# Referee report: "How much of a hyperbolic orbifold does heat hear?" (Annals of Global Analysis and Geometry)

I could not save this report to `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-5/A-e-rigour-citations-figures/REPORT.md`: the harness refused file writes from this agent. The complete report follows. Scripts, renders and fetched literature are in `.../A-e-rigour-citations-figures/scratch/`.

Referee remit: rigour, citations and figures, covering the whole submission (44 pp.) and its electronic supplementary material (18 pp.). As instructed, the author-contribution, AI-use and Zenodo-DOI placeholders are treated as known. I read the rendered pages, not only the extracted text, before reporting any typographical, sign or figure point.

## Summary

The paper asks how many heat invariants c_1, c_2, ... of a closed orientable hyperbolic 2-orbifold with cone points are needed to determine its signature. Its main results are:

- **Bounds on the growth function.** The least such number, maximised over area ≤ A, is f(A). Elementary bounds are √(A/6π) ≲ f(A) ≤ ⌊A/π⌋+4.
- **Equivalence with a Prouhet–Tarry–Escott question (Thm 1.1(ii)).** The statement "f(A) ≥ cA^α" is equivalent to N(k) = O(k^{1/α}).
- **Bounded cone orders (Thm 1.2 / Thm 3.8).** If every cone order is at most M, the first M+1 invariants suffice against all of Sig, the number M+1 is attained, and M suffices within Sig_{≤M}.
- **Genus-0 recovery (Thms A–C).** For genus 0 there is an explicit linear-algebraic recovery of the orders from n invariants. Its determinant is an Orlando/Hurwitz determinant.
- **Triangle orbifolds (Section 5).** Three invariants always suffice. Two suffice up to cone-order sum 17. The first failure is the pair O(2,8,8), O(3,3,12), which is isolated via a rank-0 elliptic curve with 12 rational points.
- **Further material.** A section on variable curvature, a stability theorem, and numerical illustrations from computed spectra.

The core mathematics is correct wherever I could test it, and that covers a great deal; details are below. The bibliography is accurate at the level of volume, page and DOI, and the figures agree with the data and formulas they claim to show.

My concerns are of three kinds:
- one claim in the abstract does not match the theorem it summarises;
- two "Propositions" in Section 2.4 are supported only by sketches;
- a cluster of pinpoint citations do not say exactly what they are cited for.

## Significance

The question is natural, and the answer has real structure. The paper gives:
- a sharp area-free answer M+1 for bounded orders, proved by a clean sign-change (Descartes-type) argument;
- a reduction of the growth question to the Prouhet–Tarry–Escott function N(k), losing only constant factors;
- a "price" of a genus change;
- an arithmetic explanation of the first triangle collision.

The Prouhet–Tarry–Escott connection (Prop. 3.15) is the most interesting contribution: it relocates an inverse-spectral counting question onto a classical open Diophantine problem with explicit two-sided constants.

The triangle-orbifold section answers precisely the question left open in Dryden–Gordon–Greenwald–Webb, Rem. 5.16. The variable-curvature discussion (Section 2.4) is a useful contrast, but it is the least rigorous part (see M2).

The paper is appropriate for AGAG in scope.

## Correctness and what was recomputed or checked

All computations were done in a private venv, using exact rational arithmetic (Python Fractions / SymPy) and PARI/GP 2.17.2 via cypari2, unless stated otherwise.

### A. Mathematics recomputed

1. **Lemma 2.6 and Lemma 2.8.**
   - The closed form Φ_m(u) = (cot u − m cot mu)/(4m sin u) and the Bernoulli formula (4) for φ_k(m) agree with the Taylor coefficients of the defining sum, for m = 3, 5, 8 and k ≤ 3, to 10^{-15}.
   - p_0,…,p_3 come out as (m²−1)/12; (m²−1)(m²+11)/360; (m²−1)(2m⁴+9m²+37)/5040; and (m²−1)(m²+3)(3m⁴+2m²+19)/30240. These agree with (8) and with the K³ coefficient of Prop. 2.11(iv).
   - The leading coefficients equal |B_{2l+2}|/(2(l+1)!(2l+1)).
2. **α_k (Prop. 2.7).** Both formulas give 1, −1/3, 1/15, −4/315, 1/315, −4/3465: the Bernoulli-polynomial form and the μ_j form of Appendix B. Every term has the sign (−1)^k, as claimed.
3. **Formula (10) and the minimal pair.**
   - (10) holds, and so does c_2 = (S_1+R−2)/12.
   - For O(2,8,8) and O(3,3,12): c_1 = 1/8 and c_2 = 67/48 for both. c_3 = −1601/480 and −867/160 respectively.
   - d_3 = 25/12, d_4 = −1775/24, d_5 = 153025/48: all as stated (p. 27; Suppl. S4).
4. **Proposition 6.1 and the amplification constants.**
   - F has diagonal −1/2, 1/12, −1/360, 1/2520, −1/10080.
   - The row sums of |F^{-1}| are amp_0..4 = 2, 14, 498, 4062, 56230/3, and P_3 = −18c̃_1 − 120c̃_2 − 360c̃_3, as stated (p. 34).
   - The constants 14 and 498 in Prop. 6.4 follow.
5. **Prop. 2.11.**
   - Π_2, Π_3 and Π_4 have the closed forms implied by (ii)–(iv); checked numerically for m = 2, 3, 5, 7, 12.
   - The Δ²K coefficient in (iv) equals Π_4(m), consistent with (iii) at l = 3.
   - The m⁷ coefficients of (iv) match |B_8|/8!·β_{3,4} with β_{3,4} = 120K³ − 42KΔK + Δ²K.
   - β_{1,2} and β_{2,3} match p_1 and p_2.
   - 2Π_3(m)(−Δ)K reproduces Schueth's full ΔK coefficient in [20, Thm 4.1], including the −191/(30240m) constant term.
   - The formula β_{l,l+1} = 4^l l! [v^{2l}](J^{-1})′(v) gives (2l)!/l! K^l at constant curvature.
   - The second-order Duhamel constant ω_n of Prop. 2.12(ii) agrees with the classical a_2 density K²/15 at n = 2. I did not verify other n.
6. **Theorem B.**
   - The linear system (12) was built symbolically for m = (3,5), (2,8,8), (2,3,7), (3,10,15,30), (2,2,3,5) and (2,3,4,5,7).
   - det M equals ς_n ∏_{i<j}(m_i+m_j)/∏m_i exactly, including the sign ς_n = (−1)^{n(n+1)/2}.
   - In every case the system returns the true e.
7. **Theorem C(3).** The values R, P_1, P_3 and P_5 for both pairs are as stated.
8. **All explicit pairs.**
   - Every pair printed in the paper agrees with the stated area and has exactly the stated number L of shared invariants (Lemma 3.3 criterion). This covers Example 3.6, Example 3.17(i)–(ii), Thm 1.2(ii), the Thm 3.8 examples for M = 3, 4 and (iv) for M = 2, X = 4, the surfaces (2;) / (0;2⁸), the pair (0;2⁵) / (1;2), and (0;5,5,5) / (0;2,2,2,10).
   - The same holds for all 21 pairs of Table S1 whose cone lists are printed. These are the genus, equal-count and cone-count rows for L = 2..7, and the Prouhet rows for L = 2, 3. This includes the 30–40-digit orders and the exact s values for L = 4, 5.
9. **Theorem 3.8.**
   - C, ν, s and the least-g areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054} for M = 2..9 are all as stated (p. 19).
   - Each pair shares exactly M−1 invariants.
   - (iv) also checks for (M,X) = (3,4), (3,7), (4,6): each pair shares exactly M invariants, X lies in m′, and the orders of m are at most M.
10. **Section 5.**
    - Table S3: there are 83 hyperbolic triads with 10 ≤ S ≤ 18, with the only coincidence at S = 18.
    - Table S2: x*(p), S*(p) and the first collision sums and pairs agree for all p ≤ 14.
    - Theorem 5.4: gap_p(3p+7) = −2(p²−5p−30)/(p(p+1)(p+3)(p+4)(p+5)) for p ≤ 11. The odd gaps are 1/840, 1/2310, 1/10296, and the gaps at S*(p)+1 are as printed.
    - Lemma 5.3, (15), x*(p) − 18 = 3(p−2)(p−3)/(p−1) and the φ_p′ factorisation were checked by hand.
    - Prop. S2.1: the collision-free sums in [18, 600] are exactly the 38 listed (all of them are ≤ 557). S = 557 has 25 575 triads. I did not run the range 600–4800.
11. **Theorem 5.8.**
    - ψ maps E into C_{27/2}, and φ∘ψ = id on E (symbolic remainder).
    - The values of φ at the twelve points are as stated.
    - PARI: disc(E) = 2^18 3^8 5^6; E(Q)_tors ≅ Z/2 × Z/6, generated by (−24,360) and (0,0); #E(F_7) = #E(F_11) = 12; ellrank returns [0,0].
    - The flex (16,400) with tangent y = 21x + 64 checks, since x³+393x²+3456x − (21x+64)² = (x−16)³.
    - I re-derived every local step of the hand 2-isogeny descent in Section S7. This covers the mod-5 non-residue argument on E and the mod-3 / mod-9 arguments for d_1 = 3, 5, 15 on E′. The Selmer groups are {±1, ±6} and {1}, and the rank is 0.
12. **Stability (Section S3).**
    - The series sech²U for (2,2,2,2,3) is 1 − 121z² + 9328z⁴ − 601472z⁶, and ζ_3, ζ_4, ζ_5 = 1, 79/3, 14048/15.
    - From Theorems S3.2–S3.4 I recomputed δ_thm for (2,8,8), (3,3,12), (2,3,7), (4,4,4), (7,7,7), (3,10,15,30) and (2,2,2,3). All match Table S4 to the printed digits (rounded down).
    - The ratio column and the δ_cert/|c_j| columns are consistent with the printed δ's; see m14 for a rounding remark.
    - I hand-checked the logic of Lemma S3.1, Theorem S3.2(a)(b), the Rouché step of Theorem S3.3 and the third term of δ_thm.
    - I did not recompute δ_cert (Proposition S3.5).
13. **Table S6 (blind recovery).** Solving the n = 3 system from the printed estimates reproduces the stated roots: 2, 8 ± 0.00502i for A, and 2.99154, 3.00851, 11.99995 for B.
14. **Hand-checked proofs.** Lemma 2.4, Lemma 2.5 and (3), Theorem 4.2, Lemma B.1, Proposition B.2 and the proof of Prop. 2.7 were checked line by line. This includes the Euler beta integral, the moments of r/(e^{2πr}+1), the range condition t ≤ ℓ²/(2(1+ℓ)) and the inequality 1 + 2t/(ℓ−t) ≤ (2+3ℓ)/(2+ℓ). So were the following, all of which I found correct:
    - Lemma 3.1, Theorems A, 3.4 and 3.11 (the Descartes counting), Lemma 3.7 and Theorem 3.8(i)–(iv);
    - Corollaries 3.5 and 3.9, Proposition 3.12, Theorem 3.13, Lemma A.1, Proposition A.2 and Theorem 3.14(a)–(d);
    - Proposition 3.15, including the two equivalences;
    - Corollary 4.1 and Corollary 5.1.
15. **Area classes behind Figure 3.** I reproduced the enumeration independently, with a fresh exact enumerator.
    - It finds 525 areas 2πs with s ≤ 7/5, attained by genus ≤ 1, at most four cone points and orders ≤ 12.
    - The classes contain 33 946 signatures in total, and 504 classes contain orders above 12.
    - The class maxima of K_mult are 1 for 17 classes, 2 for 311 and 3 for 197. The first class with maximum 3 is s = 1/4.
    - All of this exactly as stated in Suppl. S1.

### B. Citations checked (bibliographic data via Crossref / zbMATH / DataCite / Zenodo, and statement-level content)

All DOIs resolve to the cited items, with correct authors, title, journal, volume, issue, pages and year. Outcomes are listed by item. "OK" means the pinpoint (theorem, equation, page) says what it is cited for. Where only an arXiv version was available, published numbering is unconfirmed.

- **[1] Donnelly 1976:** bibliographic data OK; paywalled, full text not read. It is a manifold/isometry fixed-point expansion. The orbifold locality cited to "[1], [2, Thm 4.8]" is due to Donnelly, Illinois J. Math. 23 (1979) and DGGW Thm 4.8 (DGGW Rem. 4.10). See m1.
- **[2] DGGW 2008** (arXiv 0805.3148):
  - Thm 4.8, §§4.1–4.2, Ex. 5.3, Prop. 5.5, (5.7), Ex. 5.6, (5.10) and Thms 5.14–5.15: OK. Thm 5.15 is for orientable orbifolds, which matches the paper's class.
  - The Rem. 5.16 quotation is verbatim. However, DGGW's invariant c is 12 times the degree-zero coefficient, a single heat invariant. "Encodes exactly the first two" is true on triangle orbifolds only because c_2 determines (S_1, R) and hence c_1 (see m2).
- **[3] Borwein–Ingalls 1994:** §2 p. 6 (N(k)), Props. 2–3, §3, p. 7 (Wright and Melzak), and §6 Problem 3 with the verbatim "for many years" (p. 26): OK. The Letac/Gloden attribution is on p. 10, not p. 9; p. 25 lists sets without attribution (m3).
- **[4] Dryden–Strohmaier 2009** (arXiv): Thm 1.1, Prop. 3.3, eq. (1) and the cone-point classes: OK. Thm 3.2 is Gauss–Bonnet, ∫K = 2πχ; the area formula needs K = −1 (harmless). Their trace formula is stated for h entire of uniform exponential type with ĝ compactly supported, which is equivalent to the paper's wording.
- **[5] Doyle–Rossetti, NYJM 2008:** bibliographic data OK. The theorem is for surfaces; orbifolds get only an unproved comment in §6. "Proved independently by Doyle and Rossetti [5]" should point to [18] (m4).
- **[6] Linowitz–Voight:** Thm A and the following sentence (signature (0;2,2,2,2,2,3,4)): OK.
- **[8] Cheeger (4.42):** could not read (Project Euclid blocks headless access). Secondary sources (Aldana–Kirsten–Rowlett) confirm that (4.42) is the cone term.
- **[9] Bordag–Kirsten–Dowker (6.4):** OK.
- **[10] Dowker 1977:** bibliographic data OK; the coefficient could not be located (paywalled). Please give an equation number.
- **[11], [15], [16], [17], [22], [23], [37], [38], [41], [42], [44], [49], [51], [52]:** bibliographic data OK; [17] content OK. Minor: [49] and [39] omit issue numbers.
- **[12] Nursultanov–Rowlett–Sher, Rem. 6.6:** OK.
- **[13] Uçar thesis:**
  - Thm 4.20(ii), (4.33)–(4.35), Cors. 4.21(iv) and 4.23, Thm 3.40, W_ν and the verbatim "we conclude by induction…" quote: OK. (4.34) belongs to Cor. 4.19.
  - Thm 3.40 and its proof occupy printed pp. 98–99, not "pp. 98–103"; printed p. 98 is PDF p. 103 (m5).
- **[14] Stanhope 2005:** Main Thms 1–2 are finiteness and bounds under curvature lower bounds, not determination by the spectrum. Rephrase where it is listed among "data heard by heat or by the spectrum" (m6).
- **[18] Doyle–Rossetti arXiv v2:** OK.
- **[19] Abreu et al.:** Thm 1 and §6.1: OK.
- **[20] Schueth 2019:** Rem. 3.2, Thm 3.7 (with its z-substitution), Thm 4.1 (−(1/15120)k⁵ΔK with Δ = −div grad, the same convention as the paper) and Rem. 4.2: OK.
- **[21] Schueth 2026:** p. 2 statement OK (arXiv 2511.22255); the published page was not accessible.
- **[24] Grieser–Maronna Thm 1:** OK.
- **[25] Chang–DeTurck:** content confirmed via zbMATH; the theorem number "Thm 1" could not be checked (AMS PDF blocked).
- **[26] Steinig:** bibliographic data OK (Zbl 0238.10007); content only second-hand.
- **[27] Laurens Lemma 3.2** and **[28] Melánová–Sturmfels–Winter Prop. 24:** OK (arXiv numbering).
- **[29] Korobov–Bugaevskaya §3 (Thm 3.1):** OK. It appeared online in 2015 and in the 2016 issue.
- **[30] Chen survey:**
  - §A.5.8, (A.685)–(A.692) (computer search, 2017), Identity 9 with (3.27)–(3.28), (3.33), §8.1 P1 and A.1.6, A.1.17, A.1.26: OK.
  - A.1.33: the first solution, (A.313), is Chen's own from 2000; only (A.314)–(A.316) are Wróblewski's (2009).
  - The L = 6 genus piece in Table S1, B = [7,91,173,269,289,323] = [29,59,193,247,311,313], is (A.313). So "the last found by Wróblewski in 2009" is partly wrong (m7).
- **[31] Philippe GD 2010:** confirmed via [32]. **[32] Thm 3.1:** OK (verbatim).
- **[33] Bremner–Guy–Nowakowski p. 117:** equation for integer n and the reciprocal-pair remark: OK. The last two pages were not recoverable.
- **[35] Thurston Ch. 13:** 13.3.5–13.3.6: OK. "13.3.4" labels both a proposition and a displayed formula. Cor. 13.3.7 gives dimension −3χ(X_O)+2k+l, which specialises to 6g−6+2n (m8).
- **[36] Garbin–Jorgenson:** Rems. 2.6–2.7 and (2.8) normalisation: OK. Rem. 2.7 does not say that heat invariants do not see the moduli, and neither does [50] explicitly (m9).
- **[39] Watson:** bibliographic data OK. Uçar notes that Watson's lune formulas contain inaccuracies and gives corrected versions; cite those if Watson is used quantitatively.
- **[40] Holtz–Tyaglov:** (1.37) and Thm 1.17: OK (arXiv v3). The sign is (−1)^{n(n−1)/2} for monic p, consistent with the paper's use.
- **[43] Hua Ch. 18** and **[45] Borwein Ch. 11:** OK.
- **[46] Coppersmith et al.** (5) and "ideal solutions known for k ≤ 9, k = 11": OK. [46] does not state that N(k) = k+1 for all k is open; [47] does (m3).
- **[47] Croot–Mao–Yip** arXiv:2609.05061v1 (4 Sep 2026), §1: OK (their notation is P(k,2)).
- **[48] Borwein–Lisoněk–Percival:** p. 2064 has Gloden only; Letac is on pp. 2065 and 2069 (m3).
- **[50] Dryden 2004**, proof of Thm 4.5: the t^{-1/2}e^{-ℓ²/4t} form is OK.
- **[53] PARI 2.17.2:** release announcement dated 5 March 2025: OK.
- **[54] Cremona:** §3.3 p. 70 (injectivity of torsion reduction at odd good primes) and §3.6 Method 1 with (3.6.2): OK.
- **[55] Crameri:** Zenodo 8409685 is v8.0.1 (2023): OK.
- **Supplement references:**
  - Ostrowski: parts and DOIs in the correct order; Théorème XXX and (71,1) are on p. 212 of the second part.
  - Schöberl and ARPACK: OK.
  - Strohmaier–Uski §7.1 with the ancillary file: I count exactly 42 multiplicity-one eigenvalues below 998, as claimed.
- **[7] and [34]** (the companion manuscripts) are not publicly posted. The paper states that no proof depends on them, and I confirmed this.

### C. Figures checked (all against rendered pages)

- **Fig. 1.**
  - The colour bar is logarithmic from 1 to 12. Mapping each pixel of the two embedded rasters back onto the colour bar gives maxima of about 8.1 in (a) and about 11.3 in (b). This is consistent with the claim that 4πt h_t(x,x) approaches the cone order (8 and 12).
  - The smooth interior is about 1.
  - The colour map is monotone in lightness, so it survives greyscale.
- **Fig. 2.** The disc and ring sets agree with X* for both pairs: (2,8,8) against (3,3,12), and (1;15) against (0;3,3,5,5) with one padding 1. See m10.
- **Fig. 3.**
  - The solid step curve is ⌊2s⌋+4, and the dashed curve is ⌊√((s−1)/3)⌋+2 from s = 4 on; tick positions agree.
  - All diamonds and squares sit at the (s, L+1) of the Table S1 pairs.
  - The dots reproduce my independent class enumeration (item A15). See m11.
- **Fig. 4.**
  - The square-root scale was checked at the pixel level: ticks 1, 5, 10, 20, 40 and 100 fall at √λ positions within 1 px.
  - The heavy λ_1 runs from about 4.1 to about 0.43, matching S6.
  - The systoles 4b(ϑ) = 4 asinh(√(e^{−ϑ}/2)) give 2.634 → 0.694, as stated.
- **Fig. 5.**
  - (a) The grey truncations behave as d_3, d_4, d_5 predict: d_3t + d_4t² peaks at 0.0147 at t = 0.0141 and vanishes at t = 0.0282. D(t) changes sign near 0.33, consistent with "0.34" in S4.
  - (b) The emergence circles agree with t* = ℓ²/(4·24.5): about 0.0049 for ϑ = 2.8 (ℓ = 0.694) and about 0.050 for ϑ = 0.4 (ℓ = 2.208). Darker shades correspond to shorter systoles.
  - See m12.
- **Fig. 6.** Both triangles have area π/4. The colour coding (teal for O(2,8,8), orange for O(3,3,12)) is consistent with Figs. 2, 3 and 7. I could not verify the projection geometry itself.
- **Fig. 7.**
  - The dots sit at S*(p) for p = 2..7, at R = R^-_{S,p}: (19, 0.583), (23, 0.422), (26, 0.367), (29, 0.325).
  - The circles sit at the first collisions of Table S2: (20, 1/2), (38, 19/42), (34, 0.310), (62, 0.221), (117, 0.244).
  - Dot and circle coincide only for p = 2 and p = 4.
- **Fig. 8.**
  - The slopes are 1, 1/2, 1/3 and 1/2 over 12 decades.
  - The diamonds sit at δ_cert = 3.658e−3, 2.341e−3 and 4.539e−4.
  - The (4,4,4) diamond meets the rounding line, which is "nearly sharp" as stated.

### D. Not checked

- The numerical spectra and fits of S4–S6 (no data were provided to me; the paper correctly labels these as illustrations used in no proof).
- δ_cert (Proposition S3.5).
- The computer searches of Remark 3.2, Remark 3.18 and S1.
- Prop. S2.1 beyond S = 600.
- Prop. 2.11(iv) beyond the consistency checks in A5.
- The published-version numbering of arXiv-checked references.

## MAJOR issues

**M1 (Abstract, p. 1, versus Theorem 1.1(ii), p. 3, and the sentence after it): the abstract overstates the growth equivalence.**

The abstract says f grows "like a power A^α of the area exactly when the Prouhet–Tarry–Escott function satisfies N(k) = O(k^{1/α})". Theorem 1.1(ii) proves less: the *lower bound* f(A) ≥ cA^α is equivalent to N(k) = O(k^{1/α}), while the upper bound needs the separate hypothesis N(k) ≥ ck^{1/α}.

Read literally, the abstract is false given known results. N(k) = O(k²) is known (Borwein–Ingalls Prop. 3), so the abstract would assert that f grows like A^{1/2}. But N(k) = O(k²) is also consistent with f = Θ(A), which is open. The paper itself says on p. 3: "Whether f grows like a power of A at all is open."

The abstract is the claim of record and must match Theorem 1.1(ii).

**M2 (Section 2.4, pp. 11–14; also Section 1, p. 3; and Problem 5): two Propositions rest on sketches only.**

Proposition 2.11 (i)–(iv) and Proposition 2.12 (ii)–(iii) are stated as Propositions, but each is followed by "Sketch", not "Proof". In detail:
- **2.11(i).** The key boundedness claim, that (2 sin(ϑ/2))^{2l+2}B_l stays bounded, is justified by "following the substitution … of Schueth's proof … to all orders".
- **2.11(iv).** This is "an exact computation" whose method (transport equations, then Laplace's method) is named but not given. It is "confirmed" by an unpublished second computation.
- **2.11(ii).** The notation [v^{2l}](J^{-1})′(v) and "the corresponding average over directions" are not defined.
- **2.12(ii).** The second-order Duhamel constant ω_n is asserted without derivation; I could confirm it only at n = 2.
- **2.12(iii).** The gluing is described in two sentences.

These statements are not peripheral decoration. The Introduction (p. 3) uses 2.12(iii) to assert that "the setting of constant curvature is essential: the minimal pair … also carries metrics … whose heat expansions agree to all orders". The end of Section 2.4 draws a general conclusion ("heat invariants of any finite order hear only c_2"), and Problem 5 builds on both.

My consistency checks (A5) give me no reason to doubt the formulas. But a journal Proposition needs a proof that a reader can check.

**M3 (Section 1.2, Sections 2–4 and the supplement): several pinpoint citations do not say what they are cited for.**

The bibliographic data is very clean, so these stand out. None affects a proof, but together they misattribute results or send readers to the wrong page. Details are in Section B; the fixes are minor items m1–m9:
- **Doyle–Rossetti [5].** The orbifold statement is a remark in [5]; the proof is in [18].
- **Locality of the orbifold heat expansion.** This should be credited to Donnelly 1979 and DGGW Thm 4.8, not Donnelly 1976.
- **DGGW's invariant c.** It is a single invariant, 12 times the degree-zero coefficient.
- **"Heat invariants do not see the moduli".** Garbin–Jorgenson Rem. 2.7 does not say this.
- **Stanhope [14].** It proves bounds, not determination.
- **Page pinpoints.** Uçar is pp. 98–99, not 98–103; Borwein–Ingalls is p. 10, not p. 9; [48] has Letac on p. 2069, not p. 2064.
- **Openness of N(k) = k+1.** This should be credited to [47], not [46].
- **Wróblewski attribution.** It is wrong for (A.313), which is used in Table S1.

## MINOR issues

- **m1 (p. 5, l. "The heat expansion of an orbifold is local … [1], [2, Thm 4.8]"; also p. 11).** [1] (1976) is the fixed-point expansion for isometries of manifolds. For orbifolds, cite Donnelly, Illinois J. Math. 23 (1979) 485–496 alongside DGGW Thm 4.8.
- **m2 (p. 6, "the invariant c … encodes exactly the first two heat invariants").** DGGW define c as 12 times the t⁰ coefficient (their (5.13)), that is 12c_2. Say that c = 12c_2, and that on triangle orbifolds c_2 already determines c_1 (as the paper itself notes on p. 28).
- **m3 (p. 23 and p. 22).** Change the following pinpoints:
  - "[3, pp. 9, 25]" → "[3, pp. 9–10]", since the attribution to Letac and Gloden is on p. 10.
  - "[48, p. 2064]" → "[48, pp. 2064, 2069]".
  - Attribute the openness of "N(k) = k+1 for all k" to [47, §1]; [46] gives only the known range.
- **m4 (p. 5, "proved independently by Doyle and Rossetti [5]").** [5] treats surfaces; its §6 only remarks on orbifolds. Cite [18], or say "announced in [5, §6] and proved in [18]".
- **m5 (p. 10, "[13, Thm 3.40 and its proof, pp. 98–103]").** The theorem and proof are on printed pp. 98–99. Use one page numbering consistently.
- **m6 (p. 5, "isotropy types and the number of singular points [14, Main Thms 1–2]").** These are finiteness and bound results under curvature hypotheses. Rephrase, e.g. "spectral bounds on …".
- **m7 (p. 23, "the last found by Wróblewski in 2009 according to that survey").** The L = 6 genus piece B is Chen's (A.313) (2000). Only (A.314)–(A.315), used in the equal-count L = 6 pair, are Wróblewski's. Cite equation numbers.
- **m8 (p. 7 and p. 25, Thurston [35]).** Specify "Prop. 13.3.4" or "formula 13.3.4". Say that Cor. 13.3.7 gives the dimension −3χ(X_O)+2k+l, which specialises to 6g−6+2n.
- **m9 (p. 25, "classical in substance [37, 49], [36, Rem. 2.7], [50, proof of Thm 4.5]").** Neither [36, Rem. 2.7] nor [50] states this. They give the trace formula from which it follows. Rephrase as "follows from".
- **m10 (Fig. 2, p. 18).** By the definition in Theorem 3.4, X* is empty for an orbifold against itself, after removing common elements. The lower row of (a) therefore draws X, not X*; say so. The colour key (teal for (2,8,8), orange for (3,3,12)) is not in the caption, and (b) switches to black/grey without explanation.
- **m11 (Fig. 3, p. 24, and its description on pp. 23–24).** Each constructed pair is "drawn at K_mult = L+1". A pair sharing exactly L invariants only shows K_mult ≥ L+1, since a third orbifold could share more. Call the diamonds and squares lower bounds in the caption. The caption also does not explain the markers (dots, split disc, diamonds, squares, line styles); currently this is only in the text.
- **m12 (Fig. 5, p. 28).** There is no legend, and the caption identifies neither the three grey truncation curves nor the dashed cone-point term in (a). In (b), the caption does not say what the shading is, and the text's "ten times the error budget (shaded)" is ambiguous (is the shading the budget, or ten times it?). Panel (a) also has no x-axis label of its own.
- **m13 (Fig. 1, p. 2, "h_t is the heat kernel computed on the true hyperbolic triangle").** This is ambiguous: it could mean the Neumann kernel or the Dirichlet kernel of T. The quantity plotted, approaching m at a vertex and 1 inside, is the orbifold kernel, ½(h^N + h^D) on T. Say so.
- **m14 (Table S4 caption, Suppl. p. 11: "δ_up is rounded up, every other entry down").** The ratio column is not rounded down. For example, (3,3,12) gives 4.589e−3/4.040e−3 = 1.1359 from the printed bounds, and the true ratio is no larger, yet 1.14 is printed. The same happens with 2.05 (2.046), 1.25 (1.245), 1.03 (1.025), 1.06 (1.058), 1.36 (1.356) and 6.72 (6.717). Either round down or amend the caption. The main text's "1.03–6.72" (p. 35) inherits this.
- **m15 (Suppl. p. 7, "Proposition S2.1, moved here from the paper,").** This is an editorial leftover; delete "moved here from the paper".
- **m16 (Theorem 3.8, pp. 18–19).** (ii) defines ν(a) = C a w_a, while (iv) redefines ν(a) = −C a w_a, "as in (ii)". State the sign change explicitly, or use a different letter.
- **m17 (Prop. S2.2 proof, Suppl. p. 7).** For odd parity the argument needs the gap never to vanish *at an integer*. This follows because the gap is positive at every odd-parity sum below x*(p) and negative from S*(p)+1 on (Theorem 5.4(b), (d)). Say this; "positive at the last odd-parity sum below its zero and negative at the next" is circular as written.
- **m18 (p. 25, Fig. 4(a)).** At 160 dpi the four raster panels show faint off-white rectangles around the shapes. Use transparent backgrounds.
- **m19 (pp. 4 and 34).** "Hölder of exponent 1/k at k-fold orders" sits next to dist(m, m′) = min_π max_i, while Fig. 8 plots ‖m̃ − m‖_∞. State that the plotted norm is the matched one.
- **m20 (references).** Add the issue number to [39] (No. 1) and [49] (No. 3). Give an equation number for [10], or drop it in favour of [9] and [12].
- **m21 (p. 34, Prop. 6.3(i)).** "δR = s²/(4(64 − s²))" holds for the double order a = 8 of (2,8,8). Name a = 8 explicitly; the general family is written (a+s, a−s, m_3, …).

## Presentation (figures, captions, notation, exposition; not length)

- **Captions.** Captions are terse throughout. Several figures (2, 3, 5, 7, 8) rely entirely on the body text to identify markers, line styles and shading. Springer's guidelines ask for self-contained captions. Adding one sentence per figure listing the encodings would fix this (see m10–m12).
- **Colour.** Colour use is consistent across the paper: teal for O(2,8,8) and orange for O(3,3,12) in Figs. 2, 3, 6 and 7, and the Crameri colour maps. Every figure I checked stays readable in greyscale. The exception is Fig. 7, where seven grey bands overlap and are hard to tell apart. Labelling the bands p = 2, …, 8 at their right ends would help.
- **Overloaded symbols.** These should be disambiguated or listed in Table 1:
  - φ / ϕ: ϕ_k(m), ϕ in Lemma 2.5, φ_p in §5.1, and the map φ in Thm 5.8;
  - ψ: ψ_k, the test function in Lemma B.1, and the map ψ in Thm 5.8;
  - ϱ: the reciprocal sum ϱ(P), the cutoff parameter in Lemma B.1, and the remainder ϱ(t) in Prop. B.2;
  - χ: the Euler characteristic and the polynomial χ_m;
  - R: the reciprocal sum and the rotation in §2.4;
  - σ: the signature and the coefficients σ_i of u/sin u;
  - C: several different constants;
  - e: the coprime integer e in S7 and the e_k.
- **Redundant notation.** S_1 = P_1 is redundant; one symbol would do.
- **Undefined notation (§2.4).** The coefficient-extraction notation [v^{2l}] and J^{-1} need definitions (see M2).
- **Exposition.** The exposition is otherwise precise and economical. The organisation paragraph (p. 6) and Table 1 are helpful. The repeated, explicit separation between what is proved, what is computer-checked, and what is numerical illustration (Sections 4, S4–S6, S8) is exemplary.

## Recommendation

**Minor revision** (confidence: fairly high, about 0.8).

The main theorems are correct as far as I could test them, and I tested a great deal:
- Theorems A, B, C, 3.4, 3.8, 3.11 and 3.14, and Proposition 3.15;
- Section 5 with Theorem 5.8 (including the hand descent);
- the stability constants;
- every printed explicit pair;
- the complete area-class data behind Figure 3.

The figures agree with their data, and the bibliographic data is accurate.

What needs fixing:
- the misstatement in the abstract (M1);
- the status of the Section 2.4 Propositions (M2);
- a set of attribution and pinpoint errors (M3, m1–m9).

I did not classify the revision as major because M1 and M3 are local fixes, and M2 can be resolved either way described below. Should the authors keep Prop. 2.11 and 2.12 as Propositions, I would want to see the full proofs before acceptance.

## What resolves each issue

- **M1:** Rewrite the abstract sentence to match Thm 1.1(ii). For example: "f(A) ≥ cA^α for large A exactly when N(k) = O(k^{1/α})". Optionally add "and f(A) = O(A^α) when N(k) ≥ ck^{1/α}".
- **M2:** Do one of the following.
  - (a) Supply complete proofs of Prop. 2.11(i)–(iv) and 2.12(ii)–(iii), with the derivation of ω_n and the computation behind (iv), possibly in the supplement. Define [v^{2l}], J^{-1} and the directional average.
  - (b) Relabel them as Claims or Remarks with sketches, state that nothing else in the paper depends on them, and soften the Introduction's sentence on p. 3 accordingly.
- **M3:** Apply m1–m9.
- **m1–m9:** Correct the attributions and pinpoints exactly as listed.
- **m10–m13, m18:** Revise the captions and figure details as listed.
- **m14:** Round the ratio column down, or change the caption, and update "1.03–6.72" if needed.
- **m15–m17, m19–m21:** Make the editorial and textual corrections as listed.
