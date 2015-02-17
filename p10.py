import math, sys

prime = [True] * 2000000
sum = 0

for i in range(2,len(prime)):
    if not prime[i]: continue
    sum += i
    for j in range(i*2, len(prime), i):
        prime[j] = False

print(sum)
