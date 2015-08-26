from itertools import product
from functools import reduce
from operator import mul

def ways(n):
    w = 0
    for i in range(2,2*n+1):
        if n==i: continue
        j = n*i // (i-n)
        if j >= i and n*(i+j) == i*j: w += 1
    return w

p = list(reversed([2, 3, 5, 7, 11, 13]))
for t in product(range(1,3), repeat=6):
    n = reduce(mul, [p[i]**v for i,v in enumerate(t)])
    w = ways(n)
    if w > 1000:
        print(n, w)
        break
