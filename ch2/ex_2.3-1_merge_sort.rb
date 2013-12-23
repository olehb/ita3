def merge a, p, r, q
	sorted_a = Array.new(q-p+1)
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
		sorted_a[k, sorted_a.length-k] = a[i, r-i+1]
	elsif j <= q
		sorted_a[k, sorted_a.length-k] = a[j, q-j+1]
	end
	
	a[p,sorted_a.length]=sorted_a
end

def merge_sort a, p, q
	if p != q
		r = (q-p) / 2
		merge_sort a, p, p+r
		merge_sort a, p+r+1, q
		merge a, p, p+r, q
	end
end

a = (0..30).to_a.shuffle
puts a.to_s
merge_sort a, 0, a.length-1
puts a.to_s
