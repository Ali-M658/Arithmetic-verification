# G5-bis comparison: group `trace-formula`

Written after the blind REVIEW.md was frozen. Files read in this phase:

- `theory/revision/lemma25.tex` (full, with proofs);
- `theory/revision/remark412.tex` and `theory/revision/thm12iii.tex`;
- `theory/revision/check_lemma25.py` and its `.txt` (623 checks, 0 failures);
- `theory/revision/check_remark412.py` and its `.txt` (32/0);
- `theory/revision/check_thm12iii.py` and its `.txt` (48/0);
- `theory/revision/attack-log.md`, `theory/revision/locality.tex` and `theory/revision/locality-sources.md`.

Nothing else was opened. In particular I did not read `paper/` (the manuscript), although several
fragments point to it (the proof of Thm 4.9(b), the definitions at "manuscript ll. 679-680").

**No blind grade changes.** The table at the end gives the status of each finding.

## Per result

### TF.1 Elliptic moments: agrees

- **(i).** The existing proof substitutes x = -2 pi r with c = (a-s)/2pi, uses Euler's beta integral, and
  dominates by |r|^n e^{s_0|r|} F_a. This is the same as my derivation.
- **(ii).** Same Taylor remainder argument.
- **Check script.** `check_lemma25.py` (a) checks (i) by 30-digit quadrature only, at 18 points. That is
  appropriate for a classical integral and is not an exact certificate.
- **Discrepancies.** None.

### TF.2 Closed form: agrees, by a slightly different route

- **cot-sum identity.** The existing proof uses Liouville: the difference
  sum_j cot(x + pi j/m) - m cot(mx) is pi/m-periodic, entire, and tends to 0 as Im x -> +-oo. I quoted
  the identity as classical. Both are fine.
- **sigma_i > 0.** The existing proof uses the product u/sin u = prod (1 - u^2/n^2 pi^2)^{-1}, a product
  of series with positive coefficients. I used partial fractions, sigma_i = 2 eta(2i)/pi^{2i}.
  Equivalent.
- **(phik).** Same Bernoulli expansion. The sign step goes through Euler's formula, as in my derivation.
- **Scripts do not certify the closed form exactly.**
  - (b) compares the defining sum with the closed form in 50-digit floating point at four points per m,
    m in {2,3,4,5,7,12,30}.
  - (c) compares Taylor coefficients by a numerical Cauchy integral, k <= 6 and m in
    {2,3,5,8,12}. Of the coefficient checks, only (c) compares the Bernoulli formula with the function
    itself.
  - No exact comparison of the defining sum with (phik) exists in the existing scripts.
  - My `check_closedform.py` supplies one: an exact defining-sum route via Newton power sums of
    cot(pi j/m), with the closed form by exact series, for k <= 40 and m <= 12 / 30.
  - Not a defect of the mathematics, which is proved analytically.

### TF.3 Hyperbolic-term bound: agrees, but the fragment has no proof

The existing "proof" of `lem:hypbound` (lemma25.tex ll. 95-99) is a pointer: "This is the bound for
one Hyp_i established in the proof of Theorem 4.9(b) ... in the reorganised text that argument is given
here." So the argument is **not yet written in the fragment**. I could not compare it line by line
without the manuscript, which I did not open.

`check_thm12iii.py` checks the ingredients:

- (c): phi_t decreasing for x >= l when t <= l^2/2.
- (d): the "erfc step" int_l^oo e^x phi_t <= 2tl/(l-t) e^{l/2 - l^2/4t}/sqrt(4 pi t).
- (e): the Stieltjes majorant with n(x) = (pi/A)e^{x+3D}.

These match my derivation step for step: the same f, the same integration by parts, the same
x/(x-t) <= l/(l-t) bound. Checks (d) and (e) are quadrature (30 digits). My blind proof (REVIEW.md TF.3)
can serve as the text to be inserted.

Minor observations on `check_thm12iii.py`:

- Its comment on (c) reads "1/x + 1/2 - x/(2t)"; the logarithmic derivative is 1/x - 1/2 - x/(2t).
  This is a typo in a comment only, and the conclusion (negative) is unaffected.
- Check (c)'s first conjunct, `simplify(tmax - l**2/2) != 0`, tests nothing useful. The second
  conjunct carries the content.

**Status of my MINOR (systole undefined in the lemma):**

- The PLACEMENT comment (lemma25.tex ll. 10-13) moves "the definitions of h_t, g_t, gamma_0, closed
  geodesic and systole (manuscript ll. 679-680)" ahead of the lemma.
- thm12iii.tex now defines the systole including geodesics through cone points (attack-log F10).
- So the finding is **covered if** the manuscript definition at ll. 679-680 is the "all hyperbolic
  classes" one, which I could not verify, and **if** placement option (a) is taken. Under option (b)
  the lemma still precedes the definition.
- Blind grade MINOR stands until the lead confirms ll. 679-680.
- The "Orb in Sig" notation query is also unresolved: lemma25.tex uses it in `lem:hypbound` and
  `prop:heatinput`.

### TF.4 Proposition: agrees

- **Elliptic part.** The existing proof is identical to mine:
  sum_j mu_{2k}(2 theta_j)/(2m sin theta_j) = Phi_m^{(2k)}(0)/4^k = (2k)! phi_k/4^k, convolved with
  e^{-t/4}.
- **Identity part.** r tanh(pi r) = |r| - 2|r|/(e^{2pi|r|}+1). The alpha_k formula in nu_j,
  "(-1/4)^k/k! - 4 sum_{i+j=k-1} (-1/4)^i/i! (-1)^j nu_j/j!", is exactly my S(t) e^{-t/4}. The final step
  uses B_{2l}(1/2) = (2^{1-2l}-1)B_{2l}, as in my derivation.
- **Scripts.** `check_remark412.py` (b) checks alpha_k exactly for k <= 14 (mine: k <= 40). Its moments
  (a) are checked by quadrature, k <= 8. I checked them exactly against sympy's zeta(2k+2), k <= 40.
- **Weak check.** `check_lemma25.py` (d), "[t^l] E_m = (-1)^l p_l/m (exact)", convolves m_phi and
  compares it with p_trace, which is built from the same m_phi. It tests only the bookkeeping of (bl).
  The real link to the integral is (d)'s quadrature of the moments (k <= 5) and (h) (the truncation
  ratio). This is adequate but is not an independent certificate of (bl).
- **Discrepancies.** None.

### TF.5 Lemma 2.5 and printed values: agrees

**Proof.** The existing proof is the same positive-combination argument with the same leading
coefficient computation. One sentence is terse: "All weights in (phik) and (bl) are positive". It is
correct, since sigma_i > 0, |B_{2n}| > 0 and (2k)!/(k!(l-k)!) > 0, and it is what my weight formula
w_{l,n} makes explicit.

**Positivity for real m > 1.**

- Check `check_lemma25.py` (e) tests p_l(m) > 0 **only at integers m = 2..40**. Its docstring says
  "p_l(m) > 0 for m >= 2". The statement claims every real m > 1, including (1, 2).
- The structural check (ll. 197-200: every term of m phi_k is a positive multiple of m^{2n}-1,
  k <= 40) does cover the real claim, combined with the positive weights of (bl). So the claim is
  tested, but not by the line that names it.
- My `check_conepoly.py` adds two direct certificates: positive weights w_{l,n}, and all coefficients
  of p_l(1+x) positive.

**Printed values.** alpha_0..alpha_4 and p_0, p_1, p_2 agree. The script also matches the factorised
p_3, p_4 of `theory/cone-coefficients/ucar-source.md`, which I did not see. My p_3 = (m^8/10080 + m^6/3780
+ m^4/2160 + m^2/945 - 19/10080) expands from their factorisation (m^2-1)(m^2+3)(3m^4+2m^2+19)/30240:
(m^2-1)(m^2+3) = m^4+2m^2-3, times 3m^4+2m^2+19 gives 3m^8+8m^6+14m^4+32m^2-57, over 30240, which is the
same. Consistent.

**Schueth sentence (my TF.5c MINOR).** lemma25.tex ll. 170-171 still reads "The polynomials p_1,p_2
agree with the cone coefficients of Schueth [Rem. 4.2, Thm 4.1], which she attributes to [§5.6] at order
t^1." The finding is **not covered**; attack-log F3 restored the sentence unchanged.

**What the scripts test against Schueth.** `check_lemma25.py` (f) tests only Schueth's a_0, a_1 (ll.
215-219). The claimed agreement of **p_2 with Schueth Thm 4.1 is not tested by any existing script**;
p_2 is only compared with the paper's own (plexplicit). My `check_conepoly.py` tests it exactly at K=-1,
m = 2..30. The claim is true.

### TF.6 rem:ucaragree: agrees

- **The omitted identity.** It is m t^2 Phi_m(it/2) = (t/2)/sinh(t/2) [(mt/2)coth(mt/2) - (t/2)coth(t/2)].
  This is algebraically identical to my F(t) = t^2/(4 sinh(t/2))(m coth(mt/2) - coth(t/2)).
- **Coefficient relation.** Their m Phi_m^{(2k)}(0) = 2 * 4^k k! m c^S_k(pi/m) is my
  2c^S_k = (2k)! phi_k/(k!4^k). Same proof: the coth and sinh Bernoulli generating functions.

**Is the script comparison independent?** `check_lemma25.py` (f) compares p_trace (built from (phik),
the trace-formula route) with p_ucar (built from (4.25)+(4.33)) exactly, as polynomials, for l <= 40.

- It is a genuine comparison of two **different** closed forms, not a restatement: the formula for
  c^S is Ucar's and is never derived from (phik).
- Common-mode caveats:
  - both use the same Bernoulli routine (B_1 = -1/2 convention, only even indices used, so harmless);
  - p_ucar is "as transcribed in the manuscript (eq:ucarlune, eq:pl)", and the script does not check
    that transcription against the fetched thesis. I did check it by eye against Ucar (4.25),
    printed p. 134, and it matches exactly. So this gap is closed by REVIEW.md, not by the script.
- My `check_ucar.py` additionally:
  - checks the coefficient identity (a) and the generating-function identity (e) through t^82 by
    exact series without Bernoulli numbers;
  - checks (4.35) at kappa = -1 against alpha_k.
  No existing script tests the (4.35) claim directly. `check_remark412.py` tests alpha_k against
  (alphak), which is the same formula.
- The attack-log reviewer compared exactly for l <= 7 only.

**Status of my MINOR.** The text still cites "(4.33)--(4.34) at $K=-1$", with no Thm 4.20(ii) and K
instead of kappa. **Not covered.** This is also G5 item 10, still open in this fragment. Attack-log F6
changed the wording to "(-1)^l times Ucar's cone contribution" but did not add Thm 4.20(ii).

### TF.7 Remark 4.12: agrees in substance; the old wording is still present

The fragment's own header (remark412.tex ll. 4-9) states the reasoning I reproduced: O(x) counting
only, which "fixes no c_j with j >= 2". The attack log ("Circularity: ... nothing beyond Z(s) = O(1/s)")
agrees.

**Still saying the old thing:**

1. **"(or of Weyl's law)"** remains in both versions (2A l. 41, 2B l. 60) and in the lemma25.tex
   EXTERNAL INPUT comment (l. 200).
   - My point: an orbifold Weyl law is normally proved from the same leading heat term, so it is not an
     independent source.
   - The fragment's NOTE (ll. 63-66) recognises a related issue. The DGGW dependence would disappear if
     Lemma 4.7 were replaced by Hejhal/Iwaniec's admissible class, but locality.tex (b) keeps Lemma 4.7
     because Hejhal Ch. 3 could not be read.
   - So the dependence on DGGW Thm 4.8 for O(1/s) **remains**. My self-contained replacement (the
     trace formula with a compactly supported test function) removes it without any library access.
   - **Not covered.**
2. **"a second, independent proof"** remains in sentence (1B) (l. 19). Version 2A's sentence (1A)
   changes the framing: the structural DGGW route becomes "a second proof".
   - locality.tex now goes further. It demotes Theorem 4.1 to a classical Proposition whose proof is
     "This is Proposition prop:heatinput. Structurally: ... [DGGW Def. 4.7, §4.1], [Donnelly]".
   - That makes my point (a) sharper. With locality.tex adopted, the paper cites DGGW Thm 4.8 both as
     the structural proof of locality and as the source of the O(1/s) bound in the trace-formula
     proof. "Independent" is then true only of the coefficient computations, which is what 2A/2B say
     in the body. The first-paragraph wording (1B) must not be used with locality.tex.
   - **Partly covered** by (1A).
3. **Hypothesis class of DS (1).** lemma25.tex l. 198 says "for even entire h of uniform exponential
   type", which is DS's literal wording. It admits h = 1 and is too weak.
   - locality.tex (S3) cites DS eq. (1) via Hejhal/Iwaniec "applied to h_t (Lemma admissible)", and
     Lemma 4.7 (LO.7) itself uses g_R in C_c^oo. So the proof uses the right class and only the
     stated hypothesis is loose.
   - **Not covered.**

**Scripts.** `check_remark412.py` (d) "verifies" #{lambda_j <= x} <= e Z(1/x) on the round-sphere
spectrum. That inequality is the one-line Chebyshev bound, true for any nonnegative spectrum. The check
is an illustration, not evidence about orbifolds. Harmless, but the docstring calls it "the a-priori Weyl
bound used by Lemma 4.7"; it does not test the O(1/s) input.

Blind grade MINOR stands.

### TF.8 Theorem 1.2(iii): agrees

**(a) Constant.** thm12iii.tex derives C from Theorem 4.9(b) exactly as I did: the factor is increasing
in t with value (2+3l)/(2+l) at the endpoint, and pi/sqrt(4pi) = sqrt(pi)/2. `check_thm12iii.py` (a),
(b) is the same symbolic check as mine.

**Different systoles.** thm12iii.tex and check_thm12iii.py take the pair bound of Theorem 4.9(b)
(LO.9(b), stated directly with l = min and the common D) as given. Neither contains the monotonicity in l
that is needed if the pair bound is to be **derived from** the one-orbifold `lem:hypbound`. Under the
reorganisation, Theorem 4.9(b) quotes `lem:hypbound`.

Since `lem:hypbound`'s own proof is only a pointer back to Thm 4.9(b)'s proof, the logical order is
currently circular in the text: lemma -> proof of Thm 4.9(b) -> lemma. The mathematics is not circular.
When the argument is written into the lemma, one of the following must be stated:

- "the proof gives the bound with $\ell$ replaced by any $\ell'\le$ systole and $D$ by any
  $D'\ge$ diameter, as long as $t\le\ell'^2/(2(1+\ell'))$"; or
- the monotonicity line of REVIEW.md TF.8a.

My blind note ("one proof line to add") is confirmed as necessary. The grade stays NONE, since the
statement is true.

**(b) Attained.** This is Thm 4.10 / Cor 4.11 (LO.11), as thm12iii.tex says (item 5). It agrees with my
derivation. The "never differ (equivalently isospectral)" phrasing is attack-log F10, the same as I
re-derived. The equivalence of first-difference positions for the weighted, all-class and primitive
spectra is not discussed in the existing material. It is a harmless strengthening and needs no change.

## Other discrepancies and cross-file notes

- **alpha indexing clash.** lemma25.tex and locality.tex (Proposition `thm:locality`:
  Phi_j = alpha_{j-1} Phi_1 + sum b_{j-2}) use alpha_k with c_j = alpha_{j-1} A/4pi. The signatures
  statements (H3) write c_{l+2} = alpha_l Area + C_l. I could not open `theory/signatures/proof.md`, which
  remains forbidden, to see whether the paper uses both, so this is **not resolved**. Note that
  locality.tex's Phi_j = alpha_{j-1}Phi_1 + ... uses Phi_1 = A/4pi, consistent with TF.4.
- **lemma25.tex header.** It claims "independent of Ucar's thesis". That is correct for the derivation;
  Ucar enters only in the agreement remark.
- **Stronger claims than the statements.** I found none in lemma25.tex, remark412.tex or thm12iii.tex.

## Scripts: do they test what they claim?

| script / item | claim | verdict |
|---|---|---|
| check_lemma25 (a), (b), (c) | moment formula, closed form, Taylor coefficients | floating point (30-50 digits); correct, but not exact certificates. My exact routes cover them |
| check_lemma25 (d) "exact" | [t^l]E_m = (-1)^l p_l/m | bookkeeping only (both sides from m_phi); the link to the integral is the quadrature part |
| check_lemma25 (e) | Lemma 2.5 properties | exact; positivity printed only for integers 2..40, the real-m claim is covered by the structural check ll. 197-200 |
| check_lemma25 (f) | agreement with Ucar | genuine exact comparison of two different formulas, l <= 40; the transcription of (4.25) is not checked by the script (I checked it against the fetched text: correct). Schueth only a_0, a_1; **p_2 vs Schueth Thm 4.1 untested** (I tested it) |
| check_remark412 (b) | alpha_k from the identity term | exact, k <= 14 |
| check_remark412 (d) | "the a-priori Weyl bound" | illustration on the sphere; tests nothing about the orbifold input |
| check_thm12iii (a), (b) | the constant | exact symbolic; agrees with mine |
| check_thm12iii (c)-(e) | ingredients of the Hyp bound | symbolic plus quadrature; matches my proof; no monotonicity-in-l test (not claimed) |

## Status of my findings

| finding | blind grade | status in the existing fragments | grade now |
|---|---|---|---|
| TF.3 systole definition (and Orb in Sig) | MINOR | covered only if placement (a) is taken and manuscript ll. 679-680 define it over all hyperbolic classes (unverified) | MINOR (unchanged) |
| TF.3 proof missing from the fragment | (comparison finding) | `lem:hypbound` proof is a pointer to Thm 4.9(b), which will quote the lemma | new MINOR (write-up) |
| TF.5c Schueth/DGGW attribution | MINOR | not covered | MINOR (unchanged) |
| TF.6 cite Ucar Thm 4.20(ii); kappa | MINOR | not covered (G5 item 10 still open here) | MINOR (unchanged) |
| TF.7 "independent" / Weyl "or" / DS hypothesis class | MINOR | (1A) partly addresses "independent"; Weyl clause and hypothesis class not covered; locality.tex makes the DGGW dependence more visible | MINOR (unchanged) |
| TF.8a monotonicity line | NONE (note) | not present in thm12iii.tex | NONE (unchanged) |
| alpha indexing clash | note | unresolved (signatures proof not released) | note |

No grade changes.
