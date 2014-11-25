def swap(a, i, j):
    if i == j: 
        return
    t = a[i]
    a[i] = a[j]
    a[j] = t

def partition(a, p, q, i):
    swap(a, p, i)
    j = p+1

    for n in range(p+1,q+1):
        if a[p] >= a[n]:
            swap(a, n, j)
            j += 1

    swap(a, p, j-1)
    return j-1
