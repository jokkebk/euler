from collections import Counter, defaultdict
from operator import mul
from functools import reduce

def prime(n): return n==2 or (n not in prime.poulet and pow(2, n-1, n) == 1)

def initpoulet():
    prime.poulet = {}
    with open('poulet.txt', 'r') as f:
        for s in f: prime.poulet[int(s)] = True

def getprimesieve(N):
    primes = [True] * (N+1)
    for i in range(2,int(N**.5)):
        if not primes[i]: continue
        for j in range(i*2, N+1, i): primes[j] = True
    return primes

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
