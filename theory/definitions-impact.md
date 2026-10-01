# Impact of `definitions.tex` on `paper/main.tex`

Checked against `paper/main.tex` (MD5 `adfa0001c73e3721f3ccdcc6dcda7e12`, 723 lines). `theory/definitions.tex` compiles against the main preamble (tested in a scratch copy, with stub labels for `prop:recovery` and `thmC`); `main.tex` itself was not touched.

**Result: 8 sentences must change; 14 more read correctly but rest on the new definitions and should be re-read when those 8 are edited. 22 sentences in all.** Two bibliography entries must be added (`troyanov1991`, `thurston1998`, both already in `refs/sources.bib`).

The restated Remark 5.6 and Theorem C do read correctly in context: Theorem C's own title (line 113) already says "determinacy of the cone-order multiset", and the body of the remark (line 494) is a three-sentence unit whose only wrong step is "so the upper bound $K\le n$ extends the $n=3$ case of Theorem C". Nothing else in Section 5 depends on the remark. The remark's label compiles as **Remark 5.1** (not 5.6): `\newtheorem{remark}[definition]` shares the `definition` counter, and Section 5 contains no definition before it. The labels `rem:ncone` and `tab:density` / `tab:enum` (Tables 1 and 2 in the compiled order) are the stable names.

Recommended minimal-edit route: keep the symbol $K(F)$ everywhere and define it once, at line 103, as $K(F):=K_{\mathrm{iso}}(F;\mathcal P_3)=K_{\mathrm{mult}}(F;\mathcal P_3)$ with a pointer to the rigidity proposition. Then every sentence marked CHECK below stays as written.

## A. Sentences that must change (8)

| # | Line | Current sentence (trimmed) | Kind | Required change |
|---|---|---|---|---|
| 1 | 103 | "Throughout, $K(F)$ denotes the least number of leading heat coefficients that distinguish a pillow $F$ from every other hyperbolic triangular pillow" | REWRITE | Name the comparison class $\mathcal P_3$ and the notion (Def. K). State that on $\mathcal P_3$ the isometry and multiset readings coincide (Prop. rigidity), so one symbol suffices. |
| 2 | 114 | "The first three heat coefficients determine a hyperbolic triangular pillow up to isometry, equivalently, they determine its singular set together with the cone order at each singular point." | REWRITE | "…determine its signature, i.e. the multiset of cone orders, and hence, by rigidity of triangle orbifolds, its isometry class." The coefficients do not see the positions of the cone points as such; the "equivalently" is true only through rigidity. |
| 3 | 160 | "(i) … the $n$-cone generalization is discussed in Remark 5.1 and established here only for $n=3$." | REWRITE | "…discussed in Remark 5.1, where only the cone-order multiset (not the isometry class) is at issue for $n\ge4$; the isometry statement is specific to $n=3$." |
| 4 | 357 | "…and non-isometric, having distinct cone-order multisets, yet share the signature $\sigma(2,8,8)=\sigma(3,3,12)$." | ADD | "non-isometric" is deduced from "distinct multisets" here; insert "(by rigidity, Prop. rigidity)". Note that $\sigma$ in main.tex denotes the pair $(S_1,R)$, which collides with the signature $\sigma(\mathcal O)$ of Def. signature: rename one of them. |
| 5 | 373 | "…determine the cone-order multiset $\{p,q,r\}$, hence the pillow up to isometry: $K(F)\le3$ for every hyperbolic triangular pillow." | ADD | The step "multiset $\Rightarrow$ isometry class" is rigidity and is currently unstated. Insert the proposition (Möbius triple transitivity plus Troyanov's uniqueness theorem) or cite it. |
| 6 | 373 | "The multiset is exactly the data of the singular stratum, the three cone points together with the cone angle $2\pi/m_i$ at each, so three coefficients determine the singular stratum with its cone orders." | REWRITE | A multiset of orders is not "the three cone points". Say: the multiset is the signature; rigidity then fixes the pillow, and with it the cone points and their angles. |
| 7 | 494 | "…and when these are independent they recover the multiset, so the upper bound $K\le n$ extends the $n=3$ case of Theorem C." | REWRITE | The defect of ledger item FAT-01. Replace by part (a)+(b) of the restated remark: multiset level $K_{\mathrm{mult}}\le n$ (conditional on injectivity); isometry level $K_{\mathrm{iso}}=\infty$ for $n\ge4$ (conditional on the locality theorem). |
| 8 | 494 | "The matching lower bound $K\ge n$ for $n\ge4$ would require two $n$-cone pillows agreeing in $n-1$ prescribed symmetric functions … for which we have neither a construction nor a non-existence proof; we leave it open." | REWRITE | Restate for $K_{\mathrm{mult}}$ and, if the author agrees, replace "neither a construction" by the $n=4$ witness $\{3,10,15,30\}$, $\{4,5,21,28\}$ (shared $S_1=58$, $R=8/15$, $P_3=31402$; $P_5$ differs), checked in `theory/definitions-check.py`. As printed the sentence is stale against that computation. |

## B. Sentences that read correctly but depend on the definitions (14)

| # | Line | Sentence (trimmed) | Why it is in the list |
|---|---|---|---|
| 9 | 58 | "the first three always determine the pillow up to isometry" | Abstract; true for triangular pillows by rigidity. Consider adding "triangular". |
| 10 | 101 | "pinning down the singular stratum, the cone points together with their orders" | "singular stratum" is used for the multiset in several places; harmless once line 114 and 373 are fixed. |
| 11 | 103 | "…a pair of non-isometric pillows sharing their first two heat coefficients is a *two-coefficient spectral degeneracy*" | Equivalent to "distinct signatures" only by rigidity. |
| 12 | 106 | "…so $K(F)\le2$." (Theorem A) | Correct under either reading on $\mathcal P_3$. |
| 13 | 114 | "Thus $K(F)\le3$ for every such pillow, and $K(F)=3$ for the collision pair." | Correct; it is Theorem C restated. |
| 14 | 118 | "…the two leading coefficients resolve the full singular stratum for every pillow with $p+q+r\le17$" | Uses "singular stratum" for the signature. |
| 15 | 121 | "…the third completes the singular stratum" | Same. |
| 16 | 153 | "…and the full singular stratum recovered by three" | Same. |
| 17 | 160 | "(iv) The two-coefficient theory has $K(F)\le3$ unconditionally (Theorem C)…" | Correct on $\mathcal P_3$. |
| 18 | 357 | "…so $K(F)=3$ for both (Proposition 2.7)." | Correct. |
| 19 | 373 | "For the pair … we have $K(F)=3$: they are not separated by two coefficients, yet are separated by three." | Correct. |
| 20 | 373 | "We do not assert that these are the *only* pillows with $K(F)=3$…" | Correct; "$K(F)=3$ iff in a collision" is in the restated theorem. |
| 21 | 481 | "…exhibits a further pillow with $K(F)=3$: since Theorem C gives $K(F)\le3$ unconditionally, the set enumerated here is exactly the set of hyperbolic triangular pillows for which two heat coefficients do not suffice" | Correct; it uses $K=3\iff$ collision, which holds on $\mathcal P_3$ only. |
| 22 | 494 | "For an $n$-cone pillow $\mathcal O(m_1,\dots,m_n)$, a sphere with $n$ cone points, hyperbolic when $\sum_i(1-1/m_i)>2$, the first $n$ leading heat coefficients again supply $n$ symmetric functions of the orders" | True; to be made explicit ($R,S_1,P_3,\dots,P_{2n-3}$) when the remark is rewritten. |

## C. Dependencies the restated statements create

* **Locality theorem.** Part (b) of the restated remark and the statement "$K_{\mathrm{iso}}=\infty$ whenever the moduli space has positive dimension" depend on Theorem Locality (all heat coefficients are functions of the signature), which `definitions.tex` states as a forward reference and does not prove. Until it is proved, those statements must be worded as conditional or as an expectation in the manuscript. Owner: session S5.
* **Injectivity.** Part (a) is conditional on injectivity of $(R,S_1,P_3,\dots,P_{2n-3})$ on $n$-element multisets, unproved for $n\ge4$. Owner: session S4.
* **Nonvanishing weights.** "$c_j$ carries $P_{2j-3}$ with a nonzero weight" rests on the Bernoulli closed form for the leading coefficient of $p_\ell$, verified exactly for $\ell=0,\dots,6$ in `theory/cone-coefficients/` and not proved for all $\ell$ in this fragment.
* **Genus.** The moduli count is used only for genus $0$. The $6g-6+2n$ count for $g\ge1$ has no fetched source and is not asserted.
* **Citations.** `troyanov1991` and `thurston1998` must be added to the bibliography of `main.tex`. Records and verbatim quotations: `theory/teichmuller-dimension-sources.md`. Thurston's result is the flat analogue; the hyperbolic count is a two-step deduction, which that file flags.
* **Notation clash.** `main.tex` already uses $\sigma$ for the pair $(S_1,R)$ (line 357, Theorem 3.4); Definition signature uses $\sigma(\mathcal O)$ for $(g;m_1,\dots,m_n)$. One of the two needs renaming at rewrite time.
