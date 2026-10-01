# P7. Theorem A: prior art

Theorem A (AU.1) says that m ↦ I_n(m) = (R, P_1, P_3, …, P_{2n−3}) is injective on n-multisets of nonzero complex numbers with m_i + m_j ≠ 0, and in particular on positive reals.

## Verdicts

**(i) Does arXiv:1311.5493 (Müller–Feliu–Regensburger–Conradi–Shiu–Dickenstein, FoCM 16 (2016)) give the positive-real case of Theorem A? NO.** It does not, even partially.

1. Its theorems characterise injectivity of the **entire family** f_κ(x) = A diag(κ) x^B, for **all** κ ∈ R^r_+, on the **full open orthant** R^n_+ (or with respect to a set S of differences).
2. The Theorem A map, encoded directly, is symmetric, so it is not injective on ordered tuples. Their criterion fails, and must fail. I give an explicit witness w = Bv ∈ ker A, w ≠ 0, for n = 2,…,6. The Theorem 1.5 (bnd) minor products take both signs for n = 2,3,4.
3. "Modulo permutation" cannot be encoded through their restricted injectivity. Every nonzero d ∈ Rⁿ is the difference of a non-permutation pair, so S would have to be all of Rⁿ.
4. The ordered chamber {x_1 < … < x_n} is not a positive orthant and is not the image of one under a monomial change of variables, which maps R^n_+ onto R^n_+. So their theorems cannot be restricted to the chamber.
5. The reduction to elementary symmetric functions e gives a generalised polynomial map with mixed-sign coefficients. That map is **not injective on the positive e-orthant**, even at κ = 1, for every n ≥ 3. Exact witnesses come from {ib, −ib, c_1, …}; for n = 3, e = (2,1,2) and (2,4,8) have the same (R, P_1, P_3). Condition (jac) fails at an explicit point. So no theorem on the full orthant can yield Theorem A. The relevant domain is the real-rooted region, which they do not treat.
6. The paper contains no example about power sums, symmetric maps or permutations. A text search for "power sum", "symmetric", "permut", "Newton" and "Vandermonde" finds nothing relevant.

The only link in the literature is a pointer. Melánová–Sturmfels–Winter, after proving their Proposition 24, write: "For a much more general version of this argument, we refer to the equivalence of conditions (inj) and (jac) in [12, Theorem 1.4]", where [12] is 1311.5493. This is an analogy for the Jacobian argument on the chamber. It is not an application of 1311.5493.

**The actual prior art for the positive-real case is Steinig (1971), through Laurens.**
- Laurens (arXiv:2206.09050, p. 14) says Steinig's result is "even more general: it is shown that any n power sums of n distinct positive real numbers has at most one solution (up to permutation)".
- Laurens' self-contained proof of Lemma 3.2 (pp. 14–16) carries over verbatim to the exponents −1, 1, 3, …, 2n−3. There is one simplification: since both multisets have n elements, no zero-padding is needed, so the negative exponent causes no problem. The reasoning is in §3, and the supporting checks are in `check_mueller.py` §4.
- Hence the positive-real case of Theorem A is classical in substance. Whether Steinig's paper literally covers negative exponents is unverified, because Steinig 1971 is a standing gap.
- Theorem A's genuinely new content is:
  - the **complex** case with the sharp Orlando condition ∏(m_i+m_j) ≠ 0;
  - the explicit linear system and determinant (Theorem B);
  - the fibre and sharpness analysis (Theorem C).
- Theorem B's linear system is the tanh/arth identity of Korobov–Bugaevskaya (Math. Comp. 85 (2016), §3) with R in place of the top odd power sum. Korobov–Bugaevskaya should be cited for it.

**(ii) Proposed wording:** see §5.

## 1. Müller et al.: verbatim statements

Source: arXiv:1311.5493v2 (`../sources/mueller_1311.5493.txt`). The FoCM version could not be fetched (fetches.md, gap 1).

- **Definition 1.1** (p. 2): "Let A = (aij) ∈ R^{m×r}, B = (bij) ∈ R^{r×n}, and κ ∈ R^r_+. We define the associated generalized polynomial map fκ: R^n_+ → R^m as fκ,i(x) = Σ_j aij κj x1^{bj1} ··· xn^{bjn}".
- **Definition 1.2** (p. 2): "Given two subsets Ω, S ⊆ R^n, a function g defined on Ω is called injective with respect to S if x, y ∈ Ω, x ≠ y, and x − y ∈ S imply g(x) ≠ g(y)."
- **Theorem 1.4** (p. 3): "Let fκ : R^n_+ → R^m be the generalized polynomial map fκ(x) = Aκ x^B … The following statements are equivalent: (inj) fκ is injective with respect to S, for all κ ∈ R^r_+. (jac) ker(Jfκ(x)) ∩ S* = ∅, for all κ ∈ R^r_+ and x ∈ R^n_+. (lin) … (sig) σ(ker(A)) ∩ σ(B(Σ(S*))) = ∅."
- **Corollary 2.8** (p. 10): "(i) fκ is injective, for all κ ∈ R^r_+. (ii) ker(B) = {0} and σ(ker(A)) ∩ σ(im(B)) = {0}."
- **Theorem 1.5 (bnd)** (p. 6): "Assume that for all index sets J ⊆ [r] of cardinality n, the product det(A[n],J) det(BJ,[n]) either is zero or has the same sign as all other nonzero products, and moreover, at least one such product is nonzero. Then, (3) has at most one positive solution x ∈ R^n_+, for any y ∈ R^n."
- **Proposition 3.12** (p. 19) shows that (bnd) is the κ = (1,…,1) case of the all-κ criterion: "statement (i) is equivalent to the injectivity of fκ for all κ ∈ R^r_+."

Every result is therefore an all-κ, full-orthant statement. The κ = 1 case of Theorem 1.5 inherits the all-κ sign hypothesis.

## 2. Exact checks

`check_mueller.py` uses sympy and exact Fractions. Its output is in `check_mueller.out`. It exits 0, and every check is an assert.

1. **Direct encoding.**
   - Set-up: variables m_1..m_n; r = n² monomials m_i^e with e ∈ {−1,1,…,2n−3}. A is n×r with A_{e,(i,e)} = 1. B is r×n with row e·u_i.
   - For n = 2..6, rank B = n, and w = B(1,−1,0,…) is nonzero with Aw = 0, so Corollary 2.8(ii) fails.
   - The (bnd) products take both signs for n = 2,3,4.
   - At κ = 1 the swap of two coordinates is a non-injectivity witness.
2. **e-encoding.**
   - Set-up: Φ(e) = (e_{n−1}e_n^{−1}, P_1(e), P_3(e), …), with P_k from the Newton identities. There are r = 5, 11, 25, 52 monomials for n = 3..6, and A has coefficients of both signs.
   - Non-injectivity on R^n_+, exactly. Let e(b) be the elementary symmetric functions of {ib, −ib, 2, …, n−1}. These are positive for b = 1, 2, 1/3 and give the same Φ. Examples:
     - n = 3: e = (2,1,2) and (2,4,8);
     - n = 4: (5,7,5,6) and (5,10,20,24).
   - The Jacobian at e(1) annihilates de/db, so (jac) fails at κ = 1.
3. **Restricted injectivity.** For 1500 sampled d ≠ 0, x = 3T(1,10,100,…) with T = 1 + Σ|d_i| and y = x − d gives a positive, non-permutation pair. Hence S ⊇ Rⁿ \ {0}.
4. **Steinig/Laurens route.** All square minors of K(s)_k = a_k s^{a_k−1}, with a = (−1,1,3,…,2n−3), are nonzero and of constant sign at sampled ordered positive rational points (n ≤ 6). The run-count bound (at most n sign intervals of φ) holds exhaustively for all pairs of n-multisets from {1..6}, n ≤ 5.
5. **Consistency.** I_3 is injective on the 11,480 multisets from {1..40}, and I_4 on the 12,650 from {1..22}.

## 3. Odd power sums and the Steinig argument

- **MathOverflow 410757** (Stack Exchange API, `search/mo_*.json`).
  - The question asks whether p_3, p_5, …, p_{2n+1} determine n positive reals.
  - The accepted answer (Jaume) says this "is precisely the content of [1]", where [1] is "J. Steinig, On some rules of Laguerre's, and systems of equal sums of like powers. Rend. Mat. (6) 4 (1971), 629–644". It also says the proof idea is in Drury–Marshall 1987, §3: "The key idea is using that the Jacobian matrix is a strictly totally positive matrix".
- **Laurens**, arXiv:2206.09050.
  - Lemma 3.2 (p. 14): "Given constraints e1, . . . , en, there is at most one choice of N ≤ n and β1 > · · · > βN > 0 so that Em(Qβ,c) = em for m = 1,…,n". The constraints are odd power sums with exponents 3, 5, …, 2n+1.
  - Also p. 14: "We will follow the clever argument from [34] … In fact, the result in [34] is even more general: it is shown that any n power sums of n distinct positive real numbers has at most one solution (up to permutation)". Here [34] = Steinig 1971.
  - Proof (pp. 14–16):
    1. summation by parts to "0 = ∫ φ(s) f′(s) ds" with a step function φ;
    2. "at most n such intervals";
    3. strict total positivity of the kernel, with nonvanishing proved by a Rolle induction on Σ λ_j x^{2k_j}.
  - Corollary 3.3 (p. 16) allows repeated values.
- **Transfer to Theorem A** (my reasoning). Take f(x) = (x^{−1}, x, x^3, …, x^{2n−3}) on (0, ∞).
  1. The two multisets have equal size n. After cancellation, Σ ε_j = 0, so the partial sums end at 0 and no zero is appended. The integral therefore lives on [β_M, β_1] ⊂ (0,∞), where x^{−1} is smooth.
  2. The number of sign intervals is at most n. A merged partial-sum path is a subsequence of a ±1 path of length 2n from 0 to 0.
  3. The m×m minors of ∫_{I_j}|φ| a_k s^{a_k−1} ds equal ∫ (positive weight) × ∏_{k∈K} a_k × det[s_i^{a_k−1}]. The generalised Vandermonde factor is nonzero, by Rolle's induction, which works verbatim for distinct real exponents a_k − 1 ∈ {−2, 0, 2, …, 2n−4}. It has constant sign on the connected set of ordered tuples. Column factors a_k ≠ 0 only fix a sign.
  4. So the rows are independent, contradicting Σ_j ±row_j = 0 unless φ ≡ 0, i.e. m = m′.

  This proves the positive-real case of Theorem A, with repeated orders allowed.
- **Melánová–Sturmfels–Winter**, arXiv:2106.13981, Proposition 24 (p. 12): "For m = n, recovery from p-norms is always unique. Given any set A of n positive integers, the map φA,≥0 : R^n_≥0 → R^n_≥0 is injective up to permuting coordinates."
  - This covers only **positive integer** exponents, so it gives odd power sums {1,3,…,2n−1} but not exponent −1.
  - Referee caution: the written proof asserts "the coordinates of the vector Jφ·(X2 − X1) do not vanish at any point on L \ {X1}" from the nonvanishing of the Jacobian determinant. That inference is not justified as written. Cite Steinig/Laurens for the argument, not MSW.
- **Korobov–Bugaevskaya**, Math. Comp. 85 (2016) 717–736, §3 "Power sum systems with even gaps" (p. 724):
  > "(3.1) Σ arth(Ti/z) = Σ S2k−1/((2k − 1) z^{2k−1})"

  They define R_1, R_2 as the ratio of the odd and even parts of ∏(z + T_i) and derive linear equations (3.5)/(3.10) for σ_1, …, σ_n in terms of γ_{2k−1}(S_1, …, S_{2k−1}). Theorem 3.1 (p. 727): "The equality (3.5) for even n and the equality (3.10) for odd n express the connection between elementary symmetric functions σ1,...,σn and odd power sums S1,...,S2n−1".

  On uniqueness, p. 718 says: "the system (1.8) may have a unique solution (up to permutation of the variable), as well as an infinite number of solutions, and a solution may not exist at all". Solvability needs a nonvanishing Hankel determinant.

  This is the same tanh generating function as Theorem B's T(z) = tanh(Σ_odd P_k z^k/k). Theorem B replaces the last odd power sum by R, i.e. by e_{n−1} = R e_n, and computes the determinant (Orlando factor). **Cite KB as prior art for the odd-power-sum Newton analogue.** They prove no injectivity theorem on positive reals.

## 4. Search log

- **arXiv full text:** "Steinig odd power sums" (hit: Laurens), "recovery from power sums" (MSW), "odd power sums determine positive reals" (nothing relevant).
- **Crossref:** Korobov–Bugaevskaya (DOI 10.1090/mcom/2994); Steinig (no DOI for the 1971 paper); 1311.5493 (FoCM DOI 10.1007/s10208-014-9239-3). Crossref also surfaced Thomas–Tung, ECA 7 (2027), "Injectivity of symmetric polynomial maps on partitions". It concerns elementary/Schur partition functions on integer partitions and is not relevant.
- **zbMATH:** Steinig 0238.10007 (no review text); "power sums recovery", "injectivity power sums positive" (nothing relevant). Conca–Singh–Soundararajan (regular sequences of power sums) is not relevant.
- **Stack Exchange API:** MathOverflow 410757.

## 5. Proposed manuscript wording (prior-art sentence for Theorem A)

> For positive reals, the injectivity part of Theorem A is classical in substance. That any n power sums with distinct exponents determine an n-multiset of positive reals goes back to Steinig [Rend. Mat. (6) 4 (1971) 629–644], as reported and reproved in [Laurens, arXiv:2206.09050, Lemma 3.2 and the remark preceding it] (see also [Melánová–Sturmfels–Winter, Prop. 24] for positive integer exponents). Laurens' total-positivity argument applies verbatim to the exponents −1, 1, 3, …, 2n−3, because the two multisets have the same cardinality. The linear system of Theorem B is the odd-power-sum analogue of Newton's identities of [Korobov–Bugaevskaya, Math. Comp. 85 (2016), §3, Thm 3.1], with the reciprocal sum R in place of the top power sum. What is new here is the complex case under the sharp condition ∏_{i<j}(m_i + m_j) ≠ 0, the closed form of the determinant, and the sharpness statements of Theorem C.

Do **not** cite Müller et al. (FoCM 2016) as giving Theorem A. If it is mentioned at all, it should be as follows:

> Sign-vector injectivity criteria for generalized polynomial maps [Müller et al., Found. Comput. Math. 16 (2016), Thm 1.4] concern injectivity on the whole positive orthant for all coefficient scalings, and so do not apply to the permutation-invariant map I_n.

Citations:
- Steinig, J., On some rules of Laguerre's, and systems of equal sums of like powers, Rend. Mat. (6) 4 (1971), 629–644 (Zbl 0238.10007).
- Laurens, T., Multisolitons are the unique constrained minimizers of the KdV conserved quantities, arXiv:2206.09050.
- Melánová, H., Sturmfels, B., Winter, R., Recovery from power sums, arXiv:2106.13981.
- Korobov, V. I., Bugaevskaya, A. N., Almost power sum systems, Math. Comp. 85 (2016), 717–736.
