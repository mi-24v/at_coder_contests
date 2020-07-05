// https://atcoder.jp/contests/abc168/tasks/abc168_c

#include <cstdio>
#include <cmath>
#include <boost/math/constants/constants.hpp>
#include <boost/multiprecision/cpp_dec_float.hpp>

const int A_MAX = 1000;
const int B_MAX = 1000;
const int H_MAX = 11;
const int M_MAX = 59;

int A, B, H, M;

namespace BC = boost::math::constants;
namespace MP = boost::multiprecision;

double time_to_angle(){
  double long_hand = H/6 * BC::pi<double>();
  double short_hand = M/30 * BC::pi<double>();
  double delta_1 = abs(long_hand - short_hand);
  double delta_2 = abs(short_hand - long_hand);
  double val = long_hand > short_hand ? delta_1 : delta_2;
  return val;
}

void solve() {
  auto a = MP::cpp_dec_float<100>(A);
  auto b = MP::cpp_dec_float<100>(B);
  double ans = sqrt(pow(sqrt(a),2)+pow(sqrt(b),2)-2.0*A*B*cos(time_to_angle()));
  printf("%lf\n", ans);
}

void input() {
  scanf("%d%d%d%d", &A, &B, &H, &M);
}

int main() {
  input();
  solve();
  return 0;
}
