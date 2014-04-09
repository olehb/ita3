def merge_calculate_inversions(a, p, r, q):
	sorted_a = []
	i = p
	j = r+1

	inversions = 0

	while i <= r and j <= q:
		if a[i] > a[j]:
			inversions += r-i+1
			sorted_a.append(a[j])
			j += 1
		else:
			sorted_a.append(a[i])
			i += 1

	if i <= r:
		sorted_a.extend(a[i:r+1])
	elif j <= q:
		sorted_a.extend(a[j:q+1])

	a[p:q+1] = sorted_a
	
	return inversions

def merge(a, p, q):
	if p < q:
		r = (p+q) // 2
		i = merge(a, p, r)
		i += merge(a, r+1, q)
		i += merge_calculate_inversions(a, p, r, q)
		return i
	else:
		return 0


from random import random
magnitude = 10
size = 4
a = [int(magnitude*random()) for i in range(size)]
print a
b = sorted(a[:])
print merge(a, 0, len(a)-1)
assert a == b, a





