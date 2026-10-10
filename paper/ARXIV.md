# ARXIV: posting Papers A and B and the arithmetic note on arXiv

Paper A is `paper/jga/manuscript.tex`, "How much of a hyperbolic orbifold does heat hear?", with its supplement `supplement.tex`.
Paper B is `paper/eigen/manuscript.tex`, "Finitely many eigenvalues determine the signature of a hyperbolic orbifold".
The arithmetic note is `paper/arith/note.tex`, "Triples with equal sum and equal reciprocal sum" (the amsart version; the version for Integers, `paper/arith/integers/note.tex`, carries the journal's header fields and is not posted).

The packages are built by `python3 paper/tools/make_arxiv.py` into the git-ignored `paper/arxiv/` folder, which then holds `paperA/`, `paperB/`, `note/` and their `.tar.gz` files. Before running it, build all three, Paper A first, because Paper B reads Paper A's numbering:

```
cd paper/jga && latexmk && latexmk
cd paper/eigen && latexmk
cd paper/arith && latexmk
```

## What a package contains

Each package follows arXiv's TeX submission guidance, fetched 2026-10-10 from info.arxiv.org/help/submit_tex, ancillary_files and endorsement.

- The main `manuscript.tex`, with every comment removed and the figure captions inlined.
- The class file `sn-jnl.cls` (Papers A and B; the note uses the standard `amsart`).
- The figures in `figures/out/`.
- The pre-generated `manuscript.bbl`. arXiv uses a `.bbl` whose name matches the main file, so no `.bib` is shipped.
- No `xr`, which arXiv advises against. Every cross-document reference is replaced by its number:
  - in Paper A, the references to its supplement;
  - in Paper B, the references to Paper A.
- No hidden files.
- For Paper A only, the supplement as an ancillary file, `anc/supplement.pdf`. arXiv lists ancillary files on the abstract page.

The script compiles each package in a temporary copy and refuses to write it if:

- there is a LaTeX error or an undefined reference;
- the page count differs from the build;
- a forbidden string appears: a repository path, review history, the earlier target journal, or any attribution.

## What the authors must do

1. **Fill the placeholders first.** All three manuscripts still carry three placeholders, and none of them should reach arXiv:
   - `[PLACEHOLDER: author contributions]`;
   - `[PLACEHOLDER: AI-use statement]`;
   - `[PLACEHOLDER: Zenodo DOI, to be minted at submission]`.

   Mint the Zenodo DOI, fill all three, rebuild, and rerun `make_arxiv.py`.
2. **Account.** The submitting author needs an arXiv account; registration is at arxiv.org/user/register. arXiv asks first-time submitters to associate an institutional email address if they have one, because this speeds up endorsement.
3. **Endorsement.** A first submission to a category needs endorsement. Without an institutional address or claimed prior papers, the submitter must find a personal endorser:
   - start a submission in the category;
   - arXiv emails an endorsement request containing a link;
   - send that link to an established author in the area.

   arXiv suggests looking at recent arXiv papers the manuscript cites and following "Which authors of this paper are endorsers?" on their abstract pages. Endorsement is needed for math.SP, the primary category. Check whether the cross-list categories need it too.
4. **Categories.**
   - Paper A: primary **math.SP**, cross-lists **math.DG** and **math.NT**.
   - Paper B: primary **math.SP**, cross-list **math.DG**.
   - The note: primary **math.NT**, cross-list **math.SP**. Its primary category is math.NT, so endorsement is needed there too.
5. **Order.** Paper B cites Paper A as `arXiv:[PLACEHOLDER: arXiv number of the companion paper]` (in `paper/eigen/references.bib`, entry `companionA`).
   - Submit Paper A first and wait for its identifier.
   - Replace the placeholder with the identifier, rebuild Paper B, rerun `make_arxiv.py`, and submit Paper B.
   - Then submit the note. It cites Paper A through `COMPANION` in `paper/arith/tools/build_bib.py` (run the script without `--fetch` after filling the number) and through `gangetal-heat` in `paper/arith/integers/make_integers.py`; rebuild the note and rerun `make_arxiv.py` first.
   - Optionally, give Paper A a second version whose bibliography cites Paper B and the note by their identifiers (`companionB` and `companion` in `paper/jga/references.bib`).
6. **Metadata.**
   - The title and the six authors as on the title page.
   - The abstract as plain text: it is in each `manuscript.tex`, and LaTeX math is acceptable in arXiv abstracts.
   - A comments line, e.g. "44 pages, 8 figures; supplementary material as an ancillary file" for A, "26 pages, 3 figures" for B, and "12 pages, 1 figure" for the note. Use the page counts of the final build.
   - The MSC classes, which are in each manuscript.
   - A licence of the authors' choice. The Springer policy (`paper/jga/fetched/springer-journal-policies-20260919.html`, "Preprint sharing") encourages posting preprints of primary research manuscripts before peer review.
7. **After acceptance.** Add the journal reference and DOI to the arXiv records.

## Checks before uploading

- Open `paper/arxiv/paperA/`, `paperB/` and `note/` and look at the PDF that arXiv's preview produces.
- Check that the supplement appears as an ancillary file of Paper A.
- Check that no placeholder text remains: `grep -r PLACEHOLDER paper/arxiv/`.
