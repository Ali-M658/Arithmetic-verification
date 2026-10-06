"""Comparison phase: independent planted test of the producer's T_3 decision routine.

Compiles theory/pte/search_T3.c (read-only; binary in the session scratchpad) and feeds its `test`
mode (S, C, Rn, Rd) computed EXACTLY from planted genuine positive rational triples U with
S = sum u and C = sum u^3 integral, S <= 1100 (the searched regime).  decide() <= 0 on such a
U is a false negative (a genuine solution would be rejected).  Families (own design):
  P  u1 = p/q, u2 = (k q^3 - p)/q, u3 = w integer: all q = 2..33, all p <= q^3/2
     with p not divisible by q, k = 1, w in {1, 7, 50, 300} (subject to S <= 1100);
  N  near-double: u1, u2 = (q^3 -+ d)/(2q), d = 1..60, q = 4..33, u3 integer;
  T  entries p_i/q (q = 2..12, not all integral) with S, C integral (random search);
  W  integer triples with a near-triple cluster {a, a+1, a+2} and {a, a, a+1}, a = 1..360.
Exit nonzero if any false negative occurs.
"""
import os, random, subprocess, sys, tempfile
from fractions import Fraction as F

SRC = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'theory', 'pte', 'search_T3.c')
SP = os.environ.get('SCRATCH', tempfile.gettempdir())
binp = os.path.join(SP, 'producer_search_T3')
subprocess.run(['cc', '-O2', '-o', binp, SRC, '-lm'], check=True)
random.seed(4242)
fam = {k: [] for k in 'PNTW'}

def add(k, U):
    U = [F(u) for u in U]
    if min(U) <= 0:
        return
    S, C, R = sum(U), sum(u ** 3 for u in U), sum(1 / u for u in U)
    if S.denominator != 1 or C.denominator != 1 or S > 1100:
        return
    fam[k].append((int(S), int(C), R.numerator, R.denominator, U))

for q in range(2, 34):
    for p in range(1, q ** 3 // 2 + 1):
        if p % q == 0:
            continue
        for w in (1, 7, 50, 300):
            add('P', [F(p, q), F(q ** 3 - p, q), w])
for q in range(4, 34):
    for d in range(1, 61):
        if (q ** 3 - d) % 2 == 0 and d < q ** 3:
            add('N', [F(q ** 3 - d, 2 * q), F(q ** 3 + d, 2 * q), random.randint(1, 500)])
tries = 0
while len(fam['T']) < 20000 and tries < 3_000_000:
    tries += 1
    q = random.randint(2, 12)
    p = [random.randint(1, 60 * q) for _ in range(3)]
    if all(x % q == 0 for x in p):
        continue
    add('T', [F(x, q) for x in p])
for a in range(1, 361):
    add('W', [a, a + 1, a + 2]); add('W', [a, a, a + 1]); add('W', [a, a + 1, a + 1])

bad = 0
for k, lst in fam.items():
    if not lst:
        print(f"family {k}: 0 planted"); continue
    inp = "\n".join(f"{S} {C} {Rn} {Rd}" for S, C, Rn, Rd, _ in lst)
    out = list(map(int, subprocess.run([binp, 'test'], input=inp, capture_output=True, text=True, check=True).stdout.split()))
    assert len(out) == len(lst)
    neg = [(lst[i][4], out[i]) for i in range(len(lst)) if out[i] <= 0]
    counts = {c: out.count(c) for c in sorted(set(out))}
    print(f"family {k}: {len(lst)} planted genuine U; decisions {counts}; false negatives {len(neg)}")
    for U, c in neg[:5]:
        print("   FALSE NEGATIVE", [str(u) for u in U], "code", c)
    bad += len(neg)
os.remove(binp)
print("total false negatives:", bad)
sys.exit(1 if bad else 0)
