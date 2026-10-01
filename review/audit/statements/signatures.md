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

## Group: signatures

### SG.0. Setting and heat input (H)

Source: `theory/signatures/proof.md` lines 41-75 (verbatim).

````
## 1. Setting, heat input and notation

$\mathrm{Sig}$ denotes the set of signatures $\sigma=(g;m_1,\dots,m_n)$ of closed orientable
hyperbolic 2-orbifolds (`definitions.tex`, `def:signature`). Here $g\ge0$, each $m_i\ge2$, and
$m=\{m_i\}$ is a multiset. Write
$$n=|m|,\qquad R(m)=\sum_i\frac1{m_i},\qquad P_j(m)=\sum_im_i^j,\qquad
s(\sigma)=2g-2+\sum_i\Bigl(1-\frac1{m_i}\Bigr)=-\chi=\frac{\mathrm{Area}}{2\pi}>0 .$$
$H_k(\mathcal O)=(c_1,\dots,c_k)$ are the first $k$ heat coefficients (`def:heatcoef`), and
$K_{\rm mult}(\mathcal O;\mathcal P)$ is as in `def:K`.

**Heat input (H).** This is the only analytic input. Every quoted statement was fetched and is
recorded in `literature.md` and `../cone-coefficients/ucar-source.md`.

- (H1) *Smooth part.* At constant curvature $\kappa$ the smooth-stratum coefficient $a_\nu$ is
  $\mathrm{vol}(\mathcal O)$ times a constant depending only on $\nu$ and $\kappa$. This is
  Uçar, Thm 4.20(i), eq. (4.35), for every $\nu$. The structure (smooth part plus one term per
  singular stratum) is DGGW, Thm 4.8 and Def. 4.7.
- (H2) *Cone part.* A cone point of order $k$ contributes $b_l(k)$ at order $t^l$, with
  $b_l(k)=K^l\sum_{i=0}^{l}\frac{2}{4^ii!}c^{\mathbb S}_{l-i}(\pi/k)$ and $c^{\mathbb S}$ given
  by (4.25). This is Uçar, Thm 4.20(ii), eqs. (4.33)–(4.34).
- (H3) The expansion runs in the powers $t^{-1},t^0,t^1,\dots$ (`def:heatcoef`). Hence, at
  $K=-1$,
  $$c_1=\frac{\mathrm{Area}}{4\pi}=\frac s2,\qquad c_{l+2}=\alpha_l\,\mathrm{Area}+C_l(m),\qquad
  C_l(m):=\sum_ib_l(m_i)\quad(l\ge0),$$
  with universal constants $\alpha_l$.

Two consequences follow. Genus enters the heat data only through the area. And two orbifolds of
equal area have equal $c_{l+2}$ exactly when they have equal $C_l$.

The first consequence is an inference, not a fetched sentence: by Gauss–Bonnet the area is
$2\pi s$, and $g$ appears nowhere else. `literature.md` ("What is fetched vs. what is inferred")
records this.

Put $\psi_k(x)=x^{2k-1}-x^{-1}$ for $k\ge1$, and $\Psi_k(m)=\sum_i\psi_k(m_i)=P_{2k-1}(m)-R(m)$.

````

### SG.1. Lemma 1 (cone polynomials)

Source: `theory/signatures/proof.md` lines 78-81 (verbatim).

````
**Lemma 1 (cone polynomials, every $l$).** $p_l(k):=k\,b_l(k)/K^l$ is an even polynomial of
degree $2l+2$ with $p_l(1)=0$. Its leading coefficient is
$|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$.

````

### SG.2. Lemma 2 (triangular basis)

Source: `theory/signatures/proof.md` lines 95-99 (verbatim).

````
**Lemma 2 (triangular basis).** $\phi_l(x):=p_l(x)/x=\sum_{k=1}^{l+1}a_{l,k}\,\psi_k(x)$ with
$a_{l,l+1}\ne0$. Hence, for multisets $m,m'$ and $L\ge1$:
$$C_l(m)=C_l(m')\ (0\le l\le L-2)\iff\Psi_k(m)=\Psi_k(m')\ (1\le k\le L-1).$$
The direction "$\Leftarrow$" does not use $a_{l,l+1}\neq0$.

````

### SG.3. Lemma 3 (padding)

Source: `theory/signatures/proof.md` lines 105-106 (verbatim).

````
**Lemma 3 (padding).** Adjoining points of order 1 changes neither the area nor any $C_l$.

````

### SG.4. Lemma 4 (reduction)

Source: `theory/signatures/proof.md` lines 110-132 (verbatim).

````
**Lemma 4 (reduction).** Let $\sigma=(g;m)$ and $\sigma'=(g';m')$ have $n$ and $n'$ cone
points, and let $L\ge1$. Then $H_L(\mathcal O)=H_L(\mathcal O')$ if and only if
$$2g+n-R(m)=2g'+n'-R(m')\quad\text{and}\quad\Psi_k(m)=\Psi_k(m')\ (1\le k\le L-1).\tag{4.1}$$
Assume (4.1). Then $d:=R(m')-R(m)=2(g'-g)+n'-n$ is an integer. Put
$$U=m\uplus\{1\}^{\max(d,0)},\qquad V=m'\uplus\{1\}^{\max(-d,0)} .$$
Then
$$R(U)=R(V),\qquad P_j(U)=P_j(V)\ \ (j\text{ odd},\ j\le2L-3),\qquad |V|-|U|=2(g-g'),\tag{4.2}$$
and
$$|U|+|V|=2\max\bigl(n+g-g',\;n'+g'-g\bigr).\tag{4.3}$$

Conversely, let $U=m\uplus\{1\}^a$ and $V=m'\uplus\{1\}^b$ be any paddings, and let $g,g'\ge0$.
If (4.2) holds, then $(g;m)$ and $(g';m')$ have equal area and equal first $L$ heat
coefficients.

*In terms of the mirror multiset.* Pad both multisets to a common length $N$, write $R_N$, $P_{j,N}$
for the padded sums, and put $X=m_N\uplus(-m'_N)$. Equal area is
$$s_{-1}(X)=R_N-R'_N=2(g-g').$$
Equal $C_0,\dots,C_{L-2}$ is then equivalent to
$$s_j(X)=P_{j,N}-P'_{j,N}=2(g-g')\qquad (j\text{ odd},\ j\le2L-3),$$
the *same* multiple $2(g-g')$ for every odd $j$ and for $j=-1$. This is the unique solution of
the linear system formed by the cone-sum differences, computed in `heat_structure.py` (4) for
$L\le16$. It follows for all $L$ from Lemma 2, because $\sum_ka_{l,k}=0$.

````

### SG.5. Theorem S

Source: `theory/signatures/proof.md` lines 152-157 (verbatim).

````
**Theorem S.** Let $\mathcal O,\mathcal O'$ be closed orientable hyperbolic 2-orbifolds with
$\sigma(\mathcal O)\neq\sigma(\mathcal O')$ and $H_L(\mathcal O)=H_L(\mathcal O')$. Let $U,V$ be
as in Lemma 4, and let $U^*,V^*$ be obtained by cancelling the elements they have in common.
Then
$$|U^*|+|V^*|\ \ge\ 2L+2 .$$

````

### SG.6. Corollary S1

Source: `theory/signatures/proof.md` lines 179-182 (verbatim).

````
**Corollary S1 (pairwise form).** If $H_L(\mathcal O)=H_L(\mathcal O')$ with
$$L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),$$
then $\sigma(\mathcal O)=\sigma(\mathcal O')$.

````

### SG.7. Corollary S2

Source: `theory/signatures/proof.md` lines 185-191 (verbatim).

````
**Corollary S2 (area form: genus and cone orders from finitely many coefficients).** Let
$\mathcal O$ have area $A$. Any closed orientable hyperbolic 2-orbifold $\mathcal O'$ with
$H_{\lfloor A/\pi\rfloor+4}(\mathcal O')=H_{\lfloor A/\pi\rfloor+4}(\mathcal O)$ has the same
genus and the same cone-order multiset. In the notation of `def:K`, with
$\mathrm{Sig}$ the class of all closed orientable hyperbolic 2-orbifolds,
$$K_{\rm mult}(\mathcal O;\mathrm{Sig})\ \le\ \Bigl\lfloor\frac{\mathrm{Area}(\mathcal O)}{\pi}\Bigr\rfloor+4 .$$

````

### SG.8. Theorem T1

Source: `theory/signatures/proof.md` lines 202-211 (verbatim).

````
**Theorem T1 (cone count and cone orders, genus 0).** Let $\mathcal O$ be a hyperbolic
genus-0 orbifold of area $A$ with $n$ cone points.

1. $n\le A/\pi+4$, with equality iff every order is 2.
2. The first $\lfloor A/\pi\rfloor+4$ heat coefficients determine the cone-order multiset, and
   in particular $n$, among *all* hyperbolic genus-0 orbifolds. The number $n$ need not be known
   in advance.
3. More sharply, the first $\max(n,n')$ coefficients separate it from every genus-0 orbifold
   with $n'$ cone points and a different multiset.

````

### SG.9. Proposition P (Prouhet)

Source: `theory/signatures/proof.md` lines 235-241 (verbatim).

````
**Proposition P (Prouhet; Thue–Morse).** Let $t(i)$ be the parity of the binary digit sum of
$i$. Let $D\ge1$, and let $T_0,T_1$ split $\{0,\dots,2^D-1\}$ according to $t(i)$. Then:

1. $\sum_{T_0}f=\sum_{T_1}f$ for every polynomial $f$ of degree $<D$.
2. For every $c>0$ and $h>0$,
   $$\sum_{i<2^D}\frac{(-1)^{t(i)}}{hi+c}>0 .$$

````

### SG.10. Theorem N

Source: `theory/signatures/proof.md` lines 247-263 (verbatim).

````
**Theorem N (non-uniformity).**

(a) *Genus.* For every $L\ge2$ and every $g'\ge0$ there are closed orientable hyperbolic
2-orbifolds of genus $g'+1$ and $g'$ with equal first $L$ heat coefficients. For $g'=0$ they can
be chosen with area $<2\pi(4^{L-1}-1)$.

(b) *Cone count.* For every $k\ge2$ there are hyperbolic genus-0 orbifolds with $n$ and $n+1$
cone points, for some $n$, with equal first $k$ heat coefficients.

(c) Consequently:

- no fixed number of heat coefficients determines the genus among closed orientable hyperbolic
  2-orbifolds;
- no fixed number determines the cone count among genus-0 ones;
- $\sup_{\mathcal O}K_{\rm mult}(\mathcal O;\mathcal P)=\infty$, both for $\mathcal P=\mathrm{Sig}$
  and for $\mathcal P$ the genus-0 class.

````

### SG.11. Construction claims for Theorem N (computed ranges)

Source: `theory/signatures/proof.md` lines 305-313 (verbatim).

````
The constructions are built and checked with the actual cone coefficients $b_l$:

- (a) for $L=2,\dots,6$ (`genus.py` (A)). Each pair shares *exactly* $L$ coefficients; the
  $L=6$ pair has 1023 and 1025 cone points.
- (b) for $k=2,3$ (`cone_count.py` (d)): 9 vs 10 and 103 vs 104 cone points, sharing exactly
  2 and 3 coefficients.

For $k\ge4$ the greedy denominators grow doubly exponentially, which makes exact verification
impractical. The proof above covers every $k$.
````

### SG.12. Corollary N1

Source: `theory/signatures/proof.md` lines 315-319 (verbatim).

````
**Corollary N1 (growth).** Let $f(A)=\max\{K_{\rm mult}(\mathcal O;\mathrm{Sig}):
\mathrm{Area}(\mathcal O)\le A\}$. For $A\ge6\pi$,
$$\Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\
\Bigl\lfloor\frac A\pi\Bigr\rfloor+4 .$$

````

### SG.13. Manuscript-facing LaTeX versions (statements.tex)

Source: `theory/signatures/statements.tex` lines 11-117 (verbatim).

````
\subsection{The signature from finitely many heat coefficients}\label{subsec:signature}

Throughout, $\Sig$ is the class of all closed orientable hyperbolic $2$-orbifolds, and $\Pill_0\subset\Sig$
the subclass of genus $0$. For a signature $(g;m_1,\dots,m_n)$ write $R=\sum_i1/m_i$,
$P_j=\sum_im_i^{\,j}$ and $s=2g-2+n-R=\operatorname{Area}/2\pi$.

\begin{lemma}[Heat data of a signature]\label{lem:sigdata}
For $\Orb,\Orb'\in\Sig$ with signatures $(g;m)$, $(g';m')$ and $L\ge1$, the following are equivalent:
\begin{enumerate}[label=(\roman*)]
\item $H_L(\Orb)=H_L(\Orb')$;
\item there are paddings $U=m\uplus\{1\}^a$, $V=m'\uplus\{1\}^b$ with
\[
  R(U)=R(V),\qquad P_j(U)=P_j(V)\ \ (j\ \text{odd},\ j\le 2L-3),\qquad |V|-|U|=2(g-g').
\]
\end{enumerate}
Moreover, if the multisets are padded to a common length and $X=m\uplus(-m')$, then (i) holds if and only if
$\sum_{x\in X}x^{-1}=\sum_{x\in X}x^{j}=2(g-g')$ for every odd $j\le2L-3$.
\end{lemma}

\noindent
The input is the structure of the heat expansion at constant curvature
\cite[Theorem~4.8]{dggw2008}, \cite[Theorem~4.20]{ucar2017}: the smooth part of every coefficient is a fixed
multiple of the area, and a cone point of order $k$ contributes $(-1)^l k^{-1}p_l(k)$ at order $t^l$ (curvature $-1$), with
$p_l$ even, $p_l(1)=0$ and leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$. The genus enters only
through the area.

\begin{theorem}[Separation]\label{thm:sigsep}
Let $\Orb,\Orb'\in\Sig$ have signatures $(g;m_1,\dots,m_n)\neq(g';m'_1,\dots,m'_{n'})$ and equal first $L$
heat coefficients. Let $U,V$ be any paddings as in Lemma~\ref{lem:sigdata}(ii), and let $U^*,V^*$ be
obtained by removing their common elements (these do not depend on the choice of paddings). Then
$|U^*|+|V^*|\ge 2L+2$. In particular, if
\[
  L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),
\]
then $H_L(\Orb)=H_L(\Orb')$ implies $\sigma(\Orb)=\sigma(\Orb')$.
\end{theorem}

\begin{corollary}[Genus and cone orders from $\lfloor\operatorname{Area}/\pi\rfloor+4$ coefficients]\label{cor:sigarea}
For every $\Orb\in\Sig$,
\[
  \Kmult(\Orb;\Sig)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
That is, the first $\lfloor\operatorname{Area}(\Orb)/\pi\rfloor+4$ heat coefficients determine the genus and
the cone-order multiset of $\Orb$ among all closed orientable hyperbolic $2$-orbifolds. The number is
read off from the first coefficient $c_1=\operatorname{Area}/4\pi$.
\end{corollary}

\begin{theorem}[Cone count in genus $0$]\label{thm:sigcount}
Let $\Orb\in\Pill_0$ have $n$ cone points. Then $n\le\operatorname{Area}(\Orb)/\pi+4$, with equality exactly
when every cone order is $2$, and
\[
  \Kmult(\Orb;\Pill_0)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
More precisely, $H_{\max(n,n')}$ separates $\Orb$ from every $\Orb'\in\Pill_0$ with $n'$ cone points and a
different cone-order multiset. In particular the cone count $n$ is determined without being known in
advance.
\end{theorem}

\begin{theorem}[No uniform number of coefficients]\label{thm:signonuniform}
\leavevmode
\begin{enumerate}[label=(\alph*)]
\item For every $L\ge2$ and every $g'\ge0$ there are orbifolds in $\Sig$ of genus $g'+1$ and $g'$ with equal
  first $L$ heat coefficients; for $g'=0$ they may be taken of area less than $2\pi(4^{L-1}-1)$.
\item For every $k\ge2$ there are orbifolds in $\Pill_0$ with $n$ and $n+1$ cone points, for some $n$, with
  equal first $k$ heat coefficients.
\end{enumerate}
Hence $\sup_{\Orb}\Kmult(\Orb;\Sig)=\sup_{\Orb}\Kmult(\Orb;\Pill_0)=\infty$, and no fixed number of heat
coefficients determines the genus in $\Sig$ or the cone count in $\Pill_0$.
\end{theorem}

\begin{corollary}[Growth]\label{cor:siggrowth}
Let $f(A)=\max\{\Kmult(\Orb;\Sig):\operatorname{Area}(\Orb)\le A\}$. For $A\ge6\pi$,
\[
  \Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\ \Bigl\lfloor\frac{A}{\pi}\Bigr\rfloor+4 .
\]
\end{corollary}

\begin{example}\label{ex:siggenus}
The orbifolds of signatures $(1;15)$ and $(0;3,3,5,5)$ have the same first two heat coefficients, and
$(1;15,15,15)$ and $(0;3,3,5,7,7,21)$ have the same first three (exact computation). In each pair the genera
differ.
\end{example}

\begin{remark}[Relation to $\Kmult$ and $\Kiso$]\label{rem:sigK}
Theorem~\ref{thm:sigsep} with $g=g'=0$ and $n=n'$ is the statement $\Kmult(\Orb;\Pill_n)\le n$ for the class
$\Pill_n$ of hyperbolic spheres with $n$ cone points, i.e.\ the injectivity that Remark~\ref{rem:nconerestated}(a) leaves conditional, now proved
independently (\texttt{theory/audibility/proof.md}, Theorem~A). Corollary~\ref{cor:sigarea} extends it to all genera and all cone
counts at once, at the price of a bound that depends on the area, and Theorem~\ref{thm:signonuniform}
shows that some such dependence is unavoidable. All of this concerns $\Kmult$; by \eqref{eq:Kcompare}
and Proposition~\ref{prop:Kinf} (conditional on Theorem~\ref{thm:locality}), $\Kiso$ remains infinite
whenever two non-isometric orbifolds share a signature.
\end{remark}

\begin{remark}[What short-time heat flow detects]\label{rem:sigphysics}
This remark is interpretation, not part of any proof. Heat at short times is local: it sees curvature,
hence the area, and each cone point through a fixed function of its order. A handle has no local
signature and is heard only through the area it uses up. Comparing two orbifolds through the mirror
multiset $U^*\uplus(-V^*)$, a genus difference appears as an imbalance between its positive and negative
parts, and Theorem~\ref{thm:sigsep} says that the heat coefficients force the mirror multiset to be
symmetric, hence balanced, once there are enough of them relative to its size. A handle therefore costs
no more coefficients to hear than a cone point.
\end{remark}

% Exact extent. Lemma sigdata, Theorems sigsep, sigcount, signonuniform and Corollaries sigarea,
% siggrowth are proved for all L given the cited heat input (proof.md sections 2-4). The constructions of
% Theorem signonuniform are built and checked with the actual cone coefficients for L <= 6 (a) and
% k <= 3 (b). Open: whether f(A) grows linearly (proof.md section 7).
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
