---
title: The Prouhet–Tarry–Escott problem for subsets with small doubling in integral
  domains
id: the-prouhettarryescott-problem-for-subsets-with-small-doubling-in-integral-domai
tags:
- round1-citations
created: '2026-10-06T17:36:54.882697Z'
source: https://arxiv.org/html/2609.05061v1
source_domain: arxiv.org
fetched_at: '2026-10-06T17:36:54.881956Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
---

The Prouhet–Tarry–Escott problem for subsets with small doubling in integral domains
Title:
Content selection saved. Describe the issue below:
Description:
arXiv is now an independent nonprofit!
Learn more
×
License: arXiv.org perpetual non-exclusive license
arXiv:2609.05061v1 [math.NT] 04 Sep 2026
The Prouhet–Tarry–Escott problem for subsets with small doubling in integral domains
Ernie Croot
Address:
School of Mathematics
Georgia Institute of Technology
Atlanta, GA 30332
United States
Email address:
ernest.croot@math.gatech.edu
,
Junzhe Mao
Address:
School of Mathematics
Georgia Institute of Technology
Atlanta, GA 30332
United States
Email address:
jmao87@gatech.edu
and
Chi Hoi Yip
Address:
Department of Mathematics, Hong Kong University of Science and Technology, Clear Water Bay, Hong Kong
Email address:
machyip@ust.hk
Abstract.
The Prouhet–Tarry–Escott (PTE) problem has many generalizations and has
been studied in various algebraic domains. In this paper, we prove that finite
subsets
S
S
of integral domains with small additive doubling constant (but
still a power of
|
S
|
|S|
) always contain solutions to Wright’s generalization
of the PTE problem: there are small subsets
A
A
and
B
B
of the same size
such that
∑
a
∈
A
a
j
=
∑
b
∈
B
b
j
\sum_{a\in A}a^{j}=\sum_{b\in B}b^{j}
for
1
≤
j
≤
k
1\leq j\leq k
, but not
for
j
=
k
+
1
j=k+1
. More generally, our method gives simultaneous solutions for
m
m
systems, with pairwise distinct
(
k
+
1
)
(k+1)
-th power sums. In contrast with
the classical case
S
⊆
[
N
]
S\subseteq[N]
, where the problem has been studied by
Wooley and others using Vinogradov’s mean value theorem, our approach is based
on polynomial identities and additive properties of
S
S
. We also discuss
barriers to extending these results to broader settings.
Key words and phrases:
Prouhet–Tarry–Escott problem, Hilbert cubes, Vinogradov’s mean value theorem, Sidon sets
2020 Mathematics Subject Classification
Primary 11B30; Secondary 11D72, 11P05
1.
Introduction
The Prouhet–Tarry–Escott (PTE) problem is that of finding two distinct, non-decreasing sequences of integers
a
1
,
a
2
,
…
,
a
s
a_{1},a_{2},\ldots,a_{s}
and
b
1
,
b
2
,
…
,
b
s
b_{1},b_{2},\ldots,b_{s}
, such that
(1)
∑
i
=
1
s
a
i
j
=
∑
i
=
1
s
b
i
j
(
1
≤
j
≤
k
)
.
\sum_{i=1}^{s}a_{i}^{j}\ =\ \sum_{i=1}^{s}b_{i}^{j}\quad(1\leq j\leq k).
The PTE problem has a long history and has been studied extensively. There are many well-studied generalizations and variants of the PTE problem. We refer to
[
24
,
19
]
for some historical notes as well as the survey
[
2
,
4
]
.
In this paper, we focus on variants of the PTE problem introduced by Wright. One variant of the PTE problem was introduced by Wright
[
25
]
, where he looked for solutions to (
1
) with the extra condition that
∑
i
=
1
s
a
i
k
+
1
≠
∑
i
=
1
s
b
i
k
+
1
\sum_{i=1}^{s}a_{i}^{k+1}\neq\sum_{i=1}^{s}b_{i}^{k+1}
. In subsequent work
[
23
,
24
]
, Wright also considered nontrivial solutions to the simultaneous Diophantine equations
(2)
∑
i
=
1
s
x
i
​
1
j
=
∑
i
=
1
s
x
i
​
2
j
=
⋯
=
∑
i
=
1
s
x
i
​
m
j
(
1
≤
j
≤
k
)
.
\sum_{i=1}^{s}x_{i1}^{j}=\sum_{i=1}^{s}x_{i2}^{j}=\cdots=\sum_{i=1}^{s}x_{im}^{j}\quad(1\leq j\leq k).
Let
P
⁡
(
k
,
m
)
P(k,m)
denote the least
s
s
for which equation (
2
) has an integer solution
𝐱
\mathbf{x}
in which the sets
{
x
1
​
h
,
…
,
x
s
​
h
}
​
(
1
≤
h
≤
m
)
\{x_{1h},\ldots,x_{sh}\}(1\leq h\leq m)
are distinct. Similarly, let
W
⁡
(
k
,
m
)
W(k,m)
denote the least
s
s
such that equation (
2
) has an integer solution
𝐱
\mathbf{x}
with
∑
i
=
1
s
x
i
​
h
k
+
1
≠
∑
i
=
1
s
x
i
​
t
k
+
1
​
(
h
≠
t
)
\sum_{i=1}^{s}x_{ih}^{k+1}\neq\sum_{i=1}^{s}x_{it}^{k+1}(h\neq t)
.
It is easy to see
P
⁡
(
k
,
2
)
≥
k
+
1
P(k,2)\geq k+1
and it is an open problem to determine if
P
⁡
(
k
,
2
)
=
k
+
1
P(k,2)=k+1
. It is only known that
P
⁡
(
k
,
2
)
=
k
+
1
P(k,2)=k+1
when
2
≤
k
≤
9
2\leq k\leq 9
and
k
=
11
k=11
[
4
]
. Using a pigeonhole principle argument one can easily see that
P
⁡
(
k
,
m
)
≤
k
⁡
(
k
+
1
)
2
+
1
P(k,m)\leq\frac{k(k+1)}{2}+1
. However, the pigeonhole principle does not readily yield an upper bound on
W
⁡
(
k
,
2
)
W(k,2)
. Nonetheless, Hua
[
10
,
11
]
and Wright
[
24
]
were able to provide upper bounds on
W
⁡
(
k
,
m
)
W(k,m)
using elementary arguments.
By considering solutions to equation (
2
) with
x
i
​
h
∈
[
N
]
:=
{
1
,
2
,
…
,
N
}
x_{ih}\in[N]:=\{1,2,\ldots,N\}
, one can see that estimating
W
⁡
(
k
,
m
)
W(k,m)
is related to Vinogradov’s mean value theorem. The best-known upper bound is
W
⁡
(
k
,
m
)
≤
k
⁡
(
k
+
1
)
2
+
1
W(k,m)\ \leq\ \frac{k(k+1)}{2}+1
, due to Wooley
[
22
, Theorem 13.1]
.
These results of Hua, Wright, and Wooley, as well as the work of Bourgain–Demeter–Guth
[
5
]
, leverage properties of dense subsets of integer intervals
[
N
]
=
{
1
,
2
,
…
,
N
}
[N]=\{1,2,\ldots,N\}
, as we will discuss in Section
1.2
.
However, it is not immediately obvious how to extend these proofs to the case where the solutions are restricted to being contained in sparse subsets of the integers. In this paper, we address this question for when those sparse subsets have some additive structure, specifically that they have “small doubling constant” or “high additive energy”; although our proof gives only an exponential-in-
k
k
upper bound on
s
s
, the number of variables in each system.
It is worth mentioning that the systems (
1
) and (
2
) make sense over any ring. In particular, there have been studies on the PTE problem in Gaussian integers, Eisenstein integers, finite fields, function fields, and number fields; see for example
[
1
,
6
,
7
,
12
,
15
,
22
]
.
In this paper we will also study equation (
1
) over an arbitrary ring (not necessarily commutative) and equation (
2
) over an integral domain for technical reasons. Recall that an
integral domain
is a nonzero commutative ring with a multiplicative identity that has no zero divisors.
1.1.
Main results
We now state the main theorem of the paper.
Theorem 1.1
.
Let
k
≥
1
k\geq 1
,
m
≥
2
m\geq 2
be two integers. There is a constant
c
>
0
c>0
depending on
k
k
and
m
m
, such that the following holds. Suppose
R
R
is a ring and
S
⊆
R
S\subseteq R
is a nonempty finite subset satisfying
|
S
−
S
|
=
K
​
|
S
|
,
where
​
K
≤
c
​
|
S
|
1
/
(
2
k
+
1
−
1
)
,
|S-S|\ =\ K|S|,\ {\rm where}\ K\leq c|S|^{1/(2^{k+1}-1)},
then
(1)
There exist distinct
A
1
,
A
2
,
…
,
A
m
⊆
S
A_{1},A_{2},\ldots,A_{m}\subseteq S
,
|
A
i
|
=
⌈
log
2
⁡
m
⌉
​
2
k
|A_{i}|=\lceil\log_{2}m\rceil 2^{k}
, such that
∑
a
∈
A
i
a
j
=
∑
b
∈
A
1
b
j
for
​
j
=
1
,
…
,
k
,
and
​
i
=
1
,
…
,
m
.
\sum_{a\in A_{i}}a^{j}\ =\ \sum_{b\in A_{1}}b^{j}\qquad{\rm for\ }j=1,\ldots,k,\ {\rm and\ }i=1,\ldots,m.
(2)
Assume additionally that
R
R
is an integral domain with characteristic
char
⁡
(
R
)
=
0
\mathrm{char}(R)=0
or
char
⁡
(
R
)
>
k
+
1
\mathrm{char}(R)>k+1
. Then
there exist
A
1
,
A
2
,
…
,
A
m
⊆
S
A_{1},A_{2},\ldots,A_{m}\subseteq S
,
|
A
i
|
=
⌈
log
2
⁡
m
⌉
​
2
k
|A_{i}|=\lceil\log_{2}m\rceil 2^{k}
, such that
∑
a
∈
A
i
a
j
=
∑
b
∈
A
1
b
j
for
​
j
=
1
,
…
,
k
,
and
​
i
=
1
,
…
,
m
,
\sum_{a\in A_{i}}a^{j}\ =\ \sum_{b\in A_{1}}b^{j}\qquad{\rm for\ }j=1,\ldots,k,\ {\rm and\ }i=1,\ldots,m,
while for all
h
,
t
=
1
,
2
,
…
,
m
,
h
≠
t
h,t=1,2,\ldots,m,\ h\neq t
, we have
∑
a
∈
A
h
a
k
+
1
≠
∑
b
∈
A
t
b
k
+
1
.
\sum_{a\in A_{h}}a^{k+1}\ \neq\ \sum_{b\in A_{t}}b^{k+1}.
Theorem
1.1
can be applied in a wide range of settings, for example generalized arithmetic progressions, finite fields with large characteristic, polynomials over finite fields with bounded degree, and algebraic integers with bounded norm.
A special case of Theorem
1.1
is the following, which is formulated in a slightly different way.
Theorem 1.2
.
Let
k
k
be a positive integer. Suppose
R
R
is an integral domain with characteristic
char
⁡
(
R
)
=
0
\mathrm{char}(R)=0
or
char
⁡
(
R
)
>
k
+
1
\mathrm{char}(R)>k+1
. Then there is a positive integer
N
=
N
⁡
(
k
)
N=N(k)
such that for any finite subset
T
⊆
R
T\subseteq R
with
|
T
|
≥
N
|T|\geq N
and any
S
⊆
T
S\subseteq T
of size
|
S
|
≥
(
24
​
|
T
−
T
|
)
1
−
1
/
2
k
+
1
|S|\geq(24|T-T|)^{1-1/2^{k+1}}
, there exist
A
,
B
⊆
S
A,B\subseteq S
,
|
A
|
=
|
B
|
=
2
k
|A|=|B|=2^{k}
, such that
∑
a
∈
A
a
j
=
∑
b
∈
B
b
j
,
for
j
=
1
,
…
,
k
,
\sum_{a\in A}a^{j}\ =\ \sum_{b\in B}b^{j},\ {\rm for\ }j=1,\ldots,k,
while
∑
a
∈
A
a
k
+
1
≠
∑
b
∈
B
b
k
+
1
.
\sum_{a\in A}a^{k+1}\ \neq\ \sum_{b\in B}b^{k+1}.
Using Plünnecke–Ruzsa inequality (see for example
[
13
]
), when
|
S
+
S
|
≤
K
′
​
|
S
|
|S+S|\leq K^{\prime}|S|
, we have
|
S
−
S
|
≤
K
′
2
​
|
S
|
|S-S|\leq K^{\prime 2}|S|
. This allows us to deduce a version of Theorem
1.1
for sets with small doubling constant. We can also deduce a corollary for sets with large additive energy using the best quantitative version of the Balog–Szemerédi–Gowers theorem
[
9
]
by Reiher–Schoen
[
16
]
:
Corollary 1.3
.
The conclusion of Theorem
1.1
remains valid if the hypothesis
on
|
S
−
S
|
|S-S|
is replaced by the following additive-energy hypothesis:
E
(
S
)
:=
#
{
a
1
,
a
2
,
b
1
,
b
2
∈
S
:
a
1
+
a
2
=
b
1
+
b
2
}
>
c
′
|
S
|
3
−
1
5
​
(
2
k
+
1
−
1
)
,
{\rm E}(S)\ :=\ \#\{a_{1},a_{2},b_{1},b_{2}\in S\ :\ a_{1}+a_{2}=b_{1}+b_{2}\}\ >\ c^{\prime}|S|^{3-\frac{1}{5(2^{k+1}-1)}},
where
c
′
>
0
c^{\prime}>0
is some constant depending only on
k
k
and
m
m
.
We briefly outline the proof of Theorem
1.1
here. By exploiting the additive properties of
S
S
, we first find several disjoint large Hilbert cubes in
S
S
, whose generators satisfy certain algebraic constraints. Then we use polynomial identities to construct solutions based on these Hilbert cubes.
In the classical setting when
R
=
ℤ
R=\mathbb{Z}
and
T
=
[
N
]
T=[N]
, Theorem
1.2
allows us to find a solution to the system of equations with
2
k
+
1
2^{k+1}
variables in any subset
S
⊆
[
N
]
S\subseteq[N]
with
|
S
|
≫
k
N
1
−
1
/
(
2
k
+
1
−
1
)
|S|\gg_{k}N^{1-1/(2^{k+1}-1)}
. As shown by Wooley and others, using Vinogradov’s mean value theorem, the bounds on
|
S
|
|S|
and
|
A
|
,
|
B
|
|A|,|B|
can be improved. We refer to Corollary
1.6
for a general version. In contrast, we do not have such powerful tools to estimate the number of solutions to equations (
1
) and (
2
) in an arbitrary subset of a general ring.
In a different direction, one can ask about lower bounds. For example, given some integers
s
s
and
k
k
, how large must
S
⊆
[
N
]
S\subseteq[N]
be in order to guarantee that sets
A
,
B
⊆
S
A,B\subseteq S
with
|
A
|
=
|
B
|
≤
s
|A|=|B|\leq s
exist, such that equation (
1
) holds, but
that the sums do not equal when
j
=
k
+
1
j=k+1
? And what about subsets of general rings? These questions are partially addressed in Section
3
, though the bounds produced are very far from the upper-bound results appearing in Theorem
1.1
and Corollary
1.6
below. We also remark that there might be a way to employ polynomial methods to produce lower bounds. For example, Borwein and Mossinghoff
[
3
]
connected a variant of the PTE problem to a question about polynomials with high-order vanishing at
1
1
.
Some Additional Remarks:
•
First, the assumption on the characteristic of
R
R
in Theorem
1.1
(2) cannot be omitted entirely. To see this, consider the case where
R
R
has characteristic
p
p
and
p
|
(
k
+
1
)
p\mid(k+1)
. In this case we would have
∑
a
∈
A
a
k
+
1
=
(
∑
a
∈
A
a
(
k
+
1
)
/
p
)
p
=
(
∑
b
∈
B
b
(
k
+
1
)
/
p
)
p
=
∑
b
∈
B
b
k
+
1
.
\sum_{a\in A}a^{k+1}=\left(\sum_{a\in A}a^{(k+1)/p}\right)^{p}=\left(\sum_{b\in B}b^{(k+1)/p}\right)^{p}=\sum_{b\in B}b^{k+1}.
Thus, the conclusion in Theorem
1.1
(2) cannot hold.
•
Second, we will show in Proposition
2.5
that improving the
2
k
2^{k}
for the size of the sets
A
A
and
B
B
in Theorem
1.2
to something closer to
k
2
k^{2}
would require a different method than ours, or at least would require adding substantial new ingredients.
•
Third, as we will see in the remark following Corollary
1.6
below, one cannot, in general, prove such a corollary just assuming the hypotheses of Theorem
1.1
. That is, the ability to pick and choose the exponents
j
j
where the
∑
a
∈
A
a
j
≠
∑
b
∈
B
b
j
\sum_{a\in A}a^{j}\neq\sum_{b\in B}b^{j}
is quite limited.
1.2.
Results from the literature and some further directions
Given two positive integers
s
,
k
s,k
, let
J
s
,
k
​
(
N
)
J_{s,k}(N)
denote the number of solutions to equation (
1
) with
a
i
,
b
i
∈
[
N
]
a_{i},b_{i}\in[N]
. Then we know
J
s
,
k
(
N
)
=
∫
𝕋
k
|
∑
1
≤
n
≤
N
e
(
α
1
n
+
⋯
+
α
k
n
k
)
|
2
​
s
d
α
1
⋯
d
α
k
,
J_{s,k}(N)=\int_{\mathbb{T}^{k}}\bigg|\sum_{1\leq n\leq N}e(\alpha_{1}n+\cdots+\alpha_{k}n^{k})\bigg|^{2s}d\alpha_{1}\cdots d\alpha_{k},
where
𝕋
=
ℝ
/
ℤ
\mathbb{T}=\mathbb{R}/\mathbb{Z}
.
Recall that Vinogradov’s mean value theorem provides an almost sharp upper bound
(3)
J
s
,
k
(
N
)
≪
s
,
k
,
ε
N
ε
(
N
s
+
N
2
​
s
−
k
⁡
(
k
+
1
)
/
2
)
.
J_{s,k}(N)\ll_{s,k,\varepsilon}N^{\varepsilon}(N^{s}+N^{2s-k(k+1)/2}).
In the famous work of Bourgain–Demeter–Guth
[
5
]
and Wooley
[
20
,
22
]
, they established Vinogradov’s mean value theorem together with some generalizations. We refer to the survey by Pierce
[
14
]
for further discussion.
In
[
22
, Corollary 1.4]
Wooley proved the following generalization of Vinogradov’s mean value theorem:
Theorem 1.4
(Wooley)
.
Let
s
,
k
∈
ℕ
s,k\in\mathbb{N}
,
ε
>
0
\varepsilon>0
,
(
a
n
)
n
∈
ℤ
(a_{n})_{n\in\mathbb{Z}}
be a sequence of complex numbers. Then
∫
𝕋
k
|
∑
|
n
|
≤
N
a
n
e
(
α
1
n
+
⋯
+
α
k
n
k
)
|
2
​
s
d
α
1
⋯
d
α
k
\displaystyle\int_{\mathbb{T}^{k}}\bigg|\sum_{|n|\leq N}a_{n}e(\alpha_{1}n+\cdots+\alpha_{k}n^{k})\bigg|^{2s}d\alpha_{1}\cdots d\alpha_{k}
≪
s
,
k
,
ε
N
ε
(
1
+
N
s
−
k
⁡
(
k
+
1
)
/
2
)
(
∑
|
n
|
≤
N
|
a
n
|
2
)
s
.
\displaystyle\ll_{s,k,\varepsilon}N^{\varepsilon}(1+N^{s-k(k+1)/2})\bigg(\sum_{|n|\leq N}|a_{n}|^{2}\bigg)^{s}.
Following a simple counting argument (see for example
[
21
, Section 8]
), one can deduce the following corollary of Theorem
1.4
.
Corollary 1.5
.
Suppose that
t
≥
1
t\geq 1
and that
k
1
,
…
,
k
t
k_{1},\ldots,k_{t}
are positive integers with
1
≤
k
1
<
k
2
<
⋯
<
k
t
=
k
1\leq k_{1}<k_{2}<\cdots<k_{t}=k
. Let
s
≥
k
⁡
(
k
+
1
)
/
2
s\geq k(k+1)/2
, and write
K
=
k
1
+
⋯
+
k
t
K=k_{1}+\cdots+k_{t}
. Then for any
ε
>
0
\varepsilon>0
, and any sequence
c
−
N
,
…
,
c
N
∈
ℂ
c_{-N},\ldots,c_{N}\in{\mathbb{C}}
, one has
(4)
∫
𝕋
t
|
∑
|
n
|
≤
N
c
n
e
(
α
1
n
k
1
+
⋯
+
α
t
n
k
t
)
|
2
​
s
d
α
1
⋯
d
α
t
≪
s
,
k
,
ε
N
s
−
K
+
ε
(
∑
|
n
|
≤
N
|
c
n
|
2
)
s
.
\displaystyle\int_{\mathbb{T}^{t}}\bigg|\sum_{|n|\leq N}c_{n}e(\alpha_{1}n^{k_{1}}+\cdots+\alpha_{t}n^{k_{t}})\bigg|^{2s}d\alpha_{1}\cdots d\alpha_{t}\ll_{s,k,\varepsilon}N^{s-K+\varepsilon}\left(\sum_{|n|\leq N}|c_{n}|^{2}\right)^{s}.
As an application, Corollary
1.5
will imply the following result (proved in Section
4
), providing bounds for a generalization of the function
W
⁡
(
k
,
m
)
W(k,m)
. In particular, it generalizes a result of Wooley
[
22
, Theorem 13.1]
.
Corollary 1.6
.
For every
k
≥
1
k\geq 1
and every proper subset
J
⊂
{
1
,
2
,
…
,
k
}
J\subset\{1,2,\ldots,k\}
, if
N
≥
N
0
​
(
k
)
N\geq N_{0}(k)
, then for any integer
m
≥
2
m\geq 2
and
S
⊆
[
N
]
S\subseteq[N]
satisfying
|
S
|
≥
m
2
/
k
⁡
(
k
+
1
)
​
N
1
−
2
/
(
k
2
+
k
+
1
)
|S|\geq m^{2/k(k+1)}N^{1-2/(k^{2}+k+1)}
, there exist
A
1
,
A
2
,
…
,
A
m
⊆
S
A_{1},A_{2},\ldots,A_{m}\subseteq S
,
each of size
s
=
k
⁡
(
k
+
1
)
/
2
,
s\ =\ k(k+1)/2,
such that
∑
a
∈
A
i
a
j
=
∑
b
∈
A
1
b
j
,
for
j
∈
J
,
and
i
=
1
,
…
,
m
.
\sum_{a\in A_{i}}a^{j}\ =\ \sum_{b\in A_{1}}b^{j},\ {\rm for\ }j\in J,\ {\rm and}\ i=1,\ldots,m.
while for any
1
≤
h
<
t
≤
m
1\leq h<t\leq m
,
∑
a
∈
A
h
a
j
≠
∑
b
∈
A
t
b
j
,
for
​
j
∈
{
1
,
2
,
…
,
k
}
∖
J
.
\sum_{a\in A_{h}}a^{j}\neq\sum_{b\in A_{t}}b^{j},\ {\rm for}\ j\in\{1,2,\ldots,k\}\setminus J.
Remark 1.7
.
The following shows that we cannot get a result like this just assuming
S
S
is an arbitrary subset of integers with small doubling constant like in Theorem
1.1
: if we take
S
=
{
1
+
r
M
:
r
=
1
,
2
,
…
,
n
}
S=\{1+rM\ :\ r=1,2,\ldots,n\}
, then for
M
M
large enough, if
A
,
B
⊆
S
A,B\subseteq S
, we have
A
=
{
1
+
a
i
M
:
i
=
1
,
…
,
s
}
A=\{1+a_{i}M\ :\ i=1,\ldots,s\}
and
B
=
{
1
+
b
i
M
:
i
=
1
,
…
,
s
}
B=\{1+b_{i}M\ :\ i=1,\ldots,s\}
, where the
a
i
,
b
i
a_{i},b_{i}
are in
{
1
,
…
,
n
}
\{1,\ldots,n\}
. Then, if
∑
i
=
1
s
(
1
+
a
i
​
M
)
j
≠
∑
i
=
1
s
(
1
+
b
i
​
M
)
j
\sum_{i=1}^{s}(1+a_{i}M)^{j}\neq\sum_{i=1}^{s}(1+b_{i}M)^{j}
, expanding out the terms (using the binomial theorem) one sees this implies that for some
h
≤
j
h\leq j
,
∑
i
=
1
s
a
i
h
≠
∑
i
=
1
s
b
i
h
\sum_{i=1}^{s}a_{i}^{h}\neq\sum_{i=1}^{s}b_{i}^{h}
; and so, for any
j
′
≥
h
j^{\prime}\geq h
we would have to have
∑
i
=
1
s
(
1
+
a
i
​
M
)
j
′
≠
∑
i
=
1
s
(
1
+
b
i
​
M
)
j
′
\sum_{i=1}^{s}(1+a_{i}M)^{j^{\prime}}\neq\sum_{i=1}^{s}(1+b_{i}M)^{j^{\prime}}
. Therefore, the only choices of
J
J
like in Corollary
1.6
that would work for this set would be ones of the form
J
=
{
1
,
2
,
…
,
m
}
J=\{1,2,\ldots,m\}
for some
m
≤
k
m\leq k
.
Results similar to Corollary
1.6
can also be proved in number fields/function fields as a consequence of Vinogradov’s mean value theorem in number fields and function fields proved by Wooley
[
22
]
. The remark above also applies to the number field/function field setting.
An example consequence of Corollary
1.6
is the following corollary related to a theorem of Friedlander and Lagarias on smooth numbers in short intervals
[
8
, Theorem 4]
:
Corollary 1.8
.
For integers
r
≥
3
r\geq 3
of the form
k
⁡
(
k
+
1
)
/
2
k(k+1)/2
, real numbers
0
<
α
<
1
(
r
+
1
)
​
2
​
r
0<\alpha<{1\over(r+1)\sqrt{2r}}
, integers
N
>
N
0
​
(
α
,
r
)
N>N_{0}(\alpha,r)
, and
sets of integers
C
⊆
[
1
,
N
1
/
r
]
,
|
C
|
>
N
(
1
−
α
)
/
r
,
C\ \subseteq\ [1,N^{1/r}],\ |C|>N^{(1-\alpha)/r},
there exists some constant
κ
=
κ
⁡
(
α
,
r
)
>
0
\kappa=\kappa(\alpha,r)>0
, an integer
M
<
N
M<N
, and an increasing sequence of integers
x
1
,
x
2
,
…
,
x
n
∈
[
1
,
2
​
M
]
,
n
>
κ
​
M
1
2
​
r
5
/
2
​
(
r
+
1
)
−
α
r
2
,
x_{1},\ x_{2},\ \ldots,\ x_{n}\in[1,2M],\ n\ >\ \kappa M^{\frac{1}{\sqrt{2}r^{5/2}(r+1)}-\frac{\alpha}{r^{2}}},
each the product of exactly
r
r
numbers from
C
C
, such that for all
1
≤
i
≤
n
−
1
1\leq i\leq n-1
,
x
i
+
1
−
x
i
=
κ
​
M
1
−
2
r
+
ε
i
,
where
​
1
r
≤
ε
i
≤
3
r
.
x_{i+1}-x_{i}\ =\ \kappa M^{1-\sqrt{2\over r}+\varepsilon_{i}},\ {\rm where\ }\frac{1}{r}\leq\varepsilon_{i}\leq{3\over r}.
Remark 1.9
.
The proof of
[
8
, Theorem 4]
, like the
proof of Corollary
1.8
, forms products of small integers, up to
N
1
/
r
N^{1/r}
; however, it does not allow one to choose the set
C
C
from which to draw the factors as we do above. On the other hand, our corollary pays a price by not requiring the
r
r
-fold products to come close to every integer in
[
1
,
N
]
[1,N]
.
In Section
4.2
, we state and prove a more general corollary (Corollary
4.2
) of Corollary
1.6
from which it can be derived.
The results above motivate the following questions:
•
Can one improve the strength of Theorem
1.4
above, so that we get a result like Corollary
1.6
just when
|
S
|
≫
m
N
θ
|S|\gg_{m}N^{\theta}
, for some
θ
∈
(
0
,
1
)
\theta\in(0,1)
that does not depend on
k
k
? For example, can one replace
|
S
|
≫
m
N
1
−
2
/
(
k
2
+
k
+
1
)
|S|\gg_{m}N^{1-2/(k^{2}+k+1)}
with
|
S
|
≫
m
N
1
/
2
|S|\gg_{m}N^{1/2}
, say?
•
From the remark after Corollary
1.6
we see that we cannot get a conclusion like in that corollary just assuming the hypotheses of Theorem
1.1
. What kinds of natural conditions could we add to those hypotheses to get such a conclusion?
•
What can one say about the possible sizes of
∑
a
∈
A
a
j
−
∑
b
∈
B
b
j
\sum_{a\in A}a^{j}-\sum_{b\in B}b^{j}
for
j
=
k
+
1
j=k+1
in Theorems
1.1
and
1.2
, as well as the value of
j
∈
{
1
,
2
,
…
,
k
}
∖
J
j\in\{1,2,\ldots,k\}\setminus J
in Corollary
1.6
? The stronger the conclusion
on this, the tighter the range of differences in Corollary
1.8
and similar sorts of conclusions.
2.
Proof of Theorem
1.1
To prove the theorem we will need a proposition about Hilbert cubes. First, though, we need some notation.
Definition 2.1
.
Given
an abelian group
G
G
and
α
1
,
…
,
α
d
∈
G
∖
{
0
}
\alpha_{1},\ldots,\alpha_{d}\in G\setminus\{0\}
, we define
the
Hilbert cube
H
0
​
(
α
1
,
…
,
α
d
)
⊆
G
H_{0}(\alpha_{1},\ldots,\alpha_{d})\subseteq G
to be the set of all sums
∑
s
∈
S
α
s
\sum_{s\in S}\alpha_{s}
where
S
⊆
{
1
,
2
,
…
,
d
}
S\subseteq\{1,2,\ldots,d\}
. Alternatively, we could define this
as the following sumset
H
0
​
(
α
1
,
…
,
α
d
)
:=
{
0
,
α
1
}
+
{
0
,
α
2
}
+
⋯
+
{
0
,
α
d
}
.
H_{0}(\alpha_{1},\ldots,\alpha_{d})\ :=\ \{0,\alpha_{1}\}+\{0,\alpha_{2}\}+\cdots+\{0,\alpha_{d}\}.
In addition, if
α
0
\alpha_{0}
is some
translate, we let
H
⁡
(
α
0
,
α
1
,
…
,
α
d
)
:=
α
0
+
H
0
​
(
α
1
,
…
,
α
d
)
.
H(\alpha_{0};\alpha_{1},\ldots,\alpha_{d})\ :=\ \alpha_{0}+H_{0}(\alpha_{1},\ldots,\alpha_{d}).
We say
H
⁡
(
α
0
,
α
1
,
…
,
α
d
)
H(\alpha_{0};\alpha_{1},\ldots,\alpha_{d})
is
proper
if
|
H
⁡
(
α
0
,
α
1
,
…
,
α
d
)
|
=
2
d
|H(\alpha_{0};\alpha_{1},\ldots,\alpha_{d})|=2^{d}
.
The following lemma is a variant of Szemerédi’s cube lemma
[
18
]
:
Lemma 2.2
.
Suppose
d
≥
1
d\geq 1
is an integer,
G
G
is an abelian group,
and that
S
S
is a subset of
G
G
such that
|
S
−
S
|
=
K
​
|
S
|
|S-S|=K|S|
where
(5)
|
S
|
≥
3
d
+
1
​
(
2
​
K
)
2
d
−
1
.
|S|\ \geq\ 3^{d+1}(2K)^{2^{d}-1}.
Then,
S
S
contains a proper Hilbert cube of dimension
d
d
.
Proof.
We construct the Hilbert cube iteratively, by constructing a sequence of elements
α
1
,
α
2
,
…
,
α
d
\alpha_{1},\alpha_{2},\ldots,\alpha_{d}
in
G
G
, and a corresponding sequence of sets
S
0
:=
S
⊇
S
1
⊇
⋯
⊇
S
d
,
S_{0}\ :=S\ \supseteq\ S_{1}\ \supseteq\ \cdots\ \supseteq\ S_{d},
where for
i
≥
1
i\geq 1
we have that
H
0
​
(
α
1
,
…
,
α
i
)
H_{0}(\alpha_{1},\ldots,\alpha_{i})
is proper, and so that
S
i
S_{i}
will consist of all the choices
of
α
0
\alpha_{0}
so that the Hilbert cubes
H
⁡
(
α
0
,
α
1
,
…
,
α
i
)
⊆
S
H(\alpha_{0};\alpha_{1},\ldots,\alpha_{i})\subseteq S
.
The way we construct a set
S
i
+
1
S_{i+1}
from
S
i
S_{i}
is given as follows: given
α
1
,
…
,
α
i
\alpha_{1},\ldots,\alpha_{i}
, among all choices of
x
∈
S
i
−
S
i
x\in S_{i}-S_{i}
, we initially select those so that
H
0
​
(
α
1
,
…
,
α
i
,
x
)
H_{0}(\alpha_{1},\ldots,\alpha_{i},x)
is proper; and then among
those
, we select
α
i
+
1
:=
x
\alpha_{i+1}:=x
so that
|
S
i
∩
(
S
i
−
x
)
|
|S_{i}\cap(S_{i}-x)|
is maximal. We furthermore will
show that the sets
S
j
S_{j}
,
j
≥
0
j\geq 0
, we construct have the property that
(6)
|
S
j
−
S
j
|
=
K
j
​
|
S
j
|
,
where
​
K
j
≤
(
2
​
K
)
2
j
2
,
and
​
|
S
j
|
≥
3
d
+
1
.
|S_{j}-S_{j}|\ =\ K_{j}|S_{j}|,\ {\rm where\ }K_{j}\ \leq\ {(2K)^{2^{j}}\over 2},\ {\rm and\ }|S_{j}|\geq 3^{d+1}.
Note that
K
0
=
K
K_{0}=K
.
Let us first establish there are many choices for
x
x
and that we can get that
S
i
∩
(
S
i
−
x
)
S_{i}\cap(S_{i}-x)
has an abundance of elements for at least one of them: we assume that
H
0
​
(
α
1
,
…
,
α
i
)
H_{0}(\alpha_{1},\ldots,\alpha_{i})
is proper. We will say that a choice for
x
x
is
bad
if
H
0
​
(
α
1
,
…
,
α
i
,
x
)
H_{0}(\alpha_{1},\ldots,\alpha_{i},x)
is not proper.
Notice that since
|
H
0
​
(
α
1
,
…
,
α
i
)
−
H
0
​
(
α
1
,
…
,
α
i
)
|
≤
3
i
,
|H_{0}(\alpha_{1},\ldots,\alpha_{i})-H_{0}(\alpha_{1},\ldots,\alpha_{i})|\leq 3^{i},
there can be at most
3
i
3^{i}
bad choices for
x
x
. Let
X
X
denote the remaining
good
choices for
x
∈
S
i
−
S
i
x\in S_{i}-S_{i}
(note that this means
S
i
∩
(
S
i
−
x
)
≠
∅
S_{i}\cap(S_{i}-x)\neq\emptyset
).
Obviously
|
X
|
≥
|
S
i
−
S
i
|
−
3
d
.
|X|\ \geq\ |S_{i}-S_{i}|-3^{d}.
This lower bound is trivially non-zero assuming the last lower bound in (
6
).
We have that
(7)
max
x
∈
X
⁡
|
S
i
∩
(
S
i
−
x
)
|
\displaystyle\max_{x\in X}|S_{i}\cap(S_{i}-x)|\
≥
\displaystyle\geq
1
|
X
|
∑
x
∈
X
#
{
a
,
b
∈
S
i
:
a
−
b
=
x
}
\displaystyle\ {1\over|X|}\sum_{x\in X}\#\{a,b\in S_{i}\ :\ a-b=x\}
≥
\displaystyle\geq
|
S
i
|
2
−
3
i
​
|
S
i
|
|
S
i
−
S
i
|
≥
|
S
i
|
2
​
K
i
.
\displaystyle\ {|S_{i}|^{2}-3^{i}|S_{i}|\over|S_{i}-S_{i}|}\ \geq\ {|S_{i}|\over 2K_{i}}.
As we said before, we let
α
i
+
1
\alpha_{i+1}
denote this maximal choice for
x
∈
X
x\in X
.
If we then let
S
i
+
1
S_{i+1}
denote this set
S
i
∩
(
S
i
−
α
i
+
1
)
S_{i}\cap(S_{i}-\alpha_{i+1})
we have
that
K
i
+
1
=
|
S
i
+
1
−
S
i
+
1
|
|
S
i
+
1
|
≤
|
S
i
−
S
i
|
|
S
i
|
/
2
​
K
i
=
K
i
​
|
S
i
|
|
S
i
|
/
2
​
K
i
=
2
​
K
i
2
,
K_{i+1}\ =\ {|S_{i+1}-S_{i+1}|\over|S_{i+1}|}\ \leq\ {|S_{i}-S_{i}|\over|S_{i}|/2K_{i}}\ =\ {K_{i}|S_{i}|\over|S_{i}|/2K_{i}}\ =\ 2K_{i}^{2},
provided
|
S
i
|
≥
2
|S_{i}|\geq 2
. So,
K
i
+
1
≤
2
​
K
i
2
≤
2
3
​
K
i
−
1
4
≤
2
7
​
K
i
−
2
8
≤
⋯
≤
2
2
i
+
1
−
1
​
K
0
2
i
+
1
=
(
2
​
K
)
2
i
+
1
2
.
K_{i+1}\ \leq\ 2K_{i}^{2}\ \leq\ 2^{3}K_{i-1}^{4}\ \leq\ 2^{7}K_{i-2}^{8}\ \leq\ \cdots\ \leq\ 2^{2^{i+1}-1}K_{0}^{2^{i+1}}\ =\ {(2K)^{2^{i+1}}\over 2}.
From inequality (
7
), it follows that
|
S
i
+
1
|
≥
|
S
i
|
2
​
K
i
≥
|
S
i
−
1
|
4
​
K
i
​
K
i
−
1
≥
⋯
≥
|
S
|
2
i
+
1
K
i
K
i
−
1
⋯
K
0
≥
|
S
|
(
2
​
K
)
2
i
+
1
−
1
.
|S_{i+1}|\ \geq\ {|S_{i}|\over 2K_{i}}\ \geq\ {|S_{i-1}|\over 4K_{i}K_{i-1}}\ \geq\ \cdots\ \geq\ {|S|\over 2^{i+1}K_{i}K_{i-1}\cdots K_{0}}\ \geq\ {|S|\over(2K)^{2^{i+1}-1}}.
We note that if
i
≤
d
−
1
i\leq d-1
then
the last inequality of (
6
) holds, provided
|
S
|
≥
3
d
+
1
​
(
2
​
K
)
2
d
−
1
.
|S|\ \geq\ 3^{d+1}(2K)^{2^{d}-1}.
To finish the proof, we need to establish that
S
d
S_{d}
contains all the choices
for
α
0
\alpha_{0}
such that
H
⁡
(
α
0
,
α
1
,
…
,
α
d
)
⊆
S
H(\alpha_{0};\alpha_{1},\ldots,\alpha_{d})\subseteq S
.
We prove this by induction. Assume that
S
i
S_{i}
consists of all choices of
α
0
\alpha_{0}
such that
H
⁡
(
α
0
,
α
1
,
…
,
α
i
)
⊆
S
H(\alpha_{0};\alpha_{1},\ldots,\alpha_{i})\subseteq S
.
Now suppose
α
0
′
∈
S
i
+
1
=
S
i
∩
(
S
i
−
α
i
+
1
)
.
\alpha^{\prime}_{0}\in S_{i+1}=S_{i}\cap(S_{i}-\alpha_{i+1}).
Then
α
0
′
∈
S
i
\alpha^{\prime}_{0}\in S_{i}
and
α
0
′
+
α
i
+
1
∈
S
i
\alpha^{\prime}_{0}+\alpha_{i+1}\in S_{i}
. By the
induction hypothesis,
H
⁡
(
α
0
′
,
α
1
,
…
,
α
i
)
⊆
S
and
H
⁡
(
α
0
′
+
α
i
+
1
,
α
1
,
…
,
α
i
)
⊆
S
.
H(\alpha^{\prime}_{0};\alpha_{1},\ldots,\alpha_{i})\subseteq S\quad\text{and}\quad H(\alpha^{\prime}_{0}+\alpha_{i+1};\alpha_{1},\ldots,\alpha_{i})\subseteq S.
Since
H
⁡
(
α
0
′
,
α
1
,
…
,
α
i
)
∪
H
⁡
(
α
0
′
+
α
i
+
1
,
α
1
,
…
,
α
i
)
=
H
⁡
(
α
0
′
,
α
1
,
…
,
α
i
+
1
)
,
H(\alpha^{\prime}_{0};\alpha_{1},\ldots,\alpha_{i})\cup H(\alpha^{\prime}_{0}+\alpha_{i+1};\alpha_{1},\ldots,\alpha_{i})=H(\alpha^{\prime}_{0};\alpha_{1},\ldots,\alpha_{i+1}),
we get
H
⁡
(
α
0
′
,
α
1
,
…
,
α
i
+
1
)
⊆
S
H(\alpha^{\prime}_{0};\alpha_{1},\ldots,\alpha_{i+1})\subseteq S
. This completes
the induction and finishes the proof of the lemma.
∎
To prove Theorem
1.1
, we need to find several Hilbert cubes in the set
S
S
, with their generators satisfying some algebraic relations. This can be summarized in the following proposition.
Proposition 2.3
.
Suppose
d
,
ℓ
d,\ell
are positive integers,
R
R
is an integral domain, and
S
⊆
R
S\subseteq R
is finite such that
|
S
−
S
|
≤
ℓ
​
K
​
|
S
|
|S-S|\leq\ell K|S|
, where
(8)
|
S
|
≥
2
​
ℓ
​
(
3
d
+
1
+
3
ℓ
)
​
(
4
​
ℓ
2
​
K
)
2
d
−
1
|S|\geq 2\ell(3^{d+1}+3^{\ell})(4\ell^{2}K)^{2^{d}-1}
Then there exist
ℓ
\ell
disjoint proper Hilbert cubes
H
i
=
H
⁡
(
α
i
,
0
,
α
i
,
1
,
…
,
α
i
,
d
)
,
(
1
≤
i
≤
ℓ
)
H_{i}=H(\alpha_{i,0};\alpha_{i,1},\ldots,\alpha_{i,d}),(1\leq i\leq\ell)
, such that
H
i
⊆
S
H_{i}\subseteq S
for all
i
i
, and
(9)
∑
i
=
1
ℓ
ε
⁡
(
i
)
​
∏
j
=
1
d
α
i
,
j
≠
0
\sum_{i=1}^{\ell}\varepsilon(i)\prod_{j=1}^{d}\alpha_{i,j}\neq 0
for any
ε
∈
{
−
1
,
0
,
1
}
ℓ
∖
{
(
0
,
0
,
…
,
0
)
}
\varepsilon\in\{-1,0,1\}^{\ell}\setminus\{(0,0,\ldots,0)\}
.
Proof.
We partition
S
S
into
ℓ
\ell
disjoint subsets
S
1
,
S
2
,
…
,
S
ℓ
S_{1},S_{2},\ldots,S_{\ell}
with
|
S
i
|
≥
⌊
|
S
|
/
ℓ
⌋
|S_{i}|\geq\lfloor|S|/\ell\rfloor
for all
i
i
. Then for any fixed
1
≤
i
≤
ℓ
1\leq i\leq\ell
, we have
(10)
|
S
i
−
S
i
|
≤
|
S
−
S
|
≤
ℓ
​
K
​
|
S
|
≤
2
​
ℓ
2
​
K
​
|
S
i
|
.
|S_{i}-S_{i}|\leq|S-S|\leq\ell K|S|\leq 2\ell^{2}K|S_{i}|.
We also know that
(11)
|
S
i
|
≥
|
S
|
2
​
ℓ
≥
(
3
d
+
1
+
3
ℓ
)
​
(
4
​
ℓ
2
​
K
)
2
d
−
1
,
|S_{i}|\geq\frac{|S|}{2\ell}\geq(3^{d+1}+3^{\ell})(4\ell^{2}K)^{2^{d}-1},
hence by Lemma
2.2
there exists a proper Hilbert cube
H
1
=
H
⁡
(
α
1
,
0
,
α
1
,
1
,
…
,
α
1
,
d
)
⊆
S
1
H_{1}=H(\alpha_{1,0};\alpha_{1,1},\ldots,\alpha_{1,d})\subseteq S_{1}
.
To guarantee the algebraic restriction (
9
), we construct the remaining Hilbert cubes inductively. Suppose that we have constructed a proper Hilbert cube
H
i
=
H
⁡
(
α
i
,
0
,
α
i
,
1
,
…
,
α
i
,
d
)
⊆
S
i
H_{i}=H(\alpha_{i,0};\alpha_{i,1},\ldots,\alpha_{i,d})\subseteq S_{i}
for every
1
≤
i
≤
t
1\leq i\leq t
, and that
∑
i
=
1
t
ε
⁡
(
i
)
​
∏
j
=
1
d
α
i
,
j
≠
0
\sum_{i=1}^{t}\varepsilon(i)\prod_{j=1}^{d}\alpha_{i,j}\neq 0
for every nonzero
ε
∈
{
−
1
,
0
,
1
}
t
\varepsilon\in\{-1,0,1\}^{t}
. For
i
=
t
+
1
i=t+1
, following the proof of Lemma
2.2
for
d
−
1
d-1
steps, we can construct
A
0
:=
S
t
+
1
⊇
A
1
⊇
⋯
⊇
A
d
−
1
A_{0}:=S_{t+1}\supseteq A_{1}\supseteq\cdots\supseteq A_{d-1}
and
α
t
+
1
,
1
,
…
,
α
t
+
1
,
d
−
1
\alpha_{t+1,1},\ldots,\alpha_{t+1,d-1}
such that
|
A
j
−
A
j
|
=
K
j
​
|
A
j
|
,
K
j
≤
(
4
​
ℓ
2
​
K
)
2
j
2
,
|
A
j
|
≥
3
d
+
1
+
3
ℓ
.
|A_{j}-A_{j}|=K_{j}|A_{j}|,\qquad K_{j}\leq{(4\ell^{2}K)^{2^{j}}\over 2},\qquad|A_{j}|\geq 3^{d+1}+3^{\ell}.
The last inequality follows from
|
A
j
|
≥
|
S
t
+
1
|
(
4
​
ℓ
2
​
K
)
2
j
−
1
|A_{j}|\geq\frac{|S_{t+1}|}{(4\ell^{2}K)^{2^{j}-1}}
and inequality (
11
). Put
B
=
A
d
−
1
B=A_{d-1}
. Since
B
B
is the set of admissible translates for the
(
d
−
1
)
(d-1)
-dimensional cube, to add the last generator we must choose
α
t
+
1
,
d
∈
B
−
B
,
\alpha_{t+1,d}\in B-B,
so that some translate
α
t
+
1
,
0
∈
B
∩
(
B
−
α
t
+
1
,
d
)
\alpha_{t+1,0}\in B\cap(B-\alpha_{t+1,d})
exists.
There are at most
3
d
−
1
3^{d-1}
choices of
x
∈
B
−
B
x\in B-B
for which
H
0
​
(
α
t
+
1
,
1
,
…
,
α
t
+
1
,
d
−
1
,
x
)
H_{0}(\alpha_{t+1,1},\ldots,\alpha_{t+1,d-1},x)
is not proper. Also, for any
ε
∈
{
−
1
,
0
,
1
}
t
×
{
±
1
}
\varepsilon\in\{-1,0,1\}^{t}\times\{\pm 1\}
, the equation
∑
i
=
1
t
ε
⁡
(
i
)
​
∏
j
=
1
d
α
i
,
j
+
ε
⁡
(
t
+
1
)
​
x
​
∏
j
=
1
d
−
1
α
t
+
1
,
j
=
0
\sum_{i=1}^{t}\varepsilon(i)\prod_{j=1}^{d}\alpha_{i,j}+\varepsilon(t+1)x\prod_{j=1}^{d-1}\alpha_{t+1,j}=0
has at most one solution in
x
x
, since
R
R
is an integral domain and
∏
j
=
1
d
−
1
α
t
+
1
,
j
≠
0
\prod_{j=1}^{d-1}\alpha_{t+1,j}\neq 0
, with the usual convention that an
empty product is
1
1
. Thus there are at most
3
ℓ
3^{\ell}
additional forbidden choices. Since
|
B
−
B
|
≥
|
B
|
≥
3
d
+
1
+
3
ℓ
>
3
d
−
1
+
3
ℓ
,
|B-B|\geq|B|\geq 3^{d+1}+3^{\ell}>3^{d-1}+3^{\ell},
we can choose
α
t
+
1
,
d
∈
B
−
B
\alpha_{t+1,d}\in B-B
avoiding all forbidden choices, and then choose
α
t
+
1
,
0
∈
B
∩
(
B
−
α
t
+
1
,
d
)
.
\alpha_{t+1,0}\in B\cap(B-\alpha_{t+1,d}).
This gives us a proper Hilbert cube
H
t
+
1
=
H
⁡
(
α
t
+
1
,
0
,
α
t
+
1
,
1
,
…
,
α
t
+
1
,
d
)
⊆
S
t
+
1
H_{t+1}=H(\alpha_{t+1,0};\alpha_{t+1,1},\ldots,\alpha_{t+1,d})\subseteq S_{t+1}
so that
∑
i
=
1
t
+
1
ε
⁡
(
i
)
​
∏
j
=
1
d
α
i
,
j
≠
0
\sum_{i=1}^{t+1}\varepsilon(i)\prod_{j=1}^{d}\alpha_{i,j}\neq 0
for every nonzero
ε
∈
{
−
1
,
0
,
1
}
t
+
1
\varepsilon\in\{-1,0,1\}^{t+1}
. This finishes the induction step.
∎
We will also use the following polynomial identity.
Lemma 2.4
.
Let
d
≥
1
d\geq 1
. In the free associative algebra
ℤ
⁡
⟨
x
0
,
x
1
,
…
,
x
d
⟩
\mathbb{Z}\langle x_{0},x_{1},\ldots,x_{d}\rangle
, we have
(12)
∑
U
⊆
[
d
]
(
−
1
)
|
U
|
​
(
x
0
+
∑
i
∈
U
x
i
)
j
=
0
(
0
≤
j
<
d
)
.
\sum_{U\subseteq[d]}(-1)^{|U|}\left(x_{0}+\sum_{i\in U}x_{i}\right)^{j}=0\qquad(0\leq j<d).
Moreover, in the commutative polynomial ring
ℤ
⁡
[
x
0
,
x
1
,
…
,
x
d
]
\mathbb{Z}[x_{0},x_{1},\ldots,x_{d}]
, we have
(13)
∑
U
⊆
[
d
]
(
−
1
)
|
U
|
(
x
0
+
∑
i
∈
U
x
i
)
d
=
(
−
1
)
d
d
!
x
1
⋯
x
d
.
\sum_{U\subseteq[d]}(-1)^{|U|}\left(x_{0}+\sum_{i\in U}x_{i}\right)^{d}=(-1)^{d}d!x_{1}\cdots x_{d}.
Proof.
To prove equation (
12
), fix a non-commutative monomial
W
W
of degree
j
<
d
j<d
, and let
T
=
{
i
∈
[
d
]
:
x
i
​
occurs in
​
W
}
.
T=\{i\in[d]:x_{i}\text{ occurs in }W\}.
The coefficient of
W
W
in
(
x
0
+
∑
i
∈
U
x
i
)
j
(x_{0}+\sum_{i\in U}x_{i})^{j}
is
1
1
if
T
⊆
U
T\subseteq U
, and is
0
0
otherwise. Since
|
T
|
≤
j
<
d
|T|\leq j<d
, the coefficient of
W
W
in the left-hand side of equation (
12
) is
∑
[
d
]
⊇
U
⊇
T
(
−
1
)
|
U
|
=
(
−
1
)
|
T
|
​
(
1
−
1
)
d
−
|
T
|
=
0
.
\sum_{[d]\supseteq U\supseteq T}(-1)^{|U|}=(-1)^{|T|}(1-1)^{d-|T|}=0.
This proves equation (
12
).
For equation (
13
), the same argument shows that every monomial of degree
d
d
missing some
x
i
x_{i}
,
1
≤
i
≤
d
1\leq i\leq d
, has coefficient zero. The only remaining monomial is
x
1
⋯
x
d
x_{1}\cdots x_{d}
, whose coefficient is
(
−
1
)
d
​
d
!
(-1)^{d}d!
.
∎
Now we are ready to present the proof of Theorem
1.1
.
Proof of Theorem
1.1
(2).
Given Proposition
2.3
, to prove our theorem we first let
ℓ
=
⌈
log
2
⁡
m
⌉
\ell=\lceil\log_{2}m\rceil
,
d
=
k
+
1
d=k+1
, and
then we note that (
8
)
would hold, provided that
K
≤
c
​
|
S
|
1
/
(
2
k
+
1
−
1
)
,
where
​
c
=
1
4
​
ℓ
​
[
2
​
ℓ
​
(
3
k
+
2
+
3
ℓ
)
]
1
/
(
2
k
+
1
−
1
)
.
K\ \leq\ c|S|^{1/(2^{k+1}-1)},\ {\rm where\ }c\ =\ \frac{1}{4\ell[2\ell(3^{k+2}+3^{\ell})]^{1/(2^{k+1}-1)}}.
Note that
c
c
here depends only on
k
k
and
m
m
. So, assuming
S
S
satisfies the hypotheses of the main theorem, we get that it contains
ℓ
\ell
disjoint proper Hilbert cubes
H
i
=
H
⁡
(
α
i
,
0
,
α
i
,
1
,
…
,
α
i
,
k
+
1
)
H_{i}=H(\alpha_{i,0};\alpha_{i,1},\ldots,\alpha_{i,k+1})
,
(
1
≤
i
≤
ℓ
)
(1\leq i\leq\ell)
, each of dimension
k
+
1
k+1
as given by the above proposition.
The idea of the rest of the proof is to prove a polynomial analogue of the main theorem, and then to replace the variables with the
α
i
,
j
\alpha_{i,j}
’s. Towards this goal we define a set of special linear forms (with coefficients
0
0
and
1
1
) in
ℤ
⁡
[
x
1
,
…
,
x
k
+
1
]
{\mathbb{Z}}[x_{1},\ldots,x_{k+1}]
as follows:
ℒ
k
+
1
:=
{
ε
1
x
1
+
⋯
+
ε
k
+
1
x
k
+
1
:
for
i
=
1
,
…
,
k
+
1
,
ε
i
∈
{
0
,
1
}
}
.
\mathcal{L}_{k+1}\ :=\ \{\varepsilon_{1}x_{1}+\cdots+\varepsilon_{k+1}x_{k+1}\ :\ {\rm for\ }i=1,\ldots,k+1,\ \varepsilon_{i}\in\{0,1\}\}.
We then let
𝒪
k
+
1
\mathcal{O}_{k+1}
denote the elements of
ℒ
k
+
1
\mathcal{L}_{k+1}
with an odd number of non-zero terms, and
ℰ
k
+
1
\mathcal{E}_{k+1}
denote the elements with an even number of non-zero terms. By Lemma
2.4
, for
j
=
1
,
…
,
k
j=1,\ldots,k
,
(14)
∑
f
∈
𝒪
k
+
1
(
x
0
+
f
⁡
(
x
1
,
…
,
x
k
+
1
)
)
j
=
∑
g
∈
ℰ
k
+
1
(
x
0
+
g
⁡
(
x
1
,
…
,
x
k
+
1
)
)
j
,
\sum_{f\in\mathcal{O}_{k+1}}(x_{0}+f(x_{1},\ldots,x_{k+1}))^{j}=\sum_{g\in\mathcal{E}_{k+1}}(x_{0}+g(x_{1},\ldots,x_{k+1}))^{j},
while
(15)
∑
f
∈
𝒪
k
+
1
(
x
0
+
f
(
x
1
,
…
,
x
k
+
1
)
)
k
+
1
−
∑
g
∈
ℰ
k
+
1
(
x
0
+
g
(
x
1
,
…
,
x
k
+
1
)
)
k
+
1
=
(
−
1
)
k
(
k
+
1
)
!
x
1
⋯
x
k
+
1
.
\sum_{f\in\mathcal{O}_{k+1}}(x_{0}+f(x_{1},\ldots,x_{k+1}))^{k+1}-\sum_{g\in\mathcal{E}_{k+1}}(x_{0}+g(x_{1},\ldots,x_{k+1}))^{k+1}=(-1)^{k}(k+1)!x_{1}\cdots x_{k+1}.
Now for any fixed
1
≤
i
≤
ℓ
1\leq i\leq\ell
, replacing
x
r
x_{r}
by
α
i
,
r
\alpha_{i,r}
in equations (
14
) and (
15
), we have
∑
a
∈
B
i
,
0
a
j
=
∑
b
∈
B
i
,
1
b
j
\sum_{a\in B_{i,0}}a^{j}=\sum_{b\in B_{i,1}}b^{j}
for all
1
≤
j
≤
k
1\leq j\leq k
while
(16)
∑
a
∈
B
i
,
0
a
k
+
1
−
∑
b
∈
B
i
,
1
b
k
+
1
=
(
−
1
)
k
(
k
+
1
)
!
α
i
,
1
⋯
α
i
,
k
+
1
≠
0
,
\sum_{a\in B_{i,0}}a^{k+1}-\sum_{b\in B_{i,1}}b^{k+1}=(-1)^{k}(k+1)!\alpha_{i,1}\cdots\alpha_{i,k+1}\ \neq\ 0,
where
B
i
,
0
=
{
α
i
,
0
+
f
⁡
(
α
i
,
1
,
…
,
α
i
,
k
+
1
)
:
f
∈
𝒪
k
+
1
}
,
B
i
,
1
=
{
α
i
,
0
+
g
⁡
(
α
i
,
1
,
…
,
α
i
,
k
+
1
)
:
g
∈
ℰ
k
+
1
}
.
B_{i,0}=\{\alpha_{i,0}+f(\alpha_{i,1},\ldots,\alpha_{i,k+1}):f\in\mathcal{O}_{k+1}\},\quad B_{i,1}=\{\alpha_{i,0}+g(\alpha_{i,1},\ldots,\alpha_{i,k+1}):g\in\mathcal{E}_{k+1}\}.
Here the last inequality follows since
char
⁡
(
R
)
>
k
+
1
\mathrm{char}(R)>k+1
or
char
⁡
(
R
)
=
0
\mathrm{char}(R)=0
, and
α
i
,
1
⋯
α
i
,
k
+
1
\alpha_{i,1}\cdots\alpha_{i,k+1}
is non-zero. Since
H
i
H_{i}
is proper, we also have
|
B
i
,
0
|
=
|
B
i
,
1
|
=
2
k
|B_{i,0}|=|B_{i,1}|=2^{k}
.
Next we define
2
ℓ
2^{\ell}
distinct subsets of
S
S
as follows: for each
σ
∈
{
0
,
1
}
ℓ
\sigma\in\{0,1\}^{\ell}
, let
A
σ
=
⋃
i
=
1
ℓ
B
i
,
σ
⁡
(
i
)
.
A_{\sigma}=\bigcup_{i=1}^{\ell}B_{i,\sigma(i)}.
For any
σ
≠
τ
∈
{
0
,
1
}
ℓ
\sigma\neq\tau\in\{0,1\}^{\ell}
, from our definition of
B
i
,
0
,
B
i
,
1
B_{i,0},B_{i,1}
we must have
∑
a
∈
A
σ
a
j
=
∑
b
∈
A
τ
b
j
\sum_{a\in A_{\sigma}}a^{j}=\sum_{b\in A_{\tau}}b^{j}
for any
1
≤
j
≤
k
1\leq j\leq k
. On the other hand, from equation (
16
), there exists some
ε
∈
{
−
1
,
0
,
1
}
ℓ
∖
{
(
0
,
0
,
…
,
0
)
}
\varepsilon\in\{-1,0,1\}^{\ell}\setminus\{(0,0,\ldots,0)\}
such that
∑
a
∈
A
σ
a
k
+
1
−
∑
b
∈
A
τ
b
k
+
1
=
(
k
+
1
)
!
​
∑
i
=
1
ℓ
ε
⁡
(
i
)
​
∏
j
=
1
k
+
1
α
i
,
j
.
\sum_{a\in A_{\sigma}}a^{k+1}-\sum_{b\in A_{\tau}}b^{k+1}=(k+1)!\sum_{i=1}^{\ell}\varepsilon(i)\prod_{j=1}^{k+1}\alpha_{i,j}.
By Proposition
2.3
, this is nonzero. Since
|
A
σ
|
=
∑
i
|
B
i
,
σ
⁡
(
i
)
|
=
ℓ
​
2
k
|A_{\sigma}|=\sum_{i}|B_{i,\sigma(i)}|=\ell 2^{k}
for each
σ
∈
{
0
,
1
}
ℓ
\sigma\in\{0,1\}^{\ell}
, and
2
ℓ
≥
m
2^{\ell}\geq m
, this finishes the proof of the theorem.
∎
Proof of Theorem
1.1
(1).
The proof is almost identical to the proof above. We shall only need the existence of
ℓ
=
⌈
log
2
⁡
m
⌉
\ell=\lceil\log_{2}m\rceil
disjoint proper Hilbert cubes
H
1
,
…
,
H
ℓ
H_{1},\ldots,H_{\ell}
in
S
S
, each of dimension
k
+
1
k+1
, without the extra algebraic constraint (
9
). This can be proved in any ring by modifying the proof of Proposition
2.3
. Also, we now regard
ℒ
k
+
1
\mathcal{L}_{k+1}
as a subset of
ℤ
⁡
⟨
x
1
,
…
,
x
k
+
1
⟩
\mathbb{Z}\langle x_{1},\ldots,x_{k+1}\rangle
, polynomials in non-commuting variables. By equation (
12
), for
j
=
1
,
…
,
k
j=1,\ldots,k
,
∑
f
∈
𝒪
k
+
1
(
x
0
+
f
⁡
(
x
1
,
…
,
x
k
+
1
)
)
j
=
∑
g
∈
ℰ
k
+
1
(
x
0
+
g
⁡
(
x
1
,
…
,
x
k
+
1
)
)
j
\sum_{f\in\mathcal{O}_{k+1}}(x_{0}+f(x_{1},\ldots,x_{k+1}))^{j}=\sum_{g\in\mathcal{E}_{k+1}}(x_{0}+g(x_{1},\ldots,x_{k+1}))^{j}
holds in
ℤ
⁡
⟨
x
0
,
x
1
,
…
,
x
k
+
1
⟩
\mathbb{Z}\langle x_{0},x_{1},\ldots,x_{k+1}\rangle
.
It follows that for any
1
≤
i
≤
ℓ
1\leq i\leq\ell
,
1
≤
j
≤
k
1\leq j\leq k
,
∑
f
∈
𝒪
k
+
1
(
α
i
,
0
+
f
⁡
(
α
i
,
1
,
…
,
α
i
,
k
+
1
)
)
j
=
∑
g
∈
ℰ
k
+
1
(
α
i
,
0
+
g
⁡
(
α
i
,
1
,
…
,
α
i
,
k
+
1
)
)
j
.
\sum_{f\in\mathcal{O}_{k+1}}(\alpha_{i,0}+f(\alpha_{i,1},\ldots,\alpha_{i,k+1}))^{j}=\sum_{g\in\mathcal{E}_{k+1}}(\alpha_{i,0}+g(\alpha_{i,1},\ldots,\alpha_{i,k+1}))^{j}.
Defining
B
i
,
0
,
B
i
,
1
B_{i,0},B_{i,1}
for
1
≤
i
≤
ℓ
1\leq i\leq\ell
and
A
σ
A_{\sigma}
for
σ
∈
{
0
,
1
}
ℓ
\sigma\in\{0,1\}^{\ell}
as in the proof of Theorem
1.1
(2) completes the proof.
∎
We have the following proposition showing that for the polynomial analogue established in the above proof, the choice of
𝒪
k
+
1
\mathcal{O}_{k+1}
and
ℰ
k
+
1
\mathcal{E}_{k+1}
is optimal.
Proposition 2.5
.
Let
h
=
k
+
1
h=k+1
. For each
U
⊆
[
h
]
U\subseteq[h]
, write
ℓ
U
=
∑
i
∈
U
x
i
∈
ℒ
h
.
\ell_{U}=\sum_{i\in U}x_{i}\in\mathcal{L}_{h}.
Let
𝒜
,
ℬ
⊆
ℒ
h
\mathcal{A},\mathcal{B}\subseteq\mathcal{L}_{h}
be disjoint and nonempty, and suppose that
ℓ
∅
=
0
∈
𝒜
∪
ℬ
\ell_{\emptyset}=0\in\mathcal{A}\cup\mathcal{B}
. Assume that
∑
ℓ
U
∈
𝒜
ℓ
U
j
=
∑
ℓ
U
∈
ℬ
ℓ
U
j
\sum_{\ell_{U}\in\mathcal{A}}\ell_{U}^{j}=\sum_{\ell_{U}\in\mathcal{B}}\ell_{U}^{j}
as identities in
ℤ
⁡
[
x
1
,
…
,
x
h
]
\mathbb{Z}[x_{1},\ldots,x_{h}]
for
1
≤
j
≤
k
1\leq j\leq k
. Then
𝒜
∪
ℬ
=
ℒ
h
.
\mathcal{A}\cup\mathcal{B}=\mathcal{L}_{h}.
Moreover, after possibly interchanging
𝒜
\mathcal{A}
and
ℬ
\mathcal{B}
, the nonzero elements
of
𝒜
\mathcal{A}
are precisely the
ℓ
U
\ell_{U}
with
|
U
|
≡
h
(
mod
2
)
|U|\equiv h\pmod{2}
, and the nonzero
elements of
ℬ
\mathcal{B}
are precisely the
ℓ
U
\ell_{U}
with
|
U
|
≢
h
(
mod
2
)
|U|\not\equiv h\pmod{2}
. The zero
form may lie on either side.
Proof.
For
U
⊆
[
h
]
U\subseteq[h]
, set
w
U
=
𝟏
ℓ
U
∈
𝒜
−
𝟏
ℓ
U
∈
ℬ
,
F
(
T
)
=
∑
U
⊇
T
w
U
(
T
⊆
[
h
]
)
.
w_{U}=\mathbf{1}_{\ell_{U}\in\mathcal{A}}-\mathbf{1}_{\ell_{U}\in\mathcal{B}},\qquad F(T)=\sum_{U\supseteq T}w_{U}\quad(T\subseteq[h]).
We claim that
F
⁡
(
T
)
=
0
F(T)=0
for every nonempty proper subset
T
⊊
[
h
]
T\subsetneq[h]
.
Indeed, writing
r
=
|
T
|
≤
h
−
1
=
k
r=|T|\leq h-1=k
, the coefficient of
x
T
=
∏
i
∈
T
x
i
x_{T}=\prod_{i\in T}x_{i}
in
ℓ
U
r
\ell_{U}^{r}
is
r
!
r!
if
T
⊆
U
T\subseteq U
, and is
0
0
otherwise. Comparing
the coefficient of
x
T
x_{T}
in the identity for the
r
r
-th powers gives
0
=
r
!
​
∑
U
⊇
T
w
U
=
r
!
​
F
​
(
T
)
.
0=r!\sum_{U\supseteq T}w_{U}=r!F(T).
By Möbius inversion on the subset lattice
2
[
h
]
2^{[h]}
(see for example
[
17
, Example 3.8.3]
),
w
U
=
∑
T
⊇
U
(
−
1
)
|
T
|
−
|
U
|
​
F
​
(
T
)
(
U
⊆
[
h
]
)
.
w_{U}=\sum_{T\supseteq U}(-1)^{|T|-|U|}F(T)\qquad(U\subseteq[h]).
Thus, for every nonempty
U
⊆
[
h
]
U\subseteq[h]
, all terms vanish except possibly
T
=
[
h
]
T=[h]
, and so
w
U
=
(
−
1
)
h
−
|
U
|
​
F
​
(
[
h
]
)
.
w_{U}=(-1)^{h-|U|}F([h]).
Since
𝒜
\mathcal{A}
and
ℬ
\mathcal{B}
are nonempty and disjoint, and since
ℓ
∅
∈
𝒜
∪
ℬ
\ell_{\emptyset}\in\mathcal{A}\cup\mathcal{B}
, some nonzero
ℓ
U
\ell_{U}
belongs to
𝒜
∪
ℬ
\mathcal{A}\cup\mathcal{B}
.
Hence
w
U
≠
0
w_{U}\neq 0
for some nonempty
U
U
, so
F
⁡
(
[
h
]
)
≠
0
F([h])\neq 0
. But
F
⁡
(
[
h
]
)
=
w
[
h
]
∈
{
−
1
,
0
,
1
}
F([h])=w_{[h]}\in\{-1,0,1\}
, hence
F
⁡
(
[
h
]
)
=
±
1
F([h])=\pm 1
. Therefore
w
U
∈
{
±
1
}
w_{U}\in\{\pm 1\}
for every nonempty
U
U
, so every nonzero element of
ℒ
h
\mathcal{L}_{h}
lies in exactly one of
𝒜
,
ℬ
\mathcal{A},\mathcal{B}
. Together with
ℓ
∅
∈
𝒜
∪
ℬ
\ell_{\emptyset}\in\mathcal{A}\cup\mathcal{B}
, this gives
𝒜
∪
ℬ
=
ℒ
h
\mathcal{A}\cup\mathcal{B}=\mathcal{L}_{h}
.
The same formula also gives the stated parity description after possibly
interchanging
𝒜
\mathcal{A}
and
ℬ
\mathcal{B}
. The zero form is not determined by the identities,
since all of its positive powers vanish.
∎
3.
Lower bounds
In the setting of Theorem
1.2
, one would expect that when
S
S
becomes sparser, more variables (
|
A
|
+
|
B
|
|A|+|B|
) are needed to guarantee the existence of a solution. When
R
=
ℤ
R=\mathbb{Z}
and
T
=
[
N
]
T=[N]
, given some positive integer
M
=
M
⁡
(
N
)
M=M(N)
allowed to grow with
N
N
, and let
k
≥
2
k\geq 2
be fixed, we would like to know what is the smallest number
s
s
such that for any
S
⊆
[
N
]
S\subseteq[N]
of size
|
S
|
=
M
|S|=M
, there exist
A
,
B
⊆
S
A,B\subseteq S
with
|
A
|
=
|
B
|
=
s
|A|=|B|=s
such that
(17)
∑
a
∈
A
a
j
=
∑
b
∈
B
b
j
,
for
1
≤
j
≤
k
,
but
not
k
+
1
.
\sum_{a\in A}a^{j}\ =\ \sum_{b\in B}b^{j},\ {\rm for\ }1\leq j\leq k,\ {\rm but\ not\ }k+1.
It turns out that this problem is related to the study of generalized Sidon sets. Given an abelian group
G
G
and an integer
s
≥
2
s\geq 2
, we call a set
A
⊆
G
A\subseteq G
to be a
B
s
​
[
1
]
B_{s}[1]
set
if for any
g
∈
G
g\in G
, the number of solutions to the equation
g
=
x
1
+
x
2
+
⋯
+
x
s
g=x_{1}+x_{2}+\cdots+x_{s}
with
x
1
,
…
,
x
s
∈
A
x_{1},\ldots,x_{s}\in A
is at most
1
1
, where we consider two such solutions to be the same if they differ only in the ordering of the summands. In particular, Sidon sets are precisely
B
2
​
[
1
]
B_{2}[1]
sets. When
S
⊆
[
N
]
S\subseteq[N]
is chosen in such a way that
S
~
:=
{
(
n
,
n
2
,
…
,
n
k
)
:
n
∈
S
}
⊆
ℤ
k
\tilde{S}:=\{(n,n^{2},\ldots,n^{k}):n\in S\}\subseteq\mathbb{Z}^{k}
is a
B
s
​
[
1
]
B_{s}[1]
set, it is impossible to find
A
,
B
⊆
S
A,B\subseteq S
with
|
A
|
=
|
B
|
=
s
|A|=|B|=s
satisfying (
17
). Notice that the discrete moment curve
𝒞
N
k
=
{
(
n
,
n
2
,
…
,
n
k
)
:
n
∈
[
N
]
}
\mathcal{C}_{N}^{k}=\{(n,n^{2},\ldots,n^{k}):n\in[N]\}
is a
B
k
​
[
1
]
B_{k}[1]
set. This shows that
s
s
must be greater than
g
⁡
(
M
)
g(M)
, where
g
⁡
(
M
)
=
max
⁡
{
s
∈
ℕ
:
there exists a
​
B
s
​
[
1
]
​
subset of
​
𝒞
N
k
​
of size
​
M
}
.
g(M)=\max\{s\in\mathbb{N}:\text{there exists a }B_{s}[1]\text{ subset of }\mathcal{C}_{N}^{k}\text{ of size }M\}.
Given
s
>
k
s>k
, the asymptotic size of the maximum
B
s
​
[
1
]
B_{s}[1]
subset of
𝒞
N
k
\mathcal{C}_{N}^{k}
seems still unknown. Here we provide a probabilistic construction that produces a large
B
s
​
[
1
]
B_{s}[1]
subset of
𝒞
N
k
\mathcal{C}_{N}^{k}
when
s
>
k
s>k
and
N
N
is sufficiently large, but we do not expect such a construction to be optimal.
Proposition 3.1
.
Suppose
k
,
s
k,s
are positive integers such that
k
≥
2
k\geq 2
and
s
>
k
s>k
. Then for any
ε
>
0
\varepsilon>0
, when
N
>
N
0
​
(
k
,
s
,
ε
)
N>N_{0}(k,s,\varepsilon)
, there exists a
B
s
​
[
1
]
B_{s}[1]
subset of
𝒞
N
k
\mathcal{C}_{N}^{k}
of size
≫
k
,
s
,
ε
N
k
−
2
​
ε
2
​
(
s
−
1
)
\gg_{k,s,\varepsilon}N^{\frac{k-2\varepsilon}{2(s-1)}}
.
We first prove the following lemma, which allows us to bound the number of solutions to equation (
1
) with repeated elements.
Lemma 3.2
.
Let
f
(
α
)
=
∑
1
≤
n
≤
N
e
(
α
1
n
+
α
2
n
2
+
⋯
+
α
k
n
k
)
,
α
=
(
α
1
,
…
,
α
k
)
∈
[
0
,
1
)
k
.
f(\alpha)=\sum_{1\leq n\leq N}e(\alpha_{1}n+\alpha_{2}n^{2}+\cdots+\alpha_{k}n^{k}),\qquad\alpha=(\alpha_{1},\dots,\alpha_{k})\in[0,1)^{k}.
For an integer
c
≠
0
c\neq 0
, write
c
​
α
=
(
c
​
α
1
,
…
,
c
​
α
k
)
(
mod
1
)
.
c\alpha=(c\alpha_{1},\dots,c\alpha_{k})\pmod{1}.
Let
n
1
,
…
,
n
t
,
m
1
,
…
,
m
r
n_{1},\dots,n_{t},m_{1},\dots,m_{r}
be nonzero integers, and define
I
=
∫
[
0
,
1
)
k
∏
i
=
1
t
f
(
n
i
α
)
∏
j
=
1
r
f
⁡
(
m
j
​
α
)
¯
d
α
.
I=\int_{[0,1)^{k}}\prod_{i=1}^{t}f(n_{i}\alpha)\prod_{j=1}^{r}\overline{f(m_{j}\alpha)}\,d\alpha.
If
L
=
t
+
r
L=t+r
, then
|
I
|
≤
J
⌊
L
/
2
⌋
,
k
​
(
N
)
1
/
2
​
J
⌈
L
/
2
⌉
,
k
​
(
N
)
1
/
2
.
|I|\leq J_{\lfloor L/2\rfloor,k}(N)^{1/2}J_{\lceil L/2\rceil,k}(N)^{1/2}.
Proof.
By Hölder’s inequality with exponent
L
L
,
|
I
|
≤
∏
i
=
1
t
∥
f
(
n
i
⋅
)
∥
L
∏
j
=
1
r
∥
f
(
m
j
⋅
)
∥
L
.
|I|\leq\prod_{i=1}^{t}\|f(n_{i}\cdot)\|_{L}\prod_{j=1}^{r}\|f(m_{j}\cdot)\|_{L}.
Since multiplication by any nonzero integer
c
c
is measure-preserving on the torus
[
0
,
1
)
k
[0,1)^{k}
,
we have
∥
f
(
c
⋅
)
∥
L
=
∥
f
∥
L
.
\|f(c\cdot)\|_{L}=\|f\|_{L}.
Hence
|
I
|
≤
∥
f
∥
L
L
=
∫
[
0
,
1
)
k
|
f
(
α
)
|
L
d
α
.
|I|\leq\|f\|_{L}^{L}=\int_{[0,1)^{k}}|f(\alpha)|^{L}\,d\alpha.
Put
u
=
⌊
L
/
2
⌋
u=\lfloor L/2\rfloor
and
v
=
⌈
L
/
2
⌉
v=\lceil L/2\rceil
. Thus, by Cauchy–Schwarz, we have
|
I
|
≤
(
∫
[
0
,
1
)
k
|
f
(
α
)
|
2
​
u
d
α
)
1
/
2
(
∫
[
0
,
1
)
k
|
f
(
α
)
|
2
​
v
d
α
)
1
/
2
=
J
u
,
k
(
N
)
1
/
2
J
v
,
k
(
N
)
1
/
2
.
∎
|I|\leq\left(\int_{[0,1)^{k}}|f(\alpha)|^{2u}\,d\alpha\right)^{1/2}\left(\int_{[0,1)^{k}}|f(\alpha)|^{2v}\,d\alpha\right)^{1/2}=J_{u,k}(N)^{1/2}J_{v,k}(N)^{1/2}.\qed
Proof of Proposition
3.1
.
Let
S
⊆
[
N
]
S\subseteq[N]
be a random set formed by picking each element independently with probability
p
p
.
For any
k
<
L
≤
2
​
s
k<L\leq 2s
, we need to bound the number of nontrivial solutions to (
1
) in
[
N
]
[N]
with exactly
L
L
distinct elements, denoted by
T
L
,
s
​
(
N
)
T_{L,s}(N)
. (Using the Vandermonde matrix, it is easy to see that when
L
≤
k
L\leq k
, all solutions to (
1
) are trivial.) For each such solution, if there is some
a
i
=
b
i
′
a_{i}=b_{i^{\prime}}
, we delete
a
i
a_{i}
and
b
i
′
b_{i^{\prime}}
. Continue this process until the remaining sequence
a
i
1
,
…
,
a
i
t
a_{i_{1}},\ldots,a_{i_{t}}
is disjoint from
b
i
1
′
,
…
,
b
i
t
′
b_{i_{1}^{\prime}},\ldots,b_{i_{t}^{\prime}}
, and let
L
′
L^{\prime}
denote the number of distinct elements in
{
a
i
1
,
…
,
a
i
t
}
∪
{
b
i
1
′
,
…
,
b
i
t
′
}
\{a_{i_{1}},\ldots,a_{i_{t}}\}\cup\{b_{i_{1}^{\prime}},\ldots,b_{i_{t}^{\prime}}\}
. It follows from Lemma
3.2
that
T
L
,
s
​
(
N
)
=
O
k
,
s
​
(
∑
max
⁡
(
k
,
L
−
s
+
k
)
≤
L
′
≤
L
J
⌊
L
′
/
2
⌋
,
k
​
(
N
)
1
/
2
​
J
⌈
L
′
/
2
⌉
,
k
​
(
N
)
1
/
2
​
N
L
−
L
′
)
.
T_{L,s}(N)=O_{k,s}\left(\sum_{\max(k,L-s+k)\leq L^{\prime}\leq L}J_{\lfloor L^{\prime}/2\rfloor,k}(N)^{1/2}J_{\lceil L^{\prime}/2\rceil,k}(N)^{1/2}N^{L-L^{\prime}}\right).
Fix some
ε
>
0
\varepsilon>0
, Vinogradov’s mean value theorem implies that
J
⌊
L
′
/
2
⌋
,
k
​
(
N
)
1
/
2
​
J
⌈
L
′
/
2
⌉
,
k
​
(
N
)
1
/
2
=
{
O
k
,
s
,
ε
​
(
N
L
′
/
2
+
ε
)
,
if
​
2
≤
L
′
≤
k
⁡
(
k
+
1
)
O
k
,
s
,
ε
​
(
N
L
′
−
k
⁡
(
k
+
1
)
/
2
+
ε
)
,
if
​
k
​
(
k
+
1
)
<
L
′
≤
2
​
s
.
J_{\lfloor L^{\prime}/2\rfloor,k}(N)^{1/2}J_{\lceil L^{\prime}/2\rceil,k}(N)^{1/2}=\begin{cases}O_{k,s,\varepsilon}(N^{L^{\prime}/2+\varepsilon}),&\text{if }2\leq L^{\prime}\leq k(k+1)\\
O_{k,s,\varepsilon}(N^{L^{\prime}-k(k+1)/2+\varepsilon}),&\text{if }k(k+1)<L^{\prime}\leq 2s.\end{cases}
Hence we have
T
L
,
s
​
(
N
)
=
{
O
k
,
s
,
ε
​
(
N
L
−
k
/
2
+
ε
)
,
if
​
L
≤
s
O
k
,
s
,
ε
​
(
N
(
L
+
s
−
k
)
/
2
+
ε
)
,
if
​
s
<
L
≤
s
+
k
2
O
k
,
s
,
ε
​
(
N
L
−
k
⁡
(
k
+
1
)
/
2
+
ε
)
,
if
​
s
+
k
2
<
L
≤
2
​
s
T_{L,s}(N)=\begin{cases}O_{k,s,\varepsilon}(N^{L-k/2+\varepsilon}),\ &\text{if }L\leq s\\
O_{k,s,\varepsilon}(N^{(L+s-k)/2+\varepsilon}),\ &\text{if }s<L\leq s+k^{2}\\
O_{k,s,\varepsilon}(N^{L-k(k+1)/2+\varepsilon}),\ &\text{if }s+k^{2}<L\leq 2s\end{cases}
Notice that if
s
≤
k
2
s\leq k^{2}
, only the first two cases are possible.
Since
s
>
k
s>k
, by taking
p
=
δ
​
N
1
−
s
+
k
/
2
−
ε
s
−
1
<
1
p=\delta N^{\frac{1-s+k/2-\varepsilon}{s-1}}<1
for some sufficiently small constant
δ
=
δ
⁡
(
k
,
s
,
ε
)
>
0
\delta=\delta(k,s,\varepsilon)>0
, when
N
>
N
0
​
(
k
,
s
,
ε
)
N>N_{0}(k,s,\varepsilon)
, one can verify that the expected number of nontrivial solutions in
S
S
is
∑
L
=
k
2
​
s
p
L
​
T
L
,
s
​
(
N
)
=
O
k
,
s
,
ε
​
(
p
s
​
N
s
−
k
/
2
+
ε
)
<
p
​
N
/
2
.
\sum_{L=k}^{2s}p^{L}T_{L,s}(N)=O_{k,s,\varepsilon}\left(p^{s}N^{s-k/2+\varepsilon}\right)<pN/2.
Now we can apply the alteration method to get a subset of size at least
p
​
N
/
2
pN/2
that contains no nontrivial solutions. Hence there exists a
B
s
​
[
1
]
B_{s}[1]
subset of
𝒞
N
k
\mathcal{C}_{N}^{k}
of size
p
​
N
2
=
δ
2
​
N
k
−
2
​
ε
2
​
(
s
−
1
)
.
∎
\frac{pN}{2}=\frac{\delta}{2}N^{\frac{k-2\varepsilon}{2(s-1)}}.\qed
Therefore, given
M
=
N
c
M=N^{c}
for some
0
<
c
<
k
2
​
(
k
−
1
)
0<c<\frac{k}{2(k-1)}
, when
N
N
is sufficiently large, we have
g
⁡
(
M
)
≥
⌊
k
+
2
​
c
−
2
​
ε
2
​
c
⌋
=
⌊
1
+
(
k
−
2
​
ε
)
​
log
⁡
N
2
​
log
⁡
M
⌋
.
g(M)\geq\bigg\lfloor\frac{k+2c-2\varepsilon}{2c}\bigg\rfloor=\bigg\lfloor 1+\frac{(k-2\varepsilon)\log N}{2\log M}\bigg\rfloor.
This shows that, in the interval setting, one cannot force such a conclusion
for all subsets of size
N
O
⁡
(
k
/
2
k
)
N^{O(k/2^{k})}
with the same number of variables.
Remark 3.3
.
In the general setting, one can still obtain a universal lower bound by a greedy
argument. Let
R
R
be an integral domain and
T
⊆
R
T\subseteq R
be finite, and write
𝒞
T
k
=
{
(
n
,
n
2
,
…
,
n
k
)
:
n
∈
T
}
⊆
R
k
\mathcal{C}_{T}^{k}=\{(n,n^{2},\ldots,n^{k}):n\in T\}\subseteq R^{k}
.
Let
H
=
∞
H=\infty
if
char
⁡
(
R
)
=
0
\mathrm{char}(R)=0
, and
H
=
char
⁡
(
R
)
−
1
H=\mathrm{char}(R)-1
otherwise. For
M
≤
|
T
|
M\leq|T|
, put
g
T
(
M
)
=
max
{
h
∈
ℕ
:
h
≤
H
,
there exists a
B
h
[
1
]
subset of
𝒞
T
k
of size
M
}
.
g_{T}(M)=\max\{h\in\mathbb{N}:h\leq H,\ \text{there exists a }B_{h}[1]\text{ subset of }\mathcal{C}_{T}^{k}\text{ of size }M\}.
In general, good estimates for the number of solutions to (
1
)
in
T
T
may not be available. Nevertheless, a standard greedy argument gives a
B
h
​
[
1
]
B_{h}[1]
subset of
𝒞
T
k
\mathcal{C}_{T}^{k}
of size
≫
h
|
T
|
1
/
(
2
​
h
−
1
)
\gg_{h}|T|^{1/(2h-1)}
for every positive integer
h
≤
H
h\leq H
. Consequently, if
M
=
|
T
|
c
M=|T|^{c}
for some
0
<
c
<
1
0<c<1
, then, for
|
T
|
|T|
sufficiently large,
g
T
​
(
M
)
≥
min
⁡
{
H
,
⌈
c
+
1
2
​
c
⌉
−
1
}
.
g_{T}(M)\geq\min\left\{H,\left\lceil\frac{c+1}{2c}\right\rceil-1\right\}.
4.
Proof of Corollaries
1.6
and
1.8
4.1.
Proof of Corollary
1.6
We first prove a combinatorial lemma.
Lemma 4.1
.
Let
𝒜
⊆
∏
j
∈
Λ
Ω
j
\mathcal{A}\subseteq\prod_{j\in\Lambda}\Omega_{j}
, where
Λ
\Lambda
and
the
Ω
j
\Omega_{j}
’s are finite nonempty sets. If
𝒜
\mathcal{A}
contains no
m
m
elements
𝐮
1
,
…
,
𝐮
m
\mathbf{u}_{1},\ldots,\mathbf{u}_{m}
satisfying
u
h
,
j
≠
u
t
,
j
(
1
≤
h
<
t
≤
m
,
j
∈
Λ
)
,
u_{h,j}\neq u_{t,j}\qquad(1\leq h<t\leq m,\ j\in\Lambda),
then
|
𝒜
|
≤
(
m
−
1
)
​
∑
j
∈
Λ
∏
r
∈
Λ
r
≠
j
|
Ω
r
|
.
|\mathcal{A}|\leq(m-1)\sum_{j\in\Lambda}\prod_{\begin{subarray}{c}r\in\Lambda\\
r\neq j\end{subarray}}|\Omega_{r}|.
Proof.
Choose a maximal coordinatewise separated collection
𝐮
1
,
…
,
𝐮
q
∈
𝒜
\mathbf{u}_{1},\ldots,\mathbf{u}_{q}\in\mathcal{A}
. Then
q
≤
m
−
1
q\leq m-1
, and by
maximality every element of
𝒜
\mathcal{A}
shares a coordinate with some
𝐮
ℓ
\mathbf{u}_{\ell}
. For each fixed
ℓ
\ell
and
j
j
, at most
∏
r
≠
j
|
Ω
r
|
\prod_{r\neq j}|\Omega_{r}|
elements of the ambient product have
j
j
-th
coordinate
u
ℓ
,
j
u_{\ell,j}
. Summing over
ℓ
≤
q
\ell\leq q
and
j
∈
Λ
j\in\Lambda
gives the result.
∎
Next we prove Corollary
1.6
by adapting the proof from
[
20
, Section 9]
.
Proof of Corollary
1.6
.
We will use the notation
I
♯
:=
{
1
,
2
,
…
,
k
}
∖
I
I^{\sharp}:=\{1,2,\ldots,k\}\setminus I
for a
given subset
I
⊆
{
1
,
2
,
…
,
k
}
I\subseteq\{1,2,\ldots,k\}
. Given
S
⊆
[
N
]
S\subseteq[N]
, for a
set
I
⊆
{
1
,
2
,
…
,
k
}
I\subseteq\{1,2,\ldots,k\}
and for a vector of integers
z
→
=
(
z
i
)
i
∈
I
\vec{z}=(z_{i})_{i\in I}
, let
r
I
​
(
z
→
)
r_{I}(\vec{z})
be the number of ordered
s
s
-tuples
(
x
1
,
…
,
x
s
)
∈
S
s
(x_{1},\ldots,x_{s})\in S^{s}
with pairwise distinct entries such that
∑
ℓ
=
1
s
x
ℓ
i
=
z
i
,
i
∈
I
.
\sum_{\ell=1}^{s}x_{\ell}^{i}=z_{i},\qquad i\in I.
Let
G
J
​
(
S
)
G_{J}(S)
denote the number of pairs of such ordered
s
s
-tuples with
equal
i
i
-th power sums for every
i
∈
J
i\in J
. Equivalently,
G
J
​
(
S
)
=
∑
z
→
r
J
​
(
z
→
)
2
.
G_{J}(S)=\sum_{\vec{z}}r_{J}(\vec{z})^{2}.
Since
r
J
r_{J}
has total mass
≫
s
|
S
|
s
\gg_{s}|S|^{s}
and support of size
O
s
​
(
N
∑
i
∈
J
i
)
O_{s}(N^{\sum_{i\in J}i})
, Cauchy–Schwarz gives
(18)
G
J
(
S
)
≫
s
|
S
|
2
​
s
N
−
∑
i
∈
J
i
.
G_{J}(S)\gg_{s}|S|^{2s}N^{-\sum_{i\in J}i}.
For any
z
→
=
(
z
i
)
i
∈
J
\vec{z}=(z_{i})_{i\in J}
, we have
r
J
​
(
z
→
)
=
∑
(
z
j
)
j
∈
J
♯
1
≤
z
j
≤
s
​
N
j
r
[
k
]
​
(
z
1
,
…
,
z
k
)
.
r_{J}(\vec{z})=\sum_{\begin{subarray}{c}(z_{j})_{j\in J^{\sharp}}\\
1\leq z_{j}\leq sN^{j}\end{subarray}}r_{[k]}(z_{1},\ldots,z_{k}).
Let
P
z
→
P_{\vec{z}}
denote the set of vectors
(
z
j
)
j
∈
J
♯
(z_{j})_{j\in J^{\sharp}}
such
that
r
[
k
]
​
(
z
1
,
…
,
z
k
)
>
0
r_{[k]}(z_{1},\ldots,z_{k})>0
. Then, by Cauchy–Schwarz,
G
J
​
(
S
)
\displaystyle G_{J}(S)
≤
∑
z
→
|
P
z
→
|
​
∑
(
z
j
)
j
∈
J
♯
1
≤
z
j
≤
s
​
N
j
r
[
k
]
​
(
z
1
,
…
,
z
k
)
2
\displaystyle\leq\sum_{\vec{z}}|P_{\vec{z}}|\sum_{\begin{subarray}{c}(z_{j})_{j\in J^{\sharp}}\\
1\leq z_{j}\leq sN^{j}\end{subarray}}r_{[k]}(z_{1},\ldots,z_{k})^{2}
≤
max
z
→
⁡
|
P
z
→
|
⋅
G
[
k
]
​
(
S
)
,
\displaystyle\leq\max_{\vec{z}}|P_{\vec{z}}|\cdot G_{[k]}(S),
where
G
[
k
]
​
(
S
)
=
∑
w
→
r
[
k
]
​
(
w
→
)
2
G_{[k]}(S)=\sum_{\vec{w}}r_{[k]}(\vec{w})^{2}
.
Suppose for contradiction that, for every
z
→
=
(
z
i
)
i
∈
J
\vec{z}=(z_{i})_{i\in J}
, the set
P
z
→
P_{\vec{z}}
contains no
m
m
vectors
𝐮
1
,
…
,
𝐮
m
\mathbf{u}_{1},\ldots,\mathbf{u}_{m}
satisfying
u
h
,
j
≠
u
t
,
j
(
1
≤
h
<
t
≤
m
,
j
∈
J
♯
)
.
u_{h,j}\neq u_{t,j}\qquad(1\leq h<t\leq m,\ j\in J^{\sharp}).
Then Lemma
4.1
gives
(19)
max
z
→
|
P
z
→
|
≪
k
(
m
−
1
)
∑
h
∈
J
♯
N
(
∑
j
∈
J
♯
j
)
−
h
≪
k
m
N
(
∑
j
∈
J
♯
j
)
−
1
.
\max_{\vec{z}}|P_{\vec{z}}|\ll_{k}(m-1)\sum_{h\in J^{\sharp}}N^{(\sum_{j\in J^{\sharp}}j)-h}\ll_{k}mN^{(\sum_{j\in J^{\sharp}}j)-1}.
Now Corollary
1.5
, applied to the unrestricted ordered
solutions, gives
G
[
k
]
(
S
)
≪
k
,
ε
N
s
−
k
⁡
(
k
+
1
)
/
2
+
ε
|
S
|
s
≪
k
,
ε
N
ε
|
S
|
s
,
G_{[k]}(S)\ll_{k,\varepsilon}N^{s-k(k+1)/2+\varepsilon}|S|^{s}\ll_{k,\varepsilon}N^{\varepsilon}|S|^{s},
since
G
[
k
]
​
(
S
)
G_{[k]}(S)
is a subcount of the unrestricted count and
s
=
k
⁡
(
k
+
1
)
/
2
s=k(k+1)/2
. Combining this estimate with inequality (
19
), we get
G
J
(
S
)
≪
k
,
ε
m
N
(
∑
j
∈
J
♯
j
)
−
1
+
ε
|
S
|
s
.
G_{J}(S)\ll_{k,\varepsilon}mN^{(\sum_{j\in J^{\sharp}}j)-1+\varepsilon}|S|^{s}.
Comparing this with inequality (
18
), and using
∑
i
∈
J
i
+
∑
j
∈
J
♯
j
=
s
,
\sum_{i\in J}i+\sum_{j\in J^{\sharp}}j=s,
we obtain
|
S
|
s
≪
k
,
ε
m
N
s
−
1
+
ε
.
|S|^{s}\ll_{k,\varepsilon}mN^{s-1+\varepsilon}.
Choosing
ε
<
1
/
(
k
2
+
k
+
1
)
\varepsilon<1/(k^{2}+k+1)
, this contradicts the assumption
|
S
|
≥
m
2
/
k
⁡
(
k
+
1
)
​
N
1
−
2
/
(
k
2
+
k
+
1
)
|S|\geq m^{2/k(k+1)}N^{1-2/(k^{2}+k+1)}
for all sufficiently large
N
N
.
Hence there exist some
z
→
=
(
z
i
)
i
∈
J
\vec{z}=(z_{i})_{i\in J}
and
m
m
vectors
𝐮
1
,
…
,
𝐮
m
∈
P
z
→
\mathbf{u}_{1},\ldots,\mathbf{u}_{m}\in P_{\vec{z}}
such that
u
h
,
j
≠
u
t
,
j
(
1
≤
h
<
t
≤
m
,
j
∈
J
♯
)
.
u_{h,j}\neq u_{t,j}\qquad(1\leq h<t\leq m,\ j\in J^{\sharp}).
For each
1
≤
h
≤
m
1\leq h\leq m
, choose an ordered
s
s
-tuple
(
x
1
​
h
,
…
,
x
s
​
h
)
∈
S
s
(x_{1h},\ldots,x_{sh})\in S^{s}
with pairwise distinct entries whose full power-sum vector is
(
z
→
,
𝐮
h
)
(\vec{z},\mathbf{u}_{h})
, and set
A
h
=
{
x
1
​
h
,
…
,
x
s
​
h
}
.
A_{h}=\{x_{1h},\ldots,x_{sh}\}.
Then
|
A
h
|
=
s
|A_{h}|=s
, and the sets
{
A
h
}
1
≤
h
≤
m
\{A_{h}\}_{1\leq h\leq m}
satisfy the required equalities for
j
∈
J
j\in J
and inequalities for
j
∈
J
♯
j\in J^{\sharp}
. This finishes the proof.
∎
4.2.
Proof of Corollary
1.8
We will deduce the corollary from a more technical one, given as follows:
Corollary 4.2
.
Suppose
0
<
θ
<
1
0<\theta<1
,
k
≥
1
k\geq 1
. Put
k
′
=
⌈
k
1
−
θ
⌉
,
s
=
k
′
​
(
k
′
+
1
)
2
.
k^{\prime}=\left\lceil\frac{k}{1-\theta}\right\rceil,\qquad s=\frac{k^{\prime}(k^{\prime}+1)}{2}.
Then there is
N
0
=
N
0
​
(
k
,
θ
)
N_{0}=N_{0}(k,\theta)
such that, whenever
N
≥
N
0
N\geq N_{0}
, for any integer
m
≥
2
m\geq 2
and
C
⊆
(
N
,
N
+
N
θ
]
∩
ℤ
C\subseteq(N,N+N^{\theta}]\cap\mathbb{Z}
satisfying
|
C
|
>
m
s
​
N
θ
⁡
(
1
−
1
/
(
s
+
1
)
)
|C|>m^{s}N^{\theta(1-1/(s+1))}
, the following holds. For every
1
≤
j
≤
k
1\leq j\leq k
,
there exist elements
x
i
,
h
∈
C
x_{i,h}\in C
with
1
≤
i
≤
s
1\leq i\leq s
and
1
≤
h
≤
m
1\leq h\leq m
, such that, writing
P
h
=
∏
i
=
1
s
x
i
,
h
(
1
≤
h
≤
m
)
,
P_{h}=\prod_{i=1}^{s}x_{i,h}\qquad(1\leq h\leq m),
we have, for all
1
≤
h
<
t
≤
m
1\leq h<t\leq m
,
|
P
h
−
P
t
|
∈
[
κ
1
​
N
s
−
j
,
κ
2
​
N
s
−
j
⁡
(
1
−
θ
)
]
,
|P_{h}-P_{t}|\in[\kappa_{1}N^{s-j},\kappa_{2}N^{s-j(1-\theta)}],
where
κ
1
,
κ
2
>
0
\kappa_{1},\kappa_{2}>0
depend only on
k
k
and
θ
\theta
.
To apply this corollary we first observe that
since
[
N
(
1
−
α
)
/
r
/
2
]
[N^{(1-\alpha)/r}/2]
contains at most
half the elements of
C
C
, at least half the elements of
C
C
are contained in
D
:=
(
N
(
1
−
α
)
/
r
/
2
,
N
1
/
r
]
D:=(N^{(1-\alpha)/r}/2,N^{1/r}]
. Next, for
θ
=
1
/
2
​
r
\theta=1/\sqrt{2r}
we partition the interval
D
D
into subintervals
(
M
j
,
M
j
+
M
j
θ
]
,
j
=
1
,
2
,
…
(M_{j},\ M_{j}+M_{j}^{\theta}],\ j=1,2,\ldots
with
M
1
=
N
(
1
−
α
)
/
r
/
2
M_{1}=N^{(1-\alpha)/r}/2
. Now, if the
j
j
-th interval contained at most
M
j
θ
−
α
/
4
M_{j}^{\theta-\alpha}/4
many elements of
C
C
, then the total number of elements of
C
C
in all such intervals would be at most
≪
∫
M
1
N
1
/
r
d
​
x
4
​
x
α
≪
N
(
1
−
α
)
/
r
4
​
(
1
−
α
)
<
|
C
|
2
,
\ll\ \int_{M_{1}}^{N^{1/r}}{dx\over 4x^{\alpha}}\ \ll\ {N^{(1-\alpha)/r}\over 4(1-\alpha)}\ <\ {|C|\over 2},
for
0
<
α
<
1
/
2
0<\alpha<1/2
. Hence, for some choice of
j
=
j
0
j=j_{0}
, the interval contains at least
M
j
0
θ
−
α
/
4
M_{j_{0}}^{\theta-\alpha}/4
elements in
C
C
. Let
M
′
=
M
j
0
M^{\prime}=M_{j_{0}}
and let
M
=
⌊
(
M
′
)
r
⌋
M=\lfloor(M^{\prime})^{r}\rfloor
.
Next, assume
r
r
has the form
k
′
​
(
k
′
+
1
)
/
2
k^{\prime}(k^{\prime}+1)/2
for some
integer
k
′
k^{\prime}
. We apply Corollary
4.2
to the interval
(
M
′
,
M
′
+
(
M
′
)
θ
]
(M^{\prime},M^{\prime}+(M^{\prime})^{\theta}]
and its intersection with
C
C
, and with parameters
s
=
r
s=r
,
m
=
⌊
(
(
M
′
)
θ
r
+
1
−
α
/
4
)
1
/
r
⌋
m=\lfloor((M^{\prime})^{\frac{\theta}{r+1}-\alpha}/4)^{1/r}\rfloor
,
and
j
=
k
j=k
. From our choice for
θ
\theta
we note that
k
=
k
′
−
1
k=k^{\prime}-1
, so we also get
j
=
k
′
−
1
=
⌊
2
​
r
⌋
−
1
j=k^{\prime}-1=\lfloor\sqrt{2r}\rfloor-1
. Since
r
≥
3
r\geq 3
, we must have
j
≥
1
j\geq 1
. From this
it follows that
|
P
h
−
P
t
|
∈
[
κ
1
​
M
1
−
2
r
+
1
r
,
κ
2
​
M
1
−
2
r
+
3
r
−
2
r
3
]
.
|P_{h}-P_{t}|\in[\kappa_{1}M^{1-\sqrt{2\over r}+\frac{1}{r}},\kappa_{2}M^{1-\sqrt{2\over r}+\frac{3}{r}-\sqrt{\frac{2}{r^{3}}}}].
Note that
P
h
≤
(
M
′
+
(
M
′
)
θ
)
r
≤
2
​
M
P_{h}\leq(M^{\prime}+(M^{\prime})^{\theta})^{r}\leq 2M
when
N
N
(and hence
M
′
M^{\prime}
) is sufficiently large. Taking
κ
<
min
⁡
(
κ
1
,
κ
2
)
\kappa<\min(\kappa_{1},\kappa_{2})
finishes the proof.
We conclude the paper with a proof of Corollary
4.2
.
Proof of Corollary
4.2
.
Let
S
=
C
−
N
=
{
c
−
N
:
c
∈
C
}
⊆
[
1
,
N
θ
]
S=C-N=\{c-N:c\in C\}\subseteq[1,N^{\theta}]
. Since
1
−
1
s
+
1
=
1
−
2
k
′
​
(
k
′
+
1
)
+
2
>
1
−
2
k
′
​
(
k
′
+
1
)
+
1
,
1-\frac{1}{s+1}=1-\frac{2}{k^{\prime}(k^{\prime}+1)+2}>1-\frac{2}{k^{\prime}(k^{\prime}+1)+1},
the density assumption is strong enough to apply Corollary
1.6
to
S
S
, with
N
θ
N^{\theta}
in place of
N
N
, with
k
′
k^{\prime}
in place of
k
k
,
and with
J
=
{
1
,
2
,
…
,
k
′
}
∖
{
j
}
.
J=\{1,2,\ldots,k^{\prime}\}\setminus\{j\}.
Thus we obtain
m
m
subsets of
S
S
, written as
{
a
1
,
h
,
…
,
a
s
,
h
}
(
1
≤
h
≤
m
)
,
\{a_{1,h},\ldots,a_{s,h}\}\qquad(1\leq h\leq m),
such that their
r
r
-th power sums agree for every
r
∈
J
r\in J
, while their
j
j
-th power sums are pairwise distinct.
For
1
≤
h
≤
m
1\leq h\leq m
, put
P
h
=
∏
i
=
1
s
(
N
+
a
i
,
h
)
.
P_{h}=\prod_{i=1}^{s}(N+a_{i,h}).
Fix
1
≤
h
<
t
≤
m
1\leq h<t\leq m
, and put
D
h
,
t
=
(
−
1
)
j
+
1
​
(
∑
i
=
1
s
a
i
,
h
j
−
∑
i
=
1
s
a
i
,
t
j
)
.
D_{h,t}=(-1)^{j+1}\left(\sum_{i=1}^{s}a_{i,h}^{j}-\sum_{i=1}^{s}a_{i,t}^{j}\right).
Then
D
h
,
t
D_{h,t}
is a nonzero integer and
1
≤
|
D
h
,
t
|
≤
2
​
s
​
N
j
​
θ
.
1\leq|D_{h,t}|\leq 2sN^{j\theta}.
Using the Taylor expansion for
log
⁡
(
1
+
x
)
\log(1+x)
, we have
|
log
⁡
P
h
P
t
|
=
|
D
h
,
t
j
​
N
j
+
E
h
,
t
|
,
\left|\log{P_{h}\over P_{t}}\right|=\left|{D_{h,t}\over jN^{j}}+E_{h,t}\right|,
where all terms with
1
≤
r
≤
k
′
1\leq r\leq k^{\prime}
,
r
≠
j
r\neq j
, vanish, and
|
E
h
,
t
|
≤
∑
r
=
k
′
+
1
∞
2
​
s
​
N
r
​
θ
r
​
N
r
≪
k
,
θ
N
(
k
′
+
1
)
​
(
θ
−
1
)
<
N
−
k
−
ε
|E_{h,t}|\leq\sum_{r=k^{\prime}+1}^{\infty}{2sN^{r\theta}\over rN^{r}}\ll_{k,\theta}N^{(k^{\prime}+1)(\theta-1)}<N^{-k-\varepsilon}
for some
ε
>
0
\varepsilon>0
. Hence, for sufficiently large
N
N
,
c
1
​
N
−
j
≤
|
log
⁡
P
h
P
t
|
≤
c
2
​
N
−
j
⁡
(
1
−
θ
)
.
c_{1}N^{-j}\leq\left|\log{P_{h}\over P_{t}}\right|\leq c_{2}N^{-j(1-\theta)}.
Since the logarithm tends to
0
0
, this gives
c
3
N
j
≤
|
P
h
P
t
−
1
|
≤
c
4
N
j
⁡
(
1
−
θ
)
.
{c_{3}\over N^{j}}\leq\left|{P_{h}\over P_{t}}-1\right|\leq{c_{4}\over N^{j(1-\theta)}}.
Finally, since
P
t
≍
s
N
s
P_{t}\asymp_{s}N^{s}
, multiplying by
P
t
P_{t}
gives
|
P
h
−
P
t
|
∈
[
κ
1
​
N
s
−
j
,
κ
2
​
N
s
−
j
⁡
(
1
−
θ
)
]
.
|P_{h}-P_{t}|\in[\kappa_{1}N^{s-j},\kappa_{2}N^{s-j(1-\theta)}].
Since this holds for every
1
≤
h
<
t
≤
m
1\leq h<t\leq m
, and since
N
+
a
i
,
h
∈
C
N+a_{i,h}\in C
,
the corollary follows.
∎
References
[1]
A. Alpers and R. Tijdeman
(2007)
The two-dimensional Prouhet-Tarry-Escott problem
.
J. Number Theory
123
(
2
),
pp. 403–412
.
External Links:
ISSN 0022-314X,1096-1658
,
Document
,
Link
,
MathReview (Maurice Mignotte)
Cited by:
§1
.
[2]
P. Borwein and C. Ingalls
(1994)
The Prouhet-Tarry-Escott problem revisited
.
Enseign. Math. (2)
40
(
1-2
),
pp. 3–27
.
External Links:
ISSN 0013-8584
,
MathReview (Ekkehard Krätzel)
Cited by:
§1
.
[3]
P. Borwein and M. J. Mossinghoff
(2000)
Polynomials with height 1 and prescribed vanishing at 1
.
Experiment. Math.
9
(
3
),
pp. 425–433
.
External Links:
ISSN 1058-6458,1944-950X
,
Link
,
MathReview (Sergeĭ V. Konyagin)
Cited by:
§1.1
.
[4]
P. Borwein
(2009)
“The Prouhet–Tarry–Escott problem”, ch. 11
.
In
Computational Excursions in Analysis and Number Theory, CMS Books in Mathematics
,
pp. 85–96
.
External Links:
ISBN ISBN 0-387-95444-9
Cited by:
§1
,
§1
.
[5]
J. Bourgain, C. Demeter, and L. Guth
(2016)
Proof of the main conjecture in Vinogradov’s mean value theorem for degrees higher than three
.
Ann. of Math. (2)
184
(
2
),
pp. 633–682
.
External Links:
ISSN 0003-486X,1939-8980
,
Document
,
Link
,
MathReview (Ben Joseph Green)
Cited by:
§1.2
,
§1
.
[6]
T. Caley
(2013)
The Prouhet-Tarry-Escott problem for Gaussian integers
.
Math. Comp.
82
(
282
),
pp. 1121–1137
.
External Links:
ISSN 0025-5718,1088-6842
,
Document
,
Link
,
MathReview (Rainer Dietmann)
Cited by:
§1
.
[7]
D. Coppersmith, M. J. Mossinghoff, D. Scheinerman, and J. M. VanderKam
(2024)
Ideal solutions in the Prouhet-Tarry-Escott problem
.
Math. Comp.
93
(
349
),
pp. 2473–2501
.
External Links:
ISSN 0025-5718,1088-6842
,
Document
,
Link
,
MathReview (Michael P. Knapp)
Cited by:
§1
.
[8]
J. Friedlander and J. Lagarias
(1987)
On the distribution in short intervals of integers having no large prime factor
.
J. Number Theory
25
,
pp. 249–273
.
Cited by:
§1.2
,
Remark 1.9
.
[9]
W. T. Gowers
(1998)
A new proof of Szemerédi’s theorem for arithmetic progressions of length four
.
Geom. Funct. Anal.
8
(
3
),
pp. 529–551
.
External Links:
ISSN 1016-443X,1420-8970
,
Document
,
Link
,
MathReview (D. R. Heath-Brown)
Cited by:
§1.1
.
[10]
L. Hua
(1938)
On Tarry’s problem
.
Q. J. Math., Oxf. Ser.
9
,
pp. 315–320
(
English
).
External Links:
ISSN 0033-5606
,
Document
Cited by:
§1
.
[11]
L. Hua
(1949)
Improvement of a result of Wright
.
J. London Math. Soc.
24
,
pp. 157–159
.
External Links:
ISSN 0024-6107,1469-7750
,
Document
,
Link
,
MathReview (D. H. Lehmer)
Cited by:
§1
.
[12]
S. Kongsiriwong and S. Prugsapitak
(2014)
On the number of solutions of the Tarry-Escott problem of degree two and the related problem over some finite fields
.
Period. Math. Hungar.
69
(
2
),
pp. 190–198
.
External Links:
ISSN 0031-5303,1588-2829
,
Document
,
Link
,
MathReview (Boqing Xue)
Cited by:
§1
.
[13]
G. Petridis
(2012)
New proofs of Plünnecke-type estimates for product sets in groups
.
Combinatorica
32
(
6
),
pp. 721–733
.
External Links:
ISSN 0209-9683,1439-6912
,
Document
,
Link
,
MathReview (Olof Sisask)
Cited by:
§1.1
.
[14]
L. B. Pierce
(2019)
The Vinogradov mean value theorem [after Wooley, and Bourgain, Demeter and Guth]
.
Note:
Séminaire Bourbaki. Vol. 2016/2017. Exposés 1120–1135
External Links:
ISSN 0303-1179,2492-5926
,
ISBN 978-2-85629-897-8
,
Document
,
Link
,
MathReview (Rainer Dietmann)
Cited by:
§1.2
.
[15]
S. Prugsapitak
(2012)
The Tarry-Escott problem of degree two
.
Period. Math. Hungar.
65
(
1
),
pp. 157–165
.
External Links:
ISSN 0031-5303,1588-2829
,
Document
,
Link
,
MathReview (Maurice Mignotte)
Cited by:
§1
.
[16]
C. Reiher and T. Schoen
(2024)
Note on the theorem of Balog, Szemerédi, and Gowers
.
Combinatorica
44
(
3
),
pp. 691–698
.
External Links:
ISSN 0209-9683,1439-6912
,
Document
,
Link
,
MathReview (Xuancheng Shao)
Cited by:
§1.1
.
[17]
R. P. Stanley
(1997)
Enumerative combinatorics. Vol. 1
.
Cambridge Studies in Advanced Mathematics
, Vol.
49
,
Cambridge University Press, Cambridge
.
Note:
With a foreword by Gian-Carlo Rota,
Corrected reprint of the 1986 original
External Links:
ISBN 0-521-55309-1; 0-521-66351-2
,
Document
,
Link
,
MathReview (Wayne M. Dymacek)
Cited by:
§2
.
[18]
E. Szemerédi
(1969)
On sets of integers containing no four elements in arithmetic progression
.
Acta Math. Acad. Sci. Hungar.
20
,
pp. 89–104
.
External Links:
ISSN 0001-5954,1588-2632
,
Document
,
Link
,
MathReview (H. Halberstam)
Cited by:
§2
.
[19]
T. D. Wooley
(1996)
Some remarks on Vinogradov’s mean value theorem and Tarry’s problem
.
Monatsh. Math.
122
(
3
),
pp. 265–273
.
External Links:
ISSN 0026-9255,1436-5081
,
Document
,
Link
,
MathReview (R. C. Baker)
Cited by:
§1
.
[20]
T. D. Wooley
(2012)
Vinogradov’s mean value theorem via efficient congruencing
.
Ann. of Math. (2)
175
(
3
),
pp. 1575–1627
.
External Links:
ISSN 0003-486X,1939-8980
,
Document
,
Link
,
MathReview (Rainer Dietmann)
Cited by:
§1.2
,
§4.1
.
[21]
T. D. Wooley
(2017)
Discrete Fourier restriction via efficient congruencing
.
Int. Math. Res. Not. IMRN
(
5
),
pp. 1342–1389
.
External Links:
ISSN 1073-7928,1687-0247
,
Document
,
Link
,
MathReview (Ben Joseph Green)
Cited by:
§1.2
.
[22]
T. D. Wooley
(2019)
Nested efficient congruencing and relatives of Vinogradov’s mean value theorem
.
Proc. Lond. Math. Soc. (3)
118
(
4
),
pp. 942–1016
.
External Links:
ISSN 0024-6115,1460-244X
,
Document
,
Link
,
MathReview (Moubariz Z. Garaev)
Cited by:
§1.2
,
§1.2
,
§1.2
,
Remark 1.7
,
§1
,
§1
.
[23]
E. M. Wright
(1948)
Equal sums of like powers
.
Bull. Amer. Math. Soc.
54
,
pp. 755–757
.
External Links:
ISSN 0002-9904
,
Document
,
Link
,
MathReview (N. G. W. H. Beeger)
Cited by:
§1
.
[24]
E. M. Wright
(1948)
The Prouhet-Lehmer problem
.
J. Lond. Math. Soc.
23
,
pp. 279–285
(
English
).
External Links:
ISSN 0024-6107
,
Document
Cited by:
§1
,
§1
,
§1
.
[25]
E. M. Wright
(1935)
On Tarry’s problem. I
.
Q. J. Math., Oxf. Ser.
6
,
pp. 261–267
(
English
).
External Links:
ISSN 0033-5606
,
Document
Cited by:
§1
.