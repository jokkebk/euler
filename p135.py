from itertools import count

diff = lambda a, d: -a*a + 2*a*d + 3*d*d

W = [0] * (10**6)
last = 0 # Terminate after enough zeroes
for a in count(1):
    for d in count(2*a//6+1): # First diff(a,d)>0
        v = diff(a,d)
        if v >= 10**6: break
        W[v] += 1
        last = a
    if last+2 < a: break

print(sum(1 for v in W if v==10))
