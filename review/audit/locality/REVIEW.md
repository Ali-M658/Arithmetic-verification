# G5 referee report: group LOCALITY

Scope: items LO.0–LO.11 of `review/audit/statements/locality.md`, plus DF.3 (prop:rigidity) and
DF.5 (prop:Kinf). Each result was re-derived from its statement and the fetched sources only; the
existing proofs were not consulted. Scripts (run from the repository root, nonzero exit on failure):

| script | output | covers |
|---|---|---|
| `review/audit/locality/check_expansion.py` | `check_expansion.txt` | LO.1, LO.6: small-t expansion of the identity and elliptic terms vs LO.1, Uçar (4.33)/(4.35), DGGW (5.7)/(5.10), Schueth Thm 4.1 |
| `review/audit/locality/check_P2.py` | `check_P2.txt` | LO.6, LO.7: Fourier normalisation, g_t, spectral/elliptic/hyperbolic convergence, window test function |
| `review/audit/locality/check_thm34.py` | `check_thm34.txt` | LO.8–LO.11: Lemma 3.3 inequalities, Thm 3.4 (b),(c) chain, boundary t, LO.10 limit, Thm 3.5 |
| `review/audit/locality/check_teich.py` | `check_teich.txt` | LO.0, LO.3, LO.5, DF.3: signature bookkeeping, boundary signatures |

Every identity marked [exact] is checked symbolically or in rational arithmetic; mpmath appears
only in lines labelled "sanity".

## Summary table

| item | statement | grade | one-line reason |
|---|---|---|---|
| LO.0 | setting, Area = −2πχ | NONE | Thurston 13.3.5 + sentence (p. 312), DS Thm 3.2 (p. 5); sign checked |
| LO.1 | Theorem 1, signature locality, α_k, β_k(m) | NONE | re-derived from the trace formula; α_k (k≤7) and β_k(m) (m≤13, k≤7) agree exactly with Uçar, DGGW, Schueth |
| LO.2 | Thurston Cor 13.3.7 as quoted | NONE | verbatim; electronic p. 318, original 13.27 confirmed |
| LO.3 | Prop 2.1, dim T = 6g−6+2n | NONE | follows from Cor 13.3.7; 0 only for (0;3); (1;) is Euclidean |
| LO.4 | Prop 2.2, uncountably many classes | NONE | short proof via the countable length spectrum, given below |
| LO.5 | Cor 2.3, K_iso = ∞ | NONE | Theorem 1 + Prop 2.2; triangle case from DF.3 |
| LO.6 | Theorem 3.1 (heat trace formula) | NONE (statement) | every term and normalisation re-derived; see P2 |
| LO.7 | Lemma 3.2 (admissibility of h_t) | MINOR | **SOUND WITH REPAIR**: take the Weyl bound from DGGW Thm 4.8 or the self-contained window argument, not from "Theorem 1"; the decay order must be ≥ 3 |
| LO.8 | Lemma 3.3 (counting) | NONE | independent packing proof; base point must avoid the cone points |
| LO.9 | Theorem 3.4 (a),(b),(c) | MINOR | constants and range re-derived exactly; range is sufficient but not sharp. Wording: "systole" must include geodesics through cone points; (c) also needs ℓ, A and σ |
| LO.10 | the t^{-1/2} cannot be dropped | MINOR | true; w is undefined in the excerpt (should be \|w_1(ℓ)−w_2(ℓ)\|); the hedge "in which the systole varies" can be removed |
| LO.11 | Theorem 3.5 | MINOR | true; the statement must define w_i(L) (sum of ℓ(γ_0) over hyperbolic conjugacy classes of length L) |
| DF.3 | prop:rigidity | NONE | T(O) is a point for (0;p,q,r) (Cor 13.3.7) |
| DF.5 | prop:Kinf | NONE | pigeonhole on two non-isometric representatives |

No FATAL or SERIOUS findings.

---

## External inputs used (verbatim, with location)

- **DS eq. (1), p. 3.** Σ_n h(r_n) = μ(F)/4π ∫ r h(r) tanh(πr) dr + Σ_{P hyp} ln N(P_c)/(N(P)^{1/2}−N(P)^{−1/2}) g[ln N(P)] + Σ_{R ell} 1/(2m(R) sin θ(R)) ∫ e^{−2θ(R)r}/(1+e^{−2πr}) h(r) dr, "where h is any entire function of uniform exponential type and h(r) = h(−r)"; "The function g is the Fourier transform of h and thus is a compactly supported smooth function"; "θ(R) = πl/m(R) where 1 ≤ l ≤ m(R) − 1"; λ_n = 1/4 + r_n² (DS write the eigenvalues as λ_n²).
- **DS normalisation, p. 4.** For the wave trace (h(r) = cos(tr)): "g[ln N(P)] = 1/2[δ(ln N(P) − t) + δ(ln N(P) + t)]". This fixes g(u) = (1/2π)∫h(r)e^{−iru}dr, i.e. h(r) = ∫g(u)e^{iru}du (checked in `check_P2.py`: the 1/2 is reproduced exactly; the convention without 1/2π would give π instead). The same normalisation is Marklof (69), p. 13. The first term of DS (2), p. 4, is the derivative of μ/(4π sinh(t/2)) (exact check).
- **DS p. 4.** ψ_m(r) "behave asymptotically like (2m sin π/m)^{−1} e^{−2πr/m}".
- **DS Thm 3.2, p. 5.** ∫_O K dA = 2πχ(O).
- **DGGW p. 2.** "In the case of closed orbifolds, the Laplacian has a discrete spectrum."
- **DGGW Def 4.7 (iii), Thm 4.8, (4.9), p. 17.** The heat trace is asymptotic to I_0 + Σ_N I_N/|Iso(N)|, I_0 = (4πt)^{−dim O/2} Σ a_k t^k, "a_0 = vol(O)"; I_N = (4πt)^{−dim N/2} Σ t^k ∫_N b_k(N,x).
- **DGGW Prop 5.5 and (5.7), p. 24.** Degree-zero term χ(O)/6 + Σ (m_i²−1)/(12m_i).
- **DGGW (5.9)–(5.10), p. 26.** Cone term in degree one: R_1212 (m⁴+10m²−11)/(360m).
- **Uçar Thm 4.11 (p. 127), (4.25) (p. 134), (4.33), Thm 4.20 (i) and (4.35) (p. 137), Thm 4.20 (ii) (p. 138).**
- **Schueth Thm 4.1, p. 14.** a_2({p}) = [(k⁵−1/k)/2520 + (k³−1/k)/720 + (k−1/k)/180] K² − [...] ΔK.
- **Thurston, p. 312.** 13.3.5 ∫K dA = 2πχ(O); "If O is elliptic or hyperbolic, then area (O) = 2π|χ(O)|." Thm 13.3.6: hyperbolic iff χ(O) < 0.
- **Thurston, pp. 315–318, Cor 13.3.7.** Pieces "have hyperbolic structures parametrized by the lengths of their boundary components"; Cor 13.3.7 as quoted in LO.2; proof: "The lengths of the arcs, and lengths and twist parameters for simple closed curves form a set of parameters".

---

## P2 verdict: Lemma 3.2 / Theorem 3.1

**Verdict: SOUND WITH REPAIR.** Theorem 3.1 is true as stated. The extension from DS's class to
h_t goes through. The repair concerns where the a-priori eigenvalue count comes from, plus one
quantitative point that the proof must get right (decay of order > 2).

### Setup and normalisation

h_t(r) = e^{−t(1/4+r²)}. In DS normalisation, g_t(u) = (1/2π)∫h_t e^{−iru}dr =
e^{−t/4}e^{−u²/4t}/√(4πt), and ∫g_t e^{iru}du = h_t, both exact (`check_P2.py`). With
g_R = g_t·χ(·/R), the function g_R is even, C^∞ and supported in [−2R,2R]. So h_R(z) = ∫g_R(u)e^{izu}du is entire and even, and
|h_R(z)| ≤ ‖g_t‖₁ e^{2R|Im z|}: exponential type ≤ 2R. Integrating by parts k times,
|h_R(r)| ≤ ‖g_R^{(k)}‖₁ |r|^{−k}. Expanding g_R^{(k)} by Leibniz gives
‖g_R^{(k)}‖₁ ≤ Σ_j C(k,j) ‖g_t^{(k−j)}‖₁ ‖χ^{(j)}‖_∞ R^{−j}, which is bounded uniformly for R ≥ 1. Here
g_t^{(j)} = (polynomial)·g_t (exact), so every norm is finite. Hence

  (★) |h_R(r)| ≤ C_k(t)(1+|r|)^{−k} for real r, all k, uniformly in R ≥ 1; and h_R → h_t pointwise,
  since |h_R(r)−h_t(r)| ≤ ∫_{|u|>R} g_t → 0 uniformly in r.

So h_R lies in DS's class, and DS (1) holds for h_R with transform g_R. Each claim of LO.7's
statement is correct.

### Term by term

1. **Identity term.** |r tanh(πr) h_R(r)| ≤ C_3|r|(1+|r|)^{−3} is integrable. Dominated convergence gives
   ∫ r tanh(πr) h_R → ∫ r tanh(πr) h_t, and the limit integral converges absolutely (Gaussian).
   As a cross-check, tanh(πr) = 1 − 2/(1+e^{2πr}) gives I(t)·4π/A = e^{−t/4}[1/t − 4∫_0^∞ r e^{−tr²}/(1+e^{2πr})dr].
   Its expansion reproduces LO.1's α_k exactly for k ≤ 7 (α = 1, −1/3, 1/15, −4/315, …).
2. **Elliptic terms.** k_θ(r) = e^{−2θr}/(1+e^{−2πr}) satisfies 0 < k_θ ≤ 1 exactly: for r ≥ 0 the
   bound is e^{−2θr} ≤ 1; for r < 0, k_θ = e^{(2π−2θ)r}/(1+e^{2πr}) ≤ 1. The exact decay is
   k_θ ~ e^{−2θr} as r → +∞ and ~ e^{−(2π−2θ)|r|} as r → −∞. With θ = πl/m the rate is ≥ 2π/m. The even part is
   cosh((π−2θ)r)/(2cosh πr), and k_θ(−r) = k_{π−θ}(r) (l ↔ m−l), so E_m is real. All of this is exact; it agrees
   with DS's ψ_m asymptotics. Domination is |k_θ h_R| ≤ C_2(1+r²)^{−1}. The elliptic weight 1/(2m sin θ) is
   independently confirmed: the t⁰ coefficient of E_m is exactly (m²−1)/(12m) = DGGW (5.7). Doubling the
   weight would contradict (5.7). The t¹ coefficient is −(m⁴+10m²−11)/(360m) = DGGW (5.10) with R_1212 = −1,
   and the t² coefficient equals Schueth Thm 4.1 at K = −1.
3. **Hyperbolic sum.** g_R(ℓ) = g_t(ℓ)χ(ℓ/R), so 0 ≤ g_R ≤ g_t, and g_R(ℓ) = g_t(ℓ) for ℓ ≤ R. Domination
   needs Σ_{[γ]} ℓ(γ_0)/(2 sinh(ℓ/2)) g_t(ℓ) < ∞. This follows from Lemma 3.3 (proved independently below,
   using geometry only): N(L) ≤ (π/A)e^{L+3δ}. By Stieltjes, the sum is ≤ (1−e^{−ℓ_sys})^{−1}(4πt)^{−1/2}·(π e^{3δ}/A)·∫_{ℓ_sys}^∞ e^{L/2−L²/4t}(L/2+L²/2t−1)dL < ∞
   (exact integrand in `check_P2.py`). The weight identity ln N(P_c)/(N^{1/2}−N^{−1/2}) = ℓ(γ_0)/(2 sinh(ℓ/2)) is exact.
4. **Spectral side, imaginary r_j.** By DGGW p. 2 the spectrum is discrete, so only finitely many λ_j lie
   in [0, 1/4). For these, r_j = iy with 0 < y ≤ 1/2, and h_R(iy) = ∫g_R e^{−yu}du → ∫g_t e^{−yu}du = h_t(iy) by
   dominated convergence. The dominating function is g_t e^{|u|/2}, with ∫ g_t e^{|u|/2} = 1 + erf(√t/2) (exact).
   λ = 0 gives r = ±i/2 and h_t(i/2) = 1 (exact). In general h_t(r_j) = e^{−tλ_j} for real and imaginary r_j.
5. **Spectral side, real r_j.** By (★) with k = 4, |h_R(r_j)| ≤ C(λ_j + 3/4)^{−2}. This is summable
   **provided N(Λ) = #{λ_j ≤ Λ} = O(1+Λ)**: by Stieltjes, Σ(1+λ_j)^{−2} ≤ 3C. Dominated convergence then gives
   Σ h_R(r_j) → Σ e^{−tλ_j} = Z(t).
   *Quantitative point (failure mode to check against the existing text):* the order of decay must exceed 2.
   With λ_j = j, Σ(1+r_j²)^{−1} = ∞ while Σ(1+r_j²)^{−2} = ψ′(7/4) < ∞ (exact). A proof that only uses
   |h_R(r)| ≤ C/(1+r²), i.e. two integrations by parts, does not close.

### The circularity question

The only non-trivial input is the a-priori bound N(Λ) = O(Λ).

- **Is it circular to take it from Theorem 1?** Only in the narrow sense. If "Theorem 1" in the proof of
  Lemma 3.2 means a theorem whose proof (Proof C) uses Theorem 3.1, then the citation is circular as
  written. The needed fact is only the *leading* term Z(t) ~ Area/(4πt). That term is not specific to Proof C.
- **Is it legitimate to take it from DGGW?** Yes. DGGW Thm 4.8 with Def 4.7(iii) ("a_0 = vol(O)") gives
  Z(t) ~ vol(O)/(4πt) as t → 0. In dimension 2 the singular strata are points and contribute O(1) (DGGW (4.9), §5.6).
  This rests on Donnelly and the DGGW parametrix, not on any trace formula. Then for t ≤ 1, Z(t) ≤ C/t, and
  N(Λ) ≤ e^{tΛ}Z(t) at t = 1/Λ gives N(Λ) ≤ eCΛ. No Tauberian theorem is needed. DS p. 5 also points to
  Weyl's law for orbifolds (Farsi), which is not fetched and not needed.
- **Self-contained alternative 1 (window test function, DS (1) only).** Take φ ∈ C_c^∞, even, φ ≥ 0,
  φ ≢ 0, supp φ ⊂ [−1,1], and h_0 = (φ̂)². Then h_0 is even and of Paley–Wiener class, h_0 ≥ 0 on ℝ, and
  h_0(s) ≥ c := (cos 1·∫φ)² > 0 for |s| ≤ 1. Set h_T(r) = h_0(r−T) + h_0(r+T). This is even, entire, of exponential
  type, and its transform is 2cos(Tu)g_0(u) (exact): same compact support, |g_T| ≤ 2|g_0|. DS (1) for h_T gives:
  - identity side ≤ (A/4π)·2∫(|s|+T)h_0(s)ds = O(1+T);
  - elliptic side ≤ Σ 1/(2m sinθ)·2‖h_0‖₁ = O(1), since |k_θ| ≤ 1;
  - hyperbolic side: a fixed finite sum (classes with ℓ ≤ diam supp g_0, finite by Lemma 3.3);
  - the finitely many imaginary r_j contribute h_T(iy) = 2 Re h_0(T+iy), bounded by 2∫|g_0|e^{|u|/2}.

  The remaining terms h_T(r_j), r_j real, are ≥ 0, and the series converges because DS (1) asserts an
  equality with a finite right-hand side. Therefore #{j : |r_j − T| ≤ 1} ≤ c^{−1}·O(1+T). Summing over windows T = 1, 3, 5, … gives
  #{r_j ∈ [0,T]} = O(T²), i.e. N(Λ) = O(Λ). No heat expansion is used.
- **Self-contained alternative 2 (positivity + Fatou).** Choose the cutoff positive definite,
  χ = ψ*ψ̃ with ψ even, C_c^∞ and ‖ψ‖₂ = 1. Then g_R = g_t·χ(·/R) is positive definite (Schur product), so
  h_R ≥ 0 on ℝ. Fatou on the real-r_j terms plus convergence of the finitely many imaginary terms gives
  Z(s) ≤ I(s)+E(s)+H(s) for every s > 0. The right-hand side is O(1/s) as s → 0, because I(s) ~ A/(4πs), E = O(1),
  and H(s) = O(e^{−c/s}) by Lemma 3.3. Hence N(Λ) = O(Λ), and then dominated convergence (step 5)
  upgrades the inequality to equality. This needs a different cutoff from the one fixed in LO.7.
  If LO.7's χ (equal to 1 on [−1,1]) is to be kept, use alternative 1 or the DGGW route.

**Repair to state in the paper.** In the proof of Lemma 3.2, replace "by Theorem 1" with "by DGGW
Thm 4.8 and Def 4.7(iii) (a_0 = vol)", or insert alternative 1, which costs five lines. Make sure the
domination of h_R uses decay of order ≥ 3, not 2. With either repair, Theorem 1 (Proof C) → Theorem 3.1 →
Lemma 3.2 is acyclic.

---

## Item-by-item

### LO.0 (setting): NONE
Gauss–Bonnet with K ≡ −1 gives −Area = 2πχ, so Area = −2πχ (DS Thm 3.2, p. 5; Thurston 13.3.5,
p. 312, "area(O) = 2π|χ(O)|" with χ < 0). Closed orientable hyperbolic 2-orbifolds are Γ\H² with Γ
cocompact Fuchsian (Thurston 13.3.2 and 13.3.6, pp. 310–312). χ(O) = χ(X_O) − Σ(1−1/m_i) agrees with
Thurston's general formula 13.3.4 (no corner reflectors) and DS Def 3.1. Page references verified.

### LO.1 (Theorem 1): NONE
*Independent proof (via the trace formula).* By Theorem 3.1, Z = I + E + H. Lemma 3.3 gives
H(t) = O(e^{−ℓ_sys²/8t}), so H contributes nothing to any order. The identity and elliptic kernels decay exponentially,
so expanding e^{−tr²} termwise gives asymptotic series in integer powers of t. I(t) is
(A/4πt)Σα_k t^k with α_k from μ_j = ∫_0^∞ r^{2j+1}/(1+e^{2πr})dr = (1−2^{−2j−1})(2j+1)!ζ(2j+2)/(2π)^{2j+2}.
E_m(t) is e^{−t/4}Σ_j (−t)^j/j!·Σ_l F^{(2j)}(2πl/m)/(2m sin(πl/m)) with F(a) = 1/(2 sin(a/2)). The csc-power sums are
evaluated exactly (resultant + Newton identities). Results:
- α_k equals the LO.1 formula and Uçar (4.35)/vol at κ = −1, exactly, for k = 0..7;
- β_k(m) equals Uçar (4.33) at κ = −1, exactly, for m = 2..13, k = 0..7. Also β_0 = (m²−1)/(12m) (DGGW (5.7)),
  β_1 = −(m⁴+10m²−11)/(360m) (DGGW (5.10), R_1212 = −1), and β_2 = Schueth Thm 4.1;
- (A/4π)α_1 = χ/6, matching DGGW (5.7).

The c_j and Φ_j bookkeeping is right: c_1 = A/4π, and c_j = α_{j−1}A/4π + Σβ_{j−2}(m_i) for j ≥ 2. "No half-integer powers" is
right: orientable 2-orbifolds have only cone points (DGGW §5.6, p. 24), and Def 4.7(ii) with dim N = 0 gives integer
powers. The trace-formula route also closes the Donnelly dependence of Uçar Thm 4.20(ii) for all k.
*Failure modes tried:* m = 2 (smallest order), large m, and the cases (0;2,3,7), (0;2,2,2,3) and (1;2) through c_1. None found.

### LO.2 (Thurston Cor 13.3.7 as quoted): NONE
The quote matches the fetched text character for character (up to ligatures). The corollary sits on
electronic p. 318, after the "13.27" marker, so "original p. 13.27" is correct. The proof begins on p. 318 as stated.

### LO.3 (Prop 2.1): NONE
For a closed orientable O: χ(X_O) = 2−2g, k = n, l = 0, so −3χ(X_O)+2k+l = 6g−6+2n (valid for χ(O) < 0).
The value 6g−6+2n is even. It is 0 iff (g,n) ∈ {(0,3),(1,0)}, and (1;) has χ = 0, so it is not hyperbolic. g = 0 with n ≤ 2
has χ > 0. Hence among hyperbolic signatures the dimension is 0 exactly for (0;3) and ≥ 2 otherwise. An exact enumeration of
49 407 hyperbolic signatures (g ≤ 3, n ≤ 6, m ≤ 12) confirms this (`check_teich.py`). Boundary cases:
- (0;2,2,2,3): χ = −1/6, dim 2;
- (0;2,2,2,2,2): χ = −1/2, dim 4. This is the case containing Thurston's degenerate piece D(2,2;), the "infinitely thin
  rectangle", p. 317. Its edge length replaces the boundary length as parameter, so the count is unchanged. The result
  agrees with eq:moduli (2n−6 = 4);
- (1;2): dim 2;
- (0;2,2,2,2) and (1;) are Euclidean and excluded;
- the smallest area is (0;2,3,7), with χ = −1/42.

### LO.4 (Prop 2.2): NONE
*Independent proof.* Suppose 6g−6+2n > 0. Thurston's dissection (pp. 314–318) cuts O along at least one
simple closed curve c, or along the doubled arc between two order-2 cone points (the degenerate piece). By Thurston,
p. 315 ("parametrized by the lengths of their boundary components") and the reassembly on p. 318, for every
s > 0 there is a hyperbolic O_s of signature σ in which c is a closed geodesic of length s, or 2× the edge
length in the degenerate case. Each O has a countable length set (Γ is finitely generated, hence countable).
If O_s ≅ X then s ∈ Lspec(X), so each isometry class contains O_s for only countably many s. Since (0,∞) is
uncountable, the O_s fall into uncountably many classes. This argument avoids the mapping class group entirely.
An alternative is Teichmüller space modulo a countable group (Aut of the finitely generated π_1^orb).

### LO.5 (Cor 2.3): NONE
By Theorem 1, H_k(O′) = H_k(O) for all k whenever σ(O′) = σ(O). By Prop 2.2 there is O′ ∈ P of signature σ
not isometric to O, so no k works and K_iso = ∞. For (0;3): DF.3 gives "same signature ⇒ isometric", so the
two defining conditions coincide and K_iso = K_mult for every P. "Not a triangle orbifold ⇔ 6g−6+2n > 0" holds
by Prop 2.1. P_n contains every orbifold of a g = 0, n-cone-point signature, as required.

### LO.6 (Theorem 3.1): NONE (statement)
Everything matches DS (1):
- I has weight Area/4π (μ(F) = Area);
- E_m is the DS elliptic term summed over the m−1 elliptic classes R_c^l, θ = πl/m, of the cone point. These classes are pairwise
  non-conjugate (distinct rotation angles), and distinct cone points give non-conjugate classes;
- H is the DS hyperbolic term with g_t.

All parts converge absolutely (see P2). Positivity of each H-term is clear. *Clarification (not an error):*
when a closed geodesic runs between two order-2 cone points P_1, P_2, the class γ = R_1R_2 satisfies
γ^{−1} = R_1γR_1^{−1}. That is one conjugacy class, i.e. one "oriented periodic geodesic" in DS's sense, not two.
Any later multiplicity count (w, Lemma 3.3) must count such classes once. This occurs whenever there are ≥ 2 order-2
cone points, e.g. (0;2,2,2,3) and (0;2,2,2,2,2).

### LO.7 (Lemma 3.2): MINOR. See the P2 verdict.
The statement is correct. Grade MINOR because the repair is a citation change, or a five-line insertion, plus the
order-of-decay check. It would be SERIOUS only if the t^{−1} heat term had no proof independent of Theorem 3.1.
It has one (DGGW Thm 4.8).

### LO.8 (Lemma 3.3): NONE
*Independent proof.* Fix x_0 ∈ H² **not fixed by any non-trivial element of Γ** (possible: the fixed points
are discrete). Let D be the Dirichlet domain at x_0. Then D is a fundamental domain, Area(D) = A, and for every y ∈ D,
d(x_0,y) = d_O([x_0],[y]) ≤ δ. Given a hyperbolic class, pick p on the axis of a representative and conjugate
so that p ∈ D̄. Then d(x_0,γx_0) ≤ d(x_0,p) + d(p,γp) + d(γp,γx_0) ≤ ℓ(γ)+2δ. Distinct classes give distinct γ.
The tiles γD with d(x_0,γx_0) ≤ L+2δ have disjoint interiors and lie in B(x_0, L+3δ). Hence
N(L)·A ≤ 2π(cosh(L+3δ)−1), and 2π(cosh x−1) ≤ πe^x (exact). *Failure mode:* if x_0 is a cone point, D is a
union of m fundamental domains and the count is off by the factor m, so the generic base point is necessary.
The statement itself is unaffected.

### LO.9 (Theorem 3.4): MINOR
(a) Same signature implies the same A (Gauss–Bonnet) and the same cone multiset. So I_1 = I_2 and E_1 = E_2, hence
Z_1−Z_2 = H_1−H_2. Both H_i ≥ 0, so |H_1−H_2| ≤ max H_i.

(b) *Re-derivation.* Write f(L) = Le^{−L/2}e^{−L²/4t}. Using ℓ(γ_0) ≤ ℓ(γ), 1/(2sinh(L/2)) = e^{−L/2}/(1−e^{−L}) ≤ e^{−L/2}/(1−e^{−ℓ})
and e^{−t/4} ≤ 1, we get H_i ≤ [(1−e^{−ℓ})√(4πt)]^{−1}Σf(ℓ_γ). Next, −f′/f = L/2t + 1/2 − 1/L is increasing in L. At L = ℓ and
t = ℓ²/(2(1+ℓ)) it equals 3/2, and it is larger for smaller t, so −f′ > 0 on [ℓ,∞). Tonelli then gives
Σf(ℓ_γ) = ∫_ℓ^∞(−f′)N_i ≤ (πe^{3δ}/A)∫_ℓ^∞(−f′)e^L. Two exact identities finish the bound:
- −f′e^L = −(Le^φ)′ + Le^φ, with φ = L/2 − L²/4t;
- with D = 2tLe^φ/(L−t): −D′ = Le^φ + 2t²e^φ/(L−t)² ≥ Le^φ, and D(∞) = 0.

Together they give Σf ≤ (πe^{3δ}/A)ℓe^{ℓ/2}e^{−ℓ²/4t}(1+2t/(ℓ−t)). The assembled bound is identical to the stated right-hand side (exact).
*Range:* the proof needs only t < ℓ and t ≤ ℓ²/(2−ℓ) (ℓ < 2). The stated t ≤ ℓ²/(2(1+ℓ)) lies inside both:
ℓ²/(2−ℓ) − ℓ²/(2(1+ℓ)) = 3ℓ³/(2(2−ℓ)(1+ℓ)) and ℓ − ℓ²/(2(1+ℓ)) = ℓ(2+ℓ)/(2(1+ℓ)). So the range is correct but not sharp.
*Boundary and small-systole tests:* the extremal counting function N = Ce^L on [ℓ,∞) gives (Σf dN)/bound between
0.941 and 0.99999998 at ℓ ∈ {1/100, 1/10, 1/2, 1, 2, 5} and t ∈ {t_b, t_b/2, t_b/10}, t_b the boundary. The bound is
never exceeded, and it is essentially sharp for the worst-case counting function.

(c) The term ratio is term(t)/term(t_1) = √(t_1/t)e^{(t_1−t)/4}e^{ℓ²/4t_1}e^{−ℓ²/4t}·e^{−(L²−ℓ²)(1/4t−1/4t_1)} (exact). The last factor is ≤ 1 for
L ≥ ℓ_i ≥ ℓ and t ≤ t_1. Correct.

*Fixes (wording):*
1. Define the systole as min{ℓ(γ): γ ∈ Γ hyperbolic}, i.e. including closed geodesics through cone points. In
   (0;2,2,2,3) the shortest class can be a doubled segment between order-2 points. A systole "among closed
   geodesics avoiding the cone points" can be larger, and then (b) and (c) fail.
2. In (c), "computable from the spectrum at the single time t_1" also needs A and σ (for I and E) and ℓ. Say so.
3. Optionally record that the range in (b) can be relaxed to t < min(ℓ, ℓ²/(2−ℓ)).

### LO.10 (t^{−1/2} cannot be dropped): MINOR
True. If L_* = ℓ, then e^{ℓ²/4t}|Z_1−Z_2| ~ |w_1(ℓ)−w_2(ℓ)|/(2 sinh(ℓ/2)√(4πt)) → ∞. The exact limit is
√t e^{ℓ²/4t}·(main term) → w/(2sinh(ℓ/2)√(4π)). If L_* > ℓ, then sup_t t^{−1/2}e^{−(L_*²−ℓ²)/4t} = ((L_*²−ℓ²)/2)^{−1/2}e^{−1/2} < ∞.
For large t, Z_i → 1, so a global constant exists: the "if L_* > ℓ the constant-C bound holds" clause is right.
The ε-version follows from (b). *Fixes:*
1. Define w as |w_1(ℓ)−w_2(ℓ)|.
2. "Pairs with ℓ_1 ≠ ℓ_2 exist in every signature with dim T > 0 in which the systole varies" is true but
   over-hedged. By the LO.4 construction a cutting geodesic can be made arbitrarily short, so the systole is
   never constant on T when dim T > 0, and the qualifier can be dropped.
3. The T4 example (systole 4b(τ), certified enumeration) depends on numerics outside this group's remit and
   was not checked.

### LO.11 (Theorem 3.5): MINOR
*Proof.* H_1−H_2 = Σ_L (w_1(L)−w_2(L))/(2sinh(L/2))·g_t(L), with w_i(L) := Σ_{[γ]: ℓ(γ)=L} ℓ(γ_0).
- If w_1 ≡ w_2, then Z_1 ≡ Z_2, and the Dirichlet series Σe^{−λt} determines the spectrum.
- Otherwise L_* exists, because the union of two length spectra is discrete. Let L′ be the next length. The remainder
  over the leading term is ≤ e^{−(L′²−L_*²)/8t}·Σ_{L>L_*}|c_L/c_{L_*}|(sinh(L_*/2)/sinh(L/2))e^{−(L²−L_*²)/8t}. The second
  factor is non-increasing as t ↓ 0 and finite at t = 1 by Lemma 3.3, so the remainder is o(1).
- If ℓ_1 < ℓ_2, then w_1(ℓ_1) > 0 = w_2(ℓ_1), so L_* = ℓ.

Exact toy models were run (`check_thm34.py`): ℓ_1 = ℓ_2 with different multiplicities, ℓ_1 ≠ ℓ_2, and a large
weight just above L_*. In each, (Z_1−Z_2)/leading → 1. *Fix:* the excerpt never defines w_i. Add the definition
above, counting classes, so a self-inverse class through two order-2 points counts once.

### DF.3 (prop:rigidity): NONE
Two orbifolds of signature (0;p,q,r) are diffeomorphic as orbifolds: any three points of S² can be moved to
any three. T(O) is homeomorphic to ℝ⁰ (Cor 13.3.7, dim = 6·0−6+6 = 0) and so is a point. The two pulled-back hyperbolic
structures therefore coincide in T(O), and the orbifolds are isometric. Thurston p. 315 says the same for
S²(n_1,n_2,n_3): its structures are parametrised by its (empty) set of boundary lengths. The consequence K_iso = K_mult holds
because the two defining implications coincide.

### DF.5 (prop:Kinf): NONE
Suppose O_1, O_2 ∈ P have signature σ_0 and are non-isometric. For any O of signature σ_0, at least one O_i
is not isometric to O. By thm:locality, H_k(O_i) = H_k(O) for every k, so K_iso = ∞. For the second sentence:
n ≥ 4 with σ hyperbolic gives dim = 2n−6 > 0 (eq:moduli, or Cor 13.3.7), hence two non-isometric members (LO.4).
For non-hyperbolic (0;m_1,…,m_n), e.g. (0;2,2,2,2), M is empty and the claim is vacuous. Correct as stated.
