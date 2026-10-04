# G5 theorem register

One row per result. Statement text is verbatim from the source file (same anchored line
ranges as `STATEMENTS.md`, produced by `build_register.py`). Status vocabulary: PROVED /
PROVED GIVEN CITED INPUT / COMPUTATION / CONJECTURE / OPEN; CLAIM (FALSE) marks a sentence
that is refuted. Audit verdict is the worst grade the independent reviewer assigned
(FATAL / SERIOUS / MINOR / NONE), after the comparison phase. 'In paper' says whether the
result should appear: YES, YES REVISED (with the change in the note), REMARK ONLY, CITE AS
PRIOR WORK, or NO.

Audit evidence: `review/audit/<folder>/REVIEW.md`, `COMPARISON.md` and `check_*.py`.

## Summary

| # | result | status | audit verdict | in paper? | source |
|---|---|---|---|---|---|
| 1 | lem:cot | PROVED | NONE | YES | `paper/main.tex` |
| 2 | prop:csc | PROVED | NONE | YES | `paper/main.tex` |
| 3 | def:cone, cor:conevals | PROVED GIVEN CITED INPUT | NONE | YES | `paper/main.tex` |
| 4 | eq:a0conv, eq:s1inv, rem:bugfix | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `paper/main.tex` |
| 5 | Heat expansion structure (sec:heatexp) | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `paper/main.tex` |
| 6 | eq:b1, eq:a2red | PROVED GIVEN CITED INPUT | NONE | YES | `paper/main.tex` |
| 7 | prop:cs | PROVED | NONE | YES | `paper/main.tex` |
| 8 | prop:recovery | PROVED GIVEN CITED INPUT | NONE | YES | `paper/main.tex` |
| 9 | Jacobian of (S1,R,P3) | PROVED | NONE | YES | `paper/main.tex` |
| 10 | lem:chamber | PROVED | MINOR | YES, REVISED | `paper/main.tex` |
| 11 | lem:bound and the R^+ formula | PROVED | MINOR | YES, REVISED | `paper/main.tex` |
| 12 | prop:min | PROVED | NONE | YES | `paper/main.tex` |
| 13 | thm:separation | PROVED | NONE | YES | `paper/main.tex` |
| 14 | thmA | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `paper/main.tex` |
| 15 | thmB | PROVED GIVEN CITED INPUT | NONE | YES | `paper/main.tex` |
| 16 | thmC | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `paper/main.tex` |
| 17 | corD | PROVED GIVEN CITED INPUT | NONE | YES | `paper/main.tex` |
| 18 | remark* on a_0 | PROVED | NONE | YES | `paper/main.tex` |
| 19 | prop:scaling | PROVED | NONE | YES | `paper/main.tex` |
| 20 | Degeneracy localization to adjacent strata (sentence before prop:scaling; repeated in sec:density) | CLAIM (FALSE) | SERIOUS | NO | `paper/main.tex` |
| 21 | thm:density-lower | PROVED | NONE | YES, REVISED | `paper/main.tex` |
| 22 | Primitive pair at S=36 | COMPUTATION | NONE | YES | `paper/main.tex` |
| 23 | tab:density and fitted exponent | COMPUTATION | SERIOUS | YES, REVISED | `paper/main.tex` |
| 24 | conj:density | CONJECTURE | SERIOUS | NO | `paper/main.tex` |
| 25 | rem:ncone | CLAIM (FALSE) | SERIOUS | NO | `paper/main.tex` |
| 26 | tab:enum | COMPUTATION | NONE | YES | `paper/main.tex` |
| 27 | prop:rigidity | PROVED GIVEN CITED INPUT | NONE | YES | `theory/definitions.tex` |
| 28 | eq:moduli | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/definitions.tex` |
| 29 | thm:locality, prop:Kinf | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/definitions.tex` |
| 30 | thm:Crestated | PROVED GIVEN CITED INPUT | NONE | YES | `theory/definitions.tex` |
| 31 | rem:nconerestated | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/definitions.tex` |
| 32 | Heat input (cone polynomials p_l) | PROVED GIVEN CITED INPUT | MINOR | YES | `theory/audibility/proof.md` |
| 33 | Theorem A (audibility of the cone orders) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/audibility/proof.md` |
| 34 | Theorem B (linear system, det M) | PROVED | MINOR | YES, REVISED | `theory/audibility/proof.md` |
| 35 | Theorem C(1)-(2) (pair criterion; real sharpness) | PROVED | NONE | YES | `theory/audibility/proof.md` |
| 36 | Theorem C(3) (integer sharpness) | COMPUTATION | NONE | YES | `theory/audibility/proof.md` |
| 37 | Integer sharpness K_mult >= n for n >= 5 | OPEN | NONE | YES | `theory/audibility/proof.md` |
| 38 | Lemma 1 (parity) | PROVED | NONE | YES | `theory/audibility/proof.md` |
| 39 | Remark 2 (Jacobian), Remark 3 (padding) | PROVED | MINOR | YES, REVISED | `theory/audibility/proof.md` |
| 40 | Heat input (H1)-(H3) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/signatures/proof.md` |
| 41 | Lemma 1 (cone polynomials) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/signatures/proof.md` |
| 42 | Lemma 2 (triangular basis) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/signatures/proof.md` |
| 43 | Lemma 3 (padding) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/signatures/proof.md` |
| 44 | Lemma 4 (reduction) / lem:sigdata | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| 45 | Theorem S / thm:sigsep | PROVED GIVEN CITED INPUT | NONE | YES | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| 46 | Corollary S1 | PROVED GIVEN CITED INPUT | NONE | YES | `theory/signatures/proof.md` |
| 47 | Corollary S2 / cor:sigarea | PROVED GIVEN CITED INPUT | NONE | YES | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| 48 | Theorem T1 / thm:sigcount | PROVED GIVEN CITED INPUT | NONE | YES | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| 49 | Proposition P (Prouhet) | PROVED | NONE | YES | `theory/signatures/proof.md` |
| 50 | Theorem N / thm:signonuniform | PROVED GIVEN CITED INPUT | NONE | YES | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| 51 | Construction ranges remark | COMPUTATION | MINOR | YES, REVISED | `theory/signatures/proof.md` |
| 52 | Corollary N1 / cor:siggrowth | PROVED GIVEN CITED INPUT | NONE | YES | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| 53 | Growth of f(A) (linear?) and T_L | OPEN | NONE | YES | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| 54 | ex:siggenus | COMPUTATION | NONE | YES | `theory/signatures/statements.tex` |
| 55 | Theorem 1 (signature locality) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/locality/proof.md` |
| 56 | Proposition 2.1 (dim T = 6g-6+2n) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/locality/proof.md` |
| 57 | Proposition 2.2 (uncountably many isometry classes) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/locality/proof.md` |
| 58 | Corollary 2.3 (K_iso = infinity) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/locality/proof.md` |
| 59 | Theorem 3.1 (I+E+H decomposition) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/locality/proof.md` |
| 60 | Lemma 3.2 (admissibility of the heat function) | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/locality/proof.md` |
| 61 | Lemma 3.3 (counting closed geodesics) | PROVED | NONE | YES | `theory/locality/proof.md` |
| 62 | Theorem 3.4 (quantitative locality) | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/locality/proof.md` |
| 63 | t^{-1/2} prefactor cannot be dropped | PROVED | MINOR | YES, REVISED | `theory/locality/proof.md` |
| 64 | Theorem 3.5 (sharp asymptotics) | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/locality/proof.md` |
| 65 | Proposition S1 (front end) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/stability/proof.md` |
| 66 | Lemma S2.1 (c_n for all n) | PROVED | NONE | YES | `theory/stability/proof.md` |
| 67 | Lemma S2.2 (Hurwitz factorisation) | PROVED | NONE | YES | `theory/stability/proof.md` |
| 68 | Theorem S2 (Lipschitz, explicit constants) | PROVED | NONE | YES | `theory/stability/proof.md` |
| 69 | Ostrowski input | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/stability/proof.md` |
| 70 | Lemma S3 (explicit Rouché) | PROVED | NONE | YES | `theory/stability/proof.md` |
| 71 | Theorem S3 (combined stability) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/stability/proof.md` |
| 72 | Proposition S3.2 (exponent 1/k sharp) | PROVED | MINOR | YES, REVISED | `theory/stability/proof.md` |
| 73 | Remark S3.3 | PROVED | NONE | YES | `theory/stability/proof.md` |
| 74 | Theorem S4 (explicit threshold) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/stability/proof.md` |
| 75 | Proposition S5 (certificates) | PROVED | MINOR | YES, REVISED | `theory/stability/proof.md` |
| 76 | Results table (delta_thm, delta_cert, delta_up) | COMPUTATION | MINOR | YES, REVISED | `theory/stability/proof.md` |
| 77 | Lemmas 1-2 (one inequality; adjacent separation) | PROVED | NONE | YES | `theory/threshold/proof.md` |
| 78 | Theorem 1 (closed form S*(p)) | PROVED | NONE | YES | `theory/threshold/proof.md` |
| 79 | Corollary 2 (no collision below 18) | PROVED | NONE | YES | `theory/threshold/proof.md` |
| 80 | First-overlap vs first-collision table | COMPUTATION | NONE | YES | `theory/threshold/proof.md` |
| 81 | Proposition 3 (tangency only at p=2,4) | PROVED | MINOR | YES, REVISED | `theory/threshold/proof.md` |
| 82 | Flat-cone input (Kokotov) | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/curvature/proof.md` |
| 83 | Lemma 2 (invariant multiplicities) | PROVED | MINOR | REMARK ONLY | `theory/curvature/proof.md` |
| 84 | Proposition (curvature comparison), Parts 1-2 | PROVED GIVEN CITED INPUT | MINOR | CITE AS PRIOR WORK | `theory/curvature/proof.md` |
| 85 | Proposition (curvature comparison), Part 3 | PROVED GIVEN CITED INPUT | NONE | YES | `theory/curvature/proof.md` |
| 86 | Proposition (curvature comparison), Part 4 | PROVED GIVEN CITED INPUT | MINOR | REMARK ONLY | `theory/curvature/proof.md` |
| 87 | Lemma 1 (generating function, positivity, poles) | PROVED GIVEN CITED INPUT | NONE | REMARK ONLY | `theory/divergence/proof.md` |
| 88 | Theorem 2 (asymptotics of b_l(m)) | PROVED GIVEN CITED INPUT | MINOR | REMARK ONLY | `theory/divergence/proof.md` |
| 89 | Theorem 3 (divergence rate hears M) | PROVED GIVEN CITED INPUT | MINOR | REMARK ONLY | `theory/divergence/proof.md` |
| 90 | Corollary 4 (peeling) | PROVED GIVEN CITED INPUT | MINOR | REMARK ONLY | `theory/divergence/proof.md` |
| 91 | Borel reading | PROVED GIVEN CITED INPUT | MINOR | REMARK ONLY | `theory/divergence/proof.md` |
| 92 | Proposition 1 (reformulation on C_lambda) | PROVED | MINOR | YES, REVISED | `theory/diophantine/variety.md` |
| 93 | Pencil, Weierstrass model, fibres, generic torsion | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/diophantine/variety.md` |
| 94 | Reciprocation = 2-torsion translation; dual family | PROVED | MINOR | YES, REVISED | `theory/diophantine/variety.md` |
| 95 | Proposition 2 (no linear families) | PROVED | MINOR | REMARK ONLY | `theory/diophantine/variety.md` |
| 96 | Theorem 3 (arbitrarily large fibres) | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/diophantine/variety.md` |
| 97 | Rank certification of fibre curves | COMPUTATION | NONE | YES | `theory/diophantine/RECOMMENDATION.md`, `theory/diophantine/variety.md` |
| 98 | Isolation of the base pair (rank C_{27/2} = 0) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/diophantine/variety.md` |
| 99 | Hyperbolicity of copies kD, k>=4 | PROVED | MINOR | YES | `theory/diophantine/variety.md` |
| 100 | Theorem 4 (c_iso X log X) | PROVED | NONE | YES | `theory/diophantine/variety.md` |
| 101 | Theorem 5 (X (log X)^2) | PROVED | NONE | YES | `theory/diophantine/variety.md` |
| 102 | First fibres of each size (S=136, 408, 1849, 4600) | COMPUTATION | SERIOUS | YES, REVISED | `theory/diophantine/RECOMMENDATION.md` |

**Counts by status:** CLAIM (FALSE): 2; COMPUTATION: 10; CONJECTURE: 1; OPEN: 2; PROVED: 36; PROVED GIVEN CITED INPUT: 51; total 102.

Multi-result excerpts (e.g. PC.1 for thmA-corD, AU.1 for Theorems A-C, CU.3 for Parts 1-4) are repeated under each row they support.

## Rows

### 1. lem:cot

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*PC.4, `paper/main.tex` lines 180-182:*

````
\begin{lemma}[Cotangent sum]\label{lem:cot}
For every integer $m\ge2$, $\ \displaystyle\sum_{j=1}^{m-1}\cot^2\!\Big(\tfrac{j\pi}{m}\Big)=\tfrac{(m-1)(m-2)}{3}$.
\end{lemma}
````

### 2. prop:csc

| field | value |
|---|---|
| status | PROVED |
| dependencies | lem:cot |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*PC.5, `paper/main.tex` lines 188-190:*

````
\begin{proposition}[Cosecant sum]\label{prop:csc}
For every integer $m\ge2$, $\ \displaystyle\sum_{j=1}^{m-1}\csc^2\!\Big(\tfrac{j\pi}{m}\Big)=\tfrac{m^2-1}{3}$.
\end{proposition}
````

### 3. def:cone, cor:conevals

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | prop:csc |
| external inputs | DGGW cone convention (§5.6, (5.7)) |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*PC.6, `paper/main.tex` lines 196-205:*

````
In the convention of~\cite{dggw2008} a rotation of order $m$ through angle $2\pi j/m$ contributes $b_0(\gamma^j)=\tfrac14\csc^2(j\pi/m)$ to its fixed-point stratum, and the stratum term is divided by the isotropy order $m$.

\begin{definition}\label{def:cone}
The \emph{cone contribution} of a cone point of order $m\ge2$ is
$\ \operatorname{cone}(m):=\tfrac{1}{4m}\sum_{j=1}^{m-1}\csc^2(j\pi/m)$.
\end{definition}

\begin{corollary}\label{cor:conevals}
$\operatorname{cone}(m)=\dfrac{m^2-1}{12m}=\tfrac1{12}\big(m-\tfrac1m\big)$; in particular $\operatorname{cone}(2)=\tfrac18$, $\operatorname{cone}(3)=\tfrac29$, $\operatorname{cone}(5)=\tfrac25$.
\end{corollary}
````

### 4. eq:a0conv, eq:s1inv, rem:bugfix

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | cor:conevals |
| external inputs | DGGW (5.7) |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Keep eq:s1inv; drop rem:bugfix (records an internal error only). State that the reference triple (2,3,5) is spherical and the t^0 smooth term is curvature-sign independent. |

*PC.2, `paper/main.tex` lines 139-144:*

````
We use the orbifold heat-trace expansion of Dryden--Gordon--Greenwald--Webb~\cite{dggw2008}. With the smooth principal-stratum series carrying the $(4\pi t)^{-1}$ prefactor and each cone point $C$ of order $m$ contributing $b_\ell(C)$ at order $t^{\ell}$, the degree-zero (constant) coefficient of $\mathcal{O}(p,q,r)$ is
\begin{equation}
    a_0 \;=\; \frac{\chi(\mathcal{O})}{6} \;+\; \sum_{i}\frac{m_i^2-1}{12\,m_i},
    \label{eq:a0conv}
\end{equation}
where $\chi(\mathcal{O}) = 2 - \sum_i(1-\tfrac1{m_i}) = R-1$ is the orbifold Euler characteristic, $R:=\sum_i \tfrac1{m_i}$, and the normalization is the $1/(4\pi)$ of~\cite{dggw2008} (no separate Euler factor). As a fixed reference point, the spherical triple $(2,3,5)$ gives cone sum $\tfrac18+\tfrac29+\tfrac25=\tfrac{269}{360}$ and, with the smooth term $\chi/6=\tfrac1{180}$, total $a_0=\tfrac{271}{360}$.
````

*PC.7, `paper/main.tex` lines 216-231:*

````
Write the elementary symmetric functions $e_1=p+q+r=S_1$, $e_2=pq+qr+rp$, $e_3=pqr$, so $R=e_2/e_3$. The heat expansion supplies, in order:

\begin{enumerate}[label=(\roman*)]
\item \textbf{Area.} By~\eqref{eq:area} the first coefficient determines $R=\tfrac1p+\tfrac1q+\tfrac1r=e_2/e_3$.
\item \textbf{Zeroth coefficient.} By~\eqref{eq:a0conv} and Corollary~\ref{cor:conevals}, using $\sum_i\operatorname{cone}(m_i)=\tfrac1{12}(S_1-R)$ and $\chi/6=(R-1)/6$,
\begin{equation}
    a_0=\frac{S_1+R-2}{12}\qquad\Longleftrightarrow\qquad \boxed{\,S_1=12\,a_0+2-R\,}.
    \label{eq:s1inv}
\end{equation}
With $R$ known, \eqref{eq:s1inv} returns $S_1=e_1$.
\item \textbf{Third invariant.} The third coefficient supplies one further symmetric function $I_3$, independent of $(S_1,R)$; it is derived in Section~\ref{sec:a2}.
\end{enumerate}

\begin{remark}\label{rem:bugfix}
The constant $+2$ in~\eqref{eq:s1inv} is the smooth term $\chi(\mathcal{O})/6=(R-1)/6$ carried through the inversion. Treating the topological Euler characteristic of the underlying sphere as an additive constant instead would give $S_1=12(a_0-2)+R$, which already fails the reference triple: it returns a negative value for $(2,3,5)$, where $S_1=10$. We record the correct normalization to preclude this.
\end{remark}
````

### 5. Heat expansion structure (sec:heatexp)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | DGGW Thm 4.8, Def 4.7 |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Integer powers of t come from the orbifold strata (points), not from constant curvature. |

*PC.3, `paper/main.tex` lines 171-175:*

````
On a closed hyperbolic $2$-orbifold $\mathcal{O}$ the heat trace has the small-time asymptotic expansion of Minakshisundaram--Pleijel type~\cite{mckeansinger1967}, refined to the orbifold stratification by Donnelly and Dryden--Gordon--Greenwald--Webb~\cite{donnelly1976, dggw2008}. It splits along the strata:
\[
    \operatorname{tr}e^{-t\Delta}\ \sim\ \underbrace{(4\pi t)^{-1}\sum_{\ell\ge0} a^{\mathrm{sm}}_\ell\, t^{\ell}}_{\text{principal (smooth) stratum}}\ +\ \sum_{\text{cone points }C}\ \underbrace{\sum_{\ell\ge0} b_\ell(C)\, t^{\ell}}_{\text{singular stratum}},
\]
where each $a^{\mathrm{sm}}_\ell$ is the integral over $\mathcal{O}$ of a universal polynomial in the curvature and its covariant derivatives, and each cone point $C$ (a zero-dimensional singular stratum) contributes a series $b_\ell(C)$ carrying no $(4\pi t)^{-1}$ prefactor. Because the cones have constant curvature the expansion contains only integer powers of $t$: the half-integer and logarithmic terms that arise for genuinely curved conical singularities~\cite{schueth2025, suleymanova2017, nrs2024} are absent, as a constant-curvature orbifold cone has no curvature blow-up at the tip. The three invariants of this paper are the coefficients of $t^{-1}$, $t^{0}$, and $t^{1}$. At constant curvature each smooth term $a^{\mathrm{sm}}_\ell$ is a fixed multiple of $\operatorname{Area}(\mathcal{O})$, hence a function of $R$ alone; the geometric content beyond the area therefore lives entirely in the cone-point sums $\sum_i b_\ell(C_i)$, which we compute in the next two subsections.
````

### 6. eq:b1, eq:a2red

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | eq:a0conv |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20; Schueth Rem 4.2; DGGW (5.10) |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*PC.8, `paper/main.tex` lines 236-246:*

````
The three leading coefficients are those of $t^{-1}$ (area, giving $R$), $t^0$ (giving $S_1$), and $t^1$. For a cone of order $m$ and Gauss curvature $K$, the constant-curvature cone coefficient at order $t^1$ is\footnote{The expression~\eqref{eq:b1} is quoted from the constant-curvature cone/orbifold literature, not rederived here. It is the cone-point coefficient $a_1(\{\bar p\})$ of Schueth~\cite{schueth2019}, Remark~4.2 (there attributed to Dryden--Gordon--Greenwald--Webb~\cite{dggw2008}, §5.6), restated with the same attribution in~\cite{schueth2025}, and consistent with U\c{c}ar's constant-curvature form $b_\ell(C)=\kappa^\ell\tfrac1m p_\ell(m)$, $\deg p_\ell=2\ell+2$~\cite{ucar2017}. We use only the specialization $K=-1$. The normalization matches Section~\ref{sec:conventions}: the smooth series carries the $(4\pi t)^{-1}$ prefactor, while a cone point ,  a zero-dimensional stratum ,  contributes at order $t^\ell$ with no such prefactor (\cite{schueth2019}, Rem.~3.2) and with the $\tfrac1m$-average over the $m-1$ nontrivial rotations built in (\cite{schueth2019}, eq.~(17)).}
\begin{equation}
    b_1(C)=\Big[\tfrac1{360}\big(m^3-\tfrac1m\big)+\tfrac1{36}\big(m-\tfrac1m\big)\Big]K,
    \label{eq:b1}
\end{equation}
with $b_0(C)=\tfrac{m^2-1}{12m}$ as above. At constant negative curvature $K=-1$ the smooth part of the $t^1$ coefficient is a universal constant times $\operatorname{Area}(\mathcal{O})=2\pi(1-R)$, hence a function of the already-known $R$; the new content is $\sum_i b_1(C_i)$. Summing~\eqref{eq:b1} at $K=-1$,
\begin{equation}
    \sum_i b_1(C_i)\Big|_{K=-1}=-\tfrac1{360}\,P_3-\tfrac1{36}\,S_1+\tfrac{11}{360}\,R,\qquad P_3:=\sum_i m_i^3,
    \label{eq:a2red}
\end{equation}
using $\tfrac1{360}+\tfrac1{36}=\tfrac{11}{360}$. Thus, modulo $(S_1,R)$, the third invariant delivers the power sum $P_3=\sum m_i^3$. For the determinacy results only a weaker feature of~\eqref{eq:a2red} is needed: after subtracting the terms in $R$ and $S_1$ (both known from the first two coefficients), what remains is a \emph{nonzero} rational multiple of $P_3$ (here $-\tfrac1{360}$). The recovery of Proposition~\ref{prop:recovery} therefore depends on $b_1$ only through this nonvanishing $m^3$-coefficient, and is unaffected by the precise values of the lower-order terms of~\eqref{eq:b1}. This is not the flat-cone quantity $\sum m_i^{-3}$: a flat cone contributes nothing at this order ($b_1=0$ at $K=0$), so $\sum m_i^{-3}$ is not a hyperbolic heat invariant.
````

### 7. prop:cs

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*PC.9, `paper/main.tex` lines 248-250:*

````
\begin{proposition}[Cauchy--Schwarz bound]\label{prop:cs}
For every hyperbolic triad, $S_1 R=(p+q+r)\big(\tfrac1p+\tfrac1q+\tfrac1r\big)\ge 9$, with equality iff $p=q=r$.
\end{proposition}
````

### 8. prop:recovery

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | eq:a2red, prop:cs |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*PC.9b, `paper/main.tex` lines 256-258:*

````
\begin{proposition}[Recovery from three symmetric functions]\label{prop:recovery}
The values $R=\sum_i m_i^{-1}$, $S_1=\sum_i m_i$, and $P_3=\sum_i m_i^{3}$ determine the multiset $\{p,q,r\}$; equivalently, the map sending a hyperbolic triangular pillow to its first three heat coefficients is injective.
\end{proposition}
````

### 9. Jacobian of (S1,R,P3)

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*PC.10, `paper/main.tex` lines 269-269:*

````
This Newton--Vieta inversion is a standard symmetric-function recovery. Its infinitesimal counterpart is immediate: the map $F=(S_1,R,P_3)$ has Jacobian determinant $\det DF=-3\,(p-q)(p-r)(q-r)(p+q)(p+r)(q+r)/(p^2q^2r^2)$, nonzero off the diagonals $p=q$, $p=r$, $q=r$, so the three invariants form a local coordinate system on each open ordered chamber $\{p<q<r\}$. This plays no role in the two-coefficient threshold of Section~\ref{sec:threshold}, which concerns the discrete map $\sigma=(S_1,R)$.
````

### 10. lem:chamber

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | For p=2 (and (S,p)=(9,3)) the spread triad is not hyperbolic, so the maximum is not attained there. |

*PC.11, `paper/main.tex` lines 279-290:*

````
The first two heat coefficients resolve a triad to $\sigma(p,q,r)=(S_1,R)$, where $S_1=p+q+r$ and $R=\tfrac1p+\tfrac1q+\tfrac1r$. A \emph{two-coefficient collision} is a pair of distinct hyperbolic triads with the same $\sigma$. Since $\sigma$ records $S_1$ first, a collision forces equal $S_1$; within a fixed sum $S_1=S$ there are finitely many triads and $\sigma$ reduces to $R$, so injectivity can be decided sum by sum. The proof rests on the monotonicity of $R$ within a stratum of fixed sum and least order. Fix a sum $S$ and a least order $p$. The hyperbolic triads $\mathcal{O}(p,q,r)$ with $p\le q\le r$ and $p+q+r=S$ form the \emph{$(S,p)$-stratum}; on it $r=S-p-q$ and the reciprocal sum is the one-variable function
\[
    R_{S,p}(q)=\frac1p+\frac1q+\frac1{\,S-p-q\,},\qquad p\le q\le\tfrac{S-p}{2}.
\]

\begin{lemma}[Chamber monotonicity]\label{lem:chamber}
On the ordered chamber $p\le q\le r=S-p-q$,
\[
    R_{S,p}'(q)=-\frac1{q^2}+\frac1{(S-p-q)^2}\le0,
\]
with equality only at $q=r$. Hence $R_{S,p}$ is strictly decreasing in $q$: on each stratum $R$ is injective, attains its maximum at the spread triad $q=p$, namely $\mathcal{O}(p,p,S-2p)$, and its minimum at the balanced triad $q=\lfloor\tfrac{S-p}2\rfloor$.
\end{lemma}
````

### 11. lem:bound and the R^+ formula

| field | value |
|---|---|
| status | PROVED |
| dependencies | lem:chamber |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | R^+_{S,2} is never attained; the stratum is a finite set, not a filled interval. |

*PC.12, `paper/main.tex` lines 295-303:*

````
In particular a two-coefficient collision cannot occur \emph{within} a stratum: distinct triads of equal sum and equal least order have distinct $R$. Write $R^{-}_{S,p}$ and $R^{+}_{S,p}$ for the minimum (balanced) and maximum (spread) values; by Lemma~\ref{lem:chamber} the reciprocal sums of the stratum fill $[R^{-}_{S,p},R^{+}_{S,p}]$ injectively. The maximum is explicit,
\[
    R^{+}_{S,p}=R_{S,p}(p)=\frac2p+\frac1{\,S-2p\,},
\]
and is non-increasing in $p$ for $p\le S/3$. The minimum admits a clean uniform lower bound.

\begin{lemma}[Balanced lower bound]\label{lem:bound}
$R^{-}_{S,p}\ge \dfrac1p+\dfrac4{\,S-p\,}$, with equality iff $S-p$ is even.
\end{lemma}
````

### 12. prop:min

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*PC.13, `paper/main.tex` lines 310-312:*

````
\begin{proposition}[Balanced configurations minimize $R$ and $a_0$]\label{prop:min}
At a fixed cone-order sum $S_1$, the reciprocal sum $R=\sum_i m_i^{-1}$ is minimized by the most balanced admissible triple and increases as the orders spread apart; equivalently $R$ is Schur-convex in $(m_1,m_2,m_3)$. Since $a_0=\tfrac{S_1+R-2}{12}$ by~\eqref{eq:a0conv}, the constant heat coefficient at fixed $S_1$ is likewise smallest for the balanced pillow and grows with the anisotropy of the cone orders. This is a convexity statement about the two leading invariants.
\end{proposition}
````

### 13. thm:separation

| field | value |
|---|---|
| status | PROVED |
| dependencies | lem:chamber, lem:bound |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | Threshold Theorem 1 / Corollary 2 give a uniform-in-p replacement for the per-p list. |

*PC.14, `paper/main.tex` lines 319-323:*

````
Since $\sigma$ records $S_1$ first, a collision forces equal sum, and by Lemma~\ref{lem:chamber} it must join \emph{different} least-order strata. It therefore suffices to separate the strata of each fixed sum. No hyperbolic triad has $S_1\le9$: for $2\le p\le q\le r$ with $R<1$, if $p=2$ then $\tfrac1q+\tfrac1r<\tfrac12$ forces $q+r\ge9$ and $S_1\ge11$; if $p=3$ then $q+r\ge7$ and $S_1\ge10$; and $p\ge4$ gives $S_1\ge12$. Thus $S_1\ge10$, with equality only for $\mathcal{O}(3,3,4)$. For $S\le17$ the least order obeys $p\le\lfloor S/3\rfloor\le5$, so only the strata $p\in\{2,3,4,5\}$ arise.

\begin{theorem}[Interval separation]\label{thm:separation}
For every $S\le17$ the reciprocal-sum intervals $[R^{-}_{S,p},R^{+}_{S,p}]$ of the distinct least-order strata are pairwise disjoint; consequently $\sigma$ is injective on hyperbolic triads of sum $S\le17$. Moreover the intervals of least orders $2$ and $3$ first meet at $S=18$, at the common value $R=\tfrac34$ realized by the balanced triad $\mathcal{O}(2,8,8)$ and the spread triad $\mathcal{O}(3,3,12)$; at $S=18$ every other adjacent pair of strata is still separated.
\end{theorem}
````

*PC.15, `paper/main.tex` lines 333-345:*

````
\item[$(p=2)$:] $\tau_2=\tfrac16$; both strata occur for $11\le S\le18$, where $\varphi_2$ decreases (peak at $S=10$). At the right end $\varphi_2(17)=\tfrac4{15}-\tfrac1{11}=\tfrac{29}{165}>\tfrac16$, so $\varphi_2(S)>\tfrac16$ throughout $S\le17$; and $\varphi_2(18)=\tfrac14-\tfrac1{12}=\tfrac16$ exactly.
\item[$(p=3)$:] $\tau_3=\tfrac16$; both strata occur for $12\le S\le17$. By unimodality (peak at $S=13$) the minimum sits at an endpoint: $\varphi_3(12)=\tfrac7{36}$ and $\varphi_3(17)=\tfrac{11}{63}$, both $>\tfrac16$.
\item[$(p=4)$:] $\tau_4=\tfrac3{20}$; both strata occur for $15\le S\le17$, and $\min\{\varphi_4(15),\varphi_4(16),\varphi_4(17)\}=\varphi_4(15)=\tfrac9{55}>\tfrac3{20}$.
\end{itemize}
This proves pairwise disjointness for all $S\le17$, hence Theorem~\ref{thmA}.

At $S=18$ the pair $(2,3)$ reaches equality: here $S-2=16$ is even, so Lemma~\ref{lem:bound} is tight and $\varphi_2(18)=\tau_2$, giving $R^{-}_{18,2}=R^{+}_{18,3}$; explicitly $R(2,8,8)=\tfrac12+\tfrac18+\tfrac18=\tfrac34$ and $R(3,3,12)=\tfrac23+\tfrac1{12}=\tfrac34$, both hyperbolic. The other adjacent pairs remain strictly separated at $S=18$: with $S-3=15$ and $S-5=13$ odd, Lemma~\ref{lem:bound} is strict, and one computes
\[
    R^{-}_{18,3}=\tfrac{101}{168}>\tfrac35=R^{+}_{18,4},\qquad
    R^{-}_{18,4}=\tfrac{15}{28}>\tfrac{21}{40}=R^{+}_{18,5},\qquad
    R^{-}_{18,5}=\tfrac{107}{210}>\tfrac12=R^{+}_{18,6}.
\]
Thus $S=18$ produces exactly one coincidence, the pair $\{\mathcal{O}(2,8,8),\mathcal{O}(3,3,12)\}$.
````

### 14. thmA

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | thm:separation, eq:s1inv |
| external inputs | DGGW (5.7) |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | 'once the cone-order sum reaches 18' reads as every S>=18; sums 19, 21-25, ... have no collision (last collision-free sum 557). |

*PC.1, `paper/main.tex` lines 103-119:*

````
Our main results are the following. Throughout, $K(F)$ denotes the least number of leading heat coefficients that distinguish a pillow $F$ from every other hyperbolic triangular pillow, and a pair of non-isometric pillows sharing their first two heat coefficients is a \emph{two-coefficient spectral degeneracy}, or \emph{collision} ,  the two terms are used interchangeably.

\begin{mainthm}[Finite-coefficient determinacy threshold]\label{thmA}
Let $F=\mathcal{O}(p,q,r)$ be a hyperbolic triangular pillow. If $p+q+r\le17$, then $F$ is determined among all hyperbolic triangular pillows by its first two heat coefficients, so $K(F)\le2$. The bound $17$ is sharp: two coefficients no longer determine every pillow once the cone-order sum reaches $18$ (Theorem~\ref{thmB}).
\end{mainthm}

\begin{mainthm}[Minimal two-coefficient degeneracy]\label{thmB}
The non-isometric pillows $\mathcal{O}(2,8,8)$ and $\mathcal{O}(3,3,12)$ have identical first two heat coefficients. Among all two-coefficient degeneracies this pair has the smallest cone-order sum, $p+q+r=18$; it is the unique degeneracy at that sum, and none occurs for $p+q+r\le17$.
\end{mainthm}

\begin{mainthm}[Three-coefficient determinacy of the cone-order multiset]\label{thmC}
The first three heat coefficients determine a hyperbolic triangular pillow up to isometry ,  equivalently, they determine its singular set together with the cone order at each singular point. Thus $K(F)\le3$ for every such pillow, and $K(F)=3$ for the collision pair $\mathcal{O}(2,8,8),\mathcal{O}(3,3,12)$ of Theorem~\ref{thmB}.
\end{mainthm}

\begin{maincor}[What the heat coefficients detect]\label{corD}
For $\mathcal{O}(p,q,r)$ write $R=\sum_i m_i^{-1}$ and $S_1=\sum_i m_i$. The first heat coefficient detects the area, equivalently $R$; the first two factor through the pair $(R,S_1)$ ,  the area and the total cone order ,  so that two-coefficient determinacy is exactly injectivity of the map $(p,q,r)\mapsto(R,S_1)$; the first three additionally detect $\sum_i m_i^3$, hence the individual cone orders. Consequently the two leading coefficients resolve the full singular stratum for every pillow with $p+q+r\le17$, and this range is sharp: the first failure occurs at $p+q+r=18$, for the pair of Theorem~\ref{thmB}. The larger-sum pillows for which two coefficients fail to suffice are enumerated, and their density studied, in Section~\ref{sec:density}.
\end{maincor}
````

### 15. thmB

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | thm:separation, eq:a2red |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*PC.1, `paper/main.tex` lines 103-119:*

````
Our main results are the following. Throughout, $K(F)$ denotes the least number of leading heat coefficients that distinguish a pillow $F$ from every other hyperbolic triangular pillow, and a pair of non-isometric pillows sharing their first two heat coefficients is a \emph{two-coefficient spectral degeneracy}, or \emph{collision} ,  the two terms are used interchangeably.

\begin{mainthm}[Finite-coefficient determinacy threshold]\label{thmA}
Let $F=\mathcal{O}(p,q,r)$ be a hyperbolic triangular pillow. If $p+q+r\le17$, then $F$ is determined among all hyperbolic triangular pillows by its first two heat coefficients, so $K(F)\le2$. The bound $17$ is sharp: two coefficients no longer determine every pillow once the cone-order sum reaches $18$ (Theorem~\ref{thmB}).
\end{mainthm}

\begin{mainthm}[Minimal two-coefficient degeneracy]\label{thmB}
The non-isometric pillows $\mathcal{O}(2,8,8)$ and $\mathcal{O}(3,3,12)$ have identical first two heat coefficients. Among all two-coefficient degeneracies this pair has the smallest cone-order sum, $p+q+r=18$; it is the unique degeneracy at that sum, and none occurs for $p+q+r\le17$.
\end{mainthm}

\begin{mainthm}[Three-coefficient determinacy of the cone-order multiset]\label{thmC}
The first three heat coefficients determine a hyperbolic triangular pillow up to isometry ,  equivalently, they determine its singular set together with the cone order at each singular point. Thus $K(F)\le3$ for every such pillow, and $K(F)=3$ for the collision pair $\mathcal{O}(2,8,8),\mathcal{O}(3,3,12)$ of Theorem~\ref{thmB}.
\end{mainthm}

\begin{maincor}[What the heat coefficients detect]\label{corD}
For $\mathcal{O}(p,q,r)$ write $R=\sum_i m_i^{-1}$ and $S_1=\sum_i m_i$. The first heat coefficient detects the area, equivalently $R$; the first two factor through the pair $(R,S_1)$ ,  the area and the total cone order ,  so that two-coefficient determinacy is exactly injectivity of the map $(p,q,r)\mapsto(R,S_1)$; the first three additionally detect $\sum_i m_i^3$, hence the individual cone orders. Consequently the two leading coefficients resolve the full singular stratum for every pillow with $p+q+r\le17$, and this range is sharp: the first failure occurs at $p+q+r=18$, for the pair of Theorem~\ref{thmB}. The larger-sum pillows for which two coefficients fail to suffice are enumerated, and their density studied, in Section~\ref{sec:density}.
\end{maincor}
````

### 16. thmC

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | prop:recovery, prop:rigidity |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20; Troyanov Thm A |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | 'Up to isometry' needs prop:rigidity (or locality Prop 2.1); cite it. |

*PC.1, `paper/main.tex` lines 103-119:*

````
Our main results are the following. Throughout, $K(F)$ denotes the least number of leading heat coefficients that distinguish a pillow $F$ from every other hyperbolic triangular pillow, and a pair of non-isometric pillows sharing their first two heat coefficients is a \emph{two-coefficient spectral degeneracy}, or \emph{collision} ,  the two terms are used interchangeably.

\begin{mainthm}[Finite-coefficient determinacy threshold]\label{thmA}
Let $F=\mathcal{O}(p,q,r)$ be a hyperbolic triangular pillow. If $p+q+r\le17$, then $F$ is determined among all hyperbolic triangular pillows by its first two heat coefficients, so $K(F)\le2$. The bound $17$ is sharp: two coefficients no longer determine every pillow once the cone-order sum reaches $18$ (Theorem~\ref{thmB}).
\end{mainthm}

\begin{mainthm}[Minimal two-coefficient degeneracy]\label{thmB}
The non-isometric pillows $\mathcal{O}(2,8,8)$ and $\mathcal{O}(3,3,12)$ have identical first two heat coefficients. Among all two-coefficient degeneracies this pair has the smallest cone-order sum, $p+q+r=18$; it is the unique degeneracy at that sum, and none occurs for $p+q+r\le17$.
\end{mainthm}

\begin{mainthm}[Three-coefficient determinacy of the cone-order multiset]\label{thmC}
The first three heat coefficients determine a hyperbolic triangular pillow up to isometry ,  equivalently, they determine its singular set together with the cone order at each singular point. Thus $K(F)\le3$ for every such pillow, and $K(F)=3$ for the collision pair $\mathcal{O}(2,8,8),\mathcal{O}(3,3,12)$ of Theorem~\ref{thmB}.
\end{mainthm}

\begin{maincor}[What the heat coefficients detect]\label{corD}
For $\mathcal{O}(p,q,r)$ write $R=\sum_i m_i^{-1}$ and $S_1=\sum_i m_i$. The first heat coefficient detects the area, equivalently $R$; the first two factor through the pair $(R,S_1)$ ,  the area and the total cone order ,  so that two-coefficient determinacy is exactly injectivity of the map $(p,q,r)\mapsto(R,S_1)$; the first three additionally detect $\sum_i m_i^3$, hence the individual cone orders. Consequently the two leading coefficients resolve the full singular stratum for every pillow with $p+q+r\le17$, and this range is sharp: the first failure occurs at $p+q+r=18$, for the pair of Theorem~\ref{thmB}. The larger-sum pillows for which two coefficients fail to suffice are enumerated, and their density studied, in Section~\ref{sec:density}.
\end{maincor}
````

### 17. corD

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | thmA, thmB, prop:recovery |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*PC.1, `paper/main.tex` lines 103-119:*

````
Our main results are the following. Throughout, $K(F)$ denotes the least number of leading heat coefficients that distinguish a pillow $F$ from every other hyperbolic triangular pillow, and a pair of non-isometric pillows sharing their first two heat coefficients is a \emph{two-coefficient spectral degeneracy}, or \emph{collision} ,  the two terms are used interchangeably.

\begin{mainthm}[Finite-coefficient determinacy threshold]\label{thmA}
Let $F=\mathcal{O}(p,q,r)$ be a hyperbolic triangular pillow. If $p+q+r\le17$, then $F$ is determined among all hyperbolic triangular pillows by its first two heat coefficients, so $K(F)\le2$. The bound $17$ is sharp: two coefficients no longer determine every pillow once the cone-order sum reaches $18$ (Theorem~\ref{thmB}).
\end{mainthm}

\begin{mainthm}[Minimal two-coefficient degeneracy]\label{thmB}
The non-isometric pillows $\mathcal{O}(2,8,8)$ and $\mathcal{O}(3,3,12)$ have identical first two heat coefficients. Among all two-coefficient degeneracies this pair has the smallest cone-order sum, $p+q+r=18$; it is the unique degeneracy at that sum, and none occurs for $p+q+r\le17$.
\end{mainthm}

\begin{mainthm}[Three-coefficient determinacy of the cone-order multiset]\label{thmC}
The first three heat coefficients determine a hyperbolic triangular pillow up to isometry ,  equivalently, they determine its singular set together with the cone order at each singular point. Thus $K(F)\le3$ for every such pillow, and $K(F)=3$ for the collision pair $\mathcal{O}(2,8,8),\mathcal{O}(3,3,12)$ of Theorem~\ref{thmB}.
\end{mainthm}

\begin{maincor}[What the heat coefficients detect]\label{corD}
For $\mathcal{O}(p,q,r)$ write $R=\sum_i m_i^{-1}$ and $S_1=\sum_i m_i$. The first heat coefficient detects the area, equivalently $R$; the first two factor through the pair $(R,S_1)$ ,  the area and the total cone order ,  so that two-coefficient determinacy is exactly injectivity of the map $(p,q,r)\mapsto(R,S_1)$; the first three additionally detect $\sum_i m_i^3$, hence the individual cone orders. Consequently the two leading coefficients resolve the full singular stratum for every pillow with $p+q+r\le17$, and this range is sharp: the first failure occurs at $p+q+r=18$, for the pair of Theorem~\ref{thmB}. The larger-sum pillows for which two coefficients fail to suffice are enumerated, and their density studied, in Section~\ref{sec:density}.
\end{maincor}
````

### 18. remark* on a_0

| field | value |
|---|---|
| status | PROVED |
| dependencies | prop:min, prop:cs |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*PC.16, `paper/main.tex` lines 394-396:*

````
\begin{remark*}
Proposition~\ref{prop:min} places the balanced end of each stratum: at fixed cone-order sum the constant coefficient $a_0=\tfrac{S_1+R-2}{12}$ is minimized by the balanced pillow $p=q=r$ where one exists ($3\mid S_1$, $S_1/3\ge4$) and is non-increasing under balancing otherwise. This is a fixed-sum statement ,  across \emph{all} pillows $a_0$ is smallest for the non-balanced $\mathcal{O}(3,3,4)$, with $a_0=\tfrac{107}{144}$, consistent with the sharp bound $S_1R\ge9$ (Proposition~\ref{prop:cs}) ,  and is a convexity fact about the two leading invariants.
\end{remark*}
````

### 19. prop:scaling

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | The sentence in the same excerpt claiming that interval separation localizes every degeneracy to adjacent strata is FALSE (row 'degeneracy localization'). |

*PC.17, `paper/main.tex` lines 402-421:*

````
Theorem~\ref{thmA} and its sharp failure at $S_1=18$ (Theorem~\ref{thmB}) are the base cases of a Diophantine phenomenon that recurs at larger cone-order sums. A \emph{two-coefficient spectral degeneracy} is a pair of distinct hyperbolic triples with equal $\sigma=(S_1,R)$; by Lemma~\ref{lem:chamber} the two triples share the sum $S_1$ and lie in different least-order strata, so a degeneracy is exactly a pair of distinct triples $2\le p\le q\le r$ and $2\le p'\le q'\le r'$ with
\[
    p+q+r=p'+q'+r'=S \qquad\text{and}\qquad \tfrac1p+\tfrac1q+\tfrac1r=\tfrac1{p'}+\tfrac1{q'}+\tfrac1{r'},
\]
that is, two three-term Egyptian-fraction representations of a common value with equal denominator sum. Section~\ref{sec:threshold} establishes that none exists for $S\le17$ and that $\{\mathcal{O}(2,8,8),\mathcal{O}(3,3,12)\}$ is the unique one at $S=18$. Beyond the base case the counting problem opens up. Write
\[
    N(S):=\#\{\text{two-coefficient degeneracies with cone-order sum }S\},\qquad
    \mathcal{N}(S):=\sum_{s\le S}N(s)
\]
for the number of degeneracies at sum exactly $S$ and cumulatively up to $S$. The interval-separation mechanism of Theorem~\ref{thm:separation} localizes every degeneracy at sum $S$ to the finitely many contacts between adjacent least-order strata, so $N(S)$ is computable in exact rational arithmetic for each $S$, and the growth of $\mathcal{N}(S)$ becomes a well-posed asymptotic question: does $\mathcal{N}(S)\to\infty$, and if so at what rate and with what density among all hyperbolic pillows of sum $\le S$? We answer the first question unconditionally, with an explicit linear-order lower bound, and give a numerically supported conjecture on the true (quadratic-order) growth rate.

\subsection{An exact scaling law and the unconditional lower bound}

\begin{proposition}[Scaling law for degeneracies]\label{prop:scaling}
Let $\{\mathcal O(p,q,r),\mathcal O(p',q',r')\}$ be a two-coefficient degeneracy at cone-order sum $S_0$. Then for every integer $k\ge1$,
\[
    \{\mathcal O(kp,kq,kr),\ \mathcal O(kp',kq',kr')\}
\]
is a two-coefficient degeneracy at cone-order sum $kS_0$.
\end{proposition}
````

### 20. Degeneracy localization to adjacent strata (sentence before prop:scaling; repeated in sec:density)

| field | value |
|---|---|
| status | CLAIM (FALSE) |
| dependencies | thm:separation |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/`, `review/audit/consistency/` |
| audit verdict | SERIOUS |
| in paper? | NO |
| note | 2793 of the 3067 pairs with S<=600 join strata whose least orders differ by >=2; first at S=35, (5,15,15)~(7,7,21). Describe the enumeration as exhaustive. |

*PC.17, `paper/main.tex` lines 402-421:*

````
Theorem~\ref{thmA} and its sharp failure at $S_1=18$ (Theorem~\ref{thmB}) are the base cases of a Diophantine phenomenon that recurs at larger cone-order sums. A \emph{two-coefficient spectral degeneracy} is a pair of distinct hyperbolic triples with equal $\sigma=(S_1,R)$; by Lemma~\ref{lem:chamber} the two triples share the sum $S_1$ and lie in different least-order strata, so a degeneracy is exactly a pair of distinct triples $2\le p\le q\le r$ and $2\le p'\le q'\le r'$ with
\[
    p+q+r=p'+q'+r'=S \qquad\text{and}\qquad \tfrac1p+\tfrac1q+\tfrac1r=\tfrac1{p'}+\tfrac1{q'}+\tfrac1{r'},
\]
that is, two three-term Egyptian-fraction representations of a common value with equal denominator sum. Section~\ref{sec:threshold} establishes that none exists for $S\le17$ and that $\{\mathcal{O}(2,8,8),\mathcal{O}(3,3,12)\}$ is the unique one at $S=18$. Beyond the base case the counting problem opens up. Write
\[
    N(S):=\#\{\text{two-coefficient degeneracies with cone-order sum }S\},\qquad
    \mathcal{N}(S):=\sum_{s\le S}N(s)
\]
for the number of degeneracies at sum exactly $S$ and cumulatively up to $S$. The interval-separation mechanism of Theorem~\ref{thm:separation} localizes every degeneracy at sum $S$ to the finitely many contacts between adjacent least-order strata, so $N(S)$ is computable in exact rational arithmetic for each $S$, and the growth of $\mathcal{N}(S)$ becomes a well-posed asymptotic question: does $\mathcal{N}(S)\to\infty$, and if so at what rate and with what density among all hyperbolic pillows of sum $\le S$? We answer the first question unconditionally, with an explicit linear-order lower bound, and give a numerically supported conjecture on the true (quadratic-order) growth rate.

\subsection{An exact scaling law and the unconditional lower bound}

\begin{proposition}[Scaling law for degeneracies]\label{prop:scaling}
Let $\{\mathcal O(p,q,r),\mathcal O(p',q',r')\}$ be a two-coefficient degeneracy at cone-order sum $S_0$. Then for every integer $k\ge1$,
\[
    \{\mathcal O(kp,kq,kr),\ \mathcal O(kp',kq',kr')\}
\]
is a two-coefficient degeneracy at cone-order sum $kS_0$.
\end{proposition}
````

### 21. thm:density-lower

| field | value |
|---|---|
| status | PROVED |
| dependencies | prop:scaling, thmB |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES, REVISED |
| note | Correct but superseded by Diophantine Theorem 4 (c_iso X log X) and Theorem 5 (X (log X)^2); state the stronger bound. |

*PC.17b, `paper/main.tex` lines 426-431:*

````
\begin{theorem}[Infinitude and a linear lower bound]\label{thm:density-lower}
There are infinitely many two-coefficient spectral degeneracies. More precisely, for every $S\ge18$,
\[
    \mathcal N(S)\ \ge\ \Big\lfloor \frac S{18}\Big\rfloor.
\]
\end{theorem}
````

### 22. Primitive pair at S=36

| field | value |
|---|---|
| status | COMPUTATION |
| dependencies | — |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | 'Almost every sum' should read 'most sums' (507 of 582 sums in 19..600). |

*PC.18, `paper/main.tex` lines 436-436:*

````
Theorem~\ref{thm:density-lower} is unconditional and elementary, but it undercounts the true growth substantially: it accounts only for scaled copies of the single base pair, whereas exact enumeration shows that new (\emph{primitive}, i.e.\ not obtained by scaling a smaller degeneracy) collisions appear at almost every sum beyond $18$. For instance at $S=36=2\cdot18$ there are two degeneracy classes: the scaled copy $\{\mathcal O(4,16,16),\mathcal O(6,6,24)\}$ predicted by Proposition~\ref{prop:scaling}, and a second, primitive one, $\{\mathcal O(6,15,15),\mathcal O(8,8,20)\}$, at reciprocal sum $R=3/10$, not obtainable by scaling the base pair.
````

### 23. tab:density and fitted exponent

| field | value |
|---|---|
| status | COMPUTATION |
| dependencies | — |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | enumerate_degeneracies.py (external repo) |
| audit evidence | `review/audit/threshold/`, `review/audit/consistency/`, `review/audit/diophantine/` |
| audit verdict | SERIOUS |
| in paper? | YES, REVISED |
| note | Table values are exact under the pairs convention (classes: 2977 at 600) - keep, state the convention. The exponent 2.03, 'stabilizes', 'quadratic-order' and the birthday heuristic must go: N(S)/S^2 falls to 0.00405 at S=6000. |

*PC.19, `paper/main.tex` lines 440-481:*

````
We enumerated $N(S)$ exactly (in exact rational arithmetic, via the interval-localization of Theorem~\ref{thm:separation}) for every $10\le S\le600$; this extends Table~\ref{tab:enum} well beyond its printed range of $S\le18$, and the full data and generating script are in the public repository (Appendix~\ref{sec:appendix}). Table~\ref{tab:density} records the cumulative count $\mathcal N(S)$ at a sample of checkpoints.

\begin{table}[h!]
\centering
\caption{Exact cumulative count $\mathcal N(S)$ of two-coefficient degeneracies, from enumeration through $S=600$.}
\label{tab:density}
\begin{tabular}{rrrrr}
\toprule
$S$ & $\mathcal N(S)$ & $\mathcal N(S)/S$ & $\mathcal N(S)/S^2$ & \\
\midrule
18   & 1    & 0.056 & 0.0031 & \\
100  & 92   & 0.92  & 0.0092 & \\
200  & 386  & 1.93  & 0.0097 & \\
300  & 840  & 2.80  & 0.0093 & \\
400  & 1496 & 3.74  & 0.0094 & \\
500  & 2210 & 4.42  & 0.0088 & \\
600  & 3067 & 5.11  & 0.0085 & \\
\bottomrule
\end{tabular}
\end{table}

The ratio $\mathcal N(S)/S$ grows roughly linearly with $S$ over this range, while $\mathcal N(S)/S^2$ stabilizes to within about $10\%$ of $0.009$; a power-law fit $\log\mathcal N(S)$ against $\log S$ over $50\le S\le600$ returns exponent $2.03$. This is far above the exponent $1$ guaranteed by Theorem~\ref{thm:density-lower}, confirming that the scaling law of Proposition~\ref{prop:scaling} captures only a vanishing fraction of the degeneracies at large $S$: at $S=600$ it accounts for $\lfloor600/18\rfloor=33$ of the $3067$ recorded, about one percent.

\subsection{A heuristic for the quadratic growth rate}

The empirical exponent $2$ is consistent with the following counting heuristic, of the birthday-paradox type standard in analogous Diophantine settings. The number of hyperbolic triads of sum $S$ is $\asymp S^2$, since $p$ ranges over $\asymp S$ values and, for each $p$, $q$ ranges over $\asymp S$ values with $r=S-p-q$ determined. Each such triad determines a reduced fraction $R=e_2/e_3$ whose denominator divides $e_3=pqr\le(S/3)^3$, so $R$ lies among $O(S^3)$ rationals of bounded height in a fixed interval. If the values $R$ arising from the $\asymp S^2$ triads of sum $S$ were distributed among these $O(S^3)$ possible values as though at random, a birthday-paradox count of coincidences would predict
\[
    N(S)\ \sim\ \frac{(\text{number of triads})^2}{\text{number of possible }R\text{-values}}\ \asymp\ \frac{(S^2)^2}{S^3}\ =\ S,
\]
matching the observed linear growth of $N(S)$, hence quadratic growth of the cumulative count $\mathcal N(S)=\sum_{s\le S}N(s)$. We state this as a precise conjecture rather than a theorem, since the heuristic treats the arithmetic denominators $e_3(p,q,r)$ as if independent and uniformly distributed, which we have not justified rigorously; in particular it does not by itself explain the sizable and structured population of degeneracies produced by Proposition~\ref{prop:scaling} and its non-scaled analogues (pairs related by a common integer factor extracted from both triples, which contribute a positive but lower-order density).

\begin{conjecture}[Quadratic density]\label{conj:density}
There is a constant $c>0$ such that
\[
    \mathcal N(S)\ \sim\ c\,S^2\qquad(S\to\infty).
\]
Equivalently, $N(S)=\Theta(S)$, so a positive proportion, of order $1/S$, of hyperbolic triads of sum $S$ participate in a two-coefficient degeneracy of sum $S$.
\end{conjecture}

Exact enumeration through $S=600$ is consistent with Conjecture~\ref{conj:density}, with $c$ near $0.0085$ at the top of the computed range (Table~\ref{tab:density}); whether $\mathcal N(S)/S^2$ has in fact stabilized, or is still drifting toward a different limiting constant ,  or a different power of $S$ altogether ,  cannot be resolved from data at this scale, and we leave the conjecture, together with the identification of $c$, open.

Each degeneracy, whether accounted for by Theorem~\ref{thm:density-lower} or only by Conjecture~\ref{conj:density}, exhibits a further pillow with $K(F)=3$: since Theorem~\ref{thmC} gives $K(F)\le3$ unconditionally, the set enumerated here is exactly the set of hyperbolic triangular pillows for which two heat coefficients do not suffice, and Theorem~\ref{thm:density-lower} already shows this set is infinite, of density at least $1/18$ among cone-order sums, with numerical evidence for substantially higher (quadratic-order cumulative) density.
````

### 24. conj:density

| field | value |
|---|---|
| status | CONJECTURE |
| dependencies | — |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/`, `review/audit/consistency/`, `review/audit/diophantine/` |
| audit verdict | SERIOUS |
| in paper? | NO |
| note | Contradicted by enumeration to S=6000; its 'equivalently N(S)=Theta(S)' is not equivalent and the 'positive proportion of order 1/S' clause is self-contradictory. Replace by the Diophantine section's N(S)=S^{1+o(1)} conjecture with the proven X(log X)^2 floor. |

*PC.19, `paper/main.tex` lines 440-481:*

````
We enumerated $N(S)$ exactly (in exact rational arithmetic, via the interval-localization of Theorem~\ref{thm:separation}) for every $10\le S\le600$; this extends Table~\ref{tab:enum} well beyond its printed range of $S\le18$, and the full data and generating script are in the public repository (Appendix~\ref{sec:appendix}). Table~\ref{tab:density} records the cumulative count $\mathcal N(S)$ at a sample of checkpoints.

\begin{table}[h!]
\centering
\caption{Exact cumulative count $\mathcal N(S)$ of two-coefficient degeneracies, from enumeration through $S=600$.}
\label{tab:density}
\begin{tabular}{rrrrr}
\toprule
$S$ & $\mathcal N(S)$ & $\mathcal N(S)/S$ & $\mathcal N(S)/S^2$ & \\
\midrule
18   & 1    & 0.056 & 0.0031 & \\
100  & 92   & 0.92  & 0.0092 & \\
200  & 386  & 1.93  & 0.0097 & \\
300  & 840  & 2.80  & 0.0093 & \\
400  & 1496 & 3.74  & 0.0094 & \\
500  & 2210 & 4.42  & 0.0088 & \\
600  & 3067 & 5.11  & 0.0085 & \\
\bottomrule
\end{tabular}
\end{table}

The ratio $\mathcal N(S)/S$ grows roughly linearly with $S$ over this range, while $\mathcal N(S)/S^2$ stabilizes to within about $10\%$ of $0.009$; a power-law fit $\log\mathcal N(S)$ against $\log S$ over $50\le S\le600$ returns exponent $2.03$. This is far above the exponent $1$ guaranteed by Theorem~\ref{thm:density-lower}, confirming that the scaling law of Proposition~\ref{prop:scaling} captures only a vanishing fraction of the degeneracies at large $S$: at $S=600$ it accounts for $\lfloor600/18\rfloor=33$ of the $3067$ recorded, about one percent.

\subsection{A heuristic for the quadratic growth rate}

The empirical exponent $2$ is consistent with the following counting heuristic, of the birthday-paradox type standard in analogous Diophantine settings. The number of hyperbolic triads of sum $S$ is $\asymp S^2$, since $p$ ranges over $\asymp S$ values and, for each $p$, $q$ ranges over $\asymp S$ values with $r=S-p-q$ determined. Each such triad determines a reduced fraction $R=e_2/e_3$ whose denominator divides $e_3=pqr\le(S/3)^3$, so $R$ lies among $O(S^3)$ rationals of bounded height in a fixed interval. If the values $R$ arising from the $\asymp S^2$ triads of sum $S$ were distributed among these $O(S^3)$ possible values as though at random, a birthday-paradox count of coincidences would predict
\[
    N(S)\ \sim\ \frac{(\text{number of triads})^2}{\text{number of possible }R\text{-values}}\ \asymp\ \frac{(S^2)^2}{S^3}\ =\ S,
\]
matching the observed linear growth of $N(S)$, hence quadratic growth of the cumulative count $\mathcal N(S)=\sum_{s\le S}N(s)$. We state this as a precise conjecture rather than a theorem, since the heuristic treats the arithmetic denominators $e_3(p,q,r)$ as if independent and uniformly distributed, which we have not justified rigorously; in particular it does not by itself explain the sizable and structured population of degeneracies produced by Proposition~\ref{prop:scaling} and its non-scaled analogues (pairs related by a common integer factor extracted from both triples, which contribute a positive but lower-order density).

\begin{conjecture}[Quadratic density]\label{conj:density}
There is a constant $c>0$ such that
\[
    \mathcal N(S)\ \sim\ c\,S^2\qquad(S\to\infty).
\]
Equivalently, $N(S)=\Theta(S)$, so a positive proportion, of order $1/S$, of hyperbolic triads of sum $S$ participate in a two-coefficient degeneracy of sum $S$.
\end{conjecture}

Exact enumeration through $S=600$ is consistent with Conjecture~\ref{conj:density}, with $c$ near $0.0085$ at the top of the computed range (Table~\ref{tab:density}); whether $\mathcal N(S)/S^2$ has in fact stabilized, or is still drifting toward a different limiting constant ,  or a different power of $S$ altogether ,  cannot be resolved from data at this scale, and we leave the conjecture, together with the identification of $c$, open.

Each degeneracy, whether accounted for by Theorem~\ref{thm:density-lower} or only by Conjecture~\ref{conj:density}, exhibits a further pillow with $K(F)=3$: since Theorem~\ref{thmC} gives $K(F)\le3$ unconditionally, the set enumerated here is exactly the set of hyperbolic triangular pillows for which two heat coefficients do not suffice, and Theorem~\ref{thm:density-lower} already shows this set is infinite, of density at least $1/18$ among cone-order sums, with numerical evidence for substantially higher (quadratic-order cumulative) density.
````

### 25. rem:ncone

| field | value |
|---|---|
| status | CLAIM (FALSE) |
| dependencies | — |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/threshold/`, `review/audit/consistency/` |
| audit verdict | SERIOUS |
| in paper? | NO |
| note | Out of date: Theorem A proves K_mult<=n for all n (K_iso is infinite for n>=4); an n=4 witness {3,10,15,30}/{4,5,21,28} exists. Replace by Theorems A and C. |

*PC.20, `paper/main.tex` lines 493-495:*

````
\begin{remark}[Larger cone counts]\label{rem:ncone}
For an $n$-cone pillow $\mathcal{O}(m_1,\dots,m_n)$ ,  a sphere with $n$ cone points, hyperbolic when $\sum_i(1-\tfrac1{m_i})>2$ ,  the first $n$ leading heat coefficients again supply $n$ symmetric functions of the orders, and when these are independent they recover the multiset, so the upper bound $K\le n$ extends the $n=3$ case of Theorem~\ref{thmC}. The matching lower bound $K\ge n$ for $n\ge4$ would require two $n$-cone pillows agreeing in $n-1$ prescribed symmetric functions ,  an $(n-1)$-fold simultaneous Egyptian-fraction and power-sum system ,  for which we have neither a construction nor a non-existence proof; we leave it open.
\end{remark}
````

### 26. tab:enum

| field | value |
|---|---|
| status | COMPUTATION |
| dependencies | — |
| external inputs | — |
| source file | `paper/main.tex` |
| verifying script (existing) | make_table.py (external repo) |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | All 83 entries reproduced. |

*PC.21, `paper/main.tex` lines 504-504:*

````
As an independent cross-check of Theorem~\ref{thm:separation}, Table~\ref{tab:enum} lists \emph{every} hyperbolic triad with $10\le S_1\le18$ together with its reciprocal sum $R$ as an exact rational. The interval argument of Section~\ref{sec:threshold} predicts, and the table confirms, that $R$ is distinct across all triads of a common sum for $S_1\le17$, and that the only within-sum coincidence at $S_1\le18$ is the boldface pair $\{\mathcal{O}(2,8,8),\mathcal{O}(3,3,12)\}$ at $S_1=18$. The table plays no role in the proof; it is exhaustive supporting evidence.
````

### 27. prop:rigidity

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | Troyanov Thm A; equivalently Thurston Cor 13.3.7 |
| source file | `theory/definitions.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/locality/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*DF.3, `theory/definitions.tex` lines 69-74:*

````
\begin{proposition}[Rigidity of triangular pillows]\label{prop:rigidity}
If $\Orb,\Orb'\in\Pill_3$ have the same signature then they are isometric. Consequently
\[
  \Kiso(\Orb;\Pill_3)=\Kmult(\Orb;\Pill_3)\qquad\text{for every }\Orb\in\Pill_3 .
\]
\end{proposition}
````

### 28. eq:moduli

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | Troyanov; Thurston |
| source file | `theory/definitions.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/consistency/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Superseded by locality Prop 2.1 (all genera, one source); update the 'needs its own source' comment. |

*DF.4, `theory/definitions.tex` lines 95-105:*

````
By Troyanov's Theorem~A a hyperbolic cone metric on the sphere with prescribed angles is the same
datum as a conformal structure on the sphere with $n$ labelled marked points, and the space of such
structures has complex dimension $n-3$; Thurston's description of the space of shapes of
polyhedra with $n$ cone points, locally isometric to $\mathbb{C}H^{\,n-3}$, is the flat analogue
\cite{thurston1998}. Hence, for genus $0$,
\begin{equation}\label{eq:moduli}
  \dim_{\mathbb R}\mathcal M(0;m_1,\dots,m_n)=2n-6,
\end{equation}
which is $0$ for $n=3$ and positive for every $n\ge4$. (This is a two-step deduction from the two
cited sources and is flagged as such in \texttt{theory/teichmuller-dimension-sources.md}; for $g\ge1$
the corresponding count is not used here and would need its own source.)
````

### 29. thm:locality, prop:Kinf

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | locality Theorem 1 |
| external inputs | DGGW Thm 4.8, Def 4.7 |
| source file | `theory/definitions.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/locality/`, `review/audit/consistency/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Drop 'forward reference'/'conditional': locality Theorem 1 proves it. |

*DF.5, `theory/definitions.tex` lines 110-128:*

````
\begin{theorem}[Locality; forward reference]\label{thm:locality}
For every $j\ge1$ there is a function $\Phi_j$ of the signature alone with
$c_j(\Orb)=\Phi_j(\sigma(\Orb))$ for every closed orientable hyperbolic $2$-orbifold $\Orb$.
\end{theorem}

\noindent
Informally: heat invariants cannot see moduli. What is available now is the cone part: the
closed forms of Dryden--Gordon--Greenwald--Webb, Schueth and U\c{c}ar
\cite{dggw2008, schueth2019, ucar2017} depend only on the order $m_i$ of the cone point, for every
$j$ in U\c{c}ar's case, and were recomputed in exact arithmetic for $j\le6$
(\texttt{theory/cone-coefficients/}). What the locality theorem has to supply is the smooth part
at every order and the assembly of the pieces.

\begin{proposition}[Conditional on Theorem~\ref{thm:locality}]\label{prop:Kinf}
Suppose $\Pill$ contains two non-isometric orbifolds of the same signature $\sigma_0$. Then
$\Kiso(\Orb;\Pill)=\infty$ for every $\Orb\in\Pill$ with $\sigma(\Orb)=\sigma_0$. In particular,
if $\Pill\supseteq\mathcal M(0;m_1,\dots,m_n)$ with $n\ge4$, then $\Kiso(\Orb;\Pill)=\infty$ for all
$\Orb$ of signature $(0;m_1,\dots,m_n)$.
\end{proposition}
````

### 30. thm:Crestated

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | prop:recovery, prop:rigidity |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/definitions.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/audibility/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*DF.6, `theory/definitions.tex` lines 142-150:*

````
\begin{theorem}[Theorem~\ref{thmC}, restated]\label{thm:Crestated}
For every $\Orb\in\Pill_3$,
\[
  \Kiso(\Orb;\Pill_3)=\Kmult(\Orb;\Pill_3)\le3 .
\]
The value is $3$ exactly when $\Orb$ belongs to a two-coefficient collision, that is, when some
$\Orb'\in\Pill_3$ with $\sigma(\Orb')\ne\sigma(\Orb)$ has the same $R$ and the same $S_1$; for
instance for $\Orb(2,8,8)$ and $\Orb(3,3,12)$.
\end{theorem}
````

### 31. rem:nconerestated

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Theorem A, prop:Kinf |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/definitions.tex` |
| verifying script (existing) | theory/definitions-check.py |
| audit evidence | `review/audit/audibility/`, `review/audit/consistency/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | (a) is out of date: Theorem A proves injectivity for every n; remove the conditionals in (a)-(c). |

*DF.7, `theory/definitions.tex` lines 159-177:*

````
\begin{remark}[Larger cone counts, restated]\label{rem:nconerestated}
Let $\Pill_n$ be the class of hyperbolic spheres with $n\ge3$ cone points, $\sum_i(1-1/m_i)>2$.
\begin{enumerate}[label=(\alph*)]
\item \emph{Multiset level.} Modulo the universal smooth contributions, $c_1,\dots,c_n$ are the $n$
  functions $R,\,S_1,\,P_3,\,P_5,\dots,P_{2n-3}$ of the multiset $\{m_i\}$, with $P_k=\sum_im_i^k$ and
  $c_j$ carrying $P_{2j-3}$ for $j\ge2$ with a nonzero weight. If the map
  $\{m_i\}\mapsto(R,S_1,P_3,\dots,P_{2n-3})$ is injective on $n$-element multisets, then
  $\Kmult(\Orb;\Pill_n)\le n$. For $n=3$ this is Proposition~\ref{prop:recovery}; for $n\ge4$ injectivity is not
  proved here.
\item \emph{Isometry level.} For $n\ge4$, $\Kiso(\Orb;\Pill_n)=\infty$ by
  Proposition~\ref{prop:Kinf} and \eqref{eq:moduli}. The statement that the bound $K\le n$ extends
  the case $n=3$ of Theorem~\ref{thmC} is therefore valid for $\Kmult$ (conditionally on injectivity) and
  false for $\Kiso$; what singles out $n=3$ is rigidity, Proposition~\ref{prop:rigidity}.
\item \emph{A lower bound at $n=4$.} The multisets $\{3,10,15,30\}$ and $\{4,5,21,28\}$ are
  hyperbolic, have the same $S_1=58$, $R=8/15$ and $P_3=31402$, and have $P_5=25159618\ne21298618$
  (exact computation, \texttt{theory/definitions-check.py}). Hence $\Kmult\ge4$ for pillows with
  these signatures, and $\Kmult=4$ for them if the injectivity in (a) holds for $n=4$.
\end{enumerate}
\end{remark}
````

### 32. Heat input (cone polynomials p_l)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20, (4.35) |
| source file | `theory/audibility/proof.md` |
| verifying script (existing) | theory/cone-coefficients/verify_cone_coefficients.py |
| audit evidence | `review/audit/audibility/` |
| audit verdict | MINOR |
| in paper? | YES |
| note | Proved for all l from (4.25)/(4.33); cite Thm 4.20(ii) and (4.35); Holtz-Tyaglov is arXiv:0912.4703. |

*AU.0, `theory/audibility/proof.md` lines 26-50:*

````
**Input from the heat expansion (not re-derived here).** On a closed hyperbolic orbifold of
genus 0 with cone points of orders $m_1,\dots,m_n\ge2$, the heat coefficient of $t^{-1}$ is a
fixed multiple of the area $2\pi(n-2-R)$. Every smooth-stratum term is a fixed multiple of the
area. A cone point of order $m$ contributes $b_l(m)=K^l\,\tfrac1m\,p_l(m)$ at order $t^l$ (Gauss curvature $K=-1$),
where $p_l$ is an *even* polynomial of degree $2l+2$ with
$p_l(1)=0$ and leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$. Sources:
`review/hyperresearch/Q2-cone-coefficients.md`, Uçar (4.25)+(4.33), and Schueth Thm 4.1 for
$l\le2$. The explicit $p_0,\dots,p_3$ listed there are even with root $m=1$.

Hence $\sum_i b_l(m_i)$ is a rational combination of $R,P_1,P_3,\dots,P_{2l+1}$ (write
$P_k=\sum_i m_i^k$) with a nonzero coefficient on $P_{2l+1}$. The map from the first $n$ heat
coefficients to

$$\mathcal I_n(m)=(R,\;P_1,\;P_3,\;\dots,\;P_{2n-3})$$

is therefore triangular and invertible, for a fixed number $n$ of cone points. Throughout,
$e_k$ denotes the elementary symmetric functions of the $m_i$, $e_0=1$, and $R=e_{n-1}/e_n$. Two
polynomials are attached to $m$:

- $f(z)=\prod_i(1+m_iz)=\sum_k e_kz^k$;
- $p(z)=\prod_i(z+m_i)=\sum_k e_kz^{n-k}$.

$\Delta_k$ is the $k$-th Hurwitz determinant of $p$, following Holtz–Tyaglov (1.37); see
`sources/SOURCES.md`.

````

### 33. Theorem A (audibility of the cone orders)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Lemma 1 (parity) |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20; Orlando (Holtz-Tyaglov Thm 1.17) |
| source file | `theory/audibility/proof.md` |
| verifying script (existing) | theory/audibility/verify_elimination.py, orlando_check.py |
| audit evidence | `review/audit/audibility/` |
| audit verdict | NONE |
| in paper? | YES |
| note | Injectivity itself is PROVED (elementary); 'K_mult<=n' uses the cited heat input. Positive-real case is classical in substance (Steinig 1971 via Laurens): see THEOREM-A-PRIOR-ART.md. |

*AU.1, `theory/audibility/proof.md` lines 51-84:*

````
> **Theorem A (audibility of the cone orders; all $n\ge1$).** Let $m$ be a multiset of $n$
> nonzero complex numbers with $m_i+m_j\neq0$ for all $i<j$. Equivalently, by Orlando,
> $e_n\Delta_{n-1}\neq0$. Let $m'$ be any multiset of $n$ nonzero complex numbers with
> $\mathcal I_n(m')=\mathcal I_n(m)$. Then $m'=m$.
>
> In particular $\mathcal I_n$ is injective on multisets of positive reals, repeated orders
> allowed. So the first $n$ heat coefficients determine the cone-order multiset of an $n$-cone
> hyperbolic orbifold of genus 0: $K_{\rm mult}\le n$.

> **Theorem B (the linear system and its determinant).** Let $T(z)=\tanh\bigl(\sum_{k\ {\rm odd}}
> P_kz^k/k\bigr)$. The $n-1$ equations
> $$e_{2j+1}-\sum_{i=0}^{j}T_{2i+1}\,e_{2j-2i}=0\qquad (j=0,\dots,n-2),$$
> together with $e_{n-1}-Re_n=0$, form a square linear system $M\,e=b$ in $e_1,\dots,e_n$.
> Its coefficients are polynomials in the heat invariants $\mathcal I_n$ alone, and the true
> $e$ solves it. For every $n\ge2$,
> $$\det M=c_n\,\frac{\Delta_{n-1}(p)}{e_n}=c_n\,\frac{\prod_{i<j}(m_i+m_j)}{\prod_i m_i},
> \qquad c_n\in\mathbb Q^\times .$$
> For $n=3,\dots,8$, $c_n=+1,+1,-1,-1,+1,+1$ (`linear_system.py`).

> **Theorem C (the fibres of $n-1$ invariants; sharpness).**
>
> 1. *Pair criterion.* Let $m,m'$ be multisets of $n$ nonzero complex numbers, and let
>    $Q(z)=\prod_i(z-m_i)\prod_j(z+m'_j)$. Then $\mathcal I_{n-1}$ agree, meaning $R$ and
>    $P_1,\dots,P_{2n-5}$, if and only if $Q(z)-Q(-z)=2\kappa z^3$ for some $\kappa$. If
>    $m_i+m_j\neq0$ for $i<j$, then $\kappa=0$ exactly when $m'=m$.
> 2. *Real sharpness, every $n\ge2$.* Every multiset of $n$ pairwise distinct positive reals lies
>    on a real curve of positive-real multisets sharing $\mathcal I_{n-1}$. Over the positive
>    reals, $n-1$ invariants never suffice.
> 3. *Integer sharpness ($n\ge3$, the range where hyperbolic genus-0 orbifolds exist).* It is
>    equivalent to finding a positive rational pair $m\neq m'$ (as multisets), i.e. a point off
>    all permutation components
>    on the pair variety, by scaling. It holds for $n=3$ and $n=4$ with explicit witnesses. For
>    $n=5$ no witness exists with all orders $\le120$ (216,071,394 multisets, exhaustive). For
>    $n\ge5$ it is open.
````

### 34. Theorem B (linear system, det M)

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | Orlando |
| source file | `theory/audibility/proof.md` |
| verifying script (existing) | theory/audibility/linear_system.py |
| audit evidence | `review/audit/audibility/`, `review/audit/stability/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Replace 'c_n in Q^x, computed for n<=8' by c_n=(-1)^{n(n+1)/2} for all n (Lemma S2.1; reproved independently). Cite Korobov-Bugaevskaya 2016 §3. |

*AU.1, `theory/audibility/proof.md` lines 51-84:*

````
> **Theorem A (audibility of the cone orders; all $n\ge1$).** Let $m$ be a multiset of $n$
> nonzero complex numbers with $m_i+m_j\neq0$ for all $i<j$. Equivalently, by Orlando,
> $e_n\Delta_{n-1}\neq0$. Let $m'$ be any multiset of $n$ nonzero complex numbers with
> $\mathcal I_n(m')=\mathcal I_n(m)$. Then $m'=m$.
>
> In particular $\mathcal I_n$ is injective on multisets of positive reals, repeated orders
> allowed. So the first $n$ heat coefficients determine the cone-order multiset of an $n$-cone
> hyperbolic orbifold of genus 0: $K_{\rm mult}\le n$.

> **Theorem B (the linear system and its determinant).** Let $T(z)=\tanh\bigl(\sum_{k\ {\rm odd}}
> P_kz^k/k\bigr)$. The $n-1$ equations
> $$e_{2j+1}-\sum_{i=0}^{j}T_{2i+1}\,e_{2j-2i}=0\qquad (j=0,\dots,n-2),$$
> together with $e_{n-1}-Re_n=0$, form a square linear system $M\,e=b$ in $e_1,\dots,e_n$.
> Its coefficients are polynomials in the heat invariants $\mathcal I_n$ alone, and the true
> $e$ solves it. For every $n\ge2$,
> $$\det M=c_n\,\frac{\Delta_{n-1}(p)}{e_n}=c_n\,\frac{\prod_{i<j}(m_i+m_j)}{\prod_i m_i},
> \qquad c_n\in\mathbb Q^\times .$$
> For $n=3,\dots,8$, $c_n=+1,+1,-1,-1,+1,+1$ (`linear_system.py`).

> **Theorem C (the fibres of $n-1$ invariants; sharpness).**
>
> 1. *Pair criterion.* Let $m,m'$ be multisets of $n$ nonzero complex numbers, and let
>    $Q(z)=\prod_i(z-m_i)\prod_j(z+m'_j)$. Then $\mathcal I_{n-1}$ agree, meaning $R$ and
>    $P_1,\dots,P_{2n-5}$, if and only if $Q(z)-Q(-z)=2\kappa z^3$ for some $\kappa$. If
>    $m_i+m_j\neq0$ for $i<j$, then $\kappa=0$ exactly when $m'=m$.
> 2. *Real sharpness, every $n\ge2$.* Every multiset of $n$ pairwise distinct positive reals lies
>    on a real curve of positive-real multisets sharing $\mathcal I_{n-1}$. Over the positive
>    reals, $n-1$ invariants never suffice.
> 3. *Integer sharpness ($n\ge3$, the range where hyperbolic genus-0 orbifolds exist).* It is
>    equivalent to finding a positive rational pair $m\neq m'$ (as multisets), i.e. a point off
>    all permutation components
>    on the pair variety, by scaling. It holds for $n=3$ and $n=4$ with explicit witnesses. For
>    $n=5$ no witness exists with all orders $\le120$ (216,071,394 multisets, exhaustive). For
>    $n\ge5$ it is open.
````

### 35. Theorem C(1)-(2) (pair criterion; real sharpness)

| field | value |
|---|---|
| status | PROVED |
| dependencies | Theorem A, Lemma 1 |
| external inputs | — |
| source file | `theory/audibility/proof.md` |
| verifying script (existing) | theory/audibility/sharpness_search.py |
| audit evidence | `review/audit/audibility/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*AU.1, `theory/audibility/proof.md` lines 51-84:*

````
> **Theorem A (audibility of the cone orders; all $n\ge1$).** Let $m$ be a multiset of $n$
> nonzero complex numbers with $m_i+m_j\neq0$ for all $i<j$. Equivalently, by Orlando,
> $e_n\Delta_{n-1}\neq0$. Let $m'$ be any multiset of $n$ nonzero complex numbers with
> $\mathcal I_n(m')=\mathcal I_n(m)$. Then $m'=m$.
>
> In particular $\mathcal I_n$ is injective on multisets of positive reals, repeated orders
> allowed. So the first $n$ heat coefficients determine the cone-order multiset of an $n$-cone
> hyperbolic orbifold of genus 0: $K_{\rm mult}\le n$.

> **Theorem B (the linear system and its determinant).** Let $T(z)=\tanh\bigl(\sum_{k\ {\rm odd}}
> P_kz^k/k\bigr)$. The $n-1$ equations
> $$e_{2j+1}-\sum_{i=0}^{j}T_{2i+1}\,e_{2j-2i}=0\qquad (j=0,\dots,n-2),$$
> together with $e_{n-1}-Re_n=0$, form a square linear system $M\,e=b$ in $e_1,\dots,e_n$.
> Its coefficients are polynomials in the heat invariants $\mathcal I_n$ alone, and the true
> $e$ solves it. For every $n\ge2$,
> $$\det M=c_n\,\frac{\Delta_{n-1}(p)}{e_n}=c_n\,\frac{\prod_{i<j}(m_i+m_j)}{\prod_i m_i},
> \qquad c_n\in\mathbb Q^\times .$$
> For $n=3,\dots,8$, $c_n=+1,+1,-1,-1,+1,+1$ (`linear_system.py`).

> **Theorem C (the fibres of $n-1$ invariants; sharpness).**
>
> 1. *Pair criterion.* Let $m,m'$ be multisets of $n$ nonzero complex numbers, and let
>    $Q(z)=\prod_i(z-m_i)\prod_j(z+m'_j)$. Then $\mathcal I_{n-1}$ agree, meaning $R$ and
>    $P_1,\dots,P_{2n-5}$, if and only if $Q(z)-Q(-z)=2\kappa z^3$ for some $\kappa$. If
>    $m_i+m_j\neq0$ for $i<j$, then $\kappa=0$ exactly when $m'=m$.
> 2. *Real sharpness, every $n\ge2$.* Every multiset of $n$ pairwise distinct positive reals lies
>    on a real curve of positive-real multisets sharing $\mathcal I_{n-1}$. Over the positive
>    reals, $n-1$ invariants never suffice.
> 3. *Integer sharpness ($n\ge3$, the range where hyperbolic genus-0 orbifolds exist).* It is
>    equivalent to finding a positive rational pair $m\neq m'$ (as multisets), i.e. a point off
>    all permutation components
>    on the pair variety, by scaling. It holds for $n=3$ and $n=4$ with explicit witnesses. For
>    $n=5$ no witness exists with all orders $\le120$ (216,071,394 multisets, exhaustive). For
>    $n\ge5$ it is open.
````

### 36. Theorem C(3) (integer sharpness)

| field | value |
|---|---|
| status | COMPUTATION |
| dependencies | Theorem C(1) |
| external inputs | — |
| source file | `theory/audibility/proof.md` |
| verifying script (existing) | theory/audibility/sharpness_search.py |
| audit evidence | `review/audit/audibility/` |
| audit verdict | NONE |
| in paper? | YES |
| note | Proved for n=3,4 by exact witnesses (n=4: 11 witness classes with orders<=90, 9 primitive - so 'one primitive witness' and 'rare for n>=4' in the notes should be revised); n=5: none with orders<=120 (reproduced); n>=5 OPEN. |

*AU.1, `theory/audibility/proof.md` lines 51-84:*

````
> **Theorem A (audibility of the cone orders; all $n\ge1$).** Let $m$ be a multiset of $n$
> nonzero complex numbers with $m_i+m_j\neq0$ for all $i<j$. Equivalently, by Orlando,
> $e_n\Delta_{n-1}\neq0$. Let $m'$ be any multiset of $n$ nonzero complex numbers with
> $\mathcal I_n(m')=\mathcal I_n(m)$. Then $m'=m$.
>
> In particular $\mathcal I_n$ is injective on multisets of positive reals, repeated orders
> allowed. So the first $n$ heat coefficients determine the cone-order multiset of an $n$-cone
> hyperbolic orbifold of genus 0: $K_{\rm mult}\le n$.

> **Theorem B (the linear system and its determinant).** Let $T(z)=\tanh\bigl(\sum_{k\ {\rm odd}}
> P_kz^k/k\bigr)$. The $n-1$ equations
> $$e_{2j+1}-\sum_{i=0}^{j}T_{2i+1}\,e_{2j-2i}=0\qquad (j=0,\dots,n-2),$$
> together with $e_{n-1}-Re_n=0$, form a square linear system $M\,e=b$ in $e_1,\dots,e_n$.
> Its coefficients are polynomials in the heat invariants $\mathcal I_n$ alone, and the true
> $e$ solves it. For every $n\ge2$,
> $$\det M=c_n\,\frac{\Delta_{n-1}(p)}{e_n}=c_n\,\frac{\prod_{i<j}(m_i+m_j)}{\prod_i m_i},
> \qquad c_n\in\mathbb Q^\times .$$
> For $n=3,\dots,8$, $c_n=+1,+1,-1,-1,+1,+1$ (`linear_system.py`).

> **Theorem C (the fibres of $n-1$ invariants; sharpness).**
>
> 1. *Pair criterion.* Let $m,m'$ be multisets of $n$ nonzero complex numbers, and let
>    $Q(z)=\prod_i(z-m_i)\prod_j(z+m'_j)$. Then $\mathcal I_{n-1}$ agree, meaning $R$ and
>    $P_1,\dots,P_{2n-5}$, if and only if $Q(z)-Q(-z)=2\kappa z^3$ for some $\kappa$. If
>    $m_i+m_j\neq0$ for $i<j$, then $\kappa=0$ exactly when $m'=m$.
> 2. *Real sharpness, every $n\ge2$.* Every multiset of $n$ pairwise distinct positive reals lies
>    on a real curve of positive-real multisets sharing $\mathcal I_{n-1}$. Over the positive
>    reals, $n-1$ invariants never suffice.
> 3. *Integer sharpness ($n\ge3$, the range where hyperbolic genus-0 orbifolds exist).* It is
>    equivalent to finding a positive rational pair $m\neq m'$ (as multisets), i.e. a point off
>    all permutation components
>    on the pair variety, by scaling. It holds for $n=3$ and $n=4$ with explicit witnesses. For
>    $n=5$ no witness exists with all orders $\le120$ (216,071,394 multisets, exhaustive). For
>    $n\ge5$ it is open.
````

*AU.4, `theory/audibility/proof.md` lines 217-225:*

````
In the table, $\Phi(z):=p(z)p'(-z)-p'(z)p(-z)$ with $p=\prod(z+m_i)$ and $p'=\prod(z+m'_j)$.
It satisfies $\Phi=(-1)^{n+1}\bigl(Q(z)-Q(-z)\bigr)$.

| $n$ | witness sharing $\mathcal I_{n-1}$ | separated by | $\Phi(z)$ |
|---|---|---|---|
| 3 | $\{2,8,8\}$, $\{3,3,12\}$ ($R=3/4$, $S_1=18$) | $P_3$: 1032 vs 1782 | $500\,z^3$ |
| 4 | $\{3,10,15,30\}$, $\{4,5,21,28\}$ ($R=8/15$, $S_1=58$, $P_3=31402$) | $P_5$: 25159618 vs 21298618 | $1544400\,z^3$ |
| 5 | none with orders $\le60$ (7,028,847 multisets) or $\le120$ (216,071,394) | | |

````

### 37. Integer sharpness K_mult >= n for n >= 5

| field | value |
|---|---|
| status | OPEN |
| dependencies | Theorem C(1) |
| external inputs | — |
| source file | `theory/audibility/proof.md` |
| verifying script (existing) | theory/audibility/sharpness_search.py |
| audit evidence | `review/audit/audibility/` |
| audit verdict | NONE |
| in paper? | YES |
| note | Stated as open; no witness with orders <= 120 at n=5 (reproduced). Do not claim more. |

*AU.1, `theory/audibility/proof.md` lines 51-84:*

````
> **Theorem A (audibility of the cone orders; all $n\ge1$).** Let $m$ be a multiset of $n$
> nonzero complex numbers with $m_i+m_j\neq0$ for all $i<j$. Equivalently, by Orlando,
> $e_n\Delta_{n-1}\neq0$. Let $m'$ be any multiset of $n$ nonzero complex numbers with
> $\mathcal I_n(m')=\mathcal I_n(m)$. Then $m'=m$.
>
> In particular $\mathcal I_n$ is injective on multisets of positive reals, repeated orders
> allowed. So the first $n$ heat coefficients determine the cone-order multiset of an $n$-cone
> hyperbolic orbifold of genus 0: $K_{\rm mult}\le n$.

> **Theorem B (the linear system and its determinant).** Let $T(z)=\tanh\bigl(\sum_{k\ {\rm odd}}
> P_kz^k/k\bigr)$. The $n-1$ equations
> $$e_{2j+1}-\sum_{i=0}^{j}T_{2i+1}\,e_{2j-2i}=0\qquad (j=0,\dots,n-2),$$
> together with $e_{n-1}-Re_n=0$, form a square linear system $M\,e=b$ in $e_1,\dots,e_n$.
> Its coefficients are polynomials in the heat invariants $\mathcal I_n$ alone, and the true
> $e$ solves it. For every $n\ge2$,
> $$\det M=c_n\,\frac{\Delta_{n-1}(p)}{e_n}=c_n\,\frac{\prod_{i<j}(m_i+m_j)}{\prod_i m_i},
> \qquad c_n\in\mathbb Q^\times .$$
> For $n=3,\dots,8$, $c_n=+1,+1,-1,-1,+1,+1$ (`linear_system.py`).

> **Theorem C (the fibres of $n-1$ invariants; sharpness).**
>
> 1. *Pair criterion.* Let $m,m'$ be multisets of $n$ nonzero complex numbers, and let
>    $Q(z)=\prod_i(z-m_i)\prod_j(z+m'_j)$. Then $\mathcal I_{n-1}$ agree, meaning $R$ and
>    $P_1,\dots,P_{2n-5}$, if and only if $Q(z)-Q(-z)=2\kappa z^3$ for some $\kappa$. If
>    $m_i+m_j\neq0$ for $i<j$, then $\kappa=0$ exactly when $m'=m$.
> 2. *Real sharpness, every $n\ge2$.* Every multiset of $n$ pairwise distinct positive reals lies
>    on a real curve of positive-real multisets sharing $\mathcal I_{n-1}$. Over the positive
>    reals, $n-1$ invariants never suffice.
> 3. *Integer sharpness ($n\ge3$, the range where hyperbolic genus-0 orbifolds exist).* It is
>    equivalent to finding a positive rational pair $m\neq m'$ (as multisets), i.e. a point off
>    all permutation components
>    on the pair variety, by scaling. It holds for $n=3$ and $n=4$ with explicit witnesses. For
>    $n=5$ no witness exists with all orders $\le120$ (216,071,394 multisets, exhaustive). For
>    $n\ge5$ it is open.
````

### 38. Lemma 1 (parity)

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `theory/audibility/proof.md` |
| verifying script (existing) | theory/audibility/verify_elimination.py |
| audit evidence | `review/audit/audibility/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*AU.2, `theory/audibility/proof.md` lines 88-91:*

````
**Lemma 1 (parity).** In $\mathbb Q[x_1,\dots,x_N]$ let $s_j=\sum x_i^j$ and let $e_j$ be the
elementary symmetric functions. For odd $j$, $e_j$ lies in the ideal generated by
$s_1,s_3,\dots,s_j$. Conversely, $s_j$ lies in the ideal generated by $e_1,e_3,\dots,e_j$.

````

### 39. Remark 2 (Jacobian), Remark 3 (padding)

| field | value |
|---|---|
| status | PROVED |
| dependencies | Theorem A |
| external inputs | — |
| source file | `theory/audibility/proof.md` |
| verifying script (existing) | theory/audibility/sharpness_search.py |
| audit evidence | `review/audit/audibility/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Rename the Jacobian constant (clashes with Theorem B's c_n); say 'hyperbolic genus-0'. |

*AU.3, `theory/audibility/proof.md` lines 123-136:*

````
2. Repeated orders are allowed. The Jacobian of $\mathcal I_n$ is
   $c_n\,V(m)\prod_{i<j}(m_i+m_j)/\prod m_i^2$ with $V(m)=\prod_{i<j}(m_j-m_i)$ and
   $c_n=-\prod_{r<n}(2r-1)$ (checked $n\le7$).
   It vanishes on the diagonals $m_i=m_j$, so the map is not an immersion there, yet it is
   injective. The obstruction to injectivity is the Orlando factor $\prod(m_i+m_j)$, not the
   Vandermonde $V(m)$.
3. Different numbers of cone points. An order-1 "cone" is invisible to every heat coefficient
   ($b_l(1)=0$, and the area $2\pi(n-2-R)$ is unchanged by adding $m=1$). An orbifold with
   $n'\le n$ cone points padded by ones is therefore an $n$-multiset of positive reals. By
   Theorem A, the first $n$ coefficients distinguish an $n$-cone orbifold from every genus-0
   orbifold with at most $n$ cone points.
   - The comparison with orbifolds having *more* cone points is not covered by Theorem A.
   - A search of 3-cone against 4-cone orbifolds with orders $\le60$ found no pair sharing three
     coefficients (`sharpness_search.py`, part C).
````

### 40. Heat input (H1)-(H3)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20, (4.35); DGGW Thm 4.8, Def 4.7 |
| source file | `theory/signatures/proof.md` |
| verifying script (existing) | theory/signatures/heat_structure.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*SG.0, `theory/signatures/proof.md` lines 41-75:*

````
## 1. Setting, heat input and notation

$\mathrm{Sig}$ denotes the set of signatures $\sigma=(g;m_1,\dots,m_n)$ of closed orientable
hyperbolic 2-orbifolds (`definitions.tex`, `def:signature`). Here $g\ge0$, each $m_i\ge2$, and
$m=\{m_i\}$ is a multiset. Write
$$n=|m|,\qquad R(m)=\sum_i\frac1{m_i},\qquad P_j(m)=\sum_im_i^j,\qquad
s(\sigma)=2g-2+\sum_i\Bigl(1-\frac1{m_i}\Bigr)=-\chi=\frac{\mathrm{Area}}{2\pi}>0 .$$
$H_k(\mathcal O)=(c_1,\dots,c_k)$ are the first $k$ heat coefficients (`def:heatcoef`), and
$K_{\rm mult}(\mathcal O;\mathcal P)$ is as in `def:K`.

**Heat input (H).** This is the only analytic input. Every quoted statement was fetched and is
recorded in `literature.md` and `../cone-coefficients/ucar-source.md`.

- (H1) *Smooth part.* At constant curvature $\kappa$ the smooth-stratum coefficient $a_\nu$ is
  $\mathrm{vol}(\mathcal O)$ times a constant depending only on $\nu$ and $\kappa$. This is
  Uçar, Thm 4.20(i), eq. (4.35), for every $\nu$. The structure (smooth part plus one term per
  singular stratum) is DGGW, Thm 4.8 and Def. 4.7.
- (H2) *Cone part.* A cone point of order $k$ contributes $b_l(k)$ at order $t^l$, with
  $b_l(k)=K^l\sum_{i=0}^{l}\frac{2}{4^ii!}c^{\mathbb S}_{l-i}(\pi/k)$ and $c^{\mathbb S}$ given
  by (4.25). This is Uçar, Thm 4.20(ii), eqs. (4.33)–(4.34).
- (H3) The expansion runs in the powers $t^{-1},t^0,t^1,\dots$ (`def:heatcoef`). Hence, at
  $K=-1$,
  $$c_1=\frac{\mathrm{Area}}{4\pi}=\frac s2,\qquad c_{l+2}=\alpha_l\,\mathrm{Area}+C_l(m),\qquad
  C_l(m):=\sum_ib_l(m_i)\quad(l\ge0),$$
  with universal constants $\alpha_l$.

Two consequences follow. Genus enters the heat data only through the area. And two orbifolds of
equal area have equal $c_{l+2}$ exactly when they have equal $C_l$.

The first consequence is an inference, not a fetched sentence: by Gauss–Bonnet the area is
$2\pi s$, and $g$ appears nowhere else. `literature.md` ("What is fetched vs. what is inferred")
records this.

Put $\psi_k(x)=x^{2k-1}-x^{-1}$ for $k\ge1$, and $\Psi_k(m)=\sum_i\psi_k(m_i)=P_{2k-1}(m)-R(m)$.

````

### 41. Lemma 1 (cone polynomials)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/signatures/proof.md` |
| verifying script (existing) | theory/signatures/heat_structure.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*SG.1, `theory/signatures/proof.md` lines 78-81:*

````
**Lemma 1 (cone polynomials, every $l$).** $p_l(k):=k\,b_l(k)/K^l$ is an even polynomial of
degree $2l+2$ with $p_l(1)=0$. Its leading coefficient is
$|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$.

````

### 42. Lemma 2 (triangular basis)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Lemma 1 |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/signatures/proof.md` |
| verifying script (existing) | theory/signatures/heat_structure.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*SG.2, `theory/signatures/proof.md` lines 95-99:*

````
**Lemma 2 (triangular basis).** $\phi_l(x):=p_l(x)/x=\sum_{k=1}^{l+1}a_{l,k}\,\psi_k(x)$ with
$a_{l,l+1}\ne0$. Hence, for multisets $m,m'$ and $L\ge1$:
$$C_l(m)=C_l(m')\ (0\le l\le L-2)\iff\Psi_k(m)=\Psi_k(m')\ (1\le k\le L-1).$$
The direction "$\Leftarrow$" does not use $a_{l,l+1}\neq0$.

````

### 43. Lemma 3 (padding)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Lemma 1 |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/signatures/proof.md` |
| verifying script (existing) | theory/signatures/heat_structure.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*SG.3, `theory/signatures/proof.md` lines 105-106:*

````
**Lemma 3 (padding).** Adjoining points of order 1 changes neither the area nor any $C_l$.

````

### 44. Lemma 4 (reduction) / lem:sigdata

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Lemmas 2-3 |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| verifying script (existing) | theory/signatures/heat_structure.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Write 1<=j<=2L-3 (j odd); index the a_{l,k} sum from k=0; add '(g;m) in Sig' to the converse. |

*SG.4, `theory/signatures/proof.md` lines 110-132:*

````
**Lemma 4 (reduction).** Let $\sigma=(g;m)$ and $\sigma'=(g';m')$ have $n$ and $n'$ cone
points, and let $L\ge1$. Then $H_L(\mathcal O)=H_L(\mathcal O')$ if and only if
$$2g+n-R(m)=2g'+n'-R(m')\quad\text{and}\quad\Psi_k(m)=\Psi_k(m')\ (1\le k\le L-1).\tag{4.1}$$
Assume (4.1). Then $d:=R(m')-R(m)=2(g'-g)+n'-n$ is an integer. Put
$$U=m\uplus\{1\}^{\max(d,0)},\qquad V=m'\uplus\{1\}^{\max(-d,0)} .$$
Then
$$R(U)=R(V),\qquad P_j(U)=P_j(V)\ \ (j\text{ odd},\ j\le2L-3),\qquad |V|-|U|=2(g-g'),\tag{4.2}$$
and
$$|U|+|V|=2\max\bigl(n+g-g',\;n'+g'-g\bigr).\tag{4.3}$$

Conversely, let $U=m\uplus\{1\}^a$ and $V=m'\uplus\{1\}^b$ be any paddings, and let $g,g'\ge0$.
If (4.2) holds, then $(g;m)$ and $(g';m')$ have equal area and equal first $L$ heat
coefficients.

*In terms of the mirror multiset.* Pad both multisets to a common length $N$, write $R_N$, $P_{j,N}$
for the padded sums, and put $X=m_N\uplus(-m'_N)$. Equal area is
$$s_{-1}(X)=R_N-R'_N=2(g-g').$$
Equal $C_0,\dots,C_{L-2}$ is then equivalent to
$$s_j(X)=P_{j,N}-P'_{j,N}=2(g-g')\qquad (j\text{ odd},\ j\le2L-3),$$
the *same* multiple $2(g-g')$ for every odd $j$ and for $j=-1$. This is the unique solution of
the linear system formed by the cone-sum differences, computed in `heat_structure.py` (4) for
$L\le16$. It follows for all $L$ from Lemma 2, because $\sum_ka_{l,k}=0$.

````

*SG.13, `theory/signatures/statements.tex` lines 11-117:*

````
\subsection{The signature from finitely many heat coefficients}\label{subsec:signature}

Throughout, $\Sig$ is the class of all closed orientable hyperbolic $2$-orbifolds, and $\Pill_0\subset\Sig$
the subclass of genus $0$. For a signature $(g;m_1,\dots,m_n)$ write $R=\sum_i1/m_i$,
$P_j=\sum_im_i^{\,j}$ and $s=2g-2+n-R=\operatorname{Area}/2\pi$.

\begin{lemma}[Heat data of a signature]\label{lem:sigdata}
For $\Orb,\Orb'\in\Sig$ with signatures $(g;m)$, $(g';m')$ and $L\ge1$, the following are equivalent:
\begin{enumerate}[label=(\roman*)]
\item $H_L(\Orb)=H_L(\Orb')$;
\item there are paddings $U=m\uplus\{1\}^a$, $V=m'\uplus\{1\}^b$ with
\[
  R(U)=R(V),\qquad P_j(U)=P_j(V)\ \ (j\ \text{odd},\ j\le 2L-3),\qquad |V|-|U|=2(g-g').
\]
\end{enumerate}
Moreover, if the multisets are padded to a common length and $X=m\uplus(-m')$, then (i) holds if and only if
$\sum_{x\in X}x^{-1}=\sum_{x\in X}x^{j}=2(g-g')$ for every odd $j\le2L-3$.
\end{lemma}

\noindent
The input is the structure of the heat expansion at constant curvature
\cite[Theorem~4.8]{dggw2008}, \cite[Theorem~4.20]{ucar2017}: the smooth part of every coefficient is a fixed
multiple of the area, and a cone point of order $k$ contributes $(-1)^l k^{-1}p_l(k)$ at order $t^l$ (curvature $-1$), with
$p_l$ even, $p_l(1)=0$ and leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$. The genus enters only
through the area.

\begin{theorem}[Separation]\label{thm:sigsep}
Let $\Orb,\Orb'\in\Sig$ have signatures $(g;m_1,\dots,m_n)\neq(g';m'_1,\dots,m'_{n'})$ and equal first $L$
heat coefficients. Let $U,V$ be any paddings as in Lemma~\ref{lem:sigdata}(ii), and let $U^*,V^*$ be
obtained by removing their common elements (these do not depend on the choice of paddings). Then
$|U^*|+|V^*|\ge 2L+2$. In particular, if
\[
  L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),
\]
then $H_L(\Orb)=H_L(\Orb')$ implies $\sigma(\Orb)=\sigma(\Orb')$.
\end{theorem}

\begin{corollary}[Genus and cone orders from $\lfloor\operatorname{Area}/\pi\rfloor+4$ coefficients]\label{cor:sigarea}
For every $\Orb\in\Sig$,
\[
  \Kmult(\Orb;\Sig)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
That is, the first $\lfloor\operatorname{Area}(\Orb)/\pi\rfloor+4$ heat coefficients determine the genus and
the cone-order multiset of $\Orb$ among all closed orientable hyperbolic $2$-orbifolds. The number is
read off from the first coefficient $c_1=\operatorname{Area}/4\pi$.
\end{corollary}

\begin{theorem}[Cone count in genus $0$]\label{thm:sigcount}
Let $\Orb\in\Pill_0$ have $n$ cone points. Then $n\le\operatorname{Area}(\Orb)/\pi+4$, with equality exactly
when every cone order is $2$, and
\[
  \Kmult(\Orb;\Pill_0)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
More precisely, $H_{\max(n,n')}$ separates $\Orb$ from every $\Orb'\in\Pill_0$ with $n'$ cone points and a
different cone-order multiset. In particular the cone count $n$ is determined without being known in
advance.
\end{theorem}

\begin{theorem}[No uniform number of coefficients]\label{thm:signonuniform}
\leavevmode
\begin{enumerate}[label=(\alph*)]
\item For every $L\ge2$ and every $g'\ge0$ there are orbifolds in $\Sig$ of genus $g'+1$ and $g'$ with equal
  first $L$ heat coefficients; for $g'=0$ they may be taken of area less than $2\pi(4^{L-1}-1)$.
\item For every $k\ge2$ there are orbifolds in $\Pill_0$ with $n$ and $n+1$ cone points, for some $n$, with
  equal first $k$ heat coefficients.
\end{enumerate}
Hence $\sup_{\Orb}\Kmult(\Orb;\Sig)=\sup_{\Orb}\Kmult(\Orb;\Pill_0)=\infty$, and no fixed number of heat
coefficients determines the genus in $\Sig$ or the cone count in $\Pill_0$.
\end{theorem}

\begin{corollary}[Growth]\label{cor:siggrowth}
Let $f(A)=\max\{\Kmult(\Orb;\Sig):\operatorname{Area}(\Orb)\le A\}$. For $A\ge6\pi$,
\[
  \Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\ \Bigl\lfloor\frac{A}{\pi}\Bigr\rfloor+4 .
\]
\end{corollary}

\begin{example}\label{ex:siggenus}
The orbifolds of signatures $(1;15)$ and $(0;3,3,5,5)$ have the same first two heat coefficients, and
$(1;15,15,15)$ and $(0;3,3,5,7,7,21)$ have the same first three (exact computation). In each pair the genera
differ.
\end{example}

\begin{remark}[Relation to $\Kmult$ and $\Kiso$]\label{rem:sigK}
Theorem~\ref{thm:sigsep} with $g=g'=0$ and $n=n'$ is the statement $\Kmult(\Orb;\Pill_n)\le n$ for the class
$\Pill_n$ of hyperbolic spheres with $n$ cone points, i.e.\ the injectivity that Remark~\ref{rem:nconerestated}(a) leaves conditional, now proved
independently (\texttt{theory/audibility/proof.md}, Theorem~A). Corollary~\ref{cor:sigarea} extends it to all genera and all cone
counts at once, at the price of a bound that depends on the area, and Theorem~\ref{thm:signonuniform}
shows that some such dependence is unavoidable. All of this concerns $\Kmult$; by \eqref{eq:Kcompare}
and Proposition~\ref{prop:Kinf} (conditional on Theorem~\ref{thm:locality}), $\Kiso$ remains infinite
whenever two non-isometric orbifolds share a signature.
\end{remark}

\begin{remark}[What short-time heat flow detects]\label{rem:sigphysics}
This remark is interpretation, not part of any proof. Heat at short times is local: it sees curvature,
hence the area, and each cone point through a fixed function of its order. A handle has no local
signature and is heard only through the area it uses up. Comparing two orbifolds through the mirror
multiset $U^*\uplus(-V^*)$, a genus difference appears as an imbalance between its positive and negative
parts, and Theorem~\ref{thm:sigsep} says that the heat coefficients force the mirror multiset to be
symmetric, hence balanced, once there are enough of them relative to its size. A handle therefore costs
no more coefficients to hear than a cone point.
\end{remark}

% Exact extent. Lemma sigdata, Theorems sigsep, sigcount, signonuniform and Corollaries sigarea,
% siggrowth are proved for all L given the cited heat input (proof.md sections 2-4). The constructions of
% Theorem signonuniform are built and checked with the actual cone coefficients for L <= 6 (a) and
% k <= 3 (b). Open: whether f(A) grows linearly (proof.md section 7).
````

### 45. Theorem S / thm:sigsep

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Lemma 4, Lemma 5 (parity) |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| verifying script (existing) | theory/signatures/genus.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*SG.5, `theory/signatures/proof.md` lines 152-157:*

````
**Theorem S.** Let $\mathcal O,\mathcal O'$ be closed orientable hyperbolic 2-orbifolds with
$\sigma(\mathcal O)\neq\sigma(\mathcal O')$ and $H_L(\mathcal O)=H_L(\mathcal O')$. Let $U,V$ be
as in Lemma 4, and let $U^*,V^*$ be obtained by cancelling the elements they have in common.
Then
$$|U^*|+|V^*|\ \ge\ 2L+2 .$$

````

*SG.13, `theory/signatures/statements.tex` lines 11-117:*

````
\subsection{The signature from finitely many heat coefficients}\label{subsec:signature}

Throughout, $\Sig$ is the class of all closed orientable hyperbolic $2$-orbifolds, and $\Pill_0\subset\Sig$
the subclass of genus $0$. For a signature $(g;m_1,\dots,m_n)$ write $R=\sum_i1/m_i$,
$P_j=\sum_im_i^{\,j}$ and $s=2g-2+n-R=\operatorname{Area}/2\pi$.

\begin{lemma}[Heat data of a signature]\label{lem:sigdata}
For $\Orb,\Orb'\in\Sig$ with signatures $(g;m)$, $(g';m')$ and $L\ge1$, the following are equivalent:
\begin{enumerate}[label=(\roman*)]
\item $H_L(\Orb)=H_L(\Orb')$;
\item there are paddings $U=m\uplus\{1\}^a$, $V=m'\uplus\{1\}^b$ with
\[
  R(U)=R(V),\qquad P_j(U)=P_j(V)\ \ (j\ \text{odd},\ j\le 2L-3),\qquad |V|-|U|=2(g-g').
\]
\end{enumerate}
Moreover, if the multisets are padded to a common length and $X=m\uplus(-m')$, then (i) holds if and only if
$\sum_{x\in X}x^{-1}=\sum_{x\in X}x^{j}=2(g-g')$ for every odd $j\le2L-3$.
\end{lemma}

\noindent
The input is the structure of the heat expansion at constant curvature
\cite[Theorem~4.8]{dggw2008}, \cite[Theorem~4.20]{ucar2017}: the smooth part of every coefficient is a fixed
multiple of the area, and a cone point of order $k$ contributes $(-1)^l k^{-1}p_l(k)$ at order $t^l$ (curvature $-1$), with
$p_l$ even, $p_l(1)=0$ and leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$. The genus enters only
through the area.

\begin{theorem}[Separation]\label{thm:sigsep}
Let $\Orb,\Orb'\in\Sig$ have signatures $(g;m_1,\dots,m_n)\neq(g';m'_1,\dots,m'_{n'})$ and equal first $L$
heat coefficients. Let $U,V$ be any paddings as in Lemma~\ref{lem:sigdata}(ii), and let $U^*,V^*$ be
obtained by removing their common elements (these do not depend on the choice of paddings). Then
$|U^*|+|V^*|\ge 2L+2$. In particular, if
\[
  L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),
\]
then $H_L(\Orb)=H_L(\Orb')$ implies $\sigma(\Orb)=\sigma(\Orb')$.
\end{theorem}

\begin{corollary}[Genus and cone orders from $\lfloor\operatorname{Area}/\pi\rfloor+4$ coefficients]\label{cor:sigarea}
For every $\Orb\in\Sig$,
\[
  \Kmult(\Orb;\Sig)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
That is, the first $\lfloor\operatorname{Area}(\Orb)/\pi\rfloor+4$ heat coefficients determine the genus and
the cone-order multiset of $\Orb$ among all closed orientable hyperbolic $2$-orbifolds. The number is
read off from the first coefficient $c_1=\operatorname{Area}/4\pi$.
\end{corollary}

\begin{theorem}[Cone count in genus $0$]\label{thm:sigcount}
Let $\Orb\in\Pill_0$ have $n$ cone points. Then $n\le\operatorname{Area}(\Orb)/\pi+4$, with equality exactly
when every cone order is $2$, and
\[
  \Kmult(\Orb;\Pill_0)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
More precisely, $H_{\max(n,n')}$ separates $\Orb$ from every $\Orb'\in\Pill_0$ with $n'$ cone points and a
different cone-order multiset. In particular the cone count $n$ is determined without being known in
advance.
\end{theorem}

\begin{theorem}[No uniform number of coefficients]\label{thm:signonuniform}
\leavevmode
\begin{enumerate}[label=(\alph*)]
\item For every $L\ge2$ and every $g'\ge0$ there are orbifolds in $\Sig$ of genus $g'+1$ and $g'$ with equal
  first $L$ heat coefficients; for $g'=0$ they may be taken of area less than $2\pi(4^{L-1}-1)$.
\item For every $k\ge2$ there are orbifolds in $\Pill_0$ with $n$ and $n+1$ cone points, for some $n$, with
  equal first $k$ heat coefficients.
\end{enumerate}
Hence $\sup_{\Orb}\Kmult(\Orb;\Sig)=\sup_{\Orb}\Kmult(\Orb;\Pill_0)=\infty$, and no fixed number of heat
coefficients determines the genus in $\Sig$ or the cone count in $\Pill_0$.
\end{theorem}

\begin{corollary}[Growth]\label{cor:siggrowth}
Let $f(A)=\max\{\Kmult(\Orb;\Sig):\operatorname{Area}(\Orb)\le A\}$. For $A\ge6\pi$,
\[
  \Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\ \Bigl\lfloor\frac{A}{\pi}\Bigr\rfloor+4 .
\]
\end{corollary}

\begin{example}\label{ex:siggenus}
The orbifolds of signatures $(1;15)$ and $(0;3,3,5,5)$ have the same first two heat coefficients, and
$(1;15,15,15)$ and $(0;3,3,5,7,7,21)$ have the same first three (exact computation). In each pair the genera
differ.
\end{example}

\begin{remark}[Relation to $\Kmult$ and $\Kiso$]\label{rem:sigK}
Theorem~\ref{thm:sigsep} with $g=g'=0$ and $n=n'$ is the statement $\Kmult(\Orb;\Pill_n)\le n$ for the class
$\Pill_n$ of hyperbolic spheres with $n$ cone points, i.e.\ the injectivity that Remark~\ref{rem:nconerestated}(a) leaves conditional, now proved
independently (\texttt{theory/audibility/proof.md}, Theorem~A). Corollary~\ref{cor:sigarea} extends it to all genera and all cone
counts at once, at the price of a bound that depends on the area, and Theorem~\ref{thm:signonuniform}
shows that some such dependence is unavoidable. All of this concerns $\Kmult$; by \eqref{eq:Kcompare}
and Proposition~\ref{prop:Kinf} (conditional on Theorem~\ref{thm:locality}), $\Kiso$ remains infinite
whenever two non-isometric orbifolds share a signature.
\end{remark}

\begin{remark}[What short-time heat flow detects]\label{rem:sigphysics}
This remark is interpretation, not part of any proof. Heat at short times is local: it sees curvature,
hence the area, and each cone point through a fixed function of its order. A handle has no local
signature and is heard only through the area it uses up. Comparing two orbifolds through the mirror
multiset $U^*\uplus(-V^*)$, a genus difference appears as an imbalance between its positive and negative
parts, and Theorem~\ref{thm:sigsep} says that the heat coefficients force the mirror multiset to be
symmetric, hence balanced, once there are enough of them relative to its size. A handle therefore costs
no more coefficients to hear than a cone point.
\end{remark}

% Exact extent. Lemma sigdata, Theorems sigsep, sigcount, signonuniform and Corollaries sigarea,
% siggrowth are proved for all L given the cited heat input (proof.md sections 2-4). The constructions of
% Theorem signonuniform are built and checked with the actual cone coefficients for L <= 6 (a) and
% k <= 3 (b). Open: whether f(A) grows linearly (proof.md section 7).
````

### 46. Corollary S1

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Theorem S |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/signatures/proof.md` |
| verifying script (existing) | theory/signatures/genus.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*SG.6, `theory/signatures/proof.md` lines 179-182:*

````
**Corollary S1 (pairwise form).** If $H_L(\mathcal O)=H_L(\mathcal O')$ with
$$L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),$$
then $\sigma(\mathcal O)=\sigma(\mathcal O')$.

````

### 47. Corollary S2 / cor:sigarea

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Corollary S1 |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20; Gauss-Bonnet |
| source file | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| verifying script (existing) | theory/signatures/genus.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | Novelty wording per PRIORITY.md: first explicit count uniform over all closed orientable hyperbolic 2-orbifolds. |

*SG.7, `theory/signatures/proof.md` lines 185-191:*

````
**Corollary S2 (area form: genus and cone orders from finitely many coefficients).** Let
$\mathcal O$ have area $A$. Any closed orientable hyperbolic 2-orbifold $\mathcal O'$ with
$H_{\lfloor A/\pi\rfloor+4}(\mathcal O')=H_{\lfloor A/\pi\rfloor+4}(\mathcal O)$ has the same
genus and the same cone-order multiset. In the notation of `def:K`, with
$\mathrm{Sig}$ the class of all closed orientable hyperbolic 2-orbifolds,
$$K_{\rm mult}(\mathcal O;\mathrm{Sig})\ \le\ \Bigl\lfloor\frac{\mathrm{Area}(\mathcal O)}{\pi}\Bigr\rfloor+4 .$$

````

*SG.13, `theory/signatures/statements.tex` lines 11-117:*

````
\subsection{The signature from finitely many heat coefficients}\label{subsec:signature}

Throughout, $\Sig$ is the class of all closed orientable hyperbolic $2$-orbifolds, and $\Pill_0\subset\Sig$
the subclass of genus $0$. For a signature $(g;m_1,\dots,m_n)$ write $R=\sum_i1/m_i$,
$P_j=\sum_im_i^{\,j}$ and $s=2g-2+n-R=\operatorname{Area}/2\pi$.

\begin{lemma}[Heat data of a signature]\label{lem:sigdata}
For $\Orb,\Orb'\in\Sig$ with signatures $(g;m)$, $(g';m')$ and $L\ge1$, the following are equivalent:
\begin{enumerate}[label=(\roman*)]
\item $H_L(\Orb)=H_L(\Orb')$;
\item there are paddings $U=m\uplus\{1\}^a$, $V=m'\uplus\{1\}^b$ with
\[
  R(U)=R(V),\qquad P_j(U)=P_j(V)\ \ (j\ \text{odd},\ j\le 2L-3),\qquad |V|-|U|=2(g-g').
\]
\end{enumerate}
Moreover, if the multisets are padded to a common length and $X=m\uplus(-m')$, then (i) holds if and only if
$\sum_{x\in X}x^{-1}=\sum_{x\in X}x^{j}=2(g-g')$ for every odd $j\le2L-3$.
\end{lemma}

\noindent
The input is the structure of the heat expansion at constant curvature
\cite[Theorem~4.8]{dggw2008}, \cite[Theorem~4.20]{ucar2017}: the smooth part of every coefficient is a fixed
multiple of the area, and a cone point of order $k$ contributes $(-1)^l k^{-1}p_l(k)$ at order $t^l$ (curvature $-1$), with
$p_l$ even, $p_l(1)=0$ and leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$. The genus enters only
through the area.

\begin{theorem}[Separation]\label{thm:sigsep}
Let $\Orb,\Orb'\in\Sig$ have signatures $(g;m_1,\dots,m_n)\neq(g';m'_1,\dots,m'_{n'})$ and equal first $L$
heat coefficients. Let $U,V$ be any paddings as in Lemma~\ref{lem:sigdata}(ii), and let $U^*,V^*$ be
obtained by removing their common elements (these do not depend on the choice of paddings). Then
$|U^*|+|V^*|\ge 2L+2$. In particular, if
\[
  L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),
\]
then $H_L(\Orb)=H_L(\Orb')$ implies $\sigma(\Orb)=\sigma(\Orb')$.
\end{theorem}

\begin{corollary}[Genus and cone orders from $\lfloor\operatorname{Area}/\pi\rfloor+4$ coefficients]\label{cor:sigarea}
For every $\Orb\in\Sig$,
\[
  \Kmult(\Orb;\Sig)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
That is, the first $\lfloor\operatorname{Area}(\Orb)/\pi\rfloor+4$ heat coefficients determine the genus and
the cone-order multiset of $\Orb$ among all closed orientable hyperbolic $2$-orbifolds. The number is
read off from the first coefficient $c_1=\operatorname{Area}/4\pi$.
\end{corollary}

\begin{theorem}[Cone count in genus $0$]\label{thm:sigcount}
Let $\Orb\in\Pill_0$ have $n$ cone points. Then $n\le\operatorname{Area}(\Orb)/\pi+4$, with equality exactly
when every cone order is $2$, and
\[
  \Kmult(\Orb;\Pill_0)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
More precisely, $H_{\max(n,n')}$ separates $\Orb$ from every $\Orb'\in\Pill_0$ with $n'$ cone points and a
different cone-order multiset. In particular the cone count $n$ is determined without being known in
advance.
\end{theorem}

\begin{theorem}[No uniform number of coefficients]\label{thm:signonuniform}
\leavevmode
\begin{enumerate}[label=(\alph*)]
\item For every $L\ge2$ and every $g'\ge0$ there are orbifolds in $\Sig$ of genus $g'+1$ and $g'$ with equal
  first $L$ heat coefficients; for $g'=0$ they may be taken of area less than $2\pi(4^{L-1}-1)$.
\item For every $k\ge2$ there are orbifolds in $\Pill_0$ with $n$ and $n+1$ cone points, for some $n$, with
  equal first $k$ heat coefficients.
\end{enumerate}
Hence $\sup_{\Orb}\Kmult(\Orb;\Sig)=\sup_{\Orb}\Kmult(\Orb;\Pill_0)=\infty$, and no fixed number of heat
coefficients determines the genus in $\Sig$ or the cone count in $\Pill_0$.
\end{theorem}

\begin{corollary}[Growth]\label{cor:siggrowth}
Let $f(A)=\max\{\Kmult(\Orb;\Sig):\operatorname{Area}(\Orb)\le A\}$. For $A\ge6\pi$,
\[
  \Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\ \Bigl\lfloor\frac{A}{\pi}\Bigr\rfloor+4 .
\]
\end{corollary}

\begin{example}\label{ex:siggenus}
The orbifolds of signatures $(1;15)$ and $(0;3,3,5,5)$ have the same first two heat coefficients, and
$(1;15,15,15)$ and $(0;3,3,5,7,7,21)$ have the same first three (exact computation). In each pair the genera
differ.
\end{example}

\begin{remark}[Relation to $\Kmult$ and $\Kiso$]\label{rem:sigK}
Theorem~\ref{thm:sigsep} with $g=g'=0$ and $n=n'$ is the statement $\Kmult(\Orb;\Pill_n)\le n$ for the class
$\Pill_n$ of hyperbolic spheres with $n$ cone points, i.e.\ the injectivity that Remark~\ref{rem:nconerestated}(a) leaves conditional, now proved
independently (\texttt{theory/audibility/proof.md}, Theorem~A). Corollary~\ref{cor:sigarea} extends it to all genera and all cone
counts at once, at the price of a bound that depends on the area, and Theorem~\ref{thm:signonuniform}
shows that some such dependence is unavoidable. All of this concerns $\Kmult$; by \eqref{eq:Kcompare}
and Proposition~\ref{prop:Kinf} (conditional on Theorem~\ref{thm:locality}), $\Kiso$ remains infinite
whenever two non-isometric orbifolds share a signature.
\end{remark}

\begin{remark}[What short-time heat flow detects]\label{rem:sigphysics}
This remark is interpretation, not part of any proof. Heat at short times is local: it sees curvature,
hence the area, and each cone point through a fixed function of its order. A handle has no local
signature and is heard only through the area it uses up. Comparing two orbifolds through the mirror
multiset $U^*\uplus(-V^*)$, a genus difference appears as an imbalance between its positive and negative
parts, and Theorem~\ref{thm:sigsep} says that the heat coefficients force the mirror multiset to be
symmetric, hence balanced, once there are enough of them relative to its size. A handle therefore costs
no more coefficients to hear than a cone point.
\end{remark}

% Exact extent. Lemma sigdata, Theorems sigsep, sigcount, signonuniform and Corollaries sigarea,
% siggrowth are proved for all L given the cited heat input (proof.md sections 2-4). The constructions of
% Theorem signonuniform are built and checked with the actual cone coefficients for L <= 6 (a) and
% k <= 3 (b). Open: whether f(A) grows linearly (proof.md section 7).
````

### 48. Theorem T1 / thm:sigcount

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Theorem A or Corollary S1 |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| verifying script (existing) | theory/signatures/cone_count.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*SG.8, `theory/signatures/proof.md` lines 202-211:*

````
**Theorem T1 (cone count and cone orders, genus 0).** Let $\mathcal O$ be a hyperbolic
genus-0 orbifold of area $A$ with $n$ cone points.

1. $n\le A/\pi+4$, with equality iff every order is 2.
2. The first $\lfloor A/\pi\rfloor+4$ heat coefficients determine the cone-order multiset, and
   in particular $n$, among *all* hyperbolic genus-0 orbifolds. The number $n$ need not be known
   in advance.
3. More sharply, the first $\max(n,n')$ coefficients separate it from every genus-0 orbifold
   with $n'$ cone points and a different multiset.

````

*SG.13, `theory/signatures/statements.tex` lines 11-117:*

````
\subsection{The signature from finitely many heat coefficients}\label{subsec:signature}

Throughout, $\Sig$ is the class of all closed orientable hyperbolic $2$-orbifolds, and $\Pill_0\subset\Sig$
the subclass of genus $0$. For a signature $(g;m_1,\dots,m_n)$ write $R=\sum_i1/m_i$,
$P_j=\sum_im_i^{\,j}$ and $s=2g-2+n-R=\operatorname{Area}/2\pi$.

\begin{lemma}[Heat data of a signature]\label{lem:sigdata}
For $\Orb,\Orb'\in\Sig$ with signatures $(g;m)$, $(g';m')$ and $L\ge1$, the following are equivalent:
\begin{enumerate}[label=(\roman*)]
\item $H_L(\Orb)=H_L(\Orb')$;
\item there are paddings $U=m\uplus\{1\}^a$, $V=m'\uplus\{1\}^b$ with
\[
  R(U)=R(V),\qquad P_j(U)=P_j(V)\ \ (j\ \text{odd},\ j\le 2L-3),\qquad |V|-|U|=2(g-g').
\]
\end{enumerate}
Moreover, if the multisets are padded to a common length and $X=m\uplus(-m')$, then (i) holds if and only if
$\sum_{x\in X}x^{-1}=\sum_{x\in X}x^{j}=2(g-g')$ for every odd $j\le2L-3$.
\end{lemma}

\noindent
The input is the structure of the heat expansion at constant curvature
\cite[Theorem~4.8]{dggw2008}, \cite[Theorem~4.20]{ucar2017}: the smooth part of every coefficient is a fixed
multiple of the area, and a cone point of order $k$ contributes $(-1)^l k^{-1}p_l(k)$ at order $t^l$ (curvature $-1$), with
$p_l$ even, $p_l(1)=0$ and leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$. The genus enters only
through the area.

\begin{theorem}[Separation]\label{thm:sigsep}
Let $\Orb,\Orb'\in\Sig$ have signatures $(g;m_1,\dots,m_n)\neq(g';m'_1,\dots,m'_{n'})$ and equal first $L$
heat coefficients. Let $U,V$ be any paddings as in Lemma~\ref{lem:sigdata}(ii), and let $U^*,V^*$ be
obtained by removing their common elements (these do not depend on the choice of paddings). Then
$|U^*|+|V^*|\ge 2L+2$. In particular, if
\[
  L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),
\]
then $H_L(\Orb)=H_L(\Orb')$ implies $\sigma(\Orb)=\sigma(\Orb')$.
\end{theorem}

\begin{corollary}[Genus and cone orders from $\lfloor\operatorname{Area}/\pi\rfloor+4$ coefficients]\label{cor:sigarea}
For every $\Orb\in\Sig$,
\[
  \Kmult(\Orb;\Sig)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
That is, the first $\lfloor\operatorname{Area}(\Orb)/\pi\rfloor+4$ heat coefficients determine the genus and
the cone-order multiset of $\Orb$ among all closed orientable hyperbolic $2$-orbifolds. The number is
read off from the first coefficient $c_1=\operatorname{Area}/4\pi$.
\end{corollary}

\begin{theorem}[Cone count in genus $0$]\label{thm:sigcount}
Let $\Orb\in\Pill_0$ have $n$ cone points. Then $n\le\operatorname{Area}(\Orb)/\pi+4$, with equality exactly
when every cone order is $2$, and
\[
  \Kmult(\Orb;\Pill_0)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
More precisely, $H_{\max(n,n')}$ separates $\Orb$ from every $\Orb'\in\Pill_0$ with $n'$ cone points and a
different cone-order multiset. In particular the cone count $n$ is determined without being known in
advance.
\end{theorem}

\begin{theorem}[No uniform number of coefficients]\label{thm:signonuniform}
\leavevmode
\begin{enumerate}[label=(\alph*)]
\item For every $L\ge2$ and every $g'\ge0$ there are orbifolds in $\Sig$ of genus $g'+1$ and $g'$ with equal
  first $L$ heat coefficients; for $g'=0$ they may be taken of area less than $2\pi(4^{L-1}-1)$.
\item For every $k\ge2$ there are orbifolds in $\Pill_0$ with $n$ and $n+1$ cone points, for some $n$, with
  equal first $k$ heat coefficients.
\end{enumerate}
Hence $\sup_{\Orb}\Kmult(\Orb;\Sig)=\sup_{\Orb}\Kmult(\Orb;\Pill_0)=\infty$, and no fixed number of heat
coefficients determines the genus in $\Sig$ or the cone count in $\Pill_0$.
\end{theorem}

\begin{corollary}[Growth]\label{cor:siggrowth}
Let $f(A)=\max\{\Kmult(\Orb;\Sig):\operatorname{Area}(\Orb)\le A\}$. For $A\ge6\pi$,
\[
  \Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\ \Bigl\lfloor\frac{A}{\pi}\Bigr\rfloor+4 .
\]
\end{corollary}

\begin{example}\label{ex:siggenus}
The orbifolds of signatures $(1;15)$ and $(0;3,3,5,5)$ have the same first two heat coefficients, and
$(1;15,15,15)$ and $(0;3,3,5,7,7,21)$ have the same first three (exact computation). In each pair the genera
differ.
\end{example}

\begin{remark}[Relation to $\Kmult$ and $\Kiso$]\label{rem:sigK}
Theorem~\ref{thm:sigsep} with $g=g'=0$ and $n=n'$ is the statement $\Kmult(\Orb;\Pill_n)\le n$ for the class
$\Pill_n$ of hyperbolic spheres with $n$ cone points, i.e.\ the injectivity that Remark~\ref{rem:nconerestated}(a) leaves conditional, now proved
independently (\texttt{theory/audibility/proof.md}, Theorem~A). Corollary~\ref{cor:sigarea} extends it to all genera and all cone
counts at once, at the price of a bound that depends on the area, and Theorem~\ref{thm:signonuniform}
shows that some such dependence is unavoidable. All of this concerns $\Kmult$; by \eqref{eq:Kcompare}
and Proposition~\ref{prop:Kinf} (conditional on Theorem~\ref{thm:locality}), $\Kiso$ remains infinite
whenever two non-isometric orbifolds share a signature.
\end{remark}

\begin{remark}[What short-time heat flow detects]\label{rem:sigphysics}
This remark is interpretation, not part of any proof. Heat at short times is local: it sees curvature,
hence the area, and each cone point through a fixed function of its order. A handle has no local
signature and is heard only through the area it uses up. Comparing two orbifolds through the mirror
multiset $U^*\uplus(-V^*)$, a genus difference appears as an imbalance between its positive and negative
parts, and Theorem~\ref{thm:sigsep} says that the heat coefficients force the mirror multiset to be
symmetric, hence balanced, once there are enough of them relative to its size. A handle therefore costs
no more coefficients to hear than a cone point.
\end{remark}

% Exact extent. Lemma sigdata, Theorems sigsep, sigcount, signonuniform and Corollaries sigarea,
% siggrowth are proved for all L given the cited heat input (proof.md sections 2-4). The constructions of
% Theorem signonuniform are built and checked with the actual cone coefficients for L <= 6 (a) and
% k <= 3 (b). Open: whether f(A) grows linearly (proof.md section 7).
````

### 49. Proposition P (Prouhet)

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `theory/signatures/proof.md` |
| verifying script (existing) | theory/signatures/genus.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*SG.9, `theory/signatures/proof.md` lines 235-241:*

````
**Proposition P (Prouhet; Thue–Morse).** Let $t(i)$ be the parity of the binary digit sum of
$i$. Let $D\ge1$, and let $T_0,T_1$ split $\{0,\dots,2^D-1\}$ according to $t(i)$. Then:

1. $\sum_{T_0}f=\sum_{T_1}f$ for every polynomial $f$ of degree $<D$.
2. For every $c>0$ and $h>0$,
   $$\sum_{i<2^D}\frac{(-1)^{t(i)}}{hi+c}>0 .$$

````

### 50. Theorem N / thm:signonuniform

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Proposition P, Lemma 4 |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| verifying script (existing) | theory/signatures/genus.py, cone_count.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | P1: true for all L>=2, k>=2 (all of (a)-(g) re-proved). A smaller (b) witness exists: 23 vs 24 cone points sharing three coefficients. |

*SG.10, `theory/signatures/proof.md` lines 247-263:*

````
**Theorem N (non-uniformity).**

(a) *Genus.* For every $L\ge2$ and every $g'\ge0$ there are closed orientable hyperbolic
2-orbifolds of genus $g'+1$ and $g'$ with equal first $L$ heat coefficients. For $g'=0$ they can
be chosen with area $<2\pi(4^{L-1}-1)$.

(b) *Cone count.* For every $k\ge2$ there are hyperbolic genus-0 orbifolds with $n$ and $n+1$
cone points, for some $n$, with equal first $k$ heat coefficients.

(c) Consequently:

- no fixed number of heat coefficients determines the genus among closed orientable hyperbolic
  2-orbifolds;
- no fixed number determines the cone count among genus-0 ones;
- $\sup_{\mathcal O}K_{\rm mult}(\mathcal O;\mathcal P)=\infty$, both for $\mathcal P=\mathrm{Sig}$
  and for $\mathcal P$ the genus-0 class.

````

*SG.13, `theory/signatures/statements.tex` lines 11-117:*

````
\subsection{The signature from finitely many heat coefficients}\label{subsec:signature}

Throughout, $\Sig$ is the class of all closed orientable hyperbolic $2$-orbifolds, and $\Pill_0\subset\Sig$
the subclass of genus $0$. For a signature $(g;m_1,\dots,m_n)$ write $R=\sum_i1/m_i$,
$P_j=\sum_im_i^{\,j}$ and $s=2g-2+n-R=\operatorname{Area}/2\pi$.

\begin{lemma}[Heat data of a signature]\label{lem:sigdata}
For $\Orb,\Orb'\in\Sig$ with signatures $(g;m)$, $(g';m')$ and $L\ge1$, the following are equivalent:
\begin{enumerate}[label=(\roman*)]
\item $H_L(\Orb)=H_L(\Orb')$;
\item there are paddings $U=m\uplus\{1\}^a$, $V=m'\uplus\{1\}^b$ with
\[
  R(U)=R(V),\qquad P_j(U)=P_j(V)\ \ (j\ \text{odd},\ j\le 2L-3),\qquad |V|-|U|=2(g-g').
\]
\end{enumerate}
Moreover, if the multisets are padded to a common length and $X=m\uplus(-m')$, then (i) holds if and only if
$\sum_{x\in X}x^{-1}=\sum_{x\in X}x^{j}=2(g-g')$ for every odd $j\le2L-3$.
\end{lemma}

\noindent
The input is the structure of the heat expansion at constant curvature
\cite[Theorem~4.8]{dggw2008}, \cite[Theorem~4.20]{ucar2017}: the smooth part of every coefficient is a fixed
multiple of the area, and a cone point of order $k$ contributes $(-1)^l k^{-1}p_l(k)$ at order $t^l$ (curvature $-1$), with
$p_l$ even, $p_l(1)=0$ and leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$. The genus enters only
through the area.

\begin{theorem}[Separation]\label{thm:sigsep}
Let $\Orb,\Orb'\in\Sig$ have signatures $(g;m_1,\dots,m_n)\neq(g';m'_1,\dots,m'_{n'})$ and equal first $L$
heat coefficients. Let $U,V$ be any paddings as in Lemma~\ref{lem:sigdata}(ii), and let $U^*,V^*$ be
obtained by removing their common elements (these do not depend on the choice of paddings). Then
$|U^*|+|V^*|\ge 2L+2$. In particular, if
\[
  L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),
\]
then $H_L(\Orb)=H_L(\Orb')$ implies $\sigma(\Orb)=\sigma(\Orb')$.
\end{theorem}

\begin{corollary}[Genus and cone orders from $\lfloor\operatorname{Area}/\pi\rfloor+4$ coefficients]\label{cor:sigarea}
For every $\Orb\in\Sig$,
\[
  \Kmult(\Orb;\Sig)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
That is, the first $\lfloor\operatorname{Area}(\Orb)/\pi\rfloor+4$ heat coefficients determine the genus and
the cone-order multiset of $\Orb$ among all closed orientable hyperbolic $2$-orbifolds. The number is
read off from the first coefficient $c_1=\operatorname{Area}/4\pi$.
\end{corollary}

\begin{theorem}[Cone count in genus $0$]\label{thm:sigcount}
Let $\Orb\in\Pill_0$ have $n$ cone points. Then $n\le\operatorname{Area}(\Orb)/\pi+4$, with equality exactly
when every cone order is $2$, and
\[
  \Kmult(\Orb;\Pill_0)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
More precisely, $H_{\max(n,n')}$ separates $\Orb$ from every $\Orb'\in\Pill_0$ with $n'$ cone points and a
different cone-order multiset. In particular the cone count $n$ is determined without being known in
advance.
\end{theorem}

\begin{theorem}[No uniform number of coefficients]\label{thm:signonuniform}
\leavevmode
\begin{enumerate}[label=(\alph*)]
\item For every $L\ge2$ and every $g'\ge0$ there are orbifolds in $\Sig$ of genus $g'+1$ and $g'$ with equal
  first $L$ heat coefficients; for $g'=0$ they may be taken of area less than $2\pi(4^{L-1}-1)$.
\item For every $k\ge2$ there are orbifolds in $\Pill_0$ with $n$ and $n+1$ cone points, for some $n$, with
  equal first $k$ heat coefficients.
\end{enumerate}
Hence $\sup_{\Orb}\Kmult(\Orb;\Sig)=\sup_{\Orb}\Kmult(\Orb;\Pill_0)=\infty$, and no fixed number of heat
coefficients determines the genus in $\Sig$ or the cone count in $\Pill_0$.
\end{theorem}

\begin{corollary}[Growth]\label{cor:siggrowth}
Let $f(A)=\max\{\Kmult(\Orb;\Sig):\operatorname{Area}(\Orb)\le A\}$. For $A\ge6\pi$,
\[
  \Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\ \Bigl\lfloor\frac{A}{\pi}\Bigr\rfloor+4 .
\]
\end{corollary}

\begin{example}\label{ex:siggenus}
The orbifolds of signatures $(1;15)$ and $(0;3,3,5,5)$ have the same first two heat coefficients, and
$(1;15,15,15)$ and $(0;3,3,5,7,7,21)$ have the same first three (exact computation). In each pair the genera
differ.
\end{example}

\begin{remark}[Relation to $\Kmult$ and $\Kiso$]\label{rem:sigK}
Theorem~\ref{thm:sigsep} with $g=g'=0$ and $n=n'$ is the statement $\Kmult(\Orb;\Pill_n)\le n$ for the class
$\Pill_n$ of hyperbolic spheres with $n$ cone points, i.e.\ the injectivity that Remark~\ref{rem:nconerestated}(a) leaves conditional, now proved
independently (\texttt{theory/audibility/proof.md}, Theorem~A). Corollary~\ref{cor:sigarea} extends it to all genera and all cone
counts at once, at the price of a bound that depends on the area, and Theorem~\ref{thm:signonuniform}
shows that some such dependence is unavoidable. All of this concerns $\Kmult$; by \eqref{eq:Kcompare}
and Proposition~\ref{prop:Kinf} (conditional on Theorem~\ref{thm:locality}), $\Kiso$ remains infinite
whenever two non-isometric orbifolds share a signature.
\end{remark}

\begin{remark}[What short-time heat flow detects]\label{rem:sigphysics}
This remark is interpretation, not part of any proof. Heat at short times is local: it sees curvature,
hence the area, and each cone point through a fixed function of its order. A handle has no local
signature and is heard only through the area it uses up. Comparing two orbifolds through the mirror
multiset $U^*\uplus(-V^*)$, a genus difference appears as an imbalance between its positive and negative
parts, and Theorem~\ref{thm:sigsep} says that the heat coefficients force the mirror multiset to be
symmetric, hence balanced, once there are enough of them relative to its size. A handle therefore costs
no more coefficients to hear than a cone point.
\end{remark}

% Exact extent. Lemma sigdata, Theorems sigsep, sigcount, signonuniform and Corollaries sigarea,
% siggrowth are proved for all L given the cited heat input (proof.md sections 2-4). The constructions of
% Theorem signonuniform are built and checked with the actual cone coefficients for L <= 6 (a) and
% k <= 3 (b). Open: whether f(A) grows linearly (proof.md section 7).
````

### 51. Construction ranges remark

| field | value |
|---|---|
| status | COMPUTATION |
| dependencies | Theorem N |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/signatures/proof.md` |
| verifying script (existing) | theory/signatures/genus.py, cone_count.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | 'k>=4 impractical' is specific to the greedy route; the doubling construction is exact for every k. |

*SG.11, `theory/signatures/proof.md` lines 305-313:*

````
The constructions are built and checked with the actual cone coefficients $b_l$:

- (a) for $L=2,\dots,6$ (`genus.py` (A)). Each pair shares *exactly* $L$ coefficients; the
  $L=6$ pair has 1023 and 1025 cone points.
- (b) for $k=2,3$ (`cone_count.py` (d)): 9 vs 10 and 103 vs 104 cone points, sharing exactly
  2 and 3 coefficients.

For $k\ge4$ the greedy denominators grow doubly exponentially, which makes exact verification
impractical. The proof above covers every $k$.
````

### 52. Corollary N1 / cor:siggrowth

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Corollary S2, Theorem N(a) |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*SG.12, `theory/signatures/proof.md` lines 315-319:*

````
**Corollary N1 (growth).** Let $f(A)=\max\{K_{\rm mult}(\mathcal O;\mathrm{Sig}):
\mathrm{Area}(\mathcal O)\le A\}$. For $A\ge6\pi$,
$$\Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\
\Bigl\lfloor\frac A\pi\Bigr\rfloor+4 .$$

````

*SG.13, `theory/signatures/statements.tex` lines 11-117:*

````
\subsection{The signature from finitely many heat coefficients}\label{subsec:signature}

Throughout, $\Sig$ is the class of all closed orientable hyperbolic $2$-orbifolds, and $\Pill_0\subset\Sig$
the subclass of genus $0$. For a signature $(g;m_1,\dots,m_n)$ write $R=\sum_i1/m_i$,
$P_j=\sum_im_i^{\,j}$ and $s=2g-2+n-R=\operatorname{Area}/2\pi$.

\begin{lemma}[Heat data of a signature]\label{lem:sigdata}
For $\Orb,\Orb'\in\Sig$ with signatures $(g;m)$, $(g';m')$ and $L\ge1$, the following are equivalent:
\begin{enumerate}[label=(\roman*)]
\item $H_L(\Orb)=H_L(\Orb')$;
\item there are paddings $U=m\uplus\{1\}^a$, $V=m'\uplus\{1\}^b$ with
\[
  R(U)=R(V),\qquad P_j(U)=P_j(V)\ \ (j\ \text{odd},\ j\le 2L-3),\qquad |V|-|U|=2(g-g').
\]
\end{enumerate}
Moreover, if the multisets are padded to a common length and $X=m\uplus(-m')$, then (i) holds if and only if
$\sum_{x\in X}x^{-1}=\sum_{x\in X}x^{j}=2(g-g')$ for every odd $j\le2L-3$.
\end{lemma}

\noindent
The input is the structure of the heat expansion at constant curvature
\cite[Theorem~4.8]{dggw2008}, \cite[Theorem~4.20]{ucar2017}: the smooth part of every coefficient is a fixed
multiple of the area, and a cone point of order $k$ contributes $(-1)^l k^{-1}p_l(k)$ at order $t^l$ (curvature $-1$), with
$p_l$ even, $p_l(1)=0$ and leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$. The genus enters only
through the area.

\begin{theorem}[Separation]\label{thm:sigsep}
Let $\Orb,\Orb'\in\Sig$ have signatures $(g;m_1,\dots,m_n)\neq(g';m'_1,\dots,m'_{n'})$ and equal first $L$
heat coefficients. Let $U,V$ be any paddings as in Lemma~\ref{lem:sigdata}(ii), and let $U^*,V^*$ be
obtained by removing their common elements (these do not depend on the choice of paddings). Then
$|U^*|+|V^*|\ge 2L+2$. In particular, if
\[
  L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),
\]
then $H_L(\Orb)=H_L(\Orb')$ implies $\sigma(\Orb)=\sigma(\Orb')$.
\end{theorem}

\begin{corollary}[Genus and cone orders from $\lfloor\operatorname{Area}/\pi\rfloor+4$ coefficients]\label{cor:sigarea}
For every $\Orb\in\Sig$,
\[
  \Kmult(\Orb;\Sig)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
That is, the first $\lfloor\operatorname{Area}(\Orb)/\pi\rfloor+4$ heat coefficients determine the genus and
the cone-order multiset of $\Orb$ among all closed orientable hyperbolic $2$-orbifolds. The number is
read off from the first coefficient $c_1=\operatorname{Area}/4\pi$.
\end{corollary}

\begin{theorem}[Cone count in genus $0$]\label{thm:sigcount}
Let $\Orb\in\Pill_0$ have $n$ cone points. Then $n\le\operatorname{Area}(\Orb)/\pi+4$, with equality exactly
when every cone order is $2$, and
\[
  \Kmult(\Orb;\Pill_0)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
More precisely, $H_{\max(n,n')}$ separates $\Orb$ from every $\Orb'\in\Pill_0$ with $n'$ cone points and a
different cone-order multiset. In particular the cone count $n$ is determined without being known in
advance.
\end{theorem}

\begin{theorem}[No uniform number of coefficients]\label{thm:signonuniform}
\leavevmode
\begin{enumerate}[label=(\alph*)]
\item For every $L\ge2$ and every $g'\ge0$ there are orbifolds in $\Sig$ of genus $g'+1$ and $g'$ with equal
  first $L$ heat coefficients; for $g'=0$ they may be taken of area less than $2\pi(4^{L-1}-1)$.
\item For every $k\ge2$ there are orbifolds in $\Pill_0$ with $n$ and $n+1$ cone points, for some $n$, with
  equal first $k$ heat coefficients.
\end{enumerate}
Hence $\sup_{\Orb}\Kmult(\Orb;\Sig)=\sup_{\Orb}\Kmult(\Orb;\Pill_0)=\infty$, and no fixed number of heat
coefficients determines the genus in $\Sig$ or the cone count in $\Pill_0$.
\end{theorem}

\begin{corollary}[Growth]\label{cor:siggrowth}
Let $f(A)=\max\{\Kmult(\Orb;\Sig):\operatorname{Area}(\Orb)\le A\}$. For $A\ge6\pi$,
\[
  \Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\ \Bigl\lfloor\frac{A}{\pi}\Bigr\rfloor+4 .
\]
\end{corollary}

\begin{example}\label{ex:siggenus}
The orbifolds of signatures $(1;15)$ and $(0;3,3,5,5)$ have the same first two heat coefficients, and
$(1;15,15,15)$ and $(0;3,3,5,7,7,21)$ have the same first three (exact computation). In each pair the genera
differ.
\end{example}

\begin{remark}[Relation to $\Kmult$ and $\Kiso$]\label{rem:sigK}
Theorem~\ref{thm:sigsep} with $g=g'=0$ and $n=n'$ is the statement $\Kmult(\Orb;\Pill_n)\le n$ for the class
$\Pill_n$ of hyperbolic spheres with $n$ cone points, i.e.\ the injectivity that Remark~\ref{rem:nconerestated}(a) leaves conditional, now proved
independently (\texttt{theory/audibility/proof.md}, Theorem~A). Corollary~\ref{cor:sigarea} extends it to all genera and all cone
counts at once, at the price of a bound that depends on the area, and Theorem~\ref{thm:signonuniform}
shows that some such dependence is unavoidable. All of this concerns $\Kmult$; by \eqref{eq:Kcompare}
and Proposition~\ref{prop:Kinf} (conditional on Theorem~\ref{thm:locality}), $\Kiso$ remains infinite
whenever two non-isometric orbifolds share a signature.
\end{remark}

\begin{remark}[What short-time heat flow detects]\label{rem:sigphysics}
This remark is interpretation, not part of any proof. Heat at short times is local: it sees curvature,
hence the area, and each cone point through a fixed function of its order. A handle has no local
signature and is heard only through the area it uses up. Comparing two orbifolds through the mirror
multiset $U^*\uplus(-V^*)$, a genus difference appears as an imbalance between its positive and negative
parts, and Theorem~\ref{thm:sigsep} says that the heat coefficients force the mirror multiset to be
symmetric, hence balanced, once there are enough of them relative to its size. A handle therefore costs
no more coefficients to hear than a cone point.
\end{remark}

% Exact extent. Lemma sigdata, Theorems sigsep, sigcount, signonuniform and Corollaries sigarea,
% siggrowth are proved for all L given the cited heat input (proof.md sections 2-4). The constructions of
% Theorem signonuniform are built and checked with the actual cone coefficients for L <= 6 (a) and
% k <= 3 (b). Open: whether f(A) grows linearly (proof.md section 7).
````

### 53. Growth of f(A) (linear?) and T_L

| field | value |
|---|---|
| status | OPEN |
| dependencies | Corollary N1 |
| external inputs | — |
| source file | `theory/signatures/proof.md`, `theory/signatures/statements.tex` |
| verifying script (existing) | — |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | Stated as open. |

*SG.12, `theory/signatures/proof.md` lines 315-319:*

````
**Corollary N1 (growth).** Let $f(A)=\max\{K_{\rm mult}(\mathcal O;\mathrm{Sig}):
\mathrm{Area}(\mathcal O)\le A\}$. For $A\ge6\pi$,
$$\Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\
\Bigl\lfloor\frac A\pi\Bigr\rfloor+4 .$$

````

*SG.13, `theory/signatures/statements.tex` lines 11-117:*

````
\subsection{The signature from finitely many heat coefficients}\label{subsec:signature}

Throughout, $\Sig$ is the class of all closed orientable hyperbolic $2$-orbifolds, and $\Pill_0\subset\Sig$
the subclass of genus $0$. For a signature $(g;m_1,\dots,m_n)$ write $R=\sum_i1/m_i$,
$P_j=\sum_im_i^{\,j}$ and $s=2g-2+n-R=\operatorname{Area}/2\pi$.

\begin{lemma}[Heat data of a signature]\label{lem:sigdata}
For $\Orb,\Orb'\in\Sig$ with signatures $(g;m)$, $(g';m')$ and $L\ge1$, the following are equivalent:
\begin{enumerate}[label=(\roman*)]
\item $H_L(\Orb)=H_L(\Orb')$;
\item there are paddings $U=m\uplus\{1\}^a$, $V=m'\uplus\{1\}^b$ with
\[
  R(U)=R(V),\qquad P_j(U)=P_j(V)\ \ (j\ \text{odd},\ j\le 2L-3),\qquad |V|-|U|=2(g-g').
\]
\end{enumerate}
Moreover, if the multisets are padded to a common length and $X=m\uplus(-m')$, then (i) holds if and only if
$\sum_{x\in X}x^{-1}=\sum_{x\in X}x^{j}=2(g-g')$ for every odd $j\le2L-3$.
\end{lemma}

\noindent
The input is the structure of the heat expansion at constant curvature
\cite[Theorem~4.8]{dggw2008}, \cite[Theorem~4.20]{ucar2017}: the smooth part of every coefficient is a fixed
multiple of the area, and a cone point of order $k$ contributes $(-1)^l k^{-1}p_l(k)$ at order $t^l$ (curvature $-1$), with
$p_l$ even, $p_l(1)=0$ and leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$. The genus enters only
through the area.

\begin{theorem}[Separation]\label{thm:sigsep}
Let $\Orb,\Orb'\in\Sig$ have signatures $(g;m_1,\dots,m_n)\neq(g';m'_1,\dots,m'_{n'})$ and equal first $L$
heat coefficients. Let $U,V$ be any paddings as in Lemma~\ref{lem:sigdata}(ii), and let $U^*,V^*$ be
obtained by removing their common elements (these do not depend on the choice of paddings). Then
$|U^*|+|V^*|\ge 2L+2$. In particular, if
\[
  L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),
\]
then $H_L(\Orb)=H_L(\Orb')$ implies $\sigma(\Orb)=\sigma(\Orb')$.
\end{theorem}

\begin{corollary}[Genus and cone orders from $\lfloor\operatorname{Area}/\pi\rfloor+4$ coefficients]\label{cor:sigarea}
For every $\Orb\in\Sig$,
\[
  \Kmult(\Orb;\Sig)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
That is, the first $\lfloor\operatorname{Area}(\Orb)/\pi\rfloor+4$ heat coefficients determine the genus and
the cone-order multiset of $\Orb$ among all closed orientable hyperbolic $2$-orbifolds. The number is
read off from the first coefficient $c_1=\operatorname{Area}/4\pi$.
\end{corollary}

\begin{theorem}[Cone count in genus $0$]\label{thm:sigcount}
Let $\Orb\in\Pill_0$ have $n$ cone points. Then $n\le\operatorname{Area}(\Orb)/\pi+4$, with equality exactly
when every cone order is $2$, and
\[
  \Kmult(\Orb;\Pill_0)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
More precisely, $H_{\max(n,n')}$ separates $\Orb$ from every $\Orb'\in\Pill_0$ with $n'$ cone points and a
different cone-order multiset. In particular the cone count $n$ is determined without being known in
advance.
\end{theorem}

\begin{theorem}[No uniform number of coefficients]\label{thm:signonuniform}
\leavevmode
\begin{enumerate}[label=(\alph*)]
\item For every $L\ge2$ and every $g'\ge0$ there are orbifolds in $\Sig$ of genus $g'+1$ and $g'$ with equal
  first $L$ heat coefficients; for $g'=0$ they may be taken of area less than $2\pi(4^{L-1}-1)$.
\item For every $k\ge2$ there are orbifolds in $\Pill_0$ with $n$ and $n+1$ cone points, for some $n$, with
  equal first $k$ heat coefficients.
\end{enumerate}
Hence $\sup_{\Orb}\Kmult(\Orb;\Sig)=\sup_{\Orb}\Kmult(\Orb;\Pill_0)=\infty$, and no fixed number of heat
coefficients determines the genus in $\Sig$ or the cone count in $\Pill_0$.
\end{theorem}

\begin{corollary}[Growth]\label{cor:siggrowth}
Let $f(A)=\max\{\Kmult(\Orb;\Sig):\operatorname{Area}(\Orb)\le A\}$. For $A\ge6\pi$,
\[
  \Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\ \Bigl\lfloor\frac{A}{\pi}\Bigr\rfloor+4 .
\]
\end{corollary}

\begin{example}\label{ex:siggenus}
The orbifolds of signatures $(1;15)$ and $(0;3,3,5,5)$ have the same first two heat coefficients, and
$(1;15,15,15)$ and $(0;3,3,5,7,7,21)$ have the same first three (exact computation). In each pair the genera
differ.
\end{example}

\begin{remark}[Relation to $\Kmult$ and $\Kiso$]\label{rem:sigK}
Theorem~\ref{thm:sigsep} with $g=g'=0$ and $n=n'$ is the statement $\Kmult(\Orb;\Pill_n)\le n$ for the class
$\Pill_n$ of hyperbolic spheres with $n$ cone points, i.e.\ the injectivity that Remark~\ref{rem:nconerestated}(a) leaves conditional, now proved
independently (\texttt{theory/audibility/proof.md}, Theorem~A). Corollary~\ref{cor:sigarea} extends it to all genera and all cone
counts at once, at the price of a bound that depends on the area, and Theorem~\ref{thm:signonuniform}
shows that some such dependence is unavoidable. All of this concerns $\Kmult$; by \eqref{eq:Kcompare}
and Proposition~\ref{prop:Kinf} (conditional on Theorem~\ref{thm:locality}), $\Kiso$ remains infinite
whenever two non-isometric orbifolds share a signature.
\end{remark}

\begin{remark}[What short-time heat flow detects]\label{rem:sigphysics}
This remark is interpretation, not part of any proof. Heat at short times is local: it sees curvature,
hence the area, and each cone point through a fixed function of its order. A handle has no local
signature and is heard only through the area it uses up. Comparing two orbifolds through the mirror
multiset $U^*\uplus(-V^*)$, a genus difference appears as an imbalance between its positive and negative
parts, and Theorem~\ref{thm:sigsep} says that the heat coefficients force the mirror multiset to be
symmetric, hence balanced, once there are enough of them relative to its size. A handle therefore costs
no more coefficients to hear than a cone point.
\end{remark}

% Exact extent. Lemma sigdata, Theorems sigsep, sigcount, signonuniform and Corollaries sigarea,
% siggrowth are proved for all L given the cited heat input (proof.md sections 2-4). The constructions of
% Theorem signonuniform are built and checked with the actual cone coefficients for L <= 6 (a) and
% k <= 3 (b). Open: whether f(A) grows linearly (proof.md section 7).
````

### 54. ex:siggenus

| field | value |
|---|---|
| status | COMPUTATION |
| dependencies | Lemma 4 |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/signatures/statements.tex` |
| verifying script (existing) | theory/signatures/genus.py |
| audit evidence | `review/audit/signatures/` |
| audit verdict | NONE |
| in paper? | YES |
| note | Shares exactly 2 and exactly 3 coefficients. |

*SG.13, `theory/signatures/statements.tex` lines 11-117:*

````
\subsection{The signature from finitely many heat coefficients}\label{subsec:signature}

Throughout, $\Sig$ is the class of all closed orientable hyperbolic $2$-orbifolds, and $\Pill_0\subset\Sig$
the subclass of genus $0$. For a signature $(g;m_1,\dots,m_n)$ write $R=\sum_i1/m_i$,
$P_j=\sum_im_i^{\,j}$ and $s=2g-2+n-R=\operatorname{Area}/2\pi$.

\begin{lemma}[Heat data of a signature]\label{lem:sigdata}
For $\Orb,\Orb'\in\Sig$ with signatures $(g;m)$, $(g';m')$ and $L\ge1$, the following are equivalent:
\begin{enumerate}[label=(\roman*)]
\item $H_L(\Orb)=H_L(\Orb')$;
\item there are paddings $U=m\uplus\{1\}^a$, $V=m'\uplus\{1\}^b$ with
\[
  R(U)=R(V),\qquad P_j(U)=P_j(V)\ \ (j\ \text{odd},\ j\le 2L-3),\qquad |V|-|U|=2(g-g').
\]
\end{enumerate}
Moreover, if the multisets are padded to a common length and $X=m\uplus(-m')$, then (i) holds if and only if
$\sum_{x\in X}x^{-1}=\sum_{x\in X}x^{j}=2(g-g')$ for every odd $j\le2L-3$.
\end{lemma}

\noindent
The input is the structure of the heat expansion at constant curvature
\cite[Theorem~4.8]{dggw2008}, \cite[Theorem~4.20]{ucar2017}: the smooth part of every coefficient is a fixed
multiple of the area, and a cone point of order $k$ contributes $(-1)^l k^{-1}p_l(k)$ at order $t^l$ (curvature $-1$), with
$p_l$ even, $p_l(1)=0$ and leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$. The genus enters only
through the area.

\begin{theorem}[Separation]\label{thm:sigsep}
Let $\Orb,\Orb'\in\Sig$ have signatures $(g;m_1,\dots,m_n)\neq(g';m'_1,\dots,m'_{n'})$ and equal first $L$
heat coefficients. Let $U,V$ be any paddings as in Lemma~\ref{lem:sigdata}(ii), and let $U^*,V^*$ be
obtained by removing their common elements (these do not depend on the choice of paddings). Then
$|U^*|+|V^*|\ge 2L+2$. In particular, if
\[
  L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),
\]
then $H_L(\Orb)=H_L(\Orb')$ implies $\sigma(\Orb)=\sigma(\Orb')$.
\end{theorem}

\begin{corollary}[Genus and cone orders from $\lfloor\operatorname{Area}/\pi\rfloor+4$ coefficients]\label{cor:sigarea}
For every $\Orb\in\Sig$,
\[
  \Kmult(\Orb;\Sig)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
That is, the first $\lfloor\operatorname{Area}(\Orb)/\pi\rfloor+4$ heat coefficients determine the genus and
the cone-order multiset of $\Orb$ among all closed orientable hyperbolic $2$-orbifolds. The number is
read off from the first coefficient $c_1=\operatorname{Area}/4\pi$.
\end{corollary}

\begin{theorem}[Cone count in genus $0$]\label{thm:sigcount}
Let $\Orb\in\Pill_0$ have $n$ cone points. Then $n\le\operatorname{Area}(\Orb)/\pi+4$, with equality exactly
when every cone order is $2$, and
\[
  \Kmult(\Orb;\Pill_0)\ \le\ \Bigl\lfloor\frac{\operatorname{Area}(\Orb)}{\pi}\Bigr\rfloor+4 .
\]
More precisely, $H_{\max(n,n')}$ separates $\Orb$ from every $\Orb'\in\Pill_0$ with $n'$ cone points and a
different cone-order multiset. In particular the cone count $n$ is determined without being known in
advance.
\end{theorem}

\begin{theorem}[No uniform number of coefficients]\label{thm:signonuniform}
\leavevmode
\begin{enumerate}[label=(\alph*)]
\item For every $L\ge2$ and every $g'\ge0$ there are orbifolds in $\Sig$ of genus $g'+1$ and $g'$ with equal
  first $L$ heat coefficients; for $g'=0$ they may be taken of area less than $2\pi(4^{L-1}-1)$.
\item For every $k\ge2$ there are orbifolds in $\Pill_0$ with $n$ and $n+1$ cone points, for some $n$, with
  equal first $k$ heat coefficients.
\end{enumerate}
Hence $\sup_{\Orb}\Kmult(\Orb;\Sig)=\sup_{\Orb}\Kmult(\Orb;\Pill_0)=\infty$, and no fixed number of heat
coefficients determines the genus in $\Sig$ or the cone count in $\Pill_0$.
\end{theorem}

\begin{corollary}[Growth]\label{cor:siggrowth}
Let $f(A)=\max\{\Kmult(\Orb;\Sig):\operatorname{Area}(\Orb)\le A\}$. For $A\ge6\pi$,
\[
  \Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\ \Bigl\lfloor\frac{A}{\pi}\Bigr\rfloor+4 .
\]
\end{corollary}

\begin{example}\label{ex:siggenus}
The orbifolds of signatures $(1;15)$ and $(0;3,3,5,5)$ have the same first two heat coefficients, and
$(1;15,15,15)$ and $(0;3,3,5,7,7,21)$ have the same first three (exact computation). In each pair the genera
differ.
\end{example}

\begin{remark}[Relation to $\Kmult$ and $\Kiso$]\label{rem:sigK}
Theorem~\ref{thm:sigsep} with $g=g'=0$ and $n=n'$ is the statement $\Kmult(\Orb;\Pill_n)\le n$ for the class
$\Pill_n$ of hyperbolic spheres with $n$ cone points, i.e.\ the injectivity that Remark~\ref{rem:nconerestated}(a) leaves conditional, now proved
independently (\texttt{theory/audibility/proof.md}, Theorem~A). Corollary~\ref{cor:sigarea} extends it to all genera and all cone
counts at once, at the price of a bound that depends on the area, and Theorem~\ref{thm:signonuniform}
shows that some such dependence is unavoidable. All of this concerns $\Kmult$; by \eqref{eq:Kcompare}
and Proposition~\ref{prop:Kinf} (conditional on Theorem~\ref{thm:locality}), $\Kiso$ remains infinite
whenever two non-isometric orbifolds share a signature.
\end{remark}

\begin{remark}[What short-time heat flow detects]\label{rem:sigphysics}
This remark is interpretation, not part of any proof. Heat at short times is local: it sees curvature,
hence the area, and each cone point through a fixed function of its order. A handle has no local
signature and is heard only through the area it uses up. Comparing two orbifolds through the mirror
multiset $U^*\uplus(-V^*)$, a genus difference appears as an imbalance between its positive and negative
parts, and Theorem~\ref{thm:sigsep} says that the heat coefficients force the mirror multiset to be
symmetric, hence balanced, once there are enough of them relative to its size. A handle therefore costs
no more coefficients to hear than a cone point.
\end{remark}

% Exact extent. Lemma sigdata, Theorems sigsep, sigcount, signonuniform and Corollaries sigarea,
% siggrowth are proved for all L given the cited heat input (proof.md sections 2-4). The constructions of
% Theorem signonuniform are built and checked with the actual cone coefficients for L <= 6 (a) and
% k <= 3 (b). Open: whether f(A) grows linearly (proof.md section 7).
````

### 55. Theorem 1 (signature locality)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | DGGW Thm 4.8, Def 4.7; Uçar Thm 4.11, 4.20; Thurston 13.3.5 |
| source file | `theory/locality/proof.md` |
| verifying script (existing) | theory/locality/check_locality.py |
| audit evidence | `review/audit/locality/` |
| audit verdict | NONE |
| in paper? | YES |
| note | Proof A (DGGW) is the proof; Proof C (trace formula) is a cross-check and must be labelled so. |

*LO.0, `theory/locality/proof.md` lines 9-17:*

````
**Setting.** $\mathcal O=\Gamma\backslash\mathbb H^2$ is a closed orientable hyperbolic
2-orbifold, i.e. $\Gamma\subset PSL(2,\mathbb R)$ is a cocompact Fuchsian group. Its
signature $\sigma(\mathcal O)=(g;m_1,\dots,m_n)$ is as in `\label{def:signature}`
(`theory/definitions.tex`). $\Delta\ge0$ is the Laplacian, $0=\lambda_0<\lambda_1\le\dots$ its
eigenvalues, $Z_{\mathcal O}(t)=\sum_j e^{-\lambda_j t}$ its heat trace, and $c_j(\mathcal O)$
the coefficients of `\label{def:heatcoef}`. The orbifold Euler characteristic is
$\chi(\mathcal O)=2-2g-\sum_i(1-1/m_i)$. By the orbifold Gauss–Bonnet theorem,
$\operatorname{Area}(\mathcal O)=-2\pi\chi(\mathcal O)$ [Thurston, 13.3.5 and the sentence
after it, "If O is elliptic or hyperbolic, then area(O) = 2π|χ(O)|", electronic p. 312; DS, Thm 3.2, p. 5].
````

*LO.1, `theory/locality/proof.md` lines 47-69:*

````
**Theorem 1 (signature locality).** There are universal constants $\alpha_k$
($k\ge0$) and $\beta_k(m)$ ($k\ge0$, $m\ge2$) such that every closed orientable hyperbolic
2-orbifold $\mathcal O$ of signature $(g;m_1,\dots,m_n)$ satisfies
$$
Z_{\mathcal O}(t)\;\sim\;\frac{\operatorname{Area}(\mathcal O)}{4\pi t}\sum_{k\ge0}\alpha_k t^k
\;+\;\sum_{i=1}^n\sum_{k\ge0}\beta_k(m_i)\,t^k\qquad(t\downarrow0),
\qquad \operatorname{Area}(\mathcal O)=2\pi\Big(2g-2+\sum_i\big(1-\tfrac1{m_i}\big)\Big).
$$
Consequently $c_1=\operatorname{Area}/4\pi$ and, for $j\ge2$,
$c_j(\mathcal O)=\alpha_{j-1}\operatorname{Area}(\mathcal O)/4\pi+\sum_i\beta_{j-2}(m_i)$, a
function of $\sigma(\mathcal O)$ alone. This proves `\label{thm:locality}` (the forward
reference in `theory/definitions.tex`), with
$\Phi_j(g;m_1,\dots,m_n)=\alpha_{j-1}\tfrac{1}{2}\big(2g-2+\sum_i(1-\tfrac1{m_i})\big)+\sum_i\beta_{j-2}(m_i)$.
(For $j=1$ the cone sum is absent: $\Phi_1=\tfrac12\big(2g-2+\sum_i(1-\tfrac1{m_i})\big)$.)
In particular two orbifolds of the same signature have the same expansion to all orders.
No half-integer powers occur: [DGGW] (4.9) allows $t^{j/2}$, but the only strata are the
2-dimensional regular part and points, whose series are in integer powers.

The constants are explicit [Uçar, Thm 4.20 (i), (ii) at $\kappa=-1$]:
$\alpha_k=\frac{(-1)^k}{k!\,4^k}\sum_{l=0}^k\binom kl(-4)^lB_{2l}(\tfrac12)$, and $\beta_k(m)$ is
the coefficient of $t^k$ in $C$ of [Uçar, (4.33)], built from $c^S_\ell(\pi/m)$ of (4.25). These
are the formulas implemented in `numerics/theory.py` and asserted there against DGGW §5.6
and Schueth's Theorem 4.1 for $k\le2$.
````

### 56. Proposition 2.1 (dim T = 6g-6+2n)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | Thurston Cor 13.3.7 / 13.3.5 |
| source file | `theory/locality/proof.md` |
| verifying script (existing) | — |
| audit evidence | `review/audit/locality/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*LO.2, `theory/locality/proof.md` lines 154-157:*

````
**Source statement** [Th, Corollary 13.3.7, electronic ed. p. 318, original p. 13.27],
verbatim: *"The Teichmüller space T(O) of an orbifold O with χ(O) < 0 is homeomorphic to
Euclidean space of dimension −3χ(X_O) + 2k + l, where k is the number of elliptic points and
l is the number of corner reflectors."* The proof (p. 318) cuts $\mathcal O$ along disjoint
````

*LO.3, `theory/locality/proof.md` lines 167-171:*

````
**Proposition 2.1.** For a closed orientable hyperbolic 2-orbifold of signature
$(g;m_1,\dots,m_n)$,
$$\dim_{\mathbb R}T(\mathcal O)=6g-6+2n .$$
Among hyperbolic signatures, it vanishes exactly for $(g;n)=(0;3)$, the triangle orbifolds,
and is $\ge2$ otherwise.
````

### 57. Proposition 2.2 (uncountably many isometry classes)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Proposition 2.1 |
| external inputs | Thurston Cor 13.3.7 / 13.3.5; DS p. 3 |
| source file | `theory/locality/proof.md` |
| verifying script (existing) | — |
| audit evidence | `review/audit/locality/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*LO.4, `theory/locality/proof.md` lines 184-185:*

````
**Proposition 2.2.** If $6g-6+2n>0$, the closed orientable hyperbolic orbifolds of
signature $\sigma=(g;m_1,\dots,m_n)$ fall into uncountably many isometry classes.
````

### 58. Corollary 2.3 (K_iso = infinity)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Theorem 1, Proposition 2.2, prop:rigidity |
| external inputs | Thurston Cor 13.3.7 / 13.3.5 |
| source file | `theory/locality/proof.md` |
| verifying script (existing) | — |
| audit evidence | `review/audit/locality/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*LO.5, `theory/locality/proof.md` lines 212-219:*

````
**Corollary 2.3 ($K_{\rm iso}=\infty$).** Let $\sigma$ be a hyperbolic signature with
$6g-6+2n>0$, i.e. any closed orientable hyperbolic 2-orbifold that is not a triangle
orbifold. Let $\mathcal P$ be a comparison class (`\label{def:K}`) containing every orbifold
of signature $\sigma$. Examples: the class of all closed orientable hyperbolic
2-orbifolds; for $g=0$, the class $\mathcal P_n$ of `\label{rem:nconerestated}`. Then
$$K_{\rm iso}(\mathcal O;\mathcal P)=\infty\qquad\text{for every }\mathcal O\in\mathcal P\text{ with }\sigma(\mathcal O)=\sigma .$$
For the triangle orbifolds ($g=0$, $n=3$), $K_{\rm iso}(\mathcal O;\mathcal P)=K_{\rm mult}(\mathcal O;\mathcal P)$ for
every class $\mathcal P$.
````

### 59. Theorem 3.1 (I+E+H decomposition)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Lemmas 3.2-3.3 |
| external inputs | Dryden–Strohmaier trace formula eq. (1) |
| source file | `theory/locality/proof.md` |
| verifying script (existing) | theory/locality/check_locality.py |
| audit evidence | `review/audit/locality/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*LO.6, `theory/locality/proof.md` lines 254-265:*

````
**Theorem 3.1.** For every $t>0$,
$$Z_{\mathcal O}(t)=I(t)+E(t)+H(t),$$
with all series and integrals absolutely convergent, where

- $I(t)=\dfrac{\operatorname{Area}(\mathcal O)}{4\pi}\displaystyle\int_{\mathbb R}r\tanh(\pi r)\,e^{-t(1/4+r^2)}dr$ (identity term);
- $E(t)=\displaystyle\sum_{i=1}^nE_{m_i}(t)$, with $E_m(t)=\displaystyle\sum_{l=1}^{m-1}\frac1{2m\sin(\pi l/m)}\int_{\mathbb R}\frac{e^{-2\pi lr/m}}{1+e^{-2\pi r}}e^{-t(1/4+r^2)}dr$ (elliptic terms);
- $H(t)=\displaystyle\sum_{[\gamma]\ \rm hyperbolic}\frac{\ell(\gamma_0)}{2\sinh(\ell(\gamma)/2)}\,\frac{e^{-t/4}\,e^{-\ell(\gamma)^2/4t}}{\sqrt{4\pi t}}$ (hyperbolic terms).

In $H$ the sum runs over the conjugacy classes of hyperbolic elements of $\Gamma$, i.e. over
the oriented closed geodesics with their iterates [DS p. 3]; $\gamma_0$ is the primitive
element with $\gamma=\gamma_0^k$. $I$ depends only on the area, and $E$ only on the multiset
of cone orders. Every term of $H$ is positive.
````

### 60. Lemma 3.2 (admissibility of the heat function)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Lemma 3.3; Weyl bound from DGGW Thm 4.8 at t^-1 |
| external inputs | Dryden–Strohmaier trace formula eq. (1); DGGW Thm 4.8, Def 4.7 |
| source file | `theory/locality/proof.md` |
| verifying script (existing) | theory/locality/check_locality.py |
| audit evidence | `review/audit/locality/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | P2 SOUND: decay order 3 is used; cite 'DGGW Thm 4.8 at order t^-1' for the Weyl bound, not 'Theorem 1', so no cycle with Proof C. |

*LO.7, `theory/locality/proof.md` lines 289-293:*

````
**Lemma 3.2 (admissibility of the heat function).** Fix $\chi\in C_c^\infty(\mathbb R)$, even,
$0\le\chi\le1$, $\chi=1$ on $[-1,1]$, $\operatorname{supp}\chi\subset[-2,2]$, and put $g_R(u)=g_t(u)\chi(u/R)$ and
$h_R(r)=\int g_R(u)e^{iru}du$. Then $h_R$ is even, entire and of exponential type $\le2R$
(Paley–Wiener), so [DS] (1) holds for $h_R$, with Fourier transform $g_R$. As
$R\to\infty$ each term converges to the corresponding term for $h_t$:
````

### 61. Lemma 3.3 (counting closed geodesics)

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `theory/locality/proof.md` |
| verifying script (existing) | — |
| audit evidence | `review/audit/locality/` |
| audit verdict | NONE |
| in paper? | YES |
| note | Base point must not be a cone point (it is chosen so). |

*LO.8, `theory/locality/proof.md` lines 321-324:*

````
**Lemma 3.3 (counting).** Let $A=\operatorname{Area}(\mathcal O)$ and
$\delta=\operatorname{diam}(\mathcal O)$, and let $N(L)$ be the number of hyperbolic conjugacy
classes $[\gamma]$ with $\ell(\gamma)\le L$. Then
$$N(L)\le\frac{2\pi(\cosh(L+3\delta)-1)}{A}\le\frac{\pi}{A}e^{L+3\delta}.$$
````

### 62. Theorem 3.4 (quantitative locality)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Theorem 3.1, Lemma 3.3 |
| external inputs | Dryden–Strohmaier trace formula eq. (1) |
| source file | `theory/locality/proof.md` |
| verifying script (existing) | theory/locality/check_locality.py |
| audit evidence | `review/audit/locality/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Define the systole over all hyperbolic classes (including geodesics through cone points); (c) also needs area, signature and ell. |

*LO.9, `theory/locality/proof.md` lines 347-362:*

````
**Theorem 3.4.** Let $\mathcal O_1,\mathcal O_2$ be closed orientable hyperbolic 2-orbifolds
with the same signature. Write $A$ for their common area, $\ell_i$ for their systoles (the
length of the shortest closed geodesic), $\delta_i$ for their diameters,
$\ell=\min(\ell_1,\ell_2)$ and $\delta=\max(\delta_1,\delta_2)$.

**(a) Exact cancellation.** For every $t>0$,
$Z_1(t)-Z_2(t)=H_1(t)-H_2(t)$. Hence
$|Z_1(t)-Z_2(t)|\le\max(H_1(t),H_2(t))$.

**(b) Explicit bound.** For $0<t\le\ell^2/(2(1+\ell))$,
$$|Z_1(t)-Z_2(t)|\;\le\;\frac{\pi\,e^{3\delta}}{A\,(1-e^{-\ell})}\;\ell\,e^{\ell/2}\Big(1+\frac{2t}{\ell-t}\Big)\;\frac{e^{-\ell^2/4t}}{\sqrt{4\pi t}} .$$

**(c) Controlled bound from one reference time.** For any $t_1>0$ and $0<t\le t_1$,
$$|Z_1(t)-Z_2(t)|\le\sqrt{t_1/t}\;e^{(t_1-t)/4}\,e^{\ell^2/4t_1}\,\max_iH_i(t_1)\;e^{-\ell^2/4t}.$$
Here $H_i(t_1)=Z_i(t_1)-I(t_1)-E(t_1)$ is computable from the spectrum at the single time
$t_1$.
````

### 63. t^{-1/2} prefactor cannot be dropped

| field | value |
|---|---|
| status | PROVED |
| dependencies | Theorem 3.5 |
| external inputs | — |
| source file | `theory/locality/proof.md` |
| verifying script (existing) | numerics/moduli/geodesics.py |
| audit evidence | `review/audit/locality/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Write |w_1(ell)-w_2(ell)|. |

*LO.10, `theory/locality/proof.md` lines 396-412:*

````
**The prefactor $t^{-1/2}$ cannot be dropped.** T3 as posed asks for
$|Z_1-Z_2|\le Ce^{-\ell^2/4t}$ with a constant $C$. In general that bound is **false**. By
Theorem 3.5, whenever the shortest geodesics differ, $|Z_1-Z_2|\,e^{\ell^2/4t}$ grows like
$t^{-1/2}$. The family of T4 is an example:
$\sqrt t\,e^{\ell^2/4t}|Z_1-Z_2|\to w/(2\sinh(\ell/2)\sqrt{4\pi})\ne0$.

What is true:

- the bound with $t^{-1/2}$ (Theorem 3.4);
- as a consequence, for every $\varepsilon\in(0,\ell)$, $|Z_1-Z_2|\le C_\varepsilon e^{-(\ell-\varepsilon)^2/4t}$
  for $t\le t_0$.

The falsity of the constant-$C$ form is proved for every pair with $L_*=\ell$, in particular
whenever $\ell_1\ne\ell_2$ (if $L_*>\ell$ the constant-$C$ bound does hold). Pairs with
$\ell_1\ne\ell_2$ exist in every signature with $\dim T>0$ in which the systole varies on
$T$; in the T4 family they are exhibited explicitly (systole $4b(\tau)$, by certified
enumeration of the reflection group, `numerics/moduli/geodesics.py`).
````

### 64. Theorem 3.5 (sharp asymptotics)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Theorem 3.1, Lemma 3.3 |
| external inputs | Dryden–Strohmaier trace formula eq. (1) |
| source file | `theory/locality/proof.md` |
| verifying script (existing) | — |
| audit evidence | `review/audit/locality/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Define w_i(L) in the statement. |

*LO.11, `theory/locality/proof.md` lines 423-430:*

````
**Theorem 3.5.** Let $\mathcal O_1,\mathcal O_2$ have the same signature.

- If $w_1\equiv w_2$, then $Z_1\equiv Z_2$, and the orbifolds are isospectral.
- Otherwise, let $L_*=\min\{L:w_1(L)\ne w_2(L)\}$. Then, as $t\downarrow0$,
$$Z_1(t)-Z_2(t)=\frac{w_1(L_*)-w_2(L_*)}{2\sinh(L_*/2)}\,\frac{e^{-t/4}e^{-L_*^2/4t}}{\sqrt{4\pi t}}\,\big(1+o(1)\big),$$
  so $Z_1-Z_2\ne0$ for small $t$ and $\log|Z_1-Z_2|=-L_*^2/4t-\tfrac12\log t+O(1)$.
- In particular, if $\ell_1\ne\ell_2$, then $L_*=\min(\ell_1,\ell_2)=\ell$, and the
  exponent $\ell^2/4$ of Theorem 3.4 is attained.
````

### 65. Proposition S1 (front end)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20, (4.35) |
| source file | `theory/stability/proof.md` |
| verifying script (existing) | theory/stability/front_end.py |
| audit evidence | `review/audit/stability/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*ST.0, `theory/stability/proof.md` lines 45-75:*

````
## 1. Setting and the recovery map

Conventions (`numerics/REPORT.md` §2; `theory/cone-coefficients/ucar-source.md`): positive
Laplacian, K = κ = −1, and

- H₋₁ = Area/(4π) = (n − 2 − R)/2;
- H_ν = (Area/4π)·α_{ν+1} + Σ_i b_ν(m_i) for ν ≥ 0;
- b_ν(m) = (−1)^ν p_ν(m)/m, with p_ν = Σ_k π_{ν,k} m^{2k} even of degree 2ν + 2 and
  p_ν(1) = 0 (Uçar (4.25)+(4.33));
- α_j = a_j^{sm}/vol (Uçar (4.35)): α = 1, −1/3, 1/15, −4/315, 1/315, …

The smooth coefficients α_j are also derived independently from the Selberg identity term
(`stab_common.alpha_smooth_selberg`), and the two agree for j ≤ 11.

The number n of cone points is assumed known. The **recovery map** studied throughout is:

1. **Front end.** Ĩ := L⁻¹(H̃ − h₀).
2. **Linear solve.** ẽ := M(Ĩ)⁻¹ b(Ĩ) (Theorem B).
3. **Roots.** Take the roots of q̃(z) := Σ_{j=0}^{n}(−1)^j ẽ_j z^{n−j}, with ẽ₀ = 1.
4. **Rounding** (integer orders only). Round the real part of every root.

Throughout, μ := max_i m_i. Hats denote scale-free quantities:

- m̂ = m/μ ∈ (0,1]ⁿ and ê_k = e_k/μ^k;
- Î = (μR, P₁/μ, P₃/μ³, …).

Theorem B's system is weighted-homogeneous: row j has weight 2j+1, the last row weight n−1,
and column k weight k. Hence M(Î) = D_r⁻¹ M(I) D_c, and ê solves M(Î) ê = b(Î).
Distances between multisets are optimal matching distances,
d(m, m′) = min_π max_i |m_i − m′_{π(i)}|.

````

*ST.1, `theory/stability/proof.md` lines 78-88:*

````
**Proposition S1.** For every n, (H₋₁, …, H_{n−2}) = L·I_n + h₀(n), where L is lower
triangular with entries

- L₀₀ = −1/2;
- L_{ν+1,0} = −α_{ν+1}/2 + (−1)^ν π_{ν,0};
- L_{ν+1,k} = (−1)^ν π_{ν,k} for 1 ≤ k ≤ ν+1.

The offset is h₀(n) = ((n−2)/2)(1, α₁, …, α_{n−1}). The matrix L does not depend on n, which
enters only through h₀. Its diagonal is L_{ν+1,ν+1} = (−1)^ν |B_{2ν+2}|/(2(ν+1)!(2ν+1)) ≠ 0,
so L is invertible.

````

*ST.2, `theory/stability/proof.md` lines 100-131:*

````
The first rows of L⁻¹, which give I = L⁻¹(H − h₀):

| | H₋₁ | H₀ | H₁ | H₂ | H₃ |
|---|---|---|---|---|---|
| R | −2 | | | | |
| P₁ | 2 | 12 | | | |
| P₃ | −18 | −120 | −360 | | |
| P₅ | 30 | 252 | 1260 | 2520 | |
| P₇ | −70/3 | −240 | −1680 | −6720 | −10080 |

**Amplification.** With every |δH_ν| ≤ δ, the worst-case error in I_r is ℓ_r·δ, where ℓ_r is
the absolute row sum of L⁻¹. Row r involves only the first r+1 coefficients, so ℓ_r is the
same for every n:

| | R | P₁ | P₃ | P₅ | P₇ | P₉ | P₁₁ | P₁₃ |
|---|---|---|---|---|---|---|---|---|
| diagonal 1/\|L_rr\| | 2 | 12 | 360 | 2520 | 10080 | 28512 | 43243200/691 | 112320 |
| ℓ_r (row sum) | 2 | 14 | 498 | 4062 | 56230/3 | 303654/5 | 104899830/691 | 10805786/35 |

**Correction to the review (DEFECTS.md MAJ-05).**

- The factors 12, 360, 2520 are correct as the diagonal entries of L⁻¹: for P₁ from H₀, P₃
  from H₁ and P₅ from H₂.
- They are not the amplification factors. Each invariant also inherits the errors of all
  lower coefficients through the off-diagonal entries, e.g.
  δP₃ = −18 δH₋₁ − 120 δH₀ − 360 δH₁.
- So the worst-case factors are **14, 498, 4062**, larger by 1.17, 1.38 and 1.61.
- R is recovered from H₋₁ with factor 2. Equivalently, R = n − 2 − Area/(2π), so the factor
  is 1/(2π) per unit of area.
- In relative terms the front end is harmless. The ratio
  κ_r = Σ_c |(L⁻¹)_{rc}| |H_c| / |I_r| lies between 0.02 and 3.7 on every test multiset of
  `front_end_output.md`. For (2,8,8) it is 0.33, 0.94, 1.33 for R, P₁, P₃.
````

### 66. Lemma S2.1 (c_n for all n)

| field | value |
|---|---|
| status | PROVED |
| dependencies | Theorem B |
| external inputs | — |
| source file | `theory/stability/proof.md` |
| verifying script (existing) | theory/stability/lipschitz_e.py |
| audit evidence | `review/audit/stability/`, `review/audit/audibility/` |
| audit verdict | NONE |
| in paper? | YES |
| note | Reproved by two independent routes. |

*ST.3, `theory/stability/proof.md` lines 142-146:*

````
**Lemma S2.1 (the constant c_n of Theorem B, all n).** For every n ≥ 2,

  det M = (−1)^{n(n+1)/2} ∏_{i<j}(m_i + m_j) / e_n,

so c_n = (−1)^{n(n+1)/2}. This replaces "c_n ∈ ℚ^×, computed for n ≤ 8" in Theorem B.
````

### 67. Lemma S2.2 (Hurwitz factorisation)

| field | value |
|---|---|
| status | PROVED |
| dependencies | Lemma S2.1 |
| external inputs | Orlando |
| source file | `theory/stability/proof.md` |
| verifying script (existing) | theory/stability/lipschitz_e.py |
| audit evidence | `review/audit/stability/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*ST.4, `theory/stability/proof.md` lines 172-183:*

````
**Lemma S2.2 (Hurwitz factorisation of M).** Let f(z) = ∏(1 + m_i z) = E(z²) + zO(z²), and for
D(z) = Σ_{k=1}^n d_k z^k let W_D := E_f O_D − E_D O_f, a polynomial in w = z² of degree ≤ n−1.
Define two n × n matrices (with e_i := 0 outside 0 ≤ i ≤ n):

- B_{k,j} = (−1)^{j+1} e_{2k+1−j}, for 0 ≤ k ≤ n−1 and 1 ≤ j ≤ n. This is the map
  d ↦ (coefficients of W_D).
- S_{k,i} = e_{2(k−i)} for i ≤ k ≤ n−2, S_{n−1,n−1} = (−1)ⁿ e_n, and all other entries 0.

Then

  B = S·M,  det B = (−1)^{n(n−1)/2} ∏_{i<j}(m_i+m_j),  M⁻¹ = B⁻¹ S.

````

### 68. Theorem S2 (Lipschitz, explicit constants)

| field | value |
|---|---|
| status | PROVED |
| dependencies | Lemmas S2.1-S2.2 |
| external inputs | — |
| source file | `theory/stability/proof.md` |
| verifying script (existing) | theory/stability/lipschitz_e.py |
| audit evidence | `review/audit/stability/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*ST.5, `theory/stability/proof.md` lines 196-222:*

````
**Theorem S2 (Lipschitz dependence of e on I_n, explicit constants).**

*Setting.* Let m be positive reals and μ = max m_i. Let Ĩ be any real data vector with
scale-free error

  η := max( μ|R̃ − R|, max_{1≤l≤n−1} |P̃_{2l−1} − P_{2l−1}| / μ^{2l−1} ) ≤ 1.

*Constants.* Put κ := ‖M(Î)⁻¹‖_∞ and

- σ_k(n) := [w^k] artanh(w) · sec²((n+1) artanh w). For instance σ₁ = 1 and
  σ₃ = 1/3 + (n+1)²; n = 3: (1, 49/3); n = 4: (1, 76/3, 6628/15).
- ζ_n := max(1, max_{0≤j≤n−2} Σ_{0≤i<j, 2≤2j−2i≤n} σ_{2i+1}(n)). For example ζ₃ = 1,
  ζ₄ = 79/3, ζ₅ = 14048/15.
- ρ_n(m̂) := max( ê_n, max_{0≤j≤n−2} Σ_{i=0}^{j} σ_{2i+1}(n) ê_{2j−2i} ).

*Conclusions.*

(a) The inverse is bounded by

  κ ≤ n Λ(m̂) ‖Ŝ‖_∞ / ∏_{i<j}(m̂_i + m̂_j) ≤ n · binom(2n,n)^{n/2} · 2^{n−1} / ∏_{i<j}(m̂_i + m̂_j),

  where Λ(m̂) = ∏_c ‖c-th column of B(ê)‖₂ and ‖Ŝ‖_∞ ≤ max(Σ_{k even} ê_k, ê_n).

(b) If β := κ ζ_n η ≤ 1/2, then M(Ĩ) is invertible, and ẽ = M(Ĩ)⁻¹ b(Ĩ) satisfies

  max_k |ẽ_k − e_k| / μ^k ≤ 2 κ ρ_n(m̂) η.

````

### 69. Ostrowski input

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | Ostrowski, Acta Math. 72 (1940), Thm XXX, (71,1) |
| source file | `theory/stability/proof.md` |
| verifying script (existing) | — |
| audit evidence | `review/audit/stability/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | gamma is the largest root modulus of both polynomials; follow Ostrowski's indexing of (69,3)-(69,4). |

*ST.6, `theory/stability/proof.md` lines 264-273:*

````
**Standard global theorem (fetched, `review/literature/root-perturbation.md`).** Ostrowski,
*Acta Math.* 72 (1940), Théorème XXX, eq. (71,1), p. 212, read from the primary. For monic
f, g of degree n with roots x_ν and y_ν, after renumbering,

  |y_ν − x_ν| ≤ (2n−1)ε,  ε = (Σ_{ν=1}^{n} |a_ν − b_ν| γ^{n−ν})^{1/n},

where γ is the largest root modulus. "Les racines … satisfont … à une condition de Lipschitz
d'ordre 1/n." This is uniform but crude: exponent 1/n everywhere, with no use of
separation. The local statement below has the exponent 1/k at a k-fold root, and is
Lipschitz at simple roots, with explicit constants.
````

### 70. Lemma S3 (explicit Rouché)

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `theory/stability/proof.md` |
| verifying script (existing) | theory/stability/roots_holder.py |
| audit evidence | `review/audit/stability/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*ST.7, `theory/stability/proof.md` lines 275-287:*

````
**Lemma S3 (clusters, explicit Rouché).** Work in scale-free variables. Let
q(z) = ∏(z − m̂_i) = Σ_j (−1)^j ê_j z^{n−j}, and let q̃ be the same polynomial with ẽ in place
of ê, where |ẽ_j − ê_j| ≤ ε. Let a be a distinct value among the m̂_i, of multiplicity k, and
put

- g_a := min_{b≠a} |a − b| (∞ if there is no other value);
- Q_a := ∏_{b≠a} |a − b|^{k_b}.

If 0 < r ≤ min(g_a, 1)/2 and r^k Q_a ≥ 2^{1−k} 3ⁿ ε, then q̃ has exactly k zeros in |z − a| < r.
In particular, for r_a(ε) := (2^{1−k}3ⁿ ε/Q_a)^{1/k}, whenever r_a(ε) ≤ min(g_a, 1)/2, the k
roots of the cluster lie within r_a(ε) = O(ε^{1/k}) of a. The bound is Lipschitz for simple
orders, where Q_a = |q′(a)|.

````

### 71. Theorem S3 (combined stability)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Prop S1, Thm S2, Lemma S3 |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/stability/proof.md` |
| verifying script (existing) | theory/stability/roots_holder.py |
| audit evidence | `review/audit/stability/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*ST.8, `theory/stability/proof.md` lines 301-321:*

````
**Theorem S3 (heat coefficients → orders; the combined stability theorem).**

*Setting.* Let m be positive reals, n = |m|, μ = max m_i. Let H̃ be data with
δ := max_{−1≤ν≤n−2} |H̃_ν − H_ν(m)|. Put

- λ_μ := max(μ ℓ₀, max_{1≤r≤n−1} ℓ_r μ^{1−2r}), with ℓ = (2, 14, 498, 4062, …) as in §2;
- κ, ρ_n, ζ_n as in Theorem S2.

*Statement.* Suppose λ_μ δ ≤ 1 and κ ζ_n λ_μ δ ≤ 1/2. Then for every distinct order a, of
multiplicity k_a, with

  r_a := μ · (2^{2−k_a} 3ⁿ κ ρ_n λ_μ δ / Q̂_a)^{1/k_a} ≤ μ · min(ĝ_a, 1)/2,

the recovered polynomial q̃ has exactly k_a roots within r_a of a. Consequently, if the
radius hypothesis holds for **every** distinct order a,

  d(roots of q̃, m) ≤ max_a C_a δ^{1/k_a},  C_a = μ (2^{2−k_a} 3ⁿ κ ρ_n λ_μ / Q̂_a)^{1/k_a}.

So recovery is Lipschitz with constant C_a at simple orders, where Q̂_a = |q̂′(â)| measures the
gaps, and Hölder with exponent 1/k at a k-fold coincidence.

````

### 72. Proposition S3.2 (exponent 1/k sharp)

| field | value |
|---|---|
| status | PROVED |
| dependencies | Theorem B |
| external inputs | — |
| source file | `theory/stability/proof.md` |
| verifying script (existing) | theory/stability/roots_holder.py |
| audit evidence | `review/audit/stability/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | (ii) needs a != 0, g(0) != 0 and prod(z_i+z_j) != 0 so that the recovery is defined. |

*ST.9, `theory/stability/proof.md` lines 328-347:*

````
**Proposition S3.2 (the exponent 1/k is sharp).**

(i) *Double order, realisable data.* Take m(s) = (a+s, a−s, c₃, …, c_n). Then H(m(s)) is
smooth and even in s, so ‖H(m(s)) − H(m(0))‖_∞ = C s² + O(s⁴), while the orders move by
exactly s. No bound d ≤ C′δ^γ with γ > 1/2 can hold.

- Exactly, for a = 8, c = 2 (the pillow (2,8,8)): ΔR = 2s²/(8(64−s²)), ΔP₁ = 0, ΔP₃ = 48s².
- The ratio s/‖ΔH‖^{1/2} converges to 2.7385 for (2,8,8), 4.4630 for (3,3,12) and 2.0446 for
  (3,3,4,4), splitting the pair of 3s (splitting the pair of 4s gives 1.3593) (`roots_holder_output.md`).

(ii) *k-fold order, general data.* Take q_s(z) = ((z − a)^k − s^k) g(z), with g real monic
of degree n − k and g(a) ≠ 0.

- q_s has real coefficients, so its heat data H(q_s) are real. They are computed from e(q_s)
  through Newton's identities and R = e_{n−1}/e_n, and are within O(s^k) of H(m).
- By Theorem B the recovery map returns q_s, whose roots a + sω^j lie at distance exactly s
  from a. Hence the exponent 1/k cannot be improved.
- Ratios s/‖ΔH‖^{1/k} converge for k = 3 at (4,4,4), (7,7,7), (2,2,2,3), and for k = 4 at
  (5,5,5,5).

````

### 73. Remark S3.3

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `theory/stability/proof.md` |
| verifying script (existing) | theory/stability/roots_holder.py |
| audit evidence | `review/audit/stability/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*ST.10, `theory/stability/proof.md` lines 348-357:*

````
**Remark S3.3 (realisable data at a triple order).** The exponent 1/k concerns arbitrary data
vectors, which is the right model for noisy measurements. For data that are heat
coefficients of a *real* multiset near (a,a,a), the exponent is 1/2. For real d with
|d_i| ≤ a,

  (P₃ − 3a²P₁)(a + d) − (P₃ − 3a²P₁)(a) = 3a Σd_i² + Σd_i³ ≥ 2a Σd_i²,

so max|d_i| ≤ (|ΔP₃ − 3a²ΔP₁|/(2a))^{1/2}. This was checked on 900 random real perturbations.
No general statement for realisable data at mixed clusters is claimed.

````

### 74. Theorem S4 (explicit threshold)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Theorem S3 |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/stability/proof.md` |
| verifying script (existing) | theory/stability/threshold.py |
| audit evidence | `review/audit/stability/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*ST.11, `theory/stability/proof.md` lines 360-366:*

````
**Theorem S4 (explicit threshold).** Let m be integer orders. Define

  δ_thm(m) := min( 1/λ_μ,  1/(2κζ_nλ_μ),  min_a  Q̂_a 2^{k_a−1} / (3ⁿ (2μ)^{k_a} · 2κρ_nλ_μ) ).

If |H̃_ν − H_ν(m)| ≤ δ_thm(m) for ν = −1, …, n−2, then rounding the real parts of the roots
of q̃ returns m exactly.

````

### 75. Proposition S5 (certificates)

| field | value |
|---|---|
| status | PROVED |
| dependencies | Theorem B, Lemma S3 |
| external inputs | — |
| source file | `theory/stability/proof.md` |
| verifying script (existing) | theory/stability/threshold.py |
| audit evidence | `review/audit/stability/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Write out why (I-A)^{-1}1>0 gives rho(A)<1 and invertibility, and why the tan majorant bounds the tanh remainder; state the radius set and the integer hypothesis. |

*ST.12, `theory/stability/proof.md` lines 378-408:*

````
**Proposition S5 (certificates, exact arithmetic).**

*Input.* Fix m and componentwise radii ρ_ν ≥ 0. Every data vector with |H̃_ν − H_ν(m)| ≤ ρ_ν
is recovered exactly if either test below succeeds, with all quantities evaluated in
rational arithmetic (`threshold.py`).

*Common part.*

1. |δI| ≤ |L⁻¹|ρ.
2. Bound |δT_k| ≤ (|sech²U| ∗ |δU|)_k + [z^k](tan(U+|δU|) − tan U − sec²U·|δU|). The first
   term is the exact linear part. The second is the coefficientwise majorant of the
   remainder, valid because U ≥ 0.
3. Form the residual bound |r|, the bound |δM|, and A := |M⁻¹||δM|.
4. Certify ρ(A) < 1 by checking that v = (I − A)⁻¹𝟙 > 0.
5. Then |ẽ − e| ≤ E := (I − A)⁻¹|M⁻¹||r|.

*(i) Componentwise test.* For each distinct order a, some radius r ∈ {1/2, 19/40, …, 1/40,
1/100, 1/1000} satisfies

  r^{k_a} ∏_{b≠a}(|a−b| − r)^{k_b} > Σ_j E_j (a + r)^{n−j}.

*(ii) Coherent test.* Write ẽ − e = G·δH + ϱ, where:

- G = (D_I e) L⁻¹ is exact (Lemma S2.1);
- |ϱ| ≤ |M⁻¹||r_rem| + A E, with r_rem the remainder part of r.

On |z − a| = r, bound the first-order part through the exact Taylor coefficients at a of
the polynomials p_c(z) = Σ_j (−1)^j G_{jc} z^{n−j}. The test is

  r^{k_a} ∏(|a−b| − r)^{k_b} > Σ_c ρ_c Σ_l |p_c^{(l)}(a)/l!| r^l + Σ_j |ϱ_j| (a + r)^{n−j}.

````

*ST.13, `theory/stability/proof.md` lines 413-429:*

````
**Upper bound by construction.** For each order a, the search minimises
‖H(q̃) − H(m)‖_∞ over real monic polynomials of two shapes:

- q̃ = (z − c) g(z), with a real root at c = a ± 1/2;
- q̃ = ((z − c)² + y²) g(z), with a complex pair of real part c = a ± 1/2.

The optimiser is numerical. The reported minimiser is rebuilt exactly in rationals, and its
data are evaluated exactly. Its recovery is q̃ itself (Theorem B, checked by an exact solve),
and that q̃ has a root with real part exactly a ± 1/2. At that point rounding is a tie, so
δ_up is an infimum: arbitrarily small further perturbations push the root across, and
recovery fails at every level above δ_up. Hence the true threshold is at most δ_up.

*Rounding of printed values.* δ_thm and δ_cert are printed rounded **down**, and δ_up
rounded **up**, so that each printed number keeps its meaning. An adversarial search found
that the exact test fails at the up-rounded values 2.342e−3 and 1.462e−3, which an earlier
version printed.

````

### 76. Results table (delta_thm, delta_cert, delta_up)

| field | value |
|---|---|
| status | COMPUTATION |
| dependencies | Theorem S4, Proposition S5 |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/stability/proof.md` |
| verifying script (existing) | theory/stability/threshold.py |
| audit evidence | `review/audit/stability/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Every delta_thm, delta_cert, epsilon_cert re-certified exactly (P3). (2,2,2,2,3): delta_up <= 5.312e-05, ratio <= 6.72 (not 7.3/7.26). Regenerate threshold_output.md from threshold.py. |

*ST.14, `theory/stability/proof.md` lines 430-446:*

````
**Results** (`threshold_output.md`, `threshold_results.json`). The absolute model is
|δH_ν| ≤ δ for all ν. The relative precision listed is δ_cert/|H_ν| for ν = −1, …, n−2, and
ε_cert is the largest uniform relative error |δH_ν| ≤ ε|H_ν| that is certified.

| m | n | δ_thm | δ_cert | δ_up | δ_up/δ_cert | failure built at | δ_cert/|H_ν|, ν = −1..n−2 | ε_cert (uniform relative) |
|---|---|---|---|---|---|---|---|---|
| (2, 8, 8) | 3 | 3.80e-07 | 2.341e-03 | 2.485e-03 | 1.06 | 8−1/2 | 1.8e-02, 1.6e-03, 7.0e-04 | 1.9e-03 |
| (3, 3, 12) | 3 | 1.18e-07 | 4.040e-03 | 4.589e-03 | 1.14 | 3+1/2 | 3.2e-02, 2.8e-03, 7.4e-04 | 4.4e-03 |
| (3, 10, 15, 30) | 4 | 4.02e-11 | 3.660e-03 | 7.488e-03 | 2.05 | 10+1/2 | 4.9e-03, 8.0e-04, 4.1e-05, 3.6e-07 | 8.7e-04 |
| (4, 5, 21, 28) | 4 | 3.14e-11 | 1.461e-03 | 2.018e-03 | 1.38 | 5−1/2 | 1.9e-03, 3.2e-04, 1.6e-05, 1.7e-07 | 4.6e-04 |
| (2, 3, 7) | 3 | 4.49e-07 | 3.658e-03 | 6.587e-03 | 1.80 | 3−1/2 | 3.0e-01, 4.0e-03, 2.7e-03 | 5.0e-03 |
| (4, 4, 4) | 3 | 9.35e-07 | 4.539e-04 | 5.036e-04 | 1.11 | 4+1/2 | 3.6e-03, 5.0e-04, 5.4e-04 | 8.2e-04 |
| (7, 7, 7) | 3 | 9.97e-08 | 8.068e-05 | 8.273e-05 | 1.03 | 7−1/2 | 2.8e-04, 4.9e-05, 2.3e-05 | 1.2e-04 |
| (3, 3, 4, 4) | 4 | 1.48e-09 | 9.597e-05 | 1.195e-04 | 1.24 | 4−1/2 | 2.3e-04, 1.0e-04, 1.1e-04, 7.2e-05 | 1.1e-04 |
| (5, 5, 5, 5) | 4 | 4.74e-10 | 3.617e-05 | 3.826e-05 | 1.06 | 5−1/2 | 6.0e-05, 2.5e-05, 1.9e-05, 6.2e-06 | 3.1e-05 |
| (2, 2, 2, 3) | 4 | 2.03e-09 | 1.858e-04 | 2.520e-04 | 1.36 | 3−1/2 | 2.2e-03, 3.2e-04, 5.6e-04, 7.7e-04 | 4.3e-04 |
| (2, 2, 2, 2, 3) | 5 | 2.72e-12 | 7.908e-06 | 5.743e-05 | 7.26 | 2+1/2 | 2.3e-05, 1.2e-05, 2.1e-05, 2.9e-05, 1.9e-05 | 1.4e-05 |
````

### 77. Lemmas 1-2 (one inequality; adjacent separation)

| field | value |
|---|---|
| status | PROVED |
| dependencies | lem:chamber, lem:bound |
| external inputs | — |
| source file | `theory/threshold/proof.md` |
| verifying script (existing) | theory/threshold/threshold.py |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*TH.0, `theory/threshold/proof.md` lines 20-45:*

````
## 1. Notation (from `paper/main.tex`, Section `sec:threshold`)

A hyperbolic triad is $2\le p\le q\le r$ with $R=\frac1p+\frac1q+\frac1r<1$. The
$(S,p)$-stratum is the set of hyperbolic triads with $p+q+r=S$ and least order $p$.

- For $p\ge3$ it is nonempty for $S\ge3p$ except $(S,p)=(9,3)$, and it contains both its
  balanced and its spread triad. $(p,p,S-2p)$ is hyperbolic unless it is $(3,3,3)$.
- For $p=2$ it is nonempty iff $S\ge11$, and it never contains its spread triad.

By Lemma `lem:chamber` and Lemma `lem:bound`,
$$R^+_{S,p}=\frac2p+\frac1{S-2p},\qquad
R^-_{S,p}=\frac1p+\frac1{\lfloor D/2\rfloor}+\frac1{\lceil D/2\rceil},\quad D=S-p,$$
and
$$\varphi_p(S)=\frac4{S-p}-\frac1{S-2p-2},\qquad \tau_p=\frac{p-1}{p(p+1)}$$
as in the proof of Theorem `thm:separation`. Write $\operatorname{gap}_p(S)=R^-_{S,p}-R^+_{S,p+1}$.

**Definition.** The strata $p$ and $p+1$ *overlap at $S$* if their sets of reciprocal sums
have intersecting convex hulls.

Stratum $p=2$ is truncated by $R<1$. Its spread triad $(2,2,S-4)$ is not hyperbolic, so its
upper endpoint is the largest hyperbolic value, not $R^+_{S,2}$. Its lower endpoint
$R^-_{S,2}$ is attained iff $S\ge11$. For the two formal cases $(p,S)=(2,9),(2,10)$ covered by
"$S\ge3p+3$" below, stratum 2 is empty and $\operatorname{gap}_2(S)>0$, so all statements hold
trivially. Every other endpoint is attained. Brute-force agreement for $S\le600$ is in
`threshold.py` C5.

````

*TH.1, `theory/threshold/proof.md` lines 48-50:*

````
**Lemma 1 (one inequality).** For $S\ge3p+3$, the strata $p,p+1$ overlap at $S$ iff
$\operatorname{gap}_p(S)\le0$.

````

*TH.2, `theory/threshold/proof.md` lines 63-67:*

````
**Lemma 2 (adjacent separation suffices; the chain in the proof of `thm:separation`).** If
$\operatorname{gap}_p(S)>0$ for every $p$ with both strata $p,p+1$ nonempty at $S$, then all
strata of sum $S$ have pairwise disjoint reciprocal-sum sets, and $\sigma$ is injective on
triads of sum $S$.

````

### 78. Theorem 1 (closed form S*(p))

| field | value |
|---|---|
| status | PROVED |
| dependencies | Lemma 1 |
| external inputs | — |
| source file | `theory/threshold/proof.md` |
| verifying script (existing) | theory/threshold/threshold.py |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | P4: true for all p; p<=8 cases redone exactly. |

*TH.3, `theory/threshold/proof.md` lines 74-79:*

````
**Theorem 1.** For every $p\ge2$ let
$$S^*(p)=\begin{cases}18,&p=2,\\ 19,&p=3,\\ 3p+8,&4\le p\le8,\\ 3p+7,&p\ge9.\end{cases}$$
For $S\ge3p+3$, the strata $p$ and $p+1$ overlap at $S$ iff $S\ge S^*(p)$. Equivalently,
$S^*(p)$ is the least $S\ge x^*(p)=\dfrac{3p(p+1)}{p-1}=3p+6+\dfrac6{p-1}$ with $S\equiv p$
(mod 2), except for $p\ge9$, where the odd-parity sum $3p+7$ comes first.

````

### 79. Corollary 2 (no collision below 18)

| field | value |
|---|---|
| status | PROVED |
| dependencies | Theorem 1, Lemma 2 |
| external inputs | — |
| source file | `theory/threshold/proof.md` |
| verifying script (existing) | theory/threshold/threshold.py |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*TH.4, `theory/threshold/proof.md` lines 138-141:*

````
**Corollary 2.** For every $S\le17$, the map $\sigma=(S_1,R)$ is injective on hyperbolic
triads of sum $S$. At $S=18$ there is exactly one collision,
$\{\mathcal O(2,8,8),\mathcal O(3,3,12)\}$.

````

### 80. First-overlap vs first-collision table

| field | value |
|---|---|
| status | COMPUTATION |
| dependencies | — |
| external inputs | — |
| source file | `theory/threshold/proof.md` |
| verifying script (existing) | theory/threshold/threshold.py |
| audit evidence | `review/audit/threshold/` |
| audit verdict | NONE |
| in paper? | YES |
| note | All 14 rows reproduced. |

*TH.5, `theory/threshold/proof.md` lines 165-187:*

````
Overlap is necessary for a collision, not sufficient. The table compares $S^*(p)$ with the
first sum at which a triad of least order $p$ and one of least order $p+1$ share $R$. It comes
from exact enumeration of every hyperbolic triad with $S\le600$ (`threshold.py`, full table in
`first_overlap_vs_collision.csv`). The enumeration reproduces all 2,977 collision fibres of
`theory/diophantine/data/groups.csv` for $S\le600$. "Window" counts the triads of each stratum
lying in $[R^-_{S,p},R^+_{S,p+1}]$, the only candidates for an adjacent collision.

| $p$ | $x^*(p)$ | $S^*(p)$ | first collision | gap | window at $S^*$ / at collision | colliding pair |
|---|---|---|---|---|---|---|
| 2 | 18 | 18 | 18 | 0 | 1+1 / 1+1 | (2,8,8), (3,3,12) |
| 3 | 18 | 19 | 38 | 19 | 2+1 / 11+3 | (3,14,21), (4,6,28) |
| 4 | 20 | 20 | 20 | 0 | 1+1 / 1+1 | (4,8,8), (5,5,10) |
| 5 | 45/2 | 23 | 117 | 94 | 1+1 / 49+12 | (5,32,80), (6,15,96) |
| 6 | 126/5 | 26 | 34 | 8 | 2+1 / 6+3 | (6,14,14), (7,9,18) |
| 7 | 28 | 29 | 62 | 33 | 2+1 / 18+8 | (7,20,35), (8,14,40) |
| 8 | 216/7 | 32 | 64 | 32 | 2+1 / 18+8 | (8,20,36), (9,15,40) |
| 9 | 135/4 | 34 | 42 | 8 | 1+1 / 5+3 | (9,15,18), (10,12,20) |
| 10 | 110/3 | 37 | 109 | 72 | 1+1 / 37+18 | (10,44,55), (11,28,70) |
| 11 | 198/5 | 40 | 66 | 26 | 1+1 / 14+8 | (11,22,33), (12,18,36) |
| 12 | 468/11 | 43 | 188 | 145 | 1+1 / 74+34 | (12,72,104), (13,45,130) |
| 13 | 91/2 | 46 | 94 | 48 | 1+1 / 25+15 | (13,39,42), (14,28,52) |
| 14 | 630/13 | 49 | 69 | 20 | 1+1 / 11+7 | (14,20,35), (15,18,36) |
| 22 | 506/7 | 73 | 422 | 349 | 1+1 / 176+96 | (22,92,308), (23,77,322) |
````

### 81. Proposition 3 (tangency only at p=2,4)

| field | value |
|---|---|
| status | PROVED |
| dependencies | Theorem 1 |
| external inputs | — |
| source file | `theory/threshold/proof.md` |
| verifying script (existing) | theory/threshold/threshold.py |
| audit evidence | `review/audit/threshold/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | P4: add 'S >= 3p+3' to part (1) (at S=3p+2 the gap is formally 0 for every p). |

*TH.6, `theory/threshold/proof.md` lines 193-198:*

````
**Proposition 3 (why the gap is positive except at $p=2,4$).**

1. The balanced triad of stratum $p$ and the spread triad of stratum $p+1$ have equal $R$
   (a tangency) iff $p\in\{2,4\}$, at $S=x^*(p)$.
2. For every $p\notin\{2,4\}$ the first adjacent collision occurs strictly after $S^*(p)$.

````

### 82. Flat-cone input (Kokotov)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | Kokotov Prop 1, Thm 1; Uçar Thm 4.20 at kappa=0 |
| source file | `theory/curvature/proof.md` |
| verifying script (existing) | theory/curvature/curvature_checks.py |
| audit evidence | `review/audit/curvature-divergence/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Kokotov's deficiency space is span{chi, chi log r}; the orbifold domain forces Friedrichs. DGGW 4.8 does not give the vanishing or the remainder. |

*CU.0, `theory/curvature/proof.md` lines 37-54:*

````
## 1. Conventions

All orbifolds are closed and orientable, with cone points as the only singularities (no
mirrors). Such an orbifold of genus $g$ with orders $m_1,\dots,m_n\ge2$ has
$\chi=2-2g-\sum_i(1-1/m_i)$, and a constant-curvature metric of sign $\operatorname{sgn}\chi$
exists iff it is good (Thurston, Thm 13.3.6).

Heat coefficients are counted as in Theorem A: the first $k$ coefficients are those of
$t^{-1},t^0,\dots,t^{k-2}$. For a class $\mathcal C$, $K_{\rm mult}(\mathcal C)$ is the least $k$
such that, for every metric of the allowed kind, the first $k$ coefficients determine the
cone-order multiset on $\mathcal C$. When the curvature is normalised to $K=\pm1$ the area is
fixed by $\chi$. For $K=0$ the area is a free parameter.

- Parts 1, 2 and 4 below hold whether or not $K$ is normalised, because the coefficient that
  does the work, $t^0$, is scale-invariant.
- Part 3 is stated for $K=-1$, as in Theorem A. With $K$ free and only the area common, the
  triangular structure of Theorem A is not available, and no claim is made.

````

*CU.1, `theory/curvature/proof.md` lines 57-76:*

````
**Flat cones and flat orbifolds.**

- Kokotov's Proposition 1 gives the exact local statement on an infinite flat cone of angle
  $\beta$: area term plus $\frac1{12}(\frac{2\pi}\beta-\frac\beta{2\pi})$, plus
  $O(e^{-\epsilon/t})$, with nothing at any other order.
- His Theorem 1 globalises this to every compact flat surface with conical points:
  $$\operatorname{Tr}e^{-t\Delta}=\frac{\operatorname{Area}}{4\pi t}+\frac1{12}\sum_k
  \Big(\frac{2\pi}{\beta_k}-\frac{\beta_k}{2\pi}\Big)+O(e^{-\epsilon/t}).\tag{F}$$
- A flat orientable orbifold is such a surface with $\beta_k=2\pi/m_k$. Its Laplacian is
  Kokotov's Friedrichs extension: for $\beta\le2\pi$ only the bounded mode enters his
  deficiency space (p. 9), and the Friedrichs domain consists of the functions bounded at the
  vertex, which is the orbifold domain. So its expansion is
  $\frac{A}{4\pi t}+\sum_i\frac{m_i^2-1}{12m_i}$. The same follows from DGGW Thm 4.8, whose
  coefficients are integrals of curvature polynomials, plus $b_\ell=K^\ell\cdot(\cdots)$.
- Every coefficient of $t^\ell$, $\ell\ge1$, vanishes identically. At $K=0$ Uçar's coefficients
  vanish for every $\ell\ge1$ and every $m$, trivially, because of the factor $K^\ell$. F3 is a
  bookkeeping check of this. At $K\neq0$ none
  vanishes for $m\ge2$; positivity for all $\ell$ is proved in `theory/divergence/proof.md`,
  Lemma 1.

````

### 83. Lemma 2 (invariant multiplicities)

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `theory/curvature/proof.md` |
| verifying script (existing) | theory/curvature/curvature_checks.py |
| audit evidence | `review/audit/curvature-divergence/` |
| audit verdict | MINOR |
| in paper? | REMARK ONLY |
| note | Classical (Molien/Frobenius). |

*CU.2, `theory/curvature/proof.md` lines 92-95:*

````
**Lemma 2 (invariant multiplicities).** Let $G\subset SO(3)$ be finite, with $S^2/G$ having cone
orders $m_1,\dots,m_k$. The multiplicity of the eigenvalue $\ell(\ell+1)$ on $S^2/G$ is
$$N_\ell=\frac{2\ell+1}{|G|}+\frac12\sum_{i=1}^k\Big[2\Big\lfloor\frac\ell{m_i}\Big\rfloor+1-\frac{2\ell+1}{m_i}\Big].$$

````

### 84. Proposition (curvature comparison), Parts 1-2

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Lemma 2 |
| external inputs | DGGW Thm 5.15, Prop 5.22; Thurston 13.3.6 |
| source file | `theory/curvature/proof.md` |
| verifying script (existing) | theory/curvature/curvature_checks.py |
| audit evidence | `review/audit/curvature-divergence/` |
| audit verdict | MINOR |
| in paper? | CITE AS PRIOR WORK |
| note | DGGW Thm 5.15 / Prop 5.22 and Uçar Cor 4.21(iv); 'for every n' should be n>=2. |

*CU.3, `theory/curvature/proof.md` lines 121-168:*

````
**Proposition (curvature comparison).**

1. **$K=0$.** The closed orientable flat 2-orbifolds are $T^2$, $S^2(2,2,2,2)$, $S^2(3,3,3)$,
   $S^2(2,4,4)$ and $S^2(2,3,6)$.
   - For every flat metric, the heat expansion is $\frac A{4\pi t}+c_0+O(e^{-\epsilon/t})$, with
     $c_0=0,\frac12,\frac23,\frac34,\frac56$ respectively.
   - The constant term alone determines the orbifold. $K_{\rm mult}=2$, and this is sharp,
     since the area term carries no cone information.
   - All coefficients of $t^\ell$, $\ell\ge1$, vanish identically.
2. **$K=+1$.** The good closed orientable spherical 2-orbifolds are $S^2$, $S^2(n,n)$ and
   $S^2(2,2,n)$ ($n\ge2$), and $S^2(2,3,3)$, $S^2(2,3,4)$, $S^2(2,3,5)$. The bad orbifolds
   $S^2(n)$ and $S^2(n_1,n_2)$ with $n_1<n_2$ are excluded, since they carry no
   constant-curvature metric.
   - On this class the constant term
     $a_0=\frac\chi6+\sum_i\frac{m_i^2-1}{12m_i}$ alone determines the orbifold, so
     $K_{\rm mult}=2$.
   - The $t^{-1}$ coefficient alone does not, even with $K=1$ fixed:
     $\chi(S^2(2,2,n))=\chi(S^2(2n,2n))=1/n$ for every $n$.
   - The higher coefficients are nonzero (the amplifier is on) but are never needed.
3. **$K=-1$, genus 0, $n$ cone points.** $K_{\rm mult}\le n$ for every $n\ge3$ (Theorem A).
   Equality holds for $n=3,4$ by explicit integer witnesses. Over real orders, $n-1$
   coefficients never suffice (Theorem C(2)). Integer sharpness for $n\ge5$ is open.
4. **Flat cone surfaces that are not orbifolds.** On closed flat surfaces with conical points,
   the heat coefficients are exactly the area and $\sum_k(\frac{2\pi}{\beta_k}-\frac{\beta_k}
   {2\pi})$. Hence:
   - Among doubled Euclidean triangles (flat cone spheres with three cone points), every
     surface other than the doubled equilateral triangle shares all heat coefficients with a
     one-parameter family of pairwise non-isometric ones.
   - The heat coefficients do not detect whether a flat cone sphere is an orbifold. The doubled
     triangles with angles $\pi(\frac14,\frac14,\frac12)$ (the orbifold $S^2(2,4,4)$) and
     $\pi(\frac15,\frac25,\frac25)$ (cone angles $\frac{2\pi}5,\frac{4\pi}5,\frac{4\pi}5$, not
     an orbifold) have the same area and every heat coefficient in common.

**Strength.** Parts 1 and 2 are the good-orbifold restriction of DGGW Theorem 5.15, split by
the sign of $K$. That theorem is strictly stronger: its invariant $c$ ($12\times$ the $t^0$
coefficient) separates all closed orientable 2-orbifolds with $\chi\ge0$ at once, bad ones and
smooth surfaces included.

- $K_{\rm mult}\le2$ is therefore DGGW's result, and the sharpness ($\ne1$) is elementary.
- Part 2 is also covered by DGGW Proposition 5.22 (spherical, non-orientable included) and by
  Uçar Cor. 4.21(iv) (any $\kappa\ne0$).
- What is added here:
  - an independent derivation of the spherical expansion from the spectrum (Lemma 2, S2);
  - placing the three geometries side by side in one count;
  - Part 4.

Part 3 is Theorem A of `theory/audibility/proof.md`. Part 4 rests on Kokotov's Theorem 1 and
is elementary given it.
````

### 85. Proposition (curvature comparison), Part 3

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Theorem A, Theorem C |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/curvature/proof.md` |
| verifying script (existing) | theory/audibility/sharpness_search.py |
| audit evidence | `review/audit/curvature-divergence/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*CU.3, `theory/curvature/proof.md` lines 121-168:*

````
**Proposition (curvature comparison).**

1. **$K=0$.** The closed orientable flat 2-orbifolds are $T^2$, $S^2(2,2,2,2)$, $S^2(3,3,3)$,
   $S^2(2,4,4)$ and $S^2(2,3,6)$.
   - For every flat metric, the heat expansion is $\frac A{4\pi t}+c_0+O(e^{-\epsilon/t})$, with
     $c_0=0,\frac12,\frac23,\frac34,\frac56$ respectively.
   - The constant term alone determines the orbifold. $K_{\rm mult}=2$, and this is sharp,
     since the area term carries no cone information.
   - All coefficients of $t^\ell$, $\ell\ge1$, vanish identically.
2. **$K=+1$.** The good closed orientable spherical 2-orbifolds are $S^2$, $S^2(n,n)$ and
   $S^2(2,2,n)$ ($n\ge2$), and $S^2(2,3,3)$, $S^2(2,3,4)$, $S^2(2,3,5)$. The bad orbifolds
   $S^2(n)$ and $S^2(n_1,n_2)$ with $n_1<n_2$ are excluded, since they carry no
   constant-curvature metric.
   - On this class the constant term
     $a_0=\frac\chi6+\sum_i\frac{m_i^2-1}{12m_i}$ alone determines the orbifold, so
     $K_{\rm mult}=2$.
   - The $t^{-1}$ coefficient alone does not, even with $K=1$ fixed:
     $\chi(S^2(2,2,n))=\chi(S^2(2n,2n))=1/n$ for every $n$.
   - The higher coefficients are nonzero (the amplifier is on) but are never needed.
3. **$K=-1$, genus 0, $n$ cone points.** $K_{\rm mult}\le n$ for every $n\ge3$ (Theorem A).
   Equality holds for $n=3,4$ by explicit integer witnesses. Over real orders, $n-1$
   coefficients never suffice (Theorem C(2)). Integer sharpness for $n\ge5$ is open.
4. **Flat cone surfaces that are not orbifolds.** On closed flat surfaces with conical points,
   the heat coefficients are exactly the area and $\sum_k(\frac{2\pi}{\beta_k}-\frac{\beta_k}
   {2\pi})$. Hence:
   - Among doubled Euclidean triangles (flat cone spheres with three cone points), every
     surface other than the doubled equilateral triangle shares all heat coefficients with a
     one-parameter family of pairwise non-isometric ones.
   - The heat coefficients do not detect whether a flat cone sphere is an orbifold. The doubled
     triangles with angles $\pi(\frac14,\frac14,\frac12)$ (the orbifold $S^2(2,4,4)$) and
     $\pi(\frac15,\frac25,\frac25)$ (cone angles $\frac{2\pi}5,\frac{4\pi}5,\frac{4\pi}5$, not
     an orbifold) have the same area and every heat coefficient in common.

**Strength.** Parts 1 and 2 are the good-orbifold restriction of DGGW Theorem 5.15, split by
the sign of $K$. That theorem is strictly stronger: its invariant $c$ ($12\times$ the $t^0$
coefficient) separates all closed orientable 2-orbifolds with $\chi\ge0$ at once, bad ones and
smooth surfaces included.

- $K_{\rm mult}\le2$ is therefore DGGW's result, and the sharpness ($\ne1$) is elementary.
- Part 2 is also covered by DGGW Proposition 5.22 (spherical, non-orientable included) and by
  Uçar Cor. 4.21(iv) (any $\kappa\ne0$).
- What is added here:
  - an independent derivation of the spherical expansion from the spectrum (Lemma 2, S2);
  - placing the three geometries side by side in one count;
  - Part 4.

Part 3 is Theorem A of `theory/audibility/proof.md`. Part 4 rests on Kokotov's Theorem 1 and
is elementary given it.
````

### 86. Proposition (curvature comparison), Part 4

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | Kokotov Thm 1 |
| source file | `theory/curvature/proof.md` |
| verifying script (existing) | theory/curvature/curvature_checks.py |
| audit evidence | `review/audit/curvature-divergence/` |
| audit verdict | MINOR |
| in paper? | REMARK ONLY |
| note | Say 'rescaled to the same area'; name the Friedrichs extension. |

*CU.3, `theory/curvature/proof.md` lines 121-168:*

````
**Proposition (curvature comparison).**

1. **$K=0$.** The closed orientable flat 2-orbifolds are $T^2$, $S^2(2,2,2,2)$, $S^2(3,3,3)$,
   $S^2(2,4,4)$ and $S^2(2,3,6)$.
   - For every flat metric, the heat expansion is $\frac A{4\pi t}+c_0+O(e^{-\epsilon/t})$, with
     $c_0=0,\frac12,\frac23,\frac34,\frac56$ respectively.
   - The constant term alone determines the orbifold. $K_{\rm mult}=2$, and this is sharp,
     since the area term carries no cone information.
   - All coefficients of $t^\ell$, $\ell\ge1$, vanish identically.
2. **$K=+1$.** The good closed orientable spherical 2-orbifolds are $S^2$, $S^2(n,n)$ and
   $S^2(2,2,n)$ ($n\ge2$), and $S^2(2,3,3)$, $S^2(2,3,4)$, $S^2(2,3,5)$. The bad orbifolds
   $S^2(n)$ and $S^2(n_1,n_2)$ with $n_1<n_2$ are excluded, since they carry no
   constant-curvature metric.
   - On this class the constant term
     $a_0=\frac\chi6+\sum_i\frac{m_i^2-1}{12m_i}$ alone determines the orbifold, so
     $K_{\rm mult}=2$.
   - The $t^{-1}$ coefficient alone does not, even with $K=1$ fixed:
     $\chi(S^2(2,2,n))=\chi(S^2(2n,2n))=1/n$ for every $n$.
   - The higher coefficients are nonzero (the amplifier is on) but are never needed.
3. **$K=-1$, genus 0, $n$ cone points.** $K_{\rm mult}\le n$ for every $n\ge3$ (Theorem A).
   Equality holds for $n=3,4$ by explicit integer witnesses. Over real orders, $n-1$
   coefficients never suffice (Theorem C(2)). Integer sharpness for $n\ge5$ is open.
4. **Flat cone surfaces that are not orbifolds.** On closed flat surfaces with conical points,
   the heat coefficients are exactly the area and $\sum_k(\frac{2\pi}{\beta_k}-\frac{\beta_k}
   {2\pi})$. Hence:
   - Among doubled Euclidean triangles (flat cone spheres with three cone points), every
     surface other than the doubled equilateral triangle shares all heat coefficients with a
     one-parameter family of pairwise non-isometric ones.
   - The heat coefficients do not detect whether a flat cone sphere is an orbifold. The doubled
     triangles with angles $\pi(\frac14,\frac14,\frac12)$ (the orbifold $S^2(2,4,4)$) and
     $\pi(\frac15,\frac25,\frac25)$ (cone angles $\frac{2\pi}5,\frac{4\pi}5,\frac{4\pi}5$, not
     an orbifold) have the same area and every heat coefficient in common.

**Strength.** Parts 1 and 2 are the good-orbifold restriction of DGGW Theorem 5.15, split by
the sign of $K$. That theorem is strictly stronger: its invariant $c$ ($12\times$ the $t^0$
coefficient) separates all closed orientable 2-orbifolds with $\chi\ge0$ at once, bad ones and
smooth surfaces included.

- $K_{\rm mult}\le2$ is therefore DGGW's result, and the sharpness ($\ne1$) is elementary.
- Part 2 is also covered by DGGW Proposition 5.22 (spherical, non-orientable included) and by
  Uçar Cor. 4.21(iv) (any $\kappa\ne0$).
- What is added here:
  - an independent derivation of the spherical expansion from the spectrum (Lemma 2, S2);
  - placing the three geometries side by side in one count;
  - Part 4.

Part 3 is Theorem A of `theory/audibility/proof.md`. Part 4 rests on Kokotov's Theorem 1 and
is elementary given it.
````

### 87. Lemma 1 (generating function, positivity, poles)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | — |
| external inputs | Uçar (4.25), (3.69) |
| source file | `theory/divergence/proof.md` |
| verifying script (existing) | theory/divergence/divergence.py |
| audit evidence | `review/audit/curvature-divergence/` |
| audit verdict | NONE |
| in paper? | REMARK ONLY |
| note | — |

*DV.0, `theory/divergence/proof.md` lines 32-44:*

````
## 1. Notation

$$A_\ell(m)=\frac{(2\ell)!}{\ell!\;m\sin(\pi/m)}\Big(\frac m{2\pi}\Big)^{2\ell+1},\qquad
\sigma_m=\frac{\pi/m}{\sin(\pi/m)} .$$

By Stirling, $A_\ell(m)=\ell!\,(m^2/\pi^2)^\ell\cdot\frac{1}{2\pi\sin(\pi/m)\sqrt{\pi\ell}}
(1+O(1/\ell))$.

Uçar's coefficients are $b_\ell(m)=K^\ell\beta_\ell(m)$, with
$\beta_\ell(m)=\sum_{i=0}^\ell\frac2{4^ii!}c_{\ell-i}(\pi/m)$ and $c_\ell$ given by (4.25). In
the manuscript's notation $p_\ell(m)=m\,\beta_\ell(m)$. $\beta_\ell$ does not depend on $K$, so
any statement about $\beta_\ell$ holds for $K=+1$ and $K=-1$ alike.

````

*DV.1, `theory/divergence/proof.md` lines 47-59:*

````
**Lemma 1.** Let
$$G_k(t)=\frac{t/2}{\sinh(t/2)}\Big[\frac{kt}2\coth\frac{kt}2-\frac t2\coth\frac t2\Big]
=\sum_Ng_N(k)t^N .$$
Then:

- (a) $c_\ell(\pi/k)=\dfrac{(-1)^\ell(2\ell+2)!}{4k(\ell+1)!(2\ell+1)}\,g_{2\ell+2}(k)$.
- (b) $(-1)^\ell g_{2\ell+2}(k)>0$ for all $\ell\ge0$ and $k\ge2$. Hence $c_\ell(\pi/k)>0$ and
  $\beta_\ell(k)>0$ for every $\ell$.
- (c) For fixed $k\ge2$ and every $\rho<1$,
  $g_{2\ell+2}(k)=2(-1)^\ell\sigma_k(k/2\pi)^{2\ell+2}(1+O((2\rho)^{-2\ell}))$. For $k\ge3$ the
  relative error is in fact $\Theta(4^{-\ell})$. For $k=2$ it is $O(9^{-\ell})$, since
  $G_2(t)=(t/2)^2\operatorname{sech}(t/2)$ has its next poles at $\pm3\pi i$.

````

### 88. Theorem 2 (asymptotics of b_l(m))

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Lemma 1 |
| external inputs | Uçar (4.25), (4.33) |
| source file | `theory/divergence/proof.md` |
| verifying script (existing) | theory/divergence/divergence.py |
| audit evidence | `review/audit/curvature-divergence/` |
| audit verdict | MINOR |
| in paper? | REMARK ONLY |
| note | Second form follows from the first but is not equivalent. |

*DV.2, `theory/divergence/proof.md` lines 101-108:*

````
**Theorem 2.** For fixed $m\ge2$, as $\ell\to\infty$,
$$\frac{b_\ell(m)}{K^\ell}=A_\ell(m)\Big(1+\frac{\pi^2}{2m^2(2\ell-1)}+O(\ell^{-2})\Big).$$
Equivalently, with $\lambda_\ell=|B_{2\ell+2}|/(2(\ell+1)!(2\ell+1))$, the leading coefficient
of $p_\ell$,
$$\frac{p_\ell(m)}{\lambda_\ell\,m^{2\ell+2}}\longrightarrow\sigma_m=\frac{\pi/m}{\sin(\pi/m)} .$$
So the full polynomial exceeds its leading term by the factor $\sigma_m$, which lies in
$(1,\pi/2]$.

````

### 89. Theorem 3 (divergence rate hears M)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Theorem 2, Lemma 1(b) |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20, (4.35); Thurston 13.3.5 |
| source file | `theory/divergence/proof.md` |
| verifying script (existing) | theory/divergence/divergence.py |
| audit evidence | `review/audit/curvature-divergence/` |
| audit verdict | MINOR |
| in paper? | REMARK ONLY |
| note | Genus-10^4 test: the smooth part dominates for l<=8 (not l<=5). |

*DV.3, `theory/divergence/proof.md` lines 155-177:*

````
**Theorem 3.** Let $K\in\{-1,+1\}$, $C\ge0$, and let $m_1,\dots,m_n$ ($n\ge1$) be integers
$\ge2$ with largest value $M$ of multiplicity $\mu$. Let
$$a_\ell=C\,s_{\ell+1}K^{\ell+1}+K^\ell\sum_i\beta_\ell(m_i).$$
This covers the heat coefficients ($t^\ell$, $\ell\ge0$) of every closed orientable 2-orbifold of
constant curvature $K$ with cone points $m_i$, of any genus, with $C=|\chi|/2$. It also covers
the partial sequences left after peeling. Then
$$\frac{a_\ell}{K^\ell}=\mu\,A_\ell(M)\Big(1+O(1/\ell)+O\Big(\sum_{m_i<M}(m_i/M)^{2\ell}\Big)
+O(C\,\ell\,M^{-2\ell})\Big).$$
Consequently
$$\lim_{\ell\to\infty}\frac{2\pi^2\,|a_\ell|}{(2\ell-1)\,|a_{\ell-1}|}=M^2,\qquad
\lim_{\ell\to\infty}\frac{|a_\ell|}{\ell\,|a_{\ell-1}|}=\frac{M^2}{\pi^2},\qquad
\mu=\lim_{\ell\to\infty}\frac{a_\ell}{K^\ell A_\ell(M)} .$$
If $n=0$ (and $C>0$), the first two limits are $1$ and $1/\pi^2$. There the convergence is only
$O(1/\ell)$, because $s_{\ell+1}$ carries an extra factor $\ell$.

The error terms are not uniform over orbifolds. Many copies of a slightly smaller order, or a
huge $|\chi|$, delay the asymptotic regime. Independent tests:

- $1000\times49$ together with one cone of order 50: the estimator still rounds to 49 at
  $\ell=150$.
- Genus $10^4$ with one cone of order 2: the smooth part dominates, with the opposite sign, for
  $\ell\le5$.

````

### 90. Corollary 4 (peeling)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Theorem 3 |
| external inputs | Uçar (4.25)/(4.33), Thm 4.20 |
| source file | `theory/divergence/proof.md` |
| verifying script (existing) | theory/divergence/divergence.py |
| audit evidence | `review/audit/curvature-divergence/` |
| audit verdict | MINOR |
| in paper? | REMARK ONLY |
| note | s_k>0 is used but not proved (one-line proof in the audit); 'and K' can be dropped. Uçar Cor 4.21(iv) already gives the determination. |

*DV.4, `theory/divergence/proof.md` lines 199-203:*

````
**Corollary 4 (peeling).** For every $L$, the tail $(a_\ell)_{\ell\ge L}$ and $K$ determine the
cone-order multiset, $\chi$, the area and the genus. The inputs assumed known are $K$, Uçar's
(4.25)/(4.33) and $s_k>0$. This tail-only form is a small strengthening of Uçar's
Cor. 4.21(iv), whose extraction starts at $\nu=0$ and uses the area.

````

### 91. Borel reading

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Theorem 3 |
| external inputs | Dunne arXiv:2109.03897; Li-Li-Tang Ex. 2.30 |
| source file | `theory/divergence/proof.md` |
| verifying script (existing) | theory/divergence/divergence.py |
| audit evidence | `review/audit/curvature-divergence/` |
| audit verdict | MINOR |
| in paper? | REMARK ONLY |
| note | Needs n>=1. |

*DV.5, `theory/divergence/proof.md` lines 233-246:*

````
**Borel reading (stated, not proved beyond the radius).** By Theorem 3 the Borel transform
$\sum a_\ell\zeta^\ell/\ell!$ has radius of convergence exactly $\pi^2/M^2$. All
$a_\ell/K^\ell>0$ for large $\ell$. By Pringsheim's theorem (applied in the variable $K\zeta$,
after removing finitely many terms), the point $\zeta=K\pi^2/M^2$ on the circle of convergence is
a singularity:

- on the negative axis for hyperbolic orbifolds;
- on the positive axis for spherical ones.

The smooth heat kernel of $\mathbb H^2$ or $S^2$ has its nearest Borel singularity at distance
$\pi^2$ (Dunne, arXiv:2109.03897; Li–Li–Tang, arXiv:2606.21909). A cone of order $M$ pulls it in
by the factor $M^2$. Nothing is claimed here about the analytic continuation or about Borel
summability.

````

### 92. Proposition 1 (reformulation on C_lambda)

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `theory/diophantine/variety.md` |
| verifying script (existing) | theory/diophantine/variety_checks.py |
| audit evidence | `review/audit/diophantine/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | 'primitive sums' -> 'primitive triples t_i with sums s_i'; the rescaled triples lie in a class that may contain more points. |

*DI.1, `theory/diophantine/variety.md` lines 18-33:*

````
**Proposition 1.** Two triples with the same sum $S$ have the same $R$ if and
only if they have the same $\lambda$. Conversely, let $t_1,\dots,t_k$ be
pairwise non-proportional positive integer triples with a common
$\lambda$, primitive sums $s_i$, and $L=\operatorname{lcm}(s_i)$. Then the
rescaled triples $(L/s_i)\,t_i$ form a degeneracy class at sum $L$, and it is
primitive. Its multiples $mL$ are its scaled copies. It is hyperbolic as soon
as $mL>\lambda$, since $R=\lambda/(mL)$, and all entries are $\ge2$.

So a degeneracy class is a finite set of positive rational points on one
plane cubic

$$C_\lambda:\ (x+y+z)(xy+yz+zx)=\lambda\,xyz ,$$

and the counting problem is how often a cubic in this pencil carries two or
more positive rational points of small height.

````

### 93. Pencil, Weierstrass model, fibres, generic torsion

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Proposition 1 |
| external inputs | Beauville 1982 (table row); BGN 1993; Shioda (unretrieved, remark only) |
| source file | `theory/diophantine/variety.md` |
| verifying script (existing) | theory/diophantine/variety_checks.py |
| audit evidence | `review/audit/diophantine/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Base-point orders in listed order are 6,6,2,1,3,3 (not 1,2,3,3,6,6). |

*DI.2, `theory/diophantine/variety.md` lines 36-77:*

````
* **The pencil.** We have $(x+y)(y+z)(z+x)=e_1e_2-e_3$. So $C_\lambda$ is the
  member $t=1-\lambda$ of the pencil $(X+Y)(Y+Z)(Z+X)+tXYZ=0$. Beauville's
  theorem (C. R. Acad. Sci. Paris 294 (1982), Théorème and Tableau, p. 658)
  lists exactly this pencil, in the row he labels $\Gamma^0_0(6)$, with
  singular-fibre components 6, 3, 2, 1. The change of variables is the
  identity with $t=1-\lambda$ (asserted, `variety_checks.py` §2).
* **Weierstrass model.** Derived here and checked by sympy. The
  explicit maps to Bremner–Guy–Nowakowski's model are asserted in §3c: the
  forward map $\sigma=-4e_2/z^2$, $\tau=4\lambda(\lambda-1)(x-y)/(x+y-(\lambda-1)z)$,
  and the inverse $(x+y)/z=\sigma(\lambda-1)/(\sigma-4\lambda)$,
  $(x-y)/z=\tau\big((x+y)/z-\lambda+1\big)/(4\lambda(\lambda-1))$. So BGN's
  curve is $C_\lambda$ over $\mathbf Q$ itself, not a twist. Our own model:
  $$y^2=x^3+(\lambda-3)^2x^2+8(\lambda-3)(\lambda-1)x+16(\lambda-1)^2,\qquad
  \Delta=2^{12}\lambda^2(\lambda-9)(\lambda-1)^3 .$$
  Its $j$-invariant agrees with the model of Bremner–Guy–Nowakowski
  (Math. Comp. 61 (1993) 117–130, DOI 10.1090/s0025-5718-1993-1189516-5):
  $\tau^2=\sigma(\sigma^2+(n^2-6n-3)\sigma+16n)$. Their paper studies exactly
  this curve, for integer $n$, as "Knight's problem"
  $n=(x+y+z)(1/x+1/y+1/z)$.
* **Fibre types.** $I_6$ at $\lambda=\infty$, $I_3$ at $1$, $I_2$ at $0$, $I_1$
  at $9$. The Euler numbers sum to 12, so the pencil, blown up at its 9 base
  points, is a rational elliptic surface $\mathcal E\to\mathbf P^1_\lambda$.
  For every $\lambda\notin\{0,1,9,\infty\}$, $C_\lambda$ is a smooth genus-one
  curve. The positive values relevant here satisfy $\lambda>9$ by AM–HM; at
  $\lambda=9$ only the point $(1:1:1)$ is positive.
* **Mordell–Weil over $\overline{\mathbf Q}(\lambda)$** (a remark; it rests on Shioda,
  Comment. Math. Univ. St. Pauli 39 (1990) 211–240, Thm 1.3 as reported by zbMATH,
  whose text is unretrieved). By the Shioda–Tate count the
  rank is $8-\sum_v(m_v-1)=8-(5+2+1)=0$. The six base points
  $(1{:}0{:}0),(0{:}1{:}0),(0{:}0{:}1),(1{:}{-1}{:}0),(0{:}1{:}{-1}),(1{:}0{:}{-1})$
  are sections of orders $1,2,3,3,6,6$ (base point $O=(1{:}{-1}{:}0)$). So the
  generic Mordell–Weil group is $\mathbf Z/6$, matching BGN's statement that
  the torsion is $\mathbf Z/6$ except at $n=10$. **No section of infinite
  order exists.** Every infinite family of degeneracies is therefore either
  torsion-driven or comes from a base change (a rational curve in the
  $\lambda$-line's covers), never from a "constant" point.
* **Real picture.** The positive points of $C_\lambda$ form a whole
  connected component, the oval (BGN's "egg"). The base points lie on the
  coordinate lines, which positive points never approach, since $\lambda\to\infty$
  there. So the egg is the non-identity component, and BGN state that "if $P$
  is on the egg, then just the odd multiples of $P$ give positive solutions".

````

### 94. Reciprocation = 2-torsion translation; dual family

| field | value |
|---|---|
| status | PROVED |
| dependencies | Proposition 1 |
| external inputs | BGN p. 120 |
| source file | `theory/diophantine/variety.md` |
| verifying script (existing) | theory/diophantine/variety_checks.py, families.py |
| audit evidence | `review/audit/diophantine/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | 'Differs by a point of infinite order' needs its short proof; the 12-point orbit holds for non-torsion P. |

*DI.3, `theory/diophantine/variety.md` lines 80-104:*

````
The Vieta move $(p,q,r)\mapsto(qr/p,q,r)$ preserves $\lambda$, and up to
permutation it is reciprocation. With base point $O=(1{:}{-1}{:}0)$:

- the line through $P=(x{:}y{:}z)$ and $T_2=(0{:}0{:}1)$ meets $C_\lambda$
  again at $(xz{:}yz{:}xy)$;
- the line through $O$ and that point meets it again at
  $(yz{:}xz{:}xy)=(1/x{:}1/y{:}1/z)$.

Hence $P+T_2=\iota(P)$ **exactly**, for every point of every $C_\lambda$,
and $2T_2=O$ because $\iota$ is an involution. This is proved symbolically
in `variety_checks.py` §5. BGN's table (p. 120) records the same relation
in their model. Two consequences follow.

* **Every triple has a degeneracy partner.** For $t=(a,b,c)$,
  $$\{\,e_2(t)\,(a,b,c),\ e_1(t)\,(bc,ca,ab)\,\}\quad\text{has}\quad S=e_1e_2,\ R=1/e_3 ,$$
  divided by the gcd of its six entries. This is the **dual family**. It
  fails only for geometric progressions, which are self-dual. The base pair
  is $t=(1,4,4)$.
* **The trivial symmetries are exhausted.** Up to permutation, the orbit of a
  point under $S_3$, reciprocation and the torsion translations is
  $\{\pm P+T\}$: 12 points, i.e. $t$ and its dual. Any other pair on the same
  curve differs by a point of infinite order. Among the 1,753 primitive pairs
  with $S\le600$, 423 are dual pairs and the other 1,330 differ by points of
  infinite order. None of those 1,330 differs by torsion.

````

### 95. Proposition 2 (no linear families)

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `theory/diophantine/variety.md` |
| verifying script (existing) | theory/diophantine/families.py |
| audit evidence | `review/audit/diophantine/` |
| audit verdict | MINOR |
| in paper? | REMARK ONLY |
| note | Exclude families whose entries are all proportional. |

*DI.4, `theory/diophantine/variety.md` lines 162-168:*

````
**Proposition 2.** Let $(t(u,v),t'(u,v))$ be a two-parameter family in which
every entry is a linear form, the triples are positive on an open cone, and
$S$ and $R$ agree identically. Then $t'$ is a permutation of $t$. A family
affine in one parameter (a line not through the origin) is likewise trivial.
In particular every non-scaling polynomial family has degree $\ge2$ in its
parameter.

````

### 96. Theorem 3 (arbitrarily large fibres)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Proposition 1 |
| external inputs | Mazur's torsion theorem; BGN 'egg' (p. 119) |
| source file | `theory/diophantine/variety.md` |
| verifying script (existing) | theory/diophantine/cubic_group.py |
| audit evidence | `review/audit/diophantine/` |
| audit verdict | MINOR |
| in paper? | YES, REVISED |
| note | Fix 'distinct choices give distinct classes' / 'multiplied by any m': the theorem holds because L is unbounded. |

*DI.5, `theory/diophantine/variety.md` lines 220-223:*

````
**Theorem 3 (arbitrarily large fibres).** For every $k$ there are
infinitely many primitive degeneracy classes of size at least $k$, i.e. $k$
pairwise distinct hyperbolic triples with a common $S$ and a common $R$.

````

### 97. Rank certification of fibre curves

| field | value |
|---|---|
| status | COMPUTATION |
| dependencies | — |
| external inputs | PARI/GP 2.17.2 ellrank (unconditional with rational 2-torsion) |
| source file | `theory/diophantine/RECOMMENDATION.md`, `theory/diophantine/variety.md` |
| verifying script (existing) | theory/diophantine/ranks.py |
| audit evidence | `review/audit/diophantine/` |
| audit verdict | NONE |
| in paper? | YES |
| note | Ranks 2,2,3,3 and C_{155/12} rank 2 PROVEN (r1=r2) and confirmed by an independent 2-isogeny descent. |

*DI.6, `theory/diophantine/variety.md` lines 233-237:*

````
$3P=(162833463,287876366,723926268)$ is already large. Fibres from a single
generator are astronomically far out, and the enumeration finds far smaller
ones: the first sizes 3, 4, 5, 6 occur at $S=136,408,1849,4600$. The curves
carrying them have ranks 2, 2, 3, 3, proven with $r_1=r_2$, torsion
$\mathbf Z/6$ ([data/ranks.txt](data/ranks.txt)).
````

*DI.11, `theory/diophantine/RECOMMENDATION.md` lines 54-69:*

````
**First fibres of each size**, i.e. $k$ pairwise non-isometric pillows
sharing $a_0$ and $a_1$:

| size | $S$ | example |
|---:|---:|---|
| 3 | 136 | (15,55,66), (16,40,80), (17,34,85) |
| 4 | 408 | the $S=136$ curve $\lambda=68/5$ plus one more point |
| 5 | 1849 | (168,820,861), (172,645,1032), (185,480,1184), (215,344,1290), (253,276,1320) |
| 6 | 4600 | (750,1750,2100), (756,1674,2170), (800,1400,2400), (805,1380,2415), (882,1170,2548), (920,1104,2576) |

No fibre of size 7 occurs up to 4800. The curves carrying the first fibres
of sizes 3, 4, 5, 6 have Mordell–Weil rank 2, 2, 3, 3, and $C_{155/12}$ has
rank 2. All are **PROVEN**, with the PARI lower and upper bounds equal; the
exact calls and full outputs are in [data/ranks.txt](data/ranks.txt). The
claim that every primitive size-5 class up to 4800 lies on a curve of rank
3 or 4 was not certified by that script and is not proposed.
````

### 98. Isolation of the base pair (rank C_{27/2} = 0)

| field | value |
|---|---|
| status | PROVED GIVEN CITED INPUT |
| dependencies | Proposition 1, thmB |
| external inputs | PARI/GP 2.17.2 ellrank/elltors |
| source file | `theory/diophantine/variety.md` |
| verifying script (existing) | theory/diophantine/ranks.py |
| audit evidence | `review/audit/diophantine/` |
| audit verdict | NONE |
| in paper? | YES |
| note | P5: rank 0 unconditional (ellrank without GRH; exact 2-isogeny descent; analytic rank); 12 torsion points; pinned script agrees. Isosceles points are all of order 6 - provable, may replace 'as far as tested'. |

*DI.7, `theory/diophantine/variety.md` lines 239-252:*

````
**What does *not* adapt: the base pair is isolated.** $C_{27/2}$ has rank 0
**unconditionally**. PARI/GP 2.17.2 `ellrank` on the integral model
$[0,393,0,3456,0]$ returns $[0,0,0,[\,]]$, and the manual states that the
upper bound $r_2=C-T-s$ is computed unconditionally from the 2-Selmer group.
`elltors` gives torsion of order 12, $\mathbf Z/2\times\mathbf Z/6$.
`ranks.py` lists the 12 points on the plane cubic exactly (the six base
points and their translates by the order-6 point $(1,4,4)$) and asserts that
the only positive ones are the permutations of $(1,4,4)$ and $(1,1,4)$. Hence, for every
$k$, the class of $\{(2k,8k,8k),(3k,3k,12k)\}$ has exactly two members: no
third pillow ever joins the minimal degeneracy. Every isosceles
triple tested is torsion: all 1,482 triples $(u,v,v)$ with $u\ne v\le39$,
by exact order computation. So the isosceles
family, including the base pair, is (as far as tested) a torsion phenomenon, and the unbounded
fibres come only from curves of positive rank.
````

### 99. Hyperbolicity of copies kD, k>=4

| field | value |
|---|---|
| status | PROVED |
| dependencies | — |
| external inputs | — |
| source file | `theory/diophantine/variety.md` |
| verifying script (existing) | — |
| audit evidence | `review/audit/diophantine/` |
| audit verdict | MINOR |
| in paper? | YES |
| note | R<=3 holds for every positive triple. |

*DI.8, `theory/diophantine/variety.md` lines 261-269:*

````
Notation: $\mathcal N(X)$ is the cumulative count of degenerate **pairs**
with $S\le X$, the paper's convention. $\mathcal N_{\rm cl}(X)$ is the count
of classes. For a primitive pair $D$ with sum $S_D$, its copies $kD$ are
hyperbolic for all $k\ge4$. Indeed, if $D$ is the reduced dual pair of a
primitive $t$, then $R_D=G/e_3(t)\le e_2(t)/e_3(t)\le3$, because the gcd $G$
divides $e_2(t)$. So $R_{kD}\le 3/k<1$, and every entry of $kD$ is
$\ge k\ge2$. Distinct $(k,D)$ give distinct pairs, so

$$\mathcal N(X)\ \ge\ \sum_{D}\#\{k\ge4:\ kS_D\le X\}.\tag{$*$}$$
````

### 100. Theorem 4 (c_iso X log X)

| field | value |
|---|---|
| status | PROVED |
| dependencies | DI.3, DI.8 |
| external inputs | — |
| source file | `theory/diophantine/variety.md` |
| verifying script (existing) | theory/diophantine/families.py |
| audit evidence | `review/audit/diophantine/` |
| audit verdict | NONE |
| in paper? | YES |
| note | — |

*DI.9, `theory/diophantine/variety.md` lines 271-278:*

````
**Theorem 4 (isosceles family; explicit constant).** For coprime $1\le u<v$,
$$D_{u,v}=\{(2u+v)(u,v,v),\ (u+2v)(v,u,u)\}/g,\qquad g=\gcd(2u+v,u+2v)\in\{1,3\},$$
is a primitive degeneracy with $S=(2u+v)(u+2v)/g$ and $R=g/(uv)$; the base
pair is $D_{1,4}$. The number of these with $S\le y$ is
$c_{\rm iso}\,y+O(\sqrt y\log y)$, where $c_{\rm iso}=\dfrac{3\log2}{2\pi^2}=0.10535\ldots$.
Hence
$$\mathcal N(X)\ \ge\ \mathcal N_{\rm cl}(X)\ \ge\ \big(c_{\rm iso}+o(1)\big)\,X\log X .$$

````

### 101. Theorem 5 (X (log X)^2)

| field | value |
|---|---|
| status | PROVED |
| dependencies | DI.3, DI.8 |
| external inputs | — |
| source file | `theory/diophantine/variety.md` |
| verifying script (existing) | theory/diophantine/families.py |
| audit evidence | `review/audit/diophantine/` |
| audit verdict | NONE |
| in paper? | YES |
| note | Constant 3/(128 pi^4) re-derived exactly. |

*DI.10, `theory/diophantine/variety.md` lines 300-302:*

````
**Theorem 5 (the conic bundle; one more logarithm).**
$$\mathcal N(X)\ \ge\ \Big(\frac{3}{128\pi^4}+o(1)\Big)\,X(\log X)^2 .$$

````

### 102. First fibres of each size (S=136, 408, 1849, 4600)

| field | value |
|---|---|
| status | COMPUTATION |
| dependencies | — |
| external inputs | — |
| source file | `theory/diophantine/RECOMMENDATION.md` |
| verifying script (existing) | theory/diophantine/enumerate_fast.py |
| audit evidence | `review/audit/diophantine/`, `review/audit/consistency/` |
| audit verdict | SERIOUS |
| in paper? | YES, REVISED |
| note | Reproduced exactly (S<=4800). 'share a_0 and a_1' uses Uçar's indexing; in the paper's t^l indexing write 'share c_1, c_2 (R and S_1)' - otherwise false. |

*DI.11, `theory/diophantine/RECOMMENDATION.md` lines 54-69:*

````
**First fibres of each size**, i.e. $k$ pairwise non-isometric pillows
sharing $a_0$ and $a_1$:

| size | $S$ | example |
|---:|---:|---|
| 3 | 136 | (15,55,66), (16,40,80), (17,34,85) |
| 4 | 408 | the $S=136$ curve $\lambda=68/5$ plus one more point |
| 5 | 1849 | (168,820,861), (172,645,1032), (185,480,1184), (215,344,1290), (253,276,1320) |
| 6 | 4600 | (750,1750,2100), (756,1674,2170), (800,1400,2400), (805,1380,2415), (882,1170,2548), (920,1104,2576) |

No fibre of size 7 occurs up to 4800. The curves carrying the first fibres
of sizes 3, 4, 5, 6 have Mordell–Weil rank 2, 2, 3, 3, and $C_{155/12}$ has
rank 2. All are **PROVEN**, with the PARI lower and upper bounds equal; the
exact calls and full outputs are in [data/ranks.txt](data/ranks.txt). The
claim that every primitive size-5 class up to 4800 lies on a curve of rank
3 or 4 was not certified by that script and is not proposed.
````

