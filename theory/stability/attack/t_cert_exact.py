from cert import *
for m, dc in [((2,8,8), F('2.342e-3')), ((3,3,12), F('4.040e-3')), ((3,10,15,30), F('3.660e-3')), ((4,5,21,28), F('1.462e-3'))]:
    C = Cert(m)
    lo, hi = float(dc)*0.995, float(dc)*1.005
    for _ in range(25):
        mid = (lo+hi)/2
        if C.test(F(mid).limit_denominator(10**14), True): lo = mid
        else: hi = mid
    print(m, 'tabulated delta_cert=%s  coherent test passes at tabulated value: %s ; certified sup ~ %.7e' % (float(dc), C.test(dc, True), lo), flush=True)
