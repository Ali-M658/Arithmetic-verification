# PTE literature: retrieved sources and verbatim quotes

Retrieval date: 2026-10-05. All quotes are copied from the fetched files named below. Two kinds of quote appear:

- **[text]**: copied from the text layer of the saved PDF/HTML (`.txt` next to it). Formulas in text layers are linearised. Where the extraction mangled a formula, the formula is given in readable form and marked "(formula as printed)".
- **[page image]**: transcribed from the scanned page image, because the OCR text of that page is garbled. This applies only to Borwein–Ingalls 1994. The page images were fetched from the e-periodica IIIF server and are bundled in `BorweinIngalls1994_EnsMath40_pages3-27.pdf` (PDF page i = journal page i+2).

Notation used in these notes (not inside quotes): `A =_k B` means equal power sums for exponents 1..k. N(k) is the least size of a nontrivial solution of degree k. M(k) / W(k,2) is the least size of a solution of degree exactly k, meaning the (k+1)-th power sums differ.

All explicit numerical solutions quoted below were re-checked by exact integer arithmetic (python `fractions`) for the stated exponent sets. Every one checked out.

---

## 0. Summary of the key findings (pointers to the quotes below)

1. **Upper bounds on N(k).** The best bound stated for the plain PTE minimal size N(k) is **quadratic**:
   - Proposition 3 of Borwein–Ingalls: `N(k) <= (1/2)k(k+1) + 1`, proved by pigeonhole.
   - The refinement attributed to Wright 1935 [22] and Melzak 1961 [15]: `N(k) <= (1/2)(k^2-3)` for k odd and `(1/2)(k^2-4)` for k even.
   - Borwein–Ingalls list "Prove N(k) <= o(k^2)" as an **open problem** (§6, Q3) and say "No progress on questions 3 and 4 has been made for many years".
   - No fetched source states any o(k^2) or O(k log k) bound on N(k).
2. **The O(k log k) form.** A bound like `(k+1)(floor(log(k+1)/log 2)+1)` does **not** appear in any fetched source. What Borwein–Ingalls attribute to Hua's book is a bound for the **exact-degree** quantity M(k):
   - `M(k) <= (k+1)( log(½(k+2)) / log(1+1/k) + 1 ) ~ k^2 log k`.
   - The denominator is `log(1+1/k) ~ 1/k`, not `log 2`. The bound is therefore order **k^2 log k**, not k log k.
   - Wooley quotes Hua's result as `W(k,h) <= k^2(log k + O(1))`.
   - Later improvements to the exact-degree quantity:
     - Wooley 1996: `W(k,2) <= ½k^2(log k + log log k + O(1))`.
     - Wooley 2012: `W(k,h) <= k^2+k-2`.
     - Wooley 2019, Theorem 13.1: `W(k,h) <= ½k(k+1)+1` for all k, h >= 2.
   - So today the exact-degree quantity has the same `½k(k+1)+1` bound as the pigeonhole bound for N(k).
3. **Known ideal sizes.** Ideal solutions are known for n <= 10 and n = 12. Size 11 is open.
   - Searches with no size-11 solution found: Borwein–Ingalls (symmetric, |entries| <= 363), BLP 2003 (symmetric, search limit 2000), CMSV 2023 (extended searches; no new integral solutions for 9 <= n <= 16).
4. **Reciprocal / negative exponents.** Yes, there is literature:
   - Chen Shuwen's survey treats exponent sets that include -1. Appendix A.5 covers 33 mixed-sign types, e.g. (k = -1, 1), (-1, 1, 3), (-1, 1, 5), (-1, 1, 2, 3), (-1, 0, 1, 2, 3), and up to (-3, ..., 3).
   - Choudhry, "Equal sums of like powers, both positive and negative", Rocky Mountain J. Math. 41(3) (2011) 737–763. This paper could not be fetched; see the instrument gaps.

---

## 1. Borwein & Ingalls 1994 (key survey)

- **Citation:** Peter Borwein and Colin Ingalls, "The Prouhet-Tarry-Escott problem revisited", L'Enseignement Mathématique (2) 40 (1994), fasc. 1-2, pp. 3–27. Received 13 Oct 1992.
- **e-periodica record:** pid `ens-001:1994:40::10` (article). The viewer page for journal p. 3 is `https://www.e-periodica.ch/digbib/view?pid=ens-001:1994:40::156`.
- **Files:**
  - `BorweinIngalls1994_EnsMath40_pages3-27.pdf`: 25 page scans.
    - Assembled from IIIF images `https://iiif.library.ethz.ch/iiif/2/e-periodica!ens!1994_040!ens-001_1994_040_000NN.jpg/full/1800,/0/default.jpg`, NN = 09..33.
    - The image URLs come from the manifest `https://www.e-periodica.ch/iiif/ens-001:1994:40/manifest`.
  - `BorweinIngalls1994_EnsMath40_pages3-27.txt`: e-periodica OCR of the article, one block per journal page.
  - `EnsMath40_1994_volume_OCR.txt`: the full-volume OCR from `https://www.e-periodica.ch/digbib/download/ocr-fulltext/ens-001:1994:40`.
- **Status:** retrieved in full (scans plus OCR). The e-periodica PDF endpoint (`/cntmng?pid=...`) sits behind a bot-verification page and was not used.

### Definitions (item 1)
- p. 4 [page image]: "This we will call the Prouhet-Tarry-Escott Problem. We call *n* the size of the solution and *k* the degree."
- p. 6 [page image]: "We are particularly interested in the solutions of small size and we define *N(k)* to be the least integer *n* such that there is a solution of size *n* and degree *k*."
- p. 6 [page image]: "PROPOSITION 2. N(k) ≥ k + 1 ."
- p. 6 [page image]: "Solutions of degree *k* and size *k* + 1 are called **ideal**."
- p. 7 [page image]: "We can also define *M(k)* to be the least *s* such that there is a solution of size *s* and degree exactly *k* and no higher."

### Upper bounds (item 1)
- p. 6 [page image]: "LEMMA 2. If {α₁, ..., αₙ} =ᵏ {β₁, ..., βₙ} then {α₁, ..., αₙ, β₁ + M, ..., βₙ + M} =ᵏ⁺¹ {α₁ + M, ..., αₙ + M, β₁, ..., βₙ} for any integer M."
- p. 6 [page image]: "COROLLARY 1. N(k) ≤ C2ᵏ ." … "As will be shown later N(k) = k + 1 for k = 1, ..., 9 so we can choose C to be 10/2⁹ for k ≥ 9, but this is unnecessary in light of the next proposition."
- p. 6 [page image]: "PROPOSITION 3. N(k) ≤ ½ k(k + 1) + 1 ."
  - The proof (pp. 6–7) is a pigeonhole count over s-tuples from {1..n}.
  - p. 7: "We may now choose s = ½k(k + 1) + 1".
- p. 7 [page image]: "Slightly stronger upper bounds are discussed in [22] and [15], but they are much more difficult to establish and only improve the estimates to
  N(k) ≤ { ½(k² − 3)  k odd ; ½(k² − 4)  k even } ."
  - [22] = Wright, On Tarry's Problem (I), Quart. J. Math. Oxford 6 (1935) 261–267.
  - [15] = Melzak, A Note on the Tarry-Escott Problem, Canad. Math. Bull. 4 (1961) 233–237.
- p. 7 [page image]: "Hua in [11] shows
  M(k) ≤ (k + 1) ( log ½(k + 2) / log (1 + 1/k) + 1 ) ∼ k² log k .
  This is also a considerably harder argument than the above bound for N(k)." (formula as printed)
  - [11] = Hua, Introduction to Number Theory, Springer 1982.
- p. 26, §6 "OPEN PROBLEMS" [page image]:
  - "1. Find an ideal solution for any size higher than 10 or find some degree for which an ideal solution does not exist. (Even a heuristic argument would be of interest.)"
  - "2. Find another class of solutions of size 9 or 10."
  - "3. Prove N(k) ≤ o(k²)."
  - "4. Prove M(k) ≤ O(k²)."
  - "7. Find a true algorithm, even an impractical one, that determines if there is an ideal solution of size 11."
  - "The big prize is to find ideal solutions of all degrees, if indeed they exist. Question 1 above is, of course, the first step. No progress on questions 3 and 4 has been made for many years."
- p. 15 [text, OCR]: "Note that we must use M(k) and not N(k) since we require exact solutions so that C ≠ 0." (OCR prints "C ^ 0". The context is the "easier" Waring bound in Proposition 9.)

### Symmetric solutions: definitions (item 2)
- p. 8 [page image]: "An **even ideal symmetric solution** of size *k* + 1 and odd degree *k* is of the form {±α₁, ..., ±α₍ₖ₊₁₎/₂}, {±β₁, ..., ±β₍ₖ₊₁₎/₂} and satisfies any of the following equivalent statements: Σ α_i^{2j} = Σ β_i^{2j} for j = 1, ..., (k−1)/2; Π (x² − α_i²) − Π (x² − β_i²) = C for some constant C; …"
- p. 8 [page image]: "An **odd ideal symmetric solution** of size *k* + 1 and even degree *k* is of the form {α₁, ..., α_{k+1}}, {−α₁, ..., −α_{k+1}} and satisfies any of the following equivalent statements: Σ_{i=1}^{k+1} α_i^j = 0 for j = 1, 3, 5, .., k − 1; Π (x − α_i) − Π (x + α_i) = C for some constant C; (1 − x)^{k+1} | Σ x^{α_i} − Σ x^{−α_i}."

### Explicit symmetric ideal solutions (item 2)
p. 9 [page image]:

> "Symmetric ideal solutions are only known for sizes n ≤ 10. Throughout this paper we call an odd symmetric ideal solution **perfect** if it forms a complete set of residues modulo n. Listed below are ideal symmetric solutions for sizes 2 ≤ n ≤ 10, the odd symmetric solutions (with even degrees) are all perfect. These solutions are listed in abbreviated symmetric form. For example the solution for size 6 is {±4, ±9, ±13}, {±1, ±11, ±12} and the solution for size 5 is {−8, −7, 1, 5, 9}, {8, 7, −1, −5, −9}."

The table on p. 9, verbatim. For odd n, B = −A.

```
2  {3},{1}
3  {−2, −1, 3}
4  {3, 11},{7, 9}
5  {−8, −7, 1, 5, 9}
6  {4, 9, 13},{1, 11, 12}
7  {−51, −33, −24, 7, 13, 38, 50}
8  {2, 16, 21, 25},{5, 14, 23, 24}
9  {−98, −82, −58, −34, 13, 16, 69, 75, 99}  and
   {−169, −161, −119, −63, 8, 50, 132, 148, 174}
10 {436, 11857, 20449, 20667, 23750},{12, 11881, 20231, 20885, 23738}  and
   {133225698289, 189880696822, 338027122801, 432967471212, 529393533005},
   {87647378809, 243086774390, 308520455907, 441746154196, 527907819623}
```

- pp. 9–10 [page image]: "Chernick discusses symmetric solutions up to size 8 in [4]. Sinha discusses some parametric ideal symmetric solutions in [18]. There are two solutions of size 9 and two of size 10 listed; three of these were found in the 1940's by Letac and Gloden (see [10]). The last solution was found by Smyth who has shown in [19] that one can generate infinitely many solutions of size 10. There are no known ideal solutions, symmetric or otherwise, of size 11 or higher."
- p. 10, Proposition 4 [page image]: "If x, y are rational solutions of x²y² − 13x² − 13y² + 121 = 0 then {±(4x+4y), ±(xy+x+y−11), ±(xy−x−y−11), ±(xy+3x−3y+11), ±(xy−3x+3y+11)}, {±(4x−4y), ±(xy−x+y+11), ±(xy+x−y+11), ±(xy−3x−3y−11), ±(xy+3x+3y−11)} gives rise to an ideal symmetric solution of size 10." The two listed size-10 solutions "correspond to (x, y) = (153/61, 191/79) and (x, y) = (−296313/249661, −1264969/424999)."
- p. 25 [page image], perfect size-7 and size-11 search:

  > "We were hoping to find a perfect solution of size 11 using this method, but we were only able to show that there is no such solution with coefficients in the range [−363, 363]. … We were able to compute all 7⁸ solutions mod 7³ to find that all perfect solutions of size 7 with coefficients in the range [−171, 171] are
  > {−51, −33, −24, 7, 13, 38, 50}
  > {−90, −86, −39, −5, 48, 77, 95}
  > {−116, −104, −36, −19, 75, 77, 123}
  > {−120, −110, −23, −13, 38, 105, 123}
  > {−134, −75, −66, 8, 47, 87, 133} ."

  Each set is A with B = −A. All five were verified to satisfy exponents 1..6.

### Prouhet (item 4)
- p. 4 [page image]: "A general solution of the problem for all degrees, but large sizes, came a century later in 1851 when Prouhet found that there are n^{k+1} numbers separable into n sets so that each pair of sets forms a solution of degree k and size n^k. … Prouhet's result, while the first general solution of the problem, was not properly noticed until 1959 when Wright [23] took exception to the problem being called the Tarry-Escott problem and drew attention to Prouhet's contribution in a paper called *Prouhet's 1851 Solution of the Tarry-Escott Problem of 1910*."
- p. 4 [page image]: "The problem is called the problem of Prouhet and Tarry by Hua in his text [11] … Solutions are often called 'multigrades' as in Smyth [19]."

### References (p. 27 [text, OCR], verbatim)
- "[9] Fuchs, W.H.J, and E.M. Wright. The 'Easier' Waring Problem. Quart. J. Math. 10 (1939), 190-209."
- "[10] Gloden, A. Mehrgradige Gleichungen. Noordhoff, Groningen, 1944."
- "[11] Hua, L.K. Introduction to Number Theory. Springer-Verlag, Berlin, Heidelberg, New York, 1982."
- "[15] Melzak, Z.A. A Note on the Tarry-Escott Problem. Canad. Math. Bull. vol. 4, no. 3 (1961), 233-237."
- "[19] Smyth, C.J. Ideal 9th-order Multigrades and Letac's Elliptic Curve. Math. Comp. 57 (1991), 817-823."
- "[22] On Tarry's Problem (I). Quart. J. Math., Oxford Ser. 6 (1935), 261-267." (Wright)
- "[23] Prouhet's 1851 Solution of the Tarry-Escott Problem of 1910. M.A.A. Monthly 66 (1959), 199-201." (Wright)
- "[24] The Tarry-Escott and the "Easier" Waring Problem. J. Reine Angew. Math. 311/312 (1972), 170-173." (Wright)

---

## 2. Melzak 1961

- **Citation:** Z. A. Melzak, "A Note on the Tarry-Escott Problem", Canad. Math. Bull. 4(3) (Sept 1961), 233–237. DOI 10.4153/CMB-1961-025-1.
- **File:** `Melzak1961_CMB4.pdf` / `.txt`, from cambridge.org (free PDF). **Status:** retrieved.
- **Notation warning:** in Melzak, n is the degree and K(n) is the least size. So K(n) = N(n) in Borwein–Ingalls notation.
- p. 233 [text]: "what is the smallest integer K = K(n) in the set of all k's for which the system (1) possesses a non-trivial solution in integers?" … "Therefore (2) K(n) > n + 1." (The extraction prints ">"; in context this is "≥".) "It has been conjectured in [1] that in fact K(n) = n + 1".
- pp. 233–234 [text]: "A simple combinatorial proof has been given in [1] of the estimate (3) K(n) < [n(n + 1)/2] + 1; the above bound has been slightly improved in [2] to K(n)< (n2 + 4)/2, and this would appear to be the best bound known so far."
  - [1] = Hardy & Wright, An introduction to the theory of numbers, 2nd ed. 1945.
  - [2] = "E. M. Wright, Quart. J. Math., Oxford Ser. 6 (1935), 261 - 267."
  - The extraction drops the "≤"/superscripts. Read as K(n) ≤ [n(n+1)/2]+1 and K(n) ≤ (n²+4)/2.
- p. 234, Theorem 1 [text, formula as printed]: "K(n) = ½ min_{P ∈ 𝔄} S[P(x)(1 − x)^{n+1}]".
  - 𝔄 is "the class of all polynomials whose coefficients are integers, not all 0".
  - S[P] = Σ|a_i|.
  - p. 234: "Our expression is of non-constructive nature, that is, it does not allow one to compute K(n), but it leads to estimates for K(n) which are better that (3) for certain values of n."
- p. 237, Table 1 (from the page image of the fetched PDF). Upper bounds b_n on K(n) = N(n), with multiplier Q, compared against [n(n+1)]/2+1:

| n | b_n | Q | [n(n+1)]/2+1 |
|---|---|---|---|
| 2 | 3 | 1 | 4 |
| 3 | 4 | 1 | 7 |
| 4 | 6 | 1 | 11 |
| 5 | 8 | 1 | 16 |
| 6 | 10 | 1 | 22 |
| 7 | 14 | 1 | 29 |
| 8 | 18 | 1 | 37 |
| 9 | 22 | 1 | 46 |
| 10 | 22 | 1−x | 56 |
| 11 | 34 | 1−x | 67 |
| 12 | 32 | 1−x | 79 |
| 13 | 41 | 1−x | 92 |
| 14 | 46 | 1−x | 106 |
| 15 | 58 | 1−x | 121 |
| 16 | 58 | 1−x | 137 |
| 17 | 75 | 1−x | 154 |
| 18 | 74 | 1−x | 172 |
| 19 | 92 | (1−x)(1−x²) | 191 |
| 20 | 100 | 1−x | 211 |
| 21 | 124 | (1−x)(1−x²) | 232 |
| 22 | 118 | (1−x)(1−x²) | 254 |
| 23 | 146 | (1−x)(1−x²) | 277 |
| 24 | 159 | (1−x)(1−x²) | 301 |
| 25 | 170 | (1−x)(1−x²) | 326 |
| 26 | 196 | (1−x)(1−x²) | 352 |
| 27 | 216 | (1−x)(1−x²) | 379 |
| 28 | 207 | (1−x)(1−x²) | 407 |
| 29 | 266 | (1−x)(1−x²) | 436 |

These are numerical bounds for individual n ≤ 29 only. No asymptotic improvement is claimed.

---

## 3. Wooley 2019 / 2012: the exact-degree quantity W(k,h)

### Wooley 2019
- **Citation:** T. D. Wooley, "Nested efficient congruencing and relatives of Vinogradov's mean value theorem", Proc. London Math. Soc. (3) 118(4) (2019) 942–1016. arXiv:1708.01220v2.
- **File:** `Wooley2019_NestedEC_arXiv1708.01220.pdf` / `.txt`. **Status:** retrieved.
- §13 "A remark on Tarry's problem" (arXiv pp. 52–53) [text]:
  - "Let W(k, h) denote the least natural number s having the property that the simultaneous equations (13.1) possess an integral solution x with Σ x_{iu}^{k+1} ≠ Σ x_{iv}^{k+1} (1 ⩽ u < v ⩽ h)."
  - (13.1) is "Σ_{i=1}^s x_{i1}^j = Σ x_{i2}^j = . . . = Σ x_{ih}^j (1 ⩽ j ⩽ k)".
  - "Classically, Hua [21] was able to show that W(k, h) ⩽ k2(log k + O(1)). In recent work [58, Theorem 12.1] based on efficient congruencing, the author was able to improve this conclusion, showing that W(k, h) ⩽ 1/2 k(k + 1) + 1 for k sufficiently large. We now show that the latter hypothesis on k may be dropped."
  - "Theorem 13.1. When h and k are natural numbers with h ⩾ 2, one has W(k, h) ⩽ 1/2 k(k + 1) + 1."
  - "The bound obtained in Theorem 13.1 apparently achieves the limits of this kind of analytic argument. The best available lower bound for W(k, h) is the trivial bound W(k, h) ⩾ k + 1, one that for large values of k seems unlikely to represent the true state of affairs. For small values of k, however, explicit numerical examples show that W(k, 2) = k + 1 for 2 ⩽ k ⩽ 9 and k = 11 (see http://euler.free.fr/eslp/eslp.htm)."
  - Refs, verbatim:
    - "[20] L.-K. Hua, On Tarry's problem, Quart. J. Math. Oxford 9 (1938), 315–320."
    - "[21] L.-K. Hua, Improvement of a result of Wright, J. London Math. Soc. 24 (1949), 157– 159."
    - "[58] T. D. Wooley, Approximating the main conjecture in Vinogradov's mean value theorem, Mathematika 63 (2017), no. 1, 292–350."
    - "[60] E. M. Wright, The Prouhet-Lehmer problem, J. London Math. Soc. 23 (1948), 279–285."

### Wooley 2012
- **Citation:** T. D. Wooley, "Vinogradov's mean value theorem via efficient congruencing", Ann. of Math. (2) 175(3) (2012) 1575–1627. arXiv:1101.0574v1.
- **File:** `Wooley2012_Annals_EC_arXiv1101.0574.pdf` / `.txt`. **Status:** retrieved.
- p. 3 [text]: "L.-K. Hua was able to show that W(k, h) ⩽ k2(log k + O(1)) for h ⩾ 2, a conclusion improved by the present author when h = 2 with the bound W(k, 2) ⩽ 1/2 k2(log k+log log k+O(1)) (see [42, Theorem 1]). We improve both estimates in §9."
  - [42] = Wooley, Some remarks on Vinogradov's mean value theorem and Tarry's problem, Monatsh. Math. 122 (1996) 265–273; reference as listed in Croot–Mao–Yip [19].
- p. 3 [text]: "Theorem 1.3. When h and k are natural numbers with h ⩾ 2 and k ⩾ 2, one has W(k, h) ⩽ k2 + k −2."

**Relation to Borwein–Ingalls:** W(k,2) is exactly Borwein–Ingalls' M(k), "degree exactly k and no higher". Note also that N(k) ≤ M(k) trivially, since an exact-degree solution is a solution.

---

## 4. Croot, Mao, Yip 2026

- **Citation:** E. Croot, J. Mao, C. H. Yip, "The Prouhet–Tarry–Escott problem for subsets with small doubling in integral domains", arXiv:2609.05061v1 (4 Sep 2026).
- **File:** `CrootMaoYip2026_arXiv2609.05061.pdf` / `.txt`. **Status:** retrieved.
- p. 1 [text]: "Let P(k, m) denote the least s for which equation (2) has an integer solution x in which the sets {x1h, . . . , xsh}(1 ≤ h ≤ m) are distinct. Similarly, let W(k, m) denote the least s such that equation (2) has an integer solution x with Σ x_{ih}^{k+1} ≠ Σ x_{it}^{k+1} (h ≠ t)."
- p. 1 [text]: "It is easy to see P(k, 2) ≥ k + 1 and it is an open problem to determine if P(k, 2) = k + 1. It is only known that P(k, 2) = k + 1 when 2 ≤ k ≤ 9 and k = 11 [2]. Using a pigeonhole principle argument one can easily see that P(k, m) ≤ k(k+1)/2 + 1. However, the pigeonhole principle does not readily yield an upper bound on W(k, 2). Nonetheless, Hua [10, 11] and Wright [25] were able to provide upper bounds on W(k, m) using elementary arguments."
- p. 2 [text]: "The best-known upper bound is W(k, m) ≤ k(k+1)/2 + 1, due to Wooley [22, Theorem 13.1]."
- P(k,2) = N(k).
- This is the most recent fetched statement (Sept 2026). It names no bound on P(k,2) = N(k) better than the pigeonhole k(k+1)/2+1.
- [2] there is "P. Borwein. "The Prouhet–Tarry–Escott problem", ch. 11. In Computational Excursions in Analysis and Number Theory, CMS Books in Mathematics, pages 85–96. Springer-Verlag, 2009." (sic; the original edition is 2002).

---

## 5. Coppersmith, Mossinghoff, Scheinerman, VanderKam 2023 (CMSV)

- **Citation:** D. Coppersmith, M. J. Mossinghoff, D. Scheinerman, J. M. VanderKam, "Ideal solutions in the Prouhet–Tarry–Escott problem", arXiv:2304.11254v1 (2023). Published as Math. Comp. 93(349) (2024) 2473–2501, per Croot–Mao–Yip ref [7].
- **File:** `CMSV2023_arXiv2304.11254.pdf` / `.txt`. **Status:** retrieved.
- p. 2 [text]:
  - "Much study of the PTE problem concentrates on the special class of symmetric solutions. When n is even, a symmetric solution has the property that A = −A and B = −B, so that all of the odd moments of A and B are 0 and thus automatically match. When n is odd, a symmetric solution has B = −A, so that all of the even moments of these two sets automatically match."
  - "Ideal solutions in the PTE problem over Z are known for n ≤ 10 and n = 12. Infinite families of such solutions are known in each of these cases except n = 9, where just two solutions are known up to affine equivalence, both found by Letac in 1942 [18] (see also [15, pages 47–48]):
    A = {−98, −82, −58, −34, 13, 16, 69, 75, 99}, B = −A;
    A = {−174, −148, −132, −50, −8, 63, 119, 161, 169}, B = −A. (3)"
- p. 2 [text]:
  - "In 2002, Borwein, Lisonek, and Percival [4] developed an algorithm that found two symmetric ideal solutions at n = 10 … A = ±{99, 100, 188, 301, 313}, B = ±{71, 131, 180, 307, 308}; A = ±{103, 189, 366, 452, 515}, B = ±{18, 245, 331, 471, 508}. (4)"
  - "They also proved that no symmetric ideal solutions with size n = 11 exist with height at most 2000 … and no additional symmetric ideal solutions with size n = 9 exist up to this same height".
- pp. 2–3 [text]:
  - "The first ideal solution with size n = 12 was discovered in 1999 by Kuosa, Meyrignac, and Shuwen … A = ±{22, 61, 86, 127, 140, 151}, B = ±{35, 47, 94, 121, 146, 148}. (5)"
  - "A second symmetric solution was discovered by Broadhurst in 2007 [6]: A = ±{257, 891, 1109, 1618, 1896, 2058}, B = ±{472, 639, 1294, 1514, 1947, 2037}. (6)"
  - "In 2008, Choudhry and Wróblewski [11] employed an elliptic curve to construct an infinite family of symmetric ideal PTE solutions at n = 12 … the smallest of which is A = ±{107, 622, 700, 1075, 1138, 1511}, B = ±{293, 413, 886, 953, 1180, 1510}; (7)"
- p. 3 [text]: "For sizes n = 9 through n = 12, our searches cover a significantly larger space compared to the work of [4]. For example, at n = 9 we complete a search for solutions with height at most 7000, compared to 2000 in [4]. … No new integral solutions are found for 9 ≤ n ≤ 16, beyond ones equivalent to known configurations."
- pp. 4–5 [text], Prop. 2.1 (Rees and Smyth): "(i) If k is a positive integer and p < n/k then p^{k+1} | Cn. (ii) If p ≥ 5 then p | Cp. (iii) If n + 2 ≤ p < n + 2 + (n−3)/6 then p | Cn. (iv) 16 | C5, 32 | C6, 11 | C7, 11 · 13 | C8, 13 | C9, and 17 | C11." (formula as printed)
- Relevant references, verbatim:
  - "[9] J. Chernick. Ideal solutions of the Tarry–Escott problem, Amer. Math. Monthly, 44(10):626–633, 1937."
  - "[10] A. Choudhry. A new approach to the Tarry–Escott problem, Int. J. Number Theory, 13(2):393–417, 2017."
  - "[11] A. Choudhry and J. Wróblewski. Ideal solutions of the Tarry–Escott problem of degree eleven with applications to sums of thirteenth powers, Hardy–Ramanujan J., 31:1–13, 2008."
  - "[15] A. Gloden. Mehrgradige Gleichungen, P. Noordhoff, Groningen, 2nd ed., 1944."
  - "[16] L. K. Hua. Introduction to Number Theory, Springer, Berlin, 1982."
  - "[18] A. Letac. Gazeta Matematica, 48:68–69, October 1942."
  - "[21] C. J. Smyth. Ideal 9th-order multigrades and Letac's elliptic curve, Math. Comp., 57(196):817–823, 1991."
  - "[22] E. M. Wright. Prouhet's 1851 solution of the Tarry–Escott problem of 1910, Amer. Math. Monthly, 66:199–201, 1959."

---

## 6. Borwein, Lisoněk, Percival 2003 (BLP)

- **Citation:** P. Borwein, P. Lisoněk, C. Percival, "Computational investigations of the Prouhet-Tarry-Escott problem", Math. Comp. 72(244) (2003) 2063–2070. DOI 10.1090/S0025-5718-02-01504-1.
- **File:** `BLP2003_MathComp72_authorcopy.pdf` / `.txt`, from https://www.daemonology.net/papers/pte.pdf. **Status:** retrieved.
  - This is the published Math. Comp. layout ("c ⃝2002 by the authors").
  - The ams.org copy returned HTTP 429.
- p. 2063 [text]: "If k = n −1, then the solution is called ideal and n is called the size of this ideal solution." … "Ideal solutions to the PTE Problem are known only for sizes n = 1, 2, . . . , 10 and n = 12. Parametric ideal solutions are known for n = 1, 2, . . . , 8 and n = 10; in each case they give rise to infinitely many nonequivalent ideal solutions."
- p. 2064 [text]:
  - "For n odd, the symmetric version takes the form (2) Σ_{i=1}^n x_i^e = 0 for e = 1, 3, . . ., n −2. If x1, . . . , xn satisfy (2), then {x1, . . . , xn} =_{n−1} {−x1, . . . , −xn} is an odd ideal symmetric solution of the PTE Problem."
  - "For n even … Σ_{i=1}^{n/2} x_i^e = Σ y_i^e for e = 2, 4, . . ., n −2."
- p. 2064 [text], Gloden's size-7 family: "The values α1, . . . , α7 satisfy Σ_{i=1}^7 α_i^e = 0 for e = 1, 3, 5."
  - α1 = −(f² − kf + k²)(−3kf² + k³ + f³)
  - α2 = −(k − f)(f + k)(f² − 3kf + k²)f
  - α3 = (−f + 2k)(−f² − kf + k²)kf
  - α4 = (k − f)(k − 2f)(−f² + kf + k²)k
  - α5 = (k − f)(f⁴ − 2kf³ − k²f² + k⁴)
  - α6 = −(k⁴ − 2fk³ − k²f² + 4kf³ − f⁴)k
  - α7 = −(k⁴ − 5k²f² + 4kf³ − f⁴)f

  (formula as printed) "For example, plugging in f = 3, k = 1 yields the following ideal symmetric solution of size 7: {−7, 24, 33, −50, −38, −13, 51} =6 {7, −24, −33, 50, 38, 13, −51}." (verified)
- p. 2069 [text], Table 2:
  - size 9: search limit 2000, "no new solutions found"
  - size 10: search limit 1500, "two new solutions found"
  - size 11: search limit 2000, "no solutions found"
  - size 12: search limit 1000, "no new solutions found"
- p. 2069 [text]:
  - "For size 9 … The only primitive solutions found were {−169, −161, −119, −63, 8, 50, 132, 148, 174} and {−98, −82, −58, −34, 13, 16, 69, 75, 99}."
  - "We found the two solutions {±71, ±131, ±308, ±180, ±307} =9 {±99, ±100, ±301, ±188, ±313} and {±18, ±245, ±331, ±471, ±508} =9 {±103, ±189, ±366, ±452, ±515}."
  - "For size 11, we searched up to 2000 and did not find any solutions. At present no solutions of size 11 are known."
- pp. 2069–2070 [text]: "more than 85% of all nonequivalent ideal symmetric solutions {x1, . . . , x7} of size 7 that we computed … are subject to a relation of the form x1 + x2 + x3 = x4 + x5 + x6 + x7 = 0. A similar observation holds for the two known ideal symmetric solutions of size 9".

---

## 7. Chen Shuwen 2025 survey (tables; odd-exponent and negative-exponent variants)

- **Citation:** Chen Shuwen, "A survey of The Prouhet-Tarry-Escott Problem and Its Generalizations", arXiv:2506.11429v1 (13 Jun 2025), 368 pp.
- **File:** `ChenShuwen2025_survey_arXiv2506.11429.pdf` / `.txt`. **Status:** retrieved.
- **Notation warning:** Chen indexes by **degree n**, with size m = n+1.

### Definitions and status (pp. 11–13)
- p. 11 [text]: "If m = n + 1, a solution of the system (1.1) is called an ideal solution of the PTE problem."
- p. 12 [text]: "To date, ideal solutions of the PTE problem have been discovered for degrees n ≤ 9 and n = 11." That is, sizes ≤ 10 and 12.
- p. 12 [text], Definition 2: an ideal solution is symmetric if "a1 + an+1 = a2 + an = · · · = b1 + bn+1 = b2 + bn = . . . , if n is odd, a1 + bn+1 = a2 + bn = · · · = an+1 + b1, if n is even." Here n is the degree.
- p. 12 [text]: "As of the present, ideal symmetric solutions have been found for the PTE problem of degrees n ≤ 9 and n = 11."
- p. 13 [text]: "To date, ideal non-symmetric solutions have only been discovered for PTE of degrees n ≤ 7."
- p. 188 [text], open problem: "P1. Ideal Solution of PTE: How to find ideal solutions of the PTE problem of degrees n = 10 and n ≥ 12?"

### Odd-size (even-degree) symmetric ideal solutions in shifted form
Symmetric means a_i + b_{n+2-i} is constant.
- degree 2 (A.1.5, p. 197): "[0, 3, 3]k = [1, 1, 4]k" "[0, 4, 5]k = [1, 2, 6]k" "[0, 7, 7]k = [1, 4, 9]k"
- degree 4 (A.1.21, p. 214): "J.Chernick gave a two-parameter solution of this system in 1937 [35]. All solutions by his method are symmetric: [0, 4, 8, 16, 17]k = [1, 2, 10, 14, 18]k [0, 6, 8, 17, 19]k = [1, 3, 12, 14, 20]k" … "Ajai Choudhry obtained the complete ideal symmetric solution and a parametric ideal non-symmetric solution in 2000 [42]."
- degree 6 (A.1.35, p. 226): "The first known symmetric solution was discovered by E.B.Escott in 1910 … [0, 18, 27, 58, 64, 89, 101]k = [1, 13, 38, 44, 75, 84, 102]k" … "J.Chernick gave a two-parameter symmetric solution in 1937 [35]. Numerical example: [0, 59, 68, 142, 181, 221, 267]k = [1, 47, 87, 126, 200, 209, 268]k"
- degree 8 (A.1.40, p. 230): "So far only two ideal symmetric solutions, based on (A.269) and (A.270), were found by A.Latec in 1942 [103] [71, p.48] [63]: [0, 24, 30, 83, 86, 133, 157, 181, 197]k = [1, 17, 41, 65, 112, 115, 168, 174, 198]k [0, 26, 42, 124, 166, 237, 293, 335, 343]k = [5, 13, 55, 111, 182, 224, 306, 322, 348]k". These are equivalent to the Borwein–Ingalls / CMSV size-9 sets.
- degree 10 (size 11): **no entry**. The appendix jumps from A.1.41 (k = 1..9) to A.1.42 (k = 1..11).
- degree 11 (A.1.42, p. 232):
  - "[0, 11, 24, 65, 90, 129, 173, 212, 237, 278, 291, 302]k = [3, 5, 30, 57, 104, 116, 186, 198, 245, 272, 297, 299]k" (Kuosa–Meyrignac–Chen 1999)
  - "[0, 162, 440, 949, 1167, 1801, 2315, 2949, 3167, 3676, 3954, 4116]k = [21, 111, 544, 764, 1419, 1586, 2530, 2697, 3352, 3572, 4005, 4095]k" (Broadhurst 2007)
  - "In 2008, A.Choudhry and Jarosław Wróblewski proved that this system has infinitely many solutions".

### Equal sums of odd powers only (item 3)
- A.1.6 (k = 1, 3), p. 198: "A.Moessner gave parameter solutions of this type in 1939 [105]. … [0, 7, 8]k = [1, 5, 9]k". Smallest: "[1, 5, 5]k = [2, 3, 6]k".
- A.1.17 (k = 1, 3, 5), p. 211: "Parameter solutions were obtained by A.Gloden in 1949, G.Xeroudakes and A.Moessner in 1958 [145], Lander in 1968 [98], and Ajai Choudhry in 1991[36] [37] . Numerical examples are: [1, 13, 17, 23]k = [3, 9, 21, 21]k … [0, 24, 33, 51]k = [7, 13, 38, 50]k". Smallest new: "[6, 16, 18, 24]k = [7, 13, 21, 23]k".
- A.1.26 (k = 1, 3, 5, 7), p. 218:
  - "First known solutions, by A.Gloden in 1940's [71] [72] [76]: [3, 19, 37, 51, 53]k = [9, 11, 43, 45, 55]k"
  - "Only two solutions with zero term are known so far, which lead to the ideal solution of (k = 1, 2, 3, 4, 5, 6, 7, 8), found by A.Letac in 1942 [103] [71]: [0, 34, 58, 82, 98]k = [13, 16, 69, 75, 99]k [0, 63, 119, 161, 169]k = [8, 50, 132, 148, 174]k"
  - "A.Moessner gave a two-parameter solution … T.N.Sinha gave a two-parameter solution in 1966".
- A.1.33 (k = 1, 3, 5, 7, 9), p. 224:
  - "First known solution, based on computer search with Identity (2.236), by Chen Shuwen in 2000 [24, 30]: [7, 91, 173, 269, 289, 323]k = [29, 59, 193, 247, 311, 313]k"
  - "Second known solutions, by Jarosław Wróblewski in 2009 … [23, 163, 181, 341, 347, 407]k = [37, 119, 221, 311, 371, 403]k [43, 161, 217, 335, 391, 463]k = [85, 91, 283, 287, 403, 461]k [57, 399, 679, 995, 1167, 1293]k = [115, 299, 767, 925, 1205, 1279]k"
  - "Only the above four ideal non-negative solutions are known so far. In addition, Jarosław Wróblewski found one integer solution in 2009 [91, p.24]: [−13, 365, 689, 1111, 1115, 1325] = [23, 305, 731, 1037, 1177, 1319]."
- Odd-exponent to PTE lifting: `eslpower_TarryPrb.txt`, Theorem 3 (see §8).

### Exponent sets with negative exponents / reciprocals (item 3)
- p. 13 [text]: "Since 1995, the author has systematically studied the generalized case where the exponents are arbitrary integer sequences [30], including negative integers [32]. In particular, the case where k = 0 is defined as the equal products case [31]."
- p. 13 [text], Definition 4: "[a1, a2, . . . , am]k := a1^k + · · · + am^k if k ≠ 0, a1a2 · · · am if k = 0."
- p. 15 [text], reciprocal transform: "Let C be the least common multiple (LCM) of all {ai, bi}. Then [C/a1, C/a2, . . . , C/am]k = [C/b1, . . . , C/bm]k, (k = −k1, −k2, . . . , −kn). (1.10)"
- p. 275 [text]: "A.5 GPTE with k1<0 and kn>0. To date, 33 distinct types of ideal non-negative integer solutions of GPTE have been identified with k1 < 0 and kn > 0."
- Selected entries (pp. 276–290), verbatim, all verified:
  - (k = −1, 1): "[4, 10, 12]k = [5, 6, 15]k" "[6, 14, 14]k = [7, 9, 18]k"; "Ajai Choudhry gave a three-parameter solutions in 2011 [48]."
  - (k = −1, 1, 3): "[3, 10, 15, 30]k = [4, 5, 21, 28]k" (A.685); also (A.686)–(A.692).
  - (k = −1, 1, 5): "[81, 374, 585, 891]k = [85, 286, 702, 858]k" (A.693), "First known solution, smallest solution, by Chen Shuwen in 2017".
  - (k = −1, 1, 2): "[15, 28, 48, 70]k = [16, 24, 55, 66]k".
  - (k = −1, 1, 2, 3): "[266, 494, 494, 1463, 1547]k = [287, 374, 611, 1394, 1598]k" (p. 16, (A.728)).
  - (k = −1, 0, 1, 2, 3): "[11, 18, 35, 84, 90, 132]k = [12, 15, 44, 63, 110, 126]k" (A.740).
  - (k = −1, 0, 1, 2, 3, 4): "[9, 17, 21, 51, 99, 143, 143]k = [11, 11, 33, 39, 117, 119, 153]k" (A.773).
  - (k = −3, −2, −1, 0, 1, 2, 3): "[21, 24, 28, 42, 44, 66, 77, 88]k = [22, 22, 33, 33, 56, 56, 84, 84]k" (A.777).
  - (k = −2, 2): "All solutions listed above satisfy a1b1 = a2b2 = a3b3."
- There is **no** listed type combining −1 with 1, 3, 5, ... beyond (−1, 1, 3) and (−1, 1, 5). For example, (−1, 1, 3, 5) does not appear in the table of contents. Absence from the list is all that is recorded here.
- Ref, verbatim: "[48] Ajai Choudhry. Equal sums of like powers, both positive and negative. Rocky Mountain J. Math., 41(3):737–763, 2011."
- Odd-exponent Girard–Newton generalisation, p. 58 [text]: "in the Identity 5 presented below, we only address cases where all exponential powers are positive odd integers. We will provide examples later for cases where exponential powers include both positive and negative odd integers."

---

## 8. Chen Shuwen web pages (eslpower.org)

- **Files:**
  - `eslpower_TarryPrb.htm/.txt` from http://eslpower.org/TarryPrb.htm
  - `eslpower_kminus.htm/.txt` from http://eslpower.org/kminus.htm
  - `eslpower_eslp.htm/.txt` from http://eslpower.org/eslp.htm
- **Status:** retrieved (HTTP 200).

### TarryPrb.htm (text, whitespace normalised)
- "Theorem 2 [1] [2] If [ a1 , ... , am ] = [ b1 , ... , bm ] ( k = 1, 2, ... , n ) then [ a1 , ... , am , b1 + T , ... , bm + T ] = [ b1 , ... , bm , a1 + T , ... , am + T ] ( k = 1, 2, ... , n + 1 ) where T is arbitrary integer."
- "Theorem 3 [5] If [ a1 , ... , am ] = [ b1 , ... , bm ] ( k = 1, 3, ... , 2n - 1 ) then [ T + a1 , ... , T + am , T - b1 , ... , T - bm ] = [ T + b1 , ... , T + bm , T - a1 , ... , T - am ] ( k = 1, 2, ... , 2n ) where T is arbitrary integer."
- "Theorem 4 [5] If [ a1 , ... , am ] = [ b1 , ... , bm ] ( k = 2, 4, ... , 2n ) then [ T + a1 , ... , T + am , T - a1 , ... , T - am ] = [ T + b1 , ... , T + bm , T - b1 , ... , T - bm ] ( k = 1, 2, ... , 2n + 1 )".
- "Theorem 6 [1] [2] If the system … ( k = 1, 2, ..., n ) have a non-trival solution, then m >= n + 1."
- Ideal symmetric lists, including "( k = 1, 2, 3, 4, 5, 6 ) [ 0, 18, 27, 58, 64, 89, 101 ] = [ 1, 13, 38, 44, 75, 84 , 102 ] First known solution, by E.B.Escott in 1910."
- **Inconsistency on the page:** the "Definitions" paragraph lists [0, 59, 68, 142, 181, 221, 267] = [1, 47, 87, 126, 200, 209, 268] as a "non-symmetric" example. The same page and the survey give it as Chernick's symmetric solution, and a_i + b_{8−i} = 268 for all i, so it is symmetric.

### kminus.htm
- "Theorem 9 ( By Chen Shuwen, March 2001 ) If [ a1 , ... , am ] = [ b1 , ... , bm ] ( ai <>0 , bi <>0 ) ( k = k1 , ... , kn ) then [ C /a1 , ... , C /am ] = [ C /b1 , ... , C /bm ] ( k = - k1 , ... , - kn ) where C is the least common multiple of all { ai , bi }."
- "In 2001, on Guo Xianqiang's Website on Maths ( in Chinese ), he ask such an interesting question: If k1 < 0 and kn > 0 , is there solution in positive integer? As an answer, Chen Shuwen solved ( k = -1, 1 ) in May of 2001."

---

## 9. Caley 2013 (Gaussian integers)

- **Citation:** T. Caley, "The Prouhet-Tarry-Escott problem for Gaussian integers", Math. Comp. 82(282) (2013) 1121–1137. arXiv:1011.1262v2.
- **File:** `Caley_Gaussian_arXiv1011.1262.pdf` / `.txt`. **Status:** retrieved (arXiv version).
- p. 1 [text]: "For example, {0, 3, 5, 11, 13, 16} =5 {1, 1, 8, 8, 15, 15} is an ideal pte solution of size 6 and degree 5".
- p. 2 [text]: "Note that v(k) is conjectured to be O(k). For arbitrary k, the best known bound is v(k) ≪ k log(k) [3, Chapter 12], which is derived from the usual Waring's problem."
  - This k log k bound concerns the "easier" Waring number v(k), **not** N(k). It may be one source of the k log k confusion.

## 10. Choudhry 2022

- **Citation:** A. Choudhry, "Ideal solutions of the Tarry-Escott Problem of degree seven", arXiv:2207.12726v1 (2022).
- **File:** `Choudhry2022_deg7_arXiv2207.12726.pdf` / `.txt`. **Status:** retrieved.
- p. 1 [text]: "When s = k+1, solutions of the diophantine system (1.1) are known as ideal solutions. Parametric ideal solutions of the TEP are known only when k ≤ 7."
  - This counts polynomial parametrisations.
  - CMSV count infinite families, including the elliptic-curve families at n = 10 and 12; see §5.
  - BLP say "Parametric ideal solutions are known for n = 1, 2, . . . , 8 and n = 10".
  - The three sources therefore use different senses of "parametric".

## 11. Tsai, Lee, Takahashi 2026 (minor)

- **Citation:** Y.-D. Tsai, J. Lee, F. Takahashi, "Arithmetic Symmetry in Ideal Prouhet–Tarry–Escott Solutions", arXiv:2606.07735v1 (2026).
- **File:** `ArithSymmetry_arXiv2606.07735.pdf` / `.txt`. **Status:** retrieved.
- Abstract [text]: "we study the symmetric locus in the ideal degree-three Prouhet–Tarry–Escott problem. … Nsym(H) = 4 log 2/(3π²) H³ log H + O(H³)." (formula as printed)
- Not used for items 1–4 beyond context.

---

## Instrument gaps (not fetched; nothing above is filled in from memory)

| Source | URLs tried | Result |
|---|---|---|
| E. M. Wright, "On Tarry's problem (I)", Quart. J. Math. Oxford 6 (1935) 261–267, DOI 10.1093/qmath/os-6.1.261 | https://doi.org/10.1093/qmath/os-6.1.261 → academic.oup.com | HTTP 403. Content known only through Borwein–Ingalls p. 7 and Melzak p. 234 |
| L.-K. Hua, "On Tarry's problem", Quart. J. Math. Oxford 9 (1938) 315–320, DOI 10.1093/qmath/os-9.1.315 | https://doi.org/10.1093/qmath/os-9.1.315 → academic.oup.com | HTTP 403 |
| L.-K. Hua, Introduction to Number Theory (Springer 1982), ch. 18 "Waring's Problem and the Problem of Prouhet and Tarry", pp. 494–513, DOI 10.1007/978-3-642-68130-1_18 | Crossref lookup only; Springer paywall, not attempted further | Not fetched. Hua's bound known only as restated by Borwein–Ingalls p. 7 and Wooley |
| L.-K. Hua, "Improvement of a result of Wright", J. London Math. Soc. 24 (1949) 157–159 | none (no OA copy found) | Not fetched |
| T. D. Wooley, "Some remarks on Vinogradov's mean value theorem and Tarry's problem", Monatsh. Math. 122 (1996) 265–273 | none (no OA copy found) | Not fetched. Its bound is known only as quoted by Wooley 2012 |
| P. Borwein, Computational Excursions in Analysis and Number Theory (2002), ch. 11, DOI 10.1007/978-0-387-21652-2_11 | https://doi.org/10.1007/978-0-387-21652-2_11 (HTTP 200 landing page, no preview text); http://link.springer.com/content/pdf/10.1007/978-0-387-21652-2_11.pdf not attempted (paywall) | No text retrieved |
| J. Chernick, "Ideal solutions of the Tarry-Escott problem", Amer. Math. Monthly 44 (1937) 626–633, DOI 10.1080/00029890.1937.11988045 | https://doi.org/10.1080/00029890.1937.11988045 → tandfonline | HTTP 403 |
| E. M. Wright, "Prouhet's 1851 solution of the Tarry-Escott problem of 1910", Amer. Math. Monthly 66 (1959) 199–201, DOI 10.1080/00029890.1959.11989269 | Semantic Scholar: openAccessPdf CLOSED | Not fetched. Prouhet's statement is recorded via Borwein–Ingalls p. 4 only |
| C. J. Smyth, "Ideal 9th-order multigrades and Letac's elliptic curve", Math. Comp. 57 (1991) 817–823 | https://www.ams.org/mcom/1991-57-196/S0025-5718-1991-1094960-9/S0025-5718-1991-1094960-9.pdf | HTTP 429 (rate limited). Content known via Borwein–Ingalls Prop. 4 and the Chen survey |
| Caley 2013 Math. Comp. published version | https://www.ams.org/mcom/2013-82-282/S0025-5718-2012-02532-4/S0025-5718-2012-02532-4.pdf | HTTP 429. The arXiv version was used instead |
| T. Caley, PhD thesis "The Prouhet-Tarry-Escott problem", Univ. of Waterloo 2012 | https://uwspace.uwaterloo.ca/server/api/discover/search/objects?query=Prouhet&dsoType=ITEM | HTTP 200 but a bot-check page ("Making sure you're not a bot!"); not bypassed |
| A. Choudhry, "Equal sums of like powers, both positive and negative", Rocky Mountain J. Math. 41(3) (2011) 737–763, DOI 10.1216/RMJ-2011-41-3-737 | Landing page https://projecteuclid.org/.../10.1216/RMJ-2011-41-3-737.full (200, no abstract text extracted); PDF https://projecteuclid.org/journals/rocky-mountain-journal-of-mathematics/volume-41/issue-3/Equal-sums-of-like-powers-both-positive-and-negative/10.1216/RMJ-2011-41-3-737.pdf | Returned HTML (6 KB), not a PDF; OpenAlex abstract index unusable. Not fetched |
| A. Gloden, Mehrgradige Gleichungen (2nd ed. 1944) | not found on archive.org-type sources in this pass | Not fetched |
| Borwein–Ingalls e-periodica PDF | https://www.e-periodica.ch/cntmng?pid=ens-001:1994:40::10 | Bot-verification page. Content was obtained instead from the official IIIF page images and the OCR full-text endpoint (see §1) |
| Chen Shuwen old site euler.free.fr/eslp | not attempted; current site eslpower.org was fetched instead | — |
