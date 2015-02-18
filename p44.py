from itertools import product

p = [n*(3*n-1)//2 for n in range(1,2500)]
isp = {n: True for n in p}

print(min(abs(Pj-Pk) for Pj, Pk in product(p, p)
    if abs(Pj-Pk) in isp and (Pj+Pk) in isp))
