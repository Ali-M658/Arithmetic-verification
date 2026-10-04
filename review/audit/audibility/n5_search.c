/* Exhaustive search for 5-element multisets 2 <= a <= b <= c <= d <= e <= N sharing
 * I_4 = (R, P1, P3, P5).  Integer arithmetic only (int64 / __int128 where products can overflow).
 * Multisets are bucketed by P1; within a bucket they are sorted by (P3, reduced R, P5).
 * Output: total multisets, number of I_3 = (R,P1,P3) collision classes (sensitivity control),
 * number of I_4 collision classes, and the first few I_4 collisions if any.
 * Usage: n5_search N
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct { int64_t p3, rn, rd, p5; int v[5]; } rec;

static int64_t gcd64(int64_t a, int64_t b) { if (a < 0) a = -a; if (b < 0) b = -b;
  while (b) { int64_t t = a % b; a = b; b = t; } return a; }

static int cmp(const void *x, const void *y) {
  const rec *a = x, *b = y;
  if (a->p3 != b->p3) return a->p3 < b->p3 ? -1 : 1;
  if (a->rn != b->rn) return a->rn < b->rn ? -1 : 1;
  if (a->rd != b->rd) return a->rd < b->rd ? -1 : 1;
  if (a->p5 != b->p5) return a->p5 < b->p5 ? -1 : 1;
  return 0;
}

int main(int argc, char **argv) {
  int N = atoi(argv[1]);
  long long total = 0, c3 = 0, c4 = 0;
  size_t cap = 1 << 20; rec *buf = malloc(cap * sizeof(rec));
  for (int S = 10; S <= 5 * N; S++) {
    size_t cnt = 0;
    for (int a = 2; 5 * a <= S; a++)
      for (int b = a; a + 4 * b <= S; b++)
        for (int c = b; a + b + 3 * c <= S; c++) {
          int rem = S - a - b - c;          /* d + e = rem, c <= d <= e <= N */
          int dlo = c > rem - N ? c : rem - N;
          for (int d = dlo; 2 * d <= rem; d++) {
            int e = rem - d;
            if (e > N || e < d) continue;
            int v[5] = {a, b, c, d, e};
            int64_t p3 = 0, p5 = 0, e5 = 1, e4 = 0;
            for (int i = 0; i < 5; i++) {
              int64_t x = v[i];
              p3 += x * x * x; p5 += x * x * x * x * x; e5 *= x;
            }
            for (int i = 0; i < 5; i++) e4 += e5 / v[i];
            int64_t g = gcd64(e4, e5);
            if (cnt == cap) { cap *= 2; buf = realloc(buf, cap * sizeof(rec)); }
            rec *r = &buf[cnt++];
            r->p3 = p3; r->p5 = p5; r->rn = e4 / g; r->rd = e5 / g;
            for (int i = 0; i < 5; i++) r->v[i] = v[i];
          }
        }
    total += cnt;
    qsort(buf, cnt, sizeof(rec), cmp);
    size_t i = 0;
    while (i < cnt) {
      size_t j = i + 1;
      while (j < cnt && buf[j].p3 == buf[i].p3 && buf[j].rn == buf[i].rn && buf[j].rd == buf[i].rd) j++;
      if (j - i > 1) {
        c3++;
        if (c3 <= 3) {
          printf("I3-collision S=%d:", S);
          for (size_t t = i; t < j && t < i + 3; t++)
            printf(" {%d,%d,%d,%d,%d}", buf[t].v[0], buf[t].v[1], buf[t].v[2], buf[t].v[3], buf[t].v[4]);
          printf("\n");
        }
        for (size_t s = i; s + 1 < j; s++)
          if (buf[s].p5 == buf[s + 1].p5) {
            c4++;
            if (c4 <= 10)
              printf("I4-COLLISION {%d,%d,%d,%d,%d} {%d,%d,%d,%d,%d}\n",
                     buf[s].v[0], buf[s].v[1], buf[s].v[2], buf[s].v[3], buf[s].v[4],
                     buf[s+1].v[0], buf[s+1].v[1], buf[s+1].v[2], buf[s+1].v[3], buf[s+1].v[4]);
          }
      }
      i = j;
    }
  }
  printf("N=%d total=%lld I3_collision_classes=%lld I4_collision_pairs=%lld\n", N, total, c3, c4);
  return 0;
}
