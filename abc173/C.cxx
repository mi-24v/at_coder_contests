// https://atcoder.jp/contests/abc173/tasks/abc173_c

#include <cstdio>

using namespace std;

#define REP(i,n)   for(int i=0; i<(int)(n); i++)
#define FOR(i,b,e) for(int i=(b); i<=(int)(e); i++)

const int H_MAX = 6;
const int W_MAX = 6;

int H, W, K;
char c[H_MAX][W_MAX + 1];

void solve() {
  int ans = 0;
  printf("%d\n", ans);
}

void input() {
  scanf("%d%d%d", &H, &W, &K);
  REP(i, H) scanf("%s", c[i]);
}

int main() {
  input();
  solve();
  return 0;
}
