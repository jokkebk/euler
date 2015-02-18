import math

def prime(n): return n not in poulet and pow(2, n-1, n) == 1

poulet = {}

with open('poulet.txt', 'r') as f:
    for s in f:
        poulet[int(s)] = True

(d, primes) = (3, 3)

while primes / (2*d - 1) > 0.1:
    d += 2
    primes += sum(1 for i in range(1,4) if prime(d*d - i*(d-1)))

print(d)
