class Matrix:
    def __init__(self, a, n, m):
        self.a = a
        self.n = n
        self.m = m

    def getRow(self, i):
        j = self.m*i
        return self.a[j:j+self.n]

    def getColumn(self, j):
        return list(self.a[i*self.m+j] for i in range(self.n))

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
        return all(self(i,j) == m(i,j) for i in range(self.m) for j in range(self.n))

    def __mul__(self, s):
        if isinstance(s, Matrix):
            return self.multipleWithMatrix(s)
        else:
            return self.multipleWithScalar(s)

    def multipleWithScalar(self, s):
        return Matrix([s*e for e in self], self.n, self.m)

if __name__ == '__main__':
    a = [1, 3, 2, 4]
    m = Matrix(a, 2, 2)

    assert m.getRow(0) == [1, 3], m.getRow(0)
    assert m.getRow(1) == [2, 4], m.getRow(1)
    assert m.getColumn(0) == [1, 2], m.getColumn(0)
    assert m.getColumn(1) == [3, 4], m.getColumn(1)
    assert m(0, 1) == 3, m(0, 1)
    assert m == Matrix(a, 2, 2)
    print list(x for x in m)
    assert m*2 == Matrix([1, 6, 4, 8], 2, 2), m*2

    
