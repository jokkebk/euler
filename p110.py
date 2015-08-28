from itertools import product
from functools import reduce
from operator import mul

def gen():
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in product(range(1,4), repeat=4):
        a = list(a) + [1,1,1,1,1,1,1,1] # Best a is [3, 3, 2, 2]
        n = reduce(mul, [p[i]**v for i,v in enumerate(a)])
        if reduce(mul, [2*v+1 for v in a])//2+1 > 4*10**6: yield n

print(min(gen()))
