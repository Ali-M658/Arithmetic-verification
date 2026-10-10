#!/usr/bin/env python3
"""Build paper/arith/references.bib from fetched bibliographic records only.

Each entry is assembled from a record retrieved by this script: a DOI resolved by content
negotiation (CSL-JSON from Crossref), a zbMATH Open API record, or an arXiv API record. The
PARI/GP entry describes software with no registry record; its fields are read off the fetched
release changelog. The companion paper is the authors' own submitted manuscript and has no
external record. Corrections to a fetched record are listed in CORRECTIONS with their evidence.

    python3 paper/arith/tools/build_bib.py --fetch   # download raw records into paper/arith/fetched/
    python3 paper/arith/tools/build_bib.py           # assemble references.bib and SOURCES.md

The raw records are not committed (paper/arith/fetched/ is git-ignored); SOURCES.md lists the
URL and SHA-256 of each one as fetched for this build.
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

HERE = Path(__file__).resolve().parent.parent          # paper/arith
RAW = HERE / "fetched"
OUT = HERE / "references.bib"
LOG = HERE / "SOURCES.md"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) bibliography-build"}

# key -> (kind, identifier)
SOURCES = {
    "bgn1993": ("doi", "10.1090/s0025-5718-1993-1189516-5"),
    "beauville1982": ("zbmath", "0504.14016"),
    "schinzel1996": ("zbmath", "0932.11019"),
    "mazur1977": ("doi", "10.1007/bf02684339"),
    "kelly1989": ("doi", "10.1090/s0002-9939-1989-0984800-0"),
    "zhangcai2013": ("doi", "10.1090/s0025-5718-2012-02609-3"),
    "bremnerguy1997": ("doi", "10.1017/s0013091500023397"),
    "sadekelsissi2015": ("arxiv", "1303.6705"),
    "ysv2024": ("doi", "10.3336/gm.60.1.04"),
    "schoen1988": ("doi", "10.1007/bf01215188"),
    "dggw2008": ("doi", "10.1307/mmj/1213972406"),
    "crameri2020": ("doi", "10.1038/s41467-020-19160-7"),
    "crameri2023": ("doi", "10.5281/zenodo.8409685"),
    "pari2172": ("document", "https://pari.math.u-bordeaux.fr/pub/pari/OLD/2.17/pari-2.17.2.changelog"),
}
# Records fetched only as evidence for a correction.
EVIDENCE_ZB = {"dggw2008_pages": "doi:10.1307/mmj/1213972406"}

# Corrections applied to fetched records; each is justified by a fetched document.
CORRECTIONS = {
    # zbMATH doubles a word in the title; the first page of the paper (fetched in the G5 audit,
    # review/audit/fetches.md) prints this title.
    ("schinzel1996", "title"): "Triples of positive integers with the same sum and the same product",
    # zbMATH drops the accent; the printed title (Gallica scan, review/literature-pass/_fetched/pdf/
    # beauville1982.pdf, p. 657) has it.
    ("beauville1982", "title"): "Les familles stables de courbes elliptiques sur $\\mathbf{P}^1$ admettant quatre fibres singuli{\\`e}res",
}


def get(url, headers=None, tries=3):
    h = dict(UA)
    if headers:
        h.update(headers)
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=90) as r:
                return r.read()
        except Exception:  # noqa: BLE001
            if k == tries - 1:
                raise
            time.sleep(3)


def zb_url(query):
    q = urllib.parse.quote(query)
    return f"https://api.zbmath.org/v1/document/_search?search_string={q}&page=0&results_per_page=1"


def urls():
    out = {}
    for key, (kind, ident) in SOURCES.items():
        if kind == "doi":
            out[f"{key}.json"] = ("https://doi.org/" + ident, {"Accept": "application/vnd.citationstyles.csl+json"})
        elif kind == "zbmath":
            out[f"{key}.json"] = (zb_url("an:" + ident), None)
        elif kind == "arxiv":
            out[f"{key}.xml"] = ("https://export.arxiv.org/api/query?id_list=" + ident, None)
        else:
            out[f"{key}.document"] = (ident, None)
    for key, q in EVIDENCE_ZB.items():
        out[f"{key}.json"] = (zb_url(q), None)
    return out


def fetch_all():
    RAW.mkdir(parents=True, exist_ok=True)
    for name, (url, hdr) in urls().items():
        (RAW / name).write_bytes(get(url, hdr))
        time.sleep(1)


def names(lst):
    # The Crossref record of ysv2024 deposits the affiliations as extra name-only "authors"
    # (no family name); those entries are not authors and are skipped.
    lst = [a for a in lst if a.get("family")]
    return " and ".join(f"{a['family']}, {a['given']}" if a.get("given") else a["family"] for a in lst)


def year_of(d):
    for k in ("journal-issue", "published-print", "issued"):
        v = d.get(k)
        if isinstance(v, dict) and k == "journal-issue":
            v = v.get("published-print") or v.get("published-online")
        if v and v.get("date-parts") and v["date-parts"][0] and v["date-parts"][0][0]:
            return str(v["date-parts"][0][0])
    raise SystemExit("no year")


def from_csl(key):
    d = json.loads((RAW / f"{key}.json").read_text(encoding="utf-8"))
    title = d["title"] if isinstance(d["title"], str) else d["title"][0]
    title = " ".join(title.replace("’", "'").split())
    title = CORRECTIONS.get((key, "title"), title)
    cont = d.get("container-title")
    cont = cont[0] if isinstance(cont, list) and cont else cont
    if d.get("type") not in ("journal-article", "article-journal"):  # DataCite software record
        ver = d.get("version", "")
        f = {"author": names(d["author"]), "title": "{" + title + "}", "howpublished": d.get("publisher", ""),
             "note": f"Version {ver}" if ver else "", "year": year_of(d), "doi": d["DOI"]}
        f = {k: v for k, v in f.items() if v}
        body = ",\n".join(f"  {k:<12} = {{{v}}}" for k, v in f.items())
        return f"@misc{{{key},\n{body}\n}}"
    f = {"author": names(d["author"]), "title": "{" + title + "}", "journal": cont,
         "volume": d.get("volume", ""), "number": d.get("issue", ""), "pages": (d.get("page") or d.get("article-number", "")).replace("-", "--"),
         "year": year_of(d), "doi": d["DOI"]}
    if not f["pages"] and key == "dggw2008":
        r = json.loads((RAW / "dggw2008_pages.json").read_text())["result"][0]
        assert any(l.get("identifier", "").lower() == SOURCES[key][1] for l in r.get("links", []) if l.get("type") == "doi"), "zbMATH record is not DGGW"
        f["pages"] = r["source"]["pages"].replace("-", "--")
    f = {k: v for k, v in f.items() if v}
    body = ",\n".join(f"  {k:<7} = {{{v}}}" for k, v in f.items())
    return f"@article{{{key},\n{body}\n}}"


def from_zbmath(key):
    r = json.loads((RAW / f"{key}.json").read_text())["result"][0]
    assert r["identifier"] == SOURCES[key][1], key
    authors = " and ".join(a["name"] for a in r["contributors"]["authors"])
    title = CORRECTIONS.get((key, "title"), r["title"]["title"])
    ser = r["source"]["series"][0]
    issue = ser.get("issue") or ""
    pages = r["source"]["pages"].replace("-", "--")
    f = {"author": authors, "title": "{" + title + "}", "journal": ser["title"], "volume": ser["volume"],
         "number": issue, "pages": pages, "year": ser["year"], "note": "Zbl " + r["identifier"]}
    f = {k: v for k, v in f.items() if v}
    body = ",\n".join(f"  {k:<7} = {{{v}}}" for k, v in f.items())
    return f"@article{{{key},\n{body}\n}}"


def from_arxiv(key):
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    e = ET.parse(RAW / f"{key}.xml").getroot().find("a:entry", ns)
    title = " ".join(e.find("a:title", ns).text.split())
    authors = " and ".join(a.find("a:name", ns).text for a in e.findall("a:author", ns))
    aid = SOURCES[key][1]
    jr = e.find("x:journal_ref", ns)
    if jr is None:  # preprint
        year = e.find("a:published", ns).text[:4]
        return (f"@misc{{{key},\n  author = {{{authors}}},\n  title  = {{{title}}},\n"
                f"  year   = {{{year}}},\n  note   = {{Preprint, arXiv:{aid}}}\n}}")
    jref = jr.text.strip()
    m = re.match(r"Osaka J\. Math\.,? Volume (\d+), Number (\d+), (\d{4}), (\d+)-(\d+)", jref)
    assert m, jref
    vol, num, year, p1, p2 = m.groups()
    aid = SOURCES[key][1]
    return (f"@article{{{key},\n  author  = {{{authors}}},\n  title   = {{{title}}},\n"
            f"  journal = {{Osaka J. Math.}},\n  volume  = {{{vol}}},\n  number  = {{{num}}},\n"
            f"  pages   = {{{p1}--{p2}}},\n  year    = {{{year}}},\n  note    = {{arXiv:{aid}}}\n}}")


def from_document(key):
    text = (RAW / f"{key}.document").read_text(encoding="utf-8", errors="replace")
    m = re.search(r"Done for version 2\.17\.2 \(released (\d\d)/(\d\d)/(\d{4})\)", text)
    assert m, "release line not found in the changelog"
    year = m.group(3)
    return (f"@misc{{{key},\n  author       = {{{{The PARI~Group}}}},\n"
            f"  title        = {{{{PARI/GP}} version 2.17.2}},\n"
            f"  howpublished = {{Univ. Bordeaux, \\url{{https://pari.math.u-bordeaux.fr/}}}},\n  year         = {{{year}}},\n"
            f"  url          = {{https://pari.math.u-bordeaux.fr/}}\n}}")


COMPANION = """@unpublished{gangetal-heat,
  author = {Gang, Palaash and Agadi, Akshaj and Veluri, Arjun and Wang, Jerry and Barreto, Jeremy and Chouthaiwale, Aarin},
  title  = {How much of a hyperbolic orbifold does heat hear?},
  note   = {Preprint, arXiv:\\textbf{[PLACEHOLDER: arXiv number of Paper A]}},
  year   = {2026}
}"""


def tidy(b):
    b = b.replace("‐", "-").replace("–", "--").replace("—", "---")
    return re.sub(r"(?<!\\)&", r"\\&", b)


def build():
    entries, rows = [], []
    for key, (kind, ident) in SOURCES.items():
        entries.append(tidy({"doi": from_csl, "zbmath": from_zbmath, "arxiv": from_arxiv,
                             "document": from_document}[kind](key)))
    entries.append(COMPANION)
    for name, (url, _) in urls().items():
        rows.append(f"| `{name}` | {url} | `{hashlib.sha256((RAW / name).read_bytes()).hexdigest()}` |")
    OUT.write_text("% Generated by paper/arith/tools/build_bib.py from fetched records; do not edit.\n\n"
                   + "\n\n".join(entries) + "\n", encoding="utf-8")
    corr = "\n".join(f"- `{k}` {f}: {v}" for (k, f), v in CORRECTIONS.items())
    LOG.write_text(
        "# Bibliography sources of the arithmetic note\n\n"
        "Generated by `tools/build_bib.py`. Every entry of `references.bib` is assembled from the\n"
        "record fetched from the URL below (the raw records are in the git-ignored `fetched/`).\n"
        "`gangetal-heat` is the companion paper by the same authors (Paper A), cited by its arXiv\n"
        "number once posted; it has no external record.\n\n| record | fetched from | SHA-256 |\n|---|---|---|\n" + "\n".join(rows)
        + "\n\n## Corrections to fetched records\n\n" + corr + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(entries)} entries) and {LOG}")


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        fetch_all()
    build()
