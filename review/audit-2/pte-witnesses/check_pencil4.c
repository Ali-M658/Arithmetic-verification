/* PW.3/PW.5 enumeration, step 1 (exact integer arithmetic).
 * Enumerate every multiset A = {x1<=x2<=x3<=x4} of NONZERO integers with x1+x2+x3+x4 = 0,
 * |xi| <= N, gcd(x1..x4) = 1.  Compute e3, e4 (int64, exact: |e3| <= 4N^3, |e4| <= N^4) and the
 * weighted-projective invariant J = e3^4 / e4^3 as a reduced fraction of __int128
 * No overflow: mode 0, N <= 500: |e3| <= 4N^3 = 5e8, e3^4 < 6.3e34 < 2^127, |e4|^3 <= N^12 < 2.5e32;
 * mode 1, N <= 250: |e3| <= 4(3N)^3 < 1.7e9, e3^4 < 8.6e36 < 2^127 = 1.7e38, |e4|^3 <= (3N)^12 < 3.2e34.
 * N is capped accordingly in main().
 * Sort by J; print every class with >= 2 members (one line per member: e3 e4 x1 x2 x3 x4,
 * classes separated by blank line).  Also prints the number of sets and of e3 = 0 sets.
 * Each set A is identified with -A (same J; -A = (-1)A is a trivial pencil partner, excluded):
 * only the representative with e3 > 0 is kept.
 * Usage: check_pencil4 N [mode] > out
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef __int128 i128;
typedef struct { i128 num, den; long long e3, e4; int x[4]; } rec;
static long long gcdll(long long a, long long b){ if(a<0)a=-a; if(b<0)b=-b; while(b){long long t=a%b;a=b;b=t;} return a; }
static i128 gcd128(i128 a, i128 b){ if(a<0)a=-a; if(b<0)b=-b; while(b){i128 t=a%b;a=b;b=t;} return a; }
static int cmp(const void*p,const void*q){ const rec*a=p,*b=q;
  if(a->num<b->num) return -1; if(a->num>b->num) return 1;
  if(a->den<b->den) return -1; if(a->den>b->den) return 1; return 0; }
int main(int argc,char**argv){
  int N = atoi(argv[1]);
  /* mode 0 (default): all four entries in [-N,N].
     mode 1: three entries a,b,c in [-N,N], the fourth -(a+b+c) unrestricted (|.| <= 3N),
             i.e. at most one entry of absolute value > N (the reading 'A = {a,b,c,-(a+b+c)}, |a|,|b|,|c| <= N'). */
  int mode = argc > 2 ? atoi(argv[2]) : 0;
  if(N > (mode ? 250 : 500)){ fprintf(stderr,"N too large for the int128 bound\n"); return 2; }
  size_t cap = 1<<20, n = 0; rec *R = malloc(cap*sizeof(rec));
  long long nz3 = 0;
  int M = mode ? 3*N : N;
  for(int a=-M;a<=M;a++) for(int b=a;b<=M;b++) for(int c=b;c<=M;c++){
    int d = -(a+b+c);
    if(d < c || d > M) continue;
    int big = (a<-N||a>N) + (b<-N||b>N) + (c<-N||c>N) + (d<-N||d>N);
    if(big > (mode ? 1 : 0)) continue;
    if(!a||!b||!c||!d) continue;
    if(gcdll(gcdll(a,b),gcdll(c,d)) != 1) continue;
    long long A=a,B=b,C=c,D=d;
    long long e3 = A*B*C + A*B*D + A*C*D + B*C*D;
    long long e4 = A*B*C*D;
    if(e3 == 0){ nz3++; continue; }   /* e1=e3=0: symmetric {u,-u,v,-v}, self-cancelling */
    if(e3 < 0) continue;  /* A and -A have the same J and lambda(-A) = -A... ; keep the representative with e3>0
                             (each unordered pair {A,-A} is enumerated once with e3>0, since e3(-A)=-e3(A)) */
    i128 t3 = (i128)e3*e3; t3 = t3*t3;  /* e3^4 > 0 */
    i128 t4 = (i128)e4*e4*e4;
    if(t4 < 0){ t4 = -t4; t3 = -t3; }
    i128 g = gcd128(t3,t4);
    if(n==cap){ cap*=2; R = realloc(R,cap*sizeof(rec)); }
    R[n].num = t3/g; R[n].den = t4/g; R[n].e3=e3; R[n].e4=e4;
    R[n].x[0]=a; R[n].x[1]=b; R[n].x[2]=c; R[n].x[3]=d; n++;
  }
  qsort(R,n,sizeof(rec),cmp);
  long long classes=0, members=0;
  for(size_t i=0;i<n;){
    size_t j=i; while(j<n && R[j].num==R[i].num && R[j].den==R[i].den) j++;
    if(j-i>=2){ classes++; members += j-i;
      for(size_t k=i;k<j;k++) printf("%lld %lld %d %d %d %d\n",R[k].e3,R[k].e4,R[k].x[0],R[k].x[1],R[k].x[2],R[k].x[3]);
      printf("\n"); }
    i=j;
  }
  fprintf(stderr,"N=%d sets(e3!=0)=%zu sets(e3=0)=%lld classes>=2: %lld members: %lld\n",N,n,nz3,classes,members);
  printf("# mode=%d N=%d sets_e3_nonzero=%zu sets_e3_zero=%lld classes=%lld members=%lld\n",mode,N,n,nz3,classes,members);
  return 0;
}
