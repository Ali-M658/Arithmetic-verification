"""Build the arXiv source packages of Paper A (paper/jga) and Paper B (paper/eigen) in paper/arxiv/
(git-ignored), from the built papers (run latexmk in both first, Paper A before Paper B).

    python3 paper/tools/make_arxiv.py

Each package is self-contained, following arXiv's TeX submission guidance (info.arxiv.org/help/
submit_tex, ancillary_files): the main .tex with every comment removed and the figure captions
inlined, the class file, the figures, and the pre-generated .bbl named after the main file. arXiv
advises against xr, so every cross-document reference is replaced by its number, read from the .aux
of the built document: in Paper A the references to its supplement, in Paper B those to Paper A.
Paper A's supplement goes in as an ancillary file, anc/supplement.pdf. Each package is compiled in a
temporary copy (pdflatex twice, no BibTeX) and checked: no undefined references, the same page count
as the build, and no forbidden strings (repository paths, review history, the earlier target
journal). Writes paper/arxiv/paperA/, paper/arxiv/paperB/ and the two .tar.gz files.
"""
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "paper", "arxiv")
FORBIDDEN = [r"review/", r"round1", r"referee-round", r"referee", r"\bjga\b", r"paper/", r"theory/", r"numerics/",
             r"figures/gen", r"figures/src", r"code/run", r"CONVENTIONS", r"SPEC\.md", r"FIGURE-RESTORE",
             r"OUTSTANDING", r"VERDICT", r"Claude", r"Anthropic", r"Co-Authored"]


def strip_comments(tex):
    out = []
    for line in tex.split("\n"):
        m = re.search(r"(?<!\\)%", line)
        if m is None:
            out.append(line)
            continue
        code = line[:m.start()]
        if code.strip() == "":
            continue                       # a comment line: drop it
        out.append(code + "%")             # keep the % so that no space is introduced
    return "\n".join(out)


def labels(aux):
    lab = {}
    for line in open(aux, encoding="utf-8", errors="replace"):
        m = re.match(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}", line)
        if m:
            lab[m.group(1)] = m.group(2)
    return lab


def inline_captions(tex):
    cap = strip_comments(open(os.path.join(ROOT, "figures", "captions.tex"), encoding="utf-8").read())
    return tex.replace("\\input{../../figures/captions.tex}", cap)


def figures_used(tex, prefix):
    return sorted(set(re.findall(r"\\paperfigure(?:\[[^\]]*\])?\{(" + prefix + r"\d)\}", tex)))


def package(name, src_dir, main, xr_prefix, xr_aux, figprefix, anc=None):
    src = os.path.join(ROOT, "paper", src_dir)
    tex = open(os.path.join(src, main), encoding="utf-8").read()
    tex = inline_captions(tex)
    tex = strip_comments(tex)
    lab = labels(xr_aux)
    tex = re.sub(r"\\usepackage\{xr\}%?\n", "", tex)
    tex = re.sub(r"\\externaldocument\[[^\]]*\]\{[^}]*\}%?\n", "", tex)
    tex = tex.replace("\\graphicspath{{../../}}", "\\graphicspath{{./}}")

    def num(m):
        key = m.group(2) if m.group(1) == "sref" else m.group(2)[len(xr_prefix):]   # the .aux has no xr prefix
        if key not in lab:
            sys.exit(f"{name}: label {key} not found in {xr_aux}")
        return lab[key]
    if xr_prefix == "S-":
        tex = re.sub(r"\\newcommand\{\\sref\}\[1\]\{\\ref\*?\{S-#1\}\}%?\n", "", tex)
        tex = re.sub(r"\\(sref)\{([^}]*)\}", num, tex)
    else:
        tex = re.sub(r"\\(ref)\*?\{(A-[^}]*)\}", num, tex)
    left = re.findall(r"\\(?:sref|ref\*?)\{(?:S-|A-)[^}]*\}", tex)
    if left:
        sys.exit(f"{name}: unresolved cross-document references {left[:5]}")
    d = os.path.join(OUT, name)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(os.path.join(d, "figures", "out"))
    open(os.path.join(d, main), "w", encoding="utf-8").write(tex)
    shutil.copy(os.path.join(src, "sn-jnl.cls"), d)
    shutil.copy(os.path.join(src, "build", main.replace(".tex", ".bbl")), d)
    for f in figures_used(tex, figprefix):
        shutil.copy(os.path.join(ROOT, "figures", "out", f + ".pdf"), os.path.join(d, "figures", "out"))
    if anc:
        os.makedirs(os.path.join(d, "anc"))
        shutil.copy(anc, os.path.join(d, "anc", "supplement.pdf"))
    for root, _, files in os.walk(d):
        for f in files:
            if f.endswith((".tex", ".bbl")):
                body = open(os.path.join(root, f), encoding="utf-8").read()
                for pat in FORBIDDEN:
                    if re.search(pat, body):
                        sys.exit(f"{name}: forbidden string /{pat}/ in {f}: " + re.search(".{60}" + pat + ".{0,60}", body, re.S).group(0))
    # test build in a temporary copy
    with tempfile.TemporaryDirectory() as tmp:
        t = os.path.join(tmp, name)
        shutil.copytree(d, t)
        for _ in range(2):
            subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", main], cwd=t,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        log = open(os.path.join(t, main.replace(".tex", ".log")), encoding="utf-8", errors="replace").read()
        bad = re.findall(r"^!.*|Reference `[^']*' on page \d+ undefined|Citation `[^']*' on page \d+ undefined", log, re.M)
        if bad:
            sys.exit(f"{name}: package build problems: {bad[:5]}")
        pages = subprocess.run(["pdfinfo", main.replace(".tex", ".pdf")], cwd=t, capture_output=True, text=True).stdout
        npk = int(re.search(r"Pages:\s+(\d+)", pages).group(1))
        ref = subprocess.run(["pdfinfo", os.path.join(src, "build", main.replace(".tex", ".pdf"))], capture_output=True, text=True).stdout
        nref = int(re.search(r"Pages:\s+(\d+)", ref).group(1))
        if npk != nref:
            sys.exit(f"{name}: package has {npk} pages, the build {nref}")
    tgz = os.path.join(OUT, name + ".tar.gz")
    with tarfile.open(tgz, "w:gz") as tf:
        for root, _, files in os.walk(d):
            for f in sorted(files):
                p = os.path.join(root, f)
                tf.add(p, arcname=os.path.relpath(p, d))
    print(f"{name}: {npk} pages, {sum(len(fs) for _, _, fs in os.walk(d))} files, {tgz}")


def main():
    os.makedirs(OUT, exist_ok=True)
    package("paperA", "jga", "manuscript.tex", "S-", os.path.join(ROOT, "paper", "jga", "build", "supplement.aux"), "F",
            anc=os.path.join(ROOT, "paper", "jga", "build", "supplement.pdf"))
    package("paperB", "eigen", "manuscript.tex", "A-", os.path.join(ROOT, "paper", "jga", "build", "manuscript.aux"), "E")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
