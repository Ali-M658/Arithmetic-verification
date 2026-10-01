# How precisely must one listen? Stability of the cone orders under errors in the heat coefficients

Scope: closed hyperbolic orbifolds (K = −1) of genus 0 with n cone points of orders
m_1, …, m_n. Manuscript results are referred to by their labels in `theory/audibility/proof.md`:

- Theorem A: injectivity of I_n;
- Theorem B: the linear system M e = b;
- Theorem C: sharpness.

All scripts are in this directory and exit nonzero on any failed assert.

## 0. The answer in physical terms

A heat-trace measurement returns the first few coefficients H₋₁, H₀, H₁, … of
Z(t) = Σ e^{−λ_j t} ~ Σ_ν H_ν t^ν, each with some error. The cone orders sit inside these
numbers in three layers. The question is how large an error each layer tolerates.

1. **Front end (exact, linear, benign).** The coefficients are a fixed triangular linear
   image of I_n = (R, P₁, P₃, …, P_{2n−3}). Undoing it multiplies absolute errors by at most
   2, 14, 498, 4062, … (§2). The review's factors 12, 360, 2520 are only the diagonal of this
   map. *Relative* errors are amplified by factors between 0.02 and 3.7 on every test
   multiset.
2. **The linear system (Theorem B; well conditioned).** The elementary symmetric functions
   come out of a linear solve.
   - Its determinant is (−1)^{n(n+1)/2} ∏_{i<j}(m_i+m_j)/e_n, now proved for every n (§3,
     Lemma S2.1).
   - Its inverse factors through a Hurwitz matrix whose determinant is ∏(m_i+m_j) (Lemma S2.2).
   - Positive orders never make it singular. In scale-free units the inverse has norm 1 to
     3.5 on every test multiset.
3. **Roots (the only place stability degrades).**
   - A simple order moves linearly with the error.
   - A k-fold order splits like (error)^{1/k}, and this exponent cannot be improved for
     general data (§4).
   - A double order is the generic coincidence, and both test pillows have one. It already
     costs a square root.
4. **Integers (stability becomes exactness).** Below an explicit threshold δ*(m), rounding the
   recovered roots returns the orders exactly (§5).
   - For the pillows (2,8,8) and (3,3,12), H₁ must be known to about 2·10⁻³ in absolute
     terms, i.e. about 7·10⁻⁴ relative. The certified threshold is within 6% (resp. 12%) of
     an explicit failure.
   - The computed spectra deliver H₁ to 2·10⁻⁵ (resp. 1.4·10⁻⁴). The blind experiment (§6)
     recovers both multisets exactly and certifies the recovery. Neither of the first two
     coefficients separates them, at any precision.

## 1. Setting and the recovery map

Conventions (`numerics/REPORT.md` §2; `theory/cone-coefficients/ucar-source.md`): positive
Laplacian, K = κ = −1, and

- H₋₁ = Area/(4π) = (n − 2 − R)/2;
- H_ν = (Area/4π)·α_{ν+1} + Σ_i b_ν(m_i) for ν ≥ 0;
- b_ν(m) = (−1)^ν p_ν(m)/m, with p_ν = Σ_k π_{ν,k} m^{2k} even of degree 2ν + 2 and
  p_ν(1) = 0 (Uçar (4.25)+(4.33));
- α_j = a_j^{sm}/vol (Uçar (4.35)): α = 1, −1/3, 1/15, −4/315, 1/315, …

The smooth coefficients α_j are also derived independently from the Selberg identity term
(`stab_common.alpha_smooth_selberg`), and the two agree for j ≤ 11.

The number n of cone points is assumed known. The **recovery map** studied throughout is:

1. **Front end.** Ĩ := L⁻¹(H̃ − h₀).
2. **Linear solve.** ẽ := M(Ĩ)⁻¹ b(Ĩ) (Theorem B).
3. **Roots.** Take the roots of q̃(z) := Σ_{j=0}^{n}(−1)^j ẽ_j z^{n−j}, with ẽ₀ = 1.
4. **Rounding** (integer orders only). Round the real part of every root.

Throughout, μ := max_i m_i. Hats denote scale-free quantities:

- m̂ = m/μ ∈ (0,1]ⁿ and ê_k = e_k/μ^k;
- Î = (μR, P₁/μ, P₃/μ³, …).

Theorem B's system is weighted-homogeneous: row j has weight 2j+1, the last row weight n−1,
and column k weight k. Hence M(Î) = D_r⁻¹ M(I) D_c, and ê solves M(Î) ê = b(Î).
Distances between multisets are optimal matching distances,
d(m, m′) = min_π max_i |m_i − m′_{π(i)}|.

## 2. Front end (T1)

**Proposition S1.** For every n, (H₋₁, …, H_{n−2}) = L·I_n + h₀(n), where L is lower
triangular with entries

- L₀₀ = −1/2;
- L_{ν+1,0} = −α_{ν+1}/2 + (−1)^ν π_{ν,0};
- L_{ν+1,k} = (−1)^ν π_{ν,k} for 1 ≤ k ≤ ν+1.

The offset is h₀(n) = ((n−2)/2)(1, α₁, …, α_{n−1}). The matrix L does not depend on n, which
enters only through h₀. Its diagonal is L_{ν+1,ν+1} = (−1)^ν |B_{2ν+2}|/(2(ν+1)!(2ν+1)) ≠ 0,
so L is invertible.

*Proof.* Sum the cone terms. Σ_i m_i^{2k}/m_i = P_{2k−1}, with P₋₁ = R. Collect the smooth
term (n − 2 − R)/2 · α_{ν+1}. The leading coefficient of p_ν is the Bernoulli expression
verified in `theory/cone-coefficients/`. ∎

Exact tables are in `front_end_output.md`. The script asserts the following:

- L·I + h₀ equals the cone-by-cone evaluation for n = 3..8 at the named multisets and at
  random rational ones;
- L·L⁻¹ = Id;
- the cone polynomials agree with `numerics/theory.py` for orders 2..40.

The first rows of L⁻¹, which give I = L⁻¹(H − h₀):

| | H₋₁ | H₀ | H₁ | H₂ | H₃ |
|---|---|---|---|---|---|
| R | −2 | | | | |
| P₁ | 2 | 12 | | | |
| P₃ | −18 | −120 | −360 | | |
| P₅ | 30 | 252 | 1260 | 2520 | |
| P₇ | −70/3 | −240 | −1680 | −6720 | −10080 |

**Amplification.** With every |δH_ν| ≤ δ, the worst-case error in I_r is ℓ_r·δ, where ℓ_r is
the absolute row sum of L⁻¹. Row r involves only the first r+1 coefficients, so ℓ_r is the
same for every n:

| | R | P₁ | P₃ | P₅ | P₇ | P₉ | P₁₁ | P₁₃ |
|---|---|---|---|---|---|---|---|---|
| diagonal 1/\|L_rr\| | 2 | 12 | 360 | 2520 | 10080 | 28512 | 43243200/691 | 112320 |
| ℓ_r (row sum) | 2 | 14 | 498 | 4062 | 56230/3 | 303654/5 | 104899830/691 | 10805786/35 |

**Correction to the review (DEFECTS.md MAJ-05).**

- The factors 12, 360, 2520 are correct as the diagonal entries of L⁻¹: for P₁ from H₀, P₃
  from H₁ and P₅ from H₂.
- They are not the amplification factors. Each invariant also inherits the errors of all
  lower coefficients through the off-diagonal entries, e.g.
  δP₃ = −18 δH₋₁ − 120 δH₀ − 360 δH₁.
- So the worst-case factors are **14, 498, 4062**, larger by 1.17, 1.38 and 1.61.
- R is recovered from H₋₁ with factor 2. Equivalently, R = n − 2 − Area/(2π), so the factor
  is 1/(2π) per unit of area.
- In relative terms the front end is harmless. The ratio
  κ_r = Σ_c |(L⁻¹)_{rc}| |H_c| / |I_r| lies between 0.02 and 3.7 on every test multiset of
  `front_end_output.md`. For (2,8,8) it is 0.33, 0.94, 1.33 for R, P₁, P₃.

## 3. From I_n to e (T2)

Let N := ∂(M e − b)/∂I, evaluated at fixed e, with columns ordered as I = (R, P₁, …, P_{2n−3}).
By T = tanh U, U = Σ_{k odd} P_k z^k/k, one has ∂T_k/∂P_l = [z^{k−l}] sech²U / l. Row j of N
therefore involves only P₁, …, P_{2j+1}, and its entry at P_{2j+1} is −1/(2j+1). The last row
is (−e_n, 0, …, 0). Hence

  det N = −e_n / ∏_{j=0}^{n−2}(2j+1).

**Lemma S2.1 (the constant c_n of Theorem B, all n).** For every n ≥ 2,

  det M = (−1)^{n(n+1)/2} ∏_{i<j}(m_i + m_j) / e_n,

so c_n = (−1)^{n(n+1)/2}. This replaces "c_n ∈ ℚ^×, computed for n ≤ 8" in Theorem B.

*Proof.* Write G : e ↦ I_n(e), so R = e_{n−1}/e_n and P_k is the Newton polynomial in e. The
identity M(G(e)) e = b(G(e)) holds on {e_n ≠ 0} (Theorem B). Differentiating in e gives
M + N·D_eG = 0, hence

  D_I e = (D_eG)⁻¹ = −M⁻¹N  and  det M = (−1)ⁿ det N · det D_eG.

On the dense set of multisets with distinct m_i, D_eG = D_mI · (D_m e)⁻¹.

- Multiply column i of D_mI by m_i². Row r becomes c_r m_i^{2r}, with c₀ = −1 and c_r = 2r−1.
  Hence det D_mI = −∏_{r=1}^{n−1}(2r−1) · ∏_{i<j}(m_j² − m_i²) / ∏ m_i².
- The classical Jacobian of the elementary symmetric functions is
  det D_m e = ∏_{i<j}(m_i − m_j).

Therefore

  det D_eG = −∏(2r−1) · (−1)^{n(n−1)/2} ∏(m_i+m_j)/e_n²,

and det M = (−1)ⁿ · (−e_n/∏(2j+1)) · det D_eG = (−1)^{n+n(n−1)/2} ∏(m_i+m_j)/e_n. Both sides
are rational in e and agree on a dense set. ∎

Checked exactly at random rational multisets for n = 2..10 (`lipschitz_e.py` (a)). This
agrees with the values +1, +1, −1, −1, +1, +1 computed for n = 3..8 by
`theory/audibility/linear_system.py`.

**Lemma S2.2 (Hurwitz factorisation of M).** Let f(z) = ∏(1 + m_i z) = E(z²) + zO(z²), and for
D(z) = Σ_{k=1}^n d_k z^k let W_D := E_f O_D − E_D O_f, a polynomial in w = z² of degree ≤ n−1.
Define two n × n matrices (with e_i := 0 outside 0 ≤ i ≤ n):

- B_{k,j} = (−1)^{j+1} e_{2k+1−j}, for 0 ≤ k ≤ n−1 and 1 ≤ j ≤ n. This is the map
  d ↦ (coefficients of W_D).
- S_{k,i} = e_{2(k−i)} for i ≤ k ≤ n−2, S_{n−1,n−1} = (−1)ⁿ e_n, and all other entries 0.

Then

  B = S·M,  det B = (−1)^{n(n−1)/2} ∏_{i<j}(m_i+m_j),  M⁻¹ = B⁻¹ S.

*Proof.* For j ≤ n−2, (Md)_j = [z^{2j+1}](zO_D − T E_D). Since T ≡ zO_f/E_f mod z^{2n−1},

  E_f · (zO_D − T E_D) ≡ z W_D(z²) mod z^{2n−1}.

The coefficient of z^{2k+1}, for k ≤ n−2, is Σ_{i≤k} e_{2(k−i)} (Md)_i = (B d)_k. The top
coefficient is W_{n−1} = (−1)ⁿ(e_n d_{n−1} − e_{n−1}d_n) = (−1)ⁿ e_n (Md)_{n−1}, using
R = e_{n−1}/e_n. Finally, det S = (−1)ⁿ e_n, and det B = det S · det M by Lemma S2.1. ∎

B is the Hurwitz matrix of p(z) = ∏(z + m_i), up to signs. Its determinant
∏(m_i + m_j) (Orlando) is the quantity whose positivity for stable p underlies Theorem A.
Inverting Theorem B is exactly as well conditioned as this Hurwitz matrix.

**Theorem S2 (Lipschitz dependence of e on I_n, explicit constants).**

*Setting.* Let m be positive reals and μ = max m_i. Let Ĩ be any real data vector with
scale-free error

  η := max( μ|R̃ − R|, max_{1≤l≤n−1} |P̃_{2l−1} − P_{2l−1}| / μ^{2l−1} ) ≤ 1.

*Constants.* Put κ := ‖M(Î)⁻¹‖_∞ and

- σ_k(n) := [w^k] artanh(w) · sec²((n+1) artanh w). For instance σ₁ = 1 and
  σ₃ = 1/3 + (n+1)²; n = 3: (1, 49/3); n = 4: (1, 76/3, 6628/15).
- ζ_n := max(1, max_{0≤j≤n−2} Σ_{0≤i<j, 2≤2j−2i≤n} σ_{2i+1}(n)). For example ζ₃ = 1,
  ζ₄ = 79/3, ζ₅ = 14048/15.
- ρ_n(m̂) := max( ê_n, max_{0≤j≤n−2} Σ_{i=0}^{j} σ_{2i+1}(n) ê_{2j−2i} ).

*Conclusions.*

(a) The inverse is bounded by

  κ ≤ n Λ(m̂) ‖Ŝ‖_∞ / ∏_{i<j}(m̂_i + m̂_j) ≤ n · binom(2n,n)^{n/2} · 2^{n−1} / ∏_{i<j}(m̂_i + m̂_j),

  where Λ(m̂) = ∏_c ‖c-th column of B(ê)‖₂ and ‖Ŝ‖_∞ ≤ max(Σ_{k even} ê_k, ê_n).

(b) If β := κ ζ_n η ≤ 1/2, then M(Ĩ) is invertible, and ẽ = M(Ĩ)⁻¹ b(Ĩ) satisfies

  max_k |ẽ_k − e_k| / μ^k ≤ 2 κ ρ_n(m̂) η.

(c) To first order, ẽ − e = (D_I e)(Ĩ − I) + O(η²), with D_I e = −M⁻¹N exact (Lemma S2.1).

In physical terms, the constant degrades only through:

- the Orlando product ∏(m̂_i + m̂_j), which is small only when at least two orders are small
  compared with the largest;
- the size e_n of the orders, through ê_n in ρ_n and ‖Ŝ‖;
- the binomial sizes of ê_k ≤ binom(n,k).

It is uniform near coincident orders, because the diagonals m_i = m_j play no role here.

*Proof.* Work in scale-free variables.

- *Bound on κ.* By Lemma S2.2, M⁻¹ = B⁻¹S. Every column of B̂ contains ê₀ = 1 or
  ê₁ = Σ m̂_i ≥ 1, so all column norms are ≥ 1. Hadamard's inequality then bounds every
  cofactor of B̂ by Λ. Using |det B̂| = ∏(m̂_i + m̂_j), this gives (a). The closed form uses
  ê_k ≤ binom(n,k), Σ_{i ≡ c mod 2} binom(n,i)² ≤ binom(2n,n), and Σ_{k even} binom(n,k) = 2^{n−1}.
- *Majorants.* Write T = tanh U and T̃ = tanh Ũ. All P_k > 0, so U has nonnegative
  coefficients, and Û ≤ n·artanh(w) coefficientwise, since P̂_k ≤ n. Also
  |δÛ| ≤ η·artanh(w). The coefficients of tanh are those of tan up to sign, and expanding
  (U + δU)^p − U^p gives only terms that contain δU. Hence, coefficientwise,

  |T̃_k − T_k| ≤ [w^k](tan((n+η) artanh w) − tan(n artanh w)) ≤ η σ_k(n),

  using tan(a + b) − tan a = ∫₀¹ b sec²(a + sb) ds and the monotonicity of sec² in its
  argument.
- *Residual and perturbation.* The residual r := b(Ĩ) − M(Ĩ) e has |r_j| ≤ Σ_i |δT_{2i+1}| ê_{2j−2i}
  and |r_{n−1}| ≤ η ê_n, so ‖r‖_∞ ≤ ρ_n η. Also ‖δM‖_∞ ≤ ζ_n η. Since M(Ĩ)(ẽ − e) = r, the
  standard bound ‖(M + δM)⁻¹‖ ≤ κ/(1 − β) gives (b).
- *First order.* (c) is Lemma S2.1. ∎

*Checks* (`lipschitz_e.py`, output in `lipschitz_e_output.md`):

- (a) holds at every test multiset. The exact κ is 1 to 3.5, against a Hadamard bound of
  12–4425 and a closed form of 10²–10⁶. The Hadamard step is the lossy one.
- (b) and the majorant |δT_k| ≤ η σ_k hold for 240 random exact rational perturbations
  (η = 10⁻² to 10⁻⁸).
- (c) agrees with an exact finite difference.

## 4. From e to the orders (T3)

**Standard global theorem (fetched, `review/literature/root-perturbation.md`).** Ostrowski,
*Acta Math.* 72 (1940), Théorème XXX, eq. (71,1), p. 212, read from the primary. For monic
f, g of degree n with roots x_ν and y_ν, after renumbering,

  |y_ν − x_ν| ≤ (2n−1)ε,  ε = (Σ_{ν=1}^{n} |a_ν − b_ν| γ^{n−ν})^{1/n},

where γ is the largest root modulus. "Les racines … satisfont … à une condition de Lipschitz
d'ordre 1/n." This is uniform but crude: exponent 1/n everywhere, with no use of
separation. The local statement below has the exponent 1/k at a k-fold root, and is
Lipschitz at simple roots, with explicit constants.

**Lemma S3 (clusters, explicit Rouché).** Work in scale-free variables. Let
q(z) = ∏(z − m̂_i) = Σ_j (−1)^j ê_j z^{n−j}, and let q̃ be the same polynomial with ẽ in place
of ê, where |ẽ_j − ê_j| ≤ ε. Let a be a distinct value among the m̂_i, of multiplicity k, and
put

- g_a := min_{b≠a} |a − b| (∞ if there is no other value);
- Q_a := ∏_{b≠a} |a − b|^{k_b}.

If 0 < r ≤ min(g_a, 1)/2 and r^k Q_a ≥ 2^{1−k} 3ⁿ ε, then q̃ has exactly k zeros in |z − a| < r.
In particular, for r_a(ε) := (2^{1−k}3ⁿ ε/Q_a)^{1/k}, whenever r_a(ε) ≤ min(g_a, 1)/2, the k
roots of the cluster lie within r_a(ε) = O(ε^{1/k}) of a. The bound is Lipschitz for simple
orders, where Q_a = |q′(a)|.

*Proof.* Take z on the circle |z − a| = r.

- *Lower bound on q.* For b ≠ a, |z − b| ≥ |a − b| − r ≥ |a − b|/2, so
  |q(z)| ≥ r^k Q_a 2^{−(n−k)}.
- *Upper bound on the perturbation.* Since |z| ≤ 3/2,
  |q̃(z) − q(z)| ≤ ε Σ_{j=0}^{n−1}(3/2)^j < 2^{1−n}3ⁿ ε ≤ |q(z)|.

Rouché's theorem gives the count. ∎

*Check* (`roots_holder.py` (a)): 742 cluster instances at 9 multisets, with random
e-perturbations of scale-free size 10⁻³ to 10⁻¹². Every cluster has exactly k roots inside
r_a. The largest observed displacement/r_a is 0.10, 0.40, 0.69 and 0.78 for k = 1, 2, 3, 4.

**Theorem S3 (heat coefficients → orders; the combined stability theorem).**

*Setting.* Let m be positive reals, n = |m|, μ = max m_i. Let H̃ be data with
δ := max_{−1≤ν≤n−2} |H̃_ν − H_ν(m)|. Put

- λ_μ := max(μ ℓ₀, max_{1≤r≤n−1} ℓ_r μ^{1−2r}), with ℓ = (2, 14, 498, 4062, …) as in §2;
- κ, ρ_n, ζ_n as in Theorem S2.

*Statement.* Suppose λ_μ δ ≤ 1 and κ ζ_n λ_μ δ ≤ 1/2. Then for every distinct order a, of
multiplicity k_a, with

  r_a := μ · (2^{2−k_a} 3ⁿ κ ρ_n λ_μ δ / Q̂_a)^{1/k_a} ≤ μ · min(ĝ_a, 1)/2,

the recovered polynomial q̃ has exactly k_a roots within r_a of a. Consequently, if the
radius hypothesis holds for **every** distinct order a,

  d(roots of q̃, m) ≤ max_a C_a δ^{1/k_a},  C_a = μ (2^{2−k_a} 3ⁿ κ ρ_n λ_μ / Q̂_a)^{1/k_a}.

So recovery is Lipschitz with constant C_a at simple orders, where Q̂_a = |q̂′(â)| measures the
gaps, and Hölder with exponent 1/k at a k-fold coincidence.

*Proof.* Chain the three layers:

- Proposition S1 gives |δI_r| ≤ ℓ_r δ, i.e. η ≤ λ_μ δ.
- Theorem S2(b) gives ε ≤ 2κρ_nλ_μδ.
- Lemma S3 converts ε into root positions, and r_a is Lemma S3's radius in physical units. ∎

**Proposition S3.2 (the exponent 1/k is sharp).**

(i) *Double order, realisable data.* Take m(s) = (a+s, a−s, c₃, …, c_n). Then H(m(s)) is
smooth and even in s, so ‖H(m(s)) − H(m(0))‖_∞ = C s² + O(s⁴), while the orders move by
exactly s. No bound d ≤ C′δ^γ with γ > 1/2 can hold.

- Exactly, for a = 8, c = 2 (the pillow (2,8,8)): ΔR = 2s²/(8(64−s²)), ΔP₁ = 0, ΔP₃ = 48s².
- The ratio s/‖ΔH‖^{1/2} converges to 2.7385 for (2,8,8), 4.4630 for (3,3,12) and 2.0446 for
  (3,3,4,4), splitting the pair of 3s (splitting the pair of 4s gives 1.3593) (`roots_holder_output.md`).

(ii) *k-fold order, general data.* Take q_s(z) = ((z − a)^k − s^k) g(z), with g real monic
of degree n − k and g(a) ≠ 0.

- q_s has real coefficients, so its heat data H(q_s) are real. They are computed from e(q_s)
  through Newton's identities and R = e_{n−1}/e_n, and are within O(s^k) of H(m).
- By Theorem B the recovery map returns q_s, whose roots a + sω^j lie at distance exactly s
  from a. Hence the exponent 1/k cannot be improved.
- Ratios s/‖ΔH‖^{1/k} converge for k = 3 at (4,4,4), (7,7,7), (2,2,2,3), and for k = 4 at
  (5,5,5,5).

**Remark S3.3 (realisable data at a triple order).** The exponent 1/k concerns arbitrary data
vectors, which is the right model for noisy measurements. For data that are heat
coefficients of a *real* multiset near (a,a,a), the exponent is 1/2. For real d with
|d_i| ≤ a,

  (P₃ − 3a²P₁)(a + d) − (P₃ − 3a²P₁)(a) = 3a Σd_i² + Σd_i³ ≥ 2a Σd_i²,

so max|d_i| ≤ (|ΔP₃ − 3a²ΔP₁|/(2a))^{1/2}. This was checked on 900 random real perturbations.
No general statement for realisable data at mixed clusters is claimed.

## 5. Exact integer recovery (T4)

**Theorem S4 (explicit threshold).** Let m be integer orders. Define

  δ_thm(m) := min( 1/λ_μ,  1/(2κζ_nλ_μ),  min_a  Q̂_a 2^{k_a−1} / (3ⁿ (2μ)^{k_a} · 2κρ_nλ_μ) ).

If |H̃_ν − H_ν(m)| ≤ δ_thm(m) for ν = −1, …, n−2, then rounding the real parts of the roots
of q̃ returns m exactly.

*Proof.* Distinct integers are at least 1 apart, so ĝ_a ≥ 1/μ and min(ĝ_a, 1)/2 ≥ 1/(2μ).
The third term of the minimum makes r_a ≤ 1/2 in Theorem S3.

- Each open disk |z − a| < 1/2 contains exactly k_a roots.
- The disks are pairwise disjoint, and Σ k_a = n, so they contain all the roots.
- Every root in the disk around a has real part in (a − 1/2, a + 1/2), so it rounds to a. ∎

Theorem S4 is a closed form, and it is pessimistic because of the triangle inequalities in
S2(b) and Lemma S3. The thresholds actually reported come from a sharper certificate, which
is equally rigorous.

**Proposition S5 (certificates, exact arithmetic).**

*Input.* Fix m and componentwise radii ρ_ν ≥ 0. Every data vector with |H̃_ν − H_ν(m)| ≤ ρ_ν
is recovered exactly if either test below succeeds, with all quantities evaluated in
rational arithmetic (`threshold.py`).

*Common part.*

1. |δI| ≤ |L⁻¹|ρ.
2. Bound |δT_k| ≤ (|sech²U| ∗ |δU|)_k + [z^k](tan(U+|δU|) − tan U − sec²U·|δU|). The first
   term is the exact linear part. The second is the coefficientwise majorant of the
   remainder, valid because U ≥ 0.
3. Form the residual bound |r|, the bound |δM|, and A := |M⁻¹||δM|.
4. Certify ρ(A) < 1 by checking that v = (I − A)⁻¹𝟙 > 0.
5. Then |ẽ − e| ≤ E := (I − A)⁻¹|M⁻¹||r|.

*(i) Componentwise test.* For each distinct order a, some radius r ∈ {1/2, 19/40, …, 1/40,
1/100, 1/1000} satisfies

  r^{k_a} ∏_{b≠a}(|a−b| − r)^{k_b} > Σ_j E_j (a + r)^{n−j}.

*(ii) Coherent test.* Write ẽ − e = G·δH + ϱ, where:

- G = (D_I e) L⁻¹ is exact (Lemma S2.1);
- |ϱ| ≤ |M⁻¹||r_rem| + A E, with r_rem the remainder part of r.

On |z − a| = r, bound the first-order part through the exact Taylor coefficients at a of
the polynomials p_c(z) = Σ_j (−1)^j G_{jc} z^{n−j}. The test is

  r^{k_a} ∏(|a−b| − r)^{k_b} > Σ_c ρ_c Σ_l |p_c^{(l)}(a)/l!| r^l + Σ_j |ϱ_j| (a + r)^{n−j}.

*Proof.* The exact expansion of ẽ − e follows from M(Ĩ)(ẽ − e) = r, splitting r into its
part linear in δI (which is −N δI) and the remainder. The Rouché argument is that of
Theorem S4, with the sharper bound on |q̃ − q| on the circle. ∎

**Upper bound by construction.** For each order a, the search minimises
‖H(q̃) − H(m)‖_∞ over real monic polynomials of two shapes:

- q̃ = (z − c) g(z), with a real root at c = a ± 1/2;
- q̃ = ((z − c)² + y²) g(z), with a complex pair of real part c = a ± 1/2.

The optimiser is numerical. The reported minimiser is rebuilt exactly in rationals, and its
data are evaluated exactly. Its recovery is q̃ itself (Theorem B, checked by an exact solve),
and that q̃ has a root with real part exactly a ± 1/2. At that point rounding is a tie, so
δ_up is an infimum: arbitrarily small further perturbations push the root across, and
recovery fails at every level above δ_up. Hence the true threshold is at most δ_up.

*Rounding of printed values.* δ_thm and δ_cert are printed rounded **down**, and δ_up
rounded **up**, so that each printed number keeps its meaning. An adversarial search found
that the exact test fails at the up-rounded values 2.342e−3 and 1.462e−3, which an earlier
version printed.

**Results** (`threshold_output.md`, `threshold_results.json`). The absolute model is
|δH_ν| ≤ δ for all ν. The relative precision listed is δ_cert/|H_ν| for ν = −1, …, n−2, and
ε_cert is the largest uniform relative error |δH_ν| ≤ ε|H_ν| that is certified.

| m | n | δ_thm | δ_cert | δ_up | δ_up/δ_cert | failure built at | δ_cert/|H_ν|, ν = −1..n−2 | ε_cert (uniform relative) |
|---|---|---|---|---|---|---|---|---|
| (2, 8, 8) | 3 | 3.80e-07 | 2.341e-03 | 2.485e-03 | 1.06 | 8−1/2 | 1.8e-02, 1.6e-03, 7.0e-04 | 1.9e-03 |
| (3, 3, 12) | 3 | 1.18e-07 | 4.040e-03 | 4.589e-03 | 1.14 | 3+1/2 | 3.2e-02, 2.8e-03, 7.4e-04 | 4.4e-03 |
| (3, 10, 15, 30) | 4 | 4.02e-11 | 3.660e-03 | 7.488e-03 | 2.05 | 10+1/2 | 4.9e-03, 8.0e-04, 4.1e-05, 3.6e-07 | 8.7e-04 |
| (4, 5, 21, 28) | 4 | 3.14e-11 | 1.461e-03 | 2.018e-03 | 1.38 | 5−1/2 | 1.9e-03, 3.2e-04, 1.6e-05, 1.7e-07 | 4.6e-04 |
| (2, 3, 7) | 3 | 4.49e-07 | 3.658e-03 | 6.587e-03 | 1.80 | 3−1/2 | 3.0e-01, 4.0e-03, 2.7e-03 | 5.0e-03 |
| (4, 4, 4) | 3 | 9.35e-07 | 4.539e-04 | 5.036e-04 | 1.11 | 4+1/2 | 3.6e-03, 5.0e-04, 5.4e-04 | 8.2e-04 |
| (7, 7, 7) | 3 | 9.97e-08 | 8.068e-05 | 8.273e-05 | 1.03 | 7−1/2 | 2.8e-04, 4.9e-05, 2.3e-05 | 1.2e-04 |
| (3, 3, 4, 4) | 4 | 1.48e-09 | 9.597e-05 | 1.195e-04 | 1.24 | 4−1/2 | 2.3e-04, 1.0e-04, 1.1e-04, 7.2e-05 | 1.1e-04 |
| (5, 5, 5, 5) | 4 | 4.74e-10 | 3.617e-05 | 3.826e-05 | 1.06 | 5−1/2 | 6.0e-05, 2.5e-05, 1.9e-05, 6.2e-06 | 3.1e-05 |
| (2, 2, 2, 3) | 4 | 2.03e-09 | 1.858e-04 | 2.520e-04 | 1.36 | 3−1/2 | 2.2e-03, 3.2e-04, 5.6e-04, 7.7e-04 | 4.3e-04 |
| (2, 2, 2, 2, 3) | 5 | 2.72e-12 | 7.908e-06 | 5.743e-05 | 7.26 | 2+1/2 | 2.3e-05, 1.2e-05, 2.1e-05, 2.9e-05, 1.9e-05 | 1.4e-05 |

*Reading the table.*

- The exponent shows up as the jump between the closed form δ_thm and the true threshold.
  The closed form uses the worst-case Lemma S3 constant, which carries (1/(2μ))^{k} and the
  factor 3ⁿ.
- The certified δ_cert is within a factor 1.03–2.05 of the constructed failure δ_up for every
  n ≤ 4 case, and 7.3 for the n = 5 case (2,2,2,2,3). So the reported thresholds are close to
  the truth, not just safe.
- For the two pillows the binding coefficient is H₁, the first that carries P₃. Its required
  *relative* precision is about 7·10⁻⁴ for (2,8,8) and 7·10⁻⁴ for (3,3,12).
- H₋₁ (the area) and H₀ need only percent-level and 10⁻³-level relative accuracy. They fix
  R and P₁, which the two pillows share anyway.

## 6. Blind end-to-end experiment (T5)

`blind/PROTOCOL.md` was committed (3c1139a) before the pipeline code (a4a87d7) and before the
result (1fa4ff4). Only the eigenvalue CSVs and universal constants were used. Full output is in
`blind/RESULT.md`.

| specimen | H₋₁ | H₀ | H₁ | recovered | certified | (est − true)/U |
|---|---|---|---|---|---|---|
| A (true (2,8,8)) | 0.1250000000 ± 1.1·10⁻¹¹ | 1.3958333303 ± 2.4·10⁻⁸ | −3.3354134980 ± 2.1·10⁻⁵ | (2,8,8) | yes | +0.11, −0.13, +0.15 |
| B (true (3,3,12)) | 0.1250000000 ± 4.9·10⁻¹¹ | 1.3958332915 ± 1.3·10⁻⁷ | −5.4186953214 ± 1.4·10⁻⁴ | (3,3,12) | yes | +0.29, −0.33, +0.39 |

**Three coefficients recover both multisets exactly.**

- The recovered polynomial's double root shows the √δ law directly:
  - A gives 8 ± 0.0050i;
  - B gives 2.9915 and 3.0085, for an H₁ error of order 10⁻⁴.
- The a-posteriori certificate (Proposition S5 at the candidate, with radius
  |H̃ − H(m̂)| + U) succeeds for both specimens.
- The margin to the certified threshold is about 100× for A and 20× for B.
- The same holds with the conservative eigenvalue errors.

**Two coefficients cannot separate them.**

- Structurally, H₋₁ = (1 − R)/2 and H₀ = (P₁ + R − 2)/12 for n = 3. Both are functions of
  (R, P₁) = (3/4, 18), which the two pillows share.
- Empirically, the estimates of H₋₁ and H₀ for A and B agree to 0.2σ and 0.3σ. The estimates
  of H₁ differ by 2.0833 ± 1.6·10⁻⁴, against the exact 25/12.
- The exhaustive enumeration of hyperbolic integer triples consistent with the first two
  estimates, at 1U and 3U, returns exactly {(2,8,8), (3,3,12)} for both specimens. Adding H₁
  leaves exactly one triple.

**Error bars.** Every estimate is within 0.62 U of the truth under both error models.

## 7. What is proved, what is checked, what is open

**Proved for all n:**

- Proposition S1;
- Lemma S2.1, which gives c_n = (−1)^{n(n+1)/2} in Theorem B for every n;
- Lemma S2.2;
- Theorem S2;
- Lemma S3;
- Theorem S3;
- Proposition S3.2;
- Theorem S4;
- Proposition S5.

**Computed exactly:**

- the front-end tables for n ≤ 8;
- the T4 thresholds at 11 multisets (δ_thm, δ_cert rigorous; δ_up an exact counterexample).

**Assumptions:**

- The analytic input of Theorem A (the cone polynomials) is used as in
  `theory/audibility/proof.md` §1.
- The error model is on heat coefficients, not eigenvalues. Converting eigenvalue errors into
  coefficient errors is done empirically in §6. It is not proved: the fit's model-error term
  is empirical, and the eigenvalue error estimates are a-posteriori agreements, not
  enclosures (`numerics/REPORT.md` §7).

**Not claimed:**

- a general realisable-data exponent at mixed clusters (Remark S3.3);
- sharpness of the constants in Theorem S2 or S4. Only the exponents are sharp. δ_cert is
  within a factor 2.05 of the truth for the n ≤ 4 cases, and 7.3 for n = 5.
