def quicksort(a):
	if len(a) > 1:
		p = a.pop(len(a) // 2)
		l, g = [], []
		for x in a:
			if x < p:
				l.append(x)
			else:
				g.append(x)

		return quicksort(l) + [p] + quicksort(g)
	else:
		return a

from random import random
magnitude = 10000
a = [int(magnitude * random()) for x in range(magnitude)]
b = sorted(a)
a = quicksort(a)
assert a == b, a
