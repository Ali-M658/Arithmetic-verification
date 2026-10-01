# Curvature as the amplifier: flat, spherical and hyperbolic cone data compared

Sources and page references are in `sources.md`. Exact checks are in `curvature_checks.py`,
with output in `curvature_output.txt`.

## 0. Physical reading, and what it does not say

A cone point of order $m$ contributes to the heat trace at order $t^\ell$ the amount
$b_\ell(m)=K^\ell\,\tfrac1m\,p_\ell(m)$ (Uçar (4.25), (4.33)). Here $p_\ell$ is an even
polynomial of degree $2\ell+2$ with $p_\ell(1)=0$.

The curvature $K$ works as a gain. At $K=0$ every term with $\ell\ge1$ is switched off, and the
heat trace hears one number per cone surface, $\sum_i(m_i-1/m_i)$. At $K\neq0$ each further order
adds one new odd power sum $\sum_im_i^{2\ell+1}$. Theorem A is the statement that the first $n$
coefficients are enough for $n$ cones. Of these, $t^{-1}$ (area, by Gauss–Bonnet) and $t^0$
exist at $K=0$ too; the remaining $n-2$, at $t^1,\dots,t^{n-2}$, are the amplified ones.

The zero-versus-nonzero curvature contrast is Uçar's for polygons:

- at $\kappa=0$ a polygon has "at most three nonvanishing heat invariants" (printed p. 97);
- "the heat invariants do not provide much information" there (printed p. 99);
- his Theorem 3.40 and Corollary 4.21 exploit $\kappa\ne0$.

It does **not** follow that curvature is *required* for audibility of orbifold cone data. In
non-negative curvature, Gauss–Bonnet leaves only a finite list and a few one-integer families,
and one number happens to separate them. That is a counting accident of the class, not a
mechanism, and it is already in the literature (DGGW Thm 5.15).

Capping the number of cones is not by itself enough. Hyperbolic triads also have $n=3$, yet
$\{2,8,8\}$ and $\{3,3,12\}$ share $t^{-1}$ and $t^0$. The amplifier is used where one number
does not separate:

- for hyperbolic orbifolds, which have an unbounded number of cone points;
- for flat cone surfaces with arbitrary angles, where the single available number provably
  fails.

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

## 2. The heat-trace structure in each geometry

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

**Spherical orbifolds.**

- For $\mathcal O=S^2/G$ with $G\subset SO(3)$ finite, the trace is a sum over $G$. Grouping the
  nontrivial rotations by their fixed poles gives the exact multiplicity formula (Lemma 2 below).
- That formula splits the trace into a smooth part $\frac\chi2Z_{S^2}(t)$ plus one *local*
  series $B_m(t)$ per cone point.
- The small-time expansion of $B_m$ follows exactly from Hurwitz zeta values at negative
  integers. Its $t^\ell$ coefficient equals Uçar's $b_\ell(m)$ at $K=+1$. This is checked
  exactly for $\ell\le12$ and $2\le m\le30$ (S2), and is an independent confirmation of the
  $K^\ell$ structure from the spectrum itself.

**Hyperbolic orbifolds.** The expansion has every integer order. The cone part at order
$\ell$ is $(-1)^\ell\sum_i\frac1{m_i}p_\ell(m_i)$, and the smooth part is a multiple of the area
(manuscript Section `sec:heatexp`).

**Lemma 2 (invariant multiplicities).** Let $G\subset SO(3)$ be finite, with $S^2/G$ having cone
orders $m_1,\dots,m_k$. The multiplicity of the eigenvalue $\ell(\ell+1)$ on $S^2/G$ is
$$N_\ell=\frac{2\ell+1}{|G|}+\frac12\sum_{i=1}^k\Big[2\Big\lfloor\frac\ell{m_i}\Big\rfloor+1-\frac{2\ell+1}{m_i}\Big].$$

*Proof.*

1. $N_\ell=\frac1{|G|}\sum_{g\in G}\chi_\ell(g)$, where $\chi_\ell(\theta)=\sum_{s=-\ell}^\ell
   e^{is\theta}$ is the character of the degree-$\ell$ harmonics.
2. Each $g\ne1$ fixes exactly two antipodal poles. Pole stabilisers are cyclic, so the sum over
   $g\ne1$ equals $\frac12\sum_x\sum_{g\in G_x\setminus1}\chi_\ell(g)$, with $x$ running over
   all poles.
3. For a cyclic stabiliser of order $m$, $\sum_{j=0}^{m-1}\chi_\ell(2\pi j/m)$ counts the
   $s\in[-\ell,\ell]$ with $m\mid s$, times $m$. So
   $\sum_{j=1}^{m-1}\chi_\ell(2\pi j/m)=m(2\lfloor\ell/m\rfloor+1)-(2\ell+1)$.
4. The poles over the cone point of order $m_i$ form one orbit of size $|G|/m_i$. Summing gives
   the formula.

$\square$

The formula was checked against explicit character sums over generated matrix groups
$C_5,D_2,D_6,T,O,I$, for $\ell\le61$ (S1).

The summand $f_m(\ell)=2\lfloor\ell/m\rfloor+1-(2\ell+1)/m=(m-1-2r)/m$, with $r=\ell\bmod m$, is
$m$-periodic with mean zero. So
$B_m(t)=\frac12\sum_\ell f_m(\ell)e^{-\ell(\ell+1)t}$ has a pure power-series expansion, with no
$t^{-1/2}$ term.

## 3. The proposition

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

## 4. Proofs

**Part 1.**

*Classification.* Orientable genus $g\ge1$ gives $\chi\le0$, with equality only for $T^2$ and no
cone points. For $g=0$, $\chi=0$ means $\sum_i(1-1/m_i)=2$. Each term is $\ge\frac12$, so
$n\le4$; $n=4$ forces all $m_i=2$; and $n\le2$ gives a sum $<2$. For $n=3$,
$\frac1a+\frac1b+\frac1c=1$ with $a\le b\le c$ forces $a\le3$:

- $a=2$: $\frac1b+\frac1c=\frac12$, which gives $(4,4)$ or $(3,6)$.
- $a=3$: $b=c=3$.

This agrees with Thurston's table and was enumerated exactly (F1). All of these are good,
being quotients of $\mathbb E^2$.

*Expansion.* By (F) with $\beta_i=2\pi/m_i$. The constants are $\sum_i\frac{m_i^2-1}{12m_i}$
(F2), and they agree with DGGW Table 1.

*Determination.* The five values are distinct. The area term is the same for any two flat
metrics of equal area, whatever the orbifold, so one coefficient never suffices.

$\square$

**Part 2.**

*Classification.* Thurston's table for $X_{\mathcal O}=S^2$. Orientable $g\ge1$ has $\chi\le0$.
The constant term is DGGW (5.7), $a_0=\frac\chi6+\sum_i\frac{m_i^2-1}{12m_i}$. It was confirmed
here from the exact spectrum (Lemma 2 and S2), and it agrees with DGGW Table 1 for
$(2,3,3)$, $(2,3,4)$, $(2,3,5)$.

Multiply by 12:

| orbifold | $12a_0$ |
|---|---|
| $S^2$ | $4$ |
| $S^2(n,n)$ | $2n+\frac2n$ |
| $S^2(2,2,n)$ | $3+n+\frac1n$ |
| $S^2(2,3,3)$ | $7+\frac16$ |
| $S^2(2,3,4)$ | $8+\frac1{12}$ |
| $S^2(2,3,5)$ | $9+\frac1{30}$ |

*Each family is internally injective.* $x+\frac1x$ is increasing on $x\ge1$.

*The families against each other.* Write each value as integer part plus fractional part.

- For $n\ge3$, $2n+\frac2n$ has fractional part $\frac2n$ and integer part $2n$.
- For $n=2$ it is the integer 5.
- $3+n+\frac1n$ has fractional part $\frac1n$ ($n\ge2$) and integer part $n+3$.

Equality between the two families would need either

- $\frac2n=\frac1{n'}$ and $2n=n'+3$, i.e. $n=2n'$ and $3n'=3$, so $n'=1$, which is excluded; or
- $5=3+n'+\frac1{n'}$, which needs $n'+\frac1{n'}=2$, i.e. $n'=1$, which is excluded.

*The exceptional values.*

- $4$ and $7\frac16,8\frac1{12},9\frac1{30}$ have fractional parts $0,\frac16,\frac1{12},\frac1{30}$.
- They would match $S^2(n,n)$ only at $n=12,24,60$, with integer parts $24,48,120$, or at $2n+\frac2n=4$, i.e. $n=1$.
- They would match $S^2(2,2,n)$ only at $n=6,12,30$, with integer parts $9,15,33$.

None of these agrees. So $a_0$ is injective on the class. This was checked by enumeration for
$n\le20000$ (S3).

*Sharpness.* With $K=1$, the $t^{-1}$ coefficient is $\frac{A}{4\pi}=\frac\chi2$, and
$\chi(2,2,n)=\chi(2n,2n)=\frac1n$, while the two $a_0$ differ (S3). With $K$ unnormalised the
$t^{-1}$ coefficient is the area alone and carries no information. Either way one coefficient is
insufficient.

$\square$

**Part 3.** Theorem A and Theorem C of `theory/audibility/proof.md`, together with the
witnesses $\{2,8,8\},\{3,3,12\}$ ($n=3$) and $\{3,10,15,30\},\{4,5,21,28\}$ ($n=4$) recorded
there. $\square$

**Part 4.** The expansion is (F).

*Non-determination.* The double of a Euclidean triangle with angles $\alpha_i$,
$\sum\alpha_i=\pi$, is a flat cone sphere with cone angles $\beta_i=2\alpha_i$. Write $\alpha_i=\pi x_i$. Then
$\frac1{12}\sum(\frac{2\pi}{\beta_i}-\frac{\beta_i}{2\pi})=\frac1{12}(\sum_i\frac1{x_i}-1)$. So
the heat coefficients are the area and $\sum1/x_i$: two numbers on a three-parameter space,
two shape parameters plus scale. Fix the area.

- On the open simplex $\sum1/x_i\ge9$, with equality only at the centre (AM–HM). The centre is
  the only critical point of $\sum1/x_i$ restricted to the simplex: Lagrange gives
  $x_i^{-2}$ constant. So for every $h>9$ the level set
  $\{\sum x_i=1,\ \sum1/x_i=h\}$ is a smooth closed curve, and for $h=9$ it is the single
  equilateral point.
- Its points are non-congruent triangles away from the permutations.
- For $h=10$ it contains interior points for 299 of the sampled $x=k/1000$ (F4).

*The explicit pair.*

- $(\frac14,\frac14,\frac12)$: $\sum1/x_i=4+4+2=10$.
- $(\frac15,\frac25,\frac25)$: $\sum1/x_i=5+\frac52+\frac52=10$.

Both constant terms equal $\frac34$, the value of $S^2(2,4,4)$, and the cone angle $\frac{4\pi}5$
is not of the form $\frac{2\pi}m$ (F4). Scaled to equal area, the two surfaces share every heat
coefficient by (F). They are not isometric, since their cone angles differ. $\square$

## 5. The physical reading, stated honestly

| geometry | class | orders heard by the heat coefficients | $K_{\rm mult}$ | reason |
|---|---|---|---|---|
| flat orbifolds | 5 orbifolds | $\sum(m_i-1/m_i)$ only | 2 | finite class, distinct values |
| flat cone spheres | continuum | $\sum(2\pi/\beta-\beta/2\pi)$ only | none | one number, two or more shape parameters |
| spherical | infinite families, $n\le3$ | all odd power sums (unused) | 2 | Gauss–Bonnet caps $n$; one number separates |
| hyperbolic, genus 0 | $n$ unbounded | all odd power sums | $\le n$; $=n$ for $n=3,4$; $\ge4$ for $n\ge4$ | Theorem A: first $n$ coefficients, $n-2$ of them amplified |

- In **non-negative curvature** the cone data of an orbifold are heard for a trivial reason.
  $\chi\ge0$ leaves a finite list (flat) or a finite list plus two one-integer families
  (spherical), and the single constant term separates them. The spherical case needs a short
  fractional-part argument. A cap on the number of cones alone would not suffice: hyperbolic
  triads also have $n=3$.
  So the statement "curvature is required to hear the cone orders" is **false** for orbifolds.
  The flat orbifolds are heard with the amplifier fully off.
- What **is** true is the mechanism statement. At $K=0$ the heat trace hears exactly one
  symmetric function of the cone angles, whatever the surface. That number fails as soon as the
  class has more cone freedom than Gauss–Bonnet removes, as Part 4 shows with explicit flat
  examples. For orbifolds with $K\ne0$, Uçar's Corollary 4.21(iv) states that $\kappa$ and the
  spectrum determine the cone multiset in full generality. His proof extracts the orders from the
  coefficients of $\kappa^\nu$ by a $\nu\to\infty$ limit and uses only heat invariants
  (printed p. 140). Theorem A is the finite, quantitative version for genus 0: the first $n$
  coefficients for $n$ cones, with the obstruction $\prod(m_i+m_j)$ never vanishing.
- So the comparison is this. **For orbifolds in non-negative curvature, two coefficients always
  suffice. In negative curvature, the first $n$ coefficients suffice for $n$ cones and all but
  two of them exist only because $K\ne0$.**
  - Whether the integer $K_{\rm mult}$ actually grows with $n$ is open. It is $n$ for $n=3,4$,
    non-decreasing in $n$ (pad a witness with common cones), hence $\ge4$ for $n\ge4$.
  - Over real orders $n-1$ never suffice (Theorem C(2)).
  - No integer witness exists for $n=5$ with orders $\le120$ (`theory/audibility`).

  For flat cone surfaces that are not orbifolds, two coefficients do not suffice at all
  (Part 4).

## 6. Scope

- Only orientable orbifolds without mirrors are treated. The 17 flat orbifolds include
  non-orientable ones and ones with mirrors. There the heat coefficients do not determine the
  orbifold:
  - DGGW Remark 5.23 gives $O(2,*2,2)$ against $O(2,2*)$.
  - DGGW Table 1 lists the torus and the Klein bottle with the same expansion
    $V\frac1t+O(t)$. All their higher coefficients vanish too, by flatness (local curvature
    invariants), so their full expansions agree at equal area.

  This is cited, not reproved here.
- Part 2 is proved for the good class. DGGW Thm 5.15 also separates bad orbifolds, which do not
  carry constant curvature and are outside this comparison.
