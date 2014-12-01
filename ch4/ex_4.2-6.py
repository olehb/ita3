from __future__ import print_function
import random
from matrix import matrix
from matrix import multiplication

def concatenate(matrices, nRows, nCols, n, m):
    for i in range(nRows):
        for k in range(n):
            for j in range(nCols):
                for e in matrices[i*nRows + j].getRow(k):
                    yield e


def multiply(m1, m2, n, routine = multiplication.strassen):
    assert m1.nCols == n and m1.nRows % n == 0 and m2.nRows == n and m2.nCols % n == 0 or m2.nCols == n and m2.nRows % n == 0 and m1.nRows == n and m1.nCols % n == 0

    if m1.nRows > m1.nCols:
        c = list(routine(matrix.Submatrix(m1, i*n, 0, n, n), matrix.Submatrix(m2, 0, j*n, n, n))
                    for i in range(m1.nRows / n)
                        for j in range(m2.nCols / n))
        return matrix.Matrix(list(concatenate(c, m1.nRows / n, m2.nCols / n, n, n)), m1.nRows, m2.nCols)
    else:
        return sum((routine(matrix.Submatrix(m1, 0, i*n, n, n), matrix.Submatrix(m2, i*n, 0, n, n)) for i in range(m1.nCols / n)), matrix.empty(n,n))


def random_array(n, m, p=0):
    return [random.randint(p, m) for x in range(n)]


if __name__ == '__main__':
    n = 8
    k = 10
    m1 = matrix.Matrix(random_array(n*n*k, 10), n*k, n)
    m2 = matrix.Matrix(random_array(n*n*k, 10), n, n*k)

    assert multiply(m1, m2, n) == m1*m2
    assert multiply(m2, m1, n) == m2*m1
