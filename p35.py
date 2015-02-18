from math import factorial

prime = [True] * 1000000

for i in range(2, 1001):
    for j in range(2*i, len(prime), i):
        prime[j] = False

def rot(n):
    s = str(n)
    return int(s[-1] + s[0:-1])

for i,t in enumerate(prime):
    if str(i).find('0') != -1:
        prime[i] = False
    elif not t:
        n = rot(i)
        while n != i:
            prime[n] = False
            n = rot(n)

print(sum(1 for i in range(2,1000000) if prime[i]))
