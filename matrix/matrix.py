from __future__ import print_function

def multiple_submatrices(m1, i1, j1, m2, i2, j2, n, m, p):
    return Matrix(list(sum(m1(i1+i,j1+x)*m2(i2+x,j2+j) for x in range(m)) for i in range(n) for j in range(p)), n, p)

class Matrix:
    def __init__(self, a, n, m):
        assert n*m == len(a)
        self.a = a
        self.n = n
        self.m = m

    def getRow(self, i):
        j = self.m*i
        return self.a[j:j+self.m]

    def getColumn(self, j):
        return list(self.a[i*self.m+j] for i in range(self.n))

    def getDimensions(self):
        return (self.n, self.m)

    def __iter__(self):
        for e in self.a: 
            yield e

    def __call__(self, i, j):
        return self.a[self.m*i + j]

    def __add__(self, m):
        return Matrix(list(self(i,j) + m(i,j) for i in range(self.m) for j in range(self.n)), self.n, self.m)

    def __sub__(self, m):
        return Matrix(list(self(i,j) - m(i,j) for i in range(self.m) for j in range(self.n)), self.n, self.m)

    def __repr__(self):
        return '\n'.join(' '.join(map(str, self.getRow(i))) for i in range(self.n))

    def __eq__(self, m):
        return self.getDimensions() == m.getDimensions() and all(self(i,j) == m(i,j) for i in range(self.n) for j in range(self.m))

    def __mul__(self, s):
        if isinstance(s, Matrix):
            return self.multipleWithMatrix(s)
        else:
            return self.multipleWithScalar(s)

    def __rmul__(self, s):
        return self*s

    def __neg__(self):
        return self*-1

    def multipleWithScalar(self, s):
        return Matrix([e*s for e in self], self.n, self.m)

    def multipleWithMatrix(self, m):
        (n1, m1) = m.getDimensions()
        a = list(sum(self(i,x)*m(x,j) for x in range(self.m)) for i in range(self.n) for j in range(m1))
        return Matrix(a, self.n, m1)


if __name__ == '__main__':
    a = [1, 3, 2, 4, 5, 8]
    m = Matrix(a, 2, 3)
    assert m.getRow(0) == [1, 3, 2], m.getRow(0)
    assert m.getRow(1) == [4, 5, 8], m.getRow(1)
    assert m.getColumn(0) == [1, 4], m.getColumn(0)
    assert m.getColumn(1) == [3, 5], m.getColumn(1)
    assert m(0, 1) == 3, m(0, 1)
    assert m.getDimensions() == (2,3), m.getDimensions()
    assert m == Matrix(a[:], 2, 3)
    assert m*2 == Matrix([2, 6, 4, 8, 10, 16], 2, 3), m*2
    assert 2*m == Matrix([2, 6, 4, 8, 10, 16], 2, 3), 2*m
    assert -m == Matrix([-1, -3, -2, -4, -5, -8], 2, 3), -m

    m1 = Matrix([1, 3, 4, 5], 2, 2)
    m2 = Matrix([2, 4, 6, 8, 10, 12, 14, 16], 2, 4)
    m3 = Matrix([32, 40, 48, 56, 58, 76, 94, 112], 2, 4)

    assert m1*m2 == m3, m1*m2
    assert multiple_submatrices(m1, 0, 1, m2, 1, 1, 2, 1, 3) == Matrix([3, 5], 2, 1)*Matrix([12, 14, 16], 1, 3)

