from __future__ import print_function
import random

def find_max_subarray(a, p, q):
    if p==q:
        return (p, q, a[p])
    m = a[q]
    low = q
    high = q
    for i in range(p,q):
        c = a[i]
        if c > m:
            m = c
            low = i
            high = i

        for j in range(i+1,q+1):
            c += a[j]
            if c > m:
                m = c
                low = i
                high = j
    return (low, high, m)

def generate_random_array(n, m, p=0):
    return list(random.randint(p, m) for x in range(n))

if __name__ == '__main__':
    a = generate_random_array(100000, 100, -100)
    (l, h, m) = find_max_subarray(a, 0, len(a)-1)
    print(a[l:h+1], m)

