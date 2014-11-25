from sorting import quicksort, mergesort, insertion_sort
import benchmark.inputs
import benchmark.profiler

if __name__ == '__main__':
    a = benchmark.inputs.random_array(100000, 100, -100)
    p = benchmark.profiler.profile
    i = 0
    j = len(a)-1

    rr = [
        p(mergesort.sort, a[:], i, j),
        p(quicksort.sort, a[:], i, j),
        p(insertion_sort.sort, a[:], i, j),
    ]

    sorted_a = sorted(a)
    for r in rr:
        assert r == sorted_a
