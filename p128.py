from primes import getprimesieve
from itertools import islice, count

N = lambda r,i: 2+6*r*(r-1)//2+(6*r+i)%(6*r)
P = getprimesieve(10**6)

def gen():
    for r in count(2):
        for i in [0,r,2*r,3*r,4*r,5*r,-1]:
            p0, p1 = i*(r-1)//r, i*(r+1)//r
            vs = [N(r,i-1), N(r,i+1), N(r-1, p0), N(r+1, p1), N(r+1, p1+1)]
            vs += [N(r+1, p1-1)] if i%r == 0 else [N(r-1, p0+1)]
            if sum(1 for v in vs if P[abs(N(r,i)-v)]) == 3: yield N(r,i)

print(next(islice(gen(), 1997, 1998)))
