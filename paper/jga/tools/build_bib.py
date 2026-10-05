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
    "pari2172": ("document", "https://pari.math.u-bordeaux.fr/pub/pari/OLD/2.17/pari-2.17.2.changelog"),
    # numerics
    "strohmaieruski2013": ("doi", "10.1007/s00220-012-1557-1"),
    "schoberl1997": ("doi", "10.1007/s007910050004"),
    "arpack1998": ("doi", "10.1137/1.9780898719628"),
    # colour maps used by the figures
    "crameri2023": ("doi", "10.5281/zenodo.8409685"),
    "crameri2020": ("doi", "10.1038/s41467-020-19160-7"),
}

# Documents with no registry record: fields read off the fetched document (SOURCES.md).
# thurston1980: title page of the fetched chapter ("Electronic version 1.1 - March 2002",
# "electronic edition of the 1980 notes distributed by Princeton University").
# pari2172: the fetched changelog ("Done for version 2.17.2 (released 01/03/2025)"); the
# version used is recorded in theory/diophantine/data/ranks.txt.
DOCUMENT_ENTRIES = {
    "thurston1980": """@misc{thurston1980,
  author       = {Thurston, William P.},
  title        = {The Geometry and Topology of Three-Manifolds},
  howpublished = {Lecture notes, Princeton University, 1980; electronic edition 1.1, 2002, Chapter 13, available at https://library.slmath.org/books/gt3m/},
  year         = {2002},
  url          = {https://library.slmath.org/books/gt3m/PDF/13.pdf}
}""",
    "pari2172": """@misc{pari2172,
  author       = {{The PARI~Group}},
  title        = {{PARI/GP} version 2.17.2},
  howpublished = {Univ. Bordeaux, released 1 March 2025; functions ellrank and elltors},
  year         = {2025},
  url          = {https://pari.math.u-bordeaux.fr/}
}""",
}

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


EVIDENCE = {"ostrowski1940_reprint": "10.1007/978-3-0348-9355-8_50"}
# Publisher locations missing from the Crossref record, read from zbMATH Open (the record is
# fetched as evidence and must contain the location string).
ADDRESS_ZB = {"arpack1998": ("0901.65021", "Philadelphia, PA"), "marklof2011": ("1282.11053", "Cambridge")}


def fetch_all():
    RAW.mkdir(parents=True, exist_ok=True)
    for key, doi in EVIDENCE.items():
        (RAW / f"{key}.json").write_bytes(get("https://doi.org/" + doi, {"Accept": "application/vnd.citationstyles.csl+json"}))
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
# Title corrections, each justified by a second fetched record (see SOURCES.md).
TITLE_FIX = {
    # Crossref lower-cases the two proper names; the Crossref record of the reprint in
    # Ostrowski's Collected Mathematical Papers (10.1007/978-3-0348-9355-8_50) has them.
    "ostrowski1940": ("graeffe", "Graeffe", "laurent", "Laurent"),
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


def from_csl(key, doi):
    d = json.loads((RAW / f"{key}.json").read_text(encoding="utf-8"))
    title = d["title"] if isinstance(d["title"], str) else d["title"][0]
    title = " ".join(title.replace("’", "'").split())
    for i in range(0, len(TITLE_FIX.get(key, ())), 2):
        a, b = TITLE_FIX[key][i:i + 2]
        title = title.replace(a, b)
    braced = "{" + title + "}" if d.get("type") not in ("monograph", "book") else title
    f = {"author": names(d.get("author", [])), "title": braced, "year": year_of(d),
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
        f["journal"] = cont.replace("\u2019", "'")
    elif typ in ("book-chapter", "chapter"):
        kind = "incollection"
        f["booktitle"] = cont
        f["publisher"] = d.get("publisher", "")
    elif typ in ("monograph", "book"):
        kind = "book"
        f["publisher"] = d.get("publisher", "")
    else:  # DataCite records (software, datasets)
        kind = "misc"
        f["howpublished"] = d.get("publisher", "")
        f["note"] = "Software, version of record DOI " + f["doi"]
    body = ",\n".join(f"  {k:<9}= {{{v}}}" for k, v in f.items())
    return f"@{kind}{{{key},\n{body}\n}}"


def from_arxiv(key, aid):
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    root = ET.parse(RAW / "arxiv.xml").getroot()
    for e in root.findall("a:entry", ns):
        eid = e.find("a:id", ns).text.rsplit("/abs/", 1)[1]
        if re.sub(r"v\d+$", "", eid) != aid:
            continue
        title = " ".join(e.find("a:title", ns).text.split())
        authors = [a.find("a:name", ns).text for a in e.findall("a:author", ns)]
        year = e.find("a:published", ns).text[:4]
        if key == "ucar2017":
            # The thesis title page (fetched PDF) spells the surname with a cedilla;
            # the arXiv author field is ASCII. Degree data are from the same title page.
            authors = ["Eren U{\\c{c}}ar"]
            return ("@phdthesis{ucar2017,\n"
                    f"  author = {{{' and '.join(authors)}}},\n"
                    f"  title  = {{{title}}},\n"
                    "  school = {Humboldt-Universit{\\\"a}t zu Berlin},\n"
                    f"  year   = {{{year}}},\n"
                    "  eprint = {1711.03405},\n"
                    "  note   = {arXiv:1711.03405}\n}")
        return (f"@misc{{{key},\n"
                f"  author = {{{' and '.join(authors)}}},\n"
                f"  title  = {{{title}}},\n"
                f"  year   = {{{year}}},\n"
                f"  eprint = {{{aid}}},\n"
                f"  note   = {{Preprint, arXiv:{aid}}}\n}}")
    raise SystemExit(f"arXiv id {aid} not in arxiv.xml")


def from_zbmath(key):
    d = json.loads((RAW / f"{key}.json").read_text())
    r = d["result"][0]
    authors = " and ".join(a["name"] for a in r["contributors"]["authors"])
    title = CORRECTIONS.get((key, "title"), r["title"]["title"])
    title = title.replace("\\(P^ 1 \\)", "$\\mathbf{P}^1$ ")
    ser = r["source"]["series"][0]
    pages = r["source"]["pages"].replace("-", "--")
    year = {"0238.10007": "1971"}.get(r["identifier"], ser["year"])
    return (f"@article{{{key},\n"
            f"  author  = {{{authors}}},\n"
            f"  title   = {{{title}}},\n"
            f"  journal = {{{ser['title']}}},\n"
            f"  volume  = {{{ser['volume']}}},\n"
            f"  pages   = {{{pages}}},\n"
            f"  year    = {{{year}}},\n"
            f"  note    = {{Zbl {r['identifier']}}}\n}}")


def tidy(b):
    b = b.replace("‐", "-").replace("–", "--").replace("—", "---")
    b = re.sub(r"\s+\}", "}", b)
    b = re.sub(r"(?<!\\)&", r"\\&", b)
    return b


def build():
    entries, log = [], []
    for key, (kind, ident) in SOURCES.items():
        if kind == "doi":
            e = from_csl(key, ident)
            log.append((key, f"https://doi.org/{ident}", sha(RAW / f"{key}.json")))
        elif kind == "arxiv":
            e = from_arxiv(key, ident)
            log.append((key, f"https://export.arxiv.org/api/query?id_list={ident}", sha(RAW / "arxiv.xml")))
        elif kind == "zbmath":
            e = from_zbmath(key)
            log.append((key, f"https://api.zbmath.org/v1/document/_search?search_string=an:{ident}", sha(RAW / f"{key}.json")))
        else:
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
