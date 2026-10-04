"""ST.6: the Ostrowski input.  (1) anchors in the fetched text; (2) exact counterexample showing that
gamma must be the largest root modulus of BOTH polynomials (Ostrowski (69,4): gamma = Max(|x_v|, |y_v|));
(3) numerical sanity check of (71,1) with that reading (floats, heuristic only, not a certificate).
Pages: the PDF page images ostrowski_p53.png (p. 210: (69,1)-(70,2)) and ostrowski_p55.png
(p. 212: (71,1) and Theoreme XXX) were rendered from review/audit/sources/ostrowski_1940.pdf.
Run from repo root: python3 review/audit/stability/check_ostrowski.py"""
import os, sys, random, itertools
from fractions import Fraction as F
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'sources', 'ostrowski_1940.txt')
out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

t = open(SRC, encoding='utf-8', errors='replace').read()
i_xxx = t.index('\nXXX. \n')
i_211 = t.index('Recherches sur la m6thode de Graeffe. \n211')
i_212 = t.index('212 \nAlexandre Ostrowski.')
i_711 = t.index('(7I, I)')
assert i_211 < i_212 < i_711 < i_xxx  # (71,1) and Theoreme XXX sit on p. 212
assert 'condition de L@schitz d\'ordre' in t[i_xxx:i_xxx + 2000]
i_694 = t.index('(69, 4)')
assert 'Soit 7--Max([x~[, \nly, D' in t[i_694 - 200:i_694]  # OCR of 'Soit gamma = Max(|x_v|, |y_v|)'
log('anchors: (71,1) and Theoreme XXX on p. 212; (69,4) preceded by gamma = Max(|x_v|,|y_v|) (both root sets): OK')

# (2) reading gamma as the largest root modulus of f alone breaks the inequality:
# f = z^2, g = z^2 - B z.  Roots {0,0} and {0,B}.  gamma_f = 0 gives eps = (|B| * 0^1 + 0)^(1/2) = 0.
B = F(1)
n = 2
a = [F(1), F(0), F(0)]
b = [F(1), -B, F(0)]
def eps_pow_n(gamma):
    return sum(abs(a[v] - b[v]) * gamma ** (n - v) for v in range(1, n + 1))
assert eps_pow_n(F(0)) == 0  # gamma from f only: eps = 0, yet the roots move by B = 1
assert eps_pow_n(B) == B * B  # gamma over both: eps = B, and (2n-1) eps = 3B >= B
log('reading gamma = max |roots of f| only: f=z^2, g=z^2-z gives eps=0 while a root moves by 1 -> the quote must say "of f and g"')

# (3) heuristic numerical check of |y - x| <= (2n-1) eps with gamma over both root sets
mp.mp.dps = 40
random.seed(2)
worst = 0
for trial in range(3000):
    n = random.randint(2, 6)
    xs = [mp.mpc(random.uniform(-3, 3), random.uniform(-3, 3) * (trial % 2)) for _ in range(n)]
    f = [mp.mpf(1)]
    for x in xs:
        f = [c - x * d for c, d in zip(f + [0], [0] + f)]
    g = [f[0]] + [c + mp.mpf(10) ** random.randint(-8, 0) * mp.mpf(random.uniform(-1, 1)) for c in f[1:]]
    ys = mp.polyroots(g, maxsteps=200, extraprec=200)
    gam = max([abs(x) for x in xs] + [abs(y) for y in ys])
    eps = sum(abs(f[v] - g[v]) * gam ** (n - v) for v in range(1, n + 1)) ** (mp.mpf(1) / n)
    best = min(max(abs(ys[p[i]] - xs[i]) for i in range(n)) for p in itertools.permutations(range(n)))
    assert best <= (2 * n - 1) * eps * (1 + mp.mpf(10) ** -20)
    worst = max(worst, best / ((2 * n - 1) * eps))
log('heuristic check of (71,1) with gamma over both root sets: 3000 random cases, max ratio %.4f' % float(worst))
open(os.path.join(HERE, 'check_ostrowski.txt'), 'w').write('\n'.join(out) + '\nALL CHECKS PASSED\n')
print('ALL CHECKS PASSED')
