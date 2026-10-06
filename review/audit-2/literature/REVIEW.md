# G5-bis blind review, group `literature` (bundle LIT.0: claims B1-B12, M1-M2, W1-W2, C1-C3, D1-D4, P1-P2, S1-S6, O1-O4)

Each claim reads "source X says S at place Z". I located every passage in a text I fetched and checked by hash. I quote
it verbatim and grade it. Sources: `fetches.md`. Exact checks: `check_solutions.py` -> `check_solutions.txt` (all OK,
exit 0) and `check_lifting_and_bounds.py` -> `check_lifting_and_bounds.txt` (all OK, exit 0).

The Borwein-Ingalls (BI) PDF is a scan with no text layer, so **every BI quote below was read from the page images**
(110 dpi renders of the hash-verified copy). Page numbers are journal pages. For the arXiv texts I give the PDF page,
which equals the printed page number in the Chen survey.

Two kinds of grade appear:
- **Attribution**: CONFIRMED / CONFIRMED WITH CORRECTION / NOT FOUND / CONTRADICTED / SOURCE UNREACHABLE.
- **Severity for the manuscript** (scale of the brief): FATAL / SERIOUS / MINOR / NONE.

## Summary table

| id | attribution grade | severity | verbatim quote (abridged only by "...") | place | correction |
|---|---|---|---|---|---|
| B1 | CONFIRMED | NONE | "we define N(k) to be the least integer n such that there is a solution of size n and degree k." | BI p.6, l.1-3 | BI's solutions are "two distinct sets"; its own pigeonhole proof produces tuples with repeats, so multisets are meant, as in the paper |
| B2 | CONFIRMED WITH CORRECTION | MINOR | "PROPOSITION 1. The following are equivalent: (1) Σα_i^j = Σβ_i^j for j = 1,...,k (2) deg(Π(x−α_i) − Π(x−β_i)) ≤ n − (k+1) (3) (x−1)^{k+1} \| Σx^{α_i} − Σx^{β_i}." | BI p.5 | Prop. 1 is the three equivalent forms of the problem, **not** a bound on N(k). Cite "Prop. 1" only for the equivalent forms; cite Props. 2 and 3 for the bounds |
| B3 | CONFIRMED | NONE | "PROPOSITION 2. N(k) ≥ k + 1. Proof. This follows from the second form of the problem since monic polynomials with identical coefficients have identical roots." | BI p.6 | Also Melzak p.233, (2): "K(n) ≥ n + 1" |
| B4 | CONFIRMED | MINOR (citation) | "PROPOSITION 3. N(k) ≤ ½k(k+1) + 1. Proof. Let n > s^k s! and A = {(α_1,...,α_s) : 1 ≤ α_i ≤ n ...}" ... "We may now choose s = ½k(k+1)+1" | BI pp.6-7 | The pigeonhole proof is confirmed, and its inequality is re-checked exactly for k ≤ 5. The bound is older than BI: Melzak p.233 gives "(3) K(n) ≤ [n(n+1)/2] + 1" with "A simple combinatorial proof has been given in [1]" ([1] = Hardy-Wright, 2nd ed. 1945). Add that attribution |
| B5 | CONFIRMED as a quotation; **content not supported by the primary source** | **SERIOUS** (remark wording) | "Slightly stronger upper bounds are discussed in [22] and [15], but they are much more difficult to establish and only improve the estimates to N(k) ≤ ½(k²−3) k odd, ½(k²−4) k even." | BI p.7 ([22] = Wright, Quart. J. Math. 6 (1935); [15] = Melzak, CMB 4 (1961); BI p.27) | BI's printed formula is **false for k = 2 and k = 3** ((4−4)/2 = 0 < N(2) = 3; (9−3)/2 = 3 < N(3) = 4). It **differs from Melzak's own report of Wright's bound**, "K(n) ≤ (n²+4)/2" (Melzak p.234), by a constant 4 (even k) or 7/2 (odd k). That is not an index shift (none exists; checked). Melzak contains no closed-form bound of his own, only a table. See §B5/M1 |
| B6 | CONFIRMED | NONE | "We can also define M(k) to be the least s such that there is a solution of size s and degree exactly k and no higher. Hua in [11] shows M(k) ≤ (k+1)(log ½(k+2)/log(1+1/k) + 1) ~ k² log k." | BI p.7 | log ½(k+2) = log((k+2)/2), as in the claim. Context: M(k) = W(k,2) of Wooley, and Wooley has since proved M(k) ≤ k² + k − 2 (2012) and M(k) ≤ k(k+1)/2 + 1 (2019) (W1, W2) |
| B7 | CONFIRMED (quotation); see O4 for currency | MINOR | "3. Prove N(k) ≤ o(k²). 4. Prove M(k) ≤ O(k²)." ... "The big prize is to find ideal solutions of all degrees, if indeed they exist. ... No progress on questions 3 and 4 has been made for many years." | BI p.26, §6 "Open Problems" | Problem 4 is **no longer open**: Wooley's W(k,2) = M(k) ≤ k² + k − 2 (Annals 2012, Thm 1.3) proves M(k) = O(k²). Do not repeat BI's "no progress on 3 and 4" as current. Problem 3 is still open (O4) |
| B8 | CONFIRMED | NONE | "An odd ideal symmetric solution of size k+1 and even degree k is of the form {α_1,...,α_{k+1}}, {−α_1,...,−α_{k+1}} and satisfies ... Σ_{i=1}^{k+1} α_i^j = 0 for j = 1, 3, 5, .., k − 1" | BI p.8 | With size 2L−1 the degree is k = 2L−2, so the exponents are 1,3,...,2L−3, consistent with Prop. 2.3(a) |
| B9 | CONFIRMED | NONE | "LEMMA 2. If {α_1,...,α_n} =^k {β_1,...,β_n} then {α_1,...,α_n, β_1+M,...,β_n+M} =^{k+1} {α_1+M,...,α_n+M, β_1,...,β_n} for any integer M. Proof. This follows upon multiplying (3) by (x^M − 1)." | BI p.6 | (BI's Lemma 1 on p.5 is the affine-invariance lemma) |
| B10 | CONFIRMED WITH CORRECTION | MINOR | table "4 {3,11},{7,9} ... 6 {4,9,13},{1,11,12} ... 7 {−51,−33,−24,7,13,38,50} 8 {2,16,21,25},{5,14,23,24} 9 {−98,−82,−58,−34,13,16,69,75,99} and {−169,−161,−119,−63,8,50,132,148,174} 10 {436,11857,20449,20667,23750},{12,11881,20231,20885,23738} and {133225698289,...}"; p.25: "all perfect solutions of size 7 with coefficients in the range [−171,171] are" (five sets) | BI p.9 table, p.25 | All 14 printed solutions verified exactly. Each has exactly the stated degree, and the five 7-sets and two 9-sets are complete residue systems. Attribution: BI p.10 says "three of these were found in the 1940's by Letac and Gloden (see [10]). The last solution was found by Smyth". BI does not separate Letac from Gloden. The size-10 solution {436,...} is called Letac's by BLP p.2069, and both 9-sets are called Letac's (1942) by CMSV p.2. Cite those for the "Letac" attributions |
| B11 | CONFIRMED | NONE | "in 1851 when Prouhet found that there are n^{k+1} numbers separable into n sets so that each pair of sets forms a solution of degree k and size n^k." ... "not properly noticed until 1959 when Wright [23] took exception ... Prouhet's 1851 Solution of the Tarry-Escott Problem of 1910." | BI p.4 | |
| B12 | CONFIRMED | NONE | "PROPOSITION 4. If x, y are rational solutions of x²y² − 13x² − 13y² + 121 = 0 then {±(4x+4y), ±(xy+x+y−11), ...} gives rise to an ideal symmetric solution of size 10." "Smyth shows in [19] ..." | BI p.10 | Re-proved symbolically: every non-constant coefficient of the difference of the two products is divisible by the curve polynomial. At the printed points (153/61, 191/79) and (−296313/249661, −1264969/424999) the construction gives, after scaling, exactly the two size-10 entries of p.9 |
| M1 | CONFIRMED; **not the same bound as B5** | (feeds B5) | "what is the smallest integer K = K(n) in the set of all k's for which the system (1) [Σ_{i=1}^k a_i^j = Σ_{i=1}^k b_i^j, j = 1,...n] possesses a non-trivial solution" ... "the above bound has been slightly improved in [2] to K(n) ≤ (n²+4)/2, and this would appear to be the best bound known so far." | Melzak pp.233-234 ([2] = Wright, Quart. J. Math. 6 (1935) 261-267) | In Melzak, **n is the degree and k the size**, so K(n) = N(n) in the paper's notation. Wright's bound as Melzak reports it is N(k) ≤ (k²+4)/2. That is not BI's (k²−3)/2, (k²−4)/2 |
| M2 | CONFIRMED | NONE | "The results are given in the enclosed Table 1 where b_n is the upper bound on K(n) obtained from (13)" ... Table 1, n = 2..29 (b_2 = 3, ..., b_29 = 266) | Melzak pp.236-237 | No asymptotic statement; Melzak says only that his estimates "are better that (3) for certain values of n" (p.234). The b_n stay quadratic (b_29/29² ≈ 0.32). Table 1 was read from the image |
| W1 | CONFIRMED | NONE | "Let W(k,h) denote the least natural number s having the property that the simultaneous equations (1.10) possess an integral solution x with Σx_{iu}^{k+1} ≠ Σx_{iv}^{k+1} (1 ≤ u < v ≤ h)." "Theorem 1.3. When h and k are natural numbers with h ⩾ 2 and k ⩾ 2, one has W(k,h) ⩽ k² + k − 2." | Wooley arXiv:1101.0574v1, p.3 | Hypotheses: h ≥ 2, k ≥ 2. Numbering checked in the arXiv v1 only; Wooley 2019 refers to it as "[47, Theorem 1.3]" |
| W2 | CONFIRMED | NONE | "Theorem 13.1. When h and k are natural numbers with h ⩾ 2, one has W(k,h) ⩽ ½k(k+1) + 1." ... "The bound obtained in Theorem 13.1 apparently achieves the limits of this kind of analytic argument." | Wooley arXiv:1708.01220v2, §13, p.53 | **W(k,2) is the exact-degree M(k)** of BI p.7 (equal sums for j ≤ k, unequal at k+1), not N(k). Since every W-solution is a P-solution, N(k) ≤ M(k) = W(k,2), and Theorem 13.1 gives only N(k) ≤ k(k+1)/2 + 1, the pigeonhole bound. No improvement for N(k) |
| C1 | CONFIRMED | NONE | "Let P(k,m) denote the least s for which equation (2) has an integer solution x in which the sets {x_{1h},...,x_{sh}} (1 ≤ h ≤ m) are distinct." ... "Using a pigeonhole principle argument one can easily see that P(k,m) ≤ k(k+1)/2 + 1." | Croot-Mao-Yip arXiv:2609.05061v1, p.1 | P(k,2) = N(k) |
| C2 | CONFIRMED | NONE | "It is easy to see P(k,2) ≥ k+1 and it is an open problem to determine if P(k,2) = k+1. It is only known that P(k,2) = k+1 when 2 ≤ k ≤ 9 and k = 11 [2]." | CMY p.1 | [2] = P. Borwein, *Computational Excursions*, ch. 11 (2009) |
| C3 | CONFIRMED | NONE | "The best-known upper bound is W(k,m) ≤ k(k+1)/2 + 1, due to Wooley [22, Theorem 13.1]." | CMY p.2 | CMY's own theorems give sizes ⌈log₂ m⌉2^k, which is exponential. No sub-quadratic bound on P(k,2) is stated anywhere in CMY (grep for o(k, log k, P(k: none) |
| D1 | CONFIRMED WITH CORRECTION | NONE | "Ideal solutions in the PTE problem over Z are known for n ≤ 10 and n = 12." | CMSV arXiv:2304.11254v1, p.2 | "Size 11 is open" is implicit, not printed: CMSV p.2 says BLP "proved that no symmetric ideal solutions with size n = 11 exist with height at most 2000", and p.3 says "No new integral solutions are found for 9 ≤ n ≤ 16". BLP p.2069 states it outright: "At present no solutions of size 11 are known" |
| D2 | CONFIRMED | NONE | "No new integral solutions are found for 9 ≤ n ≤ 16, beyond ones equivalent to known configurations." | CMSV p.3 | The searches are for **symmetric** ideal solutions ("search for symmetric ideal solutions with sizes between n = 9 and n = 16") |
| D3 | CONFIRMED | NONE | "The first ideal solution with size n = 12 was discovered in 1999 by Kuosa, Meyrignac, and Shuwen ... A = ±{22,61,86,127,140,151}, B = ±{35,47,94,121,146,148}. (5)"; "both found by Letac in 1942 ... (3)" | CMSV pp.2-3 | Verified exactly (degree 11; and (6), (7) too). CMSV's second 9-set is the negative of BI's (the same solution) |
| D4 | CONFIRMED | NONE | (D1 and C2 above); Chen p.12: "ideal solutions of the PTE problem have been discovered for degrees n ≤ 9 and n = 11" | - | Same set: size n ↔ degree n−1. Beware that **Chen's n is the degree, CMSV's and BLP's n is the size, BI's n is the size and Melzak's n is the degree** |
| P1 | CONFIRMED | NONE | "Ideal solutions to the PTE Problem are known only for sizes n = 1, 2, ..., 10 and n = 12. Parametric ideal solutions are known for n = 1, 2, ..., 8 and n = 10; in each case they give rise to infinitely many nonequivalent ideal solutions." | BLP p.2063 | |
| P2 | CONFIRMED WITH CORRECTION | MINOR | p.2064: "Gloden [5] on pages 42-43 describes the derivation of a parametric ideal symmetric solution of size 7 ... the final solution, which uses four parameters f, g, k, l ... after dividing it out the parametric solution turns out to depend only on f and k"; p.2069: the two size-9 sets, "the smallest (found by A. Letac in the 1940s) being {±436, ...}", "We found the two solutions {±71, ±131, ±308, ±180, ±307} =_9 {±99, ±100, ±301, ±188, ±313} and {±18, ±245, ±331, ±471, ±508} =_9 {±103, ±189, ±366, ±452, ±515}." | BLP pp.2064, 2069 | (i) "Gloden's two-parameter family" is BLP's **reduction** of Gloden's four-parameter solution to two parameters (f, k), so say "Gloden's family, in the two-parameter form of BLP". (ii) BLP p.2069 does **not** name Letac for the 9-sets (it calls them "the only primitive solutions found"); it names Letac for the size-10 {±436,...}. Cite CMSV p.2 for "Letac's 9-sets". (iii) The two "further size-10 solutions" are BLP's own new ones (2002). All verified exactly; Gloden's family is verified identically in f, k, and f = 3, k = 1 gives BLP's example, which is −(BI's first perfect 7-set) |
| S1 | CONFIRMED (every number and entry) | NONE | A.1.6 (k = 1,3): "Smallest solution, by computer search: [1,5,5]_k = [2,3,6]_k (A.48)"; "A.Moessner gave parameter solutions of this type in 1939". A.1.17 (k = 1,3,5): "Parameter solutions were obtained by A.Gloden in 1949, G.Xeroudakes and A.Moessner in 1958, Lander in 1968, and Ajai Choudhry in 1991 ... [1,13,17,23]_k = [3,9,21,21]_k (A.178)". A.1.26 (k = 1,3,5,7): "First known solutions, by A.Gloden in 1940's: [3,19,37,51,53]_k = [9,11,43,45,55]_k (A.266)". A.1.33 (k = 1,3,5,7,9): "First known solution ... by Chen Shuwen in 2000: [7,91,173,269,289,323]_k = [29,59,193,247,311,313]_k (A.313)"; "Second known solutions, by Jarosław Wróblewski in 2009: (A.314)-(A.316)"; "Only the above four ideal non-negative solutions are known so far. In addition, Jarosław Wróblewski found one integer solution in 2009: [−13,365,689,1111,1115,1325] = [23,305,731,1037,1177,1319]." | Chen pp.198, 211, 218, 224 | The section numbers A.1.6/17/26/33 carry exactly those exponent sets. A.48, A.178, A.266 and A.313 are **equation** numbers inside them. The negative-entry solution has no equation number. All 16 listed solutions were verified exactly for their exponent sets |
| S2 | CONFIRMED | NONE (one hypothesis remark) | "Theorem 3 [5] If [a_1,...,a_m] = [b_1,...,b_m] (k = 1, 3, ..., 2n − 1) then [T+a_1,...,T+a_m, T−b_1,...,T−b_m] = [T+b_1,...,T+b_m, T−a_1,...,T−a_m] (k = 1, 2, ..., 2n) where T is arbitrary integer." | eslpower.org TarryPrb.htm, "General theorems" | Proved below. The identity was checked symbolically for m ≤ 4, k ≤ 9 and on four survey solutions with five values of T. **A non-trivial input can give a trivial lift**: A = {1,−1,5}, B = {2,−2,5} have equal odd power sums, yet A ∪ (−B) = B ∪ (−A). So Prop. 2.2 needs (or must check) A ∪ (−B) ≠ B ∪ (−A) as multisets. The bundle does not show Prop. 2.2's statement, so this is flagged, not graded |
| S3 | CONFIRMED WITH CORRECTION | MINOR | "To date, 33 distinct types of ideal non-negative integer solutions of GPTE have been identified with k_1 < 0 and k_n > 0." A.5.1 (k = −1,1): "[4,10,12]_k = [5,6,15]_k (A.650)". A.5.8 (k = −1,1,3): "[3,10,15,30]_k = [4,5,21,28]_k (A.685)". A.5.9 (k = −1,1,5): "[81,374,585,891]_k = [85,286,702,858]_k (A.693)" | Chen §1.2.1, Example 1.7, p.16; Appendix A.5, pp.275-290 (A.650 p.276, A.685 p.279, A.693 p.280) | The 33-types sentence is in **§1.2.1 (Example 1.7, p.16), not §1.4** (§1.4 is "Multigrade Chains"). The A.5 table of contents lists exactly 33 types (A.5.1-A.5.33). All solutions verified exactly; A.685 fails at exponent 5 |
| S4 | **CONTRADICTED as worded ("does not appear"); CONFIRMED for "not tabulated"** | MINOR | Type (k = −1,1,3,5) **does occur** in the survey: Example 2.36 "P_k = a_1^k + a_2^k + a_3^k + a_4^k, (k = −1, 1, 3, 5) (2.275)" (p.70); Example 3.4 "C = U5V2 − V5U2 + U3V4 − V3U4, for (k = −1, 1, 3, 5) (3.33)" (p.83); "For types (k = 0, 1, 3, 5), (k = −1, 1, 3, 5), and (k = −2, 1, 3, 5), we obtain the same results: β5,min = 0.9009688679..." (p.120, (5.107)); "For type (k = −1, 1, 3, 5), we have β4,min(β5) = y4 ..." (p.139). Also (−1,1,3,5,7) in Example 2.38 (p.71) and Example 5.17 (p.137), and (−1,1,3,5,9) in (2.281) (p.72) | Chen pp.70-72, 83, 120, 137-139 | **No numerical solution** of type (−1,1,3,...,2L−3), L ≥ 4, appears. It is not among the 33 tabulated types of A.5, and eslpower kminus.htm lists (−1,1), (−1,1,2), (−1,1,3), (−1,1,5), (−1,1,2,3), but not (−1,1,3,5). Nothing on unequal-size GPTE in the survey (no hits for "unequal" or "different sizes"; p.14 reads "When m = n, no non-negative integer solutions are found for any exponent set"). Nearest unequal-size literature: Choudhry, arXiv:1602.08698 (sizes s_1 ≠ s_2, exponents 1..k). Replace "does not appear in the survey" by "is not tabulated (no numerical solution is listed), although the survey treats the type in its identities (Ex. 2.36, (3.33)) and normalized bounds ((5.107))" |
| S5 | CONFIRMED | NONE | "To date, ideal non-symmetric solutions have only been discovered for PTE of degrees n ≤ 7." | Chen §1.1.2, p.13 | Here n is the degree. The three non-symmetric examples (A.282, A.324, A.358) were verified exactly |
| S6 | CONFIRMED | NONE | A.1.21 (k = 1,2,3,4): "J.Chernick gave a two-parameter solution of this system in 1937 [35]. All solutions by his method are symmetric: (A.219) (A.220)"; A.1.35 (k = 1,...,6): "J.Chernick gave a two-parameter symmetric solution in 1937 [35]. Numerical example: (A.323)" | Chen pp.214, 226 | Sizes 5 and 7 confirmed. Examples verified |
| O1 | CONFIRMED | NONE | "the "Easier" Waring problem asks for the smallest n, denoted v(k) ... For arbitrary k, the best known bound is v(k) ≪ k log(k)" | Caley arXiv:1011.1262v2, p.2 | Caley p.2 also says: "The best upper bound is due to Melzak, which is N(k) ≤ ½(k²−3) when k is odd, and N(k) ≤ ½(k²−4) when k is even". That repeats the BI formula and attributes it to Melzak, whose paper does not contain it (see B5). Do not use Caley as independent support for B5 |
| O2 | CONFIRMED | NONE | "When s = k+1, solutions ... are known as ideal solutions. Parametric ideal solutions of the TEP are known only when k ≤ 7." ... "all other known parametric ideal solutions ... are given by univariate polynomials of degrees ≥ 5" | Choudhry arXiv:2207.12726v1, p.1 | Choudhry counts polynomial parametrizations (degree k ≤ 7, i.e. size ≤ 8). BLP's "parametric ... n = 10" (size) counts the elliptic-curve families (Letac/Smyth, BI Prop. 4). So the two statements are consistent under different meanings of "parametric", as the claim says |
| O3 | n/a | NONE | (covered by B11) | | |
| O4 | **CONFIRMED** (no refereed o(k²) bound found); one unrefereed contrary claim reported | MINOR | Most recent statements: CMY 2026 p.2: "The best-known upper bound is W(k,m) ≤ k(k+1)/2 + 1"; Wooley 2019 p.53: "apparently achieves the limits of this kind of analytic argument" | see §O4 | No source gives N(k) = o(k²) or anything below (k²+O(k))/2. **Sun-Zhao, arXiv:2307.11330v3 (math.RT, 2023, unpublished, 0 citations)** claims to prove Wright's conjecture: "Theorem 6.5. An ideal solution of the PTE Problem with any degree k always exists." If true it would give N(k) = k+1. The later refereed literature does not accept it (CMSV 2024, Chen 2025, CMY 2026 all call the problem open), and I did not verify it. The paper should not cite it as a result. If the paper says "no proof is known", add "(a 2023 preprint, arXiv:2307.11330, claims one by representation theory; it is unrefereed and not accepted in the subsequent literature)" or rephrase as "open according to [CMSV 2024, CMY 2026]" |

**Claims that failed or need a change:** B5/M1 (SERIOUS: false-for-small-k formula attributed to Wright and Melzak),
S4 (CONTRADICTED as worded), B2, B4, B7, B10, P2, S3 (corrections), O4 (one unrefereed counter-claim to be acknowledged).
No claim is NOT FOUND. SOURCE UNREACHABLE applies only to the primary Wright 1935 behind M1/B5 (gap logged).

## Contamination

None. I opened no file of `theory/pte/` other than the raw source files listed in its SHA256SUMS (BI PDF and BI OCR txt).
For the OCR txt I used only keyword-to-page location. I did not open NOTES.md, LITERATURE.md, `paper/`, `theory/revision/`,
`review/referee-sim/` or any other session's check scripts. `review/audit/G5-VERDICT.md` and the brief were read as instructed.

## Instrument gaps

1. **Borwein-Ingalls**: e-periodica PDF download sits behind a proof-of-work captcha (HTTP 200 "Verification required"),
   so I could not re-fetch it independently. I used theory/pte/sources/BorweinIngalls1994_EnsMath40_pages3-27.pdf; SHA256
   9f864554... matches SHA256SUMS. It is a 25-page scan with the running heads "L'Enseignement Mathématique, t. 40 (1994),
   p. 3-27" and pp. 4-27, read from images.
2. **Wright 1935** (Quart. J. Math. 6, 261-267): OUP returns 403. Wright's bound is known here only through Melzak p.234.
   So I cannot say whether BI's (k²−3)/2, (k²−4)/2 is a sign misprint of a parity-split form of Wright's bound
   ((k²+3)/2, (k²+4)/2 would fit), or something else. Either way BI's printed formula is false for k = 2, 3.
3. Hua (1938, 1949, 1982 book), Gloden (1944), Letac (1942): not reached; attributions to them rest on secondary sources.
4. Published versions of Wooley 2012/2019: theorem numbering checked in the arXiv versions (v1 and v2) only.
5. Search coverage for O4: the Semantic Scholar keyword API was rate-limited (429), and two OpenAlex pages were truncated.
   Coverage came from arXiv (304 records for Tarry/Escott/multigrade), zbMATH Open (64 records with "Tarry" in the title,
   1994-2026), OpenAlex (139 records), and the Semantic Scholar citation list of BLP 2003.

---

## Details for the items singled out by the lead

### B2-B4: what BI Propositions 1, 2, 3 say (BI pp.5-7, read from images)

- Conventions (p.4): "We call n the size of the solution and k the degree." The sets are of size n; the equations run m = 1..k.
- **Prop. 1** (p.5): three equivalent forms. (1) equal power sums for j = 1..k. (2) deg(Π(x−α_i) − Π(x−β_i)) ≤ n − (k+1).
  (3) (x−1)^{k+1} divides Σ x^{α_i} − Σ x^{β_i}. Proof: Newton's identities, and xd/dx applied k+1 times at x = 1.
  It is **not** a statement about N(k).
- **Prop. 2** (p.6): N(k) ≥ k+1. Hypothesis: N(k) as defined on p.6 (size n, degree k). Here k is the degree and the bound
  is on the size, so the bound is k+1 and not k (size n ≤ k would force equal polynomials by form (2)).
- **Prop. 3** (pp.6-7): N(k) ≤ ½k(k+1) + 1, by pigeonhole. Take s = ½k(k+1)+1 and n > s^k s!. There are ≥ n^s/s! classes of
  s-tuples in [1,n] up to permutation, and < s^k n^{k(k+1)/2} = s^k n^{s−1} < n^s/s! possible vectors (s_1,...,s_k).
  I re-checked the inequality chain exactly for k ≤ 5 (check_lifting_and_bounds.txt §3).

My proof of Prop. 2 for multisets: if n ≤ k and p_j(A) = p_j(B) for j ≤ n, Newton's identities give e_j(A) = e_j(B) for
j ≤ n. Then Π(x−a) = Π(x−b), so A = B as multisets. Hence a non-trivial solution has n ≥ k+1.

### B5 / M1: Wright's and Melzak's bounds, translated

- **Melzak's notation** (p.233): system (1) is Σ_{i=1}^k a_i^j = Σ_{i=1}^k b_i^j, j = 1,...,n. A solution is trivial if the two
  sets are permutations of each other, so repeats are allowed (multisets). **n = degree, k = size, K(n) = least size =
  N(n)** in the paper's notation. Melzak's (2), K(n) ≥ n+1, is BI's Prop. 2. His (3), K(n) ≤ [n(n+1)/2] + 1, is BI's Prop. 3,
  credited to Hardy-Wright [1]. On p.234 he writes that "the above bound has been slightly improved in [2] to K(n) ≤ (n²+4)/2"
  ([2] = Wright 1935).
- Melzak's own contribution is Theorem 1, an exact non-constructive formula
  K(n) = ½ min_{P ∈ 𝔄} S[P(x)(1−x)^{n+1}] (S = sum of |coefficients|), plus the numerical Table 1 (b_n for 2 ≤ n ≤ 29).
  There is no closed-form or asymptotic bound in Melzak. I verified the 2^n construction of p.234 for n ≤ 7, and that
  Table 1's last column equals n(n+1)/2 + 1.
- **BI p.7's formula is not the same bound.** In the same notation, BI's ½(k²−3) (odd) / ½(k²−4) (even) and Melzak's report
  of Wright, ½(k²+4), differ by 7/2 or 4 for every k, and no shift k → k±1, k±2 reconciles them (checked for k < 200).
  BI's formula is **false as a bound for k = 2, 3**: it gives 0 < N(2) = 3 and 3 < N(3) = 4 (Prop. 2 and known ideal
  solutions). So it cannot be a correct statement of any theorem. Melzak's tabulated individual bounds are below BI's closed
  form for every 5 ≤ n ≤ 29, but they are numbers, not a formula. Caley (p.2) repeats BI's formula and calls it Melzak's;
  Melzak's text does not support that.
- **Verdict.** The paper's remark "the bounds of Wright and Melzak give (k²−3)/2, (k²−4)/2" faithfully copies BI p.7.
  It is **not supported by Melzak** and is false for k = 2, 3. Wright's paper itself is unreachable (gap 2).
- **Required wording** (replacement for the remark after Theorem 4.2):
  "The pigeonhole bound N(k) ≤ k(k+1)/2 + 1 [Hardy-Wright; BI Prop. 3] was improved by Wright (1935) to N(k) ≤ (k²+4)/2
  (as reported by Melzak [CMB 4 (1961), p.234]). Melzak gave an exact but non-constructive formula for N(k) and numerical
  upper bounds for k ≤ 29 [ibid., Table 1]. None of these is o(k²), and N(k) = o(k²) remains open [BI §6, Problem 3;
  Croot-Mao-Yip 2026]."
  If the authors want BI's parity-split form, they must check it against Wright 1935 first. As printed it is wrong for k = 2, 3.

### B7 / O4: is N(k) = o(k²) open? (adversarial)

1. **Wooley's bounds do not touch N(k).** Wooley defines W(k,h) (p.3 of 1101.0574; p.53 of 1708.01220) with the extra
   condition that the (k+1)-th power sums differ. For h = 2 this is exactly BI's M(k), "degree exactly k and no higher".
   Every solution counted by W is a PTE solution, so N(k) ≤ M(k) = W(k,2), and Wooley's best bound yields only
   N(k) ≤ k(k+1)/2 + 1, identical to pigeonhole. Wooley 2019 p.53 adds that this "apparently achieves the limits of this kind
   of analytic argument". His 1996 result (zbMATH 0881.11043), W(k) ≤ ½k²(log k + log log k + O(1)), is weaker. By-product:
   **BI's Problem 4, M(k) = O(k²), was solved by Wooley 2012 (Thm 1.3)**, so BI's sentence "No progress on questions 3 and
   4 has been made for many years" is obsolete for Q4.
2. **Hua**: M(k) ≤ (k+1)(log ½(k+2)/log(1+1/k) + 1) ~ k² log k (BI p.7). This concerns M(k) and is worse than quadratic.
3. **Caley p.2**: the k log k statement is about v(k) (easier Waring), not N(k) (O1).
4. **CMY 2026 (latest)**: P(k,2) = k+1 open; best bound quadratic (C2, C3).
5. **Searches** (fetches.md): arXiv (304 records), zbMATH Open (64 titles with "Tarry", 1994-2026), OpenAlex (139 records,
   plus abstracts of the 2025-26 Zenodo/SSRN preprints of S. Jovičević on Prouhet-type 2^k constructions, a "six-fold
   improvement over Prouhet's" 2^k bound), the 2011-indexed Barrodale thesis, and the works citing BLP. **No result
   N(k) = o(k²), and no bound below (k² + O(k))/2, was found.**
6. **One contrary claim**: Sun and Zhao, "Strongly commuting ring and the Prounet-Tarry-Escott problem", arXiv:2307.11330v3
   (27 Sep 2023, math.RT). Their Theorem 1.3(2)/6.5 reads "An ideal solution of the PTE problem with any degree always exists",
   claimed via Kostant's strongly commuting rings. zbMATH indexes it as an arXiv preprint only; Semantic Scholar shows 0
   citations. The subsequent refereed and survey literature (CMSV, Math. Comp. 2024; Chen 2025; CMY 2026) treats the problem
   as open. I have not checked the argument; this is out of scope for an attribution audit. It is the only "counterexample"
   to the paper's commentary, and it is an unaccepted preprint, so the commentary stands. A footnote acknowledging it would
   pre-empt a referee.

### C2 / D1 / D4: consistency

- CMY p.1: P(k,2) = k+1 known for 2 ≤ k ≤ 9 and k = 11 (degree).
- CMSV p.2: ideal solutions known for n ≤ 10 and n = 12 (size).
- Chen p.12: degrees n ≤ 9 and n = 11.
- BLP p.2063: sizes n = 1..10 and 12.
- Wooley 2019 p.53: W(k,2) = k+1 for 2 ≤ k ≤ 9 and k = 11.

All the same set under size = degree + 1. I verified one ideal solution of each degree 1-9 and 11 exactly
(check_solutions.txt: BI table, Chen Example 1.1, the size-12 solutions), each failing at the next exponent.
BI 1994 (p.10: "There are no known ideal solutions ... of size 11 or higher") predates the 1999 size-12 solution.
That is consistent in time, but BI must not be cited for the size-12 case.

### S2: Theorem 3 and the lifting (my proof)

Let p_j(X) = Σ_{x∈X} x^j. For each i,
(T+a)^k + (T−b)^k − (T+b)^k − (T−a)^k = Σ_j C(k,j) T^{k−j} [a^j + (−b)^j − b^j − (−a)^j].
The bracket is 0 for even j and 2(a^j − b^j) for odd j. Summing over i, the difference of the k-th power sums of the lifted
multisets is Σ_{j odd ≤ k} 2C(k,j) T^{k−j} (p_j(A) − p_j(B)). For k ≤ 2n only odd j ≤ 2n−1 occur, so the difference vanishes
when p_j(A) = p_j(B) for j = 1, 3, ..., 2n−1. ∎ The size doubles (m → 2m).

The lift is non-trivial iff A ∪ (−B) ≠ B ∪ (−A) as multisets. This fails, for example, for A = {1,−1,5}, B = {2,−2,5}, and in
general whenever A and B are both ±-symmetric up to a common part. For an odd symmetric input B = −A at T = 0 the lift is
"A twice" versus "−A twice": still a solution, of the same degree only. Exact checks: check_lifting_and_bounds.txt §1.

### S1 / S3 / S4: entry numbers

A.1.6 = type (k = 1,3), p.198. A.1.17 = (1,3,5), p.211. A.1.26 = (1,3,5,7), p.218. A.1.33 = (1,3,5,7,9), p.224.
A.1.21 = (1,2,3,4), p.214. A.1.35 = (1,...,6), p.225-226. A.5 = "GPTE with k1 < 0 and kn > 0", 33 subsections A.5.1-A.5.33.
Inside these sections, (A.nn) are equation numbers: A.48 ∈ A.1.6; A.178 ∈ A.1.17; A.266, A.269, A.270 ∈ A.1.26;
A.313-A.316 ∈ A.1.33; A.650 ∈ A.5.1; A.685 ∈ A.5.8; A.693 ∈ A.5.9.
The paper's references to "A.48", "A.313", "A.314-A.316" and "A.685" are therefore correct as equation numbers.
