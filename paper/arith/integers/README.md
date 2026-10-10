# The arithmetic note in the format of *Integers*

`note.tex` in this folder is *Triples with equal sum and equal reciprocal sum* set in the article template of *Integers: Electronic Journal of Combinatorial Number Theory*. It is generated from `../note.tex`, the amsart version used for arXiv. The mathematics and wording are unchanged except where the journal's guidelines require a change; those changes are listed below.

Build, from this folder:

```
latexmk        # pdflatex, three passes; writes note.pdf, auxiliary files go to build/
```

The bibliography is written into `note.tex` (`thebibliography`), as the journal requires, so no BibTeX run is needed. The figure is read from `figures/out/F9.pdf` at the repository root.

## Sources (fetched 2026-10-10)

| what | URL | SHA-256 |
|---|---|---|
| Journal home page | https://math.colgate.edu/~integers/ | `af15e12b1a5918c141ef2ab5fef8b9f07d44f51c2f853275242e7ef12d03ecb8` |
| Submission info and instructions for authors | https://math.colgate.edu/~integers/submit.html | `95e6c6d37da5ccb7ea69e4479bde018e4a02368074bf477841e69da3dc0aa9a1` |
| Policies (ethics, review, copyright) | https://math.colgate.edu/~integers/policies.html | `d47d07e391c5e3726efde736e0d9aab7329c220bac79aa3ed81ce96c7409a1a3` |
| Article template (zip: `integers.sty`, `IntegersTemplate.tex`, `erdos1.pdf`, the template PDF) | https://math.colgate.edu/~integers/IntegersTemplate.zip | `659d72739579e355a1e8dce20b4f5d2a8eab8867afff6805532e532b992405ba` |
| Template and formatting information (PDF; identical to the copy in the zip) | https://math.colgate.edu/~integers/IntegersTemplateAndFormattingInfo.pdf | `53545fce3c740a8543b6f1682027ca16e5324ff78b51b11f8b701da97208032b` |
| AMS *Abbreviations of Names of Serials* (the template requires these journal abbreviations) | https://mathscinet.ams.org/msnhtml/serials.pdf | (list dated 10 October 2026) |
| Crossref record of the published version of `ysv2024` | https://api.crossref.org/works/10.3336/gm.60.1.04 | `729462c5f0be66700036e4a1f4a7cd7b0457b1ccdffb1b26bd809c3db7a26159` |

`integers.sty` (dated 2026/08/21) and `erdos1.pdf` are the journal's files from the template zip, unmodified. The style's `\maketitle` places `erdos1.pdf` in the header, so both must sit next to `note.tex`. The address `https://www.integers-ejcnt.org/` failed TLS verification from this machine, so the Colgate address, which serves the current pages, was used.

## What the journal asks for

From the submission page:

- **Submission:** a PDF sent by e-mail to the address on the submission page.
- **The e-mail must give:**
  - (i) the MSC codes;
  - (ii) the keywords;
  - (iii) the authors' confirmation that the article complies with the journal's "Use of AI" guideline.
- **Use of AI guideline**, verbatim: "Integers will not consider any article that makes use of artificial intelligence in producing mathematics, computer code, bibliographic information, or other content. This does not apply to the use of basic tools to improve the presentation, such as grammar and spelling."
- **The template:**
  - required on acceptance (source file with `integers.sty`, plus the graphics);
  - welcome at any stage, including first submission.
- **Review:** single-blind; referees know the authors.

So the MSC codes and keywords are not printed in the article, since the template has no place for them. They go in the e-mail, which is `paper/submission/cover-letter-note-Integers.tex`.

## Changes from `../note.tex`

All changes are made by the template or its guidelines.

**Title page:**
- Class `article` with `integers.sty` and the template's hyperref set-up.
- Title in the template's style.
- Authors with affiliation and e-mail in the template's format, set in two columns so that the title, authors and abstract fit on the first page, as in the template.
- The ORCID iDs and the corresponding-author footnote of the amsart version are not printed; the template has no field for them.
- The header fields (`#A1`, "Received: , Revised: …", DOI) are the template's defaults; the editors fill them on acceptance.

**Theorem environments:** those of `integers.sty`, numbered separately (Theorem 1, Lemma 1, …), instead of by section.

**Section titles:** capitalised words ("Relation to the Literature", "The Curves $C_\Lambda$", …).

**Writing guidelines:**
- Oxford commas, including "Bremner, Guy, and Nowakowski".
- "Proposition", "Theorem", "Corollary" and "Chapter" written out in citations.
- "Equation (n)" for equation references.
- An unreferenced display, the Weierstrass model, is unnumbered.
- A comma after a sentence-initial "Hence".
- "(b) The ratio $\mathcal N(S)/S$ …" in the figure caption, so that the sentence does not begin with notation.
- Table captions beneath the tables.
- Acknowledgements in the template's `\acknowledgements`, immediately before the references.

**Margins:**
- The two bounds of Theorem 1 on separate display lines.
- `\emergencystretch` so that lines with long inline formulas stay within the margins.

**Statements and declarations:**
- Kept as one unnumbered section before the acknowledgements, with the same placeholders as the amsart version.
- The data statement names the programs by file name instead of by repository path.

**References:**
- Inline, alphabetical, with numeric labels, in the template's format.
- Journal names abbreviated as in the AMS list. Three journals are not in the current AMS list, so their names follow the fetched zbMATH records instead (*C. R. Acad. Sci., Paris, Sér. I*, *Serdica Math. J.*) or are given in full (*Nature Communications*).
- The companion paper is cited as "preprint, arXiv:[PLACEHOLDER]".
- `ysv2024` is cited as published in *Glas. Mat. Ser. III* 60 (2025), following its Crossref record.
