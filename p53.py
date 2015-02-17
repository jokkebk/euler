from itertools import product
from math import factorial

def choose(n,r): return factorial(n) // factorial(r) // factorial(n-r)

print(sum(1 for n,r in product(range(101), range(101)) if n>r and choose(n,r) > 1e6))
