from primes import getprimes
from util import chinese_remainder

def S(p,q):
    d = next(10**i for i in range(1,9) if 10**i > p)
    return chinese_remainder([d,q],[p,0])

p = sorted(getprimes(10**6+5))

print(sum(S(p[i], p[i+1]) for i in range(2, len(p)-1)))
