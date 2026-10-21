<!-- Round 10, N-c, returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

I could not write REPORT.md: the write to /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/N-c-diophantine-equations-classical/REPORT.md was refused because subagents may not write report files. The full report is below; please save it there. My scripts and fetched sources are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/N-c-diophantine-equations-classical/scratch/ (enumerator and checks in tools/, papers in lit/).

# Referee report for *Integers*: "Triples with Equal Sum and Equal Reciprocal Sum"

**Referee:** classical Diophantine equations (symmetric systems, multigrade equations, equal sums of like powers, parametric solutions)
**Scope of this report:** Sections 1, 4 and 6.4, and how the note treats prior work (Choudhry 2011; Bremner–Guy–Nowakowski 1993; Schinzel 1996; Chen Shuwen's survey). I treat the marked placeholders (author contributions, AI-use statement, Zenodo DOIs, preprint identifiers) as known. Page numbers are those of the submitted PDF. Before raising any point about wording or typesetting I checked it against the rendered page images.

---

## 1. Summary

The note counts unordered pairs of triples of positive integers that have the same sum S and the same reciprocal sum R. It follows Bremner–Guy–Nowakowski (BGN) in placing these on the cubic pencil C_Λ: e1e2 = Λe3, with Λ = SR. The pencil is Beauville's I6/I3/I2/I1 pencil, the universal curve with a rational 6-torsion point.

In the sections assigned to me:

- **Section 1** states the results: torsion (Theorem A); lower bounds N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X and N(X) ≫ X(log X)² (Theorem B); arbitrarily large classes by Schinzel's argument (Theorem C); an upper bound n(S) ≪ S^{2+ε} (Proposition D); and Question E, whether N(X) = X^{1+o(1)}. It also surveys the literature.
- **Section 4** proves the two lower bounds. The first uses the isosceles family D_{u,v}. The second uses the "dual family" x ↦ (e2·x, e1·(bc, ca, ab)), written as a conic bundle (Lemma 6, Theorem 3). Section 4 then identifies the dual pairs with rational points of a quartic del Pezzo surface and applies Browning–Sofos to get an O(X(log X)^5) upper bound for their contribution (Proposition 4).
- **Section 6.4** gives a heuristic for what a positive answer to Question E would require, and reports a search for one-parameter families along lines.

## 2. Significance

**What is good.**
- Every proof I was asked to check is correct.
- The arithmetic is careful, and the caveats are honest: the note says plainly that Theorem 3 is not sharp, that the positivity part of the Browning–Sofos lower bound is not claimed, and that Question E is open.
- The literature review is better than usual for this subject. Two examples:
  - It records the Sadek–El-Sissi / Moreland–Zieve correction accurately, including the version numbering.
  - It notes, correctly, that Chen's survey misses the smaller pairs at S = 18, 20, 31 and 32.
- The exhaustive enumeration is a real contribution. I reproduced every row of Table 3 up to X = 2000.

**What is weak.**
- The genuinely new mathematics in my sections is modest:
  - Theorem 2 counts an explicit, classical two-parameter family by a standard lattice-point and Möbius argument.
  - Theorem 3 gains one logarithm with a constant of 2.4·10⁻⁴. It overtakes Theorem 2 only when log X > 438, and nothing else in the paper uses it.
  - Theorem C is, by the authors' own account, Schinzel's rescaling combined with BGN's observation that odd multiples of a point on the egg are positive.
- The main open question (E) is left fully open, and Section 6.4 offers heuristics only.

For *Integers* I consider this acceptable: an exact, well-documented enumeration together with correct elementary counting results on a classical system. The paper should not, however, overstate priority or the evidential weight of its data, and in two places it currently does (M1, M2, M4).

## 3. Correctness, and what I recomputed

All computations were run in my scratch folder, using a small C enumerator and Python with exact rationals.

### Exhaustive enumeration up to S = 2000

I enumerated every admissible triple 2 ≤ a ≤ b ≤ c and grouped them by the exact reduced fraction e2/e3. This reproduces exactly:

- **Table 3** for X = 18, 100, 200, 300, 400, 500, 600, 1000, 2000:
  - N(X) = 1, 92, 386, 840, 1496, 2210, 3067, 7641, 25042;
  - N_cl(X), the primitive-class counts and the largest class sizes all match;
  - local exponents 2.524, 2.069, 2.007, 1.954, 1.993, 1.868, 1.790, 1.713.
- **The smallest coincidences** quoted on p. 5:
  - S = 18: {(2,8,8), (3,3,12)}
  - S = 20: {(4,8,8), (5,5,10)}
  - S = 26: {(4,10,12), (5,6,15)}
  - S = 31: {(4,9,18), (5,6,20)}
  - S = 32: {(4,14,14), (5,7,20)}
  - S = 34: {(6,14,14), (7,9,18)}
- **Table 2:** the first classes of sizes 3, 4 and 5 are at S = 136, 408 and 1849, with exactly the listed members. The class at S = 408 also contains (51, 102, 255), as the note says.
- I also checked the classes at S = 1849 and S = 4600 directly, by exact search over every possible least entry. They have sizes 5 and 6, with Λ = 1849/120 and 230/21.
- **Other counts:**
  - 507 of the 582 sums 19 ≤ S ≤ 600 carry a primitive class.
  - A(1000) = 4141 and A(2000) = 12512 (A = number of primitive pairs).
  - Dual pairs are 32.9% of primitive pairs for S ≤ 200.
  - There are 1330 non-dual primitive pairs with S ≤ 600.
- **The four torsion-type pairs on C_{169/16}:** sums 845, 1183, 2145 and 3003, all with Λ = 169/16. Confirmed.

### Section 4

- **Theorem 2:**
  - |Ω| = (log 2)/6 is correct.
  - The Möbius argument with the classes U1 and U3 modulo 3 is correct.
  - c_iso = 3 log 2/(2π²) = 0.1053457… is correct.
  - The pair D_{u,v} is primitive, and distinct D_{u,v} have distinct Λ; checked.
  - Numerically:
    - there are 506 pairs D_{u,v} with S ≤ 4800 (c_iso · 4800 = 505.66);
    - A_iso(4·10⁷) = 4,213,811 against 4,213,830 predicted;
    - exactly 27 of the D_{u,v} with S ≤ 4800 lie in classes of size ≥ 3.
  - The count of the copies kD_{u,v}, minus c_iso X log X, divided by X:

    | X | value |
    |---|---|
    | 4800 | −0.2852 (count = 0.6077X) |
    | 10⁴ | −0.2860 |
    | 10⁵ | −0.2862 |
    | 10⁶ | −0.2863 |
    | 10⁷ | −0.2863 |
    | 4·10⁷ | −0.2863 |

    So the statement on p. 14 ("−0.286X to three digits for 10⁴ ≤ X ≤ 4·10⁷"; "0.608X at 4800") is correct.
  - 18·c_iso = 1.896, and c_iso divided by 3/(128π⁴) = 437.8, matching "log X > 438".
- **Lemma 6:** the displayed pair, W(u, v), the geometric-progression exceptions and the multiplicity 6 all check out.
- **Theorem 3:**
  - U ≥ V/2, β/α ≤ α, and W ≤ 4αβV² = y all hold.
  - The coprime count in the box is 3y/(2π²α²) plus an error of O(M√y log y).
  - The bound Σ1/α² ≥ Σφ(n)/(2n²) holds.
  - The total error is O(M³√y log y) = o(y) for M = y^{1/8}.
  - c_A = 3/(32π⁴) and the final 3/(128π⁴) are correct.
- **Proposition 4:**
  - The six cubics have rank exactly 5, with the first five independent (checked symbolically).
  - They vanish at the three coordinate points and at (1:ω:ω²).
  - No three of the five points are collinear.
  - The sixteen lines are as listed, and positive triples avoid all of them.
  - Picard rank 5 over Q and the conic class H − E1 are both correct.
  - The hypotheses of Browning–Sofos (Math. Ann. 373, Theorem 1.1: X(Q) ≠ ∅ and a conic defined over Q) are met. Their N(B) uses the standard height on P⁴ and the open set with the 16 lines removed, as the note uses it.

### Section 1

- **Heat-invariant constant:** (R−1)/6 + Σ(m − 1/m)/12 = (S + R − 2)/12.
- **Tate normal form:** I verified symbolically that the stated substitution (with c = −1/Λ) multiplies E_Λ by c⁶/64 to give the Tate normal form. The image of the order-6 point is (4Λ, −4Λ(Λ−1)), which is BGN's order-6 point (p. 120).
- **Integer Λ > 9:** the only positive torsion points occur at Λ = 10. For (1:1:t), pq | 2(p² + q²) forces t ∈ {1, 2, 1/2}; for geometric progressions, r + 1/r ∈ Z forces r = ±1.
- **Question E:** the equivalence argument is correct.
- **Triangle substitutions:** the MacLeod substitution gives R/r = (Λ−1)/4, and the Bremner–Macleod substitution gives Λ = 2N + 6. For N odd this gives 4 | Λ, consistent with Nguyen Xuan Tho's theorem.

### Section 6.4

- I recounted the lines meeting the positive triangle (coprime |a|, |b|, |c| ≤ 7, up to permutation and sign): there are 189.
- 83.5% = 38624/46254, from the note's own counts, is arithmetically correct.

### Literature: the four assigned sources

- **Choudhry 2011.** I used the Wayback Machine copy of the Project Euclid PDF, rendered and read §1, §3, §4.1 and §5.1.
  - §4.1 gives exactly two solutions for exponents −1, 1: y_i = m/x_i, and the three-parameter formula (35), obtained from the line (34) y = x + t(σx − x).
  - I re-derived (35) from the page image. On 18,991 random positive triples it satisfies both equations and **never** produces a positive triple. This confirms the group-law argument on p. 5 (the third point is −(2P+τ), which lies on the identity component).
  - See M1 and M2 for what the note omits.
- **BGN 1993.** I OCR'd the Wayback copy of the AMS PDF; the archived file is truncated after p. 128.
  - Verified against the page images:
    - p. 117: reciprocal pairs and scaling;
    - p. 118: model (6) and the "egg";
    - p. 119: the quotation "If P is on the egg, then just the odd multiples of P give positive solutions" is verbatim;
    - p. 120: the quotation "In all cases except n = 10, therefore, the torsion group is Z/6Z" is verbatim, and so is the permutation/reciprocal table.
  - **Not verified:** the claim attributed to p. 130 (that every n ≥ 16 is represented by four variables), because that page is missing from the archive.
- **Schinzel 1996.** Fetched from the Serdica archive.
  - Correct: the definition of primitive (p. 587), the curve x1 + x2 + x3 = x1x2x3 = 6, and the rescaling by the least common denominator d to common sum 6d (p. 588).
  - See m3 on how Schinzel actually obtains positivity.
- **Chen Shuwen, survey (arXiv:2506.11429), Appendix A.5.1.** Fetched.
  - The pairs at S = 26 and 34 appear there, described as "first known solutions, smallest solutions, by Chen Shuwen in 2001".
  - The chain at S = 408 and Choudhry's three-parameter solution are as the note says.
  - The survey also lists a chain at S = 573 (its (A.653)); my enumeration shows that class is complete.

### Other sources spot-checked (beyond my assignment), all correctly cited

- Top–Yui, Table 2: the Γ0(6) row has exactly (x+y)(y+z)(z+x) + t·xyz = 0.
- Sadek–El-Sissi (published version): Proposition 2.5, Proposition 2.7 and Theorem 2.8, including the d1(d2−d3)³ ≠ d3(d1−d2)³ hypothesis and the statement for integers M, N.
- Moreland–Zieve: the counterexample (3, 10, 24) to the preprint's Proposition 2.6 and Theorem 2.7.
- Ulas: Theorem 3.1 (n ≥ 4, exponents (−1, 1, 2)).
- Bremner–Guy 1997 and Bremner–Macleod 2014: the abstracts match how the note describes them.

**Not verified:** Dryden–Gordon–Greenwald–Webb (5.7) and its erratum; Mazur Chapter III, Theorem (5.1); Kubert; Beauville's Tableau; the theorem numbers cited from Bremner–Nguyen Xuan Tho and Nguyen Xuan Tho; Kelly 1989 (checked only through Moreland–Zieve's description of it); refs [7], [9], [16], [18], [32], [33].

---

## 4. FATAL

None. I found no error in any proof in Sections 1 or 4, and no wrong number.

## 5. MAJOR

**M1 (pp. 5, 6, 13): the isosceles family is a special case of Choudhry's first solution, and the note says the opposite.**
On p. 5 the note identifies Choudhry's first §4.1 solution, y_i = m/x_i, with "the dual family below". It then states that "the isosceles family below does not appear in that section". But Theorem 2 itself (p. 13) defines D_{u,v} as "the dual pair of (u, v, v)". So D_{u,v} is Choudhry's first solution, scaled to integers, at x = (u, v, v). It is also BGN's reciprocal pairing (p. 117) applied to an isosceles triple. The sentence is false, and the closing priority statement on p. 6 ("a parametric family in [11]") understates how much of Section 4's raw material is classical.

*Resolution.*
- Delete the clause.
- State explicitly that the families of Theorems 2 and 3 are, respectively, the specialisation x = (u, v, v) of Choudhry's §4.1 identity and the full identity. (The identity also appears in BGN.)
- Say that what is new is the primitive reduction, the class-distinctness argument and the counts.

**M2 (pp. 5–6, 17): Choudhry 2011 contains more relevant material than the note reports.**
1. Choudhry, p. 738, eq. (3), already prints 4^r + 10^r + 12^r = 5^r + 6^r + 15^r and 6^r + 14^r + 14^r = 7^r + 9^r + 18^r for r = −1, 1. It credits them to Chen Shuwen's website (Choudhry's ref. [12]) and states that, apart from these, there were no published solutions as of 2011. The note credits these pairs only through the 2025 survey (p. 5), and says that "individual coincidences are in [10]" (p. 6).
2. Choudhry §5.1 (pp. 752–753, eqs. (52)–(55)) gives a parametric solution of arbitrarily long chains of **integer triples** with equal Σx, Σx² **and Σ1/x**:
   - x1 = Ma(a+b)/D, x2 = Mb(a+b)/D, x3 = −Mab/D, with D = a² + ab + b².
   - I checked his (54): Σ1/x = 0, Σx = M and Σx² = M².
   - These are therefore "classes" of every size for the note's system, but they lie on the degenerate fibre Λ = 0 (the conic e2 = 0) and always have mixed signs.

   This is directly relevant to Theorem C and to the sentence "Our system is the case of three terms and exponents −1 and 1 …" (p. 5). Unrestricted-sign chains of every length were published in 2011; what Theorem C adds is positivity.
3. Chen's survey calls the S = 26 and 34 pairs the "smallest solutions", and calls its 2023 chains (S = 408, 573) the "first known". Both statements are wrong:
   - pairs exist at S = 18, 20, 31 and 32;
   - classes of size 3 exist at S = 136, 143, 187, 209, …

   The note's parenthesis corrects the first statement only implicitly. It should say directly that Chen's "smallest" is incorrect, and that the first chain of three is at S = 136, not 408.

*Resolution.*
- Cite Choudhry (3) and Chen Shuwen's 2001 website as the first appearance in print.
- Add one sentence on Choudhry §5.1, and position Theorem C relative to it.
- State the two corrections to Chen's survey explicitly.

**M3 (pp. 3–4, 15–16): Theorem 3 is weak and may be superseded by the literature the note already uses.**
Browning–Sofos (§3 of their paper) explain that for Picard rank ρ ≥ 4 their lower bound is Frei–Loughran–Sofos, Theorem 1.2. Here ρ = 5. Lower-bound arguments of this kind count over regions of the base of the conic bundle. Whether they localise to a real open set (the positive part of Y) is exactly the question the note sets aside on p. 16. If they do, then:
- the primitive dual pairs number ≫ y(log y)^4;
- N(X) ≫ X(log X)^5;
- together with Proposition 4, the order of the dual contribution is settled;
- Theorem 3 becomes obsolete.

As it stands, the second half of Theorem B:
- is not the order of growth;
- has a constant of 2.4·10⁻⁴;
- beats the first half only for log X > 438;
- is used nowhere else (Question E needs only Theorem 2).

Its headline placement in the abstract and in Theorem B overstates its weight. Even inside the present method there are cheap gains:
- ⌊X/S_D⌋ ≥ X/S_D − 1 loses only O(A_dual(X)) = O(X log X), which doubles the constant;
- any M = y^θ with θ < 1/6 works, not only 1/8.

*Resolution (any one of the following).*
- (a) Prove the localised lower bound, citing Frei–Loughran–Sofos.
- (b) Explain precisely why it does not follow.
- (c) At minimum, move Theorem 3 out of the abstract and Theorem B into a remark, take the cheap improvements, and state the conjectured order X(log X)^5 next to it.

**M4 (pp. 21–23): Section 6.4 overstates the evidence and frames the heuristic incompletely.**
1. *"Weak, non-asymptotic evidence for a positive answer to Question E" (p. 22) is not justified.* The log-power fit that "wins" the holdouts is N ≈ X(log X)^{4.49}. That is already below the order X(log X)^5 that the note itself expects (p. 4, p. 21) from the dual family alone. The note also concedes on p. 21 that the dual-family fit (2.56) "falls well short of the exponent 4". The fitted laws therefore demonstrably do not capture asymptotic behaviour. A comparison on a finite range between two particular two-parameter laws gives no evidence about the exponent. Remove "evidence for".
2. *The heuristic should be stated in the language that justifies it.*
   - The variety of pairs V is (p. 23) a quintic hypersurface in the hyperplane e1(x) = e1(x′) ≅ P⁴. By adjunction ω_V = O_V(5 − 5) = O_V. Equivalently, V is birational to the fibre square of a rational elliptic surface, which has trivial canonical class (Schoen's construction; the note cites [28] but says "we do not use this").
   - In Batyrev–Manin terms, a(V, O(1)) = 0. Rational points off accumulating subvarieties are then expected to be sparse, and the growth of A(y) is governed by subvarieties S ⊂ V with a(S, O(1)) > 0.
   - The note's "X^{m/d}" is exactly a(P^{m−1}, O(d)) = m/d:
     - the trivial planes give a = 3;
     - the dual del Pezzo surface (with O(1)|_Y = −K_Y) gives a = 1 with b = ρ = 5, consistent with Proposition 4;
     - a Veronese-type surface would give a = 3/2.
   - Stated this way, the obstruction to Question E is "a subvariety with a > 1 whose positive real points are Zariski-dense". The data also raise a dichotomy the note should confront: the 83.5% "third-kind" pairs either lie on accumulating subvarieties not yet identified, or the enumeration is far from the asymptotic regime. This is the heart of Question E, and the note currently passes over it in one sentence.
3. *The line search is weaker than presented.*
   - Of the 189 lines tested, 53 pass through a base point of the pencil. On those, Λ restricted to the line has degree ≤ 2, and the Vieta involution is P ↦ −P − B with B a base point. By Lemma 3 and Proposition 3 it is therefore one of the twelve maps P ↦ ±P + T, so its outcome (dual pairs on the vertex lines, permutations otherwise) is forced in advance.
   - Only the 136 lines that avoid the base points are informative, and only the (1, 1) components of their (3, 3) correspondences were tested.

*Resolution.*
- Remove the "evidence for" phrasing.
- Add the canonical-class / a-invariant framing in a short paragraph.
- State the dichotomy about the third-kind pairs.
- Report how many tested lines avoid the base points, and note that the outcome for the others is forced by Lemma 3.

## 6. MINOR

- **m1 (p. 5).** "found by Chen Shuwen": add the year (2001) and the website, as Choudhry [11, ref. 12] does. Chen's survey gives the same date.
- **m2 (p. 6, last paragraph).** "individual coincidences are in [10]" should read "in [11, (3)] and [10]" (see M2).
- **m3 (p. 4, Section 1.3; p. 17).** Schinzel obtains positivity from the Poincaré–Hurwitz density theorem (Skolem, Satz 11), not from odd multiples. Section 5 says correctly that positivity here comes from BGN's egg observation, but Section 1.3 ("The proof of Theorem C is Schinzel's argument … applied to C_{155/12}") suggests the whole argument is Schinzel's. Say which part is his: the rescaling and primitivity.
- **m4 (p. 3).** "the elliptic modular surface of Γ0(6) [30, Table 2], which is ±Γ1(6)": Shioda's elliptic modular surface is attached to a group that does not contain −I, so this is the surface of Γ1(6). Top–Yui list the Beauville pencil under Γ0(6) (I checked: their Table 2 row matches). Reword, e.g. "the Beauville surface of Γ1(6) (listed under Γ0(6) = ±Γ1(6) in [30, Table 2])".
- **m5 (p. 6).** I could not check the BGN p. 130 statement ("every n ≥ 16 is so represented"); the archived copy is truncated. Please quote it, and make clear that it concerns the four-variable problem.
- **m6 (p. 14).** The secondary constant −0.286 is elementary to compute: Σ_D ⌊X/S_D⌋ = X Σ 1/S_D − Σ_D {X/S_D}, with the Dirichlet-series constant of the isosceles sums. Either give it in closed form or call it numerical throughout. It is numerically correct (see §3).
- **m7 (p. 15).** Theorem 3's constant: see M3 for the cheap factor 2 and the θ < 1/6 improvement. "Not optimised" is acceptable, but losses this cheap should be recovered or named.
- **m8 (p. 5).** Choudhry's (34) is literally the line through x and its cyclic shift (t = 0 gives x, t = 1 gives σx). Say so: it makes the identification "third intersection = −(2P + τ)" immediate for the reader. I confirmed numerically that (35) is never positive for positive x.
- **m9 (pp. 4, 22).** "probably of that order" (for the dual contribution) and "at least X(log X)² in order of magnitude" should both point to M3's open question, so that readers do not take X(log X)^5 for a theorem.

## 7. Presentation

- **P1 (pp. 4–6).** Section 1.4 is a single paragraph about 1.5 pages long that interleaves four separate literatures:
  - equal sum and equal product (Schinzel, Kelly, Sadek–El-Sissi, Moreland–Zieve);
  - equal sums of like powers with negative exponents (Chen Shuwen, Choudhry, Ulas);
  - the BGN representation problem and its descendants (Nguyen Xuan Tho, Bremner–Macleod, MacLeod);
  - unit fractions and partitions.

  Split it into these strands. The priority statement at the end should then follow naturally from them.
- **P2 (p. 5).** The sentence on Chen's survey carries two nested parentheticals of examples. Put the corrections (S = 18, 20, 31, 32; and the S = 408 class being incomplete) in a separate sentence.
- **P3 (p. 3).** Display the Tate-normal-form substitution rather than running it inline. It is correct (verified), but hard to parse as printed.
- **P4 (p. 3).** Theorem B joins a result with a sharp constant to a weak one with a negligible constant; separating them would show the reader which is which (see M3).
- **P5.** "Pair" means both an unordered pair of triples and a pair of points (P, P′) on C_Λ, and both A(y) and A_iso(y) are used; a sentence in Section 1.2 fixing these would help.

## 8. Recommendation

**Minor revision.** Confidence: fairly high (about 75%) on the mathematics, which I recomputed extensively; moderate on the literature, since BGN p. 130 and some secondary citations could not be checked.

The mathematics in Sections 1, 4 and 6.4 is correct, and the numerical claims I recomputed all agree. The required changes are to priority statements (M1, M2) and to how strongly the note presents Theorem 3 and the data (M3, M4). None needs new mathematics unless the authors choose option (a) of M3. If the authors are unwilling to correct M1 and M2, my recommendation becomes major revision.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Delete "the isosceles family … does not appear in that section". Identify D_{u,v} as Choudhry's y_i = m/x_i (equivalently BGN's reciprocal pairing) at x = (u, v, v). Restate the novelty as the counts. |
| M2 | Cite Choudhry (3) and Chen Shuwen's 2001 website for the S = 26 and 34 pairs. Add Choudhry §5.1 (chains with Σ1/x = 0 on the fibre Λ = 0) and position Theorem C relative to it. State explicitly that Chen's "smallest" and "first known chains" are incorrect (S = 18; S = 136). |
| M3 | Either prove N(X) ≫ X(log X)^5 by localising Frei–Loughran–Sofos Theorem 1.2 at the real place, or explain why it does not localise. Otherwise demote Theorem 3, take the cheap constant gains, and state the conjectured order. |
| M4 | Remove "evidence for a positive answer". Add the trivial-canonical-class / a-invariant framing and the dichotomy for the third-kind pairs. Report that 53 of the 189 lines pass through base points, where the outcome is forced by Lemma 3. |
| m1–m9 | Text edits as described in §6. |
| P1–P5 | Restructure Section 1.4, split the Chen sentence, display the Tate substitution, separate the two halves of Theorem B, fix the notation in Section 1.2. |
