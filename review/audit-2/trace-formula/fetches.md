# fetches.md: group trace-formula

No new network retrieval was made by this reviewer. All third-party text was read from the files
fetched headlessly by `review/audit-2/fetch_sources.sh` into `review/audit-2/sources/`. The PDF
hashes were re-computed and match `sources/SHA256SUMS`.

| source | URL (from fetch_sources.sh) | file used | sha256 (pdf) | passages used (printed page) |
|---|---|---|---|---|
| Dryden-Strohmaier, arXiv:math/0504571v2 | https://arxiv.org/pdf/math/0504571v2 | `ds_math0504571.txt` | 2f805716...872755d (match) | eq. (1) and the paragraph after it, p. 3 (eigenvalue = 1/4 + r^2, weight 1/(2 m(R) sin theta(R)), theta(R) = pi l/m(R), integrand e^{-2 theta r}/(1+e^{-2 pi r}) h(r), hypothesis on h, "g is the Fourier transform of h and thus is a compactly supported smooth function") |
| Ucar, arXiv:1711.03405 | https://arxiv.org/pdf/1711.03405 | `ucar_1711.03405.txt` | b6da48a7...0c0a74 (match) | (4.20)-(4.21) p. 132; (4.22)-(4.23) p. 133; (4.24)-(4.26) p. 134 (PDF p. 139); Cor. 4.19, (4.31)-(4.34) pp. 136-137; Thm 4.20 (i) (4.35) p. 137 and (ii) p. 138 (PDF pp. 142-143) |
| Dryden-Gordon-Greenwald-Webb, arXiv:0805.3148 | https://arxiv.org/pdf/0805.3148 | `dggw_0805.3148.txt` | bda49c21...e89c892 (match) | curvature sign convention "R_abab is the sectional curvature", p. 16; Thm 4.8 and (4.9), p. 17; Prop. 5.5, Example 5.6, (5.7), p. 24; (5.9)-(5.10) and the sum 1/sin^4 identity, pp. 25-26 |
| Schueth, arXiv:1812.06119 | https://arxiv.org/pdf/1812.06119 | `schueth_1812.06119.txt` | 8a3948ae...5a82 (match) | (17) and Thm 4.1, printed p. 14 (PDF p. 17); Rem. 4.2, printed pp. 14-15; "the above formulas for a_0 and a_1 were already computed in [8], 5.6", printed p. 15 (PDF p. 18); attribution sentence in the introduction, pp. 3-4 |

Context statements read: `review/audit/statements/locality.md` (LO.6-LO.11, DF.1), and
`review/audit/statements/signatures.md` lines 36-62 (heat input H1-H3) and DF.1, as named in the task.

## Not reached (instrument gaps)

- Weyl's law for compact orbifolds (any primary source): not fetched. It is cited in Remark 4.12 as an
  alternative source of Z(s) = O(1/s); my verdict does not rely on it (a self-contained route is given
  in REVIEW.md, TF.7).
- Hejhal / Iwaniec (the sources DS cite for eq. (1)): not fetched; the trace formula is taken as stated
  in DS eq. (1), p. 3, together with the admissibility lemma LO.7 (previously audited).
- Donnelly 1976: standing gap (not needed here).
