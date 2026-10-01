from common import *
for n in range(2, 6):
    ms = sp.symbols('m1:%d' % (n+1), positive=True)
    e = [sp.Integer(1)] + [sp.Integer(0)]*n
    for x in ms:
        for k in range(n, 0, -1): e[k] = sp.expand(e[k] + e[k-1]*x)
    I = I_of_e(e)
    M, b = Mb(I, n)
    d = sp.factor(sp.together(sp.Matrix(M).det()))
    target = (-1)**(n*(n+1)//2)*sp.prod([ms[i]+ms[j] for i in range(n) for j in range(i+1, n)])/e[n]
    print(n, 'det M == (-1)^{n(n+1)/2} prod(m_i+m_j)/e_n symbolically:', sp.simplify(d - target) == 0, flush=True)
