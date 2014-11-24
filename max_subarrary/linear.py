from __future__ import print_function
import random

def find_max_subarray(a):
    m1 = 0
    m2 = 0
    m = a[0]

    t1 = 0
    t2 = 0
    t = a[0]

    for i in range(1, len(a)):
        if t > 0:
            t += a[i]
            t2 = i
        else:
            t = a[i]
            t1 = t2 = i

        if t > m:
            m1 = t1
            m2 = t2
            m = t

    return (m1, m2, m)

def generate_random_array(n, m, p=0):
    return list(random.randint(p, m) for x in range(n))

if __name__ == '__main__':
    import cProfile, pstats, StringIO
    pr = cProfile.Profile()
    a = generate_random_array(1000000, 100, -100)
    pr.enable()
    (l, h, m) = find_max_subarray(a)
    pr.disable()
    print(a[l:h+1], m)
    s = StringIO.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
