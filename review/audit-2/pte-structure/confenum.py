"""Exhaustive enumeration of L-configurations with integer entries (shared by check_*.py).

An L-configuration (Definition 1.1) is a nonempty multiset Z of nonzero rationals with
s_j(Z)=0 for odd 1<=j<=2L-3, s_{-1}(Z)=0, no pair {z,-z}, |Z| even.
Every rational configuration is a rational multiple of an integer one, so integer
entries with |z|<=H are enumerated exhaustively: Z = U (+) (-V), U,V multisets of
positive integers <= H with disjoint supports.  Exact integer arithmetic only.
"""
from itertools import combinations_with_replacement
from math import lcm
from fractions import Fraction


def ps(Z, j):
    """exact power sum s_j(Z), j may be negative"""
    if j >= 0:
        return sum(Fraction(z) ** j for z in Z)
    return sum(Fraction(1, 1) / Fraction(z) ** (-j) for z in Z)


def maxL(Z, cap=40):
    """largest L such that Z is an L-configuration (Z assumed to satisfy s_{-1}=0,
    no pair, even size).  L=1 always; L>=2 needs s_1=...=s_{2L-3}=0."""
    L = 1
    while L < cap and ps(Z, 2 * L - 1) == 0:
        L += 1
    return L


def enumerate_configs(H, Tmax, Lmin=2):
    """all integer Lmin-configurations (Lmin in {1,2}) with entries |z|<=H, size T<=Tmax.
    Returns list of tuples Z (sorted).  Both Z and -Z are returned."""
    D = lcm(*range(1, H + 1))
    groups = {}
    for k in range(1, Tmax):
        for U in combinations_with_replacement(range(1, H + 1), k):
            key = (sum(D // u for u in U),) + ((sum(U),) if Lmin >= 2 else ())
            groups.setdefault(key, []).append(U)
    out = []
    for key, lst in groups.items():
        if len(lst) < 2:
            continue
        sets = [(U, set(U)) for U in lst]
        for i in range(len(sets)):
            U, su = sets[i]
            for j in range(len(sets)):
                if i == j:
                    continue
                V, sv = sets[j]
                T = len(U) + len(V)
                if T > Tmax or T % 2:
                    continue
                if su & sv:
                    continue
                Z = tuple(sorted(list(U) + [-v for v in V]))
                out.append(Z)
    return sorted(set(out))


def is_config(Z, L):
    if len(Z) == 0 or len(Z) % 2:
        return False
    if any(z == 0 for z in Z):
        return False
    s = set(Z)
    if any(-z in s for z in s):
        return False
    if ps(Z, -1) != 0:
        return False
    return all(ps(Z, j) == 0 for j in range(1, 2 * L - 2, 2))


def iota(Z):
    return sum(1 for z in Z if z > 0) - sum(1 for z in Z if z < 0)
