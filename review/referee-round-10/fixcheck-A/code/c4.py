import mpmath as mp, itertools
mp.mp.dps=40
def sys(p,q,r,maxlen=10):
    a,b,c=mp.pi/p,mp.pi/q,mp.pi/r
    # side PQ opposite angle at R (c): cosh d = (cos a cos b + cos c)/(sin a sin b)
    d=mp.acosh((mp.cos(a)*mp.cos(b)+mp.cos(c))/(mp.sin(a)*mp.sin(b)))
    def rot(th,center_dist):
        # rotation by th about point i*e^{center_dist}
        R=mp.matrix([[mp.cos(th/2),mp.sin(th/2)],[-mp.sin(th/2),mp.cos(th/2)]])
        S=mp.matrix([[mp.e**(center_dist/2),0],[0,mp.e**(-center_dist/2)]])
        return S*R*S**-1
    A=rot(2*a,0); B=rot(2*b,d)
    gens=[A,A**-1,B,B**-1]
    best=mp.inf
    # BFS over reduced words
    frontier=[(mp.eye(2),-1)]
    for L in range(1,maxlen+1):
        new=[]
        for M,last in frontier:
            for i,g in enumerate(gens):
                if last>=0 and i==last^1: continue
                N=M*g; t=abs(N[0,0]+N[1,1])
                if t>2+mp.mpf('1e-20'):
                    best=min(best,2*mp.acosh(t/2))
                new.append((N,i))
        frontier=new
    return best
print('(3,3,12)',sys(3,3,12,11)); print('(2,8,8)',sys(8,8,2,11))
