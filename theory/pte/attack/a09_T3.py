"""Attack item 9: the T_3 search of proof.md section 6.

(i)   derive the cubic for U symbolically (own elimination);
(ii)  own exact search: every multiset V of 5 positive integers, gcd 1, v5 <= NMAX: exact rational
      roots of the cubic (integer bisection, no floating point); count cubics with 3 positive real roots
      (exact discriminant) for cross-checking search_T3.c's 'real3' counter;
(iii) run the project's search_T3.c on the same range and compare counts (binary built in attack/, removed);
(iv)  stress the floating filter (copied verbatim from search_T3_control.c) on planted *non-integral*
      rational U (K' > 1), which the project's positive control never exercises.
Usage: a09_T3.py NMAX
"""
import sys, os, itertools, subprocess, random
from fractions import Fraction as F
from math import gcd
import sympy as sp
sys.path.insert(0, os.path.dirname(__file__))
from mylib import rational_roots_cubic

sys.stdout.reconfigure(line_buffering=True)
HERE = os.path.dirname(os.path.abspath(__file__))
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 30
fail = []

# ---------- (i) symbolic derivation ----------
u1, u2, u3, t, S, C, R = sp.symbols('u1 u2 u3 t S C R')
e1, e2, e3 = sp.symbols('e1 e2 e3')
# conditions: e1 = S ; p3 = e1^3 - 3 e1 e2 + 3 e3 = C ; e2/e3 = R
sol = sp.solve([sp.Eq(e1, S), sp.Eq(e1 ** 3 - 3 * e1 * e2 + 3 * e3, C), sp.Eq(e2, R * e3)], [e1, e2, e3], dict=True)
assert len(sol) == 1
s = sol[0]
cubic = sp.together(t ** 3 - s[e1] * t ** 2 + s[e2] * t - s[e3])
Rn, Rd = sp.symbols('Rn Rd')
K = 3 * (Rd - S * Rn); Mm = C - S ** 3
claimed = K * t ** 3 - K * S * t ** 2 + Mm * Rn * t - Mm * Rd
mine = sp.numer(sp.together(cubic.subs(R, Rn / Rd)))
ratio = sp.simplify(mine / claimed)
assert ratio.free_symbols == set() or sp.simplify(ratio).is_constant(), ratio
print(f"(i) own elimination: cubic = {sp.factor(mine)};  ratio to proof.md's cubic = {ratio}  -> matches")
# sanity on a planted triple
U0 = [F(2), F(3), F(7)]
SS, CC, RR = sum(U0), sum(u ** 3 for u in U0), sum(1 / u for u in U0)
e3v = (CC - SS ** 3) / (3 * (1 - SS * RR)); e2v = RR * e3v
assert sorted(rational_roots_cubic(1, -SS, e2v, -e3v)) == U0
print("    planted U={2,3,7} recovered exactly from (S, C, R)")
print("    note: K=0 would need S*R=1, impossible (S*R >= 25 by Cauchy-Schwarz for 5 positive v)")
print("          triple root u: S*R = 9 < 25, impossible, so the C code's Q>0 guard loses nothing")

# ---------- (ii) own exact search ----------
nV = real3 = 0
hits = []
for V in itertools.combinations_with_replacement(range(1, NMAX + 1), 5):
    g = 0
    for v in V:
        g = gcd(g, v)
    if g != 1:
        continue
    nV += 1
    Si = sum(V); Ci = sum(v ** 3 for v in V)
    # R = Rn/Rd exactly
    Rf = sum(F(1, v) for v in V)
    Kf = 3 * (1 - Si * Rf)  # = K/Rd
    Mi = Ci - Si ** 3
    e3v = F(Mi) / Kf; e2v = Rf * e3v
    a2, a1, a0 = -Si, e2v, -e3v
    # exact discriminant of monic cubic t^3 + a2 t^2 + a1 t + a0
    disc = 18 * a2 * a1 * a0 - 4 * a2 ** 3 * a0 + a2 ** 2 * a1 ** 2 - 4 * a1 ** 3 - 27 * a0 ** 2
    if disc > 0:
        real3 += 1  # e1,e2,e3 > 0 => all three real roots positive (Descartes)
    rts = rational_roots_cubic(1, a2, a1, a0)
    if len(rts) == 3:
        hits.append((V, rts))
    elif len(rts) == 1 and disc >= 0:
        pass
print(f"(ii) own exact search, v5 <= {NMAX}: {nV} primitive V; {real3} cubics with 3 distinct positive real roots; "
      f"cubics splitting completely over Q: {len(hits)}")
for h in hits[:10]:
    print("     SPLIT:", h)
if hits:
    fail.append("size-8 genus collision found?!")

# ---------- (iii) the project's search_T3.c on the same range ----------
binp = os.path.join(HERE, "_search_T3_bin")
src = os.path.join(HERE, "..", "search_T3.c")
r = subprocess.run(["clang", "-O2", "-o", binp, src, "-lm"], capture_output=True, text=True)
if r.returncode == 0:
    r = subprocess.run([binp, str(NMAX), "1", str(NMAX)], capture_output=True, text=True)
    os.remove(binp)
    print(f"(iii) project search_T3.c on v5 <= {NMAX}: stderr: {r.stderr.strip()}")
    cand = [l for l in r.stdout.splitlines() if l.startswith("V")]
    print(f"     candidates printed: {len(cand)} (all must be non-splitting, as (ii) found none)")
    import re
    m = re.search(r"V-sets (\d+), 3 positive real roots (\d+)", r.stderr)
    if m:
        cV, cR = int(m.group(1)), int(m.group(2))
        print(f"     V-sets: C {cV} vs own {nV};  3-positive-real-root cubics: C {cR} (+{len([c for c in cand if c.endswith('D')])} degenerate) vs own exact {real3}")
        if cV != nV:
            fail.append("V count mismatch")
else:
    print("(iii) clang failed:", r.stderr[:300])

# ---------- (iv) stress the floating filter with K' > 1 ----------
FILTER = r'''
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef __int128 i128;
static i128 g128(i128 a,i128 b){if(a<0)a=-a;if(b<0)b=-b;while(b){i128 t=a%b;a=b;b=t;}return a;}
/* verbatim copy of filter() from theory/pte/search_T3_control.c */
int filter(i128 S,i128 C,i128 Rn,i128 Rd){
  i128 K=3*(Rd-S*Rn), M=C-S*S*S; if(K==0||M==0) return -1;
  i128 g=g128(g128(K,M*Rn),M*Rd); i128 Kp=K/g; if(Kp<0)Kp=-Kp;
  long double Sd=(long double)S, Rv=(long double)Rn/(long double)Rd, e3=((long double)M)/(3.0L*(1.0L-Sd*Rv)), e2=Rv*e3;
  if(!(e3>0&&e2>0)) return -2;
  long double a=-Sd,b=e2,c=-e3; long double Q=(a*a-3*b)/9, Rr=(2*a*a*a-9*a*b+27*c)/54;
  if(Q>0 && fabsl(Rr*Rr-Q*Q*Q)<=1e-9L*Q*Q*Q) return 2;
  if(Rr*Rr>=Q*Q*Q) return -3;
  long double th=acosl(Rr/sqrtl(Q*Q*Q)); long double sq=-2*sqrtl(Q); long double r[3];
  r[0]=sq*cosl(th/3)-a/3; r[1]=sq*cosl((th+2*M_PI)/3)-a/3; r[2]=sq*cosl((th-2*M_PI)/3)-a/3;
  int ok=1; for(int i=0;i<3;i++){ long double x=r[i]; for(int k=0;k<5;k++){ long double f=((x+a)*x+b)*x+c, fp=(3*x+2*a)*x+b; if(fp==0)break; x-=f/fp;} r[i]=x; if(x<=0){return -4;} }
  long double Kd=(long double)Kp;
  for(int i=0;i<3&&ok;i++){ long double y=Kd*r[i]; long double tol=fabsl(y)*4e-18L+1e-6L; if(tol>0.25L) continue; if(fabsl(y-roundl(y))>tol) ok=0; }
  return ok;}
int main(){ long long S,C,Rn,Rd; while(scanf("%lld %lld %lld %lld",&S,&C,&Rn,&Rd)==4) printf("%d\n",filter(S,C,Rn,Rd)); return 0;}
'''
random.seed(3)
planted = []


def add(q, p):
    U = [F(x, q) for x in p]
    if all(u.denominator == 1 for u in U) or len(set(U)) < 3 or max(U) > 1100:
        return
    Si = sum(U); Ci = sum(u ** 3 for u in U); Rf = sum(1 / u for u in U)
    if Si.denominator != 1 or Ci.denominator != 1:
        return
    planted.append((q, int(Si), int(Ci), Rf.numerator, Rf.denominator, U))


# family 1 (fast, any q): p1 + p2 = 0 mod q^3, p3 = q t  =>  q | sum p and q^3 | sum p^3
for q in range(2, 34):
    for _ in range(30):
        p1 = random.randint(1, q ** 3 - 1)
        if p1 % q == 0:
            continue
        p2 = q ** 3 * random.randint(1, 2) - p1
        add(q, [p1, p2, q * random.randint(1, 1000)])
# family 3: near-double roots inside the searched regime (S = e1(U) <= 1100 = 5*220):
#   U = {(q^3-d)/(2q), (q^3+d)/(2q), t},  q^3 - d even,  q^2 + t <= 1100
n_before3 = len(planted)
for q in range(8, 34):
    for d in range(1, 400):
        if (q ** 3 - d) % 2 or d >= q ** 3:
            continue
        for t_ in random.sample(range(1, max(2, 1101 - q * q)), min(3, max(1, 1100 - q * q))):
            add(q, [(q ** 3 - d) // 2, (q ** 3 + d) // 2, q * t_])
n_fam3 = len(planted) - n_before3
# family 2 (generic, small q): random p with the two congruences, by rejection
for q in range(2, 7):
    for _ in range(60000):
        add(q, [random.randint(1, 300 * q) for _ in range(3)])
csrc = os.path.join(HERE, "_filter_stress.c"); fbin = os.path.join(HERE, "_filter_stress_bin")
open(csrc, "w").write(FILTER)
r = subprocess.run(["clang", "-O2", "-o", fbin, csrc, "-lm"], capture_output=True, text=True)
assert r.returncode == 0, r.stderr
inp = "\n".join(f"{a} {b} {c} {d}" for _, a, b, c, d, _ in planted)
out = subprocess.run([fbin], input=inp, capture_output=True, text=True).stdout.split()
os.remove(fbin); os.remove(csrc)
res = list(zip(planted, map(int, out)))
acc = sum(1 for _, v in res if v in (1, 2))
rej = [(p[5], v) for p, v in res if v not in (1, 2)]
# K' of each planted cubic, exactly
def kprime(Si, Ci, Rn_, Rd_):
    K_ = 3 * (Rd_ - Si * Rn_); M_ = Ci - Si ** 3
    g_ = gcd(gcd(K_, M_ * Rn_), M_ * Rd_)
    return abs(K_ // g_)
kps = [kprime(a, b, c, d) for _, a, b, c, d, _ in planted]
print(f"(iv) filter of search_T3.c on {len(planted)} planted NON-integral rational U (denominators 2..33, "
      f"K' from {min(kps)} to {max(kps)}): accepted {acc}, rejected {len(rej)}")
for u, v in rej[:8]:
    print("     REJECTED (false negative):", [str(x) for x in u], "S =", sum(u), "code", v)
in_regime = [(u, v) for u, v in rej if sum(u) <= 1100]
print(f"     of which inside the searched regime S <= 1100: {len(in_regime)} (family 3 near-double cases: {n_fam3} planted)")
if rej:
    fail.append(f"BROKEN (rigour): float filter of search_T3.c rejects {len(rej)} genuine rational U "
                f"({len(in_regime)} with S <= 1100)")
print("     (project control plants integer U only: there K' = 1 always, so the q | K' logic is untested there)")

if fail:
    print("FINDINGS:", fail)
    sys.exit(1 if any("collision found" in x or "mismatch" in x for x in fail) else 2)
print("ALL CHECKS PASSED")
