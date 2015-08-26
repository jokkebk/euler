from collections import defaultdict

def dir(a,b): return 0 if a==b else (1 if a<b else 2)

c = defaultdict(int)
for i in range(1,10): c[(i,0)] = 1

N = 9
for digits in range(99):
    c2 = defaultdict(int)
    for i,d in c:
        for j in range(10):
            t = d | dir(i,j)
            c2[(j,t)] += c[(i,d)]
    c = c2
    N += sum(c[k] for k in c if k[1] != 3)

print(N)
