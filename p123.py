from primes import getprimesieve

rem = lambda p,n: 2*n*p[n] % p[n]**2 if n&1 else 2

p = sorted({i for i,v in enumerate(getprimesieve(10**6)) if v and i})

print(next(i for i,v in enumerate(p) if rem(p,i) > 1e10))
