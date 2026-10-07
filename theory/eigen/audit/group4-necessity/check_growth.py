"""Group 4 audit: (a) the pigeonhole count of eig:N1; (b) growth of N(eps) in Theorem E (eig:E),
to test the closing sentence of 'What is not proved' ("N grows roughly like 1/eps^2").
t_* = min(t_1,t_2,t_3); t_1 does not depend on eps, so for eps small t_* = t_3 and the growth
exponent can be read off with t_* = min(t_2,t_3) (we do not need t_1's value for the exponent).
"""
import math
import mpmath as mp
mp.mp.dps = 50

# (a) pigeonhole: c = ceil(Lambda_N/delta) boxes per coordinate, coordinates j = 1..N-1
for N in range(1, 6):
    for delta in (mp.mpf(1), mp.mpf('0.1'), mp.mpf('0.013')):
        h7 = mp.acosh(1/(2*mp.sin(mp.pi/7)))
        LamN = mp.mpf(1)/4 + mp.pi**2*N**2/h7**2
        c = int(mp.ceil(LamN/delta))
        K = c**(N - 1)
        if not LamN/c <= delta:
            raise AssertionError("box width")
        # bound for j<N is <= 1/4 + pi^2 N^2 / h_m^2 <= Lambda_N with equality only for m=7, j=N-1
        for m in range(8, 60):
            hm = mp.acosh(1/(2*mp.sin(mp.pi/m)))
            if not mp.mpf(1)/4 + mp.pi**2*N**2/hm**2 < LamN:
                raise AssertionError("monotonicity")
print("(a) pigeonhole: box width Lambda_N/ceil(Lambda_N/delta) <= delta; bounds < Lambda_N for m>7")
print("    note: for m=7, j=N-1 the stated bound equals Lambda_N; strictness of the box argument"
      " needs lambda_j < Lambda_N (true: the Rayleigh bound is strict since q<1/4) or half-open boxes.")


# (b) growth of N(eps)
def a_l(l):
    return abs(mp.bernoulli(2*l + 2))/(2*mp.factorial(l + 1)*(2*l + 1))


def N_of_eps(A, M, eps):
    eps = mp.mpf(eps)
    nstar = int(mp.floor(A/mp.pi)) + 4
    kstar = nstar
    LM = 1
    for i in range(1, M + 1):
        LM = LM*i//math.gcd(LM, i)
    gam = min([mp.mpf(1)/(2*LM)] + [a_l(k - 2) for k in range(2, kstar + 1)])
    d0 = min(eps/2, mp.acosh(1 + 2/(mp.pi**2*M**2)))
    r0 = d0/2
    rho1 = mp.asinh(mp.sinh(r0)*mp.sin(mp.pi/M))
    v0 = 2*mp.pi*min((mp.cosh(r0) - 1)/M, mp.cosh(rho1) - 1)
    D = 4*r0*A/v0
    p = kstar - mp.mpf(3)/2
    varpi = 63*eps*mp.e**(eps/2)/((1 - mp.e**(-eps))*mp.sqrt(4*mp.pi))
    y0 = 2*(3*D + mp.log(16*varpi/gam) + p*mp.log(4/eps**2) + p*mp.log(2*p/mp.e))
    t2 = eps**2/(2*(1 + eps)); t3 = eps**2/(4*max(y0, 1))
    ts = min(t2, t3)
    Gs = gam/2*ts**(kstar - 2)
    Zb = lambda s: A/(4*mp.pi*s) + nstar*(M**2 - 1)/(12*mp.mpf(M)) + 1
    Lam = 2/ts*mp.log(8*Zb(ts/2)/Gs)
    N = mp.floor(mp.e*Zb(1/Lam)) + 1
    return N, D, t3, ts


for A, M in ((2*mp.pi, 4), (mp.pi/3, 7)):
    print(f"(b) A={mp.nstr(A, 5)}, M={M}")
    prev = None
    for e in range(1, 8):
        eps = mp.mpf(10)**-e
        N, D, t3, ts = N_of_eps(A, M, eps)
        line = f"   eps=1e-{e}: D={mp.nstr(D, 6)}  t3={mp.nstr(t3, 6)}  N={mp.nstr(N, 6)}"
        if prev is not None:
            line += f"  dlogN/dlog(1/eps)={mp.nstr(mp.log10(N/prev), 4)}"
        prev = N
        print(line)
    N1, _, _, _ = N_of_eps(A, M, mp.mpf(10)**-12)
    N2, _, _, _ = N_of_eps(A, M, mp.mpf(10)**-13)
    slope = mp.log10(N2/N1)
    if not (2.9 < slope < 3.3):
        raise AssertionError(f"unexpected growth exponent {slope}")
    print(f"   exponent at eps~1e-12: {mp.nstr(slope, 5)}  (D ~ 1/eps, t3 ~ eps^3, N ~ eps^-3 log(1/eps))")
print("GROWTH CHECKS PASSED: N(eps) grows like eps^-3 log(1/eps), not eps^-2")
