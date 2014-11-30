import matrix
from matrix import Matrix, Submatrix, concatenate_matrices, multiple_submatrices

def multiple(m1, m2):
    assert m1.nCols == m2.nRows

    n = m1.nCols // 2

    c11 = multiple_submatrices(m1, 0, 0, m2, 0, 0, n, n, n) + multiple_submatrices(m1, 0, n, m2, n, 0, n, n, n)
    c12 = multiple_submatrices(m1, 0, 0, m2, 0, n, n, n, n) + multiple_submatrices(m1, 0, n, m2, n, n, n, n, n)
    c21 = multiple_submatrices(m1, n, 0, m2, 0, 0, n, n, n) + multiple_submatrices(m1, n, n, m2, n, 0, n, n, n)
    c22 = multiple_submatrices(m1, n, 0, m2, 0, n, n, n, n) + multiple_submatrices(m1, n, n, m2, n, n, n, n, n)

    return concatenate_matrices(c11, c12, c21, c22)

if __name__ == '__main__':
    m1 = Matrix([1, 2, 3, 4], 2, 2)
    m2 = Matrix([4, 3, 2, 1], 2, 2)
    assert multiple(m1, m2) == m1*m2




