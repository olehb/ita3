from __future__ import print_function
import random

def swap(a, i, j):
    if i == j: 
        return
    t = a[i]
    a[i] = a[j]
    a[j] = t

def choose_pivot(a, p, q):
    return random.randint(p, q)

def partition(a, p, q, i):
    swap(a, p, i)
    j = p+1

    for n in range(p+1,q+1):
        if a[p] >= a[n]:
            swap(a, n, j)
            j += 1

    swap(a, p, j-1)
    return j-1

def quicksort(a, p, q):
    if p >= q:
        return
    i = choose_pivot(a, p, q)
    j = partition(a, p, q, i)
    quicksort(a, p, j-1)
    quicksort(a, j+1, q)

def generate_random_array(n, m):
    return list(random.randint(0, m) for x in range(n))

if __name__ == '__main__':
    for i in range(1000):
        a = generate_random_array(1000, 1000)
        b = a[:]
        quicksort(a, 0, len(a)-1)
        assert sorted(b) == a, a
