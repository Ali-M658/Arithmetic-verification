<!-- Saved verbatim by the main session from the final message of reviewer A-a: the harness refused the reviewer's own write. Text from the report's first heading on; the reviewer's preceding cover note was dropped. -->
# Handling-editor report: Annals of Global Analysis and Geometry

The tool environment would not let me write `REPORT.md`, so the complete report is below. My scripts and page renders are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-5/A-a-editor-aga-handling/scratch/` (`check1.py` to `check5.py`, `fastheat.py`, `renders/`).

**Submission:** "How much of a hyperbolic orbifold does heat hear?" (P. Gang, A. Agadi, A. Veluri, J. Wang, J. Barreto, A. Chouthaiwale). Main text 44 pp. plus Online Resource 1 (18 pp.).

**Disclosed related manuscripts (not under review):**
- (B) "Finitely many eigenvalues determine the signature of a hyperbolic orbifold".
- (N) "Triples with equal sum and equal reciprocal sum".

**Editor's standpoint.** My own work is on spectra of hyperbolic surfaces over moduli space: random and large-genus surfaces, Weil–Petersson volumes and spectral gaps. I read the whole manuscript and supplement, and the parts of B and N that bear on overlap. I looked at the rendered pages of every figure and of each page cited below. Per the instructions, length is out of scope, and I treat the three marked placeholders (author contributions, AI-use statement, Zenodo DOI) as known.

## Summary

Let O be a closed orientable hyperbolic 2-orbifold with cone points, and let c_1, c_2, ... be the coefficients of its small-t heat-trace expansion (the heat invariants). The paper asks how many of them are needed to determine the signature (g; m_1, ..., m_n), that is, the genus and the multiset of cone orders.

The starting point is a closed form of the cone coefficients at curvature −1. It is stated as Prop. 2.7 and derived again in App. B from the Selberg trace formula. In this form each new heat invariant adds exactly one new odd power sum P_{2l+1} of the cone orders, with a nonzero top coefficient (Lemma 2.10). This is Uçar's induction mechanism, here used with finitely many coefficients. Through it, a collision of heat invariants becomes a signed multiset whose low odd moments and reciprocal sum vanish (Lemma 3.3, Def. 3.10).

The main results are:
- **Bounded orders (Thm 1.2 / 3.8).** If all cone orders are at most M, the first M invariants suffice within that class and the first M+1 against all of Sig, whatever the area.
  - Both numbers are sharp, shown by explicit constructions with Lagrange weights.
  - The proof uses a sign-change argument of Descartes type (Lemma 3.7).
- **Growth (Thm 1.1 / 3.14, Prop. 3.15).** The worst case f(A) over orbifolds of area at most A satisfies ≍√A ≤ f(A) ≤ A/π + 4.
  - A power-law lower bound f ≥ cA^α holds exactly when N(k) = O(k^{1/α}), where N is the Prouhet–Tarry–Escott function.
  - So linear growth is equivalent to the open problem N(k) = O(k).
- **The algebra of a collision (Thm 1.3, Thms A–C, 3.11).**
  - For spheres with n cone points, n invariants suffice.
  - The orders are recovered from a linear system whose determinant is a Hurwitz/Orlando product.
  - Changing the genus costs invariants, by a Descartes bound.
- **Triangle orbifolds (Thm 1.4, §5).**
  - Three invariants always suffice, and two suffice when p+q+r ≤ 17.
  - The first failure is O(2,8,8) and O(3,3,12).
  - This pair is isolated, because C_{27/2} is an elliptic curve of rank 0 with torsion Z/2 × Z/6.
- **Other material:**
  - a discussion of variable curvature (§2.4, Props 2.11–2.12, whose proofs are labelled "Sketch");
  - where the moduli enter the heat trace (§4), illustrated with computed spectra;
  - a stability theorem for recovering the orders from approximate invariants (§6), with explicit constants and certificates in the supplement;
  - open problems (§7).

## Significance

**What is good.**
- The question is well posed. The answer for bounded cone orders (M+1, sharp, independent of the area) is clean and, as far as I know, new.
- The reduction of the growth question to the Prouhet–Tarry–Escott problem is a genuinely interesting bridge.
  - The constant-factor comparison T(L) ≍ N(2L−2) in Prop. 3.15 is done carefully.
  - The paper is honest that it "relocates the growth question … without settling it".
- The triangle-orbifold section is complete and pleasant: an exact threshold of 17, a unique minimal pair, and an arithmetic isolation theorem. It answers precisely the remark of Dryden–Gordon–Greenwald–Webb [2, Rem. 5.16] that their invariant "does not seem sufficiently strong to distinguish" triangular pillows.
- Appendix B is a small but useful tool for analysts. It derives the full expansion from the trace formula alone, with remainders that bracket the truth (Prop. B.2).
- Computational claims are labelled carefully as exact, search-only or a-posteriori numerical. This is better than most submissions I handle.

**Reasons for caution, from AGAG's point of view.**
1. **Where the analysis sits.**
   - Once Prop. 2.7 and Lemma 2.10 are in place, Theorems 1.1–1.4 are statements about power sums, Newton identities, Descartes' rule, PTE configurations and one elliptic curve. Prop. 2.7 and Lemma 2.10 are a re-derivation of Uçar's expansion and his induction.
   - The authors say as much themselves ("What is elementary and what is not", p. 5).
   - The unconditional growth bounds come from elementary arguments: pigeonhole plus doubling below, Newton's identities above.
   - The global-analysis content consists of the trace-formula appendix, §4 and §2.4. Section 4 is largely classical: Corollary 4.1 and the exponent in Thm 4.2 are standard, as the text acknowledges. Section 2.4 is only sketched.
   - An AGAG referee will ask what an analyst learns here that is not a statement about multisets of integers.
2. **The headline growth theorem is conditional.** It is an equivalence with an open Diophantine problem, so the growth rate of f is not determined.
3. **The interesting regime is far from where most global analysis on hyperbolic surfaces happens.**
   - By Thm 1.2 the count is at most M+1 for bounded cone orders. For surfaces (no cone points) Kmult ≤ 2 trivially (p. 19).
   - So the large-genus and random-surface regime is trivial for this question. All growth comes from huge cone orders on genus at most 2 (Cor. 3.9, Thm 3.13).
   - That is legitimate, but it makes part of the audience arithmetic.

On balance the paper is within AGAG's scope. Inverse spectral problems for orbifolds recur in AGAG: Stanhope 2005, Rossetti–Schueth–Weilandt 2008, Abreu–Dryden–Freitas–Godinho 2008 and Schueth 2026, all cited. Its significance for AGAG readers is moderate. It is suitable for review, provided the introduction makes the analytic contribution explicit (M1).

## Correctness and what was recomputed or checked

I did not referee every proof line by line; that is for the referees. I checked the following, using exact arithmetic (Python fractions and sympy).

**Recomputed exactly, all in agreement with the manuscript:**
- **Heat-invariant formulas.**
  - The values α_0, ..., α_4 = 1, −1/3, 1/15, −4/315, 1/315 of Prop. 2.7.
  - The polynomials p_0, p_1, p_2 of (8), and p_3, from (4)–(5).
  - The leading coefficients |B_{2l+2}|/(2(l+1)!(2l+1)) of Lemma 2.8.
  - A direct series expansion of Φ_5, compared against (4).
  - The triangle formulas (10).
- **Collision examples.** I recomputed the number of shared invariants from the cone coefficients.
  - O(2,8,8) and O(3,3,12) share exactly 2. The differences d_3 = 25/12, d_4 = −1775/24 and d_5 = 153025/48 (p. 27) are exact.
  - (0;2^10) and (1;4^4) share exactly 2, with area 6π.
  - (1;15) and (0;3,3,5,5) share exactly 2.
  - (1;3^9) and (0;2^16) share 2.
  - (0;2^28,4^8) and (1;3^27) share 3.
  - (0;3,10,15,30) and (0;4,5,21,28) share 3, with the printed R, P_1, P_3 and P_5.
  - Both pairs of Ex. 3.17(i)–(ii) share 3, with the printed areas.
  - (0;5,5,5) and (0;2,2,2,10) share 2.
  - (2;) and (0;2^8) share 1.
  - The Prouhet L = 2 pair of Table S1 shares 2.
  - The L = 4 genus pair and the L = 4, 5 cone-count pairs of Table S1 share exactly 4, 4 and 5.
- **Theorem 3.8.**
  - For M = 2, ..., 9 I recomputed C, ν(a), s and the areas of the least-g pairs. All agree with the list 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054}.
  - The case (iv) with M = 2 and X = 4 also agrees.
  - So do the differences in c_M for M ≤ 5.
- **Theorem B.** The determinant ς_n ∏(m_i+m_j)/∏m_i is exact on six multisets with n = 3, 4, 5.
- **Section 6.**
  - The values amp_0, ..., amp_4 = 2, 14, 498, 4062, 56230/3.
  - The relation P_3 = −18c̃_1 − 120c̃_2 − 360c̃_3.
  - The variations δR and δP_3 in Prop. 6.3(i), and the constant in Prop. 6.4.
- **Section 5.**
  - There are 83 triads with 10 ≤ S ≤ 18, and the only collision among them is at S = 18.
  - S*(p) of Thm 5.4 is correct for p = 2, ..., 14.
  - Every entry of Table S2 is correct.
  - The 38 collision-free sums of Prop. S2.1 are confirmed: my exhaustive enumeration up to S = 700 gives the identical list.
  - (5,15,15) and (7,7,21) do collide, with R = 1/3.
- **Theorem 5.8.**
  - ψ maps E into C_{27/2}, and φ∘ψ = id, both checked symbolically.
  - All listed points lie on the curves.
  - Δ_E = 2^18 3^8 5^6, and #E(F_7) = #E(F_11) = 12.
  - The tangent line at the flex is as stated.
  - The values c' and d' in S7 are correct.
  - PARI was not available. LMFDB's curve **90.c3** has the same j-invariant, rank 0 and torsion Z/2 × Z/6, and its point counts agree with those of E at all 11 primes from 7 to 43. So E appears to be 90.c3, which confirms rank 0 and the torsion.
- **Hand-checked arguments.**
  - Lemmas 2.4 and 2.5, including the constant (3).
  - The beta-integral step and the moment identity in App. B, and Lemma B.1.
  - The sign bookkeeping in Thms 3.4 and 3.11, and the Lagrange-weight argument of Thm 3.8.
  - Lemma A.1 and Prop. 3.12.
  - Thm 3.14(b)–(c).
- **Section 2.4, internal consistency only.**
  - The β_{l,l+1}, at constant curvature and for l = 1, 2, 3.
  - Prop. 2.11(iv) against (ii) and (iii), including Π_4(3) = 2/243.
  - Schueth's term −m⁵∆K/15120.
  - The example in Prop. 2.12(ii).
- **Cross-document consistency.**
  - The eigenvalues in Table S5 match B's Table 5.
  - The systoles and the complete eigenvalue ranges match B's Table 4.

**Not checked:**
- The hand 2-descent in S7 line by line. The LMFDB cross-check makes it moot for correctness.
- Theorems S3.2–S3.5.
- The finite-element computations.
- The searches in Remarks 3.2 and 3.18.

**Verdict.** I found no mathematical error in what I checked. There is one false boundary case (m1) and one mis-statement of the main theorem in the abstract (M3).

## MAJOR issues

**M1. The analytic contribution is not made explicit enough for AGAG (pp. 1–6, §§1.1–1.2, p. 5).**
- After Lemma 2.10, every main theorem is a theorem about multisets of integers.
- The introduction calls the count "the part of the cone data that diffusion resolves before geometry enters". But the paper never turns a count into a statement about the heat trace at positive time, or about eigenvalues.
  - That link is deferred to manuscript B.
  - Within this paper it appears only in §6, which takes heat invariants, not traces, as its data.
- Prop. B.2 and (6) are the natural place where this paper itself connects its counts to heat traces, but they are presented as a technical appendix.

**M2. Section 2.4 states Propositions whose proofs are "Sketches", partly confirmed by computer (pp. 11–14).**
- Prop. 2.11(i)–(iii) are claimed for all l, but:
  - the sketch of (i) relies on following Schueth's substitution "to all orders";
  - (iii) rests on an unstated Duhamel computation;
  - (iv) is described only as "an exact computation";
  - the closing sentence, that an independent computation "confirms … (iii) for every l", does not say how.
- Prop. 2.12(ii) rests on two unproved steps:
  - an asserted second-order Duhamel formula for ω_n;
  - a claimed non-vanishing of a Jacobian and generalised Vandermonde determinant.
- The introduction (p. 3) uses this section for a substantive claim, "the setting of constant curvature is essential", and Problem 5 is built on it.
  - Prop. 2.12(iii), which carries that claim, is nearly complete.
  - Props 2.11 and 2.12(i)–(ii) are not proofs.

**M3. The abstract mis-states Theorem 1.1(ii) (p. 1).**
- The abstract says f grows "like a power A^α … exactly when N(k) = O(k^{1/α})". Read literally this is false.
  - N(k) = O(k) implies N(k) = O(k^{1/α}) for every α ≤ 1.
  - The sentence would then assert growth like A^α for all α at once.
- The theorem itself, and Thm 3.14(d), correctly state a *lower-bound* equivalence, f(A) ≥ cA^α ⇔ N(k) ≤ Ck^{1/α}, plus a one-way upper statement.
- The body of the paper is correct (p. 3: "whether f grows like a power of A at all is open").

**M4. Parts of the proofs of headline results appear only in the supplementary material.**
- The rank-0 claim in Thm 5.8, which is the stated "reason" in Thm 1.4(iii), is proved only by the hand 2-descent in Supplement S7, besides PARI's `ellrank`.
- The constants and proofs behind Thm 6.2 are Theorems S3.2–S3.4.
- Supplementary material is not copy-edited and often gets less scrutiny from referees. I will tell the referees that S3 and S7 are part of the refereed proof.
- The authors should make this dependence explicit in the proofs.
- They should also cite LMFDB 90.c3 as an independent confirmation, after confirming the identification.

**M5. The boundary with manuscript B must be made explicit before review.**
- Both manuscripts share:
  - the trace-formula set-up;
  - Lemmas 2.4–2.5 and Prop. B.2;
  - the heat data of a signature;
  - the *same* computed spectra, with near-verbatim descriptions of the numerical method (S4/S6 here, B §7.1).
- Thematically, A §6 together with S5 (deciding the signature from approximate data, certificates, blind recovery) and B's Thm 7.1 are two versions of one programme.
- The disclosure is good (A p. 5; B Table 1), and nothing in A depends on B.
- Still, the referees of each paper must be able to see the other, and the cover letter should say what each contributes that the other does not.

## MINOR issues

- **m1.** Prop. 2.12(ii), p. 13: "For any L" is false at L = 1, since H_1 = c_1 only, so it should read L ≥ 2.
- **m2.** Fig. 3, p. 24: the diamonds and squares are drawn at Kmult = L+1, but they are only lower bounds. Sharing exactly L invariants with one partner gives Kmult ≥ L+1. Also, the sentence "the open question lies between the two step curves" should note that the constructed pairs lie above the dashed curve.
- **m3.** Thms 1.1(ii) and 3.14(d): make the quantifier "for all large A" explicit, and note that N is nondecreasing (the proof uses this).
- **m4.** p. 28: "Off this family … (0;5,5,5)". But (0;5,5,5) *is* a triangle orbifold; write "against orbifolds outside the triangle family".
- **m5.** Thm 1.3(i), Thm A and Thm C(2) use different hypotheses on the orders (complex with m_i + m_j ≠ 0, integer, positive real). State them uniformly.
- **m6.** Prop. 2.11(ii), p. 12: the bracket [v^{2l}] is undefined, and "the corresponding average over directions" is not a definition. Define J in general or restrict the statement.
- **m7.** Δ = −div grad is first declared on p. 11 but used in (1) on p. 2.
- **m8.** Ref. [34] is listed as "in preparation", although it is a complete disclosed manuscript that cites this paper as "submitted"; [7] is listed as "submitted". Make the status of all three manuscripts consistent.
- **m9.** N proves two facts that bear directly on §5 and are not mentioned here:
  - there are unbounded collision classes (N, Thm 1.2);
  - the number of collisions is ≫ X(log X)² (N, Thm 1.1).
  
  So arbitrarily many triangle orbifolds share c_1 and c_2, while by Cor. 5.1 three invariants always suffice. One sentence would complete the picture.
- **m10.** Cor. 4.1(b), p. 25: phrase the proof using the mapping class group acting on Teich(O). The statement is classical, as the text notes.
- **m11.** Thm 3.13, p. 21: "the smaller of which can be any prescribed integer g ≥ 2" reads oddly, since genera 0 and 1 also occur. Write "can be made any g ≥ 2 by adding handles".
- **m12.** p. 27: the asymptotic |b_l(m)| ∼ C_m l^{−1/2} l! (m/π)^{2l} is unproved. Add the one-line derivation: the term k = l dominates, and (2l)!/(4^l l!) ∼ l!/√(πl).

## Presentation (figures, captions, notation, exposition; not length)

**Figures.** I inspected all eight in the rendered PDF. They are well made and genuinely explanatory. I checked that Fig. 2 plots the correct X* and −X*, and that every dot and circle in Fig. 7 matches Thm 5.4 and Table S2.
- **P1. Fig. 1 (p. 2).**
  - The text says 4πt h_t(x,x) "approaches the order" at a cone point. At t = 0.02 this is not yet so for orders 8 and 12: (π/m)² is about 0.15 and 0.07.
  - The tips render at roughly 4–5 on a colour bar that runs to 12.
  - "Lifted to a surface in space" (text) and "schematic shapes" (caption) do not match what is drawn, which is flat curvilinear triangles.
- **P2. Fig. 3.** See m2. It also needs a legend; at present the key exists only in the running text.
- **P3. Fig. 5(b).** The caption does not explain the grey band (the error budget) or the circles.
- **P4. Fig. 8.** There is no legend; the line styles are identified only in the paragraph below. Put them in the caption.
- **P5. Fig. 4.** State the square-root scale of the y-axis in the caption.

**Notation.** Several symbols carry more than one meaning:

| Symbol | Meanings |
|---|---|
| R | reciprocal sum; rotation in §2.4 |
| B | bound B(ℓ, diam, t); Bernoulli numbers and polynomials; fixed-point coefficient 𝓑_l; matrix in S3 |
| Z | heat trace Z_O; configuration (Def. 3.10); coordinate of C_Λ |
| T | tanh series T(z) (Thm B); minimal configuration size T(L) |
| M | bound on the orders; matrix 𝐌 (Thm B) |
| χ | Euler characteristic χ(O); polynomial χ_m |
| b_l | b_l(m), a function of an order; b_l(p), a function of a point |
| σ | signature; coefficients σ_i of u/sin u |

The clashes in R, Z and b_l are confusing inside the proofs.

**Exposition.**
- The lettered Theorems A–C, mixed with numbered results, make navigation harder; the map "Thm 1.3 = Thms A–C with 3.11" (p. 6) shows the problem. Consider one numbering scheme.
- The anthropomorphic metaphors ("learns", p. 2) are used repeatedly.
- "The j-th invariant is what diffusion has learned at the j-th order in t" adds nothing beyond (1).

**Data statement (p. 37) and supplement (S1, the Table S1 caption, S2, S6).**
- These name internal paths such as `review/round1-fixes/d2_explicit_pairs.py` and `paper/jga/tools/make_tables.py`.
  - The first reveals a prior review history.
  - The second suggests a different target journal ("jga").
- `theory/threshold/` is given as a source, but it is a directory.
- The paragraph on p. 37 is badly justified in the rendered page, with very wide gaps between words.

## Overlap with the disclosed related manuscripts

**With B.**
- **Shared statements.** B's Table 1 lists seven results taken from this paper and states them without proof:
  - the trace formula;
  - Lemmas 2.4–2.6;
  - Prop. B.2;
  - Lemmas 2.8 and 2.10;
  - Lemma 3.3;
  - Cor. 3.5 and Thm 3.8(i).
  
  The dependence runs in the right direction: nothing in A depends on B (A, p. 5).
- **Shared data.** Both papers use the same computed spectra of O(2,8,8), O(3,3,12) and the eight-member family (0;3,3,3,3), and largely the same method text.
  - The numbers agree where I compared them.
  - Each paper should say in one sentence that this description and the data are shared, and both should cite the one Zenodo deposit.
- **Distinct contributions.** A §6 with S5, and B's Thm 7.1, answer related practical questions by different certificates, from heat invariants and from eigenvalues respectively. The contributions are distinct:
  - B: the integrality lemma, the diameter bound, eigenvalue counting, and the cusp-like behaviour of O(2,3,m);
  - A: the PTE equivalence, the sharp M+1, and the triangle classification.
- **Verdict.** This is not redundant publication. I will make B available to the referees.

**With N.**
- **Shared ground.**
  - Both use the curves C_Λ of Bremner–Guy–Nowakowski and note the reciprocal pair.
  - Both note the torsion Z/2 × Z/6 at Λ = 27/2.
  - Both rest on the same enumeration: S ≤ 4800 in A, extended to 6000 in N.
- **Proof dependence.** N cites A's Thm 5.8 without reproving it, and A does not use N.
- **Useful context for A.** N's Remark 3.3 (isosceles points have order 6) explains structurally why the minimal pair is torsion; A could cite it (m9).
- **Verdict.** The overlap is small and properly handled; only the citation status needs fixing (m8).

**Overall.** Three simultaneous manuscripts from one group invite a salami-slicing question. Having read all three, I do not think it applies, since each has its own main theorem. The cover letter should still address it.

## Desk-reject probability

**30%.** This estimate takes no account of length.

**For desk rejection:**
- (M1) Once a known expansion is granted, the core results are algebraic or Diophantine.
- The headline growth theorem is an equivalence with an open problem, not a determination.
- The most analytic section (§2.4) consists of sketches.
- The three-manuscript pattern needs explanation.

**Against desk rejection:**
- The topic is squarely in AGAG's tradition.
- Everything I recomputed is correct.
- The sharp area-free bound M+1 and the complete answer for triangle orbifolds are new, and they answer a question raised explicitly in DGGW Rem. 5.16.
- Prior work is treated carefully, and computational claims are labelled carefully.

My decision would be to send it to review. I would use two referees:
- one from inverse spectral geometry of orbifolds and heat invariants;
- one with Diophantine expertise (PTE problem or elliptic curves).

I would ask the authors in advance for the cover-letter clarifications under M1 and M5.

## Recommendation

**Major revision**, as the handling editor's provisional view before referee reports. Confidence is moderate, about 60%.
- The mathematics I checked is correct, and nothing I found is fatal.
- M1–M3 need real changes, and M4–M5 need editorial clarification.
- If the referees, after M1 is addressed, judge the significance for AGAG readers insufficient, the outcome could be rejection with a recommendation to transfer.

## What resolves each issue

- **M1.** Add a paragraph to §1 that:
  - lists the results that use analysis beyond the coefficient formula (the trace formula with bracketing remainders, the time scale (π/µ)², Thm 4.2);
  - says what they imply for heat traces at positive time;
  - adds one sentence on the eigenvalue-level consequence via B.
  
  The cover letter should explain why AGAG rather than a number-theory journal.
- **M2.** Either:
  - prove Props 2.11 and 2.12(i)–(ii) in full; or
  - relabel them as Remarks or computer-supported Claims, and state exactly what the independent computation verified and how.
  
  At minimum, fully prove Prop. 2.12(iii).
- **M3.** Rephrase the abstract: "at least like A^α for large A exactly when N(k) = O(k^{1/α})".
- **M4.** Write in the proofs "the rank is proved in Supplement S7" and "the constants and their proofs are Supplement S3". Cite LMFDB 90.c3.
- **M5.**
  - Explain in the cover letter, and in one sentence in §1 of each paper, what each contributes that the other does not.
  - State in both papers that the data and the method description are shared, and cite the one Zenodo deposit.
- **m1–m12.** As stated in each item above.
- **P1–P5.**
  - Fig. 1: use a smaller t, or say how far the tips are from their limits; make the text and caption agree on what is drawn.
  - Figs 3 and 8: add legends.
  - Figs 4 and 5(b): complete the captions.
- **Notation.** Rename the clashing symbols, for example:
  - ρ for the rotation in §2.4;
  - a different letter for the configuration Z and for the C_Λ coordinates;
  - b̃_l(p) for the variable-curvature cone term;
  - 𝒯(z) for the tanh series.
- **Numbering.** Consider one numbering scheme in place of Theorems A–C.
- **Data statement.** Replace the internal paths with neutral script names inside the Zenodo deposit, and fix the justification of the paragraph.
