<!-- Round 9 N-c referee report: returned text saved verbatim; the reviewer could not write files -->

I could not save the report to `REPORT.md`: the write was refused ("Subagents should return findings as text"). The full report follows.

# Referee report for Integers: "Triples with Equal Sum and Equal Reciprocal Sum"

**Scope:** Section 1 (the introduction and its claims), Section 4 (Lemma 5, Theorem 2, Lemma 6, Theorem 3, Proposition 4) and Section 6.4. I also read Remark 1 on linear forms (p. 12), which Section 6.4 relies on. I looked at other sections only where these parts depend on them. Page numbers are those of the 24-page PDF. The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifier) are treated as known.

---

## Summary

The note studies pairs of positive-integer triples with the same sum S and the same reciprocal sum R. It places them on the Bremner–Guy–Nowakowski pencil C_Λ: e1e2 = Λe3, with Λ = SR. Reciprocation is translation by a point of order 2. The dual construction x ↦ (e2·x, e1·(bc,ca,ab)) gives a three-parameter family of pairs. The note then estimates the counting function N(X). The results in my sections are:

- **Theorem 2.** An asymptotic count of the isosceles dual pairs D_{u,v}, which gives N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X.
- **Theorem 3.** N(X) ≫ X(log X)², from the whole dual family.
- **Proposition 4.** The dual pairs are points of a quartic del Pezzo surface Y with Picard rank ρ = 5 and a conic bundle over Q. By Browning–Sofos, the dual pairs and their multiples contribute O(X(log X)⁵).
- **Section 6.4.** A heuristic discussion of Question E (is N(X) = X^{1+o(1)}?) in terms of parametric families, and of the threefold of pairs, which is birational to the fibre square of the Γ1(6) rational elliptic surface.

## Significance

The material in my sections is correct and carefully written, but its weight is modest.

- **What is new.** As far as I know, the counting results are new. They use standard tools: lattice-point counting with Möbius inversion (Theorem 2), a crude box count on the conic bundle (Theorem 3), and a direct appeal to Browning–Sofos (Proposition 4).
- **Theorem 3 is weak in practice.** The second bound of Theorem B beats the first only when log X > 438 (p. 3). So "one more logarithm" is a qualitative statement, not a quantitative improvement.
- **The dual family is not pinned down.** It is a rational quartic del Pezzo surface with ρ = 5, so its expected contribution is of order X(log X)⁵. The note proves only that as an upper bound, with X(log X)² as the lower bound: a gap of three logarithms. Question E is left completely open.
- **Fit for the journal.** This scope is acceptable for Integers, and the note is honest about its limits. Its value is that it organises the problem cleanly: the torsion and positivity analysis (outside my scope), the explicit identification of the dual family with a del Pezzo surface, and exact data.

What is good: the proofs in Section 4 are complete and the constants are right. The hypotheses of the one deep cited theorem (Browning–Sofos) are met. Every number I could test reproduces exactly. The literature section is unusually conscientious.

## Correctness, and what I recomputed

I found **no mathematical error** in Sections 1, 4, 6.4 or Remark 1. My own checks were:

1. **Section 1.1 (p. 2).** The heat constant term χ/6 + Σ(m_i² − 1)/(12m_i), with χ = R − 1, equals (S + R − 2)/12. The area 2π(1 − R) is right, so area and constant term determine (S, R) and conversely.
2. **Section 1.3 (p. 3), Tate normal form.** Symbolically, with c = −1/Λ:
   - The stated substitution turns the Tate normal form into E_Λ/(64Λ⁶), so it is an isomorphism.
   - The cubic's discriminant is 2⁸Λ²(Λ−1)³(Λ−9), giving Δ = 2¹²Λ²(Λ−1)³(Λ−9).
   - Tate's point (0,0) corresponds to the plane point (0:1:0).
   - At Λ = 27/2, the point (1:4:4) maps to (−6, 45), which lies on E_Λ.
3. **Theorem A, integer case (p. 3).** For integer Λ, (Λ−1)(Λ−9) is a square only at Λ = 10, and (r + 1 + 1/r)² is an integer only for r = ±1. So "only (1:1:2) and (1:2:2), at Λ = 10" is right.
4. **Theorem 2 (pp. 12–13).**
   - Sums, reciprocal sums, g ∈ {1,3} (g = 3 iff u ≡ v ≢ 0 mod 3), primitivity, and distinctness of the two members (equality would force u = v) all check.
   - |Ω| = (log 2)/6.
   - The Möbius step is right: the sum of μ(d)/d² over 3 ∤ d is (6/π²)(9/8), which gives the factor #U/8.
   - c_iso = 3 log 2/(2π²) = 0.1053457…
   - The class-distinctness argument via Λ = 5 + 2(u/v + v/u) holds.
5. **Numbers after Theorem 2 (p. 13).**
   - There are 506 pairs D_{u,v} with S ≤ 4800, against c_iso·4800 = 505.66.
   - The copies at X = 4800 number 2917, which is 0.6077X.
   - (count − c_iso X log X)/X is −0.28597, −0.28621, −0.28628, −0.28628, −0.28628 at X = 10⁴, 10⁵, 10⁶, 10⁷, 4·10⁷.
   - Enumerating each class directly gives exactly 27 of the 506 in classes of size at least 3.
   - The same enumeration confirms the classes at S = 136, at S = 408 (four members, including (51,102,255)) and at S = 845.
6. **Lemma 6 and Theorem 3 (p. 14).**
   - The algebra is correct, and each pair arises from at most 6 tuples.
   - The box bound holds: αU = βV and U ≤ αV give W ≤ 4αβV² = y.
   - The error term is O(y^{7/8} log y).
   - c_A = 3/(32π⁴), and the final constant is 3/(128π⁴) = 2.406·10⁻⁴.
   - The ratio c_iso/(3/(128π⁴)) is 437.83.
7. **Proposition 4 (pp. 15–16).**
   - The five cubic forms have rank 5.
   - Exactly two independent quadrics vanish on Y. In six coordinates they are y1y4 = y2y5 = y3y6.
   - A Gröbner-basis computation shows the singular locus is empty, so Y is a smooth quartic del Pezzo surface.
   - The statements about the sixteen lines, ρ_Q = 5, and height ≤ S_D all check.
   - I read Browning–Sofos (arXiv:1609.09057v4). Theorem 1.1 assumes X(Q) ≠ ∅ and that X contains a conic defined over Q. It gives c1·B(log B)^{ρ−1} ≤ N_U(B) ≤ c2·B(log B)^{ρ−1} for the standard height on P⁴. Y satisfies these hypotheses, so (iii) is valid.
8. **Remark 1 (p. 12).** The proof is complete. In the second two-line case, (a+b)² = ab is impossible because (a+b)² ≥ 4ab.
9. **Section 6.4.**
   - My count of the candidate lines is 189, matching the text.
   - 7626/46254 = 16.49% and 38624/46254 = 83.50%.
   - The equation is indeed quintic.
   - The twelve surfaces (six orderings, six duals) are consistent with Lemma 3 and Proposition 3.
10. **Literature spot checks.**
    - Moreland–Zieve do give the counterexample (3,10,24).
    - Chen's survey (Appendix A.5.1) lists the solutions and chain exactly as quoted, and records Choudhry's three-parameter solution.
    - The MacLeod substitution gives R/r = (Λ−1)/4.
    - The Bremner–Macleod substitution gives Λ = 2N + 6.
    - No triple with entries below 400 has an integer Λ divisible by 4, consistent with Nguyen Xuan Tho.
    - The local exponents quoted in the introduction recompute from Table 3.

## FATAL

None.

## MAJOR

**M1 (pp. 5–6). Choudhry [11] has not been consulted, so the attribution of the dual and isosceles families is unresolved.**

Chen's survey records a "three-parameter solution" of exactly this system. The dual family is also three-parameter (a point of P² plus scaling), so the two very likely coincide. OpenAlex and Unpaywall list Choudhry's paper (Rocky Mountain J. Math. 41(3) (2011) 737–763, doi:10.1216/RMJ-2011-41-3-737) as free to read on Project Euclid. "Not accessible to us" is therefore not tenable. My headless download was blocked by the publisher's bot protection; a browser should open it.

This affects Section 1.4, the novelty paragraph on p. 6, and how Corollary 1, Lemma 6 and Theorem 2 are framed.

*Fix:* read the paper, state its exact relation to Corollary 1 and Lemma 6, re-attribute as needed, and delete the "not accessible" sentence.

**M2 (p. 4). The justification for Proposition D in the introduction is misleading.**

The text says S^{2+ε} "is the size one expects for such points in general".

- (a) The S² scale comes from the trivial components, not from generic points. At fixed S, the five planes x′ = σ(x) with σ ≠ id each carry about S² integer points. Any general dimension-growth bound is stuck at S² for that reason. The real problem is counting integral points off these linear subspaces, and the text should say so.
- (b) The ε is removable. Sum the divisor bound over (p, p′) instead of using τ ≪ S^ε uniformly. Since τ(p²p′²AA′) ≤ τ(p²)τ(p′²)τ(S−p)τ(S−p′), Shiu's theorem gives n(S) ≪ S²(log S)^C, and hence N(X) ≪ X³(log X)^C.

*Fix:* reword the paragraph; optionally sharpen the bound.

**M3 (pp. 21–22). Section 6.4 claims less than it can prove, and misstates the scope of its search.**

- (a) **The "heuristic" is a theorem.** A surface in the variety of pairs that is parametrised, generically finitely, by quadratic forms in three variables, positive on an open cone, gives N(X) ≫ X^{3/2} unconditionally by counting lattice points in the cone. The same holds for any family with m/d > 1. Restricting to a generic 2-plane together with Remark 1 also excludes d = 1 in any number of variables. State this as a lemma.
- (b) **The search criterion is incomplete.** For two lines L1, L2, the correspondence {(p, p′) : Λ(p) = Λ(p′)} is a curve of bidegree (3,3) in L1 × L2. A one-parameter family can come from any rational component of it, not only from graphs of Möbius maps (bidegree (1,1)). For example, when L1 = L2 the part left after removing the diagonal has bidegree (2,2) and can be rational. So "the only such families" holds only relative to the (1,1) test.
- (c) **The search bears only indirectly on Question E.** A single curve contributes at most X^{1+o(1)}, because Remark 1 forces d ≥ 2. Only families of curves that sweep out a surface matter, as the dual conics do. Say this explicitly.
- (d) **Recommended framework.** Section 6.4 already notes that the variety of pairs Z is a quintic in P⁴, birational to E ×_{P¹} E.
  - A fibre product of rational elliptic surfaces with a section has trivial canonical bundle. To my knowledge, self-fibre products of Beauville's semistable surfaces are Schoen's rigid Calabi–Yau threefolds (see also Verrill's work on their L-series); the authors should check and cite this exactly.
  - So in the Batyrev–Manin sense a(O(1)) = 0, the same "n + 1 − d = 0" expectation as for a quintic in P⁴. Generic primitive pairs should then number y^{o(1)}.
  - N(X) is then governed by accumulating subvarieties, ranked by their Fujita invariant a: planes (a = 3, the trivial pairs), quadric surfaces and lines (a = 2), Veronese-type surfaces (a = 3/2), and conics or anticanonically embedded del Pezzo surfaces such as Y (a = 1).
  - Question E then becomes: apart from the trivial planes, Z contains no subvariety with a > 1 whose positive real points are Zariski dense.
  - This framework also flags something in the data. 83.5% of primitive pairs are of the "third kind", which the Calabi–Yau heuristic predicts should be sparse. Either there are further a = 1 surfaces inside Z, or the asymptotics set in very late. Either is worth saying.

  I do not make (d) a condition of acceptance.

*Fix:* (a) add the lemma; (b) and (c) qualify the search statement; (d) recommended.

## MINOR

- **m1 (p. 5).** A brute-force search up to S = 40 finds pairs at S = 18, 20, 26, 31, 32, 34, …. In particular {(4,9,18),(5,6,20)} (S = 31) and {(4,14,14),(5,7,20)} (S = 32) are smaller than Chen's {6,14,14},{7,9,18} (S = 34), by sum and by largest entry. The parenthetical "(the pairs at S = 18 and S = 20 are smaller)" is therefore incomplete. Chen's "smallest" is not minimal in any ordering.
- **m2 (p. 3).** Write "the elliptic modular surface of Γ1(6)". Elliptic modular surfaces need −1 ∉ Γ. The identity ±Γ1(6) = Γ0(6) is correct as a statement about groups.
- **m3 (p. 4).** "Theorem B is needed only for the lower bound A(y) ≫ y": that lower bound is Theorem 2's count A_iso, not Theorem B, which is about N.
- **m4 (p. 3).** "Only when log X > 438" compares leading terms only, and the o(1) terms are unspecified. The crossover of leading terms is at log X = 437.8.
- **m5 (p. 14).** Theorem 3 loses avoidable constant factors:
  - Keeping only D with S_D ≤ X/K, for K → ∞ slowly, removes the factor 2.
  - Taking M = y^{1/6−ε} instead of y^{1/8} gains a factor 4/3.

  Either remove these losses, or drop the explicit constant 2.4·10⁻⁴ from the introduction.
- **m6 (p. 15).** "…rank 5, and Y(Q) ≠ ∅" does not follow from the Galois computation. Give a point, for example D(1:1:1) = (1:1:1:1:1), or note that Y is rational over Q.
- **m7 (p. 15).** Quote the Browning–Sofos hypothesis as stated ("contains a conic defined over Q", together with X(Q) ≠ ∅). Also note that the conic bundle |H − E1| has the rational section E1. The upper bound then also follows from the Salberger/Leung argument that Browning–Sofos mention, which gives an independent reference.
- **m8 (p. 16).** Browning–Sofos also cite Frei–Loughran–Sofos (Theorem 1.2): lower bounds of the right order for quartic del Pezzo surfaces with a conic bundle over Q and ρ ≥ 4, which applies here (ρ = 5). Check whether that proof, or the Browning–Sofos lower bound, localises to the positive real region. If it does, Theorem 3 upgrades to N(X) ≫ X(log X)⁵ and the gap closes. If not, explain why.
- **m9 (p. 16).** "A pair comes from at most twelve points" is not needed for an upper bound. Drop it or say where it is used.
- **m10 (p. 13).** Write log 2 instead of ½ log 4, and make explicit the range of d in the Möbius sum (the terms with d > t vanish).
- **m11 (p. 21).** The heuristic count X^{m/d} counts non-coprime parameters, whose pairs are multiples by k^d, not k. Reconcile this with "X log X once the copies are counted".
- **m12 (p. 22).** Note that the fibre square has n² ordinary double points over each I_n fibre. This is what Schoen's construction needs.

## PRESENTATION

- **P1 (p. 14).** The heading "(One more logarithm; the constant is not optimised)" carries editorial content. Use "(The dual family)" and keep the caveat in the text, where it already appears on p. 15.
- **P2 (p. 3).** Consider presenting the X(log X)² bound as a remark on the dual family rather than half of a headline theorem, since the text admits it is weaker for every realistic X.
- **P3 (p. 15).** State Y explicitly: Y = {y1+y2+y3 = y4+y5+y6, y1y4 = y2y5 = y3y6} ⊂ P⁵ (I checked these quadrics span the ideal).
  - It shows the del Pezzo structure and three conic bundles at once, for example (y1:y2) = (y5:y4), which also makes m7 transparent.
  - It gives a clean characterisation: a dual pair is exactly a pair of equal-sum triples with x_i·x′_i the same for every i, after ordering.
- **P4 (pp. 21–22).** Identify the variety of pairs with Z ⊂ P⁴ before the heuristic, since the heuristic is about subvarieties of Z.
- **P5 (p. 4).** After M3(a), say that the requirement described in Section 6.4 is a proven necessary condition.

---

## Recommendation

**Minor revision.** Confidence is high on the correctness of Sections 1, 4, 6.4 and Remark 1, and moderate on the overall assessment.

Every proof I checked is correct, and every number I could recompute agrees with the text. The one deep cited counting theorem is applied within its hypotheses. The problems are:

- an attribution question that reading a freely available paper settles (M1);
- a misleading justification in the introduction (M2);
- an understated and imprecisely scoped Section 6.4 (M3).

If Choudhry's family turns out to be the dual family, the introduction and Section 4 need re-attribution. That would be a larger change of presentation, though not of mathematics.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Read Choudhry 2011; state its relation to Corollary 1, Lemma 6 and Theorem 2; re-attribute; remove "not accessible". |
| M2 | Say that the S² scale comes from the trivial planes; optionally improve the bound to S²(log S)^C. |
| M3 | Add the m/d > 1 lemma; restrict "only such families" to the (1,1) test or test all rational components; explain the surface-sweeping point; optionally add the Calabi–Yau / Fujita-invariant framing. |
| m1 | Correct the parenthetical (pairs at S = 31 and 32). |
| m2 | Γ1(6) wording. |
| m3 | Attribute A(y) ≫ y to Theorem 2. |
| m4 | "Leading term … log X > 437.8". |
| m5 | Remove the trivial losses or drop the constant from the introduction. |
| m6 | Exhibit a rational point on Y. |
| m7 | Quote the hypothesis as stated; mention the section E1 and the Salberger/Leung route. |
| m8 | Examine the Frei–Loughran–Sofos / Browning–Sofos lower bound for the positive region. |
| m9 | Drop or relocate the sentence. |
| m10 | log 2; range of d. |
| m11 | Reconcile X^{m/d} with the counting of copies. |
| m12 | Mention the nodes of the fibre square. |
| P1–P5 | As stated. |

---

The scripts I used are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/N-c-rational-points-on-surfaces/scratch/code/`:
- `c1.py`: Tate normal form and the plane-to-Weierstrass map
- `iso.py`: isosceles counts and constants
- `cls.py`: class enumeration
- `dp4.py`: del Pezzo checks and smoothness
- `ntho.py`: search for integer Λ divisible by 4

Downloaded papers (Browning–Sofos, Chen's survey, Moreland–Zieve) are in `scratch/lit/`, and the rendered pages are in `scratch/pages/`.
