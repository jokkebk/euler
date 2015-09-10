from itertools import islice, count
from primes import getprimesieve

def A(n):
    m = 1
    for i in range(2,n+2):
        m = (10*m+1) % n
        if not m: return i
    return -1

P = getprimesieve(10**6)

print(sum(islice((i for i in count(9,2) \
        if i%5 and not (P[i] or (i-1)%A(i))), 0, 25)))
