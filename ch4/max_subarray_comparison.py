from __future__ import print_function
from max_subarray import linear, divide_and_conquer, brute_force
import benchmark.inputs
import benchmark.profiler

if __name__ == '__main__':
    a = benchmark.inputs.random_array(100000, 100, -100)

    r = [benchmark.profiler.profile(linear.find_max_subarray, a),
        benchmark.profiler.profile(divide_and_conquer.find_max_subarray, a, 0, len(a)-1),
        benchmark.profiler.profile(brute_force.find_max_subarray, a, 0, len(a)-1)]

    print(r)
