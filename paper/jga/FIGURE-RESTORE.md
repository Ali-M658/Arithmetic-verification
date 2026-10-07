# FIGURE-RESTORE: figures and the admissibility lemma back in the paper; captions tightened

Input: the round-1 revision (commit `b06a563`; manuscript 35 pages, supplement 15). Output:
`manuscript.tex` **37 pages**, `supplement.tex` **12 pages**, `paper/arith/note.tex` **12 pages**,
each built with 0 LaTeX errors, 0 undefined references, 0 undefined citations and 0 overfull boxes
(`BUILD.md`; the note's log likewise). No figure output, script or data file changed, so
`DATA-MANIFEST.md` is unchanged (`admin/build_data_manifest.py --check` passes).

## 1. Figures restored (A1)

| figure | paper number | where | first mention |
|---|---|---|---|
| F1, the two pillows coloured by the heat-kernel diagonal | Fig. 1 | Introduction, foot of its first page (p. 2, placement `[b]`) | first paragraph of §1 ("where heat lingers (Figure 1)"), and after Thm 1.2 |
| F6, the moduli family and the eigenvalue flow | Fig. 4 | §4 "What heat does not hear", after Cor. 4.3 (p. 18) | the restored paragraph after Cor. 4.3 |
| F2, the (2,8,8) and (3,3,12) tilings on the hyperboloid | Fig. 5 | §5 "The rigid case", after its opening paragraph (p. 20, placement `[b]`) | §5 opening ("the double of a hyperbolic triangle ... (Figure 5)") |

F3, F4, F5, F7, F8 stay in the paper; F9 stays in the companion note. Every figure is referenced in
the text. All nine PDFs are 119 mm wide (337.323 pt), so none was resized and no script or render
was touched.

Text restored with F6 (one paragraph, after Cor. 4.3), from §S7 of the round-1 supplement (now §S6): the family of signature
$(0;3,3,3,3)$ (doubles of quadrilaterals with angles $\pi/3$, two mirror symmetries, parameter
$\vartheta$, $\sinh a\sinh b=\frac12$), systoles $2.634\to0.694$, traces equal to
$\mathrm I+4\mathrm E_3$ to $1.2\times10^{-12}$, $\lambda_1$ from $4.122$ to $0.435$.

Placement adjustments:
- §4, after Cor. 4.6: the sentence that sent the reader to Fig. 8(b) (F5) from §4 now points to the
  family of Figure 4 (F6) and to §7, so F5's first mention is in §7, where it is placed.
- F5 is placed at the start of §7 in the source; it prints at the top of p. 30, the page after its
  mention, because the generated Table 1 holds the top of p. 29. This is as in round 1.
- §7 "Changing the shape": the numbers now stated with F6 in §4 (eight members, $1.2\times10^{-12}$,
  $\lambda_1$) are no longer repeated; the paragraph keeps the 28-pair comparison with Thm 4.5.
- §7 opening: "and the moduli figure are in the supplement" removed.
- §3.3, before Fig. 3 (F4): the selection rule of the 525 areas (genus $\le1$, at most four cone
  points, orders $\le12$, complete classes, 504 with orders above 12, only bounds beyond $s=7/5$)
  moved from the caption into the sentence that introduces the figure.

## 2. Admissibility lemma restored (A2)

Lemma S1.1 is now **Lemma A.1** in **Appendix A, "Admissibility of the heat function"** (the
appendices are now A admissibility, B proofs of the growth results, C computational methods), with its
complete proof (eigenvalue counting via a compactly supported test function; dominated convergence
on each side of the trace formula). The proof of Thm 2.3 and Remark 2.9 cite Lemma A.1 instead of the
supplement. Supplement §S1 is removed (its later sections renumber: searches §S1, strata §S2,
certificates §S3, spectra §S4, blind recovery §S5, moduli §S6); its abstract now lists four sections,
and "No theorem of the paper depends on it" is now true without exception.

## 3. Captions (A3)

Every caption is at most two sentences: what is shown, and the one point. The stylised renders say
"Schematic, not isometric, shapes" (F1, F6). Colours are named only where needed (none by hue; tones
only for line styles and the split disc). Every statement is asserted by the figure's script or
proved in the paper (F1: maximum equals the largest order to 1%, median $1-t/3$; F2: tile area
$\pi(1-R)=\pi/4$; F5: slope/sign/emergence assertions; F6: systoles and $\lambda_1$; F7: overlaps and
first collisions; F8: slopes and $\delta_{\rm cert}$). `\ref` targets are unchanged and resolve.

Word counts: LaTeX source tokens, each inline formula counted as one word (script in the session
scratchpad: formulas `$...$` -> one token, `\ref{...}` -> one token, other control words dropped).

| figure | used in | old words | old sentences | new words | new sentences |
|---|---|---|---|---|---|
| F1 | paper (was supplement) | 97 | 3 | 52 | 2 |
| F2 | paper (was unused) | 74 | 3 | 51 | 2 |
| F3 | paper | 102 | 3 | 47 | 2 |
| F4 | paper | 153 | 4 | 43 | 2 |
| F5 | paper | 101 | 3 | 57 | 2 |
| F6 | paper (was supplement) | 99 | 3 | 49 | 2 |
| F7 | paper | 88 | 3 | 54 | 2 |
| F8 | paper | 75 | 3 | 51 | 2 |
| F9 (`\figcapNine`, unused macro) | — | 90 | 3 | 62 | 2 |
| F9 (companion note, `note.tex`) | note | 90 | 3 | 53 | 2 |
| **paper total (F1-F8)** | | 789 | | 404 | |

Old captions were up to four sentences; the old note caption had three.

## 4. Page budget (A4)

| | before | after |
|---|---|---|
| manuscript (references and appendices included) | 35 | **37** |
| supplement | 15 | 12 |
| companion note | 12 | 12 |

The three figures (about 1.2 pages), the F6 paragraph and Appendix A (about 0.6 page) were paid for
by the shorter captions (F3, F4, F5, F7, F8, already in the paper: 519 words before, 252 after) and the de-duplication in §7; the
result is 37 pages with p. 37 about one third full, inside the 38-page limit and at the ideal.
**No text was moved to the supplement**: a move was not needed to reach 37, and moving text further
would only have removed content from the paper. The moves made are the ones listed in §1 and §2
(caption text into §3.3; §7 numbers stated once in §4; the lemma from the supplement into the paper).

## 5. Checks (A5)

- Builds: `cd paper/jga && latexmk && latexmk` (clean `build/`), `cd paper/arith && latexmk note.tex`;
  zero errors, undefined references or citations, overfull boxes. PDFs not committed.
- Every page holding a figure was rendered (pdftoppm) and inspected: pp. 2 (F1), 13 (F3), 16 (F4),
  18 (F6), 20 (F2), 23 (F7), 28 (F8), 30 (F5) of the manuscript and p. 10 (F9) of the note. All at
  119 mm, every caption fits under its figure, and no figure sits above its section's heading.
- PDF metadata: title, keywords and the six authors only.
- `PYTHON=.venv/bin/python bash code/run_all.sh --quick --only 'figures|paper tables|DATA-MANIFEST|check_note|conventions-check|revision'`:
  7 passed, 0 failed, 1 skipped (Blender renders, by design): theory conventions-check, DATA-MANIFEST
  is current, figures data F4 F7 F8, figures vector F2-F5 F7-F9 (byte-identical), revision
  run_checks, round1 paper tables current, arith check_note.
