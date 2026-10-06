# G5-bis audit: statements under review, group `trace-formula`

Trace formula: the closed form of the elliptic weight, Lemma 2.5 for every order, agreement with Ucar, Remark 4.12, the constant of Theorem 1.2(iii)

Every result below is copied verbatim, by line range, from its source file (`review/audit-2/build_statements.py`
asserts the anchors and that no proof text is included). Items marked COMPOSED combine verbatim excerpts with
connective text in [square brackets]. **Proofs, scripts and data of the sessions that produced these results are
deliberately withheld.** You must not open any file of `theory/pte/`, `theory/revision/`, `theory/signatures/`
(other than where stated below), `review/referee-sim/` or `paper/` (the manuscript contains proofs of some of these
results). If you do open one by accident, say so in your REVIEW.md under 'contamination'.



## Context files you may read (previously audited statements, no proofs)

- review/audit/statements/locality.md  (LO.6 Theorem 3.1 = the integrated trace formula with elliptic terms, LO.7, LO.8 admissibility and counting; DF.1 definitions of the heat coefficients and signature). These are previously audited; a result below may use them as stated. Hypotheses of the trace formula are an external input: read Dryden-Strohmaier eq. (1) in the fetched text.

## External inputs

- Selberg trace formula for cocompact Fuchsian groups with elliptic elements, in the form of Dryden-Strohmaier arXiv:math/0504571 eq. (1) (fetched: sources/ds_math0504571.txt).
- Ucar, arXiv:1711.03405, (4.25), (4.33)-(4.35) (fetched: sources/ucar_1711.03405.txt).
- Dryden-Gordon-Greenwald-Webb arXiv:0805.3148, Thm 4.8, section 5.6 (fetched: sources/dggw_0805.3148.txt). Schueth arXiv:1812.06119, Rem. 4.2, Thm 4.1 (fetched: sources/schueth_1812.06119.txt).
- Classical analysis only otherwise: Euler's beta integral, Bernoulli numbers, Liouville's theorem.

## Fetched sources

Texts fetched headlessly by `review/audit-2/fetch_sources.sh` are in `review/audit-2/sources/` (not committed).
Never quote a source from memory: quote the fetched text, with page or section. An unreachable source is an
instrument gap, to be logged, not a confirmation.


## Group: trace-formula

### TF.1. Notation for the elliptic moments, and Lemma (Elliptic moments)

Source: `theory/revision/lemma25.tex` lines 16-26; `theory/revision/lemma25.tex` lines 28-39 (verbatim).

````
\subsection{The expansion}\label{sec:heatexp}

The structure of the expansion is due to Donnelly and to Dryden, Gordon, Greenwald and Webb
\cite{donnelly1976,dggw2008}, and U\c{c}ar computed every coefficient at constant curvature
\cite{ucar2017}. We derive the coefficients again from the trace formula of
Theorem~\ref{thm:IEH}, which gives them in closed form for every order. For $0<a<2\pi$ put
\[
  F_a(r)=\frac{e^{-ar}}{1+e^{-2\pi r}},\qquad \mu_n(a)=\int_\R r^nF_a(r)\,dr ,
\]
so that $F_a(r)\le e^{-ar}$ for $r\ge0$ and $F_a(r)\le e^{(2\pi-a)r}$ for $r\le0$, and every
$\mu_n(a)$ is finite.

\begin{lemma}[Elliptic moments]\label{lem:ellmoments}
Let $0<a<2\pi$.
\begin{enumerate}[label=(\roman*)]
\item For $a-2\pi<s<a$, $\displaystyle\int_\R F_a(r)\,e^{sr}\,dr=\frac1{2\sin((a-s)/2)}$; hence
  $\mu_n(a)=\frac{d^n}{ds^n}\big[2\sin((a-s)/2)\big]^{-1}\big|_{s=0}$.
\item For every $K\ge1$ and $t>0$,
  \[
    \Big|\int_\R F_a(r)\,e^{-tr^2}\,dr-\sum_{k=0}^{K-1}\frac{(-t)^k}{k!}\,\mu_{2k}(a)\Big|
    \le\frac{t^K}{K!}\,\mu_{2K}(a).
  \]
\end{enumerate}
\end{lemma}
````

### TF.2. Definition of Phi_m and Lemma (Closed form)

Source: `theory/revision/lemma25.tex` lines 50-55; `theory/revision/lemma25.tex` lines 57-67 (verbatim).

````
Write $\theta_j=\pi j/m$ and, for an integer $m\ge1$,
\[
  \Phi_m(u)=\sum_{j=1}^{m-1}\frac1{4m\,\sin\theta_j\,\sin(\theta_j-u)} .
\]
Each term is analytic in $|u|<\pi/m$, so $\Phi_m$ is analytic there; $\Phi_1=0$, and
$\Phi_m(-u)=\Phi_m(u)$ (replace $j$ by $m-j$).

\begin{lemma}[Closed form]\label{lem:Phi}
For $m\ge1$ and $0<|u|<\pi/m$,
\begin{equation}\label{eq:Phi}
  \Phi_m(u)=\frac{\cot u-m\cot(mu)}{4m\sin u}.
\end{equation}
Write $u/\sin u=\sum_{i\ge0}\sigma_iu^{2i}$, so $\sigma_i\in\Q$, $\sigma_0=1$ and in fact $\sigma_i>0$.
Then $\Phi_m(u)=\sum_{k\ge0}\phi_k(m)\,u^{2k}$ with
\begin{equation}\label{eq:phik}
  m\,\phi_k(m)=\frac14\sum_{n=1}^{k+1}\sigma_{k+1-n}\,\frac{4^n|B_{2n}|}{(2n)!}\,\big(m^{2n}-1\big).
\end{equation}
\end{lemma}
````

### TF.3. Lemma (The hyperbolic term is small)

Source: `theory/revision/lemma25.tex` lines 87-93 (verbatim).

````
\begin{lemma}[The hyperbolic term is small]\label{lem:hypbound}
Let $\Orb\in\Sig$ have area $A$, systole $\ell$ and diameter $D$. For $0<t\le\ell^2/(2(1+\ell))$,
\[
  0\le\Hyp(t)\le\frac{\pi e^{3D}}{A(1-e^{-\ell})}\;\ell e^{\ell/2}\Big(1+\frac{2t}{\ell-t}\Big)\frac{e^{-\ell^2/4t}}{\sqrt{4\pi t}} .
\]
In particular $\Hyp(t)=O(t^N)$ as $t\downarrow0$ for every $N$.
\end{lemma}
````

### TF.4. Proposition (The heat expansion at curvature -1)

Source: `theory/revision/lemma25.tex` lines 101-119 (verbatim).

````
\begin{proposition}[The heat expansion at curvature $-1$]\label{prop:heatinput}
Let $\Orb\in\Sig$ have signature $(g;m_1,\dots,m_n)$. As $t\downarrow0$,
\[
  \cZ_\Orb(t)\ \sim\ \frac{\Area(\Orb)}{4\pi t}\sum_{k\ge0}\alpha_kt^k\;+\;\sum_{i=1}^n\sum_{l\ge0}b_l(m_i)\,t^l,
\]
where
\begin{equation}\label{eq:alphak}
  \alpha_k=\frac{(-1)^k}{k!\,4^k}\sum_{l=0}^k\binom kl(-4)^lB_{2l}\big(\tfrac12\big)
\end{equation}
and, for every integer $m\ge1$,
\begin{equation}\label{eq:bl}
  b_l(m)=\frac{(-1)^l\,p_l(m)}{m},\qquad
  p_l(m)=\frac1{4^l}\sum_{k=0}^{l}\frac{(2k)!}{k!\,(l-k)!}\;m\,\phi_k(m).
\end{equation}
Consequently $c_1=\Area(\Orb)/4\pi$ and, for $j\ge2$,
\begin{equation}\label{eq:cj}
  c_j(\Orb)=\alpha_{j-1}\,\frac{\Area(\Orb)}{4\pi}+\sum_{i=1}^nb_{j-2}(m_i).
\end{equation}
\end{proposition}
````

### TF.5. Lemma (Cone polynomials) = Lemma 2.5, and the printed first values

Source: `theory/revision/lemma25.tex` lines 145-152; `theory/revision/lemma25.tex` lines 166-173 (verbatim).

````
\begin{lemma}[Cone polynomials]\label{lem:conepoly}
For every $l\ge0$, $p_l$ is an even polynomial with rational coefficients, of degree exactly
$2l+2$, with $p_l(1)=0$ and leading coefficient
\[
  \frac{|B_{2l+2}|}{2\,(l+1)!\,(2l+1)}\ne0 .
\]
Moreover $p_l(m)>0$ for every real $m>1$.
\end{lemma}

The first values are $\alpha_0,\dots,\alpha_4=1,-\tfrac13,\tfrac1{15},-\tfrac4{315},\tfrac1{315}$, and
\begin{equation}\label{eq:plexplicit}
  p_0(m)=\frac{m^2-1}{12},\qquad p_1(m)=\frac{m^4}{360}+\frac{m^2}{36}-\frac{11}{360},\qquad p_2(m)=\frac{m^6}{2520}+\frac{m^4}{720}+\frac{m^2}{180}-\frac{37}{5040}.
\end{equation}
The polynomials $p_1,p_2$ agree with the cone coefficients of Schueth \cite[Rem.~4.2, Thm~4.1]{schueth2019},
which she attributes to \cite[\S5.6]{dggw2008} at order $t^1$.
The value $p_l(1)=0$ has a direct meaning: an ``order-$1$ cone point'' is a smooth point, and the sum
defining $\Phi_1$ is empty.
````

### TF.6. Remark (Agreement with Ucar), the claim

Source: `theory/revision/lemma25.tex` lines 175-175; `theory/revision/lemma25.tex` lines 179-187 (verbatim).

````
\begin{remark}[Agreement with U\c{c}ar]\label{rem:ucaragree}

[derivation of the identity m t^2 Phi_m(it/2) = ... omitted]

where, by \cite[(4.25)]{ucar2017},
\[
  c^{\mathbb S}_k\Big(\frac\pi m\Big)=\frac1{4m}\cdot\frac{(-1)^k}{(k+1)!\,(2k+1)}\sum_{j=0}^{k+1}\binom{2k+2}{2j}\big(m^{2j}-1\big)B_{2j}\,B_{2k+2-2j}\big(\tfrac12\big).
\]
Then \eqref{eq:bl} becomes $p_l(m)/m=\sum_{i\le l}2(4^ii!)^{-1}c^{\mathbb S}_{l-i}(\pi/m)$, which is $(-1)^l$
times U\c{c}ar's cone contribution \cite[(4.33)--(4.34)]{ucar2017} at $K=-1$. So the cone terms of
Proposition~\ref{prop:heatinput} are U\c{c}ar's for every $l$; his smooth coefficients
\cite[(4.35)]{ucar2017} are given by the same formula as \eqref{eq:alphak}. The two were also compared in
exact arithmetic for $l\le40$ (code in the archived repository, Appendix~\ref{app:reproducibility}).
````

### TF.7. Remark 4.12 (the trace-formula proof of locality): the independence claim, versions 2A and 2B and the replacement sentence

Source: `theory/revision/remark412.tex` lines 17-20; `theory/revision/remark412.tex` lines 22-25; `theory/revision/remark412.tex` lines 32-45; `theory/revision/remark412.tex` lines 49-61 (verbatim).

````
No local invariant can see the moduli: any two hyperbolic orbifolds of the same signature are
locally isometric, point by point and cone point by cone point. The trace formula of
Theorem~\ref{thm:IEH} gives a second, independent proof, with the coefficients
(Remark~\ref{rem:proofC}).

% (1A) if lemma25.tex is adopted (version 2A), where the trace formula is the primary proof:
%   "No local invariant can see the moduli: any two hyperbolic orbifolds of the same signature
%    are locally isometric, point by point and cone point by cone point; this structural reading,
%    through the locality of the heat invariants \cite{donnelly1976,dggw2008}, is a second proof.

\begin{remark}[The trace-formula proof of locality]\label{rem:proofC}
Theorem~\ref{thm:IEH} proves Theorem~\ref{thm:locality} directly: $\mathrm I$ depends only on the
area and $\mathrm E$ only on the cone orders, and $0\le\Hyp(t)=O(t^{-1/2}e^{-\ell^2/4t})=O(t^N)$ for
every $N$ (Lemma~\ref{lem:hypbound}), so the asymptotic series of $\cZ_\Orb$ is that of
$\mathrm I+\mathrm E$. This is how Proposition~\ref{prop:heatinput} and Lemma~\ref{lem:conepoly} were
proved, and it is independent of the coefficient computations of \cite{dggw2008} and
\cite{ucar2017}. The only input from the heat-kernel literature is the a-priori bound
$\#\{\lambda_j\le x\}\le e\,\cZ_\Orb(1/x)=O(x)$ in the proof of Lemma~\ref{lem:admissible}, which uses
only the a-priori bound $\cZ_\Orb(s)=O(1/s)$ as $s\downarrow0$, a consequence of \cite[Thm~4.8]{dggw2008}
(or of Weyl's law). It determines no coefficient $c_j$ with $j\ge2$, so nothing is circular. U\c{c}ar's
cone terms \cite[(4.25), (4.33)--(4.34)]{ucar2017} agree with Proposition~\ref{prop:heatinput} for every
order (Remark~\ref{rem:ucaragree}), and his smooth coefficients \cite[(4.35)]{ucar2017} are given by
the same formula as \eqref{eq:alphak}.
\end{remark}

\begin{remark}[The trace-formula proof of locality]\label{rem:proofC}
Theorem~\ref{thm:IEH} gives an independent proof of Theorem~\ref{thm:locality}: $\mathrm I$ and
$\mathrm E$ depend only on the signature, and $0\le\Hyp(t)=O(t^{-1/2}e^{-\ell^2/4t})=O(t^N)$ for every
$N$, so the asymptotic series of $\cZ_\Orb$ is that of $\mathrm I+\mathrm E$. Expanding
$e^{-tr^2}$ under the integrals, with the moments
$\int_0^\infty r^{2k+1}(e^{2\pi r}+1)^{-1}dr=(1-2^{-2k-1})(-1)^kB_{2k+2}/(4(k+1))$ and
$\int_\R e^{-ar}(1+e^{-2\pi r})^{-1}e^{sr}dr=1/(2\sin((a-s)/2))$, reproduces the constants $\alpha_k$
and $b_l(m)$ of Proposition~\ref{prop:heatinput} for every order. This route does not use the
coefficient computations of \cite{dggw2008} or \cite{ucar2017}. Its only input from the
heat-kernel literature is the a-priori bound $\#\{\lambda_j\le x\}\le e\,\cZ_\Orb(1/x)=O(x)$ in
Lemma~\ref{lem:admissible}, which uses only $\cZ_\Orb(s)=O(1/s)$, a consequence of
\cite[Thm~4.8]{dggw2008} (or of Weyl's law), and determines no $c_j$ with $j\ge2$.
\end{remark}
````

### TF.8. Theorem 1.2(iii): the constant and the 'attained' statement; Theorem 4.9(b) form

Source: `theory/revision/thm12iii.tex` lines 10-23; `theory/revision/thm12iii.tex` lines 31-36 (verbatim).

````
\item Let $\Orb_1,\Orb_2$ have the same signature and area $A$, let $\ell$ be the smaller of their
systoles and $D$ the larger of their diameters. For $0<t\le\ell^2/(2(1+\ell))$,
\[
  |\cZ_{\Orb_1}(t)-\cZ_{\Orb_2}(t)|\le C(A,\ell,D)\,t^{-1/2}e^{-\ell^2/4t},\qquad
  C(A,\ell,D)=\frac{\sqrt\pi\,e^{3D}\,\ell\,e^{\ell/2}\,(2+3\ell)}{2A\,(1-e^{-\ell})\,(2+\ell)} .
\]
The constant depends on the diameter, which the signature does not determine. If the two length
spectra, counted with the weights $\ell(\gamma_0)$, first differ at the length $\ell$ (in particular,
if the two systoles differ), then $\sqrt t\,e^{\ell^2/4t}|\cZ_{\Orb_1}(t)-\cZ_{\Orb_2}(t)|$ has a
nonzero limit as $t\downarrow0$: the exponent $\ell^2/4$ and the factor $t^{-1/2}$ are attained,
the constant $C$ is not claimed to be. If they first differ at a length $L_*>\ell$, the difference
is of the smaller order $t^{-1/2}e^{-L_*^2/4t}$; if the weighted length spectra never differ
(equivalently, the orbifolds are isospectral) the difference vanishes identically. Here the
systole is the least length of a closed geodesic, including those through cone points.

%   For $0<t\le\ell^2/(2(1+\ell))$,
%   \[
%     |\cZ_{\Orb_1}(t)-\cZ_{\Orb_2}(t)|\le\frac{\pi e^{3D}}{A(1-e^{-\ell})}\;\ell e^{\ell/2}\Big(1+\frac{2t}{\ell-t}\Big)\frac{e^{-\ell^2/4t}}{\sqrt{4\pi t}}
%     \le C(A,\ell,D)\,t^{-1/2}e^{-\ell^2/4t},
%   \]
%   with $D=\max(\operatorname{diam}\Orb_1,\operatorname{diam}\Orb_2)$ and $C$ as in Theorem 1.2(iii);
````
