from math import factorial

def fsum(n): return sum(factorial(int(d)) for d in str(n))

print(sum(n for n in range(3, 45000) if n == fsum(n)))
