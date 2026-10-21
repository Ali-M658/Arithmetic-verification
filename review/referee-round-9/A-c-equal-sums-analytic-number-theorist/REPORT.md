<!-- Round 9 A-c referee report: returned text saved verbatim; the reviewer could not write files -->

Writing REPORT.md was refused (the harness does not let subagents write report files), so the full report is below. My scratch work (renders, literature PDFs, scripts) is in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/A-c-equal-sums-analytic-number-theorist/scratch/.

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

**Referee:** analytic number theory (equal sums of like powers, the Prouhet–Tarry–Escott problem, counting their solutions)

**My part of the manuscript:** Section 3 (pp. 20–33), Section 4 (pp. 33–37), Appendix A (pp. 48–49), Appendix D (p. 55), and the supplement's Sections S1, S2 and S7 (searches, explicit pairs, strata), pp. 1–8 and 14–15. Page numbers are the printed numbers; I checked them against the rendered pages. The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) are taken as known.

## 1. Summary

Using the triangular structure of the constant-curvature cone coefficients (Lemma 2.11), Section 3 turns the question "how many heat invariants determine the signature?" into a moment problem. One forms the signed multiset of cone orders, padded by 1s, and asks that its reciprocal sum and its odd power sums up to degree 2L−3 vanish. The section then proves the following.

- **Newton/Orlando results:**
  - Uniqueness from n invariants on spheres with n cone points (Thm 3.2).
  - The linear system for the elementary symmetric functions, with determinant ±∏(m_i+m_j)/∏m_i (Thm 3.3).
  - The fibres of n−1 invariants (Thm 3.4).
- **Separation:** |U\*|+|V\*| ≥ 2L+2 (Thm 3.7), and with it the area bound ⌊A/π⌋+4 (Cor 3.8).
- **Bounded orders, the exact area-free answer M+1** (Thm 3.11). The upper bound comes from the sign-change property of Chebyshev systems. The witnesses are Lagrange weights at the nodes a².
- **Descartes bound on the imbalance:** |ι| ≤ |Z|−2L (Thm 3.15).
- **Growth equivalence:** the least size T(L) of an L-configuration is squeezed between N(2L−2) and min(6(L−1)²+6, 4N(2L−3)), and A_min(L) lies between (π/2)(T(L)−8) and 2πT(L) (Prop 3.19). Hence f(A) ≥ cA^α ⇔ N(k) = O(k^{1/α}) (Thm 3.18).

Section 4 covers the following.

- The heat expansion depends only on the signature (Cor 4.1).
- The closed geodesics enter as an explicit O(t^{-1/2}e^{-ℓ²/4t}) term (Prop 4.2).
- A wave-trace reading of the cone timescale (Rem 4.3).
- A numerical illustration on computed spectra.

Appendix A proves the growth bounds by pigeonhole, doubling (Prop 3.16) and shifting (Prop A.2). Appendix D proves that adjacent triangle strata are tangent only at p = 2, 4.

## 2. Significance

**What is good.** Section 3 is correct, self-contained and honest about what is classical.

- Theorem 3.11 is a clean and, to my knowledge, new exact answer: M+1 against all of Sig, M within Sig_{≤M}, attained. The witnesses (divided-difference weights at a²) are a nice touch.
- The closed-form determinant of Theorem 3.3 is a pleasant identity, and I checked it independently (below).
- Theorem 3.15 is a neat use of Descartes' rule with lacunary coefficients.
- The dictionary between collisions and L-configurations (Lemma 3.14) is exact in both directions, which is what makes the growth equivalence work.

**Calibration.** From the number-theory side, Theorem 1.2 / 3.18 adds nothing to the Prouhet–Tarry–Escott problem. It shows that the growth of f is the PTE minimal-size problem, up to constant factors. The authors say so ("Theorem 1.2 is a reformulation", p. 6). I agree with that self-assessment and ask only that the abstract and introduction keep this tone (see M1).

**Section 4.** No new theorem of substance here. Cor 4.1 and Prop 4.2 are classical in substance (the authors say so). The novelty claimed for the explicit constant and for Remark 4.3 is thin (m7).

**Overall.** The Section 3 material is of genuine, if modest, interest to inverse-spectral readers, and it is correct.

## 3. Correctness, and what I recomputed

I read every proof in my part line by line. Below are the proofs I checked by hand and the claims I recomputed. All computations were done independently in my scratch folder, without the authors' code.

### Proofs checked by hand (no error found)

- **Lemma 3.1, Thms 3.2–3.4, Lemma 3.6, Thm 3.7, Cor 3.8.** This includes the padding identity |U|+|V| = 2max(n+g−g′, n′+g′−g) and the parity argument κ ≥ 2L+2.
- **Lemma 3.10 and Thm 3.11(i)–(iv).**
  - (i): the Vandermonde-minus-first-column determinant.
  - (ii)/(iv): the Lagrange-weight identities, including the a = 1 node absorbing the padding, and s = Σν(a) + Cw₁.
  - (iii): the counts L ≤ M and L ≤ 2d+1, including the left-end run containing the point 1.
  - Cor 3.12 follows.
- **Lemma 3.14(a)–(c)**, including the area bounds < 2π(|W|−2) and ≤ 4π.
- **Thm 3.15.** The gap-parity counting gives V⁺+V⁻ ≤ κ, and at most κ−2L odd-parity gaps.
- **Prop 3.16**, including the n = 2 hyperbolicity case and distinctness via 2x\*.
- **Thm 3.17.**
- **Prop 3.19:**
  - both directions of every equivalence;
  - the formula f(A) = 1 + max{L : A_min(L) ≤ A};
  - attainment of the infimum (well-ordering of the area set);
  - the converse argument along subsequences k_i.
- **Thm 3.18(a)–(d) and Appendix A:**
  - the pigeonhole count n^{L−1}Q^{(L−1)²} < Qⁿ/n! for n = (L−1)²+1, Q > n!n^{L−1};
  - the shift (Prop A.2), with ι(Z(c)) = 2(#{x>−c} − #{y>−c}) and ϱ a nonzero rational function because X, Y are disjoint;
  - the combination step via Lemma 3.20, with λ = −ϱ(c′)/ϱ(c);
  - the bound N(2L−3) ≤ 2L² (from ½k(k+1)+1 with k = 2L−3);
  - the thresholds 16πL² and 12πL², and the small-A fallbacks (Ex 3.9 and the (0;5,5,5) / (0;2,2,2,10) pair, both of area 2π·2/5).
- **Section 4:**
  - Lemma 2.4 and Lemma 2.5 as used in Prop 4.2, including the monotonicity of B in ℓ and the constant C_hyp;
  - Prop 4.2(a)/(b);
  - the kernel identity of Remark 4.3. With a = π−2πj/m, cos(a/2) = sin(πj/m) and cos a = −cos(2πj/m) give exactly k_m. The poles at ±2πi/m come from j = 1 and j = m−1.
- **Appendix D:** Prop D.1, with the parity analysis, the integrality condition (p−1) | 6, and the monotonicity for S ≥ 3p+5.

### Claims recomputed exactly (rational arithmetic unless stated)

1. **Cone polynomials and heat coefficients.**
   - p₀, p₁, p₂ of (8), α₀..α₄, and the leading coefficients |B_{2l+2}|/(2(l+1)!(2l+1)) for l ≤ 5.
   - p_l(1) = 0.
   - d₃ = 25/12, d₄ = −1775/24, d₅ = 153025/48 for O(2,8,8) − O(3,3,12) (p. 36).
   - c₂(2,8,8) = 67/48, matching (10).
   - Lemma B.3's asymptotic, as used on p. 36: the ratio of |b_l(m)| to (2π sin(π/m))⁻¹(πl)^{-1/2} l!(m/π)^{2l} tends to 1 (0.990 at l = 11 for m = 12; 1.015 for m = 3).
2. **Theorem 3.3:** det M = (−1)^{n(n+1)/2} ∏_{i<j}(m_i+m_j)/∏m_i, sign included, and Me = b, for 12 random rational multisets with n = 2..5 and one with repeated entries.
3. **Theorem 3.4(3):**
   - (R, P₁, P₃) = (8/15, 58, 31402) on both sides;
   - P₅ = 25159618 vs 21298618;
   - P₃ = 1032 vs 1782.
4. **Theorem 3.11:**
   - (ν(2), ν(3)) = (−16, 9), s = −2, giving (1;3⁹) vs (0;2¹⁶) at area 12π;
   - (28, −27, 8), giving (0;2²⁸,4⁸) vs (1;3²⁷) at 36π;
   - least-g areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054} for M = 2..9 — all as printed;
   - for M = 2..5, exactly M−1 shared invariants, with c_M difference (−1)^M C a_{M−2};
   - (iv) with M = 2, X = 4: C = 180, ν = (10, −4), and (0;2¹⁰) vs (1;4⁴) share exactly c₁, c₂.
   - I also confirmed by exhaustive enumeration that 12π and 36π are the least areas for M = 3, 4 (a supplement S7 search claim).
5. **Table S1** (parsed from the supplement PDF; all 20 printed pairs, 40 signatures): every area equality, every exact shared count L = 2..7 and hyperbolicity check out. Hence Table 2's upper row (6, 8, 14, 18, 24, 40) and Example 3.21's |U\*|+|V\*| values (14, 18, 24, 40 equal-count; 16, 20, 26, 40 genus) check out too.
   - The pieces also check out:
     - [1,5,5] = [2,3,6] (degree 1, 3);
     - [1,13,17,23] = [3,9,21,21] (degree 1, 3, 5);
     - (A.314) (degree up to 9);
     - the two 7-sets (odd sums vanish to degree 5);
     - Letac's 9-sets (to degree 7).
   - So do Example 3.9 and Ex 3.21(i)–(ii), including s = 113/30 and the cancellation of the common order 6.
6. **Remark 3.5 / S1:**
   - An independent search of all 4-multisets with orders ≤ 84 returns exactly eight primitive witnesses, namely Chen's (A.685)–(A.692), which I also checked against the survey's text.
   - With orders ≤ 130 there are exactly 16 primitive witnesses (S1 says 16).
   - The six "non-pencil" witnesses printed in S1 have equal (R, P₁, P₃), different P₅, and gcd 1.
   - n = 5: no witness with orders ≤ 60 (the paper claims ≤ 120).
   - The count C(123,5) = 216,071,394 is right.
7. **Remark 3.22 / S1, S7(ii):**
   - The cubic and e₃ = (P₃(V) − e₁³)/(3 − 3e₁R) are correct.
   - The Möbius count of primitive 5-multisets in [1,220] is 4,325,115,770, as printed.
   - The {1,1,1,1,7} partner triple is correct.
   - The modular rejection argument is sound (p > max V; Gauss's lemma for a monic p-integral cubic).
   - My own search (V ≤ 40, eight primes above 40, exact factoring of survivors) finds no split cubic.
8. **Strata (Thm 5.5, Prop D.1, Tables S2, S3, Computation S2.1):**
   - x\*(p), S\*(p) for p = 2..14;
   - gaps 1/840, 1/2310, 1/10296 and −7/936, …, −17/4680;
   - the closed form of gap_p(3p+7) for p = 9..13;
   - zeros of the gap only at (p, S) = (2, 18), (4, 20) for S < 600;
   - the first-collision column of Table S2 (all 13 rows);
   - the 83 triads of Table S3;
   - the 38 collision-free sums, which I reproduce exactly on 18 ≤ S ≤ 600 (all listed ones are ≤ 557).
9. **Literature checks.**
   - Chen's survey [33]:
     - (A.685)–(A.692) are attributed to Chen's 2017 computer search;
     - Identity 9 with (3.27)–(3.28), m = 3;
     - (A.313) is Chen 2000 and (A.314)–(A.316) Wróblewski 2009;
     - A.1.6 contains [1,5,5] = [2,3,6];
     - §8.1 P1 reads as quoted.
   - Croot–Mao–Yip [48, §1]: they recall only quadratic bounds and that P(k,2) = k+1 is known only for k ≤ 9 and k = 11, as the paper says.
10. **Systoles** (floating point, word enumeration): ℓ(O(3,3,12)) ≈ 1.8626 (ℓ²/4 ≈ 0.867) and ℓ(O(2,8,8)) ≈ 2.257. The "ℓ²/4 ≈ 0.87" on pp. 3 and 36 is therefore the smaller systole, that of O(3,3,12) (see m8).

**Verdict on correctness.** Every proof that the main results of my part depend on is correct, and every number I recomputed agrees with the manuscript.

## 4. FATAL

None.

## 5. MAJOR

**M1. The headline quantity N(k) must be pinned to the literature's notation (pp. 1–2 abstract, 4, 29–31).**

The abstract, Theorem 1.2 and Prop 3.19 are stated in terms of N(k), defined (p. 4) as the least size of two distinct equal-size integer multisets with equal power sums of every exponent 1, …, k. The literature uses two different quantities:

- the "at least degree k" one: Wright's M(k), Croot–Mao–Yip's P(k,2);
- the "exactly degree k" one, with unequal (k+1)-th power sums: Wright's and Hua's N(k), Croot–Mao–Yip's W(k,2).

Here "N(k)" is the name often used for the second. The paper's own arguments need the first:

- monotonicity "N being nondecreasing" (pp. 30–31);
- the pigeonhole bound ½k(k+1)+1;
- Lemma A.1's translation of a "solution of degree 2L−3".

For the second, monotonicity is not obvious, and the pigeonhole bound does not apply. Croot–Mao–Yip stress that pigeonhole "does not readily yield" a bound on W(k,2); the quadratic bound for W(k,2) is Wooley's.

Statements such as "N(k) = o(k²) is Problem 3 of [4]" and "Wright [46] and Melzak [47] give slightly stronger quadratic bounds" are only meaningful once the quantity is fixed. The equivalence "f linear ⇔ N(k) = O(k)" is a statement about P(k,2) and is not known to be equivalent to the same statement for W(k,2).

Please do the following.
- State explicitly that N(k) is the "at least degree k" quantity, and give the alternative names (Wright's M(k), [48]'s P(k,2)).
- Check that the definition and Props 2–3 of [4, §2] are for this quantity, or adjust the citations.
- Say for which quantity each of Wright's and Melzak's bounds is proved (they apply to P(k,2) a fortiori if proved for W(k,2)).
- Cite Wooley's bound for W(k,2) as recalled in [48, §1].
- Keep "no o(k²) bound is known" as a statement about P(k,2).

I could not access [4] itself, so this is a request to check, not an allegation of a mis-citation.

I found no other issue that needs a substantive change in my part.

## 6. MINOR

**m1 (pp. 30–31, Prop 3.19).** The sandwich N(2L−3) ≤ N(2L−2) ≤ T(L) ≤ 4N(2L−3) implies N(2L−2) ≤ 4N(2L−3). This is weaker than the classical Prouhet/Tarry doubling N(k+1) ≤ 2N(k). One sentence saying so would show the reader that the factor-4 loss is harmless and that no new PTE information is claimed. It would also help to say whether 4 can be lowered. With two Prop A.2 shifts the size is ≤ 4n before pair removal; choosing c with ϱ(c) = 0 would give 2n, but needs a rational zero of ϱ.

**m2 (p. 28 and supplement S1, Remark 3.22).** State in the main text that the three-element side is uniquely determined because 1 − e₁(V)R(V) ≠ 0. By the AM–HM inequality, e₁R ≥ 25 for five positive entries. Without this, the reader may wonder about the degenerate case that S7(ii) handles by skipping primes.

**m3 (p. 31, size-10 4-configurations).** The search "A ∪ (−B), A, B five-element sets with e₁ = e₃ = 0 and, after scaling B, equal e₄ and e₅" covers a narrow ansatz and says little about T(4) = 10. Please say this explicitly, and record what T(4) = 10 amounts to:
- either an ideal solution of type (−1, 1, 3, 5) of size 5 + 5 (genus 0); Chen [33] gives the identity (3.33) but no numerical solution, as the supplement notes;
- or a genus-changing configuration of shape (4, 6).

The main text currently leaves this to the supplement.

**m4 (p. 23, Remark 3.5, and S1 p. 2).** "All but six of the 107 come from one family of pencil splittings." A "family" suggests a parametrisation, which is not given. Either describe the family (curve, parameters), or say "101 of the 107 admit a pencil splitting", which is what S1 actually shows.

**m5 (p. 8 vs pp. 5–6).** Section 1.2 says "Theorem 3.15 is Descartes' rule for polynomials with few nonzero coefficients [7, Part V]", while pp. 5–6 list "the Descartes bound on the imbalance (Theorem 3.15)" as new. Say "Theorem 3.15 is proved by Descartes' rule …".

**m6 (p. 26, after Thm 3.11).** "Such a C exists, since Σw_a = 0 gives s = Σν(a) + Cw₁" applies to (ii). In (iv) the sign of ν is reversed and s = Σν(a) − Cw₁ (nodes 1, …, M, X). This is harmless, but say "and likewise in (iv)".

**m7 (pp. 33–36, Section 4 novelty claims).** "What is new here is that constant (Proposition 4.2(a), Remark 2.6) and the reading of the cone timescale through the wave trace (Remark 4.3)." These claims need recalibrating:
- Lemma 2.4 is the standard packing count for closed geodesics (cf. Buser's counting lemma in *Geometry and Spectra of Compact Riemann Surfaces*, Ch. 6). Once it is available, the explicit constant is immediate.
- The kernel representation in Remark 4.3 is Garbin–Jorgenson's, as the authors acknowledge.
- By the authors' own numbers (p. 35), the constant overestimates by 10³–10¹⁰.

I suggest presenting Section 4 as a careful record of classical facts with explicit constants, not as new results.

**m8 (pp. 3 and 36).** "(π/12)² ≈ 0.07 while ℓ²/4 ≈ 0.87" uses ℓ = systole of O(3,3,12) ≈ 1.863. O(2,8,8) has a longer systole (≈ 2.257 in my floating-point enumeration). Please say which ℓ is meant: "the smaller systole, that of O(3,3,12)".

**m9 (p. 36, Remark 4.3).** "Its Taylor coefficients at u = 0, integrated against the Gaussian g_t, are the cone coefficients b_l(m)" is not literally true. g_t carries the factor e^{−t/4}, and each b_l is the finite combination (5) of these moments after expanding e^{−t/4}. Please rephrase, for example: "the b_l are finite combinations of these moments, (5)".

**m10 (p. 33, proof of Cor 4.1(a)).** "Any two hyperbolic structures of signature (0; p, q, r) are isotopic, hence isometric" mixes notions. Either say that Teich is a point (marked structures are equivalent), or invoke the uniqueness of the hyperbolic triangle with given angles.

**m11 (p. 34–35, proof of Prop 4.2(b)).** Say that the tail bound for lengths ≥ L′ is applied to each Hyp_i separately, with its own counting function n_{O_i}. Say also that the dropped boundary term is nonpositive for each.

**m12 (p. 30, proof of Prop 3.19).** The well-ordering of the set of areas is used to make A_min(L) a minimum. A one-line justification or a reference for "a finite sum of elements of well-ordered subsets of ℝ, with boundedly many terms, is well ordered" would help.

**m13 (p. 29, Thm 3.17).** "Whose smaller genus can be made equal to any prescribed g ≥ 2." The construction gives smaller genus g₀ ≤ 2, then adds handles. Say whether g₀ = 0 or 1 can also be prescribed. If not, the "≥ 2" is a limit of the method, and saying so would help.

**m14 (supplement S1, p. 2).** The recipe notation (±{a, b}, [x] = [y], "the shift by c of X against Y") is dense. One fully worked recipe would make the others checkable by hand: for example L = 4, genus, with the scaling τ and the cancelled pairs.

## 7. Presentation

- **P1 (p. 29).** The heading "Theorem 3.18 (Growth)" is orphaned at the foot of p. 29; its statement starts on p. 30.
- **P2 (p. 31).** The long sentence listing every source of the Lemma 3.20 pieces ("among them the ideal symmetric solutions listed by Borwein and Ingalls … according to that survey") is hard to parse. A short table or a pointer to Table S1 alone would do.
- **P3 (pp. 32–33).** Figure 3's caption, together with the long paragraph after it, explains the dots, diamonds, squares and two step curves in prose. A legend inside the figure would help.
- **P4.** Notation is heavy, but Table 1 helps. Please add T_g(L) and L-configuration to Table 1 with their defining places; T_g is there, the term "configuration" is not.
- **P5.** Figures 2 and 3 render correctly. In Fig. 2 I checked that the disc and ring positions match X\* and −X\* for both pairs, and that the multiplicities are stacked correctly.

## 8. Recommendation

**Minor revision** for the part I refereed, with high confidence (about 90%) in the correctness assessment.

I checked every proof in my part and recomputed every number I could reach, and found no mathematical error. The only item I rate MAJOR (M1) is a definitional and citation precision issue around the headline PTE quantity. It is easy to fix but must be fixed, because the abstract's main equivalence depends on it. The remaining items are calibration of novelty claims (m7, m5) and clarity.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Define N(k) explicitly as the "at least degree k" quantity, with Wright's M(k) / [48]'s P(k,2) as alternative names. Verify [4, §2] and Props 2–3 for this quantity. State for which quantity Wright's and Melzak's bounds hold. Cite Wooley's bound for W(k,2) via [48]. Keep the "open o(k²)" statement for P(k,2). |
| m1 | One sentence comparing N(2L−2) ≤ 4N(2L−3) with classical doubling N(k+1) ≤ 2N(k); optionally discuss the constant 4. |
| m2 | Add "1 − e₁R ≠ 0 since e₁R ≥ 25" to Remark 3.22. |
| m3 | Say that the size-10 search is a restricted ansatz; record the two shapes that T(4) = 10 would require, and the status of type (−1, 1, 3, 5) in [33]. |
| m4 | Describe the pencil family or reword as "admit a pencil splitting". |
| m5 | Reword p. 8: "proved by Descartes' rule". |
| m6 | Add "likewise in (iv), with s = Σν − Cw₁". |
| m7 | Cite the standard counting lemma (Buser); recast "what is new" in Section 4. |
| m8 | Specify that ℓ is the systole of O(3,3,12) on pp. 3 and 36. |
| m9 | Rephrase the Taylor-coefficient sentence in Remark 4.3. |
| m10 | Fix the wording in Cor 4.1(a). |
| m11 | State that the tail bound is applied per orbifold. |
| m12 | Add a one-line justification of the well-ordering. |
| m13 | Clarify whether smaller genus 0 or 1 can be prescribed in Thm 3.17. |
| m14 | Work one Table S1 recipe in full. |
| P1–P4 | Move the heading; shorten the p. 31 sentence; add a legend to Fig. 3; extend Table 1. |
