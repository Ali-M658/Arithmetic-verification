# G5-bis audit: all statements under review

One section per reviewer group. The per-group files `statements/<group>.md` are what each reviewer receives.


---

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


---

# G5-bis audit: statements under review, group `pte-growth`

PTE growth: N_odd, the doubling, the upper bounds, the square-root lower bound, f(A) versus N(k)

Every result below is copied verbatim, by line range, from its source file (`review/audit-2/build_statements.py`
asserts the anchors and that no proof text is included). Items marked COMPOSED combine verbatim excerpts with
connective text in [square brackets]. **Proofs, scripts and data of the sessions that produced these results are
deliberately withheld.** You must not open any file of `theory/pte/`, `theory/revision/`, `theory/signatures/`
(other than where stated below), `review/referee-sim/` or `paper/` (the manuscript contains proofs of some of these
results). If you do open one by accident, say so in your REVIEW.md under 'contamination'.



## Context files you may read (previously audited statements, no proofs)

- review/audit/statements/signatures.md  (the previously audited results [Sig]: definitions DF.1; Corollary S2 and Theorem T1 give f(A) <= floor(A/pi)+4; SG.7, SG.8)

## External inputs

- [Sig] Corollary S2 / Theorem T1: f(A) <= floor(A/pi)+4 and the bound |U|+|V| <= 2 floor(A/pi)+8 (used for Theorem 4.2(a)). Previously audited; verify the use made of it.
- Borwein-Ingalls 1994, Props. 2, 3 (cited): N(k) >= k+1 and N(k) <= k(k+1)/2+1. Re-prove the upper bound yourself (pigeonhole) if you use it.
- Lemma 1.2 (PS.0 in pte-structure.md) and Proposition 3.2 (PS.5) are stated below by reference to the other group; they are NOT yours to audit, but you may assume them as stated, and must say so.

## Fetched sources

Texts fetched headlessly by `review/audit-2/fetch_sources.sh` are in `review/audit-2/sources/` (not committed).
Never quote a source from memory: quote the fetched text, with page or section. An unreachable source is an
instrument gap, to be logged, not a confirmation.


## Group: pte-growth

### PG.0. Definitions 1.3, 1.4, PTE notation and Lemma 1.5

Source: `theory/pte/proof.md` lines 99-124 (verbatim).

````
**Definition 1.3.** For $L\ge2$:

- $\tau_L$ is the least size of an $L$-configuration;
- $T_L$ is the least size with $\iota\ne0$ (the $T_L$ of [Sig] §7);
- $T^{\rm cone}_L$ is the least size of an $L$-configuration with $\iota=0$ whose primitive
  integral form contains $\pm1$ and whose genus-0 realisation is hyperbolic.

Then $2L+2\le\tau_L\le T_L$ and $\tau_L\le T^{\rm cone}_L$.

**PTE notation** (Borwein–Ingalls 1994, `sources/NOTES.md` §1).

- $[A]=_k[B]$ means equal power sums $P_j$ for $1\le j\le k$, for distinct multisets $A,B$ of
  integers of a common size $n$.
- $N(k)$ is the least such $n$.
- $N(k)\ge k+1$ (their Prop. 2), and $N(k)\le\frac12k(k+1)+1$ (their Prop. 3, by pigeonhole).
- $N$ is nondecreasing, because a solution of degree $k+1$ is one of degree $k$.

**Definition 1.4.** $N_{\rm odd}(L)$ is the least $n$ such that two distinct $n$-multisets of
*positive* integers have equal $P_j$ for every odd $j\le2L-3$.

**Lemma 1.5.**

1. $N_{\rm odd}(L)\le N(2L-3)$.
2. $N_{\rm odd}(L)\le(L-1)^2+1$.
3. $N_{\rm odd}(L)=L$ for $3\le L\le6$.

````

### PG.1. Proposition 3.3 (doubling)

Source: `theory/pte/proof.md` lines 283-293 (verbatim).

````
**Proposition 3.3 (doubling).** Let $X\ne Y$ be $n$-multisets of positive integers with equal
$P_j$ for odd $j\le2L-3$. Put
$$U=X\uplus2Y\uplus2Y,\qquad V=Y\uplus2X\uplus2X .$$
Then $Z=U\uplus(-V)$, after cancellation, is a balanced $L$-configuration of size $\le6n$.

- If $1\in X\setminus Y$, the pair $(0;U\setminus\{1\})$, $(0;V)$ consists of hyperbolic genus-0
  orbifolds whose cone counts differ by the multiplicity of $1$ in $X$. If $1\in Y\setminus X$,
  exchange the roles of $X$ and $Y$.
- If $1\notin X\cup Y$, the cone counts are equal.

In every case the area is $<2\pi(3n-2)$.
````

### PG.2. Theorem 3.4 (upper bounds)

Source: `theory/pte/proof.md` lines 311-314 (verbatim).

````
**Theorem 3.4 (upper bounds).** For every $L\ge2$:
$$\tau_L\le6N_{\rm odd}(L)\le6(L-1)^2+6,\qquad T_L\le4N(2L-3),\qquad T^{\rm cone}_L\le6N(2L-3).$$
With $N(2L-3)\le\frac12(2L-3)(2L-2)+1=2L^2-5L+4$, all three are $O(L^2)$. The previous bound
was $T_L\le2^{2L-1}$ ([Sig] N(a)).
````

### PG.3. Theorem 4.1 (square-root lower bound)

Source: `theory/pte/proof.md` lines 329-332 (verbatim).

````
**Theorem 4.1 (square-root lower bound).** For every $L\ge2$ there are two genus-0 hyperbolic
orbifolds with different signatures and area $<2\pi(3N_{\rm odd}(L)-2)\le2\pi(3(L-1)^2+1)$ that
share at least $L$ heat coefficients. Consequently, for $A\ge8\pi$,
$$f(A)\ \ge\ \Bigl\lfloor\sqrt{\tfrac13\bigl(\tfrac{A}{2\pi}-1\bigr)}\Bigr\rfloor+2 .$$
````

### PG.4. Theorem 4.2 (the exponent of f is a PTE exponent)

Source: `theory/pte/proof.md` lines 342-350 (verbatim).

````
**Theorem 4.2 (the exponent of $f$ is a PTE exponent).**

(a) If $f(A)\ge L+1$, then $N(2L-2)\le2\lfloor A/\pi\rfloor+8$.

(b) If $N(k)\le Ck^\beta$ for all $k\ge1$, then $f(A)\ge\frac12(A/6\pi C)^{1/\beta}$ for all
$A\ge8\pi$.

(c) For $0<\alpha\le1$: $f(A)\ge cA^\alpha$ for all large $A$ (some $c>0$) if and only if
$N(k)\le Ck^{1/\alpha}$ for all $k$ (some $C$). In particular $f(A)=\Theta(A)$ iff
````

### PG.5. Theorem 4.3 (genus alone, cone count alone)

Source: `theory/pte/proof.md` lines 380-390 (verbatim).

````
**Theorem 4.3 (genus alone, cone count alone).**

- Let $f_g(A)$ be the largest number of coefficients needed to determine the *genus* of an
  orbifold of area $\le A$, and $f_n(A)$ the analogous number for the *cone count* among
  genus-0 orbifolds.
- Then $f_g(A)\ge L+1$ whenever $A\ge8\pi N(2L-3)$, and $f_n(A)\ge L+1$ whenever
  $A\ge2\pi(3N(2L-3)-2)$. Both are therefore $\ge c\sqrt A$. Both are
  $\le\lfloor A/\pi\rfloor+4$ ([Sig] S2, T1).
- Theorem 4.2(c) holds verbatim for $f_g$ and for $f_n$. "⇐": by the two thresholds just
  stated. "⇒": a genus or cone-count collision is in particular a collision of signatures, so
  $f_g\le f$ and $f_n\le f$, and Theorem 4.2(a) applies.
````

### PG.6. Manuscript-facing version (statements.tex): Theorem (Growth) and Theorem (Descartes)

Source: `theory/pte/statements.tex` lines 55-70 (verbatim).

````
\begin{theorem}[Growth]\label{thm:ptegrowth}
Let $f(A)=\max\{\Kmult(\Orb;\Sig):\operatorname{Area}(\Orb)\le A\}$.
\begin{enumerate}[label=(\alph*)]
\item For $A\ge8\pi$,
  \[
    \Bigl\lfloor\sqrt{\tfrac13\bigl(\tfrac{A}{2\pi}-1\bigr)}\Bigr\rfloor+2\ \le\ f(A)\ \le\ \Bigl\lfloor\frac{A}{\pi}\Bigr\rfloor+4 .
  \]
\item If $f(A)\ge L+1$, then $N(2L-2)\le2\lfloor A/\pi\rfloor+8$.
\item For $0<\alpha\le1$: $f(A)\ge cA^{\alpha}$ for all large $A$ and some $c>0$ if and only if
  $N(k)\le Ck^{1/\alpha}$ for all $k$ and some $C$. In particular $f(A)=\Theta(A)$ if and only
  if $N(k)=O(k)$.
\end{enumerate}
The lower bound in (a) also holds, up to the constant, for the number of coefficients needed
to determine the genus alone, and for the number needed to determine the cone count alone
within genus $0$.
\end{theorem}
````


---

# G5-bis audit: statements under review, group `pte-witnesses`

PTE witnesses: the explicit pairs of section 5, the 61 pencil witnesses, the T_3 search claim

Every result below is copied verbatim, by line range, from its source file (`review/audit-2/build_statements.py`
asserts the anchors and that no proof text is included). Items marked COMPOSED combine verbatim excerpts with
connective text in [square brackets]. **Proofs, scripts and data of the sessions that produced these results are
deliberately withheld.** You must not open any file of `theory/pte/`, `theory/revision/`, `theory/signatures/`
(other than where stated below), `review/referee-sim/` or `paper/` (the manuscript contains proofs of some of these
results). If you do open one by accident, say so in your REVIEW.md under 'contamination'.



## Context files you may read (previously audited statements, no proofs)

- review/audit/statements/signatures.md  (definitions DF.1: signature and heat coefficients; Lemma 2, 4, Theorem S)
- review/audit/statements/audibility.md  (Theorem A, Theorem C(3): what 'integer sharpness' means; items AU.1)

## External inputs

- Heat coefficients: use the definition in signatures.md DF.1 with the cone polynomials of Proposition heatinput in trace-formula.md (b_l(m) = (-1)^l p_l(m)/m, p_l from the closed form), or re-derive them from Ucar (arXiv:1711.03405, (4.25),(4.33)). Compute 'the number of shared coefficients' from the coefficients themselves, not from the P_j criterion alone, and also check it against the criterion.
- Borwein-Ingalls/BLP/Chen/CMSV solutions are inputs only as numbers: re-verify every such number exactly before using it. Their provenance belongs to the literature group.

## Fetched sources

Texts fetched headlessly by `review/audit-2/fetch_sources.sh` are in `review/audit-2/sources/` (not committed).
Never quote a source from memory: quote the fetched text, with page or section. An unreachable source is an
instrument gap, to be logged, not a confirmation.


## Group: pte-witnesses

### PW.0. Headline table (proof.md section 0, items 5 and 6)

Source: `theory/pte/proof.md` lines 32-47 (verbatim).

````
5. **Explicit witnesses (§5).** Pairs sharing exactly $L$ coefficients, verified with the actual
   cone coefficients:

   | $L$ | least area found, any pair: Area$/2\pi$ | genus pair: $\lvert U^*\rvert+\lvert V^*\rvert$ | genus 0, cone counts $n$ vs $n'$ | Thue–Morse bound on Area$/2\pi$ |
   |---|---|---|---|---|
   | 2 | $1/4$ | 6 | 3 vs 4 | 3 |
   | 3 | $22/15$ | 10 | 7 vs 8 | 15 |
   | 4 | $\approx5.000$ | 16 | 11 vs 12 | 63 |
   | 5 | $\approx7.000$ | 20 | 22 vs 23 | 255 |
   | 6 | $\approx10.000$ | 26 | 29 vs 30 | 1023 |
   | 7 | $\approx18.000$ | 40 | 35 vs 36 | 4095 |

6. **$T_3$ (§6).** $T_3\in\{8,10\}$ is not decided. An exhaustive exact search excludes every
   size-8 genus collision whose 5-element side, made primitive, has entries $\le220$. The
   collision must have shape $(3,5)$ (Theorem 2.1). Real solutions of that shape exist in
   abundance, so the obstruction, if there is one, is arithmetic.
````

### PW.1. Example (Small pairs) and Remark (first open case), as in statements.tex

Source: `theory/pte/statements.tex` lines 101-120; `theory/pte/statements.tex` lines 122-127 (verbatim).

````
\begin{example}[Small pairs]\label{ex:ptepairs}
The following pairs share exactly $L$ heat coefficients (exact computation with the cone
coefficients):
\begin{itemize}
\item $L=3$, same genus and cone count: $(0;3,10,15,30)$ and $(0;4,5,21,28)$, of area
  $2\pi\cdot\frac{22}{15}$. Previously the smallest area known to share three coefficients was
  $2\pi\cdot\frac{14}5$, for $(1;15,15,15)$ and $(0;3,3,5,7,7,21)$.
\item $L=3$, genus $0$ with $7$ and $8$ cone points: $(0;4,4,5,5,6,12,12)$ and
  $(0;2,2,2,3,10,10,10,10)$, obtained from $[1,5,5]=[2,3,6]$ \cite{chen2025survey} by the doubling
  above. This replaces $103$ vs $104$.
\item $L=4,5,6,7$: genus-$0$ pairs with equal cone counts and area
  $<2\pi\cdot5,\,7,\,10,\,18$. They come from pairs of odd ideal symmetric solutions of sizes $7$
  and $9$ \cite{borweiningalls1994,blp2003}, from equal sums of odd powers
  \cite{chen2025survey}, and from the size-$12$ ideal solution \cite{cmsv2024}. The
  Prouhet--Thue--Morse pairs of Theorem~\ref{thm:signonuniform} need area up to
  $2\pi(4^{L-1}-1)$.
\item Genus $1$ versus genus $0$ sharing $L=4,5,6,7$ coefficients: configurations of size
  $16,20,26,40$, against $2^{2L-1}=128,512,2048,8192$ for Thue--Morse.
\end{itemize}
\end{example}

\begin{remark}[The first open case]\label{rem:ptet3}
By Theorem~\ref{thm:ptedescartes}, a genus collision sharing three coefficients with
$|U^*|+|V^*|=8$ must have shape $(3,5)$. An exhaustive exact search excludes all such collisions
whose five-element side, made primitive, has entries $\le220$. Real solutions of this shape
exist. So whether the least size is $8$ or $10$ remains open.
\end{remark}
````

### PW.2. Improved lower bounds on f in the covered range

Source: `theory/pte/proof.md` lines 457-470 (verbatim).

````
**Improved lower bounds on $f$ in the covered range.** Let $A_L$ be the least area in the
tables above among pairs sharing $L$ coefficients. Then $f(A)\ge L+1$ for $A\ge A_L$:

| $f(A)\ge$ | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| for $A/2\pi\ge$ (new) | $1/4$ | $22/15$ | $5.000$ | $7.000$ | $10.000$ | $18.000$ |
| for $A/2\pi\ge$ ([Sig] N1) | 3 | 15 | 63 | 255 | 1023 | 4095 |

The exact values of $A_L$ are in `data/witnesses.json`. The $\approx$ values lie just below
the integers shown, e.g. $A_4/2\pi=4.99999\ldots$, so "$\ge5.000$" is a safe rounding up.

Over this range the best pairs have Area$/2\pi\approx T/2-2$ with $T\le4L-2$ for $L\le5$. So
for $A/2\pi\le18$, $f$ grows at least linearly: $f(A)\ge L+1$ at
$A/2\pi\approx2L-3$ for $L\le5$.
````

### PW.3. Integer sharpness witnesses for Theorem A at n=4, and the n=5 claim

Source: `theory/pte/proof.md` lines 253-265 (verbatim).

````
*Instances.* For $m=4$ the hypothesis says that $A,B$ have $e_1=0$ and equal $e_3,e_4$.
`pencil_search.py` finds 25 distinct configurations from 4-sets with entries $\le130$, and 61
with entries $\le220$ (`data/pencil_log.txt`). These include 60 integer sharpness witnesses
for Theorem A at $n=4$ beyond the one recorded in `theory/audibility`. The smallest is
$A=\{-30,-3,5,28\}$, $B=\{-21,-4,10,15\}$, which gives
$\{3,10,15,30\}\sim\{4,5,21,28\}$. That is the $n=4$ witness of `theory/audibility/proof.md`
Theorem C(3) and Chen's type $(-1,1,3)$ entry A.685. So Theorem C(3) at $n=4$ is a pencil
phenomenon.

For $m=5$ the hypothesis asks for two odd symmetric 5-sets with equal $e_4,e_5$. Such a pair
would give a balanced 4-configuration of size 10, i.e. the integer sharpness of Theorem A at
$n=5$, which is open in `theory/audibility`. Among all 1,592 primitive 5-sets with entries
$\le200$, no such pair exists.
````

### PW.4. The 18 claimed pairs (generated; recipes and Z omitted)

Source: generated (witnesses) (verbatim).

Each entry is a claim: the two orbifolds below are closed orientable hyperbolic 2-orbifolds of the signature shown (cone orders; 'g' genus), they have equal area, distinct signatures, and they share EXACTLY L heat coefficients (the first L coefficients agree, the (L+1)-st differs). 'T' is the claimed size of the cancelled configuration Z = U* + (-V*), 'cone counts' the numbers of cone points (1s removed). The claimed exact area/2pi is given.

**W00** kind=genus, L=2, claimed shares exactly 2, T=6, iota=2, cone counts 4 vs 1, Area/2pi = 14/15
- O  = (g=0; 3, 3, 5, 5)
- O' = (g=1; 15)

**W01** kind=genus, L=3, claimed shares exactly 3, T=10, iota=2, cone counts 6 vs 3, Area/2pi = 14/5
- O  = (g=0; 3, 3, 5, 7, 7, 21)
- O' = (g=1; 15, 15, 15)

**W02** kind=genus, L=4, claimed shares exactly 4, T=16, iota=2, cone counts 9 vs 7, Area/2pi = 41149074301/5878522650
- O  = (g=0; 34986, 38775, 58310, 116325, 128282, 271425, 271425, 454818, 524790)
- O' = (g=1; 12925, 168025, 219725, 268226, 297275, 384846, 548114)

**W03** kind=genus, L=5, claimed shares exactly 5, T=20, iota=2, cone counts 11 vs 9, Area/2pi = 112658971081054/12517666291845
- O  = (g=0; 1517814, 2063997, 2522663, 7589070, 9861319, 10319985, 12613315, 19731582, 59194746, 77408514, 89551026)
- O' = (g=1; 687999, 4357327, 8485321, 11695983, 12154649, 34909722, 50087862, 83479770, 86515398)

**W04** kind=genus, L=6, claimed shares exactly 6, T=26, iota=2, cone counts 14 vs 12, Area/2pi = 8011672951610749084518529918806713747318107765849227714286789/667639412634229090376544159900603145300498646924203622400000
- O  = (g=0; 4093411365093597322848394806575, 7271375040829745152760217600000, 9824187276224633574836147535780, 9987923730828377467750083328043, 14793487152032929793546649600000, 48392254582073821189059379200000, 52886874837009277411201260900949, 61237434021800215949811986306362, 61932056382239553542474956800000, 77283606572967117455377693948136, 77979228886139680776152678400000, 78480703026886559752205107200000, 84160537666324360957762997223182, 90218786486662884995578621536913)
- O' = (g=1; 1755159492614076416183500800000, 22817073403982993410385510400000, 33074763829956266368615030037126, 37986857468068583156033103805016, 43377513174605031428535091200000, 67448271930455222279051673600000, 70079202570402386167164519088564, 72463013337924012039575961600000, 76137451390740910204980143402295, 80988073730620954632467251200000, 81049545028853226992398217170185, 91364941668889092245976172082754)

**W05** kind=genus, L=7, claimed shares exactly 7, T=40, iota=2, cone counts 21 vs 19, Area/2pi = 159016325127586219276587050363723886153380991692916838678380792473971519/8369280269872958909294055282301257170650883098593549936154305804369920
- O  = (g=0; 495461702484924819341859189302493184, 683624372840614274768382863229231445, 771998466662557276648943387982954496, 818087927358829352866790754429698048, 1093798996544982839629412581166770312, 1716832410936134839114814400141197312, 1855100793024951067768356499481427968, 2292950669639535791837906480725491712, 2734497491362457099073531452916925780, 3053426771128025049432388027096760320, 3237784613913113354303777492883734528, 3537366108438881849719785374787567616, 3790858142268378268917945890244657152, 6699518853838019892730152059646468161, 9160566596064231281896330367271701363, 12031788961994811235923538392834473432, 12852138209403548365645597828709551166, 16270260073606619739487512144855708391, 21055630683490919662866192187460328506, 22833054052876516777263987631856330263, 24337027673125868181754429930960639442)
- O' = (g=1; 195880207959156323925851307398660096, 1094624691536461810173874953110159360, 1117669421884597848282798636333531136, 1394206186062230305589882835013992448, 1670742950239862762896967033694453760, 2615576894513440325362838045852696576, 2915158389039208820778845927756529664, 3168650422868705239977006443213619200, 3675634490527698078373327474127798272, 3721723951223970154591174840574541824, 4648645735316177068425003469958773826, 8066767599519248442266917786104931051, 8476942223223617007127947504042469918, 10117640718041091266572066375792625386, 13672487456812285495367657264584628900, 16953884446447234014255895008084939836, 20235281436082182533144132751585250772, 23653403300285253906986047067731407997, 23926853049421499616893400213023100575)

**W06** kind=balanced, L=2, claimed shares exactly 2, T=6, iota=0, cone counts 3 vs 3, Area/2pi = 1/4
- O  = (g=0; 3, 3, 12)
- O' = (g=0; 2, 8, 8)

**W07** kind=balanced, L=3, claimed shares exactly 3, T=8, iota=0, cone counts 4 vs 4, Area/2pi = 22/15
- O  = (g=0; 3, 10, 15, 30)
- O' = (g=0; 4, 5, 21, 28)

**W08** kind=balanced, L=4, claimed shares exactly 4, T=14, iota=0, cone counts 7 vs 7, Area/2pi = 118766555393933327671589/23753311078941951481650
- O  = (g=0; 74493387367, 138344862253, 217482072530, 404392674278, 532095624050, 600937305675, 703955129505)
- O' = (g=0; 74401761655, 131633886005, 255405899544, 351183111873, 542737536531, 629553367850, 686785492200)

**W09** kind=balanced, L=5, claimed shares exactly 5, T=18, iota=0, cone counts 9 vs 9, Area/2pi = 812564706402847786089918000749235251/116080672343263975087481791511661200
- O  = (g=0; 5806604053259408, 20770022346082906, 35431214590376722, 36291275332871300, 50092406834670538, 59866534997533082, 95808966878780232, 107422174985299048, 126293638158392124)
- O' = (g=0; 7941479132325817, 9774128162862544, 42150927702344721, 45727006919417838, 45816225763418175, 60477418007711991, 86373235292233694, 116857906571845586, 122664510625104994)

**W10** kind=balanced, L=6, claimed shares exactly 6, T=24, iota=0, cone counts 12 vs 12, Area/2pi = 12395899856021215350087167375045579535671/1239589985602121535014046594388561899975
- O  = (g=0; 71623872894939389150, 129265225362823216755, 138389829506081326173, 430377162090340827549, 436460231519179567161, 507595273125005236150, 563648738868870845050, 612869244955503015909, 701073751673664740283, 1061901767703231813050, 1080586256284520349350, 1267431142097405712350)
- O' = (g=0; 65392996360016450829, 115221012917945973850, 244843544510759269383, 330006516514501623951, 370575690195555969950, 509457064665244442505, 594620036668986797073, 688211996077461087050, 704115286388084110089, 968479324796789131550, 1155324210609674494550, 1254974816376546688150)

**W11** kind=balanced, L=7, claimed shares exactly 7, T=40, iota=0, cone counts 20 vs 20, Area/2pi = 14301019323811636282516882693657383028577480873602071293040986507111198588933404629842516/794501073545090904584271260758743501587638079375203534302390704062617122289416027087675
- O  = (g=0; 595958629909279070099829518275115563729823, 1030537353727106401413686917679685652027815, 1605720993016654160342256360105556713624735, 1701584932898245453497017933843201890557555, 3570931760589275670014868621727282840747545, 3858523580234049549479153342940218371546005, 4769231009109166834449388293447847552407795, 6350986017155423171502954260118992971799325, 6734441776681788344122000555069573679530605, 7236640506041245851212215579054974702433565, 7357557385912131749627950784364267329593935, 7884809055260883861979139439921315802724445, 9620475025678362131611533652155436957352857, 13877322382173212632324601639834833841137307, 14217870170692800672381647078849185591840063, 21369373729604149513579601298150572356597939, 25626221086099000014292669285829969240382389, 32607450750750554835462100785624180129788887, 34821011376127877095832896139217466509356801, 36694024212985611316146646053796401138221959)
- O' = (g=0; 407421744496762995907736688384992001964485, 2276768572187793212425587376269072952154475, 2324700542128588859002968163137895540620885, 2899884181418136617931537605563766602217805, 2979793149546395350499147591375577818649115, 3475067820707684376860107047989637663814725, 3660888726585571430613238469404281320054627, 5440278588280305886532719309611363790937535, 6063394197510649292038669538906057441000865, 6590645866859401404389858194463105914131375, 7645149205556905629092235505577202860392395, 7741013145438496922246997079314848037325215, 10642118391237126251782669969198492209461125, 12855679016614448512153465322791778589029039, 16942252478849504992838010590963999597462111, 18985539209967033233180283225050110101678647, 26988412240177352174520851041887376243193413, 31585807385191790715290964468581124877680619, 35842654741686641216004032456260521761465069, 36183202530206229256061077895274873512167825)

**W12** kind=cone, L=2, claimed shares exactly 2, T=8, iota=0, cone counts 4 vs 3, Area/2pi = 2/5
- O  = (g=0; 2, 2, 2, 10)
- O' = (g=0; 5, 5, 5)

**W13** kind=cone, L=3, claimed shares exactly 3, T=16, iota=0, cone counts 7 vs 8, Area/2pi = 113/30
- O  = (g=0; 4, 4, 5, 5, 6, 12, 12)
- O' = (g=0; 2, 2, 2, 3, 10, 10, 10, 10)

**W14** kind=cone, L=4, claimed shares exactly 4, T=24, iota=0, cone counts 12 vs 11, Area/2pi = 2651846/320229
- O  = (g=0; 2, 2, 3, 9, 21, 21, 26, 26, 34, 34, 46, 46)
- O' = (g=0; 6, 6, 13, 17, 18, 18, 23, 42, 42, 42, 42)

**W15** kind=cone, L=5, claimed shares exactly 5, T=46, iota=0, cone counts 23 vs 22, Area/2pi = 564239482/30342025
- O  = (g=0; 2, 2, 2, 3, 10, 12, 20, 20, 21, 31, 40, 48, 48, 49, 50, 56, 56, 84, 84, 94, 94, 102, 102)
- O' = (g=0; 4, 4, 5, 6, 6, 24, 24, 24, 28, 42, 42, 42, 47, 51, 62, 62, 80, 80, 98, 98, 100, 100)

**W16** kind=cone, L=6, claimed shares exactly 6, T=60, iota=0, cone counts 30 vs 29, Area/2pi = 49020849382437764968683088/1845726112877621686996185
- O  = (g=0; 2, 2, 6, 7, 26, 26, 134, 183, 243, 252, 252, 385, 428, 428, 430, 430, 445, 494, 621, 622, 826, 826, 828, 828, 1004, 1004, 1230, 1230, 1254, 1254)
- O' = (g=0; 12, 12, 13, 14, 14, 126, 214, 215, 268, 268, 366, 366, 413, 414, 486, 486, 502, 615, 627, 770, 770, 890, 890, 988, 988, 1242, 1242, 1244, 1244)

**W17** kind=cone, L=7, claimed shares exactly 7, T=72, iota=0, cone counts 36 vs 35, Area/2pi = 70773805781898091109456/2190539016013095022275
- O  = (g=0; 2, 2, 4, 6, 24, 24, 31, 50, 50, 58, 105, 117, 132, 132, 182, 182, 187, 199, 246, 260, 260, 273, 298, 300, 348, 348, 426, 426, 476, 476, 558, 558, 584, 584, 606, 606)
- O' = (g=0; 8, 8, 12, 12, 12, 25, 62, 62, 66, 91, 116, 116, 130, 174, 210, 210, 213, 234, 234, 238, 279, 292, 303, 374, 374, 398, 398, 492, 492, 546, 546, 596, 596, 600, 600)


### PW.5. The 61 claimed pencil configurations (generated)

Source: generated (pencil61) (verbatim).

Claim (n = 4 integer sharpness of Theorem A; see Theorem C(3) in audibility.md AU.1). Below are 61 integer 8-element multisets Z. The claim is that each Z has: no pair {z,-z}; sum z^j = 0 for j = 1, 3 and j = -1; exactly four positive and four negative entries (imbalance 0); so m = positive part and m' = (-negative part) are two DISTINCT 4-multisets of positive integers with equal R = sum 1/m_i, P_1 and P_3, i.e. two orbifolds of genus 0 with four cone points sharing I_3 = (R, P_1, P_3); the 61 are pairwise distinct modulo Z -> lambda Z (lambda rational) and Z -> -Z (which swaps m, m'); and they are ALL the configurations produced as follows: A, B primitive integer 4-sets {a,b,c,-(a+b+c)} with all entries of absolute value <= 220, A and B with equal e_3^4/e_4^3 (e_k elementary symmetric), B scaled by the rational lambda with e_3(lambda B) = e_3(A), e_4(lambda B) = e_4(A), lambda B != A as multisets, then Z = A + (-lambda B) after cancelling, scaled to primitive integers. (The first claim is checkable on the list; the 'all' claim needs your own enumeration.)

```
[-28, -21, -5, -4, 3, 10, 15, 30]
[-72, -56, -10, -9, 7, 15, 50, 75]
[-75, -50, -15, -12, 10, 21, 44, 77]
[-72, -56, -12, -9, 7, 21, 44, 77]
[-77, -44, -21, -13, 12, 26, 39, 78]
[-75, -50, -15, -13, 10, 26, 39, 78]
[-72, -56, -13, -9, 7, 26, 39, 78]
[-77, -63, -18, -14, 11, 33, 44, 84]
[-91, -78, -14, -7, 6, 22, 63, 99]
[-99, -63, -22, -15, 14, 25, 60, 100]
[-91, -78, -15, -7, 6, 25, 60, 100]
[-100, -60, -25, -17, 15, 34, 51, 102]
[-99, -63, -22, -17, 14, 34, 51, 102]
[-91, -78, -17, -7, 6, 34, 51, 102]
[-130, -117, -65, -45, 42, 84, 91, 140]
[-140, -105, -20, -18, 15, 26, 99, 143]
[-126, -117, -39, -26, 22, 66, 77, 143]
[-143, -99, -26, -25, 18, 50, 75, 150]
[-153, -136, -11, -9, 8, 13, 132, 156]
[-143, -130, -22, -13, 10, 55, 78, 165]
[-156, -132, -29, -13, 11, 58, 87, 174]
[-153, -136, -29, -9, 8, 58, 87, 174]
[-174, -87, -58, -30, 29, 70, 75, 175]
[-156, -132, -30, -13, 11, 70, 75, 175]
[-153, -136, -30, -9, 8, 70, 75, 175]
[-187, -102, -28, -21, 16, 64, 66, 192]
[-182, -140, -42, -13, 12, 65, 105, 195]
[-175, -165, -33, -11, 10, 50, 126, 198]
[-195, -130, -39, -35, 26, 84, 85, 204]
[-209, -152, -33, -25, 24, 35, 150, 210]
[-210, -150, -36, -35, 25, 68, 117, 221]
[-209, -152, -36, -33, 24, 68, 117, 221]
[-221, -117, -68, -37, 36, 74, 111, 222]
[-210, -150, -37, -35, 25, 74, 111, 222]
[-209, -152, -37, -33, 24, 74, 111, 222]
[-208, -156, -42, -26, 21, 91, 96, 224]
[-198, -189, -54, -32, 28, 77, 144, 224]
[-220, -120, -8, -4, 3, 25, 99, 225]
[-224, -144, -21, -18, 14, 32, 133, 228]
[-225, -180, -33, -25, 20, 51, 154, 238]
[-238, -154, -51, -41, 33, 82, 123, 246]
[-225, -180, -41, -25, 20, 82, 123, 246]
[-246, -123, -82, -42, 41, 91, 114, 247]
[-238, -154, -51, -42, 33, 91, 114, 247]
[-225, -180, -42, -25, 20, 91, 114, 247]
[-231, -210, -34, -11, 10, 51, 170, 255]
[-255, -170, -51, -39, 34, 65, 156, 260]
[-231, -210, -39, -11, 10, 65, 156, 260]
[-260, -156, -65, -45, 39, 95, 126, 266]
[-255, -170, -51, -45, 34, 95, 126, 266]
[-231, -210, -45, -11, 10, 95, 126, 266]
[-270, -108, -27, -15, 12, 65, 70, 273]
[-304, -208, -57, -50, 39, 90, 175, 315]
[-315, -175, -90, -53, 50, 106, 159, 318]
[-304, -208, -57, -53, 39, 106, 159, 318]
[-340, -204, -85, -56, 51, 105, 184, 345]
[-342, -176, -22, -19, 12, 96, 99, 352]
[-366, -183, -122, -63, 61, 144, 161, 368]
[-390, -195, -130, -66, 65, 138, 187, 391]
[-385, -220, -105, -66, 60, 138, 187, 391]
[-438, -219, -146, -75, 73, 165, 200, 440]
```

Further claim: with m = 5 (odd symmetric 5-sets {e_1 = e_3 = 0}, primitive, entries <= 200; there are 1,592 of them), no two have equal e_4^5/e_5^4 giving a pencil pair, i.e. no integer sharpness witness of Theorem A at n = 5 arises this way.


---

# G5-bis audit: statements under review, group `trace-formula`

Trace formula: the closed form of the elliptic weight, Lemma 2.5 for every order, agreement with Ucar, Remark 4.12, the constant of Theorem 1.2(iii)

Every result below is copied verbatim, by line range, from its source file (`review/audit-2/build_statements.py`
asserts the anchors and that no proof text is included). Items marked COMPOSED combine verbatim excerpts with
connective text in [square brackets]. **Proofs, scripts and data of the sessions that produced these results are
deliberately withheld.** You must not open any file of `theory/pte/`, `theory/revision/`, `theory/signatures/`
(other than where stated below), `review/referee-sim/` or `paper/` (the manuscript contains proofs of some of these
results). If you do open one by accident, say so in your REVIEW.md under 'contamination'.



## Context files you may read (previously audited statements, no proofs)

- review/audit/statements/locality.md  (LO.6 Theorem 3.1 = the integrated trace formula with elliptic terms, LO.7, LO.8 admissibility and counting; DF.1 definitions of the heat coefficients and signature). These are previously audited; a result below may use them as stated. Hypotheses of the trace formula are an external input: read Dryden-Strohmaier eq. (1) in the fetched text.

## External inputs

- Selberg trace formula for cocompact Fuchsian groups with elliptic elements, in the form of Dryden-Strohmaier arXiv:math/0504571 eq. (1) (fetched: sources/ds_math0504571.txt).
- Ucar, arXiv:1711.03405, (4.25), (4.33)-(4.35) (fetched: sources/ucar_1711.03405.txt).
- Dryden-Gordon-Greenwald-Webb arXiv:0805.3148, Thm 4.8, section 5.6 (fetched: sources/dggw_0805.3148.txt). Schueth arXiv:1812.06119, Rem. 4.2, Thm 4.1 (fetched: sources/schueth_1812.06119.txt).
- Classical analysis only otherwise: Euler's beta integral, Bernoulli numbers, Liouville's theorem.

## Fetched sources

Texts fetched headlessly by `review/audit-2/fetch_sources.sh` are in `review/audit-2/sources/` (not committed).
Never quote a source from memory: quote the fetched text, with page or section. An unreachable source is an
instrument gap, to be logged, not a confirmation.


## Group: trace-formula

### TF.1. Notation for the elliptic moments, and Lemma (Elliptic moments)

Source: `theory/revision/lemma25.tex` lines 16-26; `theory/revision/lemma25.tex` lines 28-39 (verbatim).

````
\subsection{The expansion}\label{sec:heatexp}

The structure of the expansion is due to Donnelly and to Dryden, Gordon, Greenwald and Webb
\cite{donnelly1976,dggw2008}, and U\c{c}ar computed every coefficient at constant curvature
\cite{ucar2017}. We derive the coefficients again from the trace formula of
Theorem~\ref{thm:IEH}, which gives them in closed form for every order. For $0<a<2\pi$ put
\[
  F_a(r)=\frac{e^{-ar}}{1+e^{-2\pi r}},\qquad \mu_n(a)=\int_\R r^nF_a(r)\,dr ,
\]
so that $F_a(r)\le e^{-ar}$ for $r\ge0$ and $F_a(r)\le e^{(2\pi-a)r}$ for $r\le0$, and every
$\mu_n(a)$ is finite.

\begin{lemma}[Elliptic moments]\label{lem:ellmoments}
Let $0<a<2\pi$.
\begin{enumerate}[label=(\roman*)]
\item For $a-2\pi<s<a$, $\displaystyle\int_\R F_a(r)\,e^{sr}\,dr=\frac1{2\sin((a-s)/2)}$; hence
  $\mu_n(a)=\frac{d^n}{ds^n}\big[2\sin((a-s)/2)\big]^{-1}\big|_{s=0}$.
\item For every $K\ge1$ and $t>0$,
  \[
    \Big|\int_\R F_a(r)\,e^{-tr^2}\,dr-\sum_{k=0}^{K-1}\frac{(-t)^k}{k!}\,\mu_{2k}(a)\Big|
    \le\frac{t^K}{K!}\,\mu_{2K}(a).
  \]
\end{enumerate}
\end{lemma}
````

### TF.2. Definition of Phi_m and Lemma (Closed form)

Source: `theory/revision/lemma25.tex` lines 50-55; `theory/revision/lemma25.tex` lines 57-67 (verbatim).

````
Write $\theta_j=\pi j/m$ and, for an integer $m\ge1$,
\[
  \Phi_m(u)=\sum_{j=1}^{m-1}\frac1{4m\,\sin\theta_j\,\sin(\theta_j-u)} .
\]
Each term is analytic in $|u|<\pi/m$, so $\Phi_m$ is analytic there; $\Phi_1=0$, and
$\Phi_m(-u)=\Phi_m(u)$ (replace $j$ by $m-j$).

\begin{lemma}[Closed form]\label{lem:Phi}
For $m\ge1$ and $0<|u|<\pi/m$,
\begin{equation}\label{eq:Phi}
  \Phi_m(u)=\frac{\cot u-m\cot(mu)}{4m\sin u}.
\end{equation}
Write $u/\sin u=\sum_{i\ge0}\sigma_iu^{2i}$, so $\sigma_i\in\Q$, $\sigma_0=1$ and in fact $\sigma_i>0$.
Then $\Phi_m(u)=\sum_{k\ge0}\phi_k(m)\,u^{2k}$ with
\begin{equation}\label{eq:phik}
  m\,\phi_k(m)=\frac14\sum_{n=1}^{k+1}\sigma_{k+1-n}\,\frac{4^n|B_{2n}|}{(2n)!}\,\big(m^{2n}-1\big).
\end{equation}
\end{lemma}
````

### TF.3. Lemma (The hyperbolic term is small)

Source: `theory/revision/lemma25.tex` lines 87-93 (verbatim).

````
\begin{lemma}[The hyperbolic term is small]\label{lem:hypbound}
Let $\Orb\in\Sig$ have area $A$, systole $\ell$ and diameter $D$. For $0<t\le\ell^2/(2(1+\ell))$,
\[
  0\le\Hyp(t)\le\frac{\pi e^{3D}}{A(1-e^{-\ell})}\;\ell e^{\ell/2}\Big(1+\frac{2t}{\ell-t}\Big)\frac{e^{-\ell^2/4t}}{\sqrt{4\pi t}} .
\]
In particular $\Hyp(t)=O(t^N)$ as $t\downarrow0$ for every $N$.
\end{lemma}
````

### TF.4. Proposition (The heat expansion at curvature -1)

Source: `theory/revision/lemma25.tex` lines 101-119 (verbatim).

````
\begin{proposition}[The heat expansion at curvature $-1$]\label{prop:heatinput}
Let $\Orb\in\Sig$ have signature $(g;m_1,\dots,m_n)$. As $t\downarrow0$,
\[
  \cZ_\Orb(t)\ \sim\ \frac{\Area(\Orb)}{4\pi t}\sum_{k\ge0}\alpha_kt^k\;+\;\sum_{i=1}^n\sum_{l\ge0}b_l(m_i)\,t^l,
\]
where
\begin{equation}\label{eq:alphak}
  \alpha_k=\frac{(-1)^k}{k!\,4^k}\sum_{l=0}^k\binom kl(-4)^lB_{2l}\big(\tfrac12\big)
\end{equation}
and, for every integer $m\ge1$,
\begin{equation}\label{eq:bl}
  b_l(m)=\frac{(-1)^l\,p_l(m)}{m},\qquad
  p_l(m)=\frac1{4^l}\sum_{k=0}^{l}\frac{(2k)!}{k!\,(l-k)!}\;m\,\phi_k(m).
\end{equation}
Consequently $c_1=\Area(\Orb)/4\pi$ and, for $j\ge2$,
\begin{equation}\label{eq:cj}
  c_j(\Orb)=\alpha_{j-1}\,\frac{\Area(\Orb)}{4\pi}+\sum_{i=1}^nb_{j-2}(m_i).
\end{equation}
\end{proposition}
````

### TF.5. Lemma (Cone polynomials) = Lemma 2.5, and the printed first values

Source: `theory/revision/lemma25.tex` lines 145-152; `theory/revision/lemma25.tex` lines 166-173 (verbatim).

````
\begin{lemma}[Cone polynomials]\label{lem:conepoly}
For every $l\ge0$, $p_l$ is an even polynomial with rational coefficients, of degree exactly
$2l+2$, with $p_l(1)=0$ and leading coefficient
\[
  \frac{|B_{2l+2}|}{2\,(l+1)!\,(2l+1)}\ne0 .
\]
Moreover $p_l(m)>0$ for every real $m>1$.
\end{lemma}

The first values are $\alpha_0,\dots,\alpha_4=1,-\tfrac13,\tfrac1{15},-\tfrac4{315},\tfrac1{315}$, and
\begin{equation}\label{eq:plexplicit}
  p_0(m)=\frac{m^2-1}{12},\qquad p_1(m)=\frac{m^4}{360}+\frac{m^2}{36}-\frac{11}{360},\qquad p_2(m)=\frac{m^6}{2520}+\frac{m^4}{720}+\frac{m^2}{180}-\frac{37}{5040}.
\end{equation}
The polynomials $p_1,p_2$ agree with the cone coefficients of Schueth \cite[Rem.~4.2, Thm~4.1]{schueth2019},
which she attributes to \cite[\S5.6]{dggw2008} at order $t^1$.
The value $p_l(1)=0$ has a direct meaning: an ``order-$1$ cone point'' is a smooth point, and the sum
defining $\Phi_1$ is empty.
````

### TF.6. Remark (Agreement with Ucar), the claim

Source: `theory/revision/lemma25.tex` lines 175-175; `theory/revision/lemma25.tex` lines 179-187 (verbatim).

````
\begin{remark}[Agreement with U\c{c}ar]\label{rem:ucaragree}

[derivation of the identity m t^2 Phi_m(it/2) = ... omitted]

where, by \cite[(4.25)]{ucar2017},
\[
  c^{\mathbb S}_k\Big(\frac\pi m\Big)=\frac1{4m}\cdot\frac{(-1)^k}{(k+1)!\,(2k+1)}\sum_{j=0}^{k+1}\binom{2k+2}{2j}\big(m^{2j}-1\big)B_{2j}\,B_{2k+2-2j}\big(\tfrac12\big).
\]
Then \eqref{eq:bl} becomes $p_l(m)/m=\sum_{i\le l}2(4^ii!)^{-1}c^{\mathbb S}_{l-i}(\pi/m)$, which is $(-1)^l$
times U\c{c}ar's cone contribution \cite[(4.33)--(4.34)]{ucar2017} at $K=-1$. So the cone terms of
Proposition~\ref{prop:heatinput} are U\c{c}ar's for every $l$; his smooth coefficients
\cite[(4.35)]{ucar2017} are given by the same formula as \eqref{eq:alphak}. The two were also compared in
exact arithmetic for $l\le40$ (code in the archived repository, Appendix~\ref{app:reproducibility}).
````

### TF.7. Remark 4.12 (the trace-formula proof of locality): the independence claim, versions 2A and 2B and the replacement sentence

Source: `theory/revision/remark412.tex` lines 17-20; `theory/revision/remark412.tex` lines 22-25; `theory/revision/remark412.tex` lines 32-45; `theory/revision/remark412.tex` lines 49-61 (verbatim).

````
No local invariant can see the moduli: any two hyperbolic orbifolds of the same signature are
locally isometric, point by point and cone point by cone point. The trace formula of
Theorem~\ref{thm:IEH} gives a second, independent proof, with the coefficients
(Remark~\ref{rem:proofC}).

% (1A) if lemma25.tex is adopted (version 2A), where the trace formula is the primary proof:
%   "No local invariant can see the moduli: any two hyperbolic orbifolds of the same signature
%    are locally isometric, point by point and cone point by cone point; this structural reading,
%    through the locality of the heat invariants \cite{donnelly1976,dggw2008}, is a second proof.

\begin{remark}[The trace-formula proof of locality]\label{rem:proofC}
Theorem~\ref{thm:IEH} proves Theorem~\ref{thm:locality} directly: $\mathrm I$ depends only on the
area and $\mathrm E$ only on the cone orders, and $0\le\Hyp(t)=O(t^{-1/2}e^{-\ell^2/4t})=O(t^N)$ for
every $N$ (Lemma~\ref{lem:hypbound}), so the asymptotic series of $\cZ_\Orb$ is that of
$\mathrm I+\mathrm E$. This is how Proposition~\ref{prop:heatinput} and Lemma~\ref{lem:conepoly} were
proved, and it is independent of the coefficient computations of \cite{dggw2008} and
\cite{ucar2017}. The only input from the heat-kernel literature is the a-priori bound
$\#\{\lambda_j\le x\}\le e\,\cZ_\Orb(1/x)=O(x)$ in the proof of Lemma~\ref{lem:admissible}, which uses
only the a-priori bound $\cZ_\Orb(s)=O(1/s)$ as $s\downarrow0$, a consequence of \cite[Thm~4.8]{dggw2008}
(or of Weyl's law). It determines no coefficient $c_j$ with $j\ge2$, so nothing is circular. U\c{c}ar's
cone terms \cite[(4.25), (4.33)--(4.34)]{ucar2017} agree with Proposition~\ref{prop:heatinput} for every
order (Remark~\ref{rem:ucaragree}), and his smooth coefficients \cite[(4.35)]{ucar2017} are given by
the same formula as \eqref{eq:alphak}.
\end{remark}

\begin{remark}[The trace-formula proof of locality]\label{rem:proofC}
Theorem~\ref{thm:IEH} gives an independent proof of Theorem~\ref{thm:locality}: $\mathrm I$ and
$\mathrm E$ depend only on the signature, and $0\le\Hyp(t)=O(t^{-1/2}e^{-\ell^2/4t})=O(t^N)$ for every
$N$, so the asymptotic series of $\cZ_\Orb$ is that of $\mathrm I+\mathrm E$. Expanding
$e^{-tr^2}$ under the integrals, with the moments
$\int_0^\infty r^{2k+1}(e^{2\pi r}+1)^{-1}dr=(1-2^{-2k-1})(-1)^kB_{2k+2}/(4(k+1))$ and
$\int_\R e^{-ar}(1+e^{-2\pi r})^{-1}e^{sr}dr=1/(2\sin((a-s)/2))$, reproduces the constants $\alpha_k$
and $b_l(m)$ of Proposition~\ref{prop:heatinput} for every order. This route does not use the
coefficient computations of \cite{dggw2008} or \cite{ucar2017}. Its only input from the
heat-kernel literature is the a-priori bound $\#\{\lambda_j\le x\}\le e\,\cZ_\Orb(1/x)=O(x)$ in
Lemma~\ref{lem:admissible}, which uses only $\cZ_\Orb(s)=O(1/s)$, a consequence of
\cite[Thm~4.8]{dggw2008} (or of Weyl's law), and determines no $c_j$ with $j\ge2$.
\end{remark}
````

### TF.8. Theorem 1.2(iii): the constant and the 'attained' statement; Theorem 4.9(b) form

Source: `theory/revision/thm12iii.tex` lines 10-23; `theory/revision/thm12iii.tex` lines 31-36 (verbatim).

````
\item Let $\Orb_1,\Orb_2$ have the same signature and area $A$, let $\ell$ be the smaller of their
systoles and $D$ the larger of their diameters. For $0<t\le\ell^2/(2(1+\ell))$,
\[
  |\cZ_{\Orb_1}(t)-\cZ_{\Orb_2}(t)|\le C(A,\ell,D)\,t^{-1/2}e^{-\ell^2/4t},\qquad
  C(A,\ell,D)=\frac{\sqrt\pi\,e^{3D}\,\ell\,e^{\ell/2}\,(2+3\ell)}{2A\,(1-e^{-\ell})\,(2+\ell)} .
\]
The constant depends on the diameter, which the signature does not determine. If the two length
spectra, counted with the weights $\ell(\gamma_0)$, first differ at the length $\ell$ (in particular,
if the two systoles differ), then $\sqrt t\,e^{\ell^2/4t}|\cZ_{\Orb_1}(t)-\cZ_{\Orb_2}(t)|$ has a
nonzero limit as $t\downarrow0$: the exponent $\ell^2/4$ and the factor $t^{-1/2}$ are attained,
the constant $C$ is not claimed to be. If they first differ at a length $L_*>\ell$, the difference
is of the smaller order $t^{-1/2}e^{-L_*^2/4t}$; if the weighted length spectra never differ
(equivalently, the orbifolds are isospectral) the difference vanishes identically. Here the
systole is the least length of a closed geodesic, including those through cone points.

%   For $0<t\le\ell^2/(2(1+\ell))$,
%   \[
%     |\cZ_{\Orb_1}(t)-\cZ_{\Orb_2}(t)|\le\frac{\pi e^{3D}}{A(1-e^{-\ell})}\;\ell e^{\ell/2}\Big(1+\frac{2t}{\ell-t}\Big)\frac{e^{-\ell^2/4t}}{\sqrt{4\pi t}}
%     \le C(A,\ell,D)\,t^{-1/2}e^{-\ell^2/4t},
%   \]
%   with $D=\max(\operatorname{diam}\Orb_1,\operatorname{diam}\Orb_2)$ and $C$ as in Theorem 1.2(iii);
````


---

# G5-bis audit: statements under review, group `descent`

Descent: the 2-isogeny descent on C_{27/2}, its torsion, and the coordinates of 3P on C_{155/12}

Every result below is copied verbatim, by line range, from its source file (`review/audit-2/build_statements.py`
asserts the anchors and that no proof text is included). Items marked COMPOSED combine verbatim excerpts with
connective text in [square brackets]. **Proofs, scripts and data of the sessions that produced these results are
deliberately withheld.** You must not open any file of `theory/pte/`, `theory/revision/`, `theory/signatures/`
(other than where stated below), `review/referee-sim/` or `paper/` (the manuscript contains proofs of some of these
results). If you do open one by accident, say so in your REVIEW.md under 'contamination'.



## Context files you may read (previously audited statements, no proofs)

- review/audit/statements/diophantine.md  (the curves C_Lambda: the cubic Lambda-fibre of the pair (S_1,R) in the Diophantine section; the claim DI.7 that the base pair is isolated; DI.6 where 3P is printed). Read DI.* for the definition of the plane cubics C_Lambda, S_1, R, hyperbolic triads; do not read any other file of theory/diophantine.

## External inputs

- Cremona, Algorithms for Modular Elliptic Curves, 2nd ed., section 3.6 (descent via 2-isogeny, (3.6.2)) and section 3.3 (torsion injectivity) (fetched: sources/cremona_ch3.txt). State exactly what you take from it; re-derive any formula you can.

## Fetched sources

Texts fetched headlessly by `review/audit-2/fetch_sources.sh` are in `review/audit-2/sources/` (not committed).
Never quote a source from memory: quote the fetched text, with page or section. An unreachable source is an
instrument gap, to be logged, not a confirmation.


## Group: descent

### DE.0. The claimed isomorphism and its inverse

Source: `theory/revision/descent.tex` lines 23-24; `theory/revision/descent.tex` lines 28-28 (verbatim).

````
[COMPOSED. C_{27/2} is the plane cubic of the Diophantine section with Lambda = 27/2 (see context). Claim: with e_2 = XY+YZ+ZX the maps below are mutually inverse isomorphisms over Q between C_{27/2} and the elliptic curve E, sending the origin of E to O = (1:-1:0).]

  \varphi(X:Y:Z)=\Big(-\frac{16e_2}{Z^2},\ \frac{8(X-Y)}Z\Big(-\frac{4e_2}{Z^2}-54\Big)\Big),\qquad
  \psi(x,y)=\big(25x+y:\ 25x-y:\ 4(x-216)\big).

  E:\ y^2=x(x+9)(x+384)=x^3+393x^2+3456x,
````

### DE.1. The rank claim

````
[COMPOSED from the proof's claims. With E': y^2 = x(x^2 + c'x + d'), c' = -786, d' = 140625 the 2-isogenous curve of E (c = 393, d = 3456): the two 2-isogeny Selmer-type groups are {+-1, +-6} (order 4) for E and {1} for E'; rank E(Q) = 0, with no Sha ambiguity.]
````

### DE.2. The torsion claim

Source: `theory/revision/descent.tex` lines 78-79 (verbatim).

````
[COMPOSED.] E(Q) = E(Q)_tors is isomorphic to Z/2 x Z/6, and consists of the twelve points

  O,\ (0,0),\ (-9,0),\ (-384,0),\ (-24,\pm360),\ (-144,\pm2160),\ (16,\pm400),\ (216,\pm5400)
\]

[with (0,0), (-9,0), (-384,0) of order 2, (16,+-400) of order 3, and (-24,+-360), (-144,+-2160), (216,+-5400) of order 6. The proof reduces E modulo 7 and 11 and counts #E(F_7) = #E(F_11) = 12.]
````

### DE.3. The twelve rational points of C_{27/2}

Source: `theory/revision/descent.tex` lines 84-87 (verbatim).

````
\emph{The points of $C_{27/2}$.} The twelve points $(1:0:0)$, $(0:1:0)$, $(0:0:1)$, $(1:-1:0)$,
$(0:1:-1)$, $(1:0:-1)$ and the permutations of $(1:4:4)$ and $(1:1:4)$ lie on $C_{27/2}$ and are
distinct, so they are all of $C_{27/2}(\Q)$; the positive ones are the six permutations of $(1:4:4)$
and $(1:1:4)$.
````

### DE.4. Consequence for triads

Source: `theory/revision/descent.tex` lines 89-91 (verbatim).

````
A triad with $S_1=18k$ and $R=\frac3{4k}$ has $\Lambda=\frac{27}2$, so it is a positive rational point of
$C_{27/2}$, hence a permutation of $(1:4:4)$ or $(1:1:4)$. Each has exactly one integer representative
with sum $18k$, namely $(2k,8k,8k)$ and $(3k,3k,12k)$, and both are hyperbolic since $R=\frac3{4k}<1$.
````

### DE.5. Theorem 5.16 (isolation) as in the manuscript (statement unchanged)

Source: `review/audit/statements/diophantine.md` lines 176-188 (verbatim).

````
**What does *not* adapt: the base pair is isolated.** $C_{27/2}$ has rank 0
**unconditionally**. PARI/GP 2.17.2 `ellrank` on the integral model
$[0,393,0,3456,0]$ returns $[0,0,0,[\,]]$, and the manual states that the
upper bound $r_2=C-T-s$ is computed unconditionally from the 2-Selmer group.
`elltors` gives torsion of order 12, $\mathbf Z/2\times\mathbf Z/6$.
`ranks.py` lists the 12 points on the plane cubic exactly (the six base
points and their translates by the order-6 point $(1,4,4)$) and asserts that
the only positive ones are the permutations of $(1,4,4)$ and $(1,1,4)$. Hence, for every
$k$, the class of $\{(2k,8k,8k),(3k,3k,12k)\}$ has exactly two members: no
third pillow ever joins the minimal degeneracy. Every isosceles
triple tested is torsion: all 1,482 triples $(u,v,v)$ with $u\ne v\le39$,
by exact order computation. So the isosceles
family, including the base pair, is (as far as tested) a torsion phenomenon, and the unbounded
````

### DE.6. The coordinates of 3P

Source: `theory/revision/point3P.tex` lines 6-7 (verbatim).

````
[COMPOSED. C_{155/12} is the cubic C_Lambda with Lambda = 155/12; the group law is the chord-tangent law with base point O = (1:-1:0). Claim:]

% With base point O = (1:-1:0) and P = (4:9:18) on C_{155/12}:
%   2P = (16352 : 288 : -365),   3P = (162833463 : 723926268 : 287876366).

[The manuscript previously printed 3P = (162833463 : 287876366 : 723926268); the corrected claim is 3P = (162833463 : 723926268 : 287876366).]
````


---

# G5-bis audit: statements under review, group `stability`

Stability: Proposition 6.10 (explicit remainder formulas) and re-certification of every printed delta

Every result below is copied verbatim, by line range, from its source file (`review/audit-2/build_statements.py`
asserts the anchors and that no proof text is included). Items marked COMPOSED combine verbatim excerpts with
connective text in [square brackets]. **Proofs, scripts and data of the sessions that produced these results are
deliberately withheld.** You must not open any file of `theory/pte/`, `theory/revision/`, `theory/signatures/`
(other than where stated below), `review/referee-sim/` or `paper/` (the manuscript contains proofs of some of these
results). If you do open one by accident, say so in your REVIEW.md under 'contamination'.



## Context files you may read (previously audited statements, no proofs)

- review/audit/statements/stability.md  (ST.0 setting and recovery map, ST.12 Proposition S5, ST.13, ST.14 the printed results table). Everything you need for the setting and the printed values is in the verbatim excerpts below.

## External inputs

- None external. The only task-specific facts are the notation and formulas of the excerpts. Exact rational arithmetic only (fractions.Fraction or sympy). Floating point is not a certificate.

## Fetched sources

Texts fetched headlessly by `review/audit-2/fetch_sources.sh` are in `review/audit-2/sources/` (not committed).
Never quote a source from memory: quote the fetched text, with page or section. An unreachable source is an
instrument gap, to be logged, not a confirmation.


## Group: stability

### SB.0. Setting and recovery map (previously audited)

Source: `review/audit/statements/stability.md` lines 30-67 (verbatim).

````
### ST.0. Setting and the recovery map

Source: `theory/stability/proof.md` lines 45-75 (verbatim).

````
## 1. Setting and the recovery map

Conventions (`numerics/REPORT.md` §2; `theory/cone-coefficients/ucar-source.md`): positive
Laplacian, K = κ = −1, and

- H₋₁ = Area/(4π) = (n − 2 − R)/2;
- H_ν = (Area/4π)·α_{ν+1} + Σ_i b_ν(m_i) for ν ≥ 0;
- b_ν(m) = (−1)^ν p_ν(m)/m, with p_ν = Σ_k π_{ν,k} m^{2k} even of degree 2ν + 2 and
  p_ν(1) = 0 (Uçar (4.25)+(4.33));
- α_j = a_j^{sm}/vol (Uçar (4.35)): α = 1, −1/3, 1/15, −4/315, 1/315, …

The smooth coefficients α_j are also derived independently from the Selberg identity term
(`stab_common.alpha_smooth_selberg`), and the two agree for j ≤ 11.

The number n of cone points is assumed known. The **recovery map** studied throughout is:

1. **Front end.** Ĩ := L⁻¹(H̃ − h₀).
2. **Linear solve.** ẽ := M(Ĩ)⁻¹ b(Ĩ) (Theorem B).
3. **Roots.** Take the roots of q̃(z) := Σ_{j=0}^{n}(−1)^j ẽ_j z^{n−j}, with ẽ₀ = 1.
4. **Rounding** (integer orders only). Round the real part of every root.

Throughout, μ := max_i m_i. Hats denote scale-free quantities:

- m̂ = m/μ ∈ (0,1]ⁿ and ê_k = e_k/μ^k;
- Î = (μR, P₁/μ, P₃/μ³, …).

Theorem B's system is weighted-homogeneous: row j has weight 2j+1, the last row weight n−1,
and column k weight k. Hence M(Î) = D_r⁻¹ M(I) D_c, and ê solves M(Î) ê = b(Î).
Distances between multisets are optimal matching distances,
d(m, m′) = min_π max_i |m_i − m′_{π(i)}|.

````

````

### SB.0b. Front-end tables, Lemmas S2, Theorem S2, Lemma S3 and Theorem S3 (previously audited; define delta_thm)

Source: `review/audit/statements/stability.md` lines 86-254 (verbatim).

````
### ST.2. Front-end tables (claims)

Source: `theory/stability/proof.md` lines 100-131 (verbatim).

````
The first rows of L⁻¹, which give I = L⁻¹(H − h₀):

| | H₋₁ | H₀ | H₁ | H₂ | H₃ |
|---|---|---|---|---|---|
| R | −2 | | | | |
| P₁ | 2 | 12 | | | |
| P₃ | −18 | −120 | −360 | | |
| P₅ | 30 | 252 | 1260 | 2520 | |
| P₇ | −70/3 | −240 | −1680 | −6720 | −10080 |

**Amplification.** With every |δH_ν| ≤ δ, the worst-case error in I_r is ℓ_r·δ, where ℓ_r is
the absolute row sum of L⁻¹. Row r involves only the first r+1 coefficients, so ℓ_r is the
same for every n:

| | R | P₁ | P₃ | P₅ | P₇ | P₉ | P₁₁ | P₁₃ |
|---|---|---|---|---|---|---|---|---|
| diagonal 1/\|L_rr\| | 2 | 12 | 360 | 2520 | 10080 | 28512 | 43243200/691 | 112320 |
| ℓ_r (row sum) | 2 | 14 | 498 | 4062 | 56230/3 | 303654/5 | 104899830/691 | 10805786/35 |

**Correction to the review (DEFECTS.md MAJ-05).**

- The factors 12, 360, 2520 are correct as the diagonal entries of L⁻¹: for P₁ from H₀, P₃
  from H₁ and P₅ from H₂.
- They are not the amplification factors. Each invariant also inherits the errors of all
  lower coefficients through the off-diagonal entries, e.g.
  δP₃ = −18 δH₋₁ − 120 δH₀ − 360 δH₁.
- So the worst-case factors are **14, 498, 4062**, larger by 1.17, 1.38 and 1.61.
- R is recovered from H₋₁ with factor 2. Equivalently, R = n − 2 − Area/(2π), so the factor
  is 1/(2π) per unit of area.
- In relative terms the front end is harmless. The ratio
  κ_r = Σ_c |(L⁻¹)_{rc}| |H_c| / |I_r| lies between 0.02 and 3.7 on every test multiset of
  `front_end_output.md`. For (2,8,8) it is 0.33, 0.94, 1.33 for R, P₁, P₃.
````

### ST.3. Lemma S2.1

Source: `theory/stability/proof.md` lines 142-146 (verbatim).

````
**Lemma S2.1 (the constant c_n of Theorem B, all n).** For every n ≥ 2,

  det M = (−1)^{n(n+1)/2} ∏_{i<j}(m_i + m_j) / e_n,

so c_n = (−1)^{n(n+1)/2}. This replaces "c_n ∈ ℚ^×, computed for n ≤ 8" in Theorem B.
````

### ST.4. Lemma S2.2

Source: `theory/stability/proof.md` lines 172-183 (verbatim).

````
**Lemma S2.2 (Hurwitz factorisation of M).** Let f(z) = ∏(1 + m_i z) = E(z²) + zO(z²), and for
D(z) = Σ_{k=1}^n d_k z^k let W_D := E_f O_D − E_D O_f, a polynomial in w = z² of degree ≤ n−1.
Define two n × n matrices (with e_i := 0 outside 0 ≤ i ≤ n):

- B_{k,j} = (−1)^{j+1} e_{2k+1−j}, for 0 ≤ k ≤ n−1 and 1 ≤ j ≤ n. This is the map
  d ↦ (coefficients of W_D).
- S_{k,i} = e_{2(k−i)} for i ≤ k ≤ n−2, S_{n−1,n−1} = (−1)ⁿ e_n, and all other entries 0.

Then

  B = S·M,  det B = (−1)^{n(n−1)/2} ∏_{i<j}(m_i+m_j),  M⁻¹ = B⁻¹ S.

````

### ST.5. Theorem S2

Source: `theory/stability/proof.md` lines 196-222 (verbatim).

````
**Theorem S2 (Lipschitz dependence of e on I_n, explicit constants).**

*Setting.* Let m be positive reals and μ = max m_i. Let Ĩ be any real data vector with
scale-free error

  η := max( μ|R̃ − R|, max_{1≤l≤n−1} |P̃_{2l−1} − P_{2l−1}| / μ^{2l−1} ) ≤ 1.

*Constants.* Put κ := ‖M(Î)⁻¹‖_∞ and

- σ_k(n) := [w^k] artanh(w) · sec²((n+1) artanh w). For instance σ₁ = 1 and
  σ₃ = 1/3 + (n+1)²; n = 3: (1, 49/3); n = 4: (1, 76/3, 6628/15).
- ζ_n := max(1, max_{0≤j≤n−2} Σ_{0≤i<j, 2≤2j−2i≤n} σ_{2i+1}(n)). For example ζ₃ = 1,
  ζ₄ = 79/3, ζ₅ = 14048/15.
- ρ_n(m̂) := max( ê_n, max_{0≤j≤n−2} Σ_{i=0}^{j} σ_{2i+1}(n) ê_{2j−2i} ).

*Conclusions.*

(a) The inverse is bounded by

  κ ≤ n Λ(m̂) ‖Ŝ‖_∞ / ∏_{i<j}(m̂_i + m̂_j) ≤ n · binom(2n,n)^{n/2} · 2^{n−1} / ∏_{i<j}(m̂_i + m̂_j),

  where Λ(m̂) = ∏_c ‖c-th column of B(ê)‖₂ and ‖Ŝ‖_∞ ≤ max(Σ_{k even} ê_k, ê_n).

(b) If β := κ ζ_n η ≤ 1/2, then M(Ĩ) is invertible, and ẽ = M(Ĩ)⁻¹ b(Ĩ) satisfies

  max_k |ẽ_k − e_k| / μ^k ≤ 2 κ ρ_n(m̂) η.

````

### ST.6. Ostrowski input as quoted

Source: `theory/stability/proof.md` lines 264-273 (verbatim).

````
**Standard global theorem (fetched, `review/literature/root-perturbation.md`).** Ostrowski,
*Acta Math.* 72 (1940), Théorème XXX, eq. (71,1), p. 212, read from the primary. For monic
f, g of degree n with roots x_ν and y_ν, after renumbering,

  |y_ν − x_ν| ≤ (2n−1)ε,  ε = (Σ_{ν=1}^{n} |a_ν − b_ν| γ^{n−ν})^{1/n},

where γ is the largest root modulus. "Les racines … satisfont … à une condition de Lipschitz
d'ordre 1/n." This is uniform but crude: exponent 1/n everywhere, with no use of
separation. The local statement below has the exponent 1/k at a k-fold root, and is
Lipschitz at simple roots, with explicit constants.
````

### ST.7. Lemma S3

Source: `theory/stability/proof.md` lines 275-287 (verbatim).

````
**Lemma S3 (clusters, explicit Rouché).** Work in scale-free variables. Let
q(z) = ∏(z − m̂_i) = Σ_j (−1)^j ê_j z^{n−j}, and let q̃ be the same polynomial with ẽ in place
of ê, where |ẽ_j − ê_j| ≤ ε. Let a be a distinct value among the m̂_i, of multiplicity k, and
put

- g_a := min_{b≠a} |a − b| (∞ if there is no other value);
- Q_a := ∏_{b≠a} |a − b|^{k_b}.

If 0 < r ≤ min(g_a, 1)/2 and r^k Q_a ≥ 2^{1−k} 3ⁿ ε, then q̃ has exactly k zeros in |z − a| < r.
In particular, for r_a(ε) := (2^{1−k}3ⁿ ε/Q_a)^{1/k}, whenever r_a(ε) ≤ min(g_a, 1)/2, the k
roots of the cluster lie within r_a(ε) = O(ε^{1/k}) of a. The bound is Lipschitz for simple
orders, where Q_a = |q′(a)|.

````

### ST.8. Theorem S3

Source: `theory/stability/proof.md` lines 301-321 (verbatim).

````
**Theorem S3 (heat coefficients → orders; the combined stability theorem).**

*Setting.* Let m be positive reals, n = |m|, μ = max m_i. Let H̃ be data with
δ := max_{−1≤ν≤n−2} |H̃_ν − H_ν(m)|. Put

- λ_μ := max(μ ℓ₀, max_{1≤r≤n−1} ℓ_r μ^{1−2r}), with ℓ = (2, 14, 498, 4062, …) as in §2;
- κ, ρ_n, ζ_n as in Theorem S2.

*Statement.* Suppose λ_μ δ ≤ 1 and κ ζ_n λ_μ δ ≤ 1/2. Then for every distinct order a, of
multiplicity k_a, with

  r_a := μ · (2^{2−k_a} 3ⁿ κ ρ_n λ_μ δ / Q̂_a)^{1/k_a} ≤ μ · min(ĝ_a, 1)/2,

the recovered polynomial q̃ has exactly k_a roots within r_a of a. Consequently, if the
radius hypothesis holds for **every** distinct order a,

  d(roots of q̃, m) ≤ max_a C_a δ^{1/k_a},  C_a = μ (2^{2−k_a} 3ⁿ κ ρ_n λ_μ / Q̂_a)^{1/k_a}.

So recovery is Lipschitz with constant C_a at simple orders, where Q̂_a = |q̂′(â)| measures the
gaps, and Hölder with exponent 1/k at a k-fold coincidence.

````

````

### SB.1. Proposition S5 as previously stated (the tests that Prop. 6.10 refines)

Source: `review/audit/statements/stability.md` lines 313-350 (verbatim).

````
### ST.12. Proposition S5 (statement of the two tests)

Source: `theory/stability/proof.md` lines 378-408 (verbatim).

````
**Proposition S5 (certificates, exact arithmetic).**

*Input.* Fix m and componentwise radii ρ_ν ≥ 0. Every data vector with |H̃_ν − H_ν(m)| ≤ ρ_ν
is recovered exactly if either test below succeeds, with all quantities evaluated in
rational arithmetic (`threshold.py`).

*Common part.*

1. |δI| ≤ |L⁻¹|ρ.
2. Bound |δT_k| ≤ (|sech²U| ∗ |δU|)_k + [z^k](tan(U+|δU|) − tan U − sec²U·|δU|). The first
   term is the exact linear part. The second is the coefficientwise majorant of the
   remainder, valid because U ≥ 0.
3. Form the residual bound |r|, the bound |δM|, and A := |M⁻¹||δM|.
4. Certify ρ(A) < 1 by checking that v = (I − A)⁻¹𝟙 > 0.
5. Then |ẽ − e| ≤ E := (I − A)⁻¹|M⁻¹||r|.

*(i) Componentwise test.* For each distinct order a, some radius r ∈ {1/2, 19/40, …, 1/40,
1/100, 1/1000} satisfies

  r^{k_a} ∏_{b≠a}(|a−b| − r)^{k_b} > Σ_j E_j (a + r)^{n−j}.

*(ii) Coherent test.* Write ẽ − e = G·δH + ϱ, where:

- G = (D_I e) L⁻¹ is exact (Lemma S2.1);
- |ϱ| ≤ |M⁻¹||r_rem| + A E, with r_rem the remainder part of r.

On |z − a| = r, bound the first-order part through the exact Taylor coefficients at a of
the polynomials p_c(z) = Σ_j (−1)^j G_{jc} z^{n−j}. The test is

  r^{k_a} ∏(|a−b| − r)^{k_b} > Σ_c ρ_c Σ_l |p_c^{(l)}(a)/l!| r^l + Σ_j |ϱ_j| (a + r)^{n−j}.

````

````

### SB.2. Proposition 6.10: notation and the explicit formulas (steps 1-3, J)

Source: `theory/revision/prop610.tex` lines 14-16; `theory/revision/prop610.tex` lines 20-48 (verbatim).

````
Write $\cI=(R,P_1,P_3,\dots,P_{2n-3})$, indexed $\cI_0=R$ and $\cI_k=P_{2k-1}$, and
$U(z)=\sum_{k=1}^{n-1}P_{2k-1}z^{2k-1}/(2k-1)$; all power series are truncated after $z^{2n-3}$, and
$e_k=0$ for $k>n$. Write $\operatorname{sech}^2U=1-T^2=\sum_ks_kz^k$, $T=\tanh U$.

\begin{enumerate}[label=\arabic*.]
\item Put $\Delta=|\mathbf F^{-1}|\,\delta$, so $|\tilde\cI_k-\cI_k|\le\Delta_k$, and
  $|\delta U|(z)=\sum_{k=1}^{n-1}\Delta_kz^{2k-1}/(2k-1)$.
\item Put
  \[
    \tau^{\rm lin}=|\operatorname{sech}^2U|*|\delta U|,\qquad
    \tau^{\rm rem}=\tan(U+|\delta U|)-\tan U-\sec^2U\cdot|\delta U|,\qquad
    \tau=\tau^{\rm lin}+\tau^{\rm rem},
  \]
  coefficientwise; then $|\tilde T_k-T_k|\le\tau_k$, and the part of $\tilde T_k-T_k$ beyond first order
  in $\delta\cI$ is at most $\tau^{\rm rem}_k$ in absolute value.
\item Put, for $0\le j\le n-2$,
  \[
    \rho_j=\sum_{i=0}^{j}\tau_{2i+1}\,e_{2j-2i},\qquad
    \rho^{\rm rem}_j=\sum_{i=0}^{j}\tau^{\rm rem}_{2i+1}\,e_{2j-2i},
  \]
  and $\rho_{n-1}=\Delta_0e_n$, $\rho^{\rm rem}_{n-1}=0$. Let $\Delta_M$ be the $n\times n$ matrix, rows
  indexed by $0\le j\le n-1$ and columns by the unknowns $e_1,\dots,e_n$, with entry $\tau_{2i+1}$ in
  row $j$, column $e_{2j-2i}$, for $0\le i<j\le n-2$ and $2j-2i\le n$; entry $\Delta_0$ in row $n-1$,
  column $e_n$; and zero elsewhere. Then $|r|\le\rho$, $|r_{\rm rem}|\le\rho^{\rm rem}$ and
  $|\delta M|\le\Delta_M$ entrywise. Put $A=|M^{-1}|\Delta_M$.
\end{enumerate}
Steps 4 and 5 are unchanged, with $\rho$ in place of $|r|$. In test (ii), $|\varrho|\le|M^{-1}|\rho^{\rm rem}+AE$
and $G=-M^{-1}J\,\mathbf F^{-1}$, where $J=\partial(Me-b)/\partial\cI$ at fixed $e$ is
\[
  J_{j,k}=-\frac1{2k-1}\sum_{\substack{k-1\le i\le j\\2j-2i\le n}}e_{2j-2i}\,s_{2i+2-2k}\quad(0\le j\le n-2,\ 1\le k\le n-1),
  \qquad J_{n-1,0}=-e_n,
\]
and $J_{j,0}=0$ for $j\le n-2$, $J_{n-1,k}=0$ for $k\ge1$.
````

### SB.3. Claim after Table 4

Source: `theory/revision/prop610.tex` lines 63-65 (verbatim).

````
%   "Every entry of the $\delta_{\rm cert}$ column can be re-derived from Proposition 6.2 and the
%    formulas above in exact rational arithmetic; for $n\le5$ every series is truncated after $z^7$
%    and has at most four nonzero (odd) coefficients."
````

### SB.4. Rounding convention and the printed results table (delta_thm, delta_cert, delta_up, eps_cert)

Source: `review/audit/statements/stability.md` lines 351-397 (verbatim).

````
### ST.13. Upper bound by construction; rounding convention

Source: `theory/stability/proof.md` lines 413-429 (verbatim).

````
**Upper bound by construction.** For each order a, the search minimises
‖H(q̃) − H(m)‖_∞ over real monic polynomials of two shapes:

- q̃ = (z − c) g(z), with a real root at c = a ± 1/2;
- q̃ = ((z − c)² + y²) g(z), with a complex pair of real part c = a ± 1/2.

The optimiser is numerical. The reported minimiser is rebuilt exactly in rationals, and its
data are evaluated exactly. Its recovery is q̃ itself (Theorem B, checked by an exact solve),
and that q̃ has a root with real part exactly a ± 1/2. At that point rounding is a tie, so
δ_up is an infimum: arbitrarily small further perturbations push the root across, and
recovery fails at every level above δ_up. Hence the true threshold is at most δ_up.

*Rounding of printed values.* δ_thm and δ_cert are printed rounded **down**, and δ_up
rounded **up**, so that each printed number keeps its meaning. An adversarial search found
that the exact test fails at the up-rounded values 2.342e−3 and 1.462e−3, which an earlier
version printed.

````

### ST.14. Results table (printed values to re-certify)

Source: `theory/stability/proof.md` lines 430-446 (verbatim).

````
**Results** (`threshold_output.md`, `threshold_results.json`). The absolute model is
|δH_ν| ≤ δ for all ν. The relative precision listed is δ_cert/|H_ν| for ν = −1, …, n−2, and
ε_cert is the largest uniform relative error |δH_ν| ≤ ε|H_ν| that is certified.

| m | n | δ_thm | δ_cert | δ_up | δ_up/δ_cert | failure built at | δ_cert/|H_ν|, ν = −1..n−2 | ε_cert (uniform relative) |
|---|---|---|---|---|---|---|---|---|
| (2, 8, 8) | 3 | 3.80e-07 | 2.341e-03 | 2.485e-03 | 1.06 | 8−1/2 | 1.8e-02, 1.6e-03, 7.0e-04 | 1.9e-03 |
| (3, 3, 12) | 3 | 1.18e-07 | 4.040e-03 | 4.589e-03 | 1.14 | 3+1/2 | 3.2e-02, 2.8e-03, 7.4e-04 | 4.4e-03 |
| (3, 10, 15, 30) | 4 | 4.02e-11 | 3.660e-03 | 7.488e-03 | 2.05 | 10+1/2 | 4.9e-03, 8.0e-04, 4.1e-05, 3.6e-07 | 8.7e-04 |
| (4, 5, 21, 28) | 4 | 3.14e-11 | 1.461e-03 | 2.018e-03 | 1.38 | 5−1/2 | 1.9e-03, 3.2e-04, 1.6e-05, 1.7e-07 | 4.6e-04 |
| (2, 3, 7) | 3 | 4.49e-07 | 3.658e-03 | 6.587e-03 | 1.80 | 3−1/2 | 3.0e-01, 4.0e-03, 2.7e-03 | 5.0e-03 |
| (4, 4, 4) | 3 | 9.35e-07 | 4.539e-04 | 5.036e-04 | 1.11 | 4+1/2 | 3.6e-03, 5.0e-04, 5.4e-04 | 8.2e-04 |
| (7, 7, 7) | 3 | 9.97e-08 | 8.068e-05 | 8.273e-05 | 1.03 | 7−1/2 | 2.8e-04, 4.9e-05, 2.3e-05 | 1.2e-04 |
| (3, 3, 4, 4) | 4 | 1.48e-09 | 9.597e-05 | 1.195e-04 | 1.24 | 4−1/2 | 2.3e-04, 1.0e-04, 1.1e-04, 7.2e-05 | 1.1e-04 |
| (5, 5, 5, 5) | 4 | 4.74e-10 | 3.617e-05 | 3.826e-05 | 1.06 | 5−1/2 | 6.0e-05, 2.5e-05, 1.9e-05, 6.2e-06 | 3.1e-05 |
| (2, 2, 2, 3) | 4 | 2.03e-09 | 1.858e-04 | 2.520e-04 | 1.36 | 3−1/2 | 2.2e-03, 3.2e-04, 5.6e-04, 7.7e-04 | 4.3e-04 |
| (2, 2, 2, 2, 3) | 5 | 2.72e-12 | 7.908e-06 | 5.743e-05 | 7.26 | 2+1/2 | 2.3e-05, 1.2e-05, 2.1e-05, 2.9e-05, 1.9e-05 | 1.4e-05 |
````
````


---

# G5-bis audit: statements under review, group `threshold-sharpness`

Threshold and sharpness: Theorem 5.13 and the 38 collision-free sums; the sharpness wording of Theorem 1.4

Every result below is copied verbatim, by line range, from its source file (`review/audit-2/build_statements.py`
asserts the anchors and that no proof text is included). Items marked COMPOSED combine verbatim excerpts with
connective text in [square brackets]. **Proofs, scripts and data of the sessions that produced these results are
deliberately withheld.** You must not open any file of `theory/pte/`, `theory/revision/`, `theory/signatures/`
(other than where stated below), `review/referee-sim/` or `paper/` (the manuscript contains proofs of some of these
results). If you do open one by accident, say so in your REVIEW.md under 'contamination'.



## Context files you may read (previously audited statements, no proofs)

- review/audit/statements/threshold.md  (the previously audited threshold results: separation theorem, minimal degeneracy 18, Prop 3)
- review/audit/statements/stability.md  (ST.0-ST.11: the stability results the sharpness wording refers to: Theorem S3, Proposition S3.2, Remark S3.3, Theorem S4)

## External inputs

- None external. Exact arithmetic (integers, Fractions).

## Fetched sources

Texts fetched headlessly by `review/audit-2/fetch_sources.sh` are in `review/audit-2/sources/` (not committed).
Never quote a source from memory: quote the fetched text, with page or section. An unreachable source is an
instrument gap, to be logged, not a confirmation.


## Group: threshold-sharpness

### TH.1. Theorem 5.13 (the threshold) and the computational Proposition (collision-free sums)

Source: `theory/revision/thm513.tex` lines 11-15; `theory/revision/thm513.tex` lines 24-33 (verbatim).

````
\begin{theorem}[The threshold]\label{thm:threshold}
If $p+q+r\le17$, the first two heat invariants determine the hyperbolic triangle orbifold
$\Orb(p,q,r)$ among all hyperbolic triangle orbifolds: $\Kiso(\Orb(p,q,r);\Pill_3)\le2$. The bound
$17$ is sharp: the first failure occurs at cone-order sum $18$ (Theorem~\ref{thm:minimal}).
\end{theorem}

\begin{proposition}[Collision-free sums; computational]\label{prop:collisionfree}
Among the sums $18\le S\le4800$, exactly the $38$ sums
\[
\begin{gathered}
  19,\,21\text{--}25,\,27\text{--}30,\,33,\,41,\,44,\,46\text{--}51,\,59,\,65,\,67,\,81,\,99,\\
  115,\,119,\,123,\,125,\,173,\,199,\,203,\,223,\,235,\,243,\,251,\,307,\,329,\,557
\end{gathered}
\]
carry no collision, that is, no two hyperbolic triads of sum $S$ have the same reciprocal sum.
\end{proposition}
````

### TH.2. Sharpness wording (abstract, Theorem 1.4, after Theorem 6.6)

Source: `theory/revision/sharpness.tex` lines 21-23; `theory/revision/sharpness.tex` lines 26-28; `theory/revision/sharpness.tex` lines 40-44 (verbatim).

````
Recovering the orders from approximate coefficients is Lipschitz at simple orders and H\"older of
exponent $1/k$ at $k$-fold orders; the exponent $1/k$ is sharp for arbitrary data, while for the
coefficients of real orders it is $1/2$ when all the orders are equal.

The exponent $1/k_a$ cannot be improved for arbitrary data. For data that are the heat invariants
of real orders it is $\frac12$, and sharp, at a double order, and at an order of any multiplicity
$k=n\ge3$, that is, when all the orders are equal.

Recovery is Lipschitz at simple orders and H\"older of exponent $1/k$ at a $k$-fold coincidence.
The exponent $1/k$ is sharp for arbitrary data (Proposition~\ref{prop:sharpexp}(ii)); for data
coming from real orders it is $\frac12$ at a double order (Proposition~\ref{prop:sharpexp}(i)) and when all
the orders are equal (Remark~\ref{rem:triple}); other configurations are not settled
(Figure~\ref{fig:F8}).
````

### TH.3. Remark 6.8 addition and the real-multiset restriction

Source: `theory/revision/sharpness.tex` lines 57-59 (verbatim).

````
%   "The argument applies verbatim to $(a,\dots,a)$ with any $n\ge3$ entries. The family
%    $(a+s,a-s,a,\dots,a)$, with $\delta P_1=0$, $\delta P_3=6as^2$ and all other data changes $O(s^2)$,
%    shows that $\frac12$ is attained."

[COMPOSED from item (5) of the fragment. For k >= 3 the witnesses q_s of Proposition 6.7(ii), whose roots are a + s e^{2 pi i j/k}, are not all real, and their data are not the heat invariants of any real multiset.]
````


---

# G5-bis audit: statements under review, group `literature`

Literature: every attribution a PTE theorem depends on

Every result below is copied verbatim, by line range, from its source file (`review/audit-2/build_statements.py`
asserts the anchors and that no proof text is included). Items marked COMPOSED combine verbatim excerpts with
connective text in [square brackets]. **Proofs, scripts and data of the sessions that produced these results are
deliberately withheld.** You must not open any file of `theory/pte/`, `theory/revision/`, `theory/signatures/`
(other than where stated below), `review/referee-sim/` or `paper/` (the manuscript contains proofs of some of these
results). If you do open one by accident, say so in your REVIEW.md under 'contamination'.



## Context files you may read (previously audited statements, no proofs)

- (none)

## External inputs

- Fetched sources are in review/audit-2/sources/ (run fetch_sources.sh; unreachable files are instrument gaps). You may also read the raw fetched source files of theory/pte/sources/ (the *.pdf, *.txt, *.htm files listed in theory/pte/sources/SHA256SUMS) but NOT theory/pte/sources/NOTES.md, theory/pte/LITERATURE.md or any other file of theory/pte. Where the same document exists in both places, check the hashes agree or note that they do not.
- Borwein-Ingalls (e-periodica, L'Enseignement Math. 40 (1994) 3-27), Borwein-Lisonek-Percival (Math. Comp. 72), Melzak (Canad. Math. Bull. 4 (1961)), Wooley and Chen's web pages must be re-fetched by you or copied from theory/pte/sources with a hash check; record every HTTP result. No browser.

## Fetched sources

Texts fetched headlessly by `review/audit-2/fetch_sources.sh` are in `review/audit-2/sources/` (not committed).
Never quote a source from memory: quote the fetched text, with page or section. An unreachable source is an
instrument gap, to be logged, not a confirmation.


## Group: literature

### LIT.0. The attribution claims (composed table, see below)

Source: generated (literature) (verbatim).

Each claim says: *a statement S is made by source X at the stated place*. Verify S against the fetched text of X:
exact wording, exact hypotheses (degree versus size, k versus k+1, integers versus rationals, 'ideal' versus
'symmetric'), exact place (page, proposition, entry number). Grade each claim CONFIRMED / CONFIRMED WITH CORRECTION
(give the correction) / NOT FOUND / CONTRADICTED / SOURCE UNREACHABLE. A claim that is a *negative* statement
(for instance 'no bound o(k^2) is known') is graded against the most recent sources you can fetch.

Notation used by the paper: [A] =_k [B] means two distinct multisets of integers of a common size n with equal power sums
P_j for j = 1..k. N(k) is the least such n. A solution is ideal if n = k+1. Degree k, size n.

Where a PTE theorem of the paper uses the claim is given in brackets.

**Borwein-Ingalls, 'The Prouhet-Tarry-Escott problem revisited', L'Enseignement Math. (2) 40 (1994) 3-27**
- B1. Defines N(k) as the least size of a solution of degree k (p. 6) [all of section 4].
- B2. Proposition 1 of that paper [state what it says; the paper cites 'Props. 1-3'].
- B3. Proposition 2: N(k) >= k+1 [Lemma 1.5(3), Theorem 4.2].
- B4. Proposition 3: N(k) <= k(k+1)/2 + 1, proved by pigeonhole [Lemma 1.5(2), Theorem 3.4, Theorem 4.2(b)].
- B5. p. 7: the bounds of Wright [22] and Melzak [15] are 'slightly stronger' and only improve to
  N(k) <= (k^2-3)/2 for k odd and N(k) <= (k^2-4)/2 for k even [remark after Theorem 4.2].
- B6. p. 7: Hua's bound M(k) <= (k+1)(log((k+2)/2)/log(1+1/k) + 1) ~ k^2 log k concerns the exact-degree quantity M(k)
  (degree exactly k), of order k^2 log k [context only].
- B7. Section 6, problem 3: 'Prove N(k) <= o(k^2)' is listed as open, and the paper says no progress has been made
  'for many years'; also 'The big prize is to find ideal solutions of all degrees' [Theorem 4.2 and the Remark on exponents].
- B8. p. 8: the definition of an odd symmetric solution: sum alpha_i^j = 0 for j = 1,3,5,...,k-1 (with B = -A)
  [Proposition 2.3(a) uses 'odd ideal symmetric solution of size 2L-1'].
- B9. p. 6, Lemma 2: the Prouhet step [A]=_k[B] implies [A, B+M] =_{k+1} [A+M, B] [context].
- B10. p. 9 table and p. 25: the explicit symmetric ideal solutions: size 4 {+-3,+-11}/{+-7,+-9}; size 6 {+-4,+-9,+-13}/{+-1,+-11,+-12};
  size 8 {+-2,+-16,+-21,+-25}/{+-5,+-14,+-23,+-24}; the perfect 7-set {-51,-33,-24,7,13,38,50} (and four more); Letac's two 9-sets
  {-98,-82,-58,-34,13,16,69,75,99} and {-169,-161,-119,-63,8,50,132,148,174}; Letac's size-10 solution [witnesses, L=4,5].
- B11. p. 4: Prouhet's 1851 general solution ('n^{k+1} numbers separable into n sets') and Wright's 1959 account [context].
- B12. Proposition 4: rational points of x^2 y^2 - 13 x^2 - 13 y^2 + 121 = 0 give size-10 ideal symmetric solutions (Smyth) [context].

**Melzak, 'A note on the Tarry-Escott problem', Canad. Math. Bull. 4 (1961) 233-237**
- M1. Records Wright's bound K(n) <= (n^2+4)/2 as the best bound known so far (pp. 233-234); state what n and K(n) mean there and
  whether this is the same bound as B5 (translate degree/size conventions carefully).
- M2. Table 1 (p. 237) gives individual numerical upper bounds for n <= 29; no asymptotic improvement.

**Wooley**
- W1. Ann. of Math. 175 (2012) 1575-1627 ('Vinogradov's mean value theorem via efficient congruencing'), Theorem 1.3: W(k,h) <= k^2 + k - 2 (the hypotheses on h).
- W2. Proc. LMS 118 (2019) 942-1016 ('Nested efficient congruencing and relatives of Vinogradov's mean value theorem'), Theorem 13.1:
  W(k,h) <= k(k+1)/2 + 1. State what W(k,h) is and whether W(k,2) is N(k) or the exact-degree M(k).

**Croot-Mao-Yip, arXiv:2609.05061** (p. 1)
- C1. 'Using a pigeonhole principle argument one can easily see that P(k,m) <= k(k+1)/2+1', with P(k,2) = N(k).
- C2. 'It is an open problem to determine if P(k,2) = k+1; it is only known that P(k,2) = k+1 when 2 <= k <= 9 and k = 11.'
- C3. The paper names no bound on N(k) better than quadratic [the most recent source the paper cites].

**Coppersmith-Mossinghoff-Scheinerman-VanderKam (CMSV), arXiv:2304.11254, Math. Comp. 93 (2024) 2473-2501**
- D1. p. 2: 'Ideal solutions in the PTE problem over Z are known for n <= 10 and n = 12' (n is the size); size 11 is open.
- D2. 'No new integral solutions are found for 9 <= n <= 16' [searches].
- D3. The size-12 solution of Kuosa-Meyrignac-Chen (1999), +-{22,61,86,127,140,151} / +-{35,47,94,121,146,148} (CMSV (5)); Letac's two 9-sets (CMSV (3)).
- D4. Consistency: D1 and C2 describe the same set of ideal solutions (size n <-> degree k = n-1).

**Borwein-Lisonek-Percival, 'Computational investigations of the PTE problem', Math. Comp. 72 (2003) 2063-2070**
- P1. p. 2063: 'Parametric ideal solutions are known for n = 1,...,8 and n = 10'.
- P2. p. 2064: Gloden's two-parameter family of size 7; p. 2069: Letac's 9-sets and two further size-10 solutions
  +-{71,131,180,307,308}/+-{99,100,188,301,313} and +-{18,245,331,471,508}/+-{103,189,366,452,515}.

**Chen Shuwen, 'A survey of the Prouhet-Tarry-Escott problem and its generalizations', arXiv:2506.11429 (2025), and eslpower.org**
- S1. Appendix A.1.6, A.1.17, A.1.26, A.1.33 (equal sums of odd powers, exponents 1,3,...,2L-3 for L = 3,4,5,6):
  [1,5,5]=[2,3,6]; [1,13,17,23]=[3,9,21,21]; [3,19,37,51,53]=[9,11,43,45,55]; [7,91,173,269,289,323]=[29,59,193,247,311,313].
  Check that each entry number is the one that lists exactly this solution, its exponent set, and the stated attributions
  (A.48 'smallest solution by computer search' for [1,5,5]=[2,3,6]; Moessner 1939; Gloden; Xeroudakes-Moessner; Lander;
  Choudhry; Chen 2000 = A.313; Wroblewski 2009 = A.314-A.316, three further non-negative solutions and one with a negative entry).
- S2. eslpower.org, Theorem 3 (page TarryPrb.htm): if [a_1..a_m] = [b_1..b_m] for k = 1,3,...,2n-1 then
  [T+a_i, T-b_i] = [T+b_i, T-a_i] for k = 1,2,...,2n [Proposition 2.2 is attributed to this lifting].
- S3. Negative exponents (survey section 1.4 and Appendix A.5): '33 distinct types with k_1 < 0 and k_n > 0'; type (-1,1): [4,10,12]=[5,6,15];
  type (-1,1,3): [3,10,15,30]=[4,5,21,28] (A.685); type (-1,1,5): [81,374,585,891]=[85,286,702,858].
- S4. The type (-1,1,3,...,2L-3) for L >= 4 does not appear in the survey, and neither does an unequal-size version [negative claim; the paper
  says its system is 'not tabulated'].
- S5. Non-symmetric ideal solutions have been discovered only for degrees n <= 7 (survey p. 13) [context].
- S6. A.1.21, A.1.35: Chernick's two-parameter symmetric families of sizes 5 and 7 [context].

**Others**
- O1. Caley (arXiv:1011.1262, p. 2): the k log k statement concerns the 'easier Waring' number v(k), not N(k) [so it is not a bound on N(k)].
- O2. Choudhry (arXiv:2207.12726, 2022): polynomial parametrisations are counted 'only when k <= 7'; and BLP's 'parametric' (P1) means something
  different [context].
- O3. Prouhet-Thue-Morse: nothing to check beyond B11.
- O4. The statement 'No retrieved source contains an O(k log k) bound for N(k)': search the fetched texts and the web (arXiv listing, Semantic Scholar)
  for any bound N(k) = o(k^2) published after 1994 and report what you find. This is the adversarial search for the 'open problem' claim:
  a single counterexample makes Theorem 4.2's commentary and Remark (What the exponent means) wrong.

