import random

def random_array(n, m, p=0):
    return [random.randint(p, m) for x in range(n)]
