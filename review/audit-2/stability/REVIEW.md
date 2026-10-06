# G5-bis blind review: group `stability`

Bundle: `review/audit-2/statements/stability.md` (SB.0, SB.0b, SB.1, SB.2, SB.3, SB.4). Context read, as the
bundle allows: `review/audit/statements/stability.md` (ST.0–ST.14). That includes ST.11, Theorem S4, the
explicit formula for δ_thm.

All code is my own, written from the statements: `stab610.py` (library), `check_setup.py`, `check_cert.py`,
`check_probes.py`, `check_ladder.py`, `check_dup.py` (exact, assert-based, exit nonzero on failure), and
`search_dup.py` (numerical search, not a certificate; its output feeds `check_dup.py`). Every `.txt` file was
produced by `python3 check_x.py > check_x.txt` with `/opt/homebrew/Caskroom/miniforge/base/bin/python3`
(sympy 1.14). All exit 0.

## Summary table

| id | statement | grade |
|---|---|---|
| R1 | SB.2 steps 1–3: Δ = \|F⁻¹\|δ; τ^lin, τ^rem, τ; ρ_j, ρ^rem_j; Δ_M; A = \|M⁻¹\|Δ_M; the claims \|T̃−T\| ≤ τ, \|r\| ≤ ρ, \|r_rem\| ≤ ρ^rem, \|δM\| ≤ Δ_M | **NONE** |
| R2 | SB.2: J = ∂(Me−b)/∂I and G = −M⁻¹JF⁻¹ | **NONE** |
| R3 | SB.2: "Steps 4 and 5 are unchanged, with ρ in place of \|r\|"; \|ϱ\| ≤ \|M⁻¹\|ρ^rem + AE | **MINOR** (notation: ρ means three things; wording below) |
| R4 | SB.1 Prop. S5 tests (i) and (ii), including the radius ladder | **NONE** (the ladder reading is unambiguous; optional wording below) |
| R5 | SB.3 claim after Table 4 | **MINOR** (false as worded: sech²U and sec²U are even, with s₀ = 1; "after z⁷" should be "after z^{2n−3}") |
| R6 | SB.4 δ_cert column (11 rows) | **NONE**: every printed value certifies (all by test (ii)) and each is the 4-s.f. maximum |
| R7 | SB.4 δ_thm column (11 rows) | **NONE**: recomputed from the Theorem S2/S3/S4 constants, equal to the 3-s.f. round-down, certifies |
| R8 | SB.4 ε_cert column (11 rows) | **NONE**: every value certifies (test (ii)) and each is the 2-s.f. maximum |
| R9 | SB.4 column δ_cert/\|H_ν\| | **MINOR**: (2,3,7), ν = 0 prints 4.0e−03; with the printed δ_cert it is 3.999e−03, so 3.9e−03 rounded down |
| R10 | SB.4 / ST.13 δ_up column, ratio, "failure built at" | **MINOR**: all 11 printed δ_up are valid failure bounds, and 10 are reproduced. For (2,2,2,2,3) the best failure is at **5.312e−05** (ratio **6.72**), not the printed 5.743e−05 (7.26). This is G5 item 8, still not applied |
| R11 | Validity of the bounds themselves (task 4: probes, U ≥ 0, J) | **NONE**: 26,924 exact probes, 0 violations, 0 recovery failures |

No FATAL or SERIOUS finding. Every printed δ_cert, δ_thm and ε_cert certifies under the Prop. 6.10 formulas, and each is the round-down maximum.

## Contamination

None. I opened only REVIEWER-BRIEF.md, `review/audit/G5-VERDICT.md`, my bundle,
`review/audit/statements/stability.md` (allowed by the bundle), and the fetched Uçar text in
`review/audit-2/sources/`. I did not open `theory/**`, `paper/**`, `review/audit/stability/**` or any other
session's scripts or outputs. The G5 verdict's P3 line and item 8 state a prior δ_up bound for (2,2,2,2,3)
(5.312e−05, ratio 6.72). I read it as part of the required reading. My search did not use it; R10 reports what
my own search found.

## Instrument gaps

See `fetches.md`. In short: (1) Theorem B's M(I), b(I) is not in the bundle. I reconstructed it and verified the
reconstruction exactly against Lemma S2.2 and Lemma S2.1. (2) The cross-reference "Proposition 6.2" in SB.3
cannot be resolved without the manuscript. (3) Lemma S3 and Theorem S2 are used, not re-proved. δ_thm is
recomputed from them and certified independently by Prop. S5. No network fetch was needed.

---

## 0. Reconstruction of Theorem B (needed by every result; not in the bundle)

Data from the bundle:
- Setting: R = Σ1/m_i = e_{n−1}/e_n, from H₋₁ = (n−2−R)/2.
- Prop. 6.10: U(z) = Σ_k P_{2k−1} z^{2k−1}/(2k−1). Hence U = Σ_i artanh(m_i z) with P_j = Σ_i m_i^j.
- Lemma S2.2: f(z) = ∏(1+m_i z) = E(z²) + zO(z²).

Since tanh(Σ artanh x_i) = (∏(1+x_i) − ∏(1−x_i))/(∏(1+x_i) + ∏(1−x_i)), we get **T = tanh U = zO(z²)/E(z²)**.
Comparing the coefficients of z^{2j+1}, 0 ≤ j ≤ n−2, in E·T = zO, and adding R e_n = e_{n−1}, gives a linear
system in e₁, …, e_n. The sign convention is fixed by J_{n−1,0} = −e_n and by the minus sign in J_{j,k}:

- row j ≤ n−2: e_{2j+1} − Σ_{i<j, 2j−2i≤n} T_{2i+1} e_{2j−2i} = T_{2j+1} (the e_{2j+1} term is absent if 2j+1 > n);
- row n−1: e_{n−1} − R e_n = 0.

So M has 1 in column e_{2j+1}, −T_{2i+1} in column e_{2j−2i}, and −R in row n−1, column e_n; also b_j = T_{2j+1}
and b_{n−1} = 0. This is exactly the support described for Δ_M. `check_setup.py` §1–2 verifies the
reconstruction exactly on 41 multisets (the 11 rows and 30 random rational multisets, n = 2..6):

- S·M = B, with S and B as defined in Lemma S2.2;
- det M = (−1)^{n(n+1)/2} ∏(m_i+m_j)/e_n (Lemma S2.1) and det B = (−1)^{n(n−1)/2}∏(m_i+m_j);
- the exact solve returns e;
- the composed series tanh U equals zO/E.

The front end F = L is the inverse of the ST.2 table of L⁻¹. The offset is h₀ = ((n−2)/2)(1, α₁, …). In
`check_setup.py` §3, H_ν rebuilt from Uçar (4.25), (4.33), (4.35) (fetched text, κ = −1, genus 0) equals
F·I + h₀ exactly:
- for the 11 rows and 80 random integer multisets;
- the α_j of (4.35) are 1, −1/3, 1/15, −4/315, 1/315.

The ST.2 row sums ℓ = (2, 14, 498, 4062, 56230/3) and the diagonal (2, 12, 360, 2520, 10080) are confirmed. The
diagonal equals 2(ν+1)!(2ν+1)/|B_{2ν+2}|.

## R1. Prop. 6.10 steps 1–3. Grade NONE

**Derivation.** Fix radii δ = (δ_ν), ν = −1..n−2, and data with |δH_ν| ≤ δ_ν.

*Step 1.* δI = F⁻¹δH, so |δI_k| ≤ (|F⁻¹|δ)_k = Δ_k. Then δU = Σ_k δI_k z^{2k−1}/(2k−1) is dominated
coefficientwise by |δU| := Σ Δ_k z^{2k−1}/(2k−1).

*Step 2.* Let tanh x = Σ h_k x^k and tan x = Σ t_k x^k. Then t_k ≥ 0 and |h_k| = t_k, because
tanh x = −i tan(ix). In formal power series with U(0) = δU(0) = 0, Taylor's formula is exact:
tanh(U+δU) − tanh U = Σ_{l≥1} tanh^{(l)}(U) δU^l / l!.

- The l = 1 term is sech²U·δU. Hence |[z^k](sech²U·δU)| ≤ (|sech²U| ∗ |δU|)_k = τ^lin_k.
- For l ≥ 2: tanh^{(l)}(x)/l! = Σ_p h_p C(p,l) x^{p−l}. U has nonnegative coefficients (P_j > 0 for positive
  m), so every U^{p−l} has nonnegative coefficients, and |[z^k] tanh^{(l)}(U)/l!·δU^l| is at most
  [z^k] tan^{(l)}(U)/l!·|δU|^l.
- Summing over l ≥ 2 gives [z^k](tan(U+|δU|) − tan U − sec²U·|δU|) = τ^rem_k.

So |T̃_k − T_k| ≤ τ_k, and the part beyond first order is bounded by τ^rem_k. Here sec²U is the series
1 + tan²U, which has nonnegative coefficients. The hypothesis U ≥ 0 is only a convenience: in general replace
U by |U| in the tan terms.

*Step 3.* Put r := b̃ − M̃e, with e the true vector. From the row formulas:
- r_j = Σ_{i=0}^{j} δT_{2i+1} e_{2j−2i} for j ≤ n−2, where e_k = 0 for k > n handles the restriction 2j−2i ≤ n;
- r_{n−1} = δR·e_n.

Since e_k ≥ 0 for positive m, |r_j| ≤ Σ τ_{2i+1} e_{2j−2i} = ρ_j and |r_{n−1}| ≤ Δ₀e_n = ρ_{n−1}. The
first-order part of r is −JδI. The remainder r_rem = r + JδI equals Σ_i (δT − sech²U·δU)_{2i+1} e_{2j−2i}, so
|r_rem| ≤ ρ^rem (and the last row's remainder is 0). Finally δM has −δT_{2i+1} in row j, column e_{2j−2i}
(i < j, 2j−2i ≤ n), and −δR in row n−1, column e_n. Hence |δM| ≤ Δ_M.

**Counterexample hunt.** In `check_probes.py`, every probe checks each of |δI| ≤ Δ, |δT| ≤ τ,
|δT − sech²U·δU| ≤ τ^rem, |r| ≤ ρ, |r_rem| ≤ ρ^rem and |δM| ≤ Δ_M exactly. That is 26,924 probes on the
11 rows and 9 extra cluster multisets (n = 3, 4, 5), in these families:
- all 2ⁿ corners;
- gradient directions ±δ·G_j/max|G_j| and ±δ·sign(G_j);
- linear root-push corners ±δ·sign(p_c(a±1/2));
- random interior points and random face points;
- the absolute model at δ_cert and δ_thm, the relative model at ε_cert, and 1.001·δ_cert.

Result: 0 violations. The bound is sharp in the e₁ component: e₁ = P₁, so E₁ = 14δ is attained at a corner and
max |ẽ₁−e₁|/E₁ = 1.

**Hypothesis U ≥ 0** (`check_setup.py` §6): U_k = P_k/k > 0 for every positive multiset. It holds wherever
the proposition is applied.

## R2. J and G. Grade NONE

**Derivation.** Differentiate row j of Me − b at fixed e: ∂/∂P_{2k−1} of −Σ_{i≤j} T_{2i+1}e_{2j−2i}, with
∂T_{2i+1}/∂P_{2k−1} = [z^{2i+1}](sech²U·z^{2k−1})/(2k−1) = s_{2i+2−2k}/(2k−1). This is nonzero only for
i ≥ k−1, which gives the printed J_{j,k}. Rows j ≤ n−2 do not involve R, so J_{j,0} = 0. Row n−1 is
e_{n−1} − Re_n, which gives J_{n−1,0} = −e_n and J_{n−1,k} = 0. By the implicit-function theorem applied to
M(I)e(I) = b(I), D_Ie = −M⁻¹J. So G = (D_Ie)F⁻¹ = −M⁻¹JF⁻¹, which agrees with SB.1's G = (D_Ie)L⁻¹.

**Checks.**
- `check_setup.py` §5: the printed J equals the sympy Jacobian of M(I)e − b(I) identically in symbols
  (e, R, P), for n = 2, 3, 4, 5, 6.
- G equals the exact difference quotient of the exact recovery map (h = 10⁻³⁰, error < 10⁻²⁰) for every
  column and all 11 rows.

## R3. Steps 4–5 and the ϱ bound. Grade MINOR (notation only)

**Derivation.** A ≥ 0. If (I−A)v = 𝟙 with v > 0, then Av = v − 𝟙 < v, so ρ(A) ≤ max_i (Av)_i/v_i < 1
(Collatz–Wielandt). It follows that:
- (I−A)⁻¹ = Σ A^k ≥ 0;
- ρ(M⁻¹δM) ≤ ρ(|M⁻¹||δM|) ≤ ρ(A) < 1, so M̃ = M(I + M⁻¹δM) is invertible.

From M̃(ẽ−e) = r we get d = M⁻¹r − M⁻¹δM·d. So (I−A)|d| ≤ |M⁻¹|ρ, and therefore |d| ≤ E. Splitting
r = −JδI + r_rem gives d = GδH + ϱ with ϱ = M⁻¹r_rem − M⁻¹δM·d. Hence |ϱ| ≤ |M⁻¹|ρ^rem + AE. The probes
check |d| ≤ E and |d − GδH| ≤ |M⁻¹|ρ^rem + AE exactly (0 violations).

**Defect (wording).** The symbol ρ has three meanings in the text that Prop. 6.10 now joins:
1. the radii ρ_ν of Prop. S5 ("|H̃_ν − H_ν| ≤ ρ_ν", step 1 "|L⁻¹|ρ", test (ii) "Σ_c ρ_c");
2. the residual bound ρ_j of Prop. 6.10;
3. the spectral radius ρ(A).

Prop. 6.10 calls the radii δ ("Δ = |F⁻¹|δ"). Read literally, "Steps 4 and 5 are unchanged, with ρ in place of
|r|" puts the residual bound in step 5, which is correct. But test (ii)'s "Σ_c ρ_c" must then mean the
H-radii δ_c, not ρ_j. The text also uses both L and F for the front-end matrix.

**Replacement text** (end of Prop. 6.10): "Steps 4 and 5 are unchanged, with ρ in place of |r|. In test (ii),
the first-order term is Σ_c δ_c Σ_l |p_c^{(l)}(a)/l!| r^l, where δ_c are the data radii (written ρ_c in
Proposition S5); |ϱ| ≤ |M⁻¹|ρ^rem + AE; and G = −M⁻¹J F⁻¹ (F = L of Proposition S1), where J = ∂(Me−b)/∂I at
fixed e is …". In Prop. S5, rename the data radii from ρ_ν to δ_ν throughout.

## R4. Prop. S5, tests (i) and (ii), and the ladder. Grade NONE

**Derivation.** Suppose step 4 succeeds. On |z−a| = r with r < min_{b≠a}|a−b|:
- |q(z)| = ∏_b |z−b|^{k_b} ≥ r^{k_a} ∏_{b≠a}(|a−b|−r)^{k_b};
- q̃(z) − q(z) = Σ_{j=1}^{n}(−1)^j d_j z^{n−j}, and |z| ≤ a + r.

(i) |q̃−q| ≤ Σ_j E_j(a+r)^{n−j}.

(ii) q̃ − q = Σ_c δH_c p_c(z) + Σ_j (−1)^j ϱ_j z^{n−j}, with |p_c(z)| ≤ Σ_l |p_c^{(l)}(a)/l!| r^l.

A strict inequality in either test gives |q̃−q| < |q| on the circle. By Rouché, q̃ then has exactly k_a zeros in
the open disc |z−a| < r. For integer orders and r ≤ 1/2, the open discs are disjoint, because distinct centres
are at least 1 apart. Since Σk_a = n, these are all the roots, and every root satisfies |Re z − a| < 1/2.
Rounding therefore returns m.

Test (ii) can be applied to some orders and test (i) to others; both conclusions are per order. In practice
every row passes test (ii) at every order, so no mixing is needed.

The hypotheses used are: integer orders (for the rounding conclusion); every ladder radius ≤ 1/2 < gap; and the
strict inequality. All are in the statement or implied by the ladder.

**Ladder.** "{1/2, 19/40, …, 1/40, 1/100, 1/1000}" can only be read as {k/40 : k = 20, 19, …, 1} ∪ {1/100,
1/1000}, which is 22 radii. The step 19/40 − 1/2 = −1/40 reaches 1/40 after 19 steps. A geometric reading
(ratio 19/20) never hits 1/40 (`check_ladder.py` (a)). So the reading is not ambiguous.

The result is also insensitive to the ladder. A ladder 10× finer ({k/400} ∪ {1/1000}) raises the certified sup
by at most 0.02% ((3,3,4,4): 9.59730e−05 → 9.59950e−05). None of the printed 4-s.f. values changes, except that
(3,3,4,4) would become 9.599e−05 (`check_ladder.py` (b)).

The first passing radius at the printed δ_cert is 1/2 for the binding orders. Test (ii) needs 19/40 or 17/40
only at non-binding orders ((4,5,21,28): 5; (2,3,7): 3; (3,3,4,4): 3; (2,2,2,3): 3; (2,2,2,2,3): 3).

**Optional wording:** "r ∈ {k/40 : 1 ≤ k ≤ 20} ∪ {1/100, 1/1000}".

## R5. SB.3 claim. Grade MINOR

"for n ≤ 5 every series is truncated after z⁷ and has at most four nonzero (odd) coefficients."

- Truncation is after z^{2n−3}, which is z³, z⁵, z⁷ for n = 3, 4, 5. "After z⁷" is correct only as an upper
  bound.
- U, |δU|, T, tan U, τ^lin, τ^rem, τ are odd, with at most four nonzero coefficients (`check_setup.py` §6).
- But **sech²U = 1 − T² and sec²U are even series with constant term 1.** They enter τ^lin, τ^rem and J, so
  "(odd)" is false for them. For (2,2,2,2,3), sech²U = 1 − 121z² + 9328z⁴ − 601472z⁶.
- "Proposition 6.2" could not be resolved (instrument gap).

**Replacement:** "Every entry of the δ_cert column can be re-derived from Proposition 6.2 and the formulas above
in exact rational arithmetic. For n ≤ 5, every series is truncated after z^{2n−3} (at most z⁷). The odd series
U, |δU|, T, tan U, τ^lin, τ^rem have at most four nonzero coefficients (z, z³, z⁵, z⁷), and the even series
sech²U = 1 − T² and sec²U = 1 + tan²U have at most four (1, z², z⁴, z⁶)."

## R6–R9. Re-certification of the printed table (`check_cert.py`)

| m | δ_cert printed | passes (test, radius at binding order) | next 4-s.f. value | 4-s.f. max: (i) / (ii) | 6-s.f. sup | δ_thm printed = recomputed (binding term) | ε_cert printed / 2-s.f. max (4-s.f.) |
|---|---|---|---|---|---|---|---|
| (2,8,8) | 2.341e−03 | (ii), r = 1/2 | 2.342e−03 fails | 2.683e−04 / 2.341e−03 | 2.34171e−03 | 3.80e−07 = 1/2629632 (r_a, a = 8) | 1.9e−03 / 1.9e−03 (1.944e−03) |
| (3,3,12) | 4.040e−03 | (ii), 1/2 | 4.041e−03 fails | 9.484e−04 / 4.040e−03 | 4.04017e−03 | 1.18e−07 = 1/8408448 (a = 3) | 4.4e−03 / 4.4e−03 (4.491e−03) |
| (3,10,15,30) | 3.660e−03 | (ii), 1/2 | 3.661e−03 fails | 7.433e−05 / 3.660e−03 | 3.66010e−03 | 4.02e−11 (a = 10) | 8.7e−04 / 8.7e−04 (8.707e−04) |
| (4,5,21,28) | 1.461e−03 | (ii), 19/40 at a = 5 | 1.462e−03 fails | 4.582e−05 / 1.461e−03 | 1.46177e−03 | 3.14e−11 (a = 5) | 4.6e−04 / 4.6e−04 (4.627e−04) |
| (2,3,7) | 3.658e−03 | (ii), 17/40 at a = 3 | 3.659e−03 fails | 6.220e−04 / 3.658e−03 | 3.65881e−03 | 4.49e−07 = 1/2226168 (a = 3) | 5.0e−03 / 5.0e−03 (5.013e−03) |
| (4,4,4) | 4.539e−04 | (ii), 1/2 | 4.540e−04 fails | 5.928e−05 / 4.539e−04 | 4.53915e−04 | 9.35e−07 = 1/1069056 | 8.2e−04 / 8.2e−04 (8.259e−04) |
| (7,7,7) | 8.068e−05 | (ii), 1/2 | 8.069e−05 fails | 1.632e−05 / 8.068e−05 | 8.06865e−05 | 9.97e−08 = 1/10026576 | 1.2e−04 / 1.2e−04 (1.285e−04) |
| (3,3,4,4) | 9.597e−05 | (ii), 19/40 at a = 3 | 9.598e−05 fails | 5.660e−07 / 9.597e−05 | 9.59730e−05 | 1.48e−09 (a = 3, 4 tie) | 1.1e−04 / 1.1e−04 (1.185e−04) |
| (5,5,5,5) | 3.617e−05 | (ii), 1/2 | 3.618e−05 fails | 2.321e−07 / 3.617e−05 | 3.61790e−05 | 4.74e−10 = 1/2108058750 | 3.1e−05 / 3.1e−05 (3.149e−05) |
| (2,2,2,3) | 1.858e−04 | (ii), 1/2 at a = 2 | 1.859e−04 fails | 2.268e−06 / 1.858e−04 | 1.85881e−04 | 2.03e−09 (a = 2, 3 tie) | 4.3e−04 / 4.3e−04 (4.398e−04) |
| (2,2,2,2,3) | 7.908e−06 | (ii), 1/2 at a = 2 | 7.909e−06 fails | 1.188e−08 / 7.908e−06 | 7.90808e−06 | 2.72e−12 (a = 2, 3 tie) | 1.4e−05 / 1.4e−05 (1.466e−05) |

**R6 (δ_cert), NONE.** All 11 printed values certify, every one by test (ii) at every order, and each is the
4-s.f. maximum: the next 4-s.f. value fails both tests. Test (i) alone is weaker by a factor of 5 to 670, so
the column depends on test (ii). This should be said in the text (see "Wording" below).

**R7 (δ_thm), NONE.** δ_thm := min(1/λ_μ, 1/(2κζ_nλ_μ), min_a Q̂_a 2^{k_a−1}/(3ⁿ(2μ)^{k_a}·2κρ_nλ_μ)) is the
smallest δ at which some hypothesis of Theorem S3 fails. The last term is the rounding condition r_a ≤ 1/2;
for integer orders, μ·min(ĝ_a,1)/2 ≥ 1/2, so the radius hypothesis follows from it.

Recomputed exactly, with:
- κ = ‖M(Î)⁻¹‖_∞;
- ζ₃,₄,₅ = 1, 79/3, 14048/15;
- σ_k(n) from its definition (σ(4) = 1, 76/3, 6628/15 as printed);
- ρ_n(m̂) and λ_μ from ℓ.

In every row the binding term is a rounding term r_a, and the printed value is its 3-s.f. round-down. Each
printed δ_thm also passes both tests (i) and (ii) directly. Exact values: (3,10,15,30) 1001/24894183502800,
(4,5,21,28) 411125/13062458646372128, (3,3,4,4) 245/164770288128, (2,2,2,3) 625/307721117718,
(2,2,2,2,3) 350000/128215445811292593.

**R8 (ε_cert), NONE.** All 11 printed values certify under ρ_ν = ε|H_ν| by test (ii). Each is the 2-s.f.
maximum (the next value fails).

**R9 (relative-precision column), MINOR.** Rounded down from δ_cert/|H_ν|, 39 of the 40 entries match. The
exception is (2,3,7), ν = 0: 3.658e−03/0.914683 = 3.99920e−03, which rounds down to **3.9e−03**; the printed
value is 4.0e−03. All 40 entries equal the round-down of (unrounded sup δ)/|H_ν|, where the unrounded sup is
3.65881e−03 for this row. So the column was computed from the unrounded δ_cert, contrary to its caption
"δ_cert/|H_ν|" and to the round-down convention. The value 4.0e−03 is still a certified precision, because
4.0e−03·|H₀| = 3.6587e−03 < sup. **Replacement:** print 3.9e−03 for (2,3,7), ν = 0. Alternatively, caption the
column "computed from the unrounded δ_cert".

## R10. δ_up column (ST.13 construction; `search_dup.py`, `check_dup.py`)

**Grade: MINOR** (a printed constant; it was already a required change in G5-VERDICT item 8).

**Derivation of validity.** Let q̃ be any real monic polynomial with rational coefficients and a root (or a
complex pair) with real part exactly c = a ± 1/2, and suppose M(I(q̃)) is invertible. Then:
- the data H̃ := H(q̃) = F·I(q̃) + h₀ are exact rationals;
- Theorem B returns q̃ itself;
- moving the tied root (pair) to c ± ε changes H̃ by O(ε), and one of the two directions makes the rounded
  multiset differ from m.

So for every δ' > δ := ‖H̃ − H(m)‖_∞ there are data within δ' that recovery gets wrong. Hence the threshold
is at most δ. The printed value is valid if it is at least some such δ.

One subtlety the ST.13 text glosses over: the failing direction is not always "outward from a". At c = 2.5 for
(2,3,7), the tied root is the 3. Pushing it towards 3 recovers m; pushing it towards 2 fails. `check_dup.py`
therefore tries both directions. It decides failure exactly, with Routh–Hurwitz strip counts on the pushed
polynomial (push 10⁻²⁰, Δδ < 10⁻⁹δ), and cross-checks the count against the rounded multiset of g's roots, which
are also located exactly.

**Search.** `search_dup.py` minimises max_ν|H_ν(q̃) − H_ν(m)| numerically over both shapes, every distinct
order a, both signs, and 13–31 starts per case: Nelder–Mead, then an SLSQP epigraph step. `search_dup_deep.py`
adds 60 random cluster-splitting starts per case for (2,2,2,2,3), with real roots and complex pairs within 0.7
of the orders. Every minimiser was then rebuilt exactly in rationals by `check_dup.py`. For every candidate
(88 + 8 deep) the exact solve returns q̃, the tie is exact, and the exact push makes recovery fail.

| m | printed δ_up (built at) | best exact failure, rounded up (point, shape) | printed valid? | ratio best/δ_cert (printed) |
|---|---|---|---|---|
| (2,8,8) | 2.485e−03 (8−1/2) | 2.485e−03 = 2.4848623e−03 (15/2, real root) | yes, reproduced | 1.06 (1.06) |
| (3,3,12) | 4.589e−03 (3+1/2) | 4.589e−03 = 4.5882716e−03 (7/2, real) | yes, reproduced | 1.14 (1.14) |
| (3,10,15,30) | 7.488e−03 (10+1/2) | **7.487e−03** = 7.4865192e−03 (21/2, real) | yes (printed 1 unit loose) | 2.05 (2.05) |
| (4,5,21,28) | 2.018e−03 (5−1/2) | 2.018e−03 = 2.0176678e−03 (9/2, real) | yes, reproduced | 1.38 (1.38) |
| (2,3,7) | 6.587e−03 (3−1/2) | 6.587e−03 = 6.5869137e−03 (5/2, real) | yes, reproduced | 1.80 (1.80) |
| (4,4,4) | 5.036e−04 (4+1/2) | 5.036e−04 = 5.0358257e−04 (9/2, real) | yes, reproduced | 1.11 (1.11) |
| (7,7,7) | 8.273e−05 (7−1/2) | 8.273e−05 = 8.2721187e−05 (13/2, real) | yes, reproduced | 1.03 (1.03) |
| (3,3,4,4) | 1.195e−04 (4−1/2) | 1.195e−04 = 1.1943586e−04 (7/2, real; the crossing root is the second 3) | yes, reproduced | 1.24 (1.24) |
| (5,5,5,5) | 3.826e−05 (5−1/2) | 3.826e−05 = 3.8257987e−05 (9/2, real) | yes, reproduced | 1.06 (1.06) |
| (2,2,2,3) | 2.520e−04 (3−1/2) | 2.520e−04 = 2.5197149e−04 (5/2, real) | yes, reproduced | 1.36 (1.36) |
| **(2,2,2,2,3)** | **5.743e−05** (2+1/2) | **5.312e−05** = 5.3113199e−05 (5/2, real root; one 2 crosses to 3, the other roots round to 2,2,2,3) | yes, but **not the best** | **6.72** (7.26) |

The (2,2,2,2,3) value 5.3113199e−05 was found independently from both labels of the point 5/2 (a = 2, + and
a = 3, −), by both searches, from the natural start and from 60 random cluster splittings. The complex-pair shape
at 5/2 is much worse (8.53e−04), and so are 3/2 (1.5625e−04) and 7/2 (5.87e−03). I found nothing below
5.3113e−05. Since the search is numerical, this is the best upper bound I found, not a proven minimum.

**Required change:** in the (2,2,2,2,3) row, "5.743e-05 | 7.26" → "5.312e-05 | 6.72". The "failure built at"
2+1/2 is unchanged. Wherever the text quotes the ratio "7.26"/"7.3", replace it with "6.72"/"6.7".

**Optional changes:**
- (3,10,15,30): δ_up 7.488e−03 → 7.487e−03; the ratio stays 2.05.
- (3,3,4,4): "failure built at 4−1/2" → "3+1/2", because the crossing root is a 3. It is the same point, 7/2.
- In ST.13, add after "arbitrarily small further perturbations push the root across": "(in the direction away
  from the order whose root it is)".

## R11. Validity of the bounds (task 4). Grade NONE

`check_probes.py` (26,924 exact probes, 0 failures) checks every bound of R1 and R3. It also checks, exactly by
Routh–Hurwitz strip counts on q̃(z + a ± 1/2), that every probe inside a certified radius recovers m. This covers
the printed rows (at δ_cert, δ_thm and ε_cert) and 9 adversarial multisets: (2,2,2,2,2), (3,3,3,3), (2,3,3,3,3),
(6,6,6,6,6), (2,2,3,3,3), (3,3,3), (2,7,7), (2,2,2,2,7), (5,6,7,8,9). Each was probed at its own 4-s.f.
certified δ (all by test (ii), e.g. 8.442e−06 for (2,2,2,2,2)).

At 1.001·δ_cert, the certificate fails in all 11 rows but every probe still recovers. This is consistent with
δ_up > δ_cert. Both the hypothesis U ≥ 0 and the J formula hold (R1, R2).

## Wording changes collected

1. (R3) In Prop. 6.10, after "Steps 4 and 5 are unchanged, with ρ in place of |r|": "In test (ii) the
   first-order term is Σ_c δ_c Σ_l |p_c^{(l)}(a)/l!| r^l, with δ_c the data radii; …; G = −M⁻¹J F⁻¹, F = L."
   Rename the data radii of Prop. S5 from ρ_ν to δ_ν.
2. (R5) Replace the SB.3 sentence as given in R5.
3. (R9) (2,3,7), ν = 0: 4.0e−03 → 3.9e−03 (or re-caption).
4. (R10) (2,2,2,2,3) row: δ_up 5.743e−05 → **5.312e−05**, ratio 7.26 → **6.72** (also any "7.3" in the prose). Optional: (3,10,15,30) δ_up 7.488e−03 → 7.487e−03; (3,3,4,4) "4−1/2" → "3+1/2"; ST.13 "push the root across (away from the order whose root it is)".
5. (R6, recommended) After the table: "Every δ_cert and ε_cert is certified by test (ii); test (i) alone
   certifies only values 5 to 670 times smaller (e.g. 2.683e−04 for (2,8,8))."
