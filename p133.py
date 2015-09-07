from itertools import islice, count
from primes import gcd, getprimesieve

def A(n):
    m = 1
    for i in range(2,n+2):
        m = (10*m+1) % n
        if not m: return i
    return -1

P = sorted({i for i,v in enumerate(getprimesieve(10**5)) if v})

S = 3 # 1 and 2 fail test below
for p in P:
    # Same optimization as in 132, clean other factors than 2 and 5
    # and try 10**x % p with that
    a, q = 1, p-1
    while q%5==0: a, q = a*5, q//5
    while q%2==0: a, q = a*2, q//2
    if pow(10, a, p) != 1: S += p
    #a = A(p)
    #while a%5==0: a//=5
    #if a&(a-1): S += p
print(S)
