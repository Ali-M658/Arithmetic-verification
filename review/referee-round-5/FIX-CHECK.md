<!-- The report below is verbatim the final message of an independent checker subagent that was given only the built PDFs (Paper A sha256 adba31a0..., supplement 77b067ad..., Paper B 44c1be83...) and VERDICT-A.md, VERDICT-B.md; it could not write files. The section 'After the check', at the end, was written by the main session. -->
# FIX-CHECK: referee round 5

## Summary

All four blocking items (A1, A2, A3, B1) are resolved in the revised PDFs.

- **A1.** The abstract now claims exactly the lower-bound equivalence of Theorem 1.1(ii).
- **A2.** The authors took the "full proof" route. Propositions 2.11 and 2.13 (the old 2.12) now carry proofs instead of sketches. "(iii) for every l" is proved analytically by Duhamel's formula, the machine checks are in a separate Remark 2.12, and the supplement's S8 documents the computations.
- **A3.** The heat-trace-to-invariants claim has been withdrawn in all three passages, and Corollary 6.5 now demands a *proved* δ₁.
- **B1.** All six overstatements in §7.1 are corrected. The double-window rerun has now been run, and the two papers report it consistently: same cut λ ≈ 2.0×10⁴, no window miss, largest relative difference 1.4×10⁻¹⁴.

Most MAJOR and MINOR items are resolved. The remaining gaps are mostly in Paper B: literature and decidability (B3), the consistency check (B5), notation (B22), figure fonts (B23), and several partial minors.

The revision also introduces a few new problems. Two are mathematical slips in Paper B:
- a false "attains values below any positive bound" sentence (p. 13);
- a sentence contradicted by Table 2 (p. 10).

There is also an awkward claim that "finitely many eigenvalues do not determine the area" (B p. 15), a duplicated citation in A (p. 24), and A↔supplement hyperlinks that point to local `build/…pdf` files.

There are no "??" cross-references in any of the three PDFs.

## Paper A

| item | disposition | evidence / page | what remains |
|---|---|---|---|
| **A1** (blocking) | RESOLVED | Abstract p. 1: "grows at least like the square root of the area and at most linearly, and at least like a power A^α of the area exactly when … N(k) = O(k^{1/α}); linear growth is equivalent to the open problem N(k) = O(k)". p. 5: "makes the questions of linear growth and of power lower bounds equivalent". Thm 1.1(ii), p. 3, matches, with "for all large A" explicit. **Claims exactly what is proved.** | — |
| **A2** (blocking) | RESOLVED (route a: proofs) | Prop. 2.11, pp. 12–13: headed "Proof" (Pole order / Radial reduction / (i)–(iii)). (iii) is now stated "for every m ≥ 2 and l ≥ 1" and proved by Duhamel's formula. Remark 2.12, p. 14: "rest on exact computer algebra … used nowhere else"; β_{l,l+1} computed for l ≤ 7; "(c) … checked by machine … for l ≤ 7". Prop. 2.13 (old 2.12), pp. 14–15: full proof, with the flat cylinder built in from the start and "L ≥ 2". [vⁿ]F, Π_i, K̄, J_u and "orbifold chart" are defined (p. 12). Supplement S8 "Variable curvature" (a)–(d), pp. 17–18, gives method, truncation and l-range. **The paper now claims what it supports.** | The pole-order step is still compressed ("Following Schueth's proof … to all orders"; "equality only through the Gaussian and the area element"), and so is the ω_n derivation ("completing the square … the displayed one"). Acceptable as proofs, but terse. The wording "one new odd power still enters" overstates slightly; see New problems. There is no explicit sentence that no main theorem depends on Props 2.11/2.13 (only Remark 2.12 says so). |
| **A3** (blocking) | RESOLVED (route b) | §6 opening, p. 36: "Obtaining them from a heat trace with a stated error needs more than (6): an a-priori upper bound on the largest order, bounds on the systole and the diameter, and an extrapolation … which this paper does not analyse". Cor. 6.5, p. 37: "δ₁ is a proved bound on the error of the data; an estimated δ₁ gives no conclusion". p. 38: "for data read off a heat trace this paper does not supply it … validated, not proved". End of App. B, p. 42: "that step is not analysed here". **Claims exactly what is supported.** | — |
| A4 | RESOLVED | [5] is now only the Doyle–Rossetti arXiv:1103.4372 (p. 5). Orbifold locality is [1] Donnelly 1979. "c … is twelve times the heat invariant c₂ [2, (5.13)]" (p. 6). Stanhope is cited for "finiteness … and a bound" (p. 6). Uçar "pp. 98–99" (p. 11). "[3, p. 10]" for Letac–Gloden, "[48, pp. 2064, 2069]", "(A.313), found by Chen in 2000, and (A.314)–(A.316), found by Wróblewski in 2009" (p. 25). "classical in substance [36, 49]", with Garbin–Jorgenson cited only for the form of the trace formula (p. 27). Openness is credited to [47] (p. 24). LMFDB [53] (p. 35). | Typo: "[47, §1], [47, §1]" (p. 24); see New problems. |
| A5 | RESOLVED | New paragraph "The analysis", p. 5: Prop. 2.7 / B.2 bracketing below (π/µ)², Lemma 2.5, Section 2.4, Thm 4.2. Eigenvalue consequence via the companion, p. 5. | Cover letter: not checkable. |
| A6 | RESOLVED | Thm 5.8 proof, p. 35: hand descent in S7, "isomorphic over Q to the curve 90.c3 of the LMFDB … [53]", PARI. Thm 6.2 points to S3.2–S3.4. | — |
| A7 | PARTLY RESOLVED | Contribution sentence, pp. 5–6: "…are in this paper only; the companion adds a diameter bound, eigenvalue counting and the cusp-like behaviour…". | Paper A has no sentence saying that the spectra, method text and deposit are shared with Paper B; only supplement S4 has "the companion paper [7] uses only these". Each paper carries its own Zenodo placeholder, so it is unclear whether there is one deposit. |
| A8 | RESOLVED | p. 2 text: "computed on the true hyperbolic triangle as half the sum of its Neumann and Dirichlet heat kernels"; "(a stylised, not an isometric, picture)"; "their extreme values are confined to a few pixels". Caption: "close to m only within about √t … a region too small to resolve at the tips". | — |
| A9 | RESOLVED | Fig. 3 caption, p. 26: "lower bounds Kmult ≥ L+1 from constructed pairs (filled diamonds…; open squares…)", "dashed lower bound … drawn from s = 4". | — |
| A10 | RESOLVED | Prop. 3.15 and proof, pp. 24–25: monotonicity of N and A_min, attainment of A_min, both directions of "f(A) = o(A) iff N(k)/k → ∞" written out. Thm 1.1(ii): "for all large A". | — |
| A11 | RESOLVED (as a sentence, not a lemma) | Def. 3.10, p. 22: "Every L-configuration has \|Z\| ≥ 2L+2: the proof of Theorem 3.4 uses only these conditions on X*." | It was not made a separate lemma; acceptable. |
| A12 | RESOLVED | Lemma 5.3(ii) proof, p. 32: "For p = 2 and S = 9, 10 the stratum 2 is empty and gap₂(S) = 1/12 > 0, so both sides of (ii) fail." Checked: both values are 1/12. | — |
| A13 | RESOLVED | Prop. 2.13(ii), p. 14: "Let L ≥ 2". | — |
| A14 | RESOLVED | Prop. 2.13, p. 14: "Theorems A, 3.4, 3.8 and 3.11 and Corollary 3.5 … hold in that class … under the additional hypothesis that the Ω_l agree". p. 15: "for every L, two signatures carry metrics with the same first L heat invariants whenever their c₂ agree". | — |
| A15 | RESOLVED | p. 13: evenness via reflections conjugating Φ to Φ⁻¹. p. 12: chart. p. 12: "α_k(−K)^k in place of α_k". p. 12: "normalised by u₀ = 1, u₁ = K/3". Real-m extension "algebraic only" (p. 10). | The evenness argument differs from the suggested j ↔ m−j pairing, but is valid. |
| A16 | RESOLVED | Prop. S2.2 proof, Suppl. p. 7: parity / (p−1) \| 6 argument for even S−p; monotonicity plus listed values for odd S−p. Not circular. | — |
| A17 | RESOLVED | Main text pp. 21 and 25 point to S8. S8 "Statements that rest on computer search alone", p. 17, lists the minimal areas 12π, 36π and the size-10 4-configuration search (entries ≤ 200), now precisely defined (p. 25). | — |
| A18 | RESOLVED | Table S4 caption, Suppl. p. 11: "δ_up is rounded up, the ratio … to the nearest unit of its last digit, and every other entry down". Checked: 1.1359 → 1.14. | — |
| A19 | RESOLVED | Fig. 2 (p. 19): "drawn without cancellation in the lower row of (a)". Fig. 4 (p. 28): "on a square-root axis". Fig. 5(b) (p. 30): "shaded, dotted edge". Fig. 7 (p. 34): dots/circles explained. Fig. 8 (p. 38): line styles and "2ⁿ sign patterns" (checked on the rendered page). | — |
| A20 | RESOLVED (spot-checked) | Sign "opposite to (ii)" in 3.8(iv) (p. 20). "s is an even integer" built into C (p. 20). Thm 3.13 "any prescribed g ≥ 2" (p. 23). "integers at least 2" (p. 18). "C ≥ N(1) = 2" (p. 40). A_min attained (p. 24). Thm 6.2 "closed formulas except for one matrix norm" (p. 36). (0;5,5,5)/(0;2,2,2,10) example (p. 31). Δ defined at (1). Asymptotics of b_l justified (p. 29). "a = 8" (p. 37). | Not every sub-item was located (e.g. "Lemma A.1 phrasing"); nothing contrary was found. |
| A21 | RESOLVED | [7] "Companion manuscript, submitted (2026)"; [33] "Companion manuscript (2026)". No conflicting statuses. | [33] carries no status; [7] is not an arXiv preprint although Paper B cites A as one (minor asymmetry). |
| A22 | RESOLVED | p. 34: "at least (3/(128π⁴)+o(1))X(log X)², and … classes of every size occur infinitely often [33, Thms 1.1–1.2]". | — |
| A23 | RESOLVED | "moved here" no longer occurs in the supplement. | — |
| A24 | RESOLVED | Data statement p. 39 and S8: no `review/…`, `paper/jga/…` or `theory/…` paths; programs are named by file. Repository "maintained by A. Agadi". | Cosmetic: the file names "d1 pencil counts.py" and "d2 explicit pairs.py" (Suppl. p. 18) still carry review-item-like prefixes. |
| A25 | PARTLY RESOLVED | Table 1 extended (Ω_l, Π_i, β_{l,i}, T(L), ι). Node a versus a_l disambiguated by a sentence in Thm 3.8(ii). [vⁿ] defined. Bibliographic issue numbers present. | R is still both the reciprocal sum and the rotation in §2.4 (p. 12). ϱ is the reciprocal sum (Lemma 3.16, Prop. A.2), the cutoff radius (Lemma B.1) and the remainder (Prop. B.2). No renaming (λ_l, ρ) was done. |
| A-desk-reject | NOT APPLICABLE | Editor's judgement. A2 and A5 address two of its four reasons; A6 is resolved. | Cover letter not checkable. |
| **Rank A-1** | RESOLVED | = A1. | — |
| **Rank A-2** | RESOLVED (proof route instead of relabel) | = A2, A13, A14. | See A2 residue. |
| **Rank A-3** | RESOLVED | = A3. | — |
| **Rank A-4** | PARTLY RESOLVED | = A5 (done) and A7 (contribution sentence done). | Shared-data/deposit sentence missing; cover letter not checkable. |
| **Rank A-5** | RESOLVED | = A24. | Cosmetic file names. |
| **Rank A-6** | RESOLVED | = A4, A6. | Duplicate "[47, §1]". |
| **Rank A-7** | RESOLVED | = A8, A9, A19. | — |
| **Rank A-8** | RESOLVED | = A10–A13, A16. | — |
| **Rank A-9** | RESOLVED | = A17, A18. | — |
| **Rank A-10** | PARTLY RESOLVED | = A15, A20–A23 (done), A25 (partial). | Notation overloads (A25). |

## Paper B

| item | disposition | evidence / page | what remains |
|---|---|---|---|
| **B1** (blocking) | RESOLVED | All six points are fixed (§7.1, pp. 16–17, unless noted). **Claims exactly what is supported.**<br>(1) Weyl tail: "a Weyl-law estimate of the tail … that tail term is an estimate, not a bound, and floating-point summation is not included".<br>(2) Completeness: "a missing eigenvalue together with a spurious one nearby would not be seen … Completeness below 1.6×10⁴ is therefore supported … not proved".<br>(3) Circularity: "the comparison uses the true signature".<br>(4) Single window: "The triangle spectra used here were computed with single-window slicing … we recomputed all four problems … with the two-window solver … no window miss found … 1.4×10⁻¹⁴". This matches A's supplement S4 (p. 14).<br>(5) Upper bounds: "Conforming elements would bound … in exact arithmetic with exact integration; here … neither effect is controlled, so no λ̃_j is a proved upper bound".<br>(6) Rigorous version (p. 15): "guaranteed upper and lower eigenvalue bounds, a proof of completeness independent of the signature, a validated evaluation of G_σ(t), a certified lower bound for the systole, and outward rounding in E_N".<br>Input status: list (i)–(v), p. 15. Abstract: "estimated, not proved". Table 4 caption: "not certified". | The input-status "table" is a numbered list (adequate). Note: (iv) reports a wrong signature in "19 of these 24 cases", against 22/24 in reviewer d's experiment. These are different experiments, not necessarily an error. |
| B2 | RESOLVED (as far as checkable) | [24] is "Preprint, arXiv:[PLACEHOLDER]" (expected). The B PDF contains no external GoTo-R links, so the cross-document hyperlinks are gone. Table 1 (p. 5) lists every import. "nothing else here is taken from it". | Supplying A to the referees is not checkable. The optional import→constant map is only partly given (the diameter → t₃ link on p. 10). |
| B3 | PARTLY RESOLVED | p. 4 cites Stanhope [7], Proctor–Stanhope [8], RSW [9] and Doyle–Rossetti [5]. Area: "Whether the bound on the area can be dropped … we do not know" (p. 4). | Dryden's isospectral finiteness and McKean / OPS / BPP are not cited. The gain is not explicitly stated as a finite certifiable decision procedure. |
| B4 | PARTLY RESOLVED | (c) Abstract pp. 1–2 and intro p. 3 lead with the class-level result: "decides four of ten … with 855 to 2900 … estimated to need 4.4×10³ to 4.1×10⁵". | (b) The exact-area need is "explained" only by "finitely many eigenvalues do not determine the area" (p. 15), which conflicts with Thm 1.1; see New problems. Thm 7.1 is not extended to Sig(A, M). |
| B5 | UNRESOLVED | No consistency check (true σ satisfies the inequality for all N, t; maximal ratio reported) appears in §7. | Non-blocking strengthening. |
| B6 | RESOLVED | p. 25: Huntley–Jorgenson–Lundelius [34], Otal–Rosas [35], BMM [36]; Garbin–Jorgenson on p. 4. "What is missing here is an orbifold version of either: …" | — |
| B7 | RESOLVED | pp. 10–11: "Dryden and Parlier [29, Thm 3.1] (stated for cone angles less than π…) should give a diameter bound of order A(1+log 1/ε)+log M, since at most 3g−3+n … short"; Buser's count "does not transfer directly, as passing to a torsion-free cover multiplies the genus by an index that depends on the orders". | Buser Ch. 4 is not cited by chapter (minor). |
| B8 | PARTLY RESOLVED | p. 13: "any rational t ≤ t* may replace it, and the rule is then computable to any prescribed accuracy; e^{−λ̃t} is not rational, so the comparison is not one in exact rational arithmetic". | The new existence argument for K is incorrect as written; see New problems. |
| B9 | PARTLY RESOLVED | Fig. 1 caption is self-contained. p. 14: "at the grid times 0.050 and 0.056 (shaded); with the infimum over s taken more finely the window widens slightly"; N = 20 versus 21 eigenvalues explained. Table 6 time defined ("middle of the window"). N_obs defined (p. 19). Fig. 3(b) "dotted levels at j²". | N_obs values are not tabulated. Class-level counts are not plotted in Fig. 2. |
| B10 | RESOLVED | Table 6 caption: "≥ N_c means that the criterion fails for every N ≤ N_c − 1 … λ̃₀, …, λ̃_{N_c−1}". p. 18: "low by at least 0.27%". | — |
| B11 | PARTLY RESOLVED | The script path has moved to the data statement (p. 25). Closed form "2 arccosh((1+2cos(2π/7))/2) = 0.983986…" (p. 22). Repository "maintained by A. Agadi". | It is not said that the word-length-24 enumeration is complete (it is "used in no proof"). |
| B12 | RESOLVED | p. 10: "like A/ε when ε/2 < arccosh(1+2/(π²M²))". p. 13: "once ε is small enough for D to depend on it (ε < 0.42 …)", with a one-line ε⁻³ log(1/ε) derivation. | — |
| B13 | RESOLVED | p. 13: "the row with M = 8 … contains O(2,8,8) but not O(3,3,12)". | — |
| B14 | PARTLY RESOLVED | pp. 16–17: (0.05,10) is production and (0.07,12) the comparison; "mass quadrature raised by 2p"; "ARPACK … run to machine precision"; "Near 10⁻¹⁴λ_j the difference reflects the solver and rounding"; convergence referred to A's supplement. | Residual norms are still not reported. There is no convergence table in B itself. |
| B15 | RESOLVED (mostly) | (H2) "parabolic" (p. 8). "these orders are artefacts of the method" (p. 10). "bi-Lipschitz orbifold maps, sending cone points to cone points of the same order" (p. 3). λ₁ bound: "keeping in ∫f² only the part over the collar" (p. 24). Admissibility of ĝ_t (p. 6). B monotonicity range (p. 6). | "Sig" (class of orbifolds) versus Sig(A, M) (set of signatures) remain two notions, both now defined. |
| B16 | PARTLY RESOLVED | Thm 1.1 (p. 2): "numbers N, δ of Theorem 6.2 … G_σ … t* the time of Theorem 6.2"; "counted with multiplicity, so that none of the first N is omitted". | Thm 1.2 still states only the (C1)-type criterion; (C2) is not mentioned. Harmless, since (C2) ⇒ (C1). |
| B17 | RESOLVED | Thm 1.3 (p. 4): "no N and δ … such that any two orbifolds of area at most A and systole at least ε whose first N eigenvalues agree to within δ have the same signature". | — |
| B18 | RESOLVED | p. 5: "Lemma 3.3, not stated there, is a direct consequence of [24, Lemmas 2.10 and 3.3]". | — |
| B19 | RESOLVED | p. 24: "For k = 3 these are the orbifolds O_ϑ of Section 7 … so Table 6 runs the test along this pinching family". | — |
| B20 | RESOLVED | p. 3: "two orbifolds of different signatures have different spectra [1], [5, Thm 1]". | — |
| B21 | PARTLY RESOLVED | Buser–Courtois 287(1) [6]. [11, Thm 6.5] is now "spectral counting functions pointwise". Garbin–Jorgenson log growth "[10, Thm 5.3]". | Hejhal [12] has no pinpoint. Beardon [28] lacks "vol. 91". Ratcliffe is not cited for the hyperboloid. Buser [19] has no DOI. |
| B22 | UNRESOLVED | Γ is still both the group and the gap Γ(t), Γ* (p. 12). ε versus ϵ_j, δ versus δ_k, and A (area) versus A ∈ Γ (Lemma 8.1, p. 20) persist. | Renaming not done. |
| B23 | UNRESOLVED | pdftotext of the figure labels is still garbled ("jG¾0 (t) ¡ G¾ (t)j", "¸j", "hm2 (¸j ¡ 1=4)=¼ 2"). | Production fix. The same applies to Paper A's figures. |
| B24 | PARTLY RESOLVED | Abstract rewritten. Table 6 no longer interrupts Lemma 8.1. Prop. 8.2 proof split ("The cone ball", "The systole"). Proof of (H3) given. "aeb" defined in Tables 3 and 5. | The "–" entries in Table 4 (D, M = 3 for the triangle orbifolds) are unexplained in the caption. The garden-path sentence could not be identified. |
| B25 | PARTLY RESOLVED | Table 4: "lower bound ℓ … not certified". Brent's role explained (p. 18). 0.8 cut-off justified ("counts of three discretisations agree", p. 17). diam O = diam P observed. Fig. 3: two mesh levels. | "worst difference 2.1×10⁻¹⁵" is still not marked absolute or relative (p. 17). No sharper perturbation bound. |
| B-desk-reject | NOT APPLICABLE | Editor's judgement. | — |
| **Rank B-1** | RESOLVED | = B1. | — |
| **Rank B-2** | RESOLVED (as far as checkable) | = B2; arXiv placeholder expected. | — |
| **Rank B-3** | PARTLY RESOLVED | = B3. | Dryden, McKean / OPS / BPP; decidability framing. |
| **Rank B-4** | RESOLVED | = B7. | — |
| **Rank B-5** | PARTLY RESOLVED | = B8. | Incorrect existence sentence. |
| **Rank B-6** | PARTLY RESOLVED | B4(c) and B6 done. | B4(b). |
| **Rank B-7** | PARTLY RESOLVED | B10 done; B9 mostly done. | N_obs not tabulated; class-level counts not in Fig. 2. |
| **Rank B-8** | PARTLY RESOLVED | B13 and the path move done. | Completeness of the systole enumeration not stated (B11). |
| **Rank B-9** | PARTLY RESOLVED | B12, B15, B17–B19 done. | (C2) in Thm 1.2 (B16). |
| **Rank B-10** | PARTLY RESOLVED | B20 done. | B21–B25 partial or unresolved. |

## New problems

**Paper A**

1. **p. 24.** Duplicated citation and stray comma: "known only for k ≤ 9 and k = 11, [46], and whether N(k) = k+1 for all k is open [47, §1], [47, §1]."
2. **pp. 5, 12, 15.** "One new odd power of the order still enters per order in t" (also "the cone orders still enter through one new odd power per order"). Prop. 2.11 proves this only for m ≥ max(2, l−1). The coefficient β_{l,l+1}(p) can also vanish: it is zero near a flat cone point, exactly the situation used in Prop. 2.13(iii). Suggested rewording: "can enter, with coefficient β_{l,l+1}(p)".
3. **Manuscript ↔ supplement links.** The hyperlinks are GoTo-R links to `build/supplement.pdf#…` (about 30 in the manuscript) and `build/manuscript.pdf#…` (in the supplement). These are local build paths, and the links will dangle once the files are renamed as Online Resource 1. This is the same issue that B2 raised for Paper B's links into Paper A.
4. **Suppl. p. 7.** "Proposition S2.1, lists the sums" has a stray comma. "a partner sharing one invariant fewer; Every value" has a capital letter after a semicolon.
5. **Figures (all of A).** Figure text has no Unicode map ("4¼t", "¡12", "km~ ¡ mk"). This is the analogue of B23, for production.

**Paper B**

6. **p. 10.** "for the examples of Table 2 with M = 12 it does not depend on ε" is contradicted by Table 2 itself: at A = 4π/3, D = 3001 for ε = 1 but 3184 for ε = 0.1. Since arccosh(1 + 2/(144π²)) ≈ 0.053 > 0.05 = ε/2, the systole term binds at ε = 0.1. The sentence is true for M = 100.
7. **p. 13 (B8 fix).** "Q(K+1)/Q(K) grows at most like K(M/π)² while t* … far below (π/M)², so t*^K Q(K) first decreases and attains values below any positive bound" is false. Because the ratio grows with K, the sequence decreases only until K ≈ (π/M)²/t* and then increases, so its minimum is positive. Existence of K needs a comparison of that minimum (≈ exp(−c(π/M)²/t*)) with Γ*/16.
8. **p. 15, item (i).** "finitely many eigenvalues do not determine the area" conflicts with Thm 1.1: within C(A, ε, M) the first N eigenvalues determine the signature, hence the area 2πs(σ). It also does not answer B4(b).
9. **p. 19.** "the estimates are … 8.6×10² to 1.6×10⁴ for the family with M = 3" mixes actual counts (855) with Weyl estimates.

**Between the two papers.** No inconsistency was found on the shared numerics: 2002/2001 eigenvalues below 1.6×10⁴, the double-window rerun, 1.4×10⁻¹⁴, 4357–4451, and λ₁ 4.122 → 0.435 all agree. Table 1 of B maps correctly onto A's numbering (Thm 2.3, Lemmas 2.4–2.6, 2.8, 2.10, 3.3, Cor. 3.5, Thm 3.8(i), Lemma B.1, Prop. B.2).

There is one minor asymmetry. B cites A as an arXiv preprint, while A cites B (ref. [7], and supplement [7]) as "Companion manuscript, submitted".

Unresolved or partly resolved: A2 (residual only: terse pole-order step, "enters" wording), A7, A25, Rank A-4, Rank A-10, B3, B4, B5, B8, B9, B11, B14, B16, B21, B22, B23, B24, B25, Rank B-3, Rank B-5, Rank B-6, Rank B-7, Rank B-8, Rank B-9, Rank B-10

---

## After the check (main session)

The PDFs that were checked were built before the fixes below. The final build is recorded in the commit that carries this file.

### Fixed in the final build

- **New problem 1 (A).** The duplicated "[47, §1]" and the stray comma are removed.
- **New problem 2 (A).** In §1 and §2.4, "one new odd power … still enters" now reads "at most one new odd power", for large enough orders. At the start of §2.4 it says the new power *can* enter, with coefficient β_{l,l+1}(p), and notes that this coefficient vanishes near a flat cone point.
- **New problem 3 (A).** Links between the manuscript and the supplement are now unlinked references (`\ref*`), both ways. Paper B's references into Paper A were already unlinked. The arXiv package replaces each such reference by its number.
- **New problem 4 (A).** The stray comma and the capital letter in the supplement are fixed.
- **New problem 6 (B).** "For the examples of Table 2 with M = 12 it does not depend on ε" is replaced by "in Table 2 it does not depend on ε where that term does not bind".
- **New problem 7 (B8).** The incorrect existence argument for K is withdrawn. The text now says that the existence of K is not proved for every class, and that the rule does not need it: G_σ(t*) is a finite sum of explicit integrals, evaluable to within Γ*/16 by quadrature with a rigorous error bound.
- **New problem 8 (B4(b)).** Item (i) of §7 no longer says that finitely many eigenvalues do not determine the area. It now says:
  - Theorem 1.1 determines the area within C(A, ε, M), with the a-priori N;
  - an upper bound for the area would suffice in E_N;
  - the test has not been run over Sig(A, M).
- **New problem 9 (B).** The class-level counts (855–2900 for four members) and the estimates (4.4×10³–1.6×10⁴ for the other four) are now stated separately.
- **A7.** Paper A now says that the computed spectra are shared with the companion, which uses only the ranges where completeness is checked, and that both papers draw on one code and data deposit.
- **A25 (part).** In §2.4 the isotropy rotation is now γ, and the explicit rotation is Rot_ϑ, so R is only the reciprocal sum.
- **B3.** The intro adds the framing of effectivity as a finite decision procedure. It also adds the classical finiteness and compactness results, from fetched records: McKean (finite isospectral sets of surfaces), Dryden arXiv:math/0411290 (orbisurfaces), Osgood–Phillips–Sarnak 1988 and Brooks–Perry–Petersen 1992.
- **B5 (part).** §7.1 now says that the program checks, at every time of the grid, that the signature (C1) singles out at the least N is the true one. This is `practice.py`'s assertion.
- **B16.** Theorem 1.2 now mentions (C2).
- **B24 (part).** The Table 4 caption explains "–" (an order exceeds M).
- **B25 (part).** The quadrature difference 2.1×10⁻¹⁵ is now marked as relative for the identity term and absolute for the cone terms.

### Not changed, with reasons

- **A2 residue.** The pole-order and ω_n steps are terse but complete. Their full working is `theory/varcurv/varcurv.tex`, and Remark 2.12 and S8 name the computations.
- **A25 rest.** ϱ is still used three ways. The renaming of a_l was not done, to keep Paper A's numbering and notation stable for Paper B and the note; the clash is addressed by an explicit sentence in Theorem 3.8.
- **B5 rest.** The maximal ratio over the whole (N, t) grid is not reported. It is a strengthening, not a correction.
- **B9 rest.** N_obs is defined but not tabulated. The class-level counts are not plotted, since every figure stays as it is.
- **B11 rest.** The word-length search on O(2,3,m) is labelled as used in no proof. Its completeness is not claimed.
- **B14 rest.** Residual norms are not reported. ARPACK runs to machine precision, and the convergence table is in Paper A's supplement.
- **B21 rest.**
  - The Hejhal pinpoint, Beardon's volume number and Buser's reprint DOI could not be confirmed from fetched records (Crossref gives Beardon's series but no number), so they are not added.
  - The Ratcliffe citation was not added.
- **B22 and B23.** The notation overloads (Γ, ε/ϵ_j) and the figure-font Unicode maps are production items. They are deferred.
- **A21 asymmetry.** Paper B cites A as an arXiv preprint (placeholder). Paper A cites B as "submitted". Once A has its arXiv number, A's v2 can cite B the same way (`paper/ARXIV.md`, step 5).

### Verdict

All four blocking items (A1, A2, A3, B1) are resolved. No item the check found unresolved concerns correctness or a claim not supported by the paper: both mathematical slips that the revision introduced (new problems 6 and 7) were found by the check and are fixed above. What remains is presentation, notation and optional strengthening.
