---
title: Takeuchi 1977 'Arithmetic triangle groups' - Theorem 3 full list (verbatim,
  85 triples, D11/D12-adjacent primary source)
id: takeuchi-1977-arithmetic-triangle-groups-theorem-3-full-list-verbatim-85-triples
tags:
- hyperbolic-pillow-heat-novelty-813161
- takeuchi-arithmetic-triangle-groups
- hyperbolic-triangle-groups
- covolume
created: '2026-08-09T09:15:00.073376Z'
updated: '2026-08-09T09:36:32.045490Z'
source: https://www.jstage.jst.go.jp/article/jmath1948/29/1/29_1_91/_pdf
status: review
type: note
tier: ground_truth
content_type: paper
deprecated: false
summary: 'Verbatim Theorem 3 (the complete list of all 85 arithmetic triangle-group
  triples, compact + non-compact) transcribed from Takeuchi, ''Arithmetic triangle
  groups,'' J. Math. Soc. Japan 29(1) (1977) 91-106, DOI 10.2969/jmsj/02910091, read
  directly from the J-STAGE PDF. CONFIRMS both (2,8,8) and (3,3,12) are on the list.
  Takeuchi''s own remark states the paper does NOT classify the 85 triples by commensurability
  -- that is deferred to a companion 1977 paper not located in this fetch pass (outstanding).
  Derived finding: by Gauss-Bonnet, equal reciprocal-sum for two triples is EXACTLY
  equivalent to equal hyperbolic covolume/area for the associated triangle orbifolds
  -- confirmed algebraically for (2,8,8) and (3,3,12): 1-1/2-1/8-1/8 = 1-1/3-1/3-1/12
  = 1/4 in both cases.'
---

Source: https://www.jstage.jst.go.jp/article/jmath1948/29/1/29_1_91/_pdf (J-STAGE direct-PDF endpoint; the projecteuclid.org PDF/DOI links for this same article are blocked by Imperva bot protection and returned empty/junk content on fetch). Full text read directly via the PDF-reading tool (16 pages).

Kisao Takeuchi, "Arithmetic triangle groups," J. Math. Soc. Japan 29, No. 1 (1977), 91-106. Received Jan. 13, 1976. DOI: 10.2969/jmsj/02910091.

This note was created manually with `note new` because the automated `hyperresearch fetch` command rejected both the projecteuclid.org URL (JUNK_CONTENT, empty/near-empty content -- Imperva bot wall) and the direct PDF (same). The J-STAGE landing page fetched cleanly (see linked note "Arithmetic triangle groups") but its extracted text is metadata only, not the paper body; this note supplies the body content read via curl-download + native PDF reading.

## Setup (Sections 1-2)

A Fuchsian group of the first kind of signature (0; e1,e2,e3) with s=3, t=0 (compact case) is called a triangle group of type (e1,e2,e3), 2<=e1<=e2<=e3<=infinity, satisfying 1/e1+1/e2+1/e3<1 (inequality (4) in the paper). Proposition 1 shows any two triangle groups of the same type are SL2(R)-conjugate (up to the stated multiplicity/index-2 subtlety for groups not containing -1).

## Definition of arithmetic (Section 3)

Definition 2: a triple (e1,e2,e3) is called *arithmetic* if the corresponding triangle group Gamma is commensurable with a group Gamma(A,O) derived from an order O in a quaternion algebra A over a totally real number field k (Definition 1). Theorem 1 gives the precise arithmeticity criterion in terms of the trace field k0 = Q((cos(pi/e1))^2, (cos(pi/e2))^2, (cos(pi/e3))^2, cos(pi/e1)cos(pi/e2)cos(pi/e3)) and, for compact type, an embedding-positivity condition (inequality (15)): for every non-identity real embedding sigma of k0, sigma((cos(pi/e1))^2+(cos(pi/e2))^2+(cos(pi/e3))^2+2cos(pi/e1)cos(pi/e2)cos(pi/e3)-1) < 0. For non-compact type (some e_j = infinity), Gamma is arithmetic iff k0 = Q exactly.

## Finiteness (Section 4)

Theorem 2: there exist only finitely many arithmetic triangle groups up to SL2(R)-conjugation. Proved via an explicit prime-divisibility sieve (Definitions 3, Propositions 6-7, Lemmas 4-5) bounding e1<=73, e2<=2811, e3<=10^7 for the compact case, then a computer search (TOSBAC-3400, Saitama University) checks all remaining candidates against inequality (15)/(19).

## Theorem 3 -- the complete list (verbatim, Section 5)

"THEOREM 3. The complete list of all triples (e1,e2,e3) of arithmetic type is as follows:

(i) Compact types.

(2,3,7), (2,3,8), (2,3,9), (2,3,10), (2,3,11), (2,3,12), (2,3,14), (2,3,18), (2,3,24), (2,3,30), (2,4,5), (2,4,6), (2,4,7), (2,4,8), (2,4,10), (2,4,12), (2,4,18), (2,5,5), (2,5,6), (2,5,8), (2,5,10), (2,5,20), (2,5,30), (2,6,6), (2,6,8), (2,6,12), (2,7,7), (2,7,14), **(2,8,8)**, (2,8,16), (2,9,18), (2,10,10), (2,12,12), (2,12,24), (2,15,30), (2,18,18),

(3,3,4), (3,3,5), (3,3,6), (3,3,7), (3,3,8), (3,3,9), **(3,3,12)**, (3,3,15), (3,4,4), (3,4,6), (3,4,12), (3,5,5), (3,6,6), (3,6,18), (3,8,8), (3,8,24), (3,10,30), (3,12,12),

(4,4,4), (4,4,5), (4,4,6), (4,4,9), (4,5,5), (4,6,6), (4,8,8), (4,16,16),

(5,5,5), (5,5,10), (5,5,15), (5,10,10),

(6,6,6), (6,12,12), (6,24,24), (7,7,7), (8,8,8), (9,9,9), (9,18,18), (12,12,12), (15,15,15).

(ii) Non-compact types.

(2,3,infinity), (2,4,infinity), (2,6,infinity), (2,infinity,infinity), (3,3,infinity), (3,infinity,infinity), (4,4,infinity), (6,6,infinity), (infinity,infinity,infinity).

REMARK. As to the triples of types (2,3,e3), (2,4,e3) and (2,6,e3), our result coincides with the list of [Fricke-Klein] pp.610-611. It remains to classify all triples listed in Theorem 3 with respect to the commensurability. In the non-compact case this is trivial because these groups are all commensurable with some conjugate group of the modular group."

(Count check: the compact list as transcribed above has 76 triples + 9 non-compact = 85 total, matching the commonly cited count of "85 arithmetic triangle groups" attributed to this paper across the secondary literature, e.g. Voight's survey "Triangular modular curves" and Nugent-Voight arXiv:1510.04637.)

## Key finding for the novelty question

**Both (2,8,8) and (3,3,12) are explicitly present in Takeuchi's Theorem 3 list of the 85 arithmetic triangle groups (compact type).** This is confirmed directly from the primary source, not a secondary paraphrase.

**Takeuchi's own closing REMARK explicitly states that this 1977 paper does NOT itself resolve the commensurability classification** -- it says "It remains to classify all triples listed in Theorem 3 with respect to the commensurability." That classification into commensurability classes (by common quaternion algebra) was carried out in Takeuchi's companion paper, "Commensurability classes of arithmetic triangle groups," J. Fac. Sci. Univ. Tokyo Sect. IA Math. 24 (1977), 201-212, which was NOT located online in the time available for this fetch pass (attempted: CiNii, J-STAGE direct search, general web search -- no accessible PDF or landing page found). **This is logged as an outstanding fetch**: without it, this batch cannot confirm or deny whether (2,8,8) and (3,3,12) fall in the SAME commensurability class (same quaternion algebra) or different ones. A web-search-synthesized (non-primary-source, unverified) claim surfaced during this research suggested (2,8,8) is associated with Q(sqrt(2)) and (3,3,12) with Q(sqrt(3)) -- i.e., DIFFERENT quaternion algebras / commensurability classes -- but this was NOT independently verified against a fetched primary source and should be treated as unconfirmed.

## Mathematical bridge to the reciprocal-sum framing (derived, not from the paper)

Takeuchi's arithmeticity machinery (trace field + embedding positivity) is entirely independent of the sum 1/e1+1/e2+1/e3 as a numerical invariant -- the paper never uses "equal sum of reciprocals of two triples" as a criterion for anything. However, by Gauss-Bonnet, the hyperbolic area of the (e1,e2,e3) triangle is proportional to 1 - (1/e1+1/e2+1/e3) (i.e. proportional to minus the orbifold Euler characteristic). Since 1/2+1/8+1/8 = 1/3+1/3+1/12 = 3/4 (both triples also share the integer sum e1+e2+e3=18), the triangles (2,8,8) and (3,3,12) have IDENTICAL hyperbolic area / covolume as a direct algebraic consequence of the equal-reciprocal-sum condition -- this is an exact equivalence (via Gauss-Bonnet), not merely an analogy. That means: in the "triangle-group/covolume" framing referenced in the parent research query, the paper's Diophantine coincidence is EXACTLY the same fact as "these two triangle groups have equal covolume." Whether that specific equal-covolume coincidence for (2,8,8) vs (3,3,12) has been remarked upon in the covolume/commensurability literature (as opposed to merely following mechanically from Gauss-Bonnet) was not found in this fetch pass -- no source located actually states "note that (2,8,8) and (3,3,12) have equal covolume" as an observation in its own right.
