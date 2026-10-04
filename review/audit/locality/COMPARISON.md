# Locality: comparison of the blind review with the existing proofs

This compares `review/audit/locality/REVIEW.md` (blind phase, grades frozen) with
`theory/locality/proof.md`, `theory/locality/attack-log.md` and `theory/locality/check_locality.py`.
All three were read only. Line numbers refer to `proof.md`.

## Resolution of the four questions

**(i) Decay order on the spectral side of Lemma 3.2: it is 3, so the requirement is met.**
Lines 297–309 bound the difference, not h_R itself. With f_R = g_t(1−χ(·/R)) they get
|h_R(r_j) − h_t(r_j)| ≤ ε_R min(1, |r_j|^{−3}), where ε_R = max(‖f_R‖₁, ‖f_R‴‖₁) → 0. They then need
Σ_j min(1, |r_j|^{−3}) < ∞. Since |r_j|^{−3} = (λ_j − 1/4)^{−3/2}, this sum is finite under N(Λ) = O(Λ).

This is a different but equivalent route to mine. I dominated h_R uniformly with order 4. They use
order 3 on the difference and let ε_R → 0, so the difference goes to 0 directly and needs no
dominated convergence. The failure mode I flagged (order 2) does not occur.

Two smaller points in the same paragraph:
- The identity-term estimate ∫|r tanh(πr)||h_R − h_t| ≤ 2‖f_R‖₁ + 2‖f_R‴‖₁ is valid but generous; ‖f_R‖₁ + 2‖f_R‴‖₁ suffices. Harmless.
- "The finitely many λ_j < 1/4" is asserted without a citation. Finiteness follows from discreteness (DGGW p. 2) or from the Weyl bound used two lines later. Cosmetic.

**(ii) Circularity: not real as written.** Line 309 says "by Theorem 1 (Z(s) ~ Area/4πs)".
- Theorem 1 has Proof A (DGGW Thm 4.8 with Donnelly as restated there, lines 71–110) and Proof B (Uçar). Neither uses Theorem 3.1.
- Lines 125–127 state explicitly that Proof C "uses from outside the trace formula only the a priori Weyl bound … taken from the leading term of Theorem 1 (i.e. from [DGGW] Thm 4.8 at order t^{−1})".
- The attack log, finding 2, records that this dependence was added on purpose.

So the dependency graph is DGGW Thm 4.8 → Weyl bound → Lemma 3.2 → Theorem 3.1 → Proof C. That graph is acyclic. The circularity concern from the blind phase is resolved.

One residual imprecision remains. The sentence at line 310, "Lemma 3.3 … is purely geometric, so there is no circularity", addresses only Lemma 3.3. "By Theorem 1" at line 309 should read "by Theorem 1, Proof A ([DGGW] Thm 4.8 at order t^{−1})", so that a reader of Lemma 3.2 does not have to find lines 125–127.

The torsion-free-cover alternative in the text needs Selberg's lemma, which was not fetched. The window-function argument in REVIEW.md (P2, alternative 1) uses only DS eq. (1) and is a fetched-sources-only replacement, if one is wanted.

**(iii) Definitions of the systole and of w.**
- *Systole.* Theorem 3.4 still says "the length of the shortest closed geodesic" (line 349). Throughout proof.md, closed geodesics are DS's periodic orbits, which are in bijection with hyperbolic conjugacy classes (line 263, [DS p. 3]). DS p. 2 says such a geodesic "may pass through cone points". Prop 2.2 (lines 199–203) explicitly treats the doubled segment between two order-2 points, of length 2d, as a closed geodesic. The proof of 3.4(b) works with the class-counting functions N_i. So the intended definition is the one I asked for, and the proof is consistent with it. Only the statement lacks the explicit phrase. My MINOR fix stands as a clarification.
- *w.* Line 420 defines w_O(L) = Σ_{[γ]: ℓ(γ)=L} ℓ(γ_0), a sum over conjugacy classes. This is exactly my correction: a self-inverse class through two order-2 points counts once. The definition sits just before Theorem 3.5, outside the extracted statement, so LO.11's "undefined w" was an extraction artefact. In LO.10, line 400 uses a bare scalar w in "w/(2 sinh(ℓ/2)√(4π))", which is still undefined there. It should read |w_1(ℓ) − w_2(ℓ)|.

**(iv) Wrong, missing or overstated steps.** None that affects a statement. The full list is in the per-item section below. The most substantive item is a defect in my own blind review, not in proof.md:
- My LO.4 proof assumed that every length s > 0 is realised by a cutting geodesic. The fetched Thurston text does not state the ranges of the parameters. The existing proof avoids this assumption (lines 191–197): it uses only that Thurston's parameter map is a continuous injection from a space homeomorphic to ℝ^d, so by invariance of domain the ℓ_c-projection contains an open interval. That is the correct route.
- The same over-claim underlies my LO.10 suggestion to drop the hedge "in which the systole varies". I withdraw that suggestion. The hedge is correct as written, and the attack log lists non-constancy of the systole as an open point.

## Per item

| item | (a) route vs mine | (b) discrepancies |
|---|---|---|
| LO.0 | same (Gauss–Bonnet, Thurston p. 312, DS Thm 3.2 p. 5) | none |
| LO.1 | Proof A is new to me: locality and universality of Donnelly's b_k, which settles locality without computing constants. Proof B (Uçar) as cited. Proof C is the same as mine (trace formula plus term-by-term expansion with the bound \|e^{−x} − Σ_{j<N}(−x)^j/j!\| ≤ x^N/N!) | Coverage differs. Their checks reach ν ≤ 15 for α and ν ≤ 5 for β, with m ∈ {2,3,4,5,6,8,12}, compared against `numerics/theory.py`. Mine reach k ≤ 7, m = 2..13, against Uçar (4.25)/(4.33) implemented directly from the fetched source, plus DGGW (5.7), DGGW (5.10) and Schueth Thm 4.1. The two sets of checks agree where they overlap. Their Fermi–Dirac moment (1−2^{−2k−1})(−1)^k B_{2k+2}/(4(k+1)) equals mine. Proof A rests on Donnelly as restated in DGGW §4.1 (the accepted standing gap). Proof C closes that gap for the cone constants at all orders |
| LO.2 | same quote and page | none. The existing text also quotes the p. 315 sentence verbatim, with the exception "A(2,2; )" and [sic] |
| LO.3 | same | none. Their check_locality (C) tests only homogeneous and one mixed multiset per n; my enumeration is exhaustive for m ≤ 12. Same conclusion |
| LO.4 | different: invariance of domain on Thurston's parameter map plus countable length sets. Mine: every s > 0 realised plus countable length sets | **My proof over-claimed**, as described under (iv); theirs is correct. The degenerate piece (0;2,2,2,3) / (0;2,2,2,2,2) is handled in both, through the length 2d |
| LO.5 | same | none |
| LO.6 | same (DS eq. (1), elliptic classes R_c^l, DS wave normalisation, Marklof misprint) | none |
| LO.7 | different estimates, same structure; see (i) and (ii) | residual: the citation "Theorem 1" should name Proof A / DGGW; no citation for finitely many λ < 1/4; the identity-term constant is generous |
| LO.8 | identical (generic base point, Dirichlet domain, packing) | none. The existing proof already requires x_0 fixed by no non-trivial element |
| LO.9 | (a), (c) same. (b) different. They bound each H_i with ℓ_i, using −φ′ ≥ 0 for t ≤ ℓ_i²/2, then complete the square with the erfc bound, then replace ℓ_i by ℓ using monotonicity in ℓ_i. That last step is exactly what needs t ≤ ℓ²/(2(1+ℓ)), because ℓ/(2t) ≥ 1/ℓ + 1. I integrated from ℓ directly and closed with the exact identity −D′ = Le^φ + 2t²e^φ/(L−t)² | No error. The stated range is natural for their route; mine shows it can be relaxed to t < min(ℓ, ℓ²/(2−ℓ)). Their step-3 integral bound is analytic in the text (erfc(x) ≤ e^{−x²}/(x√π), checked by hand: it gives 2tℓ/(ℓ−t)·e^{ℓ/2−ℓ²/4t}, the same as my D(ℓ)), but the script spot-checks it only by quadrature at 40 random points. My `check_thm34.py` certifies it symbolically. The wording issues (systole definition; what "computable from the spectrum at t_1" needs) remain as in REVIEW.md |
| LO.10 | same argument | w is a bare scalar at line 400. **My suggestion to drop the hedge is withdrawn** (see (iv)) |
| LO.11 | same; the remainder is bounded by the 3.4(b) argument with L′ in place of ℓ_i, where I used a monotone-in-t tail. Equivalent | w is defined at line 420, as I asked; the statement extract simply omitted it. Lines 440–446 also justify Z_1 ≡ Z_2 ⇔ isospectral ⇔ w_1 ≡ w_2 within a signature, beyond what I checked. Correct |
| DF.3 | same (T(O) is a point); the existing text also cites Troyanov | none |
| DF.5 | same | none; line 234 notes that it is now unconditional |

## (c) Grade addenda

REVIEW.md grades stay unchanged, as instructed. Addenda:

1. **LO.7 (MINOR, unchanged).** Both concerns were resolved in the existing proof's favour: decay order 3 (question (i)) and no real circularity (question (ii)). The grade stays MINOR only for citation precision, "Theorem 1" → "Theorem 1, Proof A ([DGGW] Thm 4.8, order t^{−1})". **Final P2 verdict: SOUND.** The repair I asked for is already substantively present; one citation should be sharpened.
2. **LO.4 (NONE, unchanged).** Correction to my own report: replace "for every s > 0 there is O_s" with "the ℓ_c-coordinate ranges over an open interval (invariance of domain applied to Thurston's parameter map)". The existing proof already does this.
3. **LO.10 (MINOR, unchanged).** Fix 2 is withdrawn. Fix 1 (define w as |w_1(ℓ) − w_2(ℓ)|) stands.
4. **LO.11 (MINOR, unchanged).** The defect lies in the extracted statement, not in proof.md: w is defined at line 420. Strictly, NONE against the source; MINOR only if the statement is ever quoted without line 420.
5. **LO.9 (MINOR, unchanged).** Wording only. The systole definition matches in substance (question (iii)).

No new SERIOUS or FATAL items.
