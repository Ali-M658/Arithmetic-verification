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
