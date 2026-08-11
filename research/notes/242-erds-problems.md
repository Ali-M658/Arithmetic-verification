---
title: 242 | Erdős Problems
id: 242-erds-problems
tags:
- hyperbolic-pillow-heat-novelty-813161
- erdos-straus-conjecture
created: '2026-08-09T08:46:19.617117Z'
updated: '2026-08-09T09:36:32.364016Z'
source: https://www.erdosproblems.com/242
source_domain: www.erdosproblems.com
fetched_at: '2026-08-09T08:46:19.616842Z'
fetch_provider: builtin
status: evergreen
type: note
tier: institutional
content_type: article
deprecated: false
summary: 'Erdos Problems database (maintained by Thomas F. Bloom), problem #242, the
  Erdos-Straus conjecture: for every n>2 there exist distinct positive integers x<y<z
  with 4/n=1/x+1/y+1/z. Traces the conjecture to Oblath (1948/1950), records Mordell''s
  (1969) and Terzi''s (1971) modular exception classes, Vaughan''s (1970) bound x
  exp(-c(log x)^{2/3}) on exceptions up to x, verification up to n<=10^18 (Miller-Dumas,
  2025), an equivalence to a covering-system-type statement (Bloom-Elsholtz 2022),
  and states the Elsholtz-Tao (2013) result sum_{p<=N} f(p) = N(log N)^{2+o(1)}, f(p)<=p^{3/5+o(1)},
  and the Elsholtz-Planitzer (2020) almost-all lower bound f(n) >= (log n)^{log 6
  + o(1)}. Confirms: (a) Erdos-Straus concerns a SINGLE representation of the FIXED
  rational 4/n, with no equal-sum-of-denominators condition and no second triple to
  match against -- structurally distinct from Section 5''s two-triple, two-symmetric-function-matching
  problem. Citation format given: T. F. Bloom, Erdos Problem #242, https://www.erdosproblems.com/242,
  accessed 2026-08-09.'
---

*Suggested by [[egyptian-fractions]] — canonical curated statement of the Erdos-Straus conjecture with precise state-of-the-art asymptotic results*

242 | Erdős Problems
Forum
Inbox
Favourites
Tags
More
FAQ
Prizes
Problem Lists
Definitions
Links
Forum
Menu
Inbox
Favourites
Tags
FAQ
Prizes
Problem Lists
Definitions
Links
Go
Go
Dual View
Random Solved
Random Open
FALSIFIABLE
Open, but could be disproved with a finite counterexample.
For every $n>2$ there exist distinct integers $1\leq x<y<z$ such that\[\frac{4}{n} = \frac{1}{x}+\frac{1}{y}+\frac{1}{z}.\]
#242
:
[Er50c]
[Er61]
[Er79]
[ErGr80]
[Va99,1.13]
number theory
|
unit fractions
The open status of this problem reflects the current belief of the owner of this website. There may be literature on this problem that I am unaware of, which may partially or completely solve the stated problem. Please do your own literature search before expending significant effort on solving this problem. If you find any relevant literature not mentioned here, please add this in a comment.
The
Erdős-Straus conjecture
. Perhaps the first place it appears in the literature is in a paper of Obláth
[Ob50]
(submitted in 1948), which describes it as a conjecture of Erdős.
The existence of a representation of $4/n$ as the sum of at most four distinct unit fractions follows trivially from a greedy algorithm.
Schinzel conjectured (see
[Si56]
) the generalisation that, for any fixed $a$, if $n$ is sufficiently large in terms of $a$ then there exist distinct integers $1\leq x<y<z$ such that\[\frac{a}{n} = \frac{1}{x}+\frac{1}{y}+\frac{1}{z}.\]When $a=5$ this conjecture is due to Sierpiński
[Si56]
. For more background and results on this generalisation see Pomerance and Weingartner
[PoWe25]
.
It suffices to prove this when $n$ is prime. This has been verified for all $n\leq 10^{18}$
[MiDu25]
.
There are many partial results, some of which are listed below.
Obláth
[Ob50]
noted it is true if $n+1$ is divisible by a prime $\equiv 3\pmod{4}$. This implies almost all $n$ have the required decomposition.
Arguing via parametric solutions, Mordell
[Mo69]
proved it is true for all $n$ except those congruent to one of $\{1,121,169,289,361,529\}$ modulo $840$.
Terzi
[Te71]
extended this to prove that it is true for all $n$ except those congruent to one of $198$ possible bad congruences modulo $120120$.
Vaughan
[Va70]
proved that the number of exceptions in $[1,x]$ is\[\leq x \exp(-c(\log x)^{2/3})\]for some constant $c>0$.
This conjecture is equivalent (see Theorem 1 of
[BlEl22]
) to the statement that, for any prime $p$, there exist integers $a,c,d\geq 1$ such that either $p\equiv -a/c\pmod{4acd-1}$ or $p\equiv -\frac{4c^2d+1}{k}\pmod{4cd}$ for some $k\mid 4c^2d+1$.
Bright and Loughran
[BrLo20]
have shown there is no Brauer-Manin obstruction to the existence of solutions.
If $f(n)$ counts the number of solutions then Elsholtz and Tao
[ElTa13]
have proved\[\sum_{p\leq N}f(p)=N(\log N)^{2+o(1)}\]and $f(p)\leq p^{3/5+o(1)}$ for all primes $p$.
Elsholtz and Planitzer
[ElPl20]
have proved that for almost all $n$\[f(n) \geq (\log n)^{\log 6+o(1)}.\]
View the LaTeX source
This page was last edited 07 May 2026.
View history
External data from
the database
- you can help update this
Formalised statement?
Yes
Related OEIS sequences:
A073101
A075245
A075246
A075247
A075248
A287116
18 comments on this problem
0 claimed proofs for this problem
Likes this problem
old-bielefelder
,
jgold
,
TFBloom
,
jbbaehr22
,
Dogmachine
,
ArdaErgun
Interested in collaborating
jgold
,
Bradford
,
auro
Currently working on this problem
jgold
,
alansbor
,
Bradford
,
auro
,
mosesluajh
This problem looks difficult
Vjeko_Kovac
,
TFBloom
,
TerenceTao
This problem looks tractable
auro
,
jbbaehr22
The results on this problem could be formalisable
jbbaehr22
I am working on formalising the results on this problem
jbbaehr22
,
auro
Additional thanks to
: Alfaiz and Bryce Orloski
When referring to this problem, please use the original sources of Erdős. If you wish to acknowledge this website, the recommended citation format is:
T. F. Bloom, Erdős Problem #242, https://www.erdosproblems.com/242, accessed 2026-08-09
Previous
Next