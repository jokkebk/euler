from collections import defaultdict

N = 120000
rad, div = [1] * (N+1), [1] * (N+1)

for i in range(2,len(rad)):
    if rad[i] > 1: continue
    for j in range(i,len(rad),i):
        rad[j] *= i
        div[j] = i

def facts(n):
    d = div[n]
    f = set([d])
    return f if d==n else f.union(facts(n//d))

R = defaultdict(list)
for i,r in enumerate(rad[1:]): R[r].append(i+1)
rads = sorted(R)

S = 0
for rb in rads:
    if rb*2 > N: break
    for b in R[rb]:
        for ra in rads:
            if ra*rb*2 > N: break
            for a in R[ra]:
                if a >= b or a + b >= N: break
                if rad[a]*rad[b]*rad[a+b] >= a+b: continue
                if not facts(a).intersection(facts(b)): S += a+b

print(S)
