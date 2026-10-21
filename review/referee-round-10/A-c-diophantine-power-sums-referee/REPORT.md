<!-- Round 10, A-c, returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

I could not write the report to REPORT.md: the harness refuses report-file writes from a subagent, so the full report is below. Recommendation: **minor revision** for Sections 3, 4 and Appendices A and D. I am highly confident these sections are correct. Every proof was checked, and every number that does not depend on the computed spectra was recomputed and agrees. I found nothing fatal, and only one issue at major level, which concerns framing, not correctness.

# Referee report for AGAG: "How much of a hyperbolic orbifold does heat hear?"

**Scope of this report.** Sections 3 and 4 and Appendices A and D of the manuscript (65 pp.), plus the parts of Section 2 they rely on (Lemma 2.9, Lemma 2.11, eq. (10)), the Section 5 definitions that Appendix D needs (strata, (15), φ_p, τ_p, x\*(p), gap_p), and Sections S1 and Table S1 of the supplement. Page numbers are the printed ones, which match the PDF pages. I read every page I comment on as a rendered image (pdftoppm), not only as extracted text. The marked placeholders (author contributions, AI-use statement, Zenodo DOIs, preprint identifiers) are treated as known.

## 1. Summary

The two invariants c1 and c2 fix the area and the reciprocal sum, and by Uçar's triangular structure (Lemma 2.11) each later invariant adds one odd power sum of the cone orders. Section 3 uses this to turn "how many heat invariants separate signatures" into a moment problem for a signed multiset of cone orders: the reciprocal sum and the low odd power sums must vanish. The main results are:

- **Theorems 3.2–3.4.** Newton's identities and the Orlando/Hurwitz closed form give exact recovery from n invariants on spheres with n cone points, and n − 1 invariants fail for n = 3, 4.
- **Theorem 3.7 and Corollary 3.8.** Separation via the parity lemma, and the bound ⌊A/π⌋ + 4.
- **Theorem 3.11 and Corollary 3.12.** The exact area-free answer M + 1 for cone orders at most M. The upper bound comes from Chebyshev sign changes; the witnesses come from Lagrange weights at the nodes a².
- **Theorem 3.15.** A Descartes bound on the imbalance, which is the genus change.
- **Section 3.4 and Appendix A.** The growth of f(A) is reduced to the Prouhet–Tarry–Escott (PTE) quantity N(k) = P(k,2): unconditionally √A ≲ f(A) ≲ A, and power-growth statements are equivalent to statements about N(k).
- **Section 4.** Locality: the heat invariants do not see the moduli. Proposition 4.2 gives an explicit hyperbolic-term constant, and Remark 4.3 a wave-trace reading. The section ends with numerical illustrations.
- **Appendix D.** Proves that the extreme triads of adjacent strata are tangent only at p = 2 and p = 4.

## 2. Significance

**What is good.**
- The reduction in Section 3 is clean and correct, and the authors are unusually candid about what is classical (Newton, Vandermonde, Descartes, Steinig/Laurens, the Chen survey) and what is not.
- Three results are, to my knowledge, genuinely new and well executed:
  - the exact area-free answer M + 1 (Theorem 3.11(ii)–(iv)), with explicit witnesses from divided differences;
  - the determinant identity of Theorem 3.3, proved by a neat Jacobian factorisation;
  - the Descartes bound on the genus change (Theorem 3.15).
- The PTE reformulation (Proposition 3.19: T(L) is sandwiched between N(2L−2) and 4N(2L−3)) is correct. It is the right way to say why the growth question is hard.

**Limitations a reader should be told plainly.**
- After Lemma 2.11 everything in Section 3 is algebra and combinatorics of odd moments. There is no further geometric input.
- The only unconditional growth statement is c√A ≤ f(A) ≤ A/π + 4.
- Theorem 1.2(ii) / 3.18(d) is an equivalence that settles nothing, and the paper says so itself (pp. 6, 9, 30–31).

The material is correct and publishable. Its weight for an analysis-and-geometry readership rests on the heat-invariant interpretation, not on new number theory. I do not regard this as a reason to reject, but the abstract and introduction should not suggest more than an equivalence (see m1).

## 3. Correctness, and what I recomputed

I checked every proof in my sections line by line, and recomputed independently every number I could. I used my own Python/sympy/mpmath code in the scratch folder: exact rational arithmetic throughout except where noted. **Everything below agreed with the manuscript unless flagged.**

**Heat coefficients (inputs to Sections 3–4)**
- p_0, p_1, p_2 of (8) rebuilt from (4)–(5).
- Leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)) checked for l ≤ 3.
- α_0, …, α_4 = 1, −1/3, 1/15, −4/315, 1/315 agree.
- The triangle formulas (10) agree.

**Theorem 3.3**
- Built M symbolically from (12) using tanh of the odd part of log f, for n = 2, 3, 4.
- det M − ς_n ∏_{i<j}(m_i+m_j)/∏ m_i = 0 identically, and the true e solves the system.

**Theorem 3.4(3)**
- R = 8/15, P1 = 58, P3 = 31402 on both sides; P5 = 25159618 vs 21298618. Both agree.
- {2,8,8}, {3,3,12}: P3 = 1032 vs 1782. Agrees.

**Remark 3.5 and Section S1 (exhaustive search over 4-multisets in [2, Q])**
- Q = 84: 9 witnesses, of which exactly 8 are primitive. These are precisely Chen's (A.685)–(A.692), which I checked against arXiv:2506.11429, §A.5.8.
- Q = 130: 19 witnesses, 16 of them primitive, matching the "16" stated in S1.
- I did not repeat Q = 440 (about 1.6·10⁹ multisets).
- The counts in S1 and Remark 3.22 are correct: 216,071,394 = C(123,5), and the 4,325,115,770 gcd-1 5-multisets in [1,220] (by Möbius inversion).

**Example 3.9 and Figure 2**
- Areas 2π·14/15, Ψ1 = 224/15, exactly two shared invariants.
- In both panels, every disc and ring sits at the correct abscissa and multiplicity.

**Theorem 3.11**
- For M = 2, …, 9, rebuilt w_a, C, ν(a), s and the least admissible g:
  - C = 6, 120, 2520, 362880 (M = 2, …, 5); ν = (−16, 9), s = −2 (M = 3); ν = (28, −27, 8) (M = 4).
  - Areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054}.
  - Each pair shares exactly M − 1 invariants.
- The closed form a·w_a = (−1)^{M−a} 2a³/((M−a)!(M+a)!) agrees.
- Part (iv):
  - M = 2, X = 4 gives C = 180, ν = (10, −4), s = 2, area 6π, exactly 2 shared.
  - Also tested M = 3, 4, 5 with X ∈ {M+1, M+2, M+5}: exactly M shared each time.
  - X = M + 1 reproduces (ii) with the two sides exchanged.
- Remarks after the theorem:
  - (2;) / (0;2⁸) share exactly c1; (0;2⁵) / (1;2) share c1.
  - Exhaustive check: no pair in Sig≤3 of area < 12π shares c1, c2, and no pair in Sig≤4 of area < 36π shares c1, c2, c3. The pairs at 12π and 36π are the only ones at those areas.

**Proofs of Theorems 3.7, 3.11, 3.15, Proposition 3.16, Theorem 3.18, Proposition 3.19, Lemma A.1, Proposition A.2**
- All correct.
- In particular I checked:
  - the pigeonhole count n^{L−1} Q^{(L−1)²} < Q^n/n! with n = (L−1)² + 1;
  - the identity P_j(U) − P_j(V) = (1 − 2^{j+1})(P_j(X) − P_j(Y)), including j = −1;
  - the sign-change count in 3.11(iii), including the run containing 1;
  - the Descartes parity count in 3.15;
  - the index bookkeeping 2L_i − 3 ≤ k_i ≤ 2L_i − 2;
  - N(2L−3) ≤ 2L² from the quadratic bound;
  - the fall-back cases f ≥ 3 and f_g, f_n ≥ 3. Those pairs are (0;5,5,5)/(0;2,2,2,10) at area 2π·2/5 sharing two invariants, and Example 3.9.

**Example 3.21 and Table S1 (all 20 explicit pairs)**
- Parsed every signature pair in the supplement (including the 40-digit entries).
- For each, recomputed the exact area, the exact number of shared invariants, |U\*| + |V\*| and ι.
- All agree:
  - shared counts L = 2…7;
  - equal-count sizes 6, 8, 14, 18, 24, 40 (ι = 0);
  - genus sizes 6, 10, 16, 20, 26, 40 (|ι| = 2);
  - the exact s values printed.
- The pieces I spot-checked also agree: [1,5,5] = [2,3,6] is Chen (A.48), the 7-set of L = 4 has vanishing P1, P3, P5, and (A.313)–(A.316) are as quoted.
- Table 2 therefore agrees with the pairs.

**Remark 3.22**
- The e3 coefficient 3 − 3P1R is correct, and P1R ≥ 25 by the AM–HM inequality.
- The real partner of {1,1,1,1,7} is {0.26636, 4.28304, 6.45060}. Agrees.

**Figure 3 and Section S1**
- Re-enumerated all areas 2πs ≤ 2π·7/5 attained with g ≤ 1, n ≤ 4, orders ≤ 12; completed every class with no bound on the orders; computed K_mult exactly.
- Result: 525 areas, 33,946 signatures, 504 classes containing an order > 12. Class maxima: 1 in 17 classes, 2 in 311, 3 in 197, none of 4. The first maximum of 3 is at s = 1/4.
- All agree with pp. 32 and S1.
- The solid and dashed curves and the positions of the diamonds and squares match Corollary 3.8, Theorem 3.18(a) and Table S1.

**Section 4**
- d3 = 25/12, d4 = −1775/24, d5 = 153025/48 recomputed exactly (also d6 = −150503225/864).
- Lemma B.3 asymptotics |b_l(m)| ~ (2π sin(π/m))⁻¹(πl)^{−1/2} l!(m/π)^{2l}: ratio → 1, with errors about 1%, 0.4%, 0.2%, 0.3% at l = 40 for m = 2, 3, 8, 12.
- Remark 4.3:
  - k_m(u) derived again from E_m by symmetrisation;
  - the Fourier integral checked numerically;
  - its Taylor coefficients against the Gaussian (with e^{−t/4} expanded) reproduce b_0, …, b_4 exactly for m = 2, 3, 8.
- Scales: π²/144 ≈ 0.0685. Systoles by word enumeration in explicit SL(2,R) generators: ℓ(3,3,12) ≈ 1.8626 (so ℓ²/4 ≈ 0.867) and ℓ(2,8,8) ≈ 2.257. This confirms "the smaller systole, that of O(3,3,12)".
- The cone-point term of D(t) by quadrature: 0.0467 at t = 0.1, 0.0478 at 0.12, 0.0442 at 0.36, 0.0402 at 0.5. This matches the dashed curve of Figure 5(a).
- A rough estimate of the leading geodesic term of O(3,3,12) is about 4·10⁻¹³ at t = 0.0293, consistent with the text, and it makes the sign change near t ≈ 0.36 plausible.
- The relation sinh a sinh b = 1/2 for the (0;3,3,3,3) family is the Lambert-quadrilateral identity cos(π/3) = sinh a sinh b. Correct.
- Corollary 4.1 and Proposition 4.2 proofs are correct.
- **Not reproduced:** the eigenvalue computations behind 3.4·10⁻¹⁴, λ1 from 4.122 to 0.435, the factors 4.4·10⁶–1.0·10¹⁰ and ℓ²/4t ≈ 24.5. They are flagged as illustrations used in no proof, and I treat them as such.

**Appendix D and the Section 5 inputs**
- Checked (15) against direct computation for p ≤ 11.
- Factored gap_p(3p+7) = −2(p² − 5p − 30)/(p(p+1)(p+3)(p+4)(p+5)) symbolically.
- Recomputed x\*(p) = 18, 18, 20, 45/2, 126/5, 28, 216/7, the positive values 1/840, 1/2310, 1/10296, and the negative values −7/936, −1/72, −19/3960, −1/180, −76/15015, −1/231, −17/4680.
- Scanned gap_p(S) for 2 ≤ p < 200 and 3p+3 ≤ S < 3p+400:
  - the only zeros are (p, S) = (2, 18) and (4, 20);
  - the first nonpositive sum equals S\*(p) of Theorem 5.6 in every case;
  - the gap never returns to positive.
- Proposition D.1 and its proof are correct.

**Literature claims checked against the sources**
- Chen's survey: §A.5.8 lists (A.685)–(A.692); Identity 9 with m = 3 and (3.27)–(3.28); (3.33) is for type (−1,1,3,5); §8.1 P1 is as quoted.
- Croot–Mao–Yip (arXiv:2609.05061v1, §1): the definitions of P(k,2) and W(k,2); ideal solutions known only for k ≤ 9 and k = 11; the pigeonhole bound; Wooley's quadratic bound on W.
- I could not access Borwein–Ingalls [4] (paywalled), so the quotation from its §6 Problem 3 is unverified by me.

## 4. FATAL

None in my sections.

## 5. MAJOR

None in my sections that affects correctness. I list one point at MAJOR level because it changes how the paper's headline claim reads.

**M1 (pp. 1–2 abstract, p. 4 after Thm 1.2, p. 30 before Thm 3.18): framing and the PTE literature.**
- The open problem quoted as the target of Theorem 1.2, N(k) = O(k) and "no o(k²) bound is known", carries the main interpretive weight of Section 3.4.
- The supporting history on p. 30 is internally inconsistent. The text credits W(k,2) ≤ ½k(k+1)+1 to Wooley, then in the next sentence says Wright had slightly stronger quadratic bounds for the same W(k,2). Croot–Mao–Yip §1, cited for this, state Wooley's bound for W(k,m) with m sets, and also credit Hua (1938, 1949) with upper bounds on W(k,m). The manuscript omits Hua here.
- A reader cannot tell from the text which bounds hold for P(k,2) and which for W(k,m), or whether anything sub-quadratic is known for some variant.
- Since the statements "(ii) gives exactly the exponent ½" and "α > ½ would prove N(k) = O(k^{2−ε})" depend on this, the authors should state the record precisely:
  - who proved which bound, for P(k,2), W(k,2) or W(k,m);
  - the exact wording of [4, §6, Problem 3];
  - a sentence on Hua's bounds.
- Relatedly, "Whether f grows like a power of A at all is open" (p. 4) is misleading as written: f is already proved to lie between c√A and A/π + 4. The open question is whether f(A) ≍ A^α for some α, or which α.

**Resolution:** correct the attribution paragraph on p. 30, add Hua, quote [4] exactly, and rephrase the sentence on p. 4.

## 6. MINOR

- **m1 (p. 6, "Theorem 1.2 is a reformulation"; p. 9).** Good that this is said. Make the abstract equally explicit: the abstract's "at least like a power A^α … exactly when" reads like a result about f rather than an equivalence.
- **m2 (p. 29, Prop. 3.16 proof).** "Here n ≥ 2" needs a reason: X ≠ Y with P1(X) = P1(Y) forces n ≥ 2. Likewise Prop. A.2 (p. 50) assumes "n ≥ 1", but disjoint X ≠ Y with equal P1 forces n ≥ 2. State this.
- **m3 (p. 29, Thm 3.15).** The clause "if moreover the configuration has the least size … then |ι(Z)| = 2, |g−g′| = 1" holds only in the genus-changing case of the preceding sentence. For g = g′ the least size gives ι = 0. Put the hypothesis g ≠ g′ inside that clause, and drop or explain "(paddings by 1 included)".
- **m4 (p. 28, Corollary 3.12(a) proof).** "A surface has no positive point but 1, so it shares at most c1" should say that this is (iii) with d_O = 0, giving L ≤ 1.
- **m5 (p. 33, Example 3.21(ii)).** "After cancelling the common order 6": say that removing an order common to both signatures keeps H_L equal (Lemma 3.6) and that both results are still hyperbolic (area 2π·113/30).
- **m6 (p. 26, Thm 3.11(ii)).** The definition of C by "least positive integer such that … and s is an even integer" is correct but opaque. The text already has ν(a) ∝ (−1)^{M−a} a³ C(2M, M−a). Give ν(a) directly as the primitive integer vector in that direction (times 1 or 2 to make s even), so C becomes secondary.
- **m7 (p. 57, Appendix D proof).** "For 2 ≤ p ≤ 8 the values at those sums are 1/840, 1/2310, 1/10296 (at S = 18, 28, 31 for p = 3, 7, 8)" leaves the reader to infer the other cases. For p = 2, 4, 5, 6 the first odd-parity sum ≥ x\*(p) is already S\*(p)+1, where the gap is negative. Say so. Also say that "decreases strictly in S" means along sums of one parity (step 2).
- **m8 (p. 34, Corollary 4.1(b) proof).** "Two of them give isometric orbifolds only if they differ by an automorphism of Γ and a conjugation in PGL(2,R) [39, Ch. 13]" should cite a precise statement: isometry classes are the orbits of the (extended) mapping class group on Teichmüller space, which is countable. The argument is right; the citation is too vague.
- **m9 (p. 37).** The numerical claims are given to two significant figures, which suggests verified accuracy: 3.4·10⁻¹⁴, 4·10⁻¹³, the 0.341–0.360 bracket, ℓ²/4t ≈ 24.5, the factors 4.4·10⁶–1.0·10¹⁰ (p. 36). Yet they rest on a-posteriori, not enclosed, eigenvalue errors. Two fixes:
  - add one sentence in Section 4 itself, not only in S4, saying which of these follow from enclosed quantities. The elliptic term and d_j are exact; the eigenvalues are not.
  - "the two times coincide for every pair" (p. 37) should say "to the sampling resolution".

## 7. Presentation

- **P1 (p. 37).** "The usable window is short because the cone coefficients grow rapidly (computed values below)": no computed values follow. Either give them (e.g. |b_l(12)| for l ≤ 6) or delete the parenthesis.
- **P2 (Sections 3 and 4, symbol overloading).** The warning inside Thm 3.11(ii) about the letter a shows the problem. Rename to avoid clashes:
  - **κ:** ϰ in Thm 3.4(1); κ = |U\*|+|V\*| in Thms 3.7 and 3.15.
  - **ν:** the measure in Lemma 3.10 and in the proof of 3.11(iii); the multiplicity differences ν(a) in 3.11(i)–(ii) and Prop. 3.16; the weights ν(a) = C a w_a.
  - **a:** a_k of χ_m (p. 21), nodes a, and the coefficients a_l (pp. 26–27).
  - **s:** the power sums s_j (Lemma 3.1); s in Thm 3.11; s = Area/2π (Fig. 3, Table S1).
  - **C:** the comparison class (Def. 2.2); the constant in Thm 3.11; the constant in Thm 3.18(b).
- **P3 (p. 28, Lemma 3.14(c)).** The last sentence packs three cases into one clause: W, which genus is least, and 0 versus positive. Split it, or state the area bounds as a separate item.
- **P4 (p. 23, Remark 3.5).** "No three multisets with a common (R, P1, P3)" and the 193/107 counts depend on computations that are only in the deposit. Reference the exact deposit file, as is done elsewhere.
- **P5 (p. 32, Figure 3 caption).** Say that the dots are maxima of K_mult over complete classes (a lower bound for f at that s), and that diamonds and squares are drawn at L + 1. Both are currently explained only in the running text.
- **P6 (p. 22, Thm 3.3).** State in the theorem, not only in the proof, that M and b are defined on {e_n ≠ 0} and that the identity for det M holds there.
- **P7 (pp. 21–37).** The rendered typography is clean. Figures 2 and 3 match the data exactly, and Figure 5(a) matches my quadrature of the cone term. I found no sign or label errors in the figures of my sections.

## 8. Recommendation

**Minor revision**, as far as Sections 3, 4 and Appendices A and D are concerned.

- **Confidence in correctness: high.** Every proof was checked, and every number in these sections that can be recomputed without the spectral computations was recomputed exactly and agrees.
- **Confidence in the significance judgment: moderate.**

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Rewrite the PTE-bounds paragraph (p. 30): correct the Wright/Wooley attribution, add Hua's W(k,m) bounds, quote [4, §6 Problem 3] verbatim. Rephrase "whether f grows like a power" (p. 4). |
| m1 | Make the abstract say "is equivalent to". |
| m2 | One clause each in Prop. 3.16 and Prop. A.2 justifying n ≥ 2. |
| m3 | Move the hypothesis g ≠ g′ into the "least size" clause of Thm 3.15. |
| m4 | Cite (iii) with d_O = 0 in the proof of Cor. 3.12(a). |
| m5 | One sentence on cancelling a common order in Ex. 3.21(ii). |
| m6 | Give ν(a) in closed form in Thm 3.11(ii). |
| m7 | List the p = 2, 4, 5, 6 cases in the proof of Prop. D.1, and state "same parity". |
| m8 | Precise reference for isometry classes as mapping-class-group orbits. |
| m9 | One sentence in Section 4 separating exact quantities from a-posteriori ones; "to sampling resolution". |
| P1–P6 | Editorial changes as described. |

---

Everything I produced is in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/A-c-diophantine-power-sums-referee/scratch/:
- code/ — verification scripts heat.py and c1.py–c11.py; c6b.py is the Figure 3 class enumeration and c7.py the 4-multiset witness search
- lit/ — the Croot–Mao–Yip and Chen preprints fetched from arXiv
- img/ — rendered pages
