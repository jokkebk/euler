import math
from collections import Counter

prime = [True] * 1000000

for i in range(2,int(math.sqrt(len(prime)))):
    if not prime[i]: continue
    for j in range(i*2, len(prime), i):
        prime[j] = False

p = [i for i,t in enumerate(prime) if t and i > 100000]
c = Counter()

def process(s, i = 0, r = "", ch = None):
    if i == len(s): c[r] += 1
    else:
        process(s, i+1, r + s[i], ch) # skip
        if ch == None or ch == s[i]: # add if possible
            process(s, i+1, r + 'x', s[i])

for i in p: process(str(i))

print(c.most_common(1))
