# Submission checklist

Updated 2026-10-21 for the final build. Paper A (`paper/jga/`, *How many heat invariants determine a hyperbolic orbifold?*) and Paper B (`paper/eigen/`) go to *Annals of Global Analysis and Geometry* (AGAG). The arithmetic note (`paper/arith/`, Integers version `paper/arith/integers/`) goes to *Integers*. Every output below is in `~/Developer/release/`, outside this repository.

## Placeholders left for the authors

The list is complete: `python3 paper/tools/check_release_refs.py` checks that every placeholder in the manuscripts, the Overleaf packages, the cover letters and the three repositories is one of these four kinds.

| placeholder | where |
|---|---|
| author contribution statement | the four manuscripts (`paper/jga/manuscript.tex`, `paper/eigen/manuscript.tex`, `paper/arith/note.tex`, and `paper/arith/integers/make_integers.py`, which generates `paper/arith/integers/note.tex`) and their Overleaf copies |
| AI-use statement | the same four manuscripts and Overleaf copies; item (iii) of `paper/submission/cover-letter-note-Integers.tex` |
| Zenodo DOI, one per repository | the data statements of the four manuscripts and their Overleaf copies; the three cover letters; `README.md` and `CITATION.cff` of each repository |
| preprint identifier | `paper/eigen/references.bib` (`companionA`), `paper/arith/references.bib` (`gangetal-heat`, via `paper/arith/tools/build_bib.py`), `paper/arith/integers/make_integers.py`, the cover letters, and `README.md`, `CITATION.cff` and `.zenodo.json` of each repository |

## 1. What is ready

| output | path | built by | tested |
|---|---|---|---|
| three release repositories | `~/Developer/release/{heat-invariants-orbifolds,eigenvalues-orbifold-signature,equal-sum-reciprocal-triples}/` | `python3 paper/tools/make_release.py` | fresh copy, new environment, `make verify` then `make all`: `~/Developer/release/TEST-REPORT.md` |
| Zenodo zips, one per repository | `~/Developer/release/zenodo/*.zip`, checksums in `SHA256SUMS` there | zip of each release directory | |
| Overleaf packages | `~/Developer/release/overleaf/{paperA,paperB,note}.zip` | `python3 paper/tools/make_overleaf.py` | fresh unzip, 0 errors, 0 undefined: `OVERLEAF-TEST.md` there |
| preprint packages | `~/Developer/release/preprint/{paperA,paperB,note}.tar.gz` (copies of `paper/arxiv/`) | `python3 paper/tools/make_arxiv.py` | fresh extraction, pdflatex twice: 0 errors, 0 undefined |
| cover letters | `paper/submission/cover-letter-{A-AGAG,B-AGAG,note-Integers}.pdf` | `latexmk` in `paper/submission/` | 0 errors |

Page counts: Paper A 58 pp. with a 31-page supplement; Paper B 40 pp.; the note 19 pp. (amsart, preprint) and 25 pp. (Integers format, Overleaf).

Each repository has `README.md`, `TRACE.md` (item, script, make target), `DATA.md` (path, size, SHA-256, producing script, paper element), a `Makefile` (help, verify, full, figures, tables, data-check, all, clean), pinned `requirements.txt` and the optional environment files, `LICENSE` (MIT) and `LICENSE-DATA` (CC-BY-4.0), `CITATION.cff` and `.zenodo.json` (six authors, ORCID iDs, affiliations), and `.github/workflows/verify.yml`. The builder asserts that every data file is byte-for-byte its source or a declared edit.

## 2. Decision to settle first

**Integers' policy on AI.** The fetched submission page (`paper/arith/integers/README.md`) says: "Integers will not consider any article that makes use of artificial intelligence in producing mathematics, computer code, bibliographic information, or other content." The submission e-mail must confirm compliance. Decide, from your own knowledge of how the note, its code and its bibliography were produced, whether the note can truthfully be submitted there. Settle this before posting the note as a preprint, because its comments line and the cover letters name the journal.

## 3. The order of the remaining steps

1. **The authors review the PDFs:** `paper/jga/build/manuscript.pdf`, `paper/jga/build/supplement.pdf`, `paper/eigen/build/manuscript.pdf`, `paper/arith/build/note.pdf` and `paper/arith/integers/note.pdf`. Any change to a paper means rebuilding it and rerunning the builders (Section 4) before going on.
2. **Upload the Zenodo zips and fill the DOIs.**
   - For each repository: Zenodo > New upload, answer "No" to "Do you already have a DOI?", click "Get a DOI now!", resource type Software, metadata from the repository's `.zenodo.json`. Upload `~/Developer/release/zenodo/<name>.zip` and check its checksum against `SHA256SUMS`.
   - Fill each reserved DOI into the data statement of its paper (`paper/jga/manuscript.tex`, `paper/eigen/manuscript.tex`, `paper/arith/note.tex`, `paper/arith/integers/make_integers.py`, then rerun it), its cover letter, and the repository's `README.md` and `CITATION.cff` (`doi:`), through `paper/tools/release_config.py` and `make_release.py`. Rebuild the zip if the repository changed, then publish the record.
   - Create the public GitHub repositories `pa1aash/heat-invariants-orbifolds`, `pa1aash/eigenvalues-orbifold-signature` and `pa1aash/equal-sum-reciprocal-triples` from the same directories (`git init`, `git add .`, `git commit`, push); the workflow then runs `make verify`. The owner then makes the old repository `github.com/Ali-M658/Arithmetic-verification` private, following `paper/submission/OLD-REPO.md`.
3. **Endorsement and preprints A, B, note** (`paper/ARXIV.md`). The submitting author needs an account and endorsement in math.SP (Papers A and B) and math.NT (the note).
   1. Paper A from `~/Developer/release/preprint/paperA.tar.gz`: primary math.SP, cross-lists math.DG and math.NT, the supplement as the ancillary file `anc/supplement.pdf`.
   2. Paper B from `preprint/paperB.tar.gz`: primary math.SP, cross-list math.DG.
   3. The note from `preprint/note.tar.gz`: primary math.NT, cross-list math.SP.
4. **Fill the preprint numbers:** Paper A's into `paper/eigen/references.bib` (`companionA`), `paper/arith/tools/build_bib.py` (`COMPANION`; then run it), `paper/arith/integers/make_integers.py`; every number into the cover letters and into `README.md`, `CITATION.cff` and `.zenodo.json` of each repository (a new version of each Zenodo record). Rebuild Paper B and the note, rerun `make_arxiv.py` and replace the posted versions of B and the note if their references changed.
5. **Statements.** Fill the author contribution statements and the AI-use statements in the four manuscripts (rerun `make_integers.py`) and item (iii) of the Integers cover letter. Rebuild the papers and letters, rerun `make_overleaf.py`, and run `python3 paper/tools/check_release_refs.py`: no placeholder may remain.
6. **Six-author sign-off.** All six authors read and approve the final PDFs, the three cover letters, the three repositories and the referee suggestions they choose from `paper/submission/REFEREES.md`. The letters state that all authors have approved, so send nothing before this step.
7. **Submit.**
   - **AGAG, Paper A:** Springer's submission system. Upload the manuscript PDF and LaTeX source (`overleaf/paperA.zip`), the supplement as Online Resource 1, and `paper/submission/cover-letter-A-AGAG.pdf`. Select one of the two Co-Editors-in-Chief as handling editor. Re-check the live AGAG guidelines first (`paper/jga/AGAG.md`).
   - **AGAG, Paper B:** the same way, with `overleaf/paperB.zip`, `paper/submission/cover-letter-B-AGAG.pdf` and the same handling editor.
   - **Integers, the note:** only after the decision in Section 2. E-mail `paper/arith/integers/note.pdf` to the address on https://math.colgate.edu/~integers/submit.html, with the text of `paper/submission/cover-letter-note-Integers.tex` (MSC, keywords, AI confirmation) in the message. The source (`overleaf/note.zip`) is required on acceptance.

## 4. Commands at a glance

| purpose | command |
|---|---|
| build the three repositories | `python3 paper/tools/make_release.py` |
| test one from a fresh copy and environment | `python3 paper/tools/make_release.py --test <name> --python python3.13` |
| build and test the Overleaf packages | `python3 paper/tools/make_overleaf.py` |
| build the preprint packages | `python3 paper/tools/make_arxiv.py` (then copy `paper/arxiv/*.tar.gz` to `~/Developer/release/preprint/`) |
| check repositories and placeholders | `python3 paper/tools/check_release_refs.py` |
| full verification of this repository | `PYTHON=.venv/bin/python code/run_all.sh --full` |
