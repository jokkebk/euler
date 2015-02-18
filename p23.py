import datetime, math

def factor(n):
    facts = []
    for i in range(2,int(math.sqrt(n))+1):
        if n%i: continue
        p = 0
        while n%i == 0:
            p += 1
            n //= i
        facts.append((i, p))
    if n > 1: facts.append((n, 1))
    return facts

def dsum(facts, i=0):
    if i >= len(facts): return 1
    (n, p) = facts[i]
    sum = 0
    prod = 1

    for loop in range(p+1):
        sum += prod * dsum(facts, i+1)
        prod *= n

    return sum

def d(num): return dsum(factor(num)) - num

abus = []

for i in range(12, 28125):
    if d(i) > i: abus.append(i)

summable = {}

for idx, i in enumerate(abus):
    for j in abus[idx:]:
            summable[i+j] = True

sum = 0

for i in range(28124):
    if i not in summable:
        sum += i

print(sum)
