def get_sum_subset(n, a, s, i):
    if s < n:
        for k in range(i, len(a)):
            c, r = get_sum_subset(n, a, s+a[k], k+1)
            if c == n:
                r.append(a[k])
                return c, r
    return s, [] 

n = pow(10,8)
a = [18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]
s, r = get_sum_subset(n, sorted(a), 0, 0)
assert s == n, s
assert n == sum(r), sum(r)
print(r)
