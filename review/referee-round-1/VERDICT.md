# referee-round-1: verdict

Input: `paper/jga` at repository commit `8d07615` (manuscript 35 pp., supplement 8 pp.; companion note 12 pp. seen only by the editor). See [`README.md`](README.md) for hashes and personas. Reports: `a-inverse-spectral-sceptic/`, `b-trace-formula-analyst/`, `c-pte-combinatorialist/`, `d-jga-rigour-referee/`, `e-handling-editor/` (each `REPORT.md`). Reviewers (a), (b), (c) and (e) could not write files; their returned text was saved verbatim with a provenance line. Reviewer (d) could not hand its report back either; the orchestrating session recovered its final message verbatim from its transcript.

## 1. The five recommendations

| reviewer | persona | recommendation | confidence | MAJOR issues raised |
|---|---|---|---|---|
| (a) | inverse-spectral sceptic | **major revision** | high on correctness, moderate on fit and novelty | 3 (M1-M3) |
| (b) | trace-formula analyst | minor revision | about 80% on correctness | 0 |
| (c) | PTE combinatorialist | minor revision | 0.8 correctness, 0.5 fit | 0 |
| (d) | JGA rigour referee | minor revision | about 85% correctness, 60% fit | 0 |
| (e) | JGA handling editor | desk-reject probability **about 25%**; if sent out, **major revision** (about 60%; about 30% reject-and-resubmit-in-pieces; about 10% minor) | as stated | 3 (M1-M3) |

All five found no error in any theorem, and between them they independently reproduced nearly every exact computation: the heat coefficients, the witnesses, the n = 4 search to 440 and n = 5 search to 120, the full collision census to S = 4800, Table S3, the elliptic-curve data (rank 0, E(Q) = Z/2 x Z/6), the Hurwitz determinant, and most of Table 1. The disagreement is about framing, scope and venue fit, not correctness.

## 2. Deduplicated issue table

Severity is my assessment after checking against the paper and repository. "Reviewers" lists who raised it. "Needs" is M (mathematics), C (computation) or W (writing). "Space" is whether the fix is space-neutral in the 35-page manuscript.

| ID | reviewers | severity | location | issue | resolution | needs | space |
|---|---|---|---|---|---|---|---|
| V1 | a-M3, b-m2, c-m4, d-m3, e | MINOR (citation error, but 5 of 5 flagged it) | Sect. 1.1, l. 173 and ref. [17] | The paper says "Philippe showed that a hyperbolic triangle group is determined by its length spectrum, in practice by its first two or three lengths [Thm A]". The cited paper's title is "Les groupes de triangles (2,p,q) sont déterminés par leur spectre des longueurs"; (3,3,12) is not of that type. The bibliography also holds Philippe's (r,p,q) paper (Geom. Dedicata 149), which is not cited. | State the (2,p,q) hypothesis; cite the (r,p,q) paper for whatever it proves; drop "in practice by its first two or three lengths" unless it is in the source. | W | neutral |
| V2 | a-M1, e-M3, c-m1, c-m7, d-m7c | MINOR (abstract overclaim) | abstract; Thm 1.1(ii); Thm 1.2 | (i) "the exact threshold at which two invariants stop sufficing, sum 17" is a first failure: Prop. 5.9 shows two invariants suffice again at 38 later sums (19, 21-25, 27-30, ...). (ii) Within all signatures two invariants already fail at sum 15 ((5,5,5) vs (0;2,2,2,10)); the threshold is relative to triangle orbifolds. (iii) The growth law is only reduced to the open N(k) = O(k); the unconditional content is sqrt(A) <= f(A) <= A/pi + 4. | Say "first failure"; say "among triangle orbifolds"; state in the abstract that the growth rate is equivalent to, not decided by, the PTE problem (the abstract already calls it "a classical open question"). | W | neutral |
| V3 | a-M2, e-M1, b-m1, b-m4, c-m2, c-m9, d-m7b, d-m8, d-m9 | MINOR as written (the body is candid), MAJOR in the eyes of (a) and (e) | abstract; Thm 1.3; Sect. 6; Remark 6.1; Sect. 7 | Stability is a statement about an algebraic map c -> orders: genus 0 and known n; constants depend on the unknown true orders; errors are on the c_j, not on eigenvalues; for "positive real orders" the heat invariants are a formal continuation (Prop. 2.8 is for integer m); the 1/2 sharpness is for a double order and all-equal orders only; "certified" rests on a-posteriori, heuristic error bars with no double-window rerun. | Put these hypotheses in the abstract and Thm 1.3; call the real-order results formal; say "validated" rather than "certified"; optionally add a uniform-in-class corollary (n fixed, orders <= mu). | W (the corollary would be M) | neutral if the abstract is trimmed |
| V4 | a-M3, b (P), d (uncited), e | MINOR | Sect. 1.1 | Positioning: no citation of Brooks-Perry-Petersen, Sunada, Zelditch / Hezari-Zelditch, Osgood-Phillips-Sarnak; Abreu-Dryden-Freitas-Godinho is in the .bib but not cited in the text (b, d: nearest precedent for finitely many heat invariants fixing singular-point data); "first" claims are asserted without a documented search. | Add the missing context in 3-4 sentences; keep "to our knowledge" qualifiers. | W | +3 lines |
| V5 | e-M2, a-m1, d-m2 | MINOR | Remark 4.7 | "All but countably many points have heat traces different from a given one" along a "Thurston length coordinate" is asserted without proof or definition. | Give the 2-line argument or delete the claim. | W | +3 lines or negative |
| V6 | c-m6, b-m6, d-m1 | MINOR | Fig. 2 and caption, l. 438 | The caption says "525 area classes with s <= 7/5" without saying how they were selected. | Say: the 525 areas realised by genus <= 2, n <= 4, orders <= 12; each class is enumerated completely. | W | neutral |
| V7 | c-m6, b-m9, d-m6a | MINOR | Remark 3.2 | "15 witness configurations ... at most 130 and 35 ... at most 220" is not reproduced by three reviewers (14 primitive and 30 primitive; 17 and 49 with multiples). | Replace by the recounted numbers and define "configuration". | C (already done) | neutral |
| V8 | c-m6, d-m6b | MINOR | Example 3.12(iii), L = 4..7; Fig. 2 diamonds | The pairs rest on solutions named in other papers; the pairs themselves are not written out. | List them, with areas and shared counts, in the supplement. | C | supplement only |
| V9 | a-m6, b, c, d (P) | MINOR | Remark 3.13 | "admits three positive real partners" should read "a partner triple of positive reals". | Reword. | W | neutral |
| V10 | c-m5 | PRESENTATION | Thm 3.8, last sentence | "|U*|+|V*| = 2L+2 implies |g-g'| = 1" needs the hypothesis g != g' inside the sentence. It is in the preceding clause. | Repeat the hypothesis. | W | neutral |
| V11 | d-m5 | MINOR | Thm 5.10, descent for E | The mod-5 argument lists three cases and omits 5 not dividing Me, where the right side is = +-3 mod 5, also a non-residue. The claim stands. | Add the case; cite the independent rank-0 confirmation. | M (trivial) | +2 lines |
| V12 | b-m7, c-m10, d-m10 | MINOR | [19] (BGN), [5], [38], [37], [34], [35], [40], [12] | BGN treat integer Lambda while the paper's is 27/2; unchecked page and problem numbers (Borwein-Ingalls, Melzak, Wright); small year and page discrepancies in Crossref (Schueth 2025 vs 2026, [35] 2019 vs 2020, [40] 2018 vs 2019). | State exactly what is quoted from [19]; check against originals; fix years. | W | neutral |
| V13 | b-m11 | MINOR | Remark 4.7, ref. [8] | "genus at least one" for Dryden's finiteness may understate it (arXiv math/0411290). | Check the theorem. | W | neutral |
| V14 | c-m8 | MINOR | abstract | Add "orientable, without reflectors"; heat does not hear orientability. | One phrase. | W | neutral |
| V15 | c-m6, d-m7a | MINOR | abstract vs Thm 1.3 | Abstract says "all n >= 2 orders are equal"; Thm 1.3 says k = n >= 3. | Align. | W | neutral |
| V16 | a-m2/m3, b-m10, c-m11, d-m6c | MINOR | data statement; Appendix B | Data link points to a GitHub account that matches no author; supplement cites an internal path; "repeated independently, floating point only rejecting where certified" is vague; [20] is "in preparation" (say no proof depends on it). | Make provenance consistent; put search bounds and checksums in the supplement. | W | neutral |
| V17 | e (P1), a-P1, b-P3, c-P1, d-P1 | PRESENTATION (editorial risk) | whole paper | Four or five loosely linked strands in 35 pp.; editor sees "borderline for JGA", an elementary analytic core, and suggests splitting. | See section 4 (what to cut). | W | negative |
| V18 | b-P1, c-P3, d-P2 | PRESENTATION | notation | P_n (spheres) vs P_k (power sums); D three ways; mu two ways; lettered Theorems A-C among numbered ones. | Rename. | W | neutral |
| V19 | d-m4, d-P4, b-P6 | PRESENTATION | abstract; front matter | Abstract nearly a page; line numbers and "1 1 Introduction" from the template. | Shorten the abstract; check the class option. | W | negative |

Items raised and found **not** to be defects: the "sign error in Lemma 3.3" (b-m3, c-m3, d-m4). The printed text is d = 2(g'-g) + n' - n. Reviewers (b), (c) and (d) read plain text extracted from the PDF, which drops the prime marks; the rendered page 12 shows the correct sign (reviewer (a) called it an extraction artefact). ANSWERED IN PAPER.

## 3. Every MAJOR item checked against the repository

| item | claim | status | evidence |
|---|---|---|---|
| a-M1 | prefix measure non-canonical; "threshold 17" is a first failure; growth only reduced to PTE | **PARTLY CONFIRMED**: wording only. The growth being open is **ANSWERED IN PAPER** (abstract: "a classical open question"; Problems 1-3). The "threshold" wording is confirmed by Prop. 5.9 (38 later collision-free sums). Not a mathematical error, so I class it MINOR (V2). | manuscript abstract; Prop. 5.9; reviewers (b), (c), (d) reproduced the 38 sums |
| a-M2 | stability concerns an algebraic map on non-geometric data | **ANSWERED IN PAPER** for the body (Remark 6.1 and the sentence "The bounds concern errors in heat invariants, not eigenvalues", Thm 1.3 text, Remark 6.7). **CONFIRMED** that the abstract omits genus 0, known n, a-posteriori constants and the formal meaning of real orders (V3). | `paper/jga/manuscript.tex` Sect. 1 and 6; `theory/stability/blind/PROTOCOL.md` ("genus 0 and exactly n = 3 ... used"); G7-VERDICT G7-24 |
| a-M3 | positioning and novelty unsubstantiated; Philippe misdescribed | **CONFIRMED** (Philippe, V1; missing classical context, V4). Not a mathematical issue. | `references.bib` title of philippe2008; tex l. 173 |
| e-M1 | same as a-M2 | as a-M2 | as a-M2 |
| e-M2 | Sect. 4 largely classical; Remark 4.7 unproved | Novelty: **ANSWERED IN PAPER** (Prop. 4.1 is credited as classical; G7-CHANGES G7-2 demoted Sect. 4). Remark 4.7: **ANSWERED IN REPOSITORY BUT NOT PAPER**: the argument is in `theory/locality/proof.md` ll. 185-210 (uncountably many isometry classes per signature, a countable length set per orbifold). | repo file cited |
| e-M3 | headline growth question not answered; "iff" is a reformulation | **ANSWERED IN PAPER** (stated as equivalent to an open problem); the abstract wording could be firmer (V2). | abstract; Thm 3.11 |

Result: **no FATAL and no mathematically CONFIRMED MAJOR item.** What is confirmed is a set of statement-precision and citation defects (V1-V4), which I rate MINOR. Reviewers (a) and (e) rated the same facts MAJOR; I record that disagreement in section 5 and do not use it to pass the gate.

## 4. Space accounting (manuscript is at 35 pp. with almost no slack)

Space-neutral: V1, V2, V3 (if the abstract is trimmed in step), V6, V7, V9-V10, V12-V16, V18. Net additions: V4 (+3 lines), V5 (+3 lines, or delete the remark and save 4 lines), V11 (+2 lines). Roughly **+8 lines**, under half a page.

To pay for them and to answer V17 (length and focus), candidates in order of cost:
1. Remarks 3.2 and 3.13 (search logs, about 0.4 page) to the supplement, keeping one sentence each. Removes the counts that three reviewers could not reproduce.
2. Lemma 2.5 (admissibility of the heat function; standard, about 0.5 page) to the supplement (flagged by a-m5, b-P).
3. Table 1 columns beyond delta_thm and delta_cert, and the longer certificate discussion in Sect. 6 (about 0.5 page), to the supplement (d-P1).
4. The abstract: cut to about two-thirds length (V19); this funds V3.
5. Move Appendix A (proof of Thm 3.11) into Sect. 3, or conversely trim it (d-P8); neutral.
Cuts 1-4 free about 1.5 pages, enough to absorb V4, V5 and V11 with room to spare. Splitting the paper (a, c, e) is a larger decision, not a fix; see section 6.

## 5. Where reviewers disagree, and my assessment

1. **Overall verdict.** (a) and (e): major revision. (b), (c), (d): minor. All five agree the mathematics is correct; the split is about whether the framing (abstract thresholds, stability scope, "first" claims) and the thin analytic core justify a major revision. My assessment: the framing defects are real but mechanical; I agree with (b), (c), (d) on severity of the facts, and with (a), (e) that an editor reading the current abstract would see overclaims.
2. **Lemma 3.3 sign.** (b), (c), (d) say wrong; (a) says artefact. Verified on the rendered page: correct as printed.
3. **Fig. 2 "exact K_mult".** (d) feared the dots underestimate K_mult because competitors might be capped at orders <= 12. Checked: `theory/signatures/area_classes.py` enumerates complete area classes (33,946 signatures in 525 classes, including orders up to 90, e.g. (0;2,36,60) in s = 41/90); (b) independently recomputed the histogram 17/311/197 and found it consistent. The dots are right; the caption is incomplete (V6).
4. **Fit for JGA.** (a) and (e) doubt it; (b), (c), (d) lean to accept after revision with moderate confidence (0.5-0.6). I agree it is borderline: the analytic content is classical, the new content is arithmetic and perturbation-theoretic. This is an editor's judgement, and the 25% desk-reject estimate comes from there.
5. **Pencil counts.** Three reviewers could not reproduce 15 and 35. The repository data reproduce 25 and 61 (only three entries bounded, as the paper says in parentheses) and give 14 and 30 when all entries are bounded. So the printed 15 and 35 are wrong (V7).

## 6. GATE: **FAIL**

The gate has two conditions: no confirmed MAJOR or FATAL, and every recommendation minor or accept.
- Condition 1: met on my assessment (no mathematically confirmed MAJOR; V1-V4 are MINOR defects).
- Condition 2: **not met.** Reviewer (a) recommends major revision, and reviewer (e) expects major revision if the paper is sent out. I did not downgrade a reviewer's recommendation.

Blocking items, i.e. what stands behind the two major-revision recommendations:
1. **V3** abstract and Thm 1.3 scope of the stability claim (a-M2, e-M1).
2. **V2** abstract wording of the triangle "threshold" and of the growth law (a-M1, e-M3).
3. **V1, V4** the Philippe misdescription and missing classical context (a-M3).
4. **V5** the unproved Remark 4.7 claim (e-M2).
5. **V17** length and focus: (e) puts about 30% on "reject-and-resubmit in pieces", and (a), (b), (c), (d) all suggest moving material out.

Everything in 1-4 is writing; none needs new mathematics or computation beyond what is already in the repository. A second round on the revised manuscript would be needed to clear reviewers (a) and (e). The editorial question in 5, whether to submit as one paper or split, is for the authors.

## 7. Side effects and caveats

- Reviewer (d) ran `pip install cypari` outside its scratch folder, which put PARI bindings into the user's Python site-packages (disclosed in its report). Nothing else was written outside the scratch folders.
- Reviewers (a), (c), (e) could not recompute the finite-element spectra of Sect. 7, the proof of Prop. 6.9, or Example 3.12(iii); those remain checked only by the authors.
- The manuscript, figures, code and data were not touched.
