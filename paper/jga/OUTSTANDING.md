# OUTSTANDING: placeholders, open items and instrument gaps

Everything the authors must still supply or decide before submission, everything this session
could not retrieve, and every place where the manuscript states less than a source file does.

## 1. AI-use statement (decision for the authors)

The manuscript contains a clearly marked placeholder and no statement. The authors decide the
content.

**Location of the placeholder.** Appendix B, "Computational methods and reproducibility",
paragraph "Use of AI tools" (Appendix C before the 30-35 page revision). The journal's guidelines (quoted below) ask for use of an LLM to be
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
| Author contributions | Statements and Declarations, "Author contributions" | the authors' contribution statement (free text or CRediT) |
| AI-use statement | Appendix B, "Use of AI tools" | see section 1 |
| Zenodo DOI | Statements and Declarations, "Data and code availability"; Appendix B | mint the archive at submission and insert the DOI in both places |

## 3. Library sources (brief: refs/manual/)

`refs/manual/` does not exist in this working tree, so none of Hejhal LNM 548 Ch. 3, Iwaniec
Ch. 10, McKean 1972/1974, Buser, Steinig, Drury-Marshall, Donnelly 1976, Watson 2005 or Wolpert 1979
was read in this session. Consequences, as the brief prescribes for this case:

- Lemma 2.5 (the heat function is admissible) is kept self-contained; the bracketed replacement
  sentence of `theory/revision/locality.tex` was **not** used.
- Citations are limited to what was verified: DS eq. (1) is cited as DS state it, taken from Hejhal
  and Iwaniec (read in DS); the heat-kernel form is cited to Garbin-Jorgenson Rem. 2.7, (2.8) (read
  in the literature pass); McKean, Buser and Wolpert are cited without pinpoints; Steinig is cited
  for "n distinct positive reals" via Laurens; Watson only for the credit Ucar gives (pp. 134, 144).
- The pinpoints of `review/literature-pass/GAPS.md` section 4 and of
  `theory/revision/locality-sources.md` ("Open (needs library access)") remain open: Hejhal Ch. 3,
  Thm 5.1 hypothesis wording; Iwaniec Thm 10.2 for cocompact groups; Buser Lemma 6.6.4 numbering;
  McKean 1972 section; Steinig's scope; Korobov-Bugaevskaya s. 3 / Thm 3.1; published numbering of
  the arXiv-read items; the NGSolve ASC report.

## 4. Unresolved G7 items (details in G7-CHANGES.md)

- **G7-5 (closed 2026-10-10).** The double-window recomputation of the four spectra was run
  (`numerics/data/double_window/`, `numerics/data/rerun_double_window_comparison.json`): counts agree,
  largest relative difference 1.4e-14. Both papers say so; completeness is still supported, not proved.
- **G7-14.** The repository is `github.com/Ali-M658/Arithmetic-verification`, an account that
  matches none of the six authors. Declarations are unchanged by instruction; the authors must move
  the repository or state the account holder's relation, add a licence, and mint the Zenodo DOI.
- **G7-31.** No notation table (no room at 35 pp.); T still denotes the tanh series and T_L, and
  locally abs(Z) in two proofs.
- **G7-32.** F5(a) has tick marks but no tick labels on its own t axis (the axis is shared with (b),
  as the caption now says), and F7 has no in-figure p labels. `figures/src/F5.py` and `F7.py` are
  outside this session's write scope.

## 5. Figure choice at 35 pages

The paper carries F3, F4, F7, F8 and F5 (five of the six recommended). F1 moved to the supplement
(Fig. S1) to meet the 35-page limit; F6 is in the supplement (Fig. S2); F2 is not used; F9 belongs
to the companion note. F4 was rebuilt through `figures/src/F4.py` (new data source
`theory/pte/data/witnesses.json`, read only; new sqrt step curve; height 56 mm; all assertions pass),
which changes `figures/out/F4.pdf` and `F4.png`; `DATA-MANIFEST.md` is to be regenerated by the
close-out session. F1 and F6 were not re-rendered.

## 6. Instrument gaps (standing)

As recorded in `review/literature-pass/GAPS.md` and `review/outstanding-fetches.md`. In this
session the bibliography records were re-fetched (Crossref/DataCite content negotiation, arXiv API,
zbMATH Open API; no contact parameter was sent); the PARI release date is taken from the fetched
release announcement (5 March 2025), not the changelog (1 March), as `CITATIONS.md` section 4 asks.

## 7. Decisions for the authors

- **Preprints in the reference list.** Doyle-Rossetti (arXiv:1103.4372v2), Dryden 2004
  (arXiv:math/0411290), Chen's survey (arXiv:2506.11429) and Croot-Mao-Yip (arXiv:2609.05061) are
  unpublished; the JGA guidelines ask for published or accepted works only. Ucar's thesis has a DOI.
  The companion manuscript is cited as in preparation.
- **ORCID iDs** are printed as a title-page note (the class's `\orcid` macro needs a logo file).
- **"Corresponding author(s). E-mail(s):"** is printed by the sn-jnl class itself.
- **Line numbers** come from the `lineno` package (the class option `lineno` needs `vruler.sty`,
  which this TeX installation lacks); remove `\linenumbers` for the final version if wanted.
- **MSC.** 58J53 (primary); 58J50, 35K08, 57R18, 30F35, 11D72, 11G05. 11D72 covers the
  Prouhet-Tarry-Escott systems of Section 3.3 and 11G05 the descent of Theorem 5.10.

## 8. Places where the manuscript states less than a source

- The pencil construction is used only for m = 4 (Remark 3.2); the general pencil theorem,
  Proposition 2.3 (symmetric constructions are balanced), N_odd, tau_L and T^cone_L of
  `theory/pte/proof.md` are not stated.
- Theorem 4.4 no longer contains the a-posteriori bound (c) of the old Theorem 4.9; the supplement
  says only that (b) holds and is loose.
- Proposition 5.8 keeps only part (1) (tangency at p = 2, 4); part (2) (first collision strictly
  after the first overlap for p not in {2, 4}) is dropped for space; Table S3 shows the data.
- The divergence remark (old Remark 2.12, `theory/revision/remark212.tex`) is not in the paper; Section 7
  quotes only the growth rate of the cone coefficients with its reason.
- Philippe 2010 (Geom. Dedicata) and the a-posteriori bound of old Theorem 4.9(c) were dropped for the
  page limit; Philippe 2008 Thm A is cited.

## 9. After referee round 2 (retarget to AGAG, 2026-10-07)

- The target journal is now Annals of Global Analysis and Geometry. Section 1 above quotes the JGA
  guidelines; the AGAG paragraph on LLMs is word for word the same (AGAG.md §8a), so the placeholder
  location is unchanged. AGAG.md lists everything else.
- **Slot.** Section 4 of `manuscript.tex` ("From heat invariants to eigenvalues", `sec:eigen`) and the
  last clause of the abstract and one sentence of §1.1 are placeholders for the theorem being proved
  in a parallel session.
- **Generator fixes outside this session's scope** (`review/round1-fixes/d2_explicit_pairs.py`):
  add "(A′ and B′ exchanged when R(U_0) < R(V_0))" to the Table S1 caption, and print the exact
  exponent of tiny area deficits in `fmt_area` (the L = 6 Prouhet row is 1023 − 9.14×10^−864).
  The supplement states both corrections next to the table until then.
- **Companion note.** It cites the paper (Theorem 6.8) for the isolation; posting it to arXiv would let
  the paper cite it in the reference list (AGAG allows only published/accepted works there).
- Acknowledgements on the title page (AGAG wording) and the arXiv preprints in the list: authors' call.
