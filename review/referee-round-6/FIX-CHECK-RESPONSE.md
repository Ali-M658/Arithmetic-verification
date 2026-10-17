# Response to FIX-CHECK.md and FIX-CHECK-A2.md (round 6)

`FIX-CHECK.md` was run with stale Paper A PDFs (6 October); its Paper A section and items X1-X3 are
superseded by `FIX-CHECK-A2.md` (current build, 55 + 16 pages). Its Paper B and note sections stand.

## Paper A (FIX-CHECK-A2)

| item | action |
|---|---|
| X1 (A says B restates the shared results "without proof") | A §1: "restates them ... and reproves them in its Appendix A by the arguments of this paper" |
| X2 (note's Theorem C overstated) | "for every k infinitely many classes have at least k members" |
| X3 (Theorem 5.8 proved in both, undeclared) | the note now says "this is also [A, Theorem 5.8], proved there by a 2-isogeny descent by hand"; VERDICT-A's reason "the note cites it" was wrong and is corrected here |
| N4 / a10 (values near t = 0.03) | the data stop at t = 0.0293, the last sampled time below 0.03 (`numerics/data/heat_trace_difference.csv`); A §4 and S4 (two places) now state that time; at t = 0.0293 the deviation is 4.0e-13 (the closed-geodesic term there), at t = 0.03 the term is 7.8e-13 |
| N5 | "beyond t ≈ 0.1 the closed geodesics become visible, and near t ≈ 0.34 they reverse the sign of D" |
| N6 | Remark 4.3 moved after the paragraph "The constant of (a) is not ..." |
| N7 / a19 / a32 | proof of Corollary 3.5: with n, g bounded, Σ1/m_i is fixed and m_k ≤ (n−k+1)/r_k, so only finitely many signatures have a given area; the well-ordering of the areas is justified in one line. The checker's further wording "the areas below any bound form a finite set" was NOT adopted: it is false (the areas of O(2,3,m) accumulate at π/3) |
| a11 / N10 | "conservative" replaced by "the second estimate" (S, two places); B likewise |
| a16 / N8 | Dowker initials unified; editor "{de Gier}, Jan" braced. The page range "L137--L140" is in the record; its printing without the letter is the class's bibliography style (not changed) |
| a64 | Example 3.6: "the change of genus costs nothing beyond its bound: 2L + 2\|g − g′\| = 6" |
| A6 (Lemma 3.7 uncited) | not changed: the lemma is proved in full in the paper; the suggested locator (Pólya–Szegő, Part V, problem number) could not be checked against the book, and no reference is cited unread |
| a14, a21, a51 | open: carried to round 7 (per-piece attribution of the PTE recipes; "schematic" in the Fig. 4 caption; the search for K_mult ≤ 3) |
| also | `paper/jga/tools/make_tables.py` carried stale captions (it reverted the round-6 \pref fixes and "a real root, or a non-real complex pair" when run); the generator now writes the corrected captions and `--check` passes |

## Paper B (FIX-CHECK.md)

| item | action |
|---|---|
| B-N1 | Remark 6.4: the geodesic-side g is supported in (−ε, ε), i.e. h = ĝ has Fourier transform supported below the systole |
| B-N2 | the count constant is C_* (Lemma 4.5, Theorem 6.2, Tables 3, 4, 6, Section 7); the Section 8 integer is J; K remains only the truncation index of Proposition 2.3 and Appendix A |
| B-N3, B-N4 | counts stated as values of N (the test with N uses the eigenvalues up to λ̃_N); the 461–847 range is marked as (C1) |
| B-N5, B-N6 | "conservative" removed; "about ten to twenty times the floor 10⁻¹⁴λ_j" (Table 5: ratios 10–17) |
| B-N7, b4 | "computed diameters" in the Table 2 caption |
| B-N8, b5 | "their diameters at least log(m/2π) (Proposition 8.2)" |
| B4 residual | "applies the same idea to test a signature" |
| b37 | "(C1) is the weaker criterion; it uses only the inequality \|Σ_{j<N} e^{−λ̃_j t} − G_{σ(O)}(t)\| ≤ E_N(t) of Theorem 7.1" |
| b14, b15, b23 | Remark 6.3 (Sharper constants): worst-case δ_k and individual terms; max instead of sum (at most a factor 2); enumerated short geodesics in Theorem 7.1 |
| B8 | Theorem 7.1 keeps the plain error sum t Σ ε_j: it is a valid bound and the counts of Table 6 are computed with it; the sharper factor e^{−t min} is stated after the proof of Theorem 6.2 |
| b1 (Jørgensen order-free bound) | not added: the statement could not be checked against the source this round |
| b41 (N_obs column) | not added to Table 6; N_obs is in Figure E3 and the text (Table 6 is at its width) |
| B6 gap (margin for the family) | not computed this round; recorded for round 7 |
| B-N9 (Beardon vol. 91; volume styles) | carried to round 7 (needs the fetched record) |

## Note (FIX-CHECK.md)

| item | action |
|---|---|
| N-N1 | "and, under the hypotheses of [Thm 2.8], Z/12 does not occur" |
| N-N2 | "and the count is 0.608X at X = 4800" |
| N-N3 | "One command reruns every check; the enumerations from scratch are rerun only on request" (both versions) |
| conventions check | the hypothesis of Sadek–El-Sissi is written with u_1 > u_2 > u_3 (d_j is reserved by CONVENTIONS.md) |

## Suite

The full `code/run_all.sh --quick` run (2 h 09 min) gave 75 PASS, 4 FAIL, 9 SKIP. The failures and their fixes:
`theory conventions-check` (d_j, above; `release_config.py` already contained `$d_3$` at HEAD, now reworded);
`admin DATA-MANIFEST is current` (regenerated); `eigen practice_double_window` (round-6 regression: the
script still passed the diameter where `practice.logH`/`TailBound` now take the log of the count constant;
fixed, and the rerun reproduces the committed `practice_missing.csv` and `practice_double_window.csv`
byte for byte, 19 of 24); `round1 paper tables current` (stale generator captions, above). The failed and
affected stages were rerun after the fixes (`main/scratch/run_all_targeted.log`).
