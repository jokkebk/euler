from itertools import product

def digisum(n): return sum(int(d) for d in str(n))

print(max(digisum(a**b) for a,b in product(range(100), range(100))))
