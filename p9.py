import math, sys

for a in range(1, 500):
    for b in range(a+1, 500):
        c = int(math.sqrt(a*a + b*b))
        if c*c == a*a + b*b and a+b+c == 1000:
            print(a*b*c)
