import math, sys

prime = [True] * 1000000
num = 0

print(len(prime))

for i in range(2,len(prime)):
    if not prime[i]: continue
    num += 1
    if num == 10001:
        break
    print("%d. %d" % (num, i))
    for j in range(i*2, len(prime), i):
        prime[j] = False
