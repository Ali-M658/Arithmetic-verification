# G5-bis audit: statements under review, group `pte-structure`

PTE structure: the dictionary, the Descartes bound, balanced constructions, the pencil, the shift

Every result below is copied verbatim, by line range, from its source file (`review/audit-2/build_statements.py`
asserts the anchors and that no proof text is included). Items marked COMPOSED combine verbatim excerpts with
connective text in [square brackets]. **Proofs, scripts and data of the sessions that produced these results are
deliberately withheld.** You must not open any file of `theory/pte/`, `theory/revision/`, `theory/signatures/`
(other than where stated below), `review/referee-sim/` or `paper/` (the manuscript contains proofs of some of these
results). If you do open one by accident, say so in your REVIEW.md under 'contamination'.



## Context files you may read (previously audited statements, no proofs)

- review/audit/statements/signatures.md  (the previously audited results [Sig]: Lemma 1-4, Theorem S, Lemma 5 is quoted below as an input; definitions DF.1 of signature and heat coefficient)

## External inputs

- [Sig] Lemma 4 and Theorem S (previously audited, in signatures.md SG.4, SG.5): the reduction of 'two orbifolds share their first L heat coefficients' to an L-configuration, and |Z| even and >= 2L+2.
- [Sig] Lemma 2 (SG.2): the (L+1)-st coefficient agrees iff P_{2L-1}(U)=P_{2L-1}(V).
- [Sig] Lemma 5: a multiset of size <= 2L-2 with vanishing odd power sums up to 2L-3 is symmetric (odd elementary symmetric functions vanish). Re-prove it if you use it.
- [Sig] (4.3) and Corollary S2 (SG.7): the area bound Area/pi <= ... used by Lemma 1.2(5).

## Fetched sources

Texts fetched headlessly by `review/audit-2/fetch_sources.sh` are in `review/audit-2/sources/` (not committed).
Never quote a source from memory: quote the fetched text, with page or section. An unreachable source is an
instrument gap, to be logged, not a confirmation.


## Group: pte-structure

### PS.0. Setting, Definition 1.1, Lemma 1.2 (dictionary)

Source: `theory/pte/proof.md` lines 49-85 (verbatim).

````
## 1. Setting

Throughout, (H1)–(H3) of [Sig] §1 are assumed, as there. Two closed orientable hyperbolic
2-orbifolds with signatures $\sigma=(g;m)\ne\sigma'=(g';m')$ share their first $L$ heat
coefficients if and only if the following holds ([Sig] Lemma 4, Theorem S). Pad $m$ and $m'$
by 1s to $U$ and $V$ with $R(U)=R(V)$, and cancel common elements to get $U^*,V^*$. Then the
multiset $Z=U^*\uplus(-V^*)$ satisfies the definition below, and $|V^*|-|U^*|=2(g-g')$.

**Definition 1.1.** An *$L$-configuration* is a nonempty finite multiset $Z$ of nonzero
rationals such that:

- $s_j(Z):=\sum_{z\in Z}z^j=0$ for odd $1\le j\le2L-3$;
- $s_{-1}(Z)=0$;
- $Z$ contains no pair $\{z,-z\}$;
- $|Z|$ is even (equivalently, $\iota(Z)$ below is even).

The last condition is automatic for configurations coming from orbifold pairs, since
$|U^*|+|V^*|\equiv|V^*|-|U^*|=2(g-g')$. Without it there are odd examples, e.g.
$\{-24,-18,-8,5,45\}$ has $s_1=s_{-1}=0$; they correspond to no orbifold pair.

Write $T=|Z|$ for its *size* and $\iota(Z)=\#\{z>0\}-\#\{z<0\}$ for its *imbalance*.

**Lemma 1.2 (dictionary).**

1. Configurations are invariant under $Z\mapsto\lambda Z$ for $\lambda\in\mathbb Q^\times$. This
   preserves $T$, and multiplies $\iota$ by $\operatorname{sgn}\lambda$.
2. Let $Z$ be an $L$-configuration scaled to primitive integers. Put $U=Z_{>0}$ and
   $V=-Z_{<0}$, and let $g-g'=-\iota/2$ with the smaller genus chosen least such that both are
   hyperbolic. Then $(g;U\setminus\{1\})$ and $(g';V\setminus\{1\})$ have equal area and
   distinct signatures, and they share at least $L$ heat coefficients. They share exactly $L$
   iff $s_{2L-1}(Z)\ne0$.
3. The pair is genus-changing iff $\iota\ne0$. If $\iota=0$, the pair has equal genus, and the
   cone counts differ iff $\pm1\in Z$ (a padding point).
4. $T$ is even and $T\ge2L+2$.
5. Area. If $\iota\ne0$, then $\operatorname{Area}<2\pi T$. If $\iota=0$ and the genus-0
   realisation is hyperbolic, then $\operatorname{Area}/2\pi=-2+\sum_{v\in V}(1-1/v)<T/2-2$.

````

### PS.1. Theorem 2.1 (Descartes bound)

Source: `theory/pte/proof.md` lines 141-147 (verbatim).

````
**Theorem 2.1 (Descartes bound).** Every $L$-configuration satisfies $|\iota(Z)|\le T-2L$. In
particular:

1. Two orbifolds of genera $g\ne g'$ sharing $L$ heat coefficients have
   $|U^*|+|V^*|\ge2L+2|g-g'|$.
2. A genus-changing configuration of size $2L+2$ has $\iota=\pm2$, i.e. shape
   $\{|U^*|,|V^*|\}=\{L,L+2\}$. An $L$-configuration of size $2L+2$ has $\iota\in\{0,\pm2\}$.
````

### PS.2. Proposition 2.2 (PTE lower bound)

Source: `theory/pte/proof.md` lines 174-175 (verbatim).

````
**Proposition 2.2 (PTE lower bound).** An $L$-configuration of size $T$ gives the PTE solution
$[Z]=_{2L-2}[-Z]$ of size $T$. Hence $\tau_L\ge N(2L-2)$.
````

### PS.3. Proposition 2.3 (symmetric constructions are balanced)

Source: `theory/pte/proof.md` lines 184-194 (verbatim).

````
**Proposition 2.3 (symmetric constructions are balanced).**

(a) Let $A$ be an *odd ideal symmetric* PTE solution in the sense of Borwein–Ingalls (p. 8):
$|A|=2L-1$, $s_j(A)=0$ for odd $j\le2L-3$, $0\notin A$, and no pair $\{a,-a\}$. Then
$s_{-1}(A)\ne0$ and $\iota(A)=\operatorname{sgn}s_{-1}(A)$.

(b) For two such sets $A,B$, let $\lambda=-s_{-1}(B)/s_{-1}(A)$, so that
$s_{-1}(A\uplus\lambda B)=s_{-1}(A)+s_{-1}(B)/\lambda=0$. Then $Z=A\uplus\lambda B$ is, after
cancellation, either empty or an $L$-configuration with $\iota(Z)=0$.

(c) The pencil configurations of Theorem 3.1 have $\iota=0$.
````

### PS.4. Theorem 3.1 (pencil)

Source: `theory/pte/proof.md` lines 223-233 (verbatim).

````
**Theorem 3.1 (pencil: ideal balanced configurations).** Let $m\ge4$, put $r=m-1$ and $k_0=m-2$
if $m$ is even, and $r=m$ and $k_0=m-3$ if $m$ is odd. Let $A\ne B$ be $m$-multisets of nonzero
rationals such that:

- $e_k(A)=e_k(B)=0$ for every odd $k<r$;
- $e_k(A)=e_k(B)$ for every $k\ne k_0$.

Equivalently, $\prod_A(x-a)-\prod_B(x-b)=\kappa\,x^{m-k_0}$, and $A,B$ are two full fibres of
the rational function $x\mapsto\prod_A(x-a)/x^{m-k_0}$. Then, if nonempty after cancellation,
$Z=A\uplus(-B)$ is an $(m-1)$-configuration of size $2m=2(m-1)+2$, the least possible, with
$\iota(Z)=0$.
````

### PS.5. Proposition 3.2 (shift)

Source: `theory/pte/proof.md` lines 267-274 (verbatim).

````
**Proposition 3.2 (shift).** Let $[X]=_k[Y]$ with $k\ge2L-3$, $|X|=|Y|=n$, and $X\cap Y=\emptyset$.
For $c\in\mathbb Q\setminus(-X\cup-Y)$ put $Z(c)=(X+c)\uplus(-(Y+c))$.

1. $s_j(Z(c))=0$ for odd $j\le2L-3$.
2. $\iota(Z(c))=2(\#\{x>-c\}-\#\{y>-c\})$. It is $0$ for $c>-\min(X\cup Y)$, and nonzero on
   some open interval of $c$.
3. $\rho(c):=s_{-1}(Z(c))=\sum_x\frac1{x+c}-\sum_y\frac1{y+c}$ is a nonzero rational function of
   $c$.
````

### PS.6. Manuscript-facing versions (statements.tex)

Source: `theory/pte/statements.tex` lines 13-37; `theory/pte/statements.tex` lines 47-53 (verbatim).

````
\subsection{How many coefficients: the Prouhet--Tarry--Escott connection}\label{subsec:pte}

By Lemma~\ref{lem:sigdata} and Theorem~\ref{thm:sigsep}, two orbifolds in $\Sig$ with different
signatures share their first $L$ heat coefficients exactly when the cancelled mirror multiset
$Z=U^*\uplus(-V^*)$ is an \emph{$L$-configuration}. This means a nonempty multiset of nonzero
rationals, of even size and with no pair $\{z,-z\}$, such that
\[
  \sum_{z\in Z}z^{j}=0\quad(j\ \text{odd},\ 1\le j\le 2L-3),\qquad \sum_{z\in Z}z^{-1}=0 .
\]
Its size is $|Z|=|U^*|+|V^*|$, and its imbalance is $\iota(Z)=\#\{z>0\}-\#\{z<0\}=2(g'-g)$.

Let $N(k)$ be the least size of a non-trivial solution of the Prouhet--Tarry--Escott problem
of degree $k$, i.e.\ two distinct multisets of $n$ integers with equal power sums of exponents
$1,\dots,k$ \cite[\S1]{borweiningalls1994}. One has $k+1\le N(k)\le\tfrac12k(k+1)+1$
\cite[Props.~2, 3]{borweiningalls1994}. No bound $N(k)=o(k^2)$ is known, and this is listed
as an open problem in \cite[\S6]{borweiningalls1994}.

\begin{theorem}[Shape of a genus collision]\label{thm:ptedescartes}
Every $L$-configuration satisfies $|\iota(Z)|\le|Z|-2L$. Hence, if orbifolds in $\Sig$ of genera
$g\neq g'$ share their first $L$ heat coefficients, then
\[
  |U^*|+|V^*|\ \ge\ 2L+2|g-g'| ,
\]
and equality $|U^*|+|V^*|=2L+2$ forces $\{|U^*|,|V^*|\}=\{L,L+2\}$.
\end{theorem}

\begin{proposition}[Symmetric constructions do not change the genus]\label{prop:ptebalanced}
Let $A$ be an odd ideal symmetric solution of size $2L-1$, i.e.\ $\sum_{a\in A}a^j=0$ for odd
$j\le2L-3$ \cite[p.~8]{borweiningalls1994}. Then
$\#\{a>0\}-\#\{a<0\}=\operatorname{sgn}\sum_{a\in A}a^{-1}$. Consequently, for two such sets
$A,B$, every $L$-configuration $A\uplus\lambda B$ ($\lambda\in\mathbb Q^\times$) has
$\iota=0$.
\end{proposition}
````
