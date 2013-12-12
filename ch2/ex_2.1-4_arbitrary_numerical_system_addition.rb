base = 5
n = 4
n1 = [1, 4, 1, 4]
n2 = [0, 4, 1, 1]
res = Array.new(n+1)

r = 0
(n-1).downto(0) do |i|
	b = n1[i] + n2[i] + r
	r = b / base
	res[i+1] = b % base
end
res[0] = r

puts res

