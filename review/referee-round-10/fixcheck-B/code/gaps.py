import mpmath as mp, sympy as sp, itertools, sys
sys.path.insert(0,'.')
from consts import b_l, alpha
mp.mp.dps=30
from fractions import Fraction as F
def sig(Aover2pi, M):
    out=[]
    ns=int(mp.floor(2*Aover2pi))+4  # A/pi = 2*A/2pi
    for g in range(0,ns//4+1):
        for n in range(0,ns-4*g+1):
            for ms in itertools.combinations_with_replacement(range(2,M+1),n):
                s=2*g-2+sum(1-F(1,m) for m in ms)
                if 0<s<=Aover2pi: out.append((g,ms,s))
    return out
def I1(t):
    t=mp.mpf(t)
    return mp.e**(-t/4)/t-mp.quad(lambda r:4*r*mp.e**(-t*(0.25+r*r))/(mp.e**(2*mp.pi*r)+1),[0,1,5,40])
def E(m,t):
    t=mp.mpf(t);tot=0
    for j in range(1,m):
        th=mp.pi*j/m
        f=lambda r:mp.e**(-2*th*r-t*(0.25+r*r))/(1+mp.e**(-2*mp.pi*r))
        tot+=mp.quad(f,[-200,-20,-2,0,2,20,400])/(2*m*mp.sin(th))
    return tot
B1={ # from Table B1
 0:dict(A=F(1,4),M=8,t='0.025643',I='38.66536513',E=['0.1234174363','0.2185160355','0.3055983432','0.3885180925','0.4684419328','0.5458108691','0.6208237663'],Th='0.01588'),
 1:dict(A=F(1,4),M=12,t='0.02482',I='39.95840220',E=['0.1234676152','0.2186322319','0.3058109679','0.3888639381','0.4689603839','0.5465413064','0.6218038055','0.6948563105','0.7657755576','0.8346286578','0.9014814272'],Th='0.006527'),
 2:dict(A=F(2,3),M=3,t='0.08524',I='11.40384039',E=['0.1198849911','0.2105230871'],Th='0.1520'),
 3:dict(A=F(2,3),M=3,t='0.0060028',I='166.2559916',E=['0.1246259455','0.2213381939'],Th='0.1655'),
 4:dict(A=F(2,3),M=12,t='0.0034221',I='291.8851232',E=['0.1247864837','0.2217169676','0.3115434968','0.3983739192','0.4835438032','0.5675984568','0.6507886471','0.7332359758','0.8149991014','0.8961038659','0.9765583484'],Th='0.001373'),
 5:dict(A=F(1,1),M=3,t='0.000092402',I='10821.94325',E=['0.1249942251','0.2222085343'],Th='0.1666'),
}
def ulp(sdec):
    d=sdec.split('.')[1]; return F(1,10**len(d))
for k,r in B1.items():
    t=r['t'];M=r['M']
    # check decimals vs mpmath
    i1=I1(t); di=abs(i1-mp.mpf(r['I']))
    dE=max(abs(E(m,t)-mp.mpf(r['E'][m-2])) for m in range(2,M+1))
    S=sig(r['A'],M)
    Ifr=F(r['I']); Efr={m:F(r['E'][m-2]) for m in range(2,M+1)}
    G=[]
    for g,ms,s in S:
        val=s/2*Ifr+sum(Efr[m] for m in ms)
        err=s/2*ulp(r['I'])+len(ms)*ulp(r['E'][0])
        G.append((val,err,(g,ms)))
    best=None;cnt=0
    for a,b in itertools.combinations(G,2):
        lo=abs(a[0]-b[0])-a[1]-b[1]
        gap=abs(a[0]-b[0])
        if best is None or gap<best[0]-F(1,10**9): best=(gap,lo,a[2],b[2]);
    gaps=sorted(((abs(a[0]-b[0]),a[2],b[2]) for a,b in itertools.combinations(G,2)))
    mn=gaps[0][0]; ties=[x for x in gaps if x[0]-mn<F(1,10**8)]
    minlo=min(abs(a[0]-b[0])-a[1]-b[1] for a,b in itertools.combinations(G,2))
    maxerr=max(x[1] for x in G)
    print(k,'|Sig|',len(S),'dI',mp.nstr(di,3),'dEmax',mp.nstr(dE,3),'mingap',float(mn),'minlo>=Th',minlo>=F(r['Th']),'maxerr',float(maxerr),'ratio err/(Th/16)',float(maxerr/(F(r['Th'])/16)),'ties',[(x[1],x[2]) for x in ties])
