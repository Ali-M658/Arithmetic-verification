# Citation check: Bari–Hunsicker, *Isospectrality for Orbifold Lens Spaces* (ledger row MAJ-12)

## Verdict

- **Manuscript description (main.tex line 128, and the framing at line 392): INCORRECT.**
  Bari–Hunsicker do not analyse "how few heat coefficients suffice". They prove that the
  *full* spectrum determines 3- and 4-dimensional orbifold lens spaces up to isometry
  (Theorems 3.1, 4.3, 5.6). Separately, they show that *the entire* heat-trace asymptotic
  expansion, meaning every coefficient, is *not* sufficient: they give non-isometric,
  non-isospectral orbifold lens spaces with "the exact same asymptotic expansion"
  (Lemmas 6.5, 6.7; Examples 6.6, 6.8). The paper has no finite-coefficient count in either
  direction.
- **MAJ-12 description: CORRECT**, with two small precision points that do not change the
  verdict. (i) Items 6.6 and 6.8 are *Examples*, not lemmas; the cited items are Lemma 6.5,
  Example 6.6, Lemma 6.7 and Example 6.8. (ii) The setting is orbifold *lens spaces*
  (cyclic quotients of S^3 and S^4), which is a subclass of spherical space forms. The phrase
  "for any k" comes from the derivation just before Lemma 6.5 (arXiv v2 p. 32; CJM p. 319),
  not from the statement of the lemma. The lemma itself says "the exact same asymptotic
  expansion".

## Bibliographic record

| Field | Value | Source |
|---|---|---|
| Title | Isospectrality for Orbifold Lens Spaces | arXiv API; Crossref; CJM PDF |
| Authors | Naveed S. Bari, Eugenie Hunsicker | Crossref (`Naveed S. Bari`, `Eugenie Hunsicker`); the arXiv API lists "Naveed Bari" |
| Journal | Canadian Journal of Mathematics **72** (2), 2020, pp. 281–325 | Crossref (volume 72, issue 2, page 281-325, published-print 2020-04); CJM PDF footer "Canad. J. Math. Vol. 72 (2), 2020 pp. 281–325" |
| Published online | 27 August 2019 | Crossref published-online 2019-08-27; CJM PDF "Published online on Cambridge Core August 27, 2019." |
| DOI | 10.4153/S0008414X19000178 | Returned by the Crossref query; printed on the CJM PDF ("http://dx.doi.org/10.4153/S0008414X19000178") |
| arXiv | 1705.01412 [math.DG; cross-list math.SP]; v1 25 Apr 2017 (30 KB), v2 12 Sep 2017 (29 KB); 38 pages | arXiv API + abs page submission history |
| arXiv journal-ref | none recorded on the arXiv record | arXiv API / abs page |
| Open access | Unpaywall: `is_oa` True, `oa_status` green, best location = arXiv PDF (submittedVersion); `journal_is_oa` False | api.unpaywall.org |

**Versions compared.** I extracted the text of arXiv v1, arXiv v2 and the published CJM
version of record (45 pp.). All three use the same numbering for the Section 6 items
(Lemma 6.5, Example 6.6, Lemma 6.7, Example 6.8) and for the headline theorems (3.1, 4.3,
5.6). v1 and v2 differ only in Section 3: v1 has "Lemma 3.2 / Lemma 3.3 / Proposition 3.4",
where v2 has "Proposition 3.2 / Lemma 3.3 …". This has no bearing on the cited items. The
quotations below come from arXiv v2 (latest) with the CJM page added. Where the published
wording differs, I quote it separately.

**Bibliography defect (aside).** main.tex lines 677–678 list the work as "preprint,
arXiv:1705.01412 (2017)". It is published (record above), and the entry should be updated.

## Manuscript text (verbatim)

`paper/main.tex` line 128:

> For orbifolds, Shams--Stanhope--Webb show one cannot hear the isotropy type~\cite{ssw2006}, Rossetti--Schueth--Weilandt construct isospectral orbifolds with different maximal isotropy orders~\cite{rsw2008}, and Bari--Hunsicker analyse how few heat coefficients suffice for orbifold lens spaces~\cite{barihunsicker2017}.

`paper/main.tex` line 392:

> In the language of the isospectral-orbifold literature~\cite{ssw2006, rsw2008, barihunsicker2017}, which measures what orbifold structure the spectrum can miss, Theorem~\ref{thmB} pinpoints the least amount of heat data that already misses the cone-order distribution, and Theorem~\ref{thmC} the least amount that recovers it.

`paper/main.tex` lines 677–678:

> \bibitem{barihunsicker2017}
> N.~S. Bari and E.~Hunsicker, \emph{Isospectrality for orbifold lens spaces}, preprint, arXiv:1705.01412 (2017).

## Verbatim quotations from the paper

Page numbers are arXiv v2 printed pages, which coincide with PDF pages, and CJM journal
pages. In the CJM text extraction the "Th" ligature is dropped ("Te", "Ten"). I restore it
in square brackets.

**Q1. Abstract** (arXiv v2 p. 1; CJM p. 281. The wording is identical apart from "Can" being
capitalised in CJM):

> We answer Mark Kac's famous question [K], "can one hear the shape of a drum?" in the positive for orbifolds that are 3-dimensional and 4-dimensional lens spaces; we thus complete the answer to this question for orbifold lens spaces in all dimensions. We also show that the coefficients of the asymptotic expansion of the trace of the heat kernel are not sufficient to determine the above results.

**Q2. Main theorems as announced in the introduction** (arXiv v2 p. 2):

> Theorem 3.1 Two three-dimensional isospectral orbifold lens spaces are isometric.
> Theorem 4.3 Two four-dimensional isospectral orbifold lens spaces are isometric.
> Theorem 5.6 Let S2n−1/G and S2n−1/G′ be two (orbifold) spherical space forms. Suppose G is cyclic and G′ is not cyclic. Then S2n−1/G and S2n−1/G′ cannot be isospectral.
> The above results will complete the classification of the inverse spectral problem on orbifold lens spaces in all dimensions.

(CJM p. 282 reads "[Th]eorem 3.1 Any two three-dimensional isospectral orbifold lens spaces are isometric." and "[Th]eorem 4.3 Any two four-dimensional isospectral orbifold lens spaces are isometric.")

**Q3. Introduction, heat-kernel claim** (arXiv v2 p. 3):

> In addition to the above theorems, we also prove that the coefficients of the trace of the heat kernel are not sufficient to prove the above results, i.e., we can have two non-isospectral orbifold lens spaces with identical coefficients of the trace of heat kernel.

Published version (CJM p. 282):

> In addition to the above theorems, we also prove that one of the traditonal methods of obtaining geomeric invariants from the spectrum, i.e., from the coefficients of the trace of the heat kernel, is not sufficient to prove the above results. We will show that we can have two non-isospectral orbifold lens spaces with identical coefficients of the trace of heat kernel.

(The typos "traditonal" and "geomeric" are in the original.)

**Q4. Opening of Section 6, "Heat Kernel for Orbifold Lens Spaces"** (arXiv v2 p. 22; CJM p. 309):

> In this section we will show that the coefficients of the asymptotic expansion of the heat trace of the heat kernel are not sufficient to obtain the results in the previous sections. More specifically, if two orbifold lens spaces have the same asymptotic expansion of the heat trace, that does not imply that the two orbifolds are isospectral.

**Q5. The all-orders step, immediately before Lemma 6.5** (arXiv v2 p. 32; CJM p. 319):

> More generally, for any k, the functions bk(γrˆα, a) and bk(γr ˆβ, a) are universal polynomials in the components of the curvature tensor, its covariant derivatives and the elements of Bγr ˆα(a) and Bγr ˆβ(b) respectively. […] This means that for each k, we will have, […]

followed (arXiv v2 p. 33) by

> This observation gives us the following lemma for three-dimensional orbifold lens spaces:

**Q6. Lemma 6.5, conclusion and gloss** (arXiv v2 p. 33; CJM p. 320). The hypotheses are long
congruence/gcd conditions on generators γ1, γ2 of cyclic groups acting on S^3, defining
α_i, β_i:

> Lemma 6.5. Given two orbifold lens spaces O1 = S3/G1 and O2 = S3/G2, such that G1 =< γ1 > and G2 =< γ2 > where […]
> Then O1 = S3/G1 and O2 = S3/G2 will have the exact same asymptotic expansion of the heat kernel if α1 = α2 and β1 = β2.
> This lemma gives us a tool to find examples of 3-dimensional orbifold lens spaces that are non-isometric (hence non-isospectral) but have the exact same asymptotic expansion of the heat kernel.

**Q7. Example 6.6** (arXiv v2 p. 33; CJM p. 320):

> Example 6.6. Suppose q = 195, and consider the two lens spaces O1 = L(195 : 3, 5) and O2 = L(195 : 6, 35). Since there is no integer l coprime to 195 and no ei ∈{1, −1} such that {e1l3, e2l5} is a permutation of {6, 35}(mod q), O1 and O2 are not isometric (and hence non-isospectral). […] Therefore, O1 = L(195 : 3, 5) and O2 = L(195 : 6, 35) have the exact same asymptotic expansion.

**Q8. Section 6.3 opening** (arXiv v2 p. 33; CJM p. 320):

> Similar to the three-dimensional case we can show the construction of examples in four-dimensional lens spaces where the lens spaces will not be isospectral but will have the exact same asymptotic expansion of the trace of the heat kernel.

**Q9. Lemma 6.7, conclusion and gloss** (arXiv v2 pp. 36–37; CJM p. 323):

> Lemma 6.7. Given two orbifold lens spaces O1 = S4/G1 and O2 = S4/G2, such that G1 =< γ1 > and G2 =< γ2 > where […]
> Then O1 = S4/G1 and O2 = S4/G2 will have the exact same asymptotic expansion of the heat kernel if α1 = α2 and β1 = β2.
> This lemma gives us a tool to find examples of 4-dimensional orbifold lens spaces that are non-isometric (hence non-isospectral) but have the exact same asymptotic expansion of the heat kernel.

**Q10. Example 6.8** (arXiv v2 p. 37; CJM p. 323):

> Example 6.8. Suppose q = 195, and consider the two lens spaces O1 = ˜L1+ = L(195 : 3, 5, 0) and O2 = ˜L′1+ = L(195 : 6, 35, 0) (using the notation from Lemma 4.1). […] Therefore, O1 and O2 have the exact same asymptotic expansion.

**Searches with no hits.** I searched the full arXiv v2 text for "how many", "number of
coef", "all k", "every k" and "suffic". The only uses of "sufficient" in connection with the
heat kernel are the negative "not sufficient" statements in Q1, Q3 and Q4. (The other hits,
"it is sufficient to show" on p. 21 and "it suffices to consider" on pp. 26 and 35, are
proof steps.) "First few coefficients" occurs only as "we now calculate the first few
coefficients of the asymptotic expansion" (arXiv v2 p. 31), which introduces the explicit
computation of b0 and b1 before the general-k argument in Q5. The paper states no threshold,
bound or minimal number of coefficients anywhere.

## Analysis

**(1) What Bari–Hunsicker prove about heat coefficients.**
The positive results (Q2) concern the *full Laplace spectrum*: in dimensions 3 and 4,
isospectral orbifold lens spaces are isometric, and a cyclic quotient S^{2n-1}/G cannot be
isospectral to a non-cyclic one. The heat-coefficient result is negative only and covers all
orders. The derivation shows that for every k the fixed-point contributions b_k take a form
that depends only on (α, β) (Q5). Lemmas 6.5 and 6.7 then conclude that two orbifold lens
spaces in S^3 (resp. S^4) with α1 = α2, β1 = β2 "will have the exact same asymptotic
expansion of the heat kernel" (Q6, Q9). Examples 6.6 and 6.8 give a concrete pair with
q = 195. It is non-isometric, hence by Theorems 3.1/4.3 non-isospectral, yet has identical
heat expansions (Q7, Q10). So the answer to the task's question is: **non-determination to
all orders only.** The paper contains no finite-coefficient determination result and no
finite-coefficient count. Its only positive determination result uses the whole spectrum,
not heat invariants. It claims no minimality: the lemma is offered as "a tool to find
examples" (Q6, Q9).

**(2) The manuscript's description.** Line 128 says Bari–Hunsicker "analyse how few heat
coefficients suffice for orbifold lens spaces". This is wrong on two counts:
- *Direction:* the paper shows heat coefficients do **not** suffice (Q1, Q3, Q4).
- *Quantifier:* "how few" implies a count or threshold. The paper's statement covers the
  whole expansion ("for any k", "the exact same asymptotic expansion"), and no number of
  coefficients is singled out.

A reader who follows the citation would find the opposite of what line 128 says. The
sentence is therefore INCORRECT, not just imprecise.

At line 392, Bari–Hunsicker is one of three citations for a "language … which measures what
orbifold structure the spectrum can miss". For Bari–Hunsicker this is also inaccurate as
written. Their spectral theorems show that the spectrum misses *nothing* for 3- and
4-dimensional orbifold lens spaces (Q2). What misses structure is the *heat-invariant
expansion*, relative to the spectrum (Q3, Q4).

**(3) MAJ-12's description.** MAJ-12 says the cited lemmas show "equal heat expansions for any
k in spherical space forms, i.e. non-determination to all orders, not a finite-coefficient
count", and that this is "the opposite direction" from the manuscript's gloss. Q4–Q10 confirm
both points. The precision notes in the Verdict section are minor: 6.6 and 6.8 are Examples,
the setting is specifically orbifold lens spaces in S^3 and S^4, and "for any k" sits in the
derivation rather than the lemma statement. The review's earlier verbatim quotation of
Lemma 6.5 (Q3-priority-claim.md §1(a)) matches the fetched text exactly. MAJ-12's caveat that
the primary paper had not been re-read is now discharged.

**(4) Is the "language of Theorems B and C" framing defensible?** Only partly, and only after
rewording. There is a real conceptual link with Theorem B. Bari–Hunsicker exhibit heat data
failing to detect structure that the spectrum detects. Theorem B, as line 392 describes it,
exhibits a bounded initial segment of heat data failing to detect the cone-order
distribution, which the full spectrum detects (line 392 cites Uçar for this). The honest
relation is a *contrast in quantifier and setting*:
- Bari–Hunsicker: all orders, spherical orbifold lens spaces, negative only.
- The manuscript: a finite truncation with a threshold, hyperbolic 2-orbifolds, both a
  negative (B) and a positive (C) result.

Bari–Hunsicker give no support to Theorem C's "least amount that recovers it": they contain
no recovery-from-finitely-many-coefficients result. The current phrasing implies that
Bari–Hunsicker share the manuscript's "how much heat data" vocabulary, and they do not.
Citing them as a point of contrast is defensible. Citing them as sharing a "language" for
Theorems B and C is not.

## Recommended wording

**Line 128.** Replace the final clause with:

> …, and Bari--Hunsicker show that the spectrum determines orbifold lens spaces of dimensions 3 and 4 up to isometry, while exhibiting non-isospectral orbifold lens spaces whose heat-trace asymptotic expansions coincide to all orders, so that no number of heat coefficients suffices there~\cite{barihunsicker2017}.

A shorter alternative:

> …, and Bari--Hunsicker exhibit non-isospectral orbifold lens spaces with identical heat-trace expansions, so that in that setting the heat invariants, to all orders, do not recover what the spectrum does~\cite{barihunsicker2017}.

**Line 392.** Remove `barihunsicker2017` from the "language" citation, or restrict the
sentence to the works it fits. Then add one contrasting sentence. For example:

> In the language of the isospectral-orbifold literature~\cite{ssw2006, rsw2008}, which measures what orbifold structure the spectrum can miss, Theorem~\ref{thmB} pinpoints the least amount of heat data that already misses the cone-order distribution, and Theorem~\ref{thmC} the least amount that recovers it. This is a finite-order phenomenon and differs in kind from the spherical case, where Bari--Hunsicker exhibit non-isospectral orbifold lens spaces whose heat-trace expansions agree to all orders~\cite{barihunsicker2017}.

(Before keeping `ssw2006` and `rsw2008` in the "language" citation, the authors should
separately confirm that this phrase is apt for those two works. This note checks only
Bari–Hunsicker.)

**Bibliography (lines 677–678).** Replace with:

> N.~S. Bari and E.~Hunsicker, \emph{Isospectrality for orbifold lens spaces}, Canad. J. Math. \textbf{72} (2020), no.~2, 281--325, doi:10.4153/S0008414X19000178; arXiv:1705.01412.

## Instrument gaps

- None blocking. All of the following returned HTTP 200 with usable content:
  - the arXiv API (`https://export.arxiv.org/api/query?id_list=1705.01412`)
  - the arXiv abs page
  - `https://arxiv.org/pdf/1705.01412v1` and `…v2` (application/pdf, 38 pp. each)
  - the Crossref query
  - Crossref `works/10.4153/s0008414x19000178`
  - Unpaywall (`api.unpaywall.org/v2/10.4153/S0008414X19000178`)
  - the DOI resolver → Cambridge Core landing page
  - the CJM PDF at the landing page's `citation_pdf_url` (application/pdf, 45 pp.)
- Unpaywall lists only the arXiv submittedVersion as an open-access location
  (`journal_is_oa` False). The CJM version-of-record PDF downloaded through Cambridge Core
  carries the footer "subject to the Cambridge Core terms of use". Its open availability
  outside this access context was not established.
- In the PyMuPDF text extraction of the CJM PDF, the "Th" ligature drops out ("Te", "Ten",
  "Terefore"). Quotations from that version restore it in brackets. Matrix layouts inside
  Lemmas 6.5 and 6.7 extract imperfectly in all versions, so those hypotheses are elided
  with […] rather than quoted.
- Raw downloads and extracted text are in
  a local scratch directory (`lit-c/`, not committed)
  (`bh_v1.pdf`, `bh_v2.pdf`, `cjm.pdf`, and the `.txt` extractions).
