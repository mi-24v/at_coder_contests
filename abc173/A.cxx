// https://atcoder.jp/contests/abc173/tasks/abc173_a

#include <cstdio>

using namespace std;

const int N_MAX = 10000;

int N;

void solve() {
  int ans = 0;
  int surplus = N % 1000;
  if(surplus != 0){
    ans = 1000 - surplus;
  }
  printf("%d\n", ans);
}

void input() {
  scanf("%d", &N);
}

int main() {
  input();
  solve();
  return 0;
}
