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

sum = 0

for a in range(2, 10000):
    b = d(a)
    if d(b) == a and a != b:
        print("%d and %d" % (a,b))
        sum += a

print(sum)
