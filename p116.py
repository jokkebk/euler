from math import factorial
from itertools import combinations

def C(n,r): return factorial(n) // factorial(r) // factorial(n-r)

def ways(M, N):
    for b in range(1,N//M+1): yield C(N-b*M + b, b)

print(sum(sum(ways(m, 50)) for m in range(2,5)))
