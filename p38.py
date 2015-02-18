from itertools import product, permutations

lookup = {"".join(item): True for item in permutations("123456789")}

def pandigi(a,n): return "".join([str(a*i) for i in range(1,n+1)])

best = 0

for a in range(1,10000):
    for n in range(2,6):
        p = pandigi(a,n)
        if p in lookup:
            best = max(best, int(p))

print(best)
