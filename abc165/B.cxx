// https://atcoder.jp/contests/abc165/tasks/abc165_b
#include <iostream>
#include <cmath>

unsigned long int X;

//(100 * 1.01).floor*1.01.floor)*1.01.floor... >= X
unsigned int calc(){
  double balance = 100.0;
  const double rate = 1.01;
  unsigned int n = 0;
  while(balance < X){
    balance = floor(balance * rate);
    n++;
  }
  return n;
}

void solve() {
  unsigned int ans = calc();
  std::cout << ans << std::endl;
}

void input() {
  std::cin >> X;
}

int main() {
  input();
  solve();
  return 0;
}
