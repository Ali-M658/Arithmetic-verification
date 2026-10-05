# Novelty recalibration for the 30–35 page paper

These are the sentences the paper should use for "what is new", one block per main result. Each credits every prior
work found in this pass (CITATIONS.md, MISSING.md) and deliberately under-claims where there is doubt. Citation keys
in `\cite{...}` are those of `paper/jga/references.bib` plus `references-additions.bib`.

Rules applied:
- "To our knowledge" appears only where the systematic sweep (work/E-forward-sweep.md) found nothing. That
  happened for three things: the uniform count, the heat-invariant threshold, and stability for cone orders.
- Every "first" is restricted to heat invariants and to hyperbolic orbifolds. Finite-data rigidity of triangle groups
  on the length side is Philippe's, and finite counts for Euclidean triangles are Chang–DeTurck's and
  Grieser–Maronna's.
- Results whose mechanism is classical are stated as such, even when the statement is new.

## 0. Sentences to delete

| location | current text | why |
|---|---|---|
| §1.1, l. 174 | "To our knowledge this is the first exact finite-coefficient determinacy threshold, with an explicit minimal degeneracy, for a family of hyperbolic cone orbifolds; it answers the question left open in \cite[Rem.~5.16]{dggw2008}." | DGGW Rem. 5.16 poses no question (CITATIONS #2). "With an explicit minimal degeneracy" adds a second "first". Replaced by §2 below. |
| §1.1, l. 176 | "What is new here is the complex case under the sharp condition $\prod_{i<j}(m_i+m_j)\ne0$, the closed form of the determinant, and the sharpness statements of Theorem~\ref{thmC}." | the complex case is the classical ± pairs fact (Borwein–Ingalls Prop. 1). Replaced by §1(b). |
| §8.3, l. 1426 | "what is new is the normalization by rescaling to a common sum, which works because $\Lambda$ is scale-invariant" | it is Schinzel's step (p. 588). Replaced by §5. |
| abstract; Thm 1.2 as a headline theorem | "The coefficients carry no information about the shape: …" presented as a main theorem | classical in substance (McKean, Hejhal, Uçar Thm 4.20, Dryden 2004). Demote it to a cited proposition (G7-2). See §4. |
| abstract, Thm 1.4 | "both rates are sharp" | sharp for general data only (G7-7). See §3. |
| l. 405 | "The hypothesis is sharp over $\C$: …" | add "as in the classical case". |

## 1. Hearing the signature: the count, and no uniform count

**(a) Theorem 1.1(i)–(ii), for §1.1:**

> That the Laplace spectrum of a closed orientable hyperbolic $2$-orbifold determines its genus and its cone orders is due
> to Dryden and Strohmaier \cite[Thm~1.1, Prop.~3.3]{drydenstrohmaier2009}, after finiteness results of Stanhope
> \cite[Main Thms~1--2]{stanhope2005} and Dryden \cite[Thm~4.5]{dryden2004}; see also \cite[Thm~1]{doylerossetti2011}.
> U\c{c}ar recovered the cone orders from the whole sequence of heat invariants at any fixed nonzero curvature
> \cite[Cors~4.21(iv), 4.23]{ucar2017}, and for $\chi\ge0$ a single coefficient determines the orbifold type
> \cite[Thms~5.14--5.15]{dggw2008}. Theorem~\ref{thm:intro-signature} adds a count. To our knowledge,
> $\lfloor\Area/\pi\rfloor+4$ is the first explicit finite number of heat invariants shown to determine the genus and the
> cone-order multiset uniformly over all closed orientable hyperbolic $2$-orbifolds. Part~(ii) shows that the dependence
> on the area cannot be removed; its construction uses Prouhet's partition \cite[\S5.1, Thm~6]{alloucheshallit1999},
> \cite{borweiningalls1994}. A finite but likewise non-uniform count is known for Euclidean triangles and their Dirichlet
> eigenvalues \cite{changdeturck1989}.

**(b) Theorems A–C (n invariants for spheres with n cone points), replacing the paragraph at l. 176:**

> The mechanism of Theorem~\ref{thmA} is classical. By Newton's identities, two $n$-multisets of complex numbers have equal
> odd power sums $P_1,P_3,\dots,P_{2n-1}$ if and only if they agree after deleting pairs $\{a,-a\}$; this is the symmetric
> form of the Prouhet--Tarry--Escott problem \cite[Prop.~1 and \S3]{borweiningalls1994}. For positive reals, uniqueness of
> $n$ distinct numbers with $n$ prescribed power sums goes back to Steinig \cite{steinig1971}; see
> \cite[Lemma~3.2 and the remark following it]{laurens2023}, and \cite[Prop.~24]{msw2022} for positive integer exponents.
> Theorem~\ref{thmA} replaces the top odd power sum by the reciprocal sum $R$, which is the quantity the heat invariants
> supply; the condition $\prod_{i<j}(m_i+m_j)\ne0$ excludes pairs $\{a,-a\}$ in $m$. The linear system of
> Theorem~\ref{thmB} is the analogue, with $R$, of the odd-power-sum Newton identities of \cite[\S3]{korobovbugaevskaya2016}.
> What we add is the replacement of $P_{2n-1}$ by $R$, the closed form of $\det M$, whose zero set is the Orlando locus,
> and the sharpness statements of Theorem~\ref{thmC}.

Why this under-claims: it gives up "the complex case", which is classical, and the injectivity on positive reals,
which is Steinig's. The only claims left are the substitution of R, the determinant and Theorem C. No source found
covers any of the three. Problem 2 and Theorem C(1) should also cite Borwein–Ingalls as "odd symmetric" PTE systems.

## 2. The rigid threshold and the isolation of the minimal pair

**For §1.1, replacing the second half of the paragraph at l. 174:**

> Since $0<R<1$ for a hyperbolic triangle orbifold, the invariant $c$ of Dryden, Gordon, Greenwald and Webb, twelve
> times the $t^0$ coefficient, encodes exactly the first two heat invariants. They observe that $c$ ``does not seem
> sufficiently strong to distinguish among'' the triangular pillows with $\chi<0$, and note that the full spectrum
> determines the cone orders at curvature $-1$ \cite[Rem.~5.16]{dggw2008}. Theorem~\ref{thm:intro-rigid} makes this
> observation precise. The invariant $c$ separates the hyperbolic triangle orbifolds with $p+q+r\le17$ and first fails on
> $\Orb(2,8,8)$ and $\Orb(3,3,12)$, and the third heat invariant always separates them. To our knowledge this is the first
> sharp threshold for a finite number of heat invariants on a family of hyperbolic orbifolds. On the length side,
> Philippe showed that a hyperbolic triangle group is determined by its length spectrum, in practice by its first two or
> three lengths counted with multiplicity \cite[Thm~A]{philippe2008}, \cite{philippe2010gd}; for Euclidean triangles the
> first three heat invariants suffice \cite[Thm~1]{griesermaronna2013}.

**For §5.4, isolation (Theorem 5.16):**

> The degeneracies are positive rational points on the cubics $C_\Lambda$ of Bremner, Guy and Nowakowski \cite{bgn1993},
> and the minimal pair is a reciprocal pair in their sense \cite[p.~117 and the table in \S4]{bgn1993}, rescaled to a
> common sum. Its isolation is the statement that $C_{27/2}$ has rank $0$.

No novelty adjective is attached to the isolation. It is a rank computation, and the referees value it as a fact, not
as a method.

## 3. Stability

**For §1.1 or the opening of §6:**

> We know of no earlier quantitative stability estimate for recovering cone orders from heat invariants. For a sphere
> with a known number of cone points, the estimates of Section~\ref{sec:stability} combine the linear system of
> Theorem~\ref{thmB} with Ostrowski's root-perturbation bound \cite[Th\'eor\`eme~XXX]{ostrowski1940}. The loss of Lipschitz
> stability at a $k$-fold order, with H\"older exponent $1/k$, is the familiar behaviour of coalescing roots, and $1/k$ is
> sharp for general data. For data realised by real multisets at a triple order the exponent is $1/2$
> (Remark~\ref{rem:triple}). The rate is milder than in Prony-type moment problems with unknown amplitudes, where an
> $l$-node cluster costs the exponent $1/(2l-1)$ \cite{aby2015,bgy2020}, because here every weight equals $1$. The bounds
> concern errors in heat invariants, not in eigenvalues (Remark~\ref{rem:stabscope}).

**For the abstract and Theorem 1.4, replacing "both rates are sharp":**

> … Lipschitz at simple orders and H\"older of exponent $1/k$ at $k$-fold orders, the latter sharp for general data.

## 4. Locality, shortened (Theorem 1.2 becomes a cited proposition)

**For §1.1, or as the lead-in to the shortened §4:**

> That heat invariants do not hear the shape is classical in substance. Selberg's trace formula for cocompact Fuchsian
> groups with elliptic elements \cite[Ch.~3, Thm~5.1]{hejhal1976}, applied to the heat kernel
> \cite{mckean1972,mckean1974corr}, \cite[Rem.~2.7]{garbinjorgenson2020}, writes the heat trace of a closed hyperbolic
> $2$-orbifold as three terms: an area term, one term for each cone point depending only on its order, and a sum over closed
> geodesics of size $O(t^{-1/2}e^{-\ell^2/4t})$. In particular every heat invariant is a function of the signature, as
> also follows from \cite[Thm~4.20]{ucar2017} at curvature $-1$. For surfaces the mechanism goes back to Huber and McKean
> \cite{huber1959,mckean1972}, and for hyperbolic orbisurfaces Dryden already read the systole off the rate
> $e^{-\ell^2/4t}$ \cite[proof of Thm~4.5]{dryden2004}. We record three consequences. No finite number of heat invariants
> determines an orbifold with moduli within its signature. The difference of two heat traces of one signature is bounded
> explicitly, with a constant depending on the area, the systole and the diameter. The prefactor $t^{-1/2}$ is attained
> when the systoles differ.

**In Remark 4.13:** add Huber \cite[S\"atze~7--8]{huber1959} for surfaces, Wolpert \cite{wolpert1979} (the full spectrum
determines a generic surface), and the finiteness of isospectral sets for genus $\ge1$ \cite[Thm~5.1]{dryden2004},
\cite{mckean1972}. Frame the countability argument as a weak orbifold substitute for Wolpert's theorem.

**In the abstract, replacing the shape sentence:**

> As for surfaces, the heat invariants depend only on the signature; the moduli enter the heat trace at order
> $t^{-1/2}e^{-\ell^2/4t}$, and we bound this term explicitly.

## 5. Theorem 8.9, if §8 stays in this paper or moves to the arithmetic note

> The argument is Schinzel's \cite[p.~588]{schinzel1996}, transplanted from the equal-sum, equal-product problem to the
> curves $C_\Lambda$: put infinitely many positive rational points on one curve and rescale $k$ of them to a common sum.
> For equal sums and products, classes of every size were obtained earlier by Kelly \cite{kelly1989} and, for
> $n$-tuples, by Zhang and Cai \cite{zhangcai2013}. Schinzel's curve is a fibre of the invariant $(x+y+z)^3/xyz$ of
> Bremner and Guy \cite{bremnerguy1997}, just as $C_\Lambda$ is a fibre of $\Lambda=e_1e_2/e_3$.

Remark 8.6 should add: "the same holds on the equal-sum, equal-product curves \cite[Thm~2.8]{sadekelsissi2015}".

## 6. Headline for the abstract or cover letter, with every claim qualified

> We give an explicit number of heat invariants, $\lfloor\mathrm{Area}/\pi\rfloor+4$, that determines the genus and cone
> orders of every closed orientable hyperbolic 2-orbifold, and show that no area-independent number exists. For the rigid
> triangle orbifolds we find the exact threshold at which two invariants stop sufficing, sum 17, together with its minimal,
> isolated failure, and we prove stability estimates for recovering the cone orders from approximate invariants.
