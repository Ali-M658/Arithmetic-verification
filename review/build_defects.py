#!/usr/bin/env python3
"""Generate review/DEFECTS.md from the row table below.

The rows are the single source of truth; the counts at the end of the generated
file are computed from them, never typed. Run from the repository root:

    python3 review/build_defects.py

Source codes used in the Sources column
  CL  review/claim-ledger.md        (row ids AB-, IN-, ..., AP-, section C-1..C-6, F)
  SH  review/source-hygiene.md      (section numbers; "7.n" = item n of its summary list)
  VD  review/hyperresearch/VERDICT.md  ("#n" = row n of its corrections table, "§n" = answer n)
  CN  review/convention-note.md
  RR  review/reproducibility-report.md  (section numbers)
  P2  review/P2.md                  (sections 9 and 10; 10.x are the open questions)
  TV  review/takeuchi-verdict.md
  OF  review/outstanding-fetches.md
  BR  the brief of this session (items K1-K7 of its known list)
"""
from collections import Counter, OrderedDict
from pathlib import Path

OUT = Path(__file__).resolve().parent / "DEFECTS.md"

SEV = ["FATAL", "MAJOR", "MINOR", "COPY"]
SESSIONS = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S10", "S11", "S14"]

# id, severity, defect, main.tex lines, sources, status, closer (if CLOSED), owner, also
ROWS = [
    # ------------------------------------------------------------------ FATAL
    dict(id="FAT-01", sev="FATAL",
         text="K(F) is defined up to isometry (\"distinguish F from every other hyperbolic triangular pillow\") and is infinite for n >= 4: a sphere with n cone points of fixed orders has moduli of real dimension 2n-6 (0 at n = 3, 2 at n = 4), and every heat coefficient depends only on the cone orders, so a whole family of non-isometric pillows shares all coefficients. Remark 5.6 (compiled number 5.1, label rem:ncone), \"the upper bound K <= n extends the n = 3 case of Theorem C\", is false as stated for n >= 4. n = 3 survives by rigidity.",
         loc="103, 160, 493-495", src="VD #18, VD closing section, P2 §9, P2 §10.1, BR K3",
         status="OPEN", closer="", owner="S11", also="",
         note="Restated remark and the affected sentences: theory/definitions.tex, theory/definitions-impact.md. The infinity half depends on the locality theorem (S5). The infinity half is now proved: theory/locality/proof.md Corollary 2.3 (K_iso = infinity for every hyperbolic signature with n >= 4), commits 067fdc8 and 3506456, with the exact checks in theory/locality/check_locality.py; K_mult <= n for all n is theory/audibility/proof.md Theorem A (550491f). What remains is the text of Remark 5.6, definition and Theorem C, which only S11 can change."),
    dict(id="FAT-02", sev="FATAL",
         text="The abstract states N(S)/S^2 -> c with c ~ 0.0085-0.0093, but Table 1 (tab:density) prints 0.0097 at S = 200 and 0.0094 at S = 400. The true range at the printed checkpoints 100 <= S <= 600 is 0.0085-0.0097 (full sweep: max 0.00979 at S = 196, min 0.00851 at S = 599). The ratio is falling at the top of the range, so the text at L461 (\"stabilizes to within about 10% of 0.009\") also overstates.",
         loc="58, 461", src="VD #22, BR K1, CL DE-21",
         status="OPEN", closer="", owner="S11", also="S10 (figure, MIN-22)",
         note="\"Decreasing\" in VD #22 is a trend, not monotone: the checkpoints rise from 0.0093 (S = 300) to 0.0094 (S = 400). Least-squares slope on 200 <= S <= 600 is -1.75e-6; last 100-block mean 0.00868 vs 0.0091-0.0093 before. Verified by review/defects-check.py. The Diophantine session revises the growth statement: Conjecture 5.3 (N(S) ~ c S^2) is contradicted by the data, and the supported statement is the conjecture N(S) = S^(1+o(1)), refined empirically to N(S) = S (log S)^(kappa+o(1)) with kappa = 4.5 +/- 0.5 on 600 <= S <= 4800 (per-S and cumulative fits agree; proven floor kappa >= 2). An earlier figure of kappa about 5.3 came from a fit that absorbed a secondary term and is superseded. See theory/diophantine/RECOMMENDATION.md (Verdict and section 1.2) and data/exponent_fits.txt, data/growth_fits.txt, data/per_S.csv. The abstract's constant and the sentence at L461 must be rewritten around that statement, not merely re-rounded."),
    dict(id="FAT-03", sev="FATAL",
         text="Five places state that verification scripts, generated data and the generating script are in the public repository https://github.com/Ali-M658/Arithmetic-verification (abstract, §5.2, Appendix A, Data availability, Code availability). The remote still holds the non-functional upstream scripts; the working harness exists only in this repository. The claims are false as printed until the remote is updated.",
         loc="58, 440, 502, 624, 627", src="CL AB-12, AP-01, AP-10, AP-13, AP-18, AP-19, DE-13, CL §F.1; RR §3, §4.1",
         status="OPEN", closer="", owner="S14", also="",
         note="Plan: review/remote-remediation.md. AB-12, AP-01 and AP-10 are true of code/ and false of the cited URL."),
    dict(id="FAT-04", sev="FATAL",
         text="At the time of the audit nothing in the cited repository verified any claim of the paper: zero assert statements; enumerate_degeneracies.py keyed on the wrong invariant and fell back to hard-coded fabricated rows; advanced_pillow_verification.py printed \"all checks passed\" unconditionally and used area = pi(1-R) (factor 2 against eq:area); generate_latex_supplementary_table.py did not produce the density table; run_all.py failed on import; nothing regenerated the S <= 600 enumeration.",
         loc="502 (AP-11, AP-12, AP-13)", src="CL C-1..C-6, AP-10, AP-11, AP-12, AP-13, DE-12; RR §1, §3, §6",
         status="CLOSED", closer="code/ via c310d53, 0c2775c, 8ef300f, ab3641d, 1b0df98, bbc49dd, ce1cb19 (code/run_all.sh)", owner="S2", also="",
         note="Substance only: 150 of 172 ledger rows now have a backing script, 0 unexplained gaps (RR §1). Publication of this code is FAT-03."),
    # ------------------------------------------------------------------ MAJOR
    dict(id="MAJ-01", sev="MAJOR",
         text="N(S) is defined as the number of \"two-coefficient degeneracies\" at sum S but the manuscript never says whether a degeneracy is an unordered pair of triples or a signature class. The table follows the pair convention (a signature shared by k triples contributes C(k,2)). The two first differ at S = 136, where R = 1/10 is shared by O(15,55,66), O(16,40,80), O(17,34,85) (166 classes vs 168 pairs); by S = 600 they differ by 90 (2977 vs 3067). Fibres of size 3 first appear at S = 136.",
         loc="404-409, 440, 450-456", src="CL DE-02, DE-14..DE-20, CN, RR §4.2, BR K2",
         status="OPEN", closer="", owner="S11", also="",
         note="No number changes. Theorem 5.2 holds under both conventions; OLS exponent 2.028 (pairs) vs 2.015 (classes). Drop-in clause in CN. Both counts, per sum S up to 4800, are in theory/diophantine/data/per_S.csv (columns pairs, classes, cum_pairs, cum_classes)."),
    dict(id="MAJ-02", sev="MAJOR",
         text="The n-cone extension is asserted, not proved: \"when these [the n symmetric functions] are independent they recover the multiset\". Injectivity of (R, S1, P3, ..., P_{2n-3}) on n-element multisets is open for n >= 4; the only evidence is a bounded scan. The planned route is the Prony/Vandermonde identification in squared orders.",
         loc="493-495", src="CL DE-31, VD §3, VD §5, RR §4.4",
         status="CLOSED", closer="theory/audibility/proof.md Theorem A, injectivity of (R, P1, P3, ..., P_{2n-3}) on multisets for every n (550491f, b2dbda2; checks in theory/audibility/)", owner="S1", also="S11 (text of Remark 5.6, with FAT-01)",
         note="Cone coefficients themselves are not the gap (see MIN-08, MIN-09)."),
    dict(id="MAJ-03", sev="MAJOR",
         text="The definition of K is a choice that has not been made consciously: K as least number determining the isometry class (current text) versus least number determining the cone-order multiset. The second makes Theorem C and the n-cone remark uniform at the cost of a weaker-sounding statement at n = 3 (equivalent there by rigidity).",
         loc="103, 114", src="P2 §10.1",
         status="OPEN", closer="", owner="S11", also="",
         note="Candidate definitions K_iso, K_mult and the rigidity statement are drafted in theory/definitions.tex; the choice between them is the author's. Both candidates now have a theorem behind them (K_mult <= n for all n, theory/audibility; K_iso = infinity for n >= 4, theory/locality); the choice is the author's and is made in the rewrite."),
    dict(id="MAJ-04", sev="MAJOR",
         text="Nobody had written the restated Remark 5.6 and Theorem C and checked that the surrounding text still reads correctly; \"the fix is small\" was an estimate.",
         loc="114, 160, 357, 373, 493-495", src="P2 §10.1, P2 §10.6.1",
         status="CLOSED", closer="08ca642 (theory/definitions.tex, theory/definitions-impact.md)", owner="S2", also="",
         note="Result: 8 sentences must change, 14 more depend on the new definitions. The edit itself belongs to S11."),
    dict(id="MAJ-05", sev="MAJOR",
         text="The stability recommendation lacks its front end. Errors in the heat coefficients are amplified by 12, 360 and 2520 (the leading coefficients 1/12, 1/360, 1/2520 of the cone terms) on the way to (S1, R, P3, P5), and then by the O(S1^2) Newton step; the planned theorem never converts a heat-coefficient error into a (S1, R, P3) error. Critic finding T12 was raised and not applied.",
         loc="487 (the stability paragraph); recommendation in review/hyperresearch/Q4-stability.md", src="P2 §10.2, P2 §10.6.3, BR K4, VD §5",
         status="CLOSED", closer="theory/stability/front_end.py and proof.md: Lipschitz front end, amplification constants and the Hurwitz factorisation (84b037d, 5047f2b, ffa071d)", owner="S6", also="S11 (one paragraph)",
         note="Two lines of algebra. The factors 12, 360, 2520 are the Bernoulli leading coefficients checked in theory/cone-coefficients/."),
    dict(id="MAJ-06", sev="MAJOR",
         text="The priority sentence \"To our knowledge this is the first exact finite-coefficient determinacy threshold, with an explicit minimal degeneracy, for a family of hyperbolic cone orbifolds\" survives only on four simultaneous qualifiers (exact, finite-coefficient, hyperbolic cone orbifold, minimal), and the novelty searches behind it are negative searches (MathSciNet never queried; Semantic Scholar leg did not run for Q4). Recommended: delete it, state what is proved and quote Doyle-Rossetti that the question was open.",
         loc="146-155 (153)", src="VD #4, VD §1, VD §4, P2 §10.2, P2 §10.4",
         status="OPEN", closer="", owner="S11", also="",
         note="Related: MAJ-08 (Doyle-Rossetti), MIN-04 (Guy D16 / Schinzel)."),
    dict(id="MAJ-07", sev="MAJOR",
         text="§1.3(a) credits Ucar alone for the qualitative statement that the spectrum determines the cone-order multiset. Dryden-Strohmaier (2009, Thm 1.1) gives it exactly for compact orientable hyperbolic orbisurfaces and Doyle-Rossetti (2011) independently; Ucar generalizes Dryden-Strohmaier. The manuscript cites Dryden-Strohmaier but describes it only as \"a Huber theorem relating the Laplace and length spectra\".",
         loc="134, 151", src="VD #9, VD §4",
         status="OPEN", closer="", owner="S11", also="",
         note="Corollary for free: no two non-isometric hyperbolic triangle orbifolds are Laplace isospectral (state as an easy consequence, not as new)."),
    dict(id="MAJ-08", sev="MAJOR",
         text="Doyle-Rossetti (arXiv:1103.4372) is uncited. It is the strongest positive evidence that the finite-coefficient question was open (\"presumably it could be extracted ... by looking at higher and higher terms\"); the manuscript cites only their 2008 paper as \"orthogonal\".",
         loc="134, 155 (bibitem 703)", src="VD #10, VD §4",
         status="OPEN", closer="", owner="S11", also="",
         note=""),
    dict(id="MAJ-09", sev="MAJOR",
         text="Linowitz-Voight (Math. Z. 281 (2015) 523-569, 10.1007/s00209-015-1500-1) is uncited: isospectral non-isometric hyperbolic 2-orbifolds exist in print (minimal area 23 pi/6, signature (0;2,2,2,2,2,3,4), seven cone points), so Theorem C is untouched but a referee will expect the context; the paper also narrates earlier erroneous claims.",
         loc="128", src="VD #11, VD §4",
         status="OPEN", closer="", owner="S11", also="",
         note=""),
    dict(id="MAJ-10", sev="MAJOR",
         text="§2.2's trigonometric identities are proved from scratch and described as classical (\"The computations are classical\") without a citation; DGGW cite Berndt-Yeap, Adv. Appl. Math. 29 (2002) 358-385, 10.1016/S0196-8858(02)00020-9 for the same family, including the sin^-4 evaluation underlying eq. (4).",
         loc="166, 181-193", src="VD #17",
         status="OPEN", closer="", owner="S11", also="",
         note="Not touched by the curvature, threshold or divergence work, which cite Ucar and Dryden-Strohmaier; the Berndt-Yeap citation is a text change."),
    dict(id="MAJ-11", sev="MAJOR",
         text="§1.3 does not reconcile two cited \"one cannot hear\" results with the Ucar-based claim that the full spectrum determines the cone-order multiset: Shams-Stanhope-Webb (2006, cannot hear the isotropy type) and Rossetti-Schueth-Weilandt (2008, isospectral orbifolds with different maximal isotropy orders); the second is by the author of eq. (4).",
         loc="128, 392", src="VD #19",
         status="OPEN", closer="", owner="S11", also="",
         note=""),
    dict(id="MAJ-12", sev="MAJOR",
         text="Bari-Hunsicker is described as analysing \"how few heat coefficients suffice for orbifold lens spaces\"; the review's reading of the cited lemmas (6.5-6.8) is the opposite direction: equal heat expansions for any k in spherical space forms, i.e. non-determination to all orders, not a finite-coefficient count. The manuscript presents it as part of the \"language\" of Theorems B and C.",
         loc="128, 392", src="VD §4 (Bari-Hunsicker paragraph; Q3 §(a)-(b)); not in any account's correction table",
         status="OPEN", closer="", owner="S11", also="",
         note="Found while merging. The reading rests on Q3's verbatim quotation of Lemma 6.5; the primary paper was not re-read for this ledger. Q3 recommends one contrasting sentence."),
    dict(id="MAJ-13", sev="MAJOR",
         text="No \\author, no affiliation, no ORCID, no corresponding address, empty \\date: the manuscript is anonymous. Every journal requires these at submission.",
         loc="48-55", src="SH §3, SH 7.1",
         status="OPEN", closer="", owner="S14", also="",
         note="Compiler: \"No \\author given\"."),
    # ------------------------------------------------------------------ MINOR
    dict(id="MIN-01", sev="MINOR",
         text="Appendix A says \"A single command (run_all) reproduces all checks\"; the file is code/run_all.sh.",
         loc="502", src="CL AP-13, RR §3, BR K5",
         status="OPEN", closer="", owner="S14", also="",
         note="One-word fix; the claim is true of the file, false of the command as printed."),
    dict(id="MIN-02", sev="MINOR",
         text="The footnote attributes the constant-curvature form b_l(C) = kappa^l (1/m) p_l(m), deg p_l = 2l+2 to Ucar as if quoted; Ucar never writes it that way. It is the manuscript's paraphrase of a Bernoulli-number closed form. Cite equations (4.25) p. 134 and (4.33) p. 137.",
         loc="236", src="VD #12, VD §2",
         status="OPEN", closer="", owner="S11", also="",
         note="The paraphrase is correct: p_l = m b_l/kappa^l has degree 2l+2 for l = 0..4 (theory/cone-coefficients/). Equations (4.25) and (4.33) are transcribed in theory/cone-coefficients/ucar-source.md."),
    dict(id="MIN-03", sev="MINOR",
         text="\"A heuristic of the birthday-paradox type standard in analogous Diophantine settings\": no documented precedent in the unit-fraction literature.",
         loc="465", src="VD #13",
         status="OPEN", closer="", owner="S11", also="",
         note="theory/diophantine/RECOMMENDATION.md section on the birthday heuristic: it rests on an O(S^3) miscount and has no precedent; the recommendation is to delete the sentence (data/birthday.csv)."),
    dict(id="MIN-04", sev="MINOR",
         text="Guy, Unsolved Problems in Number Theory, D16 (equal sum and equal product) and Schinzel's elliptic-curve solution are not engaged in §5; the same problem shape for (e1, e3), and the one technique that might improve the floor(S/18) lower bound.",
         loc="399-497", src="VD #20, VD §1",
         status="OPEN", closer="", owner="S11", also="",
         note="An opportunity rather than an error. Engaged in theory/diophantine/novelty.md: the method is Schinzel's, with a verdict on what is new (e6b7bb0)."),
    dict(id="MIN-05", sev="MINOR",
         text="Remark 5.6's open lower bound is settled at n = 4 by the original computation O(3,10,15,30) vs O(4,5,21,28) (same S1 = 58, R = 8/15, P3 = 31402; P5 differs), as a statement about cone-order multisets. The sentence \"we have neither a construction nor a non-existence proof\" is stale against it.",
         loc="494", src="VD #21, VD §3",
         status="OPEN", closer="", owner="S11", also="",
         note="Re-verified in theory/definitions-check.py. The witness is re-verified exactly in theory/audibility (n = 4 sharp: {3,10,15,30} vs {4,5,21,28}); only the stale sentence at L494 remains."),
    dict(id="MIN-06", sev="MINOR",
         text="The n = 5 scan reached only order 26 (118,755 multisets); the n = 4 witness itself needed order 30 and a doubled n = 5 witness would sit past 52. It is too small to support either reading and must not be cited as evidence; push to order >= 60.",
         loc="-- (review/hyperresearch/APPENDIX-ncone-computation.md; VD §3 parenthesis)", src="P2 §10.2, P2 §10.6.2",
         status="CLOSED", closer="theory/audibility/sharpness_search.py: no n = 5 integer witness with all orders <= 60 (7,028,847 multisets) or <= 120 (216,071,394 multisets, exhaustive, exact keys); output/sharpness_search_N120.txt (fe6dbb4)", owner="S3", also="S4",
         note="Hours of compute, no new idea."),
    dict(id="MIN-07", sev="MINOR",
         text="APPENDIX-ncone-computation.md still carries the discharged b_2 -> P_5 caveat and omits the moduli issue (finding D11 was not applied); Q2 still routes the author to that caveat.",
         loc="-- (review/hyperresearch/APPENDIX-ncone-computation.md)", src="P2 §9.2, P2 §9.6",
         status="OPEN", closer="", owner="S14", also="",
         note="Research-record defect, not a manuscript sentence. Not touched by any merged session; it is a defect of the research record (review/hyperresearch/), so it goes with the submission-package clean-up."),
    dict(id="MIN-08", sev="MINOR",
         text="The l = 3 cone row p_3(m) = (3m^8+8m^6+14m^4+32m^2-57)/30240 had a single source (Ucar (4.25), (4.33)) and had never been checked character by character against the thesis text.",
         loc="-- (not in main.tex)", src="P2 §10.3.1, P2 §10.6.4, VD §3",
         status="CLOSED", closer="82e281a (theory/cone-coefficients/)", owner="S2", also="S7",
         note="Row stands: verbatim (4.25) p. 134 / (4.33) p. 137 transcribed from the PDF, recomputed l = 0..4, all asserts pass. No second source exists for l = 3 itself."),
    dict(id="MIN-09", sev="MINOR",
         text="Ucar, the only source for general l, was the one source Q2 did not quote verbatim; the transcription into Q2 had not been checked (critic finding T8).",
         loc="-- (not in main.tex)", src="P2 §10.3.2",
         status="CLOSED", closer="82e281a (theory/cone-coefficients/ucar-source.md)", owner="S2", also="S7",
         note=""),
    dict(id="MIN-10", sev="MINOR",
         text="The convention note's first divergence at S = 136 and the table's pair counts were verified three ways, but all three implementations share one enumeration logic.",
         loc="440-456", src="P2 §10.3.4",
         status="CLOSED", closer="review/defects-check.py (fresh enumerator sharing no code with code/)", owner="S2", also="",
         note="Reproduces the seven checkpoints, S = 136 and the 168 / 166 split. The definition of hyperbolic (R < 1) is the manuscript's own."),
    dict(id="MIN-11", sev="MINOR",
         text="The Q4 negative result (no stability estimate of any modulus for discrete invariants on singular spaces) was narrowed once and will need narrowing again: the Semantic Scholar leg returned HTTP 429 twelve times and never ran, and the queries lack \"Holder\", \"Lipschitz\", \"conditional stability\", \"modulus of continuity\".",
         loc="-- (review/hyperresearch/Q4-stability.md)", src="P2 §10.3.3, P2 §10.4, P2 §10.6.5",
         status="CLOSED", closer="review/literature/stability-inverse-spectral.md and the three companion notes, run with the missing terms (Holder, Lipschitz, conditional stability, modulus of continuity) (06da03e); the Semantic Scholar 429 gap is logged in review/outstanding-fetches.md section 7", owner="S6", also="",
         note=""),
    dict(id="MIN-12", sev="MINOR",
         text="Whether (2,8,8) and (3,3,12) lie in one commensurability class (a possible prior appearance of the pair) was open.",
         loc="-- (VD §1)", src="VD §1, OF §1.2, P2 §11",
         status="CLOSED", closer="70fdc8c (review/takeuchi-verdict.md)", owner="S2", also="S8",
         note="Class III vs class XV; both arithmetic; unequal invariant trace fields (degrees 2 and 4)."),
    dict(id="MIN-13", sev="MINOR",
         text="Takeuchi, Commensurability classes of arithmetic triangle groups (J. Fac. Sci. Univ. Tokyo 24 (1977) 201-212) is still unretrieved; the class partition rests on Tu-Yang's Appendix A, verified to partition Takeuchi's Theorem 3(i) exactly.",
         loc="--", src="OF §1.2, TV §1, P2 §10.4",
         status="OPEN", closer="", owner="S14", also="",
         note="Instrument gap, logged, not an absence."),
    dict(id="MIN-14", sev="MINOR",
         text="The vault note transcribing Takeuchi's Theorem 3 (tier ground_truth, \"verbatim\" in its name) dropped (2,3,16): 75 triples against a self-check that asserted 76 from a remembered figure. A summary field in a second note repeated \"85 compact\".",
         loc="--", src="P2 §10.5, P2 §10.6.6, TV §2, BR",
         status="CLOSED", closer="eb65e9b (research/notes/, review/vault-audit.md)", owner="S2", also="",
         note="Audit tally: 2 verified, 2 corrected, 0 unverifiable. The corrected 76 equal the 76 triples of the Tu-Yang class table (checked as sets in review/defects-check.py)."),
    dict(id="MIN-15", sev="MINOR",
         text="Published versions to cite. bibitem barihunsicker2017: Canad. J. Math. 72 (2020) 281-325, 10.4153/S0008414X19000178.",
         loc="677", src="VD #1",
         status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="MIN-16", sev="MINOR",
         text="bibitem schueth2025 (arXiv:2511.22255): published Ann. Global Anal. Geom. 69 (2026) Paper No. 2, 10.1007/s10455-025-10024-1. Check publication status again at proof stage.",
         loc="690", src="VD #2, SH §5",
         status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="MIN-17", sev="MINOR",
         text="bibitem gomezserrano2020: published J. Differential Equations 275 (2021) 920-938, 10.1016/j.jde.2020.11.002.",
         loc="648", src="VD #3, VD #15",
         status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="MIN-18", sev="MINOR",
         text="bibitem proctorstanhope2009: published Diff. Geom. Appl. 28 (2010) 12-18, 10.1016/j.difgeo.2009.03.015 (keyed and printed 2009, arXiv:0811.0797 is 2008).",
         loc="674", src="VD #4, SH §5",
         status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="MIN-19", sev="MINOR",
         text="bibitem richardsonstanhope2019: published Diff. Geom. Appl. 68 (2020) 101577, 10.1016/j.difgeo.2019.101577.",
         loc="680", src="VD #5",
         status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="MIN-20", sev="MINOR",
         text="DGGW erratum uncited: Michigan Math. J. 66 (2017) 221-222, 10.1307/mmj/1488510034. It corrects only Theorem 5.1, not §5.6, so eq. (4) is unaffected.",
         loc="665", src="VD #6, VD §2",
         status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="MIN-21", sev="MINOR",
         text="bibitem gittinsetal2024: Part 2 is published (Michigan Math. J., 2026, 10.1307/mmj/20236493); Part 1 is uncited (MMJ 74 (2024) no. 3, 571-598, 10.1307/mmj/20216126); key says 2024, printed year 2023, arXiv 2311.00337 is November 2023.",
         loc="683", src="VD #7, SH §5, SH 7.7",
         status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="MIN-22", sev="MINOR",
         text="The density table prints seven checkpoints only, which hides the drift of N(S)/S^2 (peak at S = 196, 0.0085 at S = 600). A full-sweep figure of the ratio would show it; the review recommends stating the downward drift.",
         loc="442-460, 479", src="VD #22",
         status="OPEN", closer="", owner="S10", also="S8",
         note="Companion to FAT-02."),
    dict(id="MIN-23", sev="MINOR",
         text="titlesec and tikz-cd are loaded, unused, and were not installed on the audit machine: they blocked compilation on a basic TeX Live. Remove them.",
         loc="6, 12", src="SH §1, SH 7.5",
         status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="MIN-24", sev="MINOR",
         text="Document class is plain article with hand-rolled geometry, \\doublespacing and theorem environments; a journal class will conflict. Rework the preamble for the target template.",
         loc="1, 22-46", src="SH §1",
         status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="MIN-25", sev="MINOR",
         text="All 28 bibitems lack a DOI; 17 have neither a DOI nor an arXiv id (kac1966, mckeansinger1967, datchevhezari2013, griesermaronna2013, lurowlett2015, hezarizelditch2022, sunada1985, gww1992, donnelly1976, dggw2008, ssw2006, rsw2008, doylerossetti2008, drydenstrohmaier2009, harmer2008, scott1983, buser1992). dggw2008, cited 8 times, is the most important omission.",
         loc="633-721", src="SH §5, SH 7.3",
         status="OPEN", closer="", owner="S14", also="",
         note="doylerossetti2008 has no DOI because New York J. Math. registers none for that era (VD closing section): correct, not a gap."),
    dict(id="MIN-26", sev="MINOR",
         text="main.tex uses a hand-written thebibliography; refs/sources.bib (94 entries, added in cc0be7a and 0b9601f) exists but is not used. SH §5 (\"no .bib file, refs/ is empty\") is stale.",
         loc="630-721", src="SH §5, SH 7.4",
         status="OPEN", closer="", owner="S14", also="",
         note="Partly closed in the repository, not in the manuscript."),
    # ------------------------------------------------------------------ COPY
    dict(id="COP-01", sev="COPY",
         text="Corrupted em-dash pattern: no real em-dash exists; every one became ' ,  '. 53 occurrences on 25 lines (48 of ' ,  ' including the leading half of 5 comment pairs, plus 5 trailing ' , ' in bibliography comments), 5 of them in the abstract. Each needs an individual decision; the 70 '--' are legitimate en-dashes and must not be replaced.",
         loc="58 (x5), 75, 101, 103, 114, 118 (x2), 121 (x2), 134, 153 (x3), 155 (x2), 160 (x4), 236 (x2), 275 (x2), 348 (x2), 360 (x2), 373 (x2), 395 (x2), 479 (x2), 489 (x2), 494 (x4); comments 632, 654, 661, 686, 702",
         src="SH §2, SH 7.2, BR K6",
         status="OPEN", closer="", owner="S11", also="",
         note="Blocking in practice (the abstract reads \"pillows ,  spheres\"), copy-edit by the scale. Counts re-derived in review/defects-check.py."),
    dict(id="COP-02", sev="COPY",
         text="bibitem ssw2006: publisher of record gives pages 375-385; manuscript prints 375-384.",
         loc="668", src="VD #8", status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="COP-03", sev="COPY",
         text="bibitem datchevhezari2013: the primary MSRI PDF and Crossref give 2012; manuscript prints 2013. Pages 455-485 are correct (Crossref's 455-486 is wrong).",
         loc="639", src="VD #14", status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="COP-04", sev="COPY",
         text="bibitem nrs2024: Ann. Math. Quebec 49, 1-61, issue year 2025; manuscript gives \"(2024)\" with no volume or pages.",
         loc="696", src="VD #16, SH §5", status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="COP-05", sev="COPY",
         text="bibitem looisher2025 (arXiv:2512.04422) is a recent preprint: check for publication before submission.",
         loc="699", src="SH §5", status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="COP-06", sev="COPY",
         text="bibitem mckeansinger1967: page range 43-69 is corroborated only by a secondary index (Project Euclid, JSTOR and MathSciNet blocked automated access); venue, volume, year and DOI confirmed.",
         loc="636", src="VD closing section", status="OPEN", closer="", owner="S14", also="",
         note="Instrument gap."),
    dict(id="COP-07", sev="COPY",
         text="Two overfull boxes: the three-way inequality chain (18.28 pt) and the display defining N(S) and the cumulative count (53.61 pt, visible in the PDF).",
         loc="341-343, 408-409", src="SH §6, SH 7.6", status="OPEN", closer="", owner="S11", also="", note=""),
    dict(id="COP-08", sev="COPY",
         text="Global hyphenation suppression (hyphenpenalty, exhyphenpenalty, pretolerance = 10000, \\sloppy) causes 24 underfull boxes and loose spacing; most journals will not want it.",
         loc="17-20", src="SH §1, SH §6, SH 7.9", status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="COP-09", sev="COPY",
         text="Four further unused packages: mathrsfs, xcolor, mathtools, caption.",
         loc="3, 10, 11, 15", src="SH §1, SH 7.8", status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="COP-10", sev="COPY",
         text="Three environments print as \"Theorem\": theorem, mainthm (A, B, C) and theorem*; a copy-editor will query it.",
         loc="31-46", src="SH §1, SH 7.10", status="OPEN", closer="", owner="S11", also="", note=""),
    dict(id="COP-11", sev="COPY",
         text="Eight labels are defined and never referenced: rem:bugfix, sec:cone, sec:core, sec:heatexp, sec:intro, sec:novelty, sec:related, sec:scope. rem:bugfix (the warning against the mis-normalized S1 formula) suggests a dropped cross-reference.",
         loc="229 (rem:bugfix); section labels at 73, 124, 147, 158, 164, 169, 178", src="SH §4, SH 7.11",
         status="OPEN", closer="", owner="S11", also="", note=""),
    dict(id="COP-12", sev="COPY",
         text="\\title carries a hard-coded \\vspace{-2cm}; fragile under any class change.",
         loc="48", src="SH §1, SH 7.12", status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="COP-13", sev="COPY",
         text="\"The author declares no competing interests\" (singular) in a paper with no author named.",
         loc="618", src="SH §3", status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="COP-14", sev="COPY",
         text="Cross-reference numbers in the review documents do not match the compiled manuscript. rem:ncone compiles as Remark 5.1 (review documents: 5.4 in CL, 5.6 in VD, P2 and the brief); prop:recovery as Proposition 2.5 (CL: 2.7); tab:density is compiled Table 1 and tab:enum Table 2, while CL calls tab:enum \"Table 1\" and tab:density \"Table 2\" and VD writes \"Table 5.1\". This ledger uses labels and line numbers.",
         loc="493 (rem:ncone), 442-445, 507-508", src="CL DE-30, CL §E, VD §1, VD #22; found while merging",
         status="OPEN", closer="", owner="S14", also="",
         note="Compiled numbers read from the .aux of a fresh build of the unchanged main.tex. The documents themselves are unedited."),
    dict(id="COP-15", sev="COPY",
         text="claim-ledger.md contradicts itself on its headline: the summary and §D say 147 of 147 checkable assertions reproduce, while §F says 121 of 121 with 10 remaining.",
         loc="-- (review/claim-ledger.md, summary and §F)", src="CL summary, CL §F.2; found while merging",
         status="OPEN", closer="", owner="S14", also="", note=""),
    dict(id="COP-16", sev="COPY",
         text="The independent readability review never returned; the readability pass was self-assessed (four changes applied, four rejected).",
         loc="--", src="P2 §10.4", status="OPEN", closer="", owner="S11", also="", note="Low stakes."),
    dict(id="COP-17", sev="COPY",
         text="Three overlapping defect accounts used incompatible severity vocabularies and no merged list existed.",
         loc="--", src="P2 §10.7", status="CLOSED", closer="review/DEFECTS.md (this file)", owner="S2", also="", note=""),
]

CHECKED_ABSENT = """\
## Checked and found absent

**(3,3,12) is arithmetic; no file carries the contrary claim.** An earlier planning note (not itself in the repository) had suggested that (3,3,12) is non-arithmetic. Both (2,8,8) and (3,3,12) are arithmetic: Takeuchi, J. Math. Soc. Japan 29 (1977), Theorem 3(i) (primary PDF read; see review/takeuchi-verdict.md §3), commensurability classes III and XV (Takeuchi's classes as reproduced in Tu-Yang, Appendix A, verified to partition the 76 compact triples exactly). Every file in the repository was searched, excluding only research/raw and .git: all lines mentioning (3,3,12) within 250 characters of "arithmetic" were scanned for negations (non-arithmetic, not arithmetic, isn't, fails, absent from, not on the list), and the whole tree was searched for `non.{0,2}arithmetic` and `not.{0,14}arithmetic`. Hits (the same text is reproduced in review/P2.md and review/STATUS.md): the generic sentence in the Takeuchi verdict ("separates an arithmetic group from a non-arithmetic one", about the argument form, stated of neither triple) and the phrase \"absent from the visible classes\" (about class membership in the same file, which states both triples are arithmetic). No file asserts that (3,3,12) is non-arithmetic, so no FATAL row is logged. The assertion that (3,3,12) is on Takeuchi's list is re-checked mechanically in review/defects-check.py.
"""


def main():
    ids = [r["id"] for r in ROWS]
    assert len(ids) == len(set(ids))
    for r in ROWS:
        assert r["sev"] in SEV and r["owner"] in SESSIONS, r["id"]
        assert r["status"] in ("OPEN", "CLOSED")
        assert (r["status"] == "CLOSED") == bool(r["closer"]), r["id"]
        assert r["id"].startswith({"FATAL": "FAT", "MAJOR": "MAJ", "MINOR": "MIN", "COPY": "COP"}[r["sev"]])

    L = []
    w = L.append
    w("# DEFECTS: one ledger for the manuscript and its verification record\n")
    w("Merged 2026-10-01 (re-triaged in the S9b consolidation, which closed the rows whose work is now in the repository) from review/claim-ledger.md, review/source-hygiene.md, the corrections table of review/hyperresearch/VERDICT.md, review/convention-note.md, review/reproducibility-report.md and section 10 of review/P2.md (plus section 9 of the same file), and the known items of the consolidation brief. Generated by `review/build_defects.py`; facts and line numbers are re-checked by `review/defects-check.py`.\n")
    w("Line numbers refer to `paper/main.tex` (723 lines, MD5 `adfa0001c73e3721f3ccdcc6dcda7e12`, unchanged). Entries marked `--` concern the review record rather than a manuscript line.\n")
    w("## Severity scale\n")
    w("| Level | Meaning |")
    w("|---|---|")
    w("| FATAL | A false or unsupported claim in the manuscript on which a stated result, the abstract, or an availability statement rests |")
    w("| MAJOR | A referee will demand it: a missing proof, citation, definition or reconciliation |")
    w("| MINOR | Precision: a statement that needs narrowing, a citation to bring current, a research-record gap |")
    w("| COPY | Copyedit and submission hygiene |\n")
    w("Mapping used when merging the old vocabularies: claim-ledger `no` on a claim about the artefact and VERDICT `substantive` that is a missing citation or proof become MAJOR or FATAL according to whether a stated result depends on them; VERDICT `precision` and `opportunity` become MINOR; VERDICT `bibliography` becomes MINOR when it changes what is cited (published version, uncited work) and COPY when it corrects a page range, year or volume; source-hygiene `Blocking` is judged on the scale above (the em-dash corruption is COPY by the scale although it shows in the abstract).\n")
    w("## Owning sessions\n")
    w("S1 audibility theorem; S3 spectral numerics; S4 general signatures; S5 locality (heat invariants cannot see moduli); S6 stability theorem; S7 curvature section and closed-form threshold; S8 Diophantine section; S10 figures; S11 manuscript rewrite; S14 submission package. **S2 is this consolidation session**: a row owned by S2 was closed here, ahead of the session that would otherwise have closed it; the `Also` column names the planned session that still has follow-up work. S3 owns one row because its only defect is compute-bound. In the S9b consolidation every row owned by S1 and S3 to S8 was either closed by work now merged (commit or file given in the Status column) or reassigned to S10, S11 or S14, because what remains of it is text, figures or submission hygiene.\n")
    w("## Source codes\n")
    w("CL claim-ledger (row ids; §C = findings C-1..C-6, §F = consequences) · SH source-hygiene (section; `7.n` = item n of its §7) · VD VERDICT (`#n` = row n of its corrections table, `§n` = its answer n) · CN convention-note · RR reproducibility-report · P2 review/P2.md · TV takeuchi-verdict · OF outstanding-fetches · BR the brief (K1 abstract range, K2 pair counting and fibres, K3 K infinite for n >= 4, K4 stability front end, K5 run_all, K6 em-dashes, K7 (3,3,12)).\n")

    for sev in SEV:
        rows = [r for r in ROWS if r["sev"] == sev]
        w(f"## {sev} ({len(rows)})\n")
        w("| ID | Defect | main.tex | Sources | Status | Owner |")
        w("|---|---|---|---|---|---|")
        for r in rows:
            status = r["status"] if r["status"] == "OPEN" else f"CLOSED: {r['closer']}"
            owner = r["owner"] + (f" (also {r['also']})" if r["also"] else "")
            text = r["text"].replace("|", "/")
            if r["note"]:
                text += f" *Note: {r['note']}*".replace("|", "/")
            w(f"| {r['id']} | {text} | {r['loc']} | {r['src']} | {status} | {owner} |")
        w("")

    w(CHECKED_ABSENT)

    w("## Counts\n")
    w("### By severity\n")
    w("| Severity | Total | OPEN | CLOSED |")
    w("|---|---:|---:|---:|")
    bys = Counter((r["sev"], r["status"]) for r in ROWS)
    for sev in SEV:
        o, c = bys[(sev, "OPEN")], bys[(sev, "CLOSED")]
        w(f"| {sev} | {o + c} | {o} | {c} |")
    to = sum(1 for r in ROWS if r["status"] == "OPEN")
    w(f"| **All** | **{len(ROWS)}** | **{to}** | **{len(ROWS) - to}** |\n")
    w("### By owning session\n")
    w("| Session | Total | OPEN | CLOSED | FATAL | MAJOR | MINOR | COPY |")
    w("|---|---:|---:|---:|---:|---:|---:|---:|")
    for s in SESSIONS:
        rs = [r for r in ROWS if r["owner"] == s]
        if not rs:
            w(f"| {s} | 0 | 0 | 0 | 0 | 0 | 0 | 0 |")
            continue
        sc = Counter(r["sev"] for r in rs)
        o = sum(1 for r in rs if r["status"] == "OPEN")
        w(f"| {s} | {len(rs)} | {o} | {len(rs) - o} | {sc['FATAL']} | {sc['MAJOR']} | {sc['MINOR']} | {sc['COPY']} |")
    w("")
    w("### OPEN FATAL and MAJOR by owning session\n")
    w("| Session | OPEN FATAL | OPEN MAJOR |")
    w("|---|---:|---:|")
    for s in SESSIONS:
        f = sum(1 for r in ROWS if r["owner"] == s and r["status"] == "OPEN" and r["sev"] == "FATAL")
        m = sum(1 for r in ROWS if r["owner"] == s and r["status"] == "OPEN" and r["sev"] == "MAJOR")
        if f or m:
            w(f"| {s} | {f} | {m} |")
    w("")
    OUT.write_text("\n".join(L))
    print("wrote", OUT, len(ROWS), "rows")


if __name__ == "__main__":
    main()
