prime = [True] * 1000000

def plen(a, b):
    n = 2
    while prime[n*n + a*n + b]: n += 1
    return n

for i in range(2, 1000):
    for j in range(i*2, 1000000, i):
        prime[j] = False

best = (0, 1)

for b in range(-999, 1000):
    if not prime[b]: continue
    for a in range(-999, 1000):
        if not prime[1+a+b]: continue
        best = max(best, (plen(a, b), a*b))

print(best)
