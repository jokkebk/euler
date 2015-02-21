from itertools import combinations, product

cubes = list(combinations(range(10), 6))

def isok(a,b):
    a = tuple(6 if v==9 else v for v in a)
    b = tuple(6 if v==9 else v for v in b)
    for n in range(1,10):
        (x, y) = (n*n//10, n*n%10)
        if y == 9: y = 6
        if not ((x in a and y in b) or (x in b and y in a)): return False
    return True

print(sum(1 for a, b in product(cubes, cubes) if a<=b and isok(a, b)))
