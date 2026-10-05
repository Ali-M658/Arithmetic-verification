# STATUS: theory/revision (response to G7-2, G7-3, G7-4, G7-7, G7-8, G7-15)

Each task has a LaTeX fragment and a verification script. The fragments use the manuscript's macros,
and every fragment compiles (`check_fragments.py`). Each fragment's first comment block says where it
goes in the paper.

`run_checks.sh` runs every script and exits nonzero on any failure. The last run was all PASS:

| Script | Checks |
|---|---|
| `check_lemma25.py` | 623 |
| `check_remark412.py` | 32 |
| `check_thm12iii.py` | 48 |
| `check_descent.py` | 49 |
| `check_thm513.py` | 59 |
| `check_remark212.py` | 27 |
| `check_prop610.py` | 39 |
| `check_point3P.py` | 10 |
| `check_sharpness.py` | 8 |
| `check_quotes.py` | 13 quotations |

All arithmetic is exact (`fractions.Fraction`, `sympy`), except where a numerical cross-check is labelled as one.

| Task | Status | Fragment | Script |
|---|---|---|---|
| 1. Lemma 2.5 for every order, without Uçar (G7-3) | **DONE** | `lemma25.tex` | `check_lemma25.py` |
| 2. Remark 4.12 corrected | **DONE** | `remark412.tex` | `check_remark412.py` |
| 3. Locality: classical vs new (G7-2) | **PARTIAL** (sources unreachable) | `locality.tex`, `locality-sources.md` | `check_quotes.py` |
| 4. Thm 1.2(iii): diameter and "attained" (G7-8) | **DONE** | `thm12iii.tex` | `check_thm12iii.py` |
| 5a. 2-isogeny descent, torsion (G7-4a) | **DONE** | `descent.tex` | `check_descent.py` |
| 5b. Thm 5.13, the 38 collision-free sums (G7-4b) | **DONE** (computational proposition) | `thm513.tex`, `collision_witnesses.csv` | `check_thm513.py` |
| 5c. Remark 2.12 (G7-4c) | **DONE**: cut to a short remark, proved | `remark212.tex` | `check_remark212.py` |
| 5d. Prop 6.10 explicit r_rem, \|δM\| (G7-4d) | **DONE** | `prop610.tex` | `check_prop610.py` |
| 6. The point 3P; ordered audit check (G7-15) | **DONE** | `point3P.tex`; `review/audit/diophantine/check_groups.py` | `check_point3P.py` |
| 7. Sharpness wording (G7-7) | **DONE** | `sharpness.tex` | `check_sharpness.py` |
| 8. Self-attack | **DONE** (13 findings, all fixed) | `attack-log.md` | — |

## 1. Lemma 2.5 for every order: DONE

**New proof.** Write θ_j = πj/m and put Φ_m(u) = Σ_j 1/(4m sin θ_j sin(θ_j − u)). This is the
elliptic weight of the trace formula, and it has the closed form

  Φ_m(u) = (cot u − m cot mu)/(4m sin u).

So the t^k Taylor data of E_m are Bernoulli expressions in m. Four facts follow:

- p_l(m) = 4^{−l} Σ_k (2k)!/(k!(l−k)!) · mφ_k(m).
- Each mφ_k(m) is a positive rational combination of m^{2n} − 1, for n ≤ k+1.
- Hence p_l is even, has degree exactly 2l+2, satisfies p_l(1) = 0, and has leading coefficient
  |B_{2l+2}|/(2(l+1)!(2l+1)).
- p_l(m) > 0 for m > 1.

The triangular expansion in odd power sums (Lemma 2.10, used by Theorems A–C) needs only these
properties, and is checked for l ≤ 40.

**Uçar as a cross-check.** The agreement with Uçar (4.25) + (4.33)–(4.34) is proved for every l
(Remark `rem:ucaragree`) and checked exactly for l ≤ 40. That covers the l ≤ 8 asked for, and the
factorised l ≤ 4 forms.

**Wording for the paper.** Proposition 2.4, new Lemmas `lem:ellmoments`, `lem:Phi` and
`lem:hypbound`, Lemma 2.5 and Remark `rem:ucaragree`, exactly as in `lemma25.tex`.

**Placement.** Move Thm 4.6 and Lemmas 4.7, 4.8 and `lem:hypbound`, with the definitions of h_t,
g_t, γ₀ and systole, to §2.2. They use nothing from §§2–3.

**External input of the new proof.** Every item below is a citation or classical analysis.

1. The Selberg trace formula for cocompact Fuchsian groups with elliptic elements, in Dryden–Strohmaier's
   eq. (1). It is fetched and quoted, and DS take it from Hejhal LNM 548 and Iwaniec. It holds for even
   entire h of uniform exponential type.
2. Its extension to h_t, by Lemma 4.7. This uses only Z(s) = O(1/s), a consequence of DGGW Thm 4.8
   (or of Weyl's law).
3. Lemma 4.8, geodesic counting. It is elementary and in the paper.
4. Classical analysis:
   - Euler's beta integral ∫ e^{cx}/(1+e^x) dx = π/sin πc;
   - (x/2)coth(x/2) = Σ B_{2n}x^{2n}/(2n)!;
   - Euler's formula for ζ(2n), for the sign and non-vanishing of B_{2n};
   - Liouville's theorem;
   - the product formula for sin.

No coefficient computation of DGGW or Uçar is used.

## 2. Remark 4.12: DONE

**What changed.** The remark wrongly said the trace-formula route is "a consistency check, not an
independent proof". In fact the route uses only Z(s) = O(1/s), which fixes no c_j with j ≥ 2.

**Wording.** `remark412.tex` gives two versions:

- (2A) if `lemma25.tex` is adopted. This is recommended; there the trace formula is the primary proof.
- (2B) otherwise.

It also gives matching replacements (1A) and (1B) for the sentence after Thm 4.1 (manuscript l. 627).

## 3. Locality, classical part: PARTIAL

**Reached.**

| Source | Coverage |
|---|---|
| Dryden–Strohmaier | full |
| Huber 1959, Huber II 1961 and its Nachtrag | full GDZ scans, quotations checked against the page images |
| Wolpert, Bull. AMS 1977 | full |
| Hejhal LNM 548 | 2-page chapter previews, plus the zbMATH review |
| Buser 1992 | Internet Archive full-text snippets only, no page numbers |

**Instrument gaps (not seen):**

- Hejhal Ch. 3 interior, including the elliptic trace formula and its hypotheses on h;
- Iwaniec, Spectral Methods (Thm 10.2): AMS returned 429;
- McKean, CPAM 1972: Wiley returned 403;
- Wolpert, Annals 1979.

Details and HTTP codes are in `locality-sources.md`.

**Decisions** (`locality.tex`):

- **(a) Classical, to be cited.**
  - Signature locality, Thm 4.1, becomes a Proposition. The surface case is McKean (Buser's text says
    "Following McKean [1], we plug the heat kernel … into the trace formula"); the orbifold case is
    immediate from DGGW/Donnelly.
  - The trace formula with elliptic terms, Thm 4.6, is classical. DS cite Hejhal and Iwaniec, and
    zbMATH says Hejhal's Ch. III first admits groups with elliptic elements.
  - The mechanism by which the difference of heat traces is a difference of hyperbolic terms is
    Selberg/Huber/McKean. Huber II p. 388 fn. 4 points to Selberg's trace formula.
  - For surfaces, geodesic counting with an explicit genus-only constant is Buser's (g−1)e^{L+6}.
- **(b) Lemma 4.7 stays,** shortened and introduced as standard. Hejhal's admissible class could not
  be read, so replacing the lemma by a citation "in the form needed" is unconfirmed. The bracketed
  replacement sentence in `locality.tex` is ready if a reader with library access confirms it.
- **(c) New, to be claimed only as an explicit packaging of the classical mechanism:**
  - the orbifold counting bound with explicit constant (Lemma 4.8);
  - the explicit bound C(A, ℓ, D) t^{−1/2} e^{−ℓ²/4t} with its range, and the a-posteriori form (Thm 4.9);
  - sharpness: the leading term at the first differing length, and that the factor t^{−1/2} cannot be
    dropped (Thm 4.10, Cor 4.11).

**Wording for the paper.**

- The section opening (S1), the new/classical sentences in (S3), and the added "Prior work" sentence (S4).
- The shortened section plan: about 4 pp.
- Prop 4.4 gets the one-line proof via mapping-class orbits (G7-20).

**Open (needs library access).**

- Hejhal LNM 548 Ch. 3, the trace-formula theorem near p. 351, and its hypotheses on h.
- Iwaniec Thm 10.2.
- McKean 1972, for the pinpoint.
- Buser, the page and statement of Lemma 6.6.4.

## 4. Theorem 1.2(iii): DONE

The constant is C(A, ℓ, D) = √π e^{3D} ℓ e^{ℓ/2}(2+3ℓ)/(2A(1−e^{−ℓ})(2+ℓ)) for 0 < t ≤ ℓ²/(2(1+ℓ)).
This is Thm 4.9(b), with the factor 1 + 2t/(ℓ−t) replaced by its maximum on that range.

"Attained" is restated precisely:

- If the weighted length spectra first differ at ℓ (for instance, if the systoles differ), then
  √t e^{ℓ²/4t}|ΔZ| has a nonzero limit. The exponent and t^{−1/2} are attained; the constant is not
  claimed to be.
- If they first differ at L* > ℓ, the order is t^{−1/2}e^{−L*²/4t}.
- If they never differ, the orbifolds are isospectral.

Wording: `thm12iii.tex`, items (1) to (4), including the abstract clause.

## 5. Proofs that lived only in the repository

### 5a. Descent: DONE (no PARI dependence)

**Model.** An explicit birational map C_{27/2} ↔ E: y² = x(x+9)(x+384) is given:

- ψ(x, y) = (25x+y : 25x−y : 4(x−216));
- smoothness of C follows from the genus argument;
- ψ sends the origin of E to O.

**Rank.** Cremona §3.6 (3.6.2) gives rank = e₁ + e₁′ − 2. In the paper's notation the two Selmer
groups are {±1, ±6} and {1}.

- The classes ±2 and ±3 on E fail mod 5.
- The negative classes on E′ fail over R.
- The classes 3, 5, 15 on E′ fail 3-adically.
- The classes ±1, ±6 are images of torsion points.

So the rank is 0.

**Torsion.** Reduction mod 7 and mod 11 gives #E(F₇) = #E(F₁₁) = 12, and Cremona §3.3 p. 70 gives
injectivity of torsion. With the twelve explicit points this gives Z/2 × Z/6:

- order 2: (0,0), (−9,0), (−384,0);
- order 3: (16, ±400);
- order 6: (−24, ±360), (−144, ±2160), (216, ±5400).

**New bibliography entry:** cremona1997, fetched from the author's page.

### 5b. Theorem 5.13: DONE

Theorem 5.13 keeps only the proved threshold. The new Proposition `prop:collisionfree`
(computational) prints all 38 sums, with its method:

- an exhaustive check at the 38 sums;
- an exactly re-verified collision at each of the other 4745 sums;
- 3962 of those come by scaling, and 783 have primitive witnesses, listed in `collision_witnesses.csv`.

The reviewer independently re-derived the 38 sums by exhaustive search over S ≤ 4800.

### 5c. Remark 2.12: DONE

The recommendation is to cut it to the short remark in `remark212.tex`, which is proved in full: the
poles of Φ_m at ±π/m give p_l(m)/m ~ A_l(m)(1 + π²/(2m²(2l−1))), and the smooth part is negligible,
so |c_{l+2}|/(l|c_{l+1}|) → M²/π². Drop the peeling, Borel-radius and "strengthening of Uçar" claims.

**Repository inconsistency found.** The manuscript's "smooth part dominates for l ≤ 8" (genus 10⁴,
one cone of order 2) is **correct**. `theory/divergence/proof.md` and `STATUS.md` say "ℓ ≤ 5", which
is wrong. They are not this session's files, so they are reported, not edited.

### 5d. Prop 6.10: DONE

Explicit formulas are given for Δ = |F⁻¹|δ, τ^lin, τ^rem, ρ, ρ^rem, Δ_M and J.

An independent implementation of exactly these formulas reproduces threshold.py's r_rem, A and E
exactly in all 11 cases of Table 4. It also certifies every printed δ_cert and δ_thm.

## 6. The point 3P: DONE

3P = (162833463 : 723926268 : 287876366). The printed (162833463 : 287876366 : 723926268) is
(1:0:−1) − 3P, the Y↔Z transposition. It is the same triad, so no orbifold statement changes.

`review/audit/diophantine/check_groups.py` now compares the ordered, normalised point and asserts
that the printed permutation is not 3P. Its regenerated output `check_groups.txt` changes in exactly
those two lines. Running the script rewrites its own `.txt`, so that file is part of the fix.

## 7. Sharpness wording: DONE

The exponent 1/k is sharp for arbitrary data. For the heat invariants of real orders it is 1/2, and
sharp, in two cases:

- at a double order;
- when all orders are equal (any n = k ≥ 3, by Remark 6.8's argument, which applies verbatim).

Other configurations are not settled. Wording: `sharpness.tex`, items (1) to (6).

## 8. Self-attack: DONE

| Severity | Count |
|---|---|
| FATAL | 0 |
| SERIOUS | 2 |
| MINOR | 9 |
| NOTE | 2 |

The two SERIOUS findings, both fixed:

- F1: descent.tex gave the wrong points of order 3. The conclusion was unaffected, and the check is now per point.
- F2: an overclaim in the sharpness wording.

See `attack-log.md`.

## Results that changed

| Result | Change |
|---|---|
| Lemma 2.5 | Now proved for every l from the trace formula, independent of Uçar's thesis |
| Remark 4.12 | Reversed: the trace-formula route is an independent proof |
| Theorem 1.2(iii) | The constant now depends explicitly on the diameter; "attained" is qualified |
| Theorem 5.13 | Split: threshold theorem plus a computational proposition listing all 38 sums |
| Remark 2.12 | Reduced; the unproved peeling and Borel claims are dropped |
| 3P | Coordinate order corrected |
| Sharpness | "1/2 at a triple order" is replaced by "1/2 when all orders are equal" (broader and correct) |
| Section 4 | Signature locality and the trace formula are recast as classical |

No theorem of the paper was found false.

## Files

| Kind | Files |
|---|---|
| Fragments | `lemma25.tex`, `remark412.tex`, `locality.tex`, `thm12iii.tex`, `descent.tex`, `thm513.tex`, `remark212.tex`, `prop610.tex`, `point3P.tex`, `sharpness.tex` |
| Checks | `check_*.py`, with outputs in `check_*.txt` |
| Scripts | `run_checks.sh`, `fetch_sources.sh` |
| Data | `collision_witnesses.csv` |
| Notes | `locality-sources.md`, `attack-log.md` |

The source cache `sources_cache/` is git-ignored. It is recreated by `fetch_sources.sh` for DS and
Cremona; the Huber, Hejhal-preview, zbMATH and Buser retrieval is logged in `locality-sources.md`.
