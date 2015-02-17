import math, sys

for a in range(0, 1000):
    for b in range(0, 1000):
        c = int(math.sqrt(a*a + b*b))
        if c*c != a*a + b*b: continue
        if a+b+c == 1000: print(a*b*c)
