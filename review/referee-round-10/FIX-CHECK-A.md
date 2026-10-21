<!-- FIX-CHECK-A (round 10), returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

FIX-CHECK-A (round 10)

Inputs: build/manuscript.pdf (74 pp., titled "How many heat invariants determine a hyperbolic orbifold?"), build/supplement.pdf (18 pp.), VERDICT-A.md and the five A-*/REPORT.md. I rendered pages with pdftoppm and read them before reporting any typographical problem. My scripts are in review/referee-round-10/fixcheck-A/code/ (c1–c4.py) and the renders in fixcheck-A/img/. Page numbers are the printed numbers, which match the PDF pages. "S-p." means a supplement page.

**Overall:** all eleven MAJOR items are resolved in the manuscript, and so are nearly all claimed minors. I found no mathematical regression. One fix was not carried over: the supplement's title page still has the old title. One fix produced a garbled sentence (p. 11).

## MAJOR items

- **A1 – RESOLVED (pp. 6–8).**
  - New paragraphs "What is analytic" and "What is the algebra of odd power sums" separate the analytic results (Prop. 2.8/B.2, B.3, B.4, B.5, Thm 1.6(i) with Lemmas E.1/E.2) from the counting results.
  - Variable curvature is promoted to a main result, Theorem 1.6 (= Props 2.14, 2.17).
  - Cor. 3.12 is now Theorem 1.1(iii).
- **A2 – PARTLY RESOLVED.**
  - Manuscript: retitled. The abstract (pp. 1–2) gives question, theorems, then one caveat. It says "is equivalent to" for growth and confines the isolation of the k ≥ 2 multiples to triangle orbifolds.
  - **Not carried over:** the supplement title page (S-p. 1) still reads "Online Resource 1 … for 'How much of a hyperbolic orbifold does heat hear?'". See new issue N1.
- **A3 – RESOLVED.**
  - p. 49: Section 6 opens as the stability of the algebraic recovery map, with the end-to-end minimal-pair numbers.
  - p. 61: Prop. S3.1 is now Proposition C.5, stated and proved in Appendix C.
  - S-p. 7 (S3) points to it. No "S3.1" reference is left in either PDF.
  - Recomputed the p. 49 numbers: δcert reached for τ ≤ 1.54e−2; smallest time 1.2e−4, or 6.0e−5 at τ/2; η ≤ 1.32e−8. All match.
- **A4 – RESOLVED.**
  - pp. 7–8: status of the companion and the note (preprints submitted at the same time), exactly what is shared, and which paper is primary.
  - p. 8 and p. 10: Thm 5.11 is proved here and the note cites it.
  - p. 47: the note's results are marked as used nowhere.
- **A5 – RESOLVED.**
  - The abstract (p. 2), p. 6 and p. 17 state the mechanism: an exactly flat cone point contributes to c2 only.
  - p. 18: Conjecture 2.13 is headed "used nowhere", and the text says Props 2.14 and 2.17 do not depend on it (also p. 7).
- **A6 – RESOLVED.**
  - p. 17: the per-point identification uses [2, Thm 4.8] and [20, Thm 4.20], and the locality-free claim is restricted to Sections 3–6.
  - The same restriction appears in Appendix B (p. 55) and in the proof of 2.17(i) (p. 21).
- **A7 – RESOLVED (pp. 65–68).**
  - Lemma E.2 is new, with proof:
    - (i) ∂εT(0,t) = 2t∫ψ q_t(x,Rx)dx + O(t^∞);
    - (ii) ∂ε²T(0,t) = D2(t) + O(t^∞), with χ = 1 on a neighbourhood of supp ψ.
  - It is used in the proofs of Prop. 2.14 (p. 19) and 2.17(ii) (p. 21).
  - I checked D2 against the second-order Dyson term (factors 4t/(2π)² and 4t²/(2π)⁴) and the step "θ²/2 ∂θ²T = θ²/2 D2" (p. 21, rendered). I also checked the Gaussian integral −l·l!·4^l t^{l−1}C^{−2l−2}, hence λl = 2Π_{l+1}/(l−1)!, and the sign of Step 6. All consistent.
- **A8 – RESOLVED.**
  - Cited: [47] Branson–Gilkey–Ørsted, [48] Vassilevich (form factors), [72] Gilkey's monograph, [73] Berline–Getzler–Vergne.
  - Remark 2.18 (pp. 22–23) presents ωn as a re-derivation and derives the same closed form from the BGØ mechanism. I checked that ω_{l+1} = (−1)^{l+1} l(l+1)(l+1)!/(2l+3)! agrees, and that ω2 = 1/30 matches Ω1 = (1/60π)∫K².
  - p. 8: the novelty list is reworded; B.2 is called elementary and is not listed first.
  - p. 62 (Appendix E intro): says what goes beyond Gilkey and BGV.
- **A9 – RESOLVED.**
  - p. 13: Remark 2.6 is marked as taken from [3], not proved here, and not used by any result.
  - p. 7 and p. 37: the diameter-free form is not claimed; only the diameter constant of Prop. 4.2(a) is listed as new (p. 8).
  - pp. 58–59: Remark B.6 marks the systole bounds as taken from [3] and "not proved here", and says no theorem uses the remark. It states the numbers for three times are the same for every ℓ0 ≥ 0.01, and those for eight times for every ℓ0 ≥ 1.1. This is narrower than the verdict's "any ℓ0 ≥ 0.01", but accurate: Lemma B.5's time range excludes tiny ℓ0 at τ ≈ 1e−2.
  - Recomputed with the new ℓ0 = 1.8626 and D = 4.897 (two-time-points rows rounded; all match the printed values):

    | quantity | recomputed |
    |---|---|
    | uniform bound | 4858τ |
    | row bound | 1139τ |
    | τ for δthm, uniform / rows (three times) | 7.82e−11 / 3.34e−10 |
    | η at τ = 1e−11, uniform / rows | 2.07e−19 / 4.61e−19 |
    | N = 8: τ for δthm, η at τ/2 | 3.60e−3, 5.00e−13 |
    | N = 8: τ for δcert, η at τ/2 | 1.54e−2, 1.32e−8 |

    With ℓ0 = 1.1 the N = 8 δcert row becomes 1.46e−2 and 1.26e−8, which still round to the printed 1.5e−2 and 1.3e−8.
  - My word enumeration gives systoles 1.862604 (3,3,12) and 2.256768 (2,8,8), so 1.8626 is a valid lower bound, by about 4e−6.
  - The diameter argument also checks: longest sides arccosh(cot²π/8) = 2.4485 and 2.158.
- **A10 – RESOLVED (p. 4, p. 32).**
  - I fetched Croot–Mao–Yip §1 (arXiv 2609.05061v1) and checked the paragraph against it. It matches on all of these points:
    - P(k,2) ≥ k+1;
    - the pigeonhole bound P(k,m) ≤ k(k+1)/2 + 1;
    - the pigeonhole principle does not readily bound W(k,2);
    - Hua and Wright gave elementary bounds on W(k,m);
    - Wooley's W(k,m) ≤ k(k+1)/2 + 1;
    - P(k,2) = k+1 is known for 2 ≤ k ≤ 9 and k = 11.
  - The Wright/Wooley inconsistency is gone and Hua is cited [51, 52].
  - [5] (Borwein–Ingalls) is no longer quoted verbatim, and "this problem and the next" is fixed.
  - p. 5 is rephrased as "which power, if any", given c√A ≤ f(A) ≤ A/π + 4.
  - Not verifiable from here: "Melzak … as reported in [5, p. 7]".
- **A11 – RESOLVED.** p. 7, p. 8 and p. 41 name Cor. 5.3 (four invariants against all of Sig) as the main geometric result of §5. p. 41 and p. 46 mark Thm 5.7 for general p and Prop. D.1 as structural.

## Claimed MINOR items

**A-a (5 resolved)**
- m1 RESOLVED: Thm 3.18(d), (e) now hold both equivalences, with a separate proof (pp. 33–34). I checked the proof.
- m2 RESOLVED: abstract, Thm 1.4(iii) (p. 5), remark after Thm 5.11 (p. 49).
- m3 RESOLVED: Suleymanova [28], pp. 9 and 18.
- m5 RESOLVED: "N nondecreasing" with its reason (p. 4).
- m7 RESOLVED: caveat in the statements of Thm 6.2 (p. 50) and Thm 1.3(i) (p. 5).

**A-b (11 resolved)**
- m1 RESOLVED: the sign convention, Schueth's included (p. 17).
- m3 RESOLVED: χ is part of the hypothesis (p. 20).
- m4 RESOLVED: Remark 2.15 sentence (p. 19).
- m5 RESOLVED: C_i t^{−3−i}e^{−c/t}, and the outer density in the Leibniz count (pp. 63–64).
- m6 RESOLVED: second fixed point; isometry used only in the last step (pp. 64–65).
- m7 RESOLVED: bounds valid for both orbifolds, ℓ0 = 1.8626 (p. 58).
- m8 RESOLVED: |ϵr| ≤ 1 < π/2 (p. 55).
- m10 RESOLVED: weight-6 invariant count, valid for every germ (p. 20).
- m11 RESOLVED: 1.0775e−3 against 1.0417e−3 (p. 14).
- P3 RESOLVED (p. 18).
- P4 RESOLVED (p. 19).

**A-c (8 resolved, 1 partly)**
- m2 RESOLVED: pp. 32 and 54.
- m3 RESOLVED: the clause now reads "if g ≠ g′ …", with "(If g = g′, then ι = 0)" (p. 31).
- m4 RESOLVED: p. 30.
- m5 RESOLVED: p. 36.
- m7 RESOLVED: p = 2, 4, 5, 6 cases and steps of 2 (p. 62).
- m9 RESOLVED: the exact versus estimated sentence is in §4 itself, and "to the resolution of the sampled times" (pp. 40–41).
- P1 RESOLVED: |b_l(12)| for l ≤ 6 (p. 40). Recomputed 0.993, 5.13, 101.2, 3621, 1.840e5, 1.206e7, 9.666e8; all match.
- P5 PARTLY RESOLVED: the explanation is in the running text (p. 35), but the Fig. 3 caption (p. 36) still does not say "drawn at L+1".

**A-d (8 resolved, 2 partly)**
- m1 RESOLVED: "area at most π/2" (p. 46).
- m2 RESOLVED.
- m3 RESOLVED: Lemma 5.5 (sign of the gap) now precedes Lemma 5.6 (p. 44).
- m4 RESOLVED: the proof of Thm 5.8 uses p ≤ 6 only, with x*(p) − 18 = 3(p−2)(p−3)/(p−1) (p. 45).
- m5 RESOLVED (p. 48). I checked that [u,r,s,t] = [2, −132, 1, 4] maps E exactly to [1, −1, 1, −3002, 63929], and the label is 90c6.
- m6 RESOLVED: Silverman VII.3.1(b) [67] and Cremona [68] (p. 48).
- m7 PARTLY RESOLVED: the clarifications (e = 0 is covered by 5 | e; n1 includes torsion) are there (p. 68). The letters are not renamed, which the verdict excluded. I re-checked the mod-9 step: 5w² − w + 2 ≡ 6 for w = 1, 4, 7.
- m8 RESOLVED by explanation: the text says the axis label denotes dist (p. 51).
- m11 RESOLVED: 2.08328 (S-p. 12).
- m12 RESOLVED (p. 43). Recomputed exactly 72,042 candidates {2,2,c,d} with d ≤ 1000 and 59,646 with b ≥ 3 and d ≤ 20000 under (P1−1)(R−1) ≥ 9.
- P3 PARTLY RESOLVED: the base point is now o, but E still names both the elliptic curve (p. 48) and the elliptic term E(t) (Thm 2.3).
- P5 RESOLVED: "equal area π/4 (equivalently equal R)" (p. 42).

**A-e (13 resolved, 1 partly)**
- m1 RESOLVED in substance: Paley–Wiener, R_c^l, Def. 3.1/Thm 3.2 (pp. 11–12). The p. 11 edit left a broken sentence (N2).
- m2 RESOLVED: p. 7.
- m3 RESOLVED: sign line for (11) (pp. 23–24). The SIAM DOI replaces the arXiv id.
- m4 RESOLVED: "a hypothesis, concerning certain strata" (p. 16).
- m5 RESOLVED: pp. 4, 9, 32, 35.
- m6 RESOLVED: p. 5.
- m7 RESOLVED: Table 2 caption (p. 35).
- m8 RESOLVED: p. 33.
- m9 RESOLVED: p. 5.
- m11 RESOLVED: pp. 64–65.
- P3 PARTLY RESOLVED: same as A-c P5.
- P5: nothing to do.
- P8 RESOLVED: derivation in Remark 2.10 (p. 15).

## Checks for things the fixes might have broken

- **Cross-references:** none broken, and there is no "??" in either PDF.
  - All internal link destinations resolve: 213 used out of 340 defined in the manuscript, 24 of 45 in the supplement.
  - There are no GoToR or cross-document links, so no \pref to the supplement can be broken; all supplement references are plain text.
  - After the renumbering, the §5 references are consistent: Lemmas 5.5–5.6, Thms 5.7–5.11 (5.10 least area, 5.11 isolation). This holds on pp. 5, 8, 10, 41–49, 62, 68 and S-pp. 1, 7, 17.
- **Abstract, introduction and body agree.**
  - Theorem 1.2(ii) matches 3.18(d)–(e) and the abstract.
  - Theorem 1.4(iii) matches Thm 5.11 and the remark on p. 49.
  - Theorem 1.6(ii) matches Prop. 2.17(ii). I checked the examples: c2 = 2/3 for both, χ = −2 and 0.
  - The Remark B.6 times agree in all three places: below 10⁻³ (p. 3, p. 6) and 1.5e−3 (p. 49, p. 59).
- **Parametric expansion:** no conditional wording is left. Lemmas E.1 and E.2 are stated as proved (pp. 6–7, 19, 62).
- **Text saying a used result is unproved:** none. The only "not proved here" statements are Remark 2.6 and the Remark B.6 systole bounds, and both are explicitly not used by any result. Everything else labelled "not proved" is numerics (S4–S6).

## New problems introduced by the fixes

- **N1 (A2 not carried over).** Supplement title page (S-p. 1) still has the old title "How much of a hyperbolic orbifold does heat hear?". The fix is to rebuild the supplement with the new title.
- **N2 (p. 11, from the A-e m1 edit).** The sentence before (2) is broken: "It carries a hyperbolic metric exactly when χ(O) < 0, and then [40, …]; Dryden and Strohmaier do not write (2) out, but it follows from … [9]", followed directly by the display (2). "and then" has lost its object. Put the Dryden–Strohmaier remark after (2).
- **N3 (pp. 58–59, minor).** Remark B.6 says δcert is "certified in the supplement (Table S4)". The certificate is now Proposition C.5 in Appendix C; Table S4 only lists its values.
- **N4 (p. 9, minor punctuation).** "…from c2 alone [2, Thms 5.14–5.15], for isospectral compact orientable orbifolds, finiteness…" needs a semicolon after the citation.

## Not claimed in the verdict but still wrong

- A-d m9 is still wrong at S-p. 11. The printed numbers give deviations of 0.43 and 0.52 error bars (|2.0833320 − 25/12|/3.1e−6 and |−73.9551 + 1775/24|/0.0062). The text still says "0.42 and 0.53".
- A-d m10 (S-p. 13) is unchanged: the "annulus whose double is a torus" argument is still there.

I did not comment on length. The marked placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) are treated as known.

## Follow-up (main session)

- **N1:** the supplement is rebuilt with the new title. Page 1 now reads "How many heat invariants determine a hyperbolic orbifold?".
- **N2:** the sentence about Dryden and Strohmaier now follows display (2).
- **N3:** Remark B.6 says δ_cert is certified by Proposition C.5, with its values in Table S4.
- **N4:** a semicolon now follows the citation of DGGW Theorems 5.14–5.15.
- **A-d m9:** the deviations now read 0.43 and 0.52.
- **A-d m10:** the annulus argument in S6 is left as it is. It was not claimed in the verdict, and it is not wrong, only longer than the standard fact.
- **A-c P5 / A-e P3:** the Fig. 3 caption is not changed. The explanation stays in the running text, because captions are limited to two short sentences.
- **Blind check:** the round-10 blind check of the Paper A changes (`blind-check-A/REPORT.md`) found all six items correct. Its ten wording points were applied before this fix check.
- **Builds:** manuscript 74 pp., supplement 18 pp. Both have zero undefined references and no overfull boxes.
