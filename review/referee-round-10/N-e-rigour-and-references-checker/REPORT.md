<!-- Round 10, N-e, returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

I could not write `REPORT.md`: the write was refused ("Subagents should return findings as text"), so the full report is below. The scripts, my independent enumeration and the fetched sources are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/N-e-rigour-and-references-checker/scratch/` (subfolders `code/` and `refs/`).

# Referee report (rigour and references) for *Integers*: "Triples with Equal Sum and Equal Reciprocal Sum"

## Summary
The note studies unordered triples of positive integers that share both their sum S and their reciprocal sum R with another triple. Such a coincidence is a pair of positive rational points on one fibre C_Λ, with Λ = SR = e1e2/e3, of the cubic pencil (x+y+z)(xy+yz+zx) = Λxyz. This is the Beauville / Γ0(6) = ±Γ1(6) pencil.

The main results are:
- **Theorem 1 / A:** the rational torsion of C_Λ, and which torsion points are positive. Lemma 4 adds which torsion translations preserve positivity.
- **Theorems 2–3 / B:** lower bounds N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X, and N(X) ≫ X(log X)².
- **Theorem 4 / C:** arbitrarily large classes, by Schinzel's argument.
- **Propositions 4–5 / D:** the dual family contributes O(X(log X)^5), via Browning–Sofos; and n(S) ≪ S^{2+ε}.
- **Section 6:** an exhaustive enumeration up to S = 6000.

The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifier for [17]) are treated as known.

## Significance
Modest but real, and appropriate for *Integers*.
- **New:** the positivity analysis of torsion (Theorem 1(iv), Lemma 4); the counting function and its two lower bounds; the reduction of the dual family to a quartic del Pezzo surface with a conic bundle; and a carefully cross-checked enumeration.
- **Not new, and credited:** most of the geometry (Propositions 2–3, the group of base points) is classical or in Bremner–Guy–Nowakowski [3], and the paper says so.
- **Open:** the limiting exponent (Question E). The paper is candid about what it does not prove.

## Correctness: what I recomputed
I used PARI/GP 2.17.2 (through cypari2), sympy, and an independent C enumerator with exact reduced fractions.

1. **Proposition 2.**
   - E_Λ evaluated at (s(x,y,z), η(x,y,z)) vanishes modulo the equation of C_Λ (symbolic check).
   - The stated inverse lands on E_Λ. The composite gives η back exactly, and gives s back up to a multiple of the equation of E_Λ.
   - The discriminant of the cubic is 256Λ²(Λ−1)³(Λ−9), so Δ = 2^12 Λ²(Λ−1)³(Λ−9).
   - The tangent at O is x + y = (Λ−1)z.
   - At Λ = 27/2, (1:4:4) maps to (−6, 45).
   - At Λ = ∞, 1, 0, 9 we have c4 ≠ 0 and ord Δ = 6, 3, 2, 1, so the fibres are I6, I3, I2, I1.
   - The Shioda–Tate count and |MW|² = 36 are correct.
2. **Tate normal form (p. 3).** With c = −1/Λ, the stated substitution carries E_Λ to the Tate normal form, up to the factor c⁶/64. The image of (0:1:0) is (0,0).
3. **Group law, Proposition 3, Lemma 3, Theorem 1.** I checked these on C_{49/4} (r = 2) and C_{169/16} (r = −4), with G = (1:r:r²).
   - G has order 12.
   - 2G = (0:1:−1) + T2, 4G = (1:0:−1), 6G = T2, 8G = (0:1:−1).
   - 3G = (1:r²:r) and 9G = (r²:1:r) have order 4; the other orderings have order 12.
   - The cyclic shifts are translations by (1:0:−1) and (0:1:−1).
   - All orders stated in Theorem 1(iv) hold.
   - Integer Λ > 9 with extra torsion forces Λ = 10.
4. **Lemma 1.**
   - For S ≤ 400 the class lists are identical with and without the restriction R < 1 (that is, allowing a least entry of 1).
   - I also checked every algebraic step of the proof by hand, including both discriminants.
5. **Theorem 2.**
   - |Ω| = (log 2)/6, the factor #U/8, and c_iso = 0.105345… are correct.
   - A_iso(4800) = 506.
   - (copies − c_iso X log X)/X = −0.2852 at X = 4800 and −0.2860 to −0.2863 for 10⁴ ≤ X ≤ 4·10⁷.
   - copies/X = 0.6077 at X = 4800.
   - 27 of the 506 pairs lie in classes of size at least 3.
6. **Theorem 3.**
   - Every inequality checks: U ≥ V/2, W ≤ y, UV = y/(4α²), the φ(n)/2 count, and the error O(y^{7/8} log y).
   - c_A = 3/(32π⁴), and the final constant 3/(128π⁴) ≈ 2.406·10⁻⁴.
   - The crossover is log X > 437.8.
7. **Proposition 5.** The identity (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′ is correct, and so is the divisor-bound argument.
8. **Proposition 4(i)–(ii).**
   - The five base points have no three collinear.
   - The six forms span the 5-dimensional space of cubics through them.
   - The Picard rank over Q is 5.
   - The conic class is H − E1.
   - The sixteen lines are as listed.
9. **Curves, using PARI** (ellminimalmodel, ellglobalred, ellrootno, elltors, ellrank), for C_{27/2}, C_{155/12}, C_{68/5}, C_{1849/120}, C_{230/21}:
   - Conductors: 90, 6250530, 82110, 1715185290, 41388270.
   - Root numbers: +, +, +, −, −.
   - Torsion: Z/2×Z/6, Z/6, Z/6, Z/6, Z/6.
   - Ranks: 0, 2, 2, 3, 3, with lower and upper bounds equal (r1 = r2).
   - Also, C_{169/16} has rank 1 and torsion Z/12, and C_{49/4} has torsion Z/12.
   - The (a, b) entries of Table 1 are correct, and 2^r = |α|·|ᾱ|/4 is consistent in every row.
10. **Points and pairs.**
    - On C_{155/12}, 3P = (162833463 : 723926268 : 287876366), and P has infinite order.
    - The four C_{169/16} pairs (S = 845, 1183, 2145, 3003) have Λ = 169/16. Their members differ by torsion of order 4 or 12, depending on the ordering.
    - Every class in Table 2 has the stated sum, a common Λ, and gcd 1.
11. **Enumeration (my own run).**
    - Every row of Table 3 (N, N_cl, primitive classes, largest class size) is reproduced exactly from X = 18 to 6000.
    - Triple counts: 3,067,197,199 up to 4800 and 5,992,496,499 up to 6000.
    - The local exponents are reproduced (my values: N(50) = 16, N(150) = 209, N(250) = 555).
    - The first classes of sizes 5 and 6 are at S = 1849 and S = 4600.
    - Class sizes up to 4800: 96981 / 1627 / 122 / 11 / 1.
    - A(500) = 1328, A(1000) = 4141, A(2000) = 12512, A(2400) = 16565, A(4000) = 35567, A(4800) = 46254. The local exponents 1.64, 1.60, 1.51 and 1.48 are all reproduced.
    - Up to 4800, 7626 primitive pairs are dual (16.5%). Exactly 4 are of torsion type, all on C_{169/16} at the stated sums. 38,624 are of the third kind.
    - Up to S = 200, 32.9% of primitive pairs are dual.
    - There are 1330 non-dual primitive pairs up to 600 and 669 up to 400.
    - 507 of the 582 sums in [19, 600] carry a primitive class.
    - The examples at S = 20, 26, 31, 32, 34 and 36 are correct.
12. **Section 6.3 fits.** Profile-likelihood Poisson fits on my own n(s) give:
    - q = 4.49 and β = 0.587;
    - window values 4.435 (stated 4.44), 4.64 and 4.39;
    - hold-out errors +0.26% / +2.34% and +0.22% / +2.32%, against the stated 0.25 / 2.33 and 0.21 / 2.32 (the small gaps are grid granularity);
    - a crossover at s ≈ 2099.
13. **Choudhry (35).** Over 20,000 random distinct triples it always gives equal sum and equal reciprocal sum, and it is never positive. This confirms the claim on p. 5.

## References checked at statement level

**Confirmed:**
- **[3] Bremner–Guy–Nowakowski:**
  - reciprocal pairs and scaling, p. 117;
  - model (6) and the "egg", p. 118;
  - "just the odd multiples of P give positive solutions", p. 119;
  - "In all cases except n = 10 … Z/6Z" and the permutation table, p. 120.
- **[4] Bremner–Macleod:**
  - E_N is literally E_{2N+6};
  - Lemma 2.1, Section 4, Theorem 5.1 and Corollary 5.2 as stated (but see M1).
- **[5] Bremner–Macleod corrigendum:** Ann. Math. Inform. 62 (2025), 26–27, as cited.
- **[6] Bremner–Tho:** IJNT 14(5) (2018), 1229–1246, confirmed through Crossref. The families are corroborated by [24]; I did not see the theorem numbers 8, 9, 14.
- **[8] Browning–Sofos, Theorem 1.1:** the hypotheses are X(Q) ≠ ∅ and a conic over Q; the height is the standard height on P⁴; the exponent is ρ − 1.
- **[10] Chen, A.5.1:** exactly as described.
- **[11] Choudhry:** §4.1 and equations (33)–(35) are as described.
- **[14] DGGW:** (5.7) in the arXiv numbering.
- **[15] DGGW erratum:** see m3.
- **[19] Kelly:** Theorem 2.
- **[22] Mazur:** Theorem (5.1), p. 156, including the pointer to Kubert's table.
- **[23] Moreland–Zieve:** the counterexample (3, 10, 24) to [26, v1, Prop. 2.6 / Thm 2.7].
- **[24] Nguyen Xuan Tho:** Theorem 1.1.
- **[26] Sadek–El-Sissi:**
  - published version: Proposition 2.5, Proposition 2.7 and Theorem 2.8, over rationals;
  - arXiv v2: Proposition 2.6 and Theorem 2.7, over integers, with the extra hypothesis;
  - arXiv v1: without that hypothesis.
- **[27] Schinzel:** pp. 587–588.
- **[30] Top–Yui, Table 2:** the Γ0(6) row has exactly this equation, and the fibre types match.
- **[31] Ulas:** Theorem 3.1 and Corollary 3.4.
- **Bibliographic data only**, confirmed through Crossref, OpenAlex, arXiv or Zenodo: [2], [7], [9], [12], [13], [16], [18], [20], [21], [28], [32], [33], [34], [35].

**Not seen:** [1] Beauville (Théorème and Tableau, p. 658), and [17] (placeholder).

## FATAL
None. I found no error in any proof or statement, and every number I could recompute is correct.

## MAJOR

**M1 (pp. 5–6): the content and priority of [4] relative to [24] are misstated.** The text says Bremner–Macleod "prove that there are none for odd N [4, Theorem 5.1 and Corollary 5.2], which on that subregion is the case 4 | Λ of the later theorem of Nguyen Xuan Tho."
- [4, Theorem 5.1] says that for every odd N, every point of E_N(Q) has x ≥ 0. So E_N has no rational points on the egg at all.
- Its proof writes N + 3 = 2M (M ≥ 2) and the curve as y² = x(x² + (16M² − 24M − 3)x + 64M). That curve is exactly E_{4M} of this paper.
- By the paper's own Lemma 2, the egg is precisely the positive locus of C_Λ. So [4] already proves that C_Λ has no positive rational point for every Λ = 4M ≥ 8.
- That is all of [24, Theorem 1.1] (the case 4 | n), not a statement "on that subregion". The present wording reverses the inclusion between the 2014 and 2021 results.
- *Fix:* credit [4, Thm 5.1], via E_{2N+6} = E_Λ and Lemma 2, as already giving the case 4 | Λ, and describe [24] as a later reproof by Hilbert symbols. Adjust the sentence on p. 5 ("For integer Λ = n, Nguyen Xuan Tho proved …") so the earlier source is credited first.

**M2 (pp. 17–18): the rank "proof" is not checkable from the paper.** The text says the 2-isogeny descent proves the ranks "without that program", because "images of explicit rational points fill" the Selmer groups.
- No points are given, and the local computation behind the listed Selmer groups is not shown.
- As printed, Table 1 is an assertion that rests on the deposit.
- The ranks are correct (ellrank gives r1 = r2), and no theorem depends on them; Theorem 4 needs only that P has infinite order, which Theorem 1(iv) proves.
- *Fix:* either list, for each Λ, points whose images generate the listed groups (x-coordinates on y² = x(x² + ax + b) suffice), plus one sentence on how the local conditions were evaluated; or downgrade the claim to "computed with ellrank, with matching bounds, and independently confirmed by a descent in the deposit".

## MINOR
- **m1 (p. 6).** After fixing M1, say that the region condition ("a subregion of the positive triangle … [4, Section 4]") matters only for the representation problem in [4]. It plays no part in the non-existence theorem.
- **m2 (p. 9, Lemma 2).** Say explicitly that the positive locus is closed in the closed triangle, because it is bounded away from ∂Π. Also replace "open in C_Λ(R), so a union of components" by "open and closed"; the argument needs both.
- **m3 (p. 2, [15]).** "Adds a hypothesis … for strata whose group Iso^max is trivial" misreads the erratum. The erratum requires a suitable stratum with Iso^max(N) **nontrivial**. Rephrase accordingly. Also, (5.7) is the arXiv numbering (Example 5.6); confirm it against the published pagination, or give a page.
- **m4 (p. 5, [26]).** The published Proposition 2.7 and Theorem 2.8 also assume N³(M³ − 27N) ≠ 0. Include this, or say "under the nondegeneracy hypotheses of [26]".
- **m5 (p. 17).** Schinzel [27] gets positivity from the Poincaré–Hurwitz density theorem near (0, 3), not from odd multiples on an egg. The present proof uses Lemma 2 instead. Say so; "we claim no novelty for the method" slightly blurs this difference.
- **m6 (p. 23).** The search over 189 lines is a deposit-only computation with an arbitrary coefficient bound (≤ 7). Label it as computational, and state that the bidegree-(1,1) components were found by exact factorisation of the (3,3) correspondence.
- **m7 (p. 6).** BGN [3, p. 130] say "it seems likely that for n > 16 there is always such a representation". Quote this faithfully. The role of [34] in that sentence is unclear: Zhang gives a sufficient condition and does not state the expectation.
- **m8 (p. 4, Question E "Equivalently").** Write out the partial-summation line: A(y) ≪_δ y^{1+δ} gives ∫ y⁻¹ dA ≪_δ X^δ/δ.
- **m9 (p. 13).** State once why the lattice count t²|Ω|/9 + O(t) holds uniformly over residue classes mod 3: the boundary is rectifiable, and each class is a translate of 3Z².
- **m10 (pp. 19–21).** A primitive class can contain non-primitive pairs. Table 3 counts primitive classes, while A(X) counts primitive pairs (45,167 against 46,254 at 4800). One sentence distinguishing the two would prevent confusion.
- **m11 (p. 15, Theorem 3).** State or cite the coprime-box estimate (6/π²)UV + O((U+V) log y), uniform in (q, r).

## Presentation and house style
- **P1.** §1.4 is a single paragraph of about 1.5 pages covering five literatures. Split it into paragraphs; this is about readability, not length.
- **P2.** Several sentences carry multiple nested parentheticals (p. 2 on the erratum; p. 5 on the Sadek–El-Sissi versions and Chen's "smallest" solutions). Move version and numbering details to footnotes or the reference list.
- **P3.** *Integers* does not use a Springer-style "Statements and Declarations" block. Fold funding and competing interests into the Acknowledgements, and check with the editor.
- **P4.** [29] should give the edition and place: 2nd ed., Springer, Cham, 2015.
- **P5.** In Figure 1(b) the dashed fit cannot be distinguished from the heavy curve at print size. Also, the caption says "(dark)" while the text on p. 21 says "dark blue-green"; make them agree.
- **P6.** On p. 3, clarify that Γ0(6) = ±Γ1(6) as groups, and that [30] lists the surface under Γ0(6).
- **P7.** The Table 1 header says "image of α", but the caption says "Selmer groups containing the images". Align the two.

## Recommendation
**Minor revision.** My confidence is high for the mathematics: I checked every proof step, and every number I could recompute came out right. For the literature it is moderate to high.
- M1 is a substantive misstatement of the content and priority of a cited theorem, and must be corrected.
- M2 is a "proved" claim whose proof is not in the paper.
- Neither affects any theorem.

With these fixed and the minor points addressed, I would support acceptance.

## What resolves each issue

| Issue | What resolves it |
|---|---|
| M1 | Credit [4, Thm 5.1] (via E_{2N+6} = E_Λ and Lemma 2) as already covering 4 \| Λ; describe [24] as a reproof. |
| M2 | Print generators and the local-condition method for Table 1, or weaken "proves" to "computed and confirmed". |
| m1 | Add one sentence separating the region condition from the non-existence theorem. |
| m2 | State that the positive locus is open and closed in C_Λ(R). |
| m3 | Correct the paraphrase of the erratum; give the published location of (5.7). |
| m4 | Add N³(M³ − 27N) ≠ 0, or "nondegeneracy". |
| m5 | Note that the positivity mechanism differs from Schinzel's. |
| m6 | Label the line search as computational; state the exact factorisation test. |
| m7 | Quote [3, p. 130] accurately; clarify the role of [34]. |
| m8 | Write out the partial-summation line. |
| m9 | Add one line on the class-wise lattice count. |
| m10 | Distinguish primitive classes from primitive pairs. |
| m11 | State the coprime-box estimate. |
| P1–P7 | As described above. |
