from operator import add, sub, mul, truediv
from itertools import combinations, permutations

def combine(a,b):
    for op in (add, sub, mul): yield op(a,b)
    if b: yield truediv(a,b)
    for op in (add, sub, mul): yield op(b,a)
    if a: yield truediv(b,a)

def gen(s):
    for v1 in combine(s[0], s[1]):
        for v2 in combine(v1, s[2]):
            for v3 in combine(v2, s[3]):
                if not v3 % 1: yield int(v3)
    for v1 in combine(s[0], s[1]):
        for v2 in combine(s[2], s[3]):
            for v3 in combine(v1, v2):
                if not v3 % 1: yield int(v3)

best = 0
bestV = (0,0,0,0)

for c in combinations(range(1,9), 4):
    nums = set()
    for s in permutations(c):
        for n in gen(s):
            if n > 0: nums.add(n)
    nums = list(nums) # convert to [1,2,3,...]
    if best < len(nums) and nums[best] == best+1:
        bestV = c
        while nums[best] == best+1: best += 1

print(best, bestV)
