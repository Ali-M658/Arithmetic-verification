# Literature: the Prouhet–Tarry–Escott problem and its variants, as used in `proof.md`

Every statement below is backed by a verbatim quote in `sources/NOTES.md`, with page or section
numbers, taken from the file named there in `sources/`. As with `theory/audibility/sources`,
the fetched third-party files themselves are kept locally and not committed. They are pinned by
`sources/SHA256SUMS`. Nothing here is recalled. Sources that
could not be retrieved are listed at the end as instrument gaps. Every explicit numerical
solution used in `proof.md` was re-verified by exact integer arithmetic before use, in
`witnesses.py` and `structure.py`.

Notation: $[A]=_k[B]$ means equal power sums for exponents $1,\dots,k$; $n$ is the size and $k$
the degree. A solution is *ideal* if $n=k+1$.

## 1. The minimal size $N(k)$: what is known

**P. Borwein and C. Ingalls, "The Prouhet–Tarry–Escott problem revisited", L'Enseignement
Math. (2) 40 (1994) 3–27.** Retrieved as the e-periodica page scans (`sources/BorweinIngalls1994_*`).

- **Definitions.** $N(k)$ is "the least integer $n$ such that there is a solution of size $n$
  and degree $k$" (p. 6). $M(k)$ is the least size with "degree exactly $k$ and no higher" (p. 7).
- **Prop. 2:** $N(k)\ge k+1$.
- **Prop. 3:** $N(k)\le\frac12k(k+1)+1$, proved by pigeonhole.
- **Stronger estimates (p. 7).** "Slightly stronger upper bounds are discussed in [22]
  [Wright 1935] and [15] [Melzak 1961] … only improve the estimates to
  $N(k)\le\frac12(k^2-3)$ ($k$ odd), $\frac12(k^2-4)$ ($k$ even)."
- **Hua's bound (p. 7).** "Hua in [11] shows $M(k)\le(k+1)\bigl(\log\frac12(k+2)/\log(1+1/k)+1\bigr)\sim k^2\log k$."
  This concerns the exact-degree quantity $M(k)$ and is of order $k^2\log k$.
- **Lemma 2 (p. 6).** The Prouhet doubling step $[A]=_k[B]\Rightarrow[A,B+M]=_{k+1}[A+M,B]$.
- **Open problems (§6, p. 26).**
  - "3. Prove $N(k)\le o(k^2)$. 4. Prove $M(k)\le O(k^2)$."
  - "No progress on questions 3 and 4 has been made for many years."
  - "The big prize is to find ideal solutions of all degrees, if indeed they exist."
- **Explicit symmetric ideal solutions** (table p. 9, perfect 7-sets p. 25), used as inputs:
  - size 4: $\{\pm3,\pm11\}$, $\{\pm7,\pm9\}$;
  - size 6: $\{\pm4,\pm9,\pm13\}$, $\{\pm1,\pm11,\pm12\}$;
  - size 8: $\{\pm2,\pm16,\pm21,\pm25\}$, $\{\pm5,\pm14,\pm23,\pm24\}$;
  - size 7: $\{-51,-33,-24,7,13,38,50\}$ and four more perfect 7-sets;
  - size 9: Letac's two 9-sets;
  - size 10: Letac's solution.
- **Definition of odd symmetric solutions (p. 8).** "$\sum\alpha_i^j=0$ for $j=1,3,5,\dots,k-1$",
  with $B=-A$.

**Z. A. Melzak, "A note on the Tarry–Escott problem", Canad. Math. Bull. 4 (1961) 233–237,
doi:10.4153/CMB-1961-025-1.**

- It records Wright's bound $K(n)\le(n^2+4)/2$ as "the best bound known so far" (pp. 233–234).
- It gives individual numerical upper bounds for $n\le29$ (Table 1, p. 237).
- No asymptotic improvement.

**T. D. Wooley.**

- "Vinogradov's mean value theorem via efficient congruencing", Ann. of Math. 175 (2012)
  1575–1627, Thm 1.3: $W(k,h)\le k^2+k-2$.
- "Nested efficient congruencing and relatives of Vinogradov's mean value theorem",
  Proc. LMS 118 (2019) 942–1016, Thm 13.1: $W(k,h)\le\frac12k(k+1)+1$.
- $W(k,2)=M(k)$ is the exact-degree quantity. Wooley quotes Hua's bound as
  $W(k,h)\le k^2(\log k+O(1))$.

**E. Croot, J. Mao, C. H. Yip, arXiv:2609.05061 (Sept. 2026)**, p. 1:

- "Using a pigeonhole principle argument one can easily see that $P(k,m)\le k(k+1)/2+1$."
- $P(k,2)=N(k)$, and "it is an open problem to determine if $P(k,2)=k+1$. It is only known
  that $P(k,2)=k+1$ when $2\le k\le9$ and $k=11$."
- This is the most recent statement retrieved. It names no bound on $N(k)$ better than
  quadratic.

**Bottom line used in `proof.md` §4.** The best known bound on $N(k)$ is quadratic. No
$o(k^2)$ bound is known, and Borwein–Ingalls list this as open. No retrieved source contains an
$O(k\log k)$ bound for $N(k)$. The only $k\log k$ statement found (Caley 2013, p. 2) concerns
the "easier Waring" number $v(k)$, not $N(k)$.

## 2. Ideal solutions up to degree 12

- **Known sizes.** "Ideal solutions in the PTE problem over $\mathbb Z$ are known for
  $n\le10$ and $n=12$" (Coppersmith–Mossinghoff–Scheinerman–VanderKam, *Ideal solutions in the
  Prouhet–Tarry–Escott problem*, arXiv:2304.11254, Math. Comp. 93 (2024) 2473–2501, p. 2).
  Size 11 is open.
- **Size-11 searches with no solution found:**
  - Borwein–Ingalls (perfect symmetric, $|\cdot|\le363$);
  - Borwein–Lisoněk–Percival 2003 (height 2000);
  - CMSV 2023 ("No new integral solutions are found for $9\le n\le16$").
- **Size 9.** Exactly two solutions are known up to equivalence, both found by Letac (1942):
  $\{-98,-82,-58,-34,13,16,69,75,99\}$ and $\{-169,-161,-119,-63,8,50,132,148,174\}$, each with
  $B=-A$. These are quoted in Borwein–Ingalls p. 9, BLP p. 2069 and CMSV (3).
- **Size 10.**
  - Letac's solution and Smyth's elliptic-curve family (Borwein–Ingalls Prop. 4: rational
    points of $x^2y^2-13x^2-13y^2+121=0$ give size-10 ideal symmetric solutions).
  - BLP's two further solutions $\pm\{71,131,180,307,308\}$/$\pm\{99,100,188,301,313\}$ and
    $\pm\{18,245,331,471,508\}$/$\pm\{103,189,366,452,515\}$.
  - P. Borwein, P. Lisoněk, C. Percival, *Computational investigations of the Prouhet–Tarry–Escott
    problem*, Math. Comp. 72 (2003) 2063–2070, doi:10.1090/S0025-5718-02-01504-1.
- **Size 12.**
  - Kuosa–Meyrignac–Chen (1999): $\pm\{22,61,86,127,140,151\}$/$\pm\{35,47,94,121,146,148\}$
    (CMSV (5)).
  - Broadhurst (2007).
  - Choudhry–Wróblewski (2008), an infinite family from an elliptic curve (CMSV (6), (7)).
- **Parametric families.** "Parametric ideal solutions are known for $n=1,\dots,8$ and $n=10$"
  (BLP p. 2063). Choudhry (arXiv:2207.12726, 2022) counts polynomial parametrisations "only when
  $k\le7$". The sources use "parametric" in different senses (`sources/NOTES.md` §10).
- **Gloden's two-parameter size-7 family** (BLP p. 2064, from Gloden, *Mehrgradige
  Gleichungen*, 2nd ed. 1944). It is used in `witnesses.py` and `structure.py`. A transcription
  slip (a dropped factor $f$ in $\alpha_3$) was caught by the exact check. The printed formula,
  with the factor, is valid for all 740 tested parameter pairs.
- **Chernick.** Chernick (Amer. Math. Monthly 44 (1937) 626–633) gave two-parameter symmetric
  families of sizes 5 and 7. We know this only through the Chen survey (A.1.21, A.1.35) and
  Borwein–Ingalls p. 9; the paper itself was not retrieved.
- **Non-symmetric ideal solutions.** These "have only been discovered for … degrees $n\le7$"
  (Chen survey p. 13).

## 3. Odd powers only; negative exponents

**Chen Shuwen, *A survey of the Prouhet–Tarry–Escott problem and its generalizations*,
arXiv:2506.11429 (2025), and eslpower.org.**

- **Equal sums of odd powers** (Appendix A.1.6, A.1.17, A.1.26, A.1.33). These are size-$L$
  solutions for exponents $1,3,\dots,2L-3$, $L=3,\dots,6$:
  - $[1,5,5]=[2,3,6]$, listed as the "Smallest solution, by computer search" (A.48); Moessner (1939) gave parametric solutions of this type;
  - $[1,13,17,23]=[3,9,21,21]$ (Gloden, Xeroudakes–Moessner, Lander, Choudhry);
  - $[3,19,37,51,53]=[9,11,43,45,55]$ (Gloden);
  - $[7,91,173,269,289,323]=[29,59,193,247,311,313]$ (Chen 2000, A.313), three further non-negative
    solutions by Wróblewski (2009, A.314–A.316), and one integer solution of his with a negative entry.

  These give $N_{\rm odd}(L)=L$ for $3\le L\le6$ (`proof.md` Lemma 1.5) and are inputs to
  `witnesses.py`.
- **Lifting (eslpower.org, Theorem 3).** "If $[a_1,\dots,a_m]=[b_1,\dots,b_m]$
  ($k=1,3,\dots,2n-1$) then $[T+a_i,T-b_i]=[T+b_i,T-a_i]$ ($k=1,2,\dots,2n$)." Our
  Proposition 2.2 is this lifting applied to a configuration.
- **Negative exponents** (survey §1.4 and Appendix A.5, "33 distinct types … with $k_1<0$ and
  $k_n>0$"):
  - type $(-1,1)$: $[4,10,12]=[5,6,15]$;
  - type $(-1,1,3)$: $[3,10,15,30]=[4,5,21,28]$ (A.685). In our language this is the balanced
    3-configuration of `proof.md` Theorem 3.1, the smallest pencil point;
  - type $(-1,1,5)$: $[81,374,585,891]=[85,286,702,858]$;
  - longer mixed types up to $(-3,\dots,3)$.
- **Our system is not tabulated.** Type $(-1,1,3,\dots,2L-3)$ for $L\ge4$ does not appear, and
  neither does the unequal-size version that the genus needs (`sources/NOTES.md` §7).
- **Choudhry 2011.** A. Choudhry, "Equal sums of like powers, both positive and negative",
  Rocky Mountain J. Math. 41 (2011) 737–763, is cited by Chen for a three-parameter solution of
  type $(-1,1)$. It is not retrieved (gap).

**Relation to the repository.** `theory/audibility/proof.md` Theorem C(3) reduces integer
sharpness of Theorem A at $n$ cone points to the balanced, size-$2n$ case of the same system.
It records witnesses for $n=3,4$ and none for $n=5$ with orders $\le120$.

## 4. Prouhet (1851) and Thue–Morse

Borwein–Ingalls p. 4 records Prouhet's 1851 general solution ("$n^{k+1}$ numbers separable into
$n$ sets …") and Wright's 1959 account of it. This is the construction behind [Sig]
Theorem N, whose $2^{2L-1}$ is replaced here by $O(L^2)$.

## 5. Instrument gaps (not retrieved; nothing above depends on their content beyond what is quoted from secondary sources)

| source | result |
|---|---|
| E. M. Wright, "On Tarry's problem (I)", Quart. J. Math. Oxford 6 (1935) 261–267 | OUP HTTP 403; known via Borwein–Ingalls p. 7 and Melzak p. 234 |
| L.-K. Hua, "On Tarry's problem", Quart. J. Math. Oxford 9 (1938) 315–320 | OUP HTTP 403 |
| L.-K. Hua, *Introduction to Number Theory* (1982), ch. 18 | Springer paywall; known via Borwein–Ingalls p. 7 and Wooley |
| L.-K. Hua, J. London Math. Soc. 24 (1949); T. D. Wooley, Monatsh. Math. 122 (1996) | no open copy |
| P. Borwein, *Computational Excursions in Analysis and Number Theory* (2002), ch. 11 | Springer paywall |
| J. Chernick, Amer. Math. Monthly 44 (1937) 626–633 | Taylor & Francis HTTP 403 |
| E. M. Wright, Amer. Math. Monthly 66 (1959) 199–201 | closed |
| C. J. Smyth, Math. Comp. 57 (1991) 817–823 | AMS HTTP 429 (rate limit); known via Borwein–Ingalls Prop. 4 |
| T. Caley, PhD thesis (Waterloo 2012) | bot-check page, not bypassed; the arXiv Gaussian-integer paper was used |
| A. Choudhry, Rocky Mountain J. Math. 41 (2011) 737–763 | Project Euclid returned HTML, not the PDF |
| A. Gloden, *Mehrgradige Gleichungen* (1944) | not found; the family is used as printed in BLP 2003 |

The retrieval log, with URLs and HTTP results, is the table at the end of `sources/NOTES.md`.
