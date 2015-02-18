import math
from itertools import product

prime = [True] * 1000000

for i in range(2,int(math.sqrt(len(prime)))):
    if not prime[i]: continue
    for j in range(i*2, len(prime), i):
        prime[j] = False

prime[0] = prime[1] = False

p = [i for i,t in enumerate(prime) if t]

def roll(n):
    s = sum(p[:n])
    if s < len(prime) and prime[s]: yield s
    for i in range(n,len(p)):
        s += p[i] - p[i-n]
        if s < len(prime) and prime[s]: yield s

for i in range(530,590): print("%d: %s" % (i, str([n for n in roll(i)])))
