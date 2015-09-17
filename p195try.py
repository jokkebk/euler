from primes import getdivs, factor
from collections import defaultdict
from itertools import combinations
from util import gcd

def rad(a, b, c):
    s = (a+b+c)/2
    return ((s-a)*(s-b)*(s-c)/s)**.5

R = 100
I = 0
ok = {}

for u in range(1,500):
    for v in range(1,u//2):
        if gcd(u,v) > 1: continue
        x, y, z = u*u-v*v, 2*u*v-v*v, u*u-u*v+v*v
        if x and y and z:
            g = gcd(x,y)
            x,y,z = x//g,y//g,z//g
            r = rad(x,y,z)
            if x>0 and y>0 and z>0 and x!=y and r < R:
                I += int(R/r)
                ok[(y,z)] = int(R/r)

for u in range(1,500):
    for v in range(1,u//2):
        if gcd(u,v) > 1: continue
        x, y, z = u*u-v*v, 2*u*v-u*u, u*u-u*v+v*v
        if x and y and z:
            g = gcd(x,y)
            x,y,z = x//g,y//g,z//g
            r = rad(x,y,z)
            if x>0 and y>0 and z>0 and x!=y and r < R:
                I += int(R/r)
                ok[(y,z)] = int(R/r)

print(sum(ok[k] for k in ok))
