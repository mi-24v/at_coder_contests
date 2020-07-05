// https://atcoder.jp/contests/abc165/tasks/abc165_c

#include <cstdio>

using namespace std;

const int N_MAX = 10;
const int M_MAX = 10;
const int Q_MAX = 50;
const int D_I_MAX = 1e5;

int N, M, Q;
int a[Q_MAX];
int b[Q_MAX];
int c[Q_MAX];
int d[Q_MAX];

void solve() {
  int ans = 0;
  printf("%d\n", ans);
}

void input() {
  scanf("%d%d%d", &N, &M, &Q);
  REP(i, Q) scanf("%d%d%d%d", a + i, b + i, c + i, d + i);
}

int main() {
  input();
  solve();
  return 0;
}
