from primes import getprimesieve
from itertools import islice, count

S = lambda r: 2+6*r*(r-1)//2
V = lambda r,p: S(r)+(6*r+p)%(6*r)
P = getprimesieve(10**6)

def gen():
    for r in count(2):
        for i in [0,r,2*r,3*r,4*r,5*r,-1]:
            r0, r1 = i*(r-1)//r, i*(r+1)//r
            vs = [V(r,i-1), V(r,i+1), V(r-1, r0), V(r+1, r1), V(r+1, r1+1)]
            vs += [V(r+1, r1-1)] if i%r == 0 else [V(r-1, r0+1)]
            if sum(1 for v in vs if P[abs(V(r,i)-v)]) == 3: yield V(r,i)

print(next(islice(gen(), 1997, 1998)))
