# Locality: what the heat expansion of a hyperbolic 2-orbifold can and cannot hear

Status: T1–T3 proved below. Every quoted statement was read in a fetched copy of the
source; retrieval routes are in `fetch_sources.sh`, and the one source that could not be
fetched (Donnelly 1976) is logged in `review/outstanding-fetches.md`. The exact identities
used in the proofs are checked by `check_locality.py` (exact rational and algebraic
arithmetic, real asserts). The adversarial review is recorded in `attack-log.md`.

**Setting.** $\mathcal O=\Gamma\backslash\mathbb H^2$ is a closed orientable hyperbolic
2-orbifold, i.e. $\Gamma\subset PSL(2,\mathbb R)$ is a cocompact Fuchsian group. Its
signature $\sigma(\mathcal O)=(g;m_1,\dots,m_n)$ is as in `\label{def:signature}`
(`theory/definitions.tex`). $\Delta\ge0$ is the Laplacian, $0=\lambda_0<\lambda_1\le\dots$ its
eigenvalues, $Z_{\mathcal O}(t)=\sum_j e^{-\lambda_j t}$ its heat trace, and $c_j(\mathcal O)$
the coefficients of `\label{def:heatcoef}`. The orbifold Euler characteristic is
$\chi(\mathcal O)=2-2g-\sum_i(1-1/m_i)$. By the orbifold Gauss–Bonnet theorem,
$\operatorname{Area}(\mathcal O)=-2\pi\chi(\mathcal O)$ [Thurston, 13.3.5 and the sentence
after it, "If O is elliptic or hyperbolic, then area(O) = 2π|χ(O)|", p. 313; DS, Thm 3.2].

**The physical picture.** For a short time $t$, heat injected at a point explores a ball
of radius about $\sqrt t$. In that time it can learn only what lies inside the ball: the
curvature (the same everywhere, $K=-1$) and, near a cone point, the cone angle $2\pi/m$.
Every term of the small-$t$ expansion is built from such local measurements, added up over
the orbifold. The global shape (the moduli) is encoded in how the orbifold closes up on
itself: in its closed geodesics. Heat learns that a geodesic of length $\ell$ closes only
after it has travelled the whole loop, and the amplitude for that is the Gaussian factor
$e^{-\ell^2/4t}$. That factor vanishes faster than any power of $t$, so it never appears in
the expansion. This is T1. T3 makes the factor explicit, with constants, and shows that it
is really there.

**Sources** (all in `sources_cache/`, re-created by `fetch_sources.sh`):

| key | source | what is used | location in the fetched copy |
|---|---|---|---|
| [DGGW] | Dryden, Gordon, Greenwald, Webb, *Asymptotic expansion of the heat kernel for orbifolds*, Michigan Math. J. 56 (2008) 205–238, arXiv:0805.3148 | Thm 4.8 (heat trace of an orbifold); Donnelly's locality and universality of $b_k$; Def. 4.7; the orientable 2-orbifold strata | §4.1, §4.2, Def. 4.7, Thm 4.8 (pp. 15–17); §5.6 (p. 24) |
| [Don] | Donnelly, *Spectrum and the fixed point sets of isometries I*, Math. Ann. 224 (1976) 161–170 | the functions $b_k(\gamma,\cdot)$ | **not fetched** (paywalled; Unpaywall: not OA). Quoted only as restated in [DGGW] §4.1–4.2 |
| [Uçar] | Uçar, PhD thesis, HU Berlin 2017, arXiv:1711.03405 | Thm 4.11 (the [DGGW] expansion for 2-orbifolds); Thm 4.20 (all coefficients at constant curvature), eqs. (4.33), (4.35) | pp. 125, 137–138 |
| [Th] | Thurston, *The Geometry and Topology of Three-Manifolds*, ch. 13, electronic ed. 1.1 (2002), SLMath mirror | Gauss–Bonnet 13.3.5; Thm 13.3.6; Cor. 13.3.7 (dimension of $T(\mathcal O)$) and its proof | pp. 313, 315–318 (original pagination 13.20–13.28) |
| [DS] | Dryden, Strohmaier, *Huber's theorem for hyperbolic orbisurfaces*, Canad. Math. Bull. 52 (2009), arXiv:math/0504571v2 | trace formula eq. (1) and its normalisation; Thm 1.1; Thm 3.2 | pp. 2–4 |
| [Mar] | Marklof, *Selberg's trace formula: an introduction*, arXiv:math/0407288v2 | Thm 4 and Prop. 10: the heat function is admissible (torsion-free case) | pp. 25–27 |
| [DR] | Doyle, Rossetti, *Laplace-isospectral hyperbolic 2-orbifolds are representation-equivalent*, arXiv:1103.4372v2 | Thm 1 | pp. 1–2 |
| [LV] | Linowitz, Voight, *Small isospectral and nonisometric orbifolds of dimension 2 and 3*, Math. Z. 281 (2015) 523–569, arXiv:1408.2001v2 | Thm A and the sentence after it | p. 2 |

---

## T1. Signature locality

**Theorem 1 (signature locality).** There are universal constants $\alpha_k$
($k\ge0$) and $\beta_k(m)$ ($k\ge0$, $m\ge2$) such that every closed orientable hyperbolic
2-orbifold $\mathcal O$ of signature $(g;m_1,\dots,m_n)$ satisfies
$$
Z_{\mathcal O}(t)\;\sim\;\frac{\operatorname{Area}(\mathcal O)}{4\pi t}\sum_{k\ge0}\alpha_k t^k
\;+\;\sum_{i=1}^n\sum_{k\ge0}\beta_k(m_i)\,t^k\qquad(t\downarrow0),
\qquad \operatorname{Area}(\mathcal O)=2\pi\Big(2g-2+\sum_i\big(1-\tfrac1{m_i}\big)\Big).
$$
Consequently $c_1=\operatorname{Area}/4\pi$ and, for $j\ge2$,
$c_j(\mathcal O)=\alpha_{j-1}\operatorname{Area}(\mathcal O)/4\pi+\sum_i\beta_{j-2}(m_i)$, a
function of $\sigma(\mathcal O)$ alone. This proves `\label{thm:locality}` (the forward
reference in `theory/definitions.tex`), with
$\Phi_j(g;m_1,\dots,m_n)=\alpha_{j-1}\tfrac{1}{2}\big(2g-2+\sum_i(1-\tfrac1{m_i})\big)+\sum_i\beta_{j-2}(m_i)$.
In particular two orbifolds of the same signature have the same expansion to all orders.

The constants are explicit [Uçar, Thm 4.20 (i), (ii) at $\kappa=-1$]:
$\alpha_k=\frac{(-1)^k}{k!\,4^k}\sum_{l=0}^k\binom kl(-4)^lB_{2l}(\tfrac12)$, and $\beta_k(m)$ is
the coefficient of $t^k$ in $C$ of [Uçar, (4.33)], built from $c^S_\ell(\pi/m)$ of (4.25). These
are the formulas implemented in `numerics/theory.py` and asserted there against DGGW §5.6
and Schueth's Theorem 4.1 for $k\le2$.

*Proof A (local invariants; [DGGW] and Donnelly as restated there).*

1. *Strata.* An orientable 2-orbifold has only isolated singular points, the cone points
   [DGGW §5.6: "An orientable 2-orbifold O can have only isolated singularities, i.e., cone
   points"]. So the strata are the regular part and the $n$ points $N_i=\{p_i\}$, with
   isotropy $\mathbb Z_{m_i}$ and $|\mathrm{Iso}(N_i)|=m_i$.
2. *The expansion.* [DGGW, Thm 4.8]: the heat trace is asymptotic to
   $I_0+\sum_N I_N/|\mathrm{Iso}(N)|$, where (Def. 4.7) $I_0=(4\pi t)^{-1}\sum_k a_kt^k$ with
   $a_k=\int_{\mathcal O}u_k\,d\mathrm{vol}$, and $I_N=(4\pi t)^{-\dim N/2}\sum_kt^k\int_N b_k(N,x)\,d\mathrm{vol}_N$.
   [Uçar, Thm 4.11] restates this for 2-orbifolds. For a point stratum,
   $\dim N=0$ and $I_N=\sum_kt^kb_k(N,p)$, with
   $b_k(N,p)=\sum_{\gamma\in\mathrm{Iso}^{\max}(\tilde N)}b_k(\gamma,\tilde p)$ [DGGW 4.5, 4.7(i)].
3. *Regular stratum.* The $u_k$ "are defined in terms of the curvature and its covariant
   derivatives on any Riemannian manifold" [DGGW 4.7(iii)]: $u_k(x)$ is a universal
   expression in the metric's jet at $x$, invariant under isometries. Every regular point of
   $\mathcal O$ has a neighbourhood isometric to a disk in $\mathbb H^2$, and $\mathbb H^2$ is
   homogeneous, so $u_k(x)=u_k^{\mathbb H}$ is the same number at every regular point of every
   hyperbolic orbifold. The cone points have measure zero. Hence
   $a_k=u_k^{\mathbb H}\operatorname{Area}(\mathcal O)$; put $\alpha_k=u_k^{\mathbb H}$.
4. *Cone points.* Near $p_i$ take the chart $(\tilde U,\mathbb Z_{m_i})$: $\tilde U$ is a disk in
   $\mathbb H^2$ about a lift $\tilde p$, and the isotropy group is generated by the rotation
   $\rho_{\tilde p}$ through $2\pi/m_i$. $\mathrm{Iso}^{\max}(\tilde N)$ is the set of the $m_i-1$
   nontrivial rotations $\rho_{\tilde p}^{\,j}$, since each fixes exactly $\tilde p$. [DGGW §4.1]
   states the two properties of Donnelly's $b_k$:
   *locality* ("$b_k((M,\gamma),a)$ depends only on the germs at $a$ of the Riemannian
   metric of M and of the isometry γ") and *universality* (if $\sigma$ is an isometry with
   $\sigma\circ\gamma=\gamma'\circ\sigma$ then $b_k((M,\gamma),x)=b_k((M',\gamma'),\sigma(x))$).
   For two cone points of the same order $m$, on the same or on different orbifolds, the
   orientation-preserving isometry $\sigma$ of $\mathbb H^2$ with $\sigma(\tilde p)=\tilde q$
   conjugates $\rho_{\tilde p}^{\,j}$ to $\rho_{\tilde q}^{\,j}$, rotation through the same angle
   in the same sense. By locality and universality,
   $b_k(\rho_{\tilde p}^{\,j},\tilde p)=b_k(\rho_{\tilde q}^{\,j},\tilde q)$. Summing over $j$,
   $b_k(N_i,p_i)=:\tilde\beta_k(m_i)$ depends only on $m_i$. Put $\beta_k(m)=\tilde\beta_k(m)/m$.
5. *Assembly.* Theorem 4.8 gives the displayed expansion. Gauss–Bonnet [Th 13.3.5; DS Thm
   3.2] gives the area in terms of $\sigma$. Matching powers, $t^{-1}$ carries
   $\alpha_0\operatorname{Area}/4\pi$ with $\alpha_0=u_0^{\mathbb H}=1$, and $t^{j-2}$ for
   $j\ge2$ carries the stated combination. ∎

*What the proof uses and what it does not.* Locality alone forces the regular-stratum
coefficients to be proportional to the area. The cone contributions are fixed numbers
attached to each order. No property of the moduli enters, because no local invariant can
detect them: any two hyperbolic orbifolds of the same signature are locally isometric,
point by point and cone point by cone point.

*Proof B (explicit constants).* [Uçar, Thm 4.20] computes, for a closed 2-orbifold of
constant curvature $\kappa$: (i)
$a_\nu(\mathcal O)=\frac{\operatorname{vol}(\mathcal O)}{\nu!\,4^\nu}\sum_{\ell=0}^\nu\binom\nu\ell(-4)^\ell B_{2\ell}(\tfrac12)\kappa^\nu$
(4.35); (ii) a cone point of order $k$ contributes $I_N/|\mathrm{Iso}(N)|=C$ with $C$ given by
(4.33). At $\kappa=-1$ this is Theorem 1 with explicit $\alpha_k$, $\beta_k(m)$.

*Proof C (trace formula; independent of [DGGW] and [Uçar]).* By Theorem 3.1 below,
$Z=I+E+H$. $I$ depends only on the area and $E$ only on the cone orders. By step 4 of the
proof of Theorem 3.4(b), $0\le H(t)=O(t^{-1/2}e^{-\ell_{\rm sys}^2/4t})=O(t^N)$ for every $N$. So the asymptotic
series of $Z$ is that of $I+E$, a function of $\sigma$. `check_locality.py` verifies
exactly that the asymptotic series of $I$ and of $E$ equal Proof B's $\alpha_k$ and
$\beta_k(m)$:

- for the identity term, through the Fermi–Dirac moments
  $\int_0^\infty r^{2k+1}(e^{2\pi r}+1)^{-1}dr=(1-2^{-2k-1})(-1)^kB_{2k+2}/(4(k+1))$, for
  $k\le14$;
- for the elliptic term, through $\int_{\mathbb R}e^{-ar}(1+e^{-2\pi r})^{-1}dr=1/(2\sin(a/2))$
  differentiated in $a$, for $\nu\le5$ and $m\in\{2,3,4,5,6,8,12\}$, in exact algebraic
  arithmetic.

So Proofs A–C agree on every constant that was checked. ∎

---

## T2. Moduli, and why $K_{\rm iso}=\infty$

**Source statement** [Th, Corollary 13.3.7, electronic ed. p. 318, original p. 13.27],
verbatim: *"The Teichmüller space T(O) of an orbifold O with χ(O) < 0 is homeomorphic to
Euclidean space of dimension −3χ(X_O) + 2k + l, where k is the number of elliptic points and
l is the number of corner reflectors."* The proof (p. 318) cuts $\mathcal O$ along disjoint
closed geodesics and arcs perpendicular to $\partial X_{\mathcal O}$ into primitive pieces. It
then states: *"The lengths of the arcs, and lengths and twist parameters for simple closed
curves form a set of parameters showing that T(O) is homeomorphic to Euclidean space of
some dimension."* The primitive pieces are listed on pp. 315–317. The only closed orientable
piece is $S^2(n_1,n_2,n_3)$, which has a unique hyperbolic structure. The others have
boundary, and their structures are "parametrized by the lengths of their boundary
components". McOwen and Troyanov were not needed for this statement. Troyanov's Theorem A
remains the input to `\label{prop:rigidity}`.

**Proposition 2.1.** For a closed orientable hyperbolic 2-orbifold of signature
$(g;m_1,\dots,m_n)$,
$$\dim_{\mathbb R}T(\mathcal O)=6g-6+2n .$$
Among hyperbolic signatures, it vanishes exactly for $(g;n)=(0;3)$, the triangle orbifolds,
and is $\ge2$ otherwise.

*Proof.* $X_{\mathcal O}$ is the closed orientable surface of genus $g$, so
$\chi(X_{\mathcal O})=2-2g$. There are no corner reflectors ($l=0$) and $k=n$, so
Corollary 13.3.7 gives $-3(2-2g)+2n$. Now $6g-6+2n=0$ iff $3g+n=3$ iff
$(g,n)\in\{(1,0),(0,3)\}$. $(1;\,)$ is the flat torus, with $\chi=0$, not hyperbolic. When
$g=0$ and $n\le2$, $\chi=2-\sum_i(1-1/m_i)>0$, also not hyperbolic. Every other hyperbolic
signature has $6g-6+2n>0$, and the value is even. ∎

This supplies the general-genus count that `theory/definitions.tex` (eq:moduli and the
comment after it) flagged as unsourced. For $g=0$ it reproduces eq:moduli,
$\dim=2n-6$, now in one sentence of one source rather than by a two-step deduction.

**Proposition 2.2.** If $6g-6+2n>0$, the closed orientable hyperbolic orbifolds of
signature $\sigma=(g;m_1,\dots,m_n)$ fall into uncountably many isometry classes.

*Proof.* Since $\dim T(\mathcal O)>0$, $\mathcal O$ is not one of Thurston's closed primitive
pieces, so the decomposition in the proof of 13.3.7 cuts along at least one closed geodesic
$c$. Its length $\ell_c$ is one of the coordinates of the homeomorphism
$T(\mathcal O)\cong\mathbb R^d$, and the boundary-length parameters of the pieces range over all
of $(0,\infty)$ [Th, pp. 315–316: the pieces "have hyperbolic structures parametrized by the
lengths of their boundary components"; for $D^2(;m_1,\dots,m_l)$, "parametrized by the lengths
of the cuts; that is, $(\mathbb R^+)^{l-3}$"]. So $\ell_c:T(\mathcal O)\to(0,\infty)$ is onto.

Points of $T(\mathcal O)$ are hyperbolic structures with a marking. If $Y,Y'\in T(\mathcal O)$
are isometric as unmarked orbifolds, then $\ell_c(Y')$ is the length of a closed geodesic
of $Y'$, hence of $Y$. So $\ell_c$ maps each isometry class into the length set of one
orbifold. That set is countable, since closed geodesics correspond to conjugacy classes of
the countable group $\Gamma$ [DS p. 3]. An uncountable image $(0,\infty)$ cannot be covered
by countably many countable sets. ∎

**Corollary 2.3 ($K_{\rm iso}=\infty$).** Let $\sigma$ be a hyperbolic signature with
$6g-6+2n>0$, i.e. any closed orientable hyperbolic 2-orbifold that is not a triangle
orbifold. Let $\mathcal P$ be a comparison class (`\label{def:K}`) containing every orbifold
of signature $\sigma$. Examples: the class of all closed orientable hyperbolic
2-orbifolds; for $g=0$, the class $\mathcal P_n$ of `\label{rem:nconerestated}`. Then
$$K_{\rm iso}(\mathcal O;\mathcal P)=\infty\qquad\text{for every }\mathcal O\in\mathcal P\text{ with }\sigma(\mathcal O)=\sigma .$$
For the triangle orbifolds ($g=0$, $n=3$), $K_{\rm iso}(\mathcal O;\mathcal P)=K_{\rm mult}(\mathcal O;\mathcal P)$ for
every class $\mathcal P$.

*Proof.* By Proposition 2.2 there is an $\mathcal O'\in\mathcal P$ of signature $\sigma$ not
isometric to $\mathcal O$. By Theorem 1, $H_k(\mathcal O')=H_k(\mathcal O)$ for every $k$. So no
$k$ satisfies the condition defining $K_{\rm iso}$, and the minimum over the empty set is
$\infty$.

For triangle orbifolds, equal signature implies isometry. This is `\label{prop:rigidity}`
(via Troyanov); equivalently, $T(\mathcal O)\cong\mathbb R^0$ is a point by Proposition 2.1, so
any two hyperbolic structures on $\mathcal O$ differ by a diffeomorphism. Hence for any
$\mathcal O'\in\mathcal P$, "$\sigma(\mathcal O')=\sigma(\mathcal O)$" and "$\mathcal O'\cong\mathcal O$" are
the same condition, and the two minima in `\label{def:K}` coincide. ∎

*Consequences for the manuscript.*

- Corollary 2.3 settles `\label{prop:Kinf}` unconditionally, since its hypothesis
  `\label{thm:locality}` is now Theorem 1.
- Corollary 2.3 extends `\label{prop:Kinf}` from $g=0$, $n\ge4$ to every non-triangle
  signature.
- The statement in `\label{rem:ncone}` of `paper/main.tex` that "the upper bound $K\le n$
  extends the $n=3$ case of Theorem~\ref{thmC}" is true for $K_{\rm mult}$ (proved for all
  $n$ in `theory/audibility/`). It is false for any isometry-level reading of $K$.
- What makes `\label{thmC}` an isometry statement is the rigidity of triangle orbifolds.

---

## T3. Where the moduli become audible

### 3.1 The decomposition

**Theorem 3.1.** For every $t>0$,
$$Z_{\mathcal O}(t)=I(t)+E(t)+H(t),$$
with all series and integrals absolutely convergent, where

- $I(t)=\dfrac{\operatorname{Area}(\mathcal O)}{4\pi}\displaystyle\int_{\mathbb R}r\tanh(\pi r)\,e^{-t(1/4+r^2)}dr$ (identity term);
- $E(t)=\displaystyle\sum_{i=1}^nE_{m_i}(t)$, with $E_m(t)=\displaystyle\sum_{l=1}^{m-1}\frac1{2m\sin(\pi l/m)}\int_{\mathbb R}\frac{e^{-2\pi lr/m}}{1+e^{-2\pi r}}e^{-t(1/4+r^2)}dr$ (elliptic terms);
- $H(t)=\displaystyle\sum_{[\gamma]\ \rm hyperbolic}\frac{\ell(\gamma_0)}{2\sinh(\ell(\gamma)/2)}\,\frac{e^{-t/4}\,e^{-\ell(\gamma)^2/4t}}{\sqrt{4\pi t}}$ (hyperbolic terms).

In $H$ the sum runs over the conjugacy classes of hyperbolic elements of $\Gamma$, i.e. over
the oriented closed geodesics with their iterates [DS p. 3]; $\gamma_0$ is the primitive
element with $\gamma=\gamma_0^k$. $I$ depends only on the area, and $E$ only on the multiset
of cone orders. Every term of $H$ is positive.

*Proof.* [DS, eq. (1)] is the Selberg trace formula for compact orientable orbisurfaces:
$\sum_nh(r_n)$ equals the identity, hyperbolic and elliptic terms, for "any entire function
of uniform exponential type" $h$ with $h(r)=h(-r)$, where $\lambda_n=\tfrac14+r_n^2$ and
$g$ is the Fourier transform of $h$. Each cone point of order $m$ gives the elliptic classes
$R_c^l$, $1\le l\le m-1$, with $\theta=\pi l/m$ [DS, p. 3: "We may identify the set of
primitive elliptic conjugacy classes R in Γ with the set of cone points in O of order
m(R)"]. This gives $E=\sum_iE_{m_i}$.

*Normalisation.* [DS] fixes $g$ by its wave example: for $h(r)=\cos(rt)$,
$g(u)=\tfrac12[\delta(u-t)+\delta(u+t)]$ (DS p. 4). That means
$g(u)=\frac1{2\pi}\int h(r)e^{-iru}dr$. For $h_t(r)=e^{-t(1/4+r^2)}$ this gives
$g_t(u)=e^{-t/4}e^{-u^2/4t}/\sqrt{4\pi t}$, verified symbolically in `check_locality.py`.
(Marklof's (192) prints the exponent as $-t^2/(2\beta)$. Its own prefactor $1/\sqrt{4\pi\beta}$
and the Gaussian integral require $-t^2/(4\beta)$, so the printed exponent is a misprint;
the script checks this too.)

The heat function is not of exponential type, so (1) must be extended to it. [Mar, Thm 4
and Prop. 10] does this for torsion-free $\Gamma$. The same approximation argument works
here:

**Lemma 3.2 (admissibility of the heat function).** Fix $\chi\in C_c^\infty(\mathbb R)$, even,
$0\le\chi\le1$, $\chi=1$ on $[-1,1]$, and put $g_R(u)=g_t(u)\chi(u/R)$ and
$h_R(r)=\int g_R(u)e^{iru}du$. Then $h_R$ is even, entire and of exponential type $\le2R$
(Paley–Wiener), so [DS] (1) holds for $h_R$, with Fourier transform $g_R$. As
$R\to\infty$ each term converges to the corresponding term for $h_t$:

- *Hyperbolic side.* $g_R(\ell)=g_t(\ell)$ once $R\ge\ell$, and $0\le g_R\le g_t$. The
  heat-function series converges by Lemma 3.3, so dominated convergence applies.
- *Identity and elliptic terms.* Put $f_R=g_t(1-\chi(\cdot/R))$, so $h_R-h_t=\hat f_R$. Then
  $\|f_R^{(k)}\|_{L^1}\to0$ for $k=0,\dots,3$: Gaussian tails beyond $|u|\ge R$, and
  derivatives of $\chi(u/R)$ are $O(R^{-k})$. Also
  $|\hat f_R(r)|\le\min(\|f_R\|_1,\ \|f_R'''\|_1|r|^{-3})$. Hence
  $\int|r\tanh(\pi r)||h_R-h_t|\,dr\le2\|f_R\|_1+2\|f_R'''\|_1\to0$. The elliptic kernels are
  in $L^1$ (they decay like $e^{-2\theta r}$ and $e^{-(2\pi-2\theta)|r|}$ with
  $0<\theta<\pi$), so those terms converge too.
- *Spectral side.* The finitely many $\lambda_j<\tfrac14$ have $r_j=is_j$ with
  $|s_j|\le\tfrac12$. For these, $|h_R(r_j)-h_t(r_j)|\le\int|f_R(u)|e^{|u|/2}du\to0$. For real
  $r_j$, $|h_R(r_j)-h_t(r_j)|\le\varepsilon_R\min(1,|r_j|^{-3})$ with
  $\varepsilon_R=\max(\|f_R\|_1,\|f'''_R\|_1)\to0$. Finally
  $\sum_j\min(1,|r_j|^{-3})<\infty$, because $\#\{\lambda_j\le\Lambda\}\le e\,Z(1/\Lambda)=O(\Lambda)$
  by Theorem 1 ($Z(s)\sim\operatorname{Area}/4\pi s$).

Hence (1) holds for $h_t$. That is Theorem 3.1. ∎

Independent numerical confirmation of the normalisation and of Theorem 3.1 as a whole: the
S3 FEM traces of O(2,8,8) and O(3,3,12) and the eight T4 members agree with
$I+E+H$ to their error budgets, with $H$ computed from enumerated closed geodesics and
nothing fitted (`numerics/moduli/REPORT.md` §4–5).

### 3.2 Counting closed geodesics

**Lemma 3.3 (counting).** Let $A=\operatorname{Area}(\mathcal O)$ and
$\delta=\operatorname{diam}(\mathcal O)$, and let $N(L)$ be the number of hyperbolic conjugacy
classes $[\gamma]$ with $\ell(\gamma)\le L$. Then
$$N(L)\le\frac{2\pi(\cosh(L+3\delta)-1)}{A}\le\frac{\pi}{A}e^{L+3\delta}.$$

*Proof.*

1. *A fundamental domain inside a ball.* Pick $x_0\in\mathbb H^2$ fixed by no nontrivial
   element of $\Gamma$. Such points exist: elliptic fixed points are discrete, and hyperbolic
   elements fix no point of $\mathbb H^2$. The Dirichlet domain
   $D=\{y:d(y,x_0)\le d(y,\gamma x_0)\ \forall\gamma\}$ is then a fundamental domain of area
   $A$. For $y\in D$, $d(x_0,y)=d_{\mathcal O}([x_0],[y])\le\delta$, so $D\subset\bar B(x_0,\delta)$.
2. *One representative per class, close to $x_0$.* Every hyperbolic class has a
   representative whose axis meets $D$: if $y\in\operatorname{axis}(\gamma)$ and $hy\in D$,
   then $hy\in\operatorname{axis}(h\gamma h^{-1})$. For such a representative, with $y$ on its
   axis in $D$,
   $d(x_0,\gamma x_0)\le d(x_0,y)+d(y,\gamma y)+d(\gamma y,\gamma x_0)\le\ell(\gamma)+2\delta$.
   Distinct classes have distinct representatives.
3. *Counting by area.* The translates $\gamma D$ with $d(x_0,\gamma x_0)\le R$ have disjoint
   interiors, have area $A$ each, and lie in $B(x_0,R+\delta)$, whose area is
   $2\pi(\cosh(R+\delta)-1)$.

Take $R=L+2\delta$. ∎

### 3.3 Quantitative locality

**Theorem 3.4.** Let $\mathcal O_1,\mathcal O_2$ be closed orientable hyperbolic 2-orbifolds
with the same signature. Write $A$ for their common area, $\ell_i$ for their systoles (the
length of the shortest closed geodesic), $\delta_i$ for their diameters,
$\ell=\min(\ell_1,\ell_2)$ and $\delta=\max(\delta_1,\delta_2)$.

**(a) Exact cancellation.** For every $t>0$,
$Z_1(t)-Z_2(t)=H_1(t)-H_2(t)$. Hence
$|Z_1(t)-Z_2(t)|\le\max(H_1(t),H_2(t))$.

**(b) Explicit bound.** For $0<t\le\ell^2/(2(1+\ell))$,
$$|Z_1(t)-Z_2(t)|\;\le\;\frac{\pi\,e^{3\delta}}{A\,(1-e^{-\ell})}\;\ell\,e^{\ell/2}\Big(1+\frac{2t}{\ell-t}\Big)\;\frac{e^{-\ell^2/4t}}{\sqrt{4\pi t}} .$$

**(c) Controlled bound from one reference time.** For any $t_1>0$ and $0<t\le t_1$,
$$|Z_1(t)-Z_2(t)|\le\sqrt{t_1/t}\;e^{(t_1-t)/4}\,e^{\ell^2/4t_1}\,\max_iH_i(t_1)\;e^{-\ell^2/4t}.$$
Here $H_i(t_1)=Z_i(t_1)-I(t_1)-E(t_1)$ is computable from the spectrum at the single time
$t_1$.

*Proof.* (a) $I$ and $E$ depend only on $(A,\{m_i\})$ (Theorem 3.1), and the signatures agree.
Since $H_i\ge0$, $|H_1-H_2|\le\max(H_1,H_2)$.

(b) Bound each $H_i$, using only $\ell(\gamma_0)\le\ell(\gamma)$, $e^{-t/4}\le1$ and, for
$L\ge\ell_i$, $2\sinh(L/2)\ge e^{L/2}(1-e^{-\ell_i})$:
$$H_i(t)\le\frac{1}{1-e^{-\ell_i}}\int_{[\ell_i,\infty)}\varphi\,dN_i,\qquad\varphi(L)=\frac{Le^{-L/2}e^{-L^2/4t}}{\sqrt{4\pi t}} .$$

1. *$\varphi$ is decreasing.* $(\log\varphi)'=1/L-1/2-L/2t\le0$ for $L\ge\ell_i$ as soon as
   $t\le\ell_i^2/2$, and $\ell^2/(2(1+\ell))\le\ell_i^2/2$.
2. *Use the counting bound.* Integrate by parts ($N_i(\ell_i^-)=0$, and
   $\varphi N_i\to0$ at infinity) and insert $N_i(L)\le(\pi/A)e^{L+3\delta_i}$ (Lemma 3.3):
   $$\int\varphi\,dN_i=-\int_{\ell_i}^\infty N_i\varphi'\le\frac{\pi e^{3\delta_i}}A\Big(e^{\ell_i}\varphi(\ell_i)+\int_{\ell_i}^\infty e^L\varphi\,dL\Big).$$
3. *Evaluate the integral.* Completing the square, $L/2-L^2/4t=-(L-t)^2/4t+t/4$. With
   $\operatorname{erfc}(x)\le e^{-x^2}/(x\sqrt\pi)$,
   $$\int_{\ell_i}^\infty e^L\varphi\,dL\le\frac{2t\ell_i}{\ell_i-t}\,\frac{e^{\ell_i/2}e^{-\ell_i^2/4t}}{\sqrt{4\pi t}} .$$
4. *Result for one orbifold.*
   $H_i(t)\le\frac{\pi e^{3\delta_i}}{A(1-e^{-\ell_i})}\,\ell_ie^{\ell_i/2}\big(1+\frac{2t}{\ell_i-t}\big)\frac{e^{-\ell_i^2/4t}}{\sqrt{4\pi t}}$.
5. *Replace $\ell_i$ by $\ell$.* For $t\le\ell^2/(2(1+\ell))$ each factor is non-increasing
   in $\ell_i\ge\ell$:
   - $x\mapsto xe^{x/2-x^2/4t}$ has logarithmic derivative $1/x+1/2-x/2t\le0$ once
     $x/2t\ge1/\ell+1$;
   - $1/(1-e^{-x})$ is decreasing;
   - $1+2t/(x-t)$ is decreasing.

   So each $H_i$ is bounded by the same expression with $\ell$ and $\delta$. Apply (a).
   `check_locality.py` verifies the algebraic steps symbolically, and spot-checks the
   final inequality against direct quadrature.

(c) For each class, $\ell(\gamma)\ge\ell_i\ge\ell$ and $t\le t_1$, so
$$\frac{g_t(\ell(\gamma))}{g_{t_1}(\ell(\gamma))}=\sqrt{t_1/t}\,e^{(t_1-t)/4}e^{-\ell(\gamma)^2(1/4t-1/4t_1)}\le\sqrt{t_1/t}\,e^{(t_1-t)/4}e^{\ell^2/4t_1}e^{-\ell^2/4t}.$$
Multiply by the class weight and sum. ∎

**The prefactor $t^{-1/2}$ cannot be dropped.** T3 as posed asks for
$|Z_1-Z_2|\le Ce^{-\ell^2/4t}$ with a constant $C$. In general that bound is **false**. By
Theorem 3.5, whenever the shortest geodesics differ, $|Z_1-Z_2|\,e^{\ell^2/4t}$ grows like
$t^{-1/2}$. The family of T4 is an example:
$\sqrt t\,e^{\ell^2/4t}|Z_1-Z_2|\to w/(2\sinh(\ell/2)\sqrt{4\pi})\ne0$.

What is true:

- the bound with $t^{-1/2}$ (Theorem 3.4);
- equivalently, for every $\varepsilon\in(0,\ell)$, $|Z_1-Z_2|\le C_\varepsilon e^{-(\ell-\varepsilon)^2/4t}$
  for $t\le t_0$.

The $t^{-1/2}$ is the one-dimensional heat kernel along the closed geodesic: heat must
travel the length $\ell$ in one dimension, and the transverse direction is already
accounted for by the $1/(2\sinh(\ell/2))$ focusing factor.

### 3.4 Sharpness: the difference is really there

Weight each length by its classes: $w_{\mathcal O}(L)=\sum_{[\gamma]:\,\ell(\gamma)=L}\ell(\gamma_0)$.
This is a finitely supported function on every bounded interval (Lemma 3.3).

**Theorem 3.5.** Let $\mathcal O_1,\mathcal O_2$ have the same signature.

- If $w_1\equiv w_2$, then $Z_1\equiv Z_2$, and the orbifolds are isospectral.
- Otherwise, let $L_*=\min\{L:w_1(L)\ne w_2(L)\}$. Then, as $t\downarrow0$,
$$Z_1(t)-Z_2(t)=\frac{w_1(L_*)-w_2(L_*)}{2\sinh(L_*/2)}\,\frac{e^{-t/4}e^{-L_*^2/4t}}{\sqrt{4\pi t}}\,\big(1+o(1)\big),$$
  so $Z_1-Z_2\ne0$ for small $t$ and $\log|Z_1-Z_2|=-L_*^2/4t-\tfrac12\log t+O(1)$.
- In particular, if $\ell_1\ne\ell_2$, then $L_*=\min(\ell_1,\ell_2)=\ell$, and the
  exponent $\ell^2/4$ of Theorem 3.4 is attained.

*Proof.* Group $H_1-H_2$ by length. Let $L'>L_*$ be the next length in
$\operatorname{supp}w_1\cup\operatorname{supp}w_2$. The terms with $L\ge L'$ are bounded in
absolute value by $H_1^{\ge L'}+H_2^{\ge L'}$. Each of these is $O(t^{-1/2}e^{-L'^2/4t})$, by
the argument of Theorem 3.4(b) with $\ell_i$ replaced by $L'$; Lemma 3.3 bounds the count of
those classes too. Divided by the $L_*$ term, this is $O(e^{-(L'^2-L_*^2)/4t})\to0$. If
$w_1\equiv w_2$, then $H_1\equiv H_2$, so $Z_1\equiv Z_2$; a heat trace determines the
spectrum (uniqueness of the Laplace transform). ∎

**Generic deformations move the length spectrum.** By [DS, Thm 1.1] the Laplace spectrum
determines the length spectrum. In the converse direction, "Knowledge of the length
spectrum and the number of cone points of each order determines the Laplace spectrum." So,
within a signature, $Z_1\equiv Z_2$ $\iff$ isospectral $\iff$ $w_1\equiv w_2$.

Take a length coordinate $\ell_c$ of Thurston's parametrisation (Proposition 2.2), and move
along it with the other coordinates fixed. A point $Y$ of this line is isospectral to a
given $\mathcal O$ only if $\ell_c(Y)$ lies in the countable length set of $\mathcal O$. So
along any such line, all but countably many points have $Z_Y-Z_{\mathcal O}\ne0$, with the
sharp asymptotics of Theorem 3.5.

In the T4 family this is visible directly. The systole is $4b(\tau)$, strictly decreasing
in $\tau$, so every pair of members has $\ell_1\ne\ell_2$, and Theorem 3.5 applies with
$L_*=\ell$ (numerics/moduli/REPORT.md).

### 3.5 Blind expansion, not blind spectrum

Isospectral non-isometric orbifolds of the same signature exist. Two fetched sources show
this:

- **[LV, Theorem A]**, verbatim: *"The minimal area of an isospectral-nonisometric pair of
  2-orbifolds associated to maximal arithmetic Fuchsian groups is 23π/6, and this bound is
  achieved by exactly three pairs, up to isomorphism."* The next sentence: *"they all have
  signature (0; 2, 2, 2, 2, 2, 3, 4)"*. LV also record (p. 1) that Vignéras' construction
  gives isospectral non-isometric hyperbolic surfaces, and that the 1994 claimed (0;2,2,3,3)
  pair of Maclachlan–Rosenberger was shown not to be isospectral.
- **[DR, Theorem 1]**: the Laplace spectrum of a compact hyperbolic 2-orbifold determines,
  and is determined by, the volume, the mirror length, the cone points of each order, and
  the primitive closed geodesics of each length and orientability class.

So the full spectrum does not always determine the isometry class, even within a signature.
That is a different phenomenon from Theorem 1, and the two must be kept apart.

- **The expansion is blind.** The small-$t$ expansion sees only $I+E$, which is the same for
  the whole Teichmüller space of the signature. That space has dimension $6g-6+2n$ (T2).
- **The function is not blind.** $Z(t)$ as a function of $t>0$ determines the whole
  spectrum, and with it the length spectrum [DS, DR]. Through $H$ it separates all but
  countably many points along every length-coordinate line (§3.4).
- **What the function still misses** is exactly the set of isospectral non-isometric
  pairs: the [LV] pairs, and any others of the Vignéras or Sunada type.

So "heat cannot hear the moduli" is a statement about the asymptotic series, which carries
no information about them. It is not a statement about the spectrum, which carries almost
all of it. The information is present in $Z(t)$ but sits beyond all orders, in
$e^{-\ell^2/4t}$.
