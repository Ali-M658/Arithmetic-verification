#!/usr/bin/env python3
"""Build paper/eigen/references.bib from fetched bibliographic records only.

The record handling (DOI content negotiation, arXiv and zbMATH Open records, the style tables, the
corrections each justified by a fetched record) is that of paper/jga/tools/build_bib.py, imported
unchanged; this script only replaces its table of sources by the works the eigen manuscript cites
and writes into paper/eigen/ (raw records in the git-ignored paper/eigen/fetched/bib/).

    python3 paper/eigen/tools/build_bib.py --fetch   # download the raw records
    python3 paper/eigen/tools/build_bib.py           # assemble references.bib from them

New records for this manuscript (round 3, items I2 and I5), each confirmed against Crossref and
zbMATH Open by the reference check of 2026-10-07:
  jorgensen1976  doi:10.2307/2373814 (zbMATH 0336.30007); the text is behind a bot wall (JSTOR):
                 an instrument gap, recorded in paper/eigen/SOURCES.md; the paper proves the special
                 case it needs and cites the original for the argument
  beardon1983    doi:10.1007/978-1-4612-1146-4 (GTM 91)
  mumford1971    doi:10.1090/s0002-9939-1971-0276410-4; Corollary 3 read from the fetched scan
  bers1972       doi:10.1007/bf02764631; abstract (fetched): the compactness theorem "remains valid
                 for groups containing elliptic and parabolic elements"
"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent          # paper/eigen
JGA = HERE.parent / "jga" / "tools" / "build_bib.py"
spec = importlib.util.spec_from_file_location("jga_build_bib", JGA)
bb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bb)

KEEP = ["dggw2008", "donnelly1976", "ucar2017", "schueth2019", "drydenstrohmaier2009", "thurston1980",
        "hejhal1976", "iwaniec2002", "garbinjorgenson2020", "stanhope2005", "changdeturck1989",
        "griesermaronna2013", "buser1992", "linowitzvoight2015", "strohmaieruski2013", "schoberl1997",
        "arpack1998", "ngsolve", "crameri2023", "crameri2020"]
SOURCES = {k: bb.SOURCES[k] for k in KEEP}
SOURCES.update({
    # the authors' companion manuscript submitted at the same time (paper/jga/manuscript.tex)
    "companionA": ("local", "paper/jga/manuscript.tex"),
    "jorgensen1976": ("doi", "10.2307/2373814"),
    "beardon1983": ("doi", "10.1007/978-1-4612-1146-4"),
    "mumford1971": ("doi", "10.1090/s0002-9939-1971-0276410-4"),
    "bers1972": ("doi", "10.1007/bf02764631"),
    # round 4 ("Relation to prior work"); texts read are logged in paper/eigen/SOURCES.md, round 4
    "busercourtois1990": ("doi", "10.1007/bf01446910"),
    "garbinjorgenson2018": ("doi", "10.4171/lem/64-1/2-7"),
    "wolpert1992a": ("doi", "10.1007/bf02100600"),
    "wolpert1992b": ("doi", "10.1007/bf02100601"),
    "ji1993": ("doi", "10.4310/jdg/1214454296"),
    "hejhal1983": ("doi", "10.1007/bfb0061302"),
    "hejhal1990": ("doi", "10.1090/memo/0437"),
    "bsv2006": ("doi", "10.1155/imrn/2006/71281"),
})
bb.SOURCES = SOURCES
bb.HERE = HERE
bb.RAW = HERE / "fetched" / "bib"
bb.OUT = HERE / "references.bib"
# Crossref prints Jorgensen's name and title without diacritics; zbMATH 0336.30007 has them
bb.TITLE_SC["jorgensen1976"] = "On discrete groups of {M}{\\\"o}bius transformations"
bb.TITLE_SC["bers1972"] = "A remark on {M}umford's compactness theorem"
bb.TITLE_SC["mumford1971"] = "A remark on {M}ahler's compactness theorem"
bb.TITLE_SC["beardon1983"] = "The geometry of discrete groups"
# round 4: record fixes, each checked against a fetched zbMATH Open record (fetched by --fetch)
bb.EVIDENCE_ZB.update({"busercourtois1990_zb": "0711.58033", "garbinjorgenson2018_zb": "1444.58012",
                       "ji1993_zb": "0793.53051", "hejhal1983_zb": "0543.10020", "bsv2006_zb": "1154.11018"})
bb.TITLE_SC.update({
    "busercourtois1990": "Finite parts of the spectrum of a {Riemann} surface",
    "garbinjorgenson2018": "Spectral asymptotics on sequences of elliptically degenerating {Riemann} surfaces",
    "wolpert1992a": "Spectral limits for hyperbolic surfaces, {I}",
    "wolpert1992b": "Spectral limits for hyperbolic surfaces, {II}",
    "ji1993": "Spectral degeneration of hyperbolic {Riemann} surfaces",
    # "Vol. 2" is in the zbMATH title, not in the Crossref one
    "hejhal1983": "The {Selberg} trace formula for $\\mathrm{PSL}(2,\\mathbb{R})$. {V}ol.~2",
    "hejhal1990": "Regular $b$-groups, degenerating {Riemann} surfaces, and spectral theory",
    "bsv2006": "Effective computation of {Maass} cusp forms",
})
bb.TITLE_EXTRA_SOURCE["hejhal1983"] = "hejhal1983_zb"
bb.PAGES_ZB["ji1993"] = ("ji1993_zb", "263-313")             # the JDG record has no pages
bb.JOURNAL["garbinjorgenson2018"] = "L'Enseignement Math{\\'e}matique (2)"
bb.JOURNAL["bsv2006"] = "International Mathematics Research Notices"
bb.AUTHORS["bsv2006"] = "Booker, Andrew R. and Str{\\\"o}mbergsson, Andreas and Venkatesh, Akshay"   # zbMATH 1154.11018
bb.EXTRA.update({
    "busercourtois1990": {"number": "3"},                  # Crossref has issue 1; zbMATH and EPFL: No. 3
    "garbinjorgenson2018": {"year": "2018", "number": "1-2"},  # Crossref dates the online issue (2019)
    "hejhal1983": {"series": "Lecture Notes in Mathematics", "volume": "1001"},
    "bsv2006": {"volume": "2006", "number": "12", "pages": "Art.~ID 71281"},
})
bb.CHECK_EXTRA.update({
    "busercourtois1990": ("busercourtois1990_zb", "287, No. 3, 523-530 (1990)"),
    "garbinjorgenson2018": ("garbinjorgenson2018_zb", "64, No. 1-2, 161-206 (2018)"),
    "hejhal1983": ("hejhal1983_zb", "Lecture Notes in Mathematics. 1001."),
    "bsv2006": ("bsv2006_zb", "2006, No. 12, Article ID 71281", "Strömbergsson, Andreas"),
})

if __name__ == "__main__":
    (HERE / "fetched").mkdir(exist_ok=True)
    zb = bb.RAW / "jorgensen1976_zb.json"
    if "--fetch" in sys.argv:
        bb.fetch_all()
        zb.write_bytes(bb.get("https://api.zbmath.org/v1/document/_search?search_string=an%3A0336.30007"
                              "&page=0&results_per_page=1"))
    bb.build()
    txt = bb.OUT.read_text(encoding="utf-8").replace("generated by paper/jga/tools/build_bib.py",
                                                       "generated by paper/eigen/tools/build_bib.py")
    # the letter o-slash of zbMATH 0336.30007, which the Crossref record writes as "o"
    txt = txt.replace("author      = {Jorgensen, T.}", "author      = {J{\\o}rgensen, T.}")
    txt = txt.replace("author      = {Jorgensen, Troels}", "author      = {J{\\o}rgensen, Troels}")
    # the page range of zbMATH 0336.30007 (Crossref gives only the first page)
    assert '"739-749"' in zb.read_text(encoding="utf-8")
    txt = txt.replace("  pages       = {739},", "  pages       = {739--749},")
    bb.OUT.write_text(txt, encoding="utf-8")
