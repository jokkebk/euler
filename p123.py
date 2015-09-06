from primes import getprimesieve

rem = lambda pn,n: 2*n*pn % pn**2 if n&1 else 2

p = sorted({i for i,v in enumerate(getprimesieve(10**6)) if v})

print(next(i for i,v in enumerate(p) if rem(v,i+1) > 1e10)+1)
