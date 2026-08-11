# Utility scoring — wave 1 URL queue

Six dimensions, 0–3 each, composite max 18:
Authority · Novelty · Stance diversity · Coverage · Redundancy · Freshness.

**A note on how "freshness" is scored here.** This is a mathematics literature sweep, so
the topic is foundational rather than temporal: a 2008 journal article that is the
analytic input to the manuscript's Theorem C is *canonical*, and scores 3, while a 2025
survey that merely restates it scores 1. Recency only earns points where the question is
explicitly time-bounded (Q3's 2017–2026 competitor search, Q5's 2019–2026 venue window).

**Selection rule applied:** every atomic item must hold ≥3 candidate URLs before any
low-utility URL from a well-covered item enters the queue. Q2's three primary sources are
the exception in the other direction — they are must-fetch regardless of score, because
the manuscript's equation (4) cannot be confirmed or refuted from anything else.

## Tier 1 — must-fetch primary sources (period-pinned, Lens D)

These are not scored competitively. They are the documents the sourcing rule requires.
A secondary description of any of them is worthless for the task: Q2 asks for the *exact
stated formula with its equation reference*, which exists only in the full text.

| URL | Batch | Auth | Nov | Stance | Cov | Redun | Fresh | Total | Why must-fetch |
|---|---|---|---|---|---|---|---|---|---|
| arxiv.org/abs/1812.06119 (Schueth, AIF 69) | 1 | 3 | 3 | 1 | 3 | 3 | 3 | **16** | Sole source for Remark 4.2; also computes the t² cone coefficient |
| arxiv.org/abs/0805.3148 (DGGW, Michigan MJ 56) | 2 | 3 | 3 | 1 | 3 | 3 | 3 | **16** | §5.6 is the attributed origin of eq. (4); b₀ convention lives here |
| arxiv.org/abs/1711.03405 (Uçar thesis) | 3 | 3 | 3 | 2 | 3 | 3 | 3 | **17** | Serves BOTH Q2 (general-ℓ p_ℓ) and Q3 (multiset determinacy) |
| arxiv.org/abs/1705.01412 (Bari–Hunsicker) | 4 | 3 | 3 | 3 | 3 | 3 | 2 | **17** | Designated closest competitor; abstract already suggests it is a *negative* result |
| arxiv.org/abs/1103.4372 (Doyle–Rossetti) | 5 | 3 | 3 | 2 | 3 | 3 | 2 | **16** | Not cited in the manuscript; may pre-empt the qualitative attribution to Uçar |
| arxiv.org/abs/2511.22255 (Schueth, AGAG 69) | 5 | 3 | 2 | 1 | 2 | 3 | 3 | **14** | Manuscript cites it as a preprint; it is published — bibliography correction |

## Tier 2 — high-utility supporting sources

| URL | Batch | Auth | Nov | Stance | Cov | Redun | Fresh | Total |
|---|---|---|---|---|---|---|---|---|
| arxiv.org/abs/1701.01874 (Suleymanova) | 5 | 3 | 2 | 1 | 2 | 2 | 2 | 12 |
| arxiv.org/abs/1905.00259 (Nursultanov–Rowlett–Sher) | 5 | 3 | 2 | 1 | 2 | 2 | 3 | 13 |
| arxiv.org/abs/2512.04422 (Looi–Sher) | 5 | 3 | 3 | 1 | 2 | 3 | 3 | 15 |
| arxiv.org/abs/1910.03224 (Richardson–Stanhope) | 6 | 3 | 2 | 2 | 2 | 2 | 2 | 13 |
| arxiv.org/abs/2311.00337 (Gittins et al.) | 6 | 3 | 2 | 2 | 2 | 2 | 3 | 14 |
| arxiv.org/abs/2305.10950 (hyperbolic/spherical survey) | 6 | 2 | 3 | 3 | 3 | 2 | 3 | 16 |
| arxiv.org/abs/math/0504571 (Dryden–Strohmaier) | 6 | 3 | 1 | 1 | 2 | 2 | 1 | 10 |
| arxiv.org/abs/0811.0797 (Proctor–Stanhope) | 6 | 3 | 2 | 2 | 3 | 2 | 1 | 13 |
| arxiv.org/abs/1905.06151 (ternary Egyptian fractions) | 7 | 3 | 3 | 1 | 3 | 3 | 2 | 15 |
| arxiv.org/abs/1706.01008 (Egyptian fractions, prime power divisors) | 7 | 3 | 2 | 1 | 3 | 2 | 2 | 13 |
| ics.uci.edu/~eppstein/numth/egypt/ (Eppstein) | 7 | 2 | 3 | 2 | 3 | 3 | 1 | 14 |
| arxiv.org/abs/1204.2071 (census-taker problem) | 8 | 2 | 3 | 3 | 3 | 3 | 1 | 15 |
| link.springer.com/book/10.1007/978-0-387-26677-0 (Guy, UPINT) | 8 | 3 | 3 | 1 | 3 | 3 | 1 | 14 |
| arxiv.org/abs/1504.02118 (Pan, Vandermonde) | 9 | 3 | 3 | 2 | 3 | 3 | 2 | 16 |
| link.springer.com/article/10.1007/BF01398878 (Gautschi) | 9 | 3 | 2 | 1 | 3 | 2 | 3 | 14 |
| epubs.siam.org/doi/10.1137/060652737 (Vandermonde lower bounds) | 9 | 3 | 2 | 1 | 3 | 2 | 2 | 13 |
| arxiv.org/abs/1701.02538 (Vandermonde, unit disk / large sieve) | 9 | 3 | 2 | 1 | 2 | 2 | 2 | 12 |

## Tier 3 — search-driven batches (no fixed seed list)

Batches 6, 7, 9 and 10 carry a bounded search allowance inside a disjoint topic. Batch 10
(inverse-spectral stability) is entirely search-driven: the whole point of that batch is
to determine whether the genre exists at all for orbifolds, and a seed list would
pre-judge the answer. Its brief therefore requires it to log every query it runs, so a
null result is *documented* rather than merely asserted — an undocumented null is not
admissible evidence for the Q4 novelty verdict.

## Q5 handled by the orchestrator, not a fetcher

The venue question was resolved directly against the Crossref REST API filtered to the
JGA ISSN (`1050-6926`). This is deliberately not delegated: Q5's deliverable is
*title + DOI + one line*, and the Crossref record is the authoritative source for DOIs,
so routing it through a fetcher would add a paraphrase layer between the DOI and the
deliverable for no benefit. Results in `research/temp/jga-venue-set.md`.

## Deliberate exclusions

- **Wikipedia** (`Optic equation`, `List of sums of reciprocals`) surfaced in the Q1
  breadth search. Treated as a source hub only — its references are worth chasing, the
  article itself is never cited.
- **ResearchGate mirrors** of Doyle–Rossetti and Dryden–Strohmaier: excluded in favour of
  arXiv and the publisher of record, which give citable DOIs.
- **MathSciNet**: named in the prompt as a permitted venue, but it is subscription-gated.
  Not queued. If a citation cannot be resolved any other way, that becomes an
  `outstanding-fetches.md` entry rather than an approximation.
- **huggingface.co dataset hit** in the Q1 breadth search: search-engine noise, dropped.
