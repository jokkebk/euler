from itertools import product
p = list(product(range(1, 21), range(1, 4))) + [(25, 1), (25, 2), (0, 0)]
print(sum(1 for c in product(p, p, p) \
        if sum(v*m for v, m in c) < 100 and c[2][1] == 2 and c[0] <= c[1]))
