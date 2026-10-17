<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Handling editor's report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

I was not allowed to write the report to `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/A-a-editor-wave-trace/REPORT.md`, so the full report is below. My check scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/A-a-editor-wave-trace/scratch/code/`.

## Summary

The manuscript studies closed orientable 2-orbifolds of curvature −1 with cone points. Its invariant is K_mult(O; C): the least k for which the first k heat-trace coefficients c_1, …, c_k separate O from every member of C with a different signature. The ingredients are as follows.

1. **The expansion.** The paper derives the complete small-t expansion of the heat trace from the Selberg trace formula (Prop. 2.7, App. B), with enveloping remainders (Prop. B.2). It credits Uçar, Donnelly and Dryden–Gordon–Greenwald–Webb for the coefficients.
2. **The triangular mechanism.** Uçar's triangular structure (Lemma 2.10) turns equality of c_1, …, c_L into equality of the reciprocal sum and of the odd power sums P_1, …, P_{2L−3}. From that point on, the problem is about signed multisets with vanishing low odd moments.

The main results are:

- **Spheres with n cone points (Thm A/1.3(i)).** The first n invariants suffice, the recovery runs through an explicit linear system with a Hurwitz-type determinant (Thm B), and n−1 invariants fail for n = 3, 4 (Thm C).
- **Area bound (Cor. 1.5/3.5).** ⌊Area/π⌋ + 4 invariants always suffice.
- **Bounded orders (Thm 1.2/3.8).** With all orders at most M, M + 1 invariants suffice against all of Sig, uniformly in the area, and M + 1 is attained.
- **Growth (Thm 1.1/3.14, Prop. 3.15).** f(A) lies between about √A and A. Power lower bounds f ≥ cA^α are equivalent to N(k) = O(k^{1/α}), where N(k) is the Prouhet–Tarry–Escott (PTE) function.
- **Changing the genus (Thm 3.11).** A Descartes-type bound prices a change of genus.
- **Triangle orbifolds (Thm 1.4, §5).** Three invariants suffice. Two first fail at O(2,8,8) and O(3,3,12), and this pair is isolated because C_{27/2} is a rank-0 elliptic curve.

The paper also contains:

- a variable-curvature section (§2.4) arguing that the counts are a constant-curvature phenomenon;
- a section on locality, with a quantitative "shape enters beyond all orders" bound (§4);
- a stability theory for recovering real orders from approximate invariants (§6).

The supplement contains extensive numerics on computed spectra.

What is good, plainly:

- The paper is careful and honest. It says which parts are elementary (p. 5) and labels every computational statement as illustration or as used in no proof (S8).
- It credits Uçar for the mechanism.
- Every claim I recomputed is correct (see below).
- The M + 1 theorem (Thm 3.8(iii)–(iv)) is a clean and genuinely nice result: a sign-change argument on the measure Σ x^{−1}δ_{x²}.
- The doubling trick of Prop. 3.12, where the reciprocal sums cancel through the factor (1 − 2^{j+1}) at j = −1, is elegant.
- The reduction of the growth exponent to PTE is correct and stated without overclaiming.

## Significance

For AGAG readers the relevant question is what this adds to spectral geometry. The honest answer is mixed.

- **The geometric input is short and prior.** It is the trace formula plus Uçar's triangular structure (Lemma 2.10, credited). After p. 11 the paper is the combinatorics of odd power sums with a reciprocal-sum constraint (§3), plus the arithmetic of one plane cubic (§5.2).
- **The deepest-looking theorem is an equivalence, not a resolution.** Theorem 1.1 makes the growth exponent of f equivalent to a PTE question that has been open for decades. It gives no new information on PTE, and Prop. 3.15 shows that the extra structure cannot decide the exponent. Whether f grows like a power of A at all is left open (p. 4).
- **By the paper's own §2.4 the counts are an artefact of constant curvature.** For every L, two signatures with equal c_2 carry metrics with equal H_L (Prop. 2.13(ii)). The minimal pair carries metrics whose invariants agree to all orders (Prop. 2.13(iii)).
- **The strongest results for a geometer are the cleanest ones.** These are Theorem 3.8 (uniform M + 1) and Theorem 3.4/Cor. 3.5 (an explicit area-only count). Theorem 3.8(i) is also the result the companion manuscript actually uses.

The paper is within AGAG's scope: inverse spectral problems on orbifolds appear in AGAG (refs [14], [16], [18], [20] of the manuscript are AGAG papers). It is not obviously below the journal's bar. Its significance rests on the referees accepting "how many Taylor coefficients at curvature −1" as a question geometers care about. The paper must argue that case better than it does now (M1, M2).

## Correctness and what was recomputed

All recomputations used my own code, exact rational arithmetic unless stated.

- **Coefficients (Prop. 2.7, Lemmas 2.6, 2.8, (8)).**
  - Recomputed p_0, …, p_3 from (4)–(5). They agree with (8), and p_3 agrees with the constant-curvature specialisation implied by Remark 2.12(b).
  - Leading coefficients equal |B_{2l+2}|/(2(l+1)!(2l+1)).
  - α_0, …, α_5 = 1, −1/3, 1/15, −4/315, 1/315, −4/3465, which is the sphere expansion with alternating signs.
  - The closed form of Φ_m (Lemma 2.6), checked at m = 5 against the defining sum to 15 digits.
- **Triangle invariants (10) and the minimal pair.**
  - c_1, c_2, c_3 for triangles agree with (10).
  - For the minimal pair, c_2 = 67/48 and d_3, d_4, d_5 = 25/12, −1775/24, 153025/48, as on p. 29 and in S4.
  - P_3 = 1032 vs 1782 confirmed.
- **Enveloping remainders (Prop. B.2(a)).**
  - E_m(t) evaluated by 30-digit quadrature of the trace-formula integral, for m = 3, 8, 12, t = 0.002, 0.01, 0.05 and K = 0, …, 6.
  - Every remainder has sign (−1)^K and modulus at most |b_K(m)|t^K, with ratio tending to 1 as t ↓ 0.
  - |b_l(m)| / (l!(m/π)^{2l} l^{−1/2}) is stable in l (≈0.106 for m = 3, ≈0.232 for m = 8), which supports the growth claim on p. 29.
- **Shared-invariant counts, recomputed exactly** (both areas equal, number of shared c_j as stated):
  - (2,8,8)/(3,3,12): 2. Theorem C(3) quadruples: 3. Example 3.6: 2.
  - (0;2^10)/(1;4^4): 2. The M = 3 and M = 4 pairs of p. 21: M − 1. (0;5,5,5)/(0;2,2,2,10): 2. Both pairs of Example 3.17(i)–(ii): 3. (2;)/(0;2^8): 1.
  - Table S1, rows L = 4 genus, L = 4, 5, 6, 7 cone count, L = 4 equal count, and Prouhet L = 2: exactly L in each case, with the printed areas where I compared them.
- **Theorem 3.8(ii) and (iv).**
  - The least-g areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054} for M = 2, …, 9 are reproduced.
  - (iv) with M = 2, X = 4: C = 180, ν = (10, −4), s = 2, as on p. 21.
  - Further instances (M, X) = (3, 5), (3, 7), (4, 6) share exactly M invariants, as (iv) predicts.
- **Theorem B.** Built the system (12) symbolically for n = 2, …, 5. At random rational orders the true e solves it, and det M = (−1)^{n(n+1)/2} ∏(m_i + m_j)/e_n exactly.
- **Theorem 5.8.**
  - ψ maps E into C_{27/2}, and φ∘ψ = id on E.
  - All twelve listed points lie on the curves.
  - #E(F_7) = #E(F_11) = 12. (16, 400) has order 3 and (−24, 360) has order 6. The discriminant is 2^18 3^8 5^6.
  - j = 4102915888729/9000000 and c_4 agree (u = 2) with LMFDB 90.c3. I fetched the LMFDB record: rank 0, torsion [2, 6].
- **Section 5 by enumeration, S ≤ 600.**
  - 83 hyperbolic triads with 10 ≤ S ≤ 18. The only collision with S ≤ 18 is the minimal pair.
  - The first overlaps S*(p), p = 2, …, 14, agree with Thm 5.4 and Table S2. The first adjacent collisions agree with Table S2.
  - The collision-free sums in [18, 600] are exactly the 38 sums of Prop. S2.1.
  - The first non-adjacent collision is (5,15,15)/(7,7,21) at S = 35.
- **Proofs checked line by line:**
  - Thm A, Lemma 3.1, Thm C(1), Thm 3.4, Cor. 3.5, Lemma 3.7, Thm 3.8(i), (iii), Cor. 3.9;
  - Thm 3.11 (the odd-gap count giving |ι| ≤ κ − 2L is correct), Prop. 3.12, Thm 3.13, Lemma A.1, Prop. A.2, Thm 3.14(a)–(d), Prop. 3.15, Lemma 3.16;
  - Cor. 5.1, Lemma 4.2's elementary parts, Prop. 6.1 (P_3 = −18c̃_1 − 120c̃_2 − 360c̃_3; amp = 2, 14, 498), Props 6.3(i) and 6.4.
- **Normalisation of Fig. 1.** The orbifold kernel is half the sum of the Neumann and Dirichlet kernels, which is correct.
- **Section 2.4, internal consistency only.**
  - β_{2,3} = 12K² − 2ΔK gives m^5-coefficients K²/2520 and −ΔK/15120, matching p_2 and Schueth.
  - β_{3,4} and Remark 2.12(b) give top coefficients 1/10080, −1/28800, 1/1209600, which agree with each other, with p_3 and with Prop. 2.11(iii).
- **PTE literature.** The claim that no bound o(k²) on N(k) is known (p. 23) is consistent with the 2026 statement of Croot–Mao–Yip ([47], §1). They state the pigeonhole bound k(k+1)/2 + 1 and Wooley's quadratic bound for W(k, m) as the best known.
- **Rendered pages viewed:** pp. 2, 3, 19, 25, 26, 28, 30, 31, 34, 38. Fig. 2's discs and rings match the multisets. Fig. 5(a)'s truncations have the right signs. Fig. 8's slopes match 1, 1/2, 1/3, 1/2. I found no typographical, sign or figure error on these pages.
- **Not verified:** the full proofs of Props 2.11 and 2.13 (see M3), the constants of Lemma 2.5 and of S3, the numerics of S4–S6, and the exhaustive searches (S8). All of these are declared outside the proof chain except §2.4.

## FATAL

None found. No main statement is false as far as I checked, and the key proofs I spot-checked are complete.

## MAJOR

**M1. The physical framing does not describe what the theorems measure (abstract; pp. 2–3, "Two facts make this a natural quantity", "large orders are heard late", "the number measures the part of the cone data that diffusion resolves before geometry enters"; p. 27; p. 29).**

K_mult counts Taylor coefficients of a divergent asymptotic series at curvature −1. It does not count what diffusion can detect. Five points need correcting.

- (a) **The heat trace at a single time already determines the signature.** At every fixed t > 0, Z_O(t) − Hyp(t) equals the explicit signature term G_σ(t) = I + ΣE_{m_i} (Thm 2.3). The companion manuscript separates signatures from one value G_σ(t*). So "heat" hears the whole signature at any single time, given a-priori bounds; only the coefficient sequence is slow.
- (b) **The time-scale ordering in "before geometry enters" is wrong in general.**
  - Optimal truncation of the cone series leaves an error of order e^{−π²/(µ²t)} = e^{−(2π/µ)²/4t} (p. 29). The closed geodesics enter at e^{−ℓ²/4t}. The cone series therefore stops being informative before geometry enters whenever µ > 2π/ℓ.
  - In the paper's own minimal pair (µ = 12; ℓ = 1.8626 for O(3,3,12), S4), π²/144 ≈ 0.069 against ℓ²/4 ≈ 0.867. At t = 0.01 the expansion's irreducible ambiguity is about e^{−6.9} ≈ 10^{−3}, while the geodesic term is about e^{−86.7} ≈ 10^{−38}.
  - Fig. 5(a) shows exactly this. The truncations leave the computed D(t) near t ≈ 0.02, while the exact cone term tracks D up to t ≈ 0.1.
- (c) **"Large orders are heard late" is misleading.**
  - Large orders dominate the t^0 coefficient Σ(m² − 1)/(12m), and Fig. 1 shows heat lingering most at the order-12 point.
  - What comes late is the separation of two configurations once their low odd moments agree.
- (d) **"Learns only what lies in that disc" (p. 2) is false at the exponentially small level that §4 is about.**
- (e) **The wave-trace description, which is the precise form of the heuristic, is missing.**
  - Each elliptic term contributes to the even wave trace the kernel 1/(2 sin((2θ_j + iu)/2)) (the Fourier form of the beta integral in App. B).
  - This kernel is real-analytic on all of ℝ: orbifold cone points are non-diffractive and give no real-time singularity.
  - Its nearest complex singularities lie at u = ±2πi/m.
  - So the cone heat invariants are Taylor coefficients at 0 of an analytic wave-trace contribution, and their divergence radius is set by 2π/µ. The length spectrum, by contrast, appears as real-time singularities (Duistermaat–Guillemin, or Selberg for constant curvature).
  - Stating this would replace the disc metaphor with a correct statement, and it explains both the late separation and the competition in (b).

**M2. Significance for AGAG must be argued, not asserted (pp. 3–6, §§3, 5.2).**

As explained under Significance, after Lemma 2.10 (prior work) the content is Diophantine.

- Theorem 1.1 relocates an open problem without progress on it.
- Theorem 1.4(iii) is the rank of one elliptic curve already in LMFDB.
- Section 2.4 shows the counts lose their meaning outside constant curvature.

The authors must say plainly what a geometer learns, and use the uniform results to do it.

- Thm 3.8 shows that bounded orders give an area-free number.
- Cor. 3.5 gives a number computable from c_1.
- The companion manuscript turns these into an effective inverse spectral theorem.

The introduction currently leads with the PTE equivalence, which is the least geometric result. The abstract's "M + 1 is attained" should also say "at sufficiently large area": the attaining pairs have areas 2π·77054 already at M = 9 (p. 21, verified).

**M3. Section 2.4 makes new variable-curvature claims on proofs that are only sketched (pp. 12–15, Props 2.11, 2.13, Remark 2.12).**

These results carry the paper's claim that "the setting of constant curvature is essential" (pp. 3, 15). Their proofs are condensed to the point where a referee cannot check them. Specifically:

- (i) **Pole order.** The pole-order bound deg P ≤ 2l comes from "following Schueth's proof of [19, Thm 3.7] to all orders" without that extension being written out.
- (ii) **Radial reduction.** It assumes the coefficients of Donnelly's polynomial are SO(2)-invariant functions of the jet. This needs a proof or a precise reference.
- (iii) **Prop. 2.13(ii).** Three steps should be written out:
  - why the conformal bumps leave the cone terms and Ω_0 unchanged;
  - why one θ gives G_l(θ) ≠ 0 for all l ≤ L simultaneously (it does, since ∫ψΔ_0^{l+1}ψ = ±∫|ξ|^{2l+2}|ψ̂|² ≠ 0, but say so);
  - why the rescaled family remains an orbifold metric of curvature K_0 near the cone points.
- (iv) **Remark 2.12** rests on computer algebra. I checked internal consistency (above), but consistency is not a proof.

Either give full proofs, which an expert in corner and cone heat coefficients must referee, or demote §2.4 to clearly marked remarks. If demoted, the headline claims on p. 3 must be softened accordingly.

**M4. Section 6 and supplement S3/S5 address an inverse problem that the paper itself says has no data (pp. 35–38, 42).**

- The "heat invariants" of real, non-integer orders are not heat invariants of any orbifold (p. 36).
- The step from a heat trace to c_1, …, c_n is explicitly not analysed (p. 36; end of App. B).
- Corollary 6.5 needs a proved bound δ_1 that the paper cannot supply, and the blind recovery is "validated, not proved" (p. 38).

The practically meaningful version of this problem, deciding the signature from computed spectral data, is the subject of the companion manuscript, on the same spectra (O1). As it stands, §6 is a stability analysis of a polynomial root-finding map. The one point of spectral interest is that the conditioning is a Hurwitz determinant (Thm B), and that point is already in §3. Either:

- connect §6 to data, by proving an error bound for extracting c_1, …, c_n from Z_O on an interval of t, given bounds on µ, ℓ and diam (Prop. B.2 is most of the way there); or
- move it out of this paper.

## MINOR

- **m1 (p. 4, Thm 1.4(ii); §5.1).** The minimal pair is also the collision of least area, and this is easy to prove. For S ≥ 18, every triad of stratum p ≥ 3 has R ≤ R⁺_{S,3} = 2/3 + 1/(S − 6) ≤ 3/4. R is injective within stratum 2, so every collision has R ≤ 3/4, and equality forces Λ = 27/2, hence (by Thm 5.8) a multiple of the minimal pair. Worth stating, since area is what c_1 measures.
- **m2 (p. 6).** "To our knowledge no explicit number was known." For spheres with known n, Uçar's triangular structure plus Newton's identities gives n at once. Restrict the novelty claim to separation against all of Sig and to the uniform results.
- **m3 (pp. 28–29, Thm 4.2).** Credit the result to Huber, McKean and Selberg more explicitly and call it a proposition. Its bound (a) overestimates by factors up to 10^{10} (p. 29, S6), and the last sentence of (b), "L* = ℓ if ℓ_1 ≠ ℓ_2", is immediate.
- **m4 (p. 23).** "No bound o(k²) is known" is load-bearing for the abstract. Support it with current sources: the pigeonhole bound, and Wooley's bound for W(k, m) as recalled in [47, §1]. Explain why Hua's 1938/1949 results on Tarry's problem do not give o(k²) for N(k).
- **m5 (p. 26, Fig. 3; S1).** The "exact" K_mult on 525 complete area classes are enumerated "with no bound on the orders". Describe the algorithm, including the a-priori bound on orders at fixed area, so that completeness of each class can be checked.
- **m6 (pp. 17–18, 13).** κ denotes the constant in Thm C(1), |U*| + |V*| in the proof of Thm 3.4, and a curvature in the proof of Prop. 2.11. The letter a is both a node and a_l (p. 20; the paper itself has to warn about this). Rename.
- **m7 (p. 14, Prop. 2.13(i)).** "For K_0 = 0 and L ≥ 3 this fails." State which assertion fails.
- **m8 (p. 3).** f(A) is undefined for A < π/21, where the set is empty. State its domain.
- **m9 (p. 12, Prop. 2.11(i)).** Explain whether anything survives for m ≤ l − 2. Problem 5(b) suggests not; say so in the statement.
- **m10 (p. 5).** The "stability theorem" paragraph promises exponents "with explicit constants". The constants live only in S3 and involve an unestimated matrix norm in one place. Adjust the wording.
- **m11 (Literature).** Add Duistermaat–Guillemin. For contrast with diffractive (non-orbifold) cones, add the wave-trace literature (e.g. Hillairet; Ford–Wunsch), since the paper extends b_l to real m (p. 10) and uses a non-orbifold cone in Prop. 2.13(iii).

## Presentation

- **P1 (abstract).** It is over-compressed: three result families, N(k) introduced only as "the Prouhet–Tarry–Escott function", and no mention of constant curvature. Lead with the uniform results, state "at curvature −1", and define N(k).
- **P2 (pp. 3–7).** Every main theorem appears under two names (1.1 = 3.14 + 3.15; 1.2 = 3.8 + 3.9; 1.3 = A–C + 3.11; 1.4 = 5.1, 5.6–5.8). Use one numbering.
- **P3 (p. 7, Table 1).** About 25 symbols are needed before §3. Combined with m6, the paper is hard to read.
- **P4 (figures).**
  - Fig. 1 concedes that the feature it is meant to show is "confined to a few pixels" (p. 3).
  - Fig. 4(a) draws (0;3,3,3,3) as surfaces of revolution without cone points.
  - Fig. 6 carries no information beyond the angles.
  - In Fig. 3, the open squares lie below the dashed proven lower bound for f. This is consistent, since they bound K_mult of specific orbifolds, but it will confuse readers; say so in the caption.
- **P5 (§2.4).** The section interrupts the logical line from §2.3 to §3. Place it after §5 or in an appendix.
- **P6 (wording).** Replace the anthropomorphic vocabulary ("heat learns", "hears", "lingers", "late") by precise statements where a claim is made (see M1).
- **P7 (§6).** It cannot be read without S3 (δ_thm, Ξ_µ, cond). If it stays, give the definitions in the main text.

## Overlap with the related manuscripts

- **O1 (companion 1, "Finitely many eigenvalues…").**
  - Its §§2–3 restate, without proof, Thm 2.3, Lemmas 2.4–2.6, 2.8, 2.10 and 3.3, Prop. B.2, Cor. 3.5 and Thm 3.8(i) of this paper (its Table 1). It adds an integrality lemma (its Lemma 3.3), a few lines from Lemmas 2.10 and 3.3 here.
  - Its new content is genuinely separate: diameter bound, eigenvalue counting, effective N and δ, the a-posteriori test, and the cusp-like behaviour of O(2,3,m).
  - The two papers share the computed spectra, and the companion re-describes the FEM/NGSolve/ARPACK method (its §7.1) that is in S4 here.
  - This is a legitimate split, not salami. However, the companion cannot be judged or accepted without this paper, so the two must go to at least one common referee and be decided in order.
  - The real overlap in purpose is this paper's §6/S3/S5: recovering the signature from approximate spectral data, with a blind recovery on the same spectra. The companion does this properly (M4).
- **O2 (companion 2, "Triples with equal sum and equal reciprocal sum", INTEGERS).**
  - The division is mostly clean. The note proves the counting asymptotics and class sizes, which are cited on p. 34 and not used in any proof here.
  - Two items are split or duplicated:
    - The exhaustive enumeration of admissible triples with S ≤ 4800 (Prop. S2.1, collision-free sums) is the same computation the note reports and extends to 6000. Report it once and cite it.
    - The arithmetic of the pencil C_Λ is split. The note treats general Λ, including the torsion family Z/2×Z/6 through isosceles points, with Λ = 27/2 named. It then explicitly defers C_{27/2} to Theorem 5.8 here. Theorem 5.8 is pure arithmetic and its natural home is the note. Keeping it here to supply an "isolation" theorem looks like slicing.
  - The authors should either move Theorem 5.8 to the note and cite it, keeping Thm 1.4(iii) as a corollary, or justify the split.
- **O3.** No result is proved twice that I could find. The authors' description of the division (pp. 5–7) is accurate.

## Editorial decision (send to review / desk-reject) and recommendation (accept / minor / major / reject) with confidence

**Decision: SEND TO REVIEW.**

The results are correct where I checked them, including every numerical claim I recomputed. The topic is within AGAG's inverse-spectral remit, and the uniform statements (Thm 3.8, Cor. 3.5) have real content for geometers. There are no grounds for a desk rejection on correctness or scope.

Referees should be:

- one spectral geometer expert in heat coefficients at conical and orbifold singularities, essential for §2.4 and for the framing;
- one number theorist familiar with PTE and elliptic curves, for §§3.4 and 5.2.

**Recommendation: MAJOR REVISION.** M1 and M2 must be fixed before this can be judged as a geometry paper. M3 must be fixed or the corresponding claims withdrawn. M4 and O2 need a decision by the authors.

**Confidence:** high on correctness of the spot-checked statements; moderate on the significance judgment, which the referees should test.

## What resolves each issue

- **M1.** Rewrite the abstract and introduction to say the paper counts Taylor coefficients of the heat expansion at curvature −1. State that G_σ(t) at one time already separates signatures, citing the companion. Add a short paragraph comparing the three exponential scales: e^{−(2π/µ)²/4t} for cone-series divergence, e^{−ℓ²/4t} for geodesics, and the truncation window t ≪ (π/µ)², using the minimal pair as the worked example. Replace "before geometry enters" and "heard late" with precise statements. Add the wave-trace formulation: analytic elliptic contributions with complex singularities at ±2πi/m, and length-spectrum singularities on the real axis.
- **M2.** Reorganise the introduction to lead with Thm 3.8 and Cor. 3.5 and their inverse-spectral use. State the geometric consequences explicitly. Add "at sufficiently large area" to "M + 1 is attained".
- **M3.** Give complete proofs of Prop. 2.11(i)–(iii) and Prop. 2.13(ii)–(iii), including the extension of Schueth's argument, the equivariance of Donnelly's coefficients, and the bump-construction details. Alternatively, demote §2.4 to remarks and soften pp. 3 and 15.
- **M4.** Either prove a data-to-invariants error bound so that Thm 6.2 and Cor. 6.5 apply to heat-trace data, or remove §6, S3 and S5 (or transfer them to the companion) and keep Thm B's Hurwitz-determinant remark in §3.
- **m1–m11.** Make the textual additions and corrections listed: least-area statement, tempered novelty claim, credit for Thm 4.2, PTE references including Hua and Wooley, area-class algorithm, renamed symbols, clarified Prop. 2.13(i), domain of f, the m ≤ l − 2 caveat, wording on constants, wave-trace and diffraction references.
- **P1–P7.** Rewrite the abstract. Use a single theorem numbering. Lighten the notation. Revise or remove Figs 1, 4(a) and 6, and clarify the caption of Fig. 3. Relocate §2.4. Use precise wording. Make §6 self-contained or remove it.
- **O1.** Submit the two papers to a common referee and decide them in order. Replace the duplicated methods text in one paper with a citation. Resolve the §6 overlap via M4.
- **O2.** Report the S ≤ 4800 enumeration in one paper only. Move Theorem 5.8 to the triples note and cite it, or explain why the curve C_{27/2} belongs to the geometry paper.
