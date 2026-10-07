<!-- Saved verbatim by the main session from the reviewer's returned text: the harness refused the reviewer's own write. Scripts (scratch/code/), PARI checks (scratch/.venv) and page renders (scratch/pages/) are in its git-ignored scratch/. -->

# Editor's assessment: "How much of a hyperbolic orbifold does heat hear?" (Annals of Global Analysis and Geometry)

Material read: the manuscript (39 pp.) and its supplement (14 pp.), both read in full. I viewed the rendered images of every page with a figure (pp. 2, 3, 4, 14, 19, 22, 23, 26, 27, 30, 31). I also read the two disclosed companions, Paper B, "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (23 pp.), and the arithmetic note, "Triples with equal sum and equal reciprocal sum" (12 pp.), but only to judge overlap. Page numbers below are the printed page numbers of the manuscript unless marked "Supp." or "B".

## Summary

The paper takes closed orientable hyperbolic 2-orbifolds whose singular points are cone points. It asks how many coefficients c_1, ..., c_k of the small-time heat-trace expansion are needed to determine the signature (genus and multiset of cone orders).

The key structural fact (Prop. 2.7, Lemmas 2.8 and 2.10, pp. 9–10) is this: at curvature −1 the j-th invariant adds exactly one new odd power sum Σ m_i^{2j−3} of the cone orders, alongside the area and R = Σ 1/m_i. Comparing two signatures therefore becomes an odd-power Prouhet–Tarry–Escott (PTE) system with a reciprocal-sum constraint. The results are:

- **Theorem 1.1 (p. 3).**
  - (i) The first ⌊Area/π⌋+4 invariants always determine the signature (Thm 3.4 and Cor. 3.5), and no area-independent number does (Thm 3.12).
  - (ii) The worst-case count f(A) lies between about √(A/6π) and A/π. Linear growth of f is equivalent to N(k) = O(k) for the PTE function (Thm 3.13, Prop. 3.14).
  - (iii) With cone orders at most M, exactly M invariants are needed and suffice. Against all of Sig, M + ⌈½ log(2⌊A/π⌋+8)⌉ suffice (Thm 3.7).
  - (iv) Among n-pointed spheres, n invariants suffice (Theorem A, with Theorems B and C for the linear system and the fibres).
- **Theorem 1.2 (p. 4).** On triangle orbifolds, two invariants suffice up to cone-order sum 17. They first fail on O(2,8,8) and O(3,3,12). This pair, and its scalings, is isolated because the curve C_{27/2} has rank 0 (Thm 5.8, proved by hand in App. C). Three invariants always suffice.
- **Theorem 1.3 (p. 4).** Explicit stability estimates for recovering the orders from approximate c_1, ..., c_n (Section 6).
- **Other material.** Section 4 records that the heat expansion cannot see the moduli and isolates the t^{−1/2}e^{−ℓ²/4t} geodesic term. Section 7 tests everything on computed spectra.

## Significance

**What is good, plainly:**
- The question is cleanly posed and honestly scoped. The authors say repeatedly that orbifolds with different signatures have different spectra, so these are statements about finite jets of the short-time expansion, not about spectral rigidity (pp. 2, 5).
- Theorem 3.7 is a pleasant, sharp result: M invariants for orders at most M, and M−1 do not suffice, with an explicit Lagrange-weight construction. It also gives the right reading of the growth: the growth is carried by large cone orders.
- Reducing the growth exponent of f(A) to the PTE function (Thm 3.13(d), Prop. 3.14) is a genuine structural insight, even though it relocates the problem rather than solving it.
- Theorem 1.2 sharpens precisely the remark of Dryden–Gordon–Greenwald–Webb [2, Rem. 5.16] that c "does not seem sufficiently strong". The isolation proof via a hand 2-descent is complete and checkable.
- The Descartes imbalance bound (Thm 3.10) and the Hurwitz/Orlando determinant (Thm B) are nice touches.
- The explicit pairs are real: I verified all of them (see below).
- Computational claims are clearly separated from proofs (App. D, p. 35). Reproducibility is exemplary.

**What limits significance for AGAG readers:**
- **Little geometric analysis beyond the entry point.** The geometric analysis is concentrated in Section 2 and App. B, and that material re-derives a known expansion (Uçar [14], at curvature −1; acknowledged on p. 9). Section 4 is "classical in substance" by the authors' own statement (p. 6 and p. 20).
- **Everything after Prop. 2.7 is algebra or number theory.** It concerns finite multisets (Newton identities, Vandermonde determinants, PTE, Descartes' rule, an elliptic curve) and numerical linear algebra. An analyst on singular spaces learns little new about heat kernels near cone points.
- **The method needs constant curvature.** The mechanism "one odd power sum per coefficient" uses constant curvature essentially. The variable-curvature case, where cone points couple to K(p) and ΔK(p) (p. 5), is mentioned but not attempted. That case is what would make the paper a geometric-analysis contribution.
- **The headline results are modest.** Theorem 1.1(i) is a short Newton-identity argument. Theorem 1.1(iii) is a Vandermonde determinant. Theorem 1.1(ii) leaves the exponent open between ½ and 1.

This is not a "routine compactness argument dressed up": the arguments are explicit and sharp where claimed. The risk is rather that referees judge the paper elementary and peripheral to AGAG's core. There is precedent for this kind of inverse-spectral orbifold paper in AGAG (Stanhope 2005; Abreu–Dryden–Freitas–Godinho 2008, both cited), so the topic is in scope.

## Correctness and what was recomputed (or checked)

I recomputed the following independently. My scripts are in scratch/code/ (heat.py, tableS1.py, triads.py, witness4.py, misc.py, misc2.py); the elliptic-curve checks used PARI through cypari2 in scratch/.venv. **Everything checked agrees with the manuscript.**

1. **Heat coefficients (Lemma 2.6, Prop. 2.7, Lemma 2.8, eq. (7), eq. (9), pp. 8–10).**
   - I implemented (4)–(5) from scratch. Then α_0, ..., α_4 = 1, −1/3, 1/15, −4/315, 1/315, and p_0, p_1, p_2 match (7).
   - The Taylor coefficients of the defining sum Φ_m match (4) to 10^−41 for m = 3, 5, 8.
   - Equation (9) holds symbolically.
   - The leading coefficient of p_l equals |B_{2l+2}|/(2(l+1)!(2l+1)) for l ≤ 4.
2. **Shared counts, computed exactly from the coefficients.** In every case the areas agree and the exact number of shared invariants is as claimed:
   - O(2,8,8)/O(3,3,12): L = 2.
   - Theorem C(3) pair: L = 3. P_3 = 31402 and P_5 = 25159618 ≠ 21298618 are confirmed.
   - Example 3.6: L = 2, s = 14/15.
   - Example 3.16(i): L = 3, s = 14/5. Example 3.16(ii): L = 3, s = 113/30.
   - (0;5,5,5)/(0;2,2,2,10): L = 2.
   - The M = 3 and M = 4 pairs after Thm 3.7 share M−1 invariants. The c_M differences are −1/3 and 1, as the formula (−1)^M C a_{M−2} predicts with C = 120 and C = 2520.
   - The Remark 3.2 exception (16,16,74,74)/(11,37,44,88): L = 3.
   - **All 20 pairs of Table S1 whose cone lists are printed (Supp. pp. 3–6)**, including the 44-digit L = 7 pairs: equal area, and shared exactly L for L = 2, ..., 7. Sizes 14, 18, 24, 40 and 16, 20, 26, 40 confirm the T(L) table on p. 19.
3. **Section 7 constants.** d_3, d_4, d_5 = 25/12, −1775/24, 153025/48 (p. 31). c_1, c_2, c_3 for both specimens match Table S6.
4. **Proofs checked by hand:**
   - Lemma 2.5 (including constant (3)).
   - Theorems A, 3.4 and 3.10.
   - Prop. 3.11 (the identity (1−2^{j+1}) for j = −1 gives equal R).
   - Thm 3.7(iii): the inequality 2M + (k−3)(k+1) > 0.
   - Lemma A.1 pigeonhole, and the lower-bound formula of Thm 3.13(a).
   - Prop. 6.6(i) formulas δR = s²/(4(64−s²)) and δP_3 = 48s².
   - Prop. 6.7.
   - Every residue computation of the 2-descent in App. C (p. 35).
5. **Theorem B (p. 11).** For (2,3,7), (2,8,8), (3,3,4,4) and (2,5,6,9,11), det M equals ς_n Π(m_i+m_j)/e_n exactly, and the true e solves (11).
6. **Section 6 constants.** amp_0, ..., amp_4 = 2, 14, 498, 4062, 56230/3, and the P_3 row (−18, −120, −360) (p. 28). ζ_3, ζ_4, ζ_5 = 1, 79/3, 14048/15. These are reproduced only with j ≤ n−2 in the maximum, which the definition on p. 28 leaves implicit (m9).
7. **Theorem 5.8 and App. C.**
   - ψ maps E into C_{27/2}: the composite equals 10800·(the equation of E).
   - Δ(E) = 2^18 3^8 5^6, and φ(1:4:4) = (−24, 360).
   - (16,400) is a flex: x³+393x²+3456x−(21x+64)² = (x−16)³.
   - PARI: conductor 90, torsion Z/6 × Z/2 generated by (−24,360) and (0,0), ellrank r_1 = r_2 = 0, analytic rank 0, #E(F_7) = #E(F_11) = 12.
8. **Section 5 by enumeration** (exact rational keys):
   - 83 hyperbolic triads with 10 ≤ S ≤ 18, and the only collision with S ≤ 18 is (2,8,8)/(3,3,12) (Thms 5.5–5.7).
   - The first-overlap formula S*(p) of Thm 5.4 agrees with direct computation for 2 ≤ p ≤ 29.
   - Table S2 (first collisions, p ≤ 14) is reproduced exactly.
   - The first non-adjacent collision is (5,15,15)/(7,7,21) at S = 35.
   - The list of 38 collision-free sums (Prop. S2.1) is reproduced exactly for 18 ≤ S ≤ 1200 (I did not go to 4800).
9. **Remark 3.2 at reduced range.** For 4-multisets with orders ≤ 130 I find 19 witnesses, 16 of them primitive, and no triple. The 8 primitive ones with orders ≤ 84 are exactly the list attributed to Chen's survey [20].
10. **Remark 3.17.** The real partner of {1,1,1,1,7} is {0.26636, 4.28304, 6.45060}, matching Supp. p. 2.
11. **Rendered figures.** I checked Figs 1–8 against the text: tick values, symbol placement and slopes. Fig. 2's discs and rings match X* for both pairs. Fig. 3's Prouhet squares sit at (s, L+1) as stated. Fig. 6's dots and circles match S*(p) and Table S2. Fig. 7's slopes are about 1, ½, ⅓ and ½. Fig. 8(a)'s truncation curves behave as described. **I found no sign error or typographical error in the mathematics.**
12. **References spot-checked.**
    - Schueth [8]: AGAG 69, article 2 (Crossref; online Dec. 2025).
    - Croot–Mao–Yip [37]: arXiv:2609.05061.
    - Chen [20]: arXiv:2506.11429.
    - An OpenAlex search found no prior paper that counts heat invariants needed for orbifold signatures.

**Not checked:** the 525-class exhaustive computation behind the dots of Fig. 3; the n = 4 search to 440 and n = 5 to 120; the modular search of Remark 3.17; the finite-element spectra of Sections S4–S6.

## MAJOR issues

**M1 (fit and significance; p. 5, §1.1, and the paper as a whole).** The geometric-analysis content stops at Prop. 2.7, a known expansion re-derived. Everything else is algebra of power sums, Diophantine geometry or numerical linear algebra. The paper must argue, in its first two pages, why the minimal number of heat invariants is a natural geometric-analytic quantity. The authors themselves note that different signatures are always spectrally distinguished, and that "no number independent of the area suffices" means in substance "no number independent of the largest cone order" (p. 5). They should also say what the results teach about heat asymptotics at cone singularities that was not already in [2, 14]. Without either:
- an extension beyond constant curvature (the coupling to K(p), ΔK(p) at orders t, t² recorded on p. 5 from Schueth [9]), or
- a sharper link to the conic heat-kernel literature (see m12),

a referee from AGAG's core may judge the paper peripheral. This is the main reason the desk-reject probability is not small.

**M2 (length, and whether every section earns its place; pp. 20–32, Supp.).** At 39 pp. plus 14 pp. of supplement, the paper reads in places as several papers stapled together:
- (a) separation and bounded orders (§3.1–3.3);
- (b) PTE growth (§3.4, App. A);
- (c) moduli invisibility (§4);
- (d) triangle orbifolds and an elliptic curve (§5, App. C);
- (e) stability (§6, S3);
- (f) numerics (§7, S4–S6).

Strands (a), (b) and (d) cohere, through the PTE/power-sum mechanism. Three sections earn their place least:
- **§4 (pp. 20–22).** Prop. 4.1 is immediate, Prop. 4.2 and Cor. 4.3 are standard Teichmüller facts, and Thm 4.4 is the classical McKean/Huber mechanism (the authors say so on p. 22). Theorem 4.4(a) has a constant they themselves call "qualitative" and "loose".
- **§6 (pp. 27–30).** It spends four pages proving a threshold δ_thm that is off by factors of 5×10² to 2×10⁸ (p. 30), while the sharp certificate is relegated to Supp. S3.
- **§7 (pp. 30–32).** By its own first sentence it is used in no proof.

Recommendation: reduce §4 to a remark of at most one page. Compress §6 to one theorem (ideally the sharp certificate, with δ_thm dropped or moved to the supplement). Move §7 entirely to the supplement. The target should be about 25–28 pp.

**M3 (depth of the headline theorems; pp. 3, 13–15).** Theorem 1.1(i) is Thm 3.4, a ten-line Newton-identity argument; "first explicit such number" (p. 5) is a modest claim. Theorem 1.1(iii) is a Vandermonde determinant. Theorem 1.1(ii) brackets the exponent between ½ and 1 and stops there. The introduction should say plainly which results are deep and which are bookkeeping. In my reading, the deeper ones are Thm 3.10, Thm 3.13(d) with Prop. 3.14, Thm B and Thm 5.8. The introduction should also stop presenting (i) and (iii) as the main theorem. A referee may otherwise conclude that the main theorem is elementary.

**M4 (overlap with Paper B; A §2–3 against B §2–3 and §7).** About 5–6 pages of the submission reappear in B, mostly verbatim:

| Paper A | Paper B |
|---|---|
| Thm 2.3 (p. 7) | Thm 2.1 (p. 4) |
| Lemma 2.4 (p. 7) | Lemma 2.2 (p. 4) |
| Lemma 2.5 (p. 8) | Lemma 2.3 (p. 5; B adds a global bound) |
| Lemma 2.6 (p. 8) | Lemma 2.4 (p. 5) |
| Lemma 2.8 (p. 9) | Lemma 2.8 (p. 7) |
| Lemma 3.1 (p. 10) | Lemma 3.2 (p. 8) |
| Lemma 3.3 (p. 13) | Lemma 3.1 (p. 8) |
| Thm 3.4 / Cor. 3.5 (p. 13) | Thm 3.3 (p. 8) |
| Thm 3.7(i) with proof (p. 14) | Thm 3.4 (p. 8) |
| Lemma B.1 (p. 34) | Appendix A |
| App. B moment computation (p. 34) | Lemma 2.5 (p. 6) |

In addition:
- **Shared data.** The same computed spectra (O(2,8,8), O(3,3,12) and the (0;3,3,3,3) family) are used in both papers. The reported ranges differ:
  - Supp. S6 says the family was computed to about 5450 eigenvalues up to λ ≈ 1.6×10⁴, with double windows; B p. 15 says 815–856 eigenvalues, complete up to λ ≈ 2440–2560.
  - A says about 2850 eigenvalues per triangle orbifold; B says about 2000, complete below 1.6×10⁴. This is consistent with Weyl's law, but it is not explained.
- **No proof dependence.** Neither paper depends on the other for a proof; I confirmed this for A. The split (heat invariants / eigenvalues / Diophantine counting) is sensible in principle.
- **Effect on review.** A's Thm 3.7(i) is the key arithmetic input of B (its Thm 3.4 and Lemma 3.5). Two sets of referees would review the same lemmas.

The authors should keep the full proofs in one paper and state and cite them in the other. They should also reconcile and explain the two datasets, and update the status of B (p. 5 says "in preparation", but B has been submitted). This is not salami-slicing of results, but it is unacceptable duplication of text as it stands.

**M5 (presentation density; throughout, especially pp. 10–18 and 27–30).** The prose is compressed to the point of opacity. Many proofs are two or three lines carrying heavy computations (Thm B p. 11, Thm 5.4 pp. 24–25, Thm 6.5 p. 29, Lemma 2.5 p. 8). The notation load is very high: K_iso, K_mult, Sig, Sig_0, Sig_{0,n}, Sig_≤M, f, f_g, f_n, f_M, T, T_g, A_min, N, ι, ϱ, I_n, Ψ_k, C_l, Ξ_µ, ζ_n, r_n, amp_r, cond and others. The labelling also mixes lettered theorems (A, B, C) with numbered ones. The introduction (pp. 1–6) carries digressions:
- the DGGW erratum (p. 2);
- the orientability paragraph (p. 3), which makes a claim ("heat invariants cannot hear orientability") with a one-sentence justification about orbifolds outside the class studied.

A notation table and a slower §3 are needed for AGAG readers.

## MINOR issues

- **m1 (p. 3, Thm 1.1(iii); p. 14, Thm 3.7(iii)).** The base of "log" is not stated. The proof uses the natural log; say so.
- **m2 (p. 5 and p. 6).** Both companions are called "in preparation". B has been submitted, so give its status and a reference.
- **m3 (p. 19, Example 3.16(ii)).** "L = 3, 7 against 8 cone points" reads as "L = 3 and 7". Write "L = 3, with 7 against 8 cone points".
- **m4 (p. 12, Theorem C(3)).** "this pair is [20, (A.685)]" is good. Also state on p. 6 that Theorem C(1) forward direction is in [20], which is done, and that the remaining seven listed witnesses are not new.
- **m5 (p. 17, Theorem 3.12).** The smaller genus "can be any prescribed integer g ≥ 2". Say why g = 0 and g = 1 are not claimed: the base construction has g_0 ≤ 2 (App. A, p. 33).
- **m6 (p. 18).** The table header "2L+2 ≤ T(L)" is typeset as a row label and is hard to parse. Use two labelled rows "lower bound" and "upper bound".
- **m7 (p. 30, Thm 6.8 and the text after it).** Stating a theorem that is loose by up to 2×10⁸, while the sharp certified bound sits in the supplement, inverts priorities (see M2).
- **m8 (pp. 35–36, App. D).** This appendix duplicates Supp. S7. Keep one copy, preferably S7, and keep the list of "statements that rest on computer search alone", which is valuable, in the main text.
- **m9 (p. 28, definition of ζ_n and r_n).** The range of j in the maximum is implicit. My recomputation reproduces ζ_4 = 79/3 and ζ_5 = 14048/15 only with j ≤ n−2, the rows of M. State the range.
- **m10 (p. 5).** "That some finite number of heat invariants suffices for each area follows" needs the full-sequence result of Uçar [14] or Thm 3.4 to be cited at that point. Make the logic explicit.
- **m11 (p. 26 and Supp. Prop. S2.1).** The statement about 38 collision-free sums up to 4800 is the same enumeration as in the arithmetic note (§6.1). Cite the note for it rather than restating it.
- **m12 (p. 5, §1.1; p. 8, §2.2).** The cone-point coefficients for a flat cone of angle 2π/m, beginning with (m²−1)/(12m), and the Sommerfeld-type sum over rotations that defines Φ_m are classical in the conic heat-kernel literature: Cheeger; Brüning–Seeley; Dowker; Bordag–Kirsten–Dowker. The paper cites none of it. AGAG readers will expect it, and it bears on M1.
- **m13 (p. 22, after Thm 4.4).** "the experiment in the supplement shows that it is loose" should say by how much.
- **m14 (p. 32, Data and code availability).** The repository lives under a GitHub account ("Ali-M658") whose name matches none of the authors. Archive under the (pending) Zenodo DOI, and cite the DOI as the primary source in all three papers.
- **m15 (Supp. p. 12, S5).** The protocol cites a commit hash and date. Keep this in the archived record and cite the DOI rather than the commit.
- **m16 (B p. 4, as it affects A).** B says A "contains a sharper and more general form of Theorem 3.4 below". A's Thm 3.7(i) is identical; what is sharper is Thm 3.7(iii). Coordinate the wording.

## Presentation (figures and captions included)

- **Fig. 1 (p. 2).**
  - The heat-kernel values are computed on the true triangle but drawn on a "schematic" shape at the same Poincaré coordinates (p. 4). This is confusing; either draw the true triangles (as Fig. 5 does) or drop the figure.
  - The colour bar is logarithmic but not labelled as such.
  - The symbol 𝔥_t (heat kernel) sits uncomfortably close to h_t(r) = e^{−t(1/4+r²)} of §2.1 (p. 7).
- **Fig. 2 (p. 14).** Correct and useful. The caption should say that (a) uses the orbifolds' colours and (b) uses black and grey. At present that is only in the text (p. 13).
- **Fig. 3 (p. 19).**
  - The caption is two lines. The meaning of the dots, diamonds, open squares, split disc, solid curve and dashed curve is given only in the body text (p. 19). Move it into the caption or a legend.
  - The solid curve leaves the frame at s ≈ 12; note this.
  - The dots for s ≤ 7/5 overprint heavily; an inset would help.
- **Fig. 4 (p. 22).** Good. The square-root scale is stated in the text only; put it in the caption.
- **Fig. 5 (p. 23).** Fine.
- **Fig. 6 (p. 26).**
  - There is no key telling which band is which p. Shade order is described only in the text (p. 25).
  - The p = 5 circle at S = 117 sits on the right frame edge.
  - At p = 4 the dot is hidden under the circle. That is intended, but say so in the caption.
- **Fig. 7 (p. 30).** No legend, and the caption does not identify the curves. Which curve is (2,3,7), (2,8,8), (4,4,4) or the realisable family, and what the diamonds and the horizontal line mean, is stated only on p. 29. This must go into the caption or a legend. The y-label ‖m̃ − m‖_∞ should match the dist(·,·) defined on p. 27.
- **Fig. 8 (p. 31).** The text (p. 32) says the predicted term is "thin and dashed", but the plotted lines look dotted. The caption should explain the shaded band and the circles.
- **Abstract and introduction.** Very dense. The abstract packs the content of five theorems into ten lines. Shorten it and lead with the cleanest results (Thm 3.7 and Thm 1.2).

## Overlap with the disclosed manuscripts

- **Paper B.** There is substantial textual duplication of preliminaries and of the bounded-order theorem (detailed in M4, about 5–6 pp.), and the same numerical datasets are reused with unexplained differences in range. A does not depend on B for any proof. B depends on material that A also proves, but proves it again itself. The scientific split is sensible: A asks how many heat invariants are needed; B asks how many eigenvalues are needed, effectively. The duplication should be cut to statements with citation in one direction. The editors handling A and B should be told about each other's submission.
- **Arithmetic note.** Overlap is small and appropriate. A proves the isolation of the minimal pair (Thm 5.8, App. C); the note cites A for it and does not reprove it. The note's Section 2–3 shares the Bremner–Guy–Nowakowski set-up with A's §5.2. The enumeration behind Prop. S2.1 and p. 26 is the note's enumeration and should be cited as such (m11).
- **A stale cross-reference in the note.** The caption of the note's Table 1 (p. 8) cites "[7, Theorem 6.8]" for C_{27/2}. In A, Theorem 6.8 is the stability threshold; the isolation result is Theorem 5.8, as the note's own introduction (p. 1) correctly says.
- **Salami-slicing.** No result of A is proved twice across the three manuscripts in a way that creates double credit, except the shared lemmas listed in M4. A stands on its own.

## Recommendation

- **Decision:** send to review. This is not a desk reject. It is a borderline call on fit (M1) and length (M2), not on correctness, and the mathematics I could check is sound.
- **Desk-reject probability:** 0.30.
- **Expected referee outcome:** accept 0.03, minor revision 0.12, major revision 0.50, reject 0.35.
- **Confidence:** moderate (about 0.65) on the recommendation. High (about 0.9) that the verified statements are correct. Lower (about 0.5) on how AGAG referees will weigh significance.
- **Choice of referees:** one inverse-spectral or orbifold referee (Dryden, Gordon or Stanhope school) and one referee comfortable with power sums and PTE. Referees should be told that Paper B has been submitted elsewhere, and given M4.

## What resolves each issue

- **M1.** Rewrite §1 and §1.1 to argue directly why the finite-jet count is a natural geometric-analytic quantity. Either add a variable-curvature result, even a partial one (for example: does Thm 3.7 survive when the curvature near each cone point is known?), or connect explicitly to the conic heat-kernel literature and state what the paper adds to it.
- **M2.** Cut §4 to at most one page. Replace §6 with one stability theorem (preferably the sharp certificate) and move the rest to the supplement. Move §7 to the supplement. Target 25–28 pp.
- **M3.** Re-rank the results in the introduction so that the deeper results lead: Thm 3.13(d) with Prop. 3.14, Thm 3.10, Thm B and Thm 5.8. Describe Thm 3.4 and Thm 3.7(i) accurately as elementary consequences of the structure in §2.3.
- **M4.** Keep the proofs of the trace formula, Lemmas 2.4–2.8 and Thm 3.7(i) in one manuscript only, and cite them in the other. Reconcile and document the eigenvalue datasets: ranges, solver versions, and why B uses truncations. Update the companion status on p. 5. Notify both handling editors.
- **M5.** Add a notation table. Expand the proofs of Thm B, Thm 5.4 and Thm 6.5 to readable length. Number all theorems in one scheme. Move the erratum and orientability digressions out of the introduction, and either prove the orientability claim or drop it.
- **m1.** State natural log. **m2.** Update companion status and references. **m3.** Rephrase Example 3.16(ii). **m4.** Attribute the known witnesses on p. 6 as well. **m5.** Explain the range of g in Thm 3.12. **m6.** Relabel the T(L) table. **m7.** Swap δ_thm and δ_cert (see M2). **m8.** Remove the duplicated App. D. **m9.** State the range of j in the definition of ζ_n. **m10.** Make the finiteness argument on p. 5 explicit. **m11.** Cite the arithmetic note for the enumeration. **m12.** Add the conic heat-kernel references. **m13.** Quantify "loose". **m14.** Make the Zenodo DOI the primary data source and note the repository ownership. **m15.** Cite the DOI rather than the commit. **m16.** Coordinate the cross-description with B.
- **Figures.** Put full keys in the captions of Figs 3, 6, 7 and 8. Fix Fig. 1 (true shapes, log colour bar). Fix the "dashed"/dotted wording for Fig. 8.
- **Arithmetic note (for the authors' information).** Correct "[7, Theorem 6.8]" to "[7, Theorem 5.8]" in the caption of its Table 1.
