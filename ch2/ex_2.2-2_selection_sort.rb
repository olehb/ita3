a = [2, 1, 0, 4, 12]

for i in 0..(a.length-2) do # n
	min_i = i #n-1
	for j in (i+1)..(a.length-1) do #sum(i+1, n) = t_i
		if a[j] < a[min_i] #t_i - 1
			min_i = j #t_i - 1
		end
	end
	t = a[min_i] #n-1
	a[min_i] = a[i] #n-1
	a[i] = t #n-1
end

puts a
