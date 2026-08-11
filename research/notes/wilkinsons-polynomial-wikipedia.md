---
title: Wilkinson's polynomial - Wikipedia
id: wilkinsons-polynomial-wikipedia
tags:
- hyperbolic-pillow-heat-novelty-813161
- root-perturbation
- source-hub
created: '2026-08-09T08:46:22.698479Z'
updated: '2026-08-09T09:36:32.380659Z'
source: https://en.wikipedia.org/wiki/Wilkinson%27s_polynomial
source_domain: en.wikipedia.org
fetched_at: '2026-08-09T08:46:22.698092Z'
fetch_provider: builtin
status: evergreen
type: note
tier: institutional
content_type: article
deprecated: false
summary: 'SOURCE HUB (Wikipedia) -- ''Wilkinson''s polynomial,'' extract only, not
  citable directly. Recounts Wilkinson''s classic w(x) = prod_{i=1}^{20}(x-i) ill-conditioning
  example (Wilkinson 1963, ''Rounding Errors in Algebraic Processes,'' Prentice Hall)
  and states, with derivation, the exact standard root-perturbation formula the manuscript
  needs: for p(x)=prod(x-alpha_j) perturbed by t*c(x), the first-order root derivative
  is dalpha_j/dt = -c(alpha_j)/p''(alpha_j); specializing to c(x)=x^19 (perturbing
  one monomial coefficient) gives dalpha_j/dt = -alpha_j^19/prod_{k!=j}(alpha_j-alpha_k)
  = -prod_{k!=j} alpha_j/(alpha_j-alpha_k) -- an explicit confirmation that root sensitivity
  is governed by the reciprocal PRODUCT OF PAIRWISE GAPS to the other roots, exactly
  the mechanism in the manuscript''s Jacobian formula. Root alpha_1=1 has derivative
  1/19! (stable); root alpha_20=20 has derivative -20^19/19! ~ -4.3e7 (unstable),
  a factor of 20^19 ~= 5.24e24 difference, because the OTHER roots are close relative
  to alpha_20''s own magnitude. Primary citations extracted for direct fetching/citing:
  J.H. Wilkinson (1959) ''The evaluation of the zeros of ill-conditioned polynomials,
  Part I/II,'' Numer. Math. 1:150-166 (DOI 10.1007/BF01386381 / 10.1007/BF01386382);
  J.H. Wilkinson (1963) Rounding Errors in Algebraic Processes, Prentice Hall; J.H.
  Wilkinson (1984) ''The Perfidious Polynomial,'' in Studies in Numerical Analysis
  (ed. G.H. Golub), MAA, ISBN 978-0-88385-126-5.'
---

Wilkinson's polynomial - Wikipedia
Jump to content
From Wikipedia, the free encyclopedia
Polynomial in numerical analysis
Graph
of Wilkinson's polynomial
Graph of
sgn
⁡
(
w
(
x
)
)
ln
⁡
(
1
+
|
w
(
x
)
|
)
{\displaystyle \operatorname {sgn}(w(x))\ln(1+|w(x)|)}
In
numerical analysis
,
Wilkinson's polynomial
is a specific
polynomial
which was used by
James H. Wilkinson
in 1963 to illustrate a difficulty when
finding the roots
of a polynomial: the location of the
roots
can be very sensitive to perturbations in the
coefficients
of the polynomial.
The polynomial is
w
(
x
)
=
∏
i
=
1
20
(
x
−
i
)
=
(
x
−
1
)
(
x
−
2
)
⋯
(
x
−
20
)
.
{\displaystyle w(x)=\prod _{i=1}^{20}(x-i)=(x-1)(x-2)\cdots (x-20).}
Sometimes, the term
Wilkinson's polynomial
is also used to refer to some other polynomials appearing in Wilkinson's discussion.
Background
[
edit
]
Wilkinson's polynomial arose in the study of algorithms for finding the roots of a polynomial
p
(
x
)
=
∑
i
=
0
n
c
i
x
i
.
{\displaystyle p(x)=\sum _{i=0}^{n}c_{i}x^{i}.}
It is a natural question in numerical analysis to ask whether the problem of finding the roots of
p
from the coefficients
c
i
is
well-conditioned
.  That is, we hope that a small change in the coefficients will lead to a small change in the roots.  Unfortunately, this is not the case here.
The problem is ill-conditioned when the polynomial has a
multiple root
. For instance, the polynomial
x
2
has a double root at
x
= 0
. However, the polynomial
x
2
−
ε
(a perturbation of size
ε
) has roots at
±√
ε
, which is much bigger than
ε
when
ε
is small.
It is therefore natural to expect that ill-conditioning also occurs when the polynomial has zeros which are very close. However, the problem may also be extremely ill-conditioned for polynomials with well-separated zeros. Wilkinson used the polynomial
w
(
x
)
to illustrate this point (Wilkinson 1963).
In 1984, he described the personal impact of this discovery:
Speaking for myself I regard it as the most traumatic experience in my career as a numerical analyst.
[
1
]
Wilkinson's polynomial is often used to illustrate the undesirability of naively computing
eigenvalues
of a
matrix
by first calculating the coefficients of the matrix's
characteristic polynomial
and then finding its roots, since using the coefficients as an intermediate step may introduce an extreme ill-conditioning even if the original problem was well-conditioned.
[
2
]
Conditioning of Wilkinson's polynomial
[
edit
]
Wilkinson's polynomial
w
(
x
)
=
∏
i
=
1
20
(
x
−
i
)
=
(
x
−
1
)
(
x
−
2
)
⋯
(
x
−
20
)
{\displaystyle w(x)=\prod _{i=1}^{20}(x-i)=(x-1)(x-2)\cdots (x-20)}
clearly has 20 roots, located at
x
= 1, 2, ..., 20
. These roots are far apart. However, the polynomial is still very ill-conditioned.
Expanding the polynomial, one finds
w
(
x
)
=
x
20
−
210
x
19
+
20615
x
18
−
1256850
x
17
+
53327946
x
16
−
1672280820
x
15
+
40171771630
x
14
−
756111184500
x
13
+
11310276995381
x
12
−
135585182899530
x
11
+
1307535010540395
x
10
−
10142299865511450
x
9
+
63030812099294896
x
8
−
311333643161390640
x
7
+
1206647803780373360
x
6
−
3599979517947607200
x
5
+
8037811822645051776
x
4
−
12870931245150988800
x
3
+
13803759753640704000
x
2
−
8752948036761600000
x
+
2432902008176640000.
{\displaystyle {\begin{aligned}w(x)={}&x^{20}-210x^{19}+20615x^{18}-1256850x^{17}+53327946x^{16}\\&{}-1672280820x^{15}+40171771630x^{14}-756111184500x^{13}\\&{}+11310276995381x^{12}-135585182899530x^{11}\\&{}+1307535010540395x^{10}-10142299865511450x^{9}\\&{}+63030812099294896x^{8}-311333643161390640x^{7}\\&{}+1206647803780373360x^{6}-3599979517947607200x^{5}\\&{}+8037811822645051776x^{4}-12870931245150988800x^{3}\\&{}+13803759753640704000x^{2}-8752948036761600000x\\&{}+2432902008176640000.\end{aligned}}}
If the coefficient of
x
19
is decreased from −210 by 2
−23
to −210.0000001192, then the polynomial value
w
(20) decreases from 0 to −2
−23
20
19
= −6.25×10
17
, and the root at
x
= 20
grows to
x
≈ 20.8
. The roots at
x
= 18
and
x
= 19
collide into a double root at
x
≈ 18.62
which turns into a pair of
complex conjugate
roots at
x
≈ 19.5 ± 1.9
i
as the perturbation increases further. The 20 roots become (to 5 decimals)
1.00000
2.00000
3.00000
4.00000
5.00000
6.00001
6.99970
8.00727
8.91725
20.84691
10.09527
±
11.79363
±
13.99236
±
16.73074
±
19.50244
±
0.64350
i
1.65233
i
2.51883
i
2.81262
i
1.94033
i
{\displaystyle {\begin{array}{rrrrr}1.00000&2.00000&3.00000&4.00000&5.00000\\[8pt]6.00001&6.99970&8.00727&8.91725&20.84691\\[8pt]10.09527\pm {}&11.79363\pm {}&13.99236\pm {}&16.73074\pm {}&19.50244\pm {}\\[-3pt]0.64350i&1.65233i&2.51883i&2.81262i&1.94033i\end{array}}}
Some of the roots are greatly displaced, even though the change to the coefficient is tiny and the original roots seem widely spaced. Wilkinson showed by the stability analysis discussed in the next section that this behavior is related to the fact that some roots
α
(such as
α
= 15) have many roots
β
that are "close" in the sense that |
α
−
β
| is smaller than
|
α
|.
Wilkinson chose the perturbation of 2
−23
because his
Pilot ACE
computer had 30-bit
floating point
significands
, so for numbers around 210, 2
−23
was an error in the first bit position not represented in the computer. The two
real numbers
−210 and −210 − 2
−23
are represented by the same floating point number, which means that 2
−23
is the
unavoidable
error in representing a real coefficient close to −210 by a floating point number on that computer. The perturbation analysis shows that 30-bit coefficient
precision
is insufficient for separating the roots of Wilkinson's polynomial.
Stability analysis
[
edit
]
Suppose that we perturb a polynomial
p
(
x
) = Π (
x
−
α
j
)
with roots
α
j
by adding a small multiple
t
·
c
(
x
)
of a polynomial
c
(
x
)
, and ask how this affects the roots
α
j
. To first order, the change in the roots will be controlled by the
derivative
d
α
j
d
t
=
−
c
(
α
j
)
p
′
(
α
j
)
.
{\displaystyle {d\alpha _{j} \over dt}=-{c(\alpha _{j}) \over p^{\prime }(\alpha _{j})}.}
When the derivative is small, the roots will be more stable under variations of
t
, and
conversely
if this derivative is large the roots will be unstable. In particular,
if
α
j
is a multiple root, then the denominator vanishes. In this case, α
j
is usually not
differentiable
with respect to
t
(unless
c
happens to vanish there), and the roots will be extremely unstable.
For small values of
t
the perturbed root is given by the
power series
expansion in
t
α
j
+
d
α
j
d
t
t
+
d
2
α
j
d
t
2
t
2
2
!
+
⋯
{\displaystyle \alpha _{j}+{d\alpha _{j} \over dt}t+{d^{2}\alpha _{j} \over dt^{2}}{t^{2} \over 2!}+\cdots }
and one expects problems when |
t
| is larger than the
radius of convergence
of this power series, which is given by the smallest value of |
t
| such that the root
α
j
becomes multiple. A very crude estimate for this radius takes half the distance from
α
j
to the nearest root, and divides by the derivative above.
In the example of Wilkinson's polynomial of
degree
20, the roots are given by
α
j
=
j
for
j
= 1, ..., 20
, and
c
(
x
)
is equal to
x
19
.
So the derivative is given by
d
α
j
d
t
=
−
α
j
19
∏
k
≠
j
(
α
j
−
α
k
)
=
−
∏
k
≠
j
α
j
α
j
−
α
k
.
{\displaystyle {d\alpha _{j} \over dt}=-{\alpha _{j}^{19} \over \prod _{k\neq j}(\alpha _{j}-\alpha _{k})}=-\prod _{k\neq j}{\alpha _{j} \over \alpha _{j}-\alpha _{k}}.\,\!}
This shows that the root
α
j
will be less stable if there are many roots
α
k
close to
α
j
, in the sense that the distance
|α
j
−
α
k
| between them is smaller than |α
j
|.
Example
. For the root α
1
= 1, the derivative is equal to 1/19! which is very small; this root is stable even for large changes in
t
. This is because all the other roots
β
are a long way from it, in the sense that |
α
1
−
β
| = 1, 2, 3, ..., 19 is larger than |
α
1
|
= 1.
For example, even if
t
is as large as –10000000000, the root
α
1
only changes from 1 to about 0.99999991779380 (which is very close to the first order approximation 1
+
t
/19! ≈ 0.99999991779365). Similarly, the other small roots of Wilkinson's polynomial are insensitive to changes in
t
.
Example
. On the other hand, for the root
α
20
= 20, the derivative is equal to −20
19
/19!  which is huge (about 43000000), so this root is very sensitive to small changes in
t
. The other roots
β
are close to
α
20
, in the sense that |
β
−
α
20
| = 1, 2, 3, ..., 19 is less than |
α
20
| = 20. For
t
= −2
−23
, the first-order approximation 20
−
t
·20
19
/19! = 25.137... to the perturbed root 20.84... is terrible; this is even more obvious for the root
α
19
where the perturbed root has a large
imaginary part
but the first-order approximation (and for that matter all higher-order approximations) are real. The reason for this discrepancy is that |
t
|  ≈ 0.000000119 is greater than the radius of convergence of the power series mentioned above (which is about 0.0000000029, somewhat smaller than the value 0.00000001 given by the crude estimate) so the linearized theory does not apply. For a value such as
t
= 0.000000001 that is significantly smaller than this radius of convergence, the first-order approximation 19.9569... is reasonably close to the root 19.9509...
At first sight the roots
α
1
= 1 and
α
20
= 20 of Wilkinson's polynomial appear to be similar, as they are on opposite ends of a symmetric line of roots, and have the same set of distances 1, 2, 3, ..., 19 from other roots. However the analysis above shows that this is grossly misleading: the root
α
20
= 20 is less stable than
α
1
= 1 (to small perturbations in the coefficient of
x
19
) by a factor of 20
19
= 5242880000000000000000000.
Wilkinson's second example
[
edit
]
The second example considered by Wilkinson is
w
2
(
x
)
=
∏
i
=
1
20
(
x
−
2
−
i
)
=
(
x
−
2
−
1
)
(
x
−
2
−
2
)
⋯
(
x
−
2
−
20
)
.
{\displaystyle w_{2}(x)=\prod _{i=1}^{20}(x-2^{-i})=(x-2^{-1})(x-2^{-2})\cdots (x-2^{-20}).}
The twenty roots of this polynomial are in a
geometric progression
with common ratio 2, and hence the quotient
α
j
α
j
−
α
k
{\displaystyle \alpha _{j} \over \alpha _{j}-\alpha _{k}}
cannot be large. Indeed, the roots of
w
2
are quite stable to large
relative
changes in the coefficients.
The effect of the basis
[
edit
]
The expansion
p
(
x
)
=
∑
i
=
0
n
c
i
x
i
{\displaystyle p(x)=\sum _{i=0}^{n}c_{i}x^{i}}
expresses the polynomial in a particular
basis
, namely that of the
monomials
. If the polynomial is expressed in another basis, then the problem of finding its roots may cease to be ill-conditioned. For example, in a
Lagrange form
, a small change in one (or several) coefficients need not change the roots too much.  Indeed, the basis polynomials for interpolation at the points 0, 1, 2, ..., 20 are
ℓ
k
(
x
)
=
∏
i
=
0
,
…
,
20
i
≠
k
x
−
i
k
−
i
,
for
k
=
0
,
…
,
20.
{\displaystyle \ell _{k}(x)=\prod _{i=0,\ldots ,20 \atop i\neq k}{\frac {x-i}{k-i}},\qquad {\text{for}}\quad k=0,\ldots ,20.}
Every polynomial (of degree 20 or less) can be expressed in this basis:
p
(
x
)
=
∑
i
=
0
20
d
i
ℓ
i
(
x
)
.
{\displaystyle p(x)=\sum _{i=0}^{20}d_{i}\ell _{i}(x).}
For Wilkinson's polynomial, we find
w
(
x
)
=
(
20
!
)
ℓ
0
(
x
)
=
∑
i
=
0
20
d
i
ℓ
i
(
x
)
with
d
0
=
(
20
!
)
,
d
1
=
d
2
=
⋯
=
d
20
=
0.
{\displaystyle w(x)=(20!)\ell _{0}(x)=\sum _{i=0}^{20}d_{i}\ell _{i}(x)\quad {\text{with}}\quad d_{0}=(20!),\,d_{1}=d_{2}=\cdots =d_{20}=0.}
Given the definition of the Lagrange basis polynomial
ℓ
0
(
x
)
, a change in the coefficient
d
0
will produce no change in the roots of
w
.  However, a perturbation in the other coefficients (all equal to zero) will slightly change the roots. Therefore, Wilkinson's polynomial is well-conditioned in this basis.
Notes
[
edit
]
↑
Wilkinson, James H.
(1984). "The perfidious polynomial". In Gene H. Golub (ed.).
Studies in Numerical Analysis
. Mathematical Association of America. p.
3.
ISBN
978-0-88385-126-5
.
↑
Trefethen, Lloyd N.; Bau, David (1997),
Numerical Linear Algebra
, SIAM
References
[
edit
]
Wilkinson discussed "his" polynomial in
J. H. Wilkinson (1959). The evaluation of the zeros of ill-conditioned polynomials. Part I.
Numerische Mathematik
1
:150–166.
J. H. Wilkinson (1963).
Rounding Errors in Algebraic Processes
.  Englewood Cliffs, New Jersey: Prentice Hall.
It is mentioned in standard text books in numerical analysis, like
F. S. Acton,
Numerical methods that work
,
ISBN
978-0-88385-450-1
, p.
201.
Other references:
Ronald G. Mosier (July 1986). Root neighborhoods of a polynomial.
Mathematics of Computation
47
(175):265–273.
J. H. Wilkinson (1984). The perfidious polynomial in
Studies in Numerical Analysis
, ed. by G. H. Golub, pp.
1–28. (Studies in Mathematics, vol. 24). Washington, D.C.: Mathematical Association of America.
A high-precision numerical computation is presented in:
Ray Buvel,
Polynomials And Rational Functions
, part of the
RPN Calculator User Manual
(for Python), retrieved on 29 July 2006.
Retrieved from "
https://en.wikipedia.org/w/index.php?title=Wilkinson%27s_polynomial&oldid=1356011114
"
Categories
:
Numerical analysis
Polynomials
Hidden categories:
Articles with short description
Short description is different from Wikidata
Use dmy dates from January 2020
Search
Search
Wilkinson's polynomial
7 languages
Add topic