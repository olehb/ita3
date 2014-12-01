def multiply_complex(a, b, c, d):
    p1 = a*(c-d)
    p2 = d*(a-b)
    p3 = c*(a+b)

    return p1+p2, p3-p1

if __name__ == '__main__':
    a = 2
    b = 3
    c = 4
    d = 5
    assert multiply_complex(a, b, c, d) == (a*c - b*d, a*d + b*c)

