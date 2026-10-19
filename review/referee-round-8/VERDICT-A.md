# VERDICT-A (round 8): "How much of a hyperbolic orbifold does heat hear?" (AGAG)

Inputs: the five reports of Panel A (README.md). Length remarks are excluded. Every FATAL and MAJOR item is
checked against the repository and classified as CONFIRMED, ANSWERED IN PAPER, or ANSWERED IN REPOSITORY BUT
NOT PAPER; disputes are settled by computation or by the LaTeX source.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| A-a editor (orbifold isospectrality) | send to review; major revision | about 0.7 (recommendation), 0.75 (correctness) |
| A-b (cone zeta analysis) | major revision | high |
| A-c (quadrature and moment problems) | major revision | high |
| A-d (Teichmüller and triangle groups) | minor revision | high |
| A-e (lemma-by-lemma, citations, figures) | minor revision (close to major) | about 0.85 |

No FATAL item. Every reviewer recomputed its part and found every number and proof of a main result correct.

**Stop condition: not met** (two referees recommend major revision, and confirmed MAJOR items remain before the fixes).

## FATAL and MAJOR items

| id | item (reviewers) | status | resolution |
|---|---|---|---|
| A1 | "reading c_3 with a proved error needs t of order 10^-11" is an artefact of three sample times and of δ_thm (A-a M2a, A-b M2, A-c M1, A-e M1) | CONFIRMED by computation (`main/scratch/A/lemB3_nodes2.py`, `lemB3_window2.py`): with N = 8 times t, …, t/128 and the row bounds, δ_thm holds for t ≤ 3.6e-3 (η ≤ 5.0e-13 at t/2), δ_cert for t ≤ 1.5e-2 (η ≤ 1.3e-8 at t/2); with all times in [a, T], N ≤ 16, nothing meets δ_cert for a ≥ 1e-3 and nothing meets δ_thm for a ≥ 3e-4 | Lemma B.4 (was B.3) now takes N ≥ n times with row bounds δ_{1,j}; Remark B.5 gives the three-time numbers, the N = 8 numbers for δ_thm and δ_cert, and the scan; the abstract, introduction and Corollary 6.5 now say that the proved recoveries use times shorter than computed spectra resolve (t ≳ 1e-3). Asserted in `check_heat_supporting.py` §9(a) |
| A2 | Proposition 2.13 has only an outline proof (A-a M3, A-b M1, A-e M2) | CONFIRMED (the paper itself listed three steps not carried out) | Split: Conjecture 2.13 (structure (i) and top coefficient (ii), with the derivation in outline); Proposition 2.14 (linear part, former (iii)) with a complete proof: Donnelly invariance, Ricci identities, the one-dimensional SO(2)-invariants of Sym^{2l−2}, Duhamel. Introduction, summary and Problem 6 updated |
| A3 | The "if" direction of Proposition 2.16(ii) (was 2.15) is sketched at its key computation (A-e M3) | CONFIRMED | The Fourier/Duhamel computation is written out (trace formula for f a(D) f b(D), completed square, Gaussian moment, the s-integrals), with ω_{l+1} as an explicit sum; analyticity of G_l and the vanishing first derivative stated; scaling exact, so no uniformity in ε is needed. Asserted in `check_heat_supporting.py` §9(c) |
| A4 | δ_thm is called explicit but Table S4 uses the exact matrix norm; the closed-form bound is lossy (A-b M3) | ANSWERED IN PAPER in part (Theorem 6.2 already says "closed formulas except for one matrix norm, cond, which Theorem C.2(a) bounds explicitly"); the labelling of Table S4 CONFIRMED | Sentence after Theorem C.4: Table S4 evaluates δ_thm with the exact cond, the closed form is smaller by large factors, and the certificate used is Proposition S3.1. Moving S3.1 into the paper is not needed: it is proved in the supplement, which is part of the submission |
| A5 | Whether three invariants suffice for a triangle orbifold against all of Sig; the abstract's comparison class (A-d M1; A-a m3) | CONFIRMED | New Proposition 5.2 (proved): a rival sharing c_1..c_3 is (0;a,b,c,d) with a ∈ {2,3} and {1,p,q,r}, {a,b,c,d} of equal R, P_1, P_3 (genus 1 and five points excluded); search: none with {2,2,c,d}, d ≤ 1000, or with b ≥ 3, d ≤ 20000; new Problem 5; abstract says "among triangle orbifolds" and that against all orbifolds the question reduces to one Diophantine system. Asserted in `check_heat_supporting.py` §9(e) |
| A6 | Significance: the main counts are power-sum combinatorics; make the geometric case; retitle (A-a M1) | ANSWERED IN PAPER in substance (the introduction states that the paper counts coefficients and what is elementary); strengthened | A sentence on the geometric meaning of a count and on constant curvature (introduction, p. 3); the variable-curvature caveat is now in the abstract. The title is the authors' and is kept |
| A7 | "At any fixed t > 0 the heat trace determines the whole spectrum" (A-a M2b) | CONFIRMED (a single value does not) | Abstract and introduction: "the heat trace on any interval of times" |
| A8 | Constant-curvature caveat buried (A-a M2c) | CONFIRMED (presentation) | Abstract: "Constant curvature is essential: with variable curvature this pair carries metrics, flat near the cone points, whose heat invariants agree to all orders" |
| A9 | Relevance of Section 6, Appendix C and the numerics to the thesis (A-a M4) | ANSWERED IN PAPER (the stability theorem and the locality section are the quantitative side of what diffusion can detect; the numerics are labelled illustrations); not a request to cut | One sentence in the introduction on what the stability theorem says about the use of the counts |
| A10 | Classical attributions on the moment side: Chebyshev systems, divided differences, Descartes for lacunary polynomials (A-c M2) | CONFIRMED | Citations of Karlin–Studden (zbMATH 0153.38902), de Boor (Surveys in Approximation Theory 1), Pólya–Szegő vol. II, Part V (Crossref chapter "The Location of Zeros"); "what is new" paragraphs rewritten accordingly |
| A11 | The growth of b_l(m) is heuristic although provable; Section 4's novelty (A-c M3) | CONFIRMED | New Lemma B.3 (growth of the cone coefficients), proved by the principal parts of Φ_m at ±π/m and a Cauchy estimate: |b_l(m)| ~ (2π sin(π/m))^{-1}(πl)^{-1/2} l!(m/π)^{2l}; Section 4 and the introduction cite it; optimal truncation stays labelled heuristic. Asserted in `check_heat_supporting.py` §9(b) |

## MINOR items (deduplicated)

| id | item | resolution |
|---|---|---|
| a1 | DGGW erratum (A-a m1, A-e m13) | cited where (5.7) is used; the erratum text could not be fetched (publisher block), and the formulas of DGGW used here are rederived in Section 2 from the trace formula |
| a2 | least-area claim only among triangle orbifolds (A-a m2) | Theorem 5.8 extended and proved over all of Sig (only (0;2,2,2,3) and (0;2,2,2,4) besides triangles have area ≤ π/2; AM–HM); asserted §9(d) |
| a3 | "first differ at the third order in t" (A-a m4) | fixed |
| a4 | family non-isometric only numerically (A-a m5, A-d m6) | already labelled numerical in Section 4; now also in the supplement |
| a5 | Steinig cited unread (A-a m6); "before Lemma 3.2" and Laurens' lemma (A-e m4) | attribution through Laurens, "after his Lemma 3.2", checked in the fetched text; the sign-change argument is in the proofs of his Lemma 3.2 and Corollary 3.3 |
| a6 | Figure 3 (F4) caption, open region (A-a m7) | caption corrected |
| a7 | Figure 1 radial profiles (A-a m8) | not done: every figure stays; the text gives the radial values |
| a8 | Chen-routed attributions (A-a m9) | kept: the original sources (Letac, Gloden) were not accessible; Chen is cited as the source of record |
| a9 | Remark B.4 time indexing (A-a m10, A-e P5) | times now τ, τ/2, τ/4 |
| a10 | non-orientable orbifolds (A-a m11) | one sentence, with DGGW (5.8) |
| a11 | note's status as a preprint (A-a m12) | the "#A1 INTEGERS 26 (2026)" header is the Integers template default, filled by the editors on acceptance (paper/arith/integers/README.md); the note is cited as a preprint |
| a12 | Lemma C.1 columns; sep = +∞ (A-b m1, m2) | fixed |
| a13 | K > 0 hand-wave (A-b m4, A-e m12) | Uçar's theorem cited for every constant curvature |
| a14 | Proposition 2.16(iii) says more plainly (A-b m6) | sentence on flat cone points contributing only to c_2 |
| a15 | row-wise bounds; "about" (A-b m7, m8) | done in Lemma B.4 and Remark B.5 |
| a16 | Corollary 6.5 hypotheses (A-b m10) | already "a sphere with n cone points" |
| a17 | well-ordering of areas (A-c m1) | the bound n + 4g ≤ A/π + 4 made explicit |
| a18 | soundness of the modular rejection (A-c m3) | Gauss's-lemma argument written in the supplement |
| a19 | Cor. 4.1(b) source; Prop. 4.2(b) range (A-c m8, m9) | Thurston Ch. 13 cited; the range t ≤ L'^2/(2(1+L')) stated |
| a20 | forward reference in Lemma 5.3(ii) (A-d m2, A-e m10) | stated that (a), (b) of the proof of Theorem 5.4 do not use the lemma |
| a21 | "fail earlier" (A-d m8) | "at a smaller order sum, though not at a smaller area", with the area 4π/5 |
| a22 | Doyle–Rossetti "independently" (A-e m3); DS Def. 3.1 (A-e m2); Fursaev (3.26) (A-e m7); DGGW Ex. 5.6 and the t^0 coefficient (A-e m13); Uçar Cor. 4.21(iv) (A-e m14); Garbin–Jorgenson half-line (A-e m6) | all corrected at statement level against the fetched texts |
| a23 | Schueth equation numbers of the published version (A-e m5) | (6), (7), (13), (15), (16) → (2.3), (2.4), (3.2), (3.4), (3.5), checked in the Ann. Inst. Fourier text |
| a24 | flat approximation of the image distance (A-e m1) | the curvature −1 relation sinh(d/2) = sinh r sin(πj/m) added (checked numerically) |
| a25 | Theorem C.2(b) Neumann step (A-e m8) | written out |
| a26 | Theorem 3.11(iv) range of the orders (A-e m9) | stated |
| a27 | μ_0 = 12 explained (A-e m17) | in Remark B.5 |
| a28 | supplement completeness wording and family ranges (B-a overlap remarks) | "a missing eigenvalue paired with a spurious one would not be seen; completeness supported, not proved"; the two-window recomputation and the companion's 0.8 range stated |
| a29 | items not done: A-c m2, m4–m7, m10; A-d m1, m3–m5, m7, m9; A-e m15, m16; A-b m3, m5, m9, m11; presentation renamings (A-a P2, A-c P1, A-e P2) and restructurings | judged not worthwhile this round or not verifiable (A-e m15, m16: sources not reachable); no correctness issue |

## Mathematical changes (each with its check)

1. Lemma B.4 with N ≥ n times and row bounds (proof unchanged in structure); Remark B.5 numbers — `check_heat_supporting.py` §9(a).
2. Lemma B.3 (growth of b_l(m)) — proof in the paper; `check_heat_supporting.py` §9(b).
3. Conjecture 2.13 / Proposition 2.14 split; complete proof of Proposition 2.14.
4. Proposition 2.16(ii): the ω_n computation written out — `check_heat_supporting.py` §9(c) (Gaussian moment by sympy; ω_{l+1} for l ≤ 10).
5. Proposition 5.2 (rivals) and its search; Problem 5 — §9(e).
6. Theorem 5.8: least area over all of Sig — §9(d).
7. Theorem C.2(b) Neumann step; Lemma C.1 column indexing; Theorem C.3 convention.

Blind check: `blind-check-A/REPORT.md`.
