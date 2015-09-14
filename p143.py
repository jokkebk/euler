from util import farey, EEA
from primes import getdivs, factor
from collections import defaultdict
from itertools import combinations
from functools import reduce
from operator import mul

# Linear Diophantine equation Dx+Ey+F=0 solver
def dsolve(D,E,F):
    g,u,v = EEA(D,E)
    if F%g: return None
    d,e,f = D//g, E//g, F//g
    # x=a+b*t, y=c+d*t
    if g<0:
        return f*u, e, f*v, -d
    else:
        return -f*u, e, -f*v, -d

def gendivs(divs, n): # 3*n^2
    c = factor(divs, n)
    c = c+c
    c[3] += 1
    f = list(c.items())
    c = [0]*len(f)
    end = False
    while not end:
        yield reduce(mul, (f[i][0]**p for i,p in enumerate(c)))
        end = True
        for i,(fact,num) in enumerate(f):
            if c[i] < num:
                c[i] += 1
                end = False
                break
            c[i] = 0

N = 120000
divs = getdivs(3*N) # For factor()
sq = {i*i: i for i in range(1,N*4)}
P = defaultdict(set)
ok = set()
done = set()
a = lambda p,q: p*p+q*q+p*q

for v in [False]:
    if v:
        for p,q in farey(N):
            if a(p,q) not in sq: continue
            for k in range(1, N//q+1):
                P[k*p].add(k*q) # values > key
                ok.add((k*p,k*q))
    else:
        for p in range(1, N):
            for u in gendivs(divs, p):
                v = -3*p*p//u
                if (u+v)&1 or (u-v)&3: continue
                x, y = (u+v)//2, (u-v)//4
                if (x-p)&1: continue
                x = (x-p)//2
                if x<0: x, y = -x, -y
                if y>0 and p<x and x<N:
                    P[p].add(x)
                    ok.add((p,x))
                    #print(x,y, a(p,x) in sq, sq[a(p,x)])

    for p in P:
        if len(P[p]) < 2: continue
        #print("%d: %s, "%(p, ', '.join(str(v) for v in reversed(sorted(P[p])))))
        for q,r in combinations(sorted(P[p]), 2):
            if (q,r) in ok:
                #print(p,q,r)
                if p+q+r <= N: done.add(p+q+r)
                #print(sq[a(p,q)], sq[a(q,r)], sq[a(r,p)], p,q,r, p+q+r)
    print(sum(done))
