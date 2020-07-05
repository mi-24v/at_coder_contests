// https://atcoder.jp/contests/abc173/tasks/abc173_b

#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <boost/range/combine.hpp>
#include <boost/foreach.hpp>

const int N_MAX = 1e5;

int N;
std::vector<std::string> S;
std::vector<std::string> ans_key = {"AC","WA","TLE","RE"};

void solve() {
  std::vector<int> ans(4);
  for(int index = 0; index < ans_key.size(); index++){
    for(std::string s : S){
      if(s.compare(ans_key[index]) == 0)
        ans[index] += 1;
    }
  }
  std::string k;
  int v;
  BOOST_FOREACH(boost::tie(k,v), boost::combine(ans_key,ans)){
    std::cout << k << " x " << v << std::endl;
  }
}

void input() {
  scanf("%d", &N);
  for(int i=0;i<N;i++){
    std::string s;
    std::cin >> s;
    S.push_back(s);
  }
}

int main() {
  input();
  solve();
  return 0;
}
