from collections import defaultdict
from primes import gcd

N = 120000
rad = [1] * (N+1)

for i in range(2,len(rad)):
    if rad[i] > 1: continue
    for j in range(i,len(rad),i): rad[j] *= i

R = defaultdict(list)
for i,r in enumerate(rad[1:]): R[r].append(i+1)
rads = sorted(R)

S = 0
for rb in rads:
    for b in R[rb]:
        for ra in rads:
            if ra*rb*2 > N: break
            for a in R[ra]:
                if a >= b or a + b >= N: break
                if ra*rb*rad[a+b] >= a+b: continue
                if gcd(a,b) == 1: S += a+b
print(S)
