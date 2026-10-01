# Vault audit: ground_truth and verbatim notes

Audit date: 2026-10-01. Scope: every file under `research/` that (a) carries `tier: ground_truth`, or (b) has `verbatim` in its filename or note id. No other file under `research/` matches either test (`grep -rIl ground_truth research/`, `find research -iname '*verbatim*'`; the `tier:` field takes the values ground_truth x3, institutional x80, practitioner x4, unknown x38).

## Method

1. Enumerate the two groups and take the union (4 primary items; one derived claims file is listed separately).
2. Re-fetch each primary source headlessly with `curl` and a desktop User-Agent (all returned HTTP 200), extract text with pymupdf 1.27, and, for the math-heavy Takeuchi pages, render pp. 105-106 to PNG at 130 dpi and read them visually against the extracted text (the J-STAGE PDF text layer is OCR with noise such as `(3,3,L15)` for (3,3,15) and `(6,24,:24)` for (6,24,24); both were checked against the page image and normalised).
3. Compare mechanically: triples parsed into sets and diffed; formulas normalised (remove `\displaystyle`, `\tfrac`->`\frac`, `\Bigl`/`\Bigr`, whitespace and braces) and tested as substrings of the source; prose compared by whitespace-normalised `difflib` ratio and listing of every differing span; the OEIS and J-STAGE pages compared word-by-word to the live page.
4. Status vocabulary: VERIFIED = whole transcription matches; CORRECTED = discrepancy found and fixed in place; PARTIAL = only part machine-checked (stated); UNVERIFIABLE = source unreachable (none arose).
5. After edits, `hyperresearch sync` was run from the worktree root (it reports `Synced: +0 ~0 -0 =523`; the id-collision errors it prints concern unrelated notes under `research/runs/` and `research/notes/bottom-up-...`, existed before this audit, and were not touched).

Fetch routes used: J-STAGE `.../29_1_91/_pdf` (200, 1,250,993 bytes, 16 pp.) and `.../_article` (200); `https://oeis.org/A334911` (200); `https://arxiv.org/pdf/1812.06119` (200, 21 pp.), `https://ar5iv.labs.arxiv.org/html/1812.06119` (200), `https://export.arxiv.org/api/query?id_list=1812.06119` (200); `https://arxiv.org/pdf/1510.04637` (200).

## Tally

| Status | Count | Items |
|---|---:|---|
| VERIFIED | 2 | `a334911-oeis`; `research/temp/Q2-schueth-verbatim.md` |
| CORRECTED | 2 | `takeuchi-1977-...-verbatim-85-triples` (transcription); `arithmetic-triangle-groups` (summary) |
| PARTIAL | 0 | (see caveats inside rows) |
| UNVERIFIABLE | 0 | none; no new instrument gap, so `outstanding-fetches.md` was not appended |

Derived (not primary-source) file: `research/temp/claims-takeuchi-...-85-triples.json` records "85 total / 76 compact / 9 non-compact", which is now consistent with the corrected note.

## Per-note table

| Note | Primary source claimed | How fetched | Comparison method | Status | Evidence |
|---|---|---|---|---|---|
| `takeuchi-1977-arithmetic-triangle-groups-theorem-3-full-list-verbatim-85-triples` | Takeuchi, J. Math. Soc. Japan 29 (1977) 91-106, Thm 3, pp. 105-106 | J-STAGE PDF, pymupdf text plus page PNGs read visually | Parsed every `(a,b,c)` from "(i) Compact types" to "(ii) Non-compact" in both texts; set difference both ways; relative order check; visual read of the 9 non-compact triples and the Remark | CORRECTED | Before: 75 distinct compact triples. Primary: 76. Only difference: `(2,3,16)` missing from note, nothing extra in note. After: 76 = 76, symmetric difference empty, same order. Non-compact: 9 listed in note and in the PDF image, identical. Remark paragraph matches. |
| `arithmetic-triangle-groups` | J-STAGE landing page for the same article | J-STAGE `_article` HTML | Word-level diff of note body vs live page text (ratio 0.83; every difference is page navigation chrome absent from the note, no differing words in the article metadata, correction notice or reference list). Summary claims checked against PDF text | CORRECTED (summary only; body VERIFIED) | Summary said Theorem 3(i) lists "85 compact-type" triples; the PDF has 76 compact + 9 non-compact = 85. Other summary claims confirmed in the PDF: Theorem 1 criterion with inequality (15), Theorem 3, "Received Jan. 13, 1976", "It remains to classify..." remark. |
| `a334911-oeis` | OEIS A334911 | `https://oeis.org/A334911` | Word-level diff of the note body vs live page (ratio 0.95; the only differing span is the site footer "Last modified ..." chrome). Summary: sequence start 36,40,72,96,126,176,200,225,234,252,280,297,320,408 present in data line. Control-search claims re-run through the OEIS JSON API | VERIFIED | Body identical to the live record (data, comments, links, example, Maple, Mathematica, crossrefs, author). Re-run searches: "census-taker number" -> A334911, A337080; "2,8,8,3,3,12", "orbifold Euler characteristic triples", "hyperbolic triangle group covolume" -> 0 hits; "equal sum equal sum of reciprocals" -> 10 hits, all irrelevant (A126336, A357059, ...). The note's summary is a point-in-time account of searches; today's results are consistent with it. |
| `research/temp/Q2-schueth-verbatim.md` (file, not a vault note) | Schueth, arXiv:1812.06119 (Ann. Inst. Fourier 69 (2019) 2827-2855) | arXiv PDF, ar5iv full text (LaTeX alt-text), arXiv API record | Normalised substring match of every quoted display formula; prose quotes diffed (ratio 0.98, remaining differences are only `$` delimiters stripped for the comparison); journal-ref compared to API; algebra of the consistency check re-derived symbolically | VERIFIED (quoted material) | Match: Remark 4.2 (both displayed formulas, the `sin^-2` identity, `b_0`, `b_1`, the closing sentence naming [8], 5.6); eq. (17); Theorem 4.1 (both brackets, concatenated); Remark 5.4(ii) quote; leading term of eq. (23). Journal-ref "Ann. Inst. Fourier 69 (2019), no. 7, 2827-2855" matches the API. The check "doubling c_2 at gamma=pi/k gives (k^5-1/k)/2520+(k^3-1/k)/720+(k-1/k)/180" is exact (sympy, difference 0). Not transcription and not checked here: the "verdict" paragraphs about the manuscript's equations (4)-(5) and `paper/main.tex` line 237. Eq. (23)'s second term is printed as `(\cdots)` in the file, i.e. an elision, not a quotation. Remark 5.2 is paraphrased, not quoted (the paraphrase agrees with the source). |

## Corrected notes: before and after

### 1. `takeuchi-1977-arithmetic-triangle-groups-theorem-3-full-list-verbatim-85-triples`

Cause: the transcription dropped `(2,3,16)`. The note's own check, "the compact list as transcribed above has 76 triples", was a count asserted from a remembered figure (the commonly cited 85 = 76 + 9), not a count of the list actually written, so it never failed although the list held 75.

Edit 1 (list), before:

    ... (2,3,12), (2,3,14), (2,3,18), (2,3,24), ...

after:

    ... (2,3,12), (2,3,14), (2,3,16), (2,3,18), (2,3,24), ...

(Primary text, p. 105, line 2 of the list: "(2, 3, 7), (2, 3, 8), (2, 3, 9), (2, 3,10), (2, 3,11), (2, 3,12), (2, 3,14), (2, 3,16),".)

Edit 2 (self-check paragraph): the sentence "(Count check: the compact list as transcribed above has 76 triples + 9 non-compact = 85 total, ...)" was replaced by a dated correction that states the omission, states that the old check compared against a remembered number, gives the corrected tally, and describes the reproducible check (parse every `(a,b,c)` between the "(i)" and "(ii)" headings, assert `len(set(t)) == len(t)`, and diff against the set parsed from the PDF). The secondary corroboration is retained and now confirmed: Nugent-Voight arXiv:1510.04637 (fetched today) says "Takeuchi finds precisely 85 such triples, and they fall into 19 commensurability classes". That reproduction is secondary and only corroborates the total; the 76-triple list was compared to the primary PDF.

Verification after the edit: parsed from the note, 76 compact triples, 76 distinct; parsed from the primary pp. 105-106, 76 distinct; set difference empty in both directions; non-compact 9; total 85. Frontmatter unchanged and valid YAML (`tier: ground_truth` retained); `hyperresearch sync` run.

Honest limits: the self-check inside the note is still prose, not an executing assertion, because notes are Markdown; the mechanical check lives in this audit and is described in the note so it can be re-run. The PDF text layer is OCR, so the set comparison used OCR text with two repairs (`3,L15`, `6,24,:24`) that were each confirmed against the rendered page image; the visual read of the full list also finds 76 compact triples.

### 2. `arithmetic-triangle-groups` (summary field only)

Before: "Theorem 3(i)'s list of 85 compact-type arithmetic triples explicitly includes both ..."
After: "Theorem 3(i)'s list of the 76 compact-type arithmetic triples (Theorem 3 overall: 85 = 76 compact + 9 non-compact) explicitly includes both ..."

The body (landing-page text) was not changed; it is identical to the live page apart from navigation chrome.

## Other observations

- The Takeuchi note's "Setup", "Finiteness" and "Key finding" sections are paraphrase and derivation, not verbatim; the sample checked against the PDF (Definitions 1-3, Theorem 1(i)(ii) with inequality (15), Theorem 2, bounds e1<=73, e2<=2811, e3<=10^7, TOSBAC-3400, Lemmas 4-5, Propositions 6-7) is consistent, but the paraphrase was not compared sentence by sentence. The note's account of failed fetch routes (projecteuclid, CiNii) is process narrative and was not re-run.
- Unrelated side finding while reading Schueth: the arXiv PDF and ar5iv both print the first term of `c_1(gamma)` as `(pi^4-gamma^4)/(720 gamma^2 pi)`; for gamma=pi/k the doubled value is only equal to Remark 4.2's `a_1` if the denominator is `gamma^3`, so this looks like a misprint in the source. Q2 does not quote `c_1`, so nothing in the vault is affected, but anyone quoting formula (2) should check.
- Notes whose body merely contains the word "verbatim" (not by name or id) were outside the stated scope and were not audited: e.g. `spectral-invariants-for-polygons-and`, `181206119-schueth-corner-contributions-ar5iv-fulltext`, `11034372-doyle-rossetti-fulltext`, `151004637-on-the-arithmetic-dimension-of-triangle-groups`, `math0504571-hubers-theorem-for-hyperbolic-orbisurfaces`.
- Pre-existing: `review/takeuchi-verdict.md` and `review/P2*.md` rely on Takeuchi Thm 3 as "76 compact triples"; that count is correct against the primary source, so those documents need no change on this point.
