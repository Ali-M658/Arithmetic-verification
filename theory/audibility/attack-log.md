# Adversarial review (T5)

## Protocol

A separate reviewer was given only a file containing the theorem statements and proofs:
proof.md §§1–4, up to but not including the integer-record table.

- **No other inputs.** The reviewer did not see the scripts, the data, the repository or any
  earlier reasoning.
- **Instructions.** Assume the author is wrong. Check every step line by line. Run independent
  exact and numeric counterexample searches with its own code in an isolated scratch directory.
- **Grading.** Mark each finding FATAL, SERIOUS, MINOR or NONE.

## Findings and responses

The reviewer reported **no fatal or serious error**. It found no counterexample to Theorem A,
Theorem B or Theorem C(1).

| # | severity | finding | response |
|---|---|---|---|
| 1 | MINOR | C(2): "the fibre through $m$ is then a smooth curve" stated twice | **Fixed.** The duplicate is replaced by the reason nearby fibre points are not permutations of $m$ (a permutation is at least the minimum gap away). |
| 2 | MINOR | $\mathcal I_0$ notation ambiguous for $n=1$ | **No change.** Read literally, $\mathcal I_{n-1}=(R)$ for $n=2$ and is vacuous at $n=1$; C(1) and C(2) are stated for $n\ge2$. |
| 3 | MINOR | $\kappa$ used both for the curvature and for the $z^3$ coefficient | **Fixed.** The curvature is now $K$ ($=-1$) in §1. |
| 4 | MINOR | C(3): "off the diagonal" should mean $m'\neq m$ as multisets, since every permutation component is trivially off the diagonal | **Fixed.** C(3) now says "a positive rational pair $m\neq m'$ (as multisets), i.e. a point off all permutation components". |
| 5 | MINOR | C(3): the scaling argument for hyperbolicity needs $n\ge3$, so that $n-2>0$ | **Fixed.** $n\ge3$ is now stated, being the range where hyperbolic genus-0 orbifolds exist. |
| 6 | MINOR | the sign of $c_n$ in Remark 2 depends on the Vandermonde convention | **Fixed.** $V(m)=\prod_{i<j}(m_j-m_i)$ is now stated. |
| 7 | NONE | no counterexample to A, B or C(1) | — |

The reviewer also noted three gaps in exposition. None is an error.

- **The "same ideal" converse in §3 is only sketched.** The reviewer supplied the missing
  argument: $zO_e-TE_e=E_e(T^{e}-T^{\rm data})$, $E_e$ is a unit, and the coefficients of
  $\tanh(S^e)-\tanh(S^{\rm data})$ are triangular in the differences. *Response:* this converse
  is not used by Theorems A or B. It only explains why the naive eliminations collapse, so the
  sketch stands.
- **$c_n\in\mathbb Q$ is not argued.** *Response:* it follows by evaluating at a rational point,
  and the values are computed exactly for $n\le8$.
- **Orlando's formula is taken from [HT].** *Response:* the proofs of Theorems A and B do not
  need it. They use $m_i+m_j\neq0$ directly, and Orlando only identifies that condition with
  $\Delta_{n-1}\neq0$. It is verified symbolically in `orlando_check.py` and
  `verify_elimination.py` (degrees 2..8 in decay-rate form).

## The reviewer's independent computations

The reviewer's own code is not committed; it is summarised here.

**Theorem B.** The reviewer built $M$ exactly for $n=2..6$, using random rational multisets
that included negative entries.

- $\det M\big/\bigl(\prod(m_i+m_j)/\prod m_i\bigr)$ was constant: $-1,+1,+1,-1,-1$ for
  $n=2..6$. This agrees with $c_3,\dots,c_6$ from `linear_system.py`.
- With a $\pm a$ pair inserted, $\det M=0$, as Step 2 says.

**Theorem A.** The reviewer used lex Gröbner bases over $\mathbb Q$ for the full polynomial
system in unknown $e'$. The test multisets were:

- $n=2$: $\{2,3\}$ and $\{2,2\}$.
- $n=3$: $\{3,3,3\}$, $\{2,2,5\}$, $\{2,3,7\}$, and the complex $\{1+i,2,-3\}$.
- $n=4$: $\{1,2,3,4\}$, $\{2,2,3,3\}$, $\{5,5,5,5\}$, and $\{1/2,-1/3,7,7\}$.
- $n=5$: $\{2,3,4,5,6\}$, $\{2,2,2,3,3\}$ and $\{1,1,1,1,1\}$.

In every case the basis is linear with a single solution, the true one. There are no spurious
solutions, including none with $e'_n=0$. Repeated orders behave as Theorem A predicts.

**Exhaustive $\mathcal I_n$ collision search.** No collision for $n=3$ with orders $1..80$, or
for $n=4$ with orders $1..45$.

**Theorem C(1), both directions.**

- Converse: 24 random complex $Q=$ even polynomial $+\kappa z^3$ for $n=2..5$. Splitting the
  roots at random into $m$ and $-m'$ gave equal $\mathcal I_{n-1}$ to 50 digits, and different
  $P_{2n-3}$.
- Forward: 20 integer pairs for $n=3$, all with $Q(z)-Q(-z)$ a pure $z^3$ term.

**Integer sharpness.**

- For $n=5$, the reviewer independently found no witness among the 7,028,847 multisets with
  orders $\le60$, in agreement with `sharpness_search.py`.
- The reviewer reports 11 witnesses for $n=4$ with orders $\le90$, including the known pair.
  The review appendix found the known pair unique with orders $\le55$. *Response:* I have not
  independently re-run an $n=4$ scan beyond the two known pairs, so this count is recorded as
  reviewer-reported only. It is consistent with integer sharpness holding at $n=4$, which is
  already established by the explicit pair.

## Outcome

The proofs of Theorems A, B and C(1)–(2) survived the attack unchanged in substance. The six
minor findings are resolved as above. STATUS.md's verdict, PROVED FOR ALL $n$, stands.
