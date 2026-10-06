# Self-review: simulated number-theory referee

A separate subagent, acting as a number-theory referee, read only the built PDF
(`note.pdf`, 12 pp., SHA-256 `19c5b9aa…305db3938`, first build). It ran its own code (an exhaustive
C enumerator to S = 6000, sympy, and PARI 2.17.2 through cypari2) and read the cited literature
online. Its report came back as text; the issues below are its items, numbered as in the report (M = major,
m = minor, p = presentation).

**Verdict:** minor revision for a venue that takes short computational-analytic notes, major
revision at a research-level number-theory journal (because of M3). No mathematical error was found.
Every table entry, the constants c_iso and 3/(128π⁴), the −0.479X secondary term, all ranks, and
the enumeration to 6000 were reproduced independently.

Revised PDF: 12 pp., SHA-256 `e1b71a11…659b417b2`. It builds with no errors, no undefined
references or citations, no overfull or underfull boxes, and no BibTeX warnings.

## Resolutions

| # | issue | resolution |
|---|---|---|
| M1 | Placeholders (Zenodo DOI, author contributions, AI use); internal repository paths | **Kept by design.** The brief requires the JGA declarations with the same placeholders. The repository paths stay, because they are how a reader reruns the checks. Open for the authors. |
| M2 | Table 1 rank 0 rests on the companion paper "in preparation" | **Fixed.** The footnote is removed. Rank 0 for C_{27/2} is now certified like every other row (ellrank r₁ = r₂ = 0, theory/diophantine/data/ranks.txt), and the caption says so. The isolation of the minimal pair is still neither stated nor proved here (brief). |
| M3 | Results modest; X^{3+ε} upper bound far from the data; asks for (a) a better upper bound, (b) an asymptotic for the dual family, or (c) N_cl ≫ X(log X)² | **Not resolved: needs new mathematics.** The note already presents itself as a short note and claims no novelty for Thm 5.1. Recorded as open issue O1. |
| M4 | Conjecture 1.4 weakly supported; the referee suggests the Shioda–Tate argument (generic Mordell–Weil rank 0, so the only graph-type surfaces are the 12 translates ±P+T), a surface search, or relabelling as a question | **Partly.** The conjecture stays (brief: "the revised conjecture"), and §6.4 already states that the data cannot exclude any exponent in (1, 1.58). The Shioda–Tate argument is **not added**: it rests on Shioda 1990, whose text was never retrieved (theory/diophantine/novelty.md, RECOMMENDATION §6). Open issue O2. |
| m1 | Cor. 3.2 calls the dual set a "pair" without proving R < 1 | **Fixed.** It is now a "primitive set", which need not be admissible; its copies with k ≥ 4 are (Lemma 4.1). |
| m2 | Same point for D(x) in Lemma 4.3 / Thm 4.4 | **Fixed.** Lemma 4.1 is stated for all primitive sets D, admissible or not, and Lemma 4.3 and Thm 4.4 count those. |
| m3 | 40,305 excludes (1,1,1) | **Fixed** ("other than (1,1,1)"). |
| m4 | Remark 3.4 "double pole" wording is wrong | **Fixed.** The mismatched case is written out: (a+b)² = ab is impossible. |
| m5 | Prop. 6.1 remark: "at most two partners" should be "at most one" | **Fixed**, with the reason. |
| m6 | Redundant "one isosceles pair per class" sentence | **Removed.** Distinct (Λ, S) suffice. |
| m7 | "r₂ uses no class-group computation" is not documented | **Replaced** by what PARI documents (r₂ unconditional from the 2-Selmer group) plus the independent descents. The finer source-code claim stays in review/audit/diophantine/REVIEW.md (P5, item 3). |
| m8 | The line search is unclear | **Fixed.** §6.4 now defines the lines, the Möbius pairing, the 189 lines and what counts as a hit. |
| m9 | Bootstrap errors ignore model uncertainty | **Fixed.** Method spread (≤ 0.1) and window dependence (4.43, 4.63, 4.37) are added from data/exponent_fits.txt. A 2400–6000 window is **not** given: per-sum class lists are committed only to 4800 for this purpose (open issue O3). |
| m10 | Abstract and Thm 1.1: the first N bound is superseded | **Fixed in the abstract** (X(log X)² for N, X log X for N_cl). Thm 1.1 keeps the chain N ≥ N_cl ≥ …, which is the statement for classes. |
| m11 | Cite arXiv:2408.13867 | **Added** (Youmbai–Shamsi Zargar–Voznyy, fetched arXiv record, first page read). |
| p1 | F9 caption: the plotted thin curve grows like c_iso log S and counts all admissible multiples | **Fixed.** |
| p2 | Acknowledgement used only for the colour maps | **Kept.** It matches the JGA paper, and figures/SPEC.md requires the Crameri citations. |
| p3 | Γ₁(6) parenthetical | **Declined.** The brief asks for Beauville's notation, and the Γ₁(6) identification is unverified in the repository (RECOMMENDATION §6). |
| p4 | BGN title ends "?," | That is how amsplain punctuates a title ending in "?". Left as is. |
| p5 | Orbit paragraph should assume infinite order | Already stated ("for a point P of infinite order"). |
| — | Referee could not check: DGGW (5.7), Mazur Cor. (5.2), Schoen Prop. 7.1, the BGN quotations, the PARI internals | Covered in the repository: CITATIONS.md (DGGW, Mazur); fetched BGN text (quotes verbatim, re-read this session); TD variety.md §4 (Schoen, read at the time; the literature pass could not reopen it); AD REVIEW.md P5 (PARI). |

## Open issues

- **O1** (M3) No upper bound better than X^{3+ε}, no asymptotic for the dual family, and N_cl only ≫ X log X.
- **O2** (M4) Shioda–Tate framing: needs Shioda 1990 (or another source for the Mordell–Weil group of this rational elliptic surface) to be fetched and read. The low-degree surface search has not been run.
- **O3** Exponent fits on a window reaching 6000 would need per-sum pair counts for 4801–6000 (the class lists are produced by `checks/check_note.py --enum` but are not stored).
- **O4** Schoen Prop. 7.1: the literature pass could not reopen the body (paywall). The sentence rests on theory/diophantine/variety.md §4.
- **O5** Placeholders: Zenodo DOI, author contributions, AI-use statement. Target journal not chosen.
