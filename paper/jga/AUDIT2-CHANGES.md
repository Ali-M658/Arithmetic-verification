# AUDIT2-CHANGES: disposition of every G5-bis (audit-2) required change

Source: `review/audit-2/VERDICT.md` ("Required changes") and `REGISTER-ADDENDUM.md` (rows A1-H11).
Locations refer to the rebuilt `manuscript.pdf` (35 pp.) and `supplement.pdf`. Results of
`theory/pte/proof.md` that the paper does not state (Theorem 3.1 in general, Proposition 2.3,
Lemma 1.5(3), N_odd, tau_L, T^cone_L) are marked NOT USED: the corresponding wording fix is
moot for the paper and stays a task for `theory/pte`.

## SERIOUS

| # | required change | status | where |
|---|---|---|---|
| [x] 1 | L-configuration dictionary must carry the genus condition iota(Z) = 2(g'-g) | DONE | Section 3.3, paragraph after Definition 3.7: "share their first L heat invariants exactly when Z = U* + (-V*) is an L-configuration with imbalance iota(Z) = 2(g'-g)"; the definition of iota carries no "= 2(g'-g)". |
| [x] 2 | delete "previously the smallest area ... 2 pi 14/5" | DONE | Example 3.12(i) uses the audit's sentence: "This is the n = 4 witness of Theorem C(3). Its area is less than that of the smallest genus-changing pair sharing three invariants found here, (1;15,15,15) and (0;3,3,5,7,7,21), of area 2 pi 14/5." |
| [x] 3 | n = 4 witnesses are not a pencil phenomenon; pencil counts exact | DONE | Remark 3.2: the pencil construction is described as one source of witnesses; counts "15 ... at most 130 and 35 ... at most 220 (25 and 61 if only three entries of A = {a,b,c,-(a+b+c)} are bounded)"; "Not every witness arises in this way: among the 107 primitive witnesses with all orders at most 440, 6 admit no pencil splitting, the smallest (0;16,16,74,74) and (0;11,37,44,88), R = 45/296, P_1 = 180, P_3 = 818640". The "unproved converse" of proof.md section 7 is not in the paper. |
| [x] 4 | Wright/Melzak: Melzak's (n^2+4)/2 as he reports Wright; never the k^2-3, k^2-4 formula | DONE | Paragraph before Theorem 3.11: pigeonhole bound [BI Props 2-3], credited by Melzak to Hardy and Wright [p. 233]; Wright (1935) N(k) <= (k^2+4)/2 as reported by Melzak [p. 234]; Melzak's exact formula and Table 1 (k <= 29); none is o(k^2); open [BI s. 6 Problem 3], [Croot-Mao-Yip]. The (k^2-3)/2, (k^2-4)/2 formula appears nowhere. |

## Changed constants and printed values

| item | status | where |
|---|---|---|
| [x] stability table (2,2,2,2,3): delta_up 5.312e-05, ratio 6.72 | DONE | Table 1 (generated from `theory/stability/threshold_results.json`); text "6.72 for n = 5". |
| [x] (3,10,15,30) delta_up 7.487e-03 (optional) | DONE | Table 1 prints 7.487e-3. |
| [x] (2,3,7), nu = 0 relative precision 3.9e-03 | DONE | Table 1 now has the column delta_cert/abs(c_j), rounded down from the printed delta_cert: (2,3,7) reads 3.0e-1, 3.9e-3, 2.7e-3. |
| [x] "at most four nonzero (odd) coefficients" | DONE | After Proposition 6.9: odd series at most four (z, z^3, z^5, z^7), even series sech^2 U and sec^2 U at most four (1, ..., z^6); example sech^2 U = 1 - 121 z^2 + 9328 z^4 - 601472 z^6 for (2,2,2,2,3). No "(odd)" for sech^2 U. |
| [x] pencil counts | DONE | Remark 3.2, as in SERIOUS 3. |
| [x] n = 5 pencil check "1,592 sets" | NOT USED | The n = 5 pencil search is not stated in the paper (only the exhaustive n = 5 search with orders <= 120). |
| [x] Theorem 4.2: L >= 2 in (a), beta > 0 in (b) | DONE | Theorem 3.11(b) "If L >= 2 and f(A) >= L+1"; (c) "If beta > 0 and N(k) <= C k^beta". |
| [x] Proposition 3.2: n >= 1 | DONE | Proposition A.2 (Shift): "n >= 1"; used in proof (3). |
| [x] Theorem 5.16 / triads: every integer k >= 1 | DONE | Theorem 1.2(iv) and Theorem 5.10: "for every integer k >= 1"; proof: hyperbolic since R < 1 and all entries >= 2k >= 2. |
| [x] Theorem 4.3: f_g, f_n defined, explicit constants | DONE | Definitions before Theorem 3.11; Theorem 3.11(e): f_g(A) >= sqrt(A/16 pi) for A >= 16 pi, f_n(A) >= sqrt(A/12 pi) for A >= 8 pi; proof in Appendix A. |

## MINOR wording changes

| group | status | where |
|---|---|---|
| [x] Proposition 3.3 (doubling): counts 3n - mu_X, 3n - mu_Y; shares first L; area via abs(V) = 3n | DONE | Proposition 3.9 states exactly that, with "every 1 removed"; proof uses abs(U) = abs(V) = 3n. |
| [x] Theorem 3.4 (T^cone, cancellation, [Sig] N(a) citation) | DONE / NOT USED | The paper uses only the T_L and cone-count constructions inside the proof of Theorem 3.11(e) (common elements cancelled; the uncancelled doubling pair is the realisation, hyperbolic by Proposition 3.9). T^cone_L and the 2^{2L-1} citation are not in the paper. |
| [x] Theorem 3.1 (pencil) "Equivalently" clause | NOT USED | Only the m = 4 pencil is used (Remark 3.2), stated directly by e_1 = 0 and equal e_3, e_4 with a two-line proof. |
| [x] Lemma 1.2: remove every 1; genus choice | DONE | Section 3.3: "with U = Z_{>0}, V = -Z_{<0} and all entries 1 removed ... once the genera are large enough to be hyperbolic (one condition)". |
| [x] Theorem 2.1 equality wording; Proposition (balanced) 0 not in A | DONE / NOT USED | Theorem 3.8: "if abs(U*)+abs(V*) = 2L+2, the least size ..., then abs(g-g') = 1 and {abs(U*),abs(V*)} = {L, L+2}". Proposition 2.3 is not in the paper. |
| [x] Lemma 1.5 (N_odd at L = 2, 7) | NOT USED | N_odd is not used; Lemma A.1 gives only the pigeonhole bounds. |
| [x] Remark first open case ("scaled to coprime integers", "nonempty open set") | DONE | Remark 3.13, audit wording, with the example {1,1,1,1,7}. |
| [x] Improved lower bounds on f | DONE | Example 3.12, last sentence: f(A) >= L+1 for A/2pi >= 2L-3, 2 <= L <= 5, and A/2pi >= 10, 18 for L = 6, 7; the "grows at least linearly for A/2pi <= 18" sentence is absent. |
| [x] Trace formula: systole over all hyperbolic classes | DONE | Section 2.1 definition; Theorem 4.4. |
| [x] Trace formula: hyperbolic-term lemma proof and monotonicity | DONE | Lemma 2.6 with proof and the monotonicity (B decreasing in l, increasing in D on the range); used in Theorem 4.4(b). |
| [x] Schueth sentence (a_0, a_1 from DGGW 5.6; a_2 hers; b_l = (-1)^l p_l/m) | DONE | After Lemma 2.9: audit replacement sentence. |
| [x] Ucar citation: Thm 4.20(ii) with (4.33)-(4.34); kappa | DONE | Remark 2.10. |
| [x] Remark 4.12 wording: "independent of the coefficient computations"; no "(or Weyl's law)"; test-function class; not combined with locality.tex 1B | DONE | Remark 2.10 and Theorem 2.3 proof; Lemma 2.5 counts eigenvalues with the audit's h_T argument (no heat-kernel input), DGGW Thm 4.8 named as an alternative. |
| [x] alpha_l notation clash | DONE | Only alpha_k (per Area/4 pi) is used. |
| [x] Descent: phi at the points with Z = 0 | DONE | Theorem 5.10 proof: phi(O) = origin, phi(1:0:0) = (216, 5400), phi(0:1:0) = (216, -5400) (rechecked by sympy in this session). |
| [x] Descent: false tangent remark; (16,400) is a flex | DONE | "(16,400) is a flex, since the tangent y = 21x + 64 meets E only there, with multiplicity 3, so 2(16,400) = (16,-400) = -(16,400)" (rechecked: (21x+64)^2 - x^3 - 393x^2 - 3456x = -(x-16)^3). |
| [x] Descent: nonsingularity; rank from descent; torsion mod 7; PARI cross-check only; drop "(as far as tested)" | DONE | Proof of Theorem 5.10: genus argument gives nonsingularity; Cremona (3.6.2); #E(F_7) = #E(F_11) = 12 (rechecked); PARI is not cited at all; no "(as far as tested)". |
| [x] Stability: data radii delta_nu; first-order term; F = L | DONE | Proposition 6.9: radii delta_j; test (ii) uses sum_c delta_c sum_l abs(p_c^(l)(a)/l!) r_0^l; front-end matrix F throughout. |
| [x] Stability: eps_cert formatting | DONE | Table 1 prints eps_cert at 2 s.f. rounded down (the producer file's 4 s.f. issue is in theory/stability, not the paper). |
| [x] Theorem 5.13: first two invariants determine S_1 | DONE | Proof of Theorem 5.6. |
| [x] Abstract sharpness wording | DONE | "...the latter sharp for general data, while for the coefficients of positive real orders the sharp exponent is 1/2 at a double order and when all n >= 2 orders are equal." |
| [x] Theorem 1.4 wording | DONE | Theorem 1.3. |
| [x] Remark S3.3: d_i >= -a; max abs(d_i) <= ((498+42a^2) delta/(2a))^{1/2}; n = 1 Lipschitz | DONE | Remark 6.7. |
| [x] Literature: BI Prop. 1 not a bound; Hardy-Wright for pigeonhole; N(k) in s. 2, p. 6 | DONE | Section 1 (N(k) defined with [BI, s. 2, p. 6]); pigeonhole bound cited as [BI, Props 2-3] with Melzak's credit to Hardy-Wright; Prop. 1 cited only for the symmetric +- form (NOVELTY 1(b)). |
| [x] Literature: Chen survey type (-1,1,3,...) "no numerical solution is listed" | DONE | Remark 3.2: n = 4 witness = type (-1,1,3) solution A.685; for type (-1,1,3,5), needed for n = 5, "no numerical solution is listed there, although the survey treats the type in its identities [Ex. 2.36, (3.33)]". |
| [x] Literature: Letac via BLP p. 2069 / CMSV p. 2; Gloden | DONE | Example 3.12(iii): "Letac's two solutions of size 9 [CMSV, p. 2]". Gloden is not mentioned. |
| [x] Literature: drop "no progress on questions 3 and 4" | DONE | Problem 4 stated as settled by Wooley (2012), with Wooley 2019 Thm 13.1. The Sun-Zhao preprint is not cited (optional footnote omitted). |
| [x] Bibliography: DOIs for cmsv2024 and wooley2019; melzak1961 cited | DONE | `tools/build_bib.py` fetches cmsv2024 by DOI 10.1090/mcom/3917 and wooley2019 by DOI 10.1112/plms.12204; both printed; melzak1961 cited three times. |

## Register rows (REGISTER-ADDENDUM.md) and where they are used

| rows | in paper | where |
|---|---|---|
| A1, A7 | YES, revised | Section 3.3 dictionary paragraph |
| A2 | YES | Theorem 3.8 |
| A3 | YES | Section 3.3 (abs(Z) >= N(2L-2)) |
| A4, A5, B1 (N_odd = L part), C9 | not used | (theory/pte only) |
| A6 | YES, revised | Proposition A.2 |
| B1 (pigeonhole parts) | YES | Lemma A.1 |
| B2 | YES, revised | Proposition 3.9 |
| B3 | partly | proof of Theorem 3.11(e) (T_L <= 4N(2L-3) and the cone-count construction) |
| B4, B5, B6, B7 | YES, revised | Theorem 3.11 and Appendix A |
| C1, C2, C3, C5 | YES, revised | Examples 3.6, 3.12; F4 (all 18 pairs, assertions in figures/src/F4.py) |
| C4 | YES, revised | Remark 3.13 |
| C6, C7 | YES, revised | Remark 3.2 |
| C8 | not used | |
| D1-D10 | YES | Lemmas 2.5-2.9, Proposition 2.8, Remark 2.10, Theorem 4.4, Corollary 4.6 |
| E1-E6 | YES | Theorem 5.10 and its proof |
| E7 | moved | companion note (3P) |
| F1-F9 | YES | Proposition 6.9, Table 1 |
| G1-G3 | YES | Theorem 5.6, Proposition 5.9 |
| G4, G5 | YES | abstract, Theorem 1.3, Proposition 6.6, Remark 6.7 |
| H1-H3, H5, H7, H9, H11 | YES | Sections 1, 3.3, Remark 3.2, Example 3.12, bibliography |
| H4, H6, H8, H10 | not used | |
