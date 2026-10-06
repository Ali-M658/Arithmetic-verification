/* PW.3 / PW.5 n = 5 claim, step 1: enumerate every multiset of five NONZERO integers with
 * s1 = sum xi = 0 and s3 = sum xi^3 = 0 (equivalently e1 = e3 = 0, 'odd symmetric') and gcd = 1.
 *   mode 0: all five |xi| <= N.
 *   mode 1: at most one entry with |xi| > N (the reading {a,b,c,d,-(a+b+c+d)}, |a|,..,|d| <= N).
 * Loop: q1<=q2<=q3<=q4 in [-N,N] nonzero, e = -(q1+..+q4).  If |e| <= N the multiset is counted
 * only when e >= q4 (e is its largest element: each multiset once).  If |e| > N (mode 1 only)
 * the big entry is unique, so the multiset is counted once.  Exact int64 (|s3| <= 4N^3 + (4N)^3).
 * Prints one sorted set per line.  Usage: check_n5 N mode
 */
#include <stdio.h>
#include <stdlib.h>
static long long gcdll(long long a, long long b){ if(a<0)a=-a; if(b<0)b=-b; while(b){long long t=a%b;a=b;b=t;} return a; }
static long long cube(long long x){ return x*x*x; }
int main(int argc,char**argv){
  int N = atoi(argv[1]); int mode = atoi(argv[2]); long long cnt=0;
  for(int a=-N;a<=N;a++){ if(!a) continue;
   for(int b=a;b<=N;b++){ if(!b) continue;
    for(int c=b;c<=N;c++){ if(!c) continue;
     long long s3abc = cube(a)+cube(b)+cube(c);
     for(int d=c;d<=N;d++){ if(!d) continue;
      int e = -(a+b+c+d); if(!e) continue;
      int small = (e >= -N && e <= N);
      if(small){ if(e < d) continue; }
      else if(!mode) continue;
      if(s3abc + cube(d) + cube(e)) continue;
      if(gcdll(gcdll(gcdll(a,b),gcdll(c,d)),e)!=1) continue;
      int v[5]={a,b,c,d,e};
      if(!small && e < d){ /* insertion of e into sorted position */
        for(int i=4;i>0 && v[i]<v[i-1];i--){ int t=v[i];v[i]=v[i-1];v[i-1]=t; } }
      printf("%d %d %d %d %d\n",v[0],v[1],v[2],v[3],v[4]); cnt++;
  }}}}
  printf("# mode=%d N=%d count=%lld\n",mode,N,cnt);
  return 0;
}
