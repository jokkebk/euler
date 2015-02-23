from primes import getdivs, factsum

N = 10**6
divs = getdivs(N)
visited = set()
best = (0,0)

for n in range(2, N+1):
    (i, p, chain) = (n, {}, [])
    while i > 1 and i <= N and i not in visited:
        visited.add(i)
        p[i] = len(chain)
        chain.append(i)
        i = factsum(divs, i) - i # next
        if i in p: best = max(best, (len(chain) - p[i], min(chain[p[i]:])))

print(best)
