# G5 audit: statements under review

Every result below is copied verbatim, by line range, from its source file on branch
`s9a-audit` (`build_statements.py` asserts the anchors and that no proof text is included).
Hypotheses and notation are the `.0` items of each group. Proofs are deliberately omitted.
Cross-references inside the statements (e.g. "Theorem A", `lem:chamber`) point to other
items in this file.

External inputs the results rely on (texts fetched headlessly by `fetch_sources.sh` into
`review/audit/sources/`, not committed):

| input | used by | fetched text |
|---|---|---|
| Uçar, PhD thesis, arXiv:1711.03405: (4.25), (4.33), (4.35), Thm 4.11, Thm 4.20, Cor 4.21, Cor 4.23 | every heat-coefficient statement | `ucar_1711.03405.txt` |
| Dryden–Gordon–Greenwald–Webb, arXiv:0805.3148: Def 4.7, Thm 4.8, §5.6, Thm 5.15, Prop 5.22 | locality, curvature, priority | `dggw_0805.3148.txt` |
| Dryden–Strohmaier, arXiv:math/0504571: trace formula eq. (1), Thm 1.1, Thm 3.2, Prop 3.3 | locality T3, divergence | `ds_math0504571.txt` |
| Thurston, ch. 13: 13.3.5, 13.3.6, Cor 13.3.7 | locality T2, curvature | `thurston_ch13.txt` |
| Ostrowski, Acta Math. 72 (1940), Théorème XXX | stability | `ostrowski_1940.txt` |
| Holtz–Tyaglov, arXiv:0912.4703 (Orlando's formula) | audibility, stability | `holtz_tyaglov_0912.4703.txt` |
| Marklof, arXiv:math/0407288 | locality (normalisation cross-check) | `marklof_math0407288.txt` |
| Schueth, arXiv:1812.06119 | cone coefficients l<=2 | `schueth_1812.06119.txt` |
| Kokotov, arXiv:0906.0717 | curvature (flat cones) | `kokotov_0906.0717.txt` |
| Linowitz–Voight arXiv:1408.2001; Doyle–Rossetti arXiv:1103.4372 | locality §3.5 | `lv_1408.2001.txt`, `dr_1103.4372.txt` |
| Bremner–Guy–Nowakowski, Math. Comp. 61 (1993); Schinzel, Serdica 22 (1996); PARI/GP manual (ellrank) | diophantine | `bgn_mcom1993.txt`, `schinzel_serdica1996.txt`, `pari_elliptic.html` |
| Müller–Feliu–Regensburger–Conradi–Shiu–Dickenstein, arXiv:1311.5493 | Theorem A prior art (P7) | `mueller_1311.5493.txt` |
| Donnelly 1976 | restated in DGGW §4 only | standing gap (not fetched) |

## Group: curvature

### CU.0. Conventions

Source: `theory/curvature/proof.md` lines 37-54 (verbatim).

````
## 1. Conventions

All orbifolds are closed and orientable, with cone points as the only singularities (no
mirrors). Such an orbifold of genus $g$ with orders $m_1,\dots,m_n\ge2$ has
$\chi=2-2g-\sum_i(1-1/m_i)$, and a constant-curvature metric of sign $\operatorname{sgn}\chi$
exists iff it is good (Thurston, Thm 13.3.6).

Heat coefficients are counted as in Theorem A: the first $k$ coefficients are those of
$t^{-1},t^0,\dots,t^{k-2}$. For a class $\mathcal C$, $K_{\rm mult}(\mathcal C)$ is the least $k$
such that, for every metric of the allowed kind, the first $k$ coefficients determine the
cone-order multiset on $\mathcal C$. When the curvature is normalised to $K=\pm1$ the area is
fixed by $\chi$. For $K=0$ the area is a free parameter.

- Parts 1, 2 and 4 below hold whether or not $K$ is normalised, because the coefficient that
  does the work, $t^0$, is scale-invariant.
- Part 3 is stated for $K=-1$, as in Theorem A. With $K$ free and only the area common, the
  triangular structure of Theorem A is not available, and no claim is made.

````

### CU.1. Flat-cone input (Kokotov) as quoted

Source: `theory/curvature/proof.md` lines 57-76 (verbatim).

````
**Flat cones and flat orbifolds.**

- Kokotov's Proposition 1 gives the exact local statement on an infinite flat cone of angle
  $\beta$: area term plus $\frac1{12}(\frac{2\pi}\beta-\frac\beta{2\pi})$, plus
  $O(e^{-\epsilon/t})$, with nothing at any other order.
- His Theorem 1 globalises this to every compact flat surface with conical points:
  $$\operatorname{Tr}e^{-t\Delta}=\frac{\operatorname{Area}}{4\pi t}+\frac1{12}\sum_k
  \Big(\frac{2\pi}{\beta_k}-\frac{\beta_k}{2\pi}\Big)+O(e^{-\epsilon/t}).\tag{F}$$
- A flat orientable orbifold is such a surface with $\beta_k=2\pi/m_k$. Its Laplacian is
  Kokotov's Friedrichs extension: for $\beta\le2\pi$ only the bounded mode enters his
  deficiency space (p. 9), and the Friedrichs domain consists of the functions bounded at the
  vertex, which is the orbifold domain. So its expansion is
  $\frac{A}{4\pi t}+\sum_i\frac{m_i^2-1}{12m_i}$. The same follows from DGGW Thm 4.8, whose
  coefficients are integrals of curvature polynomials, plus $b_\ell=K^\ell\cdot(\cdots)$.
- Every coefficient of $t^\ell$, $\ell\ge1$, vanishes identically. At $K=0$ Uçar's coefficients
  vanish for every $\ell\ge1$ and every $m$, trivially, because of the factor $K^\ell$. F3 is a
  bookkeeping check of this. At $K\neq0$ none
  vanishes for $m\ge2$; positivity for all $\ell$ is proved in `theory/divergence/proof.md`,
  Lemma 1.

````

### CU.2. Lemma 2 (invariant multiplicities)

Source: `theory/curvature/proof.md` lines 92-95 (verbatim).

````
**Lemma 2 (invariant multiplicities).** Let $G\subset SO(3)$ be finite, with $S^2/G$ having cone
orders $m_1,\dots,m_k$. The multiplicity of the eigenvalue $\ell(\ell+1)$ on $S^2/G$ is
$$N_\ell=\frac{2\ell+1}{|G|}+\frac12\sum_{i=1}^k\Big[2\Big\lfloor\frac\ell{m_i}\Big\rfloor+1-\frac{2\ell+1}{m_i}\Big].$$

````

### CU.3. Proposition (curvature comparison) and its strength claims

Source: `theory/curvature/proof.md` lines 121-168 (verbatim).

````
**Proposition (curvature comparison).**

1. **$K=0$.** The closed orientable flat 2-orbifolds are $T^2$, $S^2(2,2,2,2)$, $S^2(3,3,3)$,
   $S^2(2,4,4)$ and $S^2(2,3,6)$.
   - For every flat metric, the heat expansion is $\frac A{4\pi t}+c_0+O(e^{-\epsilon/t})$, with
     $c_0=0,\frac12,\frac23,\frac34,\frac56$ respectively.
   - The constant term alone determines the orbifold. $K_{\rm mult}=2$, and this is sharp,
     since the area term carries no cone information.
   - All coefficients of $t^\ell$, $\ell\ge1$, vanish identically.
2. **$K=+1$.** The good closed orientable spherical 2-orbifolds are $S^2$, $S^2(n,n)$ and
   $S^2(2,2,n)$ ($n\ge2$), and $S^2(2,3,3)$, $S^2(2,3,4)$, $S^2(2,3,5)$. The bad orbifolds
   $S^2(n)$ and $S^2(n_1,n_2)$ with $n_1<n_2$ are excluded, since they carry no
   constant-curvature metric.
   - On this class the constant term
     $a_0=\frac\chi6+\sum_i\frac{m_i^2-1}{12m_i}$ alone determines the orbifold, so
     $K_{\rm mult}=2$.
   - The $t^{-1}$ coefficient alone does not, even with $K=1$ fixed:
     $\chi(S^2(2,2,n))=\chi(S^2(2n,2n))=1/n$ for every $n$.
   - The higher coefficients are nonzero (the amplifier is on) but are never needed.
3. **$K=-1$, genus 0, $n$ cone points.** $K_{\rm mult}\le n$ for every $n\ge3$ (Theorem A).
   Equality holds for $n=3,4$ by explicit integer witnesses. Over real orders, $n-1$
   coefficients never suffice (Theorem C(2)). Integer sharpness for $n\ge5$ is open.
4. **Flat cone surfaces that are not orbifolds.** On closed flat surfaces with conical points,
   the heat coefficients are exactly the area and $\sum_k(\frac{2\pi}{\beta_k}-\frac{\beta_k}
   {2\pi})$. Hence:
   - Among doubled Euclidean triangles (flat cone spheres with three cone points), every
     surface other than the doubled equilateral triangle shares all heat coefficients with a
     one-parameter family of pairwise non-isometric ones.
   - The heat coefficients do not detect whether a flat cone sphere is an orbifold. The doubled
     triangles with angles $\pi(\frac14,\frac14,\frac12)$ (the orbifold $S^2(2,4,4)$) and
     $\pi(\frac15,\frac25,\frac25)$ (cone angles $\frac{2\pi}5,\frac{4\pi}5,\frac{4\pi}5$, not
     an orbifold) have the same area and every heat coefficient in common.

**Strength.** Parts 1 and 2 are the good-orbifold restriction of DGGW Theorem 5.15, split by
the sign of $K$. That theorem is strictly stronger: its invariant $c$ ($12\times$ the $t^0$
coefficient) separates all closed orientable 2-orbifolds with $\chi\ge0$ at once, bad ones and
smooth surfaces included.

- $K_{\rm mult}\le2$ is therefore DGGW's result, and the sharpness ($\ne1$) is elementary.
- Part 2 is also covered by DGGW Proposition 5.22 (spherical, non-orientable included) and by
  Uçar Cor. 4.21(iv) (any $\kappa\ne0$).
- What is added here:
  - an independent derivation of the spherical expansion from the spectrum (Lemma 2, S2);
  - placing the three geometries side by side in one count;
  - Part 4.

Part 3 is Theorem A of `theory/audibility/proof.md`. Part 4 rests on Kokotov's Theorem 1 and
is elementary given it.
````


## Group: divergence

### DV.0. Notation

Source: `theory/divergence/proof.md` lines 32-44 (verbatim).

````
## 1. Notation

$$A_\ell(m)=\frac{(2\ell)!}{\ell!\;m\sin(\pi/m)}\Big(\frac m{2\pi}\Big)^{2\ell+1},\qquad
\sigma_m=\frac{\pi/m}{\sin(\pi/m)} .$$

By Stirling, $A_\ell(m)=\ell!\,(m^2/\pi^2)^\ell\cdot\frac{1}{2\pi\sin(\pi/m)\sqrt{\pi\ell}}
(1+O(1/\ell))$.

Uçar's coefficients are $b_\ell(m)=K^\ell\beta_\ell(m)$, with
$\beta_\ell(m)=\sum_{i=0}^\ell\frac2{4^ii!}c_{\ell-i}(\pi/m)$ and $c_\ell$ given by (4.25). In
the manuscript's notation $p_\ell(m)=m\,\beta_\ell(m)$. $\beta_\ell$ does not depend on $K$, so
any statement about $\beta_\ell$ holds for $K=+1$ and $K=-1$ alike.

````

### DV.1. Lemma 1

Source: `theory/divergence/proof.md` lines 47-59 (verbatim).

````
**Lemma 1.** Let
$$G_k(t)=\frac{t/2}{\sinh(t/2)}\Big[\frac{kt}2\coth\frac{kt}2-\frac t2\coth\frac t2\Big]
=\sum_Ng_N(k)t^N .$$
Then:

- (a) $c_\ell(\pi/k)=\dfrac{(-1)^\ell(2\ell+2)!}{4k(\ell+1)!(2\ell+1)}\,g_{2\ell+2}(k)$.
- (b) $(-1)^\ell g_{2\ell+2}(k)>0$ for all $\ell\ge0$ and $k\ge2$. Hence $c_\ell(\pi/k)>0$ and
  $\beta_\ell(k)>0$ for every $\ell$.
- (c) For fixed $k\ge2$ and every $\rho<1$,
  $g_{2\ell+2}(k)=2(-1)^\ell\sigma_k(k/2\pi)^{2\ell+2}(1+O((2\rho)^{-2\ell}))$. For $k\ge3$ the
  relative error is in fact $\Theta(4^{-\ell})$. For $k=2$ it is $O(9^{-\ell})$, since
  $G_2(t)=(t/2)^2\operatorname{sech}(t/2)$ has its next poles at $\pm3\pi i$.

````

### DV.2. Theorem 2

Source: `theory/divergence/proof.md` lines 101-108 (verbatim).

````
**Theorem 2.** For fixed $m\ge2$, as $\ell\to\infty$,
$$\frac{b_\ell(m)}{K^\ell}=A_\ell(m)\Big(1+\frac{\pi^2}{2m^2(2\ell-1)}+O(\ell^{-2})\Big).$$
Equivalently, with $\lambda_\ell=|B_{2\ell+2}|/(2(\ell+1)!(2\ell+1))$, the leading coefficient
of $p_\ell$,
$$\frac{p_\ell(m)}{\lambda_\ell\,m^{2\ell+2}}\longrightarrow\sigma_m=\frac{\pi/m}{\sin(\pi/m)} .$$
So the full polynomial exceeds its leading term by the factor $\sigma_m$, which lies in
$(1,\pi/2]$.

````

### DV.3. Theorem 3

Source: `theory/divergence/proof.md` lines 155-177 (verbatim).

````
**Theorem 3.** Let $K\in\{-1,+1\}$, $C\ge0$, and let $m_1,\dots,m_n$ ($n\ge1$) be integers
$\ge2$ with largest value $M$ of multiplicity $\mu$. Let
$$a_\ell=C\,s_{\ell+1}K^{\ell+1}+K^\ell\sum_i\beta_\ell(m_i).$$
This covers the heat coefficients ($t^\ell$, $\ell\ge0$) of every closed orientable 2-orbifold of
constant curvature $K$ with cone points $m_i$, of any genus, with $C=|\chi|/2$. It also covers
the partial sequences left after peeling. Then
$$\frac{a_\ell}{K^\ell}=\mu\,A_\ell(M)\Big(1+O(1/\ell)+O\Big(\sum_{m_i<M}(m_i/M)^{2\ell}\Big)
+O(C\,\ell\,M^{-2\ell})\Big).$$
Consequently
$$\lim_{\ell\to\infty}\frac{2\pi^2\,|a_\ell|}{(2\ell-1)\,|a_{\ell-1}|}=M^2,\qquad
\lim_{\ell\to\infty}\frac{|a_\ell|}{\ell\,|a_{\ell-1}|}=\frac{M^2}{\pi^2},\qquad
\mu=\lim_{\ell\to\infty}\frac{a_\ell}{K^\ell A_\ell(M)} .$$
If $n=0$ (and $C>0$), the first two limits are $1$ and $1/\pi^2$. There the convergence is only
$O(1/\ell)$, because $s_{\ell+1}$ carries an extra factor $\ell$.

The error terms are not uniform over orbifolds. Many copies of a slightly smaller order, or a
huge $|\chi|$, delay the asymptotic regime. Independent tests:

- $1000\times49$ together with one cone of order 50: the estimator still rounds to 49 at
  $\ell=150$.
- Genus $10^4$ with one cone of order 2: the smooth part dominates, with the opposite sign, for
  $\ell\le5$.

````

### DV.4. Corollary 4

Source: `theory/divergence/proof.md` lines 199-203 (verbatim).

````
**Corollary 4 (peeling).** For every $L$, the tail $(a_\ell)_{\ell\ge L}$ and $K$ determine the
cone-order multiset, $\chi$, the area and the genus. The inputs assumed known are $K$, Uçar's
(4.25)/(4.33) and $s_k>0$. This tail-only form is a small strengthening of Uçar's
Cor. 4.21(iv), whose extraction starts at $\nu=0$ and uses the area.

````

### DV.5. Borel reading (claim)

Source: `theory/divergence/proof.md` lines 233-246 (verbatim).

````
**Borel reading (stated, not proved beyond the radius).** By Theorem 3 the Borel transform
$\sum a_\ell\zeta^\ell/\ell!$ has radius of convergence exactly $\pi^2/M^2$. All
$a_\ell/K^\ell>0$ for large $\ell$. By Pringsheim's theorem (applied in the variable $K\zeta$,
after removing finitely many terms), the point $\zeta=K\pi^2/M^2$ on the circle of convergence is
a singularity:

- on the negative axis for hyperbolic orbifolds;
- on the positive axis for spherical ones.

The smooth heat kernel of $\mathbb H^2$ or $S^2$ has its nearest Borel singularity at distance
$\pi^2$ (Dunne, arXiv:2109.03897; Li–Li–Tang, arXiv:2606.21909). A cone of order $M$ pulls it in
by the factor $M^2$. Nothing is claimed here about the analytic continuation or about Borel
summability.

````
