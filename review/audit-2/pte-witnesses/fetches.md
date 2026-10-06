# fetches.md (group pte-witnesses)

No network retrieval was made by this reviewer. Every third-party text used was the copy already
fetched headlessly by `review/audit-2/fetch_sources.sh` into `review/audit-2/sources/`.

| source | file | used for | status |
|---|---|---|---|
| Uçar, PhD thesis, arXiv:1711.03405 | `sources/ucar_1711.03405.txt` (PDF sha256 b6da48a7…0a74 matches `SHA256SUMS`; the `.txt` is not listed in `SHA256SUMS`) | Eqs (4.25) (text line 11615, Prop. 4.17), (4.33)–(4.34) (Cor. 4.19, line 11948), (4.35) (Thm 4.20(i), line 12001, printed p. 137). Cone and smooth terms re-implemented in `heatlib.py` (`ucar_b`, `ucar_alpha`). They agree exactly with the formula of Proposition heatinput for l ≤ 12, m ≤ 40 (`check_heat.txt`). | used |
| Chen, survey, arXiv:2506.11429 | `sources/chen_survey_2506.11429.txt` | Cited in PW.1 (for [1,5,5]=[2,3,6]) and PW.3 (for "type (−1,1,3) entry A.685"). Grep of the text extraction for "685", "A.6", "21, 28", "15, 30", "10, 15", "5, 21", "1, 5, 5", "2, 3, 6" and "−1, 1, 3" returned nothing. The PDF text layer may format the tables differently. | **not located** (instrument gap). Provenance belongs to the literature group. Both numbers were re-verified directly: [1,5,5] and [2,3,6] have equal s1 = 11 and s3 = 251 (s2 = 51 vs 49), see `check_pairs.txt`; {3,10,15,30} ~ {4,5,21,28} is verified in `check_pencil61.txt`. |
| Borwein–Ingalls 1994, Borwein–Lisoněk–Percival 2003, CMSV arXiv:2304.11254 | `sources/cmsv_2304.11254.txt` (present); BI and BLP are not in `sources/` | Provenance of W08–W11 (PW.1). The recipes are withheld from this bundle. The pairs themselves were verified directly from their printed orders. | not needed for the verification; provenance not checked (literature group) |

Unreachable or unavailable: none attempted. No browser was used and nothing was quoted from memory.
