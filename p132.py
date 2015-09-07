from itertools import islice, count
from primes import gcd, getprimesieve

def A(n):
    m = 1
    for i in range(2,n+2):
        m = (10*m+1) % n
        if not m: return i
    return -1

P = sorted({i for i,v in enumerate(getprimesieve(10**6)) if v})

# For all primes p>5, p-1 is divisible by A(p) (as per problem 130 def)
# Therefore, if A(p) divides 10**9, it is a subset of 2**9 and 5**9,
# So gcd(p-1, 10**9) still contains whole A(p), and
# 10^gcd(10**9, p-1)-1 is divisible by p, i.e. 10^gcd(10**9, p-1)%p == 1
print(sum(islice((p for p in P[3:10**6] if pow(10,gcd(10**9, p-1),p) == 1), 0, 40)))

# Original brute force
#print(sum(islice((p for p in P[3:10**6] if gcd(p-1, 10**9) > 1 and 10**9 % A(p) == 0), 0, 40)))
