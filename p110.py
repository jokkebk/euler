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

p = [2, 2, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]#, 43, 47, 53, 59
N = len(p)
w = set()
M = 0
for a in product(range(3), repeat=N):
    v = [1,1,1]
    for i,j in enumerate(a):
        v[j] *= p[i]
    k, m, n = v
    w.add(k*min(n,m)*(n+m))

print(reduce(mul, p[:N]), len(w), 3**N // 2 + 1)
