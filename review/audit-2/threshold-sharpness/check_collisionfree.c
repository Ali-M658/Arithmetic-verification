/* Exact exhaustive search for two-coefficient collisions at fixed sum S.
   For each S in [S0,S1]: enumerate 2<=p<=q<=r, p+q+r=S, hyperbolic iff qr+rp+pq < pqr.
   R = e2/e3 reduced by gcd (64-bit; e3 <= (S/3)^3 < 2^37 for S<=4800).
   Collision = two distinct triads with equal reduced R; every hash hit is re-checked
   by exact __int128 cross-multiplication.  No floating point.
   Output per S:  S ntriads collision(0/1) [first pair found]
   Usage: ./a.out S0 S1 outfile   (appends; one line per S, flushed = checkpoint) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64;
static u64 gcd(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
#define HB 23
#define HS (1u<<HB)
static u64 kn[HS],kd[HS]; static uint32_t gen[HS]; static int tp[HS],tq[HS];
int main(int argc,char**argv){
  long S0=atol(argv[1]),S1=atol(argv[2]); FILE*f=fopen(argv[3],"a");
  if(!f) return 2;
  if(S1>4800){fprintf(stderr,"range\n");return 2;}
  uint32_t g=0;
  for(long S=S0;S<=S1;S++){
    g++; long nt=0; int col=0; long cp1=0,cq1=0,cp2=0,cq2=0;
    for(long p=2;3*p<=S;p++) for(long q=p;2*q<=S-p;q++){
      long r=S-p-q; u64 e2=(u64)(p*q+q*r+r*p), e3=(u64)p*q*r;
      if(!(e2<e3)) continue;
      nt++;
      if(col) continue;
      u64 d=gcd(e2,e3), N=e2/d, D=e3/d;
      u64 h=(N*0x9E3779B97F4A7C15ULL ^ (D+0x632BE59BD9B4E019ULL)*0xC2B2AE3D27D4EB4FULL);
      uint32_t i=(uint32_t)(h>>(64-HB));
      for(;;){
        if(gen[i]!=g){gen[i]=g;kn[i]=N;kd[i]=D;tp[i]=(int)p;tq[i]=(int)q;break;}
        if(kn[i]==N&&kd[i]==D){
          long p2=tp[i],q2=tq[i],r2=S-p2-q2;
          __int128 a=(__int128)(p2*q2+q2*r2+r2*p2)*(__int128)e3;
          __int128 b=(__int128)e2*(__int128)((u64)p2*q2*r2);
          if(a!=b){fprintf(stderr,"hash/gcd inconsistency at S=%ld\n",S);return 3;}
          if(p2==p&&q2==q){fprintf(stderr,"duplicate triad\n");return 3;}
          col=1;cp1=p2;cq1=q2;cp2=p;cq2=q;break;}
        i=(i+1)&(HS-1);
      }
    }
    if(col) fprintf(f,"%ld %ld 1 %ld,%ld,%ld %ld,%ld,%ld\n",S,nt,cp1,cq1,S-cp1-cq1,cp2,cq2,S-cp2-cq2);
    else fprintf(f,"%ld %ld 0\n",S,nt);
    fflush(f);
  }
  fclose(f); return 0;
}
