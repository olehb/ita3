def multiple_submatrices(m1, i1, j1, m2, i2, j2, n, m, p):
    return Matrix(list(sum(m1(i1+i,j1+x)*m2(i2+x,j2+j) for x in range(m)) for i in range(n) for j in range(p)), n, p)


def concatenate_matrices(m1, m2, m3, m4):
    def generate_elements():
        for i in range(m1.nRows+m3.nRows):
            for j in range(m1.nCols+m2.nCols):
                if i < m1.nRows:
                    yield m1(i,j) if j < m1.nCols else m2(i,j-m1.nCols)
                else:
                    yield m3(i-m1.nRows,j) if j < m3.nCols else m4(i-m1.nRows,j-m3.nCols)
    return Matrix(list(generate_elements()), m1.nRows+m3.nRows, m1.nCols+m2.nCols)


class AbstractMatrix:
    def __init__(self, nRows, nCols):
        self.nRows = nRows
        self.nCols = nCols

    def getDimensions(self):
        return (self.nRows, self.nCols)

    def __add__(self, m):
        return Matrix(list(self(i,j) + m(i,j) for i in range(self.nCols) for j in range(self.nRows)), self.nRows, self.nCols)

    def __sub__(self, m):
        return Matrix(list(self(i,j) - m(i,j) for i in range(self.nCols) for j in range(self.nRows)), self.nRows, self.nCols)

    def __repr__(self):
        return '\n'.join(' '.join(map(str, self.getRow(i))) for i in range(self.nRows))

    def __eq__(self, m):
        return self.getDimensions() == m.getDimensions() and all(self(i,j) == m(i,j) for i in range(self.nRows) for j in range(self.nCols))

    def __mul__(self, s):
        if isinstance(s, self.__class__):
            return self.multipleWithMatrix(s)
        else:
            return self.multipleWithScalar(s)

    def __rmul__(self, s):
        return self*s

    def __neg__(self):
        return self*-1

    def multipleWithScalar(self, s):
        return Matrix([e*s for e in self], self.nRows, self.nCols)

    def multipleWithMatrix(self, m):
        (n1, m1) = m.getDimensions()
        a = list(sum(self(i,x)*m(x,j) for x in range(self.nCols)) for i in range(self.nRows) for j in range(m1))
        return Matrix(a, self.nRows, m1)


class Submatrix(AbstractMatrix):
    def __init__(self, p, i, j, n, m):
        AbstractMatrix.__init__(self, n, m)
        self.__p = p
        self.__i = i
        self.__j = j

    def getRow(self, i):
        return self.__p.getRow(self.__i+i)[self.__j:self.__j+self.nCols]

    def getColumn(self, j):
        return self.__p.getColumn(self.__j+j)[self.__i:self.__i+self.nRows]

    def __iter__(self):
        for i in range(self.nRows):
            for j in self.__p.getRow(self.__i+i):
                yield j

    def __call__(self, i, j):
        return self.__p(self.__i+i, self.__j+j)


class Matrix(AbstractMatrix):
    def __init__(self, a, n, m):
        assert n*m == len(a), "%sx%s != %s" % (n, m, len(a))
        AbstractMatrix.__init__(self, n, m)
        self.__a = a

    def getRow(self, i):
        j = self.nCols*i
        return self.__a[j:j+self.nCols]

    def getColumn(self, j):
        return list(self.__a[i*self.nCols+j] for i in range(self.nRows))

    def __iter__(self):
        return iter(self.__a)

    def __call__(self, i, j):
        return self.__a[self.nCols*i + j]


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
    assert Submatrix(m1, 0, 1, 2, 1)*Submatrix(m2, 1, 1, 1, 3) == Matrix([3, 5], 2, 1)*Matrix([12, 14, 16], 1, 3)

    c1 = Matrix([1, 2, 3, 4], 2, 2)
    assert concatenate_matrices(c1, 10*c1, 100*c1, 1000*c1) == Matrix([1, 2, 10, 20, 3, 4, 30, 40, 100, 200, 1000, 2000, 300, 400, 3000, 4000], 4, 4)
