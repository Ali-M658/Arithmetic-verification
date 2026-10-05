#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
typedef struct {u128 k; uint64_t s2; short a,b,c,d;} E;
int cmp(const void*x,const void*y){const E*p=x,*q=y; if(p->k!=q->k) return p->k<q->k?-1:1; if(p->s2!=q->s2) return p->s2<q->s2?-1:1; return 0;}
int main(int argc,char**argv){int M=atoi(argv[1]); size_t n=0,cap=(size_t)M*M*M*M/24+(size_t)M*M*M+100; E*e=malloc(cap*sizeof(E));
 for(int a=1;a<=M;a++)for(int b=a;b<=M;b++)for(int c=b;c<=M;c++)for(int d=c;d<=M;d++){
   u128 s4=0,s6=0; uint64_t s2=0; int v[4]={a,b,c,d};
   for(int i=0;i<4;i++){u128 x=v[i]*v[i]; s2+=x; s4+=x*x; s6+=x*x*x;}
   e[n].k=(s6<<40)^(s4); e[n].s2=s2; e[n].a=a;e[n].b=b;e[n].c=c;e[n].d=d;n++;}
 qsort(e,n,sizeof(E),cmp);
 for(size_t i=0;i<n;){size_t j=i;while(j<n&&e[j].k==e[i].k&&e[j].s2==e[i].s2)j++;
   if(j-i>1)for(size_t x=i;x<j;x++)for(size_t y=x+1;y<j;y++)printf("%d %d %d %d %d %d %d %d\n",e[x].a,e[x].b,e[x].c,e[x].d,e[y].a,e[y].b,e[y].c,e[y].d);
   i=j;}
 return 0;}
