# VERDICT-B: referee round 5, Paper B (Annals of Global Analysis and Geometry)

Paper B: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold", 26 pp., built from
commit `3134dbd` (hashes in `README.md`). Reports: `B-a-editor-aga-handling`, `B-b-hyperbolic-geometer`,
`B-c-spectral-analyst`, `B-d-numerical-analyst`, `B-e-rigour-citations-figures`. The harness refused every
reviewer's own write, so the main session extracted each `REPORT.md` verbatim from the reviewer's final
message in its task transcript. Each file starts with a provenance comment. Length is out of scope: no
reviewer raised it, and nothing here refers to it.

## Submission gate: **NOT READY**

| criterion | result |
|---|---|
| (i) no confirmed FATAL; no confirmed MAJOR on correctness, rigour or a claim the paper does not support | **not met.** There is no FATAL item and no mathematical error. One confirmed MAJOR blocks: **B1**, the numerical section's statements about completeness and certification say more than the computations show, and Paper B omits a limitation of the same spectra that Paper A's supplement records |
| (ii) AGAG editor sends to review with desk-reject probability ≤ 15%, without regard to length | **not met.** The editor sends it to review, at **25%** desk-reject probability |

**Blocking items, all fixable in the text.**

1. **B1: rewrite the completeness and certification statements of §7.1 and p. 14.** Specifically:
   - call the Weyl tail a heuristic, not a bound;
   - say that a single-time trace check excludes only isolated defects, not compensating pairs;
   - say that for the triangles completeness was checked against the true signature's I + E;
   - disclose that the triangle spectra come from single-window slicing and that the double-window rerun has not been run (as Paper A's supplement already does);
   - qualify "conforming elements give upper bounds" (quadrature of the weight, floating point);
   - complete the list of what a rigorous version needs (validated G_σ, a certified systole, outward rounding).
2. **The editor's desk-reject reasons** and what each needs:
   - the unrefereed companion (B2) needs Paper A posted (arXiv) and supplied to referees, and the cross-document hyperlinks removed;
   - perceived significance and missing AGAG literature (B3) need a related-work paragraph and a decidability framing;
   - the test as run (B1, B4) needs B1 and the class-level column foregrounded.

   Whether the estimate then falls to 15% or below is the editor's judgement and cannot be checked here.

**Dependence on Paper A.** Paper B's main theorem uses results that are proved only in Paper A (Table 1 of B). Panel A verified those proofs in this round (VERDICT-A: no mathematical error), but Paper A is itself NOT READY on writing-level items. Neither paper can be sent until Paper A is publicly citable.

**What the round established.**
- **No mathematical error.** No reviewer found one in anything Paper B proves.
- **Tables 2 and 3, Theorem 6.2.** Every entry of Table 2 (12) and Table 3 (8 rows × 10 columns) was recomputed independently by **all five** reviewers from the printed formulas, and agrees to the printed digits. That includes the binding constraints, "t_2 never binds", and the 4×10^18 claim. The last column of Table 6 was recomputed by c and d. The proof of Theorem 6.2 was re-derived step by step by c, a, b and e (y_0, the 3/8 margin, tail and perturbation).
- **Table 6 (c, d, e).** The rows for O(2,8,8) and O(3,3,12) were recomputed from Table 5 data: (C1) 18 / 25 and (C2) 20 / 29 exactly. The Weyl-replacement estimates were recomputed within about 2% (d).
- **Imported Paper A statements, tested numerically (b, c, d, e).** The geodesic-count bound B was re-derived from the count and found asymptotically sharp. Proposition 2.3's enveloping signs and moduli were checked by quadrature.
- **Section 4 (b, e).** Lemmas 4.1–4.3 and Theorem 4.4 were checked line by line. Every systole and diameter in Table 4 was confirmed by complete enumeration (b, d, e). The systole of O(2,3,7) is exactly 2 arccosh((1+2cos(2π/7))/2) (b).
- **Section 8 (a, b, e).** The Jørgensen recursion, σ* = 0.562066871…, the trace identity, (3), Propositions 8.3 and 8.5, and Remark 8.4. FEM spot checks of λ_1(O(2,3,7)) = 44.888 and of Table 5 (b).
- **Citations (e, with a).** About 30 references checked at statement level.
- **Figures (d, e).** All three figures checked against their data, at pixel level.

## Recommendations

| reviewer | recommendation (confidence) | main reasons |
|---|---|---|
| a, AGAG handling editor (determinants, isospectral compactness) | **send to review; desk-reject probability 25%**; provisional **major revision** (about 0.6) | M1 dependence on unrefereed companion; M2 missing AGAG literature, area hypothesis undiscussed, decidability not stated; M3 the test as run uses the true signature, area and instance geometry; M4 omitted numerical limitations |
| b, hyperbolic geometer | **minor revision** (high for §§4, 8) | M1 literature context for Problem 1; M2 diameter heuristic imprecise, no collar lemma |
| c, spectral analyst | **minor revision**, conditional on M1; major if the companion is unavailable (high for §§4–6; moderate for §§2–3) | M1 load-bearing results imported from the companion |
| d, numerical analyst | **major revision** (high on recomputed items; medium-high overall) | M1 completeness not a bound; M2 no consistency check; M3 "upper bounds" statement and undocumented error estimate; M4 the list of what a rigorous version needs is incomplete |
| e, rigour, citations, figures | **minor revision**, conditional on M1; major if the companion is unavailable (high) | M1 companion imports; M2 completeness overstated |

**The editor's desk-reject estimate (25%), with its reasons as stated.**

*Raising the probability:*
1. Dependence on an unrefereed companion, "the largest single risk".
2. Perceived significance: a routine effectivisation of compactness with constants that have no practical meaning, and numerical checks on orbifolds whose geometry is known.
3. Missing AGAG-relevant literature.

*Lowering the probability:*
- Strong scope fit.
- Correct and carefully written mathematics.
- Theorem 1.3 and Problem 1 are clean contributions.
- The constants are reproducible.
- The authors are candid about limitations.

The editor would send it to review with two referees, in orbifold trace-formula spectral geometry (to also receive Paper A) and in computational spectral theory.

## Deduplicated issue table

**Columns.**
- *Severity* is the highest any reviewer gave. Where the synthesis changes it, the reason is stated.
- *Type:* M = mathematics, C = computation, W = writing.
- *Status:* CONFIRMED / ANSWERED IN PAPER / ANSWERED IN REPOSITORY BUT NOT PAPER. Disputes were settled from the LaTeX source and the repository's records.

### FATAL

None.

### MAJOR

#### B1 (blocking)

**Reviewers:** a M3(a), M4; d M1, M3(a), M4; e M2. **Severity:** MAJOR (claim not supported). **Type:** W (C if certification is attempted). **Location:** §7.1 "Completeness", "Error estimates", "Discretisation and solver" (p. 15); p. 14 last paragraph before §7.1; Table 4 caption.

**Issue.** The numerical section states more than its computations show:
1. **Weyl tail.** "Within the error budget … formed by the ϵ_j and a tail bound from Weyl's law": Weyl's law is asymptotic, not a bound. The paper's proved tail (Prop. 5.2) is 1.1×10^-5, six orders above the budget (d).
2. **Completeness.** "No eigenvalue below 1.6×10^4 is missing or spurious" follows from one scalar comparison at t = 0.0015. That cannot exclude compensating missing/spurious pairs (a, d, e). Summation round-off is not in the budget (d).
3. **Circularity.** For the triangle orbifolds the comparison is against I + E of the *true* signature, which is circular for a determination (a).
4. **Undisclosed single-window computation.** The triangle spectra come from single-window slicing, which can miss an eigenvalue at a window boundary, and the double-window rerun has not been run. Paper A's supplement records this; Paper B does not (a).
5. **"Upper bounds".** "Conforming elements give upper bounds for the λ_j" ignores the quadrature of the weight w and floating point (d).
6. **"Would decide rigorously".** "With guaranteed eigenvalue enclosures and a proved completeness, the same computation would decide the signature rigorously" omits a validated G_σ, a certified systole and outward rounding (d).

**Why it matters.** d's experiment shows that one deleted or duplicated eigenvalue makes (C1) certify a *wrong* signature in 22 of 24 cases. So completeness is the decisive input.

**Resolution.**
- Replace "a tail bound from Weyl's law" by "a Weyl-law tail estimate (heuristic)".
- Reword the completeness conclusion as conditional, excluding isolated defects only.
- State that for the triangles it was checked against the true signature.
- Disclose the single-window computation and the unrun rerun, as Paper A's supplement does.
- Qualify the upper-bound sentence.
- Complete the "would decide rigorously" list.
- Put the status of each input in a short table (d).
- Optionally: report the comparison over a range of t, add the free consistency check (B5), add Sylvester-inertia counts, or certify the two triangle cases (d M4).

**Status.** **CONFIRMED** in the source:
- `paper/eigen/manuscript.tex:452`: "…within the error budget of $1.5\times10^{-11}$ formed by the $\epsilon_j$ and a tail bound from Weyl's law… so, given the budget, no eigenvalue below $1.6\times10^4$ is missing or spurious".
- `:450`: "conforming elements give upper bounds for the $\lambda_j$".
- `:419`: "with guaranteed eigenvalue enclosures and a proved completeness, the same computation would decide the signature rigorously".
- `:448`: "overlapping spectral windows of 200 …; for $\Orb_\vartheta$ every eigenvalue is covered by two windows", with no single-window disclosure for the triangles.

**ANSWERED IN REPOSITORY BUT NOT PAPER** for the window limitation:
- `paper/jga/supplement.tex:357` says the spectra "were computed with single-window spectral slicing … a recomputation of all four spectra with the double-window solver … has not been run".
- `theory/eigen/METHODS.md:70–77` confirms that the committed triangle spectra were not produced by the double-window routine, that `numerics/rerun_double_window.py` has not been run, and that `numerics/data/rerun_double_window_comparison.json` does not exist (G7-5 in `paper/jga/OUTSTANDING.md:114`).

**Partly ANSWERED IN PAPER** on d's geometric point: `:448` represents the geodesic sides exactly as rational quadratic splines, so the domain is exact. The remaining crimes are quadrature and rounding.

None of this affects Theorems 1.1, 1.3 or 6.2. The fix is a rewrite, or a rewrite plus computation.

#### B2 (not blocking under (i); conditions acceptance; drives the desk-reject estimate)

**Reviewers:** a M1, c M1, e M1. **Severity:** MAJOR (verifiability). **Type:** W. **Location:** §§2–3, Table 1 (pp. 4–7); ref. [20].

**Issue.** Theorem 2.1, the geodesic count of Lemma 2.2, Proposition 2.3, the p_l structure, Lemma 3.1 and Theorem 3.2 are stated without proof and imported from the companion. That companion is cited as "Companion manuscript, submitted (2026)" with no identifier, and the cross-document hyperlinks (e.g. "[20, Prop. B.2]") will dangle. Theorem 3.2 fixes k*, and Proposition 2.3 drives Lemma 6.1, so the main theorem cannot be verified from B alone.

**Resolution.**
- Post Paper A on arXiv and cite it with an identifier and fixed numbering.
- Supply A and its supplement to the editor and referees.
- Replace the hyperlinks by plain numbers.
- Optionally, map each import to the constant it feeds: Theorem 3.2(i) → n*, Theorem 3.2(ii) → k*, Proposition 2.3 → t_1, Lemma 2.2 → t_2, t_3, ϖ (c).

**Status.**
- **ANSWERED IN PAPER** as disclosure: `manuscript.tex:123` and Table 1 list every import with its place in A, and say nothing else is taken from A.
- **ANSWERED IN REPOSITORY BUT NOT PAPER** as proof: Paper A contains the proofs (A Thm 2.3, Lemmas 2.4–2.6, 2.8, 2.10, 3.3, Cor. 3.5, Thm 3.8(i), Lemma B.1, Prop. B.2). Panel A verified them in this round with no error (VERDICT-A).
- **CONFIRMED** that A has no public identifier (`paper/eigen/references.bib:189`: `@unpublished{companionA, note = {Companion manuscript, submitted}}`).

Not a correctness gap, so not blocking under (i). It is the editor's largest desk-reject reason, and acceptance is conditional on it.

#### B3 (not blocking: significance and scholarship)

**Reviewer:** a M2. **Severity:** MAJOR (significance and literature). **Type:** W. **Location:** §1 "What effectivity adds", "Relation to prior work" (p. 2); §8.

**Issue.**
- (a) No discussion of the AGAG-relevant orbifold literature: Stanhope (AGAG 2005), Proctor–Stanhope (2010) next to Theorem 4.4 and Proposition 8.2, Rossetti–Schueth–Weilandt (AGAG 2008), Dryden's isospectral finiteness, Doyle–Rossetti, McKean / OPS / BPP.
- (b) The necessity of the area bound is never discussed (§8 treats only the orders and the systole).
- (c) The real gain, a finite certifiable decision procedure, is not stated.

**Resolution.** Add a related-work paragraph; add a sentence or an open question on the area bound; restate significance as decidability.

**Status.** **CONFIRMED.** `grep -c "stanhope|proctor|rossetti|doyle" paper/eigen/manuscript.tex` = 0; `stanhope2005` is in `references.bib` but never cited. §8 has subsections only on the orders and the systole. Significance and scholarship, so not blocking under (i).

#### B4 (not blocking: scope of the test)

**Reviewer:** a M3(b), (c). **Severity:** MAJOR (presentation of the test). **Type:** W (M for option b). **Location:** Theorem 7.1, Table 6, abstract, p. 3.

**Issue.**
- (b) The exact-area hypothesis of Theorem 7.1 looks unnecessary: S = Sig(A, M) with area ≤ A would determine the area too.
- (c) The headline "18 to 847 eigenvalues" uses the instance diameter 2 diam P, the known area and (for completeness) the signature. The class-level column of Table 6 (855–2900 counts, estimates 5.6×10^3–4.1×10^5) is the honest analogue of Theorem 6.2.

**Resolution.** Either extend Theorem 7.1 to Sig(A, M) and rerun Table 6, or explain why the exact area is needed. Foreground the class-level column in the abstract and introduction.

**Status.** **ANSWERED IN PAPER in part.** The paper states the instance-geometry dependence and the known-area input (items (i)–(v), p. 14; p. 17, "most of that difference is the instance's diameter bound"). The suggestion in (b) is a strengthening, not an error. Not blocking.

#### B5 (not blocking: strengthening)

**Reviewer:** d M2. **Severity:** MAJOR (method). **Type:** C/W. **Location:** Theorem 7.1; Table 6.

**Issue.** A free consistency check is missing. The true σ must satisfy the inequality of Theorem 7.1 for every N and t, and no other σ may ever pass (C1). On the Table 5 data the check is clean (maximum ratio 0.91). With one eigenvalue removed it is violated by factors of 10²–4×10³.

**Resolution.** State the check as part of the procedure and report the maximal ratio and where it is attained, for all ten examples.

**Status.** **CONFIRMED as absent** (no such check in §7). It is a strengthening, not an error, so not blocking. Running it needs the family spectra (`theory/eigen/data/`). Recommended because it is the cheapest guard against the B1 failure mode.

#### B6 (not blocking: scholarship)

**Reviewer:** b M1. **Severity:** MAJOR (literature context). **Type:** W (M for option i). **Location:** §8.2, Problem 1, pp. 22–23.

**Issue.** The "missing input" for Problem 1(b) is largely available in the literature, and the paper does not engage with it: Huntley–Jorgenson–Lundelius, Garbin–Jorgenson, Otal–Rosas, Ballmann–Matthiesen–Mondal.

**Resolution.** Cite these, then either settle (b) or state exactly which orbifold ingredient is missing.

**Status.** **ANSWERED IN PAPER in part.** Ji [10] and Wolpert [11, 12] are cited, and `:604` names the missing lower bound. The listed works are not cited. Not blocking.

#### B7 (not blocking: hedged heuristic, but a factual slip)

**Reviewer:** b M2. **Severity:** MAJOR (heuristic incorrect). **Type:** W. **Location:** p. 10, after Theorem 4.4.

**Issue.** The heuristic "a diameter bound of order A + n log(1/ε) + log M" is wrong: it gives no ε-dependence for surfaces. The number of collars is ≤ 3g − 3 + n, so a natural form is C·A·(1 + log(1/ε)) + O(log M). The orbifold collar lemma (Dryden–Parlier) is not cited. Buser's count does not transfer to orbifolds directly.

**Resolution.** Correct the heuristic, cite Dryden–Parlier and Buser Ch. 4, and say why Buser's count does not transfer. Optionally carry out the ε-part.

**Status.** **CONFIRMED.** `manuscript.tex:285`: "a thick--thin decomposition should give a diameter bound of order $A+n\log\frac1\varepsilon+\log M$". The sentence is hedged ("should give") and no result depends on it, so not blocking. It is the second-ranked writing fix.

### MINOR (deduplicated; all CONFIRMED by the reviewers' own checks unless noted; none blocking)

| ID | reviewers | location | issue | resolution | type |
|---|---|---|---|---|---|
| B8 | a m1, c m3, e m4 | p. 12 after Thm 6.2 (`:362`) | "The rule is computable in exact rational arithmetic" fails as written. t* involves logarithms and exponentials. The existence of K with t*^K Q(K) ≤ Γ*/16 is asserted without argument, and Q grows factorially. | Use a rational t ≤ min(t_1, t_2, t_3) (the proof uses t* only through these inequalities, c), prove that K exists (or bound G_σ by validated quadrature), or weaken to "computable to any prescribed accuracy". | M/W (CONFIRMED at `:362`) |
| B9 | a P3 (Fig. 2), c P1, d (Figs), e m9–m11, P2–P4 | Figs 1–3, Table 6 caption | Figures without legends; captions not self-contained. Figure 1's shaded window (measured 0.050–0.056) does not match the stated rule (d and e recompute 0.048–0.059), and the "N = 21" indexing is unclear. The time reported in Table 6 is undefined (the criterion holds on an interval). N_obs is undefined and its values are not tabulated. The reference lines in Figure 3(b) are unexplained. The class-level counts are not plotted in Figure 2. | Legends and self-contained captions; state the shading rule and endpoints; define the reported time and N_obs and tabulate N_obs; label the Figure 3 reference curves. | W/C |
| B10 | d m1, e m7 | Table 6 caption; p. 16 | "> N_c": with N_c eigenvalues the largest testable N is N_c − 1, so it should read "≥ N_c". "Low by at least 0.3%" is 12/4424 = 0.27%. | Fix the convention, say whether λ_0 is counted, correct 0.27%. | W |
| B11 | a m4, b m5, d m11, e m18; a m12, e P6 | p. 20 body; data statement p. 23 | The script path `theory/eigen/systole_233.py` is in the mathematical text. The word-length-24 search wording does not say whether the enumeration is complete (b and d: it is, by a distance criterion; give the closed form 2 arccosh((1+2cos(2π/7))/2)). The repository name "Ali-M658/Arithmetic-verification" matches no author. | Move the path to the data statement; give the closed-form systole and say the enumeration is complete. The repository name is a known pending author decision (G7-14 in `paper/jga/OUTSTANDING.md:117`; declarations unchanged by instruction). | W |
| B12 | b m3, c m4, a m8 | p. 13; p. 10 | "N grows by a factor of about 9 per halving of ε" ignores that D is ε-independent at large ε (first halving factor 5.46 for M = 3, c). "Grows like A/ε" holds only for ε/2 < ≈ 0.45/M (b). The ε^{-3} log(1/ε) behaviour can be derived in one line (a). | Reword with the regime; derive the rate. | W |
| B13 | d m2 | Table 3 row 1; text `:385` | "So that the class contains both" is false for the M = 8 row, since O(3,3,12) has order 12. | Explain the M = 8 row or change it. | W (CONFIRMED at `:373`, `:385`) |
| B14 | d M3(b–d), m12, e m12 | §7.1 "Error estimates" | Which of (0.05,10) and (0.07,12) is the reference, and why. No convergence data for "h^13 to h^19". ARPACK tolerance and residuals not reported. ϵ_j at round-off level. | One sentence and a small convergence table. | W/C |
| B15 | b m1, m2, m8, m9; c m1, m2, m5, m6; e m1–m3 | §§2, 4, 8 | (H2) should say "parabolic". The M-dependence of d_0 is an artefact. Quasi-isometries must be orbifold maps. The λ_1 bound discards the region outside the collar ("exactly a"). The heat function is directly admissible in Hejhal/Iwaniec. One-line count derivation. Monotonicity range of B. "The unique σ that minimises" in Theorem 1.1. "Sig" means two things. | As listed in the reports. | W |
| B16 | c m10, m11, e m1, d (Thm 1.2) | Theorems 1.1 and 1.2 | Name G_σ and t* by reference. Put the completeness hypothesis ("first N, with multiplicity") in the statement. Mention (C2) in Theorem 1.2. | Sharpen the statements. | W |
| B17 | a m2 | Thm 1.3; Remark 8.4 | "No N and δ depending only on A and ε have the property of Theorem 1.1" is imprecise, since Sig(A, ∞) is infinite. | State the "two orbifolds … same signature" form. | W |
| B18 | a m5 | p. 4 | "Lemma 3.3 … not contained in [20]": its content is essentially in A's proof of Theorem 3.8(ii),(iv). | "A direct consequence of [20, Lemmas 2.10, 3.3]". | W |
| B19 | b m7 | §§7, 8.2 | The family O_ϑ is exactly O_{3,b} of §8.2, but this is never said. k ∈ {3,4} is unnecessary. | One sentence. | W |
| B20 | a m7, e (ref [1]), b | p. 2 | Cite Doyle–Rossetti for "the spectrum determines the signature". | Add. | W |
| B21 | e m14–m17, a m13 | refs | Buser–Courtois is Math. Ann. 287 issue 1, not 3. [7, Thm 6.5] in arXiv is convergence below 1/4, not growth above it. Hejhal pinpoint missing. Beardon GTM 91 and the hyperboloid model (cite Ratcliffe Ch. 3). Buser DOI. Garbin–Jorgenson year. b m6: quote the Garbin–Jorgenson log-growth statement. | Bibliographic corrections. | W |
| B22 | a P1, b P1, c P2, d, e P1 | throughout | Notation clashes: Γ (group / gap function / reflection group); ε and ϵ_j; δ and δ_k; A (bound / area / matrix); β, p, ℓ, h, K, N, D, Sig. | Rename (e.g. 𝒢(t) for the gap; η_j for the eigenvalue errors). | W |
| B23 | a P5 | figures | Figure fonts have no Unicode map (extracted text is garbled). | Fix in production. | W |
| B24 | a P6–P7, b P3–P5, e P5, P7 | exposition | Garden-path sentence in §1; "a-posteriori test, run at one time" in the abstract; Table 6 interrupts the statement of Lemma 8.1; the "–" entries of Table 4; the "aeb" convention; split the proof of Proposition 8.2 into steps; a sketch for (H3). | As listed. | W |
| B25 | d m3–m10 | §7.1, Fig. 3 | 2.1e-15 absolute or relative; a sharper perturbation bound; a qualified "lower bound" in the Table 4 caption; the factor 2 in 2 diam P not believed sharp; Brent's method role; the t-grid for estimates; the 0.8 cut-off; meshing and completeness for Figure 3. | One sentence each. | W |

## Writing-level fixes worth making before submission, ranked

Ranked by effect on the gate first, then on referee and editor reception.

1. **§7.1 and p. 14 (B1).** This removes the blocking item.
   - Change "a tail bound from Weyl's law" to "a Weyl-law tail estimate (not a proved bound)".
   - Change "no eigenvalue below 1.6×10^4 is missing or spurious" to a conditional statement that excludes isolated defects only.
   - Say that for the triangles the comparison is with the true signature's I + E.
   - Add the single-window disclosure, using the same sentence as `paper/jga/supplement.tex:357`.
   - Qualify "conforming elements give upper bounds" (up to quadrature of the weight and rounding).
   - Extend `:419` to "with guaranteed eigenvalue enclosures, a proved completeness, a validated evaluation of G_σ and a certified systole".
   - Add a short input-status table.
2. **Paper A on arXiv, and the citation of it (B2).** Cite A with its identifier and fixed numbering, and replace the cross-document hyperlinks with plain numbers. Not text-only for Paper B, but it is the editor's largest desk-reject reason, and Paper A's own writing fixes come first.
3. **Related work and significance (B3).** One paragraph covering Stanhope (AGAG 2005), Proctor–Stanhope, Rossetti–Schueth–Weilandt (AGAG 2008), Dryden's isospectral finiteness, Doyle–Rossetti and McKean/OPS/BPP. One sentence or open question on whether the area bound is needed. Restate the gain from effectivity as a finite certifiable decision procedure.
4. **Diameter heuristic (B7).** Correct `:285` to C·A(1 + log(1/ε)) + O(log M) with 3g − 3 + n collars. Cite Dryden–Parlier and Buser Ch. 4, and say why Buser's count does not transfer to orbifolds.
5. **"Exact rational arithmetic" (B8).** Use a rational t ≤ min(t_1, t_2, t_3) and add the one-line existence argument for K, or weaken to "to any prescribed accuracy".
6. **Foreground the class-level column of Table 6 (B4)** in the abstract and introduction. Add Problem 1 context: Huntley–Jorgenson–Lundelius, Garbin–Jorgenson, Otal–Rosas, Ballmann–Matthiesen–Mondal (B6).
7. **Figures and Table 6 (B9, B10).** Legends and self-contained captions; Figure 1's shading rule and window endpoints; the definition of the reported time and of N_obs; "≥ N_c"; 0.27%.
8. **Script path and systole (B11), and Table 3 row 1 (B13).** Move the path to the data statement; give the closed-form systole of O(2,3,7) and say the enumeration is complete; fix "so that the class contains both".
9. **Statements and small gaps (B12, B15–B19).** The ε-scaling regime; "parabolic" in (H2); orbifold quasi-isometries; "the unique σ that minimises"; the completeness hypothesis and (C2) in Theorems 1.1–1.2; Theorem 1.3's precise form; the Lemma 3.3 novelty wording; O_ϑ = O_{3,b}.
10. **Citations (B20, B21), notation (B22) and production items (B23–B25).**
