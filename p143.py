from util import farey
from collections import defaultdict
from itertools import combinations

N = 12000
sq = {i*i: i for i in range(1,N*2)}
P = defaultdict(list)
ok = set()
a = lambda p,q: p*p+q*q+p*q

for p,q in farey(N):
    if a(p,q) not in sq: continue
    for k in range(1, N//q):
        P[k*p].append(k*q)
        P[k*q].append(k*p)
        ok.add((k*p,k*q))

for p in P:
    if len(P[p]) < 2: continue
    for q,r in combinations(sorted(P[p]), 2):
        if (q,r) in ok:
            print(sq[a(p,q)], sq[a(q,r)], sq[a(r,p)], p,q,r, p+q+r)
