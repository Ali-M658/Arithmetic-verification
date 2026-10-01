# Retrieval log (audibility referee)

| what | how | result |
|---|---|---|
| Holtz–Tyaglov, "Structured matrices, continued fractions, and root localization of polynomials" | arXiv API `search_query=au:Holtz AND au:Tyaglov` → arXiv:0912.4703v3; PDF via `curl -A <desktop UA> https://arxiv.org/pdf/0912.4703v3`; text extracted with PyMuPDF | `ht_0912.4703.pdf`, `ht_0912.4703.txt` (79 pp.). Used: (1.2) p.4 (p(z)=a_0z^n+…+a_n), (1.37) p.13 (Hurwitz determinants Δ_j), Theorem 1.17 / (1.41) p.13 (Orlando: Δ_{n-1}(p) = (−1)^{n(n−1)/2} a_0^{n−1} ∏_{i<j}(z_i+z_j)). |
| Crossref metadata for the same | `api.crossref.org/works?query.bibliographic=…` | DOI 10.1137/090781127, SIAM Review 54 (2012) 421–509. |

## Instrument gap / source defect

- `review/audit/sources/holtz_tyaglov_1005.2843.txt` (and `.pdf`) is **not** Holtz–Tyaglov. arXiv:1005.2843 is
  M. Rauch, "Extended Scalar Sector and Fat Jets" (hep-ph); the text contains no Hurwitz determinant and no
  Orlando formula. The correct preprint is arXiv:0912.4703, fetched above. Every statement that cites
  "Holtz–Tyaglov (1.37)" / "Orlando" was checked against the correct text.

## Sources read from `review/audit/sources/`

- `ucar_1711.03405.txt` / `.pdf`: (4.25) printed p.134 (PDF p.139); (4.33) and Thm 4.20(i) (4.35) printed p.137
  (PDF p.142); Thm 4.20(ii) printed p.138 (PDF p.143). Layout of (4.25) and (4.33) confirmed visually from the PDF
  pages, since the text extraction garbles fractions.
- `dggw_0805.3148.txt`: Prop 5.5 (I_N = (m²−1)/12 + O(t) for a cone point of order m), cross-check for l = 0.
- `schueth_1812.06119.txt`: Theorem 4.1 (printed p.14), cross-check for l = 2.

No other retrieval was needed. Standing gaps (Steinig 1971, Drury–Marshall 1987, Donnelly 1976) not chased;
Donnelly enters only through Uçar's proof of Thm 4.20 (citing [Don76, Thm 5.1]).
