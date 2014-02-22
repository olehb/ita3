from random import random

def insertion_sort(a, p, q):
	for i in range(p+1, q+1):
		j = p
		while j < i and a[j] < a[i]:
			j += 1

		if j != i:
			t = a[i]
			a[j+1:i+1] = a[j:i]
			a[j] = t

def merge(a, p, r, q):
	sorted_a = []

	i = p
	j = r+1

	while i <= r and j <= q:
		if a[i] < a[j]:
			sorted_a.append(a[i])
			i += 1
		else:
			sorted_a.append(a[j])
			j += 1
	
	if i <= r:
		sorted_a.extend(a[i:r+1])
	else:
		sorted_a.extend(a[j:q+1])

	a[p:q+1] = sorted_a

def merge_sort(a, p, q, k):
	if (q-p+1) <= k:
		insertion_sort(a, p, q)
	elif p < q:
		r = (p+q) // 2
		merge_sort(a, p, r, k)
		merge_sort(a, r+1, q, k)
		merge(a, p, r, q)

a = [1000 * random() for x in range(10000)]
b = sorted(a)
merge_sort(a, 0, len(a)-1, 10)
assert b == a
