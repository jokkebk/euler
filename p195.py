from primes import getdivs, factor
from collections import defaultdict
from itertools import combinations
from util import gcd

def gendivs(divs, n): # 3*n^2
    c = factor(divs, n)
    c = c+c
    c[3] += 1
    f = list(c.items())
    c, go, m = [0]*len(f), True, 1
    while go:
        yield m
        go = False
        for i,(fact,num) in enumerate(f):
            if c[i] < num:
                c[i] += 1
                m *= fact
                go = True
                break
            m //= fact**num
            c[i] = 0

def rad(a, b, c, R):
    s = (a+b+c)/2
    return ((s-a)*(s-b)*(s-c)/s) <= R*R

R = 1053779 
divs = getdivs(4*R) # For factor()
I, J, K = 0, 0, 0

# Solve diophantine equation b^2+c^2-b*c=a^2 <=> (2b-c)^2-a^2=-3*c^2
for c in range(1, int(6*R/3**.5)):
    for u in gendivs(divs, c):
        v = -3*c*c//u
        if (u-v)&3: continue
        x, a = (u+v)//2, (u-v)//4
        if (x+c)&1: continue
        b = (x+c)//2
        if a<b and rad(a,b,c,R):
            I += 1
            if I % 100000 == 0: print(I)
print(I)
