# fetches: group `stability` (G5-bis)

No network retrieval was made by this review. The bundle declares no external input. The only third-party text
read is a file that `review/audit-2/fetch_sources.sh` had already fetched. It was used for an optional
cross-check of the heat coefficients H_ν, which the relative-precision column and ε_cert depend on.

| source | URL (as fetched by the lead's script) | HTTP | local file | used for |
|---|---|---|---|---|
| Uçar, PhD thesis, arXiv:1711.03405 | https://arxiv.org/abs/1711.03405 (PDF, text extracted) | not re-fetched (pre-fetched file) | `review/audit-2/sources/ucar_1711.03405.txt` (sha256 `11f231b6…c9`; the PDF's sha256 `b6da48a7…74` is in `sources/SHA256SUMS`) | (4.25) c^S_ℓ(π/k), text lines 11580–11620; (4.33)/(4.34) cone contribution C, lines 11940–11960; Theorem 4.20 (i) (4.35) a_ν(O), lines 11990–12005; Theorem 4.20 (ii), lines 12006–12010. `check_setup.py` §3 rebuilds H_ν from these formulas, with κ = −1 and genus 0, and checks H = F·I + h₀ exactly, F being the inverse of the ST.2 table of L⁻¹ |

## Instrument gaps

- **Theorem B (the matrix M(I) and vector b(I)) is not in the bundle.** I reconstructed it from the Δ_M and J
  descriptions of Prop. 6.10, and verified the reconstruction exactly against Lemma S2.2 (B = S·M) and Lemma
  S2.1 (det M) on 41 multisets. This is a reconstruction, not a reading of the printed Theorem B. See
  REVIEW.md, "Reconstruction of Theorem B".
- **"Proposition 6.2"** (SB.3) is a cross-reference into the manuscript, which I may not open. I assumed it is
  Proposition S5 (SB.1). I could not verify this.
- **Lemma S3 and Theorem S2** (SB.0b) are used only to recompute δ_thm, as Theorem S4's minimum of the
  Theorem S3 hypotheses. Their proofs were audited in G5 and are not re-derived here. Every printed δ_thm is
  also certified independently by Prop. S5 test (i) and test (ii), so the δ_thm column does not rest on them.
