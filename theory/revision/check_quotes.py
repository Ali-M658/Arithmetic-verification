"""Task 3: every quotation used in locality.tex (and the DS / Cremona inputs of lemma25.tex and
descent.tex) occurs in the fetched sources.

Comparison is after normalisation (lower case, letters and digits only), because the Huber scans and
the Buser snippets are OCR text; the Huber quotations were also checked against the page images
(locality-sources.md).  The cache is not committed: run fetch_sources.sh first for DS and Cremona;
the Huber, Hejhal-preview, zbMATH and Buser files come from the retrieval logged in
locality-sources.md.  Missing cache files are reported as SKIP (an instrument gap), not as a pass.

Run from the repository root:
    /opt/homebrew/Caskroom/miniforge/base/bin/python3 theory/revision/check_quotes.py
Writes theory/revision/check_quotes.txt.  Exits nonzero if a present source lacks its quotation.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "sources_cache")
OUT = os.path.join(HERE, "check_quotes.txt")

QUOTES = [
    ("ds_math0504571.txt", "Selberg's trace formula for orbisurfaces (see [7], [8]) reads", "DS p. 3, eq. (1)"),
    ("ds_math0504571.txt", "where h is any entire function of uniform exponential type and h(r) = h(-r)", "DS p. 3"),
    ("ds_math0504571.txt", "Dennis A. Hejhal. The Selberg trace formula for PSL(2, R). Vol. I", "DS ref. [7]"),
    ("ds_math0504571.txt", "Henryk Iwaniec. Spectral Methods of Automorphic Forms", "DS ref. [8]"),
    ("cremona_ch3.txt", "Method 1: descent using 2-isogeny", "Cremona 3.6, p. 84"),
    ("cremona_ch3.txt", "rank(E(Q)) = rank(E'(Q)) = e1 + e'1 - 2", "Cremona (3.6.2)"),
    ("cremona_ch3.txt", "for an odd prime p of good reduction (that is, p ∤2∆), the reduction map from E(Q)tors to E(Z/pZ) is injective", "Cremona 3.3, p. 70"),
    ("zbmath/hejhal*.json", "Hier werden erstmals auch Gruppen", "zbMATH Zbl 0347.10018"),
    ("zbmath/hejhal*.json", "mit kompaktem Quotienten zugelassen, welche elliptische Elemente enthalten", "zbMATH Zbl 0347.10018"),
    ("huber1961_II*ocr.txt", "allgemeinen Spurformel", "Huber II p. 388 fn. 4"),
    ("ia_fts/*", "Following McKean", "Buser (snippet)"),
    ("ia_fts/*", "plug the heat kernel", "Buser (snippet)"),
    ("ia_fts/*", "exp (L + 6) oriented closed", "Buser (snippet)"),
]


def norm(s):
    s = s.replace("′", "'").replace("−", "-")
    return re.sub(r"[^a-z0-9]", "", s.lower())


log, fails = [], 0
for pattern, quote, where in QUOTES:
    files = glob.glob(os.path.join(CACHE, pattern))
    if not files:
        log.append(f"SKIP {where}: no cached file {pattern} (instrument gap; run fetch_sources.sh)")
        continue
    hit = any(norm(quote) in norm(open(f, errors="replace").read().replace("\\n", " ")) for f in files)
    log.append(("PASS " if hit else "FAIL ") + f"{where}: \"{quote}\"")
    fails += 0 if hit else 1

with open(OUT, "w") as fh:
    fh.write("\n".join(log) + f"\n\n{len(log)} quotations, {fails} failures\n")
print("\n".join(log))
sys.exit(1 if fails else 0)
