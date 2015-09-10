from collections import Counter, defaultdict
from operator import mul
from functools import reduce

def gcd(a,b):
    while a: a, b = b % a, a
    return b

# Generate pythagorean triples where c < N
def pythag(N):
    for n in range(1,N):
        if 2*n*n > N: break
        for m in range(n+1,int((N-n*n)**.5)+1, 2):
            if gcd(m,n)!=1: continue
            a, b, c = m*m-n*n, 2*m*n, m*m+n*n
            yield (a,b,c) if a<b else (b,a,c)

def prime(n): return n==2 or (n not in prime.poulet and pow(2, n-1, n) == 1)

def initpoulet():
    prime.poulet = {}
    with open('poulet.txt', 'r') as f:
        for s in f: prime.poulet[int(s)] = True

def getprimesieve(N):
    primes = [False,False] + [True]*(N-1)
    for i in range(2,int(N**.5)):
        if not primes[i]: continue
        for j in range(i*2, N+1, i): primes[j] = False
    return primes

getprimes = lambda N: {i for i,v in enumerate(getprimesieve(N)) if v}

def getdivs(N):
    divs = [0] * (N+1)
    for i in range(2,int(N**.5)):
        if divs[i]: continue # not prime
        for j in range(i*2, N+1, i): divs[j] = i
    return divs

def factor(divs, n):
    facts = Counter()
    while divs[n]:
        facts[divs[n]] += 1
        n //= divs[n]
    facts[n] += 1
    return facts

def factsum(divs, n):
    facts = defaultdict(lambda: 1)
    while divs[n]:
        div = divs[n]
        facts[div] = facts[div] * div + 1
        n //= divs[n]
    facts[n] = facts[n] * n + 1
    return reduce(mul, facts.values(), 1)
