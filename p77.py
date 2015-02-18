prime = [True] * 101
for i in range(2,len(prime)):
    if not prime[i]: continue
    for j in range(i*2, len(prime), i):
        prime[j] = False

primes = [p for p,isp in enumerate(prime) if isp and p>1]
ways = {0: 1}

for p in primes:
    for start, w in ways.copy().items():
        for num in range(start+p, 101, p):
            ways[num] = ways.setdefault(num, 0) + w

print(min(i for i in ways if ways[i] > 5000))
