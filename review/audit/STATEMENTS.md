# G5 audit: statements under review

Every result below is copied verbatim, by line range, from its source file on branch
`s9a-audit` (`build_statements.py` asserts the anchors and that no proof text is included).
Hypotheses and notation are the `.0` items of each group. Proofs are deliberately omitted.
Cross-references inside the statements (e.g. "Theorem A", `lem:chamber`) point to other
items in this file.

External inputs the results rely on (texts fetched headlessly by `fetch_sources.sh` into
`review/audit/sources/`, not committed):

| input | used by | fetched text |
|---|---|---|
| Uçar, PhD thesis, arXiv:1711.03405: (4.25), (4.33), (4.35), Thm 4.11, Thm 4.20, Cor 4.21, Cor 4.23 | every heat-coefficient statement | `ucar_1711.03405.txt` |
| Dryden–Gordon–Greenwald–Webb, arXiv:0805.3148: Def 4.7, Thm 4.8, §5.6, Thm 5.15, Prop 5.22 | locality, curvature, priority | `dggw_0805.3148.txt` |
| Dryden–Strohmaier, arXiv:math/0504571: trace formula eq. (1), Thm 1.1, Thm 3.2, Prop 3.3 | locality T3, divergence | `ds_math0504571.txt` |
| Thurston, ch. 13: 13.3.5, 13.3.6, Cor 13.3.7 | locality T2, curvature | `thurston_ch13.txt` |
| Ostrowski, Acta Math. 72 (1940), Théorème XXX | stability | `ostrowski_1940.txt` |
| Holtz–Tyaglov, arXiv:1005.2843 (Orlando's formula) | audibility, stability | `holtz_tyaglov_1005.2843.txt` |
| Marklof, arXiv:math/0407288 | locality (normalisation cross-check) | `marklof_math0407288.txt` |
| Schueth, arXiv:1812.06119 | cone coefficients l<=2 | `schueth_1812.06119.txt` |
| Kokotov, arXiv:0906.0717 | curvature (flat cones) | `kokotov_0906.0717.txt` |
| Linowitz–Voight arXiv:1408.2001; Doyle–Rossetti arXiv:1103.4372 | locality §3.5 | `lv_1408.2001.txt`, `dr_1103.4372.txt` |
| Bremner–Guy–Nowakowski, Math. Comp. 61 (1993); Schinzel, Serdica 22 (1996); PARI/GP manual (ellrank) | diophantine | `bgn_mcom1993.txt`, `schinzel_serdica1996.txt`, `pari_elliptic.html` |
| Müller–Feliu–Regensburger–Conradi–Shiu–Dickenstein, arXiv:1311.5493 | Theorem A prior art (P7) | `mueller_1311.5493.txt` |
| Donnelly 1976 | restated in DGGW §4 only | standing gap (not fetched) |

## Group: paper-core

### PC.0. Area and hyperbolicity (eq:area)

Source: `paper/main.tex` lines 94-99 (verbatim).

````
By the Gauss--Bonnet theorem the area is
\begin{equation}
    \operatorname{Area}(\mathcal{O}) = 2\pi \left( 1 - \Big( \tfrac{1}{p} + \tfrac{1}{q} + \tfrac{1}{r} \Big) \right),
    \label{eq:area}
\end{equation}
and hyperbolicity is the condition $\tfrac1p+\tfrac1q+\tfrac1r<1$.
````

### PC.1. Main theorems A, B, C and Corollary D (thmA, thmB, thmC, corD) with the definition of K(F)

Source: `paper/main.tex` lines 103-119 (verbatim).

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

### PC.2. Conventions (eq:a0conv)

Source: `paper/main.tex` lines 139-144 (verbatim).

````
We use the orbifold heat-trace expansion of Dryden--Gordon--Greenwald--Webb~\cite{dggw2008}. With the smooth principal-stratum series carrying the $(4\pi t)^{-1}$ prefactor and each cone point $C$ of order $m$ contributing $b_\ell(C)$ at order $t^{\ell}$, the degree-zero (constant) coefficient of $\mathcal{O}(p,q,r)$ is
\begin{equation}
    a_0 \;=\; \frac{\chi(\mathcal{O})}{6} \;+\; \sum_{i}\frac{m_i^2-1}{12\,m_i},
    \label{eq:a0conv}
\end{equation}
where $\chi(\mathcal{O}) = 2 - \sum_i(1-\tfrac1{m_i}) = R-1$ is the orbifold Euler characteristic, $R:=\sum_i \tfrac1{m_i}$, and the normalization is the $1/(4\pi)$ of~\cite{dggw2008} (no separate Euler factor). As a fixed reference point, the spherical triple $(2,3,5)$ gives cone sum $\tfrac18+\tfrac29+\tfrac25=\tfrac{269}{360}$ and, with the smooth term $\chi/6=\tfrac1{180}$, total $a_0=\tfrac{271}{360}$.
````

### PC.3. Heat expansion structure (sec:heatexp)

Source: `paper/main.tex` lines 171-175 (verbatim).

````
On a closed hyperbolic $2$-orbifold $\mathcal{O}$ the heat trace has the small-time asymptotic expansion of Minakshisundaram--Pleijel type~\cite{mckeansinger1967}, refined to the orbifold stratification by Donnelly and Dryden--Gordon--Greenwald--Webb~\cite{donnelly1976, dggw2008}. It splits along the strata:
\[
    \operatorname{tr}e^{-t\Delta}\ \sim\ \underbrace{(4\pi t)^{-1}\sum_{\ell\ge0} a^{\mathrm{sm}}_\ell\, t^{\ell}}_{\text{principal (smooth) stratum}}\ +\ \sum_{\text{cone points }C}\ \underbrace{\sum_{\ell\ge0} b_\ell(C)\, t^{\ell}}_{\text{singular stratum}},
\]
where each $a^{\mathrm{sm}}_\ell$ is the integral over $\mathcal{O}$ of a universal polynomial in the curvature and its covariant derivatives, and each cone point $C$ (a zero-dimensional singular stratum) contributes a series $b_\ell(C)$ carrying no $(4\pi t)^{-1}$ prefactor. Because the cones have constant curvature the expansion contains only integer powers of $t$: the half-integer and logarithmic terms that arise for genuinely curved conical singularities~\cite{schueth2025, suleymanova2017, nrs2024} are absent, as a constant-curvature orbifold cone has no curvature blow-up at the tip. The three invariants of this paper are the coefficients of $t^{-1}$, $t^{0}$, and $t^{1}$. At constant curvature each smooth term $a^{\mathrm{sm}}_\ell$ is a fixed multiple of $\operatorname{Area}(\mathcal{O})$, hence a function of $R$ alone; the geometric content beyond the area therefore lives entirely in the cone-point sums $\sum_i b_\ell(C_i)$, which we compute in the next two subsections.
````

### PC.4. lem:cot

Source: `paper/main.tex` lines 180-182 (verbatim).

````
\begin{lemma}[Cotangent sum]\label{lem:cot}
For every integer $m\ge2$, $\ \displaystyle\sum_{j=1}^{m-1}\cot^2\!\Big(\tfrac{j\pi}{m}\Big)=\tfrac{(m-1)(m-2)}{3}$.
\end{lemma}
````

### PC.5. prop:csc

Source: `paper/main.tex` lines 188-190 (verbatim).

````
\begin{proposition}[Cosecant sum]\label{prop:csc}
For every integer $m\ge2$, $\ \displaystyle\sum_{j=1}^{m-1}\csc^2\!\Big(\tfrac{j\pi}{m}\Big)=\tfrac{m^2-1}{3}$.
\end{proposition}
````

### PC.6. Cone convention and def:cone, cor:conevals

Source: `paper/main.tex` lines 196-205 (verbatim).

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

### PC.7. Inversion eq:s1inv and rem:bugfix

Source: `paper/main.tex` lines 216-231 (verbatim).

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

### PC.8. Third coefficient eq:b1, eq:a2red

Source: `paper/main.tex` lines 236-246 (verbatim).

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

### PC.9. prop:cs

Source: `paper/main.tex` lines 248-250 (verbatim).

````
\begin{proposition}[Cauchy--Schwarz bound]\label{prop:cs}
For every hyperbolic triad, $S_1 R=(p+q+r)\big(\tfrac1p+\tfrac1q+\tfrac1r\big)\ge 9$, with equality iff $p=q=r$.
\end{proposition}
````

### PC.9b. prop:recovery

Source: `paper/main.tex` lines 256-258 (verbatim).

````
\begin{proposition}[Recovery from three symmetric functions]\label{prop:recovery}
The values $R=\sum_i m_i^{-1}$, $S_1=\sum_i m_i$, and $P_3=\sum_i m_i^{3}$ determine the multiset $\{p,q,r\}$; equivalently, the map sending a hyperbolic triangular pillow to its first three heat coefficients is injective.
\end{proposition}
````

### PC.10. Jacobian claim after prop:recovery

Source: `paper/main.tex` lines 269-269 (verbatim).

````
This Newton--Vieta inversion is a standard symmetric-function recovery. Its infinitesimal counterpart is immediate: the map $F=(S_1,R,P_3)$ has Jacobian determinant $\det DF=-3\,(p-q)(p-r)(q-r)(p+q)(p+r)(q+r)/(p^2q^2r^2)$, nonzero off the diagonals $p=q$, $p=r$, $q=r$, so the three invariants form a local coordinate system on each open ordered chamber $\{p<q<r\}$. This plays no role in the two-coefficient threshold of Section~\ref{sec:threshold}, which concerns the discrete map $\sigma=(S_1,R)$.
````

### PC.11. Two-coefficient map, strata, lem:chamber

Source: `paper/main.tex` lines 279-290 (verbatim).

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

### PC.12. R^+ formula, lem:bound

Source: `paper/main.tex` lines 295-303 (verbatim).

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

### PC.13. prop:min

Source: `paper/main.tex` lines 310-312 (verbatim).

````
\begin{proposition}[Balanced configurations minimize $R$ and $a_0$]\label{prop:min}
At a fixed cone-order sum $S_1$, the reciprocal sum $R=\sum_i m_i^{-1}$ is minimized by the most balanced admissible triple and increases as the orders spread apart; equivalently $R$ is Schur-convex in $(m_1,m_2,m_3)$. Since $a_0=\tfrac{S_1+R-2}{12}$ by~\eqref{eq:a0conv}, the constant heat coefficient at fixed $S_1$ is likewise smallest for the balanced pillow and grows with the anisotropy of the cone orders. This is a convexity statement about the two leading invariants.
\end{proposition}
````

### PC.14. S_1>=10 claim and thm:separation

Source: `paper/main.tex` lines 319-323 (verbatim).

````
Since $\sigma$ records $S_1$ first, a collision forces equal sum, and by Lemma~\ref{lem:chamber} it must join \emph{different} least-order strata. It therefore suffices to separate the strata of each fixed sum. No hyperbolic triad has $S_1\le9$: for $2\le p\le q\le r$ with $R<1$, if $p=2$ then $\tfrac1q+\tfrac1r<\tfrac12$ forces $q+r\ge9$ and $S_1\ge11$; if $p=3$ then $q+r\ge7$ and $S_1\ge10$; and $p\ge4$ gives $S_1\ge12$. Thus $S_1\ge10$, with equality only for $\mathcal{O}(3,3,4)$. For $S\le17$ the least order obeys $p\le\lfloor S/3\rfloor\le5$, so only the strata $p\in\{2,3,4,5\}$ arise.

\begin{theorem}[Interval separation]\label{thm:separation}
For every $S\le17$ the reciprocal-sum intervals $[R^{-}_{S,p},R^{+}_{S,p}]$ of the distinct least-order strata are pairwise disjoint; consequently $\sigma$ is injective on hyperbolic triads of sum $S\le17$. Moreover the intervals of least orders $2$ and $3$ first meet at $S=18$, at the common value $R=\tfrac34$ realized by the balanced triad $\mathcal{O}(2,8,8)$ and the spread triad $\mathcal{O}(3,3,12)$; at $S=18$ every other adjacent pair of strata is still separated.
\end{theorem}
````

### PC.15. Numerical endpoint claims in the proof of thm:separation (claims only)

Source: `paper/main.tex` lines 333-345 (verbatim).

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

### PC.16. Remark* on a_0

Source: `paper/main.tex` lines 394-396 (verbatim).

````
\begin{remark*}
Proposition~\ref{prop:min} places the balanced end of each stratum: at fixed cone-order sum the constant coefficient $a_0=\tfrac{S_1+R-2}{12}$ is minimized by the balanced pillow $p=q=r$ where one exists ($3\mid S_1$, $S_1/3\ge4$) and is non-increasing under balancing otherwise. This is a fixed-sum statement ,  across \emph{all} pillows $a_0$ is smallest for the non-balanced $\mathcal{O}(3,3,4)$, with $a_0=\tfrac{107}{144}$, consistent with the sharp bound $S_1R\ge9$ (Proposition~\ref{prop:cs}) ,  and is a convexity fact about the two leading invariants.
\end{remark*}
````

### PC.17. Degeneracy definition, N(S), prop:scaling

Source: `paper/main.tex` lines 402-421 (verbatim).

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

### PC.17b. thm:density-lower

Source: `paper/main.tex` lines 426-431 (verbatim).

````
\begin{theorem}[Infinitude and a linear lower bound]\label{thm:density-lower}
There are infinitely many two-coefficient spectral degeneracies. More precisely, for every $S\ge18$,
\[
    \mathcal N(S)\ \ge\ \Big\lfloor \frac S{18}\Big\rfloor.
\]
\end{theorem}
````

### PC.18. Primitive pair at S=36 (claim)

Source: `paper/main.tex` lines 436-436 (verbatim).

````
Theorem~\ref{thm:density-lower} is unconditional and elementary, but it undercounts the true growth substantially: it accounts only for scaled copies of the single base pair, whereas exact enumeration shows that new (\emph{primitive}, i.e.\ not obtained by scaling a smaller degeneracy) collisions appear at almost every sum beyond $18$. For instance at $S=36=2\cdot18$ there are two degeneracy classes: the scaled copy $\{\mathcal O(4,16,16),\mathcal O(6,6,24)\}$ predicted by Proposition~\ref{prop:scaling}, and a second, primitive one, $\{\mathcal O(6,15,15),\mathcal O(8,8,20)\}$, at reciprocal sum $R=3/10$, not obtainable by scaling the base pair.
````

### PC.19. Density table and fitted exponent (claims), conj:density, later claims

Source: `paper/main.tex` lines 440-481 (verbatim).

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

### PC.20. rem:ncone

Source: `paper/main.tex` lines 493-495 (verbatim).

````
\begin{remark}[Larger cone counts]\label{rem:ncone}
For an $n$-cone pillow $\mathcal{O}(m_1,\dots,m_n)$ ,  a sphere with $n$ cone points, hyperbolic when $\sum_i(1-\tfrac1{m_i})>2$ ,  the first $n$ leading heat coefficients again supply $n$ symmetric functions of the orders, and when these are independent they recover the multiset, so the upper bound $K\le n$ extends the $n=3$ case of Theorem~\ref{thmC}. The matching lower bound $K\ge n$ for $n\ge4$ would require two $n$-cone pillows agreeing in $n-1$ prescribed symmetric functions ,  an $(n-1)$-fold simultaneous Egyptian-fraction and power-sum system ,  for which we have neither a construction nor a non-existence proof; we leave it open.
\end{remark}
````

### PC.21. Table tab:enum claim

Source: `paper/main.tex` lines 504-504 (verbatim).

````
As an independent cross-check of Theorem~\ref{thm:separation}, Table~\ref{tab:enum} lists \emph{every} hyperbolic triad with $10\le S_1\le18$ together with its reciprocal sum $R$ as an exact rational. The interval argument of Section~\ref{sec:threshold} predicts, and the table confirms, that $R$ is distinct across all triads of a common sum for $S_1\le17$, and that the only within-sum coincidence at $S_1\le18$ is the boldface pair $\{\mathcal{O}(2,8,8),\mathcal{O}(3,3,12)\}$ at $S_1=18$. The table plays no role in the proof; it is exhaustive supporting evidence.
````


## Group: definitions

### DF.1. def:signature, def:heatcoef

Source: `theory/definitions.tex` lines 17-41 (verbatim).

````
\begin{definition}[Signature]\label{def:signature}
Let $\Orb$ be a closed, orientable $2$-orbifold whose only singular points are cone points.
Let $g$ be the genus of the underlying surface and $m_1,\dots,m_n\ge2$ the orders of the cone
points, listed with multiplicity. The \emph{signature} of $\Orb$ is
\[
  \sigma(\Orb)=(g;\,m_1,\dots,m_n),
\]
in which the $m_i$ form a multiset: the order of listing carries no information. Write
$\chi(\Orb)=2-2g-\sum_{i=1}^n(1-\tfrac1{m_i})$. The orbifold carries a hyperbolic metric exactly
when $\chi(\Orb)<0$. A \emph{hyperbolic triangular pillow} is the case $(g;n)=(0;3)$; it is
denoted $\Orb(p,q,r)$ with $p\le q\le r$, and $\chi(\Orb(p,q,r))=R-1$ for
$R=\tfrac1p+\tfrac1q+\tfrac1r$. Two orbifolds are \emph{isometric} if there is a Riemannian
isometry of the hyperbolic metrics; isometric orbifolds have equal signatures.
\end{definition}

\begin{definition}[Leading heat coefficients]\label{def:heatcoef}
For a closed orientable hyperbolic $2$-orbifold $\Orb$ with Laplacian $\Delta$ the heat trace
has an asymptotic expansion in integer powers of $t$ \cite{donnelly1976, dggw2008},
\[
  \operatorname{tr}e^{-t\Delta}\;\sim\;\sum_{j\ge1}c_j(\Orb)\,t^{\,j-2}\qquad(t\downarrow0).
\]
The coefficient $c_j(\Orb)$ is the \emph{$j$-th leading heat coefficient}. In particular
$c_1(\Orb)=\operatorname{Area}(\Orb)/4\pi=-\chi(\Orb)/2$, which for a triangular pillow equals
$\tfrac12(1-R)$. For $k\ge1$ put $H_k(\Orb)=(c_1(\Orb),\dots,c_k(\Orb))$.
\end{definition}
````

### DF.2. def:K and eq:Kcompare

Source: `theory/definitions.tex` lines 49-65 (verbatim).

````
\begin{definition}[$\Kiso$ and $\Kmult$]\label{def:K}
For $\Orb\in\Pill$ let
\begin{align*}
  \Kiso(\Orb;\Pill)&=\min\{k\ge1:\ \text{for every }\Orb'\in\Pill,\ H_k(\Orb')=H_k(\Orb)\Rightarrow\Orb'\ \text{is isometric to }\Orb\},\\
  \Kmult(\Orb;\Pill)&=\min\{k\ge1:\ \text{for every }\Orb'\in\Pill,\ H_k(\Orb')=H_k(\Orb)\Rightarrow\sigma(\Orb')=\sigma(\Orb)\},
\end{align*}
with $\min\emptyset=\infty$. Thus $\Kiso$ is the least number of leading heat coefficients that
determine $\Orb$ up to isometry among the members of $\Pill$, and $\Kmult$ is the least number that
determine its signature, i.e.\ its genus and its cone-order multiset.
\end{definition}

Both sets are upward closed in $k$, so the minima are well defined. Because isometric orbifolds
have equal signatures, the condition defining $\Kiso$ implies the one defining $\Kmult$, and
therefore
\begin{equation}\label{eq:Kcompare}
  \Kmult(\Orb;\Pill)\ \le\ \Kiso(\Orb;\Pill).
\end{equation}
````

### DF.3. prop:rigidity (statement)

Source: `theory/definitions.tex` lines 69-74 (verbatim).

````
\begin{proposition}[Rigidity of triangular pillows]\label{prop:rigidity}
If $\Orb,\Orb'\in\Pill_3$ have the same signature then they are isometric. Consequently
\[
  \Kiso(\Orb;\Pill_3)=\Kmult(\Orb;\Pill_3)\qquad\text{for every }\Orb\in\Pill_3 .
\]
\end{proposition}
````

### DF.4. eq:moduli

Source: `theory/definitions.tex` lines 95-105 (verbatim).

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

### DF.5. thm:locality, prop:Kinf (statements)

Source: `theory/definitions.tex` lines 110-128 (verbatim).

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

### DF.6. thm:Crestated (statement)

Source: `theory/definitions.tex` lines 142-150 (verbatim).

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

### DF.7. rem:nconerestated

Source: `theory/definitions.tex` lines 159-177 (verbatim).

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


## Group: audibility

### AU.0. Heat input and notation

Source: `theory/audibility/proof.md` lines 26-50 (verbatim).

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

### AU.1. Theorems A, B, C

Source: `theory/audibility/proof.md` lines 51-84 (verbatim).

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

### AU.2. Lemma 1 (parity)

Source: `theory/audibility/proof.md` lines 88-91 (verbatim).

````
**Lemma 1 (parity).** In $\mathbb Q[x_1,\dots,x_N]$ let $s_j=\sum x_i^j$ and let $e_j$ be the
elementary symmetric functions. For odd $j$, $e_j$ lies in the ideal generated by
$s_1,s_3,\dots,s_j$. Conversely, $s_j$ lies in the ideal generated by $e_1,e_3,\dots,e_j$.

````

### AU.3. Jacobian claim (Remark 2) and padding claim (Remark 3)

Source: `theory/audibility/proof.md` lines 123-136 (verbatim).

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

### AU.4. Integer witnesses table (claims)

Source: `theory/audibility/proof.md` lines 217-225 (verbatim).

````
In the table, $\Phi(z):=p(z)p'(-z)-p'(z)p(-z)$ with $p=\prod(z+m_i)$ and $p'=\prod(z+m'_j)$.
It satisfies $\Phi=(-1)^{n+1}\bigl(Q(z)-Q(-z)\bigr)$.

| $n$ | witness sharing $\mathcal I_{n-1}$ | separated by | $\Phi(z)$ |
|---|---|---|---|
| 3 | $\{2,8,8\}$, $\{3,3,12\}$ ($R=3/4$, $S_1=18$) | $P_3$: 1032 vs 1782 | $500\,z^3$ |
| 4 | $\{3,10,15,30\}$, $\{4,5,21,28\}$ ($R=8/15$, $S_1=58$, $P_3=31402$) | $P_5$: 25159618 vs 21298618 | $1544400\,z^3$ |
| 5 | none with orders $\le60$ (7,028,847 multisets) or $\le120$ (216,071,394) | | |

````


## Group: signatures

### SG.0. Setting and heat input (H)

Source: `theory/signatures/proof.md` lines 41-75 (verbatim).

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

### SG.1. Lemma 1 (cone polynomials)

Source: `theory/signatures/proof.md` lines 78-81 (verbatim).

````
**Lemma 1 (cone polynomials, every $l$).** $p_l(k):=k\,b_l(k)/K^l$ is an even polynomial of
degree $2l+2$ with $p_l(1)=0$. Its leading coefficient is
$|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$.

````

### SG.2. Lemma 2 (triangular basis)

Source: `theory/signatures/proof.md` lines 95-99 (verbatim).

````
**Lemma 2 (triangular basis).** $\phi_l(x):=p_l(x)/x=\sum_{k=1}^{l+1}a_{l,k}\,\psi_k(x)$ with
$a_{l,l+1}\ne0$. Hence, for multisets $m,m'$ and $L\ge1$:
$$C_l(m)=C_l(m')\ (0\le l\le L-2)\iff\Psi_k(m)=\Psi_k(m')\ (1\le k\le L-1).$$
The direction "$\Leftarrow$" does not use $a_{l,l+1}\neq0$.

````

### SG.3. Lemma 3 (padding)

Source: `theory/signatures/proof.md` lines 105-106 (verbatim).

````
**Lemma 3 (padding).** Adjoining points of order 1 changes neither the area nor any $C_l$.

````

### SG.4. Lemma 4 (reduction)

Source: `theory/signatures/proof.md` lines 110-132 (verbatim).

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

### SG.5. Theorem S

Source: `theory/signatures/proof.md` lines 152-157 (verbatim).

````
**Theorem S.** Let $\mathcal O,\mathcal O'$ be closed orientable hyperbolic 2-orbifolds with
$\sigma(\mathcal O)\neq\sigma(\mathcal O')$ and $H_L(\mathcal O)=H_L(\mathcal O')$. Let $U,V$ be
as in Lemma 4, and let $U^*,V^*$ be obtained by cancelling the elements they have in common.
Then
$$|U^*|+|V^*|\ \ge\ 2L+2 .$$

````

### SG.6. Corollary S1

Source: `theory/signatures/proof.md` lines 179-182 (verbatim).

````
**Corollary S1 (pairwise form).** If $H_L(\mathcal O)=H_L(\mathcal O')$ with
$$L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),$$
then $\sigma(\mathcal O)=\sigma(\mathcal O')$.

````

### SG.7. Corollary S2

Source: `theory/signatures/proof.md` lines 185-191 (verbatim).

````
**Corollary S2 (area form: genus and cone orders from finitely many coefficients).** Let
$\mathcal O$ have area $A$. Any closed orientable hyperbolic 2-orbifold $\mathcal O'$ with
$H_{\lfloor A/\pi\rfloor+4}(\mathcal O')=H_{\lfloor A/\pi\rfloor+4}(\mathcal O)$ has the same
genus and the same cone-order multiset. In the notation of `def:K`, with
$\mathrm{Sig}$ the class of all closed orientable hyperbolic 2-orbifolds,
$$K_{\rm mult}(\mathcal O;\mathrm{Sig})\ \le\ \Bigl\lfloor\frac{\mathrm{Area}(\mathcal O)}{\pi}\Bigr\rfloor+4 .$$

````

### SG.8. Theorem T1

Source: `theory/signatures/proof.md` lines 202-211 (verbatim).

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

### SG.9. Proposition P (Prouhet)

Source: `theory/signatures/proof.md` lines 235-241 (verbatim).

````
**Proposition P (Prouhet; Thue–Morse).** Let $t(i)$ be the parity of the binary digit sum of
$i$. Let $D\ge1$, and let $T_0,T_1$ split $\{0,\dots,2^D-1\}$ according to $t(i)$. Then:

1. $\sum_{T_0}f=\sum_{T_1}f$ for every polynomial $f$ of degree $<D$.
2. For every $c>0$ and $h>0$,
   $$\sum_{i<2^D}\frac{(-1)^{t(i)}}{hi+c}>0 .$$

````

### SG.10. Theorem N

Source: `theory/signatures/proof.md` lines 247-263 (verbatim).

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

### SG.11. Construction claims for Theorem N (computed ranges)

Source: `theory/signatures/proof.md` lines 305-313 (verbatim).

````
The constructions are built and checked with the actual cone coefficients $b_l$:

- (a) for $L=2,\dots,6$ (`genus.py` (A)). Each pair shares *exactly* $L$ coefficients; the
  $L=6$ pair has 1023 and 1025 cone points.
- (b) for $k=2,3$ (`cone_count.py` (d)): 9 vs 10 and 103 vs 104 cone points, sharing exactly
  2 and 3 coefficients.

For $k\ge4$ the greedy denominators grow doubly exponentially, which makes exact verification
impractical. The proof above covers every $k$.
````

### SG.12. Corollary N1

Source: `theory/signatures/proof.md` lines 315-319 (verbatim).

````
**Corollary N1 (growth).** Let $f(A)=\max\{K_{\rm mult}(\mathcal O;\mathrm{Sig}):
\mathrm{Area}(\mathcal O)\le A\}$. For $A\ge6\pi$,
$$\Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\
\Bigl\lfloor\frac A\pi\Bigr\rfloor+4 .$$

````

### SG.13. Manuscript-facing LaTeX versions (statements.tex)

Source: `theory/signatures/statements.tex` lines 11-117 (verbatim).

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


## Group: locality

### LO.0. Setting

Source: `theory/locality/proof.md` lines 9-17 (verbatim).

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

### LO.1. Theorem 1 (signature locality)

Source: `theory/locality/proof.md` lines 47-69 (verbatim).

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

### LO.2. Thurston Cor. 13.3.7 as quoted

Source: `theory/locality/proof.md` lines 154-157 (verbatim).

````
**Source statement** [Th, Corollary 13.3.7, electronic ed. p. 318, original p. 13.27],
verbatim: *"The Teichmüller space T(O) of an orbifold O with χ(O) < 0 is homeomorphic to
Euclidean space of dimension −3χ(X_O) + 2k + l, where k is the number of elliptic points and
l is the number of corner reflectors."* The proof (p. 318) cuts $\mathcal O$ along disjoint
````

### LO.3. Proposition 2.1

Source: `theory/locality/proof.md` lines 167-171 (verbatim).

````
**Proposition 2.1.** For a closed orientable hyperbolic 2-orbifold of signature
$(g;m_1,\dots,m_n)$,
$$\dim_{\mathbb R}T(\mathcal O)=6g-6+2n .$$
Among hyperbolic signatures, it vanishes exactly for $(g;n)=(0;3)$, the triangle orbifolds,
and is $\ge2$ otherwise.
````

### LO.4. Proposition 2.2

Source: `theory/locality/proof.md` lines 184-185 (verbatim).

````
**Proposition 2.2.** If $6g-6+2n>0$, the closed orientable hyperbolic orbifolds of
signature $\sigma=(g;m_1,\dots,m_n)$ fall into uncountably many isometry classes.
````

### LO.5. Corollary 2.3

Source: `theory/locality/proof.md` lines 212-219 (verbatim).

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

### LO.6. Theorem 3.1

Source: `theory/locality/proof.md` lines 254-265 (verbatim).

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

### LO.7. Lemma 3.2 (statement only)

Source: `theory/locality/proof.md` lines 289-293 (verbatim).

````
**Lemma 3.2 (admissibility of the heat function).** Fix $\chi\in C_c^\infty(\mathbb R)$, even,
$0\le\chi\le1$, $\chi=1$ on $[-1,1]$, $\operatorname{supp}\chi\subset[-2,2]$, and put $g_R(u)=g_t(u)\chi(u/R)$ and
$h_R(r)=\int g_R(u)e^{iru}du$. Then $h_R$ is even, entire and of exponential type $\le2R$
(Paley–Wiener), so [DS] (1) holds for $h_R$, with Fourier transform $g_R$. As
$R\to\infty$ each term converges to the corresponding term for $h_t$:
````

### LO.8. Lemma 3.3

Source: `theory/locality/proof.md` lines 321-324 (verbatim).

````
**Lemma 3.3 (counting).** Let $A=\operatorname{Area}(\mathcal O)$ and
$\delta=\operatorname{diam}(\mathcal O)$, and let $N(L)$ be the number of hyperbolic conjugacy
classes $[\gamma]$ with $\ell(\gamma)\le L$. Then
$$N(L)\le\frac{2\pi(\cosh(L+3\delta)-1)}{A}\le\frac{\pi}{A}e^{L+3\delta}.$$
````

### LO.9. Theorem 3.4

Source: `theory/locality/proof.md` lines 347-362 (verbatim).

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

### LO.10. Claim: the t^{-1/2} prefactor cannot be dropped

Source: `theory/locality/proof.md` lines 396-412 (verbatim).

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

### LO.11. Theorem 3.5

Source: `theory/locality/proof.md` lines 423-430 (verbatim).

````
**Theorem 3.5.** Let $\mathcal O_1,\mathcal O_2$ have the same signature.

- If $w_1\equiv w_2$, then $Z_1\equiv Z_2$, and the orbifolds are isospectral.
- Otherwise, let $L_*=\min\{L:w_1(L)\ne w_2(L)\}$. Then, as $t\downarrow0$,
$$Z_1(t)-Z_2(t)=\frac{w_1(L_*)-w_2(L_*)}{2\sinh(L_*/2)}\,\frac{e^{-t/4}e^{-L_*^2/4t}}{\sqrt{4\pi t}}\,\big(1+o(1)\big),$$
  so $Z_1-Z_2\ne0$ for small $t$ and $\log|Z_1-Z_2|=-L_*^2/4t-\tfrac12\log t+O(1)$.
- In particular, if $\ell_1\ne\ell_2$, then $L_*=\min(\ell_1,\ell_2)=\ell$, and the
  exponent $\ell^2/4$ of Theorem 3.4 is attained.
````


## Group: stability

### ST.0. Setting and the recovery map

Source: `theory/stability/proof.md` lines 45-75 (verbatim).

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

### ST.1. Proposition S1

Source: `theory/stability/proof.md` lines 78-88 (verbatim).

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

### ST.2. Front-end tables (claims)

Source: `theory/stability/proof.md` lines 100-131 (verbatim).

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

### ST.3. Lemma S2.1

Source: `theory/stability/proof.md` lines 142-146 (verbatim).

````
**Lemma S2.1 (the constant c_n of Theorem B, all n).** For every n ≥ 2,

  det M = (−1)^{n(n+1)/2} ∏_{i<j}(m_i + m_j) / e_n,

so c_n = (−1)^{n(n+1)/2}. This replaces "c_n ∈ ℚ^×, computed for n ≤ 8" in Theorem B.
````

### ST.4. Lemma S2.2

Source: `theory/stability/proof.md` lines 172-183 (verbatim).

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

### ST.5. Theorem S2

Source: `theory/stability/proof.md` lines 196-222 (verbatim).

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

### ST.6. Ostrowski input as quoted

Source: `theory/stability/proof.md` lines 264-273 (verbatim).

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

### ST.7. Lemma S3

Source: `theory/stability/proof.md` lines 275-287 (verbatim).

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

### ST.8. Theorem S3

Source: `theory/stability/proof.md` lines 301-321 (verbatim).

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

### ST.9. Proposition S3.2

Source: `theory/stability/proof.md` lines 328-347 (verbatim).

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

### ST.10. Remark S3.3

Source: `theory/stability/proof.md` lines 348-357 (verbatim).

````
**Remark S3.3 (realisable data at a triple order).** The exponent 1/k concerns arbitrary data
vectors, which is the right model for noisy measurements. For data that are heat
coefficients of a *real* multiset near (a,a,a), the exponent is 1/2. For real d with
|d_i| ≤ a,

  (P₃ − 3a²P₁)(a + d) − (P₃ − 3a²P₁)(a) = 3a Σd_i² + Σd_i³ ≥ 2a Σd_i²,

so max|d_i| ≤ (|ΔP₃ − 3a²ΔP₁|/(2a))^{1/2}. This was checked on 900 random real perturbations.
No general statement for realisable data at mixed clusters is claimed.

````

### ST.11. Theorem S4

Source: `theory/stability/proof.md` lines 360-366 (verbatim).

````
**Theorem S4 (explicit threshold).** Let m be integer orders. Define

  δ_thm(m) := min( 1/λ_μ,  1/(2κζ_nλ_μ),  min_a  Q̂_a 2^{k_a−1} / (3ⁿ (2μ)^{k_a} · 2κρ_nλ_μ) ).

If |H̃_ν − H_ν(m)| ≤ δ_thm(m) for ν = −1, …, n−2, then rounding the real parts of the roots
of q̃ returns m exactly.

````

### ST.12. Proposition S5 (statement of the two tests)

Source: `theory/stability/proof.md` lines 378-408 (verbatim).

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

### ST.13. Upper bound by construction; rounding convention

Source: `theory/stability/proof.md` lines 413-429 (verbatim).

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

### ST.14. Results table (printed values to re-certify)

Source: `theory/stability/proof.md` lines 430-446 (verbatim).

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


## Group: threshold

### TH.0. Notation and the overlap definition

Source: `theory/threshold/proof.md` lines 20-45 (verbatim).

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

### TH.1. Lemma 1

Source: `theory/threshold/proof.md` lines 48-50 (verbatim).

````
**Lemma 1 (one inequality).** For $S\ge3p+3$, the strata $p,p+1$ overlap at $S$ iff
$\operatorname{gap}_p(S)\le0$.

````

### TH.2. Lemma 2

Source: `theory/threshold/proof.md` lines 63-67 (verbatim).

````
**Lemma 2 (adjacent separation suffices; the chain in the proof of `thm:separation`).** If
$\operatorname{gap}_p(S)>0$ for every $p$ with both strata $p,p+1$ nonempty at $S$, then all
strata of sum $S$ have pairwise disjoint reciprocal-sum sets, and $\sigma$ is injective on
triads of sum $S$.

````

### TH.3. Theorem 1

Source: `theory/threshold/proof.md` lines 74-79 (verbatim).

````
**Theorem 1.** For every $p\ge2$ let
$$S^*(p)=\begin{cases}18,&p=2,\\ 19,&p=3,\\ 3p+8,&4\le p\le8,\\ 3p+7,&p\ge9.\end{cases}$$
For $S\ge3p+3$, the strata $p$ and $p+1$ overlap at $S$ iff $S\ge S^*(p)$. Equivalently,
$S^*(p)$ is the least $S\ge x^*(p)=\dfrac{3p(p+1)}{p-1}=3p+6+\dfrac6{p-1}$ with $S\equiv p$
(mod 2), except for $p\ge9$, where the odd-parity sum $3p+7$ comes first.

````

### TH.4. Corollary 2

Source: `theory/threshold/proof.md` lines 138-141 (verbatim).

````
**Corollary 2.** For every $S\le17$, the map $\sigma=(S_1,R)$ is injective on hyperbolic
triads of sum $S$. At $S=18$ there is exactly one collision,
$\{\mathcal O(2,8,8),\mathcal O(3,3,12)\}$.

````

### TH.5. First-overlap vs first-collision table (computed claims)

Source: `theory/threshold/proof.md` lines 165-187 (verbatim).

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

### TH.6. Proposition 3

Source: `theory/threshold/proof.md` lines 193-198 (verbatim).

````
**Proposition 3 (why the gap is positive except at $p=2,4$).**

1. The balanced triad of stratum $p$ and the spread triad of stratum $p+1$ have equal $R$
   (a tangency) iff $p\in\{2,4\}$, at $S=x^*(p)$.
2. For every $p\notin\{2,4\}$ the first adjacent collision occurs strictly after $S^*(p)$.

````


## Group: curvature

### CU.0. Conventions

Source: `theory/curvature/proof.md` lines 37-54 (verbatim).

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

### CU.1. Flat-cone input (Kokotov) as quoted

Source: `theory/curvature/proof.md` lines 57-76 (verbatim).

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

### CU.2. Lemma 2 (invariant multiplicities)

Source: `theory/curvature/proof.md` lines 92-95 (verbatim).

````
**Lemma 2 (invariant multiplicities).** Let $G\subset SO(3)$ be finite, with $S^2/G$ having cone
orders $m_1,\dots,m_k$. The multiplicity of the eigenvalue $\ell(\ell+1)$ on $S^2/G$ is
$$N_\ell=\frac{2\ell+1}{|G|}+\frac12\sum_{i=1}^k\Big[2\Big\lfloor\frac\ell{m_i}\Big\rfloor+1-\frac{2\ell+1}{m_i}\Big].$$

````

### CU.3. Proposition (curvature comparison) and its strength claims

Source: `theory/curvature/proof.md` lines 121-168 (verbatim).

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


## Group: divergence

### DV.0. Notation

Source: `theory/divergence/proof.md` lines 32-44 (verbatim).

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

### DV.1. Lemma 1

Source: `theory/divergence/proof.md` lines 47-59 (verbatim).

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

### DV.2. Theorem 2

Source: `theory/divergence/proof.md` lines 101-108 (verbatim).

````
**Theorem 2.** For fixed $m\ge2$, as $\ell\to\infty$,
$$\frac{b_\ell(m)}{K^\ell}=A_\ell(m)\Big(1+\frac{\pi^2}{2m^2(2\ell-1)}+O(\ell^{-2})\Big).$$
Equivalently, with $\lambda_\ell=|B_{2\ell+2}|/(2(\ell+1)!(2\ell+1))$, the leading coefficient
of $p_\ell$,
$$\frac{p_\ell(m)}{\lambda_\ell\,m^{2\ell+2}}\longrightarrow\sigma_m=\frac{\pi/m}{\sin(\pi/m)} .$$
So the full polynomial exceeds its leading term by the factor $\sigma_m$, which lies in
$(1,\pi/2]$.

````

### DV.3. Theorem 3

Source: `theory/divergence/proof.md` lines 155-177 (verbatim).

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

### DV.4. Corollary 4

Source: `theory/divergence/proof.md` lines 199-203 (verbatim).

````
**Corollary 4 (peeling).** For every $L$, the tail $(a_\ell)_{\ell\ge L}$ and $K$ determine the
cone-order multiset, $\chi$, the area and the genus. The inputs assumed known are $K$, Uçar's
(4.25)/(4.33) and $s_k>0$. This tail-only form is a small strengthening of Uçar's
Cor. 4.21(iv), whose extraction starts at $\nu=0$ and uses the area.

````

### DV.5. Borel reading (claim)

Source: `theory/divergence/proof.md` lines 233-246 (verbatim).

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


## Group: diophantine

### DI.1. Proposition 1 (reformulation)

Source: `theory/diophantine/variety.md` lines 18-33 (verbatim).

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

### DI.2. Pencil, Weierstrass model, fibre types, torsion (claims)

Source: `theory/diophantine/variety.md` lines 36-77 (verbatim).

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

### DI.3. Reciprocation is a 2-torsion translation; dual family (claims)

Source: `theory/diophantine/variety.md` lines 80-104 (verbatim).

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

### DI.4. Proposition 2 (no linear families)

Source: `theory/diophantine/variety.md` lines 162-168 (verbatim).

````
**Proposition 2.** Let $(t(u,v),t'(u,v))$ be a two-parameter family in which
every entry is a linear form, the triples are positive on an open cone, and
$S$ and $R$ agree identically. Then $t'$ is a permutation of $t$. A family
affine in one parameter (a line not through the origin) is likewise trivial.
In particular every non-scaling polynomial family has degree $\ge2$ in its
parameter.

````

### DI.5. Theorem 3 (arbitrarily large fibres)

Source: `theory/diophantine/variety.md` lines 220-223 (verbatim).

````
**Theorem 3 (arbitrarily large fibres).** For every $k$ there are
infinitely many primitive degeneracy classes of size at least $k$, i.e. $k$
pairwise distinct hyperbolic triples with a common $S$ and a common $R$.

````

### DI.6. Rank claims for fibre curves

Source: `theory/diophantine/variety.md` lines 233-237 (verbatim).

````
$3P=(162833463,287876366,723926268)$ is already large. Fibres from a single
generator are astronomically far out, and the enumeration finds far smaller
ones: the first sizes 3, 4, 5, 6 occur at $S=136,408,1849,4600$. The curves
carrying them have ranks 2, 2, 3, 3, proven with $r_1=r_2$, torsion
$\mathbf Z/6$ ([data/ranks.txt](data/ranks.txt)).
````

### DI.7. Isolation of the base pair (claim)

Source: `theory/diophantine/variety.md` lines 239-252 (verbatim).

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

### DI.8. Counting convention and the hyperbolicity of copies

Source: `theory/diophantine/variety.md` lines 261-269 (verbatim).

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

### DI.9. Theorem 4 (S log S)

Source: `theory/diophantine/variety.md` lines 271-278 (verbatim).

````
**Theorem 4 (isosceles family; explicit constant).** For coprime $1\le u<v$,
$$D_{u,v}=\{(2u+v)(u,v,v),\ (u+2v)(v,u,u)\}/g,\qquad g=\gcd(2u+v,u+2v)\in\{1,3\},$$
is a primitive degeneracy with $S=(2u+v)(u+2v)/g$ and $R=g/(uv)$; the base
pair is $D_{1,4}$. The number of these with $S\le y$ is
$c_{\rm iso}\,y+O(\sqrt y\log y)$, where $c_{\rm iso}=\dfrac{3\log2}{2\pi^2}=0.10535\ldots$.
Hence
$$\mathcal N(X)\ \ge\ \mathcal N_{\rm cl}(X)\ \ge\ \big(c_{\rm iso}+o(1)\big)\,X\log X .$$

````

### DI.10. Theorem 5 (S (log S)^2)

Source: `theory/diophantine/variety.md` lines 300-302 (verbatim).

````
**Theorem 5 (the conic bundle; one more logarithm).**
$$\mathcal N(X)\ \ge\ \Big(\frac{3}{128\pi^4}+o(1)\Big)\,X(\log X)^2 .$$

````

### DI.11. First fibres of each size and rank certification (claims)

Source: `theory/diophantine/RECOMMENDATION.md` lines 54-69 (verbatim).

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
