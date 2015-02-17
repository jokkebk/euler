import math, sys

best = (1, 1)
for n in range(2,1000000):
    val = n
    num = 1
    #print("%d:" % n)
    while n > 1:
        #print(n)
        n = 3*n + 1 if n%2 else n//2
        num += 1

    best = max(best, (num, val))

print(best)
