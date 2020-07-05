// https://atcoder.jp/contests/abc173/tasks/abc173_f

#include <cstdio>

using namespace std;

#define REP(i,n)   for(int i=0; i<(int)(n); i++)
#define FOR(i,b,e) for(int i=(b); i<=(int)(e); i++)

const int N_MAX = 2*1e5;

int N;
int u[N_MAX-1];
int v[N_MAX-1];

void solve() {
  int ans = 0;
  printf("%d\n", ans);
}

void input() {
  scanf("%d", &N);
  REP(i, N-1) scanf("%d%d", u + i, v + i);
}

int main() {
  input();
  solve();
  return 0;
}
