# PDF-only check 2 (brief Part 4.2), 2026-10-09

A second independent checker was given only the built PDFs of the close-out sources (commit 977cbc6:
Paper A 45 pp., supplement 18 pp., Paper B 26 pp., arithmetic note 12 pp.) and VERDICT-A.md /
VERDICT-B.md. It had no sources, no change logs and no web. Its task was to confirm the fixes made in
response to [PDF-CHECK-1.md](PDF-CHECK-1.md) and to check the new Section 2.4 (variable curvature) of
Paper A.

**Provenance of this file.** The checker's report itself was not saved to the repository, and the
transcript of the session that ran it is not on this machine. This record is reconstructed from the
message and diff of commit 2e043ca, which applied the fixes, and from the "PDF-only check 2" rows of
`paper/jga/ROUND4-CHANGES.md` and `paper/eigen/ROUND4-CHANGES.md`. It therefore gives the findings and
their fixes, but not the checker's per-item table or its page references.

## Outcome

- Every close-out fix listed in PDF-CHECK-1.md ("Response") and in the "Close-out" sections of the two
  ROUND4-CHANGES.md files was confirmed in the PDFs.
- No mathematical error was found.
- In Paper A it found one gap in the sketch of a proof, two imprecise hypotheses and several notation
  clashes, all in Section 2.4. In Paper B it found two wording problems. All are fixed in 2e043ca.
- A2 (Paper A length, 45 pp. against about 30) remains unresolved, as in check 1.

## Exact recomputations by the checker (all agree with the PDFs)

Paper A, Section 2.4:

- m Π_i(m) for i ≤ 6;
- the K³ part of b_3, against p_3/m;
- β_{2,3} = 12K² − 2ΔK and β_{3,4} = 120K³ − 42KΔK + Δ²K;
- the c_2 identity, c_2 = χ/6 + Σ_i (m_i² − 1)/(12 m_i);
- both hypotheses of Prop. 2.12(iii) for O(2,8,8) and O(3,3,12).

## Paper A: findings and fixes

| # | finding | fix in 2e043ca |
|---|---|---|
| 1 | The sketch of Prop. 2.12(ii) did not match the audited proof. | The sketch now follows the proof: bumps of fixed amplitude, exact ε^{-2l} scaling, a generalised Vandermonde Jacobian, bumps on both orbifolds, and Σ_s shrinking. Both orbifolds first get metrics of curvature K_0 near the cone points, with two flat discs. |
| 2 | Prop. 2.12(i) claimed everything deduced from Lemma 3.3 for the whole class. | Lemma 3.3 holds verbatim in the class; its consequences are claimed only when χ < 0, with Area read as −2πχ. |
| 3 | Ω_{−1} was used in Prop. 2.12(i) but never defined. | Ω_l is now defined for l ≥ −1, with Ω_{−1} = c_1. |
| 4 | Prop. 2.11(ii) gave the expansion of β_{l,l+1} for every l, but the expansion is valid only for l ≥ 2. The proposition also did not say that it assumes the hypothesis of (i). | The expansion is now stated for l ≥ 2, with its omitted terms described (degree at least 2 and not powers of K), and β_{1,2} = 2K is stated separately. The item now begins "Under the hypothesis of (i)". |
| 5 | Notation in Section 2.4 clashed with notation used elsewhere in the paper. The old symbols were the rotation Φ, the fixed-point coefficient ϑ_l(Φ), the angle φ with C_φ, and the bump e^{2λψ}. | Rotation R with angle ϑ; fixed-point coefficient 𝓑_l(R); 2 sin(ϑ/2) written out; bump h with amplitude θ. |
| 6 | The odd powers of cot(ϑ/2) in the fixed-point term were not accounted for. | Accounted for in the proof of Prop. 2.11(i). |
| 7 | The notation table did not list the new Section 2.4 symbols. | Table 1 lists Ω_l, Π_i and β_{l,i}, with Section 2.4. |
| 8 | The closing paragraph of Section 2.4 said the cone orders enter "in exactly the same way" in variable curvature. | It now says they "still enter through one new odd power per order". |
| 9 | Problem 5(c) stated the hypotheses of Prop. 2.12(iii) only in part. | It now gives all of them: the same genus, and equal Σ_i(1 − 1/m_i) > 1, hence equal χ. |

## Paper B: findings and fixes

| # | finding | fix in 2e043ca |
|---|---|---|
| 1 | The explanation of ε = 1.8626 in Table 3 said "the smaller of the two triangle orbifolds", which is ambiguous. | It now reads "the smaller systole of the two triangle orbifolds". |
| 2 | §8.2 repeated the pinching sentences of §1 and their citations. | §8.2 now refers back to §1 ("as recalled in Section 1"). The citations to Hejhal, Ji and Wolpert are dropped there. |
| 3 | §8.2 repeated the ε^{-3} log(1/ε) remark of §5. | The repetition was removed. |

## After the check

Commit bddc88b records the build of these fixes (BUILD.md: 45 + 18 pp., 0 errors, 0 undefined references,
0 overfull boxes above 1 pt). The later partial cut of Paper A (Appendix C and the computational detail of
Section 4 moved to the supplement) was made after this check and was not checked by it.
