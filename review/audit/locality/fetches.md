# Locality audit: source retrieval log

All external inputs were taken from the pre-fetched texts in `review/audit/sources/`
(page numbers below are the printed page numbers, cross-checked against the PDFs with pymupdf):

| source | file | anchors used |
|---|---|---|
| Dryden–Strohmaier, arXiv:math/0504571v2 | `ds_math0504571.txt` | eq. (1) p. 3; wave example g[ln N(P)] p. 4; eq. (2) p. 4; ψ_m and its asymptotics p. 4; Def 3.1, Thm 3.2 p. 5 |
| Dryden–Gordon–Greenwald–Webb, arXiv:0805.3148v1 | `dggw_0805.3148.txt` | discrete spectrum p. 2; Def 4.7 (ii),(iii) and Thm 4.8, (4.9) p. 17; Lemma 5.4, Prop 5.5, (5.7) p. 24; (5.9), (5.10) p. 26 |
| Uçar, arXiv:1711.03405 | `ucar_1711.03405.txt` | Thm 4.11 p. 127; (4.25) p. 134; (4.33), Thm 4.20 (i), (4.35) p. 137; Thm 4.20 (ii) p. 138 |
| Schueth, arXiv:1812.06119 | `schueth_1812.06119.txt` | Thm 4.1 p. 14 |
| Thurston, ch. 13 (electronic edition) | `thurston_ch13.txt` | 13.3.4, 13.3.5 and the following sentence p. 312; Thm 13.3.6 p. 312; primitive pieces pp. 315–318; Cor 13.3.7 and proof p. 318 |
| Marklof, arXiv:math/0407288 | `marklof_math0407288.txt` | (69) p. 13; Thm 4 (182) p. 25; (192)–(193) p. 26; Cor 1 p. 27 |

No further retrieval was needed. Not attempted (not required by the argument, and not
openly available headlessly): Hejhal, LNM 548 (1976) and Iwaniec, GSM 53 (2002), which DS cite
for eq. (1). The audit uses DS eq. (1) exactly as DS state it. Standing gaps accepted per
instructions: Donnelly 1976 (used only through DGGW's restatement), Steinig 1971, Drury–Marshall 1987.

Source defect noticed: Marklof (192)–(193) print the exponent as t²/(2β); with his normalisation
(69) the transform of e^{-βρ²} is e^{-t²/(4β)}/√(4πβ) (`check_P2.py`). The prefactor as printed fits only
the 4β version. This does not affect the paper, whose g_t uses 4t.
