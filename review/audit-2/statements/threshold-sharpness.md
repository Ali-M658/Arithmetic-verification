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
