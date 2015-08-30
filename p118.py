from itertools import permutations
from primes import initpoulet, prime

def ok(s, prev=0):
    if not s: return 1
    v, w = 0, 0
    for i,d in enumerate(s):
        v = v*10 + d
        if v > prev and prime(v):
            w += ok(s[i+1:], v)
    return w

initpoulet()
print(sum(ok(p) for p in permutations(range(1,10), 9)))
