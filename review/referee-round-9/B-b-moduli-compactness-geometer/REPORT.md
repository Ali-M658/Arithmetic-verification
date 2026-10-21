<!-- Round 9 B-b referee report: returned text saved verbatim; the reviewer could not write files -->

I could not save the report: writing REPORT.md was refused (subagents may not write report files), so the full report is below. In short, I found no mathematical error in Sections 3, 4 or 8 or in the appendix results they rely on, and I recommend minor revision.

# Referee report (AGAG): "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

**Referee B-b, moduli and compactness geometer.** My assignment covers Section 3 (heat invariants of a signature), Section 4 (separation, diameter bound, count of closed geodesics), Section 8 (the order hypothesis via O(2,3,m), the collar construction, Problem 1). It also covers every appendix result these sections rely on: Lemma A.2, Proposition 2.3 (proved in A.2), Lemma A.3, Lemma A.4, and the proofs of Lemma 3.1 and Theorem 3.2 in A.3. I also covered Lemma 2.2(i) and Lemma 5.1(i), which Sections 4 and 8 use. I treated the placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) as known. Page numbers are the printed page numbers of the PDF. I checked every typographical point against rendered page images (pp. 8–13, 25–30, 32–34).

## 1. Summary (of the assigned part)

- **Section 3** reduces "two signatures share their first L heat invariants" to equal area plus equal odd power sums of padded order multisets (Lemma 3.1). It proves separation: L ≥ ⌊A/π⌋+4, or L ≥ M under the order bound (Theorem 3.2). It also proves that the first nonzero difference is an integer multiple of an explicit rational (Lemma 3.3). This yields the lower bound |d_k| ≥ a_{k−2}, or 1/(2 lcm) when the areas differ.
- **Section 4** gives three elementary facts of plane hyperbolic geometry (Lemma 4.1). From them it proves:
  - a lower bound d_0(ε,M) on the distance between elliptic points (Lemma 4.2), via the reflection-triangle construction;
  - a lower bound for the area of balls of radius 2r_0 (Lemma 4.3);
  - a diameter bound D(A,ε,M) (Theorem 4.4);
  - by packing around a maximal separated net, a count n_O(x) ≤ C_*(A,ε,M)e^x of closed geodesics that needs no diameter (Lemma 4.5).
- **Section 8.1** proves the hyperbolic case of Jørgensen's inequality (Lemma 8.1). It then shows:
  - the family O(2,3,m) lies in C(π/3, ℓ_{2,3}, m) with ℓ_{2,3} = 0.56206…, uniformly in m (Proposition 8.2);
  - λ_j(O(2,3,m)) ≤ 1/4 + π²(j+1)²/h_m² (Proposition 8.3);
  - by pigeonhole, the order bound cannot be dropped (Remark 8.4), and any decision rule needs N ≳ log M / log log M (Corollary 8.5).
- **Section 8.2** constructs the pinching family O_{k,b} with an explicit collar and explicit small-eigenvalue bounds (Proposition 8.6). It then poses Problem 1: is the systole bound needed?

## 2. Significance

- **Section 3.** Within this paper Section 3 is bookkeeping. Its content comes from the companion paper [31] and is reproved in Appendix A. Lemma 3.3 is a short, clean consequence and is exactly the input Lemma 6.1 needs.
- **Section 4.** The arguments are elementary: reflection-group trigonometry plus a packing estimate. They are not new in kind. The value is that every constant is explicit and that the count of closed geodesics (Lemma 4.5) avoids the e^{3D} loss of the diameter route. Table 4 makes this concrete: C_* is between 4×10⁵ and 7×10¹⁰, against πe^{3D}/A between 3×10¹⁹⁶ and 2×10²⁹³²⁵. Theorem 4.4 itself plays no role in any main result (see m1).
- **Section 8.1.**
  - Theorem 1.2 is the most geometrically interesting statement in my part. Its novelty, however, is modest, and the authors say so honestly (p. 5). That the number of eigenvalues below any level above 1/4 grows without bound along elliptic degeneration is Garbin–Jorgenson [15, Thm 5.7].
  - What is new is the uniform systole bound ℓ_{2,3}, the explicit eigenvalue bound and the pigeonhole lower bound N ≳ log M / log log M.
  - The upper bound coming from Theorem 6.2 grows exponentially in M, through L_M. So the dependence on M is essentially open; m3 below shows the gap can be narrowed to polynomial cheaply.
- **Section 8.2** is a carefully worded open problem with supporting computations. I think Problem 1(b) is closer to resolution than the text suggests (m4).

## 3. Correctness, and what I recomputed

I read every proof in my part line by line. I found no mathematical error in any proof on which a main result depends.

**Section 3 and Appendix A.2–A.3**

- Lemma A.2:
  - Closed form Φ_m(u) = (cot u − m cot mu)/(4m sin u): checked symbolically (partial fractions and the cotangent sum identity) and numerically (m = 7, u = 0.2, agreement to 30 digits).
  - Series for mφ_k(m): rederived from the Bernoulli expansion of cot. Positivity and monotonicity in m follow as stated.
- Proposition 2.3:
  - Beta-integral moments, the sign bookkeeping of the Taylor remainders, the identity b_l = Σ_k g_k(−1/4)^{l−k}/(l−k)!, and |b_K| = Σ_k |g_k| 4^{k−K}/(K−k)!: rederived.
  - Enveloping property of E_m checked numerically by quadrature (m = 5, t = 0.05 and m = 8, t = 0.02; K = 0,…,3). The sign is always (−1)^K and |remainder|/(|b_K|t^K) lies in [0.70, 0.96].
  - α_1 = −1/4 − μ_0 = −1/3 (μ_0 = 1/12) agrees with the stated α_0,…,α_3.
- Lemma A.3: leading coefficient a_l recomputed (a_0 = 1/12, a_1 = 1/360, a_2 = 1/2520, a_3 = 1/10080). b_0(m) = (m²−1)/(12m) agrees with the formula for p_0.
- Lemma 3.1: verified the triangular system C_l ↔ Ψ_k (diagonal a_l ≠ 0) and that padding by 1 changes nothing.
- Theorem 3.2(i):
  - Checked R(U) = R(V), |V*| − |U*| = 2(g−g′), the parity argument (Lemma A.4 together with e_{κ−1} = e_κ·Σ1/x giving an even polynomial), and κ ≤ n + n′ + |d| = 2 max(n+g−g′, n′+g′−g) ≤ 2(⌊A/π⌋+4).
  - The threshold ⌊A/π⌋+4 is the correct one: ⌊A/π⌋+3 would allow κ = 2L+2.
- Theorem 3.2(ii): the column-subtracted Vandermonde argument is correct.
- Lemma 3.3:
  - (i) and (ii) verified, including the sign (−1)^k, the index 2k−3, and the use of Lemma 3.1 with L = k−1.
  - Example on p. 10: (0;4,4,4) vs (0;3,4,6) gives d_2 = −1/12 = −a_0 (verified from b_0).
  - Figure 1 (p. 17): (0;2,8,8) vs (0;3,3,12) gives d_3 = −a_1(P_3(U) − P_3(V)) = −(1/360)(1032 − 1782) = 25/12, as stated.
  - Remark 6.5: (0;2⁴,7⁷) and (0;4⁶,8⁴) have area 12π and share P_1 = 57 and P_3 = 2433 after padding. P_5 differs (117777 vs 137217). The claim is correct.

**Section 4 and Lemma 2.2(i)**

- Lemma 4.1:
  - (H1) recomputed in both models.
  - (H2) correct.
  - (H3): the hyperboloid normals, ⟨n_1,n_3⟩ = −X, X > −1 (since d > 0) and the side argument are all correct.
- Lemma 4.2:
  - Verified that γ = s_1s_3 = (s_1s_λ)(s_λs_3) ∈ Γ.
  - Hyperbolic case: cosh h = X ≤ cosh d.
  - Elliptic case: defect ≥ π/(abc), cos((θ+α+β)/2) ≥ 1/(abc), |θ−α−β| ≤ π − π/M, and sin α sin β ≤ π²/(ab), giving cosh d − 1 ≥ 2/(π²cM).
- Lemma 4.3: injectivity of the projection, the two cases, and ρ_1 ≤ r_0, ε ≥ 2d_0 = 4r_0 ≥ 2ρ_1 are all correct.
- Theorem 4.4: the closed form holds:
  - cosh ρ_1 − 1 = sinh²r_0 sin²(π/M)/(cosh ρ_1 + 1) ≥ (cosh r_0 − 1)sin²(π/M);
  - min_{M≥2} M·arccosh(1 + 2/(π²M²)) = 0.634 > 0.6.
- Lemma 4.5: the net argument, the coset packing #{γ : d(b̃,γb̃) ≤ R} ≤ M(cosh(R+ρ_1)−1)/(cosh ρ_1−1), and d(b̃,γb̃) ≤ x + 10r_0 are correct. Classes and their inverses are counted separately, as the definition of n_O requires.
- Lemma 2.2(i): correct.
- **Recomputed at 40 digits (mpmath):**
  - Every entry of Table 2: 56.6, 1125, 6.37e5; 150.9, 3001, 1.70e6; 640, 3184, 1.70e6; 1132, 2.25e4, 1.27e7. All agree, and each lies below the closed form.
  - C_* for all eight rows of Table 4: 1.3e8, 3.5e9, 4.0e5, 4.0e5, 9.5e9, 8.1e7, 3.0e6, 7.1e10. All agree.
  - The range πe^{3D}/A ∈ [3.4×10¹⁹⁶, 2.4×10²⁹³²⁵] (p. 13). Agrees.
  - k_* for every row of Table 4. Agrees.

**Section 8 and Lemma 5.1(i)**

- Lemma 8.1:
  - Recomputed B_{n+1} = B_nAB_n^{−1} and x_{n+1} = −x_n(1+x_n)(u−u^{−1})².
  - Checked the non-vanishing argument, including the "exactly one of a, d vanishes" case leading to a parabolic commutator, and that the fixed points p_n, q_n are finite and nonzero.
  - Checked the renormalisation C_n = A^{−k_n}B_nA^{k_n} → A. The proof is correct.
- Trace identity (p. 26): recomputed symbolically (the off-diagonal entries are ±sin(φ/2)cosh r) and numerically (L = 0.7, φ = 2π/3, r = 0.4, agreement to 30 digits).
- Proposition 8.2:
  - Side lengths, h_m and s_m from the hyperbolic law of cosines.
  - The cone ball: P is the regular polygon of inradius h_m, and γP ∩ P has empty interior unless γ ∈ Stab(v_m).
  - The systole argument: d(x,q) ≤ d(v_m,v_3) − h_m ≤ s_m, so r ≤ 2s_m < 2s_∞.
  - Lemma 8.1 applies, since β cannot swap the endpoints.
  - Recomputed: cosh 2s_∞ = 5/3; ℓ_{2,3} = 2 arsinh(½(37/12)^{−1/2}) = 0.5620668…; h_7 = 0.54527, h_13 = 1.3670, h_100 = 3.4596, each ≥ log(m/2π); 2 arccosh((1+2cos(2π/7))/2) = 0.9839866; 2 arccosh(3/2) = 1.9248473.
- Identity (3), both q's: rederived. Proposition 8.3, including the pigeonhole step: correct. Remark 8.4 (the A < π/3 finiteness via Lemma 5.1(i)): correct. Lemma 5.1(i): all extremal cases rechecked. Corollary 8.5: correct, with c′ = 1/4 + π²/h_7² ≈ 33.5.
- Garbin–Jorgenson condition (a) holds for m ≥ 13: m/2π ≥ 1 + m/4π exactly when m ≥ 4π.
- Section 8.2 and Proposition 8.6:
  - Q_{k,b} normals, the Lambert relation sinh a sinh b = cos(π/k), the area 4π(1−2/k) (= 4π/3 for k = 3), the collar inclusion, and both Rayleigh quotients (∫_0^a ρ² cosh ρ dρ = (a²+2) sinh a − 2a cosh a) are correct.
  - Consistency with Table 5: 4b reproduces the listed systoles (θ = 0: 4b = 2.633915; θ = 2.8: 4b = 0.693995). At θ = 2.8 the λ_1 bound is 0.718.
- The Euler-characteristic argument for (1;3) and the areas of (0;3,3,3,3), (1;3), (0;2,2,6,6), (0;3,∞,∞) (all 4π/3) are correct.
- The Jørgensen remark on p. 12 is correct. Equality in the (2,3,7) group holds because cosh d(v_2,v_7) = 1/(2 sin(π/7)), so 4 sin²(π/7)cosh²d = 1.

## 4. FATAL

None in the assigned part.

## 5. MAJOR

None in the assigned part. Every proof that a main result depends on (Lemmas 3.1, 3.3, 4.2, 4.3, 4.5, 8.1; Theorem 3.2; Propositions 2.3, 8.2, 8.3; Corollary 8.5; Appendix A.2–A.3) is correct as written. The points below are requests that would improve accuracy and value; none is a gap.

## 6. MINOR

**m1 (pp. 10–13, Section 4: framing).** Section 4 is titled "The diameter", and its headline result Theorem 4.4 is, by the authors' own statement (p. 13), "used in no proof of a main result". The load-bearing results are Lemmas 4.2, 4.3 and 4.5.
- *Fix:* retitle the section (e.g. "Separation of cone points and the count of closed geodesics"). Demote Theorem 4.4 to a Proposition or Remark, or say in the first line of Section 4 that it serves comparison only. Then Table 2 no longer reads as an input to the main theorem.

**m2 (p. 12, remark after Theorem 4.4: half incorrect).** The sentence "we expect the factors 1/M in d_0 and v_0 not to be intrinsic" is false for v_0.
- *Why v_0's 1/M is intrinsic.* On O(2,3,M) ∈ C(π/3, ℓ_{2,3}, M), the ball of radius 2r_0 about the cone point of order M is a cone of area 2π(cosh 2r_0 − 1)/M. This holds because 2r_0 ≤ d_0 < h_M (Proposition 8.2). So any admissible v_0 is O(1/M), and the 1/M in Lemma 4.3 cannot be removed. Some growth of D in M is likewise forced (Proposition 8.2), though only logarithmic growth is forced, not M³.
- *Why d_0's 1/M is not intrinsic.* The factor in d_0 can indeed be removed, by Jørgensen's inequality as the authors suggest:
  - For two elliptic points one of which has order p ≥ 7, the two rotations generate a non-elementary group (an elementary discrete group without parabolics contains no elliptic of order ≥ 3 outside a point stabiliser). So 4 sin²(π/p)(1 + sin²(π/q) sinh² d) ≥ 1, giving sinh² d ≥ 1/(4 sin²(π/7)) − 1, that is d ≥ h_7 = 0.5453 (computed).
  - For two points of orders ≤ 6, the proof of Lemma 4.2 goes through, except that the third vertex w may have large order c. If c ≥ 7, the same bound gives d(p,w) ≥ h_7. Moreover α + β ≤ 5π/6 (a = b = 2 forces X > 1). The law of sines then bounds d(p,q) below independently of c.
  - Either correct the sentence (v_0's factor is necessary for fixed-radius balls), or include the order-free d_0. It is a short paragraph, though as the authors note it barely affects Theorem 6.2.

**m3 (pp. 9, 14, 28: the M-dependence of δ_1 and of N).** Lemma 3.3(i) gives |d_1| ≥ 1/(2L_{σσ′}), and Section 6 replaces L_{σσ′} by L_M = lcm(1,…,M) ~ e^M. But σ and σ′ together have at most 2n_* cone orders, each ≤ M, so L_{σσ′} ≤ min(L_M, M^{2n_*}).
- With this, δ_1 is polynomial in M for fixed A. So are all δ_k/Q(k−1) for k ≤ k_* ≤ n_*, since |b_K(M)| ≍ (M/π)^{2K}. Then t_1 ≥ c(A)M^{−O(n_*)}, and N, δ^{−1} from Theorem 6.2 become polynomial in M for fixed A and ε.
- The sentence on p. 28 ("Theorem 6.2 gives an N that grows much faster with M, through L_M and |b_K(M)|") would then read "polynomially in M, with exponent depending on A", against the lower bound log M / log log M of Corollary 8.5. The numbers in Table 4 do not change: there M^{2n_*} > L_M.
- *Fix:* take δ_1 = 1/(2 min(L_M, M^{2n_*})) (or state the remark) and correct p. 28.

**m4 (pp. 30–31, Problem 1(b)).** The discussion lists (0;3,3,3,3), (1;3) and (0;2,2,6,6), all of area 4π/3, and contrasts only (1;3). The natural candidate pair for a negative answer to (b) is (0;3,3,3,3) and (0;2,2,6,6):
- Each, pinched along a separating curve, has one eigenvalue tending to 0. The partition for (0;2,2,6,6) is {2,6}|{2,6}, since {2,2}|{6,6} is not hyperbolic on one side.
- The cusped limits are (0;3,3,∞)⊔(0;3,3,∞) and (0;2,6,∞)⊔(0;2,6,∞), both rigid and arithmetic. (0;3,3,∞) is the index-2 subgroup Γ² ⊂ PSL(2,Z), which contains Γ(2). (0;2,6,∞) is the Hecke group G_6, which contains Γ_0(3) with index 2.
- For small levels the absence of eigenvalues in (0,1/4) is known (Huxley-type results). This should be checked and cited, not taken from me.
- The missing lower bound λ_2 ≥ 1/4 − o(1) also seems within reach, through the route the authors themselves name. Pass to a fixed torsion-free normal finite-index subgroup (Selberg's lemma), so the family lifts to degenerating closed surfaces with a fixed deck group G. The orbifold eigenfunctions are the G-invariant ones. For eigenvalues below 1/4 − η, Ji's eigenfunction convergence (no mass escapes into the collars) shows that L²-limits of G-invariant orthonormal eigenfunctions are G-invariant orthonormal eigenfunctions on the limit.
- Together with a collar bound (Proposition 8.6 covers only the symmetric quadrilaterals with k ∈ {3,4}; for (0;2,2,6,6) use the standard collar lemma), the first N eigenvalues of both families would converge to (0,0,1/4,…,1/4). That answers (b) negatively for A = 4π/3, M = 6.
- I do not ask the authors to prove this. They should at least name this pair and state precisely which two inputs remain (the small-level spectral gap for Γ² and G_6, and the G-invariant convergence). The present text slightly understates how close the problem is to settled.

**m5 (p. 28, Figure 3 discussion).** "so λ_j(O(2,3,m)) → 1/4 for every j ≥ 1" follows "Granting this", but reads as a conclusion. Condition (b) of Garbin–Jorgenson is asserted "in the sense in which they treat their own Example 5.8", which is not a verification.
- *Fix:* phrase the conclusion conditionally (as the following sentence already does for the plotted quantity), or verify condition (b).

**m6 (pp. 6, 9: cross-reference).** Table 1 attributes Theorem 3.2 to "[31, Cor. 3.8, Thm 3.11(i)]", while the header of Theorem 3.2 cites "[31, Cor. 3.8, Thm 3.11]". Make them agree.

**m7 (p. 30, Proposition 8.6 statement).** The parenthesis "Section 7 uses b ≤ a" does not belong in a proposition statement. Move it to the text.

**m8 (p. 30, Proposition 8.6 and Section 7).** The systoles in Table 5 equal 4 min(a,b) to all six printed decimals (my recomputation: 2.633915 at θ = 0, 0.693995 at θ = 2.8). Section 7 calls this a numerical identification.
- *Suggestion:* if a short proof that ℓ(O_{3,b}) = 4 min(a,b) is available, which is plausible by a reflection argument, it would strengthen Section 8.2. If not, keep the present wording.

## 7. Presentation

- **P1 (notation clashes).**
  - ℓ is used for the systole and for the interval length in the proof of Proposition 8.3 (p. 27).
  - Garbin–Jorgenson's ε (p. 28) clashes with the systole bound ε.
  - λ names a line in (H3) and Lemma 4.2 (pp. 10–11) but elsewhere means eigenvalues.
  - In Lemma 3.3(ii), "to A say" (p. 9) reuses the class bound A for the common area.
  - In (H2), "x ↦ 2c_i − x̄" (p. 10) uses x for a complex variable.
- **P2 (p. 11).** A small figure for Lemma 4.2 would help readers: the triangle p̃q̃w with L_1, L_3 and the two cases X > 1 and X < 1.
- **P3 (p. 10).** Lemma 4.1 is the only lemma in the paper without a parenthetical name; e.g. "(Plane hyperbolic geometry)".
- **P4 (p. 9).** Section 3 is very compressed. One sentence explaining why padding with orders 1 is harmless (ψ_k(1) = 0, p_l(1) = 0) would help when Lemma 3.1 is stated; at present it appears only in A.3.
- **P5 (p. 26).** The paragraph introducing Lemma 8.1 says the group generated is non-elementary, but the hypothesis of Lemma 8.1 is phrased differently (B fixes neither fixed point and does not swap them). A one-line remark that these coincide here would avoid a moment's doubt.

## 8. Recommendation

For Sections 3, 4 and 8 and the appendix results they use: **minor revision**.
- Confidence is high for the correctness of Sections 3, 4 and 8.1 and Appendix A.2–A.3, every step of which I rederived or recomputed.
- Confidence is medium for the assessment of Section 8.2 and Problem 1, where my m4 is a suggestion I have sketched, not proved.

Good points: the proofs are complete, short and checkable. Every constant in Tables 2 and 4 that falls in my part is reproduced exactly. Sections 4 and 8 state honestly what is new and what is borrowed. Lemma 8.1 and Proposition 8.2 are clean and self-contained.

Reasons for caution about significance: Section 4's tools are elementary, and Theorem 4.4 is unused. Theorem 1.2 adds explicit constants and a uniform systole bound to a phenomenon already established by Garbin–Jorgenson. And the M-dependence of the effective N is left far less sharp than it easily could be (m3).

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| m1 | Retitle Section 4. Demote Theorem 4.4 or state its auxiliary role at the start of the section. |
| m2 | Correct the remark: v_0's 1/M is intrinsic (O(2,3,M) cone ball); d_0's is not. Optionally add the Jørgensen-based order-free separation. |
| m3 | Use L_{σσ′} ≤ min(L_M, M^{2n_*}) in δ_1. Note that N and δ^{−1} are then polynomial in M for fixed A, ε. Correct the sentence on p. 28. |
| m4 | Name the pair (0;3,3,3,3) / (0;2,2,6,6) and the two remaining inputs (small-level spectral gap for Γ² and G_6; G-invariant eigenfunction convergence on a torsion-free cover), or settle Problem 1(b). |
| m5 | Make the λ_j → 1/4 statement explicitly conditional, or verify Garbin–Jorgenson (b). |
| m6 | Harmonise the citation of [31, Thm 3.11]. |
| m7 | Move "Section 7 uses b ≤ a" out of the statement of Proposition 8.6. |
| m8 | Optional: prove ℓ(O_{3,b}) = 4 min(a,b), or keep the wording. |
| P1–P5 | Rename the clashing symbols. Add the Lemma 4.2 figure, the name for Lemma 4.1, the padding sentence and the one-line remark before Lemma 8.1. |

---
Supporting files are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/B-b-moduli-compactness-geometer/scratch/:
- code/geo.py (Table 2, C_*, the πe^{3D}/A range, ℓ_{2,3}, h_m, Jørgensen separation)
- code/chk.py (Lemma A.2, b_l and a_l, the enveloping check, the trace identity, the Proposition 8.6 bound)
- img/ (rendered pages)
- ms.txt (text extraction)
