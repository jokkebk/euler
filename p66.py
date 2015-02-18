import math

def square(n): return n == int(math.sqrt(n))**2

for D in range(2,1001):
    if square(D): continue
    solution = False
    for x in range(2,10000000):
        n = x*x - 1
        if n % D or not square(n//D): continue
        print("%d: %d" % (D, x))
        solution = True
        break
    if not solution: print("No solution for %d!" % D)
