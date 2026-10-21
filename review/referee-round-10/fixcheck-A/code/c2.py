from fractions import Fraction as F
def ok(m):
    P1=sum(m); R=sum(F(1,x) for x in m)
    return R>1 and (P1-1)*(R-1)>=9
n1=0;n1b=0
for c in range(2,1001):
    for d in range(c,1001):
        m=(2,2,c,d)
        if ok(m): n1+=1
        if c>=3 and ok(m): n1b+=1
print('2,2,c,d (c>=2):',n1,' (c>=3):',n1b)
n2=0; n2b=0
for a in (2,3):
    for b in range(max(a,3),40):
        for c in range(b,40):
            R3=F(1,a)+F(1,b)+F(1,c)
            if R3+F(1,20000)<=1: 
                # R>1 needs 1/d > 1-R3
                pass
            for d in range(c,20001):
                R=R3+F(1,d)
                if R<=1: break
                if (a+b+c+d-1)*(R-1)>=9: n2+=1
print('b>=3:',n2)
