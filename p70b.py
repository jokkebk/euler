from math import sqrt

def norm(n): return "".join(sorted(ch for ch in str(n)))

N = 10000001
facts = [set() for n in range(N)]

for i in range(2, N):
    if len(facts[i]): continue
    for j in range(i*2, N, i): facts[j].add(i)

def divisors(N, facts, mul=1, i=0, sign = 1):
    if i == len(facts):
        if mul < N: yield sign*(N//mul-1)
    else:
        yield from divisors(N, facts, mul, i+1, sign)
        yield from divisors(N, facts, facts[i] * mul, i+1, -sign)

def phi(n): return sum(divisors(n, list(facts[n])))

print(min((n/phi(n), n) for n in range(2,10000001) if norm(n) == norm(phi(n))))
