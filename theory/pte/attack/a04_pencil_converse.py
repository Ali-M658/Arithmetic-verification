"""Attack item 4 (supplement): proof.md section 7 says 'T^cone_3 = 8 would be a pencil point containing a
padding 1', i.e. that every balanced size-8 3-configuration is a pencil point (Theorem 3.1, m = 4).
That converse is not proved in proof.md.  Test it on every balanced size-8 3-configuration with
entries <= NMAX: U, V disjoint 4-multisets of positive integers with equal P1, P3 and R.
Pencil test: some 4-subset A of Z with e1(A) = 0, B = -(Z minus A) with e1(B) = 0, e3, e4 equal.
Also: section 6 item 4, shifts of size-4 ideal symmetric solutions: rho(c) = 0 only at c = 0, c^2 = s/2."""
import sys, os, itertools
from fractions import Fraction as F
from collections import defaultdict
import sympy as sp
sys.path.insert(0, os.path.dirname(__file__))
from mylib import config_level, iota, psum

sys.stdout.reconfigure(line_buffering=True)
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 60
fail = []


def esym(S, k):
    return sum(sp.prod(t) for t in itertools.combinations(S, k))


def is_pencil(Z):
    idx = range(len(Z))
    for comb in itertools.combinations(idx, 4):
        A = [Z[i] for i in comb]
        if sum(A) != 0:
            continue
        B = [-Z[i] for i in idx if i not in comb]
        if sum(B) != 0:
            continue
        if esym(A, 3) == esym(B, 3) and esym(A, 4) == esym(B, 4):
            return (A, B)
    return None


groups = defaultdict(list)
for ms in itertools.combinations_with_replacement(range(1, NMAX + 1), 4):
    groups[(sum(ms), sum(x ** 3 for x in ms), sum(F(1, x) for x in ms))].append(ms)
configs = []
for lst in groups.values():
    for U, V in itertools.combinations(lst, 2):
        if set(U) & set(V):
            continue
        Z = list(U) + [-v for v in V]
        from math import gcd
        g = 0
        for z in Z:
            g = gcd(g, z)
        if g != 1:
            continue
        configs.append(Z)
print(f"balanced size-8 3-configurations, primitive, entries <= {NMAX}: {len(configs)}")
nonpencil = []
for Z in configs:
    assert config_level(Z) >= 3 and iota(Z) == 0
    p = is_pencil(Z)
    if p is None:
        nonpencil.append(Z)
    print(f"  U={sorted(z for z in Z if z > 0)} V={sorted(-z for z in Z if z < 0)}: "
          f"{'pencil A=' + str(sorted(p[0])) + ' B=' + str(sorted(p[1])) if p else 'NOT a pencil point'}")
print(f"non-pencil balanced size-8 configurations: {len(nonpencil)}")

# section 6 item 4: size-4 ideal symmetric solutions {+-a,+-b} vs {+-p,+-q}, a^2+b^2 = p^2+q^2
a, b, p, q, c = sp.symbols('a b p q c', positive=True)
X = [a, -a, b, -b]; Y = [p, -p, q, -q]
rho = sum(1 / (x + c) for x in X) - sum(1 / (y + c) for y in Y)
num = sp.factor(sp.together(rho.subs(q, sp.sqrt(a**2 + b**2 - p**2))))
print("section 6.4: rho(c) for shifted size-4 symmetric solution factors as", num)
r = sp.factor(sp.numer(sp.together(rho)))
print("  numerator (generic):", r)

if nonpencil:
    print("RESULT: the converse used in section 7 ('T^cone_3=8 would be a pencil point') FAILS on the above.")
    sys.exit(2)
print("RESULT: every balanced size-8 3-configuration in range is a pencil point (converse survives in range;"
      " it is still unproved).")
