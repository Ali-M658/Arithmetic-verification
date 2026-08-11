---
title: Egyptian Fractions
id: egyptian-fractions
tags:
- hyperbolic-pillow-heat-novelty-813161
- source-hub
- egyptian-fractions
created: '2026-08-09T08:42:29.912143Z'
updated: '2026-08-09T09:36:32.180238Z'
source: https://www.ics.uci.edu/~eppstein/numth/egypt/
source_domain: ics.uci.edu
fetched_at: '2026-08-09T08:42:29.911896Z'
fetch_provider: builtin
status: evergreen
type: note
tier: practitioner
content_type: article
deprecated: false
summary: 'David Eppstein''s Egyptian-fractions hub page (UC Irvine), a curated link
  index to the research and recreational Egyptian-fraction literature, algorithms
  (greedy, binary remainder, splitting), and unsolved problems (odd greedy termination,
  etc.). SOURCE HUB, not itself a primary source. Key outbound leads followed in Phase
  2: Thomas Bloom''s density-conjecture paper (arXiv:2112.03726) resolving an Erdos-Graham
  question that any positive-upper-density set of integers contains a finite subset
  with reciprocal sum exactly 1; Erdos, Butler and Graham''s last-paper-era work ''Egyptian
  fractions with each denominator having three distinct prime divisors'' (2015); Ron
  Graham''s survey ''Paul Erdos and Egyptian fractions''; Allan Swett''s Erdos-Straus
  conjecture verification page (solvable for n up to 10^12); K. S. Brown''s mathpages
  page on counting unit-fraction partitions of unity (kmath332, fetched); and ''A
  loving look at the unitary partition problem'' (partitioning into DISTINCT positive
  integers whose reciprocals sum to 1 -- adjacent to but distinct from Section 5''s
  problem, no sum-of-parts constraint). No page here or in its link graph addresses
  two triples with BOTH equal integer sum AND equal reciprocal sum.'
---

Egyptian Fractions
Nowadays, we usually write non-integer numbers either as
fractions (\(\tfrac27\)) or decimals (0.285714). The floating point
representation used in computers is another representation very
similar to decimals. But the ancient Egyptians (as far as we can
tell from the documents now surviving) used a number system based
on
unit fractions
: fractions with one in the numerator. This
idea let them represent numbers like \(\tfrac17\) easily enough; other
numbers such as \(\tfrac27\) were represented as sums of unit fractions
(e.g. \(\tfrac27=\tfrac14+\tfrac{1}{28}\)). Further, the same fraction
could not be used twice (so \(\tfrac27=\tfrac17+\tfrac17\) is
not allowed). We call a formula representing a sum of distinct unit
fractions an
Egyptian fraction
.
This notation is cumbersome and difficult to compute with, so
the Egyptian scribes made large tables so they could look up the
answers to arithmetic problems. However there is also some
interesting mathematics associated with the problem of
converting
modern fraction notation into the Egyptian form. A
number of famous mathematicians have looked at this problem, and
invented different ways of doing this conversion process. Each of
these methods has advantages and disadvantages in terms of the
complexity of the Egyptian fraction representations it produces and
in terms of the amount of time the conversion process takes. There
are still some unsolved problems about whether some of these
processes finish, or whether they get into an infinite loop.
To investigate some of these questions, I wrote a
Mathematica
notebook, now called "Algorithms for Egyptian
Fractions", which as the title implies implements on the computer
some of these computation methods. A version of this notebook was
published as "Ten Algorithms for Egyptian Fractions" in
Mathematica in Education and Research
, vol. 4, no. 2, 1995, pp.
5-15, available online through
MathSource
.
Since then I have made several changes including improvements to
the binary remainder method and two new sections on reverse greedy
methods and brute force searches. I am making this updated version
available here.
Algorithms for Egyptian fractions:
Algorithms for Egyptian fractions
in
HTML format,
publication
information
, and
Mathematica source code
.
Python-based command-line tool for generating
Egyptian fractions
.
Mathematica package
,
also available
through MathSource
, as is
a different Egyptian fraction package
.
C++ source code
to brute force search for
representations with few terms and
C source code
to find certain solutions to \(4/n=1/x+1/y+1/z\)
Links to my social media:
Videos
from Ravi Boppana's YouTube Channel
include one
on
Ron Graham's
"77 theorem"
: all numbers greater than 77 are sums of denominators
of Egyptian fraction representations of one.
Two
preprints by Neil Epstein on Egyptian integral domains and Egyptian
rings
, systems of numbers for which every fraction can be written as
a sum of unit fractions.
Discussion
of Thomas Bloom's paper
"
On a density conjecture
about unit fractions
". Bloom proves that any positive-density set of
integers includes the denominators of an Egyptian fraction
representation of
1.
In a
later post
, I linked to a
Lean formalization of Bloom's proof
.
On
Erdős's last paper
: "
Egyptian fractions with each denominator having
three distinct prime divisors
" with Steve Butler and Ron Graham
(2015).
Egyptian
fractions with practical denominators
and
which
integer sequences form denominators of Egyptian fractions?
The
practical
numbers
can be defined as the positive integers \(n\) that only the
divisors of \(n\) are needed as the numerators of Egyptian fractions for
\(k/n\) with \(k\lt n\). The first post shows that every
rational number has an Egyptian fraction with only practical
denominators, and the second reports on my paper
"
Egyptian
fractions with denominators from sequences closed under doubling
"
generalizing this property of the practical numbers to many other
integer sequences.
Carmichael
polynomials from Egyptian fractions
. An equivalence between Egyptian
fraction representations of 1 and polynomial products of linear factors
that, when each factor is prime, produce Carmichael numbers.
Graham
on Erdős on Egyptian fractions
. Discusses the
paper
Paul
Erdős and Egyptian fractions
by Ron Graham.
Subgreedy
Egyptian expansions
and
even
greedy expansion
. An attempt to generalize the question of whether
the odd greedy expansion always terminates. Follow the greedy algorithm
for Egyptian fractions, but sometimes choose a denominator one larger
than the greedy algorithm would choose. Can you make these choices in a
way that allows the expansion to continue forever? Choosing the
denominator to be even in each step does not work: the expansion will
definitely terminate for those choices.
Modular
Egyptian fractions
. If \(p\) is coprime to the fractions in
an expansion, they have a well-defined sum mod \(p\). What is
the smallest denominator such that sums of fractions up to that value
cover all residues mod \(p\)?
Egyptian fractions with small denominators
. If you're trying to minimize the denominators in an Egyptian fraction for a number with a composite denominator, it usually works to take a multiple of the representation of one of its divisors.
An
Egyptian fraction non-algorithm
. Some valid algorithms start with
repeated copies of the same unit fraction and then make them distinct
using substitution rules that replacement two equal fractions by another
combination of fractions with the same sum. But replacement rules using
only linear functions of the denominator,
like \(\tfrac1k+\tfrac1k\Rightarrow\tfrac1k+\tfrac2k+\tfrac3k+\tfrac6k\),
will sometimes fail to terminate.
Engel
expansion
and
infinite
odd Engel expansions
. These are Egyptian fractions in which each
denominator is a multiple of the previous one. See
also
the
Wikipedia article on Engel expansion
.
Transcriptions of older network conversations:
Egyptian
topology on Q
.  Michael Barr defines a topological space in which a
sequence of rationals converges only if its terms have bounded length
Egyptian fraction expansions, and asks how this differs from the usual
Euclidean topology.
Perfect numbers and Carmichael numbers
.
Bill Daly shows how to use Egyptian fraction representations of integers
to generate counterexamples for primality-testing algorithms.
Why use Egyptian fractions?
Darrah
Chavey gives some explanations for the Egyptians' use of this
seemingly bizarre notation.
Donald T. Davis hypothesizes that
perfect numbers were first studied for their uses in simplifying
Egyptian fraction manipulation
.
Dave Ketcheson asks how to represent the
number one as an Egyptian fraction with odd denominators
.
Quentin Grady uses Egyptian fractions to
make up electrical engineering problems
.
Stan Wagon discovers that odd greedy
performs very poorly on 3/179
, throwing into question a
heuristic analysis from my paper. 3/2879 and 5/5809 are even
worse.
Stefan Bartels looks for the maximum
denominator
among all
k
-term representations for a given
number (or equivalently the closest (
k
-1)-term
underrepresentation), which is often found by the greedy algorithm,
and investigates work on the subject by Curtiss and others.
Kevin Brown looks for the minimum
denominator
among all \(k\)-term representations for a given
number. In particular for \(k=12\) he finds the representation
\[\frac16+\frac17+\frac18+\frac19+\frac1{10}+\frac1{14}
+\frac1{15}+\frac1{18}+\frac1{20}+\frac1{24}+\frac1{28}
+\frac1{30}.\]
Bill Taylor asks about a conjecture
that for any denominator, all sufficiently large numerators can be
expressed as a sum or difference of at most three unit
fractions
.
Fibonacci
Algorithm and Egyptian Fractions
. Liz asks Dr. Math how to find
numbers for which the greedy algorithm produces long expansions.
Other sites of interest:
Wikipedia:
Egyptian fractions
and
related articles
.
The
Universe of Discourse: Egyptian Fractions
.
Mark Dominus explains why the 2/n table in the Rhind Papyrus is
sufficient for calculation of any more general Egyptian fraction.
Math
Games: Egyptian Fractions
.  Ed Pegg describes the Rhind Papyrus and
the 4/n problem, including a pretty density plot of the number of terms
required in the shortest egyptian fraction representation of rationals
with small numerators and denominators.
Approximating
1 from below by \(n\) Egyptian fractions.
A short proof that the greedy algorithm finds the largest \(n\)-term
Egyptian fraction less than one.
Izzycat
investigates odd Egyptian fraction representations of unity
.
See also
more
wrong turns
and
this paper by P. Shiu
.
Web
Mathematica applet
for the greedy Egyptian fraction algorithm.
This
week's finds in Egyptian fractions
, John Baez.
Madison
Capps' science fair project
.
Binary
Egyptian Fractions
and
other Egyptian fraction papers
by Ernie Croot
.
Egyptian Fractions
page by Ron Knott.
Lecture
notes
from a section on Egyptian fractions in a history of math course
by Carl Eberhart, U. Kentucky, including a Maple implementation of the
greedy algorithm.
Best of Mathnerds:
the magnificent seven
asks for seven-term Egyptian fraction decompositions of 1, and describes a method for finding decompositions of any fraction
using a method based on Farey sequences
(essentially equivalent to
the continued fraction method
).
The 1998 British Informatics Olympiad
used a sample programming question on Egyptian fractions, with
sample solutions including
a
Java applet for calculating 4-term representations
of a value m/n by choosing a value d (sequentially testing d=1, d=2, d=3
etc), finding the divisors of nd (using a simple brute force loop rather
than any kind of factorization technique),
and looping through all permutations of the divisors testing
which ones have a prefix that sums to md (rather than using any kind of
dynamic program).
The Distribution of Prime Primitive Roots and Dense Egyptian
Fractions
, dissertation by Greg Martin.
Jim Loy's
Egyptian fraction page
.
Julian Steprans uses Egyptian fractions for a homework
assignment
.
The Erdos-Strauss
conjecture
. Allan Swett confirms that \(4/n=1/x+1/y+1/z\) is
solvable for \(n\) up to \(10^{12}\).
Kris'
Egyptian fraction applet
. Seems to be using binary remainders?
A loving look at the unitary partition problem
.
Which numbers can be partitioned into distinct positive integers, the
reciprocals of which add to one?
An odd
Egyptian puzzle
with
many solutions
.
Stan Wagon's problem of the week #848, on odd representations of
3/179.
K. S. Brown's extensive work on Egyptian fractions includes
pages speculating on
how the Egyptians
did it
as well as several on more number-theoretic concerns:
these pages on
unit fractions and
Fibonacci
,
the two Ohm
problem
,
counting unit fraction partitions of unity
,
minimizing
denominators in unit fraction expansions
,
minimizing the
max denominator in a t-term expansion of 1
,
odd greedy
stubbornness
,
irrationality of
quadratic sums
, and
wagon
trains and sticky wickets
The
CECM Inverse
Symbolic Calculator
also mentions including Egyptian fraction
routines.
Milo Gardner has done extensive research on the
historical
methods used by the Egyptians to construct their tables of
fractions.
.
Terrance
Nevin
uses greedy Egyptian fraction methods as a basis for
investigating the dimensions of the Egyptian pyramids.
The
Magma symbolic algebra system
uses
the
splitting method
for Egyptian fractions as an example of its sequence
manipulation features.
Is there a harmonic integer?
Stan Wagon asks if any integer \(k\)
has an Egyptian fraction representation 
\[k=\frac12+\frac13+\frac14+\frac15+\cdots+\frac1n\]
(Hint: consider the largest power of two less than or equal to
\(n\).)
Unit
Fractions
from Eric Weisstein's treasure trove of
Mathematics.
Undergraduate projects
. This list of possible projects includes
a very brief mention of Egyptian fractions.
Problem: sum of unit fractions
. Which numbers \(n/(n+1)\) have a
two-term Egyptian fraction
representation? Problem from a U. Georgia summer course in
mathematical problem solving.
Good
Math, Bad Math: Egyptian Fractions
.