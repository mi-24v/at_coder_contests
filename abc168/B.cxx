// https://atcoder.jp/contests/abc168/tasks/abc168_b
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

const int K_MAX = 100;

int K;
string S;

void solve() {
  string ans = K >= S.size() ? S : S.erase(K) + "...";
  cout << ans << endl;
}

void input() {
  scanf("%d", &K);
  cin >> S;
}

int main() {
  input();
  solve();
  return 0;
}
