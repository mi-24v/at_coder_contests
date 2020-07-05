# https://atcoder.jp/contests/abc168/tasks/abc168_e

MOD = 1000000007

N = gets.to_i
As = Array.new(N)
Bs = Array.new(N)
N.times do |i|
  As[i], Bs[i] = gets.split.map(&:to_i)
end

puts ans
