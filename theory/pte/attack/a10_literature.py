"""Attack item 10: literature claims -- every quoted phrase must occur in the fetched text, and every
numerical input must satisfy what it is claimed to satisfy (own exact check)."""
import sys, os, re
import sympy as sp
sys.path.insert(0, os.path.dirname(__file__))
from mylib import psum

sys.stdout.reconfigure(line_buffering=True)
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sources')
fail = []


def text(name):
    return re.sub(r"\s+", " ", open(os.path.join(SRC, name), 'rb').read().decode('utf-8', 'replace'))


BI = text('BorweinIngalls1994_EnsMath40_pages3-27.txt')
CMSV = text('CMSV2023_arXiv2304.11254.txt')
CMY = text('CrootMaoYip2026_arXiv2609.05061.txt')
BLP = text('BLP2003_MathComp72_authorcopy.txt')
CHEN = text('ChenShuwen2025_survey_arXiv2506.11429.txt')
ESL = text('eslpower_TarryPrb.txt')
CH22 = text('Choudhry2022_deg7_arXiv2207.12726.txt')

checks = [
    ("B-I Prop 2 N(k) >= k+1", BI, "Proposition 2. N(k)"),
    ("B-I Prop 3 (pigeonhole)", BI, "Proposition 3."),
    ("B-I Wright/Melzak 'slightly stronger'", BI, "Slightly stronger upper bounds are discussed in [22] and [15]"),
    ("B-I open problem 3", BI, "3. Prove N(k) ^ o(k2)"),
    ("B-I 'no progress'", BI, "No progress on questions 3 and 4 has been made for many years"),
    ("B-I big prize", BI, "The big prize is to find ideal solutions of all degrees"),
    ("B-I size-11 search to 363", BI, "[- 363, 363]"),
    ("B-I 7-set", BI, "- 51, - 33, - 24,7,13,38,50"),
    ("B-I Letac 9-set 1", BI, "- 98, - 82, - 58, - 34, 13, 16, 69, 75, 99"),
    ("B-I Letac 9-set 2", BI, "- 169, - 161, - 119, - 63, 8, 50, 132, 148, 174"),
    ("B-I odd symmetric definition", BI, "j 1, 3, 5, ..,k- 1"),
    ("CMSV known n<=10 and 12", CMSV, "Ideal solutions in the PTE problem over Z are known for n ≤10 and n = 12"),
    ("CMSV no new 9..16", CMSV, "No new integral solutions are found for 9 ≤n ≤16"),
    ("Croot-Mao-Yip pigeonhole", CMY, "pigeonhole"),
    ("Croot-Mao-Yip known k", CMY, "only known that P(k, 2) = k + 1 when 2 ≤k ≤9 and k = 11"),
    ("BLP parametric n=1..8,10", BLP, "Parametric ideal solutions are known for n = 1, 2, . . . , 8 and n = 10"),
    ("BLP size 11 to 2000", BLP, "For size 11, we searched up to 2000 and did not ﬁnd any solutions"),
    ("Choudhry only k<=7", CH22, "known only when k ≤7"),
    ("Chen A.1.6 [1,5,5]=[2,3,6]", CHEN, "[1, 5, 5]k = [2, 3, 6]k"),
    ("Chen A.1.17", CHEN, "[1, 13, 17, 23]k = [3, 9, 21, 21]k"),
    ("Chen A.1.26", CHEN, "[3, 19, 37, 51, 53]k = [9, 11, 43, 45, 55]k"),
    ("Chen A.1.33", CHEN, "[7, 91, 173, 269, 289, 323]k = [29, 59, 193, 247, 311, 313]k"),
    ("Chen A.685", CHEN, "[3, 10, 15, 30]k = [4, 5, 21, 28]k"),
    ("Chen non-symmetric ideal only n<=7", CHEN, "have only been discovered for PTE of degrees n ≤7"),
    ("eslpower Theorem 3 (lifting)", ESL, "Theorem 3 [5]"),
]
for name, T, s in checks:
    ok = s in T
    print(f"  [{'ok' if ok else 'MISSING'}] {name}: \"{s}\"")
    if not ok:
        fail.append(name)

# attribution check: [1,5,5]=[2,3,6] is labelled 'Smallest solution, by computer search' in Chen A.1.6,
# whereas LITERATURE.md writes '(Moessner)'
i = CHEN.find("Smallest solution, by computer search: [1, 5, 5]k = [2, 3, 6]k")
print(f"  Chen A.1.6 labels [1,5,5]=[2,3,6] 'Smallest solution, by computer search' (not Moessner): {i >= 0}")
i2 = CHEN.find("Second known solutions, by Jarosław Wróblewski in 2009")
print(f"  Chen A.1.33: the two equalities used for balanced L=6 are Wroblewski's (2009), not Chen's: {i2 >= 0}")

# Gloden size-7 family as printed in BLP p. 2064 (with the factor f in alpha_3), symbolically
f, k = sp.symbols('f k')
al = [-(f**2 - k*f + k**2) * (-3*k*f**2 + k**3 + f**3),
      -(k - f) * (f + k) * (f**2 - 3*k*f + k**2) * f,
      (-f + 2*k) * (-f**2 - k*f + k**2) * k * f,
      (k - f) * (k - 2*f) * (-f**2 + k*f + k**2) * k,
      (k - f) * (f**4 - 2*k*f**3 - k**2*f**2 + k**4),
      -(k**4 - 2*f*k**3 - k**2*f**2 + 4*k*f**3 - f**4) * k,
      -(k**4 - 5*k**2*f**2 + 4*k*f**3 - f**4) * f]
for e in (1, 3, 5):
    assert sp.expand(sum(a**e for a in al)) == 0, e
ex = sorted(int(a.subs({f: 3, k: 1})) for a in al)
assert ex == sorted([-7, 24, 33, -50, -38, -13, 51]), ex
assert sp.expand(sum(a**7 for a in al)) != 0
al_slip = list(al); al_slip[2] = (-f + 2*k) * (-f**2 - k*f + k**2) * k
print("  BLP Gloden family (as printed, alpha_3 with factor f): sum alpha^e = 0 identically for e=1,3,5; "
      f"f=3,k=1 gives {ex} as printed; without f in alpha_3: e=1 sum = {sp.factor(sum(al_slip))} (fails)")
print("  B-I p.9 attributes the 9/10-sets to 'Letac and Gloden' jointly; CMSV p.2: 9-sets 'both found by Letac': "
      f"{'both found by Letac' in CMSV}")

if fail:
    print("MISSING QUOTES:", fail)
    sys.exit(1)
print("ALL QUOTES FOUND; Gloden family verified")
