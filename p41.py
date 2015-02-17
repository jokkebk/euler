import math

prime = [True] * 10000000
sum = 0

for i in range(2,int(math.sqrt(len(prime)))):
    if not prime[i]: continue
    for j in range(i*2, len(prime), i):
        prime[j] = False

def pandigi(n): return "".join(sorted(str(n))) == "123456789"[:len(str(n))]

print(max(n for n in range(10000000) if prime[n] and pandigi(n)))
