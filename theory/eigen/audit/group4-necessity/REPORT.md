<!-- Returned text of the blind reviewer for Group 4 (necessity), saved verbatim by the main session: the reviewer could not write report files. Its four check scripts are in this directory and raise on failure. -->

# Blind referee report: Group 4 (necessity)

| item | grade |
|---|---|
| (eig:rayleigh) | NONE |
| eig:233 (input: cone ball, systole) | NONE |
| eig:N1 | MINOR (strictness in the pigeonhole step) |
| Construction of Q_{k,b}, O_{k,b} | MINOR (the justification of the interior angle is incomplete) |
| eig:N2, the two bounds | NONE |
| eig:N2, the final "in particular" | SERIOUS (true, but it says nothing about the systole hypothesis) |
| "What is not proved" | SERIOUS (the opening sentence overclaims; there are also three MINOR inaccuracies) |

## 1. Identity (eig:rayleigh): NONE

**Derivation.** Put f = w^{-1/2}u. Expanding both sides gives q = w''/(2w) − w'²/(4w²). Since w'' = w, this is q = 1/2 − (w'/w)²/4:
- w = sinh: q = 1/4 − 1/(4 sinh²ρ);
- w = cosh: q = 1/4 + 1/(4 cosh²ρ).

The angular factor (2π/m on the cone, 4b on the collar) multiplies both integrals and cancels.

**Code.** `check_symbolic.py` (1) checks the identity exactly in sympy for both weights.

## 2. eig:N1: MINOR

**Test functions.** Split (0, h_m) into j+1 intervals of length L = h_m/(j+1), with a sine function on each.
- Near the cone point f ~ c ρ^{1/2}, and |f'|² sinh ρ → c²/4 is bounded. So f ∈ H¹ and f(0) = 0.
- The boundary term −(coth ρ/2)u² tends to 0 and ∫q u² converges. So the limit a → 0 is legitimate.
- The supports are disjoint, so the Rayleigh quotient of any combination is at most the largest single quotient.
- Each quotient is strictly less than 1/4 + π²(j+1)²/h_m². The span has dimension j+1, so the indexing (λ_0 = 0) is right.

**The input h_m.** The triangle has its right angle at the order-2 point Q, so PQ is itself the perpendicular from P to the opposite side. Hence cosh PQ = cos(π/3)/sin(π/m), which gives h_m, and the open ball B(P, h_m) is an embedded cone.

**Pigeonhole.** For j < N and m ≥ 7, λ_j ≤ Λ_N because h_m increases with m. Only the N−1 coordinates j ≥ 1 vary, so K = ⌈Λ_N/δ⌉^{N−1} boxes are enough.

**Issue N1-1 (MINOR).** The stated bound is "≤". At m = 7 and j = N−1 it equals Λ_N exactly. If Λ_N/δ is an integer, two values in the closed last box can differ by exactly δ, not by "< δ".
- **Fix:** state that the Rayleigh bound is strict (q < 1/4) and use half-open boxes. Alternatively, take c = ⌊Λ_N/δ⌋ + 1.

**Decision rule.** The data λ̃ = spectrum of O(2,3,m) are δ-approximations of both spectra, and the two signatures differ. So the conclusion about decision rules follows. Remark eig:Mneeded is supported.

**Code.**
- `check_symbolic.py`: the sine quotient is π²/L²; H¹ and the boundary term at the cone point; h_m ≥ log(m/2π) and h_m increasing for m = 7..1999.
- `check_geometry.py`, in PSL(2,R) with words of length ≤ 24: d(P, Q) = h_m to 1e-15, and min over gP ≠ P of d(P, gP) = 2h_m for m ∈ {7..13, 15, 20, 30, 50, 100, 1000}.
- `check_fem.py`: finite elements for m = 7, 10, 20, 50 and j = 1..5. Every eigenvalue is below its bound, for example λ_1(O(2,3,50)) ≈ 1.94 against 5.42. The bounds are valid but loose.

**eig:233.** Nothing suspicious:
- σ_0 = 0.5620668712…, which matches the printed value.
- The least translation lengths found are 0.98399 at m = 7 and 1.2659 at m = 8, increasing to 1.92481 at m = 1000. That matches the modular surface's 2 arccosh(3/2) and is well above σ_0.
- The area formula is verified exactly.

## 3. Construction of Q_{k,b} and O_{k,b}: MINOR

**Derivation.**
- For every b > 0 there is a unique a > 0 with sinh a sinh b = cos(π/k).
- In the Klein model, Q_{k,b} is simply the Euclidean rectangle [−tanh b, tanh b] × [−tanh a, tanh a]. This is a useful simplification.
- Each quarter is a Lambert quadrilateral, so all four interior angles are π/k.
- The area is 2π(2 − 4/k) ≤ 2π.
- With Fermi coordinates x(ρ, s) = (cosh ρ sinh s, sinh ρ, cosh ρ cosh s):
  - ⟨x, n_P⟩ = cosh ρ sinh(s − b), so the side s = b is exactly the line P.
  - ⟨x, n_R⟩ ≤ 0 is equivalent to tanh ρ ≤ cosh s tanh a, so the rectangle lies in Q.
  - The vertex has ρ_V > a, so the collar contains no cone point.
  - Reflection in P is s ↦ 2b − s, so doubling gives a smooth collar {|ρ| < a} × R/4bZ.
- The core geodesic has length 4b. It separates, because the underlying space is a sphere.
- τ (reflection in β) is an isometry of the double that reverses orientation and exchanges the two discs.

**Issue C-1 (MINOR).** The fact |⟨n_P, n_R⟩| < 1 fixes the angle between the lines only up to φ ↔ π − φ. It does not show the *interior* angle is π/k.
- **Fix:** cite the Lambert relation cos φ = sinh a sinh b (acute fourth angle), or orient the normals.

**Code.** `check_geometry.py` checks k = 3, 4 at 48 values of b ∈ [1e-4, 5], at 40 digits: the interior angle from tangent vectors equals π/k to 1e-20, the vertex has ρ_V > a, 41×41 sample points of the rectangle lie in Q, and the reflection is s ↦ 2b − s.

## 4. eig:N2

**λ_1 bound (NONE).** Take f = ρ on the collar and ±a on the two discs. It is in H¹ and odd under τ, so it is orthogonal to the constants.
- ∫|∇f|² = 8b sinh a.
- ∫f² ≥ 8b((a²+2) sinh a − 2a cosh a), which is positive.
- The ratio is exactly the stated bound, and it behaves like 1/a².

**λ_j bound (NONE).** Use sines on [a/2, a), where q ≤ 1/4 + 1/(4 cosh²(a/2)); the Dirichlet quotient is 4π²(j+1)²/a². The bound is correct. Using both sides of the collar would improve the last term to π²(j+1)²/a²; this is cosmetic.

**Class membership.** The membership claims hold, and "for j ≤ 1" means j ∈ {0, 1}. The claim as stated is true.

**Code.**
- `check_symbolic.py` checks the integrals exactly.
- `check_fem.py` (k = 3, 4; b ∈ {0.5, 0.2, 0.1, 0.05}): every eigenvalue is below its bound, for example λ_1 ≈ 0.082 against 0.202 at k = 3, b = 0.05.
- At b = 0.05, λ_2 ≈ 1.12 (k = 3) and 0.93 (k = 4), still above 1/4.

**Issue N2-1 (SERIOUS: the claim is true but says less than it suggests).** The same conclusion holds at a *fixed* systole, and even with exact equality:
- Q is symmetric in a ↔ b, so λ_1(O_{k,b}) → 0 both as b → 0 and as b → ∞.
- λ_1 is positive and continuous in b.
- By the intermediate value theorem, λ_1(O_{3,b}) = λ_1(O_{4,b'}) exactly for some b, b' in a fixed compact interval, where the systole is ≥ some ε_0 > 0.
- The finite-element numbers agree: for b ∈ [0.2, 0.5], λ_1 ranges over [0.54, 2.52] for k = 3 and [0.30, 1.23] for k = 4, which overlap.

So (λ_0, λ_1) fail to determine the signature inside a single class Cl(2π, ε_0, 4). This only shows that N = 2 eigenvalues are too few, which Theorem E never claims. It says nothing about whether the systole hypothesis is needed.
- **Fix:** delete the "in particular", or reword it as: "pinching gives λ_1 → 0; λ_0, λ_1 already fail at fixed systole, so this does not bear on the necessity of ε."

## 5. "What is not proved": SERIOUS

1. **(SERIOUS)** "N2 shows only that the first two eigenvalues … cannot replace a systole bound" is not shown, by N2-1. Group 4 contains no necessity result for ε at all.
   - **Fix:** say that N2 does not address necessity of the systole bound and only shows λ_1 → 0 under pinching.
2. **(MINOR) The growth claim is wrong.** The text says N grows "roughly like 1/ε²". But y_0 contains 3D, and D ∝ 1/ε (r_0 = ε/4, v_0 ∝ r_0²). So t_3 ∝ ε³ and N ∝ ε^{-3} log(1/ε).
   - `check_growth.py` evaluates the exact formulas of eig:E with A = 2π, M = 4. It gives D = 128/ε and a growth exponent of 3.14, 3.11, …, 3.05 for ε = 1e-2 … 1e-7, and 3.031 at ε = 1e-12. A = π/3, M = 7 gives the same.
   - **Fix:** replace "1/ε²" with "ε^{-3} log(1/ε), since D ∝ 1/ε".
3. **(MINOR)** "Equivalently: whether N must grow" is not equivalent to the full analogue. The analogue only says (N, δ) cannot be uniform in ε; that could also happen with δ(ε) → 0 and N fixed.
   - **Fix:** "whether (N, δ) can be chosen independently of ε".
4. **(MINOR)** "requires … no eigenvalues in (0, 1/4]" overstates. It is one sufficient route; matching small eigenvalues of the two limits would also do, and (0, 1/4) suffices.
   - **Fix:** "one route is…".

**Is a stronger statement easy?** No. On these four-point spheres at most one eigenvalue tends to 0. For fixed A and M, the number of small eigenvalues stays bounded, so any N ≥ 3 analogue needs the lower bound λ_j ≥ 1/4 − o(1) that the paragraph names. Bracketing the collar and the two discs gives no useful bound on λ_2. A bound of Otal–Rosas type for orbifolds would be a candidate, but I have not verified one. Apart from items 1 and 2, nothing in Group 4 claims more than is proved.

## Files
- `check_symbolic.py`: the identity, the integrals, H¹ at the cone point, h_m, areas, σ_0.
- `check_geometry.py`: Q_{k,b} and O(2,3,m) geometry and the systole search (about 3 minutes).
- `check_fem.py`: coarse finite-element eigenvalues against the claimed bounds (about 4 minutes).
- `check_growth.py`: the pigeonhole count and the growth of N(ε).

**Overall verdict:** every bound and construction in Group 4 is correct, with two MINOR fixes (pigeonhole strictness, angle justification). But eig:N2's "in particular" and the first sentence of "What is not proved" claim a necessity of the systole bound that is not shown, because two eigenvalues already fail at fixed systole. The stated growth N ~ 1/ε² should be ε^{-3} log(1/ε).
