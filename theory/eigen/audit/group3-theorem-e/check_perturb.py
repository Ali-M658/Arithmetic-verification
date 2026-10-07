"""Synthetic test of the perturbation step of Theorem eig:E:
|sum_{j<N} e^{-lt_j t} - sum_{j<N} e^{-l_j t}| <= e N t delta whenever l_j >= 0, |lt_j - l_j| <= delta <= 1/t,
including approximations that are negative (l_j = 0 or small, lt_j = l_j - delta)."""
import random
import mpmath as mp
mp.mp.dps = 40
rng = random.Random(3)
worst = 0
for trial in range(20000):
    t = mp.mpf(10) ** rng.uniform(-9, 0)
    N = rng.randint(1, 40)
    delta = (1 / t) * mp.mpf(rng.choice([1, rng.random(), 1e-3]))
    lam = sorted([mp.mpf(0)] + [mp.mpf(rng.choice([0, rng.random() * 1e-6, rng.random() * 10 / t])) for _ in range(N - 1)])
    lt = [l + delta * rng.choice([-1, 1, rng.uniform(-1, 1)]) for l in lam]
    lhs = abs(sum(mp.e ** (-x * t) for x in lt) - sum(mp.e ** (-x * t) for x in lam))
    rhs = mp.e * N * t * delta
    if lhs > rhs * (1 + mp.mpf(10) ** -30):
        raise SystemExit(f"FAIL perturbation {t} {N} {delta}")
    worst = max(worst, lhs / rhs)
print("perturbation bound OK in 20000 trials; max lhs/rhs =", mp.nstr(worst, 8))
# the bound is attained in the limit: all l_j = 0, lt_j = -delta, delta = 1/t: (e-1)N vs eN ; small delta: ~ N t delta
