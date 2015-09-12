from collections import defaultdict
from itertools import combinations
from util import pythag, square

P = defaultdict(list)

for i,j,k in pythag(999, False):
    P[i].append(j)
    P[j].append(i)

def gen():
    for r in P:
        if len(P[r]) < 2: continue
        for n,m in combinations(sorted(P[r]), 2):
            if not (n+m)&1 and square(n*n+m*m+r*r):
                yield (m*m+n*n+2*r*r)//2, \
                    (m*m+n*n)//2, (m*m-n*n)//2

print(sum(min(gen(), key=sum)))
