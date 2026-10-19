<!-- Round 8 N-c referee report: returned text saved verbatim; the reviewer could not write files -->

The write to `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/N-c-parametric-diophantine/REPORT.md` was refused, so the full report is below.

# Referee report: "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

**Referee profile:** classical Diophantine analysis (parametric solutions of symmetric systems, multigrade identities, Schinzel's method).

**Assignment:** Sections 1, 3, 4 and 5 of the note:
- Section 1: literature and novelty claims.
- Section 3: reciprocation, permutations, torsion.
- Section 4: lower bounds, families, constants, the dual family and its surface.
- Section 5: classes of every size.

Page numbers refer to the 22-page PDF. I read pages 1–5 and 8–15 as rendered images. The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifier) are treated as known.

## Summary

The note studies unordered triples of positive integers with equal sum and equal reciprocal sum. Following Bremner–Guy–Nowakowski (BGN), such triples are positive rational points on a fibre C_Λ of the Γ1(6) pencil (x+y+z)(xy+yz+zx) = Λxyz.

The main results in my sections:
- **Proposition 3 and Corollary 1.** Reciprocation is translation by a 2-torsion point. This gives the "dual" pair {e2·x, e1·(bc,ca,ab)}.
- **Lemma 3.** Permutations act as P ↦ ±P + (base point).
- **Theorem 1 and Lemma 4.**
  - The torsion is Z/6, Z/12 or Z/2×Z/6.
  - For Λ > 9, the positive torsion points are exactly the isosceles triples and the geometric progressions.
  - A torsion translation preserves positivity exactly when the torsion point is not positive.
- **Theorem 2 (isosceles subfamily).** N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X.
- **Lemma 6 and Theorem 3 (full dual family as a conic bundle).** N(X) ≥ (3/(128π⁴) + o(1)) X (log X)².
- **End of Section 4.** The dual family contributes O(X(log X)^5), by Browning–Sofos on a quartic del Pezzo surface.
- **Theorem 4.** Schinzel's argument on C_{155/12} gives infinitely many primitive classes of every size.

## Significance

What is good:
- The set-up is clean and correctly attributed (BGN, Beauville, Kubert, Mazur, Schinzel).
- Every proof I checked is correct.
- The counting results seem to be new as quantitative statements: Theorems 2 and 3, and the del Pezzo upper bound.
- The positivity analysis of the torsion (Theorem 1(iv), Lemma 4) is a neat complement to Sadek–El-Sissi on the equal-product side.
- The paper is unusually honest about what it does not prove.

Where the contribution is limited:
- The dual family is a one-line identity (m1).
- Theorem 4 is Schinzel's argument on another curve, as the authors say themselves.
- The torsion classification is Mazur plus Kubert.
- Theorem 3, the only result beyond X log X, is much weaker than the evident target (M2).

For a note in Integers this level of contribution is acceptable, provided the one open literature question (M1) is settled.

## Correctness, and what I recomputed

All computations used exact arithmetic: sympy, and PARI/GP through cypari2 in a virtual environment in the scratch folder.

1. **Lemma 1 (p.5–6).**
   - I checked every case by hand, including both discriminants 3(c′+3)(1−c′) and (c′+4)(24−22c′−c′²)/(6−c′).
   - The proof is correct.
2. **Weierstrass model and Tate normal form (p.3, p.6).** I verified symbolically:
   - the map to E_Λ, and the discriminant 2^12 Λ²(Λ−1)³(Λ−9);
   - the example (1:4:4) ↦ (−6, 45) at Λ = 27/2;
   - the Tate substitution x = c²s/4 + c, y = c³η/8 + c²(c−1)s/8 + c² with c = −1/Λ. It carries the Tate normal form into E_Λ times the factor 1/(64Λ⁶), so it is a genuine isomorphism.
3. **Proposition 3 and Lemma 3.**
   - I checked ι(P) = P + T2, the three transposition formulas P ↦ π(O) − P, and the cyclic permutations as translations by ±(0:1:−1).
   - Test points: P = (4:9:18) and 3P on C_{155/12}, using the group law pulled back from E_Λ.
   - All agree.
4. **Theorem 1.**
   - **Z/12 curves.** On C_{49/4} (r = 2) and C_{169/16} (r = −4) the torsion is Z/12, with:
     - 2G = (1:0:0), 3G = (1:r²:r), 4G = (1:0:−1);
     - 6G = T2, 8G = (0:1:−1), 9G = (r²:1:r).
     The orderings (1:r²:r) and (r²:1:r) have order 4 and the other four have order 12, as stated.
   - **C_{27/2}.** The points (1:4:4) and (4:1:4) have order 6, and (4:4:1) has order 2.
   - **Formulas.** Λ(1:r:r²) = (r+1+1/r)² is correct. The discriminant (Λ−1)(Λ−9) of 2t² + (5−Λ)t + 2 is correct.
   - The proofs of (i)–(iv) are complete, and Mazur gives the mutual exclusion of (ii) and (iii).
5. **Lemmas 2 and 4.**
   - Both are correct.
   - The four pairs on C_{169/16} (p.16; S = 845, 1183, 2145, 3003) all have Λ = 169/16.
   - In each pair, exactly three orderings of the second triple differ from the first triple by torsion, of orders 4, 12 and 12.
6. **Corollary 1, Theorem 2, Lemma 6.**
   - All identities check by hand. Primitivity of D_{u,v} and g ∈ {1, 3} are correct.
   - Areas: the sector {ab ≤ 1, a/2 < b < 2a} has area log 2; the quadrant part has area (log 2)/3; |Ω| = (log 2)/6.
   - The weights (3/4)·y + (1/4)·3y are correct, and c_iso = 0.105346.
   - **Numerical checks:**
     - There are **506** pairs D_{u,v} with S ≤ 4800.
     - The copies kD_{u,v} with sum at most 4800 number 2917, which is **0.6077X**.
     - The quantity (c_iso X log X − count)/X is 0.2860, 0.2862, 0.2863, 0.2863, 0.2863 at X = 10^4, 10^5, 10^6, 10^7 and 4·10^7.
   - This confirms the "−0.286X to three digits" claim.
7. **Theorem 3.**
   - Every step rechecks:
     - U ≥ V/2, and W ≤ (2βV)(2αV) = y;
     - UV = y/(4α²);
     - the error term O(M³√y log y) = o(y);
     - Σφ(n)/(2n²) ~ (3/π²) log M;
     - the factor 1/6, c_A = 3/(32π⁴), and the final constant 3/(128π⁴).
   - The proof is correct.
8. **Del Pezzo surface (p.14).**
   - The six cubics vanish at the five points. Their coefficient matrix has rank 5, and the five points impose 5 independent conditions, so the cubics span the whole space.
   - No three of the points are collinear.
   - The sixteen lines carry no positive points. They are:
     - the 5 exceptional curves;
     - 10 lines through pairs of the points, whose real ones are x=0, y=0, z=0 and x+y+z=0;
     - the conic e2 = 0.
   - The Picard rank over Q is 5.
   - The Browning–Sofos hypotheses (Theorem 1.1 of arXiv:1609.09057v4: X(Q) ≠ ∅ and a conic over Q) hold. The citation is accurate.
9. **Theorem 4 and Section 5.**
   - P = (4:9:18) lies on C_{155/12} and has infinite order. 3P = (162833463 : 723926268 : 287876366) and ι(P) = (9:4:2), as stated.
   - PARI (ellrank, elltors, ellglobalred, ellrootno) matches the text:

     | Curve | Rank | Torsion | Conductor | Root number |
     |---|---|---|---|---|
     | C_{27/2} | 0 | Z/2×Z/6 | 90 | +1 |
     | C_{68/5} | 2 | Z/6 | 82110 | +1 |
     | C_{1849/120} | 3 | Z/6 | 1715185290 | −1 |
     | C_{230/21} | 3 | Z/6 | 41388270 | −1 |
     | C_{155/12} | 2 | Z/6 | 6250530 | +1 |
     | C_{169/16} | 1 | Z/12 | — | — |

   - The descent arithmetic 2^r = |α||ᾱ|/4 gives ranks 0, 2, 3, 3, 2, consistent with the table. I did not redo the local images (see m8).
   - Every class in Table 1 has the stated sum and a common Λ.
10. **My own exact enumeration up to S = 600.**
    - It reproduces N, N_cl and the number of primitive classes at X = 100, 200, …, 600 (from 92/92/69 to 3067/2977/1714).
    - The first classes of sizes 2, 3, 4 are at S = 18, 136, 408.
    - 507 of the sums 19 ≤ S ≤ 600 carry a primitive class.
    - The two classes at S = 36 are as stated.
11. **Literature in Section 1.4.** Checked against the sources:
    - Kelly II (PAMS 1989) and Schinzel (Serdica 1996);
    - Zhang–Cai, and Ulas (arXiv:1305.6241; exponents −1, 1, 2);
    - Nguyen Xuan Tho (2021: no solutions when 4 | n), and Bremner–Nguyen Xuan Tho (IJNT 2018);
    - Chen's survey §A.5.1, and Sadek–El-Sissi (arXiv:1303.6705, see m3).

    Also correct:
    - the heat identity χ/6 + Σ(m_i²−1)/(12m_i) = (S+R−2)/12 with χ = R−1;
    - the MacLeod relation R/r = (Λ−1)/4;
    - ±Γ1(6) = Γ0(6) (both of index 12).

I found no false mathematical statement in Sections 1, 3, 4 or 5.

## FATAL

None.

## MAJOR

**M1 (p.5; consequences on p.19–20). Choudhry's three-parameter solution [8] has not been read.**

The paper says (p.5) "we have not been able to consult Choudhry's paper…", and also "individual coincidences and a parametric family are in [7, 8]". Both the novelty statements and the Section 6.4 heuristic depend on that paper. A referee cannot accept this, for three reasons:

- **(a) Access.** Choudhry, Rocky Mountain J. Math. 41(3) (2011) 737–763, doi:10.1216/RMJ-2011-41-3-737, is listed as bronze open access on Project Euclid by Unpaywall/OpenAlex and Semantic Scholar. Project Euclid blocked my scripted download, but the paper is freely readable in a browser.
- **(b) Attribution of the dual family.**
  - "Three-parameter" is exactly the parameter count of the dual family (a, b, c) ↦ {e2·x, e1·(bc, ca, ab)}.
  - That family is also the obvious classical solution: y_i = λ/x_i with λ = Σx/Σ(1/x), valid for any number of terms (see m1).
  - So [8] probably contains it. If so, the family behind Corollary 1, Lemma 6 and Theorems 2–3 needs crediting, as does BGN p.117 for the pairing.
- **(c) Question E.**
  - If [8] gives a different rational surface in the variety of pairs, the heuristic of Section 6.4 changes. There the authors say they "have not searched for" such a surface, and that quadrics in three variables would give about X^{3/2}.
  - That would bear on Question E itself and on the interpretation of the fits in Section 6.3.

*Resolution:*
- Read [8] and reproduce Choudhry's family in the paper.
- State whether it coincides with, contains, or differs from the dual and isosceles families, and credit accordingly.
- If it is a new surface, compute its (d, m) and its contribution to N(X), and revise Section 6.4.
- Remove "a parametric family are in [7, 8]" unless it is then accurate.

**M2 (abstract; p.3 Theorem B; p.13–14 Theorem 3). The second lower bound is far weaker than the evident target, and its constant means nothing at any accessible X.**

- **The constant.**
  - 3/(128π⁴) ≈ 2.41·10⁻⁴.
  - Theorem 3 beats Theorem 2 only when log X > c_iso·128π⁴/3 ≈ 438, that is, for X > e^{438}.
  - At X = 6000, Theorem 3 guarantees about 109 pairs. The true count is 145 679, and Theorem 2 gives about 5 500.
- **The gap.**
  - The authors' own Section 4 gives O(y(log y)^4) primitive dual pairs and an O(X(log X)^5) contribution, against the proved X(log X)². That is three logarithms apart.
  - The surface is better than a general conic bundle. The exceptional curves over (0:1:0) and (0:0:1) are Q-rational sections of |H − E1|, since each meets every fibre once. So Y is Q-rational, and Lemma 6 is an explicit parametrisation.
  - All the loss comes from ignoring gcd(W(u, v), …), as p.14 admits. That is a standard divisor-sum problem.
  - Alternatively, a Frei–Loughran–Sofos / Browning–Sofos lower bound run in a real box inside the positive region should give A_dual(y) ≫ y(log y)^4, hence N(X) ≫ X(log X)^5.

*Resolution:* either of the following.
- (i) Prove a stronger lower bound for positive dual pairs.
- (ii) Frame the result plainly:
  - say in the abstract and Theorem B that the dual family contributes between X(log X)² and X(log X)^5, with X(log X)^5 expected;
  - state the crossover X ≈ e^{438};
  - drop "one more logarithm" as a selling point.

This is a significance and presentation issue, not a correctness issue.

## MINOR

**m1 (p.3, p.8, Corollary 1). The dual pair does not need the group law.**
- For any n-tuple x, the tuple λ/x with λ = e_1·e_n/e_{n−1} has the same sum and the same reciprocal sum.
- Present Proposition 3 as the geometric interpretation, and relate the identity to Ulas [27].

**m2 (p.3). Soften "the description of the positive torsion points is new".**
- BGN's table [3, p.120] already writes reciprocals and permutations as torsion translates.
- The orderings of (1, 1, t) and (1, r, r²) are three lines from Kubert.
- Write "we have not found it stated".

**m3 (p.4, p.10). Sadek–El-Sissi numbering and hypotheses.**
- In arXiv:1303.6705v2 the results are Proposition 2.5 (isosceles points), Proposition 2.6 (positive rank) and Theorem 2.7 (torsion).
- The hypotheses there are distinct positive **integers** d1 > d2 > d3.
- The note cites "Proposition 2.7 and Theorem 2.8" with positive **rationals** u1 > u2 > u3. Check against the published Osaka version and correct if needed.

**m4 (p.5). Chen's survey entries can be sharpened with the paper's own data.**
- Chen's chain at S = 408 is not a full class. The class has size 4: it also contains (51,102,255), which is your Table 1 row.
- Chen's chain at S = 573, {44,253,276}, {45,198,330}, {66,78,429}, is a complete class.
- The S = 20 pair {(4,8,8), (5,5,10)} also comes before Chen's "smallest" solution at S = 26.

**m5 (p.11, after Lemma 4). A structural class of size 4 is missed.**
- On a Z/12 curve with r < 0, every positive x gives four positive points x, ι(x), x+G and ι(x+G) = x+7G.
- After rescaling, these form a class of size at least 4.
- Example on C_{169/16}: (165,240,440), (182,208,455), (6,11,16) and (16,35,40) form a class at S = 195 195.
- One sentence would record this, and it fits the Section 6.4 surfaces over Λ = (r+1+1/r)².

**m6 (p.13). Write "asymptotically" for "a factor of about 18c_iso log X ≈ 1.9 log X".**
- The statement ignores the −0.286X term the authors have just emphasised.
- At X = 4800 the actual ratio is about 10.9, against 1.9 log 4800 ≈ 16.1.

**m7 (p.11, Remark 1). Either prove it or move it to Section 6.4, where it is used.**
- The argument is complete in substance:
  - residues along each line are positive sums Σ1/a_i, so both triples have the same lines;
  - with three lines the entries match one to one;
  - with two lines the only alternative is a + b = c with 1/a + 1/b = 1/c, which is impossible.
- Its statement is loose ("degree at least 2").

**m8 (p.15). The 2-isogeny descent is not checkable as written.**
- E_Λ has rational coefficients, so "the integral model" is undefined.
- Give the scaling, a and b for each of the five curves, and the explicit generating points.

**m9 (p.14). Specify coordinates and height for the del Pezzo count.**
- Give the P⁴ coordinates: drop one of the six entries via the single linear relation, which leaves the gcd unchanged.
- State that the Browning–Sofos hypotheses hold, and note the Q-section.
- Change "comes from a point" to "comes from at least one point".

**m10 (p.15).** Write "the three orderings of each of (1,4,4) and (1,1,4)" instead of "six orderings".

**m11 (p.4).** "Equivalently (with Theorem B)": the equivalence follows from the displayed inequalities and partial summation alone. Rephrase.

**m12 (p.12–13).** "27 of them lie in classes of size at least 3" needs the full enumeration, which I did not rerun. Point to the file in the deposit.

## Presentation

- **P1 (p.4–5).** The literature paragraph runs over a page. Split it into four strands: equal products, negative exponents and PTE, representation problems, and triangle geometry. Put the novelty sentence in its own short paragraph.
- **P2 (abstract).** "and already the number of classes, is at least" is awkward; write "both N(X) and the number of classes are at least". Align the abstract with M2(ii).
- **P3 (p.8–9).** Split Lemma 3 into (a) the action and (b) the orbit.
- **P4 (p.13).** Lemma 6's conic claim needs one line of proof: cubics through (1:0:0) restricted to a line through (1:0:0) have degree 2.
- **P5.** "Dual" and "reciprocal" are used for the same involution. Fix one term.

## Recommendation

**Minor revision, conditional on M1.**
- Confidence is high on correctness: every proof and every number I could reach was recomputed and is right.
- Confidence is moderate on novelty, because [8] is still unread.
- If Choudhry's family turns out to be a rational surface other than the dual family, my recommendation becomes **major revision**. Section 6.4, the novelty paragraph and possibly Question E would then need rewriting.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Read Choudhry (RMJM 2011); state and compare his family; credit or revise Section 6.4. |
| M2 | Prove a sharper lower bound for positive dual pairs, or reframe Theorem B and the abstract with the crossover X ≈ e^{438}. |
| m1 | Add the n-term identity and credit BGN p.117. |
| m2 | Soften "new". |
| m3 | Check the numbering and hypotheses against the Osaka version. |
| m4 | Note the size-4 class at S = 408, and that S = 20 precedes S = 26. |
| m5 | Add a sentence on the size-4 class for Z/12, r < 0 curves. |
| m6 | Write "asymptotically". |
| m7 | Prove Remark 1 or move it to Section 6.4. |
| m8 | Give the integral models, a and b, and the generating points. |
| m9 | Specify the coordinates and height; note the Q-section. |
| m10 | Reword "six orderings". |
| m11 | Rephrase "Equivalently (with Theorem B)". |
| m12 | Cite the deposit file. |
| P1–P5 | Editorial. |

---

The rendered pages, verification scripts and downloaded literature are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/N-c-parametric-diophantine/scratch/` (subfolders `pages/`, `code/`, `lit/`; the virtual environment with cypari2 is `venv/`). The report file itself was not written because the write was refused.
