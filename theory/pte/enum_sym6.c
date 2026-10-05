// enumerate triples 0<a1<a2<a3<=M (distinct allowed equal? allow a1<=a2<=a3), key (sum a^2, sum a^4); print collisions
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef struct {unsigned __int128 k; int a,b,c;} E;
int cmp(const void*x,const void*y){const E*p=x,*q=y; return p->k<q->k?-1:p->k>q->k;}
int main(int argc,char**argv){int M=atoi(argv[1]); size_t n=0,cap=(size_t)M*M*M/6+M*M+10; E*e=malloc(cap*sizeof(E));
 for(int a=1;a<=M;a++)for(int b=a;b<=M;b++)for(int c=b;c<=M;c++){uint64_t s2=(uint64_t)a*a+(uint64_t)b*b+(uint64_t)c*c; unsigned __int128 s4=(unsigned __int128)a*a*a*a+(unsigned __int128)b*b*b*b+(unsigned __int128)c*c*c*c; e[n].k=(s4<<40)|s2; e[n].a=a;e[n].b=b;e[n].c=c;n++;}
 qsort(e,n,sizeof(E),cmp);
 for(size_t i=0;i<n;){size_t j=i;while(j<n&&e[j].k==e[i].k)j++; if(j-i>1){for(size_t x=i;x<j;x++)for(size_t y=x+1;y<j;y++)printf("%d %d %d %d %d %d\n",e[x].a,e[x].b,e[x].c,e[y].a,e[y].b,e[y].c);} i=j;}
 return 0;}
