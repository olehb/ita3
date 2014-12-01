from __future__ import print_function
from matrix import multiplication, matrix
import benchmark.inputs
import benchmark.profiler

if __name__ == '__main__':
    n = 8
    m1 = matrix.Matrix(benchmark.inputs.random_array(pow(2,n*2), 100, -100), pow(2,n), pow(2,n))
    m2 = matrix.Matrix(benchmark.inputs.random_array(pow(2,n*2), 100, -100), pow(2,n), pow(2,n))
    p = benchmark.profiler.profile

    #print(m1*m2)

    r = [p(multiplication.strassen, m1, m2), 
         p(multiplication.divide_and_conquer, m1, m2),
         p(multiplication.simple, m1, m2)]
    print(r)
