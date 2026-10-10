# Two papers by Nguyen Xuan Tho: what they prove, and what they change in the note

Numbers of results in the note refer to the Integers version, `integers/note.pdf`.

Both papers were fetched and read in full on 2026-10-10. The PDFs are not committed (third-party texts).

| key | record | fetched text | SHA-256 of the PDF |
|---|---|---|---|
| `tho2021` | Nguyen Xuan Tho, *What positive integers $n$ can be presented in the form $n=(x+y+z)(1/x+1/y+1/z)$?*, Ann. Math. Inform. 54 (2021), 141–146, doi:10.33039/ami.2021.04.005 | http://publikacio.uni-eszterhazy.hu/6965/1/AMI_54_from141to146.pdf (the published paper, 6 pp.) | `6fc4ced80a662ff343a1a09f3743ed5948db6b0408ed01b5e2fa01a3fc6f5f89` |
| `bremnertho2018` | A. Bremner and Nguyen Xuan Tho, *The equation $(w+x+y+z)(1/w+1/x+1/y+1/z)=n$*, Int. J. Number Theory 14(5) (2018), 1229–1246, doi:10.1142/s1793042118500768 | https://mathpost.asu.edu/~tnguyenx/paper1.pdf (the journal's typeset version, posted on the second author's page, 18 pp. numbered 1–18) | `69449f487bb7d3f72344164c66703803e34e67c66d3d7f1689d7ec98fba5303f` |

The bibliography records are built from the Crossref records by `tools/build_bib.py` (see `SOURCES.md`). Two corrections were needed, both taken from the printed papers:
- Crossref gives `tho2021` as an "Accepted manuscript" with no volume or pages. The published paper prints vol. 54 (2021), pp. 141–146.
- Crossref splits the author's name inconsistently between the two records. He signs "Nguyen Xuan Tho", so the name is kept whole.

There is one oddity, which needs no action: reference [2] of `tho2021` gives the DOI of the 2018 paper as 10.1142/S1793042118500756. That DOI belongs to a different paper, on the equation $x^y+y^x=z^2$. The DOI used here, …500768, is the one printed on the 2018 paper and is the Crossref record with the right title.

## `tho2021`: three variables, $4\mid n$

**Statement.** Theorem 1.1 (p. 142): if $n$ is a positive integer with $4\mid n$, then $(x+y+z)(1/x+1/y+1/z)=n$ has no solution in positive integers.

**How it is proved:**
- Proposition 4.1 (p. 145, quoted from Bremner–Guy–Nowakowski, §2): with the curve $v^2=u(u^2+(n^2-6n-3)u+16n)$ and the map $u=-4(xy+yz+zx)/z^2$, positive integer solutions exist exactly when $n>0$ and there is a rational point with $u<0$.
- Theorem 3.1 (p. 143): if $4\mid n$, every rational point on this curve with $u,v\neq0$ has $u>0$. The proof shows that the Hilbert symbol $(u,-D)_p$ equals $+1$ for every prime $p$ (Lemmas 3.2 and 3.3), where $D=n-1$. The product formula then gives $(u,-D)_\infty=+1$ (Lemma 3.4), and since $-D<0$ this forces $u>0$.
- The case $v=0$ is excluded separately (p. 146): it would make $(n-9)(n-1)$ a square, which no $n$ divisible by 4 does.

The abstract calls this a partial answer to the question of Melvyn Knight reported by Bremner, Guy and Nowakowski. The paper says it is the first parametric family of $n$ with no positive solutions. It counts nothing.

**Relation to the note:**
- The curve is the note's $E_\Lambda$ at $\Lambda=n$. In Section 2 the note writes $E_\Lambda:\eta^2=s(s^2+(\Lambda^2-6\Lambda-3)s+16\Lambda)$ and says it is the model (6) of Bremner–Guy–Nowakowski with $n=\Lambda$. The note's $(x+y+z)(1/x+1/y+1/z)$ is $\Lambda=e_1e_2/e_3$.
- **Consequence:** for every integer $\Lambda$ divisible by 4, the curve $C_\Lambda$ has no positive rational points, so no coincidence class has such a $\Lambda$.
- The note works with rational $\Lambda$, and its classes mostly have non-integral $\Lambda$ (Table 1: $27/2$, $68/5$, $1849/120$, $230/21$). Some classes do have integral $\Lambda$; the second-smallest, $\{(4,8,8),(5,5,10)\}$ at $S=20$, has $\Lambda=10$.
- **Consistency check (run for this memo, not part of the committed suite):** in `theory/diophantine/data/groups.csv`, 392 classes have integral $\Lambda$, with $\Lambda\equiv2\pmod4$ for 266 of them and $\Lambda\equiv3\pmod4$ for 126. None has $4\mid\Lambda$, as Theorem 1.1 requires.

**Claims of the note affected: none.**
- No statement of the note asserts that positive points exist on $C_\Lambda$ for any family of integer $\Lambda$ that this theorem rules out.
- Lemma 1 ("the egg": the positive real points of $C_\Lambda$ form the real component not containing $O$, so odd multiples of a positive point are positive) agrees with Proposition 4.1 above, where positive solutions are the points with $u<0$.
- The torsion remark (Remark 1, quoting Bremner–Guy–Nowakowski for integer $n$) is untouched.
- The novelty sentence ("As far as we know, the counting function $\mathcal N(X)$, the bounds of Theorem 1 and Proposition 1, and the enumeration are new") stands. `tho2021` decides which $n$ are represented, not how many representations there are, and gives no bound or enumeration.

## `bremnertho2018`: four variables, $n=4m^2$ and $4m^2+4$

**Statement:**
- Theorems 8 and 9 (p. 9): if $n=4m^2$ with $m\equiv0\pmod4$, or with $m$ odd, then $(w+x+y+z)(1/w+1/x+1/y+1/z)=n$ has no solution in positive rationals.
- Theorem 14 (p. 14): the same holds for $n=4m^2+4$ with $m\not\equiv2\pmod4$.
- This refutes the remark of Bremner, Guy and Nowakowski that "it seems likely that for $n\ge16$ there is always such a representation" (quoted on p. 2).

**How it is proved:**
- Fixing $y/z$ makes the equation a cubic in $w,x$, with Weierstrass model $F_n: Y^2=X(X^2+AX+B)$ over $\mathbb Q(y,z)$ (§3).
- Positive $w,x$ correspond to points on the bounded real component, $X<0$ (p. 5).
- For the two families, $(X,-D)_p=+1$ for every prime $p$ (Lemmas 2, 3, 5, 10–12), where $D=-y^2+(n-2)yz-z^2>0$. Hence $X>0$ unless $Y=0$ (Theorems 6 and 13).
- The torsion case reduces to $w=x$ and is excluded by hand.

**Further results:**
- A Fibonacci identity gives positive solutions at $n=(4+F_{2k}^2)^2$ (p. 2).
- A search over $16\le n\le1000$ (Appendix A, Table A.1) finds positive solutions for every other $n$ in range. The paper says the converse "seems very difficult to prove", so it remains conjectural.
- The paper credits the method to M. Stoll's argument for $x/(y+z)+y/(z+x)+z/(x+y)=n$.

**Relation to the note:**
- This is the four-variable analogue of the note's invariant. The note treats triples only, and nothing in it concerns quadruples.
- The relation is one of method: Hilbert symbols on a genus-one fibration, showing that positivity fails. It is the same method as `tho2021`, which `tho2021` (p. 142) says it follows.

**Claims of the note affected: none.**

## What was changed

1. `tools/build_bib.py`: two new records (`tho2021`, `bremnertho2018`), the corrections above, and a `--fetch-missing` option, so that only the new records were downloaded. `references.bib` and `SOURCES.md` were regenerated; the existing entries are unchanged.
2. `integers/make_integers.py` (and the regenerated `integers/note.tex`): one passage in "Relation to the Literature", placed before "As far as we know". It gives Theorem 1.1 of `tho2021`, its consequence for $C_n$, and Theorems 8, 9 and 14 of `bremnertho2018`, and notes that both papers concern existence, not counting. Two references were added. The Integers note grows from 15 to 16 pages.
3. **Not changed:** the amsart version `note.tex` (the arXiv version). For both versions to cite the papers, move the passage into `note.tex` and delete the corresponding substitution in `make_integers.py`, which then fails loudly if left in.

**For the authors to decide:**
- Whether the consistency check above should become a committed check (for example in `checks/`), so that the note could state it.
- `paper/submission/REFEREES.md` lists Nguyen Xuan Tho as a suggested referee and warns against choosing him together with Bremner. Now that both papers are cited, he is a closer, more natural referee. Nothing there was changed.
