from math import sqrt

N = 1000001
div = [1] * N

for i in range(2, int(sqrt(N))):
    if div[i] != 1: continue
    for j in range(i*2, N, i): div[j] = i

def factor(n):
    if div[n] == 1: return set([n])
    facts = factor(n // div[n])
    facts.add(div[n])
    return facts

def divisors(N, facts, mul=1, i=0, sign = 1):
    if i == len(facts):
        if mul < N: yield sign*(N//mul-1)
    else:
        yield from divisors(N, facts, mul, i+1, sign)
        yield from divisors(N, facts, facts[i] * mul, i+1, -sign)

def phi(n):
    return sum(divisors(n, list(factor(n))))

print(max((n/phi(n), n) for n in range(2,1000001)))
