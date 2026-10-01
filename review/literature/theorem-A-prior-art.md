# Theorem A: prior-art search

Retrieval date: 2026-10-01. Every source was retrieved headlessly (curl, arXiv API, arXiv full-text search, StackExchange API, Crossref, Unpaywall, OpenAlex, zbMATH Open API). Raw material is stored outside the repository. All quotations below come from text retrieved in this session. Page numbers are PDF pages of the retrieved file unless a journal page is given.

Statements under test:

- **(i) Theorem A.** Let m = {m_1,...,m_n} be a multiset of nonzero complex numbers with m_i + m_j != 0 for i < j. Then R = sum 1/m_i together with P_1, P_3, ..., P_{2n-3} determines m.
- **(ii) Odd-power-sum version.** P_1, P_3, ..., P_{2n-1} determine m. The search covered two forms: (a) m is a multiset of positive reals; (b) m is a complex multiset with no two elements summing to zero.

---

## 1. Verdicts

### (i) Theorem A (R = sum 1/m_i together with P_1, ..., P_{2n-3})

**NOT FOUND**, in either the complex form or the positive-real form.

No retrieved source states a uniqueness result for a power-sum system that mixes the exponent -1 with odd positive exponents. The two ingredients of the proof each appear in the literature separately (Section 2):

1. **The "vanishing odd power sums make the polynomial even" step.**
   - MathOverflow 473148 (answer by Dave Benson).
   - Math.SE 3876700.
   - Pokora and Szemberg, arXiv:2606.18387, Remark 13. This is the case 2n = 6 with p_1 = p_3 = p_5 = 0, and the conclusion is stated verbatim.
2. **The union-plus-reciprocal device.** Diederichs, Kolountzakis and Papageorgiou (Monatsh. Math. 2022, arXiv:2107.10348), proof of Theorem 1, after Courtney:
   - They merge the two unknown configurations into one multiset, {z, w'} versus {z', w}.
   - They match the low power sums.
   - They obtain the missing top elementary symmetric functions from the reciprocal symmetry sigma_k(1/x) = sigma_{M-k}(x)/sigma_M(x).
   - In that setting the reciprocal symmetry comes from |z| = 1, not from a prescribed sum of reciprocals. The odd/even structure is also different: there the signs alternate, z versus w.
   - This is the closest structural analogue of the role R plays in Theorem A. It is not a statement of Theorem A.

**Positive-real special case (not stated anywhere found, but within reach of a known method).** Steinig's argument (1971) is reproduced in Jesurum, arXiv:2204.10257, Prop. 4.2. It shows that t -> gamma(t_1) + ... + gamma(t_d) is one-to-one on ordered tuples t_1 < ... < t_d whenever certain Jacobians det[zeta'(u_1) ... zeta'(u_n)] are single-signed and nonzero.

- **Our verification, not taken from any source.** Take gamma(t) = (t^{-1}, t, t^3, ..., t^{2n-3}) on (0, infinity). The relevant Jacobians are constant multiples of generalized Vandermonde determinants with increasing real exponents (-2, 0, 2, ...). Such determinants have constant sign on ordered positive tuples.
- So the Steinig argument plausibly yields the distinct-element, positive-real case of (i).
- Extending it to multisets with repetitions needs a small extension, because the argument as reproduced uses coefficients ±1.
- No source states this application.
- Melánová, Sturmfels and Winter, Prop. 24, does **not** cover (i). It is stated only for exponent sets A of positive integers.

### (ii) Odd-power-sum version (P_1, ..., P_{2n-1})

**(ii-a) Positive reals: KNOWN.** The result is a special case of the following.

- **Melánová, Sturmfels and Winter, "Recovery from Power Sums", Experimental Mathematics (published online 2022), DOI 10.1080/10586458.2022.2061650, arXiv:2106.13981, Proposition 24.**
  - Statement: for any set A of n positive integers, the power-sum map on R^n_{>=0} is injective up to permutation.
  - Taking A = {1, 3, ..., 2n-1} gives (ii-a), repetitions included.
  - Caveat on the proof as printed: it passes from "the determinant of the Jacobian is nonzero along the segment" to "each coordinate of J·(X_2 - X_1) has constant sign". That step is not immediate. The authors also refer to Müller et al., Found. Comput. Math. 16 (2016), Thm. 1.4, for "a much more general version of this argument".
- **Steinig's theorem.** MathOverflow 410757 attributes an essentially equivalent statement to J. Steinig, Rend. Mat. (6) 4 (1971) 629–644. That paper was not retrieved (see Section 4).
  - The MO question asks about the shifted system p_3, p_5, ..., p_{2n+1} on positive reals.
  - The top-scored answer, by "Jaume" (score 10), restates the problem as the nonexistence of nontrivial solutions of sum_{i<=a} gamma(x_i) = sum_{i<=b} gamma(y_i) with a + b <= 2n and gamma(x) = (x^3, ..., x^{2n+1}). It says this is "precisely the content of [Steinig]".
  - An MO comment by the user YCor (2021-12-14) says: "I can prove it's true for p_1,…,p_{2n−1}".
- (ii-a) is also immediate from (ii-b), since a multiset of positive reals has no two elements summing to zero.

**(ii-b) Complex multisets with no two elements summing to zero: KNOWN IN EQUIVALENT FORM, with one caveat.**

- **Korobov and Bugaevskaya, "Almost power sum systems", Math. Comp. 85 (2016), no. 298, 717–736, DOI 10.1090/mcom/2994, Section 3.**
  - They derive "analogs of Newton's identities" linking sigma_1, ..., sigma_n to the odd power sums S_1, ..., S_{2n-1}.
  - They prove that if a Hankel determinant built from the data is nonzero, then sigma = -A^{-1} gamma is uniquely determined. Hence the multiset is determined.
  - When the Hankel determinant vanishes, the system has infinitely many solutions or none. Their degenerate example is T_1 = -T_2.
- **What Korobov and Bugaevskaya do not do.** They do not phrase the nondegeneracy hypothesis as "no two T_i sum to zero".
  - The equivalence would go through their rational function R_1(z): the ratio of the odd and even parts of prod(z - T_i). Hankel nonvanishing means this fraction is in lowest terms, and that should mean "no T_i, T_j with T_i + T_j = 0".
  - This is a standard Kronecker/Padé fact. It is not written in their paper.
  - We checked this equivalence only for the even-n case. For odd n, the fraction R_2 has a factor z in the denominator, so the equivalence needs separate checking.
- **The elementary route to (ii-b) is folklore-level and appears in fetched sources.**
  - MO 473148: for 2n complex numbers in characteristic 0, vanishing odd power sums up to 2n-1 imply the multiset is invariant under negation.
  - Apply this to m ∪ (-m').
  - No source found combines these into the statement "a multiset with no two elements summing to zero is determined by its first n odd power sums".
- If the caveat matters, read (ii-b) as: **known in substance (Korobov–Bugaevskaya Hankel criterion; MO 473148 lemma), not found as a stated theorem in the "m_i + m_j != 0" form.**

### Closely related known results, and how close they are

| Result | Source | Relation to (i)/(ii) |
|---|---|---|
| Any n power sums with positive integer exponents determine a multiset of n nonnegative reals | Melánová, Sturmfels and Winter, Prop. 24 | Contains (ii-a). Does not contain (i), because exponent -1 is not allowed. |
| Steinig's rule: sums of points on a curve with single-signed Jacobian minors are one-to-one on ordered tuples | Steinig 1971 (not retrieved), reproduced as Jesurum, Prop. 4.2; cited for the two-variable case by Brüdern and Wooley | Contains (ii-a) for distinct points. Plausibly gives the positive-real case of (i) (our verification above; not stated in any source). |
| Odd-power-sum Newton analogues and a Hankel uniqueness criterion | Korobov and Bugaevskaya 2016 | (ii-b) in Hankel-determinant form. Nothing on reciprocals. |
| n consecutive power sums p_{d+1}, ..., p_{d+n} form a regular sequence; n! must divide the product of the degrees | Conca, Krattenthaler and Watanabe (CKW), Prop. 2.9 and Lemma 2.8 | Concerns the zero fibre (quasi-finiteness), not injectivity. For A = {1, 3, ..., 2n-1}, n! does not divide the product of the degrees when n >= 2, so the odd power sums are **not** a regular sequence. Their zero fibre contains the pairs {x, -x}, which is exactly the obstruction Theorem A's hypothesis removes. |
| n + 1 power sums with coprime exponents should generically determine n complex numbers | Melánová, Sturmfels and Winter, Conjecture 6; Dvornicich and Zannier 2009 (field generation, title and citation only) | Generic injectivity over C. Different regime (n + 1 measurements, generic points). |
| The ring generated by the odd power sums has the Q-cancellation property f(x_1, -x_1, x_2, ...) = f(x_2, ...) | MO 212800 | Structural reason the odd power sums cannot separate multisets that differ by cancelling pairs {x, -x}. Theorem A's hypothesis m_i + m_j != 0 removes exactly this. |
| Characteristic 2 (BCH decoding): odd syndromes determine the error locators | Belinsky and Zabokritskiy, arXiv:2608.23833 (snippet seen) | Analogue in characteristic 2 only. Not relevant to C. |

---

## 2. Closest sources, with verbatim quotes

### 2.1 Melánová, Sturmfels and Winter, "Recovery from Power Sums"

- **Bibliographic data.** H. Melánová, B. Sturmfels, R. Winter. Experimental Mathematics, published online 2022-04-23, DOI 10.1080/10586458.2022.2061650 (Crossref). arXiv:2106.13981 [math.AG], v1, 26 Jun 2021. The arXiv v1 PDF was read.
- **Proposition 24** (p. 12 of the PDF):
  > "Proposition 24. For m = n, recovery from p-norms is always unique. Given any set A of n positive integers, the map φ_{A,≥0} : R^n_{≥0} → R^n_{≥0} is injective up to permuting coordinates."
- **Section 5 opening** (p. 11):
  > "Hence, our recovery problem for nonnegative vectors x ∈ R^n_{≥0} is equivalent to recovery of x from values of the p-norms || · ||_p, where p runs over a prespecified set A of positive integers."
- **The step in the proof noted above** (p. 12):
  > "The Schur polynomial S does not vanish on L \ {X1}, and neither do the linear factors. Hence, the coordinates of the vector Jφ · (X2 − X1) do not vanish at any point on L \ {X1}. … For a much more general version of this argument, we refer to the equivalence of conditions (inj) and (jac) in [12, Theorem 1.4]."
- **Conjecture 6** (p. 4):
  > "The recovery of a set of n complex numbers from n + 1 power sums with coprime powers is unique. To be precise, for m = n + 1, the map φ is generically injective."
- **The odd-exponent obstruction over C** (Remark 9, p. 5):
  > "set n = m = 4, and let A consist of four odd coprime integers. … the scheme (HS) is not zero-dimensional in P^4, since it contains the lines defined by x_i = −x_j, x_k = −x_l, x_0 = 0".
- **Example 4** (p. 3), for A = {3, 5, 7}:
  > "The radical of this ideal equals ⟨x1 + x2, x3⟩ ∩ ⟨x1 + x3, x2⟩ ∩ ⟨x2 + x3, x1⟩."
- **Relevance.** This proves (ii-a) as the special case A = {1, 3, ..., 2n-1}. Nothing in the paper concerns negative exponents or the complex no-opposite-pairs hypothesis.

### 2.2 Korobov and Bugaevskaya, "Almost power sum systems"

- **Bibliographic data.** V. I. Korobov, A. N. Bugaevskaya. Mathematics of Computation 85 (2016), no. 298, 717–736. DOI 10.1090/mcom/2994. Published electronically 2015-06-26. The open-access PDF from ams.org was located via Unpaywall.
- **Abstract** (journal p. 717):
  > "For the system with even power gaps the obtained equalities are the analogs of Newton's identities. These equalities express the connection between elementary symmetric functions and odd power sums."
- **Uniqueness discussion** (journal p. 720):
  > "We note that the solution of the system (1.3) is unique (up to permutation of variables). On the other hand, the system (1.2) and, in particular, the system (1.8), may have a unique solution (up to permutation of the variable), as well as an infinite number of solutions, and a solution may not exist at all."
  
  Here (1.8) is the system sum_{i=1}^n T_i^{2k-1} = s_{2k-1}, k = 1, ..., n.
- **Key identity** (journal p. 724, eq. (3.1)):
  > "sum_{i=1}^n arth (T_i / z) = sum_{k>=1} S_{2k-1} / ((2k−1) z^{2k−1})".
  
  The paper defines R_1(z) = (σ_1 z^{n−1} + σ_3 z^{n−3} + …)/(z^n + σ_2 z^{n−2} + …).
- **Uniqueness criterion** (journal p. 726):
  > "Observe that det A = (−1)^{n/2} Δ̃_{1,n/2}. Suppose that Δ̃_{1,n/2} is nonzero, then from (3.6) we obtain the equality (3.7) σ = −A^{−1} γ."
- **Theorem 3.1** (journal p. 726):
  > "Theorem 3.1. The equality (3.5) for even n and the equality (3.10) for odd n express the connection between elementary symmetric functions σ1, . . . , σn and odd power sums S1, . . . , S2n−1, . . ."
- **Degenerate case** (journal pp. 728–729):
  > "Consider the cases when Hankel determinants Δ̃_{1,n/2} and Δ̃_{1,(n−1)/2} are equal to zero. In these cases the system (1.8) for even n and odd n has the infinite set of solutions if the conditions rank(…) = rank(…) … are fulfilled".
- **Example 3.3:**
  > "Put s1 = 1, s3 = 1. Then s5 = s7 = 1 and the system (3.17) has the infinite number of solutions T1 = −T2, T3 = 0 and T4 = 1."
- **Relevance.** This is the closest published treatment of the odd-power-sum fibre over C. Uniqueness is stated under a Hankel-determinant hypothesis, not under "T_i + T_j != 0". It contains no reciprocal power sum.

### 2.3 MathOverflow 410757, "Do power sums determine the variables?"

- **Bibliographic data.** Question by Thierry Laurens, 2021-12-14. https://mathoverflow.net/questions/410757/do-power-sums-determine-the-variables
- **Question:**
  > "Given n positive real numbers x_1,…,x_n, consider the n-many power sums p_3 = …, p_5 = …, ⋮ p_{2n+1} = … Do the values of the power sums p_3,p_5,…,p_{2n+1} uniquely determine x_1,…,x_n (up to reordering)? I was wondering if this problem exists in the literature?"
- **Answer 410848 by "Jaume" (2021-12-15, score 10):**
  > "the problem can be restated as: Let 0≤a,b, a+b≤2n integers, and x_1,…x_a,y_1,…y_b ∈ R_{≥0}. Then sum_{i=1}^a γ(x_i) = sum_{i=1}^b γ(y_i) has no nontrival solutions. From what I can see from the MathSciNet review, that is precisely the content of [1]. … [1] J. Steinig, On some rules of Laguerre's, and systems of equal sums of like powers. Rend. Mat. (6) 4 (1971), 629–644 (1972). [2] S. W. Drury and B. P. Marshall, Fourier restriction theorems for degenerate curves. Mathematical Proceedings of the Cambridge Philosophical Society, 101(3), 541-553."
- **Answer 410780 by Chris McDaniel (2021-12-15)** points to CKW, Lemma 2.8, Proposition 2.9 and Conjecture 2.10.
- **Comment by YCor (2021-12-14):**
  > "I can prove it's true for p_1,…,p_{2n−1}, but I'm not sure about p_3,…,p_{2n+1}."
- **Comment by Brendan McKay (2021-12-15)** on the Korobov–Bugaevskaya paper:
  > "Amongst other things, the paper shows how to solve the version with p_1,p_3,…,p_{2n−1}. It says there can be infinitely many solutions, though it doesn't have the positivity constraint."
- **A further comment** points to arXiv:2106.13981 (Section 2.1 above).
- **Relevance.** Positive-real odd-power systems were treated as a reference request in 2021. The answers point to Steinig 1971. Neither the question nor the answers mention a reciprocal sum.

### 2.4 Steinig's argument, as reproduced by Jesurum

- **Bibliographic data.** M. Jesurum, "Fourier restriction to smooth enough curves", arXiv:2204.10257, Section 4, pp. 17–18 of the PDF. The cited original is J. Steinig, "On some rules of Laguerre's, and systems of equal sums of like powers", Rend. Mat. (6) 4 (1971), 629–644 (zbMATH Zbl 0238.10007, year 1972; zbMATH has no review text).
- **Jesurum, p. 17:**
  > "the Jacobian J_{Φζ_h} is single-signed and nonzero in the region A = {(t_1, . . . , t_n) ∈ I^d : t_1 < · · · < t_n}. With that, an argument of Steinig [34] (see also [11, 16]) shows that Φ_{γ_h} is 1-to-1 on A. Proposition 4.2 (Steinig). Φ_{γ_h} is 1-to-1 on A = {(t_1, . . . , t_d) ∈ I^d : t_1 < · · · < t_d}."
- **Jesurum, proof sketch:**
  > "We can rewrite (39) as sum_{j=1}^m ε_j γ_h(u_j) = 0 for some even integer m ∈ [2, 2d], u_1 < · · · < u_m ∈ I, ε_j ∈ {−1, 1} … Then the sequence of α_l's has at most d−1 changes of sign."
- **Brüdern and Wooley, "A paucity problem for certain triples of diagonal equations", arXiv:2106.03986, p. 4:**
  > "when m ≠ k, it follows that whenever x, y ∈ N^2 and x_1^k + x_2^k = y_1^k + y_2^k, x_1^m + x_2^m = y_1^m + y_2^m, then {x_1, x_2} = {y_1, y_2}. This assertion may be confirmed either by elementary arguments, or by reference to [10]."
  
  Here [10] is Steinig.
- **Relevance.** This is the classical real-variable injectivity principle (Laguerre/Descartes rule of signs, a Chebyshev-system type argument). It covers ordered positive tuples for any curve satisfying the Jacobian sign condition. It is the most plausible prior source for the positive-real forms of both (i) and (ii). However, Steinig's own statement could not be read (Section 4).

### 2.5 The vanishing-odd-power-sums lemma and the union device

- **MathOverflow 473148, "Question about the sum of odd powers equation".**
  - Question by Dmitri Scheglov, 2024-06-13:
    > "Assume we have 2n real numbers … Assume also that S_k=0 for any odd positive integer k … Conjecture: these 2n numbers can be split on n pairs of type (x,−x)."
  - Answer 473181 by Dave Benson (2024-06-13):
    > "This is true over any field of characteristic zero, or characteristic larger than 2n. … Now suppose that p_k=0 for k odd. Then p_k(x_1,…,x_{2n}) = p_k(−x_1,…,−x_{2n}) for all 1⩽k⩽2n and so {x_1,…,x_{2n}} = {−x_1,…,−x_{2n}}."
  - Answer 473149 by "GH from MO" gives a real-variable growth argument.
- **Math.SE 3876700, "Sum of odd powers of even number of complex numbers".** Answer by "metamorphy", 2020-10-22:
  > "The above basically shows that p(z)=prod_{j=1}^n (z−z_j) satisfies p(z)=p(−z), so that z↦−z acts as a permutation on z_1,…,z_n."
- **Pokora and Szemberg, "A Pascal-type construction of the Segre cubic and the Cremona–Richmond configuration", arXiv:2606.18387, Remark 13, p. 12:**
  > "on each plane Π_{ab|cd|ef} : x_a + x_b = x_c + x_d = x_e + x_f = 0, all odd power sums vanish. Conversely, if p1 = p3 = p5 = 0, then Newton identities give e1 = e3 = e5 = 0. Hence prod_{i=1}^6 (t − x_i) = t^6 + e2 t^4 + e4 t^2 + e6 is an even polynomial, so the coordinates x1, . . . , x6 can be paired as opposites."
- **Diederichs, Kolountzakis and Papageorgiou, "How many Fourier coefficients are needed?"** Monatshefte für Mathematik (online 2022-10-21), DOI 10.1007/s00605-022-01792-0 (Crossref); arXiv:2107.10348.
  - Theorem 1, p. 2:
    > "Suppose that the sets E, E′ ⊆ T are both unions of at most N open arcs and that χ̂_E(ν) = χ̂_{E′}(ν) for ν = 0, 1, . . . , N. Then E = E′."
  
    They credit the theorem to D. Courtney, "Unions of arcs from Fourier partial sums", New York J. Math. 16 (2010) 235–243.
  - Proof, p. 3:
    > "From this we get s_ν(z, w′) = s_ν(z′, w), for ν = 1, 2, . . . , N … We now use the fact that |z_j| = |w_j| = |z′_j| = |w′_j| = 1: (3) σ_k(z, w′) = σ_k(1/z, 1/w′)‾ = σ_{M−k}(z, w′)/σ_M(z, w′) … We have proved that σ_ν(z, w′) = σ_ν(z′, w), ν = 0, 1, 2, . . . , M, hence the multisets {z_j, w′_j} and {z′_j, w_j} are equal … But {z_j} ∩ {w_j} = {z′_j} ∩ {w′_j} = ∅ so the only possibility is that {z_j} = {z′_j} and {w_j} = {w′_j}".
  - Section 2.2, p. 4:
    > "s1(x) = s2(x) = . . . s2N−1(x) = 0 ⇐⇒ σ1(x) = σ2(x) = . . . σ2N−1(x) = 0."
- **Relevance.** Together these contain every step of the proof idea of Theorem A:
  - form the union m ∪ (-m');
  - vanishing low power sums give vanishing low elementary symmetric functions;
  - a reciprocal relation supplies the missing top coefficient;
  - a disjointness hypothesis separates the union.

  No source assembles them into the statement of Theorem A or of (ii-b).

### 2.6 Conca, Krattenthaler and Watanabe, and successors (regular sequences of power sums)

- **Bibliographic data.** A. Conca, C. Krattenthaler, J. Watanabe, "Regular sequences of symmetric polynomials", arXiv:0801.2662 (v3, 29 Aug 2018). Published as Rend. Sem. Mat. Univ. Padova 121 (2009) 179–199; this citation is as given in arXiv:2106.13981 and in MO 410757.
- **Lemma 2.8** (p. 5):
  > "Let f1, f2, . . . , fn be a regular sequence of homogeneous symmetric polynomials in R_n. Then n! divides (deg f1)(deg f2) · · ·(deg fn)."
- **Abstract:**
  > "n consecutive power sums in n variables form a regular sequence."
- **Successor paper.** A. Conca, A. K. Singh, K. Soundararajan, "Ideals generated by power sums", arXiv:2409.18906, Remark 1.2(6), p. 2:
  > "polynomials p_a, p_b form a regular sequence in K[x1,x2] if and only if the characteristic of K differs from 2, and either a/gcd(a,b) or b/gcd(a,b) is even."
- **Relevance.** These papers concern only the zero fibre. With all exponents odd, the power sums are never a regular sequence for n >= 2, because pairs {x, -x} lie in the zero fibre. They say nothing about injectivity, and nothing about the exponent -1.

---

## 3. Search log

"Hits" means the total reported by the endpoint. For StackExchange it means the number of items returned, with a page size of 30, or 100 for title searches over 2 pages. "Relevant" lists the hits opened and judged pertinent.

### arXiv API (export.arxiv.org/api/query)

| # | Query (exact) | Hits | Relevant |
|---|---|---|---|
| 1 | `all:"power sums" AND all:"regular sequence"` | 4 | 0801.2662 (CKW); 1110.6813, 1309.1098, 2609.07932 (regular-sequence follow-ups, context only) |
| 2 | `all:"odd power sums"` | 11 | none |
| 3 | `abs:"power sums" AND abs:determine AND abs:multiset` | 1 | none |
| 4 | `all:"power sum" AND all:injective AND all:symmetric` | 2 | none |
| 5 | `abs:"sums of odd powers"` | 2 | none |
| 6 | `abs:"Newton identities" AND abs:gaps` | 1 | none |
| 7 | `all:"power sums" AND all:"positive reals" AND all:uniquely` | 0 | none |
| 8 | `abs:"hyperoctahedral" AND abs:"power sums" AND abs:"odd"` | 0 | none |
| 9 | `abs:"power sums" AND abs:"Vandermonde" AND abs:"determine"` | 0 | none |
| 10 | `all:"Prouhet-Tarry-Escott" AND all:odd` | 1 | 2506.11429 (PTE survey; full text grepped, no uniqueness statement for real/odd systems) |
| 11 | `abs:"power sums" AND abs:"generate" AND abs:"ring of symmetric"` | 5 | none |
| 12 | `all:"power sums" AND all:"injectivity"` | 6 | none |
| 13 | `ti:"power sums" AND cat:math.AC` | 7 | 2409.18906, 1110.6813 |
| 14 | `abs:"moment problem" AND abs:"odd moments"` | 0 | none |
| 15 | `abs:"signed multiset"` | 3 | none |
| 16 | `all:"Conca" AND all:"Krattenthaler" AND all:"Watanabe"` | 5 | 0801.2662, 2409.18906 |
| 17 | `abs:"power sum" AND abs:"reconstruct" AND abs:"multiset"` | 0 | none |
| 18 | `id:2106.13981` (lookup) | 1 | 2106.13981 (Melánová–Sturmfels–Winter) |
| 19 | `all:"almost power sum"` | 0 | none (Korobov–Bugaevskaya is not on arXiv) |
| 20 | `au:Korobov AND all:"power sum"` | 0 | none |
| 21 | `abs:"equal sums of like powers" AND abs:real` | 0 | none |
| 22 | `abs:"generalized Vandermonde" AND abs:injective` | 1 | none |
| 23 | `abs:"power sum" AND abs:"positive orthant" AND abs:unique` | 0 | none |

### arXiv full-text search

| # | Query (exact) | Hits | Relevant |
|---|---|---|---|
| 24 | `"odd power sums"` | 50 | 2608.23833 (characteristic 2 analogue only) |
| 25 | `"odd power sums" uniquely determine` | 10 | none |
| 26 | `"odd power sums" "positive real"` | 1 | none |
| 27 | `"sums of odd powers" determine` | 12 | none |
| 28 | `"power sums" "positive reals" "uniquely determined"` | 8 | none |
| 29 | `"odd power sums" "elementary symmetric" even polynomial` | 21 | 2606.18387 (Pokora–Szemberg, Remark 13) |
| 30 | `"x_i + x_j" "odd power sums"` | 0 (no results block) | none |
| 31 | `"Steinig"` | 78 | 2204.10257 (Jesurum, Prop. 4.2); 2106.03986 (Brüdern–Wooley) |
| 32 | `"power sums" "reciprocals" "uniquely determine"` | 5 | none |
| 33 | `"equal sums of like powers" Laguerre` | 1 | none |
| 34 | `"odd power sums" "sum of reciprocals"` | 1 | none |
| 35 | `"power sums" "Descartes" "rule of signs" injective` | 4 | 2303.09512 (image of the power-sum map; context only) |
| 36 | `"Chebyshev system" "power sums" unique` | 1 | 2107.10348 (Diederichs–Kolountzakis–Papageorgiou) |

### StackExchange API, MathOverflow (`/2.3/search/advanced`, `q=`)

| # | Query (exact) | Hits | Relevant |
|---|---|---|---|
| 37 | odd power sums determine | 2 | none |
| 38 | sums of odd powers determine | 6 | none |
| 39 | power sums determine multiset | 0 | none |
| 40 | odd power sums positive | 29 | none |
| 41 | power sums uniquely determine | 8 | 410757 |
| 42 | odd powers uniquely determine | 0 | none |
| 43 | same odd power sums | 21 | none |
| 44 | power sums positive reals injective | 1 | 410757 |
| 45 | power sums with gaps | 13 | none |
| 46 | Newton identities odd | 4 | none |
| 47 | odd moments determine | 3 | none |
| 48 | power sums positive numbers determine | 5 | 410757 |
| 49 | equal sums of like powers real numbers | 3 | none |
| 50 | Prouhet Tarry Escott odd powers | 0 | none |
| 51 | sum of reciprocals power sums determine | 5 | none |
| 52 | `title=power sums` | 17 | 410757 |
| 53 | `title=odd powers` | 8 | 473148 |
| 54 | `title=power sum` | 31 | 212800 (Q-cancellation property); 510933 (Lander–Parkin–Selfridge, not relevant) |

The following MathOverflow question bodies were fetched with `/2.3/questions/<id>?filter=withbody`, together with their answers (and, for 410757, comments): 410757, 212800, 473148, 510933.

### StackExchange API, Math.SE (same endpoint, `site=math`)

| # | Query (exact) | Hits | Relevant |
|---|---|---|---|
| 55 | odd power sums determine | 17 | none |
| 56 | sums of odd powers determine | 15 | none |
| 57 | power sums determine multiset | 0 | none |
| 58 | odd power sums positive | 30 | none |
| 59 | power sums uniquely determine | 22 | none |
| 60 | odd powers uniquely determine | 9 | none |
| 61 | same odd power sums | 30 | 4899756 (opened; the classical p_1..p_n system, not relevant) |
| 62 | power sums positive reals injective | 0 | none |
| 63 | power sums with gaps | 22 | none |
| 64 | Newton identities odd | 5 | none |
| 65 | odd moments determine | 7 | none |
| 66 | power sums positive numbers determine | 9 | none |
| 67 | equal sums of like powers real numbers | 10 | none |
| 68 | Prouhet Tarry Escott odd powers | 0 | none |
| 69 | sum of reciprocals power sums determine | 2 | none |
| 70 | `title=power sums` | 35 | 2824954, 1354296 (titles concern the classical p_1..p_n case; bodies not opened) |
| 71 | `title=odd powers` | 35 | 3876700 |
| 72 | `title=power sum` | 68 | 66827 (classical case by title; body not opened) |

### Crossref (`query.bibliographic`)

| # | Query (exact) | Hits | Relevant |
|---|---|---|---|
| 73 | Steinig On some rules of Laguerre's and systems of equal sums of like powers | 6,162,682 | none: Steinig is not in Crossref; top hits were other "equal sums of like powers" papers |
| 74 | Drury Marshall Fourier restriction theorems for degenerate curves | 443,269 | 10.1017/s0305004100066901 |
| 75 | Korobov Bugaevskaya Almost power sum systems | 6,190,399 | 10.1090/mcom/2994 |
| 76 | Melanova Sturmfels Winter Recovery from power sums | 11,275,311 | 10.1080/10586458.2022.2061650 |
| 77 | Dvornicich Zannier Newton functions generating symmetric fields irreducibility Schur polynomials | 18,091 | 10.1016/j.aim.2009.06.021 (title only) |
| 78 | Diederichs Kolountzakis Papageorgiou How many Fourier coefficients are needed | 1,413,630 | 10.1007/s00605-022-01792-0 |
| 79 | odd power sums determine the numbers uniquely | 2,098,332 | none in top 8 |
| 80 | power sums with even gaps Newton identities | 2,152,673 | none in top 6 |
| 81 | uniqueness of solutions of power sum systems positive real numbers | 7,835,618 | none in top 8 |

### OpenAlex (`/works?search=`)

| # | Query (exact) | Hits | Relevant |
|---|---|---|---|
| 82 | odd power sums | 279,346 | none in top 15 |
| 83 | Steinig Laguerre equal sums of like powers | 1 | none (Borwein et al., PTE, 1997) |
| 84 | power sums determine positive real numbers | 537,715 | none in top 15 |
| 85 | systems of equal sums of like powers real numbers uniqueness | 97,324 | none in top 15 |
| 86 | Newton identities odd power sums elementary symmetric | 2,349 | none in top 15 |
| 87 | power sum map injective positive orthant | 577 | 10.48550/arxiv.1311.5493 (Müller et al., sign conditions for injectivity; the reference [12] of Melánová–Sturmfels–Winter; not read) |

### zbMATH Open API (`/v1/document/_search`)

| # | Query (exact) | Hits | Relevant |
|---|---|---|---|
| 88 | `ti:Laguerre & au:Steinig` | 1 | Zbl 0238.10007 (Steinig 1971/72; metadata only, no review text) |
| 89 | `rf:0238.10007` | error / no result list | none |
| 90 | `ti:"odd power sums"` | 2 | none |
| 91 | `ab:"odd power sums" & ab:determine` | error / no result list | none |
| 92 | `ti:"power sums" & ti:(determine \| uniqueness \| recovery)` | 1 | 1543.13023 (content withheld by zbMATH licence notice) |
| 93 | `ab:"sums of odd powers" & ab:unique` | 1 | none |

### Semantic Scholar (`/graph/v1/paper/search`)

| # | Query (exact) | Hits | Relevant |
|---|---|---|---|
| 94 | odd power sums determine positive real numbers | HTTP 429 throughout | — |
| 95 | equal sums of like powers Laguerre rule of signs | HTTP 429 throughout | — |
| 96 | power sums uniquely determine variables | HTTP 429 throughout | — |
| 97 | recovery from power sums positive reals injective | HTTP 429 throughout | — |
| 98 | sums of odd powers uniqueness multiset | HTTP 429 throughout | — |

### Unpaywall

| # | Lookup | Result |
|---|---|---|
| 99 | 10.1090/mcom/2994 | is_oa = true; PDF at ams.org, retrieved |
| 100 | 10.1017/s0305004100066901 | is_oa = false |
| 101 | 10.1080/10586458.2022.2061650 | is_oa = true; arXiv copy used |

---

## 4. Instrument gaps

1. **Semantic Scholar API.**
   - URL: `https://api.semanticscholar.org/graph/v1/paper/search?query=...` (five queries).
   - Error: every attempt returned HTTP 429 "Too Many Requests", including the full backoff of 4, 8, 16, 32 and 40 s.
   - Why it matters: no citation-graph traversal was possible. Forward citations of Steinig 1971, Korobov–Bugaevskaya 2016 and Melánová–Sturmfels–Winter 2022 are the most likely places for a later explicit statement of (ii-b) or (i).
2. **J. Steinig, "On some rules of Laguerre's, and systems of equal sums of like powers", Rend. Mat. (6) 4 (1971), 629–644.**
   - No DOI exists in Crossref. zbMATH Open (Zbl 0238.10007) gives metadata only. No online full text was found.
   - Why it matters: this is the most likely classical source for the positive-real statements, possibly including general real exponents such as -1, which would cover the positive-real case of (i). Its content is known here only through MO 410757 and Jesurum's reconstruction. The MathSciNet review cited in MO 410757 was not accessible.
3. **S. W. Drury and B. P. Marshall, "Fourier restriction theorems for degenerate curves", Math. Proc. Cambridge Philos. Soc. 101 (1987).**
   - DOI 10.1017/s0305004100066901. The Cambridge landing page returned HTTP 200 with the abstract only. Unpaywall reports is_oa = false.
   - Why it matters: per MO 410757 it contains the Steinig-type injectivity argument "in a slightly more general setting", possibly with real exponents.
4. **Müller, Feliu, Regensburger, Conradi, Shiu and Dickenstein, "Sign conditions for injectivity of generalized polynomial maps…", Found. Comput. Math. 16 (2016); arXiv:1311.5493 per OpenAlex.**
   - Identified but not fetched.
   - Why it matters: Melánová, Sturmfels and Winter cite its Theorem 1.4 to justify the step in Prop. 24 flagged in Section 2.1. Its real-exponent setting might give the positive-real case of (i).
5. **Dvornicich and Zannier, Adv. Math. 222 (2009), DOI 10.1016/j.aim.2009.06.021.** Known only from Crossref metadata and citations; not fetched. It concerns generic generation of symmetric fields by n + 1 power sums, which is tangential.
6. **MathSciNet.** Not accessible headlessly without a subscription. Its review of Steinig is the source quoted secondhand in MO 410757.
7. **arXiv full-text search.**
   - What happened: the documented POST to `https://arxiv.org/search_classic` with `searchtype=ft` returned HTTP 302, redirecting to `https://search.arxiv.org/?query=...&in=`.
   - GET requests to `https://search.arxiv.org/` with `query=...&in=&startat=0|10|20` returned HTML result pages, which were parsed.
   - Limits: only the first 30 hits per query were examined. One query (`"x_i + x_j" "odd power sums"`) returned a page with no results block.
8. **zbMATH Open "cited-by" search.** `rf:0238.10007` and one abstract query returned a response without a result list. Forward citations of Steinig could not be listed there. Some zbMATH records (1423.11036, 1543.13023) are withheld under a licence notice.
9. **Google Scholar.** Not used, under the headless-only retrieval rule. Forward citations of the key sources were therefore not traced through Scholar either.

Summary: on the evidence retrieved, (ii) is known for positive reals, and over C it is known in Hankel-determinant form. Theorem A (i), with the reciprocal sum, was not found in any form. Gaps 1–4 are the places where a counterexample to the "NOT FOUND" verdict for (i) could most plausibly be hiding, especially its positive-real case via real-exponent Steinig/Drury–Marshall/Müller-type injectivity theorems.
