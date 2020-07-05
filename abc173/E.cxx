// https://atcoder.jp/contests/abc173/tasks/abc173_e

#include <cstdio>

using namespace std;

#define REP(i,n)   for(int i=0; i<(int)(n); i++)
#define FOR(i,b,e) for(int i=(b); i<=(int)(e); i++)

const int N_MAX = 2*1e5;
const int A_I_MAX = 1e9;
const int MOD = 1e9+7;

int N, K;
int A[N_MAX];

void solve() {
  int ans = 0;
  printf("%d\n", ans);
}

void input() {
  scanf("%d%d", &N, &K);
  REP(i, N) scanf("%d", A + i);
}

int main() {
  input();
  solve();
  return 0;
}
