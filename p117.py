from math import factorial
from itertools import product
from operator import mul

def C(n,r): return factorial(n) // factorial(r) // factorial(n-r)

def ways(N):
    for v in product(range(26), repeat=3):
        f, n = N - sum(map(mul, v, (2,3,4))), sum(v)
        if f >= 0: yield C(f+n, n) * C(n, v[0]) * C(n-v[0], v[1])

print(sum(ways(50)))
