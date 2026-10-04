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

## Group: locality

### LO.0. Setting

Source: `theory/locality/proof.md` lines 9-17 (verbatim).

````
**Setting.** $\mathcal O=\Gamma\backslash\mathbb H^2$ is a closed orientable hyperbolic
2-orbifold, i.e. $\Gamma\subset PSL(2,\mathbb R)$ is a cocompact Fuchsian group. Its
signature $\sigma(\mathcal O)=(g;m_1,\dots,m_n)$ is as in `\label{def:signature}`
(`theory/definitions.tex`). $\Delta\ge0$ is the Laplacian, $0=\lambda_0<\lambda_1\le\dots$ its
eigenvalues, $Z_{\mathcal O}(t)=\sum_j e^{-\lambda_j t}$ its heat trace, and $c_j(\mathcal O)$
the coefficients of `\label{def:heatcoef}`. The orbifold Euler characteristic is
$\chi(\mathcal O)=2-2g-\sum_i(1-1/m_i)$. By the orbifold Gauss–Bonnet theorem,
$\operatorname{Area}(\mathcal O)=-2\pi\chi(\mathcal O)$ [Thurston, 13.3.5 and the sentence
after it, "If O is elliptic or hyperbolic, then area(O) = 2π|χ(O)|", electronic p. 312; DS, Thm 3.2, p. 5].
````

### LO.1. Theorem 1 (signature locality)

Source: `theory/locality/proof.md` lines 47-69 (verbatim).

````
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
(For $j=1$ the cone sum is absent: $\Phi_1=\tfrac12\big(2g-2+\sum_i(1-\tfrac1{m_i})\big)$.)
In particular two orbifolds of the same signature have the same expansion to all orders.
No half-integer powers occur: [DGGW] (4.9) allows $t^{j/2}$, but the only strata are the
2-dimensional regular part and points, whose series are in integer powers.

The constants are explicit [Uçar, Thm 4.20 (i), (ii) at $\kappa=-1$]:
$\alpha_k=\frac{(-1)^k}{k!\,4^k}\sum_{l=0}^k\binom kl(-4)^lB_{2l}(\tfrac12)$, and $\beta_k(m)$ is
the coefficient of $t^k$ in $C$ of [Uçar, (4.33)], built from $c^S_\ell(\pi/m)$ of (4.25). These
are the formulas implemented in `numerics/theory.py` and asserted there against DGGW §5.6
and Schueth's Theorem 4.1 for $k\le2$.
````

### LO.2. Thurston Cor. 13.3.7 as quoted

Source: `theory/locality/proof.md` lines 154-157 (verbatim).

````
**Source statement** [Th, Corollary 13.3.7, electronic ed. p. 318, original p. 13.27],
verbatim: *"The Teichmüller space T(O) of an orbifold O with χ(O) < 0 is homeomorphic to
Euclidean space of dimension −3χ(X_O) + 2k + l, where k is the number of elliptic points and
l is the number of corner reflectors."* The proof (p. 318) cuts $\mathcal O$ along disjoint
````

### LO.3. Proposition 2.1

Source: `theory/locality/proof.md` lines 167-171 (verbatim).

````
**Proposition 2.1.** For a closed orientable hyperbolic 2-orbifold of signature
$(g;m_1,\dots,m_n)$,
$$\dim_{\mathbb R}T(\mathcal O)=6g-6+2n .$$
Among hyperbolic signatures, it vanishes exactly for $(g;n)=(0;3)$, the triangle orbifolds,
and is $\ge2$ otherwise.
````

### LO.4. Proposition 2.2

Source: `theory/locality/proof.md` lines 184-185 (verbatim).

````
**Proposition 2.2.** If $6g-6+2n>0$, the closed orientable hyperbolic orbifolds of
signature $\sigma=(g;m_1,\dots,m_n)$ fall into uncountably many isometry classes.
````

### LO.5. Corollary 2.3

Source: `theory/locality/proof.md` lines 212-219 (verbatim).

````
**Corollary 2.3 ($K_{\rm iso}=\infty$).** Let $\sigma$ be a hyperbolic signature with
$6g-6+2n>0$, i.e. any closed orientable hyperbolic 2-orbifold that is not a triangle
orbifold. Let $\mathcal P$ be a comparison class (`\label{def:K}`) containing every orbifold
of signature $\sigma$. Examples: the class of all closed orientable hyperbolic
2-orbifolds; for $g=0$, the class $\mathcal P_n$ of `\label{rem:nconerestated}`. Then
$$K_{\rm iso}(\mathcal O;\mathcal P)=\infty\qquad\text{for every }\mathcal O\in\mathcal P\text{ with }\sigma(\mathcal O)=\sigma .$$
For the triangle orbifolds ($g=0$, $n=3$), $K_{\rm iso}(\mathcal O;\mathcal P)=K_{\rm mult}(\mathcal O;\mathcal P)$ for
every class $\mathcal P$.
````

### LO.6. Theorem 3.1

Source: `theory/locality/proof.md` lines 254-265 (verbatim).

````
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
````

### LO.7. Lemma 3.2 (statement only)

Source: `theory/locality/proof.md` lines 289-293 (verbatim).

````
**Lemma 3.2 (admissibility of the heat function).** Fix $\chi\in C_c^\infty(\mathbb R)$, even,
$0\le\chi\le1$, $\chi=1$ on $[-1,1]$, $\operatorname{supp}\chi\subset[-2,2]$, and put $g_R(u)=g_t(u)\chi(u/R)$ and
$h_R(r)=\int g_R(u)e^{iru}du$. Then $h_R$ is even, entire and of exponential type $\le2R$
(Paley–Wiener), so [DS] (1) holds for $h_R$, with Fourier transform $g_R$. As
$R\to\infty$ each term converges to the corresponding term for $h_t$:
````

### LO.8. Lemma 3.3

Source: `theory/locality/proof.md` lines 321-324 (verbatim).

````
**Lemma 3.3 (counting).** Let $A=\operatorname{Area}(\mathcal O)$ and
$\delta=\operatorname{diam}(\mathcal O)$, and let $N(L)$ be the number of hyperbolic conjugacy
classes $[\gamma]$ with $\ell(\gamma)\le L$. Then
$$N(L)\le\frac{2\pi(\cosh(L+3\delta)-1)}{A}\le\frac{\pi}{A}e^{L+3\delta}.$$
````

### LO.9. Theorem 3.4

Source: `theory/locality/proof.md` lines 347-362 (verbatim).

````
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
````

### LO.10. Claim: the t^{-1/2} prefactor cannot be dropped

Source: `theory/locality/proof.md` lines 396-412 (verbatim).

````
**The prefactor $t^{-1/2}$ cannot be dropped.** T3 as posed asks for
$|Z_1-Z_2|\le Ce^{-\ell^2/4t}$ with a constant $C$. In general that bound is **false**. By
Theorem 3.5, whenever the shortest geodesics differ, $|Z_1-Z_2|\,e^{\ell^2/4t}$ grows like
$t^{-1/2}$. The family of T4 is an example:
$\sqrt t\,e^{\ell^2/4t}|Z_1-Z_2|\to w/(2\sinh(\ell/2)\sqrt{4\pi})\ne0$.

What is true:

- the bound with $t^{-1/2}$ (Theorem 3.4);
- as a consequence, for every $\varepsilon\in(0,\ell)$, $|Z_1-Z_2|\le C_\varepsilon e^{-(\ell-\varepsilon)^2/4t}$
  for $t\le t_0$.

The falsity of the constant-$C$ form is proved for every pair with $L_*=\ell$, in particular
whenever $\ell_1\ne\ell_2$ (if $L_*>\ell$ the constant-$C$ bound does hold). Pairs with
$\ell_1\ne\ell_2$ exist in every signature with $\dim T>0$ in which the systole varies on
$T$; in the T4 family they are exhibited explicitly (systole $4b(\tau)$, by certified
enumeration of the reflection group, `numerics/moduli/geodesics.py`).
````

### LO.11. Theorem 3.5

Source: `theory/locality/proof.md` lines 423-430 (verbatim).

````
**Theorem 3.5.** Let $\mathcal O_1,\mathcal O_2$ have the same signature.

- If $w_1\equiv w_2$, then $Z_1\equiv Z_2$, and the orbifolds are isospectral.
- Otherwise, let $L_*=\min\{L:w_1(L)\ne w_2(L)\}$. Then, as $t\downarrow0$,
$$Z_1(t)-Z_2(t)=\frac{w_1(L_*)-w_2(L_*)}{2\sinh(L_*/2)}\,\frac{e^{-t/4}e^{-L_*^2/4t}}{\sqrt{4\pi t}}\,\big(1+o(1)\big),$$
  so $Z_1-Z_2\ne0$ for small $t$ and $\log|Z_1-Z_2|=-L_*^2/4t-\tfrac12\log t+O(1)$.
- In particular, if $\ell_1\ne\ell_2$, then $L_*=\min(\ell_1,\ell_2)=\ell$, and the
  exponent $\ell^2/4$ of Theorem 3.4 is attained.
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
