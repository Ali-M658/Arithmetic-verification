# Fetch log (stability referee)

All retrieval headless (curl with a desktop user agent; arXiv export API). No browser.

| what | how | result |
|---|---|---|
| Uçar thesis, arXiv:1711.03405, (4.22)-(4.35) | `review/audit/sources/ucar_1711.03405.txt` (provided) | used: (4.25) c^S_l(π/k), (4.33) C, (4.35) a_ν(O); Thm 4.20(ii) (cone contribution = C) |
| Ostrowski, Acta Math. 72 (1940), §69-71, Théorème XXX | `review/audit/sources/ostrowski_1940.txt` + `.pdf` (provided) | OCR text is garbled; pages 210 and 212 rendered from the PDF to `ostrowski_p53.png`, `ostrowski_p55.png` and read visually. (71,1) and Théorème XXX are on p. 212; ε is defined in (69,4) on p. 210 with γ = Max(\|x_ν\|, \|y_ν\|). |
| Holtz–Tyaglov (Orlando's formula) | `review/audit/sources/holtz_tyaglov_1005.2843.txt` (provided) | **GAP / WRONG SOURCE.** arXiv:1005.2843 is M. Rauch, "Extended Scalar Sector and Fat Jets" (hep-ph), not Holtz–Tyaglov. |
| Holtz–Tyaglov, correct identifier | `curl https://export.arxiv.org/api/query?search_query=au:Holtz+AND+au:Tyaglov` | returns arXiv:0912.4703, "Structured matrices, continued fractions, and root localization of polynomials" (journal_ref from the arXiv API: SIAM Review 54 (2012), no. 3, 421-509; DOI 10.1137/090781127). Fetched `https://arxiv.org/pdf/0912.4703v3` to `holtz_tyaglov_0912.4703.pdf`, text in `holtz_tyaglov_0912.4703.txt`. Theorem 1.14 (generalized Orlando formula, eq. (1.30)) and the remark that the classical Orlando formula follows from it are on pp. 3 and 12. |
| Donnelly 1976 | not fetched | standing gap (not needed for the stability group). |

Not needed for my re-derivations: the Hurwitz-determinant evaluation det B = (−1)^{n(n−1)/2}∏(m_i+m_j)
is proved in REVIEW.md by a divisibility and degree argument, independently of Orlando's formula.
