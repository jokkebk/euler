from itertools import product, combinations

def prime(n): return n not in poulet and pow(2, n-1, n) == 1
poulet = {}
with open('poulet.txt', 'r') as f:
    for s in f: poulet[int(s)] = True

def gen(n, m, d):
    for ds in combinations(range(n), m):
        dss = set(ds)
        for ns in product(range(10), repeat=m):
            v = d * sum(10**i for i in range(n) if i not in dss)
            v += sum(ns[i] * 10**ds[i] for i in range(m))
            if v > 10**(n-1) and prime(v): yield v

n, S = 10, 0

for d in range(10):
    s = S
    for m in range(n):
        S += sum(gen(n, m, d))
        if S > s: break

print(S)
