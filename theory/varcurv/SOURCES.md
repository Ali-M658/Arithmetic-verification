# Sources for theory/varcurv

Fetched 2026-10-08 with `curl` from arxiv.org (desktop User-Agent), text extracted with PyMuPDF; PDFs kept
in the session scratchpad, not in the repository. Every statement below is transcribed from the
extracted text (equation layout repaired by hand; no formula is recalled). SHA-256 of the PDFs:

| arXiv | published version | sha256 of fetched PDF |
|---|---|---|
| 1812.06119v1 | D. Schueth, *On the corner contributions to the heat coefficients of geodesic polygons*, Ann. Inst. Fourier 69 (2019) no. 7, 2827-2855, doi:10.5802/aif.3338 | `8a3948ae0216d2f670f9fd3e7b996e6c8bccc0c7b5c8d3c04b85bc3928415a82` |
| 2511.22255v1 | D. Schueth, *Heat coefficients of surfaces with curved conical singularities*, Ann. Global Anal. Geom. 69 (2026), no. 1, Paper No. 2, doi:10.1007/s10455-025-10024-1 | `20e6ce87733fbbeca6e7bec8126de866c706b181a899af703c090e3224252028` |
| 0805.3148 | E. Dryden, C. Gordon, S. Greenwald, D. Webb, *Asymptotic expansion of the heat kernel for orbifolds*, Michigan Math. J. 56 (2008) 205-238 | `bda49c2124b25df3873f7d0fff5b2bc3d9ac683340646d816d7414065e89c892` |

The journal data for the two Schueth papers are those already verified in the vault notes
`181206119-schueth-corner-contributions-ar5iv-fulltext` and
`heat-coefficients-of-surfaces-with-curved-conical-singularities` (publisher pages). Ucar's
constant-curvature formulas are used through `theory/cone-coefficients/ucar-source.md` (transcribed
there from arXiv:1711.03405, eqs. (4.25), (4.33)-(4.34)) and Paper A, Proposition `prop:heatinput`.

Sign convention in all three sources and here: `Delta_g = -div grad` (Schueth 2019, p. 3 and Sec. 2).

## 1. Schueth 2019 (arXiv:1812.06119)

**Abstract.** "Let O be a compact Riemannian orbisurface. We compute formulas for the contribution of
cone points of O to the coefficient at t^2 of the asymptotic expansion of the heat trace of O, the
contributions at t^0 and t^1 being known from the literature. [...] The main novelty here is the
determination of the way in which the Laplacian of the Gauss curvature at the corner point enters
into the coefficient at t^2."

**2.1 (i), (4)** (Jacobi field length, unit u, Jacobi field J with J(0)=0, J'(0) unit, orthogonal to u):
`l_u(r) = r - (1/6)K(p) r^3 - (1/12) dK_p(u) r^4 + ((1/120)K(p)^2 - (1/40) Hess K_p(u,u)) r^5 + O(r^6)`.

**(6)** `u_0(p, exp_p(ru)) = 1 + (1/12)K(p) r^2 + (1/24) dK_p(u) r^3 + ((1/160)K(p)^2 + (1/80) Hess K_p(u,u)) r^4 + O(r^5)`.

**(7)** (Berger, in dimension two) `u_2(p,p) = (1/15)K(p)^2 - (1/15) Delta_g K(p)`.

**Lemma 2.2, (8)** `u_1(p, exp_p(ru)) = (1/3)K(p) + (1/6)dK_p(u) r + ((1/30)K(p)^2 - (1/120)Delta_g K(p) + (1/20) Hess K_p(u,u)) r^2 + O(r^3)`.

**3.1 / (12).** For an isometry Phi of a neighbourhood of p with Phi(p)=p, dPhi_p = rotation by phi in
(0, pi]: `I(t) = int_U H(t, q, Phi(q)) dvol(q) ~ sum_l b_l(Phi) t^l`.

**Remark 3.2.** "Donnelly's formulas for b_0 and b_1 amount to
`b_0(Phi) = (2 - 2cos phi)^{-1}` and `b_1(Phi) = 2K(p)(2 - 2cos phi)^{-2}`."

**Lemma 3.4.** "dK_p = 0. Moreover, if phi in (0, pi) then Hess K_p = -(1/2) Delta_g K(p) g_p."

**(15)-(16)** (proof of Thm 3.7): the substitution `z = d_u(r)/sqrt(t)` with `d_u(r) = dist(exp_p(ru), exp_p(r D_phi u))`,
`I~(t) = int_{S^1} int_0^{eta/sqrt t} H(t, ...) sqrt(t) l_u(d_u^{-1}(z sqrt t)) (d_u^{-1})'(z sqrt t) dz du`,
H approximated by `(4 pi t)^{-1} e^{-z^2/4} (sum_{i<=2} u_i t^i + O(t^3))`; and
`int_0^oo e^{-z^2/4} z^{2k+1} dz = 2^{2k+1} k!`.

**Theorem 3.7.** "In the situation of 3.1, and with C := sqrt(2 - 2cos phi), the coefficient b_2(Phi) in (12) is given by
`b_2(Phi) = (12/C^6 - 2/C^4) K(p)^2 - (2/C^6) Delta_g K(p)`."

**(17)** (from DGGW): for a cone point p-bar of order k arising from a rotation Phi with angle 2pi/k,
`a_l^{({p-bar})} = (1/k) sum_{j=1}^{k-1} b_l(Phi^j)`.

**Theorem 4.1.** "Let p-bar in (O, g) be a cone point of order k in N as above. Then
`a_2 = [ (1/2520)(k^5 - 1/k) + (1/720)(k^3 - 1/k) + (1/180)(k - 1/k) ] K(p-bar)^2
     - [ (1/15120)(k^5 - 1/k) + (1/1440)(k^3 - 1/k) + (1/180)(k - 1/k) ] Delta_g K(p-bar)`."
Proof uses `sum_{j=1}^{k-1} sin^{-4}(j pi/k) = (k^4-1)/45 + 2(k^2-1)/9` and
`sum_{j=1}^{k-1} sin^{-6}(j pi/k) = 2(k^6-1)/945 + (k^4-1)/45 + 8(k^2-1)/45`.

**Remark 4.2.** `a_0 = (1/12)(k - 1/k)`, `a_1 = [(1/360)(k^3 - 1/k) + (1/36)(k - 1/k)] K(p-bar)`,
"using `sum_{j=1}^{k-1} 1/sin^2(j pi/k) = (k^2-1)/3` and `b_0(Phi) = 1/C^2`, `b_1(Phi) = 2K(p)/C^4`" [the extracted
text prints `b_0 = 1/C`, `b_1 = 2K/C^2`, with C^2 lost to the extraction; Remark 3.2 fixes the powers].

## 2. Schueth 2026 (arXiv:2511.22255)

**Setting (Notation 2.1, (1)).** Near the cone point, `g = dr^2 + f(r)^2 dtheta^2`, theta on the circle of
length 2pi, f smooth on [0, eps), f(0)=0, f'(0)>0.

**(2)** `tr exp(-t Delta) ~ (4 pi t)^{-1} sum_j a_j(M) t^j + sum_j b_{j/2}(C) t^{j/2} + sum_j c_{j/2}(C) t^{j/2} log t`.
"`b_0(C) = (1/12)(1/f'(0) - f'(0))` [...] `c_0(C) = 0` [...] and `c_{j/2}(C) = 0` for all odd j."

**Introduction, p. 2.** "For cone points C of order n in two-dimensional Riemannian orbifolds, it was
shown in [5] that `b_1(C) = [(1/360)(n^3 - 1/n) + (1/36)(n - 1/n)] K(p)` [...]. In [10], the author obtained
a similar formula for b_2(C) in the same context; b_2(C) turns out to be linear combination of K(p)^2 and
(Delta K)(p), where the coefficients are, again, rational functions of the order of the cone point. The
cited results for b_1(C) and b_2(C) in the orbifold case do not assume full rotational symmetry".
"Ucar [13] obtained explicit formulas for all b_l(C) for cone points C of two-dimensional orbifolds under
the special assumption that the orbifold has constant curvature kappa [...] b_l(C) can then be written as
kappa^l times (1/n) p_l(n), where [...] p_l is a certain polynomial of order 2l+2."
"We note here, without proving it in this paper, that in the case of full rotational symmetry around C,
it would be possible to reprove the formulas for b_1(C) [...] and for b_2(C) [...] For this, it plays no
role at all whether n = 1/f'(0) > 0 is a natural number or not."
"it is well-known that `f(r) = r - (1/6)K(p) r^3 + O(r^4)`; in particular, f''(0) = 0. Passing to an orbifold
cone point of order n just corresponds to passing from f to f/n, so f''(0) = 0 still holds for cone points
in orbisurfaces."
"If f''(0) != 0 in (1), then, unlike in the orbifold case, half powers of t can occur in the middle sum of
(2), and logarithmic terms can occur, too. For example, it turns out that `c_1(C) = -(1/60) f''(0)^2/f'(0)`."

**Abstract / (3) / Theorem 4.1.** Explicit formula for b_{1/2}(C); "In the case that the Gaussian curvature
K of (M, g) satisfies |K(p)| -> infinity as p -> C, we show that b_{1/2}(C) varies irrationally under
constant rescalings of the distance circles near the cone point. This is a sharp contrast to the behavior
of b_0(C) and of those coefficients b_j(C) which appear in certain known formulas in the case of orbifold
cone points or corners of geodesic polygons." `b_{1/2}(C) = (2 f''(0)/(sqrt(pi) f'(0))) int_0^1 (h^_{2,alpha}(1-u^2) - (1/4) h^_{0,alpha}(1-u^2)) du`, alpha = 1/f'(0).

## 3. Dryden-Gordon-Greenwald-Webb (arXiv:0805.3148)

**4.1 (Locality).** "For a in W, b_k((M, gamma), a) depends only on the germs at a of the Riemannian metric
of M and of the isometry gamma."

**4.2 (Donnelly).** For a fixed point component W, `A_gamma(x) = gamma_* on T_x(W)^perp`,
`B_gamma(x) = (I - A_gamma(x))^{-1}`. "Donnelly showed that `b_k(gamma, x) = |det(B_gamma(x))| b~_k(gamma, x)`,
where b~_k(gamma, .) is an O(m) x O(n - m) universal invariant polynomial in the components of B_gamma and
in the curvature tensor R of M and its covariant derivatives." `b_0(gamma, x) = |det(B_gamma(x))|`.

**Theorem 4.8.** The heat trace of a Riemannian orbifold is asymptotic to `I_0 + sum_{N in S(O)} I_N/|Iso(N)|`
[...] "of the form `(4 pi t)^{-dim(O)/2} sum_j c_j t^{j/2}`".

**Proposition 4.11 (Donnelly).** `int_M K(t, x, gamma(x)) dvol ~ sum_W (4 pi t)^{-dim(W)/2} sum_k t^k int_W b_k(gamma, a) dvol_W(a)`.

**Proposition 5.5.** For a cone point of order m, `I_N = (m^2 - 1)/12 + O(t)`; proof: `I_N = sum_{j=1}^{m-1} 1/(4 sin^2(j pi/m)) + O(t)`.

**Example 5.6, (5.7).** Degree-zero term of an orientable 2-orbifold with cone points of orders m_i:
`chi(O)/6 + sum_i (m_i^2 - 1)/(12 m_i)`, using Gauss-Bonnet `a_1 = (2pi/3) chi(O)` "valid also for orbifolds".
In dimension two, `B_{gamma_j} = [[1/2, -sin(2j pi/m)/(2 - 2cos(2j pi/m))], [sin(2j pi/m)/(2 - 2cos(2j pi/m)), 1/2]]`,
`b_1(gamma_j) = R_1212/(8 sin^4(j pi/m))`.

## How each source is used

| claim here | uses |
|---|---|
| VC1 structure | DGGW 4.1-4.2 (locality; Donnelly form with B = (I-A)^{-1}), Schueth 2019 (15)-(17) (substitution method) |
| VC2 top coefficient | Schueth 2019 (15)-(16); checked against Thm 3.7, Thm 4.1, Remark 3.2/4.2 and Ucar |
| VC3 t^3 | own computation (twisted_mp.py); checked against (6), (7), (8), Remark 3.2, Thm 3.7, Thm 4.1, Ucar |
| VC4 extension | DGGW 4.1 (locality), Ucar / Paper A eq. (bl) with kappa^l |
| VC5, VC6 obstruction | DGGW 4.1, 4.8, (5.7); Schueth 2019 (7) (normalisation of the quadratic form) |
| remark on non-orbifold cones | Schueth 2026 (2), c_1, b_{1/2}, Theorem 4.1 |
