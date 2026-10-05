# Attack log: theory/revision fragments (task 8)

One adversarial review was run by a separate agent. It was given only the fragments
(`lemma25.tex`, `remark412.tex`, `thm12iii.tex`, `descent.tex`, `thm513.tex`, `remark212.tex`,
`prop610.tex`, `point3P.tex`, `sharpness.tex`), the manuscript (to look up referenced results) and the
cached texts of Dryden–Strohmaier and Cremona ch. 3.

- It was not allowed to read the check scripts or their outputs.
- It recomputed everything with its own code.
- It ran before `locality.tex` existed, so that fragment was not attacked. Its quotations are
  checked mechanically instead (`check_quotes.py`).

**Verdict before fixes:** FATAL 0, SERIOUS 2, MINOR 9, NOTE 2. No theorem statement was false. One
proof contained a false sentence (F1), and one wording overclaimed (F2). All findings are fixed below.
Every check script was then re-run (`run_checks.sh`: all PASS).

## Findings and dispositions

| # | severity | fragment | finding | disposition |
|---|---|---|---|---|
| F1 | SERIOUS | descent.tex | The torsion paragraph gave the orders of the points of E wrongly. It said (−144, ±2160) has order 3; in fact (16, ±400) have order 3 and (−144, ±2160) has order 6. The conclusion Z/2 × Z/6 was unaffected. My check (d) had compared only the order histogram, so it could not catch the swap. | **Fixed.** Every point's order is now stated, with the tangent at (16, 400) as a hand check. `check_descent.py` (d) asserts each point's order and that the printed list is all of E(Q). |
| F2 | SERIOUS | sharpness.tex | The abstract (item 1) and the sentence after Thm 6.6 (item 4) claimed exponent 1/2 "at a triple order" for real data. Remark 6.8 covers only (a,a,a), and a triple order inside a larger multiset is not settled. | **Fixed.** The wording is now "when all the orders are equal". The reviewer's F12 shows Remark 6.8's argument covers (a,…,a) for every n = k ≥ 3, so the corrected statement covers all-equal multisets of any size. `check_sharpness.py` (e) adds n = 4. |
| F3 | MINOR | lemma25.tex | The replacement dropped `\label{eq:cj}` and `\label{eq:plexplicit}` (both cited elsewhere), the α₀…α₄ values and the Schueth sentence. | **Fixed.** All restored. |
| F4 | MINOR | lemma25.tex, remark412.tex | Hyp = O(t^N) was cited to Thm 4.9(b), whose statement is about pairs (the one-orbifold bound is only in its proof). Placement option (a) also left definitions behind. | **Fixed.** New Lemma `lem:hypbound` (one-orbifold bound). Option (a) now moves h_t, g_t, γ₀, closed geodesic, systole, Lemmas 4.7 and 4.8 and the new lemma. Remark 4.12 (2A) cites the new lemma. |
| F5 | MINOR | lemma25.tex | The step from the moments ν_j to the Bernoulli-polynomial form of α_k was not stated. | **Fixed.** The α_k formula in ν_j is given, with the identity B_{2l}(½) = (2^{1−2l}−1)B_{2l}. Already verified for k ≤ 14 by `check_remark412.py` (b). |
| F6 | MINOR | lemma25.tex | (a) Uçar's (4.25) is no longer displayed. (b) (4.33)–(4.34) give the cone contribution (p_l/m up to sign), not p_l. (c) The paper text named a repository path. | **Fixed.** (4.25) is displayed in the remark, the wording is "(−1)^l times Uçar's cone contribution (4.33)–(4.34)", and the reference is now to the archived repository / Appendix. |
| F7 | MINOR | remark412.tex | (a) Only Z(s) = O(1/s) is used, not "the leading term". (b) Replacement (1) fits only version 2B. (c) The agreement with (4.35) is not covered by Remark ucaragree. | **Fixed.** The wording is now "only the a-priori bound Z(s) = O(1/s)". Sentence (1A) is added for version 2A. (4.35) is stated to be the same formula as (eq:alphak). |
| F8 | MINOR | remark212.tex | The α bound, the ε_k Cauchy estimate and the O(l⁻²) tail were asserted, not shown. Also, "nothing below uses" is inaccurate because §7 cites the growth. | **Fixed.** The three short justifications are now in the remark, and the wording is "No proof below uses this remark". |
| F9 | MINOR | descent.tex | A curve isomorphism is a group isomorphism only if it sends origin to origin. Also, the label "In the notation of G7" leaked into paper text. | **Fixed.** ψ(O_E) = (1:−1:0) is stated, with the limit argument; `check_descent.py` (b) checks it. The G7 label is removed. |
| F10 | MINOR | thm12iii.tex | The isospectral case was phrased as a subcase of "first differ at L* > ℓ". "Systole" was undefined in the introduction. | **Fixed.** The case is restated as "never differ (equivalently, isospectral)", and the systole is defined to include geodesics through cone points. |
| F11 | MINOR | sharpness.tex | "Roots not real ⇒ data not realisable" needs uniqueness of the preimage. | **Fixed.** One line added: the Theorem B system is invertible at those data, so a real preimage would have e(m′) = e(q_s). |
| F12 | NOTE | sharpness.tex | "k ≥ 4 not settled" was too pessimistic, because Remark 6.8 works for any all-equal multiset. | **Adopted** (see F2). |
| F13 | NOTE | prop610.tex | "At most 7 terms" was unclear. | **Fixed.** It now reads "truncated after z⁷, at most four nonzero (odd) coefficients". |

## What the reviewer tried to break and could not

- **lemma25.tex:**
  - the beta integral and its domain;
  - differentiation under the integral;
  - the Taylor remainder;
  - the cot identity (Liouville);
  - the Bernoulli expansion and sign;
  - m·φ_k;
  - σ_i > 0;
  - the 4^{−k} factor and the e^{−t/4} convolution;
  - the degree, leading coefficient, p_l(1) = 0 and positivity;
  - agreement with Uçar (by hand for the identity, exactly for l ≤ 7);
  - the DS normalisation (E_m(0) = (m²−1)/(12m)).
- **Circularity:** Thm 4.6, Lemmas 4.7 and 4.8 and the Hyp bound use nothing from §§2–3 and nothing beyond Z(s) = O(1/s).
- **thm12iii.tex:** the constant, the monotonicity in t, the erfc step and the attainment claims, against Thm 4.10 and Cor 4.11.
- **descent.tex:**
  - φ(C) ⊂ E, ψ(E) ⊂ C and φ∘ψ = id (Gröbner);
  - Disc = 2¹⁸3⁸5⁶;
  - C_{27/2} nonsingular;
  - every congruence (mod 5; real; 3-adic, including the mod-9 values 6, 6, 6);
  - c′ = −786 and d′ = 140625;
  - n₁ = 4 and n₁′ = 1;
  - the match with Cremona's H(d₁, c, d₂) and (3.6.2);
  - #E(F₇) = #E(F₁₁) = 12;
  - the 12 points of C_{27/2} and the final step.
- **thm513.tex:** an independent exhaustive search over all S in [18, 4800] gives exactly the 38 listed sums. S = 557 has 25 575 triads. The counts 4745 = 3962 + 783 hold.
- **prop610.tex:** r, r_rem, Δ_M and J agree with the symbolic Jacobian for (2,8,8), (3,10,15,30) and (2,2,2,2,3), and e_k > 0 is used correctly.
- **point3P.tex:** 2P and 3P were recomputed, and the printed point is (1:0:−1) − 3P.
- **sharpness.tex:** the (a+s, a−s, a) family and Remark 6.8's inequality hold.

## Residual open points (not defects in what is claimed)

- **locality.tex:** not adversarially reviewed. Its claims are restricted to what the fetched texts
  show, and the unreachable sources are marked as instrument gaps.
- **Lemma 4.7:** kept rather than replaced by a citation, because Hejhal's class of test functions
  could not be read.
- **Real data at a k-fold order inside a larger multiset (k ≥ 3), and mixed clusters:** the exponent
  is not settled. The reviewer suggests a second-order argument might work; it is not attempted here.
