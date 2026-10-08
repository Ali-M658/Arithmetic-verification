# STATUS: variable curvature (theory/varcurv), 2026-10-08

## Verdict

**Proved.**
- **The structure survives, the factorisation does not.** At a cone point of order m, the order-t^l term
  is still sum_{i<=l+1} beta_{l,i}(p) Pi_i(m), with exactly one new odd power m^{2l+1} per order (VC1, for
  m >= l-1). But the coefficient of the new power is (|B_{2l+2}|/(2l+2)!) beta_{l,l+1}(p) with
  beta_{l,l+1} = 4^l l! [v^{2l}](f^{-1})' = (2l)!K^l/l! + ... + 2(-Delta)^{l-1}K/(l-1)!.
  So from t^2 on it contains Delta^{l-1}K(p) with nonzero coefficient (VC2). This is already visible as
  -m^5 Delta K/15120 in Schueth's Thm 4.1.
- **The suggested ansatz fails.** "K^l p_l(m)/m with derivative terms at lower powers of m" holds only for
  l = 0, 1.
- **A new closed form at t^3:** a_3(p) = A(m)K^3 + B(m)K Delta K + D(m)Delta^2 K for all m >= 2 (VC3).
- **Extension.** If K = kappa != 0 to order 2L-6 at every cone point and the smooth parts S_l are known,
  Paper A's reduction (Lemma sigdata) holds verbatim, and so do its counts (VC4).
- **Finite-order obstruction.** Without the smooth parts, nothing survives at finite order beyond c_2.
  For every L, two signatures carry metrics, of constant curvature kappa near the cone points, with
  equal c_1..c_{L+2} if and only if their c_2 values agree (VC5).
- **All-order obstruction.** Explicit metrics, flat near the cone points, give O(2,8,8) and O(3,3,12)
  identical heat invariants to all orders (VC6). This is Paper A's own minimal pair.

**Open.**
- The lower coefficients beta_{l,i} for l >= 4.
- Non-radial terms at small m (they do occur at l = 4, m = 2).
- Whether c_2 alone always allows agreement to all orders.
- Whether such pairs can be isospectral.

**Recommendation.** Add a ~1.5-page subsection "Variable curvature" to Paper A, made of one proposition on
cone terms, one proposition with three parts (extension / finite-order obstruction / all-order
obstruction), and a closing paragraph. Text: `paperA-insert.tex`. It argues that constant curvature is
the right setting because there the smooth part is fixed by the area.

## Exact statements

The statements are in `statements.tex` (corrected after the attack), with proofs in `varcurv.tex`:

| | statement | status |
|---|---|---|
| VC1 | a_l(p) = sum_{i=1}^{l+1} beta_{l,i} Pi_i(m), for m >= max(2, l-1); m Pi_i is an even polynomial of degree 2i with leading coefficient abs(B_{2i})/(2i)! | proved (Lemmas pole/radial plus Donnelly's form) |
| VC2 | beta_{l,l+1} = 4^l l! [v^{2l}] rho_u' averaged over directions; consequences (i)-(iv); explicit for l <= 7 | proved; explicit values computed (`top_coefficient.py`) |
| VC3 | b_3(phi) and a_3(p) closed forms | computed exactly (`twisted_mp.py`), independently reproduced by the attacker |
| VC4 | extension in the class K = kappa != 0 to order 2L-6 (and the common-J version for L <= 5); fails for kappa = 0 | proved |
| VC5 | finite-order iff c_2 | proved |
| VC6 | all-order pairs, under sum(1-1/m) and sum(m-1/m) equal and > 1 | proved, explicit |
| VC5a | second variation, F_n = (-1)^n n(n-1)n!/(2n+1)! | proved (Duhamel); sign convention fixed after the attack |

**Computed by one method only, not a theorem.** The full radial b_4 from `attack/ATTACK-REPORT.md`; its
top part agrees with VC2(iii).

**Task 1 (closed forms known).** The table is in varcurv.tex Section 1:
- t^0: any cone, (1/12)(m - 1/m).
- t^1: [(m^3 - 1/m)/360 + (m - 1/m)/36] K (DGGW).
- t^2: K^2 and Delta K, with coefficients of degree m^5 (Schueth 2019).
- All orders at constant curvature (Ucar).
- Non-orbifold curved cones: t^{1/2} and t log t terms, irrational in the cone angle (Schueth 2026).

## Files

| file | content | runtime |
|---|---|---|
| `SOURCES.md` | fetched statements (sha256 of PDFs) | |
| `statements.tex` | statements only (input to the attack) | |
| `varcurv.tex` | statements and proofs (LaTeX fragment, compiles standalone) | |
| `paperA-insert.tex` | recommended text for Paper A (about 1.5 pp) | |
| `twisted_mp.py` | MP-recursion computation of b_0..b_3 and a_0..a_3 | ~4.5 min |
| `top_coefficient.py` | beta_{l,l+1} for l <= 7, its checks, Paper A leading coefficients | ~50 s |
| `quadratic_form.py` | F_n and its normalisation checks | ~10 s |
| `obstruction_check.py` | VC4-VC6 arithmetic: 383 VC6 pairs, D_l, Vandermonde | ~3 min |
| `attack-log.md`, `attack/` | adversarial check | |

Every script uses exact arithmetic with asserts, and every `*_output.txt` ends in "ALL ASSERTS PASSED".
