from itertools import product
from primes import getprimesieve

P = getprimesieve(10**6)

print(sum(1 for i,j in product(range(1,600), repeat=2) \
        if i<j and (j**3-i**3) < 1e6 and P[j**3-i**3]))
