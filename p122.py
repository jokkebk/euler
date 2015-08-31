from itertools import product
from collections import defaultdict

best = defaultdict(lambda: 11) # 191=11 not found at d=10

def rec(s, i, d=1):
    for j in list(s):
        if (i+j in s) or i+j > 200 or d > 10: continue
        s.add(i+j)
        best[i+j] = min(best[i+j], d)
        rec(s, i+j, d+1)
        s.remove(i+j)

rec(set([1]), 1)
print(sum(best[i] for i in range(2,201)))
