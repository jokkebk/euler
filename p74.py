from math import factorial

nx = lambda n: sum(factorial(int(c)) for c in str(n))

def loop(n, seen, d=1):
    seen.add(n)
    n2 = nx(n)
    if n2 in seen: return d
    return loop(n2, seen, d+1)

norm = lambda n: "".join(c for c in str(n))
cache = {}
c = 0

for n in range(10**6):
    l = cache.setdefault(norm(n), 0)
    if not l:
        l = loop(n, set())
        cache[norm(n)] = l
        if l >= 60: c += 1

print(c)
