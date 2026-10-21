<!-- Blind check: parametric heat expansion (Lemma C.1 of Paper A): returned text saved verbatim; the reviewer could not write files -->

**Blind referee report: Lemma `lem:param` in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/main/scratch/param_appendix.tex**

I read only that file. My check script is /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/main/scratch/blind-param/checks.py. It covers the Beta induction, the parity claim with a generic non-symmetric phase, the degree bound 3n, and a flat rotation with and without a cutoff. Every check passed.

**Step 1 (geometry): CORRECT, with one wording error and one small gap.**
- The bounds in eq:dsq hold:
  - The lower bound follows from comparing metrics: d_ε ≥ √c_0 |x−y|.
  - The bound on ∂_ε^i d² follows from second-order vanishing at the diagonal, Taylor's formula, and bounds that are uniform on [−1,1]×compact. Outside K_0 + B_1, d² = |x−y|² does not depend on ε.
- (a) The sentence "for x∉K_0 and |v|≤1 it is (ε,x,x+v)" is false when x is within distance 1 of K_0, because the segment can enter K_0. It should read "dist(x,K_0)≥1". This is also what makes the compact set closure(K_0+B_1) the right one.
- (b) "y=exp_x v for a unique v" should read "for a unique v with |v|<r" for a uniform r. Minimality needs one more line:
  - The inverse function theorem makes exp_x a diffeomorphism from B_r(0) onto its image, uniformly in (ε,x). By the Gauss lemma, radial geodesics of length < r are then minimising.
  - Every curve shorter than √C_0 ρ stays inside that image. Choose ρ so that √C_0 ρ < r·√c_0.

**Step 2 (parametrix with ε-derivatives): CORRECT.**
- With Δ the positive Laplacian, the transport identity Q = G(ζ t^N Δu_N + F) is correct.
- The Euclidean cutoff ζ(|x−y|) does not depend on ε. This is a good choice and it is used correctly.
- Each ∂_ε of e^{−d²/4t} produces O(s) with s = |x−y|²/t. The bound (1+s)^i e^{−c_1 s/4} ≤ C e^{−c_1 s/8} then gives eq:EQ.
- On ρ/3 ≤ |x−y| ≤ 2ρ/3 the F-terms are O(t^{-3} e^{-c/t}), so absorbing them into t^{N−1} is fine. The stated "Ct^{-2}" for F is conservative (the actual order is t^{-1}) and harmless.
- u_j is bounded uniformly because u_0 = 1 and u_j = 0 (j ≥ 1) where the metric is flat.
- Wording: the "I" in "for i≤I" is never defined.

**Step 3 (Volterra series and H = h): the ε-estimates are CORRECT; there is a GAP in regularity and identification.**
- **Induction checked explicitly.** The step needs C^{m+1}V^m/(m−1)! · B(N,mN) ≤ C^{m+1}V^m/m!, that is, m·B(N,mN) ≤ 1.
  - This holds because B is decreasing in its first argument, so B(N,mN) ≤ B(1,mN) = 1/(mN) ≤ 1/m for N ≥ 1.
  - Numerically, max_m m·B(N,mN) is 1 for N=1, 1/6 for N=2 and 1/30 for N=3.
- The Leibniz expansion has (2m−1)^i ≤ (2m)^i terms. Using |∂_ε^k σ| ≤ Cσ (since σ ≥ c > 0), each term is dominated by the same majorant kernel.
- This gives |∂_ε^i Φ| ≤ C t^{N−1}, and then |∂_ε^i(H−E)| ≤ C∫_0^t s^{N−1} ds = C t^N/N. Correct.
- **GAP 1: regularity in x and t.**
  - The text says "same estimates for x- and t-derivatives … show H is smooth". For a fixed N the Levi construction only gives finite regularity. For example, ∂_x² of E#Φ requires moving derivatives onto Φ, because ∂_x²E(t−s) integrates to (t−s)^{-1}, which is not integrable in s.
  - The standard statement (Berline–Getzler–Vergne, Thm 2.30) gives H ∈ C^l when N is large relative to n/2 + l/2. With n = 2, N = 2 is borderline for C^{2,1}.
  - Fix: take N ≥ max(L,3). Prove, or cite BGV Thm 2.30 / Rosenberg for, only the C^{2,1} regularity and superexponential decay that the uniqueness argument uses. Smoothness of H then follows a posteriori from H = h.
  - Citing Donnelly for these x,t estimates is weak. BGV is the precise reference.
- **GAP 2: uniqueness argument.** Two small points need justification:
  - (i) "∫H f → f" must hold in L², not just pointwise. This follows from uniform convergence on compacts plus the uniform superexponential tail.
  - (ii) u is C¹ into L² with u' = −Δ_ε u. Differentiation under the integral is justified by the ∂_t bounds with decay.
  - The energy identity is taken in L²(dA_ε). The domain H²(R²) is correct, since the metric is Euclidean outside K_0 and uniformly elliptic.

**Step 4 (Laplace method and parity): CORRECT, with one gap.**
- The substitution x = sz gives dx = t dz, so I_j = t∫F_j dz. This is correct.
- **Integral formula for Ψ.** It is valid because φ ≥ 0 has a minimum at 0, so dφ(0) = 0. This holds even without the isometry hypothesis.
- **Degree bound.** ∂_s^n Ψ has degree n+2 in z and ∂_ε adds degree at most 2, so the total is ≤ 3n + 2i. Symbolically, ∂_s^n F(0,z)e^{Ψ_0} has degree exactly 3n for n = 1..5 with a generic phase.
- **Parity.** F_j(ε,−s,z) = F_j(ε,s,−z) is a purely formal identity: a_j(−sz) = a_j(s(−z)) and φ(−sz)/s² = Ψ(s,−z). So odd s-derivatives at s = 0 are odd in z and β_{j,odd} = 0. Verified symbolically for n = 1..4 with non-even φ and a.
- **Power counting.** Taylor to order 2L gives O(s^{2L}) = O(t^L), so I_j = Σ_{k<L} β_{j,2k} t^{k+1} + O(t^{L+1}). Hence t^{j−1}I_j = Σ_k β_{j,2k} t^{j+k} + O(t^{j+L}). With N = L, every term with j+k ≥ L is O(t^L). This gives c_k = (4π)^{-1}Σ_{j+k'=k} β_{j,2k'} with error t^L = t^{L−d}, d = 0. Correct.
- **Identity case.** T = Σ_{k≤N} c_k t^{k−1} + O(t^N). With N = L, the leftover c_L t^{L−1} is O(t^{L−1}) = O(t^{L−d}), d = 1. Correct, and with room to spare.
- **Flat sanity check.** ∫h_t(x,Rx)dx = 1/(4 sin²(ϑ/2)), which equals (4π)^{-1}β_{0,0}. I confirmed this numerically for ϑ = 1.1. With a cutoff χ, the difference from c_0 decays like e^{−c/t}: −3.8e−2, −1.0e−3 and −9.1e−6 at t = 0.05, 0.02 and 0.01.
- **GAP 3: wording that hides a real point.** "Both are smooth" is wrong for φ_ε. φ_ε is only known to be smooth on |x| < ρ/C_ϑ, since d² is smooth only for |x−y| < ρ. So Ψ_ε is defined and smooth only on {|sz| < ρ/C_ϑ}.
  - F_j is still C^∞ on [−1,1]×R², because a_j(ε,sz) vanishes for |sz| ≥ 2ρ/(3C_ϑ). It should be defined as a_j·e^{−Ψ} there and 0 elsewhere.
  - The polynomial bounds should be stated on the support of a_j(ε,sz).
- **GAP 4: identification with Donnelly's B_k(ε).** Uniqueness of asymptotic coefficients identifies c_k with Donnelly's coefficient only if both are expansions of the same quantity. Donnelly works on a closed manifold; here the manifold is R². A locality step is needed. Fix:
  - c_k depends only on the jets at 0 of the metric (β_{j,n} uses only the s-jets at s = 0, and χ = 1 and ζ = 1 near 0). So c_k does not depend on χ, ζ or ρ.
  - Replace g_ε outside a large ball by a rotation-invariant cap, giving an R-invariant metric on S².
  - The same construction shows h_{S²} − E = O(t^N) on the ball. So the localised integrals near 0 agree to O(t^N).
  - Donnelly's trace expansion localises at the fixed points 0 and the antipode. Its contribution at 0 is therefore c_k.
  - Alternatively, note that Donnelly's B_k are defined by exactly this Laplace-method computation on the u_j.
- The last assertion, about ∂_ε^i c_k(0), follows correctly by setting ε = 0 in the ∂_ε^i estimate.

**Bookkeeping (d and N = L): CORRECT, with one wording conflict.**
- "fix N≥2" conflicts with "N=L" when L ∈ {0,1}. Use N = max(L,2), or max(L,3) to fit Gap 1.
- Taking N larger is harmless. The extra terms j > L contribute O(t^{j−1+1}) = O(t^L) in the rotation case and O(t^{L−1}) in the identity case.

**Wording errors**
1. Step 1: "x∉K_0" should be "dist(x,K_0)≥1".
2. Step 1: "unique v" should be "unique v with |v|<r".
3. Step 2: I is undefined. Say "fix I; constants depend on I".
4. Step 2: "fix N≥2" versus "N=L" in Step 4. Use N = max(L,2) or larger.
5. Step 2: the bound Ct^{-2} on F is not sharp (it is t^{-1}). Harmless, but it reads as if derived.
6. Step 3: "∫H f → f" should say "in L²". "Hence u … lies in H²" needs the derivative decay that comes from Gap 1.
7. Step 4: "Both are smooth" is false for φ_ε globally; it is smooth only on |x| < ρ/C_ϑ. Ψ_ε and F_j are "C^∞ for s∈[−1,1]" only once F_j is extended by 0.
8. Step 4: "as 0 is fixed by R" is a weak justification. The real reason dφ(0) = 0 is that φ ≥ 0 and φ(0) = 0.
9. Lemma statement: the hypothesis that R is an isometry of every g_ε is used only to identify c_k with Donnelly's B_k. The expansion itself does not need it. Say so, or move the hypothesis to the last sentence.

**Overall verdict: minor revision.** The analytic core is sound and I verified it: the ε-uniform parametrix bounds, the Beta/factorial Volterra induction, the Laplace expansion with parameter, the parity argument and the power counting. None of the problems is an ERROR. What a strict AGAG referee would require is:
- the regularity and identification of H stated with the correct N-dependence and a precise reference (BGV Thm 2.30), together with the L² details;
- a locality sentence that transfers Donnelly's closed-manifold coefficients to R²;
- the domain of smoothness of φ and Ψ corrected;
- the wording fixes listed above.
