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

## Group: audibility

### AU.0. Heat input and notation

Source: `theory/audibility/proof.md` lines 26-50 (verbatim).

````
**Input from the heat expansion (not re-derived here).** On a closed hyperbolic orbifold of
genus 0 with cone points of orders $m_1,\dots,m_n\ge2$, the heat coefficient of $t^{-1}$ is a
fixed multiple of the area $2\pi(n-2-R)$. Every smooth-stratum term is a fixed multiple of the
area. A cone point of order $m$ contributes $b_l(m)=K^l\,\tfrac1m\,p_l(m)$ at order $t^l$ (Gauss curvature $K=-1$),
where $p_l$ is an *even* polynomial of degree $2l+2$ with
$p_l(1)=0$ and leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$. Sources:
`review/hyperresearch/Q2-cone-coefficients.md`, Uçar (4.25)+(4.33), and Schueth Thm 4.1 for
$l\le2$. The explicit $p_0,\dots,p_3$ listed there are even with root $m=1$.

Hence $\sum_i b_l(m_i)$ is a rational combination of $R,P_1,P_3,\dots,P_{2l+1}$ (write
$P_k=\sum_i m_i^k$) with a nonzero coefficient on $P_{2l+1}$. The map from the first $n$ heat
coefficients to

$$\mathcal I_n(m)=(R,\;P_1,\;P_3,\;\dots,\;P_{2n-3})$$

is therefore triangular and invertible, for a fixed number $n$ of cone points. Throughout,
$e_k$ denotes the elementary symmetric functions of the $m_i$, $e_0=1$, and $R=e_{n-1}/e_n$. Two
polynomials are attached to $m$:

- $f(z)=\prod_i(1+m_iz)=\sum_k e_kz^k$;
- $p(z)=\prod_i(z+m_i)=\sum_k e_kz^{n-k}$.

$\Delta_k$ is the $k$-th Hurwitz determinant of $p$, following Holtz–Tyaglov (1.37); see
`sources/SOURCES.md`.

````

### AU.1. Theorems A, B, C

Source: `theory/audibility/proof.md` lines 51-84 (verbatim).

````
> **Theorem A (audibility of the cone orders; all $n\ge1$).** Let $m$ be a multiset of $n$
> nonzero complex numbers with $m_i+m_j\neq0$ for all $i<j$. Equivalently, by Orlando,
> $e_n\Delta_{n-1}\neq0$. Let $m'$ be any multiset of $n$ nonzero complex numbers with
> $\mathcal I_n(m')=\mathcal I_n(m)$. Then $m'=m$.
>
> In particular $\mathcal I_n$ is injective on multisets of positive reals, repeated orders
> allowed. So the first $n$ heat coefficients determine the cone-order multiset of an $n$-cone
> hyperbolic orbifold of genus 0: $K_{\rm mult}\le n$.

> **Theorem B (the linear system and its determinant).** Let $T(z)=\tanh\bigl(\sum_{k\ {\rm odd}}
> P_kz^k/k\bigr)$. The $n-1$ equations
> $$e_{2j+1}-\sum_{i=0}^{j}T_{2i+1}\,e_{2j-2i}=0\qquad (j=0,\dots,n-2),$$
> together with $e_{n-1}-Re_n=0$, form a square linear system $M\,e=b$ in $e_1,\dots,e_n$.
> Its coefficients are polynomials in the heat invariants $\mathcal I_n$ alone, and the true
> $e$ solves it. For every $n\ge2$,
> $$\det M=c_n\,\frac{\Delta_{n-1}(p)}{e_n}=c_n\,\frac{\prod_{i<j}(m_i+m_j)}{\prod_i m_i},
> \qquad c_n\in\mathbb Q^\times .$$
> For $n=3,\dots,8$, $c_n=+1,+1,-1,-1,+1,+1$ (`linear_system.py`).

> **Theorem C (the fibres of $n-1$ invariants; sharpness).**
>
> 1. *Pair criterion.* Let $m,m'$ be multisets of $n$ nonzero complex numbers, and let
>    $Q(z)=\prod_i(z-m_i)\prod_j(z+m'_j)$. Then $\mathcal I_{n-1}$ agree, meaning $R$ and
>    $P_1,\dots,P_{2n-5}$, if and only if $Q(z)-Q(-z)=2\kappa z^3$ for some $\kappa$. If
>    $m_i+m_j\neq0$ for $i<j$, then $\kappa=0$ exactly when $m'=m$.
> 2. *Real sharpness, every $n\ge2$.* Every multiset of $n$ pairwise distinct positive reals lies
>    on a real curve of positive-real multisets sharing $\mathcal I_{n-1}$. Over the positive
>    reals, $n-1$ invariants never suffice.
> 3. *Integer sharpness ($n\ge3$, the range where hyperbolic genus-0 orbifolds exist).* It is
>    equivalent to finding a positive rational pair $m\neq m'$ (as multisets), i.e. a point off
>    all permutation components
>    on the pair variety, by scaling. It holds for $n=3$ and $n=4$ with explicit witnesses. For
>    $n=5$ no witness exists with all orders $\le120$ (216,071,394 multisets, exhaustive). For
>    $n\ge5$ it is open.
````

### AU.2. Lemma 1 (parity)

Source: `theory/audibility/proof.md` lines 88-91 (verbatim).

````
**Lemma 1 (parity).** In $\mathbb Q[x_1,\dots,x_N]$ let $s_j=\sum x_i^j$ and let $e_j$ be the
elementary symmetric functions. For odd $j$, $e_j$ lies in the ideal generated by
$s_1,s_3,\dots,s_j$. Conversely, $s_j$ lies in the ideal generated by $e_1,e_3,\dots,e_j$.

````

### AU.3. Jacobian claim (Remark 2) and padding claim (Remark 3)

Source: `theory/audibility/proof.md` lines 123-136 (verbatim).

````
2. Repeated orders are allowed. The Jacobian of $\mathcal I_n$ is
   $c_n\,V(m)\prod_{i<j}(m_i+m_j)/\prod m_i^2$ with $V(m)=\prod_{i<j}(m_j-m_i)$ and
   $c_n=-\prod_{r<n}(2r-1)$ (checked $n\le7$).
   It vanishes on the diagonals $m_i=m_j$, so the map is not an immersion there, yet it is
   injective. The obstruction to injectivity is the Orlando factor $\prod(m_i+m_j)$, not the
   Vandermonde $V(m)$.
3. Different numbers of cone points. An order-1 "cone" is invisible to every heat coefficient
   ($b_l(1)=0$, and the area $2\pi(n-2-R)$ is unchanged by adding $m=1$). An orbifold with
   $n'\le n$ cone points padded by ones is therefore an $n$-multiset of positive reals. By
   Theorem A, the first $n$ coefficients distinguish an $n$-cone orbifold from every genus-0
   orbifold with at most $n$ cone points.
   - The comparison with orbifolds having *more* cone points is not covered by Theorem A.
   - A search of 3-cone against 4-cone orbifolds with orders $\le60$ found no pair sharing three
     coefficients (`sharpness_search.py`, part C).
````

### AU.4. Integer witnesses table (claims)

Source: `theory/audibility/proof.md` lines 217-225 (verbatim).

````
In the table, $\Phi(z):=p(z)p'(-z)-p'(z)p(-z)$ with $p=\prod(z+m_i)$ and $p'=\prod(z+m'_j)$.
It satisfies $\Phi=(-1)^{n+1}\bigl(Q(z)-Q(-z)\bigr)$.

| $n$ | witness sharing $\mathcal I_{n-1}$ | separated by | $\Phi(z)$ |
|---|---|---|---|
| 3 | $\{2,8,8\}$, $\{3,3,12\}$ ($R=3/4$, $S_1=18$) | $P_3$: 1032 vs 1782 | $500\,z^3$ |
| 4 | $\{3,10,15,30\}$, $\{4,5,21,28\}$ ($R=8/15$, $S_1=58$, $P_3=31402$) | $P_5$: 25159618 vs 21298618 | $1544400\,z^3$ |
| 5 | none with orders $\le60$ (7,028,847 multisets) or $\le120$ (216,071,394) | | |

````


## Group: definitions

### DF.1. def:signature, def:heatcoef

Source: `theory/definitions.tex` lines 17-41 (verbatim).

````
\begin{definition}[Signature]\label{def:signature}
Let $\Orb$ be a closed, orientable $2$-orbifold whose only singular points are cone points.
Let $g$ be the genus of the underlying surface and $m_1,\dots,m_n\ge2$ the orders of the cone
points, listed with multiplicity. The \emph{signature} of $\Orb$ is
\[
  \sigma(\Orb)=(g;\,m_1,\dots,m_n),
\]
in which the $m_i$ form a multiset: the order of listing carries no information. Write
$\chi(\Orb)=2-2g-\sum_{i=1}^n(1-\tfrac1{m_i})$. The orbifold carries a hyperbolic metric exactly
when $\chi(\Orb)<0$. A \emph{hyperbolic triangular pillow} is the case $(g;n)=(0;3)$; it is
denoted $\Orb(p,q,r)$ with $p\le q\le r$, and $\chi(\Orb(p,q,r))=R-1$ for
$R=\tfrac1p+\tfrac1q+\tfrac1r$. Two orbifolds are \emph{isometric} if there is a Riemannian
isometry of the hyperbolic metrics; isometric orbifolds have equal signatures.
\end{definition}

\begin{definition}[Leading heat coefficients]\label{def:heatcoef}
For a closed orientable hyperbolic $2$-orbifold $\Orb$ with Laplacian $\Delta$ the heat trace
has an asymptotic expansion in integer powers of $t$ \cite{donnelly1976, dggw2008},
\[
  \operatorname{tr}e^{-t\Delta}\;\sim\;\sum_{j\ge1}c_j(\Orb)\,t^{\,j-2}\qquad(t\downarrow0).
\]
The coefficient $c_j(\Orb)$ is the \emph{$j$-th leading heat coefficient}. In particular
$c_1(\Orb)=\operatorname{Area}(\Orb)/4\pi=-\chi(\Orb)/2$, which for a triangular pillow equals
$\tfrac12(1-R)$. For $k\ge1$ put $H_k(\Orb)=(c_1(\Orb),\dots,c_k(\Orb))$.
\end{definition}
````

### DF.2. def:K and eq:Kcompare

Source: `theory/definitions.tex` lines 49-65 (verbatim).

````
\begin{definition}[$\Kiso$ and $\Kmult$]\label{def:K}
For $\Orb\in\Pill$ let
\begin{align*}
  \Kiso(\Orb;\Pill)&=\min\{k\ge1:\ \text{for every }\Orb'\in\Pill,\ H_k(\Orb')=H_k(\Orb)\Rightarrow\Orb'\ \text{is isometric to }\Orb\},\\
  \Kmult(\Orb;\Pill)&=\min\{k\ge1:\ \text{for every }\Orb'\in\Pill,\ H_k(\Orb')=H_k(\Orb)\Rightarrow\sigma(\Orb')=\sigma(\Orb)\},
\end{align*}
with $\min\emptyset=\infty$. Thus $\Kiso$ is the least number of leading heat coefficients that
determine $\Orb$ up to isometry among the members of $\Pill$, and $\Kmult$ is the least number that
determine its signature, i.e.\ its genus and its cone-order multiset.
\end{definition}

Both sets are upward closed in $k$, so the minima are well defined. Because isometric orbifolds
have equal signatures, the condition defining $\Kiso$ implies the one defining $\Kmult$, and
therefore
\begin{equation}\label{eq:Kcompare}
  \Kmult(\Orb;\Pill)\ \le\ \Kiso(\Orb;\Pill).
\end{equation}
````

### DF.3. prop:rigidity (statement)

Source: `theory/definitions.tex` lines 69-74 (verbatim).

````
\begin{proposition}[Rigidity of triangular pillows]\label{prop:rigidity}
If $\Orb,\Orb'\in\Pill_3$ have the same signature then they are isometric. Consequently
\[
  \Kiso(\Orb;\Pill_3)=\Kmult(\Orb;\Pill_3)\qquad\text{for every }\Orb\in\Pill_3 .
\]
\end{proposition}
````

### DF.4. eq:moduli

Source: `theory/definitions.tex` lines 95-105 (verbatim).

````
By Troyanov's Theorem~A a hyperbolic cone metric on the sphere with prescribed angles is the same
datum as a conformal structure on the sphere with $n$ labelled marked points, and the space of such
structures has complex dimension $n-3$; Thurston's description of the space of shapes of
polyhedra with $n$ cone points, locally isometric to $\mathbb{C}H^{\,n-3}$, is the flat analogue
\cite{thurston1998}. Hence, for genus $0$,
\begin{equation}\label{eq:moduli}
  \dim_{\mathbb R}\mathcal M(0;m_1,\dots,m_n)=2n-6,
\end{equation}
which is $0$ for $n=3$ and positive for every $n\ge4$. (This is a two-step deduction from the two
cited sources and is flagged as such in \texttt{theory/teichmuller-dimension-sources.md}; for $g\ge1$
the corresponding count is not used here and would need its own source.)
````

### DF.5. thm:locality, prop:Kinf (statements)

Source: `theory/definitions.tex` lines 110-128 (verbatim).

````
\begin{theorem}[Locality; forward reference]\label{thm:locality}
For every $j\ge1$ there is a function $\Phi_j$ of the signature alone with
$c_j(\Orb)=\Phi_j(\sigma(\Orb))$ for every closed orientable hyperbolic $2$-orbifold $\Orb$.
\end{theorem}

\noindent
Informally: heat invariants cannot see moduli. What is available now is the cone part: the
closed forms of Dryden--Gordon--Greenwald--Webb, Schueth and U\c{c}ar
\cite{dggw2008, schueth2019, ucar2017} depend only on the order $m_i$ of the cone point, for every
$j$ in U\c{c}ar's case, and were recomputed in exact arithmetic for $j\le6$
(\texttt{theory/cone-coefficients/}). What the locality theorem has to supply is the smooth part
at every order and the assembly of the pieces.

\begin{proposition}[Conditional on Theorem~\ref{thm:locality}]\label{prop:Kinf}
Suppose $\Pill$ contains two non-isometric orbifolds of the same signature $\sigma_0$. Then
$\Kiso(\Orb;\Pill)=\infty$ for every $\Orb\in\Pill$ with $\sigma(\Orb)=\sigma_0$. In particular,
if $\Pill\supseteq\mathcal M(0;m_1,\dots,m_n)$ with $n\ge4$, then $\Kiso(\Orb;\Pill)=\infty$ for all
$\Orb$ of signature $(0;m_1,\dots,m_n)$.
\end{proposition}
````

### DF.6. thm:Crestated (statement)

Source: `theory/definitions.tex` lines 142-150 (verbatim).

````
\begin{theorem}[Theorem~\ref{thmC}, restated]\label{thm:Crestated}
For every $\Orb\in\Pill_3$,
\[
  \Kiso(\Orb;\Pill_3)=\Kmult(\Orb;\Pill_3)\le3 .
\]
The value is $3$ exactly when $\Orb$ belongs to a two-coefficient collision, that is, when some
$\Orb'\in\Pill_3$ with $\sigma(\Orb')\ne\sigma(\Orb)$ has the same $R$ and the same $S_1$; for
instance for $\Orb(2,8,8)$ and $\Orb(3,3,12)$.
\end{theorem}
````

### DF.7. rem:nconerestated

Source: `theory/definitions.tex` lines 159-177 (verbatim).

````
\begin{remark}[Larger cone counts, restated]\label{rem:nconerestated}
Let $\Pill_n$ be the class of hyperbolic spheres with $n\ge3$ cone points, $\sum_i(1-1/m_i)>2$.
\begin{enumerate}[label=(\alph*)]
\item \emph{Multiset level.} Modulo the universal smooth contributions, $c_1,\dots,c_n$ are the $n$
  functions $R,\,S_1,\,P_3,\,P_5,\dots,P_{2n-3}$ of the multiset $\{m_i\}$, with $P_k=\sum_im_i^k$ and
  $c_j$ carrying $P_{2j-3}$ for $j\ge2$ with a nonzero weight. If the map
  $\{m_i\}\mapsto(R,S_1,P_3,\dots,P_{2n-3})$ is injective on $n$-element multisets, then
  $\Kmult(\Orb;\Pill_n)\le n$. For $n=3$ this is Proposition~\ref{prop:recovery}; for $n\ge4$ injectivity is not
  proved here.
\item \emph{Isometry level.} For $n\ge4$, $\Kiso(\Orb;\Pill_n)=\infty$ by
  Proposition~\ref{prop:Kinf} and \eqref{eq:moduli}. The statement that the bound $K\le n$ extends
  the case $n=3$ of Theorem~\ref{thmC} is therefore valid for $\Kmult$ (conditionally on injectivity) and
  false for $\Kiso$; what singles out $n=3$ is rigidity, Proposition~\ref{prop:rigidity}.
\item \emph{A lower bound at $n=4$.} The multisets $\{3,10,15,30\}$ and $\{4,5,21,28\}$ are
  hyperbolic, have the same $S_1=58$, $R=8/15$ and $P_3=31402$, and have $P_5=25159618\ne21298618$
  (exact computation, \texttt{theory/definitions-check.py}). Hence $\Kmult\ge4$ for pillows with
  these signatures, and $\Kmult=4$ for them if the injectivity in (a) holds for $n=4$.
\end{enumerate}
\end{remark}
````
