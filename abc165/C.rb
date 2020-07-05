# https://atcoder.jp/contests/abc165/tasks/abc165_c


N, M, Q = gets.split.map(&:to_i)
as = Array.new(Q)
bs = Array.new(Q)
cs = Array.new(Q)
ds = Array.new(Q)
Q.times do |i|
  as[i], bs[i], cs[i], ds[i] = gets.split.map(&:to_i)
end

puts ans
