"""Phase 2: independent re-derivation of the smooth coefficients alpha_j from the identity term of
Selberg's trace formula (Dryden-Strohmaier eq. (1), fetched: (mu(F)/4pi) int r h(r) tanh(pi r) dr),
with h(r) = exp(-(r^2 + 1/4) t), compared exactly with Ucar (4.35), K = -1, for j <= 15.

Derivation.  r tanh(pi r) = |r| - 2|r|/(e^{2pi|r|} + 1).  int |r| e^{-r^2 t} dr = 1/t, and
  int_R 2|r| e^{-r^2 t}/(e^{2pi|r|}+1) dr = 4 sum_k (-t)^k/k! int_0^inf r^{2k+1}/(e^{2pi r}+1) dr
with int_0^inf r^{2k+1}/(e^{2pi r}+1) dr = (1 - 2^{-2k-1}) |B_{2k+2}| / (4(k+1))
(from int_0^inf x^{s-1}/(e^x+1) dx = (1-2^{1-s}) Gamma(s) zeta(s) and Euler's zeta(2k+2)).
Hence Z_id(t) ~ (Area/4pi) e^{-t/4} [ 1/t - sum_k (-t)^k (1-2^{-2k-1}) |B_{2k+2}| / (k+1)! ],
and alpha_j = [t^{j-1}] of the bracket times e^{-t/4}.
Run from repo root: python3 review/audit/stability/check_selberg.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stab_lib import *
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

J = 15
# bracket as a Laurent series: coefficient list c[i] of t^{i-1}, i = 0..J
br = [F(0)] * (J + 1)
br[0] = F(1)
for k in range(J):
    br[k + 1] -= F((-1) ** k) * (1 - F(1, 2 ** (2 * k + 1))) * abs(bern(2 * k + 2)) / factorial(k + 1)
ex = [F((-1) ** i, 4 ** i * factorial(i)) for i in range(J + 1)]  # e^{-t/4}
sel = [sum(ex[i] * br[j - i] for i in range(j + 1)) for j in range(J + 1)]
uc = [alpha(j) for j in range(J + 1)]
for j in range(J + 1):
    assert sel[j] == uc[j], (j, sel[j], uc[j])
log('alpha_j (Selberg identity term) == alpha_j (Ucar (4.35), K=-1) exactly for j = 0..%d' % J)
log('alpha_0..11 =', [str(x) for x in uc[:12]])

# the moment formula, numerically (heuristic sanity check only)
mp.mp.dps = 30
for k in range(5):
    num = mp.quad(lambda r: r ** (2 * k + 1) / (mp.e ** (2 * mp.pi * r) + 1), [0, mp.inf])
    ex_ = (1 - mp.mpf(2) ** (-2 * k - 1)) * abs(mp.bernoulli(2 * k + 2)) / (4 * (k + 1))
    assert abs(num - ex_) < mp.mpf(10) ** -20
log('moment identity int r^{2k+1}/(e^{2 pi r}+1) = (1-2^{-2k-1})|B_{2k+2}|/(4(k+1)) checked numerically, k <= 4')
# and the full identity term at small t against the series (heuristic)
for t in (mp.mpf('0.05'), mp.mpf('0.02')):
    Zid = mp.quad(lambda r: 2 * r * mp.tanh(mp.pi * r) * mp.e ** (-(r * r + mp.mpf(1) / 4) * t), [0, mp.inf])
    ser = sum(mp.mpf(sel[j].numerator) / sel[j].denominator * t ** (j - 1) for j in range(8))
    log('  t=%s: (4pi/Area) Z_id = %s, series through t^6 = %s, diff/t^7 = %s' % (t, mp.nstr(Zid, 15), mp.nstr(ser, 15), mp.nstr((Zid - ser) / t ** 7, 5)))
    assert abs(Zid - ser) < 10 * t ** 7 * abs(mp.mpf(sel[8].numerator) / sel[8].denominator) + mp.mpf(10) ** -25

open(os.path.join(HERE, 'check_selberg.txt'), 'w').write('\n'.join(out) + '\nALL CHECKS PASSED\n')
print('ALL CHECKS PASSED')
