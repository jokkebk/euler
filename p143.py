from primes import getdivs, factor
from collections import defaultdict
from itertools import combinations

def gendivs(divs, n): # 3*n^2
    c = factor(divs, n)
    c = c+c
    c[3] += 1
    f = list(c.items())
    c, go, m = [0]*len(f), True, 1
    while go:
        yield m
        go = False
        for i,(fact,num) in enumerate(f):
            if c[i] < num:
                c[i] += 1
                m *= fact
                go = True
                break
            m //= fact**num
            c[i] = 0

N, P, ok, done = 120000, defaultdict(set), set(), set()
divs = getdivs(N//2) # For factor()

# Solve diophantine equation p^2+r^2+p*r=y^2 <=> (2r+p)^2-y^2=-3*p^2
for p in range(1, N//2):
    for u in gendivs(divs, p):
        v = -3*p*p//u
        if (u-v)&3 or u+v<4*p: continue
        r = (u+v-2*p)//4
        if r<N:
            P[p].add(r)
            ok.add((p,r))

for p in P:
    if len(P[p]) < 2: continue
    for q,r in combinations(sorted(P[p]), 2):
        if (q,r) in ok:
            if p+q+r <= N: done.add(p+q+r)

print(sum(done))
