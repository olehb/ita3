import random
import array_partition

def choose_pivot(a, p, q):
    return random.randint(p, q)

def sort(a, p, q):
    if p < q:
        i = choose_pivot(a, p, q)
        j = array_partition.partition(a, p, q, i)
        sort(a, p, j-1)
        sort(a, j+1, q)
    return a
