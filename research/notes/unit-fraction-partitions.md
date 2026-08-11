---
title: Unit Fraction Partitions
id: unit-fraction-partitions
tags:
- hyperbolic-pillow-heat-novelty-813161
- ternary-egyptian-fractions
- recreational-mathematics
created: '2026-08-09T08:46:25.068935Z'
updated: '2026-08-09T09:36:32.386867Z'
source: http://www.mathpages.com/home/kmath332.htm
source_domain: www.mathpages.com
fetched_at: '2026-08-09T08:46:25.066984Z'
fetch_provider: builtin
status: evergreen
type: note
tier: practitioner
content_type: article
deprecated: false
summary: K. S. Brown (mathpages, kmath332), 'Unit Fraction Partitions.' Tabulates
  U(k) = number of unordered 3-part unit-fraction partitions of 1/k for k=1..24 (e.g.
  U(12)=160, U(24)=366), and decomposes these by gcd of the three denominators via
  inclusion-exclusion (e.g. 202 of the 366 partitions of 1/24 are non-primitive, via
  U(12)+U(8)-U(4)=160+70-28=202). Defines D(k) = least integer such that 3-part partitions
  of 1/k correspond to partitions of D(k)/k into three divisors of D(k) (D(1)=12,
  giving 12=6+4+2=6+3+3=4+4+4; D(2)=2520). Gives specific non-unity-numerator multiplicity
  counts as worked examples (5/12 has 9 primitive 3-part partitions, 7/12 has 5) and
  an exact closed form for the 2-part case, U2(N) = [(2a1+1)(2a2+1)...(2at+1)+1]/2
  for N with prime-factorization exponents a1,...,at. Directly demonstrates that per-value
  multiplicity tabulation for f_a(n) (task Q1.3) is an established recreational/expository
  tradition, BUT the specific value 3/4 is not among the worked examples in this page,
  and no page found anywhere in this fetcher's search cross-tabulates multiplicities
  of TWO DIFFERENT target values against each other (i.e., nothing here searches for
  coincidences between the partition list of one k and another).
---

*Suggested by [[egyptian-fractions]] — mathpages page specifically on counting unit fraction partitions of unity, relevant to multiplicity-of-representations question*

Unit Fraction Partitions
Unit Fraction Partitions
Consider the Diophantine equation

                n    1        1
              SUM   ----  =  ---
               i=0  a(i)      k

where n, k, and a(i), i=0 to n, are positive integers.  Empirically we
note that, for fixed n, the number of unordered solution sets for the
array a() increases roughly (though not uniformly) as k increases.  
For example, with n=2 the number of solution sets for 0 < k < 25
are
         3  10  21  28  36  57  42  70  79  96  62 160
        59 136 196 128  73 211  80 292 245 157  93 366

Can the number of solutions for a() be given explicitly in terms of k
for any fixed n?

When n equals 2 this asks for the number of partitions of 1/k into
three unit fractions.  I think a complete answer to this question 
will be difficult, because it includes as a special case the 
unproved conjecture (of Erdos and Straus) that 4/k can always be 
expressed as a sum of three unit fractions.  (Clearly any such 
expression can be divided through by 4 to give 1/k as a sum of 
three unit fractions.)  According to Richard Guy's Unsolved Problems 
in Number Theory, "there is a good account of this problem in 
Mordell's book, where it is shown that the conjecture is true, 
except possibly in cases where n is congruent to 1^2, 11^2, 13^2, 
17^2, 19^2, or 23^2 mod 840."  Also, it's been verified numerically 
for all k < 10^8.

Of course, we can account for many of the partitions of 1/k simply 
in terms of the partitions of 1/j where j divides k.  For example,
of the 366 partitions of 1/24, only 164 are "primitive" in the
sense that the gcd of the three denominators is 1.  Letting U(n)
denote the number of 3-part unit fraction partitions of n, the 
non-primitive partitions of 1/24 can be counted by inclusion-
exclusion as follows

   U(24/2) + U(24/3) - U(24/6)  =  160 + 70 - 28  =  202

In general, the number of 3-part partitions of 1/k can be grouped 
according to the greatest common divisor (gcd) of their denominators.  
The results are summarized in the table below.  (For reasons of space 
I've shown only gcd's up to 21.)

                        gcd of denominators

 k    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21
 -   -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 1    1  1  1
 2    4  1  2  1  1  1
 3    8  4  1  3  2  1  1  0  1
 4   11  4  2  1  3  2  1  1  1  1  0  1
 5   13  6  6  1  1  3  2  1  0  1  1  0  0  0  1
 6   20  8  4  4  1  1  6  3  2  2  1  1  1  1  1  0  0  1
 7   12  8  4  4  3  1  1  3  2  0  1  0  0  1  1  0  0  0  0  0  1
 8   20 11 10  4  3  2  1  1  4  3  2  2  1  1  0  1  1  1  0  1  0...
 9   28 10  8  2  6  4  1  1  1  4  3  3  1  1  2  0  0  1  1  0  1...
10   34 13  6  6  4  6  2  1  2  1  5  3  2  2  2  1  1  0  0  1  1...
11   20 10  7  6  2  4  1  0  0  0  1  3  2  1  1  0  1  0  0  0  0...
12   55 20 11  8  9  4  5  4  2  1  2  1  9  6  3  3  2  2  2  2  1...
13   19 11  5  0  3  1  5  3  1  0  1  0  1  3  2  0  0  0  0  1  0...

Letting G(k,j) denote the number of 3-part unit fraction partitions
of 1/k whose denominators have a gcd of j, we have

                    G(kn,jn) = G(k,j)

It follows that, for example, the sum of G(24,2j) for j=1,2,... is 
equal to the sum of G(12,j) for j=1,2,..., which equals U(12) = 160. 
Similarly the sum of G(24,3j), j=1,2,... is just equal to U(8) = 28.  
Then by inclusion-exclusion we know that the sum of G(24,j) for 
all j divisible by either 2 or 3 is given by

   U(12) + U(8) - U(4)    =    160 + 70 - 28     =    202

By the same approach we see that there are 285 non-primitive partitions 
of 1/30, given by

 U3(15) + U3(10) + U3(6) - U3(5) - U3(3) - U3(2) + U3(1)

     =    196 + 96 + 57 - 36 - 21 - 10 + 3     =    285

Once the non-primitive partitions have been accounted for, the 
remaining partitions counted by the terms G(k,j) for j < 3k and j 
coprime to k.  For example, there are 55 primitive partitions of 
1/12, and there are 9 primitive partitions of 5/12, and 5 of 7/12, 
and so on.

It might seem at first that the above table implies no solution
of 4/13, because there are no primitive solutions for 1/13 with
gcd of 4.  However, there are solutions with gcd=8 and gcd=20, so 
we can multiply these by 4 to express 4/13 as a sum of three unit 
fractions.  However, the table also shows that there are no 3-part 
partitions of 1/11 with gcd of 8, 16, 24, or 32.  It follows that 
8/11 cannot be expressed as a sum of three unit fractions.

Another approach is based on the fact that for any positive integer 
k there exists a least integer D(k) such that the partitions of 1/k 
into three unit fractions correspond to the partitions of D(k)/k into 
three divisors of D(k).  For example, we have D(1)=12 because the 
3-part unit fraction partitions of 1/1 correspond to the partitions 
of 12 into three divisors of 12: 

   12    =    6 + 4 + 2     =    6 + 3 + 3     =    4 + 4 + 4

Similarly, we have D(2) = 2520 because the 3-part unit fraction 
partitions of 1/2 correspond to the partitions of 1260 into exactly 
three divisors of 2520:

      1260  =  840 + 360 +  60
               840 + 315 + 105
               840 + 280 + 140
               840 + 252 + 168
               840 + 210 + 210
               630 + 504 + 126
               630 + 420 + 210
               630 + 315 + 315
               504 + 504 + 252
               420 + 420 + 420

The first few values of D(k) are 12, 2520, 65520, 3603600, ...  It may 
be easier to express these in terms of the exponents in their prime
factorizations:

 k   exponents of D(k)
--  ---------------------------------
 1  21
 2  3211
 3  421101
 4  422111
 5  52211110001
 6  53221111100001
 7  6221101101
 8  542111110001100000001
 9  532111111011001000001
10  632121111011000001001
11  432111111001001000101
12  6422121111111101010011000000000000001
13  5322111010100010010011
14  73221111111111110001110000010100000000000000001 
15  85322111111011110100111000000000000000000000000000001
16  642211211101100010001110000000001
17  3421111111110101000011100010000000000000000000000000000000000000001
18  742311121111111011001110000000100000000101
19  7421111111100100001011101000001000000000001
20  7432211111111111111111111101100000000000000000100...   (421)

It's clear that D(k) is always divisible by k+1.  Also, it appears 
that D(k) is always divisible by  q = k^2 + k + 1.  Moreover, if q is 
a prime, then it is the largest prime dividing D(k).  In any case, the 
largest prime divisor of D(k) is no greater than q.

Another interesting approach is to place the original equation 

                 1/k  =  1/a + 1/b + 1/c                     (1)

in "dimensionless" form by simply multiplying through by k:

                   1 = x + y + z                             (2)

where x=k/a, y=k/b, and z=k/c.  Equation (1) is just the equation
of a diagonal plane in 3D space, and we are looking for rational
points on this plane whose numerators divide k.  We could try rotating 
this plane into a 2D space to simplify things (although the rotation 
might not preserve rationality).

Interestingly, if we make the substitutions 

        X = a/k - 1         Y = b/k - 1       Z = c/k - 1

then the original equation (1) becomes

                  XYZ - X - Y - Z  =  2                      (3)

This equation seems to arise in many different problems.  Here the 
only effect of k is to determine which of the rational solutions 
of (3) give integer values of a,b,c according to

           a = (X+1)k       b = (Y+1)k      c = (Z+1)k

In other words, k just "scales up" the rational solutions of (2), 
resulting in a certain number of them being integers.  If k=1 then 
the only integer solutions (a,b,c) correspond to the positive integer 
solutions (X,Y,Z) of (3), namely 

                  (1,2,5)     (1,3,3)     (2,2,2)

For k=2 we can accept half-integer solutions of (3), and so on.  In
effect this is a way of "stratifying" the rational solutions of an
equation.  It could probably be applied to other equations as well,
i.e., given an equation with finitely many positive integer solutions,
count the numbers of rational solutions whose common denominators 
divide k=1,2,3,...

Still another approach is to lower our ambitions and determine the
number of 2-part unit fraction partitions of 1/k.  Let U2(N) denote 
the number of distinct partitions of 1/N into exactly two unit 
fractions (not counting order).  The first several values of U2(N) 
for N = 1, 2, 3,... are

    1  2  2  3  2  5  2  4  3  5  2  8  2  5  5  5  2  8 ...

Surrisingly, this sequence doesn't appear in Sloane's Encyclopedia, 
so maybe it's worth covering this admittedly simple case.  Clearly 
U2(N) depends only on the exponents in the prime factorization of N.
In general, if N has the factorization

                  N = (p1^a1)(p2^a2)...(pt^at)

then
               (2 a1 + 1)(2 a2 + 1) ... (2 at + 1)  +  1
    U2(N)   =  ----------------------------------------- 
                                  2

Incidentally, if N is square-free the above formula reduces to 
(3^t + 1)/2.  This sequence of numbers (1,2,5,14,41,122,365,...) 
DOES appear in Sloane's Encyclopedia, although I don't know if 
the reference relates this sequence to the numbers of partitions 
of 1/N into two unit fractions for square-free integers N with 
t prime divisors.

The function U2(N) is formally similar to the number-of-divisors
function tau(N), although U2 is not multiplicative.  We could
generalize this to give the family of functions

                   (j a1 + 1)(j a2 + 1)...(j at + 1)  + (j-1)
       F_j(N)  =  -------------------------------------------
                                      j

We know that F_1(N) gives the number of divisors of N, and F_2(N)
gives the number of 2-part unit fraction partitions of N.  I'm not
sure what, if anything, is counted by F_3(N).
Return to MathPages Main Menu