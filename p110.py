import itertools
from functools import reduce
from operator import mul

def gen():
    p, q = [2, 3, 5, 7], 11*13*17*19*23*29*31*37 
    for a in itertools.product(range(5), repeat=4):
        if 3**8 * reduce(mul, [2*v+1 for v in a])//2+1 > 4*10**6:
            yield q * reduce(mul, [p[i]**v for i,v in enumerate(a)])

print(min(gen()))
