<!-- FIX-CHECK B (round 7): returned text saved verbatim; the reviewer could not write files -->

I checked VERDICT-B against the 36-page PDF, rendering pages at 110 dpi (Figures 1 and 3 also at 300 dpi). Almost every CONFIRMED resolution is in the paper and correct. Four prose errors remain, and Corollary 6.3, Corollary 8.5, Theorem 7.1 and the systole certification are all sound.

Four things the authors should fix:
1. **Wrong column pointer.** Item (i) on p. 18 and §7.2 on p. 21 both say "(the last column of Table 6)". On the rendered p. 23 the last column is "N, Thm 6.2"; the new "(C1), Sig(A,M)" column is second to last.
2. **Count convention broken.** §7.2 on p. 21 says "(C1) holds with 24 and 36 eigenvalues". Under the paper's own convention (§7.1, Table 6 caption) these are values of N, so the test uses 25 and 37 eigenvalues.
3. **Corollary 6.3 lead-in mismatch.** The p. 14 lead-in says the corollary assumes the two consequences "Θ∗ ≤ 1/8 and Λt∗ ≥ 1". The corollary actually assumes 0 < Θ ≤ 8, which is the weaker condition the proof needs (Hyp ≤ Θ/8 ≤ 1), so the mathematics is fine and only the sentence is off.
4. **One factor in §7.2 (p. 22).** "10^10 to 2×10^11 for the family at M = 12" does not match the Sig(A,M) column the paragraph compares against: 7.4e12/842 to 7.4e12/59 gives about 9×10^9 to 1.3×10^11. The "2×10^11" matches the C∗ column (44) instead. The other factors in that paragraph check out.

Things I recomputed:
- **Table 3:** all eight t₁ values match, and the minimum is attained at k = k∗ in every row, as Remark 6.4(a) says.
- **Lemma 4.5 / Table 2:** C∗ ranges from 4×10^5 to 7.1×10^10. πe^{3D}/A ranges from 10^196.5 to 10^29325.4; the paper rounds the top to "10^29326", which is fine.
- **Table 2:** the D values match.
- **Fig. 1:** the 25/12 slope (P₃ difference 750 × a₁ = 1/360) is right. In the shaded window, half the nearest gap (about 0.021) exceeds the bound sum (about 0.013).
- **§7.2 and Fig. 2 numbers:** "6 to 12", "at most 1.7", "1.9–2.8×10^8", "56 to 2.7×10^11", and the 7.7 and 8.4 checked against Table 5 all match.

I could not check the Corollary 6.3 values themselves (244, 283, 139, 2605, 7415, 3.9×10^5), since they need the quadrature. They are consistent with Table 3 and with an order-of-magnitude estimate from the N, Λ and Z♯ formulas.

## MAJOR items

| id | page / passage | verdict | reason |
|---|---|---|---|
| B1 | p. 26, Cor. 8.5: "(⌊Λ_N/δ⌋+1)^{N−1} ≥ M−6 … N grows at least like log M/log log M"; abstract p. 2; §1 p. 5 "it gives a lower bound for N in terms of M (Corollary 8.5)"; p. 3 "What effectivity adds" | DONE | The pigeonhole and δ/2 argument is correct, M−6 counts orders 7..M, and the log M/log log M asymptotic follows. |
| B2 | p. 14 Cor. 6.3 with proof and numbers; abstract p. 1–2 ("10² to 10⁴ … computed, not certified"); p. 3 "They are enormous (Table 3) because…"; p. 22 "comes not from the data but from Lemma 6.1"; Remark 6.4(a) p. 16 | DONE | Statement and proof are sound and the numbers are labelled "computed, not certified". Only flaws are issues 3 and 4 above. |
| B3 | p. 18 item (iv): "The test presupposes a complete list … 19 of these 24 … the protocol … rejects all 24 lists, and accepts the true signature on the ten"; abstract end p. 2; inertia/enclosures "We have not done this" p. 19 | DONE | Item (iv) does not say which count (Δ or C∗) the 19/24 figure uses (see b20). |
| B4 | p. 17 Thm 7.1: E_N contains t Σ ϵⱼ e^{−t max(λ̃ⱼ−ϵⱼ,0)}, proof uses min(λⱼ,λ̃ⱼ) ≥ max(λ̃ⱼ−ϵⱼ,0); O and S "of area at most A"; Thm 1.2 p. 3 likewise; item (i) p. 18; (v) "unchanged for r ≤ 10⁻³, and for r = 10⁻² they become 21 and 43"; new Table 6 column p. 23 | DONE (item (i) has the wrong column pointer, issue 1) | The perturbation term is sharp and valid, and the new column is present. |
| B5 | p. 14–15 "In the companion paper, heat invariants are recovered … [31, Lemma B.3]; Theorem 6.2 replaces values of the trace by eigenvalues…"; Table 5 caption "whose supplement gives their convergence data [31]"; App. A and §1 justify self-containment | DONE | The caption does not name "Table S5" (the verdict's locator). |
| B6 | p. 2 "the heat invariants alone already determine the cone orders [2, Cor. 4.21]" | DONE as applied (the issue table's version is PARTIAL) | Cited in §1 only. The issue table also asked for it before Theorem 3.2, with Theorem 3.2 and Lemma 3.3 called the quantitative additions; that is not done. |
| B7 | p. 5 "[15, Cor. 5.5] … [15, Thm 5.7] … [17, p. 579], [15, Ex. 5.8], and Judge … [18]"; p. 26–27 condition (a) for m ≥ 13 with "1/(2 sin(π/m)) ≥ m/2π ≥ 1+m/4π", condition (b) granted ("Granting this…"); novelty "What Theorem 1.3 adds…" | DONE | Condition (a) checks (m ≥ 4π). I could not verify the Judge content from here. |
| B8 | p. 3 "Dirichlet energy by a factor in [K⁻²,K²] and the L² norm … [K⁻²,K²] … each λⱼ by a factor in [K⁻⁴,K⁴]"; "a positive minimum, larger than 2δ" | DONE | In dimension 2 the energy factor is s_max/s_min ≤ K², so these factors are correct. |
| B9 | p. 20–21 "The same enumeration in interval arithmetic (60 digits …) certifies all ten values of ℓ"; Table 4 caption "(certified in interval arithmetic)"; item (ii) p. 18; §1 p. 3; the limitation list no longer mentions systoles | DONE | The Data availability paragraph (p. 29) lists every script but not the new certification program or the computed-gap program. |
| B10 | p. 28 "Proposition 8.6 is the classical collar argument … (see Buser's book [27]), included here for its explicit constants"; the intermediate-value remark is gone; Problem 1 discussion with (0;3,3,3,3), (1;3), (0;2,2,6,6) and the (1;3) non-separating observation | DONE | The areas and the Gauss–Bonnet step check out. The (0;2,8,8)/(0;3,3,12) pair is not used here, which the applied resolution does not require. |

## Minor items marked done or fix

| id | page / passage | verdict | reason |
|---|---|---|---|
| b2 | p. 11 "we expect the factors 1/M … not to be intrinsic, but do not prove it" | DONE | |
| b4 | p. 28 "ℓ(O_{k,b}) ≤ 4 min(a,b); Section 7 uses b ≤ a" | DONE | ϑ ≥ 0 gives a ≥ b. |
| b5 | p. 26 Fig. 3 text "thin dashed … runs close to the curve of λ_{j+1}" | DONE | The rendering shows thin dashed bounds, so text and figure agree (the verdict's "dotted" wording was replaced by the accurate "dashed"). |
| b6 | p. 12 "between about 10^196 and 10^29326 with D of Table 2" | DONE | The values are right, but only 4 of the 8 classes have their D in Table 2. |
| b7 | p. 23 "generates a non-elementary group, so this is the classical inequality" | DONE | |
| b8 | p. 20 "conjugate to γ in W … mirror class"; "d(x₀,wx₀) ≤ L+3r" | DONE | |
| b11 | p. 11 "sin(πj/k) ≥ sin(π/k) ≥ sin(π/M)" | DONE | |
| b12 | p. 4 (Proctor–Stanhope hypotheses fixed by the spectrum); p. 12 role of Thm 4.4 | DONE | "used for the finiteness statement of Section 1" (p. 12) is vague, because §1's compactness argument does not use Theorem 4.4. |
| b13 | Table 2 caption "against computed diameters"; Table 4 caption "proved diameter bound … and the computed diameter" | DONE | |
| b16 | p. 13 non-hyperbolic cases listed; p. 2 "area in (0, A]" | DONE | |
| b17 | p. 7 "classical, with the extension to the heat function of [31, Lemma B.1]" | DONE | |
| b19 | Table 6 caption states both conventions; §7.1 p. 21 | PARTIAL | Issue 2 above: p. 21 says "(C1) holds with 24 and 36 eigenvalues". |
| b21 | p. 16 "for N = 21, at the times 0.050 and 0.056 of the figure's grid of 61 … (C2) holds already with N = 20 (Table 6)" | DONE | Matches the rendered shading and Table 6. |
| b22 | p. 22 "1.9 to 2.8×10⁸"; p. 21 "7.7 and 8.4" | DONE | Both verified from Tables 5 and 6. |
| b23 | p. 21 "240 log-spaced values of s/t in [10⁻⁸,1]"; "floating-point summation is not included"; quadrature check 2.1×10⁻¹⁵ | DONE | |
| b27 | p. 3 "for the family with … M = 3 and M = 12 and for the triangle orbifolds with M = 12" | DONE | |
| b28 | p. 22 "criterion (C1) with Δ = 2 diam P (diamonds; the counts with C∗ and against Sig(A,M) are in Table 6)"; N_obs "in the data files" | DONE | Fig. 2 renders as described. |
| b29 | Table 4: 4.672, 5.821 | DONE | Rounded up. |
| b30 | Table 5 rendered p. 22 | DONE | No collision. The header has no labels for the ϵⱼ and N/D columns, but the caption explains them. |
| b34 | p. 29 "Consent for publication", "Materials availability" | DONE | The MSC comma spacing remains (class-file rendering, as stated). |
| b20 (regenerate (v), which count in (iv)) | p. 18 | PARTIAL | (v) is regenerated. (iv) still does not say which count, and the C∗ figure is not given. |
| b14 (with B2) | Remark 6.4(a) "attained at k = k∗" | DONE | Table 3 itself does not note the binding k; the remark covers it, and my recomputation confirms it. |

## Other findings

- **(a) Wrong or overstated statements:** issues 1, 3 and 4 above. A minor one: the §7.2 factor "283 vs 24" compares the triangle class at ε = 1.8626 with O(2,8,8), whose own ℓ is 2.2568. The protocol claim in (iv) and the Corollary 6.3 hedging are appropriately stated.
- **(b) Broken cross-references:** there is no "??" anywhere. The only bad pointer is the textual "last column of Table 6" (twice).
- **(c) Comments on length or suggested cuts:** none.
- **(d) AI tools, internal paths, review history:** none. Only the allowed placeholders appear (Zenodo DOI, two preprint identifiers, author contributions, the AI-use statement). The deposit script names in Data availability are deposit file names, not internal paths.
- **Data availability (p. 29):** it lists every program except the two new ones, the computed-gap program (Corollary 6.3) and the systole certification program (Table 4). Worth adding.

Everything is in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/fixcheck-B/scratch/`: the extracted text is `txt/B.txt` and the rendered pages are `img/p-01.png` to `img/p-36.png`.
