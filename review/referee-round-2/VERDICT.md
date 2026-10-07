# VERDICT: referee round 2

Input: the PDFs of `README.md` (manuscript 37 pp., supplement 12 pp., companion note 12 pp.; sources
of commit `d7ed90d`). Reports: `a-isospectral-constructor/`, `b-orbifold-trace-formula-analyst/`,
`c-equal-power-sums-combinatorialist/`, `d-jga-regular-referee/`, `e-jga-handling-editor/`.

No reviewer could write files, so each `REPORT.md` is its returned text, saved verbatim with a
one-line provenance comment. Reviewers (c) and (d) were cut off by a connection error and were
resumed once, with their context intact, to finish and return their reports.

## 1. Recommendations

| reviewer | recommendation | confidence | mathematical errors found |
|---|---|---|---|
| (a) isospectral constructor, sceptical of the topic | **major revision** | high on correctness, moderate on the recommendation | none |
| (b) orbifold trace-formula analyst | **minor revision** | high (analysis), moderate (fit) | none; every proof the main results depend on is complete where it appears, Appendix A included |
| (c) PTE / equal-power-sums combinatorialist | **major revision** | high (Sections 3, 5, App. B), moderate overall | none (one caption typo in Table S1) |
| (d) JGA regular referee | **major revision** | high (correctness), moderate (recommendation) | none; 23 citations spot-checked, none wrong in substance |
| (e) JGA handling editor | **major revision**; desk decision **send to review** | moderate (about 65%) | none |

**Editor's desk-reject probability: 35%** (round 1: 25%).

All five reviewers independently recomputed most of the checkable claims and agree with every one:
- the cone polynomials and α_k (also against quadrature of the trace-formula integrals);
- Theorems A–C;
- every printed pair of Table S1 with its exact shared count;
- the n=4 search counts 16/33/107;
- the n=5 and (3,5) search sizes (c extended n=5 to orders ≤200: still no witness);
- the 83 triads, Table S2 and Theorem 5.4;
- the 38 collision-free sums up to 4800;
- Theorem 5.10 (PARI: rank 0 proven, torsion Z/2×Z/6, conductor 90);
- the δ_thm column of Table 1 and the Section 6 constants.

Every objection is about significance, length, attribution, structure or presentation.

## 2. Deduplicated issues

Severity is my assessment after checking. Where it differs from a reviewer's, §4 says why.

Status:
- **CONFIRMED**: the issue is real as stated.
- **ANSWERED IN PAPER**: the manuscript already does what is asked.
- **ANSWERED IN REPOSITORY BUT NOT PAPER**: the repository has the answer and the paper does not.
- **NOT CHECKED**: minor items taken as reported.

The "needs" column says whether a fix needs mathematics (M), computation (C) or writing (W).

| ID | reviewers | severity | location | issue | status (evidence) | resolution | needs | space |
|---|---|---|---|---|---|---|---|---|
| R1 | a M1, b M2, c M3, d M1, e M2 | **MAJOR** | §1, §1.1 | The paper does not argue why counting heat invariants matters for inverse spectral geometry (the spectrum is what one has; no c_j is computable from finitely many eigenvalues; heat invariants are blind inside a signature, where every 2-D isospectral pair lives). The new content is mostly algebraic and arithmetic, so the fit to JGA is questioned. | **CONFIRMED**. No paragraph in §1 addresses it. `review/literature-pass/NOVELTY.md` assesses novelty, not significance. | A half-page motivation in §1. Candidate contents: wave-trace/t=0 singularity reading; variable or unknown curvature where only local invariants are available (Schueth); why the exhibited collisions are never isospectral (different signatures, Dryden–Strohmaier). Optionally new analysis (d M1: a diameter-free Thm 4.4; a link from finitely many eigenvalues to c_1..c_n). | W (M optional) | +0.5 p; pay with R2 |
| R2 | a M3, b M2, c M3, d M2, e M1, e M3 | **MAJOR** | §2.2, §4, §6, §7, Table 1 | Length not earned (37+12 pp.). §2.2 re-derives Uçar's coefficients; §4 is classical; §6's error model is on c_j with constants at the unknown orders, and δ_thm sits 3–7 orders below δ_cert; §7 is illustration. Editor targets 22–25 pp. | **CONFIRMED** (the paper itself calls §2.2/§4 classical and §7 unused in proofs). The scope limits of §6 are ANSWERED IN PAPER (Remark 6.1, "Three limits of scope"), but the structural request stands. | Move §7 and most of §6 (Thms 6.4, 6.5, 6.8 constants, Table 1) to the supplement, keeping Thm 1.3 qualitatively with Prop. 6.6/Rem. 6.7. Compress §4 to about one page. Shorten §2.2 to a citation of Uçar plus the closed form (5) and Lemma 2.8. | W | saves roughly 8–12 pp. |
| R3 | c M1 (also a: Thm A classical) | **MAJOR** | Thm C(1), C(3), Rem. 3.2, §1.1 "What we add", Ex. 3.12(i) | PTE-side prior art not credited in the main text. Chen's survey lists [3,10,15,30]=[4,5,21,28] as A.685 and the other primitive n=4 witnesses up to 84 as A.686–A.692. Chen's Identity 9 with m=3, (3.27)–(3.28), is the forward direction of the pair criterion Q(z)−Q(−z)=2κz³ of Thm C(1). | **CONFIRMED; ANSWERED IN REPOSITORY BUT NOT PAPER**: `review/audit-2/REGISTER-ADDENDUM.md` H9 and `review/audit-2/literature/check_solutions.txt` (A.685, A.686, A.692 verified). Identity 9 read in the fetched survey text (`review/referee-round-1/c-pte-combinatorialist/scratch/chen.txt`, l. 4388–4425). Only the supplement mentions A.685. | Credit Chen A.685–A.692 in Thm C(3)/Rem. 3.2 and Identity 9 in Thm C(1). Recalibrate "What we add" to: separation T≥2L+2, the Descartes imbalance bound, doubling, the growth equivalence, the exhaustive counts. Frame Thm A as Steinig-type uniqueness extended to complex multisets plus the Orlando determinant. | W | about 4 lines |
| R4 | d M3, a M3, a m6, b m12 | **MAJOR** | Table 1, Rem. 6.1, §6 end; supplement Prop. S3.1 | The δ_cert column of a main-text table, and the a-posteriori certification of Rem. 6.1, rest on Prop. S3.1, which is stated and proved only in the supplement (dense statement, one-paragraph proof). | **CONFIRMED** by reading the LaTeX (`manuscript.tex` Table 1 caption and Rem. 6.1 cite `\sref{prop:S5}`). No main theorem depends on it. | Either move Prop. S3.1 with a fuller proof to an appendix, or drop δ_cert/δ_up and the F8 diamonds from the main text (goes with R2). | W | +1 p, or saves 0.5 p |
| R5 | e M4 | **MAJOR** | §1.1, §5.1–5.2; note Fig. 1, Table 2 | Division of material with the companion note. The note's F9 caption and its Table 2 (rank 0 at Λ=27/2) restate the conclusion of Thm 5.10. Both papers use the C_Λ/BGN framework and the S≤4800 enumeration behind Prop. 5.9. | **CONFIRMED** (`paper/arith/note.tex` l. 320, 385). Mitigation: the note cites the paper for the spectral consequences at S=18 (`gangetal-heat`), and the manuscript says no proof depends on the note. Not duplicate publication. | State the division explicitly in both. The note cites Thm 5.10 rather than restating it. Move Prop. 5.9 / Table S2 to the note or the supplement. Post the note to arXiv so it can be cited. | W | saves about 0.5 p |
| R6 | a M2, d m2, e m7 | MINOR (a: MAJOR) | §1 definition of Sig, Thm 1.1(i) | A cone-point orbifold on a non-orientable surface with k crosscaps has χ = 2−k−Σ(1−1/m_i). With k=2g it has the same area and cone orders as the orientable genus-g one, hence the same heat invariants (Prop. 4.1 mechanism). So heat invariants cannot hear orientability, and "genus" in Thm 1.1 is meaningful only within the orientable class. Relevant literature: Bérard–Webb. | **CONFIRMED** (χ computation above). Not treated anywhere in the repository. The theorem is correct as stated ("among all closed orientable"), and §1 already says non-orientable orbifolds "are not considered". | Add one sentence stating the phenomenon and citing Bérard–Webb. Optionally extend Thm 1.1 to locally orientable orbifolds, determining (χ, cone orders). | W (M optional) | 2 lines |
| R7 | c M2, a M5 | MINOR (c, a: MAJOR) | Thm 1.1(ii), §3.3, Thm 3.11, Problems 1–3 | State the growth result through the minimal configuration size T(L) with explicit constants (A_min(L) ≍ T(L); N(2L−2) ≤ T(L) ≤ 6((L−1)²+1)), with a table of best known T(L): 6, 8, 14, 18, 24, 40 for L=2..7. Say in the abstract that the exponent is undetermined between 1/2 and 1. | The abstract part is **ANSWERED IN PAPER** ("grows at least like the square root of the area; whether it grows linearly is equivalent to the open question…"). The T(L) restatement is a strengthening, not a defect: T_L is already defined for genus-changing pairs in Rem. 3.13, and all bounds are in the proofs. | Define T(L) for all configurations, state A_min ≍ T with the constants from the proof of Thm 3.11, add the 6-row table, and restate Problems 1–3. | W (M light) | +0.3 p |
| R8 | b M1, d M1(part), a m11 | MINOR (b: MAJOR) | Thm 4.4, §1.1 | The "explicit" bound has the non-spectral factor e^{3·diam}. Only the exponent and t^{−1/2} are sharp, and those are classical. | **ANSWERED IN PAPER**: after Thm 4.4 the paper says "The explicit constant is qualitative … only the exponent and the factor t^{−1/2} are sharp", and §1 says "explicit but qualitative constant". | Either tone down "explicit" further in §1.1, or prove a diam-free constant via thick–thin plus Buser counting (new mathematics). | W (or M) | 0 |
| R9 | a M4 | MINOR (a: MAJOR) | Thm B, Thm 3.8, Thm C(2), Lem. 2.5, Prop. 6.6(ii) | Proofs too compressed to check without redoing them. | **ANSWERED IN PAPER** (complete): (b) checked Lem. 2.5 and Thm B; (c) checked Thm 3.8 and C(2); (d) checked Lem. 2.5, Thm 3.8 and Thm B line by line, and all found them complete; (a) also verified every statement. Terse, not incomplete. | Add 2–3 sentences each where space allows (displayed rank matrix for C(2); sign bookkeeping for det M). | W | +0.3 p |
| R10 | b, a, c, d M4, e m1 | PRESENTATION (d: MAJOR) | Fig. 5 (F2), p. 20 | The rim is drawn as an ellipse (aspect about 1.18), but the caption says "Exact tilings of the hyperboloid". (d) reads it as a stretched, non-conformal Poincaré disc. | **ANSWERED IN REPOSITORY BUT NOT PAPER.** `figures/src/F2.py` draws the cap of the upper sheet of the hyperboloid in an orthographic view at elevation 58°, so the circular rim projects to an ellipse; it asserts every tile angle and area exactly. (d)'s "stretched disc" reading is wrong, but the caption no longer says "oblique orthographic view": that clause was dropped in this session's caption cut (`FIGURE-RESTORE.md`). | Restore "in an oblique orthographic view" to `\figcapTwo`. | W | 0 |
| R11 | a, b, c, d, e (figure notes) | PRESENTATION | Figs 1–4, 6–8 | Missing decoding: Fig. 4(b) square-root λ-axis and the grey verticals marking the members of (a); Fig. 3 split disc = (2,8,8)/(3,3,12); Fig. 2 colour key (teal/orange vs black/grey); Fig. 8(a) truncation orders d₃t, +d₄t², +d₅t³; Fig. 8(b) shows the 7 pairs with ϑ=0 of the 28; Fig. 6 log axes and dotted connectors; Fig. 1 shows one triangle (the upper sheet) per panel, how the values were mapped onto the schematic shape, and "darkest tip" vs the two order-8 tips; Fig. 7 how the worst-case curves were computed. (e) also judges Figs 1, 4(a), 5 decorative. | **CONFIRMED.** Most of these were stated in the round-1 captions (`figures/captions.tex` before `dbc4b05`) and were removed by the two-sentence cap of this session. | Add the decoding as short clauses inside the two sentences, or into the sentence of the text that cites the figure. Keeping or dropping the decorative figures is the authors' call (the brief required F1, F2, F6). | W | +3–6 lines |
| R12 | c m1 | MINOR | Table S1 caption | σ₁ = (1; qU₀ ∪ pB′) and σ₂ = (0; qV₀ ∪ pA′) as written force p/q<0. The script swaps A′ and B′ when r₀<0; the caption omits the swap. | **CONFIRMED** (`review/round1-fixes/d2_explicit_pairs.py` l. 54–57 and 66–74; caption text from l. 151–176). | Add "(A′ and B′ exchanged when R(U₀)<R(V₀))" in `d2_explicit_pairs.py`, which generates the caption. | W | 0 |
| R13 | a m9, c m2, d m18, e m14 | MINOR | Table S1, L=6 Prouhet row | "1023 − 0.00×10⁰" is a formatting underflow. | **CONFIRMED** (`supplement.tex` generated table). | Print the deficit's exponent (format in `d2_explicit_pairs.py`). | C/W | 0 |
| R14 | a, b, c, d, e | MINOR | App. C, supplement, data statement | Internal paths (`review/audit-2/…`, `review/round1-fixes/…`); repository account matches no author; T_3 filter platform/format not stated. | **CONFIRMED.** Round 1 declined this as the authors' decision. The `long double` point matters: on this machine `long double` is IEEE double (project memory). | Neutral archive paths in the Zenodo deposit; state the filter's arithmetic. | W | 0 |
| R15 | d m3–m8, m20; e m17 | MINOR | §1.1, §2, Rem. 2.11 | Citation precision: DGGW Thm 5.15 needs "orientable"; "[2, §5.6]" is Example 5.6; Prop. 5.22 concerns the spectrum; the DS normalisation is stated in GJ Rem. 2.6; Linowitz–Voight "sentence after Thm A"; BGN p. 117 locator; Schueth date. | **NOT CHECKED** (d reports none wrong in substance). | Fix each locator. | W | 0 |
| R16 | d m15 | resolved | §7 Error budget | Is 2.9×10⁻¹¹ used twice (eigenvalue relative error, D(t) error) a slip? | **ANSWERED IN REPOSITORY**: `numerics/REPORT.md` l. 281 ((2,8,8) Dirichlet, first 500: 2.9e-11 relative) and l. 389 (total error in D ≤ 2.9e-11). Both are genuine; it is a coincidence. | Optionally give the D-bound as 2.9×10⁻¹¹ (absolute) to make the distinction visible. | W | 0 |
| R17 | b, c, d, e (minor lists) | MINOR | various | Representative items: ρ undefined in the proof of Thm 2.3; real-m extension of b_l; Rem. 2.9 "putting u=it/2"; Prop. 6.2 diagonal formula covers F_{ν+1,ν+1}, with F₀₀=−1/2 stated separately (CONFIRMED, wording); Thm 3.11(e) case W empty (bound still holds); Rem. 6.7 to a proposition; abstract "n invariants suffice" should read "among spheres with the same n"; "between 19 and 4800" vs 18≤S; s-multisets clash with s=Area/2π; Ex. 3.12(iii) recipe; Thm 3.10 wording; notation overloads (e_k, σ, ψ, φ). | Spot-checked where marked; otherwise **NOT CHECKED**. | Each a one-line edit. | W | about 0 |

## 3. FATAL and MAJOR items checked against the repository

There is no FATAL item. No reviewer found a mathematical error, and the four reviewers who could check
them (a–d) recomputed the main results exactly.

The MAJOR items that survive checking are **R1, R2, R3, R4, R5, all CONFIRMED**:
- R3 is answered in the repository (audit-2 H9) but not in the paper.
- R1, R2, R4 and R5 are structural or expository. They need writing, not new mathematics; R1 needs mathematics only if the authors choose to add new analysis.

Four reviewer MAJORs were downgraded after checking:
- **R6, orientability.** The theorem is correct as scoped; one sentence closes the gap.
- **R7, T(L) restatement.** A strengthening, not a defect.
- **R8, Theorem 4.4 constant.** Already stated in the paper.
- **R9, proof compression.** Three other reviewers checked these proofs line by line and found them complete.

R10 is (d)'s figure MAJOR. It is wrong in substance (the projection is correct, see `F2.py`), but it exposes a caption omission introduced in this session.

## 4. Where reviewers disagree

**Severity.** (b) recommends minor revision; (a), (c), (d), (e) recommend major. They do not
disagree about correctness: all five find the mathematics correct. They disagree about whether the
paper earns its length and fits JGA. (b), the analyst closest to the paper's analytic core, judges
the fit acceptable and the defects to be framing. The other four judge the new content too
algebraic and arithmetic for the length. My assessment: the four have the stronger case. The paper
itself labels §2.2 and §4 classical and §7 unused in proofs, and R2 is cheap to fix.

**Fig. 5.** (d) says the figure is anisotropically stretched and "not exact". (a), (b), (c) and (e)
ask only for the projection to be named. Settled by the source: `F2.py` is an exact orthographic
projection of the hyperboloid, with angle and area assertions. The others are right; (d) is wrong on
substance and right that the caption misleads.

**Orientability.** (a) rates it MAJOR; (d) and (e) minor. Settled by the χ computation (R6): the
phenomenon is real, the theorem is correctly scoped, and one sentence fixes the exposition. MINOR.

**Proof completeness.** (a) asks for several proofs to be expanded. (b), (c) and (d) checked those
proofs and found them complete. Terse, not gapped.

**Figures.** The editor (e) would keep only Figs 2, 3, 6 and perhaps 7, and calls Figs 1, 4(a) and 5
decorative. The brief that produced this version required F1, F2 and F6 in the main paper. This is
an editorial trade-off for the authors.

**Captions.** Several presentation complaints (R10, R11) concern decoding that the round-1 captions
contained and the two-sentence cap removed. The cap and full decoding are compatible only if the
decoding moves into the citing sentence of the text.

## 5. Space

Fixing R1, R3, R6, R7, R9, R10, R11 and R12 adds about 1.5 pages. R2 alone frees 8–12 pages (§7 and
most of §6 to the supplement, §4 to about one page, §2.2 shortened). R5 frees about 0.5 page.

R4 costs about 1 page if Prop. S3.1 moves into an appendix. It saves about 0.5 page if δ_cert leaves
the main text, which is the natural choice once §6 is cut.

The net is a paper of roughly 27–30 pages, within reach of the editor's 22–25 if §2.2 is cut to a
citation.

## 6. GATE

**FAIL.**

Blocking:
- Four recommendations are major revision ((a), (c), (d), (e)). Only (b) is minor.
- Five MAJOR items are confirmed against the repository:
  - **R1**: significance and fit;
  - **R2**: length and focus;
  - **R3**: uncredited PTE prior art (Chen A.685–A.692, Identity 9), answered in the repository but not in the paper;
  - **R4**: δ_cert rests on a supplement-only proposition;
  - **R5**: division of material with the companion note.

None is a mathematical error. All five are fixable by restructuring and writing, and the restructuring
(R2) more than pays for the additions.
