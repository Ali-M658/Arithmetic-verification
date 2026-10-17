> **Input error (recorded by the orchestrator).** The Paper A PDFs given to this check were stale copies
> (`paper/jga/manuscript.pdf` and `supplement.pdf` of 6 October, 35 pages), not the current build
> (`paper/jga/build/`, 55 + 16 pages). The Paper A section and the cross-paper items X1-X3 below therefore
> describe an old draft and are superseded by `FIX-CHECK-A2.md`, a rerun on the current PDFs. The
> Paper B and note sections used the current PDFs and stand.

# FIX-CHECK, referee round 6

Inputs checked: `fix-check/scratch/input/` (A-manuscript.pdf 35 pp., A-supplement.pdf 8 pp., B-manuscript.pdf 34 pp., N-note-integers.pdf 19 pp., VERDICT-A/B/N.md). Page numbers are PDF pages; "S p" means a page of the A supplement. Formulas and figures were checked on rendered pages in `scratch/img/`. The numerical recomputations are in `scratch/code/`.

The extracted text contains no "??".

**Paper A was restructured, not patched.** The following are gone:
- Propositions 2.11 and 2.13 (variable curvature);
- old §2.4;
- Appendix B (enveloping remainders, Lemma B.1, Proposition B.2) and bound (6);
- old Figures 6–8 and the notation table;
- supplement sections S5–S8.

The results were also renumbered: growth is now Theorem 3.11, the Descartes bound Theorem 3.8 and isolation Theorem 5.10. Many A rows are therefore resolved by deletion, and they are marked NA (removed). This restructuring is the source of the main cross-paper problem (X1 below).

---

## Paper A: "How much of a hyperbolic orbifold does heat hear?" (+ supplement)

**Recomputed and found to agree with the PDF:**
- Theorem 5.4: S\*(p) and the gaps.
- Proposition 5.9: the 38 collision-free sums, checked by brute force to S = 600, and the 25 575 triads at S = 557.
- Tables S3 and S4: 83 triads; 101/168 at (3,7,8).
- Theorem 5.10:
  - φ∘ψ = id;
  - Δ = 2^18·3^8·5^6;
  - #E(F₇) = #E(F₁₁) = 12;
  - the 12 points;
  - Selmer orders (4,1), which match the note.
- d₃, d₄, d₅ = 25/12, −1775/24, 153025/48.
- The sign of det M for n = 3, 4, 5.
- Examples 3.6 and 3.12, and Remark 3.2.

### MAJOR

| id | status | evidence |
|---|---|---|
| A1 | RESOLVED (removed) | No bracketing claim remains; bound (6) and Appendix B are gone. The only "bracket" is inside the proof of Lemma 2.6 (p7). |
| A2 | RESOLVED (removed) | The non-integral-angle sentence attributed to Schueth is gone. Schueth is cited only as "see also [34, p. 2]" (p7, l.200), and Proposition 2.8 is stated for integer m. The Fursaev/Dowker literature is not added, but it is no longer needed. |
| A3 | RESOLVED (removed) | Old Propositions 2.11 and 2.13 are deleted. Remark 2.12 (p10) now reads "None of this is new", with citations. |
| A4 | PARTLY | The "doubled Prouhet"/"Proposition 3.12" wording is gone. The Fig. 2 caption (p16) now says "genus pairs built from Prouhet's partition (L = 2,…,6)". It neither points to the construction (proof of Theorem 3.11(e), p31) nor gives c, c′, so the squares still cannot be rebuilt from the paper. |
| A5 | NOT RESOLVED | p2, ll.2–7 still says "explores a disc of radius about √t and learns only what lies in that disc … what all the points have learned". This is wrong near a cone point. The wave-trace picture is absent. |
| A6 | RESOLVED | "weight of the paper" and "M+1 is attained" are gone; Theorem 1.1 is now the uniform count. The mechanism is credited to [5, Prop. 1, §3] (p4, ll.84–95), and Theorem 3.8 is named a Descartes bound. |
| A7 | PARTLY | The framing is honest: p3 l.53 "errors in heat invariants, not eigenvalues", and Remark 6.1 (p23). The planned lemma giving a proved δ₁ from finitely many heat-trace values is absent. |
| A8 | RESOLVED | §4 is labelled classical (p5 l.121, p16 l.457). "Three analytic results carry the counts" is gone. |
| A9 | RESOLVED | The proofs of Theorems 6.5 and 6.8 are in §6. The 2-isogeny descent is in the proof of Theorem 5.10 (pp22–23). The supplement says "Nothing here is used in a proof". |
| A10 | PARTLY | The quotation of unrefereed note results is gone. p5 l.112 says only that the arithmetic "is the subject of the companion manuscript [20]"; what is shared is not stated. The S ≤ 4800 enumeration is still in both papers (A Proposition 5.9, p22; note Table 2), and A does not say so. |

### MINOR and presentation

| id | status | evidence |
|---|---|---|
| a1 | NA (removed) | Bound (6) is gone. |
| a2 | NA (removed) | Variable-curvature Proposition 2.13 is gone. |
| a3 | NA (removed) | |
| a4 | RESOLVED | Remark 2.12 (p10): "the t⁰ coefficient determines the closed orientable orbifold type". |
| a5 | RESOLVED | p6 l.153 defines a geodesic as a hyperbolic conjugacy class; p29 has "one geodesic, two orientations". |
| a6 | RESOLVED | Lemma 2.5 is "the standard approximation argument … for completeness" (p6). |
| a7 | RESOLVED | Remark 2.10 (p9) gives the normalisation mΦ_m^(2k)(0) = 2·4^k k! m c_{S_k}(π/m). |
| a8 | NA (removed) | |
| a9 | NA (removed) | Old S8 is gone. |
| a10 | PARTLY | One window is now used consistently (p28 l.796; S p3: 0.0015 ≤ t ≤ 0.03, agreement 7×10⁻¹³ against budget 1.5×10⁻¹¹). Whether Hyp was subtracted is still not said, and Hyp(0.03) ≈ 7.8×10⁻¹³ exceeds the stated agreement. |
| a11 | NOT RESOLVED | "conservative" is still used (p27 l.791; S p2). In Table S1 (S p3) the second difference is below the estimate at j = 1 (8.5e−14 against 5.9e−13). |
| a12 | RESOLVED | p30: "One command … (with --quick … --full …)". Versions are in requirements.txt (S p2), the protocol commit is dated (S p4), and the data file for Table S1 is named. The pointer "(Appendix B)" is broken (new problem A-N1). |
| a13 | NA | The statement is gone ([18] is now Grieser–Maronna, p5). |
| a14 | PARTLY | Example 3.12(iii) (p16) cites [5, p.9], [41, p.2], [37, A.1.33], [41], but does not say which source gives which L, and Borwein–Lisoněk–Percival is not named for L = 6. |
| a15 | RESOLVED | Theorem C(1): "odd symmetric system in the sense of [5, §3]". Problems are attributed to [5, §6] and to Wooley [40] (p15). |
| a16 | NA | Those entries and "wrote in 1994" are gone. |
| a17 | NA | Phrase gone. |
| a18 | NA | Table removed. |
| a19 | PARTLY | Corollary 3.5 makes no finiteness claim. Fig. 2 (525 classes with s ≤ 7/5) still presupposes finitely many signatures per area class, with no line saying why. |
| a20 | NOT RESOLVED | The Fig. 4 axis (p26) is ‖m̃ − m‖∞, while Theorem 6.5 uses dist. Neither caption nor text reconciles the two, and they differ for the complex roots in Table S2. |
| a21 | RESOLVED | The renderings are now Figs S1 and S2(a), captioned "Stylised renderings, not isometric". |
| a22 | PARTLY | The Fig. 5 caption (p29) says "ten times the budget"; p29 l.824 and S p6 say "10³ times the noise". Both thresholds remain, unreconciled. |
| a23 | PARTLY | The proof of Lemma 5.3(ii) (p20) has R > 7/10 > 1/3 + 60/224 ≥ R⁻_{S,3} and makes S ≥ 18 explicit. It does not say that 1/3 + 60/224 = 101/168 = R⁻_{18,3} at (3,7,8) (verified), or why that is the maximum. |
| a24 | NA (removed) | |
| a25 | RESOLVED | No clash inside a single argument. |
| a26 | NOT RESOLVED | Captions are still several sentences long (new problem A-N2). |
| a27 | NA (removed) | Old §2.4 is gone. |
| a28 | NA (removed) | |
| a29 | NA (removed) | |
| a30 | PARTLY | f(A) is defined (p2), but not its domain: it is a max over the empty set for A < π/21. |
| a31 | RESOLVED | Pigeonhole bound, Wright via Melzak [38], [5, §6 Problem 3] and [39] (p15). |
| a32 | NOT RESOLVED | No a-priori order bound or algorithm for the area classes of Fig. 2, in the paper or in the supplement. |
| a33 | NOT RESOLVED | Theorem 5.7 claims only the least sum. The least-area statement, its proof and its script are absent. |
| a34 | RESOLVED | Theorem 6.4(a) gives the explicit cond bound, cond ≤ 3.511 (p25). |
| a35 | NOT RESOLVED | Neither Duistermaat–Guillemin nor Hillairet / Ford–Wunsch is cited; this goes with the missing wave picture (A5). |
| a36 | NOT RESOLVED (cosmetic) | The proof of Theorem 3.11(c) (p31) still says "Kmult = 3"; only ≥ 3 is needed. |
| a37 | RESOLVED | p16 l.449: f(A) ≥ L+1 for A/2π ≥ 2L−3 (L ≤ 5), and for A/2π ≥ 10, 18 when L = 6, 7. |
| a38 | RESOLVED | Lemma 3.3 (p12) is an iff, and d is defined for every pair. |
| a39 | RESOLVED | Definition 3.7 excludes pairs {z, −z}; Theorem 3.4 uses evenness. |
| a40 | RESOLVED | The gap count in the proof of Theorem 3.8 (p14) checks out. |
| a41 | RESOLVED | ς_n and the [36, (1.37)] normalisation are stated; the signs were verified for n = 3, 4, 5. |
| a42 | RESOLVED | β > 0, and Lemma A.1 has n ≤ (L−1)²+1 (p30). |
| a43 | RESOLVED | Theorem 1.1(i): "No number independent of the area suffices". |
| a44 | PARTLY | The pieces are listed, but not which source gives which L (as in a14). |
| a45 | PARTLY | The s values of the Fig. 2 squares are not printed; checksums are only by reference to DATA-MANIFEST. |
| a46 | RESOLVED | Remark 3.13 states the scope of the bound 220. |
| a47 | NA | Table removed; T₂ = 6 and T₃ ≤ 10 are given in the text. |
| a48 | NOT RESOLVED | p29 l.820 and S p5 assert "systoles are 4b(ϑ)" and derive non-isometry from them. See X3. |
| a49 | NOT RESOLVED | p28 l.813: "testing every order of the cone expansion at once". |
| a50 | NOT RESOLVED | p29 l.814: "coefficients growing like l!(144/π²)^l" is stated as fact, not labelled heuristic. |
| a51 | NA | No Sig-level claim about Kmult of triangle orbifolds remains. |
| a52 | RESOLVED | Theorem 5.10 proof (pp22–23): "mutually inverse isomorphisms over Q"; verified. |
| a53 | NA (removed) | |
| a54 | NOT RESOLVED | S p3: "The orbifold with the smaller P₃ has the larger heat trace" is unqualified, but D(t) changes sign near t ≈ 0.34 (S p4, Fig. 5). |
| a55 | RESOLVED | Proposition 5.9 is labelled "computational" and has a "Method" (p22). |
| a56 | PARTLY | Remark 6.7 still says "For n = 1 recovery is Lipschitz" without saying it is algebraic only. The abstract says "all n ≥ 2 orders equal", while Theorem 1.3 says k = n ≥ 3. |
| a57 | PARTLY | Old Fig. 7 is gone. In Fig. 3 (p21) the p = 5 circle (117, 0.244) sits on the frame edge, and the caption does not mention it. |
| a58 | RESOLVED | φ is displayed in full (p22). |
| a59 | NA (removed) | |
| a60 | RESOLVED | key₂ = (S₁, R) is defined (p19). |
| a61 | NA, but the stated reason no longer holds | The reason was that renumbering would break the cross-citations; the paper was renumbered anyway (1.x and 3.x are distinct now), and B's citations did break (X1). |
| a62 | NA, but the reason is void | "every figure stays" is no longer true: old Figs 1, 4(a) and 6–8 were removed or moved to the supplement. |
| a63 | NOT RESOLVED | "learns" and "have learned" remain (p2). |
| a64 | PARTLY | P3 is not fixed: Example 3.6 (p14) still says "a handle costs no more invariants than a cone point". P5 (an S1 table of pieces) is absent. P2, P4 and P7 are no change, as decided. |

### New problems in A

- **A-N1 (p30 l.845), broken reference.** The text reads "DATA-MANIFEST.md lists every data file … (Appendix B)", but Appendix B (p31) holds only the AI-use placeholder and "Computations". Fix: delete "(Appendix B)".
- **A-N2, caption rule.** Captions should be at most two short sentences. The current counts are:

  | figure | page | sentences |
  |---|---|---|
  | Fig. 1 | p13 | 4 |
  | Fig. 2 | p16 | 4 |
  | Fig. 3 | p21 | 3 |
  | Fig. 4 | p26 | 4 |
  | Fig. 5 | p29 | 5 |
  | Fig. S1 | S p2 | 4 |
  | Fig. S2 | S p6 | 4 |

  Suggested captions:
  - Fig. 1: "The mirror argument of Theorem 3.4: discs mark X\* = U\* ⊎ (−V\*), rings mark −X\*. (a) (2,8,8) against (3,3,12), and below it (2,8,8) against itself; (b) (1;15) against (0;3,3,5,5)."
  - Fig. 3: "Least-order strata of hyperbolic triads, p = 2,…,8, between R⁻_{S,p} and R⁺_{S,p}. Dots mark first overlaps S\*(p), circles first collisions."
  - Fig. 4: "Recovery error of the cone orders against a uniform error δ in the heat coefficients. Diamonds mark δ_cert."
  - Fig. 5: "(a) D(t) for (2,8,8) against (3,3,12), with the cone-point term and partial sums. (b) |Z₀ − Z_ϑ| for (0;3,3,3,3), with the predicted hyperbolic difference and the error budget (shaded)."

  Shorten Figs 2, S1 and S2 the same way, and move the remainder of each caption into the text.
- **A-N3 (pp1–2), abstract.** All inline math in the abstract is set in bold (confirmed on the render). Fix: put `\unboldmath` at the start of the abstract.
- **A-N4 (abstract against Theorem 1.3).** The abstract says "all n ≥ 2 orders are equal" and Theorem 1.3 says "k = n ≥ 3". Fix: write "n ≥ 3" in the abstract.
- **A-N5 (p26), Fig. 4 caption.** "Diamonds sit on each curve" is wrong, since the dotted curve has none. Fix: "on the three uniform-error curves".
- **A-N6 (p16), Fig. 2 caption.** "their companions" is undefined. Fix: name the pair, and add "(construction in the proof of Theorem 3.11(e))".
- **A-N7 (pp18–19), Remark 4.7.** "along a Thurston length coordinate all but countably many points have heat traces different from a given one" is stated without proof. Fix: add the reason (real-analytic and non-constant in the coordinate), or delete the sentence.

Suggested wording for the open items:

| item | page | suggested change |
|---|---|---|
| A5 / a63 | p2 | Replace "explores a disc of radius about √t and learns only what lies in that disc" with "is determined, up to exponentially small terms, by the geometry within distance about √t, except near a cone point of order m, where the reflected images reach out to about √t/sin(π/m)". Replace "what all the points have learned" with "the contributions of all points". |
| a11 | p27 l.791; S p2–3 | Replace "conservative estimate" with "second, independent difference". |
| a49 | p28 l.813 | Replace with "a check of the elliptic terms as functions of t". |
| a50 | p29 l.814 | Insert "heuristically" before "growing like". |
| a54 | S p3 | Write "For small t, the orbifold …". |
| a36 | p31 | "Kmult = 3" → "Kmult ≥ 3". |

---

## Paper B: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

**Recomputed and found to agree with the PDF:**
- All eight rows of Table 3, and the K columns of Table 4: 3.55e9, 4.01e5, 9.45e9. The verdict's "about 3.5×10⁹" is confirmed with B's formula K = A M e^{10r₀+ρ₁}/(2v₀(cosh ρ₁−1)).
- All of Table 2.
- N ≈ 4.19e18 at A = 10π.
- ℓ_{2,3} = 0.562067.
- The closed-form systoles 2.2567679 and 1.8626041.
- d₂ = −1/12 and d₃ = 25/12.
- Every ratio quoted in §7.2 and in the Fig. 2 caption, checked against Table 6.

**The required framing is intact.** Errors are called "estimates, not enclosures" (pp2, 3, 17, 18), completeness is "supported … not proved" (pp17, 19), and "the test presupposes a complete list" (p17). The Table 6 caption says "estimated errors and lists assumed complete".

### MAJOR

| id | status | evidence |
|---|---|---|
| B1 | RESOLVED within B; but see X1 | Appendix A (pp28–30) proves Theorem 2.1 (Lemma A.1), Proposition 2.3, Lemmas A.2–A.4, Lemma 3.1 and Theorem 3.2, and Lemma 2.2 is proved on p7. However, the Table 1 column "in [30]" now points to statements that no longer exist in A, or have different numbers there. |
| B2 | RESOLVED | Lemma 4.5 (p11) gives the diameter-free count; Theorem 6.2, Table 3 and the (C1) K column of Table 6 use it. "does not transfer directly" is gone (p11 reads "The same lemmas give a count without the diameter"). The diameter bound is kept separately (p12). |
| B3 | RESOLVED, with an error inside the remark | Remark 6.3 (pp15–16) compares the two routes as resolved and attributes the method to no paper. Its convention is wrong (new problem B-N1). |
| B4 | RESOLVED (one residual) | Abstract, p3 and p20 say "holds … with estimated errors and lists assumed complete"; "four of ten" is gone, and the M dependence is reported. Residual: p5 says the test "applies the same idea to decide a signature". |
| B5 | RESOLVED | p20: the diameter changes the counts by "at most 1.7 in either direction" (max 1.664 recomputed), and the gap is attributed to the data factor. The ranges agree with Table 6, which gives every row. |
| B6 | RESOLVED (small gap) | p17: the domain is a polynomial approximation and there is no min-max bound; the inertia route is "not done". p18: rounding level is stated. p19: the trace is compared against every σ ∈ S (margin 2.96e-3, about 2×10⁸ budgets). p17(v): counts unchanged for r ≤ 1e-4. Gap: for the family O_ϑ the margin against other signatures is not reported. |
| B7 | RESOLVED | p5: the new input is the uniform systole bound (Proposition 8.2); [14, Thm 5.3] and [14, Cor. 5.5] are credited. Whether [14] says this cannot be checked from the inputs. |
| B8 | PARTLY | The proof of Theorem 6.2 (p14) uses t\|a−b\|e^{−t min(a,b)}, and the weakened hypothesis is stated. Theorem 7.1's E_N (p16) still uses the plain t Σ ϵ_j; the text only says the factor "may be kept". |

### MINOR and presentation

| id | status | evidence |
|---|---|---|
| b1 | PARTLY | p11: "the factors 1/M … are not intrinsic". The Jørgensen order-free remark (an order at least 7) is missing. |
| b2 | RESOLVED | The speculation and Dryden–Parlier are gone. |
| b3 | RESOLVED | p19 gives the closed forms (verified); the family value 4b is a "numerical identification", and Proposition 8.5 proves ℓ ≤ 4b only. |
| b4 | PARTLY | p19 proves diam O ≤ 2 diam P, and Table 4 says "computed diameter". The Table 2 caption (p12) still reads "against true diameters". |
| b5 | NOT RESOLVED | p4: "their diameters growing like log m". Only a lower bound is proved. |
| b6 | RESOLVED | "bi-Lipschitz" on pp3 and 26. |
| b7 | RESOLVED | p23: "loses mainly through the crude bound 2s_m". |
| b8 | NA (reason holds) | The collar enters only a constant. |
| b9 | RESOLVED | Lemma 2.2(ii) and Theorem 7.1 state the lower bound ℓ. |
| b10 | RESOLVED | Lemma A.1 is proved; pp6–7 state the convention, and E_m → b₀(m) is verified. |
| b11 | RESOLVED | p29: proof of Proposition 2.3 and the monotonicity of \|b_K\|. |
| b12 | RESOLVED | p30: Vandermonde proof. |
| b13 | PARTLY | A still serves as both the class bound and the exact area (Theorems 1.2 and 7.1, Lemma 3.3(ii)). This is harmless. |
| b14 | NOT RESOLVED | The planned remark on δ₁ = 1/(2 lcm) and individual δ_k is absent. |
| b15 | NOT RESOLVED | The planned remark (max against sum; least area in Sig(A,M)) is absent. |
| b16 | RESOLVED | p14: the constants must be recomputed, and the cost and the truncation K are discussed. |
| b17 | PARTLY | p20 states the convention (N means N+1 eigenvalues λ̃₀..λ̃_N), but the abstract, p3, p20 and the Fig. 2 axis call N "eigenvalues" (new problem B-N3). |
| b18 | RESOLVED | p9: "For k = 2 the bound is attained", (4,4,4) against (3,4,6). |
| b19 | RESOLVED | Fig. 1 caption and text agree: N = 21 and 100, half-gap, grid times 0.050 and 0.056. |
| b20 | RESOLVED | p16: one-sided remark. |
| b21 | RESOLVED | p19: budget formula with the Weyl tail. |
| b22 | RESOLVED | p20: "about 8 to 11". |
| b23 | NOT RESOLVED | The planned remark (enumerated short geodesics in place of H) is absent. |
| b24 | RESOLVED | p20: every N in the complete range, every time of the grid. |
| b25 | RESOLVED | p19: family completeness details. |
| b26 | RESOLVED | p18: mixed corners. |
| b27 | RESOLVED | Theorems 1.1, 6.2 and 7.1 make completeness explicit; no ordering is assumed. |
| b28 | RESOLVED | p5: "follows the idea of Strohmaier and Uski, without their rigorous control of the tail". |
| b29 | Cannot be checked from the inputs | "log Q" is gone; Hejhal [16] is cited without a page. |
| b30 | Cannot be checked from the inputs | "[3, Cor. 3]" is unchanged. |
| b31 | RESOLVED (small mismatch) | C_l is defined (pp9, 30). The Theorem 3.2 header cites "[30, Thm 3.8]" while Table 1 cites "Theorem 3.8(i)"; both are wrong for the new A (X1). |
| b32 | PARTLY | [35] Beardon lacks "vol. 91" in "Graduate Texts in Mathematics". [23] and [10] are present. |
| b33 | RESOLVED | p27: SciPy 1.18.1, mpmath 1.3.0, NGSolve/NETGEN 6.2.2607, pinned versions, logarithms of the count constants, figure scripts. Python and NumPy versions are not printed. |
| b34 | RESOLVED | p4: reworded. |
| b35 | RESOLVED | p24: "suggested", "which we have not checked". |
| b36 | RESOLVED | p26: "in a loose sense". |
| b37 | PARTLY | p16 still says "(C1) … is the conclusion of Theorem 7.1 itself". Suggested: "(C1) is the weaker criterion; it uses only the inequality \|Σ − G_{σ(O)}\| ≤ E_N of Theorem 7.1." |
| b38 | RESOLVED | [23] LMPT, [24] Friedman–Jorgenson–Kramer, [36] Liu–Oishi, [37] Carstensen–Gedicke. |
| b39 | RESOLVED | [5] is marked as a preprint. |
| b40 | RESOLVED (residual) | Θ(t) replaces Γ(t), and ℓ_{2,3} replaces σ\*. K is still overloaded (new problem B-N2). |
| b41 | PARTLY | Captions are at most two sentences (Figs 1–3). Offsets are stated in the text (p21), and the figures contain only axis titles, ticks and panel letters (rendered). The N_obs column was not added to Table 6; N_obs appears only in Fig. 2 and on p21. |
| b42 | RESOLVED | p10: (H2) asymptotic case. |
| b43 | RESOLVED | p13: constants displayed together; caveats (i)–(v) on pp16–17. |

### After the fixes

| item | status | evidence |
|---|---|---|
| estimated-counts paragraph | RESOLVED | p20: "In every case of Table 6 both criteria hold within the complete range." |
| "at most 1.7 in either direction" | RESOLVED | p20; Table 6 maximum 1.664. |
| 2.96e-3 | RESOLVED | p19. |
| "461 to 847, λ_N up to 2540" | RESOLVED (but see B-N4) | p20. |
| "19 of 24 … at the first N" | RESOLVED | p17. |
| weighted-error parenthetical restricted to over-estimates | RESOLVED | p14. |

### New problems in B

- **B-N1 (p15), Remark 6.3.** "If ĝ is supported in (−ε, ε) … no geodesic term" contradicts B's own convention, in which h = ĝ is the spectral side and g the geodesic side (Theorem 2.1, Lemma A.1). Fix: "If g is supported in (−ε, ε), that is, if h = ĝ has Fourier transform supported below the systole, …".
- **B-N2, three meanings of K.** K is the count constant (Lemma 4.5, Theorem 6.2, p14), the truncation index (Proposition 2.3; p14 "for any K with t\*^K Q(K) ≤ Θ\*/16", right after "With K = K(A,ε,M)"), and the number of orders (Proposition 8.3, Remark 8.4). Fix: rename the count constant (for example K_geo) and the index in §8 (for example J).
- **B-N3 (pp1, 3, 20; Fig. 2), off by one.** "with 24 to 842 eigenvalues" counts N, but the test uses N+1 eigenvalues. Fix: "with N = 24 to 842 (the first N+1 eigenvalues)", or label the Fig. 2 axis "N".
- **B-N4 (p20).** "between 461 and 847 eigenvalues … t between about 0.004 and 0.007" are (C1) values only; (C2) needs 848–933, at t ≈ 0.00406. Fix: insert "for (C1)".
- **B-N5 (p18).** "within the conservative error estimate" contradicts "estimates, not bounds". Fix: "within the error estimate ϵ_j".
- **B-N6 (p18).** "the ϵ_j are at the floor 10⁻¹⁴λ_j or a few times it". In Table 5 the ratio is about 10–17 for j ≤ 40. Fix: "about ten to twenty times the floor 10⁻¹⁴λ_j".
- **B-N7.** Fix b4: "true diameters" → "computed diameters" in the Table 2 caption (p12).
- **B-N8.** Fix b5: on p4, "growing like log m" → "at least log(m/2π) (Proposition 8.2)".
- **B-N9 (bibliography).** Add "vol. 91" to [35]. Unify the volume styles of [16] ("Vol. 2") and [33] ("Vol. I").

---

## Note N: "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

The PDF uses Integers numbering. The verdict's Theorem 3.3, Lemma 2.1, Lemma 4.3 and Theorem 4.4 are the PDF's Theorem 1, Lemma 1, Lemma 4 and Theorem 3.

**Recomputed:**
- On C_{27/2}: (1:4:4) and (4:1:4) have order 6, and (4:4:1) has order 2.
- On C_{49/4}: (1:2:4) has order 12, with 2G = (0:1:−1)+T₂.
- Geometric-progression orderings have orders 4 (two of them) and 12 (four).
- The Ravi identity R/r = (Λ−1)/4.
- 128π⁴c_iso/3 = 437.83.
- Lemma 1: brute force to S < 400 finds no coincidence with R ≥ 1.
- Table 1: S and Λ.
- Table 2: local exponents 1.993 and 1.585; the histogram sums 98742 and 102719.
- Selmer orders against ranks 0, 2, 3, 3, 2.

### MAJOR

| id | status | evidence |
|---|---|---|
| N1 | RESOLVED | p8, Theorem 1(iv): orders 6, 6, 2 for (u:v:v), (v:u:v), (v:v:u); the proof (p9) uses the fixing transposition. |
| N2 | RESOLVED | p8, Theorem 1(i)–(iii): Z/6, Z/12 or Z/2×Z/6 (Mazur [12, III Cor. 5.2]). Z/2×Z/6 iff (Λ−1)(Λ−9) is a square. Z/12 iff Λ = (r+1+1/r)², proved, not only computed. Example C_{49/4} on p9. |
| N3 | RESOLVED | Table 1 (p14) gives rank and torsion for every row. p13 shows C_{27/2}(Q) has 12 explicit points, and the S = 18 class and its multiples are the only coincidences with Λ = 27/2. The companion is cited only for spectral consequences ("nothing here depends on it", p2). |
| N4 | RESOLVED | p13: Selmer orders (4,1), (4,4), (8,4), (16,2), (8,2); 2^{r+2} = \|Sel^φ\|\|Sel^φ̂\| [19, Ch. III]; what `ellrank` proves; root numbers. |
| N5 | RESOLVED | Lemma 4 (p11), "the dual family as a conic bundle", covers every primitive triple. p12: "a lower bound for the dual family, not its order of growth". The threshold log X > 438 is on pp3 and 12. |
| N6 | RESOLVED | p16: residual block bootstrap with Poisson MLE: 4.49±0.06 and 4.56±0.08; 3.53±0.08 and 3.63±0.11. The window spread 4.39–4.64 exceeds the bootstrap, as the text says. |
| N7 | RESOLVED | Conjecture → Question E (p3). Power law β = 0.587 (X^{1.59}), scaled difference 1.4 (p16). "a finite range bounds the limiting exponent from neither side". The heuristic is labelled. |
| N8 | RESOLVED | Lemma 1 with proof (p5); k ≥ 1 throughout; −0.286X (p11); ⌊X/S_D⌋ ≥ X/(2S_D) (p12). |
| N9 | RESOLVED | p3 and p15: the upper bound is at the scale of the number of triples and "does not show that coincidences are rare". |
| N10 | RESOLVED | p4: Sadek–El-Sissi with pinpoints and hypotheses, Moreland–Zieve, Cha et al., Ulas, MacLeod with R/r = (Λ−1)/4. Quintic on p17. Choudhry is not cited, for the verdict's reason. |

### MINOR and presentation

| id | status | evidence |
|---|---|---|
| n1 | RESOLVED | pp3 and 6: fibres I6, I3, I2, I1 [1, p. 658]; no subgroup symbol. |
| n2 | RESOLVED | p6, Proposition 2: six base points, nine with multiplicity; orders proved by lines through the flex O. |
| n3 | RESOLVED | p7: nonemptiness via (1:1:t); "rational" dropped. |
| n4 | RESOLVED | p5, Proposition 1: k ≥ 2, admissibility by Lemma 1. |
| n5 | RESOLVED | p7: ι undefined at three points and extended; collinearity shown. |
| n6 | RESOLVED | p4: [16, Prop. 2.5], [16, Prop. 2.7, Thm 2.8] with the hypothesis; Mazur locator on p8. |
| n7 | RESOLVED | p13: infinite order from Theorem 1(iv); "next positive multiple of P is 3P"; positivity from Lemma 2. No Nagell–Lutz certificate, as decided. |
| n8 | RESOLVED | p11: √(qr), q²/r, r²/q. p12: U ≥ V/2 ≥ 1. |
| n9 | RESOLVED | p11: Möbius step over residue classes written out. |
| n10 | RESOLVED | p11: 506 pairs D_{u,v}, 27 in classes of size ≥ 3. |
| n11 | RESOLVED | p8: "six orderings of x and six of its dual". |
| n12 | RESOLVED | p17: two-sentence caption; the thin curve is all copies, S ≤ 4800; colours are explained in the text (p16). The figure has only panel letters, axes and ticks. |
| n13 | RESOLVED | Table 2 (p15) is indexed by X; caption: "largest class size up to X". |
| n14 | RESOLVED | p16: Poisson MLE. |
| n15 | RESOLVED | p17: 189 lines up to permutation and sign; method described. |
| n16 | RESOLVED | p14: program per column; 5 992 496 499 triples. |
| n17 | RESOLVED | Abstract, p3 and p15: exponent quoted from X = 500 (1.99). |
| n18 | RESOLVED | p1: shortened, one convention. |
| n19 | NA (reason holds) | p3: Theorems A–C, Proposition D and Question E each name their section counterpart. |
| n20 | NA (reason holds) | p18: the placeholders are present, as required. |
| n21 | RESOLVED (artefact) | The render reads "with sum S". |
| n22 | NA (reason holds) | [8, (5.7)] is kept; (S+R−2)/12 is verified with χ = R−1. |
| n23 | RESOLVED (partly, as decided) | p2: the companion paragraph is two sentences. |
| n24 | RESOLVED | p9: "Remark 1 (No linear families; a sketch)". |

### Resolutions table

Every row (N1/N2 through N10, and the bundled minors) matches the PDF under the Integers numbering. The notation changes are present: Π (p6), W(u,v) (p11), and (p,b,c) in Proposition 4 (p15).

### New problems in N

- **N-N1 (p9).** "and Z/12 does not occur [16, Theorem 2.8]" reads as unconditional, but p4 describes Theorem 2.8 under the hypothesis d₁(d₂−d₃)³ ≠ d₃(d₁−d₂)³. Fix: "under the hypotheses of [16, Theorem 2.8], Z/12 does not occur".
- **N-N2 (p11), cosmetic.** In "it is 0.608X at X = 4800", "it" could mean the secondary term. Fix: "the count is 0.608X at X = 4800".
- **N-N3 (p18).** "One command reruns every check." is unqualified, while A (p30) and B (p27) now qualify the same sentence (see X5).

---

## Cross-paper problems

- **X1 (main finding; B pp5–6, 7–8, against A).** Paper B's Table 1 and its in-statement citations use Paper A's old numbering. Several of the cited statements are no longer in A at all.

  | B cites | what the new A has | suggested fix |
  |---|---|---|
  | Theorem 2.1 "[30, Thm 2.3, Lemma B.1]" | A has no Lemma B.1 (Appendix B, p31, is only the AI placeholder and "Computations"); admissibility is A's Lemma 2.5 | → "[30, Thm 2.3, Lemma 2.5]" |
  | Lemma 2.2 "Lemmas 2.4, 2.5" | count = Lemma 2.4, hyperbolic term = Lemma 2.6 | → "Lemmas 2.4, 2.6" |
  | positivity/monotonicity of ϕ_k "Lemma 2.6" (p6; also "[30, Lemma 2.6]", p8) | σ_i > 0 and ϕ_k are in A's Lemma 2.7 | → "Lemma 2.7" |
  | Proposition 2.3 "[30, Prop. B.2]" (p8) | A no longer contains enveloping remainders; Prop. B.2 was deleted (this was the A1 resolution) | Drop the attribution. In Table 1, mark the row "not in [30]; proved in Appendix A". |
  | cone polynomials / triangular expansion "Lemmas 2.8, 2.10" (p8) | Lemma 2.9 and Lemma 2.11 (2.8 is a Proposition, 2.10 a Remark) | → "Lemmas 2.9, 2.11" |
  | p5 "Lemma 3.3 … consequence of [30, Lemmas 2.10 and 3.3]" | Lemma 2.11 and Lemma 3.3 | → "[30, Lemmas 2.11 and 3.3]" |
  | Theorem 3.2 "[30, Cor. 3.5, Thm 3.8]" / Table 1 "Theorem 3.8(i)" | Corollary 3.5 is correct for (i). A's Theorem 3.8 is the Descartes bound, has no part (i), and A contains no "orders ≤ M and c₁..c_M shared ⇒ equal" statement (searched) | Cite only Corollary 3.5 for (i). Mark (ii) "not in [30]" (it is proved in Appendix A, p30). |

  Lemma 3.3 [30] and Theorem 2.3 [30] are correct. A consequence: B's claim that Table 1 lists the results "with their place in that paper" is currently false for 5 of its 7 rows. A's planned "no change" on a61 (renumbering would break cross-citations) was overtaken by the restructuring, and B was not updated.
- **X2 (B p5 and p19, against A S p5).** The eigenvalue counts for the family O_ϑ disagree:
  - B says the companion "reports all the eigenvalues computed (about 2850 and 5800 per orbifold)", and B Table 6 lists 5805–5815 per member.
  - A's supplement (S3, S p5) says "about 5450 eigenvalues each up to λ ≈ 1.6 × 10⁴".

  Either A reports only those below 1.6×10⁴, in which case B's "that paper reports all the eigenvalues computed" is false, or one of the numbers is wrong. The 2850 figure agrees (A S p2, A p28). Fix: make A's S3 say "about 5800 eigenvalues each (about 5450 below λ ≈ 1.6×10⁴)", or change B to "reports the eigenvalues below 1.6×10⁴".
- **X3 (A p29 l.820 and S p5, against B p19/p26).** A states as fact that the family systoles "are 4b(ϑ)" and derives pairwise non-isometry from them. B (b3) says 4b is a "numerical identification", and B's Proposition 8.5 proves only ℓ ≤ 4b. Fix in A: "computed systoles 4b(ϑ)", and base non-isometry on the distinct λ₁ (a48).
- **X4 (bibliographic status).** A [20] lists the note as "Companion manuscript, in preparation (2026)". B [31] lists it as "Preprint, [PLACEHOLDER: preprint identifier]". The note cites A as a preprint with a placeholder. Fix: make A [20] match B [31] (preprint with placeholder). Separately, B says A was "submitted at the same time", but A never cites B; consider a one-line mention in A.
- **X5 (reproducibility sentence).** The three papers now say different things:
  - A p30: "One command … reruns every check (with --quick … --full …)".
  - B p27: "One command reruns every check except the finite-element solves, which it reruns only on request".
  - Note p18: "One command reruns every check."

  Fix the note: "One command reruns every check; the full enumerations are run with a separate flag (see the repository)", worded to match the repository.
- **X6 (overlap, A10).** Both A (Proposition 5.9, S ≤ 4800 with 783 explicit pairs) and the note (Table 2, complete to S ≤ 4800) report the same enumeration, and neither says so. Fix: one sentence in A's §5 noting that the enumeration underlying Proposition 5.9 is also the one tabulated in [20].

**Checked and consistent across the papers:**
- C_{27/2}: rank 0, torsion Z/2×Z/6, 12 points, Selmer orders (4,1). This appears in A Theorem 5.10 and in the note on p13.
- The minimal pair (2,8,8), (3,3,12), with S = 18 and R = 3/4.
- B's "supplement of [30] tabulates the convergence in h and p", which matches A S p2–3.
- B's count with the diameter, which matches A Lemma 2.4.
- The note no longer cites A by theorem number, so no "Appendix E there" or "Theorem 5.8" dangles.

---

## Summary

The note is in good shape. All ten major items and every applicable minor item are resolved, the three no-change reasons hold, and only a hedge on a cited torsion result (N-N1) and a reproducibility sentence (X5) remain.

Paper B resolves its mathematical majors B1–B7. The new diameter-free count and all of Tables 2–4 and 6 recompute exactly, and the required honest framing is intact. B8 (Theorem 7.1 still uses the plain budget) and several minors are partly done (b1, b4, b13, b17, b32, b37, b41). Five planned remarks or fixes were not made: b5, b14, b15, b23, and the N_obs column of b41. There is also a convention error in Remark 6.3 (ĝ against g).

Paper A was restructured rather than patched. A1–A3 are resolved by deleting the contested material, A6, A8 and A9 are resolved, A4, A7 and A10 are partly resolved, and A5 is not resolved: the "disc of radius √t" opening survives on p2. About fifteen minor items remain open (a11, a20, a26, a32, a33, a35, a36, a48, a49, a50, a54, a63, among others). Every figure caption exceeds the two-sentence limit, the abstract math is bold, and the "(Appendix B)" reference is broken.

The most consequential new problem is X1. A's restructuring silently broke Paper B's Table 1 and its bracketed citations of A: five of seven rows point to renumbered or deleted results, including Proposition B.2 and Lemma B.1, which no longer exist, and a "Theorem 3.8(i)" that does not state what B attributes to it. This must be fixed in B before submission, together with the eigenvalue-count mismatch X2 (about 5800 against about 5450).
