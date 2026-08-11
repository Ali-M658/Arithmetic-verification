# Original computation — witnesses for the open lower bound in Remark 5.6

**Status: this is NOT a literature finding.** It is an original exact-arithmetic
computation run during the sweep. It is recorded separately from the literature results
so the two are never conflated in the deliverables. Everything below is reproducible in
exact rational arithmetic (Python `fractions.Fraction`, no floating point).

## What the manuscript leaves open

`paper/main.tex`, Remark 5.6 (`rem:ncone`, line 493):

> For an $n$-cone pillow $\mathcal{O}(m_1,\dots,m_n)$ … the first $n$ leading heat
> coefficients again supply $n$ symmetric functions of the orders, and when these are
> independent they recover the multiset, so the upper bound $K\le n$ extends the $n=3$
> case of Theorem C. The matching lower bound $K\ge n$ for $n\ge4$ would require two
> $n$-cone pillows agreeing in $n-1$ prescribed symmetric functions — an $(n-1)$-fold
> simultaneous Egyptian-fraction and power-sum system — for which we have neither a
> construction nor a non-existence proof; we leave it open.

So for $n = 4$ the manuscript asks for two 4-cone hyperbolic pillows agreeing in
**three** symmetric functions: $R$, $S_1$, $P_3$.

## The construction, for n = 4

$$\mathcal{O}(3,10,15,30) \quad\text{and}\quad \mathcal{O}(4,5,21,28)$$

| Invariant | $(3,10,15,30)$ | $(4,5,21,28)$ | Equal? |
|---|---|---|---|
| $S_1=\sum m_i$ | 58 | 58 | **yes** |
| $R=\sum 1/m_i$ | $8/15$ | $8/15$ | **yes** |
| $P_3=\sum m_i^3$ | 31402 | 31402 | **yes** |
| $P_5=\sum m_i^5$ | 25159618 | 21298618 | no |

Both are hyperbolic: for a sphere with $n$ cone points the condition is
$\sum_i (1-1/m_i) > 2$, and here $4 - 8/15 = 52/15 > 2$ for both. The multisets are
distinct, so the orbifolds are non-isometric.

**Consequence.** These two 4-cone pillows are not separated by the first three heat
coefficients, so $K \ge 4$ for both. Combined with the manuscript's own upper bound
$K \le n = 4$, this gives $K = 4$ exactly — **the matching lower bound of Remark 5.6, for
$n = 4$, with an explicit witness.** The open problem as stated is answered for $n=4$.

**Minimality.** Over all 4-cone hyperbolic pillows with every order $\le 55$ (**395,009**
admissible multisets) the pair above is the *only* $(R,S_1,P_3)$ collision. Extending to
orders $\le 60$ (**557,844** multisets) adds exactly one more — its $\times 2$ scaling
$\{\mathcal{O}(6,20,30,60),\ \mathcal{O}(8,10,42,56)\}$ at $S_1 = 116$ — which cannot appear
in the $\le 55$ scan since it contains an order-60 cone. So $S_1 = 58$ is the minimal
cone-order sum at which three heat coefficients fail for $n = 4$ in both ranges, and the pair
is unique at that sum.

*(An earlier draft quoted 395,009 against orders $\le 60$; those two figures belong to
different scans and are now separated.)*

## The same for n = 5

$$\mathcal{O}(3,7,7,7,14) \quad\text{and}\quad \mathcal{O}(4,4,6,12,12)$$

share $S_1 = 38$, $R = 5/6$, $P_3 = 3800$, and are separated by $P_5$. This is the
minimal such pair for $n=5$ over all orders $\le 30$.

**Read this one carefully — it is weaker than the $n=4$ result.** It shows three
coefficients do not suffice for $n=5$, i.e. $K \ge 4$. Remark 5.6's matching bound for
$n = 5$ needs a pair agreeing in $n-1 = 4$ functions, $(R,S_1,P_3,P_5)$. A scan of all
5-cone pillows with orders $\le 26$ (118{,}755 multisets) found **no** such pair. So the
$n = 5$ case of Remark 5.6 remains open; only the $n=4$ case is settled here.

## The scaling law generalizes

The manuscript's Proposition 5.1 scales a 3-cone degeneracy by $k$. The same argument
works for any number of cone points *and any number of invariants*: under
$m_i \mapsto k m_i$, $S_1 \mapsto k S_1$, $R \mapsto R/k$, and $P_j \mapsto k^j P_j$.
Every equality is therefore preserved. So each witness above generates an infinite family,
which is why the $\times 2$ copy appears in the $n=4$ scan.

## Injectivity of the full invariant set, checked

| $n$ | invariants | orders searched | multisets | collisions |
|---|---|---|---|---|
| 3 | $(R,S_1)$ | $\le 60$ | — | 86 (incl. the manuscript's $(2,8,8)/(3,3,12)$) |
| 3 | $(R,S_1,P_3)$ | $\le 60$ | — | **0** — corroborates Theorem C |
| 4 | $(R,S_1,P_3)$ | $\le 55$ | 395{,}009 | 1 |
| 4 | $(R,S_1,P_3,P_5)$ | $\le 55$ | 395{,}009 | **0** |
| 5 | $(R,S_1,P_3)$ | $\le 26$ | 118{,}755 | 2 |
| 5 | $(R,S_1,P_3,P_5)$ | $\le 26$ | 118{,}755 | **0** |

## The load-bearing caveat

All of this assumes the $\ell$-th cone coefficient delivers $P_{2\ell+1}$ modulo lower-order
symmetric data — $t^1 \to P_3$, $t^2 \to P_5$, and so on. That pattern is what the
manuscript establishes for $\ell = 1$ and what Uçar's $\deg p_\ell = 2\ell+2$ (divided by
the $1/m$) predicts in general. **Whether $b_2$ actually delivers $P_5$ with a nonzero
coefficient at constant curvature is precisely question Q2**, and it is not settled by
this computation — it depends on what Schueth's $t^2$ cone formula actually says. If
$b_2$'s $m^5$ coefficient vanishes at constant curvature, the $P_5$ column above is not a
heat invariant and the $n=4$ upper bound argument fails, though the lower-bound witness
(which only uses $R, S_1, P_3$) survives regardless.

Because of that dependency the $n=4$ result should be stated to the author in two parts:

1. **Unconditional:** $\mathcal{O}(3,10,15,30)$ and $\mathcal{O}(4,5,21,28)$ agree in
   $(R,S_1,P_3)$, hence in the first three heat coefficients. So three coefficients do not
   determine a 4-cone hyperbolic pillow. This needs nothing beyond the manuscript's own
   Corollary D.
2. **Conditional on $b_2 \to P_5$:** they are separated by the fourth, giving $K = 4$
   exactly and settling Remark 5.6 for $n = 4$.

## Reproduction

Independent of the repository's existing scripts. Enumerate
`combinations_with_replacement(range(2, MAX+1), n)`, keep multisets with
$\sum_i(1-1/m_i) > 2$, key them on the exact `Fraction` tuple of invariants, and report
keys with multiplicity $> 1$.
