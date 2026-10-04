# CONVENTIONS: one notation for the paper, and a translation from every file

The theory sessions, the numerics sessions and the original verification code each fixed their own
notation. This file fixes one convention for the paper, translates every existing file into it, and
lists every symbol that is used for more than one thing. The translations are checked by
`theory/conventions_check.py` (section 5); the collisions were found by searching the repository
(section 4).

**Nothing existing was renamed.** Committed data headers (`c1`, `c2` in `numerics/data/fits.csv` and
`headline.json`, `a0`, `a1` in the numerics scripts) and the functions of the verification scripts keep
their names, because renaming them would change committed data or mathematical content. The paper
adopts the names below; this table says how to read every file against them.

## 1. The convention

**Operator and curvature.** The Laplacian `Δ` is the nonnegative one, `0 = λ_0 < λ_1 ≤ …`. The Gauss
curvature is `K`, and the paper's setting is `K = −1` throughout. (The Uçar papers write `κ` for the same
number; the paper does not use `κ` for curvature.)

**Heat coefficients.** For a closed orientable hyperbolic 2-orbifold `O`

    Z(t) = tr e^{−tΔ}  ~  Σ_{j≥1} c_j(O) t^{j−2}        (t ↓ 0).

So `c_1` is the `t^{−1}` coefficient, `c_2` the `t^0` coefficient, and **`c_{l+2}` the `t^l` coefficient**.
"The first `L` coefficients" means `(c_1, …, c_L) = H_L(O)`, a tuple (`theory/definitions.tex`,
`def:heatcoef`). `c_1 = Area/(4π) = −χ/2`, where `χ = 2 − 2g − Σ(1 − 1/m_i)` is the orbifold Euler
characteristic and `Area = 2π(2g − 2 + Σ(1 − 1/m_i))`; for a triangular pillow `Area = 2π(1 − R)` and
`c_1 = (1 − R)/2`.

**Structure of the coefficients.** With `α_j := a_j^sm / vol` (Uçar (4.35), at `K = −1`:
`α_0, α_1, α_2, … = 1, −1/3, 1/15, −4/315, …`) and the cone term `b_l(m)`,

    c_1 = Area/(4π),      c_j = (Area/4π) α_{j−1} + Σ_i b_{j−2}(m_i)      (j ≥ 2).

**Cone term.** `b_l(m)` is the contribution of one cone point of order `m` to the `t^l` coefficient,

    b_l(m) = K^l · (1/m) · p_l(m),        so at K = −1:   b_l(m) = (−1)^l p_l(m)/m,

with `p_l` an even polynomial of degree `2l + 2`, `p_l(1) = 0`, positive on `m ≥ 2`
(Uçar (4.25) + (4.33)). The sign `(−1)^l` is part of `b_l`. The unsigned positive quantity is
`β_l(m) := b_l(m)/K^l = p_l(m)/m`. Examples: `p_0 = (m² − 1)/12`, `b_0 = (m² − 1)/(12m)`;
`p_1 = m⁴/360 + m²/36 − 11/360`, `b_1 = −p_1/m`. Hence `c_2 = χ/6 + Σ(m_i² − 1)/(12 m_i)` (the paper's `a_0`).

**Orders and invariants.** Cone orders `m_1, …, m_n ≥ 2`; `R := Σ 1/m_i`; power sums
`P_k := Σ m_i^k`; the paper's `S_1` and the sum `S` of Sections 2 and 5 are the same number, `S = S_1 = P_1`.
`e_k` are the elementary symmetric functions of the orders (`e_0 = 1`), so `R = e_{n−1}/e_n`.
The heat invariants are `I_n(m) = (R, P_1, P_3, …, P_{2n−3})`: the `j`-th coefficient `c_j` is the first
to involve `P_{2j−3}` (and `c_1` is `R`, i.e. the area).

**Signatures.** `σ(O) = (g; m_1, …, m_n)`, with `g` the genus and `{m_i}` a multiset; `(2,8,8)` is
shorthand for `(0; 2,8,8)`. `O(p,q,r)` is the triangular pillow, `2 ≤ p ≤ q ≤ r`, `1/p + 1/q + 1/r < 1`
(a "triad"). `s(σ) = Area/2π = 2c_1`.

**Comparison classes and `K`.** For a class `𝒫` of closed orientable hyperbolic 2-orbifolds
(`def:K`),

    K_iso(O; 𝒫)  = min{k ≥ 1 : ∀ O' ∈ 𝒫,  H_k(O') = H_k(O) ⇒ O' isometric to O},
    K_mult(O; 𝒫) = min{k ≥ 1 : ∀ O' ∈ 𝒫,  H_k(O') = H_k(O) ⇒ σ(O') = σ(O)},     min ∅ = ∞,

so `K_mult ≤ K_iso`. Classes: `𝒫_3` (triangular pillows), `𝒫_n` (genus 0, `n` cone points), `𝒫_0` (genus 0, any `n`),
`Sig` (every genus). On `𝒫_3` the two agree (rigidity). The paper's unsubscripted `K(F)` means
`K_iso(F; 𝒫_3) = K_mult(F; 𝒫_3)`.

**Differences of coefficients.** `d_j(O, O') := c_j(O) − c_j(O')`. For the pair `(2,8,8)`, `(3,3,12)`
(same area, same `c_2`) `D(t) := Z_{(2,8,8)}(t) − Z_{(3,3,12)}(t) = Σ_{j≥3} d_j t^{j−2}`, with
`d_3 = 25/12`, `d_4 = −1775/24`, `d_5 = 153025/48`.

## 2. Reading order: `t`-power, index and name side by side

| `t`-power | −1 | 0 | 1 | 2 | `l` |
|---|---|---|---|---|---|
| paper index | `c_1` | `c_2` | `c_3` | `c_4` | `c_{l+2}` |
| value for `(2,8,8)` | 1/8 | 67/48 | −1601/480 | 555313/20160 | |
| first invariant it involves (`I_n`) | `R` | `P_1` | `P_3` | `P_5` | `P_{2l+1}` |

## 3. Translation table: every file into the paper's convention

`Z`-normalisation is the trace of the whole orbifold (a pillow) everywhere except where stated.

| File | Its notation | Meaning | In the paper's convention |
|---|---|---|---|
| `paper/main.tex` (read only) | `a_0`; `a_ℓ^sm`; `b_ℓ(C)`; `S_1`; `K(F)` | `a_0` = total `t^0` coefficient; `(4πt)^{-1} Σ a_ℓ^sm t^ℓ` smooth part; `S_1 = Σ m_i` | `a_0 = c_2`; `a_ℓ^sm = Area · α_ℓ`; `S_1 = P_1`; `K(F) = K_iso(F;𝒫_3)` |
| `main.tex`, Section 5 | `σ(p,q,r) = (S_1, R)` | a two-coefficient key | **different object** from `σ(O) = (g; m)`; write `key_2(p,q,r) = (S_1, R)` in the rewrite |
| `theory/definitions.tex` | `c_j`, `H_k`, `K_iso`, `K_mult`, `σ(O)` | as section 1 | the reference |
| `theory/audibility` | `I_n(m)`, "the first `n` heat coefficients", "the `t^{-1}` coefficient"; `e_k`, `f`, `p(z)`, `Δ_j` | `I_n = (R, P_1, P_3, …, P_{2n−3})`; no `c_k` is named | first `n` coefficients `(c_1, …, c_n)` ↔ `I_n`; `c_j` ↔ `P_{2j−3}`; `R` ↔ `c_1`. `Δ_j` is a Hurwitz minor |
| `theory/cone-coefficients` | `c_l^S(π/k)`, `b_l`, `κ`, `k` | Uçar's lune coefficient (4.25); `b_l/κ^l` is `b_ratio(l,k)`; `κ = K`; `k = m` | `c_l^S(π/k)` is an intermediate, not a heat coefficient; `b_l(m)` as in section 1 with `κ = K`, so `b_l = (−1)^l b_ratio` at `K = −1` |
| `theory/signatures` | `c_1 = s/2`, `c_{l+2} = α_l Area + C_l`; `H_k`; `heat_key(g,m,k) = (s, C_0, …, C_{k−2})` | same indexing as the paper; `C_l = Σ_i b_l(m_i)`; first entry of `heat_key` is `s = 2c_1` | `c_j` same; `α_l^{sig} = α_{l+1}/(4π)` (it multiplies `Area`, the paper's `α_{l+1}` multiplies `Area/4π`); `heat_key[0] = 2c_1`, `heat_key[1+l] = C_l = c_{l+2} − (Area/4π)α_{l+1}` |
| `theory/locality` | `c_1 = Area/4π`, `c_j = α_{j−1} Area/4π + Σ β_{j−2}(m_i)`; `α_k`, `β_k` | same indexing; **`β_k(m)` is signed**: `β_k = b_k` at `K = −1` | `α_k` same as paper; `β_k^{loc} = b_k = (−1)^k β_k` |
| `theory/stability` | `H_ν` (`ν ≥ −1`), `H_{−1}`, `α_j`, `b_ν(m) = (−1)^ν p_ν(m)/m`, `I_n`, `heat_direct(m,N)` | `H_ν` is the **`t^ν`** coefficient: `H_{−1}` is `t^{−1}`; `heat_direct` returns `[H_{−1}, …, H_{N−2}]` | `H_ν = c_{ν+2}`; `α_j`, `b_ν` same as the paper. Genus 0 only (area `(n − 2 − R)/2`) |
| `theory/threshold` | `S`, `p`, `R^±_{S,p}`, `φ_p`, `τ_p`, `S*(p)` | pure triple arithmetic; no heat coefficients. "two coefficients" = `(c_1, c_2)` ↔ `(R, S)` | `S = S_1 = P_1`; `R^±` are values of `R`; `τ_p` stays (as in `main.tex`) |
| `theory/curvature` | `b_ℓ(m) = K^ℓ (1/m) p_ℓ(m)`; `b_ucar(l,m)`, `c_ucar`; `K_mult(𝒞)` | `b_ucar(l,m)` returns `b_l/K^l` (no sign); "first `k` coefficients" as in Theorem A | `b_ucar = β_l`; `b_l = K^l b_ucar`; `K_mult(𝒞) = K_mult(·;𝒞)`; coefficients `c_1, …, c_k` |
| `theory/divergence` | `a_ℓ`, `β_ℓ(m)`, `b_ℓ = K^ℓ β_ℓ`; `coeff_hyperbolic(l, cones, genus)`; `s_k` | `a_ℓ` = **total** `t^ℓ` coefficient (`ℓ ≥ 0`); **`β_ℓ` is unsigned** (`β_ℓ = p_ℓ/m > 0`); `s_k` = unit-sphere series | `a_ℓ = c_{ℓ+2}`; `β_ℓ` same as the paper; `c_1 = |χ|/2` is not returned |
| `theory/diophantine` | `t = (p,q,r)`, `e_1, e_2, e_3`, `S = e_1`, `R = e_2/e_3`, `λ = SR`, `C_λ`; "sharing `a_0` and `a_1`" (RECOMMENDATION.md) | no heat coefficients; "`a_0`, `a_1`" is loose for the first two coefficients | "sharing `a_0` and `a_1`" = sharing `(c_1, c_2)` = sharing `(R, S_1)`; rename `λ → Λ`, `t → x` (section 4) |
| `numerics/theory.py` | `coef[ν]` (`ν = −1, 0, 1, …`), `a_smooth_over_vol(ν)`, `b_cone(ν,k)`, `c_ν` of `D(t)` | `coef[ν]` is the `t^ν` total coefficient; `c_ν` = `t^ν` coefficient of `D(t)` | `coef[ν] = c_{ν+2}`; `a_smooth_over_vol(ν) = α_ν`; **numerics `c_ν = d_{ν+2}`** |
| `numerics/heat_trace.py`, `validate.py`, `REPORT.md` | `c1, c2, c3` ; `a0`, `a1`; `a, b, c0` (Weyl terms) | `D(t)/t = c1 + c2 t + c3 t² + …`; `a0, a1` = `t^0`, `t^1` totals of one pillow; Weyl `a = A/4π`, `b = ±L/4π`, `c0 = a0/2` | `c1, c2, c3` = `d_3, d_4, d_5`; `a0 = c_2`, `a1 = c_3`; Weyl `c0` is half of `c_2` of the pillow, a constant of one triangle, not a heat index |
| `numerics/moduli` | `a0 = 7/9` for `(0;3,3,3,3)`; `H(τ)`; `K(t,x,x)` | `a0` = Weyl constant = total `t^0` coefficient; `H` = geodesic (hyperbolic) term; `K(t,x,x)` = heat-kernel diagonal | `a0 = c_2 = 7/9`; `H` → `Hyp(ϑ)` and `K(t,x,x)` → `𝔥_t(x,x)` (section 4); `τ` → `ϑ` |
| `code/orbifold_enum.py`, `verify_identities.py` | `area_over_pi`, `signature` `(S_1, num, den)`, `cone(m)`, `a0_of` | `area_over_pi = Area/π`; `signature` = `key_2`; `cone(m) = (m² − 1)/(12m)`; `a0_of` = `χ/6 + Σ cone` | `c_1 = area_over_pi/4`; `cone(m) = b_0(m)`; `a0_of = c_2` (triples) |
| `review/claim-ledger.md`, `convention-note.md` | `a_0`, `K(F)`, `σ = (S_1,R)`, `N(S)` | as `main.tex` | as `main.tex` |

## 4. Symbol collisions, and the paper's choice

Found by reading every `.py`, `.md` and `.tex` under `theory/`, `numerics/`, `code/`, `review/` and the
macro-level notation of `paper/main.tex`, and then grepping for each symbol. The rule for the choice is:
a symbol keeps its global meaning (the one used in theorem statements); every other use is renamed to a
symbol that occurs nowhere else in the repository. Section 5 asserts that the new symbols are indeed free.
"Local" means the symbol appears only inside one proof or script, is defined there at first use, and does
not occur in a statement; local uses are left alone.

| Symbol | Meanings found (file) | Kept for | Renamed to |
|---|---|---|---|
| **`c_1, c_2, c_3`** | heat coefficient, index 1 = `t^{−1}` (`definitions.tex`, `signatures/sig_common.py`, `locality/proof.md`); **coefficients of `D(t)`**, `c_ν` = `t^ν` (`numerics/theory.py:25`, `heat_trace.py:151,222`, `REPORT.md:7`); sign constant `c_n` of `det M` and the Jacobian constant `c_n`, row coefficient `c_r` (`audibility/proof.md:66,124,202`, `verify_elimination.py:23`); Uçar's lune coefficient `c^S_l` (`stab_common.py`, `theory.py`, `ucar-source.md`); Weyl constant `c0` (`heat_trace.py:47`) | `c_j` = heat coefficient | `D(t)` coefficients → `d_j` (numerics `c1, c2, c3` = `d_3, d_4, d_5`); `det M` constant → `ς_n`; Jacobian constant and row coefficient → `ϖ_n`, `ϖ_r`; `c^S_l` always carries its superscript and is not a heat coefficient; the Weyl constant is written `c_2/2` |
| **`K`** | Gauss curvature (`audibility/proof.md`, `signatures/proof.md`, `curvature/proof.md`, `divergence/proof.md`); `K_iso`, `K_mult` (`definitions.tex`); `K(F)` (`main.tex:103`); `K_n(O)`, `K_g(O)` (`signatures/area_classes.py:9,11`); heat kernel `K(t,x,x)` (`moduli/kernel.py`); the log exponent `K` in `S(log S)^K` (`diophantine/RECOMMENDATION.md:81`); function field `K` in `E(K)` (`diophantine/novelty.md:30`); `κ = K` (`stability/proof.md:48`, `ucar-source.md`) | `K` = Gauss curvature; `K_iso`, `K_mult`, `K(F)` | `K_n, K_g` → `K_mult^{(n)}, K_mult^{(g)}` (the class as superscript); heat kernel → `𝔥_t(x,y)`; log exponent → `𝔮`; function field → `𝕂` |
| **`Δ`** | Laplacian (`definitions.tex`, `locality/proof.md`, `geometry.py:14`); Hurwitz determinant `Δ_j` (`audibility_common.py:6`, `audibility/proof.md:23`); genus difference `Δ = g − g'` (`heat_structure.py:11`); differences `ΔR, ΔP_1, ΔH` (`stability/proof.md`, `REPORT.md`); discriminant of the cubic (`variety.md:49`); triangle group `Δ(p,q,r)` (`theory.py:178`); triangle Laplacians `Δ_N, Δ_D` (`REPORT.md` §1) | `Δ` = Laplacian (`Δ_N, Δ_D` on the triangle) | Hurwitz minors → `𝔇_j`; genus difference → `δg`; differences of invariants → `δR, δP_1, δH`; discriminant → `Disc`; triangle group → `Γ(p,q,r)` |
| **`R`** | `Σ 1/m_i` (everywhere); the endpoints `R^±_{S,p}` (`threshold.py`: they are values of `Σ 1/m_i`); `R(U)` for padded multisets (`signatures`); a cutoff radius `R` (`locality/proof.md:290–295`) | `R = Σ 1/m_i` and its values `R^±_{S,p}` | cutoff radius: local to the locality proof, written `r_cut` there |
| **`S`** | `S_1 = Σ m_i` (`main.tex`, `code/`); `S = e_1` (`threshold`, `diophantine`); a Hurwitz matrix `S` (`stab_common.py:276`); the class `Sig` and "Theorem S" (`signatures`) | `S := S_1 = P_1` | the Hurwitz matrices of `stability` are local (`B`, `S` there); signature class stays `Sig` |
| **`P_j`** | power sums (everywhere); the class of pillows `𝒫`, `𝒫_n` (`definitions.tex`, `locality`); the polynomial `P(z) = (z+1)^m − (z−1)^m` (`main.tex:185`); `Pillow.P(k)` (`code`); the cone polynomial `p_l(m)`; the characteristic polynomial `p(z)` (`audibility`); `p` = least order of a triad, `p` = FEM order (`numerics/solve.py`) | `P_j = Σ m_i^j` (`P_1 = S`), `𝒫` classes, `p_l(m)` cone polynomials, `p` least order of a triad | audibility's `p(z)` → `χ_m(z)`; the FEM order is a code variable (`order`), not in the paper; `main.tex:185`'s `P(z)` is left as is (local to §2.2) |
| **`e_k`** | elementary symmetric functions (`audibility`, `stability`, `diophantine`); scaled `ê_k = e_k/μ^k` (`stability/proof.md:68`); the error vector `e` of one sector (`moduli/analysis.py:130`); the exponential factor `e = np.exp(−Λt)` of the tail bounds (`heat_trace.py:63`, `moduli/analysis.py:117`) | `e_k` = elementary symmetric functions | the last two are code variables (not in the paper); eigenvalue errors are written `err_j` |
| **`κ`** | curvature (`stability/proof.md:48`, `ucar-source.md`, `KAPPA`); condition number `‖M(Î)⁻¹‖` and amplification `κ_r` (`stability/proof.md:130,203,219,309`); monomial coefficient in `Q(z) − Q(−z) = 2κz³` (`audibility/proof.md:74,198,238`); the log exponent `κ = 4.5 ± 0.5` (`RECOMMENDATION.md:17`) | none: the paper writes `K` for the curvature, and `κ` is not used | condition number → `cond(M)`; amplification → `amp_r`; monomial coefficient → `ϰ`; log exponent → `𝔮` |
| **`λ`** | eigenvalue `λ_j` (everywhere); `λ(t) = S·R` (`diophantine/variety.md:14`); `λ_μ` (`stability/proof.md:306`); `λ_ℓ = |B_{2ℓ+2}|/…` (`divergence/proof.md:103`) | `λ_j` = eigenvalue | the invariant `S·R` → `Λ` (the curve `C_Λ`, e.g. `C_{27/2}`); `λ_μ` and `λ_ℓ` are local to their proofs (weights `w_ℓ` in the divergence proof) |
| **`T`** | the triangle `Triangle(p,q,r)` (`geometry.py`, `theory.py`); Teichmüller space `T(O)` (`locality/proof.md:155`); tanh series `T(z)` (`audibility_common.py:96`, `stab_common.py:188`); `T*` (`signatures`); time grid `T_GRID` (`heat_trace.py`) | none (time is lower case `t`) | triangle → `T_{p,q,r}`; Teichmüller space → `Teich(O)`; `T*` → `N^*`; the tanh series and the time grid are code names |
| **`t`** | time; the triple `t = (p,q,r)` (`variety.md:10`); the pencil parameter `t = 1 − λ` (`variety.md:38`); `t_0`, `t^*` | `t` = time | triple → `x = (p,q,r)`; pencil parameter local to `variety.md` |
| **`τ`** | modulus of the quadrilateral family (`moduli/REPORT.md`); `τ_p = (p−1)/(p(p+1))` (`threshold.py`, `main.tex`, `verify_identities.py:454`); Weierstrass coordinate (`variety.md:44`) | `τ_p` (as in `main.tex`) | the modulus → `ϑ` (data files keep `tau`); the Weierstrass coordinate is local to `variety.md` |
| **`σ`** | signature `σ(O) = (g; m)` (`definitions.tex`); the pair `σ(p,q,r) = (S_1,R)` (`main.tex:279`) | `σ(O) = (g; m)` | the pair → `key_2(p,q,r)` |
| **`a`, `α`, `b`, `β`** | `a_ℓ^sm`, `a_0` (total `t^0`), `a_ℓ` (total `t^ℓ`, `divergence`), Hurwitz `a_0 … a_n` (`audibility`), Weyl `a` (`heat_trace.py`), triangle side `a`; `α_j` per `Area/4π` (`stability`, `locality`, `theory.py`), `α_l` per `Area` (`signatures`), triangle angle `α`; `b_ℓ(m)` signed (`stability`, `signatures`), `β_k` signed (`locality`), `β_ℓ` unsigned (`divergence`), Weyl `b`, triangle side `b` | `a_ℓ^sm = Area·α_ℓ`; `a_0 = c_2`; `α_j` per `Area/4π`; `b_ℓ` signed; `β_ℓ = b_ℓ/K^ℓ` unsigned | `divergence`'s `a_ℓ` → `c_{ℓ+2}`; `signatures`' `α_l` → `α_{l+1}/(4π)`; `locality`'s `β_k` → `b_k = (−1)^k β_k`; Hurwitz coefficients and triangle sides/angles are local (code and `audibility_common.py`) |
| **`ν`** | heat index (`stability`, `theory.py`); `ν = n + 2g` (`sig_common.py:21,81`) | heat index only in files that follow `H_ν` | `ν = n + 2g` → `ν_g`; in the paper the heat index is `l` |
| **`l`, `ℓ`** | heat index; closed geodesic length (`locality`, `moduli`, `heat_trace.geodesic_term`); rotation index in `θ_l = πl/m` | heat index `l` | geodesic length `ℓ`; rotation index `j`, angle `θ_{m,j} = πj/m` |
| **`n`, `k`, `m`** | `n` = number of cone points, but also `ν = n + 2g`, an eigenvalue count (`n = len(lam)` in `heat_trace.py`), a sphere `(n,n)`; `k` = cone order in Uçar's formulas (`cS(l,k)`), a scale, a heat index, `H_k` | `n` = number of cone points; `m_i` = cone order; `k` = number of coefficients (`H_k`) | Uçar's `k` (cone order) → `m`; eigenvalue counts are `N(λ)` |
| **`g`, `χ`, `s`** | genus; a metric; Fourier `g(u)`; `G_k`, `g_N`; spectral gap `g_a`; `χ(O)`, a cutoff function `χ`; `s = Area/2π`, a power sum `s_j`, sphere coefficients `s_k`, a sign `s = ±1` (`heat_trace.py:43`) | `g` = genus; `χ` = orbifold Euler characteristic; `s = Area/2π = 2c_1` | the rest are local to their proofs (the Fourier transform of the heat test function is `ĥ`, the unit-sphere series coefficients `s_k` stay in `divergence`) |
| **`H`, `h`** | tuple `H_k = (c_1,…,c_k)` (`definitions.tex`); `H_ν` = `t^ν` coefficient (`stability`); geodesic term `H(τ)` (`moduli/analysis.py`); test function `h(r)`; test harness `H` (`verify_identities.py:99`) | `H_k = (c_1,…,c_k)` | `H_ν = c_{ν+2}`; the geodesic term is `Hyp(ϑ)`; `h(r)` unchanged |
| **Filenames** | two scripts named `threshold.py`: `theory/threshold/threshold.py` (sum threshold `S*(p)`) and `theory/stability/threshold.py` (error threshold `δ*`) | both stay | cite as `threshold/threshold.py` and `stability/threshold.py` |

## 5. Verification of the translations

`python3 theory/conventions_check.py` recomputes, for the five signatures `(2,8,8)`, `(3,3,12)`,
`(3,10,15,30)`, `(1;15)` and `(0;3,3,5,5)`, the first four coefficients `c_1, …, c_4`

* from the reference formulas of section 1, retyped in the script from the Selberg identity term and Uçar
  (4.25)/(4.33) (and cross-asserted against Uçar (4.35), which the files use);
* from each file's own functions, through the translation of section 3:
  `stability/stab_common.heat_direct` (`H_ν = c_{ν+2}`) and its blocks `alpha_smooth`, `b_cone`;
  `signatures/sig_common.heat_key` (`s = 2c_1`, `C_l`); `divergence/divergence.coeff_hyperbolic`
  (`a_ℓ = c_{ℓ+2}`); `curvature/curvature_checks.b_ucar` (`b_l = (−1)^l b_ucar`);
  `cone-coefficients/verify_cone_coefficients.b_ratio`; `numerics/theory.pillow_coeffs` (`coef[ν] = c_{ν+2}`)
  and its blocks `a_smooth_over_vol`, `b_cone`; `audibility` (`I_n` through `audibility_common` Newton identities,
  then the affine map `c = L I_4 + h_0` of `stability/stab_common.front_end`); `code/orbifold_enum.area_over_pi`
  (`c_1 = area_over_pi/4`) and `code/verify_identities.a0_of` (`c_2`); and `locality/check_locality`
  (its cyclotomic evaluation of the elliptic Taylor coefficients equals `b_ν`, which the other rows tie to
  the reference);
* that every replacement symbol of section 4 (`d_j`, `ς`, `ϖ`, `ϰ`, `𝔮`, `ϑ`, `𝕂`, `𝔥_t`, `𝔇`, `δg`, `N^*`, `key_2`, `Hyp`, `cond`)
  occurs nowhere else in the text files of the repository (`conventions_check.py`, `check_free_symbols`);
* the numerics pair: `d_3 = 25/12`, `d_4 = −1775/24` (numerics `c1`, `c2`), with `d_1 = d_2 = 0`.

Every row is an `assert`; a file whose own function does not cover a signature (`heat_direct` is genus 0,
`pillow_coeffs` is for triples) prints `skip` for that cell and is tested through its building blocks
instead. Result at the time of writing: 45 comparisons pass, 5 skip, 0 fail
(run by `code/run_all.sh`).
