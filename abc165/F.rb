# https://atcoder.jp/contests/abc165/tasks/abc165_f


N = gets.to_i
as = gets.split.map(&:to_i)
us = Array.new(N-1)
vs = Array.new(N-1)
N-1.times do |i|
  us[i], vs[i] = gets.split.map(&:to_i)
end

puts ans
