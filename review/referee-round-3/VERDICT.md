# VERDICT: referee round 3 (Annals of Global Analysis and Geometry)

Input: manuscript 48 pp., supplement 15 pp., note 12 pp. (commit 09f9019; hashes in `README.md`).
Reports: `a-agag-handling-editor`, `b-orbifold-spectral-geometer`, `c-hyperbolic-trace-formula-analyst`,
`d-pte-combinatorialist`, `e-rigour-and-citations` (each `REPORT.md`; all five reviewers returned their
text because the harness refused their writes, and the main session saved it verbatim from the task
transcripts, with a provenance comment on the first line).

## Gate: **FAIL**

| criterion | result |
|---|---|
| (i) no confirmed MAJOR or FATAL | **not met**: five confirmed MAJOR issues (I1, I2, I5, I6, I8 below); no FATAL |
| (ii) every recurring theme judged resolved | **not met**: significance (a, b) and length (a, b, c; the manuscript grew from 33 to 48 pp.) are not resolved; "proofs outside the paper" is resolved for the two appendices but recurs in three smaller forms (I5, I7, I8); attribution is resolved |
| (iii) editor sends to review with desk-reject probability at most 10% | **not met**: the editor sends the paper to review but puts desk rejection at about 20% |
| (iv) at least four of five recommend minor revision or accept, and no remaining "major" is about substance | **not met**: three of five (c, d, e: minor revision); b recommends major revision, and the editor expects referees to reach major revision (60%); b's M2 and M3 are about substance |

**Blocking items** (in the order the revision should take them): I6 (the bounded-order observation, a
missing theorem), I2 (what Section 4 adds beyond the compactness argument; an a-posteriori version),
I1 (length and breadth), I5 and I8 and I7 (proof steps resting on "checked numerically", Wikipedia, or
the repository).

What the round established positively: **no reviewer found a mathematical error.** Reviewers c, d and e
recomputed independently, in exact arithmetic or at 30-80 digits, the heat coefficients, the
enveloping remainders, the diameter and counting constants and every row of Table 2, the integrality
lemma on 28,290 equal-area pairs, the triangle collisions (to S = 1000 and, for the collision-free
sums, to 600), the elliptic curve (rank 0 by their own 2-isogeny descent and by PARI), the n = 4 and
n = 5 integer searches, the 4.3 x 10^9-multiset exclusion of Remark 3.14 (by a different, sound test),
the 525 equal-area classes, all printed pairs of Table S1 and the three unprinted Prouhet squares, and
47 citations. Reviewer e found all eight figures consistent with their captions.

## Recommendations

| reviewer | recommendation (confidence) | notes |
|---|---|---|
| a, AGAG handling editor | send to review; desk-reject probability about 20%; expects referees to reach major revision (60%), reject 30%, accept 10% | breadth, practical value of Section 4, conditional growth result |
| b, orbifold spectral geometer | **major revision** (60%; minor 30%, reject 10%) | M1 scope, M2 Section 4, M3 the divergence is driven by unbounded cone orders |
| c, trace-formula analyst | minor revision (70%); correctness of Theorem 4.13 about 90% | M1 numerical steps and Wikipedia, M2 thin content, M3 scope |
| d, PTE combinatorialist | minor revision (70%) | M1 T(L) constructions, M2 floating-point filter, M3 literature |
| e, rigour and citations | minor revision (75%) | M1 numerical steps and Wikipedia, M2 computer searches |

## Deduplicated issue table

Severity is the highest any reviewer gave; where the main session changes it the reason is stated.
Type: M = mathematics, C = computation, W = writing. Status as in the brief: CONFIRMED, ANSWERED IN PAPER,
ANSWERED IN REPOSITORY BUT NOT PAPER.

### MAJOR (as rated by at least one reviewer)

| ID | reviewers | severity | location | issue | resolution | type | status and check |
|---|---|---|---|---|---|---|---|
| I1 | a-M1, b-M1, c-M3 (e: presentation) | MAJOR | whole paper | four separable papers in 48 + 15 pages (PTE counting, triangle orbifolds with an elliptic curve, finite-eigenvalue theorem, stability and numerics); the cross-dependencies are heavy and few referees can check all of it | split the paper, or move Sections 7-8 (and 4.6) to the supplement, or add a reader's guide stating which result depends on which section | W | **CONFIRMED.** `BUILD.md`: 48 pages; Sections 4, 7 and 8 are 12, 3 and 2 pages; wave 2 added 15 pages. AGAG has no page limit (`AGAG.md`), so this is a judgement about review burden, not a rule |
| I2 | a-M2, b-M2, c-M2 | MAJOR | abstract, Section 4, Table 2 | Theorem 4.13 is effective but unusable (N from 10^7 to 10^35, delta to 10^-384). The paper does not say what effectivity adds to the non-effective argument (finitely many signatures; moduli of bounded systole is compact; eigenvalues are continuous; the spectrum determines the signature [DS09]); the proof manufactures its gap from a divergent expansion, forcing t_* about 10^-9 to 10^-31, and an a-posteriori version (min over pairs of the exact gap |G_sigma - G_sigma'| at a moderate t) would be far cheaper; Problem 5 may yield to Selberg's lemma and the degeneration literature | state the compactness argument and what effectivity buys; add the a-posteriori corollary; compare with the constants it would give on the committed spectra; attempt or discuss Problem 5 | M, W | **CONFIRMED.** The paper says "what the theorem contributes is effectivity" (Section 4 opening) but not why it is not immediate; I checked that the compactness argument works (finitely many signatures, uniform N and delta by compactness and continuity), so the reviewers' point is right. The a-posteriori suggestion is consistent with Section 4.6, which already does it on data. Problem 5 is speculation, not settled |
| I5 | c-M1, e-M1 (a-m1, b-m2) | MAJOR | Section 4.1 before (H1); Proposition 4.4 and its commutator-trace identity; Proposition S7.1; reference [36] | steps on which the diameter bound and the O(2,3,m) necessity rest are "checked numerically with the repository code": the rotation-displacement formula, the product of two reflections, the law of cosines for angles, the identity tr[g,b] - 2 = 4 sinh^2(L/2) sin^2(phi/2) cosh^2 r, the Lambert relation; Jorgensen's inequality is cited to a Wikipedia page | give the one-line proofs or textbook citations for (H1)-(H3) and the identity (a four-line matrix computation); replace [36] by the original together with a textbook statement, or prove the special case needed | M, W | **CONFIRMED** (the text says so; `diameter.tex`). Both reviewers verified every statement numerically (identity to 3 x 10^-14), so nothing is false. Note the constraint from the brief: a textbook statement may be cited only after it is fetched; Beardon section 5.4 or Maskit has not been, so the safe resolution is to prove the special case needed (distance from the axis, order-3 rotation) |
| I6 | b-M3 | MAJOR | Theorem 1.1(i)-(ii), Theorems 3.10-3.11, Table S1, abstract, Section 1.1 | the divergence of f(A) is a large-order phenomenon: among orbifolds with all orders in {2..M} the first M heat invariants determine the signature for every area, so any growth in A needs M to grow; the extremal pairs have orders up to 10^36, where the short-time-diffusion reading is empty. "No number independent of the area" is true but is really "independent of the largest order" | state and prove K_mult <= M against competitors with orders <= M; define f(A, M); say in the abstract that the worst case is a large-order phenomenon; discuss the interpretation in Section 1.1 | M, W | **CONFIRMED by computation.** The matrix (a^(2k-1) - 1/a), 1 <= k <= M-1, 2 <= a <= M, has full rank M-1 for every M = 3..18 (exact `sympy` rank, run by the main session), which with Lemma 2.10 gives the claim; the reviewer's Lagrange-weights proof sketch for all M is plausible and not checked line by line. Neither the paper nor the repository states it. It also shortens k_* = floor(A/pi) + 4 in Theorem 4.13 to min(k_*, M), which would improve every constant in Table 2. The reviewer's further claim against arbitrary competitors (v_max <= M n^(1/(2L-3))) is not checked |
| I8 | d-M2, e-M2 (b-m6) | MAJOR (d), MAJOR (e) | Remarks 3.2 and 3.14, supplement S1 and S8(ii) | the exclusion of every (3,5) genus pair with entries at most 220 rests on a binary64 floating-point filter with "rigorous inclusion disks" and "safety factors"; the soundness of the filter is not shown, and the bounded searches are not labelled as computations where they are stated | state the exact necessary condition behind the filter and prove it sound, or replace it with an exact certificate (reviewer d's modular-splitting test: the cubic splits mod twelve primes between 223 and 277; 15 of 4.3 x 10^9 survive, all irreducible); label each search with its bound in the statement; add the key and loop bounds to S8; mark the exclusion as computer-assisted in the introduction | C, W | **CONFIRMED for the paper; the conclusion is not in doubt.** In the repository, `review/audit-2/pte-witnesses/check_t3_verify.py` checks coverage and re-examines every survivor in exact arithmetic with two planted controls (stage "audit-2 pte-witnesses"), and reviewer d reproduced the exclusion by a different sound test. What is missing is the soundness argument for the rejections, in the paper |

### Reviewer-rated MAJOR, adjudicated

| ID | reviewers | rated | location | issue | resolution | type | status and check |
|---|---|---|---|---|---|---|---|
| I3 | a-M3 | MAJOR | Theorem 1.1(ii), Theorem 3.11, Proposition 3.12 | the growth question is converted into the open PTE problem, and the sqrt(A) lower bound restates the quadratic PTE bounds | say plainly that the exponent is open and equivalent to PTE; discuss what the extra structure (odd sums, vanishing reciprocal sum) could add | W | **ANSWERED IN PAPER.** The abstract says "an open question"; Section 1.2 says that Theorem 1.1(ii) "relocates the growth question to the Prouhet-Tarry-Escott problem rather than settling it". Reviewers b, c, d, e call the reduction correct and neat. Residual: a short discussion, MINOR |
| I4 | a-M4 | MAJOR | Section 1.2, Theorem 6.8, the note | the cross-references between the paper and the note are circular; several statements rest on computer search only | state in both documents which contains the proof; list the search-only claims | W | **ANSWERED IN PAPER.** `paper/arith/note.tex` line 94: the note "also proves that the smallest coincidence is isolated [Theorem 6.8]; this note does not restate that result"; the paper says that the note "cites Theorem 6.8 for the isolation; no proof here depends on it". Both say the proof is in the paper (Theorem 6.8 and Appendix C). Residual: a list of the search-only claims, MINOR |
| I7 | d-M1 | MAJOR | Example 3.13(iii), T(L) table, Table S1 | the upper bounds T(4..7) <= 14, 18, 24, 40 and the genus pairs are given by data and a citation, without the construction (which ideal solution, which shift, how the reciprocal sum is made to vanish); the A.1.33 attribution covers at most L = 6; what was searched for T(4) <= 12 | state the construction for each L; fix the attribution | W | **ANSWERED IN REPOSITORY BUT NOT PAPER.** `theory/pte/data/witnesses.json` has a `recipe` for each of the 18 pairs (for example "shift of the size-8 ideal solution by 26, then doubling"; "size-12 solution shifted by -129/2 and -27/2"), the genus-changing combination is Theorem 3.11(c) with the shift proposition of Appendix A, and reviewers d and e verified all printed pairs and rebuilt the three unprinted squares from the caption. Severity adjusted to MINOR for the gate (every statement is checkable and was checked); it counts under the recurring theme "material outside the paper" |
| I9 | d-M3 | MAJOR | Sections 1.2 and 3.3, bibliography | PTE positioning relies on an unrefereed survey and a 1961 note; classical sources (Wright, Hua, Wooley, Letac) and a heuristic for T(L) are missing | add sources and a short discussion | W | **CONFIRMED as a request; severity adjusted to MINOR.** Every PTE statement was verified; reviewer e checked the cited statements; the bibliography already has Wooley 2012 and 2019 and Borwein-Ingalls. It is a positioning preference, not a gap in an argument |

### MINOR (deduplicated; all CONFIRMED unless stated)

| ID | reviewers | location | issue | resolution | type |
|---|---|---|---|---|---|
| n1 | a-m6, e-m5 | Table 3, Section 4.6 | the caption says the ranges run over all eight members, but the a-priori range covers the seven of systole at least 0.846; "diam <= 7.77" in the text, "7.8" in Table 1 | correct the caption; unify | W |
| n2 | e-m8 | Section 1.1 | duplicated sentence: "Section 4 connects the heat invariants to finitely many eigenvalues ... Section 4 proves that the first N eigenvalues ..." (introduced by the wave-2 edit, which replaced only the placeholder) | delete the first | W |
| n3 | c-m1, b-m5, e-m6 | notation | overloaded symbols: Phi_m / Phi_j, sigma_0 (signature and 0.5621), Gamma (group, gap), Lambda, N, T, L, C, Z, D, p, a_l | rename at least Phi_j, sigma_0, T, D | W |
| n4 | e-m7 | Appendix D, Remark 2.9 | "Appendix D" is cited for the l <= 40 comparison with Ucar and for the numerical checks of (H1)-(H3), and says neither | describe them (see I5) | W |
| n5 | e-m4 | Theorem 1.2(ii), (iii) | "always determine" and "the only such pair" lack the class "among hyperbolic triangle orbifolds" | add | W |
| n6 | e-m1, b-m2 | Section 1.1, [8] | Schueth [8] is cited for computing the K(p), K^2, Delta K terms for curved cones; its abstract (fetched by the main session) gives a formula for b_{1/2} under rotational symmetry. The terms at order t and t^2 are [2] and [13] | rephrase | W |
| n7 | e-m3 | Section 1.1 | [9, Thm 1.1] gives the number of cone points of each order; the genus needs [9, Prop. 3.3] | cite both | W |
| n8 | e-m2 | Section 1.2 | the Chang-DeTurck count holds for triangles with all angles bounded below by some epsilon | state the restriction | W |
| n9 | b-m3 | Section 1 | scope of the DGGW erratum not quoted | quote it | W |
| n10 | c-m3 | Theorem 4.13, Section 4.6 | the data are tacitly the first N eigenvalues, in order and complete (Section S4 admits that single-window slicing can miss one) | state the hypothesis | W |
| n11 | c-m2, b-m10 | Lemma 4.11 | the divisibility by every prime p with (p-1) \| 2(k-2) is stated and not used; p = 2, 3 always qualify, so |d_k| >= 6 a_{k-2} for k >= 3 | use or drop | M |
| n12 | c-m4 | Section 4.1 | the diameter detour is needed only for the geodesic-counting bound and is not binding in any row of Table 2 | say so | W |
| n13 | c-m10, b-m7 | Section 4 | "log(1/delta) grows like (A/pi)^2 log(AM)" and "N grows like eps^-3 log(1/eps)" are observations on formulas | label as heuristic | W |
| n14 | a-m7, d-m3, e-m11 | Figure 3 | no marker legend (diamonds = genus, equal-count and cone-count pairs; squares = Prouhet pairs) | add to the caption | W |
| n15 | b, d, e | Figure 2(a) | the tick labels -3 and -2 touch | re-render (`figures/out/F2.pdf`; outside this round) | W |
| n16 | b | Figure 5 | the vertices carry no order labels | add | W |
| n17 | b-m1 | title | "heat" for "heat invariants" | optional | W |
| n18 | b-m8 | Section 1.1 | the orientability remark should cite what is known, or say that nothing is | add | W |
| n19 | e-m9, e-m10 | bibliography, Theorem 3.11 | volume-year versus online-year; the Wright citation in 3.11(c) is unnecessary since N(2L-3) <= 2L^2 follows from [5, Prop. 3] | harmonise; drop | W |
| n20 | d-m1, d-m2, d-m4..m10 | Sections 1.2, 3 | Melzak's strict inequality; unrefereed sources for data; Problem 4 as the balanced case T(n-1) = 2n; the weak evidence of a bound 120 for n = 5; undefined vocabulary in Remark 3.2; sharpness of Theorem 3.8; non-optimised constants; additive constant in Proposition 3.12 | local edits | W |
| n21 | c-m7, c-m8, c-m9 | Table 3, (14), Remark 4.14 | "competitors" counts the orbifold itself; (14) needs one more line; the exponent N-1 is small on the page | edit | W |

## Disputes settled

* **c-m6, "arccosh(1+x) >= 2x/(1+x) is garbled".** Settled by the LaTeX source (`theory/eigen/diameter.tex`, now in `manuscript.tex`): it reads `\operatorname{arccosh}(1+x)\ge\sqrt{2x/(1+x)}`, the correct inequality that the reviewer also states. The garbling is in the PDF text layer. Not an issue.
* **b-m2, "[15]'s DOI 10.2307/2047071 did not resolve".** Settled by fetching: https://doi.org/10.2307/2047071 redirects to the AMS page of Chang and DeTurck, "On hearing the shape of a triangle", Proc. AMS 105 (1989); Crossref's API has metadata only for the AMS-form DOI (pages 1033-1033). The entry is correct. Not an issue.
* **a-M4, "circular cross-references".** Settled by `note.tex` line 94 against `manuscript.tex` Section 1.2: consistent (I4).
* **b-M3 against arbitrary competitors.** Not settled: the bound v_max <= M n^(1/(2L-3)) was not checked. The bounded-competitor case is settled by computation (I6).

## Recurring themes of earlier rounds

| theme | verdict |
|---|---|
| significance | **not resolved** (a, b, c): Section 4 is effective but impractical and the paper does not say what it adds to the compactness argument (I2); the growth question is conditional (I3, answered); b adds the large-order framing (I6) |
| length | **not resolved**: 33 to 48 pages; three reviewers recommend a split or cuts (I1) |
| attribution | resolved: reviewer e checked 47 citations (27 at statement level); the only loose attributions are n6 to n8 |
| proofs outside the paper | the two appendices are resolved (c and e read Appendix B and Appendix C and rebuilt them); three forms remain: (H1)-(H3) and the trace identity "checked numerically with the repository code" (I5), the recipes behind T(L) (I7), the soundness of the floating-point filter (I8) |

## What a revision should do, ranked

1. **I6.** Prove and state K_mult <= M among orders <= M (the matrix is the Vandermonde-type system in y = a^2); define f(A, M); rewrite the abstract and Section 1.1 accordingly; use min(k_*, M) in Theorem 4.13 and recompute Table 2.
2. **I2.** Add the compactness paragraph, the a-posteriori corollary and its constants on the committed spectra.
3. **I1.** Decide on a split: (a) Sections 2, 3, 5, 6 and Appendices A-C; (b) Section 4 with Section 4.6 and the numerics. Failing that, move Sections 7-8 to the supplement and add the reader's guide.
4. **I5, I8, I7.** Replace each "checked numerically" and each repository-only argument by the proof or a fetched citation (a four-line trace computation; one-line proofs of (H1)-(H3); a sound exact certificate for Remark 3.14; the construction behind each T(L) bound).
5. The MINOR table, of which n1, n2, n5 and n10 are one-line fixes.
