import random

def binary_search(a, v, start, end):
	while start <= end:
		m = (start+end) // 2
		if a[m] == v:
			return m+1
		elif a[m] > v:
			end = m-1
		else:
			start = m+1

	return start

def insertion_sort(a):
	for i in range(1,len(a)):
		for j in range(i):
			p = binary_search(a, a[i], 0, i-1) 
			t = a[i]
			a[p+1:i+1] = a[p:i]
			a[p] = t

n = 100
a = [int(n*random.random()) for x in range(n)]
b = a[:]
insertion_sort(a)
assert sorted(b) == a, str(a)
