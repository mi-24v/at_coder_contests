# https://atcoder.jp/contests/abc168/tasks/abc168_d


N, M = gets.split.map(&:to_i)
As = Array.new(M)
Bs = Array.new(M)
M.times do |i|
  As[i], Bs[i] = gets.split.map(&:to_i)
end

puts ans