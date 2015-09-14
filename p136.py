from collections import Counter
from itertools import count
import sys

diff = lambda a, d: -a*a + 2*a*d + 3*d*d

N = int(sys.argv[1])
W, I = Counter(), 0
last = 0 # Terminate after enough zeroes
for a in count(1):
    for d in count(2*a//6+1): # First diff(a,d)>0
        v = diff(a,d)
        if v >= N: break
        W[v] += 1
        I += 1
        last = a
    if last+2 < a: break

c = Counter()
for i in W: c[W[i]] += 1
for k in sorted(c):
    print(k, c[k])
print(sum(1 for i in W if W[i]==1))
