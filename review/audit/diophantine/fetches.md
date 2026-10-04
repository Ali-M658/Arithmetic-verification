# Diophantine group: retrieval log

All retrieval headless (curl, desktop browser UA string). Date: 2026-10-01.

| file | source | result |
|---|---|---|
| `review/audit/sources/bgn_mcom1993.txt` | Bremner–Guy–Nowakowski, Math. Comp. 61 (1993) (provided) | read in full; the "egg" sentence is on p. 119: "If P is on the egg, then just the odd multiples of P give positive solutions." |
| `review/audit/sources/schinzel_serdica1996.txt` | Schinzel, Serdica 22 (1996) (provided) | read in full (template for Theorem 3: infinitely many rational points in a neighbourhood of one point) |
| `review/audit/sources/pari_elliptic.html` | PARI/GP manual, elliptic curves (provided) | `ellrank`, `elltors`, `ellanalyticrank` entries read |
| `sources/pari_general_number_fields.html` | https://pari.math.u-bordeaux.fr/dochtml/html/General_number_fields.html | HTTP 200 but transfer truncated (curl error 18, ~60 kB missing). The retrieved part contains the `bnfinit` GRH paragraph ("The result is conditional on the GRH ... may be certified using bnfcertify"), which is all that was needed. |
| `sources/pari-2.17.2/src/basemath/ellrank.c` | https://pari.math.u-bordeaux.fr/pub/pari/OLD/2.17/pari-2.17.2.tar.gz | tarball transfer truncated (curl error 18) but `ellrank.c` extracted complete (2128 lines, ends with `ell2cover`; sha256 5fb22176…33d6cd). The tarball itself was deleted. First attempts `pub/pari/unix/pari-2.17.2.tar.gz` and `pub/pari/unix/OLD/2.17/…` returned 404; gitweb blob URLs returned 500. |

## Gaps (not chased)

- Beauville, C. R. Acad. Sci. Paris 294 (1982) (the pencil's row Γ⁰₀(6)): not fetched. The fibre types and the generic Mordell–Weil torsion were re-derived directly instead (check_algebra.py, check_groups.py).
- Shioda, Comment. Math. Univ. St. Pauli 39 (1990): not fetched. Only the Shioda–Tate formula (standard) is used.
- Oguiso–Shioda classification of Mordell–Weil lattices of rational elliptic surfaces: not fetched; would give "torsion exactly Z/6" over Q̄(λ) for fibre configuration I6 I3 I2 I1 without computation. Not needed for any graded item.
- The construction behind Theorem 5 (conic bundle, U, V, M = y^{1/8}) is not in the statement file and was not looked up (rules of the audit). See REVIEW.md, DI.10.
