def merge a, p, r, q
	n = q-p+1
	sorted_a = Array.new(n)
	i = p
	j = r+1
	k = 0

	while i <= r and j <= q
		if a[i] < a[j]
			sorted_a[k] = a[i]
			i += 1
		else
			sorted_a[k] = a[j]
			j += 1
		end
		k += 1
	end

	if i <= r
		sorted_a[k, n-k] = a[i, r-i+1]
	elsif j <= q
		sorted_a[k, n-k] = a[j, q-j+1]
	end

	a[p, n] = sorted_a
end

def merge_sort a, p, q
	if p < q
		r = p+(q-p)/2
		merge_sort a, p, r 
		merge_sort a, r+1, q
		merge a, p, r, q
	end
end

a = (1..20000000).to_a.shuffle
puts 'done'

#merge_sort a, 0, a.length-1
#puts 'done'
