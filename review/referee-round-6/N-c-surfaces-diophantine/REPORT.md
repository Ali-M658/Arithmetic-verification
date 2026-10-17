<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Referee report: "Triples with equal sum and equal reciprocal sum" (submitted to *Integers*)

Referee coverage: Sections 4 and 5 in full (Lemma 2, Theorem 3, Lemma 3, Theorem 4, Theorem 5, Table 1 and the text around it), and the Section 1 statements they prove (Theorem 1, Theorem 2, and the abstract's lower bounds). I read the other sections only where Sections 4–5 depend on them: Proposition 2, the birational map of Proposition 3, Lemma 1, Proposition 4/Corollary 1, and Remark 1. I read rendered images of pp. 8–11 before reporting anything typographical.

(The tool refused to write `REPORT.md`, so this message is the complete report. My scripts and outputs are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/N-c-surfaces-diophantine/scratch/`.)

## Summary

The note studies unordered pairs of admissible triples of positive integers (R = 1/a+1/b+1/c < 1) that have the same sum S and the same reciprocal sum R. My sections contain the following:

- **Lemma 2.** For k ≥ 4, every copy kD of a primitive pair D is admissible. Hence N(X) ≥ Σ_D #{k ≥ 4 : kS_D ≤ X}.
- **Theorem 3.** The explicit isosceles family D_{u,v} = {(2u+v)(u,v,v), (u+2v)(v,u,u)}/g is the dual pair of (u,v,v). Its count is A_iso(y) = c_iso·y + O(√y log y) with c_iso = 3 log 2/(2π²). This gives N(X) ≥ N_cl(X) ≥ c_iso·X log X + O(X).
- **Lemma 3 / Theorem 4.** The dual pair of x = (u, vq, vr) is parametrized and counted in boxes. This gives N(X) ≥ (3/(128π⁴) + o(1))·X(log X)².
- **Theorem 5.** Schinzel's argument, applied to the point (4:9:18) of infinite order on C_{155/12}, gives infinitely many primitive classes of size at least k for every k. The authors say plainly that the method is not new.
- **Table 1** lists the first class of each size 2–6 in an enumeration up to S = 6000, together with the Mordell–Weil ranks of the curves involved.

**Bottom line.** Every statement in my coverage is correct as stated, and every number I could recompute agreed. Within my sections I found no fatal error and no gap in any proof.

The main problem is how Theorem 4 is framed. The "two-parameter subfamily" of Lemma 3 is the whole dual family, reparametrized. Theorem 4 is a deliberately lossy count of that family. My own computation shows that the family's true contribution grows by at least one more logarithm than Theorem 4 claims. The paper's own sentence "its conic-bundle part gives X(log X)²" (§6.4) presents a lower bound as if it were the size of the contribution. The results in these sections are correct but modest: elementary lattice-point counts over a one-line algebraic identity, plus a known argument.

## Significance

**What is good.**
- The proofs in Section 4 are short, complete and correct.
- The constants are right, and the secondary-term numerics are accurate (see below).
- The authors are scrupulous about crediting Bremner–Guy–Nowakowski, Beauville and Schinzel. They say in plain words that Theorem 5 carries no new method.
- The exact enumeration behind Table 1 is correct; I reproduced it independently.

**Reasons for reservation.**

1. **The lower bounds rest on a trivial identity.** Corollary 1 says that e₂(x)·x and e₁(x)·(bc,ca,ab) share their sum and reciprocal sum. Everything in Section 4 is lattice-point counting over this identity (Theorem 3 is its restriction to x = (u,v,v)). The surface geometry announced in the abstract and the introduction (Beauville's pencil, Schoen's fibre-product threefolds) plays no role in any proof in Sections 4–5. The single exception is Lemma 1, which Theorem 5 uses.
2. **Theorem 2 is Schinzel's argument applied verbatim.** The authors concede this.
3. **The headline lower bound X(log X)² is far from the truth in two ways.**
   - It is far from the paper's own conjecture X^{1+o(1)} and from the measured local exponent ≈ 1.58.
   - It is not the true order even for the dual family it comes from (M1).
   - Its constant, 3/(128π⁴) ≈ 2.41·10⁻⁴, makes it numerically weaker than Theorem 3 until log X > 438 (m1).

The note is within the scope of *Integers*, and correct elementary results with a clear motivation can be published there. However, the advance in Sections 4–5 is small. The paper should not present Theorem 4 as capturing "the order of growth" of anything.

## Correctness and what was recomputed

All computations were done in `scratch/`, with sympy 1.x, PARI/GP 2.17.2 through cypari2, and my own C programs. Every item below agreed with the paper unless noted.

**1. Corollary 1 and Theorem 3 (p. 6, p. 8).**
- Symbolic check that e₂x and e₁(bc,ca,ab) have equal S and R: correct.
- D_{u,v} has S = (2u+v)(u+2v)/g and R = g/(uv) for both members: correct. It equals (dual pair of (u,v,v))/v: correct.
- Λ − 1 = 2(u+v)²/(uv) and Λ − 9 = 2(u−v)²/(uv): correct. So Λ determines {u/v, v/u}, and distinct D_{u,v} lie on distinct curves. I also checked this by exact enumeration for all 506 D_{u,v} with S ≤ 4800.
- Primitivity, admissibility of the copies, and distinctness of the members: checked by exact arithmetic for every D_{u,v} with S ≤ 4800. No failures.
- The smallest pair is D_{1,4} (S = 18): correct.

**2. The constant c_iso.**
- The area of the hyperbolic sector {ab ≤ 1, a/2 < b < 2a} is log 2 = ½ log 4, so |Ω| = (1/6) log 2.
- The class weighting (6 classes with g = 1, 2 with g = 3) gives (6/π²)(log 2/6)(¾ + ¾) = 3 log 2/(2π²) = 0.1053457…: correct.

**3. Counts of the isosceles family.**
- A_iso(4800) = 506, against c_iso·4800 = 505.66: agrees with p. 9.
- A_iso(y)/y = 0.1053, 0.10535, 0.105332, 0.1053444 at y = 10⁴ … 10⁷. The ratio (A_iso − c_iso·y)/(√y log y) stays below 2·10⁻³ in absolute value.
- In my enumeration, 479 of these 506 pairs are primitive classes of size exactly 2. The other 27 lie in classes of size ≥ 3.
- Every primitive size-2 class up to S = 6000 whose two members are both isosceles is some D_{u,v}.

**4. The secondary term (p. 9).** Σ_{S_D ≤ X/4}(⌊X/S_D⌋ − 3) over the D_{u,v}, minus c_iso·X log X, divided by X:

| X | 10⁴ | 10⁵ | 10⁶ | 10⁷ | 4·10⁷ |
|---|---|---|---|---|---|
| value | −0.47927 | −0.47933 | −0.47940 | −0.47941 | −0.47942 |

The claim "−0.479X to three digits" is correct. The factor 18·c_iso = 1.896 is also correct.

**5. Lemma 3 (p. 9).**
- e₁ = u+αv, e₂ = v(αu+βv), the displayed pair, and the common sum Q(u,v): verified symbolically.
- The multiplicity bound ≤ 6 holds. Enumerating all (q,r,u,v) with Q ≤ 2·10⁵ gave 96 081 distinct D, with maximum multiplicity exactly 6 (attained 1161 times).
- I also derived and checked numerically the exact reduced sum: S_{D(x)} = Q / gcd(αu+βv, (u+αv)·gcd(β,u)), where gcd(αu+βv, u+αv) divides α² − β = q²+qr+r². (This is used in M1.)

**6. Theorem 4 (pp. 9–10).**
- Q(U,V) = y·(½ + β/(2α²)) ≤ (5/8)y ≤ y, so the box inequality holds with room to spare.
- 6UV/π² = 3y/(2π²α²); Σ_{3≤n≤M} φ(n)/(2n²) ~ (3/π²) log M; the total error is O(M³√y log y) = O(y^{7/8} log y).
- c_A = (1/6)(3/(2π²))(3/π²)(1/8) = 3/(32π⁴), and N(X) ≥ (X/2)(c_A/2)(log X)² = 3/(128π⁴)·X(log X)² = 2.406·10⁻⁴·X(log X)².
- The partial-summation steps (#{k ≥ 4 : kS_D ≤ X} ≥ X/(2S_D) when S_D ≤ X/8, and Σ 1/S_D ≥ ∫ A(y)y⁻² dy) are correct.
- Conclusion: the proof is correct.

**7. Theorem 5 (p. 10).**
- (4,9,18) has Λ = 155/12.
- I verified symbolically that the map of Proposition 3 sends C_Λ to E_Λ. It sends T₂ ↦ (0,0) and (1:4:4) ↦ (−6, 45) at Λ = 27/2.
- On E_{155/12}, the image of P has nP ≠ O for 1 ≤ n ≤ 12. PARI's `ellorder` returns 0 (infinite order).
- 3P maps back to (162833463 : 723926268 : 287876366), exactly as printed.
- nP is positive for n = 1, 3, 5, 7 and not positive for n = 2, 4, 6, which is consistent with Lemma 1.
- The logic of the proof (Proposition 2, then infinitely many distinct L, then infinitely many primitive classes) is complete.

**8. Ranks (Table 1 and p. 10).** `ellrank` gives r₁ = r₂ as follows:

| Λ | 155/12 | 68/5 | 1849/120 | 230/21 | 27/2 |
|---|---|---|---|---|---|
| rank | 2 | 2 | 3 | 3 | 0 |
| torsion | Z/6 | Z/6 | Z/6 | Z/6 | Z/2×Z/6 |

This agrees with the paper. I could not check the "independent 2-isogeny descent", because no data for it are given.

**9. Table 1 and the enumeration (pp. 11–12).** I wrote an independent exact enumeration of all admissible 2 ≤ a ≤ b ≤ c with S ≤ 6000. It groups triples by double keys, then splits each group exactly with 64-bit cross-multiplication.
- Totals: 3 067 197 199 triples with S ≤ 4800 and 5 992 496 499 with S ≤ 6000.
- Every row of Table 2 (N, N_cl, primitive classes, largest class) is reproduced exactly at S = 18, 100, …, 600, 1000, 2000, 3000, 4000, 4800, 6000.
- Class-size histogram to 4800: 96 981 / 1627 / 122 / 11 / 1, as stated. To 6000: 137 520 / 2287 / 173 / 23 / 2, and no class of size 7.
- The first classes of sizes 3, 4, 5, 6 are at S = 136, 408, 1849, 4600, with exactly the members printed in Table 1. Λ is 68/5, 68/5, 1849/120, 230/21. All are primitive.

**10. Dual-family size (not claimed by the paper; used in M1).** I counted A_dual(y), the number of primitive dual pairs D(x) with S_D ≤ y, exactly up to y = 3000. Since S_D ≥ e₁(x), it is enough to enumerate all primitive x with e₁ ≤ y.
- A_dual(600) = 423, matching the paper's "423 dual pairs" on p. 7.
- A_dual(3000) = 4061.

| y | 200 | 375 | 600 | 750 | 1500 | 3000 |
|---|---|---|---|---|---|---|
| A/(y log y) | 0.077 | 0.096 | 0.110 | 0.120 | 0.142 | 0.169 |
| A/(y log² y) | 0.0146 | 0.0163 | 0.0172 | 0.0181 | 0.0194 | 0.0211 |
| A/(y log³ y) | 0.00276 | 0.00274 | 0.00269 | 0.00273 | 0.00265 | 0.00264 |

## FATAL

None. Every main result in my coverage is true and is proved: Theorem 1 (both bounds), Theorem 2 = Theorem 5, Theorem 3, Theorem 4, and Lemmas 2 and 3.

## MAJOR

**M1 (p. 9, sentence before Lemma 3; Lemma 3; Theorem 4; p. 10 "the order of growth is the point"; p. 13 §6.4 "its conic-bundle part gives X(log X)²"). Lemma 3 is the entire dual family, not a subfamily, and Theorem 4 understates what that family gives.**

*The parametrization covers every primitive triple.* Write any primitive triple as (a,b,c), and put u = a, v = gcd(b,c), (q,r) = (b,c)/v. Then q ≤ r are coprime and gcd(u,v) = gcd(a,b,c) = 1. So x = (u, vq, vr) runs over every primitive triple, three times, which is exactly the factor 3 in the multiplicity count of Lemma 3. "A two-parameter subfamily of the dual family" (p. 9) and "its conic-bundle part" (p. 13) are therefore inaccurate. The conic bundle is the dual surface itself, fibred by the lines through a vertex.

*Theorem 4 discards most of the family.* The proof keeps only q ≤ r ≤ y^{1/8}, axis-parallel boxes, and the bound S_D ≤ Q. It ignores the reduction S_D = Q/gcd(αu+βv, (u+αv)gcd(β,u)). That gcd is divisible by any d | q²+qr+r² on a sublattice of index d. Heuristically, this adds a divisor-sum over q²+qr+r², hence at least one more logarithm.

*The exact counts confirm this* (item 10 above). A_dual(y)/(y log y) rises from 0.077 to 0.169 for 200 ≤ y ≤ 3000, and A_dual(y)/(y log² y) is still rising. Only A_dual/(y log³ y) is roughly flat (≈ 0.0027). For comparison, Theorem 4's c_A·y log y is 23 at y = 3000, against the true value 4061.

*Consequence.* The dual family alone very likely gives N(X) ≫ X(log X)³, and plausibly more. Theorem 4 is a valid lower bound, but the paper repeatedly presents it as what the family "gives". It says the dual surface "gives X(log X)²" (p. 13) and that "the order of growth is the point" (p. 10). As written, a reader will conclude that dual pairs contribute ≍ X(log X)², which the data contradict.

This must be corrected. Ideally, the authors should determine the true order of A_dual(y). The family is completely explicit, and I expect the asymptotic to be provable by the same elementary methods.

## MINOR

**m1 (p. 10, Theorem 4; p. 3, Theorem 1).** Theorem 4 beats Theorem 3 only when (3/(128π⁴))·log X > c_iso, that is, when log X > 128π⁴·c_iso/3 ≈ 438. In every range the paper discusses numerically, Theorem 4 is far weaker than Theorem 3. This should be said next to Theorem 1, since the abstract places it first.

Cheap improvements are available:
- Take M = y^{1/6−ε}, since the error is O(M³√y log y).
- Use the sector area y·log(α²/β)/(2(α²−β)) instead of a box.
- Use the gcd reduction (M1).

The remark "the constant is not optimal" understates this.

**m2 (p. 8, proof of Theorem 3, "Möbius inversion … in a union of residue classes").** The step needs one more sentence. Terms with 3 | d vanish, because d·(u′,v′) ≡ (0,0) (mod 3) lies outside both unions. For 3 ∤ d, multiplication by d permutes the residue classes mod 3 and preserves each of the two unions {u ≡ v ≢ 0} and {u ≢ v} ∪ {exactly one of u, v ≡ 0}. As written, "coprime pairs are equidistributed among the 8 classes" is asserted rather than derived.

**m3 (p. 9, "There are 506 primitive isosceles pairs with S ≤ 4800").** Say that this counts the D_{u,v}. In the enumeration, 27 of them lie inside classes of size ≥ 3, so the enumeration has 479 primitive classes of size 2 made of two isosceles triples.

It would also be worth proving the converse, which I verified empirically up to S = 6000: every pair of isosceles triples with a common S and R is a D_{u,v}. This should follow from Remark 2, because isosceles points are 6-torsion, and a curve has at most 12 torsion points. With the converse, Theorem 3 counts exactly the isosceles–isosceles coincidences.

**m4 (p. 10, "Classes generated by one point are far out … the next positive point is 3P").** This is misleading. P + T₂ = ι(P) = (9:4:2) is positive and lies in ⟨P⟩ + torsion. Already at S = lcm(31,15) = 465 it gives the pair {(60,135,270), (62,124,279)} with R = 1/36, which I checked. The text should say "the next positive multiple of P other than its torsion translates".

**m5 (p. 10–11, "an independent 2-isogeny descent … confirms each rank").** No data for the descent are given (isogenous curve, Selmer group sizes, generators), so it cannot be checked. Either give the generators and the Selmer counts (two lines per curve), or rely on `ellrank`, whose r₂ comes from 2-Selmer.

Rank is not used by Theorem 5 at all. "Rank exactly 2" is a side remark and should be labelled as one.

**m6 (p. 9, Lemma 3, "for at most 3 ratios u : v").** Name the three ratios: u/v ∈ {√(qr), q²/r, r²/q}. This makes the O(M²) count in Theorem 4 immediate.

**m7 (p. 10, Theorem 4 proof).** The bound "A(y) ≥ c_A y log y(1+o(1))" holds only for large y, while the next integral starts at y = 2. Say that the integral's lower range contributes O(1). The use of U ≥ 1 (true because β/α ≥ 1/2 and V → ∞) should also be stated.

## Presentation

**P1 (Table 1, p. 11).** The rank column shows "[8]" for C_{27/2}. The rank is 0 (`ellrank` gives r₁ = r₂ = 0) and the torsion is Z/2 × Z/6. Print "0" and keep the citation in the caption.

**P2 (p. 9).** "Conic bundle" is used without definition, and neither the base nor the fibres are identified. Once M1 is fixed, say that for fixed (q:r) the line {(u : vq : vr)} through the vertex (1:0:0) maps to a conic of pairs.

**P3 (p. 8, Theorem 3 display).** The factor (6 log 2/π²)·(1/6) should be written as (6/π²)·|Ω|. Then the reader sees where 1/6 comes from, and the ¾ and ¼ weights match the class count stated just above.

**P4 (pp. 4, 10).** "Because Λ is invariant under scaling, the same steps apply verbatim" is true but overstated. Schinzel's curve has the fixed invariant 36, while here a curve of positive rank must be exhibited. Say that this is the only new input.

**P5 (abstract and §1.3).** State the bound of Theorem 3 first and that of Theorem 4 second, with the threshold of m1, so that the abstract does not suggest that the X(log X)² bound is the operative one.

## Recommendation

**Minor revision.** This recommendation covers Sections 4–5 and the Section 1 theorems they prove.

- Confidence that the results in my coverage are correct: **high**. Every identity, constant and table entry I could check was recomputed independently and agreed.
- Confidence in the recommendation: **medium**. The mathematics is sound. Whether the modest advance justifies publication depends on the other sections and on how M1 is resolved. If the authors determine the true order of the dual-family count, the note becomes noticeably stronger.

## What resolves each issue

- **M1.** Required: rewrite p. 9 ("subfamily"), p. 10 ("the order of growth is the point") and p. 13 ("its conic-bundle part gives X(log X)²"). The text should say that Lemma 3 parametrizes all primitive triples and that Theorem 4 is a lower bound for the dual family, not its order. Strongly recommended: use S_D = Q/gcd(αu+βv, (u+αv)gcd(β,u)) to prove A_dual(y) ≫ y(log y)², and so N(X) ≫ X(log X)³. Alternatively, report the exact counts A_dual(y) and state the true order as an open question.
- **m1.** Add the threshold log X > 438 next to Theorem 1, and either tighten the proof (M = y^{1/6−ε}, sector count) or remove "the order of growth is the point".
- **m2.** Add the two-sentence justification of the Möbius inversion in residue classes.
- **m3.** Clarify what the 506 counts, and add, or state as a remark, the converse that all isosceles–isosceles pairs are D_{u,v}.
- **m4.** Reword "next positive point", or mention the dual point ι(P) and the pair at S = 465.
- **m5.** Give the descent data, or drop "independent descent" and mark the rank statements as side remarks.
- **m6, m7.** One sentence each.
- **P1–P5.** Editorial changes as described.
