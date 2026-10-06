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

Source: `theory/pte/proof.md` lines 342-351 (verbatim).

````
**Theorem 4.2 (the exponent of $f$ is a PTE exponent).**

(a) If $f(A)\ge L+1$, then $N(2L-2)\le2\lfloor A/\pi\rfloor+8$.

(b) If $N(k)\le Ck^\beta$ for all $k\ge1$, then $f(A)\ge\frac12(A/6\pi C)^{1/\beta}$ for all
$A\ge8\pi$.

(c) For $0<\alpha\le1$: $f(A)\ge cA^\alpha$ for all large $A$ (some $c>0$) if and only if
$N(k)\le Ck^{1/\alpha}$ for all $k$ (some $C$). In particular $f(A)=\Theta(A)$ iff
$N(k)=O(k)$.
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
