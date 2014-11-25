import insertion_sort

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


def sort(a, p, q, k = 8):
    if q-p < k:
        return insertion_sort.sort(a, p, q)
    if p < q:
        r = (p+q) // 2
        sort(a, p, r, k)
        sort(a, r+1, q, k)
        merge(a, p, r, q)
    return a

if __name__ == '__main__':
    a = [57, -46, -72, 68, 86, 65, 89, 24, 61, -46]
    b = sort(a, 0, len(a)-1)
    assert b == sorted(a), b
