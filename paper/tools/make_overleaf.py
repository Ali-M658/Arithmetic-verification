"""Build the Overleaf packages of Paper A, Paper B and the arithmetic note (Integers version) as zip files
in ~/Desktop/release/overleaf/ (outside this repository), and test-compile each from a fresh unzip.

    python3 paper/tools/make_overleaf.py [--out DIR]

Build the papers first (latexmk in paper/jga twice, then paper/eigen; python3 make_integers.py in
paper/arith/integers): Paper B's references to Paper A are replaced by their numbers, read from
paper/jga/build/manuscript.aux, because the two papers are separate Overleaf projects.

Each package compiles with pdfLaTeX and BibTeX, with no shell escape, no absolute paths and no build
products. The sources are those of this repository with three changes: comments are removed (they name
files of this repository), figures are read from figures/ next to the main file, and the captions file
is captions.tex next to it. Paper A keeps its manuscript-supplement cross-references (xr): its latexmkrc
has the rule that Overleaf documents for xr, which compiles the other document when its .aux is
missing. The note carries its bibliography inline (Integers format); references.bib is included as the
record of its sources.

Every package is unzipped into a temporary directory and compiled with latexmk (each root file of
Paper A in turn); the log must have no errors and no undefined references or citations. The results
are printed and written to OVERLEAF-TEST.md in the output directory.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_arxiv import labels, strip_comments  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.expanduser("~/Desktop/release/overleaf")
if "--out" in sys.argv:
    OUT = os.path.abspath(sys.argv[sys.argv.index("--out") + 1])

FORBIDDEN = [r"review/", r"round1", r"referee", r"\bjga\b", r"paper/", r"theory/", r"numerics/", r"figures/out",
             r"figures/gen", r"figures/src", r"code/run", r"\.\./", r"/Users/", r"hyperbolic-pillow", r"Ali-M658",
             r"Arithmetic-verification", r"maintained by", r"Journal of Geometric Analysis", r"Claude", r"Anthropic",
             r"Co-Authored", r"VERDICT", r"SPEC\.md", r"CONVENTIONS"]
BUILD_PRODUCTS = (".aux", ".bbl", ".blg", ".log", ".out", ".fls", ".fdb_latexmk", ".toc", ".synctex.gz", ".xdv")

XR_LATEXMKRC = r"""# Overleaf: compile with pdfLaTeX; BibTeX runs automatically.
# The manuscript and the supplement cross-reference each other with the xr package. The rule below is the
# one Overleaf documents for xr: when one document needs the .aux of the other and it is missing or out of
# date, latexmk first compiles the other document. Compile either root file; the first compile of a fresh
# project builds both.
$pdf_mode = 1;
$bibtex_use = 2;
add_cus_dep('tex', 'aux', 0, 'makeexternaldocument');
sub makeexternaldocument {
    if (!($root_filename eq $_[0])) {
        return system("latexmk -pdf \"$_[0]\"");
    }
    return 0;
}
"""
PLAIN_LATEXMKRC = """# Overleaf: compile with pdfLaTeX; BibTeX runs automatically.
$pdf_mode = 1;
$bibtex_use = 2;
"""
NOTE_LATEXMKRC = """# Overleaf: compile with pdfLaTeX. The bibliography is written inline in note.tex (Integers format), so
# BibTeX is not run; references.bib is the record of the sources.
$pdf_mode = 1;
$bibtex_use = 0;
"""

README_A = """# Overleaf package: How much of a hyperbolic orbifold does heat hear?

- **Compiler:** pdfLaTeX (Menu > Settings > Compiler). BibTeX runs automatically. No shell escape is needed.
- **Main document:** `manuscript.tex` (Menu > Settings > Main document).
- **The supplement** is the second root file, `supplement.tex`, the electronic supplementary material
  (Online Resource 1). To compile it, set the main document to `supplement.tex` and recompile; switch back
  to `manuscript.tex` afterwards.
- The two documents cross-reference each other through the `xr` package (labels such as `S-...` in the
  manuscript and `P-...` in the supplement). `latexmkrc` holds the rule that Overleaf documents for `xr`:
  when one document needs the other's `.aux`, the other document is compiled first. If a reference shows
  as `??` after the first compile of a new project, recompile once.
- Template: Springer Nature LaTeX template, `sn-jnl.cls` and the reference style `sn-mathphys-num.bst`,
  unmodified.
- Files: `manuscript.tex`, `supplement.tex`, `captions.tex` (figure captions), `references.bib`,
  `figures/` (every figure, PDF), `sn-jnl.cls`, `sn-mathphys-num.bst`, `latexmkrc`.
- Code and data: https://github.com/pa1aash/heat-invariants-orbifolds
- Before submission, fill the placeholders: author contributions, the AI-use statement, the Zenodo DOI,
  and the arXiv numbers of the companion papers.
"""
README_B = """# Overleaf package: Finitely many eigenvalues determine the signature of a hyperbolic orbifold

- **Compiler:** pdfLaTeX (Menu > Settings > Compiler). BibTeX runs automatically. No shell escape is needed.
- **Main document:** `manuscript.tex`. There is no second root file.
- References to the companion paper (*How much of a hyperbolic orbifold does heat hear?*) are printed with
  their numbers in that paper ("Theorem 3.7 of [..]"); they were resolved when this package was built,
  because the two papers are separate projects.
- Template: Springer Nature LaTeX template, `sn-jnl.cls` and the reference style `sn-mathphys-num.bst`,
  unmodified.
- Files: `manuscript.tex`, `captions.tex` (figure captions), `references.bib`, `figures/` (every figure,
  PDF), `sn-jnl.cls`, `sn-mathphys-num.bst`, `latexmkrc`.
- Code and data: https://github.com/pa1aash/eigenvalues-orbifold-signature
- Before submission, fill the placeholders: author contributions, the AI-use statement, the Zenodo DOI,
  and the arXiv number of the companion paper.
"""
README_N = """# Overleaf package: Triples with Equal Sum and Equal Reciprocal Sum (Integers version)

- **Compiler:** pdfLaTeX (Menu > Settings > Compiler). No shell escape is needed.
- **Main document:** `note.tex`.
- The bibliography is written inline in `note.tex` (`thebibliography`), in the format that *Integers*
  requires, so BibTeX is not run. `references.bib` holds the bibliographic records of the same sources and
  is not read during compilation.
- Template: the *Integers* article template, `integers.sty` and `erdos1.pdf` (placed in the header by the
  style's `\\maketitle`), unmodified.
- Files: `note.tex`, `references.bib`, `figures/F9.pdf`, `integers.sty`, `erdos1.pdf`, `latexmkrc`.
- Code and data: https://github.com/pa1aash/equal-sum-reciprocal-triples
- Before submission, fill the placeholders: author contributions, the AI-use statement, the Zenodo DOI,
  and the arXiv number of the companion paper.
"""


def clean(tex, main_name):
    """The source as it goes into a package: no comments, local figures and captions."""
    tex = strip_comments(tex)
    tex = re.sub(r"\\graphicspath\{\{(\.\./)+\}\}%?", r"\\graphicspath{{./}}%", tex)
    tex = tex.replace("\\input{../../figures/captions.tex}", "\\input{captions.tex}")
    tex = tex.replace(" in figures/captions.tex}", " in captions.tex}")
    tex = tex.replace("figures/out/", "figures/")
    return tex


def resolve_xr(tex, prefix, aux, name):
    lab = labels(aux)

    def num(m):
        key = m.group(1)[len(prefix):]
        if key not in lab:
            sys.exit(f"{name}: label {key} not found in {aux}")
        return lab[key]
    tex = re.sub(r"\\usepackage\{xr\}%?\n", "", tex)
    tex = re.sub(r"\\externaldocument\[[^\]]*\]\{[^}]*\}%?\n", "", tex)
    tex = re.sub(r"\\ref\*?\{(" + re.escape(prefix) + r"[^}]*)\}", num, tex)
    left = re.findall(r"\\ref\*?\{" + re.escape(prefix) + r"[^}]*\}", tex)
    if left:
        sys.exit(f"{name}: unresolved cross-document references {left[:5]}")
    return tex


def figures_in(tex):
    found = re.findall(r"\\paperfigure(?:\[[^\]]*\])?\{([EF]\d)\}", tex)
    found += re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{figures/([EF]\d)\.pdf\}", tex)
    return sorted(set(found))


def write_zip(name, files):
    """files: {path in zip: bytes}."""
    path = os.path.join(OUT, name + ".zip")
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for arc in sorted(files):
            info = zipfile.ZipInfo(f"{name}/{arc}", date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, files[arc])
    return path


def scan(name, files):
    for arc, data in files.items():
        if arc.endswith(BUILD_PRODUCTS):
            sys.exit(f"{name}: build product {arc}")
        if arc.endswith((".tex", ".bib", ".md", "latexmkrc")):
            body = data.decode("utf-8")
            for pat in FORBIDDEN:
                m = re.search(pat, body)
                if m:
                    sys.exit(f"{name}: forbidden /{pat}/ in {arc}: ..." + body[max(0, m.start() - 60):m.end() + 60] + "...")


def read(*p):
    return open(os.path.join(ROOT, *p), "rb").read()


def bib(*p):
    """A .bib file without its comment lines (they name the builder in this repository)."""
    lines = read(*p).decode("utf-8").splitlines()
    return ("\n".join(l for l in lines if not l.lstrip().startswith("%")).lstrip("\n") + "\n").encode("utf-8")


def package_a():
    files = {}
    for main in ("manuscript.tex", "supplement.tex"):
        tex = clean(open(os.path.join(ROOT, "paper", "jga", main), encoding="utf-8").read(), main)
        tex = tex.replace("\\externaldocument[S-]{build/supplement}", "\\externaldocument[S-]{supplement}")
        tex = tex.replace("\\externaldocument[P-]{build/manuscript}", "\\externaldocument[P-]{manuscript}")
        files[main] = tex.encode("utf-8")
    figs = sorted(set(figures_in(files["manuscript.tex"].decode()) + figures_in(files["supplement.tex"].decode())))
    for f in figs:
        files[f"figures/{f}.pdf"] = read("figures", "out", f + ".pdf")
    files["captions.tex"] = strip_comments(read("figures", "captions.tex").decode()).encode()
    for f in ("sn-jnl.cls", "sn-mathphys-num.bst"):
        files[f] = read("paper", "jga", f)
    files["references.bib"] = bib("paper", "jga", "references.bib")
    files["latexmkrc"] = XR_LATEXMKRC.encode()
    files["README-OVERLEAF.md"] = README_A.encode()
    return "paperA", files, ["manuscript.tex", "supplement.tex"], figs


def package_b():
    files = {}
    tex = clean(open(os.path.join(ROOT, "paper", "eigen", "manuscript.tex"), encoding="utf-8").read(), "manuscript.tex")
    tex = resolve_xr(tex, "A-", os.path.join(ROOT, "paper", "jga", "build", "manuscript.aux"), "paperB")
    files["manuscript.tex"] = tex.encode("utf-8")
    figs = figures_in(tex)
    for f in figs:
        files[f"figures/{f}.pdf"] = read("figures", "out", f + ".pdf")
    files["captions.tex"] = strip_comments(read("figures", "captions.tex").decode()).encode()
    for f in ("sn-jnl.cls", "sn-mathphys-num.bst"):
        files[f] = read("paper", "eigen", f)
    files["references.bib"] = bib("paper", "eigen", "references.bib")
    files["latexmkrc"] = PLAIN_LATEXMKRC.encode()
    files["README-OVERLEAF.md"] = README_B.encode()
    return "paperB", files, ["manuscript.tex"], figs


def package_note():
    files = {}
    tex = clean(open(os.path.join(ROOT, "paper", "arith", "integers", "note.tex"), encoding="utf-8").read(), "note.tex")
    files["note.tex"] = tex.encode("utf-8")
    figs = figures_in(tex)
    for f in figs:
        files[f"figures/{f}.pdf"] = read("figures", "out", f + ".pdf")
    for f in ("integers.sty", "erdos1.pdf"):
        files[f] = read("paper", "arith", "integers", f)
    files["references.bib"] = bib("paper", "arith", "references.bib")
    files["latexmkrc"] = NOTE_LATEXMKRC.encode()
    files["README-OVERLEAF.md"] = README_N.encode()
    return "note", files, ["note.tex"], figs


def test(name, zpath, roots):
    """Unzip into a fresh directory and compile every root file with latexmk."""
    res = []
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(zpath) as z:
            z.extractall(tmp)
        d = os.path.join(tmp, name)
        for main in roots:
            p = subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", main], cwd=d,
                               capture_output=True, text=True)
            log = open(os.path.join(d, main.replace(".tex", ".log")), encoding="utf-8", errors="replace").read()
            errors = re.findall(r"^!.*", log, re.M)
            undef = re.findall(r"(?:Reference|Citation) `[^']*' on page \d+ undefined|There were undefined references", log)
            info = subprocess.run(["pdfinfo", main.replace(".tex", ".pdf")], cwd=d, capture_output=True, text=True).stdout
            pages = int(re.search(r"Pages:\s+(\d+)", info).group(1)) if "Pages:" in info else 0
            # TeX Live's default is the restricted mode ("restricted \write18 enabled"), which runs only a
            # fixed list of safe programs; full shell escape (-shell-escape) prints " \write18 enabled."
            shell = "full shell escape" if re.search(r"^ \\write18 enabled", log, re.M) else "none (restricted default)"
            res.append((main, p.returncode, pages, len(errors), len(undef), shell))
            if p.returncode or errors or undef or not pages:
                print(p.stdout[-3000:])
                sys.exit(f"{name}/{main}: latexmk exit {p.returncode}, {len(errors)} errors {errors[:3]}, "
                         f"{len(undef)} undefined {undef[:3]}")
    return res


def main():
    os.makedirs(OUT, exist_ok=True)
    report = ["# Overleaf packages: test compile", "",
              "Each zip was unzipped into a fresh temporary directory and every root file compiled with "
              "`latexmk -pdf` (pdfLaTeX + BibTeX through the package's latexmkrc).", "",
              "| package | root file | pages | errors | undefined refs/cites | latexmk exit | shell escape used |",
              "|---|---|---|---|---|---|---|"]
    listing = []
    for build in (package_a, package_b, package_note):
        name, files, roots, figs = build()
        scan(name, files)
        zpath = write_zip(name, files)
        for main, rc, pages, ne, nu, shell in test(name, zpath, roots):
            report.append(f"| `{name}.zip` | `{main}` | {pages} | {ne} | {nu} | {rc} | {shell} |")
            print(f"{name}/{main}: {pages} pages, {ne} errors, {nu} undefined, exit {rc}, {shell}")
        listing.append(f"- `{name}.zip` ({os.path.getsize(zpath):,} bytes): " + ", ".join(f"`{a}`" for a in sorted(files)))
    report += ["", "## Contents", ""] + listing
    open(os.path.join(OUT, "OVERLEAF-TEST.md"), "w", encoding="utf-8").write("\n".join(report) + "\n")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
