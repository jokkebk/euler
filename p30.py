def sump(n, p): return sum(int(d)**p for d in str(n))
print(sum(n for n in range(2,400000) if n == sump(n,5)))
