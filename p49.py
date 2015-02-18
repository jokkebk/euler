import math
from itertools import product

prime = [True] * 20000

for i in range(2,int(math.sqrt(len(prime)))):
    if not prime[i]: continue
    for j in range(i*2, len(prime), i):
        prime[j] = False

p = [i for i in range(1000,9999) if prime[i]]

def eq(a,b): return "".join(sorted(str(a))) == "".join(sorted(str(b)))

for a,b in product(p,p):
    c = 2*b-a
    if a < b and prime[c] and eq(a,b) and eq(a,c):
        print((a,b,c))

