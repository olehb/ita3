import matrix
from matrix import Matrix, Submatrix, concatenate_matrices, multiple_submatrices

def __M(m,n):
    def submatrix(i,j):
        return Submatrix(m, (i-1)*n, (j-1)*n, n, n)
    return submatrix


def simple(m1, m2):
    return m1*m2


def divide_and_conquer(m1, m2):
    assert m1.nCols == m2.nRows
    if m1.nCols == 1:
        return Matrix([m1(0,0) * m2(0,0)], 1, 1)

    n = m1.nCols // 2

    multiple_matrices = divide_and_conquer
    A = __M(m1, n)
    B = __M(m2, n)

    c11 = multiple_matrices(A(1,1), B(1,1)) + multiple_matrices(A(1,2), B(2,1))
    c12 = multiple_matrices(A(1,1), B(1,2)) + multiple_matrices(A(1,2), B(2,2))
    c21 = multiple_matrices(A(2,1), B(1,1)) + multiple_matrices(A(2,2), B(2,1))
    c22 = multiple_matrices(A(2,1), B(1,2)) + multiple_matrices(A(2,2), B(2,2))

    return concatenate_matrices(c11, c12, c21, c22)


def strassen(m1, m2):
    assert m1.nCols == m2.nRows
    if m1.nCols == 1:
        return Matrix([m1(0,0) * m2(0,0)], 1, 1)

    n = m1.nCols // 2

    multiple_matrices = strassen
    A = __M(m1, n)
    B = __M(m2, n)

    s1 = B(1,2) - B(2,2)
    s2 = A(1,1) + A(1,2)
    s3 = A(2,1) + A(2,2)
    s4 = B(2,1) - B(1,1)
    s5 = A(1,1) + A(2,2)
    s6 = B(1,1) + B(2,2)
    s7 = A(1,2) - A(2,2)
    s8 = B(2,1) + B(2,2)
    s9 = A(1,1) - A(2,1)
    s10 = B(1,1) + B(1,2)

    p1 = multiple_matrices(A(1,1), s1)
    p2 = multiple_matrices(s2, B(2,2))
    p3 = multiple_matrices(s3, B(1,1))
    p4 = multiple_matrices(A(2,2), s4)
    p5 = multiple_matrices(s5, s6)
    p6 = multiple_matrices(s7, s8)
    p7 = multiple_matrices(s9, s10)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p5 + p1 - p3 - p7

    return concatenate_matrices(c11, c12, c21, c22)


if __name__ == '__main__':
    m1 = Matrix([1, 2, 3, 4, 5, 12, 0, 1, 1, 12, 3, 5, 23, 6, 67, 7], 4, 4)
    m2 = Matrix([4, 3, 2, 1, 45, 5, 67, 11, 2, 23, 45, 67, 12, 32, 54, 88], 4, 4)
    assert strassen(m1, m2) == m1*m2
    assert divide_and_conquer(m1, m2) == m1*m2
    assert simple(m1, m2) == m1*m2
