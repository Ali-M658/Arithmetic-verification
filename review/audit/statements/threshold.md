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
| Holtz–Tyaglov, arXiv:0912.4703 (Orlando's formula) | audibility, stability | `holtz_tyaglov_0912.4703.txt` |
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
