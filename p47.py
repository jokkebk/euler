import math

prime = [True] * 10000

for i in range(2,int(math.sqrt(len(prime)))):
    if not prime[i]: continue
    for j in range(i*2, len(prime), i):
        prime[j] = False

def pfact(n):
    facts = []

    for i in range(2, int(math.sqrt(n))):
        if n % i or not prime[i]: continue
        p = 0
        while n % i == 0:
            n //= i
            p += 1
        facts.append((i, p))

    if n > 1: facts.append((n, 1))
    return facts

seq = 0
for i in range(1000000):
    seq += 1
    if len(pfact(i)) != 4: seq = 0
    if seq == 4:
        print(i-3)
        break
