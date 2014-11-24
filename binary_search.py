def binary_search(a, v, start, end):
	if end < start:
		return -1

	m = (start+end) // 2
	if a[m] == v:
		return m
	elif a[m] > v:
		end = m-1
	else:
		start = m+1

	return binary_search(a, v, start, end)

a = sorted('spam')
print a
print binary_search(a, 's', 0, len(a)-1) 
