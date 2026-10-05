# OUTSTANDING: placeholders, open items and instrument gaps

Everything the authors must still supply or decide before submission, everything this session
could not retrieve, and every place where the manuscript states less than a source file does.

## 1. AI-use statement (decision for the authors)

The manuscript contains a clearly marked placeholder and no statement. The authors decide the
content.

**Location of the placeholder.** Appendix C, "Computational methods and reproducibility",
paragraph "Use of AI tools". The journal's guidelines (quoted below) ask for use of an LLM to be
documented "in the Methods section (and if a Methods section is not available, in a suitable
alternative part) of the manuscript". The manuscript has no section called Methods; Appendix C,
which describes how every computation was done, is the closest equivalent and was chosen as the
"suitable alternative part". If the authors prefer, the statement can instead go into the
"Statements and Declarations" section; the Springer Nature policy below speaks of "an AI
Declaration in your manuscript" for visual content.

### 1a. Journal of Geometric Analysis, submission guidelines

Source: https://web.archive.org/web/20251204070959/https://link.springer.com/journal/12220/submission-guidelines
(fetched 2026-10-05; SHA-256 in SOURCES.md), section "Title Page", verbatim:

> Large Language Models (LLMs), such as ChatGPT, do not currently satisfy our authorship criteria. Notably an attribution of authorship carries with it accountability for the work, which cannot be effectively applied to LLMs. Use of an LLM should be properly documented in the Methods section (and if a Methods section is not available, in a suitable alternative part) of the manuscript. The use of an LLM (or other AI-tool) for "AI assisted copy editing" purposes does not need to be declared. In this context, we define the term "AI assisted copy editing" as AI-assisted improvements to human-generated texts for readability and style, and to ensure that the texts are free of errors in grammar, spelling, punctuation and tone. These AI-assisted improvements may include wording and formatting changes to the texts, but do not include generative editorial work and autonomous content creation. In all cases, there must be human accountability for the final version of the text and agreement from the authors that the edits reflect their original work.

### 1b. Springer Nature, "AI use in manuscript preparation"

Source: https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation
(fetched 2026-10-05). Verbatim extracts (the page also has a three-level risk table, green /
amber / red, reproduced in substance in 1c):

> Using AI safely when preparing your manuscript
> Artificial intelligence (AI) tools are increasingly used to support manuscript preparation, from improving clarity and structure to assisting with drafting and summarisation. These uses can enhance communication and accessibility, but they vary in the level of influence they have on the scholarly content.
> Springer Nature applies a risk-assessment approach, focusing on how AI is used, rather than whether it is used.
> A risk-assessment framework for AI use in writing
>
> What this means in practice
> Many uses of AI in writing are low risk and widely accepted, for example, improving grammar, clarity, or structure. These uses are surface-level, reversible, and remain fully under author control.
> More extensive uses, such as drafting or restructuring content, require greater care. Authors should ensure that:
> all content is accurate and verified
> disciplinary conventions are correctly applied
> references are real and have been checked
> the intellectual contribution remains their own
> AI can assist with expression, but the argument, interpretation, and conclusions must be author-led.
>
> Transparency and declaration
> Some authors may hesitate to disclose AI use due to concerns about how it might be perceived. However, the policy is designed to support openness and consistency.
> Declaration does not negatively influence editorial decisions
> It enables transparent and fair evaluation
> It reduces the need for clarification during editorial assessment
> Where AI use is not declared, editors may need to investigate or request clarification, which can delay the review process and shift attention away from the manuscript’s contribution.
> Declaring AI use helps ensure that your work is assessed on its scholarly merit.
> Transparency and disclosure for visual content
> Visual content that has been created, substantially modified or enhanced using AI should be disclosed clearly and transparently.
> Where AI-generated or AI-assisted visual content is published, information about the AI system used, the purpose of its use, and the extent of its contribution should be provided in an AI Declaration in your manuscript.
> Specific disclosure should be provided within the caption or legend of the visual content.
> Key principle
> AI is safe when it helps you communicate your research. It becomes unsafe without adequate human oversight and accountability.
> You remain fully accountable for everything submitted in your name.

### 1c. Springer journal policies, section "Artificial intelligence (AI)"

Source: Internet Archive capture of https://link.springer.com/brands/springer/journal-policies
(https://web.archive.org/web/20260919214816/https://link.springer.com/brands/springer/journal-policies?),
fetched 2026-10-05. Verbatim, opening of the section:

> Artificial intelligence (AI)
> A risk‑assessment framework for responsible AI use in research publishing
> Springer Nature supports the responsible and transparent use of artificial intelligence where it strengthens research quality, upholds editorial independence, and preserves the integrity of the scientific and scholarly record.
> These policies set out a risk‑assessment framework governing how AI may be used across the research and publishing lifecycle, applied consistently to authors, peer reviewers, and editors, while recognising their distinct roles and responsibilities.
> AI is treated as a supporting technology. Scholarly judgement, accountability, and responsibility always remain human.
> Core expectations
> Across all editorial roles and activities:
> Human accountability is non‑transferable
> Accountability for scholarly content, evaluation, and editorial decisions cannot be delegated to AI systems.
> AI may support, but must not replace, scholarly judgement
> AI can assist clarity, efficiency, and exploration, but must not determine conclusions, evaluations, or decisions.
> Transparency creates trust and confidence
> Transparent declaration of AI builds trust and confidence, and removes ambiguity about how AI might have been used.
> Confidentiality and data protection are mandatory
> Manuscripts, peer review reports, and sensitive data must not be shared with unsecured or public AI systems.
> Risk‑assessment framework for AI use and declaration
> In support of the policy, the following framework provides guidance on how to use AI safely. Use of AI is governed according to risk level, not by tool type. The same framework applies across all roles: authors, reviewers and editors.

## 2. Placeholders left in the manuscript

| placeholder | where | what is needed |
|---|---|---|
| Author contributions | Statements and Declarations, "Author contributions" | the authors' contribution statement (the guidelines suggest free text or CRediT) |
| AI-use statement | Appendix C, "Use of AI tools" | see section 1 |
| Zenodo DOI | Statements and Declarations, "Data and code availability"; Appendix C, "Repository" | mint the archive at submission and insert the DOI in both places |

## 3. Figures

Resolved at integration (branch s11b-integrate; details in `INTEGRATION.md`). The manuscript
reads `figures/captions.tex` as the figure session wrote it (`\figcapOne` ... `\figcapNine`) and
attaches the macros to F1-F9 with `\setfigcap`; each figure is included at its drawn width of
119 mm, near its first mention, and is referenced in the text. No placeholder box or TODO-CAPTION
marker remains. At submission, when the template's single `.tex` file is required, paste the
nine caption macros into the preamble in place of the `\input`.

## 4. Instrument gaps

Accepted and standing (`review/outstanding-fetches.md`): Steinig 1971 (cited through Laurens,
as THEOREM-A-PRIOR-ART.md prescribes), Drury-Marshall 1987 (not cited), Donnelly 1976 (cited for
the structure, which is quoted from DGGW Section 4.1), Watson 2005 (not cited), Shioda-Tate (the
Mordell-Weil rank remark is omitted; nothing uses it).

New in this session:

- `link.springer.com` returned a JavaScript challenge to headless requests; the Springer
  journal policy was read from an Internet Archive capture instead.
- `zbmath.org/bibtex/...` returned a Cloudflare challenge; zbMATH records were taken from the
  zbMATH Open API (`api.zbmath.org`).
- The Shams-Stanhope-Webb paper (Arch. Math. 87 (2006)) was not retrieved: Crossref carries no
  abstract and no arXiv version was found. The manuscript uses only its title-level claim
  ("one cannot hear orbifold isotropy type"), together with the fact, from Dryden-Strohmaier
  Thm 1.1, that no closed orientable hyperbolic 2-orbifold can be such an example.
- Guy, Unsolved Problems in Number Theory, section D16: text unretrieved (as logged in
  `review/outstanding-fetches.md` 1.4); Guy is therefore not cited, and the equal-sum,
  equal-product problem is credited to Schinzel's paper, which was read.
- The published FoCM version of Mueller et al. is closed access; it is cited from its Crossref
  record for a negative statement only.
- MSC: the JGA guidelines (as captured) do not require MSC codes; codes are given anyway, each
  checked against the fetched MSC 2020 list.

## 5. Open items in the repository that the manuscript reports as such

- The recomputation of the four S3 spectra with the double-window eigensolver has not been run
  (`CONSOLIDATION.md`, T3). Section 7.1 says so and gives the two checks that exclude a missing
  eigenvalue in the committed data.
- Resolved at integration: `theory/stability/threshold_output.md` was regenerated by
  `threshold.py` (with the audit's epigraph search added to its failure construction) and prints
  the corrected (2,2,2,2,3) upper bound 5.312e-05; the table is now generated from
  `threshold_results.json` alone (`INTEGRATION.md`).
- The rank stage of `code/run_all.sh` is skipped on machines without PARI/cypari2; the ranks
  quoted are those recorded in `theory/diophantine/data/ranks.txt` and confirmed by the audit's
  independent 2-isogeny descent.

## 6. Places where the manuscript states less than a source

- **Register row 94** ("any other pair on the same curve differs by a point of infinite
  order"). The source has no proof, and the audit's suggested lemma (positive torsion points
  are isosceles or geometric progressions, and their torsion cosets consist of permutations of
  the point and its dual) is only sketched. The manuscript proves the statement when the
  torsion of C_Lambda(Q) is the cyclic group of base points (for example every integer
  Lambda != 10, by Bremner-Guy-Nowakowski), and states the general case only as the exact
  computation for S <= 600 (1330 non-dual primitive pairs, none differing by a point of order
  at most 12, hence by Mazur all of infinite order). A complete proof needs the classification
  of rational torsion on C_Lambda for rational Lambda.
- **Register row 50, Theorem N(b).** Proved with the audit's doubling construction (which gives
  the 23 vs 24 witness) rather than the source's Egyptian-fraction route; the statement is
  unchanged.
- **Register rows 83, 86 and 82** (invariant multiplicities; flat cone surfaces that are not
  orbifolds; the Kokotov input) are remark-level and are omitted.
- **Register row 28** (eq:moduli) is superseded by Proposition 4.2, as its register note says.

## 7. Decisions for the authors

- **Preprints in the reference list.** The JGA guidelines say the reference list "should only
  include works that are cited in the text and that have been published or accepted for
  publication". Two cited works are not published: Doyle-Rossetti (arXiv:1103.4372, cited for
  Theorem 1 and the quotation in Section 1.1) and Ucar's thesis (a dissertation, published by
  Humboldt-Universitat, DOI 10.18452/18463, so it should qualify). The authors should decide
  whether Doyle-Rossetti stays in the list or moves to the text. Checked at integration
  (`INTEGRATION.md`): arXiv:1103.4372 has no journal reference, no Crossref record and is listed
  by zbMATH as a preprint. The New York J. Math. 14 (2008) 193-204 paper cited by the legacy
  draft is a different work ("Isospectral hyperbolic surfaces have matching geodesics") and does
  not contain Theorem 1 or the quoted sentence.
- **K_iso versus K_mult** (DEFECTS MAJ-03). The manuscript uses both, each with its comparison
  class; the triangle-orbifold theorems are stated for K_iso, equal to K_mult there.
- **ORCID iDs.** The class's `\orcid` macro needs a logo file the template does not ship, so the
  six iDs are printed as a title-page note. The submission system will also ask for them.
- **Title-page acknowledgements.** The guidelines ask for acknowledgements "in a separate section
  on the title page"; the template puts them in the back matter, where they are now.

## 8. `code/run_all.sh --quick` after this session

Run with `PYTHON=` the miniforge interpreter (the default `python3` lacks the pinned packages):
33 passed, 1 failed, 8 skipped, total 49:30 (machine under load). The 8 skips are those of the
consolidation record (full-mode stages, PARI not installed, the deferred S3 rerun record).

The one failure is `theory conventions-check`, in `check_free_symbols` of
`theory/conventions_check.py`. That check asserts that the replacement symbols CONVENTIONS.md
introduces for the paper (`d_j`, `varsigma`, `varpi`, `varkappa`, `vartheta`, `mathfrak D`,
`Hyp`, ...) occur in no text file of the working tree outside CONVENTIONS.md, so that the paper
could adopt them. The manuscript now does adopt them, and the check finds them in
`paper/jga/manuscript.tex`, `TRACE.md` and `OUTSTANDING.md`. The same stage passes on an
untouched export of the starting commit 09638ff (14 symbols free across 388 files, 45 checks
passed). Everything else in the stage (the 45 translation checks) passes. The fix is outside
this session's write scope: add `"jga"` to `skip_dirs` in `check_free_symbols` (the manuscript is
where the symbols are meant to be used). The symbols were not disguised to pass the check.
Resolved at integration: `"jga"` was added to `skip_dirs`, and the stage passes (`INTEGRATION.md`).

An earlier run in this session also reported `audibility verify_elimination` as failed (exit 97):
the committed-file guard saw paper/jga files that were being committed during that stage and
restored them. The stage's own assertions passed, and in the clean rerun above it passes.
