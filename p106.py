from math import factorial
from itertools import combinations

def C(n,r): return factorial(n) // factorial(r) // factorial(n-r)

def gen(N):
    for n in range(2, N//2+1):
        for b in combinations(range(1,n*2), n):
            a = sorted(set(range(n*2)) - set(b))
            if not all([x<y for x,y in zip(a,b)]):
                yield C(N, 2*n)

print(sum(gen(12)))
