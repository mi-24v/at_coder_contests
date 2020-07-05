// https://atcoder.jp/contests/abc168/tasks/abc168_a
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

unsigned int N;

void solve() {
  string ans = "hon";
  unsigned int digit = N % 10;
  if (digit == 3)
    ans = "bon";
  if((digit >= 0 && digit <=1) || digit == 6 || digit == 8 )
    ans = "pon";
  cout << ans << endl;
}

void input() {
  scanf("%d", &N);
}

int main() {
  input();
  solve();
  return 0;
}
