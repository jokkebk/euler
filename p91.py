from itertools import combinations, product

coords = list(product(range(51), range(51)))[1:] # omit (0,0)

def isok(p,q):
    sides = ((p[0]-q[0])**2+(p[1]-q[1])**2, p[0]**2+p[1]**2, q[0]**2+q[1]**2)
    return 2*max(sides) == sum(sides)

print(sum(1 for a, b in product(coords, coords) if a<b and isok(a, b)))
