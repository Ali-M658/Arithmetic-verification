<!-- Round 8 A-c referee report: returned text saved verbatim; the reviewer could not write files -->

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

Referee A-c (approximation theory: moment problems, quadrature, Chebyshev systems, power sums and the Prouhet–Tarry–Escott problem).

The harness refused to let me write `REPORT.md`, so the full report is below.

Scope: Section 3 (pp. 20–32), Section 4 (pp. 32–36), Appendix A (p. 47), Appendix D (p. 52), and supplement Sections S1, S2 and S7 (the searches and strata parts). I treated the marked placeholders (author contributions, AI-use statement, DOIs, preprint identifiers) as known. I rendered pp. 20–31, 47, 50 and 52 at 80–110 dpi and checked every typographical or figure point below against the images. All code is in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/A-c-quadrature-moment-theorist/scratch/code/`.

## Summary

The paper reduces "how many heat invariants determine the signature of a closed hyperbolic 2-orbifold" to a problem about one signed multiset X* = U* ⊎ (−V*). The reduction rests on Lemma 2.11 (Uçar's triangular structure) and Lemma 3.6. The question is then how small X* can be when its reciprocal sum and its odd power sums up to 2L−3 all vanish.

The results in my part:
- **Theorem 3.7 (separation).** |X*| ≥ 2L+2, proved by Newton's identities.
- **Theorem 3.11 (bounded cone orders).** The exact area-free answer M+1 for cone orders at most M. The upper bound comes from sign changes; the matching constructions use Lagrange weights at the nodes a².
- **Theorem 3.15.** A Descartes-type bound on the genus imbalance.
- **Proposition 3.16 (doubling) and Lemma A.1 (pigeonhole).** Together they give the growth bound f(A) ≥ c√A.
- **Theorem 3.18 and Proposition 3.19.** They make every power-law growth question for f(A) equivalent to the matching power-law question for the least Prouhet–Tarry–Escott size N(k).
- **Section 4.** Locality (the heat invariants do not see the moduli), with an explicit constant (Proposition 4.2), a wave-trace reading of the cone timescale (Remark 4.3), and numerical illustrations.
- **Appendix D.** Classifies the coincidences of the extreme values of adjacent triad strata.

## Significance

**What is good.**
- The reduction to a "signed odd-moment problem with a reciprocal-sum constraint" is clean and stated honestly.
- Theorem 3.3 (the linear system for e1, …, en, with determinant ±∏(mi+mj)/∏mi, i.e. the Orlando form of a Hurwitz determinant) is a genuinely nice, checkable identity.
- The exact answer M+1 in Theorem 3.11 is sharp and has explicit witnesses.
- Prop 3.19 says precisely how far the extra structure (odd exponents plus the reciprocal sum) moves the least size away from N(k): by at most a factor 4.
- The paper is unusually careful about what is proved, what is computed, and what is heuristic.

**What is weaker.** The algebraic content of Section 3 is mostly classical machinery used in a new setting:
- Theorem 3.7 is the Borwein–Ingalls argument for N(k) ≥ k+1.
- Lemma 3.10 is the standard sign-change property of a Chebyshev (Haar) system: a signed measure orthogonal to all polynomials of degree < L has at least L sign changes.
- Theorem 3.15 is Descartes' rule for a polynomial whose odd coefficients are mostly zero.
- Theorem 1.2 is, as the authors say, a reformulation that does not touch the open problem.

The paper says much of this itself (p. 5, pp. 7–8), but see M2. The geometric payoff — that growth of the count is carried exactly by large cone orders, and the M+1 theorem — is of real interest to inverse spectral theory on orbifolds.

## Correctness, and what I recomputed

I checked every proof in my assignment line by line. Apart from M1 (a claim, not a proof) and the gaps under m1–m4, I found no error in any proof on which a main result depends. What I recomputed independently, in exact rational arithmetic unless stated:

1. **Cone polynomials.** I rebuilt pl from (4)–(5) and αk from Prop 2.8. Equation (8), α0..α4, deg pl = 2l+2, the leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)) and pl(1) = 0 all hold for l ≤ 5.
2. **Theorem 3.3.** I built the system (12) from the series tanh U and checked that the true e solves it. det M = (−1)^{n(n+1)/2} ∏_{i<j}(mi+mj)/∏mi holds for random rational m with n = 2..6 and with repeated orders ({2,2,5}, {3,3,3,7}). Orlando's formula (11) holds with the stated Hurwitz normalisation (a_{2j−i}). The signs are right.
3. **Theorem 3.4(3).** R, P1, P3, P5 are as printed for both pairs, including P3 = 1032/1782 and P5 = 25159618/21298618.
4. **Remark 3.5.** An exhaustive search of 4-multisets with orders ≤ 84 gives exactly 8 primitive witnesses (plus one imprimitive, the scaled minimal pair). These are the eight Chen pairs (A.685)–(A.692), and no key is shared by three multisets. The bound-440 and n = 5 searches I did not rerun.
5. **Theorem 3.11 and the text on p. 26.**
   - For M = 2..9 I computed the Lagrange weights, the least C, ν and s. The least-g areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054} are as printed.
   - For M ≤ 6 I checked from the actual heat coefficients that the pairs share exactly c1..c_{M−1}, with c_M difference (−1)^M C a_{M−2}.
   - The examples (1;3⁹)/(0;2¹⁶) (area 12π) and (0;2²⁸,4⁸)/(1;3²⁷) (area 36π) are correct.
   - For (iv): M = 2, X = 4 gives C = 180, ν = (10, −4), s = 2, and (0;2¹⁰)/(1;4⁴) share exactly c1, c2. So do the further cases (M, X) = (3,4), (3,5), (4,7) I tried; each shares exactly M.
   - The identity a·w_a = (−1)^{M−a} 2a³/((M−a)!(M+a)!) holds.
6. **Small pairs and the explicit tables.**
   - Example 3.9, Example 3.21(i)–(ii), (0;5,5,5)/(0;2,2,2,10), (2;)/(0;2⁸), (0;2⁵)/(1;2) and the minimal pair all have the stated areas and stated exact shared counts.
   - d3 = 25/12, d4 = −1775/24, d5 = 153025/48 (p. 35) are correct.
   - I parsed all 20 pairs written out in Table S1 (L = 2..7 genus, equal-count and cone-count rows, plus the first two Prouhet rows). For every one the areas are equal, the shared count is exactly the stated L, and |U*|+|V*| is as stated (16, 20, 26, 40 for the genus pairs; 14, 18, 24, 40 for the equal-count pairs).
   - Table 2's upper row (6, 8, 14, 18, 24, 40) is therefore correct.
7. **Appendix A.**
   - Pigeonhole count: n^{L−1} Q^{(L−1)²} vs Q^n/n!.
   - Prop A.2 (1)–(3) and the sign bookkeeping of λ = −ϱ(c′)/ϱ(c) against Lemma 3.20.
   - The constants in (b) and (c), including N(2L−3) ≤ 2L² from N(k) ≤ k(k+1)/2+1, and the small-A fallbacks.
   - All correct.
8. **Theorem 3.15 and Remark 3.22.** The Descartes count (at most (κ−2L)/2 nonzero odd coefficients, hence at most κ−2L odd-parity gaps) is correct. For {1,1,1,1,7} the partner cubic is z³ − 11z² + (1189/39)z − 287/39, with roots 0.26636, 4.28304, 6.45060, as stated.
9. **Section 5 strata, Appendix D, Table S2, Computation S2.1.**
   - The gap formula, x*(p) and φ′p are correct.
   - S*(p) is correct for p = 2..14, as are the values gap_p(S*+1) and gap_p(3p+7).
   - gap_p = 0 occurs only at (p, S) = (2, 18) and (4, 20), confirming Proposition D.1. The sign pattern of gap_p is monotone for p ≤ 39.
   - All 13 first collisions of Table S2 are correct.
   - There are 83 triads with 10 ≤ S ≤ 18 (Table S3).
   - Among 18 ≤ S ≤ 600 the collision-free sums are exactly the 38 listed; the list's last entry is 557, so nothing beyond 600 was claimed.
10. **Remark 4.3.** Numerically, to 30 digits, E_m(t) = ∫ g_t k_m for m = 2, 3, 8, 12 and t = 0.01, 0.3. The Fourier identity for cosh(ar)/cosh(πr) also checks. The poles of k_m nearest the real axis are at ±2πi/m.
11. **Section 4 numbers.** The closed-geodesic term of O(3,3,12) (ℓ = 1.8626, two orientations) is ≈ 4.0×10⁻¹³ at t = 0.0293 and ≈ 7.9×10⁻¹³ at t = 0.03. This matches p. 35 and S4.
12. **Figures 2, 3 and Table 2 (rendered).**
    - Fig. 2: the discs and rings for both pairs match X* and −X* exactly, including the padding 1 in (b).
    - Fig. 3: the Prouhet squares sit at s ≈ 2.4, 15, 63, 255, 1023, drawn at L+1, consistent with Table S1.

## FATAL

None.

## MAJOR

**M1. The headline claim "reading even c3 off values of the trace with a proved error needs t of order 10⁻¹¹" is an artefact of one crude scheme, not a property of the problem (Abstract p. 1; Introduction p. 3; Remark B.4 p. 50; the framing of Section 4, pp. 32–36).**

Lemma B.3 samples the trace at exactly n times and truncates (6) at K = n−1. The truncation error is then of order t¹ after inverting a Vandermonde matrix whose inverse is of order t⁻², which forces t ≈ 10⁻¹⁰.

Nothing in the paper's own tools needs K = n. Proposition B.2 gives the remainder bound (6) at every order. So the identical proof works with K ≥ n nodes and K unknowns c1..cK, with error

  ‖row_3(V⁻¹)‖·(η + B0 + Q_K t^K), where Q_K = max(½|α_K|, 3|b_{K−1}(12)|).

I computed this exactly for O(2,8,8) with nodes t, t/2, …, t/2^{K−1}, against the paper's own target δ_thm = 3.80×10⁻⁷ (`code/lemb3.py`). The largest admissible t and the corresponding tolerated noise η (half the budget) are:

| K | largest t | η tolerated |
|---|---|---|
| 3 (the paper's choice) | 3×10⁻¹⁰ | 7.5×10⁻¹⁸ |
| 4 | 2.6×10⁻⁶ | 1.3×10⁻¹⁴ |
| 5 | 7.0×10⁻⁵ | 1.1×10⁻¹³ |
| 6 | 4.1×10⁻⁴ | 2.7×10⁻¹³ |
| 8 | 3.5×10⁻³ | 4.9×10⁻¹³ |
| 10 | 1.3×10⁻² | 4.4×10⁻¹³ |

The closed-geodesic term B0 is negligible at these times: e^{3D} ≈ 2×10⁶ against e^{−ℓ0²/4t} ≈ e^{−364} at t = 3.5×10⁻³.

So, with the paper's own proved bounds, c3 is certified from trace values at t ~ 10⁻³–10⁻² with accuracy ~10⁻¹³. That is eight orders of magnitude later in time and six orders less accuracy than the abstract states. It is also the regime of the S4 computations (error budget ~3×10⁻¹¹ there, so certification is about two orders away, not eight).

The c3 row is the binding one in the paper's example. The c1 and c2 rows should be checked the same way.

The abstract's sentence, the "10⁻¹¹" in the introduction, and the rhetoric that heat-invariant counts "describe diffusion only in the limit t → 0" must be restated or recomputed. Optimising the nodes (e.g. Chebyshev-type nodes on [0, t] rather than geometric ones) would improve these numbers further. This is precisely a quadrature and extrapolation question, and the paper should not present the ill-conditioning of a three-point Vandermonde as intrinsic.

**M2. Positioning of the moment-side "new" results (pp. 5, 7–8, 24–28).** The paper lists as new the following, and each needs to be set against the classical theory explicitly:
- **Lemma 3.10 (sign changes).** The sign-change property of the Chebyshev system {1, y, …, y^{L−1}}. See Karlin–Studden, *Tchebycheff Systems* (1966), Ch. I–II, or Krein–Nudelman. The paper cites only Laurens (2023) for it.
- **The witnesses of Theorem 3.11(ii) and (iv).** The measure Σ w_a δ_{a²} is the divided-difference functional f ↦ f[y1, …, yM] at the nodes ya = a². Its annihilation of polynomials of degree < M−1, and the value of the top coefficient, are the standard properties of divided differences (and of Gauss–Lobatto-type extremal measures). Saying so shortens the proof and makes it clear that the novelty is the use, not the mechanism.
- **Theorem 3.15.** Descartes' rule for lacunary polynomials (Pólya–Szegő, Vol. II, Part V, §1). Cite it.
- **Theorem 3.7.** Already credited to the N(k) ≥ k+1 argument; fine.

With these attributions the genuinely new algebraic items are Theorem 3.3's closed form, the exact M+1 statement, Prop 3.16/Lemma 3.20, and Prop 3.19's factor-4 comparison. These are worth publishing, but the "what is new" paragraphs (p. 5, p. 8) should say exactly this.

**M3. Proposition 4.2 and the "new constant" (pp. 33–35).** The claimed novelty of Section 4 is "that constant" (Prop 4.2(a), Remark 2.6) plus the wave-trace reading (Remark 4.3).
- By the authors' own computations (p. 35, S6) the bound of 4.2(a) exceeds the actual difference by 4×10⁶–10¹⁰ with the proved diameter bound, and by 4×10⁵–2×10⁶ with the companion's count.
- Remark 4.3's formula is Garbin–Jorgenson's [37, Thm 2.5].
- The growth claim |bl(m)| ~ C_m l^{−1/2} l! (m/π)^{2l}, on which the "cone timescale" (π/m)² rests, is labelled heuristic. It is in fact elementary to prove. By Lemma 2.7, Φ_m is meromorphic with simple poles at ±π/m and its next singularities at ±2π/m. Cauchy's estimate on a circle of radius between these gives φ_k(m) = A_m (m/π)^{2k}(1 + O((1/2+ε)^{2k})) rigorously, and the k = l dominance in (5) follows from the explicit weights.

I ask the authors to prove it, since Section 4's "two timescales" thesis depends on it. Alternatively, they should drop "new" for this section and present it as an illustrated account of classical locality. As it stands, Section 4 adds little that is both proved and new.

## MINOR

- **m1 (p. 30, proof of Prop 3.19).** "A sum of boundedly many elements of well-ordered sets is well ordered" is applied to the set of all areas, where the number of summands is unbounded. The conclusion is true because area ≤ A bounds n and g (n + 4g ≤ A/π + 4, Cor 3.8). Say so; otherwise the argument as written is incomplete.
- **m2 (p. 47, Prop A.2(2) and the proof of Thm 3.18(c)).** Choosing a rational c with ι(Z(c)) ≠ 0 ≠ ϱ(c) needs one more sentence: the interval is open, and ϱ is a nonzero rational function with finitely many zeros and poles there.
- **m3 (p. 32, Remark 3.22; S7(ii)).** The soundness of the modular rejection test is asserted ("by the argument of Remark 3.22"), but the remark does not contain the argument. State it: q_V is monic with p-integral coefficients when p > max V and p ∤ 3(1 − e1 R). By Gauss's lemma its rational roots are p-integral, so the reduction mod p splits. Also say that the denominator of e3 is handled by the skip condition.
- **m4 (p. 29, Thm 3.18(d)).** "Likewise for fg and fn" applies only to the lower-bound equivalence; Theorem 1.2(ii)'s second half (O(A^α) ⟺ N(k) ≥ c k^{1/α}) is not claimed for them. Also note that for α = 1 that second half is vacuous, since both sides always hold.
- **m5 (p. 27, Lemma 3.14(a)).** The proof refers to "the proof of Theorem 3.7 … except at its last step". Write the three lines out. The step e_{κ−1} = e_κ Σ 1/z needs κ ≤ 2L, which should be visible.
- **m6 (p. 27, Thm 3.15).** "(paddings by 1 included)" is ambiguous: it should mean that U*, V* may contain entries 1. Remark 3.22 then needs the five-element side to be allowed to contain 1s, which the search does allow; say so in the remark.
- **m7 (p. 26, Cor 3.12(a)).** The surface case uses that the padding then lies on the surface side. This holds because d = R(m′) > 0 when O′ has cone points; one clause would settle it.
- **m8 (p. 33, Cor 4.1(b)).** "Uncountably many isometry classes" uses only that Out(Γ) is countable. The phrase "differ by an automorphism of Γ and a conjugation in PGL(2,R)" should cite a source (e.g. Thurston Ch. 13, or Farb–Margalit for the orbifold mapping class group).
- **m9 (p. 34, Prop 4.2(b)).** The tail estimate "by the argument of Lemma 2.5 with L′ for ℓ" also needs the range t ≤ L′²/(2(1+L′)). This is harmless as t ↓ 0, but state it.
- **m10 (S1, p. 2; S7).** The n = 4 search to 440 and the n = 5 search to 120 are not rerun by the run-all script; only their outputs are rechecked. For a claim stated in the main text (Remark 3.5), give at least the counts at a smaller bound that the script does rerun. My count at bound 84 (8 primitive, 9 total) could serve.

## Presentation

- **P1 (notation clashes).** T denotes the tanh series (Thm 3.3), the least configuration size T(L), and a cylinder length (Prop 2.15). The letter a is both a node and, with a subscript, a leading coefficient (Thm 3.11, which itself apologises for this). ι and ϱ appear only in Section 3.4; add them to Table 1. Rename.
- **P2 (Abstract).** "two first fail on" is awkward ("two first fail for"). The abstract is also overloaded; the 10⁻¹¹ sentence should go (M1).
- **P3 (Table 2).** Say in the caption which row of Table S1 attains each upper bound: equal-count for L = 4, 5, 6; both kinds for L = 7.
- **P4 (Fig. 3).** The caption should repeat that diamonds and squares are lower bounds drawn at L+1, and that the dashed curve is valid only from s = 4.
- **P5 (pp. 27–31).** Section 3.4 alternates between statement and literature commentary (pp. 28, 30). Moving the literature on ideal solutions into one paragraph would make the chain Lemma 3.14 → Prop 3.19 → Thm 3.18(d) easier to follow.

## Recommendation

**Major revision.** My confidence is high for the parts I was assigned.

All proofs of main results in Section 3, Appendix A and Appendix D are correct, and every number I recomputed agrees. However, a claim in the abstract and introduction (M1) is contradicted by the paper's own bounds once a standard extrapolation with more nodes is used. In addition, the novelty statements for the moment-side mechanisms and for Section 4 need to be corrected against the classical literature (M2, M3).

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Generalise Lemma B.3 to K ≥ n nodes (same proof), recompute Remark B.4, and replace the "10⁻¹¹" claims in the Abstract and p. 3 (and the Section 4 framing) with the recomputed scale, or state them explicitly as properties of the three-point scheme. |
| M2 | Cite Karlin–Studden (Chebyshev systems), divided differences, and Pólya–Szegő (Descartes for lacunary polynomials). Rewrite the "what is new" paragraphs on pp. 5 and 8 accordingly. |
| M3 | Prove the growth of bl(m) by a Cauchy estimate on Φ_m, or remove "new" from Section 4's claims and label the cone timescale heuristic throughout. |
| m1–m10 | The one-line additions indicated. |
| P1–P5 | Editorial. |
