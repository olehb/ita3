import random

def insertion_sort(a, p):
	if p > 0:
		insertion_sort(a, p-1)
		#print a[:p], a[p]
		for i in range(p):
			if a[i] > a[p]:
				t = a[p];
				a[i+1:p+1] = a[i:p]
				a[i] = t
				break
		#print a[:p+1]

a = [int(10000*random.random()) for x in range(20)]
b = a[:]
insertion_sort(a, len(a)-1)
assert sorted(b) == a
