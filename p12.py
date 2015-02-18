import math, sys

def fact(n):
    facts = []

    for i in range(2, int(math.sqrt(n))):
        if n % i: continue
        p = 0
        while n % i == 0:
            n //= i
            p += 1
        facts.append((i, p))

    if n > 1: facts.append((n, 1))
    return facts

def ways(facts):
    prod = 1
    for (n, p) in facts: prod *= p + 1
    return prod

for i in range(1, 1000000):
    tri = i * (i+1) / 2
    w = ways(fact(tri))
    if w > 500: print("%d: %d" % (tri, w))
