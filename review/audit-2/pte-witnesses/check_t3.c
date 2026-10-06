/* T_3 search (PW.0 item 6, PW.1 rem:ptet3): size-8 genus collisions sharing three coefficients.
 *
 * Shape (3,5) (Descartes bound, re-derived in REVIEW.md): Z = X + (-Y), X = {x1,x2,x3} positive
 * rationals, Y = {y1..y5} positive integers (the five-element side; Z is scaled so that Y is integral),
 *     sum x = sum y = p1,   sum x^3 = sum y^3 = p3,   sum 1/x = sum 1/y = r.
 * With e_k = e_k(X):  e1 = p1,  p3 = e1^3 - 3 e1 e2 + 3 e3,  r = e2/e3, hence (p1 r > 1 always)
 *     e3 = (p3 - p1^3) / (3 (1 - p1 r)),   e2 = r e3,
 * and X exists iff the monic cubic  f(x) = x^3 - e1 x^2 + e2 x - e3  has three rational roots
 * (they are then automatically real and positive since e1, e2, e3 > 0).
 *
 * CERTIFIED FILTER.  Let p > max(Y) be a prime, p != 3.  Then every y is a p-unit, so r is p-integral.
 * If D = 1 - p1 r is a p-unit (D mod p != 0), e1, e2, e3 are p-integral; a monic polynomial with
 * p-integral coefficients has only p-integral rational roots, so if f splits over Q, f mod p is a
 * product of three linear factors over F_p.  Hence "f mod p does not split completely" PROVES that
 * Y admits no X.  If D = 0 mod p the prime is inconclusive and Y is NOT rejected by it.
 * Splitting over F_p is a table lookup (bitset of all (a,b,c) with x^3+ax^2+bx+c = prod (x - r_i)).
 * A Y is rejected as soon as one of NP primes rejects it; every survivor is written out and
 * verified exactly in Python (check_t3_verify.py).  The loop covers EVERY multiset
 * 1 <= y1 <= ... <= y5 <= N (primitive or not), i.e. C(N+4,5) multisets.
 *
 * -DSQUARE: positive control on a modified problem (sum x^2 = sum y^2 in place of the cubes):
 *     e1 = p1, e2 = (p1^2 - p2)/2, e3 = e2 / r (p-integral when r mod p != 0, else inconclusive).
 *
 * -DDELTA=d: planted positive control on the modified problem sum x^3 = sum y^3 + d (same code path as
 *     the real search, the target p3 is shifted by the constant d).  With d = 12300 the planted solution
 *     Y0 = {2,2,8,8,8}, X0 = {1,3,24} exists (sum 28, reciprocal sum 2, cubes 15876 = 1576 + 12300);
 *     with d = 18099612: Y0 = {2,2,28,77,220}, X0 = {1,20,308} (top of the range, y5 = 220).
 *
 * Usage: check_t3 N nproc k tag     (process k of nproc takes y1 = k+1, k+1+nproc, ...)
 * Checkpoint: <tag>_ckpt_<k>.txt gets "done y1 count" after each y1 (flushed); on restart the
 * finished y1 are skipped.  Survivors: <tag>_surv_<k>.txt, "y1 y2 y3 y4 y5" per line.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define NP 16
static const int PR[NP] = {223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307};
#define P0 223
#ifndef DELTA
#define DELTA 0
#endif
static uint8_t *tab[NP];
static int invt[NP][320];
static long long cntrej[NP+1];
static inline int getbit(int k, long idx){ return (tab[k][idx>>3] >> (idx&7)) & 1; }
static int mod(long long a, int p){ a %= p; return a<0 ? (int)(a+p) : (int)a; }

static void build(void){
  for(int k=0;k<NP;k++){
    int p=PR[k]; long n=(long)p*p*p;
    tab[k]=calloc((n>>3)+1,1);
    for(int r1=0;r1<p;r1++) for(int r2=r1;r2<p;r2++) for(int r3=r2;r3<p;r3++){
      int a=mod(-(long long)(r1+r2+r3),p), b=mod((long long)r1*r2+(long long)r1*r3+(long long)r2*r3,p),
          c=mod(-(long long)r1*r2*r3,p);
      long idx=((long)a*p+b)*p+c; tab[k][idx>>3] |= (uint8_t)(1u<<(idx&7));
    }
    invt[k][0]=0;
    for(int x=1;x<p;x++) for(int y=1;y<p;y++) if((x*y)%p==1){ invt[k][x]=y; break; }
  }
}
/* returns 1 if prime k does NOT reject (split or inconclusive), 0 if it rejects */
static int test_prime(int k, const int *y){
  int p=PR[k]; long long p1=0,p2=0,p3=0; int r=0;
  for(int i=0;i<5;i++){ p1+=y[i]; p2+=(long long)y[i]*y[i]; p3+=(long long)y[i]*y[i]*y[i]; r=(r+invt[k][y[i]%p])%p; }
  int P1=mod(p1,p), P3=mod(p3+(long long)DELTA,p), e2, e3;
#ifndef SQUARE
  int D=mod(1-(long long)P1*r,p); if(!D) return 1;
  int t=mod((long long)P3-(long long)P1*P1%p*P1,p);
  e3=(int)((long long)t*invt[k][(3*D)%p]%p); e2=(int)((long long)r*e3%p);
#else
  (void)P3; int P2=mod(p2,p);
  if(!r) return 1;
  e2=(int)((long long)mod((long long)P1*P1-P2,p)*invt[k][2]%p); e3=(int)((long long)e2*invt[k][r]%p);
#endif
  long idx=((long)mod(-P1,p)*p+e2)*p+mod(-e3,p);
  return getbit(k,idx);
}

int main(int argc,char**argv){
  if(argc<5){ fprintf(stderr,"usage\n"); return 2; }
  int N=atoi(argv[1]), nproc=atoi(argv[2]), K=atoi(argv[3]); const char*tag=argv[4];
  if(N>=P0){ fprintf(stderr,"N must be < smallest prime\n"); return 2; }
  build();
  /* self-test of the tables against brute-force root counting on random cubics */
  srand(12345);
  for(int k=0;k<NP;k++){ int p=PR[k];
    for(int it=0;it<20000;it++){ int a=rand()%p,b=rand()%p,c=rand()%p;
      /* count roots with multiplicity by repeated synthetic division */
      int co[4]={c,b,a,1}, deg=3, roots=0;
      for(int x=0;x<p && deg>0;){ long long v=0; for(int i=deg;i>=0;i--) v=(v*x+co[i])%p;
        if(v==0){ int q[4]; q[deg-1]=co[deg]; for(int i=deg-1;i>0;i--) q[i-1]=(int)((co[i]+(long long)q[i]*x)%p);
          for(int i=0;i<deg;i++) co[i]=q[i]; co[deg]=0; deg--; roots++; }
        else x++; }
      int split=(roots==3); long idx=((long)a*p+b)*p+c;
      if(split!=getbit(k,idx)){ fprintf(stderr,"TABLE SELF-TEST FAILED p=%d\n",p); return 3; } } }
  /* resume */
  char fn[512]; static char done[1024]; memset(done,0,sizeof done);
  snprintf(fn,sizeof fn,"%s_ckpt_%d.txt",tag,K);
  FILE*ck=fopen(fn,"r"); if(ck){ int a; long long c; while(fscanf(ck,"done %d %lld\n",&a,&c)==2) done[a]=1; fclose(ck); }
  ck=fopen(fn,"a");
  snprintf(fn,sizeof fn,"%s_surv_%d.txt",tag,K); FILE*sv=fopen(fn,"a");
  int cub0[256], iv0[256];
  for(int y=1;y<=N;y++){ cub0[y]=(int)(((long long)y*y%P0)*y%P0); iv0[y]=invt[0][y%P0]; }
  for(int y1=K+1;y1<=N;y1+=nproc){
    if(done[y1]) continue;
    long long cnt=0;
    for(int y2=y1;y2<=N;y2++) for(int y3=y2;y3<=N;y3++) for(int y4=y3;y4<=N;y4++){
      int s1=(y1+y2+y3+y4)%P0, s3=(int)((cub0[y1]+cub0[y2]+cub0[y3]+cub0[y4]+(long long)DELTA%P0+P0)%P0), sr=(iv0[y1]+iv0[y2]+iv0[y3]+iv0[y4])%P0;
#ifdef SQUARE
      int s2=(int)(((long long)y1*y1+(long long)y2*y2+(long long)y3*y3+(long long)y4*y4)%P0);
#endif
      for(int y5=y4;y5<=N;y5++){
        cnt++;
        int P1=s1+y5; if(P1>=P0) P1-=P0;
        int R=sr+iv0[y5]; if(R>=P0) R-=P0;
        int e2,e3;
#ifndef SQUARE
        int P3=s3+cub0[y5]; if(P3>=P0) P3-=P0;
        int D=(1+P0*P0-P1*R)%P0;
        if(D){
          int t=(P3+P0-(P1*P1%P0)*P1%P0)%P0;
          e3=t*invt[0][(3*D)%P0]%P0; e2=R*e3%P0;
          long idx=((long)((P0-P1)%P0)*P0+e2)*P0+(P0-e3)%P0;
          if(!getbit(0,idx)){ cntrej[0]++; continue; }
        }
#else
        (void)s3;
        int P2=(s2+y5*y5)%P0;
        if(R){
          e2=(int)((long long)((P1*P1-P2+P0*P0)%P0)*invt[0][2]%P0); e3=e2*invt[0][R]%P0;
          long idx=((long)((P0-P1)%P0)*P0+e2)*P0+(P0-e3)%P0;
          if(!getbit(0,idx)){ cntrej[0]++; continue; }
        }
#endif
        int y[5]={y1,y2,y3,y4,y5}, rej=0;
        for(int k=1;k<NP;k++) if(!test_prime(k,y)){ cntrej[k]++; rej=1; break; }
        if(rej) continue;
        cntrej[NP]++;
        fprintf(sv,"%d %d %d %d %d\n",y1,y2,y3,y4,y5);
      }
    }
    fflush(sv);
    fprintf(ck,"done %d %lld\n",y1,cnt); fflush(ck);
  }
  fprintf(stderr,"rejections by prime index:"); for(int k=0;k<NP;k++) fprintf(stderr," %lld",cntrej[k]);
  fprintf(stderr,"  survivors %lld\n",cntrej[NP]);
  fclose(ck); fclose(sv);
  return 0;
}
