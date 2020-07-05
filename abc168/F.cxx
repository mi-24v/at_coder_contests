// https://atcoder.jp/contests/abc168/tasks/abc168_f

#include <cstdio>

using namespace std;

#define REP(i,n)   for(int i=0; i<(int)(n); i++)
#define FOR(i,b,e) for(int i=(b); i<=(int)(e); i++)

const int N_MAX = 1000;
const int M_MAX = 1000;

int N, M;
int A[N_MAX];
int B[N_MAX];
int C[N_MAX];
int D[M_MAX];
int E[M_MAX];
int F[M_MAX];

void solve() {
  int ans = 0;
  printf("%d\n", ans);
}

void input() {
  scanf("%d%d", &N, &M);
  REP(i, N) scanf("%d%d%d", A + i, B + i, C + i);
  REP(i, M) scanf("%d%d%d", D + i, E + i, F + i);
}

int main() {
  input();
  solve();
  return 0;
}
