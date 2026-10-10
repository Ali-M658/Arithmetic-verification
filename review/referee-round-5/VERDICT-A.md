# VERDICT-A: referee round 5, Paper A (Annals of Global Analysis and Geometry)

Paper A: "How much of a hyperbolic orbifold does heat hear?", manuscript 44 pp. and supplement 18 pp.,
built from commit `3134dbd` (hashes in `README.md`). Reports: `A-a-editor-aga-handling`,
`A-b-conic-heat-invariants`, `A-c-pte-moment-problem`, `A-d-appendix-analyst`,
`A-e-rigour-citations-figures`. The harness refused every reviewer's own write, so the main session
extracted each `REPORT.md` verbatim from the reviewer's final message in its task transcript. Each file
starts with a provenance comment. Length is out of scope: no reviewer raised it, and nothing here
refers to it.

## Submission gate: **NOT READY**

| criterion | result |
|---|---|
| (i) no confirmed FATAL; no confirmed MAJOR on correctness, rigour or a claim the paper does not support | **not met.** There is no FATAL item and no mathematical error. Three confirmed MAJOR items block: **A1** (the abstract states a two-sided growth equivalence that the paper does not prove), **A2** (Propositions 2.11 and 2.12 rest on sketches and on computations that are not in the paper, and one stated check overreaches), **A3** (the text says heat-trace data give the invariants with an explicit error, which the paper does not prove) |
| (ii) AGAG editor sends to review with desk-reject probability ≤ 15%, without regard to length | **not met.** The editor sends the paper to review, but at **30%** desk-reject probability |

**Blocking items, all fixable in the text:**
1. **A1.** Change one phrase of the abstract.
2. **A2.** Either prove Propositions 2.11 and 2.12(i)–(ii) or relabel them. Document the computations in S8. Replace "(iii) for every l" by the range actually checked.
3. **A3.** Reword three passages, or add a lemma.
4. **Desk-reject estimate.** The editor's reasons and what each needs:
   - the algebraic core and the conditional headline (A5): needs a paragraph in §1 and the cover letter;
   - the sketches in §2.4: fixed by A2;
   - the three-manuscript pattern (A6): needs a sentence and the cover letter.

   Fixing A2 removes one of the four reasons. Whether the estimate then falls to 15% or below is the editor's judgement and cannot be checked here.

**What the round established.** No reviewer found a mathematical error in any result on which Theorems 1.1–1.4 or Corollary 1.5 depends. Between them the reviewers recomputed the following independently, in exact arithmetic or at 30–40 digits:
- **Section 2 and Appendix B.**
  - Every coefficient formula of Section 2: Lemma 2.6, Proposition 2.7, Lemma 2.8, (8), (10), and α_0..α_5.
  - The agreement with Uçar's (4.25), (4.33)–(4.35) for ν < 12 and with Schueth's Thm 4.1.
  - The enveloping signs and moduli of Proposition B.2 by direct quadrature of the trace formula (b, d).
  - Lemmas 2.4 and 2.5, and Lemma B.1.
- **Proposition 2.11, by a method independent of the authors' (b).** (iv) exactly; (ii) for l ≤ 4; (iii) for l ≤ 5. The constant ω_n of Proposition 2.12(ii) for n ≤ 7, against the Barvinsky–Vilkovisky form factors.
- **Section 3 and Appendix A.**
  - Theorem B's determinant and sign for n ≤ 6.
  - Theorem 3.8(ii) for M = 2..9 and (iv) for six (M, X).
  - The minimal areas for M = 3, 4, by exhaustive search (c).
  - All 20–21 pairs of Table S1, including the Lemma 3.16 recipes digit for digit (c).
  - The 8 primitive n = 4 witnesses against Chen's (A.685)–(A.692).
  - A brute-force test of Theorems 3.8(iii) and 3.11 on 149 pairs (c).
  - The 525 area classes behind Figure 3 (e).
- **Section 5.**
  - Table S2, Table S3, Theorem 5.4 and Proposition S2.1 to S = 600 (d, e) and S = 700 (a).
  - Theorem 5.8, including PARI `ellrank` [0,0], torsion Z/2 × Z/6, and the hand 2-descent of S7 (d, e). LMFDB 90.c3 has the same j-invariant and point counts (a).
- **Section 6.** Proposition 6.1, amp_0..amp_4, ζ_3..ζ_5, and every δ_thm of Table S4 (d, e).
- **Figures.** Every figure against its data. One reviewer mapped the Figure 1 rasters pixel by pixel to the colour bar (e).
- **Citations.** About 50 references at statement level (e). All DOIs and bibliographic data are correct.

## Recommendations

| reviewer | recommendation (confidence) | main reasons |
|---|---|---|
| a, AGAG handling editor (moduli-space spectral theory) | **send to review; desk-reject probability 30%**; provisional view **major revision** (about 60%) | M1 analytic contribution not explicit for AGAG; M2 §2.4 sketches; M3 abstract; M4 proofs in the supplement; M5 boundary with Paper B |
| b, conic heat invariants | **minor revision** (high for §§2.1–2.3 and App. B; moderate-to-high for §2.4) | M1 §2.4 propositions proved only by sketch; M2 §2.4 computations undocumented |
| c, PTE and moment problem | **minor revision** (high) | M1 abstract misstates Theorem 1.1(ii) |
| d, appendix analyst | **minor revision**, conditional on M1–M2 (high, except moderate for §2.4) | M1 §2.4 sketches; M2 heat-trace to heat-invariant link asserted |
| e, rigour, citations, figures | **minor revision** (about 0.8) | M1 abstract; M2 §2.4 sketches; M3 pinpoint and attribution cluster |

**The editor's desk-reject estimate (30%), with its reasons as stated.**

*For desk rejection:*
- Once a known expansion is granted, the core results are algebraic or Diophantine (M1).
- The headline growth theorem is an equivalence with an open problem, not a determination.
- The most analytic section (§2.4) consists of sketches.
- The three-manuscript pattern needs explanation.

*Against desk rejection:*
- The topic is squarely in AGAG's tradition.
- Everything the editor recomputed is correct.
- M+1 and the triangle classification are new, and answer DGGW Rem. 5.16.
- Prior work and computational claims are labelled carefully.

The editor would send the paper to review with two referees, one in orbifold heat invariants and one in PTE or elliptic curves.

## Deduplicated issue table

**Columns.**
- *Severity* is the highest any reviewer gave; where the synthesis changes it, the reason is stated.
- *Type:* M = mathematics, C = computation, W = writing.
- *Status* uses the brief's labels: CONFIRMED / ANSWERED IN PAPER / ANSWERED IN REPOSITORY BUT NOT PAPER. Disputes were settled from the LaTeX source, the fetched sources in the repository, or the repository's scripts.

### FATAL

None.

### MAJOR

| ID | reviewers | severity | location | issue | resolution | type | status and check |
|---|---|---|---|---|---|---|---|
| **A1** | a M3, c M1, e M1 | MAJOR (claim not supported) | Abstract, p. 1; also p. 5 ("makes the growth question equivalent") | The abstract says f grows "like a power A^α of the area exactly when … N(k) = O(k^{1/α})". Theorem 1.1(ii) and Theorem 3.14(d) prove only the lower-bound equivalence f(A) ≥ cA^α ⇔ N(k) = O(k^{1/α}), together with a one-way upper statement. Read literally, the abstract asserts f ≍ A^{1/2} (since N(k) = O(k²) is known), which contradicts p. 3: "Whether f grows like a power of A at all is open." | Change "like a power A^α" to "at least like A^α (for large A)". Optionally add "and O(A^α) when N(k) ≥ ck^{1/α}". On p. 5, name the question: linear growth, or power lower bounds. | W | **CONFIRMED.** `manuscript.tex:113` reads "and like a power $A^\alpha$ of the area exactly when the Prouhet--Tarry--Escott function satisfies $N(k)=O(k^{1/\alpha})$". Theorem 1.1(ii) and the sentence at `:147` are correct. Blocking under (i): a claim of record that the paper does not prove. A one-phrase fix. |
| **A2** | a M2, b M1+M2, d M1, e M2 | MAJOR (rigour) | §2.4, Props 2.11 and 2.12, pp. 11–14; Introduction p. 3; end of §2.4; Problem 5 | (1) Propositions 2.11(i)–(iv) and 2.12(i)–(iii) are followed by "Sketch", not a proof. The load-bearing steps are asserted: the pole order "to all orders", the reduction of the top pole to the Jacobi-field term, the Duhamel linear response for (iii), "an exact computation" for (iv), the second-order constant ω_n, and the gluing in 2.12(ii). (2) The computations behind (iv), and the "independent computation", are not described in S8. (3) "confirms … (iii) for every l" cannot be the output of a computation. (4) [v^{2l}], J^{-1} and the directional average are undefined (b m2, e). (5) The introduction and the end of §2.4 present these as established. All five reviewers who looked found every explicit claim correct; b verified (iv) exactly, (ii) for l ≤ 4 and (iii) for l ≤ 5 by an independent method. | Either (a) give full proofs: a pole-order count, the Jacobi-field reduction, the linear response, documented exact computer algebra for (iv) and ω_n, and 2.12(ii) with a flat cylinder built in from the start (b m6). Or (b) relabel 2.11 and 2.12(i)–(ii) as claims or remarks with sketches, keep "Proposition" for 2.12(iii), whose sketch the reviewers judge essentially complete, and soften p. 3 and the end of §2.4. In both cases, add an S8 subsection on the variable-curvature computations (method, truncation, normalisations, range of l), and replace "(iii) for every l" by "l ≤ 7" or by a proof. | M + C + W | **CONFIRMED** (`manuscript.tex:370–413`: both proofs are headed `\begin{proof}[Sketch]`; the supplement has no description of these computations). **ANSWERED IN REPOSITORY BUT NOT PAPER** for the computations: `theory/varcurv/top_coefficient.py` gives β_{l,l+1} for l ≤ 7 and p_3, and `linear_part.py` checks (iii) for **l ≤ 7** ("checked for l <= 7 on all monomials … 833 cases"); `quadratic_form.py`, `obstruction_check.py` and `twisted_mp.py` cover 2.12. So "(iii) for every l" overstates the repository too. No main theorem depends on §2.4 (a, b, d, e). Blocking under (i) as a rigour item. |
| **A3** | d M2 | MAJOR (claim not supported) | p. 40, end of App. B ("(6) is the link between a heat trace and the heat invariants"); p. 36 after Cor. 6.5 ("δ_1 … for instance from (6)"); p. 33, opening of §6 | The text says that, below (π/μ)², heat-trace data determine the heat invariants "up to an error that is explicit once the systole and diameter are bounded". This is not proved, for three reasons. (6) needs an a-priori bound on the largest order μ, which is what §6 recovers. Extracting c_1..c_n from samples of Z(t) needs an extrapolation step whose conditioning is not analysed. And S5 uses heuristic error bars. Theorem 6.2 and Corollary 6.5 themselves are correct, as statements about approximate invariants. | Either (a) add a lemma: given Z(t_i) to accuracy ε together with bounds μ_max, ℓ_0, D and n, the invariants are determined to an explicit δ_1 (from (6), Lemma 2.5 and a Vandermonde inverse bound). Or (b) reword the three passages to say that the conversion needs a-priori bounds on the largest order, systole and diameter plus an extrapolation step not analysed here. Put the δ_1 caveat into the statement of Cor. 6.5 (d m9). | W (or M with option a) | **CONFIRMED.** `manuscript.tex:1038`: "heat-trace data determine the heat invariants up to an error that is explicit once the systole and diameter are bounded: \eqref{eq:Grem} is the link …"; `:908`: "$\delta_1$ is an error bound for the data, for instance from \eqref{eq:Grem}". No lemma in the paper or supplement does the extrapolation. Blocking under (i) as a statement the paper does not support. Rewording option (b) suffices. |
| A4 | e M3 (with c m6, m7) | MAJOR → **MINOR** (writing; the synthesis downgrades it because no claim of the paper's own results is affected) | §1.2, §§2–4, p. 23 | A cluster of attribution and pinpoint errors: Doyle–Rossetti [5] versus [18]; Donnelly 1976 versus 1979 for orbifold locality; DGGW's c = 12c_2; Garbin–Jorgenson Rem. 2.7 as "classical in substance"; Stanhope [14] proves bounds, not determination; Uçar pp. 98–99 rather than 98–103; Borwein–Ingalls p. 10 for the Letac–Gloden attribution; BLP p. 2069; openness of N(k) = k+1 credited to [47], not [46]; Wróblewski versus Chen for (A.313). | Apply e m1–m9 and c m6. | W | **CONFIRMED** on the items checked against the sources in the repository: **(A.313)** is "by Chen Shuwen in 2000"; only (A.314) onward are Wróblewski 2009 (`theory/pte/sources/ChenShuwen2025_survey_arXiv2506.11429.txt`), while `manuscript.tex:666` says "the last found by Wr\'oblewski in 2009". **Borwein–Ingalls**: the Letac–Gloden attribution is on printed p. 10 (`theory/pte/sources/BorweinIngalls1994_EnsMath40_pages3-27.txt`), while `:666` cites "pp.~9, 25". **Doyle–Rossetti**: `:185` cites the NYJM 2008 surfaces paper as having "proved independently" the orbifold statement, whose proof is in arXiv:1103.4372 (the bib entry doylerossetti2011, which the paper also cites at `:189`). The remaining pinpoints were not re-fetched; the reviewer's checks are specific. Not blocking: these are citation corrections. |
| A5 | a M1 | MAJOR (significance) | §§1.1–1.2, p. 5 | After Lemma 2.10 every main theorem is about multisets of integers. No count is turned into a statement about the heat trace at positive time or about eigenvalues, and that link is deferred to Paper B. | Add a paragraph to §1 listing the analytic inputs (trace formula with bracketing remainders, the time scale (π/μ)², Theorem 4.2) and what they give for heat traces at positive time, plus one sentence on the eigenvalue consequence via Paper B. Argue the venue in the cover letter. | W | **CONFIRMED as a judgement** (the paper itself says so at `:183`, "What is elementary and what is not"). Significance and scope, so **not blocking** under (i). It feeds the 30% estimate. |
| A6 | a M4 | MAJOR (editorial) | Thm 5.8 rank; Thm 6.2 constants | Parts of the proofs of headline results are in the supplement (S7 descent, S3 constants). | Say so in the proofs; cite LMFDB 90.c3. | W | **ANSWERED IN PAPER.** `manuscript.tex:847` says the descent "is written out by hand in Section~\sref{app:descent} of the supplement", with PARI as independent confirmation. Theorem 6.2 says "(supplement, Theorem~\sref{thm:S3})" and "(supplement, Theorem~\sref{thm:S4})". Only the LMFDB citation is new (writing). |
| A7 | a M5 | MAJOR (editorial) | p. 5; S4/S6 versus B §7.1 | The boundary with Paper B must be explicit: the same trace-formula set-up, the same computed spectra and near-verbatim method text. A §6 with S5 and B's Thm 7.1 are "two versions of one programme". | One sentence in §1 of each paper on what each contributes; say that the data and method description are shared, cite one Zenodo deposit; address it in the cover letter. | W | **ANSWERED IN PAPER in part**: the editor found the disclosure good (A p. 5; B Table 1) and judged the papers not redundant ("each has its own main theorem"). The contribution sentence and shared-data sentence are missing (writing). Not blocking. |

### MINOR (deduplicated; all CONFIRMED by the reviewer's own check unless noted; none blocking)

| ID | reviewers | location | issue | resolution | type |
|---|---|---|---|---|---|
| A8 | a P1, b (Fig.), d P1, e (Fig.) | Fig. 1, p. 2 | The rendered tips do not visibly approach m: at print size the order-8 and order-12 tips read about 4–6 on the colour bar. e's pixel mapping finds maxima of about 8.1 and 11.3 in the rasters, so the values are there but sub-visible. "Lifted to a surface in space" versus "schematic shapes" mismatch (a); "heat kernel on the true hyperbolic triangle" is ambiguous between Neumann and Dirichlet (e m13). | Caption: say the extreme values occupy a √t-sized region at the tip, or inset the cusps; say the plotted kernel is ½(h^N + h^D); make text and caption agree. | W |
| A9 | a m2, d P2, e m11, c (Fig. 3) | Fig. 3, p. 24 | Constructed pairs are drawn at K_mult = L+1, but this is only a lower bound; the legend is only in the text. | "K_mult ≥ L+1"; put the marker key in the caption; say the dashed curve is from s = 4 (A ≥ 8π). | W |
| A10 | c m2, a m3 | Thm 1.1(ii), Prop. 3.15 | "f(A) = o(A) iff N(k)/k → ∞" introduced with "in particular" but needs the sandwich bounds and monotonicity (true; c and d checked). The quantifier "for all large A" and the monotonicity of N are implicit. | Write out the 3–4 lines; make the quantifier explicit. | W |
| A11 | c m1 | Thm 3.11 proof, Prop. 3.15 | Uses \|Z\| ≥ 2L+2 for arbitrary L-configurations, while Theorem 3.4 is stated for orbifold pairs. | State the configuration version as a lemma. | W |
| A12 | d m1 | Lemma 5.3(ii) proof, p. 30 | "For S ≥ 3p+3 the stratum p+1 contains its hyperbolic spread triad" is false at (p, S) = (2, 9). The lemma survives (gap_2(9), gap_2(10) > 0). | Exclude the case or assume both strata nonempty. | M (local) |
| A13 | a m1 | Prop. 2.12(ii), p. 13 | "For any L" is false at L = 1. | "L ≥ 2". | W |
| A14 | b m5, m7 | Prop. 2.12(i); p. 14 l. 2–4 | "Lemma 3.3 holds verbatim" and "everything deduced from it" are too broad (equal c_1 no longer means equal χ). "Heat invariants of any finite order hear only c_2" overstates 2.12(ii), whose metrics depend on L. | List the results that transfer, with the Ω-hypotheses; reword as b suggests. | W |
| A15 | b m1, m2, m3, m4, m10 | §2.3–2.4 | Reflection-evenness argument (use the j ↔ m−j pairing); J "in an orbifold chart"; at curvature K also α_k → α_k(−K)^k; normalisation of u_k; the real-m extension is algebraic only. | As listed. | W |
| A16 | d m3, e m17 | Prop. S2.2 proof, Suppl. p. 7 | The odd-parity argument is circular as written (statement true; d checked p < 400). | Give the p ≥ 9 / p ≤ 8 argument. | W |
| A17 | d m4, c m10 | after Thm 3.8, p. 19; p. 23 | Search-only statements (minimal areas M = 3, 4; the "odd symmetric 5-sets … ≤ 200" sentence) are not listed in S8, against the paper's own policy. | List them in S8; define or drop the p. 23 sentence. | W |
| A18 | e m14 | Table S4 caption; p. 35 | "Every other entry rounded down", but the ratio column is rounded to nearest (e.g. 1.1359 printed as 1.14; also 2.05, 1.25, 1.03, 1.06, 1.36, 6.72). | Round down or amend the caption and "1.03–6.72". | C/W |
| A19 | e m10, a P2–P5, d P3, c (Fig. 2) | Figs 2, 4, 5, 7, 8 | Captions not self-contained (marker keys, the grey band in 5(b), line styles in 8); Fig. 2(a) lower row draws X, not X*; Fig. 4 square-root axis not stated; Fig. 8 "worst-case error" is over the 2^n vertices. | One sentence per caption. | W |
| A20 | e m16, c m8, c m9, c m3, c m4, c m5, c m11, d m6, d m7, d m5, a m4, a m5, a m6, a m7, a m11, a m12, e m19, e m21, d m8 | §§3–6 | Small statement and proof wording items: ν sign change between 3.8(ii) and (iv); why s is an integer; (g; U∖{1}); vacuous "every entry of W is 1"; Thm 3.13 phrasing (smaller genus "any g ≥ 2"); witness entries ≥ 2; β > 0 and C ≥ 1 in 3.14(b); Lemma A.1 phrasing; A_min attained; "explicit formulas" versus cond in Thm 6.2; "Off this family … (0;5,5,5)"; uniform hypotheses in Thm 1.3(i)/A/C(2); Δ declared after first use; the asymptotic of b_l(m) unproved; the matched norm in Fig. 8; name a = 8 in Prop. 6.3(i); sign in Thm 4.2(b). | As listed in the reports. | W |
| A21 | a m8 | refs [7], [34] | Status of the three manuscripts inconsistent ("in preparation" versus "submitted"). | Make consistent. | W |
| A22 | a m9 | §5 | The note's unbounded collision classes and ≫ X(log X)² count are not mentioned. | One sentence citing the note. | W |
| A23 | e m15 | Suppl. p. 7 | "moved here from the paper" is an editorial leftover. | Delete. | W |
| A24 | a (data statement) | p. 37 data statement; Suppl. S1, Table S1 caption | Internal repository paths `review/round1-fixes/d2_explicit_pairs.py`, `review/round1-fixes/d1_pencil_counts.py` and `paper/jga/tools/make_tables.py` reveal a review history and a different target journal ("jga"); `theory/threshold/` is a directory. The paragraph is badly justified. | Replace with neutral script names inside the Zenodo deposit; fix the justification. | W |
| A25 | a, b m9, e m20, e m8, e m9 | notation, refs | Overloaded symbols (R, Z, B, b_l, χ, σ, φ/ψ, ϱ, T, M, C); the letter a used for both a node and the leading coefficient a_l (c); the [v^{2l}] notation; issue numbers for [39], [49]; an equation number for [10]; the Thurston numbering 13.3.4; Hejhal/Iwaniec admissibility remark. | Rename (e.g. λ_l for the leading coefficient, ρ for the rotation); extend Table 1. | W |

## Writing-level fixes worth making before submission, ranked

Ranked by effect on the gate first, then on referee and editor reception.

1. **Abstract (A1).** Change "and like a power $A^\alpha$ of the area exactly when" to "and at least like a power $A^\alpha$ of the area exactly when". On p. 5 name the question ("makes the question of linear growth, and of power lower bounds, equivalent …"). One line; removes a blocking item.
2. **Section 2.4 status (A2).** The writing route: rename Propositions 2.11 and 2.12(i)–(ii) to "Claim" or "Remark (sketch)", keep 2.12(iii) as a Proposition, and add one sentence saying that nothing else in the paper depends on §2.4. Then:
   - replace "(iii) for every l" by "(iii) for l ≤ 7";
   - add a short S8 subsection naming the variable-curvature computations (method, truncation, l-range);
   - define [v^{2l}], J and the chart;
   - put a flat cylinder in the 2.12(ii) construction from the start;
   - soften p. 3 and the end of §2.4 (A14).

   This also removes one of the editor's four desk-reject reasons.
3. **Heat trace to invariants (A3).** Reword `manuscript.tex:1038`, `:908` and the opening of §6 to state the a-priori bounds and the unanalysed extrapolation step, and put the δ_1 caveat into Corollary 6.5.
4. **Analytic contribution paragraph (A5) and the B boundary (A7).**
   - One paragraph in §1: what the analysis gives for heat traces at positive time, the (π/μ)² scale, Theorem 4.2, and the eigenvalue consequence through Paper B.
   - One sentence on what Paper A contributes that Paper B does not, and that the spectra and method text are shared through the one deposit.
   - The same points in the cover letter, with the venue argument.

   These address the remaining desk-reject reasons.
5. **Internal paths in the data statement and supplement (A24).** Remove `review/round1-fixes/…` (three occurrences) and `paper/jga/tools/…`, which reveal the review history and an earlier target journal.
6. **Citations (A4).** Doyle–Rossetti [18] for the orbifold proof; Donnelly 1979 for orbifold locality; Chen (A.313) versus Wróblewski (A.314)–(A.316); Borwein–Ingalls p. 10; BLP pp. 2064, 2069; [47] for the openness of N(k) = k+1; Stanhope as bounds; Garbin–Jorgenson "follows from"; Uçar pp. 98–99; c = 12c_2; cite LMFDB 90.c3 (A6).
7. **Figure captions (A8, A9, A19).** Figure 1 tip resolution and kernel; Figure 3 "K_mult ≥ L+1" and key; self-contained captions for Figures 2, 4, 5, 7, 8.
8. **Small proof-text gaps (A10–A13, A16).** The o(A) equivalence written out; the configuration lemma \|Z\| ≥ 2L+2; Lemma 5.3(ii) at (2, 9); "L ≥ 2" in Prop. 2.12(ii); Proposition S2.2's odd-parity argument.
9. **Search statements into S8 (A17)** and **Table S4 rounding (A18).**
10. **Remaining wording and notation (A15, A20–A23, A25).**
