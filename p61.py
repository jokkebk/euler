import math, itertools, collections

def recurse(nums, done = 1):
    if done == 63 and nums[0]//100 == nums[-1]%100:
        print(sum(n for n in nums))
    else:
        for i in range(6):
            if done & (1<<i): continue
            for n in paths[(i, nums[-1]%100)]:
                recurse(nums + [n], done | (1<<i))

gen = [ lambda n: n*(n+1)//2,
        lambda n: n*n,
        lambda n: n*(3*n-1)//2,
        lambda n: n*(2*n-1),
        lambda n: n*(5*n-3)//2,
        lambda n: n*(3*n-2) ]

poly = []
paths = collections.defaultdict(set)

for g in gen:
    nums = [g(i) for i in range(1,200) if g(i) > 999 and g(i) < 10000]
    for n in nums:
        paths[(len(poly), n//100)].add(n)
    poly.append(nums)

for n in poly[0]: recurse([n])
