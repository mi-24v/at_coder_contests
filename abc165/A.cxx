// https://atcoder.jp/contests/abc165/tasks/abc165_a

#include <cstdio>

using namespace std;

// #define REP(i,n)   for(int i=0; i<(int)(n); i++)
// #define FOR(i,b,e) for(int i=(b); i<=(int)(e); i++)

const int B_MAX = 1000;
const int K_MAX = 1000;

int K;
int A, B;

bool judge() {
  if ( K > B ) return false;
  for(int i=A; i<=B; i++) {
    if ( i % K == 0 )return true;
  }
  return false;
}

void solve() {
  bool cond = judge();
  puts(cond ? "OK" : "NG");
}

void input() {
  scanf("%d", &K);
  scanf("%d%d", &A, &B);
}

int main() {
  input();
  solve();
  return 0;
}
