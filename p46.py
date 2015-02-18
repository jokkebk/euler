import math

prime = [True] * 10000

for i in range(2,int(math.sqrt(len(prime)))):
    if not prime[i]: continue
    for j in range(i*2, len(prime), i):
        prime[j] = False

def gold(n):
    for i in range(1,1000):
        p = n - 2*i*i
        if p < 2: return False
        if prime[p]: return True
    return False

print(min(i for i,t in enumerate(prime) if i%2 and not t and not gold(i)))
