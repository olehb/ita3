import time
from random import random

def binary_search(a, v, start, end):
	if end < start:
		return start

	t = (start+end) // 2
	if a[t] == v:
		return t
	elif v < a[t]:
		end = t-1
	else:
		start = t+1

	return binary_search(a, v, start, end)

def insertion_sort(a, p, q):
	for i in range(p+1, q+1):
		j = binary_search(a, a[i], p, i-1)

		if j < i:
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

def test(magnitude):
	k = 15
	a = [int(magnitude * random()) for x in range(magnitude)]
	#a.sort()
	insertion_sort(a, 0, len(a)-1)
	merge_sort(a, 0, len(a)-1, k)
	b = sorted(a)
	assert a == b, a

t = time.clock()
tests = 1
magnitude = 100000
for i in range(tests):
	test(magnitude)
print("Completed %d tests of size %d in %d seconds" % (tests, magnitude, time.clock()-t))
