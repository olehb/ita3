def binary_search(a, v, start, end):
	if end < start:
		return start

	m = (start+end) // 2
	if a[m] == v:
		return m
	elif v < a[m]:
		end = m-1
	else:
		start = m+1

	return binary_search(a, v, start, end)

if __name__ == '__main__':
    a = [4, 5, 6, 8, 9]
    b = binary_search(a, 5, 0, len(a)-1)
    assert b == 1
