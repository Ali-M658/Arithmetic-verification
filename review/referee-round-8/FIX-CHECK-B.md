# FIX-CHECK-B (round 8): "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

Inputs: `fixcheck-B/scratch/input/manuscript.pdf` (38 pp.) and `VERDICT-B.md`, and nothing else. Length is not discussed.

Independent recomputation: I wrote a script, `fixcheck-B/scratch/tools/consts.py` (mpmath, 50 digits). It works only from the formulas printed in the PDF (Lemmas 4.2, 4.3 and 4.5, Theorem 6.2, Corollary 6.3, Lemma A.2, the definitions of p_l, a_l and α_k). It reproduces:
- every entry of Table 4 (C_*, t_1, t_3, Θ_*, Λ, N, δ, binding constraint);
- every N and δ of Table 3 from the printed (A, ε, M, t, Θ): 244, 283, 139, 2605, 7416 and 387182. Each row also satisfies t ≤ t_2, Λt ≥ 1 and B_*(t) ≤ Θ/8. The tightest margin is row 3: B_* = 0.01793 against Θ/8 = 0.0190;
- the |Sig(A,M)| column (27, 48, 8, 8, 281, 12) and |S| = 6, 3 and 10 in Table 7 (by enumerating signatures);
- Table 2, and the range "about 3×10^196 and 2×10^29325" for πe^{3D}/A (the computed values are 3.4×10^196 and 2.4×10^29325);
- the ε-threshold: t_3 binds from ε = 0.44 down for A = 4π/3, M = 3, and the per-halving factor runs 5.239, 5.13, 5.01, 4.90, 4.81, 4.74, 4.67 (below 4.7 after seven halvings);
- the claim of Remark 6.5(a) that "the minimum defining t_1 is attained at k = k_*", in all rows;
- N ≈ 4.2×10^18 at A = 10π without k_* ≤ M;
- the counterexample (0;2^4,7^7) / (0;4^6,8^4): both have area 12π, and R−n, Ψ_1 = 54 and Ψ_2 = 2430 agree while Ψ_3 differs;
- the elliptic commutator identity tr[f,g] − 2 = 4 sin²(π/p) sin²(π/q) sinh² d (numerically). Jørgensen's inequality is attained for (2,3,7): 0.7530 + 0.2470 = 1.0000;
- d_3 = 25/12 for (2,8,8) against (3,3,12);
- the closed-geodesic overestimate: 2.8×10^-10 for the two classes at the systole, t = 0.0562.

---

## FATAL / MAJOR items

| id | status | finding |
|---|---|---|
| B1 | **DONE** (one residual wording point) | Corollary 6.3 (p. 15) and Proposition 6.4 with Table 3 (pp. 15–16) are present. The certification method is described: Arb integration, explicit tail bounds, lower bound Θ rounded down, and the inequalities B_* ≤ Θ/8, t ≤ t_2 and Λt ≥ 1 decided. All of Table 3 recomputes exactly (see above). The δ values are correctly rounded *down*. The abstract states "N of order 10^2 to 10^4 … each known to within 10^-4 to 10^-6". Residual: (i) the introduction (p. 2, "N of order 10^2 to 10^4 eigenvalues suffice … (Proposition 6.4)") gives no accuracy δ, although VERDICT says that "abstract and introduction" state N with δ. (ii) The abstract's δ range understates the two M = 3 rows, δ = 5.89e-4 and 4.86e-4, which are nearer 10^-3. Write "about 5×10^-4 to 2.5×10^-6". |
| B2 | **DONE** | The old intro Theorem 1.2 is now the paragraph "The same mechanism … gives an a-posteriori test (Theorem 7.1)" (p. 3). Theorem 1.2 is now the cusp theorem, and all references to "Theorem 1.2" (pp. 4, 5) point to it consistently. No stale "Theorem 1.3" remains. Section 7 opens with "Its applications below are illustrations on orbifolds of known signature … none of them is a proved determination" (p. 18). The abstract's last sentence says the same. |
| B3 | **DONE** | p. 5: "…decides the signature … in principle; for the classes of Table 4 it asks for up to about 4×10^30 eigenvalues to accuracies down to 10^-277 … the practical statements are Proposition 6.4 and the test of Section 7". This matches Table 4 (3.8e30, 8.7e-278). The cost remark on p. 16 now names "computing N eigenvalues to accuracy δ" as the dominant cost. |
| B4 | **DONE** | §7.2 (p. 24): "for O(2,8,8) at t = 0.0562 it is 6.8×10^-3, against a hyperbolic term of 2.8×10^-10 … about 2.4×10^7 times smaller, so the statements of this paragraph are about that bound, not about the spectra". It cross-references Remark 6.5(c). The numbers check. |
| B5 | **DONE** | Item (iv), p. 20: "this protocol is empirical, tested on these 24 corruptions only, and not a proved criterion". The count is consistent: 6 indices × delete/duplicate × 2 orbifolds = 24. Inertia counts are not done, and the text says so ("We have not done this", p. 20). |
| B6 | **DONE** | New paragraph on p. 4: none of A, ε, M is read off finitely many eigenvalues (Theorem 1.2; Problem 1; "we know of no bound for the area"); the accuracies are absolute; the sum is order-independent and an omitted λ lowers it by e^{-λt}, which no budget covers. Minor tension: p. 16 says "the data must be the first N eigenvalues, **in order** and with multiplicity", while p. 4 stresses that the sum does not depend on order. Say "matched index by index" on p. 16. |
| B7 | **DONE** (minor overstatement) | p. 6: the reverse dependencies are stated ("the companion uses from this paper the count … of Lemma 4.5 and the certified systole bounds of Section 7.1 [31, Remarks 2.6 and B.5]; no proof of a main result of either paper depends on the other"). The phrase "apart from the computed spectra … nothing else here is taken from it" is still slightly too strong. The paper also takes from [31] the growth statement for |b_K(M)| ([31, Lemma B.3], p. 16), the comparison with [31, Lemma B.4] (p. 16) and the convergence tables of the computed spectra ("tabulated in the supplement of [31]", p. 21; Table 6 caption). None of these is used in a proof. Add "and the convergence data; we also quote [31, Lemma B.3] for an asymptotic remark", or similar. |
| B8 | **DONE** | p. 3: "The formulas of Theorem 6.2 say nothing about the size of the least admissible N, which we do not know". p. 17 repeats this ("We do not know the true order of the least admissible N"). |
| B9 | **DONE** | The paragraph after Theorem 4.4 (p. 12) is not a labelled "Remark", as VERDICT says, but its content is all there: the elliptic Jørgensen identity and inequality (verified; attained in (2,3,7), verified), [36, §5.4] = Beardon, and Dryden–Parlier [38] cited for collars and cone neighbourhoods. The reason for not pursuing it is given ("C_* enters … only through log C_* in t_3, and t_1 binds in all but one row of Table 4", which is true of Table 4). One small point: "a lower bound for d that grows with the orders once p ≥ 7" gives a bound only when 4 sin²(π/p) < 1, that is p ≥ 7. The wording is fine but could say "nontrivial only for p ≥ 7". |
| B10 | **DONE** | p. 13: "Theorem 4.4 is used in no proof of a main result: the finiteness statement of Section 1 rests on Mumford's and Bers's compactness, and the instances of Section 7 use the proved bound 2 diam P with Lemma 2.2(i). It is kept as an explicit bound and for comparison with … Proposition 8.2." Stanhope's isospectral diameter bound is credited (p. 5, "comes from Stanhope's diameter bound [12, 13]"). I found no remaining sentence saying that Theorem 4.4 is in the logical chain. |

## MINOR items

| id | status | finding |
|---|---|---|
| b1 | DONE | p. 3: "a second criterion, (C2), which implies the first". |
| b2 | DONE | The two N conventions are stated on p. 3, in §7.1 "The test" (p. 23) and in the Table 7 caption. |
| b3 | DONE | p. 17: N = 21 on the figure's 61-point grid (times 0.050 = 10^-1.3 and 0.056 = 10^-1.25, which are grid points), and N = 20 for (C2) on the finer grid, which matches Table 7. |
| b4 | NOT DONE (as declared) | Figures 1–2 still have no in-figure legend. The captions and text give the coding. Figure 2's text explains markers and colours. Acceptable, but a strict referee may repeat it. |
| b5 | DONE | p. 28: "Granting this (and only for the limit m → ∞, so that the finitely many m < 13 do not matter)". m ≥ 13 follows from m/(2π) ≥ 1 + m/(4π) ⇔ m ≥ 4π (checked). |
| b6 | DONE | p. 17: "t_3 binds, for A = 4π/3 and M = 3 from ε = 0.44 down, and from ε = 0.42 on N grows by a factor per halving … from 5.24 to below 4.7 over seven halvings". Verified exactly (5.239 … 4.673). It is labelled as observations on the formulas. |
| b7 | DONE | Table 3 gives t. |
| b8 | DONE (kept) | Lemma 8.1 is retained with the "for completeness" justification (p. 25). |
| b9 | DONE | p. 22: "a margin of at least 5×10^-8 in all ten cases". |
| b10 | DONE | See B5. |
| b11 | n/a | Template header defaults ("Corresponding author(s). E-mail(s):") are still on p. 1, as VERDICT says (journal template). |
| b12 | DONE | p. 3: the dimension-two energy factor [K^-2, K^2] and the L² factor [K^-2, K^2], hence λ_j within [K^-4, K^4]. Correct: in 2D the energy distortion is s_max/s_min ≤ K². |
| b13 | DONE | p. 4 and p. 30: "an analogue … in a loose sense". |
| b14 | DONE | Remark 6.5(a) (p. 17) is labelled "an observation and not a theorem". The failure (0;2,2,2,2,7^7) / (0;4^6,8^4) at area 12π is correct (checked) and lies outside the enumerated ranges stated, so it is consistent. |
| b15 | DONE | Lemma 2.2: "a class and its inverse are counted separately unless they coincide, as they can when Γ has elements of order 2". There is no stray "oriented" statement. |
| b16 | DONE | p. 13: "about 3×10^196 and 2×10^29325". Recomputed 3.4×10^196 and 2.4×10^29325. |
| b17 | DONE | Lemma 2.2(ii) now says "for fixed t, B_C decreases with ℓ on the set of ℓ with t ≤ ℓ²/(2(1+ℓ))". The log-derivative in the proof checks. |
| b18 | **NOT DONE** | Proposition 2.3(b) (p. 9) still reads "has the sign (−1)^{K+1} **or vanishes**". VERDICT says this was removed. The proof in A.2 gives a strict sign for every term, so the words can go. |
| b19 | DONE | B_* is defined inside Corollary 6.3. |
| b20 | DONE | p. 15: "every term to over-estimate its λ_j by up to δe^{λ_j t_*}". This is correct, since min(λ̃_j, λ_j) = λ_j for an over-estimate. |
| b21 | DONE | p. 16: "|b_K(M)| grows like K^{-1/2} K!(M/π)^{2K} up to a constant factor, since Φ_M has simple poles at ±π/M [31, Lemma B.3]". This is consistent with p_l having (2k)!/(k!(l−k)!) weights (dominant term (2K)!/(K!4^K) φ_K ~ K^{-1/2}K!(M/π)^{2K}). |
| b22 | DONE | Theorem 7.1: "with Area(O) replaced by a lower bound such as π/21". |
| b23 | DONE | p. 23: floating-point rounding and quadrature error "are not included in E_N; both are far below every margin". |
| b24 | DONE, with one residual scope issue | "Geometric middle" is fixed (p. 23, Table 7 caption). N_obs "at some single time t" is fixed (p. 25). The factor "about 6 to 12" against the Sig(A,M) column (p. 24) holds for the triangle orbifolds (283/24 = 11.8, 283/36 = 7.9) and for the two family members whose systoles define rows of Table 3 (ϑ = 0, M = 3: 139/24 = 5.8; ϑ = 2.8: 2605/461 = 5.7 and 7416/842 = 8.8). It does not hold for ϑ = 0.4–2.4, or for ϑ = 0 at M = 12. For those, the only applicable row of Table 3 is ε = 0.693994, and the factors are 2605/35 ≈ 74 and 7416/59 ≈ 126. Restrict the sentence to those cases, or add rows to Table 3. |
| b25 | DONE as far as checkable | [16, Thm 6.5] is used for the local counting function (p. 5). Stanhope's isolated-singularities statement is qualified ("for isolated singularities, bounds the number of singular points [12, Main Thms 1–2]"). "Nothing else here" is reworded (see B7). Table 6 is "1 ≤ j ≤ 40". The LMPT sentence still says "bounded effectively in terms of the area [25]". I cannot tell from the inputs what change B-e m4 asked for, so I cannot verify it. |
| b26 | not done (declared) | Nothing to check. |

---

## New points a strict referee would flag (not in VERDICT)

1. **Prop. 2.3(b) "or vanishes"** is still there; see b18.
2. **Rounding convention in Table 4.** δ is an admissible accuracy, so it should be rounded down and N rounded up. Table 3 does this. Table 4 rounds to nearest:
   - δ is printed *larger* than the computed value in 6 of 8 rows: 3.1e-21 against 3.069e-21; 4.2e-25 against 4.166e-25; 1.5e-9 against 1.479e-9 (two rows); 4.1e-41 against 4.055e-41; 5.9e-11 against 5.892e-11; 8.7e-278 against 8.654e-278.
   - N is printed *smaller* in three rows: 6.8e9 against 6.818e9; 4.3e4 against 43188; 7.4e12 against 7.436e12.
   
   Either round outward or say in the caption that the entries are two-figure approximations and that the exact values are in the deposit. The same applies to "N = 3.9×10^5" in the text (exact 387182; that one is fine as an order of magnitude).
3. **Figure 2 caption** (p. 25): "The test needs 56 to 2.7×10^11 times fewer eigenvalues than Theorem 6.2." This is correct (43188/767 = 56; 7.436e12/28 = 2.7e11). After B1 and B4, however, the paper's own conclusion is that nearly all of this gap comes from Lemma 6.1, and that the certified Proposition 6.4 is within a factor of about 6–12. As it stands, the caption keeps the old headline comparison. Add "(against Proposition 6.4, a factor of about 6 to 12)" or drop the ratio. A Proposition 6.4 column in Table 7, or a marker in Figure 2, would make the comparison honest at a glance.
4. **Proposition 6.4 is a computer-assisted proof, but the certificate is described only in words.** The paper does not state:
   - the explicit tail bounds used for the identity and elliptic integrals;
   - the finite integration interval;
   - the working precision;
   - that t is rational, or exactly representable (VERDICT says it is, but the PDF does not).
   
   Without these, a reader can rerun the code but not check the argument. A short paragraph or appendix with the two tail inequalities would close this.
5. **Software pinning.** The data statement says that `certified_gap.py` uses python-flint/Arb, but the pinned-software sentence (p. 31–32) lists NumPy, SciPy, mpmath and NGSolve/NETGEN only. Add the python-flint (and Arb/FLINT) version.
6. **Introduction lacks the δ of Proposition 6.4** (B1 residual), and the abstract's "10^-4 to 10^-6" understates the M = 3 rows (≈ 5×10^-4).
7. **"in order" on p. 16** sits uneasily with the order-independence stressed on p. 4 (B6 residual). The hypothesis is index matching, not ordering of the list.
8. **Scope of "6 to 12"** in §7.2 (b24 residual).
9. Placeholders remain:
   - Zenodo DOI;
   - the preprint identifiers of [31] and [32];
   - the author-contributions statement;
   - the AI-use statement.
   
   These presumably will be filled before submission, but a referee would note them.

No broken cross-references (no "??") were found, and all theorem, table and figure references I followed resolve to the right objects. I found no new mathematical error. Every number I recomputed from the printed formulas agrees with the manuscript.

## Summary

- B1–B10: all DONE. B1, B6, B7 and B9 each have a small wording residual, listed above.
- Minor items: all DONE or declared not-done (b4, b26), **except b18 (NOT DONE: "or vanishes" still in Prop. 2.3(b))**. b24 has a scope residual.
- New: the rounding direction in Table 4, the Fig. 2 caption still benchmarking against Theorem 6.2, and the certificate details of Proposition 6.4 (tail bounds, interval, precision, python-flint version) are the points most worth fixing.

## Resolutions after this check (round 8)

- B1: the abstract and introduction give δ "about 6×10^-4 to 2×10^-6"; Table 3 gives each δ. The certificate is described (200 bits, rational t, tail bounds of size at most e^-80 with their formulas); python-flint 0.9.0 added to the pinned software of the data statement.
- B6: "with multiplicity and none omitted" replaces "in order and with multiplicity".
- B7: "no proof here uses anything else from it".
- b18: "or vanishes" removed from Proposition 2.3(b) as well.
- b24: the factor 6–12 is now stated for the triangle orbifolds and the two family members whose systoles define the classes of Table 3.
- New: Table 4 (and the count constants and N columns of Tables 3 and 7) now round N and C_* up and Θ_*, δ down (`tools/make_tables.py`); the text quoting Table 4 updated (6.9×10^9, 4.4×10^4, 7.5×10^12).
- Not changed: the Figure 2 caption (captions are kept to two sentences; the comparison with Proposition 6.4 is in §7.2); B9's location (a paragraph, as the fix check notes, with the content present).
