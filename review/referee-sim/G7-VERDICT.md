# G7 (simulated JGA peer review): verdict

## **NEEDS SUBSTANTIVE WORK**

Five independent simulated referees reviewed the built manuscript: a spectral geometer (SG), a geometric analyst (GA), a number theorist (NT), a numerical analyst (NA) and the handling editor (HE). Each saw only the PDF: 56 pp., SHA-256 `236500606921bb46…7049223`, built from `8a9ebf0` (see [README.md](README.md)).

**Correctness.** No referee found a mathematical error in any theorem, lemma or proposition. Between them they independently recomputed most of the paper and found it correct:
- the heat coefficients, re-derived from the trace formula to 40 digits through t⁸;
- Theorem B;
- every Section 5 count, to S = 6000;
- the rank-0 proof, by two independent hand-written 2-descents;
- every δ_thm and δ_up value;
- the moduli-family λ₁, by an independent FEM.

The only misprinted number is the projective point 3P after Thm 8.9.

**Recommendations.** All five recommend **major revision**. The handling editor puts the **desk-reject probability at about 50%**.

**What drives that consensus.** It is not the correctness of the mathematics. It is four things:
- scope and length (a JGA paper with a number-theory paper and a numerics paper inside it);
- novelty claims that the classical literature does not support, especially Section 4;
- the all-l input resting on an unrefereed thesis;
- proofs and computations that live only in the repository, or have not been run.

Most items need writing only. Four need real work beyond wording, listed in the verdict below.

---

## 1. The five recommendations

| Referee | Recommendation | Confidence | MAJOR issues |
|---|---|---|---|
| (a) Spectral geometer | Major revision | medium-high | 4 |
| (b) Geometric analyst | Major revision | medium | 4 |
| (c) Number theorist | Major revision | medium-high (own area) | 3 |
| (d) Numerical analyst | Major revision | medium-high (numerics) | 5 |
| (e) Handling editor | Major revision, conditional on restructuring | medium | 6 |

**Handling editor's desk-reject probability: about 50%.**

| Reasons for desk rejection | Reasons against |
|---|---|
| About 40% of the paper is out of JGA's scope. | The question is natural. |
| The "shape" half is classical. | The paper settles DGGW Rem. 5.16. |
| Proofs rest on a thesis and on repository-only verifications. | The ⌊Area/π⌋+4 bound, the Prouhet construction and the sharp threshold 17 with its isolated pair are new and correct. |
| The paper shows visibly unfinished work. | The paper is honest about prior work. |
| It is long for its new content. | |

The editor's view: a focused 25–30-page version would be a reasonable JGA submission.

## 2. Deduplicated issue table

**Severity.**
- **FATAL:** none was raised.
- **MAJOR:** must be resolved before submission.
- **MINOR:** should be fixed.
- **PRESENTATION:** wording, layout or figures.

**Work needed.**
- **W:** writing only.
- **M:** new mathematics.
- **C:** new computation.

**Status.** Every FATAL or MAJOR item was checked against the repository and given one of three statuses:
- **CONFIRMED:** a real problem.
- **ANSWERED IN PAPER:** the referee missed it, so it becomes a presentation issue.
- **ANSWERED IN REPO, NOT PAPER:** the work exists in the repository but needs writing into the paper.

Items a referee raised as MAJOR that turned out to be answered are marked as such. They are kept in the MAJOR block so the provenance is visible, but they demote to the severity shown in their status.

### MAJOR

| ID | Source | Location | Issue | What resolves it | Work | Status (repository evidence) |
|---|---|---|---|---|---|---|
| G7-1 | HE M1, SG M3, NT M3, GA p1 | whole paper; §§6.5, 7, 8, App. A, B; MSC 11xx | The paper is three papers, and only §§2–5 (plus a condensed §6) fit JGA. About 22 of 56 pp. are number theory or numerics that no proof of Theorems 1.1–1.3 uses. This is the main desk-reject risk. | Restructure into a 25–35 pp. JGA paper: §§2–5, a condensed §6.1–6.4, and Thm 5.16. Move §6.5 and §7 to a supplement. Split §8 and Appendix A into a separate arithmetic note. Drop the 11xx MSC codes accordingly. | W (structural) | **CONFIRMED.** A structural decision for the authors, not a defect in any result. |
| G7-2 | SG M1, GA M1, HE M2 | Thm 1.2; Thm 4.1, Cor. 4.5, Thm 4.6, Lemma 4.7, Thms 4.9–4.11; §1.1 | Section 4 is presented as a headline theorem but is classical or immediate. Signature-locality is Uçar Thm 4.20 at K = −1, and McKean 1972 for surfaces. The exponentially small difference is the standard Selberg/Huber mechanism. Lemma 4.7 is redundant with the classical admissible class (Hejhal LNM 548, Iwaniec), which covers e^{−t(1/4+r²)} with elliptic terms. | Demote Thm 1.2(i)–(ii) to a cited proposition. Present Thms 4.9–4.10 as an explicit packaging of the standard argument. Cite McKean 1972, Huber, Hejhal/Iwaniec and Buser. After reading Hejhal, cut Lemma 4.7 to a remark. Shorten §4 to about 4 pp. | W | **CONFIRMED.** McKean, Hejhal, Iwaniec, Buser and Wolpert are absent from `references.bib`. `theory/locality/attack-log.md:45` records that "Hejhal and Iwaniec were not fetched … Lemma 3.2 replaces them", so Lemma 4.7 exists only because the classical source was not consulted. |
| G7-3 | SG M2, GA M2, HE M3 | Prop. 2.4, Lemma 2.5, Lemma 2.10; Remark 4.12 | Every result of §3 needs Lemma 2.5 (p_l even, of degree exactly 2l+2, with nonzero leading coefficient and p_l(1) = 0) for **all** l. That rests only on (4.25) of Uçar's PhD thesis. Remark 4.12 wrongly calls the trace-formula route "not an independent proof": DGGW is refereed, and a Weyl-type bound for convergence does not make the coefficient values circular. | Prove Lemma 2.5 for all l from the elliptic term E_m(t) of Thm 4.6: polynomiality in m, parity, degree, leading coefficient and vanishing at m = 1 for the finite cosecant-derivative sums. Keep Uçar as corroboration. Correct Remark 4.12. | M (modest) + W | **CONFIRMED.** The all-l statement is proved only from (4.25)/(4.33): `review/audit/signatures/REVIEW.md` row SG.1, `theory/divergence/STATUS.md` ("given Uçar's (4.25)/(4.33) for all ℓ"). `theory/locality/proof.md` already calls Proof C "independent of the coefficient computations of [DGGW] and [Uçar]", which contradicts the paper's Remark 4.12. Two referees independently matched (4) to 40 digits for l ≤ 8 (SG) and l ≤ 5 (GA), so the formula is not in doubt; only the proof is. |
| G7-4 | HE M4, SG M3, GA M4, NT m1/m2 | Remark 2.12; Thm 5.13 statement; Prop. 5.15(2); Thm 5.16; Prop. 6.10 step 3 | Proofs or certificates sit in the repository, not the paper. Remark 2.12 says "The proofs are in the repository". Thm 5.13's statement contains "…33, and so on". Thm 5.16 rests on PARI output and an unwritten descent. Prop. 6.10 does not specify how r_rem is bounded, so δ_cert cannot be checked. | (a) Write the 2-isogeny descent for E: y² = x(x+9)(x+384) in the paper (half a page; S^φ = {±1, ±6}, S^φ′ = {1}) and state torsion via #E(F₇) = #E(F₁₁) = 12. (b) List all 38 collision-free sums, or move them to a labelled computational proposition with the method. (c) Prove Remark 2.12 or cut it. (d) Write the explicit r_rem and \|δM\| bounds of Prop. 6.10. | W | **ANSWERED IN REPO, NOT PAPER.** (a) `review/audit/diophantine/check_descent.py` and `.txt`; NT and SG each re-derived the same Selmer groups by hand. (c) `theory/divergence/proof.md` (Theorems 2–3, Lemma 1). (d) `theory/stability/proof.md` ll. 380–412 and `theory/stability/threshold.py`; the repository's proof is no more explicit than the paper, so the formulas must be written out from the code. HE's further request for an infinite-order proof in Thm 8.9 is **ANSWERED IN PAPER**: Thm 8.9 already uses nP ≠ O for n ≤ 12 with Mazur's bound (manuscript l. 1423). |
| G7-5 | HE M5, SG M3, NA M3, GA m12 | §7.1 Limitations; Appendix C | The four §7.1 spectra were computed with a single-window solver that the authors found can miss an eigenvalue. The double-window recomputation "has not yet been run". The trace test also cannot see a missed eigenvalue in about 1.7–2.4×10⁴. | Run `numerics/rerun_double_window.py` on all four problems and commit `data/rerun_double_window_comparison.json`. Report the agreement, and restrict "no eigenvalue is missing" to the range the trace test covers. | C (heavy: 4 NGSolve runs at h = 0.05, p = 10, NEV = 1300) | **CONFIRMED.** The tool exists, but `numerics/data/rerun_double_window_comparison.json` does not, and `paper/jga/OUTSTANDING.md:130` records it as not run. |
| G7-6 | HE M6, NT M1, SG m6/M1 | bibliography; §1.1; §8.3 (Thm 8.9); §3 (Thm A) | Missing references and overstated novelty in three places. (i) Thm 8.9: "what is new is the normalization by rescaling" is exactly Schinzel's step (Zhang–Cai 2013), so it is not new. (ii) Thm A: the odd-power-sum determination modulo ± pairs is classical, and the paper should state and cite it. (iii) Missing references: McKean 1972; Hejhal/Iwaniec; Wolpert 1979; Gordon's orbifold survey; Stanhope 2005; Kelly 1964; Zhang–Cai 2013; Guy D16; Bremner–Guy 1997; Sadek–El-Sissi 2015; Schoen 1988; the Prouhet–Tarry–Escott literature; NGSolve and cypari2; and the 2017 DGGW erratum. | Remove the Thm 8.9 novelty claim. Restate Theorem A's novelty against the classical fact. Add the references, and recalibrate "to our knowledge the first" and "answers the question left open". | W | **CONFIRMED.** For the erratum, the work is done but not cited: it was read in G5 (`review/audit/literature/PRIORITY-notes.md:20`, which finds it changes only DGGW Thm 5.1) and has a BibTeX entry in `refs/sources.bib:32`, but it is not in `paper/jga/references.bib`. The Thm A prior art in `review/audit/THEOREM-A-PRIOR-ART.md` covers only the positive-real case, so the complex claim needs this check. |
| G7-7 | SG M4, GA m8/m9, HE m4 | abstract; Thm 1.4; Prop. 6.7(ii); Remarks 6.1, 6.8 | "Both rates are sharp" overstates. Sharpness of 1/k for k ≥ 3 holds for arbitrary data vectors; realizable data from real multisets at a triple order give exponent 1/2. There is also no theorem linking eigenvalue errors to errors in c_j, and the thresholds are evaluated at the unknown true m. | Qualify the abstract and Thm 1.4 ("for general data; ½ for realizable data at a triple order"). Frame §6 as conditioning of the algebraic inverse problem. State the a-posteriori logic (recover, then certify at the candidate). | W | **CONFIRMED.** Remark 6.8 in the paper already states the ½ exponent, so this is a wording error in the abstract and Thm 1.4, not a missing result. |
| G7-8 | GA M3, SG m3, HE m6 | Thm 1.2(iii) "C is explicit"; Thm 4.9(b); abstract "attained" | The constant contains e^{3·diam}, and the diameter is not a signature or spectral quantity. "Attained" holds only when the length spectra first differ at the systole. | State C = C(A, ℓ, diam) in Thm 1.2 and qualify "attained". Optionally, replace Lemma 4.8 with a geodesic-counting bound depending on (area, systole) only. | W (M if the improved counting bound is wanted) | **CONFIRMED.** The diameter dependence is in `theory/locality/proof.md:357`. |
| G7-9 | NT M2 | §8.4, Conjecture 8.10; manuscript l. 1414 | Conjecture 8.10 has no upper bound. The heuristic sentence "every family found is a rational surface" is wrong: the isosceles family is a rational curve, and a quadratic surface family would give X^{3/2}. NT's data to S ≈ 2×10⁴ cannot tell a cumulative exponent of 1+o(1) from about 1.4. | Prove 𝒩(X) ≪ X^{3+ε}; NT sketches a divisor-bound argument. Correct the heuristic sentence. Either downgrade the conjecture to a question or search for low-degree rational subvarieties. Add the fibre-product (Schoen-type) framing. | M (easy upper bound) + W | **CONFIRMED.** The sentence is verbatim at l. 1414. If G7-1 moves §8 out of the paper, this travels with it. |
| G7-10 | NA M1 | §7.1, §7.2 error budgets; Table 3 error bars; "certified" | The paper states the budget (3×10⁻¹¹) but never derives it. NA's worst-case propagation, using the quoted maximum relative error for every eigenvalue, gives up to 3×10⁴ times more. The Table 3 and d₃/d₄ error bars are undefined. | Print the budget formula and tabulate the per-eigenvalue estimates by index block. Define the error bars as fit uncertainty, max(data error, order change), with no σ language. Label "certified" as conditional on non-rigorous error bars. | W | **ANSWERED IN REPO, NOT PAPER** for the budget. `numerics/heat_trace.py:70–80` computes t·Σ err_j e^{−t(λ_j−err_j)} with per-eigenvalue absolute estimates and no cancellation assumed. From the committed `eigenvalues_*.csv` this gives 2.8×10⁻¹¹ at t = 0.0015 and 1.4×10⁻¹² at t = 0.03, inside the stated 3×10⁻¹¹. NA's objection comes from the paper quoting only the maximum relative error. **CONFIRMED** for the error bars: `heat_trace.py headline()` defines them as max(propagated data error, change from order n−1). That is heuristic, and the paper does not say so. |
| G7-11 | NA M2 | §7.1 Method/Validation; §7.2; Appendix C | The discretisation and convergence evidence cannot be assessed from the paper. Missing: the second discretisation, any h/p convergence table, the geometry representation, the quadrature order, corner regularity, eigensolver settings, and software versions. | Add a parameter table, a convergence table for representative eigenvalues (λ₁, λ₅₀₀, λ₁₄₀₀ per class), and a paragraph on corner regularity (reflection makes the N/D corner eigenfunctions smooth). | W | **ANSWERED IN REPO, NOT PAPER.** `numerics/data/convergence.csv` (5,699 rows) gives every eigenvalue under h = 0.1/0.07/0.05 and p = 8/10/12. `numerics/REPORT.md` and `numerics/requirements.txt` hold the method and pinned versions. |
| G7-12 | NA M4 | §7.1 Bolza sentence | "Reproduces all 42 multiplicity-one eigenvalues … which covers the (2,3,8) triangle orbifold" misdescribes the benchmark. Only 21 of the 42 belong to O(2,3,8) (N ∪ D); the other 21 are mixed-boundary characters. It also covers only λ < 998. | Describe the four characters (N 15, D 6, M1 10, M2 11). Optionally add a high-λ benchmark (the full Strohmaier–Uski list, or a Bolza trace test). | W (C optional) | **ANSWERED IN REPO, NOT PAPER.** `numerics/REPORT.md` §4(b) and `data/bolza_benchmark.csv` show all four characters were computed and matched one-to-one. NA's independent FEM gives the same split. |
| G7-13 | NA M5 | §6.5, Table 3; Appendix C | The blind recovery assumed g = 0 and n = 3, and only the labels were blinded. It separates two candidates whose c₃ differ by about 10⁴ error bars, so it exercises the pipeline rather than a hard inference. The protocol is not quoted. | State what was assumed and what was blinded, and quote the protocol commit `3c1139a` (2026-10-01). Optionally make it signature-blind (area π/2 admits finitely many signatures) and add decoys. Or shorten it and move it to the supplement under G7-1. | W (C optional, cheap) | **ANSWERED IN REPO, NOT PAPER** for the protocol and assumptions: `theory/stability/blind/PROTOCOL.md` states "genus 0 and exactly n = 3 … This structural fact is used", committed in `3c1139a` before any result. **CONFIRMED** that the test is easy by design. |
| G7-14 | HE M4/m18 | Data availability; Appendix C | The code repository is `github.com/Ali-M658/Arithmetic-verification`, an account that matches none of the six listed authors. An editor will ask about ownership, credit and licence. | Move the repository to an author-owned account or organisation, or state the account holder's relation to the work. Add a licence. Mint the Zenodo DOI under the authors. | W (administrative) | **CONFIRMED.** `git remote -v` points at that account, and no author is named Ali. |

### MINOR

| ID | Source | Location | Issue | What resolves it | Work |
|---|---|---|---|---|---|
| G7-15 | SG m1, NT m6 | p. 49, after Thm 8.9 | 3P is printed as (162833463 : 287876366 : 723926268). With O = (1:−1:0) it is (162833463 : 723926268 : 287876366), and the printed point is a different point. **The repository's own audit check accepts it only "as a set"** (`review/audit/diophantine/check_groups.py:99`, output `check_groups.txt:88`). | Print the computed order, or say "up to permutation". Tighten the audit check to compare ordered coordinates. | W |
| G7-16 | HE §3.2/m10, NT m10 | Table 5, p. 49 | The S = 6000 row and the "1.58 near 6000" and "0.00405 at 6000" figures come from outside the stated enumeration range (S ≤ 4800). The primitive-class column is blank at 6000. | Say the 6000 row comes from the G5 independent enumeration (`review/audit/threshold/check_enum.txt`). Fill in 62,401, as computed by NT. | W |
| G7-17 | NA m1 | p. 41 | "Binding coefficient is c₃ … 7×10⁻⁴" misreads the uniform model. Perturbed one at a time, c₂ is the most sensitive coefficient (0.28%) and c₃ tolerates 0.93%. | Rephrase, or give single-coefficient tolerances. | W |
| G7-18 | GA m1, NA m2 | p. 37 | "cond between 1 and 3.5" should be at most 3.511, and "Hadamard 12 to 4425" should be 11.9 to 4425.1. | Round outward. | W |
| G7-19 | SG m10, GA m2 | Prop. 6.7(i) | δR is printed in two equal but different forms. | Use one form. | W |
| G7-20 | SG m11, GA m3, HE m7 | Prop. 4.4 | The proof is heavy. Countable mapping-class orbits on Teich ≅ R^d give it in one line. | Replace it. | W |
| G7-21 | SG m4, HE m5 | §1.1 | "Answers the question left open in [3, Rem. 5.16]" overstates; DGGW make a remark. | Quote the remark and use "settles the question raised in". | W |
| G7-22 | HE m3, SG m5 | Thm 1.1(iii); Cor. 3.12 | The log/linear gap appears only in Problem 1. Integer-order necessity is proved only for n = 3, 4. | State both in §1. | W |
| G7-23 | GA m5–m7, m13–m14; SG m7 | Lemma 4.7, Remark 4.12, Thm 4.9 proof, Prop. 4.3 | Test-function hypotheses are not verified, the Taylor-under-the-integral step is not justified, the monotonicity condition is imprecise, and the Troyanov statement is not quoted. | One sentence each (subsumed if Lemma 4.7 is cut under G7-2). | W |
| G7-24 | GA m10, m11 | §1, Table 3 | Stability is genus 0 with known n only, and Table 3 "certified" needs a caveat. | State the limitation and the caveat. | W |
| G7-25 | NA m3–m11 | §§6.5, 7.1, 7.2 | Unstated combination rules, a t-range without a lower limit, a two-term Weyl law that should have three terms, the detectable missing-eigenvalue range, the fit degree and weights, the second-machine tolerance, and the geodesic truncation estimate. | Specify each. | W |
| G7-26 | NT m3–m5, m7–m9, m11–m12 | Prop. 8.2, §8 | The Γ₁(6) label, the explicit birational map, the egg-component argument, torsion for rational Λ ((Λ−1)(Λ−9) a square), the "most curves have positive rank" count, a lattice-point reference, and the fit protocol. | Specify each (moves with §8 under G7-1). | W |
| G7-27 | SG m8, m2, m12 | Thm 3.10(a); Prop. 5.2; Remark 3.3 | The cone orders are astronomically large (about 1.6×10⁸ at L = 3), the non-vanishing argument is roundabout (S₁R ≥ 9 > 1 suffices), and the Remark 3.3 reference is unclear. | One sentence each. | W |
| G7-28 | HE m9 | Fig. 2(a), lower panel | The "configuration that sharing c₃ would force" draws U* = V*, contradicting the disjointness in the proof of Thm 3.6. | Redraw it or correct the caption. | W (figure) |
| G7-29 | HE m11 | references [4], [10], [23], [27], [29], [35], [36] | Formatting: volume/part, capitalisation, the DOI underscore, the series name, the accent, the Mazur pinpoint, and a duplicated URL. | Fix each. | W |

### PRESENTATION

| ID | Source | Issue | Resolution |
|---|---|---|---|
| G7-30 | SG p1, GA p3, HE m2 | Lettered (A–C) and numbered theorems are interleaved. | Use one scheme, or add a roadmap table from the intro statements to the proofs. |
| G7-31 | SG p2, GA p2, HE p4, m12; NT p1 | Notation is overloaded: δ (diameter and error), T (four uses), P_n (class and power sum), ϱ, N(S) vs 𝒩(X). | Rename, and add a notation table. |
| G7-32 | HE p2, NA p2, p7; NT p2 | Figure problems: Fig. 5(a) has no t ticks; Fig. 5 and Fig. 4(b) are placed far from their discussion; Fig. 4(a) is decorative; "dark/light" captions need marker shapes; Fig. 1 writes 𝔥_t vs h_t; Fig. 7 needs p labels; Fig. 9 markers overlap. | Fix each. Cut Figs. 3, 7, 8(b) if §8 moves out. |
| G7-33 | HE p5–p8 | Abstract length; MSC primary not marked; line numbers; template residue "Corresponding author(s). E-mail(s):". | The abstract is 248 words in the source, inside JGA's 250 (HE counted about 255 from the PDF), but it will be rewritten anyway under G7-2/G7-7. Mark 58J53 as primary. Add `lineno` for review. Remove the residue. |
| G7-34 | HE m1, m13–m16; GA p4–p6; SG p3, p5 | Undefined "pillow", "complete area classes" and "witness classes are not isolated"; P_n used before its definition; Prop. 6.10 typo (M(Ĩ) = M(I)(I+X)); Fig. 1 explanation; formula parenthesisation; "genus 10⁴" renders as "104". | Fix each. |
| G7-35 | SG p7, GA p8, HE p9 | "To our knowledge the first…" is used repeatedly, and the introduction leans on metaphor. | Keep priority claims to Cor. 3.7, Thm 3.10 and Thm 1.3. |

## 3. Where the referees disagree

1. **How much of Section 6 belongs in JGA.**
   - **Positions:**
     - HE: reduce §6 to Thm 6.6 and Prop. 6.7, or move it to a supplement.
     - GA: the stability theory is among "the most interesting new mathematics" for JGA.
     - SG: keep a condensed §6.
     - NA: §6 is the part closest to numerical analysis.
   - **Assessment: GA is right.** §6.1–6.4 (explicit Lipschitz/Hölder constants, sharp exponents, a closed-form threshold) is genuine analysis and gives the paper an analytic second leg once §4 is demoted (G7-2). Keep §6.1–6.4, condensed. Move §6.5 (blind recovery) and the δ_cert machinery of Prop. 6.10 to the supplement with §7.

2. **Whether the triangle threshold is "mathematically light".**
   - **Positions:**
     - NT: the threshold is a finite check of 83 triads (Table B1), and Thm 5.11's stratum machinery explains only the number 18.
     - SG, HE, GA, NA: the threshold and isolated pair are among the paper's genuinely new results.
   - **Assessment: both are right about different things.** NT is right that the *threshold statement* needs only Table B1, and that Prop. 5.15 shows overlap does not predict collisions. The others are right that the result itself (sharp threshold, explicit minimal pair, rank-0 isolation) answers DGGW's remark and is the paper's most quotable new fact. **Resolution:** prove the threshold by the finite check in a few lines, keep Thm 5.11 as a short structural remark, and keep Thm 5.16 in full.

3. **Novelty of Theorem A.**
   - **Positions:**
     - SG: Theorem A is a modest variant of the classical fact that odd power sums determine a complex multiset modulo ± pairs.
     - HE: "pleasant algebra".
     - GA: praises Theorem B and accepts Theorem A.
   - **Assessment: SG is right in substance.** The parity argument is the classical one. What is new is replacing p_{2n−1} by R, the explicit system and determinant of Theorem B, and Theorem C's sharpness. The G5 prior-art file covers only the positive-real case, so the complex claim must be re-anchored (G7-6).

4. **The numerics error budget.**
   - **Positions:** NA says the 3×10⁻¹¹ budget cannot follow from the stated eigenvalue errors.
   - **Assessment: NA is wrong on substance and right on presentation.** The repository's budget is a worst-case sum over *per-eigenvalue* error estimates. Recomputed here from the committed data, it is 2.8×10⁻¹¹ at t = 0.0015. NA had only the paper's single maximum relative error to work with. The fix is to print the formula (G7-10). NA is fully right that the Table 3 error bars are heuristic and undefined.

5. **"Answers the question left open in DGGW Rem. 5.16."**
   - **Positions:** HE and SG say this is overstated. GA and NA accept it as written.
   - **Assessment: HE and SG are right.** DGGW say c "does not seem sufficiently strong to distinguish"; that is a remark, not a posed question. "Settles the question raised in" is accurate and loses nothing (G7-21).

6. **Lemma 4.7 (heat-function admissibility).**
   - **Positions:**
     - GA: unnecessary, because the classical Selberg admissible class covers the heat function for cocompact groups with elliptic elements.
     - SG: accepts it as correct.
   - **Assessment: GA is very likely right.** The repository records that Lemma 4.7 was written because Hejhal and Iwaniec were not fetched (`theory/locality/attack-log.md:45`). Before cutting it, fetch Hejhal LNM 548 and confirm that the theorem is stated for that class with elliptic terms.

7. **Infinite order of P in Theorem 8.9.**
   - **Positions:** HE asks for a Nagell–Lutz or reduction proof. NT and SG verified the paper's argument.
   - **Assessment: HE missed it.** The paper already proves this with nP ≠ O for n ≤ 12 plus Mazur's bound. That argument is complete.

8. **Desk-reject risk.** Only HE estimated it (about 50%). The other four referees' recommendations (major revision, no errors, fixable without new mathematics) are consistent with that estimate. All five independently recommended splitting off the arithmetic and/or the numerics, so the risk comes from structure, not correctness.

## 4. Verdict: NEEDS SUBSTANTIVE WORK

The mathematics is not the problem. No FATAL issue was raised, no result was found false, and the independent recomputations are extensive. But a wording-only revision pass would leave the main desk-reject drivers in place. Four items need real work before submission:

1. **Restructure for JGA (G7-1).** This is the single largest risk. Decide the split before any other revision, because it determines which of G7-9, G7-11 to G7-13 and G7-26 stay in this paper.
   - Main paper: §§2–5, a condensed §6.1–6.4, and Thm 5.16, at about 30–35 pp.
   - Supplement: §6.5 and §7.
   - Separate arithmetic note: §8 with Appendix A, carrying G7-9 and NT's literature.
2. **Remove the dependence on Uçar's thesis for all l (G7-3, new mathematics, modest).** Prove Lemma 2.5 from the elliptic term of the trace formula, and correct Remark 4.12. Three referees raised this independently.
3. **Recalibrate novelty and bibliography (G7-2, G7-6).**
   - Demote Section 4.
   - Fetch and read Hejhal/Iwaniec and McKean 1972, then decide whether Lemma 4.7 stays.
   - Re-anchor Theorem A and Thm 8.9.
   - Add the missing references, including the DGGW erratum.
4. **Close the open computation (G7-5, new computation).** Run the double-window recomputation of the four §7.1 spectra. That remains necessary even if §7 moves to a supplement, because the abstract cites the spectra. Otherwise drop the computed-spectra sentence from the abstract.

**Everything else is writing:**
- Bring the repository-held material into the paper (G7-4, G7-10, G7-11, G7-12, G7-13).
- Qualify the stability and shape claims (G7-7, G7-8).
- Settle repository ownership (G7-14).
- Make the minor and presentation fixes (G7-15 to G7-35).

After items 1–4, the result should be **READY FOR REVISION PASS**.

### Status summary of the FATAL and MAJOR items

| ID | Status |
|---|---|
| G7-1 | CONFIRMED |
| G7-2 | CONFIRMED |
| G7-3 | CONFIRMED |
| G7-4 | ANSWERED IN REPO, NOT PAPER; Thm 8.9 part ANSWERED IN PAPER |
| G7-5 | CONFIRMED |
| G7-6 | CONFIRMED (erratum: ANSWERED IN REPO, NOT PAPER) |
| G7-7 | CONFIRMED (½ exponent already in Remark 6.8; abstract and Thm 1.4 wording) |
| G7-8 | CONFIRMED |
| G7-9 | CONFIRMED |
| G7-10 | budget ANSWERED IN REPO, NOT PAPER; error bars CONFIRMED |
| G7-11 | ANSWERED IN REPO, NOT PAPER |
| G7-12 | ANSWERED IN REPO, NOT PAPER |
| G7-13 | protocol ANSWERED IN REPO, NOT PAPER; test design CONFIRMED |
| G7-14 | CONFIRMED |

FATAL: none.

## 5. Notes on the exercise

- **Isolation.** Each referee was given only the PDF path, with instructions not to read the repository or fetch the GitHub/Zenodo copies. Three reports state explicitly that the repository was not consulted, the editor's says it worked only from the PDF, and none of the five cites anything outside the PDF and published literature.
- **File writing.** Subagents in this session could not write outside their scratch folders. Each returned its report as text, and the coordinating session saved it verbatim, adding only a provenance footnote.
- **Network.** Network access from the referee sandboxes was patchy:
  - Crossref, zbMATH and Semantic Scholar failed.
  - arXiv mostly failed.
  - Only Strohmaier–Uski and Dryden–Strohmaier were fetched.
  - PARI, Sage and LMFDB were unavailable.

  As a result:
  - no referee verified the Uçar or DGGW citations verbatim, and SG and GA compensated by re-deriving the formulas;
  - the rank-0 and rank-2/3 claims were checked by referees' own 2-descents, not by PARI.

  A real referee with library access could add citation-level objections not found here.
- **Data.** Referees' scratch work (enumerations to S = 6000 and 2×10⁴, descents, an independent P2 FEM) is in the git-ignored `*/scratch/` folders.
