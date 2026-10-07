<!-- Returned text of the blind reviewer for Group 5 (locality), saved verbatim by the main session: the reviewer could not write report files. Its check script is check_locality.py in this directory (prints ALL CHECKS PASSED). -->

**Grade: MINOR.** I found no mathematical error in Theorem eig:loc. There are three wording or presentation points.

I read only `STATEMENTS.md` and `sources/`. The sources only cover Jørgensen's inequality, which this group does not use.

## Derivation in brief

Let O1 and O2 have signature σ, with A = Area (fixed by σ through eq:area) and M = max m_i (or 2 if there are no cone points). Let ℓ = min(ℓ1, ℓ2).

1. **Both orbifolds are in C(A, ℓ, M).**
   - The area is A ≤ A, each systole is ≥ ℓ, and every cone order is ≤ M. M is an integer ≥ 2 in both cases.
   - With no cone points, the cone-order condition is vacuous, so "put M = 2" is legitimate.
   - eig:sep, eig:balls and eig:diam are stated for every member of the class. None of them assumes cone points exist.
   - With M = 2, eig:balls gives ρ1 = r0 and v0 = π(cosh r0 − 1). This is consistent: it is well below the area of an embedded ball of radius d0 ≤ ℓ/2.
2. **The two systole definitions agree.** The class uses the least translation length of a hyperbolic element. thm:quantlocality uses "all closed geodesics, including those through cone points". The notation paragraph defines both as the same thing, so using ε = ℓ (the smaller systole) for both orbifolds is correct.
3. **Diameter.** eig:diam gives max diam_i < D(A, ℓ, M).
4. **Monotonicity.**
   - thm:quantlocality(a) gives |Z1 − Z2| ≤ B(ℓ, max diam, t).
   - B is a positive factor times e^{3·diam}, so it increases strictly with diameter. The area inside B is the same A for both orbifolds.
   - I re-proved that B decreases in ℓ: on the range, d log B/dℓ' ≤ −1/2 − 1/(e^{ℓ'} − 1) − 2t/(ℓ'² − t²) < 0. The t-range for ℓ sits inside the range for every ℓ' ≥ ℓ.
5. **The bound B ≤ C·t^{-1/2}·e^{-ℓ²/4t} holds on the whole range.**
   - The ratio is exactly B / (C·t^{-1/2}·e^{-ℓ²/4t}) = (ℓ+t)/(ℓ−t) · (2+ℓ)/(2+3ℓ).
   - This increases with t and equals 1 at t = ℓ²/(2(1+ℓ)), with t < ℓ throughout.
   - The e^{3D} factor cancels, so replacing the diameter by D is harmless.
6. **Dependence.** A and M are determined by σ, so C depends only on (σ, ℓ).

## What the code checked

- **Symbolic (sympy):** the exact ratio formula, ratio = 1 at t_max, and ℓ − t_max > 0.
- **Decrease in ℓ:** B and d log B/dℓ' were checked at 3300 points: ℓ from 1e-3 to 30, t/t_max from 1e-6 to 1, ℓ' up to 6.9ℓ. Range nesting was checked at the same points.
- **The full inequality chain:** checked at 50 digits on 9 signatures × 7 systoles × 4 values of t, together with increase in diameter and equality at the endpoint.
  - Signatures: surfaces of genus 2 and 3 (M = 2), (2,3,7), (2,3,1000), (2,2,2,3), (1;2), (0;2,2,2,2,2), (5;2,50).
  - Systoles: 1e-4 to 8, including σ0 and 3.0571.
- **Sanity checks of D (Group 1 owns its proof):**
  - D ≤ the stated crude bound.
  - D ≥ arccosh(1 + A/2π), the trivial lower bound on any diameter.
  - D(π/3, σ0, m) ≥ log(m/2π) for m from 7 to 10⁴, consistent with eig:233.
  - D(4π, ε, 2) is non-increasing in ε.
- **Sample magnitudes:**

| Case | D | C |
|---|---|---|
| Genus 2, ℓ = 3.057 | ≈ 201.5 | ≈ 7×10^262 |
| Genus 2, ℓ = 0.1 | ≈ 1280 | ≈ 3×10^1666 |
| (2,3,7), ℓ = σ0 | ≈ 29.3 | ≈ 2×10^39 |

I found no counterexample.

## Issues

1. **MINOR (wording).** "Depends only on the signature and the systole" is ambiguous when two orbifolds are involved.
   - *Fix:* "…only on the signature and on ℓ = min(ℓ(O1), ℓ(O2))."
2. **MINOR (presentation).** The M = 2 convention for surfaces is legitimate but costly. It caps d0 at arccosh(1 + 1/(2π²)) ≈ 0.317 even when ℓ/2 is much larger, so a genus-2 surface has D ≈ 201.5 and C ≈ 10^262. That is correct but useless as a number.
   - *Fix:* add a sentence saying the convention only makes the class definition apply.
   - *Optional:* note that for surfaces d0 = ℓ/2 could be used, if Group 1's proof allows it.
3. **MINOR (presentation).** Because diam < D strictly, the first inequality is actually strict; the second is an equality at the right endpoint. The constant e^{3D} is astronomically large, and eig:233 shows D must grow at least like log M.
   - *Fix:* add a remark that the constant is qualitative, as thm:quantlocality(b) already says for C.

I found nothing FATAL or SERIOUS. Class membership, the agreement of the systole definitions, the no-cone-point case, monotonicity in diameter and in ℓ, the bound on the whole range including the endpoint, and the dependence claim all hold.

**Overall verdict: Theorem eig:loc is correct as stated; the issues are wording only (grade MINOR).**
