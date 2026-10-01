# P7. Theorem A prior art: decision and manuscript wording

Evidence, verbatim quotes, exact checks and search log are in
`literature/THEOREM-A-PRIOR-ART-notes.md`, `literature/check_mueller.py` (output
`literature/check_mueller.txt`) and `literature/fetches.md`.

Theorem A (`theory/audibility`): $m\mapsto(R,P_1,P_3,\dots,P_{2n-3})$, $R=\sum1/m_i$, $P_k=\sum m_i^k$,
is injective on $n$-multisets of nonzero complex numbers with $m_i+m_j\ne0$, in particular on
positive reals.

## Verdict on arXiv:1311.5493 (Müller–Feliu–Regensburger–Conradi–Shiu–Dickenstein, Found. Comput. Math. 16 (2016))

**NO. It does not give the positive-real case of Theorem A, even partially.**

- Every result there (Def. 1.1–1.2, Thm 1.4, Cor. 2.8, Thm 1.5 (bnd), Prop. 3.12) concerns
  injectivity of the whole family $f_\kappa(x)=A\,\mathrm{diag}(\kappa)\,x^B$ for **all**
  $\kappa\in\mathbb R^r_{>0}$ on the **full** open orthant, possibly with respect to a set $S$ of
  differences.
- Theorem A's map is permutation-invariant, so it is not injective on ordered tuples. Encoded
  directly, the criterion fails, as it must (explicit $0\ne w=Bv\in\ker A$ for $n=2,\dots,6$; the
  (bnd) minor products take both signs for $n=2,3,4$).
- Injectivity modulo permutation cannot be encoded through their restricted injectivity: every
  nonzero difference vector arises from a non-permutation pair, so $S$ would be all of
  $\mathbb R^n\setminus\{0\}$. The ordered chamber is not the image of an orthant under a monomial
  change of variables.
- Rewritten in the elementary symmetric functions, the map is not injective on the positive
  $e$-orthant (exact witness, $n=3$: $e=(2,1,2)$ and $(2,4,8)$ give the same $(R,P_1,P_3)$), so no
  full-orthant theorem can yield Theorem A.
- The paper contains no power-sum or symmetric-map example. The only link in the literature is a
  pointer from Melánová–Sturmfels–Winter to its Thm 1.4 as "a much more general version of this
  argument", i.e. an analogy for a Jacobian argument, not an application.

The published FoCM version is closed access (instrument gap); arXiv v2 was used.

## The actual prior art

- **Positive reals.** Steinig, *Rend. Mat.* (6) 4 (1971) 629–644 (Zbl 0238.10007), as reported and
  reproved by Laurens, arXiv:2206.09050, Lemma 3.2 and the remark before it (p. 14): "any $n$ power
  sums of $n$ distinct positive real numbers has at most one solution (up to permutation)". Laurens'
  total-positivity argument carries over verbatim to the exponents $-1,1,3,\dots,2n-3$ (equal
  cardinalities, so no zero-padding is needed); the key minors were checked exactly. Steinig 1971
  is an accepted standing gap, so whether it literally covers a negative exponent is unverified;
  cite it through Laurens. Melánová–Sturmfels–Winter, arXiv:2106.13981, Prop. 24, covers positive
  integer exponents only, and its written proof has an unjustified step; do not rely on it for the
  argument.
- **Theorem B.** The linear system is the odd-power-sum analogue of Newton's identities of
  Korobov–Bugaevskaya, *Math. Comp.* 85 (2016) 717–736, §3, Thm 3.1 (the $\operatorname{arth}/\tanh$
  generating function), with $R$ in place of the top odd power sum. They prove no injectivity
  statement on positive reals.

**New in the manuscript:** the complex case under the sharp condition $\prod_{i<j}(m_i+m_j)\ne0$,
the closed form of $\det M$ (with $c_n=(-1)^{n(n+1)/2}$ from the stability work), and Theorem C.

## Proposed manuscript wording

> For positive reals the injectivity in Theorem~A is classical in substance: that $n$ power sums
> with distinct exponents determine an $n$-multiset of positive reals goes back to
> Steinig~\cite{steinig1971}, as reported and reproved in \cite[Lemma~3.2]{laurens2022} (see also
> \cite[Prop.~24]{msw2022} for positive integer exponents), and that total-positivity argument applies
> verbatim to the exponents $-1,1,3,\dots,2n-3$. The linear system of Theorem~B is the
> odd-power-sum analogue of Newton's identities of \cite[§3, Thm~3.1]{korobovbugaevskaya2016}, with
> the reciprocal sum $R$ in place of the top power sum. What is new here is the complex case under the
> sharp condition $\prod_{i<j}(m_i+m_j)\ne0$, the closed form of the determinant, and the sharpness
> statements of Theorem~C.

Do **not** cite Müller et al. as giving Theorem A. If it is mentioned at all:

> Sign-vector injectivity criteria for generalized polynomial maps \cite[Thm~1.4]{mueller2016}
> concern injectivity on the whole positive orthant for every coefficient scaling, and so do not
> apply to the permutation-invariant map $\mathcal I_n$.

Bibliography:
- J. Steinig, On some rules of Laguerre's, and systems of equal sums of like powers, Rend. Mat. (6) 4 (1971), 629–644.
- T. Laurens, Multisolitons are the unique constrained minimizers of the KdV conserved quantities, arXiv:2206.09050.
- H. Melánová, B. Sturmfels, R. Winter, Recovery from power sums, arXiv:2106.13981.
- V. I. Korobov, A. N. Bugaevskaya, Almost power sum systems, Math. Comp. 85 (2016), 717–736, DOI 10.1090/mcom/2994.
- S. Müller, E. Feliu, G. Regensburger, C. Conradi, A. Shiu, A. Dickenstein, Sign conditions for injectivity of generalized polynomial maps with applications to chemical reaction networks and real algebraic geometry, Found. Comput. Math. 16 (2016), 69–97, DOI 10.1007/s10208-014-9239-3.
