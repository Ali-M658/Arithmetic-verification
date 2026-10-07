# VERDICT-B: referee round 4, Paper B (Annals of Global Analysis and Geometry)

Paper B: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold", 23 pp., built from
commit `defccde` (hashes in `README.md`). Reports: `B-a-editor-comparison-geometer`,
`B-b-thick-thin-geometer`, `B-c-heat-kernel-counting-analyst`, `B-d-numerical-eigen-analyst`,
`B-e-rigour-referee`. The harness refused every reviewer's own write, so each `REPORT.md` was saved
verbatim by the main session from the task result. A provenance comment is on its first line.

## Gate: **FAIL**

| criterion | result |
|---|---|
| (i) no confirmed MAJOR or FATAL | **not met.** There is no FATAL item. Confirmed MAJOR items: B1 ("certify" for estimated inputs), B2 (abstract and p. 3 say the test succeeded on all ten examples; it failed on one), B3 (Table 3 not reproducible from the paper), B4 (positioning: Buser–Courtois and degeneration theory), B5 (duplication with Paper A) |
| (ii) every recurring theme resolved | **not met.** Overstated numerics is not resolved (B1, B2, B7). Significance is not resolved (B4; a calls the numbers "of no practical use"). Attribution is not resolved (B4, plus the Jørgensen sentence n6). Proofs outside the paper: the mathematics is resolved, but the certificate's inputs live only in the repository (B3). Length is largely resolved (23 pp.; a asks for 16–18) |
| (iii) editor sends to review with desk-reject probability ≤ 10% | **not met.** The editor sends it to review but puts desk rejection at **25%**, and expects major revision (55%) or reject (30%) |
| (iv) ≥ 4 of 5 recommend minor or accept, no substantive "major" | **not met.** c recommends minor ("bordering on major if M1 cannot be answered by rigorous enclosures"). b recommends minor, but conditional on the certificate inputs being made rigorous, "otherwise major". d and e recommend major. The editor expects major. Since B1 is confirmed and not answered by rigorous inputs, b's and c's own conditions put them at major, so in substance one or two of five are at minor |

**Blocking items, in the order a revision should take them:**
1. B1 and B2: either make the certificate rigorous, or rename it and say "nine of ten".
2. B3: add a numerical-methods subsection with the inputs and a data table.
3. B4: add the Buser–Courtois positioning and the degeneration literature.
4. B5: declare or remove the duplication with A.

WRITING-ONLY does not apply, because (iii) fails. If the authors take the "recast" route for B1, every blocking item becomes writing, and the paper would then turn on (iii) and the editor's significance judgement.

**What the round established positively.** No reviewer found a mathematical error in any theorem, proposition or lemma. Between them the reviewers checked or recomputed the following, at 40–60 digits or symbolically:
- every proof line by line (e, and c for Sections 2–6);
- all 12 entries of Table 1;
- all 8 rows of Table 2 (b, c, d, e, a), with one rounding slip (n1);
- the enveloping remainders, by quadrature;
- every hyperbolic-trigonometric identity of §4, and the Jørgensen recursion of Lemma 8.1 (b);
- σ_* = 0.56206;
- the sets S of Table 3.

Reviewer d also computed its own finite-element spectra of O(2,8,8), O(3,3,12), O(2,3,7) and O(2,3,4096). They agree with the paper's quoted values (λ_1 = 44.888 and 0.4728), and Z − G_σ matches the two systolic classes to 0.2%. Theorem 7.1 is correct as a conditional theorem (b, c, d, e).

## Recommendations

| reviewer | recommendation (confidence) | main reasons |
|---|---|---|
| a, AGAG editor (comparison geometer) | **send to review; desk-reject probability 0.25**; expected outcome accept 0.03, minor 0.12, major 0.55, reject 0.30 (moderate-high on correctness) | positioning against Buser–Courtois and degeneration (M1); certificate comparison not like-for-like (M2); certificate inputs (M3); duplication with A (M4); length (M5) |
| b, thick–thin geometer | **minor revision, conditional on M2**: "if they are only numerical … I would then regard that as a major revision" (4/5 on the geometry) | crude geometric constants (M1); systole and diameter inputs not rigorous (M2); cusp wording (M3) |
| c, heat-kernel and counting analyst | minor revision, "bordering on major if M1 cannot be answered by rigorous enclosures" (high on §§2–6, medium on §7) | certificate inputs (M1); evaluating G_σ(t_*) to the needed accuracy, and λ̃ ≥ 0 (M2) |
| d, numerical eigen-analyst | **major revision** (high on the numerics) | "certify" overstated, with a place-by-place table (M1); systole not a lower bound (M2); methods undocumented, Table 3 not reproducible (M3) |
| e, rigour referee | **major revision** (high) | certificate inputs (M1); headline success claim contradicts §7 (M2) |

## Deduplicated issue table

Severity is the highest any reviewer gave; where the main session changes it, the reason is stated. Type: M = mathematics, C = computation, W = writing. Status as in the brief: CONFIRMED, ANSWERED IN PAPER, ANSWERED IN REPOSITORY BUT NOT PAPER.

### MAJOR

| ID | reviewers | severity | location | issue | resolution | type | status and check |
|---|---|---|---|---|---|---|---|
| B1 | d-M1, d-M2, c-M1, e-M1, b-M2, a-M3 (all five) | MAJOR | abstract; p. 3 after Thm 1.2 (line 107); §7 (lines 454–485); Table 3; Fig. 2 caption | Theorem 7.1 is correct as a conditional theorem. Its application is called "certifies"/"certified"/"the certificate succeeds", but no hypothesis is established. (a) The ε_j are a-posteriori estimates (two-level agreement), not enclosures. (b) Completeness of the list ("complete below 1.6×10⁴", "up to λ ≈ 2440–2560") is asserted without method. (c) The systoles are values found by search, which are upper bounds, not lower bounds. (d) The O_ϑ diameter bound 7.8 is unexplained, and ϑ is never defined. Reviewer d showed by computation that deleting or inserting one eigenvalue makes the test "succeed" for a wrong signature, so completeness is not a technicality. d tabulates all 14 uses of the vocabulary: four are theorems or neutral, and items 1, 5 and 13 are overstatements | Either (a) make it rigorous: guaranteed lower bounds (Liu–Oishi, Carstensen–Gedicke, Lehmann–Goerisch), Sylvester-inertia counts, interval arithmetic, rigorous systole lower bounds (word cutoff via Lemma 2.2, or Prop. 8.2's argument), the O_ϑ diameter proof and a definition of ϑ. Or (b) recast: keep Theorem 7.1, call the outcome "the criterion is met with the estimated errors", and remove "certified" from the abstract, p. 3 and Fig. 2. d estimates (a) is feasible for the triangles (relative 10⁻⁴ suffices) | C, W | **CONFIRMED in the source and the repository.** (1) The paper says "high-order finite elements and error estimates" and gives no enclosure method. (2) `theory/eigen/practice.md` line 38: "N_apr is rigorous modulo those error bars and the completeness of the computed spectrum below λ_N", and the error bars are "the committed a-posteriori eigenvalue error estimates" (line 36). (3) `theory/eigen/practice.py` lines 175–186 hard-code the systoles `2.256768` and `1.862604` and read the O_ϑ systoles from `numerics/moduli/data/geometries.json`; these are numerical values, not proved lower bounds. (4) Paper A's own supplement states that these spectra are "not enclosures, so nothing … is certified" (`paper/jga/supplement.tex` line 295). So Paper B claims for the same data what Paper A disclaims. (5) `grep vartheta` finds no definition of the family parameter in `paper/eigen/manuscript.tex`; the repository parametrises the family by `tau` in `geometries.json`. Counts under "overstated numerics" |
| B2 | e-M2, d-m5, d (table rows 1, 5) | MAJOR | abstract; p. 3 (line 107) against p. 15 (line 485) | The abstract and p. 3 say the test succeeds on O(2,8,8), O(3,3,12) and the eight O_ϑ "with 21 to 750 eigenvalues". §7 says that for the member of systole 0.694 it "needs more than the 815 eigenvalues computed". So it succeeded on 9 of 10, and the headline is false as written | Say "nine of ten examples"; support "a limit of the data, not of the method" with an estimate (d-m6) | W | **CONFIRMED by the source**: line 107 against line 485, and Table 3's own caption ("over the seven of systole at least 0.846"). A one-line fix, but a false statement in the abstract, so not downgraded |
| B3 | d-M3, c (Tables; m9), e-m10, a-m3 | MAJOR | §7, Table 3, Fig. 2, Fig. 3 numerics | The numerical method is not documented: the model of H², degree, meshes, grading, quadrature, estimator, ε_j, the completeness check, multiplicities, ℓ, Δ, the t-grid, and which criterion of Thm 7.1 defines N_apr. N_obs is not defined precisely. Reviewer d reproduces N_apr = 21 for O(2,8,8) but gets 25–35 for O(3,3,12), never 39 | Add a methods subsection, a table of λ̃_j and ε_j for j ≤ 40, the inputs, and the criterion | C, W | **ANSWERED IN REPOSITORY BUT NOT PAPER.** The dispute over 39 is settled by the repository's data: `theory/eigen/data/practice.csv` evaluates N_apr only on the grid t ∈ {…, 0.02, 0.03, 0.05, …}. For O(3,3,12) and M = 12 it gives 63 at 0.02, **39 at 0.03**, and nothing at 0.05 or above. Reviewer d's 25–35 is at t ≈ 0.039, between grid points. So 39 is a coarse-grid upper value, consistent with d. The criterion and grid are in `practice.py` and `practice.md`; the paper states neither. Counts under "proofs outside the paper" |
| B4 | a-M1, b-M3 (literature part), a-m8, a-m14, e-m13 | MAJOR | §1 (pp. 2–3), §8 (pp. 16–20), bibliography | Missing positioning. Buser–Courtois (Math. Ann. 287, 1990) prove the surface analogue at the level of the full spectrum, with m(g, ε) non-effective, and conjecture ε-independence, which is Problem 1's question. Theorem 1.3 is elliptic degeneration (Garbin–Jorgenson; Selberg/Hejhal accumulation for Hecke groups; Judge 1995, 1998). The pinching discussion should engage Wolpert 1992, Ji 1993, Hejhal, Schoen–Wolpert–Yau. Editor a suggests (unverified) that degeneration theory may answer Problem 1 negatively for δ > 0 | Add a "relation to prior work" paragraph; place Thm 1.1 as an effective signature-level Buser–Courtois; cite the degeneration literature; separate Problem 1 into δ > 0 and δ = 0 | W | **CONFIRMED.** `paper/eigen/references.bib` contains Buser's book (`buser1992`, line 115) but no Buser–Courtois entry, and `manuscript.tex` cites neither. `strohmaieruski2013` is in the bib but cited 0 times in the manuscript. The Garbin–Jorgenson paper [13] is cited only for the trace formula. The possible negative answer to Problem 1 is the editor's reading and **not checked** here. Counts under "attribution" and "significance" |
| B5 | a-M4 (Panel A: a-M4, VERDICT-A item A3) | MAJOR | B §2.1–2.2, §3, App. A against A §2–3, Lemma B.1 | About nine results are proved in both papers, partly verbatim. p. 3 discloses only Thm 3.4. A is called "in preparation" | List the reproduced results in §1; compress or cite; coordinate the submissions | W | **CONFIRMED** by the sentence comparison of the two `.tex` files (VERDICT-A, A3): about 7,000 characters, roughly 2 pp. of identical or near-identical sentences, and about nine shared statements with proofs. This is less than the editor's "5–6 pages", but the disclosure on p. 3 is incomplete |

### Reviewer-rated MAJOR, adjudicated

| ID | reviewers | rated | location | issue | resolution | type | status and check |
|---|---|---|---|---|---|---|---|
| B6 | b-M3 | MAJOR | abstract ("eigenvalues near ¼"), p. 3 line 117 ("crowds towards ¼"), Fig. 3 caption | Prop. 8.3 proves only upper bounds λ_j ≤ ¼ + π²(j+1)²/h_m². "Near ¼" and "crowds towards ¼" need a lower bound λ_j ≥ ¼ − o(1), which is not proved. The careful sentence on p. 18 ("an observation and not a result") is not carried into the abstract | Say "below ¼ + η for any η > 0", or prove the lower bound (a-M1(b) suggests Garbin–Jorgenson plus PSL(2,Z)); note that Remark 8.4 needs only the upper bounds | W | **CONFIRMED; severity adjusted to MINOR.** Theorem 1.3 itself states only the upper bound and the non-uniformity, which are proved. The overstatement is in the abstract, line 117 and the caption. A wording fix that counts under "overstated numerics" until made |
| B7 | c-M2, e-m1, e-m3, d-m2 | MAJOR | Thm 1.1, Thm 6.2, Thm 1.2 against Thm 7.1 | The decision rule needs G_σ(t_*) to absolute accuracy Γ_*/8 (25 to 300 significant digits); the paper does not say how. Thm 1.1 omits λ̃_j ≥ 0, which Thm 6.2 assumes. Thm 1.2 omits "of area A" and nonnegativity | One sentence: the enveloping bound (4) with K chosen so that t_*^K Q(K) ≤ Γ_*/16 evaluates G_σ rigorously. Align the hypotheses | M, W | **CONFIRMED; severity adjusted to MINOR.** Theorem 6.2 (line 415) has λ̃_j ≥ 0 and Theorem 1.1 (line 97) does not. The fix for the evaluation is already in the paper (Props. 2.6–2.7 and (4)); it needs one sentence. Nothing false |
| B8 | b-M1, a-M5(c), c-m11, c-m12 | MAJOR | Lemma 2.2, Thm 4.4, Table 1, p. 11, p. 20 | The geometric constants are far from optimal. D ≍ A/ε + AM³, where thick–thin gives O(A + n log(1/ε) + log M), and a Buser-type count could remove D. k_* and γ_* could be computed exactly on the finite set Sig(A, M) (c: N = 1.08×10⁴ instead of 4.32×10⁴ for one row). So the "ε⁻³ log(1/ε)" rate is an artefact of the method, and p. 20 states it as fact while p. 14 calls it an observation | State that the constants are artefacts and give the expected orders; or improve them; hedge p. 20 | M, W | **CONFIRMED as a request; severity adjusted to MINOR.** Every reviewer verified that the constants are correct as stated. The inconsistency between p. 14 ("observations on the formulas, not proved asymptotics") and p. 20 is real (b-m8, c-m8, d-m7, e-m9) and is the only part that is a defect |
| B9 | a-M5 | MAJOR | Lemma 8.1 and the sentence before it (line 493), Lemma 4.1, length | "We could not obtain the text of [16]" is not an acceptable reason in a journal; Jørgensen's inequality with proof is in Beardon §5.4, the paper's own [15]. (H1)–(H3) are textbook. Target 16–18 pp. | Delete the sentence; cite Beardon; optionally keep the proof as a convenience; cite (H1)–(H3) | W | **CONFIRMED** (line 493 reads as quoted; b-m1 and e-m12 make the same point). Severity adjusted to MINOR: one sentence plus a citation. Length 23 pp. is a judgement; only the editor asks for cuts |

### MINOR (deduplicated; CONFIRMED unless stated)

| ID | reviewers | location | issue | resolution | type |
|---|---|---|---|---|---|
| n1 | e-m8, d-m1 | Table 2, row 2 | t_1 printed 6.9×10⁻⁹; the value is 6.8486×10⁻⁹, so 6.8×10⁻⁹ | **settled by computation**: the main session ran `theory/eigen/theorem_e.py`'s `theorem_E_constants(π/2, 1.8626, 12)` and got t_1 = 6.848648701×10⁻⁹; correct the entry | W |
| n2 | c-m1, a-m1, e-m2 | Thm 6.2 | δ = min{1/t_*, …}: the first entry is never active and unused | delete or explain | W |
| n3 | c-m2, e-m5 | Lemma 2.3 | stated for "ℓ the systole", applied with a lower bound | state it for "systole at least ℓ" | W |
| n4 | c-m5, b-m2, e-m6 | p. 11 after Thm 4.4 | "binding constraint through t_1" is vacuous: D does not enter t_1 | "D enters only t_3, which binds in rows 4, 6, 7" | W |
| n5 | c-m6, a-m4, b-m9, c-m13, e-m11 | Table 2, Table 3 | ε values unexplained (1.8626 is the systole of O(3,3,12), used for both triangle rows); t_2 never binds; add Γ_* and Λ | explain; add columns | W |
| n6 | b-m1, e-m12 | line 493 | see B9 | — | W |
| n7 | c-m9, d-m3, d-m4 | §7 | N_obs and N_apr not defined as formulas; which criterion of Thm 7.1 is used | define (with B3) | W |
| n8 | c-m10, d-m2, a-m5 | Thm 7.1 | assumes the area exactly; S has one area, while Thm 6.2's class has all areas ≤ A; the examples are demonstrations with known signature | say so; optionally allow unequal areas via the δ_1 gap | M, W |
| n9 | e-m7 | Remark 8.4 | finiteness "by the case analysis of Lemma 5.1" does not follow from it; give the one-line bound on r | add | M |
| n10 | e-m4 | Thm 7.1 | "min over 0 < s ≤ t" should be inf | fix | W |
| n11 | b-m4, a-m12 | Prop. 8.2 | the folding map, uniqueness of the m-vertex per tile and the regular m-gon P deserve a sentence | add | W |
| n12 | b-m5, b-m6, b-m7, d-m8 | §8 | σ_* = 0.562 is weak (true systoles ≥ 0.984); "decreases in m" is an observation (Judge may prove it); "fixed systole" in Prop. 8.5 is inaccurate; two-mesh agreement is not an error bound | remark; label; reword | W |
| n13 | b-m12, a-m6 | Lemma 2.2 | count oriented, not necessarily primitive classes | say so | W |
| n14 | e-m13, e-m17, e-m18, c-m15 | §8.2, Prop. 8.5, intro | the bounded number of small eigenvalues under pinching, continuity of λ_1 in b, continuity on moduli space, and the δ step of the compactness sketch need references or a clause | add | W |
| n15 | e-m14, e-m15 | [9], [3], [10], [13], [15] | Chang–DeTurck statement and DOI; Mumford Cor. 3 not verified; series and URL details | fix | W |
| n16 | e-m16, c-m4 | notation | Γ, L, N, K, ℓ, s, A, C_l overloaded or undefined; Sig_{≤M} unused | rename; define | W |
| n17 | c-m3, c-m11, c-m14 | (4), Prop. 5.2 | free improvements: max instead of sum; decay-weighted Lipschitz bound (δ larger by 10²–10⁴); inf_s e^{sx}Z(s) | optional | M |
| n18 | c-m7, d (item 2) | p. 14 | "a factor near 8 per halving of ε": the ratios are 8.7–9.0 | "about 9, tending to 8" | W |
| n19 | a, b, c, d, e (presentation) | Figs. 1–3 | Fig. 1: no legend; caption says "both errors" where Thm 7.1 needs their sum; plot half-gaps. Fig. 2: the open diamonds (N_apr, M = 3) are hidden under the filled ones (b at 250 dpi, e at 300 dpi); colours unkeyed (orange = O(3,3,12), teal = O(2,8,8)). Fig. 3: the ¼ line is invisible on the frame; the j² reference lines are unexplained; "approach j² slowly" against plateaus 5–12% above; "thin dashed" renders dotted; Type-3 fonts | fix captions, markers and lines | W |
| n20 | a-m10, e (Other) | data statement (line 578) | repository under "Ali-M658", which matches no author | state the maintainer; make the Zenodo DOI primary | W |
| n21 | a-m7, a-m11, a-m13, a-m2, c-m16 | p. 3, p. 6, abstract | "none of the three bounds is a matter of convenience"; say what is used in place of the Uçar/Schueth agreement; the last abstract sentence is opaque; N+1 versus N in Thm 1.2; ranges in the abstract mix classes | reword | W |

## Disputes settled

- **N_apr = 39 for O(3,3,12) against d's 25–35.** Settled by the repository's `practice.csv`: 39 is the value at t = 0.03 on a coarse grid with no admissible point at 0.05; d's values come from t ≈ 0.039. Both are right, and the paper should state the grid (B3).
- **Table 2 row 2, t_1 rounding.** Settled by computation (n1): 6.8486×10⁻⁹, so the printed 6.9 is wrong.
- **"Certified" (B1).** Settled by the repository and Paper A's own supplement: the error bars are a-posteriori estimates, the systoles are numerical values, and A's supplement says these same spectra are "not enclosures, so nothing … is certified".
- **Success "with 21 to 750 eigenvalues" on all ten examples (B2).** Settled by the source: line 485 records the failure for the member of systole 0.694.
- **Problem 1 answered negatively for δ > 0 by degeneration theory (a-M1(c)).** Not settled; the editor flags it as an unverified reading.

## Recurring themes of earlier rounds

| theme | verdict for Paper B |
|---|---|
| significance | **not resolved.** Every reviewer finds the mechanism clean (local invariants plus an exponentially small global error, and Lemma 3.5's integrality) and the constants honest but astronomically large. The editor calls the contribution "an effective, signature-level version of Buser–Courtois … respectable, not a breakthrough" once positioned, and the positioning is missing (B4) |
| length | **largely resolved**: 23 pp. Only the editor asks for 16–18, by citing Beardon instead of reproving Jørgensen, citing (H1)–(H3), and removing the duplication with A |
| attribution | **not resolved**: Buser–Courtois and the degeneration literature are missing (B4); the Jørgensen sentence (B9); Strohmaier–Uski is in the bib but not cited. Every reference e could read at statement level says what it is cited for; e could not read the text of [3], [4] and [9] |
| proofs outside the paper | **resolved for the mathematics**: e read every proof to the end and found each complete in the paper; Lemma 8.1 replaces round 3's Wikipedia citation, and (H1)–(H3) and the trace identity are proved. **Not resolved for §7**: the certificate's inputs (ε_j, completeness, systoles, ϑ, the O_ϑ diameter, the t-grid) exist only in the repository (B1, B3) |
| overstated numerics | **not resolved**: "certifies" and "certified" for a-posteriori estimates (B1), the "21 to 750" headline (B2), "near ¼" and "crowds towards ¼" (B6), and the ε⁻³ rate stated as fact on p. 20 (B8) |

## What a revision should do, ranked

1. **B1 and B2.** Decide between a rigorous certificate (enclosures, inertia counts, systole lower bounds, the O_ϑ diameter, a definition of ϑ) and a recast ("criterion met with estimated errors"). In both cases state "nine of ten", and say that a missing or spurious eigenvalue can make the test pass for a wrong signature.
2. **B3.** Add a numerical-methods subsection: model, elements, meshes, estimator, completeness, multiplicities, ℓ, Δ, the t-grid and the criterion. Add a λ̃_j/ε_j table for the triangles.
3. **B4.** Add a prior-work paragraph: Buser–Courtois; Garbin–Jorgenson and Judge; Wolpert, Ji and Hejhal for pinching; Strohmaier–Uski and Booker–Strömbergsson–Venkatesh for trace-formula checks of computed spectra. Split Problem 1 into δ > 0 and δ = 0.
4. **B5.** Declare the results reproduced from A, compress them, and update the companion status at submission.
5. **B6–B9**, then the MINOR table. n1, n2, n4, n10 and the Fig. 1 caption are one-line fixes.
