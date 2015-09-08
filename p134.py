from primes import getprimesieve
from chinese import chinese_remainder

def S(p,q):
    d = 10
    while d<p: d*=10
    return chinese_remainder([d,q],[p,0])

p = sorted({i for i,v in enumerate(getprimesieve(10**6+5)) if v})

print(sum(S(p[i], p[i+1]) for i in range(2, len(p)-1)))
