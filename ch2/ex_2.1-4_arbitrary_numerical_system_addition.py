#!/usr/bin/env python3

base = 10
n = 4

n2 = (2, 2, 2, 2)
n1 = (0, 0, 3, 0)

result = []
r = 0

for i in range(n-1, -1, -1):
	v = n1[i] + n2[i] + r
	r = v // base
	result.append(v % base)

if r>0:
	result.append(r)

result.reverse()

print(result)

