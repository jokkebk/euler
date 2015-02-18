from itertools import product, permutations

lookup = {"".join(item): True for item in permutations("123456789")}

def pandigi(a,b): return "%d%d%d" % (a,b,a*b) in lookup

nums = {}
for a in range(10000):
    for b in range(a+1, 10000):
        if pandigi(a,b): nums[a*b] = True

print(sum(ab for ab in nums))
