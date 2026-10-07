# Sources for theory/eigen

Retrieved headless with curl on 2026-10-07. Only one external input is used beyond the manuscript
itself and textbook hyperbolic trigonometry; every trigonometric identity used is also checked
numerically, in diameter.py and necessity.py.

| input | where used | primary source | status |
|---|---|---|---|
| Jørgensen's inequality: if A, B generate a non-elementary discrete subgroup of SL(2,C), then \|tr²A − 4\| + \|tr[A,B] − 2\| ≥ 1 | Proposition eig:233 (systole of O(2,3,m)) | T. Jørgensen, On discrete groups of Möbius transformations, Amer. J. Math. 98 (1976) 739–749, doi:10.2307/2373814 | **Instrument gap**: the primary source (JSTOR) is not retrievable headless; doi.org resolves to a JSTOR landing page. The statement is quoted from `wiki_jorgensen.txt` (Wikipedia, "Jørgensen's inequality", fetched text). The bibliographic data are corroborated by `arxiv_1809.07309.txt` (Gongopadhyay–Mishra–Tiwari, arXiv:1809.07309, reference [4]). |

Files:
- `wiki_jorgensen.txt`: the statement, verbatim from the fetched page.
- `arxiv_1809.07309.txt`: full text of arXiv:1809.07309, which recalls the inequality and gives the
  reference.

Attempted and unreachable (bot walls): JSTOR stable/2373814; Project Euclid and Springer PDFs of
G. J. Martin, Acta Math. 163 (1989), doi:10.1007/BF02392737.

Bibliography entry for the paper (not added to paper/jga/references.bib, which this session may not
edit):

    @article{jorgensen1976,
      author  = {J{\o}rgensen, Troels},
      title   = {On discrete groups of {M}{\"o}bius transformations},
      journal = {Amer. J. Math.},
      volume  = {98},
      number  = {3},
      pages   = {739--749},
      year    = {1976},
      doi     = {10.2307/2373814}
    }
