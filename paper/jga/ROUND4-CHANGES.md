# ROUND4-CHANGES: Paper A ("How much of a hyperbolic orbifold does heat hear?")

Response to referee round 4 (`review/referee-round-4/VERDICT-A.md` and the reports A-a to A-e).
Item IDs are those of VERDICT-A. "Section", "Theorem" and so on refer to the revised manuscript
unless marked "old". Build and page counts: `BUILD.md`.

## Structure of the revision

| old | new |
|---|---|
| §1 Introduction (Thm 1.1 hearing the signature, Thm 1.2 rigid case, Thm 1.3 stability; §1.1 Why heat invariants; §1.2 Prior work) | §1 Introduction: physics-first motivation of the count (first two pages); §1.1 Main results led by Thm 1.1 (growth and the PTE problem), Thm 1.2 (bounded orders, M+1), Thm 1.3 (algebra of a collision: Theorems A, B and the Descartes imbalance bound), Thm 1.4 (triangle orbifolds and the isolation); Cor. 1.5 (the area bound floor(A/pi)+4 as a corollary); a paragraph on what is elementary and what is not; §1.2 Prior work and what is new |
| §2 | §2 with a notation table (Table 1) and the heat expansion with explicit enveloping remainders (eq. (Grem), Prop. B.2) |
| §3 | §3 with Theorem 3.7 upgraded (see A4); slower proofs of Theorem B and Theorem 3.4; witness and first-open-case remarks shortened, details in supplement S1 |
| §4 What heat does not hear; §7 Computations | §4 "What heat does not hear, and what it hears late": locality as a cited classical fact (one paragraph), Cor. 4.1 (moduli), Thm 4.2 (where the shape enters, attained), the two-timescales computation and the shape beyond all orders, with Fig. 4 (F6, moduli family) and Fig. 5 (F5, two timescales) interpreted in the text; error budget and methods in supplement S4-S6 |
| §6 Stability (front end, Hurwitz lemma, Thms 6.4-6.5, sharpness, Thm 6.8 delta_thm) | §6: Prop. 6.1 (front end), one stability theorem (Thm 6.2) with Fig. 8 (F8), the sharpness propositions, and the new a-posteriori Corollary 6.5; the Hurwitz lemma, Thms S2-S4 (constants, delta_thm) moved to supplement S3 |
| App. C (hand descent) | supplement Section "The rank of C_{27/2} by hand" (PARI/GP's unconditional 2-Selmer bound stays in the proof of Thm 5.8) |
| intro digressions (erratum aside, orientability paragraph, "A measured heat trace is never exact") | removed |

Every figure is kept in the paper (F1-F8). Captions stay at two short sentences; decoding is in the citing sentence.

## MAJOR items

| ID | disposition |
|---|---|
| A1 significance and fit | Introduction rewritten physics-first: the count is the number of orders of short-time diffusion during which cone points of different orders are indistinguishable; growth is carried by large orders (Thm 1.2(iii)). Headline is the PTE equivalence (Thm 1.1), the sharp bounded-order theorem (Thm 1.2), the Descartes imbalance bound and Theorem B (Thm 1.3), and the isolation (Thm 1.4(iii)); floor(A/pi)+4 is Cor. 1.5. A paragraph "What is elementary and what is not" says which results are Newton-identity or Vandermonde arguments. Conic heat-kernel literature cited in §1.2. |
| A2 length | §4 and §7 merged and shortened; §6 reduced to one theorem; δ_thm derivation, Hurwitz lemma, conditioning theorem and the hand descent moved to the supplement; intro digressions removed; T(L) heuristic deleted; witness/T3/pieces remarks compressed. Page count: see "Length" below. |
| A3 overlap with B | Paper A keeps every shared proof; Paper B now states the shared results with a disclosure table and cites A (paper/eigen/ROUND4-CHANGES.md). Paper B is cited as a companion manuscript submitted at the same time. |
| A4 Theorem 3.7(iii) superseded | **Done (mathematics).** Theorem 3.7 now reads: (iii) against all of Sig, K_mult(O; Sig) <= min(M+1, 2 d_O + 2, floor(A/pi)+4) for O with orders <= M, at every area, with Lemma 3.6 (sign changes) and a proof by the moments of the signed measure sum ±δ_{x²}/x; (iv) M+1 is attained, by Lagrange weights on the nodes 1², ..., M², X² for every integer X > M; X = M+1 is (ii) at M+1, and M = 2, X = 4 is (0;2^10), (1;4^4), area 6π, sharing exactly c_1, c_2. Corollary 3.8 rewritten (each orbifold of a pair sharing L invariants has an order >= L and >= (L-1)/2 distinct orders; f_M(A) <= M+1). Thm 1.2, the abstract and every dependent sentence (after Thm 3.13; old p. 5 and p. 17) changed. Proof and fragment: `theory/msep/proof.tex`; exact verification: `theory/msep/verify.py` sections 7-8 (complete area classes with unbounded orders, 17,572 signatures, the sign-change count checked on 23,952 pairs; 48 constructed pairs for 1 <= M <= 12, M < X <= M+4; the 6π example and K_mult((0;2^10); Sig) = 3 from its complete class); blind statement check: `theory/msep/BLIND-CHECK.md`. |
| A5 Uçar's mechanism | Credited before Lemma 2.10, with the quotation "we conclude by induction that the spectrum determines the sequence (W_ν)" from the fetched thesis (arXiv 1711.03405v1, SHA-256 b6da48a7...0a74, Thm 3.40 p. 98, proof p. 103), and the identity W_ν = Ψ_{ν+1}(m) at γ_i = π/m_i; again in §1.2 and at the remark after Lemma 2.10. "First explicit such number" now reads "to our knowledge no explicit number was known". Old Thm 5.1 is now Corollary 5.1 of Theorem A (b-m6). |
| A6 remainder | Prop. B.2 (enveloping remainders for E_m and I, with |b_K(m)| increasing in m), adapted with proof from theory/eigen; stated in Prop. 2.7 as (Grem). §4 states the growth |b_l(m)| ~ C_m l^{-1/2} l! (m/π)^{2l} (two-line derivation from the simple poles of Φ_m; checked numerically for m = 3, 12, l <= 80) and the optimal-truncation scale e^{-π²/(μ²t)}. The p. 4 sentence "A measured heat trace is never exact" is removed; §6 says the data are heat invariants and that (Grem) relates them to a trace. |

## Reviewer-rated MAJOR, adjudicated

| ID | disposition |
|---|---|
| A7 Thm 1.3 last sentence | The stability sentence in §1.1 now says "for data that are heat invariants of real orders it is 1/2 at a double order and when all n >= 3 orders are equal, while other configurations are open". |
| A8 a-posteriori corollary | Corollary 6.5 (A-posteriori use) stated and proved: if δ_1 + δ_2 <= δ_thm(m*) (or the certificate of Prop. S3.5 holds at m* with these radii), then m = m*. Cited in supplement S5. |
| A9 K = -1 | "(curvature −1)" in the definition of Sig in §1; the remark on an unknown K in §2.3 kept. |
| A10 density | Notation table (Table 1); slower proofs of Theorem B (four steps), Theorem 3.4 (three steps) and Theorem 5.4 (four steps); matrix of Theorem B renamed **M** (bold) to separate it from the order bound M. |

## MINOR items

| ID | disposition |
|---|---|
| n1 log base | moot (no logarithm in the new Theorem 3.7); "All logarithms are natural" in §1 |
| n2 Cor. 3.8 provisos | new Cor. 3.8 handles surfaces (L >= 2 required, surfaces share at most c_1) |
| n3 ζ_n range | supplement S3: maximum over 1 <= j <= n-2 (the rows of **M**), stated |
| n4 notation clashes | h_t (trace-formula test function) renamed \hat g_t; h_T renamed η_T; C of Lemma 2.5 renamed C_hyp; the box size of Lemma A.1 renamed Q; matrix **M** bold |
| n5 captions | captions kept at two sentences; the decoding (marks, line styles, panels) is in the citing sentences (F3, F4, F5, F6, F7, F8). F8 caption now cites Thm 6.2 and Prop. 6.4 (not old Thm 6.5) |
| n6 Fig. 1 | text now says what map is drawn (one triangle in Poincaré-disc coordinates lifted to a surface, values from the true triangle, one logarithmic scale; the colour bar is labelled in the figure) |
| n7 T(L) rows | relabelled "lower bound (Thm 3.4)" and "upper bound (Ex. 3.16)" |
| n8 Wright and Melzak | both credited, as in Borwein-Ingalls p. 7 |
| n9 dating the quote | "wrote in 1994"; current status from Chen's 2025 survey §8.1 P1 (quoted from the fetched text) |
| n10 converse direction | added after Prop. 3.14 and in Thm 1.1(ii): N(k) >= c k^{1/α} gives f = O(A^α); f = o(A) iff N(k)/k → ∞; "growth exponent" reworded ("whether f grows like a power of A at all is open") |
| n11 4N(2L-3) | Prop. 3.14 now T(L) <= min(6(L-1)²+6, 4N(2L-3)), with the source of each bound in the proof |
| n12 sharpness areas | listed after Theorem 3.7 (s = 2, 6, 18, 190, 442, 3998, 8838, 77054 for M = 2..9, from verify.py); minimality claimed only for M = 3, 4 |
| n13 Lemma A.1 | box renamed Q; the |U| bound of old Thm 3.7(iii) no longer exists |
| n14 Uçar Thm 4.10 | the citation is gone with old §7; the Neumann/Dirichlet splitting is argued in supplement S4 |
| n15 Thurston | now 13.3.4-13.3.6 (13.3.4 the χ formula, 13.3.5 Gauss-Bonnet, 13.3.6 the classification), checked in the fetched chapter |
| n16 Newton lemma | §1.2 now cites Lemma 3.1 with the argument of Theorem A, and [5, §3] only for odd symmetric systems |
| n17 Chang-DeTurck | DOI switched to the publisher DOI (reference record, see SOURCES.md round-4 section) |
| n18, n21 erratum, crosscaps | the paragraphs are removed (the paper no longer discusses non-orientable underlying surfaces or the erratum) |
| n19 missing references | Doyle-Rossetti, Proctor-Stanhope, Rossetti-Schueth-Weilandt, Gittins et al., Nursultanov-Rowlett-Sher, Aldana-Kirsten-Rowlett, Philippe (Geom. Dedicata) and the conic heat-kernel literature cited in §1.1-1.2 (records in SOURCES.md) |
| n20 McKean correction, Ostrowski, Wróblewski | McKean's correction cited with McKean; Ostrowski: see SOURCES.md; Wróblewski credited (2009, per Chen's survey, fetched text p. 64) |
| n22 "=" for "∼" | §4 and supplement S4 "Prediction" now use ∼, and state that the series diverges |
| n23 window end | §4 uses 0.0015 <= t <= 0.025, where the geodesic term is below 3e-15 (2.6e-15 for O(3,3,12)); S4 quotes 7.8e-13 at t = 0.03; both from `numerics/moduli/locality_ratio.py` |
| n24 silent steps | n_O(ℓ−) = 0 in Lemma 2.5; the nonpositive boundary term in Thm 4.2(b); the Hadamard bound with column norms and exponent (n−1)/2 (Thm S3.3(a)); index ranges in Thm S3.4; imaginary r_j and multiplicities in Lemma B.1; why n >= 3 and no smallness in Prop. 6.4; absolute convergence in Thm 2.3 |
| n25 data statement | Zenodo deposit (all six authors) is the primary citation [placeholder DOI]; the GitHub repository is the development repository maintained by A. Agadi; the scripts producing each table are named; S5 no longer anchors to a commit hash |
| n26 spectra ranges | see paper/eigen/ROUND4-CHANGES.md "shared spectra": both papers describe the same computations with the same counts |
| n27 enumerations | supplement S1: the 525 complete classes (33,946 signatures) have maximum K_mult 1 (17 classes), 2 (311), 3 (197), with the data file and script named |
| n28 local edits | Ex. 3.16(ii) reworded; range of g in Thm 3.12 explained; Cor. 3.5's last sentence replaced; f_g, f_n maximisation classes stated; T(L) heuristic deleted; §4 states that the errors are not enclosures. Close-out: Table S1 prints the exact area under every row with L <= 5 that shows an approximation (genus L = 5, equal count L = 4, 5, Prouhet L = 3, 4, 5), written by its generator `review/round1-fixes/d2_explicit_pairs.py` from the same exact values as d2_pairs.csv; the caption says where the exact values are |
| n29 δ_thm and App. D | δ_thm and its derivation in supplement S3; App. D keeps only the list of computer-search statements and a pointer to S7 |
| n30 arithmetic note | the note now cites Theorem 5.8 for the isolation |

## Length

See BUILD.md for the page counts of this build. Every proof of the paper's results is in the paper or the
supplement, and all eight figures are in the paper.

## Close-out (2026-10-09)

| item | disposition |
|---|---|
| variable curvature | New §2.4 "Variable curvature" after §2.3, from `theory/varcurv/` (statements and proofs as audited in `attack-log.md`, rounds 1-2): Prop. 2.11 "Cone terms in variable curvature" (VC1 structure, VC2 top coefficient, VC7 linear part, the t^3 formula VC3), with a proof sketch; Prop. 2.12 "Extension and obstruction" (VC4, VC5, VC6), with a proof sketch; closing paragraph on why constant curvature is the setting. Notation adapted to Paper A: the cone term is b_l(p) (reducing to b_l(m) of (5) at K = -1), the smooth part Ω_l (S_1 is the order sum), the fixed-point term ϑ_l(Φ), the Jacobi length J (f is the growth function), the second-variation constants ω_n, the constant curvature K_0. One sentence in the introduction's motivation paragraph and one in "Organisation" point to it; the four open items (β_{l,i} for l >= 4, non-radial terms for m <= l-2, whether equal c_2 always allows all-order agreement, isospectrality) are Problem 5. No new references: Donnelly, DGGW, Schueth 2019 and Uçar are already cited. |
