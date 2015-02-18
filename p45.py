from itertools import product

T = [n*(n+1)//2 for n in range(100000)]
P = [n*(3*n-1)//2 for n in range(100000)]
H = [n*(2*n-1) for n in range(100000)]

isP = {n: True for n in P}
isH = {n: True for n in H}

print(max(n for n in T if n in isP and n in isH))
