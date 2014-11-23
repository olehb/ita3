import random

def merge(a, p, r, q):
	sorted_a = []
	i = p
	j = r+1
	while i<=r and j <=q:
		if a[i] < a[j]:
			sorted_a.append(a[i])
			i += 1
		else:
			sorted_a.append(a[j])
			j += 1
	
	if i<=r:
		sorted_a += a[i:r+1]
	
	if j<=q:
		sorted_a += a[j:q+1]

	a[p:q+1] = sorted_a
	return a

def merge_sort(a, p, q):
	if  p<q:
		r = (p+q)/2
		merge_sort(a, p, r-1)
		merge_sort(a, r, q)
		merge(a, p, r, q)
	return a

a = [int(1000000*random.random()) for i in xrange(20000000)]
merge_sort(a, 0, len(a)-1)
