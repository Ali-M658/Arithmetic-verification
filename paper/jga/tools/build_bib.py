#!/usr/bin/env python3
"""Build paper/jga/references.bib from fetched bibliographic records only.

Every entry comes from a record retrieved by this script: a DOI resolved by content
negotiation (Crossref or DataCite BibTeX), an arXiv API record, or a zbMATH Open API
record. Nothing is typed in from memory. Two entries describe documents that have no
registry record at all (Thurston's lecture notes and the PARI/GP manual); for those the
fields are copied from the fetched document itself, and the document's URL and SHA-256
are logged in paper/jga/SOURCES.md.

    python3 paper/jga/tools/build_bib.py --fetch   # download raw records into fetched/bib/
    python3 paper/jga/tools/build_bib.py           # assemble references.bib from them

The raw records are not committed (paper/jga/fetched/ is git-ignored); --fetch recreates
them, and SOURCES.md lists the SHA-256 of each one as fetched for this build.
"""
import hashlib
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent          # paper/jga
RAW = HERE / "fetched" / "bib"
OUT = HERE / "references.bib"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) bibliography-build"}

# key -> (kind, identifier). kind: doi | arxiv | zbmath | document
SOURCES = {
    # orbifold heat invariants and cone coefficients
    "dggw2008": ("doi", "10.1307/mmj/1213972406"),
    "donnelly1976": ("doi", "10.1007/BF01436198"),
    "ucar2017": ("arxiv", "1711.03405"),
    "schueth2019": ("doi", "10.5802/aif.3338"),
    "berndtyeap2002": ("doi", "10.1016/S0196-8858(02)00020-9"),
    "adfg2008": ("doi", "10.1007/s10455-007-9092-6"),
    # spectra of hyperbolic orbisurfaces
    "drydenstrohmaier2009": ("doi", "10.4153/CMB-2009-008-0"),
    "doylerossetti2011": ("arxiv", "1103.4372"),
    "linowitzvoight2015": ("doi", "10.1007/s00209-015-1500-1"),
    "marklof2011": ("doi", "10.1017/cbo9781139108782.003"),
    "troyanov1991": ("doi", "10.1090/S0002-9947-1991-1005085-9"),
    "thurston1980": ("document", "https://library.slmath.org/books/gt3m/PDF/13.pdf"),
    # isospectrality and finite spectral data
    "kac1966": ("doi", "10.1080/00029890.1966.11970915"),
    "mckeansinger1967": ("doi", "10.4310/jdg/1214427880"),
    "sunada1985": ("doi", "10.2307/1971195"),
    "gww1992": ("doi", "10.1090/S0273-0979-1992-00289-6"),
    "ssw2006": ("doi", "10.1007/s00013-006-1748-0"),
    "rsw2008": ("doi", "10.1007/s10455-008-9110-3"),
    "barihunsicker2020": ("doi", "10.4153/S0008414X19000178"),
    "griesermaronna2013": ("doi", "10.1090/noti1063"),
    "gomezserrano2021": ("doi", "10.1016/j.jde.2020.11.002"),
    # power sums, Hurwitz determinants, root perturbation
    "holtztyaglov2012": ("doi", "10.1137/090781127"),
    "ostrowski1940": ("doi", "10.1007/bf02546330"),
    "steinig1971": ("zbmath", "0238.10007"),
    "laurens2023": ("doi", "10.1007/s00526-023-02534-2"),
    "msw2022": ("doi", "10.1080/10586458.2022.2061650"),
    "korobovbugaevskaya2016": ("doi", "10.1090/mcom/2994"),
    "mueller2016": ("doi", "10.1007/s10208-014-9239-3"),
    "alloucheshallit1999": ("doi", "10.1007/978-1-4471-0551-0_1"),
    # Diophantine section
    "bgn1993": ("doi", "10.1090/s0025-5718-1993-1189516-5"),
    "schinzel1996": ("zbmath", "0932.11019"),
    "beauville1982": ("zbmath", "0504.14016"),
    "mazur1977": ("doi", "10.1007/bf02684339"),
    "pari2172": ("document", "https://pari.math.u-bordeaux.fr/archives/pari-announce-25/msg00001.html"),
    # numerics
    "strohmaieruski2013": ("doi", "10.1007/s00220-012-1557-1"),
    "schoberl1997": ("doi", "10.1007/s007910050004"),
    "arpack1998": ("doi", "10.1137/1.9780898719628"),
    # colour maps used by the figures
    "crameri2023": ("doi", "10.5281/zenodo.8409685"),
    "crameri2020": ("doi", "10.1038/s41467-020-19160-7"),
    # added in the 30-35 page revision (review/literature-pass/references-additions.bib,
    # theory/pte/references-pte.bib, theory/revision/descent.tex); each is a fetched record
    "dggw2017erratum": ("doi", "10.1307/mmj/1488510034"),
    "hejhal1976": ("zbmath", "0347.10018"),
    "iwaniec2002": ("zbmath", "1006.11024"),
    "mckean1972": ("zbmath", "0225.30021"),
    "mckean1974corr": ("zbmath", "0317.30018"),
    "huber1959": ("zbmath", "0089.06101"),
    "buser1992": ("zbmath", "0770.53001"),
    "wolpert1979": ("zbmath", "0441.30055"),
    "stanhope2005": ("doi", "10.1007/s10455-005-1584-7"),
    "dryden2004": ("arxiv", "math/0411290"),
    "garbinjorgenson2020": ("doi", "10.2996/kmj/1584345689"),
    "schueth2025": ("doi", "10.1007/s10455-025-10024-1"),
    "watson2005": ("zbmath", "1076.35042"),
    "philippe2008": ("doi", "10.5802/aif.2424"),
    "philippe2010gd": ("doi", "10.1007/s10711-010-9473-z"),
    "changdeturck1989": ("zbmath", "0721.58053"),
    "strohmaieruski2018": ("doi", "10.1007/s00220-018-3094-z"),
    "ngsolve": ("document", "https://api.zbmath.org/v1/software/_search?search_string=NGSolve"),
    "aby2015": ("doi", "10.1109/sampta.2015.7148965"),
    "bgy2020": ("doi", "10.1093/imaiai/iaaa005"),
    "borweiningalls1994": ("zbmath", "0810.11016"),
    "melzak1961": ("doi", "10.4153/CMB-1961-025-1"),
    "blp2003": ("doi", "10.1090/S0025-5718-02-01504-1"),
    "cmsv2024": ("doi", "10.1090/mcom/3917"),
    "chen2025survey": ("arxiv", "2506.11429"),
    "wooley2012": ("doi", "10.4007/annals.2012.175.3.12"),
    "wooley2019": ("doi", "10.1112/plms.12204"),
    "crootmaoyip2026": ("arxiv", "2609.05061"),
    "cremona1997": ("zbmath", "0872.14041"),
    # added in referee round 1 (review/round1-fixes/citations/)
    "richardsonstanhope2020": ("doi", "10.1016/j.difgeo.2019.101577"),
    "philippe2010tsg": ("doi", "10.5802/tsg.280"),
    # the authors' companion manuscript (paper/arith/note.tex), not a third-party record
    "companion": ("local", "paper/arith/note.tex"),
}

# Documents with no registry record: fields read off the fetched document (SOURCES.md).
# thurston1980: title page of the fetched chapter ("Electronic version 1.1 - March 2002",
# "electronic edition of the 1980 notes distributed by Princeton University").
# pari2172: the fetched release announcement (pari-announce-25, msg00001: "Done for version
# 2.17.2 (released 05/03/2025)"); the version used is recorded in theory/diophantine/data/ranks.txt.
# ngsolve: the fetched swMATH software record 13154 (zbMATH Open API); the usual NGSolve report
# has no registry record and was not fetched (review/literature-pass/GAPS.md).
DOCUMENT_ENTRIES = {
    "thurston1980": """@misc{thurston1980,
  author       = {Thurston, William P.},
  title        = {The geometry and topology of three-manifolds},
  howpublished = {Lecture notes, Princeton University, 1980; electronic ed.~1.1, Ch.~13},
  year         = {2002}
}""",
    "pari2172": """@misc{pari2172,
  author       = {{The PARI~Group}},
  title        = {{PARI/GP} version 2.17.2},
  howpublished = {Univ. Bordeaux, released 5 March 2025},
  year         = {2025},
  url          = {https://pari.math.u-bordeaux.fr/}
}""",
    "ngsolve": """@misc{ngsolve,
  author       = {Sch{\\"o}berl, J.},
  title        = {{NGSolve}},
  howpublished = {Software, swMATH 13154},
  url          = {https://www.ngsolve.org/}
}""",
}
LOCAL_ENTRIES = {
    "companion": ("\\title{Triples with equal sum and equal reciprocal sum}", """@unpublished{companion,
  author       = {Gang, Palaash and Agadi, Akshaj and Veluri, Arjun and Wang, Jerry and Barreto, Jeremy and Chouthaiwale, Aarin},
  title        = {Triples with equal sum and equal reciprocal sum},
  note         = {Companion manuscript, in preparation},
  year         = {2026}
}"""),
}
DOCUMENT_CHECK = {"pari2172": "released 05/03/2025", "ngsolve": "NGSolve"}

# Corrections applied to a fetched record, each justified by another fetched document.
CORRECTIONS = {
    # zbMATH prints the title with a doubled word; the paper's own first page (fetched in
    # the G5 audit, review/audit/fetches.md, schinzel_serdica1996.pdf) has the title below.
    ("schinzel1996", "title"): "Triples of positive integers with the same sum and the same product",
}


def get(url, headers=None, tries=3):
    h = dict(UA)
    if headers:
        h.update(headers)
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=90) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            if k == tries - 1:
                raise
            time.sleep(3)


EVIDENCE = {"ostrowski1940_reprint": "10.1007/978-3-0348-9355-8_50", "ucar2017_datacite": "10.18452/18463",
            # book records: editors of the two incollection entries; the next chapter of the
            # Bolte-Steiner volume (it starts on p. 121, so Marklof's chapter is pp. 83-120)
            "marklof2011_book": "10.1017/cbo9781139108782", "marklof2011_next": "10.1017/cbo9781139108782.004",
            "alloucheshallit1999_book": "10.1007/978-1-4471-0551-0"}
# zbMATH records used as evidence for one field each (series, pages, title punctuation)
EVIDENCE_ZB = {"alloucheshallit1999_zb": "1005.11005", "dggw2017erratum_zb": "1404.58043",
               "garbinjorgenson2020_zb": "1446.58010", "schoberl1997_zb": "0883.68130"}
# Publisher locations missing from the Crossref record, read from zbMATH Open (the record is
# fetched as evidence and must contain the location string).
ADDRESS_ZB = {"arpack1998": ("0901.65021", "Philadelphia, PA"), "marklof2011": ("1282.11053", "Cambridge")}


def fetch_all():
    RAW.mkdir(parents=True, exist_ok=True)
    for key, doi in EVIDENCE.items():
        (RAW / f"{key}.json").write_bytes(get("https://doi.org/" + doi, {"Accept": "application/vnd.citationstyles.csl+json"}))
    for key, zbl in EVIDENCE_ZB.items():
        q = urllib.parse.quote("an:" + zbl)
        (RAW / f"{key}.json").write_bytes(
            get(f"https://api.zbmath.org/v1/document/_search?search_string={q}&page=0&results_per_page=1"))
    for key, (zbl, _) in ADDRESS_ZB.items():
        q = urllib.parse.quote("an:" + zbl)
        (RAW / f"{key}_address_zbmath.json").write_bytes(
            get(f"https://api.zbmath.org/v1/document/_search?search_string={q}&page=0&results_per_page=1"))
    arxiv_ids = [v for k, (kind, v) in SOURCES.items() if kind == "arxiv"]
    if arxiv_ids:
        data = get("https://export.arxiv.org/api/query?max_results=50&id_list=" + ",".join(arxiv_ids))
        (RAW / "arxiv.xml").write_bytes(data)
    for key, (kind, ident) in SOURCES.items():
        if kind == "doi":
            data = get("https://doi.org/" + ident, {"Accept": "application/vnd.citationstyles.csl+json"})
            (RAW / f"{key}.json").write_bytes(data)
        elif kind == "zbmath":
            q = urllib.parse.quote("an:" + ident)
            data = get(f"https://api.zbmath.org/v1/document/_search?search_string={q}&page=0&results_per_page=1")
            (RAW / f"{key}.json").write_bytes(data)
        elif kind == "local":
            continue
        elif kind == "document":
            data = get(ident)
            (RAW / f"{key}.document").write_bytes(data)
        time.sleep(0.5)


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rekey(bib, key):
    return re.sub(r"^@(\w+)\{[^,]*,", lambda m: f"@{m.group(1)}{{{key},", bib.strip(), count=1)


LEGACY = Path(__file__).resolve().parents[3] / "refs" / "sources.bib"
# Fields Crossref does not carry for these DOIs, taken from the matching entry of
# refs/sources.bib (itself built from fetched records in the literature sweep).
LEGACY_FILL = {"dggw2008": ["pages"], "mckeansinger1967": ["pages"],
               "sunada1985": ["pages"], "griesermaronna2013": ["pages"]}
# Pages missing from the Crossref record, read from a fetched zbMATH record (EVIDENCE_ZB).
PAGES_ZB = {"dggw2017erratum": ("dggw2017erratum_zb", "221-222"),
            "garbinjorgenson2020": ("garbinjorgenson2020_zb", "84-128")}

# ---------------------------------------------------------------------------------------
# Style layer (review/literature-pass/CITATIONS.md section 4): sentence-case titles with
# proper nouns braced, one journal style (full names, series numbers in parentheses), and
# the record fixes listed there. Every title below is checked against the fetched title
# (case, braces, accents and punctuation ignored); the few that add text not in the primary
# record name the second fetched record that carries it (TITLE_EXTRA_SOURCE).
TITLE_SC = {
    "dggw2008": "Asymptotic expansion of the heat kernel for orbifolds",
    "dggw2017erratum": "Erratum to ``{A}symptotic expansion of the heat kernel for orbifolds''",
    "donnelly1976": "Spectrum and the fixed point sets of isometries. {I}",
    "ucar2017": "Spectral invariants for polygons and orbisurfaces",
    "schueth2019": "On the corner contributions to the heat coefficients of geodesic polygons",
    "schueth2025": "Heat coefficients of surfaces with curved conical singularities",
    "berndtyeap2002": "Explicit evaluations and reciprocity theorems for finite trigonometric sums",
    "adfg2008": "Hearing the weights of weighted projective planes",
    "drydenstrohmaier2009": "{Huber}'s theorem for hyperbolic orbisurfaces",
    "doylerossetti2011": "{Laplace}-isospectral hyperbolic 2-orbifolds are representation-equivalent",
    "linowitzvoight2015": "Small isospectral and nonisometric orbifolds of dimension 2 and 3",
    "marklof2011": "{Selberg}'s trace formula: an introduction",
    "troyanov1991": "Prescribing curvature on compact surfaces with conical singularities",
    "kac1966": "Can one hear the shape of a drum?",
    "mckeansinger1967": "Curvature and the eigenvalues of the {Laplacian}",
    "sunada1985": "{Riemannian} coverings and isospectral manifolds",
    "gww1992": "One cannot hear the shape of a drum",
    "ssw2006": "One cannot hear orbifold isotropy type",
    "rsw2008": "Isospectral orbifolds with different maximal isotropy orders",
    "barihunsicker2020": "Isospectrality for orbifold lens spaces",
    "griesermaronna2013": "Hearing the shape of a triangle",
    "gomezserrano2021": "Any three eigenvalues do not determine a triangle",
    "holtztyaglov2012": "Structured matrices, continued fractions, and root localization of polynomials",
    "ostrowski1940": "Recherches sur la m{\\'e}thode de {Graeffe} et les z{\\'e}ros des polynomes et des s{\\'e}ries de {Laurent}",
    "steinig1971": "On some rules of {Laguerre}'s, and systems of equal sums of like powers",
    "laurens2023": "Multisolitons are the unique constrained minimizers of the {KdV} conserved quantities",
    "msw2022": "Recovery from power sums",
    "korobovbugaevskaya2016": "Almost power sum systems",
    "mueller2016": "Sign conditions for injectivity of generalized polynomial maps with applications to chemical reaction networks and real algebraic geometry",
    "alloucheshallit1999": "The ubiquitous {Prouhet}--{Thue}--{Morse} sequence",
    "bgn1993": "Which integers are representable as the product of the sum of three integers with the sum of their reciprocals?",
    "schinzel1996": "Triples of positive integers with the same sum and the same product",
    "beauville1982": "Les familles stables de courbes elliptiques sur $\\mathbf{P}^1$ admettant quatre fibres singuli{\\`e}res",
    "mazur1977": "Modular curves and the {Eisenstein} ideal",
    "strohmaieruski2013": "An algorithm for the computation of eigenvalues, spectral zeta functions and zeta-determinants on hyperbolic surfaces",
    "strohmaieruski2018": "Correction to: {A}n algorithm for the computation of eigenvalues, spectral zeta functions and zeta-determinants on hyperbolic surfaces",
    "schoberl1997": "{NETGEN}: {A}n advancing front {2D/3D}-mesh generator based on abstract rules",
    "arpack1998": "{ARPACK} users' guide: solution of large-scale eigenvalue problems with implicitly restarted {Arnoldi} methods",
    "crameri2023": "Scientific colour maps",
    "crameri2020": "The misuse of colour in science communication",
    "hejhal1976": "The {Selberg} trace formula for $\\mathrm{PSL}(2,\\mathbb{R})$. {V}ol.~{I}",
    "iwaniec2002": "Spectral methods of automorphic forms",
    "mckean1972": "{Selberg}'s trace formula as applied to a compact {Riemann} surface",
    "mckean1974corr": "Correction to: ``{Selberg}'s trace formula as applied to a compact {Riemann} surface''",
    "huber1959": "Zur analytischen {Theorie} hyperbolischer {Raumformen} und {Bewegungsgruppen}",
    "buser1992": "Geometry and spectra of compact {Riemann} surfaces",
    "wolpert1979": "The length spectra as moduli for compact {Riemann} surfaces",
    "stanhope2005": "Spectral bounds on orbifold isotropy",
    "dryden2004": "Isospectral finiteness of hyperbolic orbisurfaces",
    "garbinjorgenson2020": "Heat kernel asymptotics on sequences of elliptically degenerating {Riemann} surfaces",
    "watson2005": "The trace function expansion for spherical polygons",
    "philippe2008": "Les groupes de triangles $(2,p,q)$ sont d{\\'e}termin{\\'e}s par leur spectre des longueurs",
    "philippe2010gd": "Sur la rigidit{\\'e} des groupes de triangles $(r,p,q)$",
    "philippe2010tsg": "Le spectre des longueurs des surfaces hyperboliques: un exemple de rigidit{\\'e}",
    "richardsonstanhope2020": "You can hear the local orientability of an orbifold",
    "changdeturck1989": "On hearing the shape of a triangle",
    "aby2015": "Accuracy of spike-train {Fourier} reconstruction for colliding nodes",
    "bgy2020": "Super-resolution of near-colliding point sources",
    "borweiningalls1994": "The {Prouhet}--{Tarry}--{Escott} problem revisited",
    "melzak1961": "A note on the {Tarry}--{Escott} problem",
    "blp2003": "Computational investigations of the {Prouhet}--{Tarry}--{Escott} problem",
    "cmsv2024": "Ideal solutions in the {Prouhet}--{Tarry}--{Escott} problem",
    "chen2025survey": "A survey of the {Prouhet}--{Tarry}--{Escott} problem and its generalizations",
    "wooley2012": "{Vinogradov}'s mean value theorem via efficient congruencing",
    "wooley2019": "Nested efficient congruencing and relatives of {Vinogradov}'s mean value theorem",
    "crootmaoyip2026": "The {Prouhet}--{Tarry}--{Escott} problem for subsets with small doubling in integral domains",
    "cremona1997": "Algorithms for modular elliptic curves",
}
# Titles whose text (not only its case) comes from a second fetched record.
TITLE_EXTRA_SOURCE = {
    "arpack1998": "arpack1998_address_zbmath",      # the subtitle (zbMATH 0901.65021)
    "schoberl1997": "schoberl1997_zb",              # the colon after NETGEN (zbMATH 0883.68130)
    "beauville1982": None,                          # "singuli\\`eres": print, p. 657 (CITATIONS.md section 4)
}
JOURNAL = {
    "philippe2010tsg": "S{\\'e}minaire de Th{\\'e}orie Spectrale et G{\\'e}om{\\'e}trie",
    "kac1966": "American Mathematical Monthly",
    "sunada1985": "Annals of Mathematics (2)",
    "wolpert1979": "Annals of Mathematics (2)",
    "wooley2012": "Annals of Mathematics (2)",
    "gww1992": "Bulletin of the American Mathematical Society (N.S.)",
    "steinig1971": "Rendiconti di Matematica (6)",
    "beauville1982": "Comptes Rendus de l'Acad{\\'e}mie des Sciences, S{\\'e}rie~I",
    "mazur1977": "Publications Math{\\'e}matiques de l'IH{\\'E}S",
    "borweiningalls1994": "L'Enseignement Math{\\'e}matique (2)",
    "wooley2019": "Proceedings of the London Mathematical Society (3)",
}
AUTHORS = {
    # initials as on the AMS article page (review/literature-pass/CITATIONS.md section 4)
    "korobovbugaevskaya2016": "Korobov, V. I. and Bugaevskaya, A. N.",
    "melzak1961": "Melzak, Z. A.",
    "wooley2012": "Wooley, Trevor D.",          # as in the 2019 record
    # arXiv gives the name in Chinese order ("Chen Shuwen"); the survey and the audit use Chen
    # as the surname (review/audit-2/literature/REVIEW.md, "Chen survey")
    "chen2025survey": "Chen, Shuwen",
}
# Further fields, each from a fetched record named in the comment.
EXTRA = {
    "kac1966": {"number": "4, Part 2"},                                   # journal issue as printed
    "schinzel1996": {"number": "4"},                                      # zbMATH record
    "steinig1971": {"year": "1971", "note": "Published 1972"},            # zbMATH: "4(1971), ... (1972)"
    "ucar2017": {"doi": "10.18452/18463"},                                # DataCite record
    "marklof2011": {"editor": "Bolte, Jens and Steiner, Frank",           # Crossref book record
                    "series": "London Mathematical Society Lecture Note Series", "volume": "397"},  # zbMATH 1282.11053
    "alloucheshallit1999": {"editor": "Ding, C. and Helleseth, T. and Niederreiter, H.",   # Crossref book record
                            "booktitle": "Sequences and their Applications (Singapore, 1998)",
                            "series": "Springer Series in Discrete Mathematics and Theoretical Computer Science"},  # zbMATH 1005.11005
    "arpack1998": {"series": "Software, Environments, Tools", "volume": "6"},            # zbMATH 0901.65021
    "crameri2023": {"note": "Version 8.0.1"},
    # article numbers, printed as such (Crossref "article-number")
    "schueth2025": {"pages": "Paper No.~2"}, "laurens2023": {"pages": "Paper No.~192"},
    "crameri2020": {"pages": "5444"},
    # the 1997 printing is the second edition (ISBN 0-521-59820-6 in the zbMATH record)
    "cremona1997": {"edition": "2nd"},
    # the eigenvalue data are the ancillary files of arXiv:1110.2150v4, cited in the text
}
CHECK_EXTRA = {   # (key, record, substring that must occur in the record) for EXTRA and JOURNAL
    "marklof2011": ("marklof2011_address_zbmath", "Lecture Note Series 397"),
    "alloucheshallit1999": ("alloucheshallit1999_zb", "Springer Series in Discrete Mathematics and Theoretical Computer Science"),
    "arpack1998": ("arpack1998_address_zbmath", "Software - Environments - Tools, 6"),
    "steinig1971": ("steinig1971", "4(1971), 629-644 (1972)"),
    "schinzel1996": ("schinzel1996", "No. 4, 587-588"),
    "ucar2017": ("ucar2017_datacite", "10.18452/18463"),
    "cremona1997": ("cremona1997", "0-521-59820-6"),
}


def legacy_field(key, field):
    s = LEGACY.read_text(encoding="utf-8")
    m = re.search(r"@\w+\{" + re.escape(key) + r",(.*?)\n\}", s, re.S)
    if not m:
        raise SystemExit(f"{key} not in refs/sources.bib")
    f = re.search(r"\b" + field + r"\s*=\s*\{([^}]*)\}", m.group(1))
    if not f:
        raise SystemExit(f"{key}: no {field} in refs/sources.bib")
    return f.group(1)


def year_of(d):
    for k in ("published-print", "journal-issue", "issued", "published-online", "published"):
        v = d.get(k)
        if isinstance(v, dict) and k == "journal-issue":
            v = v.get("published-print") or v.get("published-online")
        if v and v.get("date-parts") and v["date-parts"][0] and v["date-parts"][0][0]:
            return str(v["date-parts"][0][0])
    raise SystemExit("no year")


def names(lst):
    out = []
    for a in lst:
        if "family" in a:
            out.append(f"{a['family']}, {a['given']}" if a.get("given") else a["family"])
        else:
            out.append("{" + a["literal"] + "}")
    return " and ".join(out)


def zb_record(name):
    d = json.loads((RAW / f"{name}.json").read_text(encoding="utf-8"))
    return d["result"][0] if isinstance(d["result"], list) else d["result"]


def from_csl(key, doi):
    d = json.loads((RAW / f"{key}.json").read_text(encoding="utf-8"))
    title = d["title"] if isinstance(d["title"], str) else d["title"][0]
    title = " ".join(re.sub(r"<[^>]+>", "", title).replace("’", "'").split())
    f = {"author": names(d.get("author", [])), "title": title, "year": year_of(d),
         "doi": d.get("DOI", doi)}
    typ = d.get("type")
    cont = d.get("container-title")
    cont = cont[0] if isinstance(cont, list) and cont else cont
    if d.get("volume"):
        f["volume"] = d["volume"]
    if d.get("issue") and d.get("issue") != "0":
        f["number"] = d["issue"]
    if d.get("page"):
        f["pages"] = d["page"].replace("-", "--")
    elif d.get("article-number"):
        f["pages"] = d["article-number"]
    for fld in LEGACY_FILL.get(key, []):
        if fld not in f or (fld == "pages" and "--" not in f[fld]):
            f[fld] = legacy_field(key, fld)
    if key in PAGES_ZB:
        ev, pg = PAGES_ZB[key]
        assert zb_record(ev)["source"]["pages"] == pg, key
        f["pages"] = pg.replace("-", "--")
    is_article = typ in ("journal-article", "article-journal")
    if not is_article:
        if d.get("publisher-location"):
            f["address"] = d["publisher-location"]
        elif key in ADDRESS_ZB:
            zbl, loc = ADDRESS_ZB[key]
            rec = json.loads((RAW / f"{key}_address_zbmath.json").read_text())["result"][0]
            assert rec["identifier"] == zbl and loc in rec["source"]["source"], key
            f["address"] = loc
        elif typ in ("book-chapter", "chapter", "monograph", "book"):
            raise SystemExit(f"{key}: no publisher location in any fetched record")
    if is_article:
        kind = "article"
        f["journal"] = cont.replace("’", "'")
    elif typ in ("book-chapter", "chapter"):
        kind = "incollection"
        f["booktitle"] = cont
        f["publisher"] = d.get("publisher", "")
    elif typ in ("monograph", "book"):
        kind = "book"
        f["publisher"] = d.get("publisher", "")
    elif typ == "proceedings-article":
        # no publisher field: the record has no publisher location, and the bibliography
        # style prints "???" for a publisher without an address
        kind = "inproceedings"
        f["booktitle"] = cont
    else:  # DataCite records (software, datasets)
        kind = "misc"
        f["howpublished"] = d.get("publisher", "")
    return kind, f


def from_arxiv(key, aid):
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    root = ET.parse(RAW / "arxiv.xml").getroot()
    for e in root.findall("a:entry", ns):
        eid = e.find("a:id", ns).text.rsplit("/abs/", 1)[1]
        if re.sub(r"v\d+$", "", eid) != aid:
            continue
        title = " ".join(e.find("a:title", ns).text.split())
        authors = [a.find("a:name", ns).text for a in e.findall("a:author", ns)]
        if key == "ucar2017":
            # The thesis title page (fetched PDF) spells the surname with a cedilla;
            # the arXiv author field is ASCII. Degree data are from the same title page.
            return "phdthesis", {"author": "U{\\c{c}}ar, Eren", "title": title,
                                 "school": "Humboldt-Universit{\\\"a}t zu Berlin",
                                 "year": e.find("a:published", ns).text[:4],
                                 }
        # The current version is cited (doylerossetti2011: v2 of 2014, which carries the
        # quoted sentence in its section 3; CITATIONS.md correction 12).
        year = e.find("a:updated", ns).text[:4]
        first = []
        for a in authors:
            parts = a.split()
            first.append(f"{parts[-1]}, {' '.join(parts[:-1])}")
        return "misc", {"author": " and ".join(first), "title": title, "year": year,
                        "eprint": eid, "note": f"Preprint, arXiv:{eid}"}
    raise SystemExit(f"arXiv id {aid} not in arxiv.xml")


def from_zbmath(key):
    r = zb_record(key)
    authors = " and ".join(a["name"] for a in r["contributors"]["authors"])
    title = CORRECTIONS.get((key, "title"), r["title"]["title"])
    src = r["source"]
    year = r["year"]
    doi = next((l["identifier"] for l in (r.get("links") or []) if l["type"] == "doi"), None)
    if key == "buser1992":
        doi = None      # the DOI in the record belongs to the 2010 reprint (references-additions.bib)
    if r["document_type"]["code"] == "b":
        f = {"author": authors, "title": title.rstrip("."), "year": year}
        ser = src["series"][0] if src.get("series") else None
        if ser:
            f["series"] = ser["title"]
            f["volume"] = ser["volume"]
        text = src["source"]
        m = re.search(r"([A-Z][A-Za-z ,.-]*?): ([^.]*?(?:Press|Springer-Verlag|Birkhäuser|\(AMS\)))", text)
        assert m, (key, text)
        f["address"], f["publisher"] = m.group(1).split(". ")[-1].strip(), m.group(2).strip()
        if key == "hejhal1976":
            f["address"] = "Berlin"            # "Berlin-Heidelberg-New York" in the record
        if doi:
            f["doi"] = doi
        return "book", f
    ser = src["series"][0]
    f = {"author": authors, "title": title, "journal": ser["title"], "volume": ser["volume"],
         "pages": src["pages"].replace("-", "--"), "year": year}
    if doi:
        f["doi"] = doi
    else:
        f["note"] = f"Zbl {r['identifier']}"
    return "article", f


def norm(t):
    """Letters and digits of a title, without TeX markup, accents or case."""
    t = re.sub(r"\\[a-zA-Z]+", "", t)
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", t.lower())


def style(key, kind, f):
    if key in TITLE_SC:
        new = TITLE_SC[key]
        if key in TITLE_EXTRA_SOURCE:
            ev = TITLE_EXTRA_SOURCE[key]
            if ev:
                assert norm(new) == norm(zb_record(ev)["title"]["title"]), key
        else:
            assert norm(new) == norm(f["title"]), (key, new, f["title"])
        f["title"] = new
    if key in JOURNAL:
        f["journal"] = JOURNAL[key]
    elif "journal" in f:
        f["journal"] = re.sub(r"^The ", "", f["journal"])
    if key in AUTHORS:
        assert sorted(norm(x) for x in re.split(r"[ ,.]+", AUTHORS[key].split(" and ")[0]) if len(x) > 1) == \
            sorted(norm(x) for x in re.split(r"[ ,.]+", f["author"].split(" and ")[0]) if len(x) > 1) or \
            norm(AUTHORS[key].split(",")[0]) == norm(f["author"].split(",")[0]), key
        f["author"] = AUTHORS[key]
    if key in CHECK_EXTRA:
        rec, needle = CHECK_EXTRA[key]
        assert needle in (RAW / f"{rec}.json").read_text(encoding="utf-8"), (key, needle)
    f.update(EXTRA.get(key, {}))
    order = ["author", "editor", "title", "booktitle", "journal", "series", "volume", "number",
             "pages", "edition", "school", "publisher", "address", "howpublished", "year", "doi",
             "eprint", "url", "note"]
    body = ",\n".join(f"  {k:<12}= {{{f[k]}}}" for k in order if f.get(k))
    return f"@{kind}{{{key},\n{body}\n}}"


def tidy(b):
    b = b.replace("‐", "-").replace("–", "--").replace("—", "---")
    b = re.sub(r"\s+\}", "}", b)
    b = re.sub(r"(?<!\\)&", r"\\&", b)
    return b


def build():
    entries, log = [], []
    for key, (kind, ident) in SOURCES.items():
        if kind == "doi":
            e = style(key, *from_csl(key, ident))
            log.append((key, f"https://doi.org/{ident}", sha(RAW / f"{key}.json")))
        elif kind == "arxiv":
            e = style(key, *from_arxiv(key, ident))
            log.append((key, f"https://export.arxiv.org/api/query?id_list={ident}", sha(RAW / "arxiv.xml")))
        elif kind == "zbmath":
            e = style(key, *from_zbmath(key))
            log.append((key, f"https://api.zbmath.org/v1/document/_search?search_string=an:{ident}", sha(RAW / f"{key}.json")))
        elif kind == "local":
            needle, e = LOCAL_ENTRIES[key]
            text = (HERE.parents[1] / ident).read_text(encoding="utf-8")
            assert needle in text, key
            for name in ("Palaash Gang", "Akshaj Agadi", "Arjun Veluri", "Jerry Wang", "Jeremy Barreto", "Aarin Chouthaiwale"):
                assert name in text, (key, name)
            log.append((key, ident, sha(HERE.parents[1] / ident)))
        else:
            doc = (RAW / f"{key}.document").read_bytes().decode("utf-8", "replace")
            if key in DOCUMENT_CHECK:
                assert DOCUMENT_CHECK[key] in doc, key
            e = DOCUMENT_ENTRIES[key]
            log.append((key, ident, sha(RAW / f"{key}.document")))
        entries.append(tidy(e))
    header = ("% references.bib -- generated by paper/jga/tools/build_bib.py from fetched records.\n"
              "% Do not edit by hand; edit the SOURCES table in the script and rebuild.\n\n")
    OUT.write_text(header + "\n\n".join(entries) + "\n", encoding="utf-8")
    (HERE / "fetched" / "bib_log.json").write_text(json.dumps(log, indent=1))
    print(f"wrote {OUT} with {len(entries)} entries")


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        fetch_all()
    build()
