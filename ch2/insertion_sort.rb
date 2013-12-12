a = [3, 2, 1, 5, 8, 9, 0, -1, 18]

for j in 1..(a.length-1)
	key = a[j]
	i = j-1
	while i>=0 and a[i]>key
		a[i+1] = a[i]
		i -= 1
	end
	a[i+1] = key
end

puts a
