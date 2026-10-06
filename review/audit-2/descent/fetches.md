# Fetches: group `descent`

No new network retrieval was made by this reviewer. Sources used:

| source | URL | HTTP | file | used for |
|---|---|---|---|---|
| Cremona, Algorithms for Modular Elliptic Curves, 2nd ed., ch. III | https://johncremona.github.io/book/fulltext/chapter3.pdf (fetched by `review/audit-2/fetch_sources.sh`) | (pre-fetched; checksum verified) | `review/audit-2/sources/cremona_ch3.txt`, `.pdf` | §3.1 (b-invariants, Δ), §3.3 p. 69-70 (Prop. 3.3.1, 3.3.2, Δ = −16Δ₀, injectivity of reduction on torsion for odd p ∤ 2Δ), §3.6 p. 84-86 (Method 1, H(d1,c,d2), n1, n2, (3.6.2), exact sequences, real-place criterion, local solubility automatic for p ∤ 2dd′) |

SHA-256 checked against `review/audit-2/sources/SHA256SUMS`:
`cremona_ch3.pdf` c4843b80…9c26 (match), `cremona_ch3.txt` 2a56f875…f87b (match).

Not reachable / not used (instrument gaps):

- PARI/GP manual (ellrank, "r_2 = C − T − s unconditional"): not among this group's sources; not consulted. Not needed for the verdict.
- PARI/GP, Sage: not installed locally; no PARI cross-check run.
- Standard local formula |E(Q_p)/2E(Q_p)| = |E(Q_p)[2]|·|2|_p^{-1} (used only in the independent full 2-Selmer cross-check) and the group law on a plane cubic with arbitrary base point: not in the fetched text; not fetched (textbook facts, e.g. Silverman). Both are checked numerically in this folder.
