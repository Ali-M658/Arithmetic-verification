"""Build paper/arith/integers/note.tex (the note in the format of Integers) from paper/arith/note.tex.

    python3 make_integers.py          (from this folder; then latexmk)

Every change to the body is an explicit substitution below, checked to apply exactly the expected
number of times, so the mathematics is carried over verbatim; README.md lists the changes and the
journal guidelines they follow. The bibliography is written here in the journal's format from the
records of ../references.bib.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
src_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "note.tex")
out_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "note.tex")
tex = open(src_path, encoding="utf-8").read()

# ---- body: from \section{Introduction} up to the acknowledgements --------------------------------
a = tex.index("\\section{Introduction}")
b = tex.index("\\section*{Acknowledgements}")
abstract = re.search(r"\\begin\{abstract\}\n(.*?)\n\\end\{abstract\}", tex, re.S).group(1)
body = tex[a:b]


def sub(old, new, count, s):
    n = s.count(old)
    if n != count:
        sys.exit(f"expected {count} x {old!r}, found {n}")
    return s.replace(old, new)


# Section and subsection titles: capitalised words (template guideline)
for old, new in [
    ("\\subsection{Relation to the literature}", "\\subsection{Relation to the Literature}"),
    ("\\section{The curves \\texorpdfstring{$C_\\Lambda$}{C\\_Lambda}}", "\\section{The Curves \\texorpdfstring{$C_\\Lambda$}{C\\_Lambda}}"),
    ("\\section{Reciprocation and the dual family}", "\\section{Reciprocation and the Dual Family}"),
    ("\\section{Lower bounds}", "\\section{Lower Bounds}"),
    ("\\section{Classes of every size}", "\\section{Classes of Every Size}"),
    ("\\section{Enumeration and growth}", "\\section{Enumeration and Growth}"),
    ("\\subsection{The enumeration}", "\\subsection{The Enumeration}"),
    ("\\subsection{An upper bound}", "\\subsection{An Upper Bound}"),
    ("\\subsection{What Conjecture~\\ref{conj:intro} would require}", "\\subsection{What Conjecture~\\ref{conj:intro} Would Require}"),
]:
    body = sub(old, new, 1, body)

# Oxford comma (template guideline), including lists of three names
body = sub("Bremner, Guy and Nowakowski", "Bremner, Guy, and Nowakowski", body.count("Bremner, Guy and Nowakowski"), body)
abstract = sub("Bremner, Guy and Nowakowski", "Bremner, Guy, and Nowakowski", 1, abstract)
for old, new in [
    ("of two, three and four triples", "of two, three, and four triples"),
    ("$[1200,4800]$, $[600,2400]$ and $[2400,4800]$ all pairs give $4.43$, $4.63$ and $4.37$",
     "$[1200,4800]$, $[600,2400]$, and $[2400,4800]$ all pairs give $4.43$, $4.63$, and $4.37$"),
    ("$\\Z/3$, $\\Z/6$ or $\\Z/2\\times\\Z/6$", "$\\Z/3$, $\\Z/6$, or $\\Z/2\\times\\Z/6$"),
    ("under permutations, reciprocation and translation", "under permutations, reciprocation, and translation"),
    ("$11$ of size $5$ and one of size $6$", "$11$ of size $5$, and one of size $6$"),
]:
    body = sub(old, new, 1, body)

# Numbered results, equations and cited items are written out in full (template guideline)
for old, new, n in [
    ("\\cite[Prop.~2.5, Thm~2.8]{sadekelsissi2015}", "\\cite[Proposition~2.5 and Theorem~2.8]{sadekelsissi2015}", 2),
    ("\\cite[Chap.~III, Cor.~(5.2), p.~156]{mazur1977}", "\\cite[Chapter~III, Corollary~(5.2), p.~156]{mazur1977}", 2),
    ("\\cite[Prop.~7.1]{schoen1988}", "\\cite[Proposition~7.1]{schoen1988}", 1),
    ("By \\eqref{eq:copies} and partial summation", "By Equation~\\eqref{eq:copies} and partial summation", 1),
    ("In \\eqref{eq:copies}, restrict", "In Equation~\\eqref{eq:copies}, restrict", 1),
    ("both conventions of \\eqref{eq:counts}", "both conventions of Equation~\\eqref{eq:counts}", 1),
]:
    body = sub(old, new, n, body)

# Only referenced displays are numbered (template guideline): (eq:weierstrass) is never referenced
body = sub("\\begin{equation}\\label{eq:weierstrass}", "\\[", 1, body)
body = sub("  \\Delta=2^{12}\\Lambda^2(\\Lambda-1)^3(\\Lambda-9),\n\\end{equation}",
           "  \\Delta=2^{12}\\Lambda^2(\\Lambda-1)^3(\\Lambda-9),\n\\]", 1, body)

# Everything within the margins (template guideline): the two bounds of Theorem A on two lines
body = sub("\\[\n  \\N(X)\\ \\ge\\ \\Ncl(X)\\ \\ge\\ \\Big(\\frac{3\\log2}{2\\pi^2}+o(1)\\Big)X\\log X,\\qquad\n"
           "  \\N(X)\\ \\ge\\ \\Big(\\frac{3}{128\\pi^4}+o(1)\\Big)X(\\log X)^2 .\n\\]",
           "\\begin{gather*}\n  \\N(X)\\ \\ge\\ \\Ncl(X)\\ \\ge\\ \\Big(\\frac{3\\log2}{2\\pi^2}+o(1)\\Big)X\\log X,\\\\\n"
           "  \\N(X)\\ \\ge\\ \\Big(\\frac{3}{128\\pi^4}+o(1)\\Big)X(\\log X)^2 .\n\\end{gather*}", 1, body)

# A comma after a sentence-initial "Hence" (template guideline)
for old, new in [
    ("Hence $P+T_2=\\iota(P)$", "Hence, $P+T_2=\\iota(P)$"),
    ("Hence $nP$ lies on it", "Hence, $nP$ lies on it"),
    ("Hence $\\delta=p-p'\\ne0$.", "Hence, $\\delta=p-p'\\ne0$."),
    ("Hence $\\N(X)\\ge\\frac X2", "Hence, $\\N(X)\\ge\\frac X2"),
]:
    body = sub(old, new, 1, body)

# A sentence does not begin with notation (template guideline): figure caption, part (b)
body = sub("(b) $\\N(S)/S$ (heavy)", "(b) The ratio $\\N(S)/S$ (heavy)", 1, body)

# Captions beneath tables (template guideline): move each \caption{...}\label{...} below its tabular
def move_caption(m):
    block = m.group(0)
    cap = re.search(r"\\caption\{.*?\}\\label\{tab:[a-z]+\}\n", block, re.S).group(0)
    block = block.replace(cap, "")
    return block.replace("\\end{tabular}\n", "\\end{tabular}\n" + cap)
body, k = re.subn(r"\\begin\{table\}\[t\].*?\\end\{table\}", move_caption, body, flags=re.S)
if k != 2:
    sys.exit(f"expected 2 tables, found {k}")

# The companion paper is cited by its arXiv number (bibliography entry below)
if "\\cite{gangetal-heat}" not in body:
    sys.exit("companion citation not found")

# ---- bibliography: inline, alphabetical, numeric labels, Integers format ---------------------------
BIB = r"""\begin{thebibliography}{99}

\bibitem{beauville1982}
A. Beauville, Les familles stables de courbes elliptiques sur $\mathbf{P}^1$ admettant quatre fibres singuli\`eres, \textit{C. R. Acad. Sci., Paris, S\'er. I} \textbf{294} (1982), 657--660.

\bibitem{bremnerguy1997}
A. Bremner and R. K. Guy, Two more representation problems, \textit{Proc. Edinb. Math. Soc. (2)} \textbf{40}(1) (1997), 1--17.

\bibitem{bgn1993}
A. Bremner, R. K. Guy, and R. J. Nowakowski, Which integers are representable as the product of the sum of three integers with the sum of their reciprocals?, \textit{Math. Comp.} \textbf{61}(203) (1993), 117--130.

\bibitem{crameri2023}
F. Crameri, Scientific colour maps, version 8.0.1, Zenodo, 2023, \url{https://doi.org/10.5281/zenodo.8409685}.

\bibitem{crameri2020}
F. Crameri, G. E. Shephard, and P. J. Heron, The misuse of colour in science communication, \textit{Nature Communications} \textbf{11} (2020), 5444.

\bibitem{dggw2008}
E. B. Dryden, C. S. Gordon, S. J. Greenwald, and D. L. Webb, Asymptotic expansion of the heat kernel for orbifolds, \textit{Michigan Math. J.} \textbf{56}(1) (2008), 205--238.

\bibitem{gangetal-heat}
P. Gang, A. Agadi, A. Veluri, J. Wang, J. Barreto, and A. Chouthaiwale, How much of a hyperbolic orbifold does heat hear?, preprint, arXiv:\textbf{[PLACEHOLDER: arXiv number of Paper A]}.

\bibitem{kelly1989}
J. B. Kelly, Partitions with equal products. II, \textit{Proc. Amer. Math. Soc.} \textbf{107}(4) (1989), 887--893.

\bibitem{mazur1977}
B. Mazur, Modular curves and the Eisenstein ideal, \textit{Publ. Math. Inst. Hautes \'Etudes Sci.} \textbf{47} (1977), 33--186.

\bibitem{pari2172}
The PARI Group, PARI/GP version 2.17.2, Univ. Bordeaux, 2025, \url{https://pari.math.u-bordeaux.fr/}.

\bibitem{sadekelsissi2015}
M. Sadek and N. El-Sissi, Partitions with equal products and elliptic curves, \textit{Osaka J. Math.} \textbf{52}(2) (2015), 515--525.

\bibitem{schinzel1996}
A. Schinzel, Triples of positive integers with the same sum and the same product, \textit{Serdica Math. J.} \textbf{22}(4) (1996), 587--588.

\bibitem{schoen1988}
C. Schoen, On fiber products of rational elliptic surfaces with section, \textit{Math. Z.} \textbf{197}(2) (1988), 177--199.

\bibitem{ysv2024}
A. E. A. Youmbai, A. S. Zargar, and M. Voznyy, Partitions into triples with equal products and families of elliptic curves, \textit{Glas. Mat. Ser. III} \textbf{60}(1) (2025), 59--72.

\bibitem{zhangcai2013}
Y. Zhang and T. Cai, $n$-tuples of positive integers with the same sum and the same product, \textit{Math. Comp.} \textbf{82}(281) (2013), 617--623.

\end{thebibliography}
"""

PRE = r"""%% Triples with equal sum and equal reciprocal sum: the version formatted for Integers.
%% Format: the Integers article template (integers.sty, IntegersTemplate.tex) and its writing and
%% bibliography guidelines; see README.md in this folder for the sources and the changes made.
\documentclass[10pt]{article}
\usepackage{integers}

\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{hyperref}
\usepackage{xcolor}
\hypersetup{backref=true,
    pagebackref=true,
    hyperindex=true,
    colorlinks=true,
    breaklinks=true,
    urlcolor= red,
    linkcolor= blue,
    bookmarks=true,
    bookmarksopen=false,
    filecolor=black,
    citecolor=red,
    linkbordercolor=blue,
    pdftitle={Triples with equal sum and equal reciprocal sum},
    pdfauthor={Palaash Gang, Akshaj Agadi, Arjun Veluri, Jerry Wang, Jeremy Barreto, Aarin Chouthaiwale}
}
\AtBeginDocument{\hypersetup{pdfborder={0 0 0}}}

\graphicspath{{../../../}}% the figure is addressed relative to the repository root
\setlength{\emergencystretch}{3em}% keeps lines with long inline formulas within the margins

\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\N}{\mathcal{N}}
\newcommand{\Ncl}{\mathcal{N}_{\mathrm{cl}}}
\newcommand{\ciso}{c_{\mathrm{iso}}}
\newcommand{\Orb}{\mathcal{O}}

\title{Triples with Equal Sum and Equal Reciprocal Sum}

%% Six authors in two columns, so that the title, the authors and the abstract fit on the first page
\newcommand{\integersauthor}[3]{{\bfseries #1}\newline{\smallit #2}\newline{\tt #3}}
\author{%
  \begin{tabular}{@{}>{\centering\arraybackslash}p{2.4in}>{\centering\arraybackslash}p{2.4in}@{}}
  \integersauthor{Palaash Gang}{Indus International School,\newline Pune, India}{palaash.gang@indusschoolpune.com} &
  \integersauthor{Akshaj Agadi}{Texas A\&M University,\newline College Station, Texas, USA}{a0708@tamu.edu} \\ \noalign{\vspace{10pt}}
  \integersauthor{Arjun Veluri}{Indus International School,\newline Pune, India}{arjun.v@indusschoolpune.com} &
  \integersauthor{Jerry Wang}{University of California, Irvine,\newline Irvine, California, USA}{jerryiw@uci.edu} \\ \noalign{\vspace{10pt}}
  \integersauthor{Jeremy Barreto}{Lawrence High School,\newline Lawrenceville, New Jersey, USA}{jeremy.barreto@ltps.info} &
  \integersauthor{Aarin Chouthaiwale}{DriveChange Learning and Resource Centre,\newline Pune, India}{aarinchouthaiwale@gmail.com}
  \end{tabular}}

\begin{document}
\maketitle

\begin{abstract}
""" + abstract + r"""
\end{abstract}

"""

BACK = r"""\section*{Statements and Declarations}

\noindent\textit{Funding.} No funding was received for this work.

\noindent\textit{Competing interests.} The authors have no competing interests to declare that are relevant to the content of this article.

\noindent\textit{Data and code availability.} {\sloppy The code and data are archived at Zenodo, with all six authors as creators: \textbf{[PLACEHOLDER: Zenodo DOI, to be minted at submission.]} That deposit is the primary record and the version to cite. The development repository, maintained by A.~Agadi, is \url{https://github.com/Ali-M658/Arithmetic-verification}. One command reruns every check. Table~\ref{tab:fibres} is produced by \texttt{make\_tables.py} from \texttt{groups.csv}, written by \texttt{enumerate\_fast.py}, and from the ranks of \texttt{ranks.py}; Table~\ref{tab:density} is produced by the same tool from \texttt{check\_enum.py} (to $S=6000$), cross-checked against \texttt{per\_S.csv}; the fits are those of \texttt{growth\_fits.py}, and Figure~\ref{fig:F9} is drawn by \texttt{F9.py}.\par}

\noindent\textit{Author contributions.} \textbf{[PLACEHOLDER: author contribution statement, to be supplied by the authors before submission.]}

\noindent\textit{Use of AI tools.} \textbf{[PLACEHOLDER: statement on the use of AI tools in preparing this manuscript, to be written by the authors.]}

\acknowledgements{The colours of Figure~\ref{fig:F9} are from the Scientific Colour Maps \cite{crameri2023}, which are designed to be perceptually uniform and readable by people with colour-vision deficiencies \cite{crameri2020}.}

"""

out = PRE + body + BACK + BIB + "\n\\end{document}\n"
open(out_path, "w", encoding="utf-8").write(out)
print("written", out_path, len(out.splitlines()), "lines")
