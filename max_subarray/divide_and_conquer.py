from __future__ import print_function
import random

def find_max_subarray_intersected(a, p, r, q):
    c1 = a[r]
    m1 = c1
    i1 = r
    for i in range(r-1, p-1, -1):
        c1 += a[i]
        if c1 > m1:
            m1 = c1
            i1 = i
    c2 = a[r+1]
    m2 = c2
    i2 = r+1
    for i in range(r+2, q+1):
        c2 += a[i]
        if c2 > m2:
            m2 = c2
            i2 = i
    return (i1, i2, m1+m2)

def find_max_subarray(a, p, q):
    if p == q:
        return (p, q, a[p])

    r = (p+q) // 2
    (p1, q1, m1) = find_max_subarray(a, p, r)
    (p2, q2, m2) = find_max_subarray(a, r+1, q)
    (p3, q3, m3) = find_max_subarray_intersected(a, p, r, q)

    m = max(m1, m2, m3)
    if m1 == m:
        return (p1, q1, m1)
    if m2 == m:
        return (p2, q2, m2)
    return (p3, q3, m3)

def generate_random_array(n, m, p=0):
    return list(random.randint(p, m) for x in range(n))

if __name__ == '__main__':
    import cProfile, pstats, StringIO
    pr = cProfile.Profile()
    a = generate_random_array(1000000, 100, -100)
    pr.enable()
    (l, h, m) = find_max_subarray(a, 0, len(a)-1)
    pr.disable()
    #print(a[l:h+1], m)
    print(m)
    s = StringIO.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
