# VERDICT-A: referee round 4, Paper A (Annals of Global Analysis and Geometry)

Paper A: "How much of a hyperbolic orbifold does heat hear?", manuscript 39 pp. and supplement 14 pp.,
built from commit `defccde` (hashes in `README.md`). Reports: `A-a-editor-stratified-analyst`,
`A-b-equivariant-heat-invariants`, `A-c-equal-power-sums-growth`, `A-d-asymptotic-analyst`,
`A-e-citation-auditor`. The harness refused every reviewer's own write, so each `REPORT.md` was saved
verbatim by the main session from the task result. A provenance comment is on its first line.

## Gate: **FAIL**

| criterion | result |
|---|---|
| (i) no confirmed MAJOR or FATAL | **not met.** There is no FATAL item. Confirmed MAJOR items: A1 (significance and fit), A2 (length), A3 (overlap with Paper B), A4 (Theorem 3.7(iii) is superseded by a sharp area-free bound), A5 (Uçar's mechanism not credited), A6 (no remainder for the expansion in this paper) |
| (ii) every recurring theme resolved | **not met.** Significance and length are not resolved (a, b, e). Attribution is not resolved (A5, plus minor citation items). Proofs outside the paper are resolved except a stated corollary (A8). Overstated numerics are mostly resolved; Theorem 1.3's last sentence remains (A7). See the table below |
| (iii) editor sends to review with desk-reject probability ≤ 10% | **not met.** The editor sends it to review, but puts desk rejection at **30%** and expects referees to reach major revision (50%) or reject (35%) |
| (iv) ≥ 4 of 5 recommend minor or accept, no substantive "major" | **not met.** Two of five recommend minor revision (d, e). Two recommend major revision (b, c). The editor expects major revision. The majors of b (A1, A5) and c (A4) are about substance |

**Blocking items, in the order a revision should take them:**
1. A4: adopt the M+1 bound.
2. A5: credit Uçar's mechanism.
3. A3: remove the duplicated proofs between A and B.
4. A2 and A1: cut §4, §6 and §7, and argue the paper's significance on AGAG's terms.
5. A6: import or state the remainder.
6. A7 and A8: one sentence and one corollary.

WRITING-ONLY does not apply, because (iii) fails and A4 is mathematics.

**What the round established positively.** No reviewer found a mathematical error. Between them, the reviewers recomputed the following independently, in exact arithmetic or at 30-40 digits:
- every heat coefficient in Section 2, including an independent derivation of b_l(m) from Euler's beta integral to 2·10⁻⁴⁰, and the quadrature of the elliptic term;
- Appendix B line by line;
- all 20 pairs of Table S1 (equal area and exactly L shared invariants, L = 2..7);
- Theorem 3.7(ii) for M = 2..9, with the least areas exhaustively for M = 3, 4;
- Table S2, Table S3 and Theorems 5.4-5.7;
- Proposition S2.1 in full to S = 4800 (b, a C program over 3.1·10⁹ triads);
- the elliptic curve: PARI rank [0,0], analytic rank 0, torsion Z/6 × Z/2, every congruence of the hand descent in App. C;
- Theorem B's determinant;
- ζ_n, amp_r and every δ_thm of Table S4;
- the 8 primitive n = 4 witnesses;
- the partner triple of Remark 3.17.

Reviewer e checked 31 of 43 references at statement level and all bibliographic data. All eight figures were checked against their captions, with no error in what they draw.

## Recommendations

| reviewer | recommendation (confidence) | main reasons |
|---|---|---|
| a, AGAG editor (stratified analyst) | **send to review; desk-reject probability 0.30**; expected outcome accept 0.03, minor 0.12, major 0.50, reject 0.35 (confidence about 0.65) | fit and significance (M1), length (M2), depth of headline theorems (M3), overlap with B (M4), density (M5) |
| b, equivariant heat invariants | **major revision** (high on correctness, moderate on significance) | Uçar calibration (M1), scope and length (M2), §6 motivation and Thm 1.3 (M3), K = −1 (M4) |
| c, PTE growth | **major revision** (high on the mathematics) | Theorem 3.7(iii) superseded by M+1 (M1) |
| d, asymptotic analyst | minor revision (high) | no remainder (M1), a-posteriori corollary (M2), Thm 1.3 wording (M3) |
| e, citation auditor | minor revision, "bordering on major only through M2" (high on correctness, medium-high on citations) | Thm 1.3 wording (M1), scope (M2) |

## Deduplicated issue table

Severity is the highest any reviewer gave; where the main session changes it, the reason is stated. Type: M = mathematics, C = computation, W = writing. Status as in the brief: CONFIRMED, ANSWERED IN PAPER, ANSWERED IN REPOSITORY BUT NOT PAPER.

### MAJOR

| ID | reviewers | severity | location | issue | resolution | type | status and check |
|---|---|---|---|---|---|---|---|
| A1 | a-M1, a-M3, b (significance), e-M2 | MAJOR | §1, §1.1-1.2, abstract | After Prop. 2.7 the paper is power-sum algebra, PTE, Diophantine geometry and numerics. The analytic input is a re-derivation of Uçar's expansion. The headline Theorem 1.1(i), (iii) are a Newton-identity argument and a Vandermonde determinant. The paper does not argue why the finite-jet count is a geometric-analytic quantity for AGAG readers | Re-rank the results so that Thm 3.13(d) with Prop. 3.14, Thm 3.10, Thm B and Thm 5.8 lead. Say what the paper adds to heat asymptotics at cone points (conic heat-kernel literature, a-m12). Optionally treat variable curvature or unknown K (b-M4) | W | **CONFIRMED** as a judgement shared by a, b and e (d and c call the questions natural). The source confirms the structure: Section 2 plus App. B is the only heat-kernel input; line 249 credits Uçar for every coefficient; Section 4 is "classical in substance" (line 189). Not a defect of correctness |
| A2 | a-M2, b-M2, e-M2 | MAJOR | §4 (pp. 20-22), §6 (pp. 27-30), §7 (pp. 30-32), supplement | At 39 + 14 pp. §4 records classical facts. §6 proves a threshold δ_thm that is loose by 5·10² to 2·10⁸, while the sharp certificate is in the supplement. §7 is "used in no proof" | Cut §4 to a remark; reduce §6 to one theorem, preferably the certificate; move §7 to the supplement. Target 25-28 pp. | W | **CONFIRMED.** The page counts are from the build: 39 pp., down from 48 in round 3 after the split. §7's first sentence is "Nothing here is used in a proof" (line 824). AGAG has no page limit (`paper/jga/AGAG.md`), so this is review burden, not a rule |
| A3 | a-M4 (b-M2 asks the editor to check) | MAJOR | A §2-3 against B §2-3; Lemma B.1 | Paper B restates, with proofs, the trace formula, the closed-geodesic counting lemma, the hyperbolic-term lemma, Lemma 2.6, the cone polynomials, the signature lemma, the separation theorem and Theorem 3.7(i). Two sets of referees would review the same lemmas | Prove each shared result in one manuscript and cite it in the other; or, since each must stand alone, keep proofs in both but say so in both cover letters and mark the shared parts | W | **CONFIRMED, at smaller extent than a states.** Sentence-level comparison of the two `.tex` files: 13 identical and 24 near-identical (≥ 85% similar) sentences of more than 80 characters, about 7,000 characters, or roughly 2 pages, not "5-6 pp. mostly verbatim". However, about nine statements with proofs appear in both (B lines 133-275: `thm:trace`, `lem:counting`, `lem:hyp`, `lem:Phi`, `lem:conepoly`, `lem:sigdata`, `thm:sep`, `thm:bounded`). `paper/jga/ROUND3-CHANGES.md` says each paper is self-contained by design; the editor sees this as duplication |
| A4 | c-M1 | MAJOR | Thm 3.7(iii), Cor. 3.8(b),(c), Thm 1.1(iii), abstract, p. 17 | Theorem 3.7(iii)'s M + ⌈½ log(2⌊A/π⌋+8)⌉ is not sharp. A sign-change (Descartes-Laguerre) argument gives K_mult(O;Sig) ≤ M+1 for every O ∈ Sig_{≤M} and every area, and M+1 is attained. The abstract's "M plus a logarithm of the area suffice" and p. 17's "grows at most logarithmically" are true but superseded, since the count is bounded. The same argument re-proves Thm 3.7(i) in one line and gives K_mult ≤ 2d_O + 2 | Replace (iii) by "≤ M+1, attained"; revise Cor. 3.8(b),(c), Thm 1.1(iii), the abstract and the sentences on pp. 5 and 17; cite the sign rule | M | **CONFIRMED by the main session.** (1) The proof is sound. ν = Σ μ(x)/x δ_{x²} has vanishing moments of degree 0..L−1 by (eq:red2): the reciprocal sum and the odd power sums j ≤ 2L−3. A nonzero measure with this property has at least L sign changes, and y = x² preserves order. Points x > M come only from O', so they all have one sign, and points in [1, M] number at most M. Hence there are at most M+1 sign blocks and at most M sign changes, so L ≤ M. (2) A computed instance: (0;2¹⁰) and (1;4⁴) both have area 6π. The paddings U = {2¹⁰} and V = {4⁴,1⁴} give R = 5 = 5 and P_1 = 20 = 20, but P_3 = 80 ≠ 260. So they share exactly c_1, c_2 and K_mult = 3 = M+1, against the paper's bound 2 + ⌈½ ln 20⌉ = 4. (3) Reviewer c checked attainment exactly for M = 2..7 and found no violation among 24,701 signatures. The paper's statements are true, so nothing is false; the item is MAJOR because a headline theorem and the abstract are superseded by a short sharp argument. The repository saw it without proving it: `theory/msep/BLIND-CHECK.md` (lines 58-62) records that the largest K_mult in its complete equal-area classes was M + 1, on this same example, "so the logarithmic term was never needed in its data". Neither the paper nor `theory/msep/proof.tex` has the proof |
| A5 | b-M1, b-m5, b-m6 (a-M3, e Significance) | MAJOR | §1.2 (line 185), Lemma 2.10 and the sentence after it (lines 306-316), p. 5 "first explicit such number", Thm 5.1 | The mechanism on which the paper rests, that each coefficient adds one new odd power sum with nonzero top coefficient, is the engine of Uçar's proof of his Thm 3.40, which he uses for Cor. 4.21. The paper credits Uçar only for the coefficients and for recovery "from the whole sequence" | Attribute Lemma 2.10's mechanism to Uçar's proof of Thm 3.40; state that the new content is the explicit finite count and its analysis; make Thm 5.1 a corollary of Theorem A | W | **CONFIRMED against the source.** In the fetched thesis (`research/notes/spectral-invariants-for-polygons-and.md`, Thm 3.40 and proof, around line 9117), the top-degree coefficient W_ν of the ν-th angle term is (−1)^ν B_{2ν}/(4(ν+1)!(2ν+1)) ≠ 0, "we conclude by induction that the spectrum determines the sequence (W_ν)". That is Lemma 2.10's triangular structure, with angles γ = π/m. Paper A line 185 and Lemma 2.10 do not cite it. This counts against the recurring theme "attribution" |
| A6 | d-M1, b-M3 (first point) | MAJOR | Prop. 2.7, App. B, p. 4 ("A measured heat trace is never exact"), p. 5, §7, S4-S5 | The expansion is stated only as "∼", with no remainder. So nothing connects trace data to the heat invariants that Theorem 1.3 takes as input. The proof in App. B already gives an enveloping remainder by positivity, and with it the optimal-truncation scale exp(−π²/(μ²t)) | Add the enveloping-remainder proposition (half a page) and either an extraction lemma or a softened motivation on p. 4 and in §7 | M, W | **ANSWERED IN REPOSITORY BUT NOT PAPER.** Paper B already proves exactly this: `paper/eigen/manuscript.tex` line 208 "The cone term is enveloped" (`prop:remcone`) and line 220 "The area term is enveloped" (`prop:remarea`). Paper A does not state it. Paper A's supplement S4 already says that the eigenvalue errors are "not enclosures" and that nothing is "certified" (`supplement.tex` line 295), so the overstatement is confined to the motivation on p. 4 |

### Reviewer-rated MAJOR, adjudicated

| ID | reviewers | rated | location | issue | resolution | type | status and check |
|---|---|---|---|---|---|---|---|
| A7 | b-M3, d-M3, e-M1 | MAJOR | Thm 1.3, last sentence (p. 4) | "for data that are heat invariants of positive real orders it is ½, and attained, at a double order and when all n ≥ 3 orders are equal" can be read as a general claim; §6 says that "other configurations are not settled" | Append "other configurations are open" | W | **ANSWERED IN PAPER in substance; severity adjusted to MINOR.** Literally, the sentence restricts the claim to the two configurations. Line 788 says "other configurations are not settled", and the proof of Prop. 6.7 says "mixed clusters are not settled" (line 803). Three reviewers misread it, so the wording must change, but nothing false is claimed. Counts under "overstated numerics" until fixed |
| A8 | d-M2, d-m10 | MAJOR | Remark 6.1 (`rem:stabscope`), S3, S5 | The a-posteriori use of Theorem 6.8 is asserted, not stated. Applied at a candidate m*, Theorem 6.8 says that data near c(m*) round to m*. The needed conclusion m_true = m* also uses exact recovery at the true orders (Theorems A and B) and a radius covering data-to-candidate plus data-to-truth. "δ covering the distance from the data to its exact invariants" is ambiguous on exactly this point | State and prove the corollary (3 lines) and cite it in Thm 1.3, S3 and S5 | M, W | **CONFIRMED; severity adjusted to MINOR.** Remark 6.1 reads as quoted. The argument the reviewer gives is correct, and S5 already uses radii "equal to the distance ... plus the error bars". The gap is a missing three-line statement, not a missing idea. It counts under "proofs outside the paper" |
| A9 | b-M4 | MAJOR | abstract, Thm 1.1, §1.1, line 324 | Every count assumes curvature exactly −1. Does Thm 1.1(i) survive, with one more invariant, when K < 0 is unknown? | State the K = −1 setting in the abstract; add a remark on unknown K | M, W | **ANSWERED IN PAPER in part; severity adjusted to MINOR.** "Hyperbolic" means K = −1 by the standard convention, and line 324 says "an unknown K is one more unknown, tied to χ by K Area = 2πχ". The unknown-scale extension is a scope request, not a gap |
| A10 | a-M5 | MAJOR | throughout; pp. 10-18, 27-30; intro digressions (erratum, orientability) | Prose compressed to opacity; heavy notation; mixed lettered and numbered theorems | Notation table; slower §3; move the digressions | W | **CONFIRMED as a request; severity adjusted to MINOR** (b, d and e call the writing high-quality and careful; d calls it "unusually well written"). Folded with the notation clashes n4 |

### MINOR (deduplicated; CONFIRMED unless stated)

| ID | reviewers | location | issue | resolution | type |
|---|---|---|---|---|---|
| n1 | a-m1, b-m1, c-m6, d-m7, e-m15 | Thm 1.1(iii), Thm 3.7(iii), Cor. 3.8 | base of "log" not stated (natural, from log(1+y) ≥ 2y/(2+y)) | state it, or drop it under A4 | W |
| n2 | c-m7, d-m7 | Cor. 3.8(b); Thm 3.7(iii) | "largest cone order" undefined when n = 0; "L ≥ 2" belongs to the first claim only | add the proviso | W |
| n3 | a-m9, e-m14 | definition of ζ_n before Thm 6.4 | the range of j is implicit; the printed values need j ≤ n−2 (with j ≤ n−1, ζ_4 = 2336/5) | state "0 ≤ j ≤ n−2" | W |
| n4 | b-m10, e-m16, a-M5, d (presentation) | notation | h_t against 𝔥_t; κ, c, C, M, T, g overloaded | rename the worst clashes | W |
| n5 | a, b-P2..P6, d, e | Figs. 2, 3, 6, 7, 8 | captions do not identify marks and line styles (dots, diamonds, squares, split disc, step curves; which curve is (2,3,7), (2,8,8), (4,4,4); the diamonds and horizontal line of Fig. 7; the truncations, circles and shading of Fig. 8). Fig. 7's caption attributes the dotted slope to Thm 6.5, but it is Prop. 6.7. Fig. 3's dashed lower bound comes from unplotted pigeonhole pairs | make each caption self-contained | W |
| n6 | a, b-P1, e | Fig. 1 and p. 4 | "schematic"/"stylised shape" against "drawn at the point with the same Poincaré-disc coordinates" (line 163); the log colour bar is not labelled | say what map is drawn | W |
| n7 | a-m6, c-m9 | T(L) table, p. 18-19 | row labels "2L+2 ≤ T(L)" and "T(L) ≤" read badly | label the rows "lower bound (Thm 3.4)" and "upper bound (Ex. 3.16)" | W |
| n8 | c-m1, e-m3 | p. 17 | the N(k) bounds ½(k²−4), ½(k²−3) are attributed to Wright alone; Borwein-Ingalls cite Wright and Melzak; as printed they fail for k = 2, 3 | credit both; give the range of k | W |
| n9 | c-m2, e-m12 | p. 17 | "for many years" quotes a 1994 survey | date it; cite [20] or [37] for the 2026 status | W |
| n10 | c-m3 | Thm 1.1(ii) | "growth exponent" presumes an exponent exists; the converse direction (N(k) ≥ ck^{1/α} gives f = O(A^α)) follows from Prop. 3.14 and is not stated | reword; add the converse | M |
| n11 | c-m4 | Prop. 3.14 | 6N(2L−3) can be 4N(2L−3) | tighten | M |
| n12 | c-m5 | Thm 3.7(ii) | sharpness holds only at large areas (area/2π = 2, 6, 18, 190, ... for M = 2..9) | list them; say what minimality is claimed | W |
| n13 | c-m8 | Lemma A.1 | M is reused for the box size; Thm 3.7(iii) uses \|U\| ≤ 2⌊A/π⌋+8 where ⌊A/π⌋+4 is available | rename; tighten | W |
| n14 | e-m1 | §7, line 824 | [14, Thm 4.10, Cor. 4.18] is cited for "the spectrum of the triangle orbifold is the union of the Neumann and Dirichlet spectra"; Uçar's Thm 4.10 is about lune quotients M/Z_k, M/D_k on S²(r), and Cor. 4.18 about heat invariants of surfaces with geodesic boundary | **checked by the main session in the fetched thesis (line 11411 ff.)**: confirmed; cite the elementary argument in S4 instead | W |
| n15 | e-m2 | Def. 2.1 | "hyperbolic exactly when χ < 0" is Thurston 13.3.6, not 13.3.4-13.3.5 | fix | W |
| n16 | e-m4 | p. 5 | "[5, Prop. 1 and §3]" does not state the Newton-identity lemma | prove in two lines or cite Lemma 3.1 | W |
| n17 | e-m5, e-m10 | [15] Chang-DeTurck | the theorem is paraphrased from Grieser-Maronna; JSTOR alias DOI | state it from the source; use DOI 10.1090/S0002-9939-1989-0953738-7 | W |
| n18 | e-m6, e-m11 | p. 2-3 | [4, Thm 4.7] rests on the same Iso^max mechanism as [2, Thm 5.1]; say why it is unaffected by the erratum; cite [4, §1] for the open orientability question | add the sentences | W |
| n19 | b-m3, b-m4, e-m7, e-m8, a-m12 | §1.1-1.2 | missing: Doyle-Rossetti (math/0605765, arXiv:1103.4372); Proctor-Stanhope; Rossetti-Schueth-Weilandt; Gittins et al.; Nursultanov-Rowlett-Sher; Aldana-Kirsten-Rowlett; Philippe's original paper (Geom. Dedicata 2010); the conic heat-kernel literature (Cheeger, Brüning-Seeley, Dowker) | add, one sentence each | W |
| n20 | e-m9, e-m13 | references | McKean's Correction (CPAM 27 (1974) 134); Ostrowski's two-part memoir; credit Wróblewski for the A.1.33 pieces | add | W |
| n21 | b-m2, d-m11 | p. 3, non-orientable paragraph | only an even number of crosscaps is treated; glide reflections should be said to contribute O(e^{−c/t}) | restrict or extend; add the sentence | M, W |
| n22 | d-m1, d-m3 | p. 31, S4 | "D(t) = Σ d_j t^{j−2}" should be "∼"; the coefficient growth is C_m l^{−1/2} l! (m/π)^{2l} | fix; state it | W |
| n23 | d-m2 | p. 31, S4(ii) | at t = 0.03 the omitted shortest-geodesic term of O(3,3,12) is about 7.8·10⁻¹³, as large as the stated agreements of 7·10⁻¹³ and 4·10⁻¹³ (within the 1.5·10⁻¹¹ budget) | compare with I + E + Hyp, or end the window at 0.025 | C |
| n24 | d-m4, d-m5, d-m6, d-m8, d-m9, d-m12 | Lemma 2.5, Thm 4.4(b), Thm 6.4(a), Thm 6.5, Lemma B.1, Prop. 6.7 | silent one-line steps (n_O(ℓ−) = 0; the sign of the boundary term; the Hadamard exponent (n−1)/2; index ranges; imaginary r_j; why n ≥ 3) | add the sentences | M, W |
| n25 | a-m14, b-m15, e-m19, e-m20, a-m15 | data statement (line 871), S5 | the repository is under an account ("Ali-M658") that matches no author; S5 anchors its blind protocol to a commit hash | state who maintains it; cite the Zenodo DOI as the primary record | W |
| n26 | a-M4 (data), a-m2, a-m16 | Supp. S6 against B §7 | the same spectra are reported with different ranges (A: about 2850 eigenvalues per triangle and about 5450 for the family; B: 815-856 for the family); B is called "in preparation"; A's description of B's Theorem 3.4 is inaccurate | reconcile and explain the ranges; update the status when submitting; coordinate wording | W |
| n27 | a-m11, b-m13, e-m18 | p. 26, Prop. S2.1; Fig. 3; Remark 3.2 | the 38-sum enumeration is also the note's (cite it); the 525-class K_mult values are listed nowhere; "193 witnesses" and the pencil counts count different things | cite; add a table; distinguish | W |
| n28 | a-m3, a-m5, a-m10, a-m13, b-m9, b-m11, b-m14, b-m12, e-m17, c presentation | various | Ex. 3.16(ii) wording; why g ≥ 2 in Thm 3.12; logic of the finiteness sentence on p. 5; quantify "loose"; delete or sharpen the T(L) heuristic; Cor. 3.5's "determined without being known in advance"; state Steinig's theorem; state in §7 that the eigenvalue errors are not enclosures; f_g, f_n maximisation classes; exact areas for Table S1 rows L ≤ 5 | local edits | W |
| n29 | a-m7, a-m8 | Thm 6.8; App. D | the loose δ_thm is in the paper and the sharp certificate in the supplement; App. D duplicates S7 | swap (with A2); keep one copy | W |
| n30 | a (overlap section) | arithmetic note, Table 1 caption (`note.tex` line 314) | cites "[Theorem 6.8]" of Paper A for C_{27/2}; the isolation theorem is Theorem 5.8 (`thm:isolation`) | **confirmed in the source**; fix in the note | W |

## Disputes settled

- **A4 (c-M1) against Theorem 3.7(iii).** Settled by the argument and an exact instance (above): the paper's bound is true and not sharp. No reviewer disputes the paper's bound; the dispute is only whether the improvement matters, and it changes the abstract.
- **A3 extent ("5-6 pp. mostly verbatim").** Settled by comparing the two `.tex` files sentence by sentence: about 2 pp. of identical or near-identical sentences, but about nine results proved in both papers.
- **A7 (Theorem 1.3 overstated).** Settled by the source: line 788 and the proof of Prop. 6.7 already restrict the claim; the headline sentence is ambiguous, not false.
- **A5 (Uçar).** Settled by the fetched thesis text of Thm 3.40 and its proof.
- **n14 (Uçar Thm 4.10).** Settled by the fetched thesis: the citation does not state what it is cited for.

## Recurring themes of earlier rounds

| theme | verdict for Paper A |
|---|---|
| significance | **not resolved** (a, b; e defers to the editor): see A1. Every reviewer likes Theorem 3.7, the PTE equivalence and the triangle analysis; a and b judge the paper elementary and peripheral to global analysis |
| length | **not resolved**: down from 48 to 39 pp. after the split, but a, b and e still ask for 25-28 pp. by cutting §4, §6 and §7 (A2) |
| attribution | **not resolved**: Uçar's mechanism (A5), plus minor citation repairs (n8, n14-n20). The bibliographic data are clean (e) |
| proofs outside the paper | **resolved except A8.** No reviewer found a proof step resting on the repository, a website or "checked numerically"; App. D separates the computer-only statements, and every reviewer praised this. Residual: the a-posteriori corollary (A8) and the repository-ownership statement (n25) |
| overstated numerics | **mostly resolved**: the supplement says the errors are "not enclosures" and nothing is "certified". Residual: Theorem 1.3's last sentence (A7), the motivation on p. 4 (A6), "=" for "∼" (n22) and the window end (n23) |

## What a revision should do, ranked

1. **A4.** Replace Theorem 3.7(iii) by K_mult(O;Sig) ≤ M+1 (attained), with the sign-change proof. Re-prove (i) the same way if wanted, and add K_mult ≤ 2d_O + 2. Rewrite Cor. 3.8, Thm 1.1(iii), the abstract and pp. 5 and 17.
2. **A5.** Credit Uçar's Thm 3.40 mechanism at Lemma 2.10 and in §1.2. Describe the new content as the explicit count and its analysis. Make Thm 5.1 a corollary.
3. **A3.** Decide the proof home of each shared lemma between A and B, or declare the duplication in both cover letters. Reconcile the datasets (n26).
4. **A2 and A1.** Condense §4 to a remark. Reduce §6 to one theorem (the certificate) with the A8 corollary. Move §7 to the supplement. Rewrite §1 to lead with the deeper results and connect to the conic heat-kernel literature.
5. **A6.** Import B's enveloped-remainder propositions (or cite B) and soften p. 4.
6. **A7, A8, A9** (one sentence, one corollary, one remark), then the MINOR table. n1, n2, n3, n5, n7 and n14 are one-line fixes.
