# Source Hygiene Report — `paper/main.tex`

Audited 2026-08-09. Source: `paper/main.tex`, 723 lines, MD5 `adfa0001c73e3721f3ccdcc6dcda7e12`.
**Nothing in this report has been fixed.** It is an inventory only, per instruction.

---

## 1. Document class and package inventory

**Class:** `\documentclass[12pt, letterpaper]{article}` (line 1).

A plain `article` class, not a journal class. No `amsart`, no publisher template. If the target journal supplies a class (`amsart`, `elsarticle`, Springer `svjour3`), the preamble will need reworking — the geometry, `\doublespacing`, and hand-rolled theorem environments below will all be overridden or conflict.

**Packages — 16 declared, in load order:**

| # | Line | Package | Used? | Evidence |
|---|---|---|---|---|
| 1 | 3 | `amsmath` | **yes** | 175 hits (`\begin{equation}`, `\tfrac`, `\operatorname`) |
| 2 | 3 | `amssymb` | **yes** | `\mathbb` etc. |
| 3 | 3 | `amsthm` | **yes** | 27 hits (`\newtheorem`, `\begin{proof}`) |
| 4 | 3 | `mathrsfs` | **NO** | zero `\mathscr` in document |
| 5 | 4 | `geometry` | **yes** | `\geometry{...}` line 22 |
| 6 | 5 | `tikz` | **yes** | one `tikzpicture`, Figure 1 |
| 7 | 6 | `titlesec` | **NO** | zero `\titleformat` / `\titlespacing` |
| 8 | 7 | `enumitem` | **yes** | `\begin{enumerate}[label=(\roman*)]` line 218 |
| 9 | 8 | `hyperref` | **yes** | loaded; no `\href`/`\url` but provides `\ref` linking |
| 10 | 9 | `setspace` | **yes** | `\doublespacing` line 29 |
| 11 | 10 | `xcolor` | **NO** | zero `\textcolor` / `\definecolor`; `\filldraw[red]` in Fig. 1 works from TikZ's own colours |
| 12 | 11 | `mathtools` | **NO** | zero `\coloneqq`, `\DeclarePairedDelimiter`, `\mathclap`, `\prescript` |
| 13 | 12 | `tikz-cd` | **NO** | zero `tikzcd` environments |
| 14 | 13 | `booktabs` | **yes** | 17 hits (`\toprule`/`\midrule`/`\bottomrule`) |
| 15 | 14 | `longtable` | **yes** | Table 1 (`tab:enum`) |
| 16 | 15 | `caption` | **NO** | zero `\captionsetup` |

**Six packages are loaded but unused:** `mathrsfs`, `titlesec`, `xcolor`, `mathtools`, `tikz-cd`, `caption`.

Two of these — `titlesec` and `tikz-cd` — were **not installed on this machine and blocked compilation entirely** until installed during this audit. That is the worst case for an unused dependency: it adds a hard build requirement that buys nothing. Any co-author or editor with a basic TeX Live install will hit the same wall.

**Other preamble notes:**

- Lines 17–20: `\hyphenpenalty=10000`, `\exhyphenpenalty=10000`, `\pretolerance=10000`, `\sloppy`. This disables hyphenation across the whole document. It is the direct cause of the 24 underfull `\hbox` warnings (§6) and produces visibly loose inter-word spacing in a double-spaced 12pt layout. Most journals will not want this.
- Lines 31–46: theorem environments hand-declared. Note `\newtheorem{mainthm}{Theorem}` with `\renewcommand{\themainthm}{\Alph{mainthm}}` — this creates a **second, independent** Theorem counter alongside `\newtheorem{theorem}{Theorem}[section]`. The document therefore contains both "Theorem A/B/C" and "Theorem 3.4", plus `\newtheorem*{theorem*}{Theorem}`. Three distinct things all print as "Theorem". Legal, but a copy-editor will query it.
- Line 48: `\title{\vspace{-2cm}...}` — a negative vertical space hard-coded into the title. Fragile under any class change.
- No `\usepackage{amsfonts}`, no `\usepackage[T1]{fontenc}`, no `inputenc`. The file is UTF-8 and contains no non-ASCII characters (verified), so this compiles, but `fontenc` is normally expected.

---

## 2. Corrupted em-dash pattern

The manuscript contains **zero** real em-dashes (`—`, U+2014). Every em-dash has been replaced by a comma-plus-spacing artefact.

**Total: 53 occurrences across 25 distinct lines.**

- **48 inline** occurrences of the pattern ` ,  ` (space, comma, two spaces) used as a parenthetical/appositive dash.
- **5 trailing** occurrences of ` , ` at end-of-line, which are the *closing* halves of dash pairs inside bibliography section comments.

No other corruption variants were found: 0 instances of `,,`, 0 instances of a single-spaced ` , ` in body text, and the 70 occurrences of `--` are all legitimate LaTeX en-dashes in page ranges and hyphenated author names (Dryden--Gordon--Greenwald--Webb, Cauchy--Schwarz, etc.) — **do not** mass-replace those.

### Line-by-line inventory (inline ` ,  `)

| Line | Count | Context |
|---|---|---|
| 58 | **5** | Abstract — the heaviest single line |
| 75 | 1 | §1 opening paragraph |
| 101 | 1 | §1, "the question we answer is *geometric*" |
| 103 | 1 | §1, definition of *collision* |
| 114 | 1 | Theorem C statement |
| 118 | 2 | Corollary D statement |
| 121 | 2 | §1, hierarchy paragraph |
| 134 | 1 | §1.1 Related work, Uçar sentence |
| 153 | **3** | §1.4(b) Our contribution |
| 155 | 2 | §1.4(c) Load-bearing only |
| 160 | **4** | §1.5 Scope and limitations |
| 236 | 2 | §2.4 footnote on `eq:b1` |
| 275 | 2 | §3 opening |
| 348 | 2 | §3.2, after separation proof |
| 360 | 2 | §3.3, scope caveat |
| 373 | 2 | §4.1, proof of Theorem C |
| 395 | 2 | §4.2 `remark*` |
| 479 | 2 | §5.3, after Conjecture |
| 489 | 2 | §5.4 An extremal companion |
| 494 | **4** | `rem:ncone` |
| 632 | 1 | bibliography section comment |
| 654 | 1 | bibliography section comment |
| 661 | 1 | bibliography section comment |
| 686 | 1 | bibliography section comment |
| 702 | 1 | bibliography section comment |
| **total** | **48** | |

### Trailing ` , ` (closing dash), all in bibliography comments

| Line | Full line |
|---|---|
| 632 | `% ,  reading geometry from finitely many heat invariants , ` |
| 654 | `% ,  isospectral constructions , ` |
| 661 | `% ,  orbifold heat invariants and isospectral orbifolds , ` |
| 686 | `% ,  cone and corner contributions to heat coefficients , ` |
| 702 | `% ,  hyperbolic orbisurfaces and triangle groups , ` |

These five are inside `%` comments and do not affect output, but they confirm the corruption was applied mechanically across the whole file, comments included — which is useful evidence that a single global substitution caused it.

**Caution for the eventual fix:** the replacement is *not* uniformly `---`. Some sites are genuine appositive dashes (line 58: "pillows ,  spheres carrying three cone points"); at least one reads as a true comma in a list. Each of the 53 needs an individual decision, and lines 632/654/661/686/702 are paired open/close dashes that must be fixed together.

---

## 3. Missing author / affiliation / ORCID metadata

| Field | Status |
|---|---|
| `\title` | **present** (line 48) |
| `\author` | **ABSENT** |
| `\date` | present but **empty** — `\date{}` (line 50) |
| Affiliation / `\institute` / `\address` | **ABSENT** |
| ORCID | **ABSENT** |
| Email / corresponding author | **ABSENT** |
| `\thanks` (funding footnote) | **ABSENT** |
| Keywords | present (line 62) |
| 2020 MSC | present (line 65) — `58J53, 58J50, 35K08, 11D45, 11D68` |

The compiler confirms this: `LaTeX Warning: No \author given.`

The paper is therefore **fully anonymous as it stands**. Note the tension with line 618: *"The author declares no competing interests"* — singular "author", in a paper with no author named. Every journal requires author name, affiliation, and (increasingly) ORCID at submission; several require a designated corresponding author with email.

`\maketitle` is followed by `\thispagestyle{empty}` (line 55), so there is no page number on page 1.

---

## 4. Undefined references

**None.** Checked exhaustively:

| Check | Result |
|---|---|
| `\label` definitions | 42 |
| `\ref` / `\eqref` calls | 150 |
| **Undefined references** | **0** |
| `\bibitem` keys | 28 |
| `\cite` keys invoked | 69 |
| **Undefined citations** | **0** |
| Duplicate `\bibitem` keys | 0 |
| Uncited bibliography entries | 0 |

Confirmed at the LaTeX level too: a full `latexmk -pdf` run to a stable state produces **no** `Reference ... undefined`, `Citation ... undefined`, or `multiply-defined` warnings.

**Eight labels are defined but never referenced.** Harmless, but they are dead weight and a couple suggest a cross-reference was intended and dropped:

`rem:bugfix` · `sec:cone` · `sec:core` · `sec:heatexp` · `sec:intro` · `sec:novelty` · `sec:related` · `sec:scope`

`rem:bugfix` is the one worth a second look — it labels the Remark at line 229 that warns against a mis-normalization, and nothing in the text points to it.

---

## 5. Bibliography entries lacking DOIs

The bibliography is a hand-written `thebibliography` environment (lines 630–721). **There is no `.bib` file** anywhere in the project, and `refs/` is empty. That is itself a submission risk: most publishers want BibTeX source, and hand-maintained `\bibitem` lists cannot be validated against Crossref automatically.

**28 of 28 entries lack a DOI — 100%.**

Of those, 11 carry an arXiv identifier, which partially substitutes. **17 entries have neither a DOI nor an arXiv ID**, and these are the ones a production editor will bounce back:

| Key | Reference | arXiv? |
|---|---|---|
| `kac1966` | Kac, *Can one hear the shape of a drum?*, Amer. Math. Monthly 73 (1966) | no |
| `mckeansinger1967` | McKean–Singer, J. Differential Geom. 1 (1967) 43–69 | no |
| `datchevhezari2013` | Datchev–Hezari, MSRI Publ. 60 (2013) 455–485 | no |
| `griesermaronna2013` | Grieser–Maronna, Notices AMS 60 (2013) 1440–1447 | no |
| `lurowlett2015` | Lu–Rowlett, Amer. Math. Monthly 122 (2015) 815–835 | no |
| `hezarizelditch2022` | Hezari–Zelditch, Ann. of Math. 196 (2022) 1083–1134 | no |
| `sunada1985` | Sunada, Ann. of Math. 121 (1985) 169–186 | no |
| `gww1992` | Gordon–Webb–Wolpert, Bull. AMS 27 (1992) 134–138 | no |
| `donnelly1976` | Donnelly, Math. Ann. 224 (1976) 161–170 | no |
| `dggw2008` | Dryden–Gordon–Greenwald–Webb, Michigan Math. J. 56 (2008) 205–238 | no |
| `ssw2006` | Shams–Stanhope–Webb, Arch. Math. 87 (2006) 375–384 | no |
| `rsw2008` | Rossetti–Schueth–Weilandt, Ann. Global Anal. Geom. 34 (2008) 351–366 | no |
| `doylerossetti2008` | Doyle–Rossetti, New York J. Math. 14 (2008) 193–204 | no |
| `drydenstrohmaier2009` | Dryden–Strohmaier, Canad. Math. Bull. 52 (2009) 66–71 | no |
| `harmer2008` | Harmer, J. Aust. Math. Soc. 84 (2008) 217–227 | no |
| `scott1983` | Scott, Bull. London Math. Soc. 15 (1983) 401–487 | no |
| `buser1992` | Buser, *Geometry and Spectra of Compact Riemann Surfaces*, Birkhäuser 1992 | no (book) |

`dggw2008` is the most important omission: it is the analytic foundation of the entire paper, cited 8 times, and carries no persistent identifier.

Entries carrying an arXiv ID but still no DOI (11): `gomezserrano2020`, `proctorstanhope2009`, `barihunsicker2017`, `richardsonstanhope2019`, `gittinsetal2024`, `schueth2019`, `schueth2025`, `suleymanova2017`, `nrs2024`, `looisher2025`, `ucar2017`.

Several of these are labelled "preprint" but have since appeared in journals and should be updated to the published version at proof stage — `schueth2019` already gives both (Ann. Inst. Fourier 69 (2019) 2827–2855 *and* arXiv:1812.06119), so the intent is clearly to cite published versions where known.

### Additional bibliography inconsistencies noted in passing

- **`gittinsetal2024`** — the citation key says `2024`, the entry text says `(2023)`, and the arXiv ID `2311.00337` is a November 2023 submission. Key, printed year, and identifier disagree.
- **`proctorstanhope2009`** — keyed and printed as 2009, but arXiv:0811.0797 is a 2008 submission. Consistent with a 2009 publication date; worth confirming.
- **`nrs2024`** — journal given as "Ann. Math. Québec (2024)" with no volume, issue, or page range.
- **`schueth2025`** (arXiv:2511.22255) and **`looisher2025`** (arXiv:2512.04422) are recent preprints; check for publication before submission.

---

## 6. Compilation status

Compiles cleanly **once the two unused-but-missing packages are installed**.

| | |
|---|---|
| Engine | `pdflatex` via `latexmk -pdf` |
| Result | success, exit 0 |
| Output | `paper/build/main.pdf` |
| Pages | **44** |
| Undefined refs/cites | 0 |
| Overfull `\hbox` | **2** |
| Underfull `\hbox` | **24** |
| Other warnings | `No \author given` · `!h float specifier changed to !ht` (×2) |

**Overfull boxes:**

| Log line | Location |
|---|---|
| 344 (18.28 pt too wide) | §3.2, the three-way displayed inequality chain `R⁻_{18,3} > … R⁺_{18,6}` at `main.tex` line 341–343 |
| 410 (53.61 pt too wide) | §5, the displayed definition of `N(S)` and `𝒩(S)` at `main.tex` line 408–409 |

Both are display-math lines running into the margin — the 53.6 pt one is visible in the PDF. The narrow `\geometry` setting (1.5 in left and right margins on letterpaper leaves a 5.5 in text block) makes long displays tight.

The 24 underfull boxes are a direct consequence of the hyphenation suppression in lines 17–20, not of any individual paragraph.

---

## 7. Summary of hygiene findings, by severity

**Blocking for submission**

1. No `\author`, no affiliation, no ORCID, no corresponding-address (§3). The paper is anonymous.
2. 53 corrupted em-dashes across 25 lines (§2), including 5 in the abstract alone — the first thing an editor reads.

**Should fix before submission**

3. 28/28 bibliography entries lack DOIs, 17 lack any persistent identifier (§5); `dggw2008`, the paper's analytic foundation, is among them.
4. No `.bib` file; `refs/` is empty (§5).
5. Two unused packages (`titlesec`, `tikz-cd`) are hard build blockers on a standard TeX install (§1).
6. Two overfull boxes, one badly so at 53.6 pt (§6).
7. Key/year/arXiv disagreement in `gittinsetal2024` (§5).

**Cosmetic / editorial judgement**

8. Four further unused packages: `mathrsfs`, `xcolor`, `mathtools`, `caption` (§1).
9. Global hyphenation suppression causing 24 underfull boxes (§1, §6).
10. Three separate environments all printing as "Theorem" (§1).
11. Eight defined-but-unreferenced labels, notably `rem:bugfix` (§4).
12. Hard-coded `\vspace{-2cm}` inside `\title` (§1).

**Not a defect**

13. Zero undefined references and zero undefined citations (§4). The cross-referencing is clean.
