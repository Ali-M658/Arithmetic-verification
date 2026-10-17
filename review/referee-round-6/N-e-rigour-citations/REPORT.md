<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Summary

The note counts unordered pairs of positive integer triples with equal sum S and equal reciprocal sum R, where both triples are admissible (R < 1). By Dryden–Gordon–Greenwald–Webb these are exactly the pairs of hyperbolic triangle orbifolds that the first two heat invariants cannot tell apart. The contributions are:

- **Set-up.** Classes are positive rational points on one curve C_Λ : e1e2 = Λe3 of the Bremner–Guy–Nowakowski (BGN) pencil. The pencil is identified with Beauville's I6–I3–I2–I1 family. Reciprocation is translation by the 2-torsion point (0:0:1) (Prop. 4), which gives every triple that is not a geometric progression a "dual" partner (Cor. 1).
- **Lower bounds.**
  - Thm 3: N(X) ≥ N_cl(X) ≥ c_iso X log X, from the isosceles family.
  - Thm 4: N(X) ≥ (3/(128π⁴)+o(1)) X (log X)², from a conic-bundle subfamily of the dual family.
- **Upper bound.** Prop. 5: n(S) ≪ S^{2+ε}, hence N(X) ≪ X^{3+ε}.
- **Classes of every size.** Thm 5 applies Schinzel's argument to C_{155/12}.
- **Computation.** An exhaustive enumeration to S = 6000 (Tables 1–2), exponent fits, and Conjecture 1: N(X) = X^{1+o(1)}.

The main theorems are correct; I checked every step. The enumeration reproduces exactly. The errors are in side statements:

- Remark 2 makes a false claim about torsion orders.
- The note says three times that coincident pairs "need not be admissible". In fact every coincidence is admissible.
- The Figure 1(b) caption describes the thin curve wrongly.
- There are several citation and presentation points.

# Significance

The question is natural. Its spectral motivation is stated correctly, and I checked it against the source. It belongs to the tradition of Guy's problem D16, Kelly, Schinzel, Zhang–Cai and BGN. A limited OpenAlex search found no earlier study of N(X). The geometry of Sections 2–3 is credited to BGN and Beauville.

The new results are modest:

- The lower bounds come from explicit parametric families.
- The upper bound only says that each triple has about X^ε partners.
- Theorem 5 is Schinzel's argument on a different curve, and the authors say so.
- Conjecture 1 rests on a trend over a finite range, which the authors also say.

The note's strengths are honest attribution, a clean separation between what is proved and what is computed, and a reproducible computation. Once corrected it is an acceptable Integers note. Narrowing the gap between the exponents 1 and 3, for example by proving N(X) ≪ X^{2+ε}, would make it clearly stronger.

# Correctness and what was recomputed

**Checked by hand (all correct unless an issue is cited).**

- §1.1: the heat coefficient (S+R−2)/12, from χ = R−1, and the area 2π(1−R).
- Prop. 2 (gap noted in M2).
- Lemma 1 (non-emptiness of the positive locus is missing, m4).
- Remark 1, including Λ−1 = 2(u+v)²/uv and Λ−9 = 2(u−v)²/uv.
- Prop. 4, including F(ι(P)) = p0p1p2·F(P) (collinearity not shown, m3).
- Cor. 1: the criterion b² = ac for proportionality.
- The action of transpositions on C_Λ (p. 7).
- Remark 3 and Lemma 2.
- Thm 3: g ∈ {1,3}, |Ω| = (1/6) log 2, the Möbius count over residue classes mod 3, the constant 3 log 2/(2π²), and the partial summation.
- Lemma 3: the geometric-progression ratios √(qr), q²/r, r²/q, and multiplicity ≤ 6.
- Thm 4: β/α ≤ α, UV = y/(4α²), the error O(M³√y log y), c_A = 3/(32π⁴), the restriction S_D ≤ X/8, and the final constant 3/(128π⁴).
- Thm 5.
- Prop. 5: I expanded the identity (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′.

**Symbolic checks (sympy).**

- The pencil identity.
- Both maps in Prop. 3 land on the right curves, and both compositions are the identity.
- Δ = 2¹²Λ²(Λ−1)³(Λ−9).
- c4 = 16(Λ−3)(Λ³−9Λ²+3Λ−3), nonzero at Λ = 0, 1, 9. At infinity ord Δ = 6 and ord c4 = 0, giving I6.
- (Λ²−6Λ−3)² − 64Λ = (Λ−1)³(Λ−9).
- (1:4:4) ↦ (−6, 45).

**Exact chord-and-tangent arithmetic (my own code).**

- The base-point orders are 2, 3, 3, 6, 6, and (1:0:0) generates the six base points together with O.
- P + T2 = ι(P) on sample points.
- On C_{155/12}, nP ≠ O for n ≤ 12, and 3P = (162833463 : 723926268 : 287876366), as stated.

**PARI/GP 2.17.2.**

- Table 1 ranks: ellrank gives r1 = r2 = 2, 2, 3, 3, with torsion Z/6.
- C_{27/2}: conductor 90, torsion Z/2×Z/6, rank 0.
- On the minimal model [1,0,0,−2952566,1946655396], P = (916, 2842) and 2P has x = 62764/25. By Nagell–Lutz, P has infinite order.
- I did not run a separate 2-isogeny descent, so my rank check uses the same software as the authors.

**My own C enumeration of all admissible triples with S ≤ 6000 (about 6×10⁹ triples).**

- Every entry of Table 2 matches exactly, including the local exponents 1.993 and 1.585.
- 3 067 197 134 triples with 18 ≤ S ≤ 4800, plus 65 with S < 18, gives the stated 3 067 197 199.
- Class sizes to 4800: 96 981 / 1627 / 122 / 11 / 1.
- 507 of the 582 sums carry a primitive class.
- Dual pairs are 32.9% of primitive pairs to 200 and 7626/46 254 = 16.5% to 4800.
- There are 1753 primitive pairs to 600, of which 423 are dual. There are 669 non-dual primitive pairs to 400.
- Table 1: members, Λ values and first sums 136 / 408 / 1849 / 4600 all match. No class of size 7 occurs.
- N(S)/S² is 0.00935 at S = 400 and 0.00405 at S = 6000.

**Other claims checked.**

- For all 1330 non-dual pairs to 600, neither P′−P nor P′+P has order ≤ 12.
- For the 669 non-dual pairs to 400, there is no relation with m ∈ {2, 3}.
- Remark 2 census: there are exactly 40 305 triples. The torsion ones are all isosceles or geometric progressions, with 1460 of order 2, 731 of order 6 and 21 of order 12 (see M1, m7).
- A_iso(4800) = 506.
- The secondary term is −0.4793 to −0.4794 for 10⁴ ≤ X ≤ 4·10⁷.

**Fits (Poisson maximum likelihood on 600 ≤ s ≤ 4800).**

| Series | Mine | Paper |
|---|---|---|
| All pairs | 4.49 | 4.48 |
| All pairs, cumulative | 4.56 | 4.56 |
| Primitive pairs | 3.53 | 3.54 |
| Primitive pairs, cumulative | 3.63 | 3.63 |
| Primitive dual pairs | 2.56 | 2.56 |
| All pairs, [1200, 4800] | 4.44 | 4.43 |
| All pairs, [600, 2400] | 4.64 | 4.63 |
| All pairs, [2400, 4800] | 4.39 | 4.37 |

I did not redo the bootstrap.

**Line count (§6.4).** There are 1026 primitive lines with |coefficients| ≤ 7 meeting the open positive triangle, and 189 up to permutation of coordinates (m11).

**Citations checked against the source.**

- [7] DGGW: (5.7) is correct.
- [10] Mazur: Chapter III, Corollary (5.2), p. 156, is correct.
- [14] Schinzel: the definition of a primitive set is on p. 587, and the curve and rescaling are on p. 588. Correct (see m8).
- [11] Nguyen Xuan Tho: Theorem 1.1 (no positive solutions when 4 | n) and the Hilbert-symbol method are correct. [11] misprints A²−4B as (n−9)(n−1)²; the note's (Λ−1)³(Λ−9) is right.
- [13] Sadek–El-Sissi: Prop. 2.5 says isosceles points have order 6. Thm 2.8 has hypotheses the note omits, and the infinite-order statement is Prop. 2.7 (m9).
- [2] Bremner–Guy: correct.
- [16] Youmbai et al.: the summary is fair.
- [9] Kelly, [17] Zhang–Cai: the summaries are fair, checked from abstracts only.
- [4] Bremner–Nguyen Xuan Tho: the abstract confirms the BGN expectation and the forms 4m² and 4m²+4. The theorem numbers 8, 9 and 14 are unverified.
- Not checkable without a browser: [3] BGN pp. 117–120 (the AMS site blocks scripts; model (6) is indirectly confirmed by [11]), [1] Beauville, [15] Schoen Prop. 7.1, and the 2017 erratum to [7].
- Metadata for [2]–[4], [6], [7], [9]–[11], [13], [15]–[17] matches Crossref and OpenAlex, and [5] matches Zenodo.

# FATAL

None. Theorems 1–5 and Propositions 1 and 5 are correctly proved.

# MAJOR

**M1 (p. 7, Remark 2).** "A positive isosceles point therefore has order 6" is false.

- The transposition x↔y fixes O and acts as P ↦ −P; the note itself says this on p. 7 ("Q of order 1").
- So (v:v:u) satisfies P = −P and has order 2. It maps to η = 0 under Prop. 3.
- PARI confirms it: (1:1:2) on C_10 has order 2 while (2:1:1) has order 6, and (4:4:1) on C_{27/2} has order 2.
- In my census 1460 of the 2191 torsion isosceles points have order 2.
- The argument 2P = (1:0:−1) covers only the arrangements (u:v:v) and (v:u:v).
- The comparison "the same holds" with the equal-product curves overstates the analogy.

**M2 (Cor. 1 p. 6; Lemma 2 p. 8; Lemma 3 p. 9; Prop. 2 p. 4; Thm 5 p. 10; §6.3).** Every coincidence is automatically admissible, so the phrases "need not be admissible" are false.

*Claim.* If two distinct positive triples have equal S and equal R, then R < 1.

*Proof.*
- If R ≥ 1, the triple (sorted) is (1,b,c), (2,2,c), (2,3,c≤6), (2,4,4) or (3,3,3).
- Two triples (1,b,c) with equal S and R have equal b+c and equal bc, so they are the same triple.
- (1,b,c) against (2,2,c′) forces b² + bc + c² = 3(b+c), which only returns the same triple.
- (1,b,c) against (2,3,c′) gives a quadratic with negative discriminant for c′ = 3, 4, 5, and is impossible for c′ = 6.
- The remaining finite cases have distinct (S, R).

*Computational confirmation.* No exception exists for S ≤ 300. Every reduced dual pair with entries ≤ 80 has R ≤ 3/4, with the maximum at (1,4,4).

*Consequences.*
- Corollary 1 and Lemma 3: delete "need not be admissible".
- Lemma 2 and Equation (2): take k ≥ 1.
- Proposition 2: the proof never shows the triples are admissible at sum L. The statement is true only because of this lemma, so state it there.
- Theorem 5: the condition "admissible once L > 155/12" is automatic.
- The "−0.479X" secondary term (p. 9) belongs to the artificial k ≥ 4 count. With k ≥ 1 the ratio at X = 4800 is 0.608, not 0.415.
- §6.3: "for k ≥ 4 every D counts" should say "for every k".
- The leading constants of Theorems 3 and 4 are unaffected.

# MINOR

- **m1 (Prop. 2).** Add k ≥ 2. The last clause becomes redundant given M2.
- **m2 (Prop. 4, "every point P").** The formula gives (0:0:0) at base points. Say "P not a base point; ι extends to an automorphism".
- **m3 (proof of Prop. 4).** Collinearity of O, the intermediate point and ι(P) is not shown. Add that their difference is (p0−p1)p2·(1,−1,0).
- **m4 (Lemma 1).** State that the positive locus is non-empty, by the intermediate value theorem for e1e2/e3 on the open triangle.
- **m5 (Thm 5).** Replace the "exact chord-and-tangent computation" with a hand-checkable certificate: on the minimal model, 2P has x = 62764/25, so P is non-torsion by Nagell–Lutz.
- **m6 (Table 1; §1.1).** Do not defer the rank of C_{27/2} to the unpublished [8]. It is rank 0 with torsion Z/2×Z/6, so C_{27/2}(Q) has 12 points: six base points and the six permutations of (1,4,4) and (1,1,4). This also shows the S = 18 class is the only class on its curve.
- **m7 (Remarks 1–2).** Geometric-progression points give torsion Z/12; for example (1:2:4) on C_{49/4} has order 12. Mention this.
- **m8 (§5, "verbatim").** Schinzel gets positivity from the Poincaré–Hurwitz density theorem, not from odd multiples on the egg. Say so.
- **m9 ([13]).** Cite Prop. 2.7 and Thm 2.8, and add "under the hypotheses of".
- **m10 (§6.3).**
  - Say which population "non-dual 4.79" refers to. Primitive non-dual pairs fit q ≈ 3.73, so 4.79 must mean all pairs.
  - Primitive dual pairs fit q = 2.56, but their true log-power can be worked out from the three-parameter family. Use that family to calibrate the fitting procedure.
- **m11 (§6.4).**
  - The 189 lines are counted up to permutation of coordinates; say so.
  - "Not exclude ... between 1 and about 1.58" implicitly excludes values above 1.58, which the data cannot do.
  - The surface implication needs a generically finite parametrisation whose generic pair consists of distinct triples.
- **m12 (Beauville label).** The row is written Γ⁰₀(6). Top–Yui label it Γ₀(6); the usual SL₂ label is Γ₁(6), and Γ⁰₀(6) contains −I. Check against the original.
- **m13 ([7]).** An erratum exists (Michigan Math. J. 66 (2017), 221–222). Check that (5.7) is unaffected and cite it.
- **m14 (reference style).** Use AMS abbreviations:
  - [1]: "C. R. Acad. Sci. Paris Sér. I Math."
  - [6]: "Nat. Commun."
  - [16]: "Glas. Mat. Ser. III 60(80) (2025), no. 1".
  - Use issue numbers consistently; [14]'s source header shows no "(4)".
- **m15 (§1.1).** Trim the material on the unused companion manuscript.

# Presentation

- **P1 (Figure 1).** House style allows no in-figure labels or annotations.
  - The panel letters (a)/(b) and the two-coloured marker at S = 18 are inside the figure.
  - The grey triangle and the orange/teal colour key are not explained in the caption. I read teal as (1,4,4) and orange as (1,1,4).
  - The thin curve is the count of isosceles pairs with all their multiples (0.608 at S = 4800). It is not "the lower bound of Theorem 3" (0.415), nor c_iso log S (0.893).
  - Panel (b) stops at S = 4800, which the caption should say.
  - Keep the caption to two short sentences.
- **P2 (notation clashes).**
  - Δ° and Δ appear in the same proof (Lemma 1).
  - Q denotes the field, the form Q(u,v), and a base point.
  - (p, q, r) in Prop. 5 clashes with q, r in Lemma 3.
  - s is both a curve coordinate and the sums s_i.
  - y is both a coordinate and the summation bound.
- **P3.** Theorem 1 and Proposition 1 duplicate Theorems 3–4 and Proposition 5, so each result has two numbers.
- **P4.** Say "on one curve C_Λ, up to permutation".
- **P5.** Remark 3 is a sketch; it uses the independence of two non-proportional linear forms.
- **P6.** The data statement is good. Name the tool behind the "independent 2-isogeny descent", rename F9.py, and drop "all six authors as creators".
- **P7.** Computational claims are clearly separated from proved ones; only m5 crosses the line.

# Recommendation

**Minor revision**, confidence about 85%. M1 and M2 are false statements that must be fixed, but each fix is local and neither touches a theorem. Every table entry and count I tested reproduces exactly. I could not check BGN [3], Beauville [1], Schoen [15], or the theorem numbers in [4] against the sources.

# What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | State that (u:v:v) and (v:u:v) have order 6 and (v:v:u) has order 2; fix the comparison with [13]. |
| M2 | Add the lemma "every coincidence has R < 1". Remove "need not be admissible", use k ≥ 1, simplify Prop. 2 and Thms 3–5, and restate the −0.479X figure and §6.3. |
| m1–m4 | Add the missing hypotheses or one-line justifications. |
| m5 | Give the Nagell–Lutz certificate. |
| m6 | Prove rank 0 and the 12 rational points of C_{27/2} directly. |
| m7 | Add Z/12 to Remark 1. |
| m8 | Describe Schinzel's positivity argument correctly. |
| m9 | Fix the [13] pinpoints and hypotheses. |
| m10 | Specify the population; add a calibration on the dual family. |
| m11 | Add "up to permutation"; soften the exponent sentence; state the genericity conditions. |
| m12–m13 | Check Beauville's label; cite the erratum to [7]. |
| m14–m15 | Apply AMS abbreviations; trim the companion material. |
| P1 | Remove in-figure labels and the marker; give the colour key; describe the thin curve and the range S ≤ 4800 correctly. |
| P2–P6 | Rename symbols, remove duplicate numbering, call Remark 3 a sketch, name the descent tool. |

Writing REPORT.md to the review folder was refused, so this message is the complete report. The code, enumeration output and downloaded sources are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/N-e-rigour-citations/scratch/ (subfolders code/, out/ and lit/).
