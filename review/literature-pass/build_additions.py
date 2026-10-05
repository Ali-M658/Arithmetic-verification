#!/usr/bin/env python3
"""Assemble references-additions.bib from raw fetched records in _fetched/bib/.

Every entry body is the raw record as fetched (Crossref/DataCite content negotiation,
zbMATH BibTeX export) with only the citation key replaced. Three records exist only as
zbMATH/arXiv JSON or Atom XML; those are converted field by field from the fetched file,
with no field typed by hand. Known defects of a fetched record are reported in a comment
above the entry, never patched into it.
"""
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE / "_fetched" / "bib"
OUT = HERE / "references-additions.bib"

# (key, raw file, source URL, priority, where to cite, notes on the fetched record)
BIB = [
    # --- spectral side ---------------------------------------------------------------
    ("dggw2017erratum", "dggw2017erratum.bib", "https://doi.org/10.1307/mmj/1488510034", "REQUIRED",
     "next to the first dggw2008 cite (l. 119 or 220)",
     "Crossref record has no pages; the printed erratum is pp. 221--222 (zbMATH 1404.58043)."),
    ("ucar2017doi", "ucar2017.bib", "https://doi.org/10.18452/18463", "UPDATE",
     "replaces nothing; supplies the DOI and edoc URL for the existing key ucar2017",
     "DataCite record of the Humboldt edoc thesis; byte-identical PDF to arXiv:1711.03405v1."),
    ("hejhal1976", "hejhal1976_zb.bib", "https://zbmath.org/bibtex/0347.10018.bib", "REQUIRED",
     "Thm 4.6 (thm:IEH): Vol. I, Ch. 3, Thm 5.1, p. 351 (trivial character)",
     "zbMATH record used because the Crossref record lacks the LNM volume number."),
    ("iwaniec2002", "iwaniec2002_zb.bib", "https://zbmath.org/bibtex/1006.11024.bib", "REQUIRED",
     "Thm 4.6 admissible class (1.63); Thm 10.2 as 'see also'",
     "zbMATH record used because Crossref gives the ISBN of a later printing."),
    ("mckean1972", "mckean1972_zb.bib", "https://zbmath.org/bibtex/0225.30021.bib", "REQUIRED",
     "Thm 4.1 discussion, Thm 4.6, Remark 4.13, Sec. 1.1", ""),
    ("mckean1974corr", "mckean1974corr_zb.bib", "https://zbmath.org/bibtex/0317.30018.bib", "REQUIRED (with mckean1972)",
     "together with mckean1972",
     "The Crossref record for this DOI is malformed (no author, garbled title); zbMATH used."),
    ("huber1959", "huber1959_zb.bib", "https://zbmath.org/bibtex/0089.06101.bib", "REQUIRED",
     "Remark 4.13 (Saetze 7--8, p. 8); Lemma 4.8 (Satz 9, p. 10)", ""),
    ("buser1992", "buser1992.bib", "https://zbmath.org/bibtex/0770.53001.bib", "REQUIRED",
     "Lemma 4.8 (Lemma 6.6.4); Huber's theorem (Thm 9.2.9 in the 2010 reprint numbering)",
     "1992 edition. The DOI 10.1007/978-0-8176-4992-0 belongs to the 2010 reprint; do not mix."),
    ("wolpert1979", "wolpert1979_zb.bib", "https://zbmath.org/bibtex/0441.30055.bib", "REQUIRED",
     "Remark 4.13",
     "zbMATH used because Crossref gives pages '323' only."),
    ("stanhope2005", "stanhope2005.bib", "https://doi.org/10.1007/s10455-005-1584-7", "REQUIRED",
     "Sec. 1.1 first paragraph (Main Thms 1--2)", ""),
    ("dryden2004", "dryden2004.arxiv.xml", "http://export.arxiv.org/api/query?id_list=math/0411290", "REQUIRED",
     "Sec. 1.1 (Thm 4.5); before Thm 4.9 (proof of Thm 4.5, p. 9); Remark 4.13 (Thm 5.1)",
     "Converted from the arXiv Atom record. No journal version found (Crossref, zbMATH)."),
    ("garbinjorgenson2020", "garbinjorgenson2020.bib", "https://doi.org/10.2996/kmj/1584345689", "REQUIRED",
     "Thm 4.6 (Remark 2.7, eq. (2.8), p. 101)",
     "Crossref record has no pages; the published PDF header reads 'KODAI MATH. J. 43 (2020), 84--128'."),
    ("gordon2012orbifolds", "gordon2012orbifolds_zb.bib", "https://zbmath.org/bibtex/1326.58016.bib", "OPTIONAL (survey; unread)",
     "Sec. 1.1, as background only",
     "Text not read (AMS 429). zbMATH omits the series: Proc. Sympos. Pure Math. 84 is in the DOI."),
    ("schueth2025", "schueth2025.bib", "https://doi.org/10.1007/s10455-025-10024-1", "REQUIRED",
     "l. 220, alongside ucar2017",
     "Crossref record has no pages; the article is no. 2 of vol. 69 (Crossref article-number)."),
    ("philippe2008", "philippe2008_zbmath.bib", "https://zbmath.org/bibtex/1202.20049.bib", "REQUIRED",
     "Sec. 1.1 (Thm A); optionally Sec. 5",
     "zbMATH gives an English translation of the title. The paper's title is French: "
     "'Les groupes de triangles (2,p,q) sont d\\'etermin\\'es par leur spectre des longueurs' "
     "(Crossref record philippe2008.bib, whose title field carries raw MathML)."),
    ("philippe2010gd", "philippe2010gd_zbmath.bib", "https://zbmath.org/bibtex/1248.20053.bib", "REQUIRED",
     "Sec. 1.1 (rigidity of all triangle groups (r,p,q))",
     "Text not read (paywall); its theorem was read as Thm 3.1 of philippe2010tsg. "
     "zbMATH translates the French title 'Sur la rigidit\\'e des groupes de triangles (r,p,q)'."),
    ("philippe2010tsg", "philippe2010tsg.bib", "https://doi.org/10.5802/tsg.280", "OPTIONAL",
     "Sec. 1.1 or Sec. 5 (systolic twins, Thm 3.1, pp. 117--118)", ""),
    ("changdeturck1989", "changdeturck1989_zbmath.bib", "https://zbmath.org/bibtex/0721.58053.bib", "RECOMMENDED",
     "l. 178 next to griesermaronna2013",
     "zbMATH used because Crossref gives pages '1033--1033'. The zbMATH record carries the JSTOR DOI; "
     "take the AMS DOI from the Crossref record changdeturck1989.bib if preferred. Text not read (AMS 429)."),
    ("watson2005", "watson2005.bib", "https://zbmath.org/bibtex/1076.35042.bib", "RECOMMENDED",
     "l. 220/224: Ucar's (4.25) is Watson's lune expansion [Wat05, Lemma 15] reproved with corrections",
     "Text not read; attribution rests on Ucar pp. 134, 144."),
    ("strohmaieruski2013correction", "strohmaieruski2013_correction.bib", "https://doi.org/10.1007/s00220-018-3094-z",
     "RECOMMENDED", "with strohmaieruski2013", "Text not read (Springer JS shell)."),
    ("ngsolve", "ngsolve_swmath.json", "https://api.zbmath.org/v1/software/_search?search_string=NGSolve", "REQUIRED",
     "l. 1286 and l. 1578 (the finite-element solver; schoberl1997 is NETGEN only)",
     "Converted from the swMATH software record 13154. The usual NGSolve reference (J. Sch\\\"oberl, "
     "C++11 implementation of finite elements in NGSolve, ASC Report 30/2014, TU Wien) has no DOI and no "
     "Crossref/zbMATH record and could not be fetched (instrument gap); cite it only after fetching it."),
    # --- stability ---------------------------------------------------------------------
    ("aby2015", "aby2015.bib", "https://doi.org/10.1109/sampta.2015.7148965", "RECOMMENDED",
     "Sec. 6, beside Ostrowski (l. 1136): exponent 1/(2l-1) with unknown weights", ""),
    ("bgy2020", "bgy2020.bib", "https://doi.org/10.1093/imaiai/iaaa005", "RECOMMENDED",
     "Sec. 6, beside Ostrowski (l. 1136)",
     "Crossref year 2020 is the online date; the issue is vol. 10 no. 2 (2021). Erratum DOI 10.1093/imaiai/iaaa015."),
    ("batenkovyomdin2013", "batenkovyomdin2013.bib", "https://doi.org/10.1137/110836584", "OPTIONAL",
     "Sec. 6 (singularities of the Prony map at node collisions)", ""),
    # --- arithmetic and power sums -----------------------------------------------------
    ("borweiningalls1994", "borweiningalls1994.zbmath.json",
     "https://api.zbmath.org/v1/document/_search?search_string=an:0810.11016", "REQUIRED",
     "Thm A recalibration (Prop. 1 and Sec. 3); Prop. 3.9 (Prouhet); Problems 1--2; l. 1487 (ideal PTE solutions)",
     "Converted from the zbMATH API record (the zbMATH BibTeX endpoint returned a Cloudflare challenge). "
     "Read in the authors' preprint (CECM, 13 Dec 1993); published numbering unverified."),
    ("kelly1989", "kelly1989.bib", "https://doi.org/10.1090/s0002-9939-1989-0984800-0", "REQUIRED",
     "Thm 8.9 (l. 1426): classes of every size for equal sum and product", "Abstract read; body not read (AMS 429)."),
    ("kelly1964", "kelly1964.bib", "https://doi.org/10.1090/s0002-9939-1964-0168542-2", "OPTIONAL",
     "Sec. 8.4, per-sum existence of classes", "Body not read (AMS 429); content via Cha et al. arXiv:1811.07451."),
    ("zhangcai2013", "zhangcai2013.bib", "https://doi.org/10.1090/s0025-5718-2012-02609-3", "REQUIRED",
     "Thm 8.9 (l. 1426)",
     "Crossref year 2012 is the online date; the volume is Math. Comp. 82 (2013). Body not read (AMS 429)."),
    ("bremnerguy1997", "bremnerguy1997.bib", "https://doi.org/10.1017/s0013091500023397", "RECOMMENDED",
     "Sec. 8.1 after Prop. 8.1 (the sum--product invariant e1^3/e3)", ""),
    ("sadekelsissi2015", "sadekelsissi2015.arxiv.xml", "http://export.arxiv.org/api/query?id_list=1303.6705",
     "RECOMMENDED", "Remark 8.6 (isosceles triples are torsion) and l. 1364",
     "Converted from the arXiv Atom record (journal_ref Osaka J. Math. 52 (2015) 515--525); the JaLC DOI "
     "10.18910/57678 does not resolve by content negotiation."),
    ("schoen1988", "schoen1988.bib", "https://doi.org/10.1007/bf01215188", "OPTIONAL",
     "Sec. 8.1/8.4 (fibre-product frame for Conjecture 8.10)", "Body not read (paywall)."),
    ("guy2004", "guy2004.bib", "https://doi.org/10.1007/978-0-387-26677-0", "OPTIONAL",
     "Sec. 8 introduction (problem D16)", "D16 not read (archive.org lending only); check wording before quoting."),
    ("nguyen2021", "nguyen2021.bib", "https://doi.org/10.33039/ami.2021.04.005", "OPTIONAL",
     "Sec. 8.1 (no positive points when 4 | n)",
     "Crossref volume field reads 'Accepted manuscript' (a Crossref error); the PDF prints Ann. Math. Inform. 54 (2021) 141--146."),
]


def rekey(raw: str, key: str) -> str:
    raw = raw.strip()
    return re.sub(r"^@(\w+)\{[^,]*,", lambda m: "@%s{%s," % (m.group(1), key), raw, count=1)


def from_arxiv(path: Path, key: str) -> str:
    ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    e = ET.parse(path).getroot().find("a:entry", ns)
    title = " ".join(e.find("a:title", ns).text.split())
    authors = " and ".join(a.find("a:name", ns).text for a in e.findall("a:author", ns))
    aid = e.find("a:id", ns).text.rsplit("/abs/", 1)[1]
    year = e.find("a:published", ns).text[:4]
    jr = e.find("arxiv:journal_ref", ns)
    fields = [("author", authors), ("title", "{%s}" % title), ("year", year),
              ("eprint", re.sub(r"v\d+$", "", aid)), ("archivePrefix", "arXiv")]
    if jr is not None:
        fields.append(("note", " ".join(jr.text.split())))
    body = ",\n".join("  %s = {%s}" % f for f in fields)
    return "@misc{%s,\n%s}" % (key, body)


def from_zbmath_doc(path: Path, key: str) -> str:
    r = json.loads(path.read_text())["result"][0]
    authors = " and ".join(a["name"] for a in r["contributors"]["authors"])
    src = r["source"][0] if isinstance(r.get("source"), list) else r["source"]
    ser = src["series"][0] if src.get("series") else {}
    title = r["title"]["title"]
    fields = [("author", authors), ("title", "{%s}" % title),
              ("journal", ser.get("title", "")), ("volume", ser.get("volume", "")),
              ("pages", src.get("pages", "").replace("-", "--")), ("year", r.get("year", "")),
              ("note", "Zbl " + r["identifier"])]
    body = ",\n".join("  %s = {%s}" % f for f in fields if f[1])
    return "@article{%s,\n%s}" % (key, body)


def from_swmath(path: Path, key: str) -> str:
    r = next(x for x in json.loads(path.read_text())["result"] if x["name"] == "NGSolve")
    fields = [("author", " and ".join(r["authors"])), ("title", "{%s}" % r["name"]),
              ("howpublished", r["homepage"]), ("note", "swMATH %d, %s" % (r["id"], r["zbmath_url"]))]
    body = ",\n".join("  %s = {%s}" % f for f in fields)
    return "@misc{%s,\n%s}" % (key, body)


def main() -> None:
    parts = ["% references-additions.bib -- generated by review/literature-pass/build_additions.py.",
             "% Every entry is a fetched record (Crossref/DataCite content negotiation, zbMATH BibTeX,",
             "% or a mechanical conversion of a fetched zbMATH/arXiv record). Only citation keys were",
             "% changed. Defects of the fetched records are listed in the comment above each entry and",
             "% must be fixed in paper/jga/tools/build_bib.py when an entry is adopted.", ""]
    for key, fname, url, prio, where, notes in BIB:
        p = RAW / fname
        if fname.endswith(".bib"):
            entry = rekey(p.read_text(encoding="utf-8"), key)
        elif fname.endswith(".xml"):
            entry = from_arxiv(p, key)
        elif fname.startswith("ngsolve"):
            entry = from_swmath(p, key)
        else:
            entry = from_zbmath_doc(p, key)
        parts.append("%% [%s] source: %s" % (prio, url))
        parts.append("%% cite at: %s" % where)
        if notes:
            parts.append("%% record note: %s" % notes)
        parts.append(entry)
        parts.append("")
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print("wrote %d entries to %s" % (len(BIB), OUT))


if __name__ == "__main__":
    main()
