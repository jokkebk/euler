ds = lambda n: sum(int(d) for d in str(n))
a = {b**p for b in range(2,99) for p in range(2,9) if ds(b**p)==b}
print(sorted(a)[29])
