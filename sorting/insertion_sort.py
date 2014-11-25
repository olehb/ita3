import binary_search

def sort(a, p, q):
    for i in range(p+1, q+1):
        k = binary_search.binary_search(a, a[i], p, i-1) 
        if k < i:
            t = a[i]
            a[k+1:i+1] = a[k:i]
            a[k] = t
    return a

if __name__ == '__main__':
    a = [57, -46, -72, 68, 86, 65, 89, 24, 61, -46]
    b = sort(a, 0, len(a)-1)
    assert b == sorted(a), b
