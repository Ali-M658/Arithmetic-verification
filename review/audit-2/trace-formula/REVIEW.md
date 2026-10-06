# G5-bis blind review: group `trace-formula`

Reviewer input: `review/audit-2/REVIEWER-BRIEF.md`, `review/audit/G5-VERDICT.md`,
`review/audit-2/statements/trace-formula.md`, the context file `review/audit/statements/locality.md`,
lines 36-62 and DF.1 of `review/audit/statements/signatures.md` (named in the task), and the fetched
sources `review/audit-2/sources/{ds_math0504571,ucar_1711.03405,dggw_0805.3148,schueth_1812.06119}.txt`.
Scripts: `check_closedform.py`, `check_conepoly.py`, `check_ucar.py`, `check_hypbound.py`, with the
shared exact helper `tf_lib.py`. Every `.txt` was produced by `python3 check_x.py > check_x.txt`, and
every script exits 0 ("ALL CHECKS PASSED").

## Summary table

| id | result | grade |
|---|---|---|
| TF.1(i) | Elliptic moments: the two-sided Laplace transform of F_a, and mu_n as derivatives | NONE |
| TF.1(ii) | Elliptic moments: alternating remainder bound | NONE |
| TF.1-DS | F_a, the range 0<a<2pi and the weights 1/(2m sin theta_j) match DS eq. (1) | NONE |
| TF.2 | Closed form of Phi_m for every m >= 1, sigma_i > 0, Bernoulli formula (phik) | NONE |
| TF.3 | Lemma: the hyperbolic term is small (the bound and O(t^N)) | MINOR (define the systole) |
| TF.4 | Proposition: heat expansion at curvature -1, alpha_k, b_l(m), c_j | NONE |
| TF.5a | Lemma 2.5 for every l (even, rational, degree 2l+2, p_l(1)=0, leading coefficient, p_l>0 on (1,oo)) | NONE |
| TF.5b | Printed values alpha_0..alpha_4, p_0, p_1, p_2 | NONE |
| TF.5c | Sentence on agreement with Schueth / DGGW §5.6 | MINOR (attribution wording) |
| TF.6 | Remark rem:ucaragree (agreement with Ucar for every l) | MINOR (citation: add Thm 4.20(ii)) |
| TF.7 | Remark 4.12 (rem:proofC), independence claim, versions 2A/2B | MINOR (independence wording; hypothesis class of DS (1)) |
| TF.8a | Theorem 1.2(iii): the constant C(A,l,D), including two different systoles | NONE (one proof line to add) |
| TF.8b | Theorem 1.2(iii): the "attained" statement in its three cases | NONE |

No FATAL and no SERIOUS finding. No printed constant or value changes.

## Contamination

None. I opened no file under `theory/`, `paper/`, `review/referee-sim/`, no `REVIEW.md`/`COMPARISON.md`
of another group and no other session's `check_*` script or output. Besides my bundle and its context
file I read `review/audit/statements/signatures.md` lines 36-62 and DF.1 (statement file, named in my
task). I also listed the `review/audit-2/` folder and grepped `fetch_sources.sh` for the four source URLs.

## Instrument gaps

- Weyl's law for compact orbifolds (cited in Remark 4.12 as an alternative): no primary source fetched.
  My verdict does not depend on it (TF.7 gives a self-contained route).
- Hejhal / Iwaniec (DS's sources for eq. (1)): not fetched. The trace formula is taken as printed in DS
  eq. (1), p. 3, plus the previously audited admissibility lemma LO.7.
- Donnelly 1976: standing gap, not needed.

---

## TF.1 Elliptic moments (`lem:ellmoments`)

### The elliptic term, re-derived from DS eq. (1) (DS p. 3, fetched)

DS write the eigenvalues as lambda_n^2 and put r_n^2 = lambda_n^2 - 1/4 ("Let {lambda^2_n} be the
sequence of eigenvalues of Delta and denote as usual r^2_n := lambda^2_n - 1/4", p. 2-3). So an eigenvalue
is 1/4 + r^2, and the heat function is h_t(r) = e^{-t(1/4+r^2)}, even and entire. The elliptic part of
(1) is

  sum over elliptic conjugacy classes {R} of  1/(2 m(R) sin theta(R)) * int_R e^{-2 theta(R) r}/(1+e^{-2 pi r}) h(r) dr,

with theta(R) = pi l/m(R), 1 <= l <= m(R)-1, and the primitive elliptic classes identified with the cone
points (DS p. 3). For a cone point of order m, the classes R_c^l, l = 1..m-1, are pairwise non-conjugate
(an orientation-preserving conjugation preserves the rotation angle), and the elliptic classes of Gamma
are exactly these, over all cone points. With a = 2 theta = 2 pi l/m:

- the integrand is F_a(r) h(r) with F_a(r) = e^{-ar}/(1+e^{-2 pi r}), as in TF.1;
- a ranges over 2 pi l/m, l = 1..m-1, so 0 < a < 2 pi, as in TF.1;
- the weight is 1/(2 m sin(pi l/m)), as in LO.6 (E_m), and 1/(2m sin theta_j) * 1/(2 sin(theta_j - u)) =
  1/(4 m sin theta_j sin(theta_j - u)) is the j-th term of Phi_m (TF.2). The weights match.

The choice of R_c (rotation by +2pi/m or -2pi/m) does not matter: since h is even,
int F_a(r) h(r) dr = int F_{2pi-a}(r) h(r) dr because F_a(-r) = F_{2pi-a}(r), and sin(pi l/m) =
sin(pi(m-l)/m). The g-normalisation of DS (1) does not enter the elliptic term.

The bounds in the preamble hold: F_a(r) <= e^{-ar} for r >= 0, and F_a(r) = e^{(2pi-a)r}/(e^{2pi r}+1) <=
e^{(2pi-a)r} for r <= 0. So every mu_n(a) is finite.

### (i)

Put b = a - s, so 0 < b < 2pi exactly when a - 2pi < s < a. Substitute y = -2 pi r:

  int_R e^{-br}/(1+e^{-2pi r}) dr = (1/2pi) int_R e^{(b/2pi) y}/(1+e^y) dy = (1/2pi) * pi/sin(b/2) = 1/(2 sin(b/2)).

This uses Euler's beta integral int_R e^{cy}/(1+e^y) dy = pi/sin(pi c), 0 < c < 1, with c = b/2pi.
The interval a-2pi < s < a is exactly the interval of absolute convergence, so the domain of s is right.

On |s| <= s_0 < min(a, 2pi - a), we have |r^n F_a(r) e^{sr}| <= |r|^n e^{-(a-s_0)|r|} for r >= 0 and
<= |r|^n e^{-(2pi-a-s_0)|r|} for r <= 0. This bound is integrable and independent of s, so
differentiation under the integral is legitimate at s = 0 (0 is inside the interval because
0 < a < 2pi). Hence mu_n(a) = d^n/ds^n [2 sin((a-s)/2)]^{-1} at s = 0.

### (ii)

For x >= 0 the Taylor remainder of e^{-x} after K terms is (-1)^K e^{-xi} x^K/K!, with 0 <= xi <= x.
So |e^{-x} - sum_{k<K} (-x)^k/k!| <= x^K/K!. Put x = t r^2, multiply by F_a > 0 and integrate. This
gives the stated bound with t^K mu_{2K}(a)/K!.

Checks: `check_conepoly.py` (sanity only, 40-digit quadrature) confirms the integral in (i) for
a in {0.7, 2, 5} at s = 0, 0.3 and a - 0.1. Grade **NONE**.

## TF.2 Closed form (`lem:Phi`)

**Analyticity.** theta_j lies in [pi/m, pi - pi/m]. So for |u| < pi/m, theta_j - u lies in (0, pi)
and no denominator vanishes. Phi_1 = 0 because the sum is empty. Phi_m(-u) = Phi_m(u): substitute
j -> m - j, then sin(theta_{m-j} + u) = sin(theta_j - u).

**Proof of (Phi).** We have 1/(sin theta sin(theta-u)) = (cot(theta-u) - cot theta)/sin u, because
cot(theta-u) - cot theta = sin u/(sin theta sin(theta-u)). Sum over j = 1..m-1:

- sum_j cot theta_j = 0 (pair j with m-j);
- the classical identity sum_{j=0}^{m-1} cot(x + pi j/m) = m cot(mx), at x = -u, minus its j = 0 term
  cot(-u), gives sum_{j=1}^{m-1} cot(theta_j - u) = cot u - m cot(mu).

Hence Phi_m(u) = (cot u - m cot mu)/(4 m sin u) for 0 < |u| < pi/m. This holds for every m >= 1, and for
m = 1 both sides are 0.

**sigma_i > 0.** Partial fractions give 1/sin u = sum_n (-1)^n/(u - n pi). So

  u/sin u = 1 + 2 sum_{n>=1} (-1)^{n+1} u^2/(n^2 pi^2 - u^2) = 1 + sum_{i>=1} 2 eta(2i) pi^{-2i} u^{2i},

where eta is the Dirichlet eta function, which is positive. So sigma_i = 2 eta(2i)/pi^{2i} > 0. In
closed form, sigma_i = (4^i - 2)|B_{2i}|/(2i)!, which is rational and positive for i >= 1, and sigma_0 = 1.

**Proof of (phik).** We have cot x = 1/x - sum_{n>=1} 4^n|B_{2n}| x^{2n-1}/(2n)!. Hence
cot u - m cot mu = sum_{n>=1} c_n (m^{2n}-1) u^{2n-1}, with c_n = 4^n|B_{2n}|/(2n)!. Multiply by
1/sin u = sum_i sigma_i u^{2i-1}. The coefficient of u^{2k} collects n + i = k + 1, so
4 m phi_k(m) = sum_{n=1}^{k+1} sigma_{k+1-n} c_n (m^{2n}-1). This is (phik).

**Exact hunt** (`check_closedform.py`). There are three independent computations of phi_k(m):

- (A) the defining sum, with no trigonometric closed form: 1/(sin th sin(th-u)) = (1+c^2)/(cos u - c sin u)
  with c = cot th. The coefficients are polynomials in c, summed with exact power sums of the roots
  cot(pi j/m) of ((X+i)^m-(X-i)^m)/(2i) (Newton's identities);
- (B) the closed form, by exact power-series division, with no Bernoulli numbers;
- (C) (phik), with sigma_i obtained by inverting the series of sin u/u.

Results:

- (A) = (B) for m = 1..12, k <= 40.
- (A) = (C) for m = 1..30, k <= 40.
- Odd coefficients vanish.
- sigma_i > 0 and sigma_i = (4^i-2)|B_2i|/(2i)! for i <= 42.

Grade **NONE**.

## TF.3 The hyperbolic term is small (`lem:hypbound`)

**Derivation.** Hyp(t) = sum_[gamma] l(gamma_0)/(2 sinh(l(gamma)/2)) * e^{-t/4} e^{-l(gamma)^2/4t}/sqrt(4 pi t)
(LO.6, from DS (1) with g_t(u) = e^{-t/4} e^{-u^2/4t}/sqrt(4 pi t)). Every term is positive, so Hyp >= 0.
Let l be the least length over **all** hyperbolic conjugacy classes. Use three bounds:

- l(gamma_0) <= l(gamma);
- 2 sinh(x/2) = e^{x/2}(1 - e^{-x}) >= e^{x/2}(1 - e^{-l}) for x >= l;
- e^{-t/4} <= 1.

Together they give Hyp(t) <= [(1-e^{-l}) sqrt(4 pi t)]^{-1} sum_gamma f(l(gamma)), with
f(x) = x e^{-x/2 - x^2/4t}.

Next, f'(x) = e^{-x/2-x^2/4t}(1 - x/2 - x^2/(2t)). For x >= l and t <= T := l^2/(2(1+l)) we have
x^2/(2t) >= 1 + l > 1, so f is decreasing on [l, oo). By Tonelli,
sum_gamma f(l_gamma) = int_l^oo (-f'(x)) N(x) dx. Apply LO.8, N(x) <= (pi/A) e^{x+3D}:

  sum <= (pi e^{3D}/A) int_l^oo (-f') e^x dx = (pi e^{3D}/A) [ f(l) e^l + int_l^oo x e^{x/2 - x^2/4t} dx ].

The boundary term vanishes at infinity. Put g(x) = x/2 - x^2/4t, so -g'(x) = (x-t)/(2t) > 0 for x > t,
and x e^g = (2tx/(x-t)) (-g' e^g). Since x/(x-t) is decreasing on x > t, it is at most l/(l-t) on
[l, oo). Here l > T >= t, because l - T = l(2+l)/(2(1+l)) > 0. So the integral is
<= (2tl/(l-t)) e^{l/2 - l^2/4t}. Altogether

  Hyp(t) <= pi e^{3D}/(A(1-e^{-l})) * l e^{l/2} (1 + 2t/(l-t)) * e^{-l^2/4t}/sqrt(4 pi t),

which is exactly the printed bound. Since 1 + 2t/(l-t) <= (2+3l)/(2+l) on the range,
Hyp = O(t^{-1/2} e^{-l^2/4t}) = O(t^N). The hypothesis t <= T is sufficient: monotonicity of f only needs
l^2/(2t) >= 1 - l/2.

**Hunt** (`check_hypbound.py`, sanity part). Synthetic length spectra that saturate the counting bound
N(L) = floor((pi/A)e^{L+3D}) satisfy the inequality, at t = T and t = 0.2T, for
(l, D, A) = (0.05, 0.5, 3), (0.5, 2, 1), (2, 1, 0.5), (6, 4, 10). This includes the smallest systole
tried. The proof above is the certificate.

**Finding (MINOR).** The statement uses "systole l" without defining it. The bound is **false** if
"systole" is read as the least length of a closed geodesic avoiding cone points: a hyperbolic class
through cone points could then be shorter than l, and its term e^{-L^2/4t} with L < l dominates the
bound. Theorem 1.2(iii) (TF.8) defines it correctly. The lemma must do the same: the counting and the
sinh bound both need l = min over all hyperbolic classes.

- Replacement for the first line of the lemma: "Let $\Orb$ be a closed orientable hyperbolic 2-orbifold
  of area $A$ and diameter $D$, and let $\ell$ be its systole, the least length of a closed geodesic,
  including those through cone points (equivalently, the least $\ell(\gamma)$ over hyperbolic
  $\gamma\in\Gamma$). For $0<t\le\ell^2/(2(1+\ell))$, ..."
- Notation query: in `review/audit/statements/signatures.md`, Sig is a set of *signatures*. If `\Sig`
  is that set, then "$\Orb\in\Sig$" (TF.3, TF.4) is a type error and should read "$\sigma(\Orb)\in\Sig$"
  or as above.

## TF.4 Proposition (`prop:heatinput`)

**Identity term.** Write tanh(pi r) = 1 - 2/(e^{2pi r}+1). Then

  int_R r tanh(pi r) e^{-tr^2} dr = 1/t - 4 int_0^oo r e^{-tr^2}/(e^{2pi r}+1) dr.

The Fermi moments are M_k = int_0^oo r^{2k+1}/(e^{2pi r}+1) dr = (1-2^{-2k-1})(2k+1)! zeta(2k+2)/(2pi)^{2k+2}
= (1-2^{-2k-1})(-1)^k B_{2k+2}/(4(k+1)), using the eta-integral and zeta(2n) = (-1)^{n+1}B_{2n}(2pi)^{2n}/(2(2n)!).
The integrand is positive, so the alternating remainder bound of TF.1(ii) applies, and
I(t) ~ (A/4pi t) e^{-t/4} S(t) with S(t) = 1 - 4t sum_k (-t)^k M_k/k!.

Using B_{2j}(1/2) = -(1-2^{1-2j})B_{2j}, the coefficient of t^j in S (j >= 1) is
4(-1)^j M_{j-1}/(j-1)! = B_{2j}(1/2)/j!, and B_0(1/2) = 1. So S(t) = sum_j B_{2j}(1/2) t^j/j!. Multiplying
by e^{-t/4} gives

  alpha_k = sum_{j} B_{2j}(1/2)/j! (-1/4)^{k-j}/(k-j)! = (-1)^k/(k! 4^k) sum_j C(k,j)(-4)^j B_{2j}(1/2),

which is (alphak).

**Elliptic term.** By TF.1, sum_j w_j mu_{2k}(a_j) = d^{2k}/ds^{2k} Phi_m(s/2)|_0 = (2k)! phi_k(m)/4^k,
with w_j = 1/(2m sin theta_j), because sum_j w_j/(2 sin(theta_j - s/2)) = Phi_m(s/2). By TF.1(ii), with
a finite sum over j,

  E_m(t) ~ e^{-t/4} sum_k (-t)^k (2k)! phi_k/(k! 4^k).

The coefficient of t^l is (-1)^l 4^{-l} sum_k (2k)!/(k!(l-k)!) phi_k = (-1)^l p_l(m)/m, which is (bl),
sign included.

**Hyperbolic term.** It is O(t^N) by TF.3. Z = I + E + Hyp is LO.6.

**Indexing.** Area/(4 pi t) alpha_k t^k is t^{k-1} = t^{j-2}, so j = k+1. b_l t^l has l = j-2. With
DF.1 (Z ~ sum_{j>=1} c_j t^{j-2}) this gives c_1 = A/4pi and c_j = alpha_{j-1}A/4pi + sum_i b_{j-2}(m_i),
which is (cj). This agrees with LO.1.

**Checks** (`check_conepoly.py`):

- (alphak) equals the identity-term coefficients for k <= 40. M_k was computed by sympy's exact zeta at
  even integers and checked against the printed moment formula.
- DGGW (5.7) is reproduced: c_2 = chi/6 + sum (m^2-1)/(12m).
- DGGW (5.10) is reproduced with R1212 = sectional curvature = -1 ("R_abab is the sectional curvature",
  DGGW p. 16): -(m^4+10m^2-11)/(360m) = b_1(m), m = 2..30. The trig sums DGGW quote are checked exactly.
- The smooth part a_2/4pi = (1/15)A/4pi = alpha_2 A/4pi follows from DGGW's
  a_2 = (1/360)int(2|R|^2-2|rho|^2+5tau^2).
- Sanity only (mpmath): I(t) and E_m(t) (m = 2..7) at t = 0.02 agree with the truncated series, to
  within the first omitted term.

**Consistency note (not a defect of TF.4).** `signatures.md` H3 writes c_{l+2} = alpha_l Area + C_l. Its
alpha_l is alpha^{TF.4}_{l+1}/(4pi). If both texts reach the paper, the symbol alpha_l must not denote
both. Grade **NONE**.

## TF.5 Lemma 2.5 (`lem:conepoly`) and the printed values

**Proof for every l.** Substitute (phik) into (bl):

  p_l(m) = sum_{n=1}^{l+1} w_{l,n} (m^{2n} - 1),
  w_{l,n} = 4^{-l} sum_{k=n-1}^{l} (2k)!/(k!(l-k)!) * (1/4) sigma_{k+1-n} * 4^n|B_{2n}|/(2n)!.

Every summand of w_{l,n} is a product of positive rationals (sigma_i > 0 by TF.2, |B_{2n}| > 0), so
w_{l,n} is a positive rational for every 1 <= n <= l+1. No negative weight can occur for any l. Hence:

- p_l is an even polynomial with rational coefficients. It is the unique polynomial agreeing with (bl)
  on the integers m >= 1.
- p_l(1) = 0.
- p_l(m) > 0 for every real m with |m| > 1, in particular on (1, 2): each m^{2n}-1 > 0 and each weight
  is > 0.
- Degree exactly 2l+2. Only n = l+1 reaches m^{2l+2}, and it requires k = l. Its coefficient is
  4^{-l}(2l)!/l! * (1/4) * 4^{l+1}|B_{2l+2}|/(2l+2)! = |B_{2l+2}|/(l!(2l+1)(2l+2)) = |B_{2l+2}|/(2(l+1)!(2l+1)),
  which is nonzero.

**Exact hunt** (`check_conepoly.py`), for every l <= 40:

- p_l (built in M = m^2) is rational, of degree l+1 in M, has p_l(1) = 0 and the stated leading
  coefficient;
- the weights w_{l,n}, computed from the double sum and not from the monomials, are all > 0 and
  reproduce p_l;
- p_l(1+x) has every coefficient of x^1..x^{2l+2} > 0 (a second certificate of positivity on (1, oo));
- p_l built from phi_k of the defining sum (Newton route) equals the polynomial at m = 1..30.

**Printed values.**

- alpha_0..alpha_4 = 1, -1/3, 1/15, -4/315, 1/315: confirmed.
- p_0 = (m^2-1)/12, p_1 = m^4/360 + m^2/36 - 11/360, p_2 = m^6/2520 + m^4/720 + m^2/180 - 37/5040: confirmed.
- (Next values, for the record: alpha_5..alpha_7 = -4/3465, 382/675675, -232/675675;
  p_3 = m^8/10080 + m^6/3780 + m^4/2160 + m^2/945 - 19/10080.)

**Literature check, at K = -1.**

- Schueth Thm 4.1 (printed p. 14) gives
  a_2 = [(1/2520)(k^5-1/k) + (1/720)(k^3-1/k) + (1/180)(k-1/k)]K^2 - [...]Delta K.
  At K = -1, Delta K = 0, this is p_2(k)/k = b_2(k), since 1/2520 + 1/720 + 1/180 = 37/5040.
- Rem. 4.2 (pp. 14-15) gives a_0 = (k-1/k)/12 = p_0(k)/k and
  a_1 = [(k^3-1/k)/360 + (k-1/k)/36]K = -p_1(k)/k = b_1(k).
- Exact for m = 2..30.

**Finding (MINOR, TF.5c).** The printed sentence says that p_1, p_2 "agree with the cone coefficients of
Schueth [Rem. 4.2, Thm 4.1], which she attributes to [DGGW, §5.6] at order t^1". It has two problems:

- The relative clause can be read as attributing both polynomials to DGGW. Schueth (p. 15) writes
  "Note that the above formulas for a_0 and a_1 were already computed in [8], 5.6". The order-t^2
  coefficient (Thm 4.1) is her own.
- p_0 also agrees, and "agree" hides the normalisation b_l = (-1)^l p_l/m.

Replacement: "At $K=-1$ the cone terms $b_0=p_0(m)/m$, $b_1=-p_1(m)/m$, $b_2=p_2(m)/m$ agree with
Schueth's $a^{(\{\bar p\})}_0,a^{(\{\bar p\})}_1$ \cite[Rem.~4.2]{schueth2019} and $a^{(\{\bar p\})}_2$
\cite[Thm~4.1]{schueth2019}; she notes that the first two were already computed in \cite[\S5.6]{dggw2008}
(there Prop.~5.5 and (5.10))."

Grades: TF.5a **NONE**, TF.5b **NONE**, TF.5c **MINOR**.

## TF.6 Remark rem:ucaragree

**Text check.** The printed c^S_k(pi/m) is Ucar (4.25) (printed p. 134, PDF p. 139) verbatim, with
Ucar's l -> k and k -> m:

  c^S_l(pi/k) = 1/(4k) * (-1)^l/(l+1)! * 1/(2l+1) * sum_{j=0}^{l+1} C(2l+2,2j)(k^{2j}-1) B_{2j} B_{2l+2-2j}(1/2).

Ucar (4.33) (printed p. 137) is C = sum_nu sum_{l<=nu} 2/(4^l l!) c^S_{nu-l}(pi/k) kappa^nu t^nu, and
(4.34) restates its coefficient. So at kappa = -1 Ucar's t^l coefficient is
(-1)^l sum_{i<=l} 2(4^i i!)^{-1} c^S_{l-i}(pi/m). There is no index shift: both sides use t^l for the
cone term, and the c^S index is the t-power before the e^{kappa t/4} convolution. The sign statement is
correct: p_l/m = (-1)^l times Ucar's coefficient, equivalently Ucar's coefficient = b_l.

**Proof for every l.** Only even indices occur, because B_{odd}(1/2) = 0 and only B_{2j} appears. Hence

  sum_j C(2k+2,2j) x^{2j} B_{2j} B_{2k+2-2j}(1/2) = (2k+2)! [z^{2k+2}] (xz/2)coth(xz/2) * z/(2 sinh(z/2)).

Also (2k+2)!/((k+1)!(2k+1)) = 2(2k)!/k!. So

  c^S_k(pi/m) = (1/4m)(-1)^k (2(2k)!/k!) [z^{2k+2}] F(z),  F(z) = z^2/(4 sinh(z/2)) * (m coth(mz/2) - coth(z/2)).

At z = 2iu, sinh(iu) = i sin u and coth(imu) = -i cot mu give F(2iu) = -4m u^2 Phi_m(u), so
[z^{2k+2}]F = (-1)^k m phi_k/4^k. Therefore, for every k,

  2 c^S_k(pi/m) = (2k)! phi_k(m)/(k! 4^k),

and equivalently m t^2 Phi_m(it/2) = F(t). Substitute into (bl):

  p_l/m = sum_k [4^{l-k}(l-k)!]^{-1} (2k)! phi_k/(k! 4^k) = sum_{i<=l} 2(4^i i!)^{-1} c^S_{l-i}(pi/m).

This proves the remark for every l.

**Smooth coefficients.** Ucar (4.35) (p. 137) at kappa = -1 is
vol (-1)^nu/(nu! 4^nu) sum_l C(nu,l)(-4)^l B_{2l}(1/2), with Z ~ (1/4pi t) sum a_nu t^nu. This is
alpha_nu Area exactly.

**Exact checks** (`check_ucar.py`), as polynomial identities in M = m^2, hence for every m:

- (a) 2c^S_k = (2k)!phi_k/(k!4^k), k <= 40;
- (b) p_l/m = sum 2(4^i i!)^{-1} c^S_{l-i}, l <= 40 (the requested l <= 12 is included);
- (c) Ucar's coefficient at kappa = -1 equals b_l, l <= 40;
- (d) (4.35) at kappa = -1 equals alpha_nu, nu <= 40;
- (e) the series identity m t^2 Phi_m(it/2) = F(t) through t^82, m = 1..12.

This independently confirms Ucar's extension of the spherical computation to kappa < 0 (his Thm 4.20,
which rests on Donnelly's structure theorem) at kappa = -1.

**Finding (MINOR, citation).** (4.33)-(4.34) define C and identify it for the spherical orbifolds
M/Z_k, M/D_k with M = S^2(r), kappa > 0 (Cor. 4.19, pp. 136-137). The statement that C is the contribution
of a cone point on an orbifold of arbitrary constant curvature, in particular kappa = -1, is Ucar Thm 4.20(ii)
(printed p. 138). The remark should cite it, as G5 item 10 already asks. Ucar's curvature symbol is kappa,
not K.

Replacement: "... which is $(-1)^l$ times U\c{c}ar's cone contribution \cite[Thm~4.20(ii), with
(4.33)--(4.34)]{ucar2017} at $\kappa=-1$."

Grade **MINOR**.

## TF.7 Remark 4.12 (`rem:proofC`): what the trace-formula route uses

**Inputs, exactly.** The derivation of the full expansion (TF.4, TF.5) from Z = I + E + Hyp uses:

1. **DS (1), the Selberg trace formula for cocompact Fuchsian groups with elliptic elements.** It is used
   for h_R = ĝ_R with g_R in C_c^inf even (LO.7). DS print the hypothesis as "h is any entire function of
   uniform exponential type and h(r) = h(-r)". Read literally this is too weak: h = 1 or h = cos r
   qualifies and the spectral side diverges. DS's next sentence, "The function g is the Fourier
   transform of h and thus is a compactly supported smooth function", fixes the intended class
   h = ĝ, g in C_c^inf. This is the class LO.7 uses.
2. **The passage R -> oo for the Gaussian h_t** (LO.7). h_t is entire but not of exponential type, and
   the justification is the cutoff lemma. On the spectral side it needs a counting bound
   #{lambda_j <= x} = O(x), which with uniform polynomial decay of h_R gives dominated convergence. For the
   finitely many lambda_j < 1/4, r_j is imaginary, and h_R(r_j) -> h_t(r_j) pointwise.
3. **On the geometric side,** the counting lemma LO.8 (purely geometric: area, diameter) for the hyperbolic
   sum, and Gauss-Bonnet for the area.
4. **Classical analysis:** Euler's beta integral (TF.1(i)), the Fermi moments (TF.4), Bernoulli numbers,
   and the partial-fraction / cot-sum identities (TF.2).

No coefficient c_j (j >= 1) of any source is used. The only heat-kernel input is the a-priori bound in
item 2, and #{lambda_j <= x} <= e Z(1/x) is the trivial Chebyshev step
Z(1/x) >= sum_{lambda_j<=x} e^{-lambda_j/x} >= e^{-1} #{...}.

**Does DGGW Thm 4.8 give Z(s) = O(1/s)?** Yes. Thm 4.8 (printed p. 17) states that the heat trace is
asymptotic to I_0 + sum_N I_N/|Iso(N)|, "of the form (4.9) (4 pi t)^{-dim(O)/2} sum_{j>=0} c_j t^{j/2}".
For dim O = 2 this gives Z(t) = c_0/(4 pi t) + O(t^{-1/2}) as t -> 0. Z is decreasing, so it is finite for
all t > 0, and Z(s) = O(1/s) on s in (0, 1]. This is all the remark claims. The citation "at order t^{-1}"
(G5 item 9) is apt.

**Is the independence claim correct?** As phrased in 2B ("does not use the coefficient computations of
DGGW or Ucar"; "determines no c_j with j >= 2"), yes. Two wording issues remain:

- (a) In version 2A the first paragraph calls the trace-formula route "a second, independent proof". The
  only external heat input is then drawn from DGGW Thm 4.8, whose full content (stratum-wise local
  contributions) already gives locality at constant curvature, and that is the *first* proof's source.
  Logically nothing is circular, because only the weak corollary O(1/s) is used. But "independent" is
  then true only of the coefficient computations, not of the cited theorem.
- (b) "(or of Weyl's law)" does not supply an independent source. The usual proof of Weyl's law on
  compact orbifolds goes through the leading heat-trace term (Karamata), that is, again through Thm 4.8 or
  its equivalent. (Instrument gap: no orbifold Weyl-law source fetched.)

**A self-contained replacement (verified by hand).** It removes the heat-kernel input entirely.

- Take psi in C_c^inf(R), even, psi >= 0, int psi = 1, supp psi in [-eps, eps], with
  2 eps < l (the systole) and eps <= 1. Then ψ̂(r) >= cos(eps r) >= 1/2 for |r| <= 1.
- Put h_T(r) = ψ̂(r-T)^2 + ψ̂(r+T)^2. It is even, of the admissible class, and its g is
  supported in [-2eps, 2eps], so the hyperbolic side of (1) is empty.
- The identity side is <= (A/4pi) int |r| h_T = O(T). Each elliptic side is <= int h_T = O(1).
- The finitely many imaginary r_j contribute O(1) uniformly in T.
- Since h_T >= 1/4 on |r - T| <= 1, (1) gives #{j : |r_j - T| <= 1} = O(T + 1), hence
  #{lambda_j <= x} = O(x).

**Findings (MINOR).**

1. Version 2A, first paragraph. Replace "The trace formula of Theorem~\ref{thm:IEH} gives a second,
   independent proof, with the coefficients (Remark~\ref{rem:proofC})." with "The trace formula of
   Theorem~\ref{thm:IEH} gives a second proof, which also produces the coefficients and does not use the
   locality theorem of \cite{donnelly1976,dggw2008} (Remark~\ref{rem:proofC})."
2. Both versions. Replace "which uses only the a-priori bound $\cZ_\Orb(s)=O(1/s)$ as $s\downarrow0$, a
   consequence of \cite[Thm~4.8]{dggw2008} (or of Weyl's law)" with "which uses only
   $\#\{\lambda_j\le x\}=O(x)$. This follows from \cite[Thm~4.8]{dggw2008} at order $t^{-1}$, or, with no
   heat-kernel input at all, from (1) applied to $h_T(r)=\hat\psi(r-T)^2+\hat\psi(r+T)^2$ with $\psi\in
   C_c^\infty$ even, nonnegative, of support shorter than the systole, which gives
   $\#\{j:|r_j-T|\le1\}=O(T+1)$." With this, "independent" holds literally.
3. Wherever DS (1) is quoted as Theorem thm:IEH (outside my bundle, but it is the input here): state the
   test-function class as "$h=\hat g$ with $g\in C_c^\infty(\R)$ even" rather than DS's "entire of uniform
   exponential type", which read literally admits h = 1.

Grade **MINOR**.

## TF.8 Theorem 1.2(iii)

### (a) The constant

Write B(l, D, t) for the right side of TF.3. By LO.9(a), |Z_1 - Z_2| = |H_1 - H_2| <= max(H_1, H_2), and
H_i <= B(l_i, D_i, t) for t <= T(l_i). With l = min l_i and D = max D_i, three facts hold:

- **T(x) = x^2/(2(1+x)) is increasing**: T' = (x^2+2x)/(2(1+x)^2) > 0. So t <= T(l) implies t <= T(l_i),
  and both lemmas apply.
- **B is increasing in D**: d log B/dD = 3.
- **B is strictly decreasing in l on {l : t <= T(l)}**:
  d/dl log B = -1/2 - [l/(2t) - (1+l)/l] - e^{-l}/(1-e^{-l}) - 2t/(l^2-t^2), and the bracket is >= 0
  exactly when t <= T(l) (symbolic check). Hence the derivative is < -1/2. Since t <= T(l) <= T(x) for all
  x >= l, the derivative is negative on the whole segment [l, l_i].

So B(l_i, D_i, t) <= B(l, D, t), and |Z_1 - Z_2| <= B(l, D, t). (Equivalently, rerun the TF.3 proof with
any lower bound l <= l_i: N_i vanishes below l_i, and f is decreasing on [l, oo).)

Finally, 1 + 2t/(l-t) is increasing in t (derivative 2l/(l-t)^2), with value (2+3l)/(2+l) at t = T, and
pi/sqrt(4 pi) = sqrt(pi)/2. Hence

  C(A,l,D) = sqrt(pi) e^{3D} l e^{l/2} (2+3l) / (2A(1-e^{-l})(2+l)),

which is the printed constant (sympy identity).

`check_hypbound.py` covers:

- items 1-2, symbolic and exact;
- item 3, mpmath **interval** arithmetic: B(l_2,D,t) < B(l_1,D,t) in 390 grid cases,
  l in [0.01, 20], t = theta T(l_1), theta in {0.001, 0.1, 0.5, 0.9, 1}.

Grade **NONE**. The proof write-up must contain the monotonicity line above. As stated, the lemma bounds
each orbifold by its own systole and diameter, and the replacement by min/max is not automatic.

### (b) "Attained"

From DS (1), Z_1 - Z_2 = H_1 - H_2 = sum_L (w_1(L) - w_2(L))/(2 sinh(L/2)) * e^{-t/4}e^{-L^2/4t}/sqrt(4 pi t),
with w_i(L) = sum over hyperbolic classes [gamma] of length L of l(gamma_0). The sum is over the discrete
union of the two length spectra.

- Let L_* be the first length with w_1 != w_2, and L' > L_* the next length in the union.
- The tail over L >= L' is bounded, as in TF.3 with lower cut L', by O(t^{-1/2} e^{-L'^2/4t}), which is
  o(t^{-1/2} e^{-L_*^2/4t}).
- Hence sqrt t e^{L_*^2/4t}(Z_1 - Z_2) -> (w_1 - w_2)(L_*)/(2 sinh(L_*/2) sqrt(4 pi)) != 0.

The three cases follow:

- **L_* = l:** the nonzero limit is as printed.
- **L_* > l:** the difference is exactly of order t^{-1/2} e^{-L_*^2/4t}.
- **w_1 = w_2:** then H_1 = H_2, and Z_1 = Z_2 because I, E depend only on the signature. So the orbifolds
  are isospectral (Laplace transform uniqueness). Conversely, isospectral implies Z_1 = Z_2 and hence
  w_1 = w_2 by the asymptotics above. The "equivalently" is correct, given equal signature.

**Different systoles.** If l_1 < l_2, then w_1(l_1) = l_1 * #{classes of length l_1} > 0 = w_2(l_1)
(a class of minimal length is primitive). So L_* = l, and "in particular" is correct.

**What the weight counts.** Every hyperbolic class is gamma_0^k for a unique primitive class: the
centraliser of a hyperbolic element of a Fuchsian group is infinite cyclic, since an elliptic element
fixes no boundary point. So w(L) = sum_{k>=1} (L/k) n_prim(L/k) and n_all(L) = sum_k n_prim(L/k). By
induction on the discrete lengths, w_1 = w_2 below L iff n_prim agree below L iff n_all agree below L, and
at the first such L all three differ. So "first differ" is the same for the weighted spectrum, the
spectrum of all classes, and the primitive spectrum. The weight is harmless, and the limit is nonzero
exactly when the weighted multiplicities differ at l.

`check_hypbound.py` item 4 verifies this combinatorial equivalence exactly on 4000 random pairs,
including adversarial compensations at 2p.

**Conjugacy classes versus geodesics.** DS p. 3 identify hyperbolic conjugacy classes with oriented
periodic geodesics, including those through cone points. Classes with gamma ~ gamma^{-1} (an order-2
rotation reversing the axis) are single classes, and the formula counts classes. The closing sentence
"the systole is the least length of a closed geodesic, including those through cone points" is the
correct definition (cf. TF.3).

Grade **NONE**.
