# Referee report — Number theorist

**Manuscript:** "How much of a hyperbolic orbifold does heat hear?" (56 pp.), submitted to *The Journal of Geometric Analysis*.
**Focus of this report:** the triangular-pillow threshold (§5), the curve C_Λ and the isolation of the minimal pair (§5.4, §8.1), the counting bounds (§8.2, Appendix A), classes of every size (§8.3), the growth conjecture (§8.4, Conjecture 8.10), and the use of Bremner–Guy–Nowakowski [5] and Schinzel [37]. I read the whole paper and comment on the rest only where it touches these topics.

**How I checked.** I recomputed everything I could on my own code in a scratch folder:
- an exhaustive C++ enumeration of all hyperbolic triads up to S = 6000, with exact rational grouping;
- exact chord-and-tangent arithmetic on C_Λ;
- my own complete 2-isogeny descents, with p-adic local solubility tests;
- point counts mod p for torsion.

PARI/GP and Sage are not installed, LMFDB was unreachable from this machine, and I could not get the full text of [5] or [37]. Where the paper relies on [5], I checked the statements mathematically. For [37], I used the account of Schinzel's result in Zhang–Cai, *Math. Comp.* 82 (2013) 617–623.

---

## 1. Summary of the paper

The paper studies the small-t heat invariants c_j of closed orientable hyperbolic 2-orbifolds. Its results fall into four groups:
- **Signature.** The first ⌊Area/π⌋+4 invariants determine the signature, and no fixed number works for all orbifolds (§3). The proof uses a moment problem for signed multisets of cone orders, plus Prouhet–Thue–Morse constructions.
- **Shape.** The invariants depend only on the signature, and the moduli enter the heat trace only at order t^{-1/2}e^{-ℓ²/4t} (§4).
- **Triangle orbifolds O(p,q,r).** These are rigid, and c₁, c₂ are equivalent to the pair (S₁, R) = (p+q+r, 1/p+1/q+1/r). The paper proves:
  - c₁ and c₂ determine O(p,q,r) whenever p+q+r ≤ 17;
  - the first failure is the pair (2,8,8), (3,3,12) at sum 18;
  - c₃ always suffices.

  The threshold proof splits the triads of a fixed sum into strata by least order p. It shows R is monotone within a stratum and locates the first overlap S*(p) of adjacent strata (Theorem 5.11).
- **Stability and numerics.** Stability estimates (§6) and numerical spectra (§7).

**The arithmetic part (§5.4, §8).** Two triads with the same sum share R exactly when they share Λ = S₁R. A two-coefficient degeneracy is therefore a set of positive rational points on the plane cubic
C_Λ : (X+Y+Z)(XY+YZ+ZX) = ΛXYZ,
the curve of Bremner–Guy–Nowakowski, here with rational Λ. The paper shows:
- C_{27/2} has rank 0 and torsion ℤ/2×ℤ/6, so the minimal pair and its multiples are "isolated": no third orbifold ever joins them (Theorem 5.16).
- Reciprocation is translation by a 2-torsion point. This gives a "dual family" of degeneracies (Proposition 8.3).
- An isosceles subfamily gives N(X) ≥ (c_iso + o(1)) X log X (Theorem 8.7). A two-parameter subfamily gives X(log X)² (Theorem 8.8, Appendix A).
- A point of infinite order on C_{155/12}, together with rescaling to a common sum, gives classes of every size (Theorem 8.9, "Schinzel's method").
- An exhaustive enumeration to S = 4800 (6000 for some counts) supports Conjecture 8.10: N(X) = X^{1+o(1)}.

## 2. Significance and novelty

**Correctness.** The arithmetic content is correct. Every number I could check reproduced exactly (Section 3 below), and the rank-0 proof for C_{27/2} survives an independent descent.

**The triangle threshold is mathematically light.** A collision must have equal sums, and each sum carries finitely many triads. So "two invariants suffice for S ≤ 17, first failure at 18" is a finite check of the 83 triads in Table B1. The authors themselves present Table B1 as an independent proof. Theorem 5.11 (first overlap of strata p and p+1 for every p) is a pleasant exact computation. But by the authors' own Table 1 and Proposition 5.15, overlap is not what produces collisions: the first collisions sit 8–145 beyond S*(p) "with no regularity in p". The stratum machinery therefore explains the number 18 but nothing beyond it. Its relevance to the heat question is limited to that one number.

**Section 8 is essentially an independent Diophantine study** of the threefold of pairs of triads with equal sum and equal reciprocal sum. Its results are:
- (a) elementary lower bounds X log X and X(log X)² from explicit rational families;
- (b) a Schinzel-type existence theorem for large classes;
- (c) an empirical growth conjecture.

Result (b) is not new in method, contrary to what the text claims (M1). The natural geometric context is missing: the pairs are rational points on the fibre product E ×_{ℙ¹} E of Beauville's rational elliptic surface with itself. To my knowledge such self-fibre products are Schoen-type Calabi–Yau threefolds. That context is exactly what governs counting questions such as Conjecture 8.10 (see M2).

**Prior literature I checked:**
- **Bremner–Guy–Nowakowski, *Math. Comp.* 61 (1993) 117–130 [5].** The model η² = s(s² + (Λ²−6Λ−3)s + 16Λ) agrees with the standard BGN curve at Λ = n. I could not reach the full text, so I verified the two statements the paper takes from [5] directly:
  - "Odd multiples of a point on the egg are the positive points." This holds because E(ℝ) ≅ S¹ × ℤ/2, and the egg is exactly the set of positive points. That second fact follows from compactness of the positive solution set and smoothness.
  - "Torsion is the cyclic group of base points for every integer Λ ≠ 10." Full 2-torsion needs (Λ−1)(Λ−9) to be a square, which for integers gives only Λ = 10. A point of order 4 is impossible. My point counts give a gcd bound of 12 only at Λ = 10 and at perfect squares; for the squares the order-4 criterion rules out extra torsion.
- **Schinzel, *Serdica Math. J.* 22 (1996) 587–588 [37].** As reported by Zhang–Cai (*Math. Comp.* 82 (2013) 617–623, Introduction and §2), Schinzel proved that "for every k, there exist infinitely many primitive sets of k triples of positive integers with the same sum and the same product". He did this by showing that x₁+x₂+x₃ = x₁x₂x₃ = 6 has infinitely many positive rational solutions, then clearing denominators. The paper's description of Schinzel's method is accurate. Its claim that "what is new is the normalization by rescaling to a common sum" is not (M1).
- **Not cited and relevant:**
  - Zhang–Cai (2013), the n-tuple generalisation of Schinzel;
  - J. B. Kelly, *Partitions with equal products*, Proc. AMS 15 (1964) 987–990;
  - Guy, *Unsolved Problems in Number Theory*, D16 (triples with the same sum and same product);
  - Bremner–Guy, *Two more representation problems*, Proc. Edinburgh Math. Soc. (1997);
  - Brueggeman, *Integers representable by (x+y+z)³/xyz*, IJMMS 21 (1998);
  - Kozuma (2010), on the BGN problem;
  - Bremner–Macleod, *An unusual cubic representation problem*, Ann. Math. Inform. 43;
  - Sadek–El-Sissi, *Partitions with equal products and elliptic curves*, Osaka J. Math. 52 (2015);
  - the four-variable BGN analogue (arXiv:1608.03382 / IJNT 2018);
  - for the geometry, Schoen, *On fiber products of rational elliptic surfaces with section*, Math. Z. 197 (1988), and the standard identification of the pencil (x+y)(y+z)(z+x)+txyz as Beauville's Γ₁(6) surface with fibres I₆ I₃ I₂ I₁ (e.g. Miranda–Persson).

## 3. Correctness, claim by claim (my area)

| Claim (location) | What I did | Result |
|---|---|---|
| Table B1 (p. 52): 83 triads with 10 ≤ S ≤ 18; R distinct within each sum except (2,8,8)/(3,3,12) | Enumeration | **Verified** (83 triads; the first collision is at 18) |
| §5.2 nonemptiness of strata; Lemma 5.6; Lemma 5.7 | Re-derived | **Verified** |
| Theorem 5.11 (S*(p) = 18, 19, 3p+8 for 4≤p≤8, 3p+7 for p≥9; overlap iff S ≥ S*(p)) | Brute force, exact rationals, p = 2..60, S up to 3p+200; checked monotonicity after the first overlap | **Verified**, no mismatch |
| Constants in the proof of Thm 5.11: x*(p) values; gaps 1/840, 1/2310, 1/10296; −7/936, −1/72, −19/3960, −1/180, −76/15015, −1/231, −17/4680; gap_p(3p+7) formula | Exact computation | **Verified** |
| Lemma 5.10 numbers (60/224, 7/10) | Checked | **Verified** |
| Theorem 5.12 (only one collision at S = 18; R⁺_{18,4} = 3/5) | Enumeration and exact computation | **Verified** |
| Theorem 5.13: exactly 38 collision-free sums in [18, 4800], largest 557 | Full enumeration | **Verified**: 19 21 22 23 24 25 27 28 29 30 33 41 44 46 47 48 49 50 51 59 65 67 81 99 115 119 123 125 173 199 203 223 235 243 251 307 329 557. I also find **no** collision-free sum in (4800, 6000]. |
| Theorem 5.14, Corollaries 5.4–5.5, Theorem 5.3 (P₃ = 1032 vs 1782) | Checked | **Verified** |
| Prop. 5.15 (endpoint equality only for p ∈ {2,4}; for p ≥ 9 no collision at 3p+7) | Integrality argument checked; no collision of strata p, p+1 at 3p+7 for 9 ≤ p ≤ 399 | **Verified** |
| Table 1 (p. 34): x*(p), S*(p), first collision, gap, colliding pairs, p = 2..14 | Enumeration to 600 | **Verified**, all 13 rows |
| p. 33: first non-adjacent collision (5,15,15)/(7,7,21) at 35; 2793 of 3067 pairs join strata differing by ≥ 2 | Enumeration | **Verified** |
| Theorem 5.16: C_{27/2} ≅ E: y² = x³+393x²+3456x | Checked the substitution from the general s-model (x = 4s, y = 8η); (1:4:4) ↦ s = −6, η = 45 ↦ (−24, 360) | **Verified** |
| Theorem 5.16: rank 0 | Own 2-isogeny descent via T = (0,0): S^φ = {±1, ±6}, S^φ′ = {1} (E′: y² = x³−786x²+140625x); rank ≤ 2+0−2 = 0. The torsion images fill S^φ. | **Verified**, unconditionally |
| Theorem 5.16: torsion ℤ/2×ℤ/6 | x(x+9)(x+384) splits; #E(F_p) = 12, 12, 12 at p = 7, 11, 13, so gcd = 12; 12 rational points exhibited | **Verified** |
| Theorem 5.16: the 12 points, positive ones = permutations of (1:4:4), (1:1:4); (1:4:4) has order 6 | Exact group law with O = (1:−1:0) | **Verified** |
| Theorem 5.16, "Consequently …" (isolation of every multiple (2k,8k,8k), (3k,3k,12k)) | Logic checked | **Verified** |
| Prop. 8.1 (primitivity of the rescaled class) | Proof checked | **Verified** |
| Prop. 8.2 discriminant 2¹²Λ²(Λ−9)(Λ−1)³; fibre types I₂ at Λ=0, I₃ at Λ=1, I₁ at Λ=9, I₆ at ∞ | Discriminant identity recomputed; fibre types agree with the I₆I₃I₂I₁ configuration in the literature | **Verified**. The group label "Γ⁰₀(6)" could not be checked (m3). |
| Prop. 8.2 torsion orders 6, 6, 2, 1, 3, 3 of the base points | Exact group law on C_Λ for Λ = 27/2, 155/12, 68/5, 7/3 | **Verified** |
| Prop. 8.2 positive points lie on the egg | Argument checked | **Verified**, though the written proof is terse (m4) |
| Prop. 8.3 (P + T₂ = ι(P); dual pair) | Checked algebraically and numerically | **Verified** |
| Remark 8.4 (isosceles points have order 6; 2(1:4:4) = (1:0:−1)) | Computed | **Verified** |
| p. 46–47: 1753 primitive pairs with S ≤ 600, of which 423 are dual | Enumeration | **Verified** |
| p. 47: the other 1330 have P′ ± P of order > 12 | Not run | **Could not check** (immaterial) |
| p. 46: "torsion = base group for every integer Λ ≠ 10 [5,§4]" | Proved directly for integer Λ (Section 2) | **Verified**. For rational Λ the torsion is larger on an infinite family (m5). |
| Theorem 8.7: c_iso = 3 log 2/(2π²) = 0.10535; area Y log 2/3; densities 6/π², 1/4; class argument | Derivation re-done | **Verified**. 506 primitive pairs with S ≤ 4800, against c_iso·4800 = 505.66. |
| Theorem 8.8 / Appendix A, constant 3/(128π⁴) | Re-derived every step: U, V box, Q ≤ y, coprime count, Σφ(n)/(2n²) ~ (3/π²) log M, c_A = 3/(32π⁴), multiplicity ≤ 6, error O(M³√y log y), partial summation | **Verified** |
| Theorem 8.9 (P = (4:9:18) on C_{155/12}; nP ≠ O for n ≤ 12) | Exact arithmetic; Mazur bound; odd multiples on the egg | **Verified**. 3P = (162833463 : 723926268 : 287876366), a coordinate permutation of the printed value (m6). |
| p. 49: C_{155/12} has rank exactly 2 | Model y² = x³+12433x²+4285440x; S^φ = {1, 3, 155, 465, −10, −30, −62, −186}, S^φ′ = {1, 6721}; points found realise every class | **Verified**, rank 2 |
| Table 4 members, S, Λ | Common sums and R checked (R = 1/10, 1/30, 1/120, 1/420) | **Verified** |
| Table 4 ranks 2, 2, 3, 3 | Own descents (Λ = 68/5: S^φ order 4, S^φ′ order 4; Λ = 1849/120: 8 and 4; Λ = 230/21: 16 and 2), with points realising the Selmer groups | **Verified** |
| Table 4: first class of each size; no class of size 7 | Full enumeration | **Verified**; also no size 7 up to **6000** |
| Table 5 (all columns) and the triad total 3,067,197,199 | Full enumeration to 6000 | **Verified exactly**: pairs, classes, primitive classes, largest class, local exponents. I also obtain 62,401 primitive classes at S = 6000, missing from the table. |
| p. 49: 507 of 582 sums carry a primitive class; N/S² values; dual share 33% (S ≤ 200), 16.5% (S ≤ 4800) | Enumeration | **Verified** (32.9%, 16.49%) |
| Fit q = 4.5 ± 0.5 (p. 49, Fig. 8b) | Not re-fitted; independent windows below | **Consistent** |
| Conjecture 8.10 | Tested on new ranges (below) | **No contradiction, weak support** (M2) |
| Theorem C(3) and the n = 4 claim "11 witness classes ≤ 90, 9 primitive" (p. 14) | Exact recomputation | **Verified**. The n = 5 search (orders ≤ 120) was not repeated. |

**Independent test of Conjecture 8.10.** The paper's data stop at 6000. I computed the mean per-sum pair count N(s) over windows of 48 consecutive sums starting at S₀:

| S₀ | 1200 | 2400 | 4800 | 9600 | 19200 |
|---|---|---|---|---|---|
| mean N(s) | 15.10 | 23.58 | 34.52 | 47.96 | 65.17 |
| log₂ of ratio to the previous window | – | 0.64 | 0.55 | 0.48 | 0.44 |

Under the authors' fit const·(log s)^{4.5}, the predicted doubling ratios are 1.52, 1.47, 1.42 and 1.39. The observed ratios are 1.56, 1.46, 1.39 and 1.36. So the polylog fit continues to hold, perhaps with a slightly smaller q, and the per-sum exponent keeps falling (0.44 at about 2×10⁴). That is consistent with N(X) = X^{1+o(1)}, but it does not exclude a limiting exponent near 1.3–1.4 (see M2).

## 4. MAJOR issues

**M1. Overstated novelty of Theorem 8.9, and missing literature.**

*Location:* p. 48 line −2 to p. 49 line 2, which says that "The method is Schinzel's … what is new is the normalization by rescaling to a common sum, which works because Λ is scale-invariant". Also §1 and §8.1, which cite only [5] for the curve.

*Problem:* Schinzel's argument is exactly "infinitely many positive rational points on a fixed cubic, then clear denominators to put k of them at a common integer sum/product". This is how Zhang–Cai (*Math. Comp.* 82 (2013), §1–2) describe it. Rescaling to a common sum is the same step, because the defining equations are homogeneous in the same way. So Theorem 8.9 is a direct transcription of Schinzel's theorem to the BGN curve, not a new method.

The paper also omits much of the directly relevant literature: Kelly (1964), Zhang–Cai (2013), Guy D16, Bremner–Guy (1997), Brueggeman, Kozuma, Bremner–Macleod, Sadek–El-Sissi, and the four-variable BGN analogue. It also omits the geometric literature on Beauville's surface and its fibre products (Schoen 1988).

*To resolve:*
- Remove the novelty claim and state that Theorem 8.9 is Schinzel's argument applied to C_{155/12}.
- Cite the works above and place §8 in that literature.
- Say explicitly that the BGN problem concerns integer Λ and that the paper needs the whole rational family Λ ∈ ℚ, i.e. the Γ₁(6) rational elliptic surface.

**M2. Conjecture 8.10 has no upper bound, an invalid heuristic, and data that cannot settle the exponent.**

*Location:* p. 48, "every family found is a rational surface whose points have height comparable to S; for such families one expects counts of order X(log X)^{O(1)}"; p. 49, Conjecture 8.10 and the paragraph after it ("no heuristic currently accounts for it").

*Problems:*
- **(a) No upper bound.** No upper bound of any kind is proved, so the conjecture floats free. An easy bound exists. Fix the least orders p ≠ p′ (O(S²) choices) and put A = S−p, A′ = S−p′, B = qr, B′ = q′r′. Equality of R becomes
  ((p−p′)B − pp′A)·((p−p′)B′ + pp′A′) = −p²p′²AA′,
  so there are at most S^{o(1)} pairs (B, B′). Hence N(S) ≪ S^{2+ε} and 𝒩(X) ≪ X^{3+ε}. The paper should at least state X(log X)² ≪ 𝒩(X) ≪ X^{3+ε}. It should also try for something better, for example by counting points on the curves C_Λ with height bounds.
- **(b) The heuristic is incorrect as stated.**
  - Remark 8.5 excludes only *linear* families.
  - A family whose entries are quadratic forms in three variables (a rational surface parametrised by quadrics) would give about X^{3/2} primitive pairs. The isosceles family already shows that quadratic families exist; it is quadratic in two variables and is a rational *curve*, not a surface, contrary to "every family found is a rational surface".
  - So the conjecture is essentially the assertion that the pair variety contains no low-degree rational surfaces beyond the cubic-type ones. That needs at least a computational search, or an argument.
- **(c) The variety is never identified.** Primitive degeneracy pairs are the positive rational points of the self-fibre product of the Γ₁(6) Beauville surface, a Calabi–Yau threefold of Schoen type to my knowledge. Point counts on such threefolds are known to be governed by accumulating subvarieties: rational surfaces, and elliptic fibres of positive rank. This is the natural framework for a heuristic, and the paper says none exists.
- **(d) The data cannot distinguish the hypotheses.** The cumulative local exponent is still 1.58 at 6000. My windows put the per-sum exponent at 0.44 near 2×10⁴, i.e. a cumulative exponent of about 1.44, still falling. This is consistent with 1+o(1), but equally with a limit near 1.3–1.4.

*To resolve:*
- Prove a nontrivial upper bound (at least the X^{3+ε} above).
- Correct the heuristic remark: the isosceles family is a curve, and quadratic surfaces would give X^{3/2}.
- Either search systematically for low-degree rational subvarieties of the pair threefold, or downgrade Conjecture 8.10 to a question with an honest statement of the evidence.
- Add the fibre-product/Calabi–Yau framing.

**M3. The arithmetic sections are weakly tied to the paper's question and too heavy for what is used.**

*Location:* §5.3 (Theorem 5.11, Proposition 5.15, Table 1, Figure 7) and all of §8.

*Problem:*
- What the heat problem needs from the arithmetic is: (i) no collision at S ≤ 17, (ii) the collision at 18 and its uniqueness, and (iii) the fact that some triangle orbifolds require c₃.
- Items (i) and (ii) are a finite check of 83 triads (Table B1), and the paper itself treats Table B1 as an independent proof.
- Theorem 5.11 and Proposition 5.15 give exact information on interval overlaps. The authors concede that overlap does not predict collisions ("no regularity in p").
- §8 (≈ 6 pages plus Appendix A) concerns the distribution of rational points on the BGN family. Its results are either elementary lower bounds, Schinzel's argument (M1), or empirical. Apart from Theorem 5.16, none of it bears on how many heat invariants are needed.
- For a geometric-analysis readership, the arithmetic as presented dilutes the paper. For an arithmetic readership it is not deep enough to stand on its own.

*To resolve:*
- Condense §5.3 to what Theorem 5.13 needs (Table B1 suffices for the threshold). Theorem 5.11 can be kept as a short remark if desired.
- Keep Theorem 5.16, where the rank-0 statement does real work (isolation of the minimal pair, Theorem 1.3(iv)).
- Move the counting material (§8.2–8.4, Appendix A) to a separate note in an arithmetic or experimental venue, or justify explicitly why it belongs here.

## 5. MINOR issues

- **m1 (Theorem 5.16, p. 34; Appendix C).** The rank-0 proof is "PARI returns r₁ = r₂ = 0", plus an unwritten "independent 2-isogeny descent". It is correct: I reproduced S^φ = {±1, ±6} and S^φ′ = {1}. Since it is the key arithmetic input, write the descent out: E: y² = x(x+9)(x+384), E′: y² = x³−786x²+140625x. List the images of the torsion and the local obstructions that kill the other classes (for S^φ′, the classes d | 140625 other than 1). Likewise, state torsion via #E(F₇) = #E(F₁₁) = 12. Then the theorem no longer depends on software.
- **m2 (Theorem 5.13, p. 32).** A theorem statement contains "namely 19, 21–25, 27–30, 33, and so on, the largest being 557". List all 38 values (given in Section 3 above, all verified), or move the computational part to a labelled computational proposition with the method stated.
- **m3 (Prop. 8.2, p. 45).** "the row Γ⁰₀(6) of Beauville's table". The literature usually identifies this pencil with Γ₁(6). Please check the notation against [35] and add a secondary reference (e.g. Miranda–Persson). The proof's "all checked symbolically" should display the explicit birational map C_Λ → E. One instance as a check: (1:4:4) ↦ (s, η) = (−6, 45) at Λ = 27/2.
- **m4 (Prop. 8.2 proof, p. 46).** The step "the positive points form a closed component" needs one more sentence: compactness of the positive locus for fixed Λ (Λ → ∞ at the triangle's boundary), smoothness, and the fact that a cubic has at most one oval. Similarly, the "odd multiples" fact used in Theorem 8.9 should be justified by E(ℝ) ≅ S¹×ℤ/2 rather than only cited from [5, p. 119].
- **m5 (p. 46, "as it is for every integer Λ ≠ 10").** This is true for integer Λ (I checked it), but the paper works with rational Λ. Full 2-torsion occurs exactly when (Λ−1)(Λ−9) is a rational square, which is an infinite family containing Λ = 27/2. Say so; it also explains why the minimal pair's curve has torsion 12.
- **m6 (p. 49).** With O = (1:−1:0) and P = (4:9:18), I get 3P = (162833463 : 723926268 : 287876366); the printed point permutes the last two coordinates. Since points of C_Λ are ordered projective points, either print the correct order or say "up to permutation".
- **m7 (Remark 8.4 and p. 34).** "most curves C_Λ carrying collisions have positive rank" is unquantified. Give the count over the classes with S ≤ 600 (or 4800), or drop it.
- **m8 (Theorem 8.7 proof, p. 48).** "the standard boundary estimate for primitive lattice points in a region bounded by a hyperbola and two rays" needs a reference or a two-line Möbius-inversion argument giving O(√y log y).
- **m9 (p. 46–47, Mazur paragraph).** I did not re-check the 1330 non-dual pairs. Note that P′ ∓ P must be tested against the full torsion group of each C_Λ, which may exceed the base points (m5). The order-≤12 test covers this, but say so explicitly.
- **m10 (Table 5, p. 50).** The primitive-class column stops at 4800 ("–" at 6000). The value is cheap to obtain (I get 62,401); fill it in.
- **m11 (§8.4).** The fit "q = 4.5 ± 0.5" with "block-bootstrap standard deviation" is unreproducible from the text. Give the window, the smoothing of the highly arithmetic per-sum counts N(s), and the fitted constant. Also show the primitive-pair fit (q ≈ 3.5) and how it follows from the scaling identity 𝒩(X) = Σ_D #{k : kS_D ≤ X}.
- **m12 (Theorem 1.3(iv) and Theorem 5.16).** A natural strengthening is to say which other collision classes lie on rank-0 curves and are therefore finite and "isolated". Even a census for S ≤ 600 would show whether the minimal pair is exceptional or typical.

## 6. Presentation issues

- **p1.** N(S) (per-sum) and 𝒩(X) (cumulative) are typographically close, and Table 5 and Fig. 8(b) write 𝒩(S) with S as the upper limit. Use distinct letters, e.g. n(S) and N(X).
- **p2.** Fig. 7 (p. 33): on log–log axes with seven grey levels, the strata are hard to tell apart in print. Label p on the curves.
- **p3.** p. 33, "This curve is the one studied by Bremner, Guy and Nowakowski [5] for integer Λ" → add that the paper uses all rational Λ, which is a different (surface) object.
- **p4.** Appendix C quotes raw PARI output ([0,0,0,[]], [12,[6,2],…]). Once the descent is written out (m1), this can go.
- **p5.** Theorem 5.11's "Equivalently, S*(p) is the least S ≥ x*(p) with S ≡ p (mod 2), except …" is correct (checked), but the case statement and the "equivalently" clause carry the same information; keep one.
- **p6.** The keyword "Egyptian fractions" and MSC 11D68 promise more than the paper delivers: the Egyptian-fraction connection is one sentence (p. 32). The opposite holds for 14J27/14J32 (elliptic surfaces/CY threefolds), which would fit if the framing in M2 is adopted.

## 7. Recommendation

**Major revision.** Confidence: **medium-high** for the number-theoretic part; I defer to the other referees on the analysis and numerics.

**Justification.** Within my remit I found no mathematical error. The threshold theorem, Theorem 5.11, Table 1, Theorem 5.16 (rank 0, torsion ℤ/2×ℤ/6, the isolation of the minimal pair), Prop. 8.2–8.3, Theorems 8.7–8.9 with their constants, and Tables 4–5 all reproduce exactly under independent computation and independent descents. The minimal pair (2,8,8)/(3,3,12) and the proof that it is isolated are a genuine, attractive answer to the remark of Dryden–Gordon–Greenwald–Webb.

However:
- the novelty of the arithmetic in §8 is overstated, and it is detached from the relevant literature (M1);
- the growth conjecture rests on an incorrect heuristic, with no upper bound proved (M2);
- the arithmetic apparatus is out of proportion to what the heat problem needs, while the key rank-0 proof is delegated to software output (M3, m1).

All of these are fixable without new mathematics beyond what I have indicated.

---

*Saved by the coordinating session: this subagent could not write files, so the report came back as text and was saved verbatim. The coordinator removed only the hand-back note addressed to itself.*
