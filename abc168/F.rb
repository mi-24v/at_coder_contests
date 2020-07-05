# https://atcoder.jp/contests/abc168/tasks/abc168_f


N, M = gets.split.map(&:to_i)
As = Array.new(N)
Bs = Array.new(N)
Cs = Array.new(N)
N.times do |i|
  As[i], Bs[i], Cs[i] = gets.split.map(&:to_i)
end
Ds = Array.new(M)
Es = Array.new(M)
Fs = Array.new(M)
M.times do |i|
  Ds[i], Es[i], Fs[i] = gets.split.map(&:to_i)
end

puts ans
