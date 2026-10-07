# ROUND2-CHANGES: retarget to AGAG, significance, restructure, round-2 items

Input: commit `83942cd` (manuscript 37 pp., supplement 12 pp., note 12 pp.) and the five reports
of `review/referee-round-2/` with `VERDICT.md`. Target journal is now **Annals of Global Analysis and
Geometry** (requirements in `AGAG.md`).

Output, built from clean `build/` directories (`latexmk && latexmk` in `paper/jga`, `latexmk note.tex`
twice in `paper/arith`): **manuscript 33 pp.** (slot section included, as a placeholder of five
lines), **supplement 16 pp.**, **note 12 pp.** In all three: 0 LaTeX errors, 0 undefined
references, 0 undefined citations, 0 overfull boxes. No PDF is committed.

## 1. Structure

| § | title | was |
|---|---|---|
| 1 | Introduction; 1.1 Why heat invariants (**new**); 1.2 Prior work and what is new (rewritten) | 1, 1.1 |
| 2 | Heat invariants of constant-curvature orbifolds | 2 |
| 3 | Hearing the signature (adds Proposition 3.12, minimal configurations) | 3 |
| **4** | **From heat invariants to eigenvalues: SLOT** (`\label{sec:eigen}`) | new |
| 5 | What heat does not hear (compressed) | 4 |
| 6 | The rigid case: triangle orbifolds | 5 |
| 7 | Stability | 6 |
| 8 | Computations | 7 |
| 9 | Open problems (restated through T(L)) | 8 |
| A, B | Proofs of the growth results; Computational methods and reproducibility | B, C |

**The slot.** `manuscript.tex`, between the comment lines `%% SLOT FOR THE NEW SECTION` and
`%% END OF SLOT`, immediately before `\section{What heat does not hear}`: Section 4, "From heat
invariants to eigenvalues", label `sec:eigen`, one bold placeholder paragraph. Three other
placeholders refer to it and must be filled with it: the abstract's last clause, the bold
`[SLOT: ...]` sentence at the end of the second paragraph of §1.1, and nothing else (the roadmap
and §1.1 already reference `sec:eigen`).

## 2. What was cut or moved

To the supplement (Online Resource 1):
- the derivation of Proposition 2.7 from the trace formula and the admissibility lemma (old Appendix A)
  -> new §S9; the paper now proves Prop. 2.7 by citing Uçar [Thm 4.20(ii), (4.35)] through the
  closed form of Lemma 2.6 (Remark 2.9). Lemma 2.6's own proof stays in the paper.
- the hand 2-descent for C_{27/2} -> §S8; the paper's proof of Thm 6.8 now gets rank 0 from PARI's
  unconditional 2-Selmer bound r_2 = 0 (`theory/diophantine/data/ranks.txt`: "0 <= rank <= 0 ->
  PROVEN") and points to §S8. Model, torsion and the list of points stay in the paper.
- Table 1 (δ_thm, δ_cert, δ_up) and every main-text use of Prop. S3.1 (R4). The full table, now
  self-contained, is Table S4; the paper keeps one paragraph (end of §7) stating the factors.
- Prop. 5.9 (38 collision-free sums) -> Prop. S2.1; Prop. 5.8 (tangency) -> Prop. S2.2 (R5 in part).
- Appendix C's detailed computations (search keys, T_3 filter arithmetic, script list) -> §S7.

Cut or compressed in the paper:
- §1: old §1.1 (1.7 pp.) rewritten as §1.1 + §1.2 (1.6 pp. together, including the new half page);
  Theorem 1.3 shortened; "What heat does not hear" paragraph folded into the roadmap.
- §2.3 Remark 2.11 reduced to two sentences; the Huber/Buser sentence after Lemma 2.4 removed.
- §3: Remark 3.2 to six lines (details in §S1); N(k) literature paragraph halved; Example 3.12
  shortened; Theorem 3.11(b),(d) absorbed into Proposition 3.12 (new proof of (d) after it).
- §5 (old §4): Theorems 4.4, 4.5 and Corollary 4.6 merged into Theorem 5.4; rigidity proof now
  "Teich is a point" (Troyanov no longer needed); Remark 4.7 removed (its content is in §1.1).
- §8 (old §7): duplicated error-budget, Weyl and fit detail removed (all in §S4).
- Bibliography: 49 -> 40 cited entries (dropped: kac1966, buser1992, wolpert1979, mckean1974corr,
  alloucheshallit1999, aby2015, bgy2020, philippe2008, philippe2010gd, wooley2019, crameri2020,
  schoberl1997, ngsolve, arpack1998, doylerossetti2011, troyanov1991, companion; added
  berardwebb1995, berardwebb2022, iwaniec2002 stays). The FEM software references remain in the supplement.

No proof that a main result depends on was removed without either a citation that proves it
(Prop. 2.7: Uçar; Thm 2.3: Garbin–Jorgenson Rem. 2.7, (2.8)) or a rigorous replacement in the
paper (rank 0: PARI's unconditional Selmer bound), with the removed proof kept in the supplement.

## 3. Significance (new §1.1), verbatim source in `manuscript.tex`, `\subsection{Why heat invariants}`

Arguments, each with a fetched source: locality of short-time diffusion and the germ dependence of
cone terms (Donnelly; DGGW Thm 4.8; Schueth 2025 §1, `review/literature-pass/_fetched/txt/E_schueth2025.txt`
l. 44-80); exact order t^{k-1} of the trace difference; curved cones (Schueth 2025, Abstract and §1);
never isospectral (Dryden–Strohmaier Thm 1.1; Linowitz–Voight Thm A and the sentence after it);
forward reference to §4 with the SLOT sentence; positioning in the line Donnelly; DGGW; Stanhope
(Main Thms 1-2, read in `stanhope2005.txt` l. 37-46); Dryden–Strohmaier; ADFG; Schueth.

## 4. Round-2 items (VERDICT R1-R17) and reviewer MINOR/PRESENTATION items

Status: DONE, PARTIAL, DECLINED (with reason).

| item | disposition |
|---|---|
| R1 significance | DONE: §1.1 (half page) + abstract sentence; physics-first; slot for the eigenvalue theorem |
| R2 length | DONE: 37 -> 33 pp. (moves in §2 above) |
| R3 PTE prior art | DONE: §1.2 second paragraph, Thm C(1) ("forward direction is [Chen, Identity 9, m=3]"), Thm C(3) ("this pair is [Chen, (A.685)]"), Rem. 3.2 ((A.685)-(A.692) = our eight primitive witnesses with orders <= 84; checked against `review/audit-2/pte-witnesses/direct4_N440.txt`); "What we add" recalibrated (separation, Descartes, doubling, growth equivalence, searches); Thm A framed as of Steinig type |
| R4 δ_cert in main text | DONE: Table 1 removed; Rem. 7.1 and §7 no longer use Prop. S3.1; F8 caption says the diamonds are certified in the supplement |
| R5 companion overlap | DONE for the isolation result (note: F9 caption, Table 2 rank cell, §1.1 sentence now cite `gangetal-heat` Thm 6.8); Prop. 5.9 moved to the supplement; arXiv posting of the note is the authors' decision |
| R6 orientability | DONE: paragraph after Thm 1.1 (k = 2g crosscaps, locality, cannot hear orientability). Bérard–Webb verified to concern Neumann-isospectral **flat surfaces with boundary** only (`fetched/berardwebb/`); the sentence says exactly that and that the closed-orbifold case is not known to us |
| R7 T(L) | DONE: Prop. 3.12 (π(T−8)/2 ≤ A_min < 2πT; max(2L+2, N(2L−2)) ≤ T ≤ 6 min((L−1)²+1, N(2L−3))), table 6, 8, 14, 18, 24, 40 (recomputed from Table S1), Problems 1-3 restated; abstract and Thm 1.1(ii) say the exponent is open between 1/2 and 1 |
| R8 Thm 4.4 "explicit" | DONE: now "elementary explicit constant"; sharp part credited as classical |
| R9 compressed proofs | PARTIAL: Thm C(2) displays the rank-(n−1) matrix; Rem. 6.7 became Prop. 7.7 with proof; Thm B determinant and Thm 3.8 unchanged (three referees checked them line by line; no space) |
| R10 Fig. 5 | DONE: caption "in an oblique orthographic view, so the circular rim appears as an ellipse"; citing sentence in §6 gives the elevation 58° (`figures/src/F2.py`) |
| R11 figure decoding | DONE: Fig. 1 (one triangle per panel; values drawn at equal Poincaré-disc coordinates; tips of largest order), Fig. 2 (tones for U* and −V*; padding 1), Fig. 3 (split disc = minimal pair), Fig. 4 (θ values, square-root axis, verticals, sector lines), Fig. 6 (log axes, dashed connectors, split disc), Fig. 7 (worst case over 2^n sign patterns; dotted = real multisets), Fig. 8 (truncation orders; seven pairs; emergence circles). Captions still at most two sentences |
| R12 Table S1 swap | DONE in the supplement text before Table S1 (A′, B′ exchanged when R(U_0) < R(V_0)); the generated caption itself comes from `review/round1-fixes/d2_explicit_pairs.py`, outside this session's scope: **the generator still needs the same clause** |
| R13 "1023 − 0.00×10^0" | DONE as a stated correction next to Table S1 (deficit 9.14×10^−864, computed exactly from `d2_pairs.csv`); **the generator's `fmt_area` still underflows** (outside scope) |
| R14 internal paths, filter arithmetic | DONE in the paper (no repository paths left in the main text; Appendix B points to §S7); §S7 states the T_3 filter's arithmetic (64ε relative, `long double` = IEEE binary64 on arm64 macOS, round to nearest). The repository account and the Zenodo DOI remain authors' decisions (OUTSTANDING) |
| R15 citation locators | DONE: DGGW "orientable" with Thms 5.14-5.15; "[2, Ex. 5.6]"; Prop. 5.22 citation removed; normalisation cited to GJ Rems 2.6-2.7; Linowitz–Voight "Thm A and the sentence following it"; Schueth p. 2 now says what it supports. BGN p. 117: kept (the remark is on p. 117 in the fetched text); Schueth date unchanged (bib from Crossref, vol. 69 (2026), Paper No. 2) |
| R16 2.9e-11 | DONE: §8 now says "relative" and "absolute" explicitly |
| R17 minor list | see below |

Reviewer (a) MINOR: 1 DONE (Thm 1.1(iii) "same number n"); 2 DECLINED (distribution of K_iso: no space); 3 DONE (rigidity without Troyanov); 4 DONE (unknown K, end of §2.3); 5 DONE (pointer to Appendix B/§S7); 6 DONE (Table 1 gone); 7 DONE (Thm 1.3 separates rate and attainment); 8 DONE in paper, account/DOI OUTSTANDING; 9 DONE (correction note; "writes out every pair" now excepts Prouhet L ≥ 4); 10 PARTIAL (Table S1 rows are labelled by kind; no per-diamond index); 11 DONE (diameter "not determined by the signature"); 12 DONE ("primitive or not"); 13 kept (one-line argument already there); 14 DONE (already in §6 opening); 15 DONE ("explicit in the area"); 16 DECLINED (K_mult kept: CONVENTIONS.md); 17 DONE (handles in Thm 3.10; see also §7 item 11).
Figures: Fig. 1 DONE; 𝔥_t vs h_t kept distinct on purpose (h_t is the test function), now defined in the caption; Fig. 2-8 DONE (see R11); "dashed curve non-constructive" PARTIAL (the text calls it the bound of Thm 3.11(a)).

Reviewer (b) MINOR: 1 PARTIAL (GJ (2.8) now the cited source of the heat-case formula; Lemma A.1 moved to §S9 unchanged); 2 DONE (ρ defined); 3 DONE (O(t^K); C(Area(O),·)); 𝔥_t kept; 4 DONE (real-m extension stated after (5)); 5 DONE ("comparing Taylor coefficients"); 6 DECLINED (range claim needs a separate check); 7 DONE (L_* attained); 8 DONE (§7 says δ_thm is far from sharp, with the factors 5×10^2 to 2×10^8); 9 kept (A ≥ 8π ≥ π/2 is immediate); 10 kept (Lemma 3.3 states it); 11 DONE (abstract no longer has the phrase; Prop. S2.1 says 18 ≤ S); 12 DONE (supplement abstract); 13 DONE.

Reviewer (c) MINOR: 1 DONE (R12); 2 DONE (R13); 3 DONE (Rem. 3.2 defines witness, primitive, no triple keys; totals in §S1); 4 DECLINED (heuristic for n = 5 not added; no space); 5 DECLINED (second filter not in the paper; referee's own check); 6 PARTIAL (Problem 3 of Borwein–Ingalls cited; quotes not added); 7 DECLINED; 8 PARTIAL (Ex. 3.12(iii) names the sources; constructions in Table S1 and its data file); 9 DONE; 10 DONE (F_00 = −1/2); 11 DECLINED (notation kept, CONVENTIONS.md); 12 DONE in the paper; 13 DONE ("equal sums of first and third powers").

Reviewer (d) MINOR: 1 DONE (abstract cut to the headline results); 2 DONE (R6); 3 DONE; 4 DONE; 5 DONE; 6 DONE; 7 DONE; 8 DONE; 9 DONE ("hence the same area"); 10 DONE (Prop. 7.7); 11 DONE (W all ones, proof of Thm 3.11(c)); 12 DONE (vacuous exception removed); 13 DONE (gap_3(18) = 1/840 in the proof of Thm 6.5); 14 DONE (aside removed); 15 DONE (R16); 16 DONE; 17 PARTIAL (paths gone from the paper; account OUTSTANDING); 18 DONE (R13); 19 DONE (search size in Appendix B/§S7); 20 kept (p. 117 is where the remark is); 21 DECLINED (displays of ζ_n, r_n unchanged; no space). M4 (Fig. 5) answered by R10.

Reviewer (e): M1 DONE (33 pp.; the editor's 22-25 is not reached without cutting results); M2 DONE (§1.1, §1.2); M3 DONE in part (Table 1 and δ_cert out; Thms 7.4, 7.5, 7.8 kept since Thm 1.3 depends on them); M4 DONE (R5); M5 DECLINED by brief (every figure kept), defects fixed. MINOR m1-m6 DONE (figures); m7 DONE (orientability; mirrors keep the Richardson–Stanhope citation); m8 DONE; m9 DONE (abstract/intro no longer use "s-multisets"); m10 DONE (descent in §S8, PARI in paper); m11 DONE; m12 DONE (Table 1 removed); m13 PARTIAL (paths in §S7; run times not added); m14 DONE; m15 DONE; m16 DONE ("We are not aware", nearest analogues named); m17 kept (Crossref record).

## 5. Retargeting (task 1)

`AGAG.md` records the guidelines (captures of 2025-10-01; the 2026 captures are bot pages). Applied:
JGA wording removed (none left in manuscript or supplement; the AI placeholder now cites Springer
Nature's guidelines); the companion manuscript is mentioned in the text only, not in the reference
list; the supplement is titled "Online Resource 1" and the data statement says so; a "Use of AI
tools" pointer under Statements and Declarations; abstract 150 words plus the placeholder clause.
Not applied (authors' decisions): acknowledgements on the title page; preprints in the list.

## 6. Independent check

A subagent given only the three PDFs and the five round-2 reports with VERDICT.md checked every item.
Resolved by its account: R3, R4, R5, R6, R7, R8, R10, R16, and the checks on the significance
subsection, section order, Chen credit, δ_cert placement, the note, absence of JGA wording and of
dangling references. Its mathematical spot-checks (Prop. 3.12, the proof of Thm 3.11(d), Prop. 7.7
with 498 + 42a², Prop. 7.6(i), Lemma 2.8) found no error. Its "still to fix" list and what was done:

| # | finding | action |
|---|---|---|
| 1 | §4 unwritten; abstract and §1.1 placeholders | by design (slot for the parallel session); Zenodo, contributions, AI text remain authors' placeholders |
| 2 | body about 30 pp. vs editor's 22-25 | not acted on: the brief's target was ≤ 33 pp., met; moving Thms 7.4-7.8 would leave Thm 1.3 without its proof in the paper |
| 3 | Table S1: fix in the table, not as prose | not possible in scope (generated by `review/round1-fixes/d2_explicit_pairs.py`); recorded in OUTSTANDING §9 |
| 4 | internal paths in supplement and note; account; run times | OPEN (authors/archive decision; paper's main text is clean) |
| 5 | Thm 6.8 proof pointed to Appendix B for the Selmer bound | FIXED: now Section S7 |
| 6 | §1.2 cited Thm 3.4 for finiteness of signatures of given area | FIXED: Cor. 3.5 |
| 7 | Fig. 2 colours not named | FIXED in the caption ((a) orbifold colours; (b) black U*, grey −V*, padding 1) |
| 8 | Fig. 3 dashed bound is a guarantee for s ≥ 4 | FIXED in the caption |
| 9 | Fig. 4(a) cone points not drawn | FIXED in the citing sentence ("cone points unmarked") |
| 10 | terse proofs | PARTIAL: Prop. 7.6(ii) now cites Thm 7.4(b) with η = O(s^k); Thm C(2) matrix rows given; Thm B sign count and Lemma 2.5 boundary term unchanged |
| 11 | Thm 3.10: smaller genus "any g ≥ 1" not justified (construction may end at g_0 = 2) | FIXED: weakened to "any prescribed g ≥ 2" (handles added to g_0 ≤ 2) |
| 12 | minor statements | PARTIAL: reason after "exactly L iff Σz^{2L−1} ≠ 0" added (Lemma 2.10); others declined for space |
| 13 | abstract bound false for small areas | FIXED: "between constant multiples of the square root of the area and of the area" |
| 14 | notation overloads | DECLINED (CONVENTIONS.md) |
| 15 | dense displays | DECLINED (space) |
| 16 | Thm 1.3 discussion should say δ_thm far from sharp | §7 says it with factors; intro sentence dropped for space |
| 17 | Table S4 (2,2,2,2,3) δ_thm 2.72e−12 vs referees' 2.730e−12 | not changed: the table rounds down from `threshold_results.json`; the stored value is 2.72978×10^−12, which rounds down to 2.72 (both referees rounded to nearest) |
| 18 | optional (results table, 525-classes paragraph) | DECLINED (space) |

After these fixes: manuscript 33 pp., supplement 16 pp., note 12 pp.; 0 errors, undefined
references or citations, overfull boxes in each; `make_tables.py --check` reports the tables current.
