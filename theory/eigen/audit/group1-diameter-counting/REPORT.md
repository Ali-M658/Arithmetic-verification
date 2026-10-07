<!-- Returned text of the blind reviewer for Group 1 (diameter and counting), saved verbatim by the main session: the reviewer could not write report files. Its scripts are in this directory and raise on failure. -->

# Blind referee report, Group 1: diameter and counting

**Overall verdict:** all eight statements in Group 1 are correct as stated. I found nothing FATAL, SERIOUS or MINOR. Three advisory notes remain, for eig:sep, eig:233 and eig:hypall.

**What I read.** Only `STATEMENTS.md` (Sections A, B and Group 1 of C) and `sources/`. I did not see the authors' proofs, so every derivation below is my own, built from the permitted inputs.

**Scripts.** All five run with the scratchpad venv python, use checks that raise on failure, and each finished in under 3 minutes.

| script | what it checks | result |
|---|---|---|
| `trig_check.py` | (H1); (H2)+(H3) through rotation products in SL(2,R), both orientations; (H3) directly in the hyperboloid model (intersection, same side, all three angles); the Section B commutator identity, including its sign | passes on 600 + 2000 + 2000 + 1000 random cases at 40 digits |
| `sep_exhaustive.py` | the worst case allowed for eig:sep, for every M ≤ 70 and 2 ≤ m_p ≤ m_q ≤ M | passes on 57,080 cases. The smallest ratio of (cosh d − 1) to 2/(π²M²) is **9.76**, at M = 7, orders (2,3) |
| `group_enum.py` | 269 triangle groups (p ≤ q ≤ r ≤ 12) and 12 quadrilateral groups O_{k,b}: eig:sep, plus eig:diam by sampled diameter on 30 triangle orbifolds | passes. Smallest d_min/d₀ is **3.11**. Diameters are far below D (for O(2,3,7): 0.58 against 29.3) |
| `o233.py` | σ₀, s_m, h_m; a search for short geodesics in O(2,3,m) for m = 7..150; distance from each axis to the order-3 points; the Jørgensen quantity; the cone ball | passes. Shortest length found is 0.98399 (m = 7), above σ₀ = 0.562067. Over 9,000 axes checked |
| `elem_count.py` | eig:elem (exact enumeration of 1.28M signatures, quadrature); eig:counttail on synthetic spectra; both elementary steps of eig:hypall; B decreasing in ℓ; the constants 21 and 42/√π in eig:count; the closed form of eig:diam on an (ε, M) grid | passes |

## Lemma eig:sep — NONE

**My proof.** Take the two rotations counterclockwise: by 2α = 2π/m_p about p̃ and by 2β = 2π/m_q about q̃. Rotating in the same direction is exactly the "same side" configuration of (H3), which I checked numerically. Put X = sin α sin β cosh d − cos α cos β.
- **X > 1.** The product ab is hyperbolic with length 2h, where cosh h = X ≤ cosh d. So d ≥ ε/2.
- **X = 1.** The product would be parabolic, which cannot happen in a cocompact group.
- **X < 1.** ab is a rotation by 2θ = 2πk/m_r with m_r ≤ M, so θ lies in [π/M, π − π/M].
  - The triangle has positive area, so θ < θ₀ = π − α − β.
  - θ₀ − θ is π times a positive fraction whose denominator divides m_p·m_q·m_r. So θ₀ − θ ≥ π/(m_p·m_q·m_r).
  - By the mean value theorem, sin α sin β (cosh d − 1) = cos θ − cos θ₀ ≥ sin(π/M)·π/(m_p·m_q·m_r).
  - Using m·sin(π/m) ≤ π and sin(π/M) ≥ 2/M, this gives **cosh d − 1 ≥ 2/(πM²)**.

This is stronger than the stated bound by a factor of π. The hypotheses cover every case:
- no cone points (the lemma is vacuous);
- M = 2 (then X = cosh d > 1);
- two points in the same orbit;
- orientation of the rotations;
- parabolics (excluded by cocompactness).

**Advisory.** If the authors argue through the "nearly cancelling" products a^i·b^(−j), they only get roughly cosh d − 1 ≳ π²/(N²M) with N = m_p·m_q. That is too weak for large M and would be a gap. The triangle-area argument above closes it.

## Lemma eig:balls — NONE

1. **An elliptic point p̃ lies within r₀ of the centre.** Then B(p̃, r₀) sits inside the ball. Its translates are disjoint by eig:sep, so it projects to a cone of area at least 2π(cosh r₀ − 1)/M.
2. **Every elliptic point is farther than r₀.** By (H1) and sin(πk/m) ≥ sin(π/M), each rotation moves the centre by at least 2ρ₁. A hyperbolic element moves it by at least ε ≥ 2ρ₁. So B(x̃, ρ₁) embeds.

The two cases are exhaustive: the boundary case d = r₀ belongs to case 1.

## Theorem eig:diam and its closed form — NONE

Put points at spacing 4r₀ along a minimising path. The balls of radius 2r₀ around them are disjoint, so (k+1)·v₀ ≤ A, which gives diam < 4r₀A/v₀.

**Closed form.**
- arccosh(1 + 2/(π²M²)) ≥ 3/(5M), so max(4/ε, 10M/3) ≥ 2/d₀.
- First term: d₀M/(cosh r₀ − 1) ≤ 8M/d₀.
- Second term: d₀/(cosh ρ₁ − 1) ≤ 2M²/d₀, because ρ₁ ≥ 2r₀/M (Jordan's inequality and convexity of sinh).

The grid check finds the ratio of D to the closed form approaches 1 as ε → 0 with M = 2, and never exceeds it.

## Proposition eig:233 — NONE (advisory note)

**Area and distances.**
- Area = 2π(1/6 − 1/m), which is less than π/3.
- The law of cosines gives d(P₂, P₃) = s_m and d(P₂, P_m) = h_m.

**Systole ≥ σ₀.**
- The P₂P₃ edges form a tree that splits the plane into regular m-gons. Their vertices are order-3 points and their edges have length 2s_m.
- A geodesic axis cannot stay inside a compact m-gon, so it crosses an edge, within s_m of an order-3 point.
- With the order-3 rotation there, ⟨γ, β⟩ is non-elementary. Jørgensen's inequality and the commutator identity (sign checked: tr[γ,β] − 2 = +4 sinh²(L/2) sin²(φ/2) cosh²r) give 4 sinh²(L/2)(1 + ¾cosh²r) ≥ 1.
- With r ≤ 2s_∞ and cosh 2s_∞ = 5/3, this gives L ≥ σ₀ = 0.5620668….

**Diameter and cone ball.**
- diam ≥ h_m ≥ log(m/2π).
- The disc of radius h_m around P_m is the m-gon's inscribed disc, which embeds as a cone.

**Advisory.** The bound r ≤ 2s_m is valid but wasteful: the argument gives r ≤ s_m, and that improves the constant to σ = log 2 ≈ 0.693. If the written proof justifies "2s_m" by saying every point of the plane is within 2s_m of an order-3 point, that is false: points near P_m are more than h_m away, and h_m → ∞. The argument has to be about axes.

## Lemma eig:elem — NONE

**(i)**
- Area/π ≥ 4g − 4 + n, because each 1 − 1/m ≥ 1/2. That gives n + 4g ≤ Area/π + 4.
- The minimum area is π/21, at (0; 2,3,7), by the usual case analysis. The enumeration confirms both claims.

**(ii)**
- Both terms are positive.
- E_m(t) ≤ Σ 1/(4m sin²(πj/m)) = (m² − 1)/(12m) = b₀(m), by the beta integral at s = 0.
- I(t) ≤ e^(−t/4)·A/(4πt), from ∫|r|e^(−tr²) dr = 1/t.

## Proposition eig:counttail — NONE

These are standard one-line bounds, all checked:
- the counting bound Z(1/x) ≥ e⁻¹·N(x);
- the tail bound;
- the index statement: if N ≥ e·Z(1/Λ), then λ_j > Λ for all j ≥ N.

## Proposition eig:hypall — NONE (advisory note)

**My route reproduces the stated constant exactly.**
1. Use ℓ(γ₀) ≤ x and 2 sinh(x/2) ≥ e^(x/2)(1 − e^(−ℓ)).
2. Sum e^(−2x) over the closed geodesics. Integrating by parts against the decreasing function e^(−2x), with n(x) ≤ Ke^x, gives at most 2Ke^(−ℓ).
3. Using y·e^(−y²/2) ≤ e^(−1/2) and max(3x/2 − x²/8t) = 9t/2 gives x·e^(3x/2)·g_t(x) ≤ e^(17t/4 − 1/2)/√π. The bound is nearly attained at t = 1/9 (ratio 0.99999).

**Advisory.** Integrating by parts against f(x) = x·e^(−x/2)·g_t(x) instead would be invalid when ℓ is small compared with t. f is not decreasing there, so n ≤ Ke^x cannot be substituted. The stated constant matches the valid route.

## Theorem eig:count — NONE

- I ≤ A/(4πt).
- E ≤ n_*·b₀(M) = β_M: b₀ is increasing in m, and n ≤ ⌊A/π⌋ + 4.
- **Small t.** t ≤ ε²/(2(1+ε)) implies t ≤ ℓ²/(2(1+ℓ)), since u²/(2(1+u)) is increasing. Lemma hypbound then applies. B grows with the diameter and falls with ℓ (re-checked on 800 grid points), so ℓ can be replaced by ε and the diameter by D. Area ≥ π/21 gives the factor 21.
- **Large t.** eig:hypall, with e^(−ℓ)/(1 − e^(−ℓ)) decreasing in ℓ, gives 42/√π.
- The counting and tail statements follow from eig:counttail.

H jumps at the threshold, which is harmless because each branch is a valid bound on its own range.

Files in this directory: trig_check.py, sep_exhaustive.py, group_enum.py, group_enum.out, o233.py, elem_count.py.
