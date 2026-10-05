"""Compile test for the LaTeX fragments of theory/revision/.

Builds a throw-away document in a temporary directory with the manuscript's packages, theorem
environments and notation macros (read from paper/jga/manuscript.tex at run time, so they stay in
sync), inputs every fragment, and runs pdflatex twice with -halt-on-error.  Undefined references to
labels of the manuscript are expected and only counted.  Exits nonzero on any LaTeX error.

Run from the repository root:
    /opt/homebrew/Caskroom/miniforge/base/bin/python3 theory/revision/check_fragments.py
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MS = os.path.join(ROOT, "paper", "jga", "manuscript.tex")
FRAGMENTS = ["lemma25.tex", "remark412.tex", "locality.tex", "thm12iii.tex", "descent.tex", "thm513.tex",
             "remark212.tex", "prop610.tex", "point3P.tex", "sharpness.tex"]
WRAP = {"thm12iii.tex": ("\\begin{enumerate}[label=(\\roman*)]\\setcounter{enumi}{2}", "\\end{enumerate}")}

src = open(MS).read()
macros = "\n".join(l for l in src.splitlines() if l.startswith("\\newcommand{\\") and "figcap" not in l and "paperfigure" not in l)
doc = r"""\documentclass[11pt]{article}
\usepackage{amsmath,amssymb,amsfonts,amsthm,mathrsfs,enumitem,booktabs,url}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
""" + macros + "\n\\begin{document}\n\\section{Fragments}\\setcounter{section}{1}\n"
for f in FRAGMENTS:
    path = os.path.join(HERE, f)
    if not os.path.exists(path):
        print("missing fragment", f)
        sys.exit(1)
    pre, post = WRAP.get(f, ("", ""))
    doc += f"\n%% ---- {f}\n\\subsection*{{{f.replace('_', ' ')}}}\n{pre}\n\\input{{{path}}}\n{post}\n"
doc += "\n\\end{document}\n"

tmp = tempfile.mkdtemp(prefix="revision_tex_")
try:
    with open(os.path.join(tmp, "t.tex"), "w") as fh:
        fh.write(doc)
    for _ in range(2):
        p = subprocess.run(["pdflatex", "-halt-on-error", "-interaction=nonstopmode", "t.tex"], cwd=tmp,
                           capture_output=True, text=True)
    logtxt = open(os.path.join(tmp, "t.log"), errors="replace").read()
    errors = [l for l in logtxt.splitlines() if l.startswith("!")]
    undef = sorted(set(re.findall(r"Reference `([^']+)' on page", logtxt)))
    cites = sorted(set(re.findall(r"Citation `([^']+)' on page", logtxt)))
    pages = re.search(r"Output written on t\.pdf \((\d+) page", logtxt)
    print(f"pdflatex exit {p.returncode}; errors: {len(errors)}; pages: {pages.group(1) if pages else '?'}")
    for e in errors:
        print("  ", e)
    print(f"undefined references to manuscript labels ({len(undef)}): {', '.join(undef)}")
    print(f"citations (resolved by the manuscript's .bib): {', '.join(cites)}")
    ok = p.returncode == 0 and not errors
finally:
    shutil.rmtree(tmp, ignore_errors=True)
sys.exit(0 if ok else 1)
