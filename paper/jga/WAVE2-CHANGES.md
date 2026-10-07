# WAVE2-CHANGES: Section 4, the restored appendices, bibliography, Table S1, neutral paths

Branch main, after 444f54b. Target journal: Annals of Global Analysis and Geometry (no page limit,
AGAG.md). Everything below was done in `paper/jga/`, `paper/arith/` and the Table S1 generator
`review/round1-fixes/d2_explicit_pairs.py`; `figures/captions.tex` needed no change.

## Page counts (build of this commit; `BUILD.md`)

| document | pages (before) | pages (after) | errors | undefined refs / cites | overfull boxes above 1 pt |
|---|---|---|---|---|---|
| manuscript.pdf | 33 | **48** | 0 | 0 / 0 | 0 (one of 0.8 pt, in a text line after Theorem 4.13) |
| supplement.pdf | 16 | **15** | 0 | 0 / 0 | 0 |
| paper/arith/note.pdf | 12 | **12** | 0 | 0 / 0 | 0 |

The manuscript gained 15 pages: Section 4 (12 pages), Appendices B and C (about 3), Remark 5.5 and
Problem 5; the supplement lost the two appendices and gained the pinching section.

## A1. Section 4, "From heat invariants to eigenvalues" (`sec:eigen`)

Filled from `theory/eigen/` in the order of STATUS.md: opening paragraph (new), 4.1 the diameter
(`diameter.tex`: Lemma 4.1 cone separation, Lemma 4.2 balls, Theorem 4.3 diameter bound with its
Table 1, Proposition 4.4 the family O(2,3,m)), 4.2 counting (`counting.tex`: Lemma 4.5, Propositions 4.6 and 4.7, Theorem 4.8), 4.3 remainders
(`remainder.tex`), 4.4 Theorem 4.13 (the "Theorem E" of `theory/eigen`; its integrality lemma 4.11,
gap lemma 4.12, the table of N and delta, Remark 4.14 that the bound on the orders cannot be
dropped), 4.5 the hypotheses (`necessity.tex`: Proposition 4.15 for unbounded orders, then the
systole bound stated as not proved), 4.6 Theorem 4.13 on computed spectra (`practice.md`).

| item | where |
|---|---|
| Theorem E with hypotheses (area <= A, systole >= eps, orders <= M, accuracy delta) and proof | Theorem 4.13 and Lemmas 4.11, 4.12; the diameter, counting and remainder results are Theorem 4.3, Theorem 4.8 and Propositions 4.9, 4.10 |
| cone-order bound necessary (O(2,3,m): high-order cone points behave like cusps) | Proposition 4.4, Proposition 4.15, Remark 4.14 |
| N and delta explicit but enormous; the content is effectivity | the opening paragraph, "How large are N and delta", Table 2 |
| practical counts (3-98 eigenvalues observed, a-priori 21-749, against N) | Section 4.6, Table 3 |
| systole necessity stated as open | end of 4.5 and Problem 5 (`prob:systole`, Section 9) |
| abstract clause; Section 1.1 forward reference | both filled; abstract is 186 words |
| diameter-free locality | **Remark 5.5** (`eig:loc`) after Theorem 5.4, with its constant (150.9 for the diameter bound against true diameters at most 7.8; C up to about 10^197) stated; the diameter-dependent Theorem 5.4 is unchanged |

Every AUDIT.md change is already in the frozen fragments and was checked in the assembled text:
S1 and S2 (the pinching "in particular" deleted; "What is not proved" rewritten), M1 (Remark 4.14
reads for A >= pi/3, eps <= sigma_0 with M = (floor(Lambda_N/delta)+1)^(N-1)+7), M2 (growth
eps^-3 log(1/eps)), M3 (Z^sharp in Theorem 4.13), M4 (half-open intervals in Proposition 4.15), M5
(Lambert argument and Klein model, in the supplement), M6, M7 (sharp enveloping constants in
Propositions 4.9, 4.10 and in Q(K)), M8.

Differences from the fragments, none of them in a statement:
* The proof of Propositions of the pinching family (`eig:N2`, the quadrilaterals Q_{k,b}) moved to a
  new Section S7 (Proposition S7.1) of the supplement ("Pinching a systole"); the paper keeps its one-paragraph
  consequence (lambda_1 -> 0, limsup lambda_j <= 1/4, and the intermediate-value remark that
  N = 2 is too small) and says that it does not bear on the systole hypothesis.
* "Theorem E" is typeset as the ordinary numbered Theorem 4.13 (the paper's lettered Theorems A-C
  are in Section 3; a Theorem D/E would have no neighbours).
* Theory-repository file names in the text (`diameter.py` etc.) were replaced by "checked
  numerically with the repository code".
* **Correction to STATUS.md.** STATUS.md says the observed and a-priori counts are "10^8-10^12 times
  fewer eigenvalues than the theorem requires". That holds for the triangles and for M = 12 but not
  for the family at M = 3 (N = 2.0 x 10^7 against 50 observed and 694 a-priori eigenvalues: factors
  4 x 10^5 and 3 x 10^4). Section 4.6 states the true ranges (observed 4 x 10^5 to 1.5 x 10^12,
  a-priori 3 x 10^4 to 2 x 10^11), computed from Table 3.
* For the member of systole 0.694 the a-priori count does not exist (the committed 815 eigenvalues
  are too few); Section 4.6 says so and that the a-priori range covers the seven members of
  systole at least 0.846.
* `practice.md` is not covered by the blind audit of `AUDIT.md` (which graded the statements of
  `STATEMENTS.md`); Section 4.6 is a report of computed counts, not a theorem, and the script
  `practice.py` is run in the suite (stage "eigen practice").

## A2. The two proofs restored to the paper

* **Appendix B, "The heat expansion from the trace formula"** (`app:derivation`): the admissibility
  lemma (Lemma B.1) and the proof of Proposition 2.7 (the heat expansion for every order), from the
  supplement section S9. The closed form of Phi_m (Lemma 2.6 with its proof) was already in
  Section 2.2. Proposition 2.7 and Theorem 2.3 now cite the appendix as their proof; Uçar's thesis
  is cited as agreement only (Remark 2.9 says "a check and not part of the proof").
* **Appendix C, "The rank of C_{27/2} by hand"** (`app:descent`): the 2-isogeny descent, from S8.
  In the proof of Theorem 6.8 (isolation) the descent is now the argument and PARI's `ellrank` the
  "independent confirmation".
* Both sections were removed from the supplement; its abstract and the pointers (`\sref{sec:derivation}`
  in Section 4's fragments, in Theorem 2.3 and in the isolation proof) were updated.

## A3. Bibliography (fetched records only, `tools/build_bib.py`)

* `jorgensen1976`: the Crossref record by content negotiation at https://doi.org/10.2307/2373814,
  fetched 2026-10-07 without any query parameter or address (SHA-256 in `SOURCES.md`). The record
  has only the first page (739), the title "On Discrete Groups of Mobius Transformations" and the
  author "Jorgensen" without diacritics, and that is what the bibliography prints.
* `jorgensenwiki`: the Wikipedia page "Jørgensen's inequality", fetched 2026-10-07, from which the
  statement of the inequality is quoted (the primary text is not retrievable headless; the bot
  walls are listed in `theory/eigen/sources/README.md`). The proof of Proposition 4.4 and the
  opening paragraph of Section 4 say so where the inequality is used.
* arXiv:1809.07309 (Gongopadhyay-Mishra-Tiwari) only corroborated the bibliographic data
  (it does not state the inequality), and is not cited. No other reference of `theory/eigen/` is
  new: every other result it uses is in the manuscript.

## A4. Table S1

`review/round1-fixes/d2_explicit_pairs.py`: (i) the caption now says that A' and B' are exchanged
when R(U_0) < R(V_0); (ii) `fmt_area` prints the exact exponent of a tiny deficit from the exact
fraction, so the L = 6 Prouhet row reads 1023 - 9.14 x 10^-864 instead of 1023 - 0.00 x 10^0.
The table was regenerated (`d2_explicit_pairs.py`; `--check` passes), the CSV output is
byte-identical, and the correction note that preceded the table in the supplement is removed.

## A5. Neutral paths

All repository-internal paths in the supplement and in the companion note
(`review/round1-fixes/...`, `theory/pte/...`, `theory/revision/...`, `numerics/data/...`,
`code/run_all.sh`, `theory/diophantine/`, `review/audit/diophantine/`, `paper/arith/checks/`) were
replaced by descriptions ("a script of the public repository", "its single run-all script") and the
repository URL https://github.com/Ali-M658/Arithmetic-verification, including the table caption in
the generator.

## A6. Figures

All eight figures of the paper stay (F1-F8 in Figures 1-8; F9 in the note); `figures/captions.tex`
is unchanged and every caption has at most two sentences. The new figure references are in
sentences that interpret them: the caption of the diameter table, the practice paragraph
("the eight members of the family (0;3,3,3,3) of Figure 6") and Remark 5.5. Section 4 has no new
figure.

## Not done / for the authors

* The three placeholders (author contributions, AI-use statement, Zenodo DOI) are unchanged.
* Section 4 is 12 pages (pp. 17-28); if the editor wants a shorter paper, Table 1 (the diameter bounds) and
  Section 4.6 are the first to move to the supplement.
