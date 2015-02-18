N = 1000001
facts = [set() for n in range(N)]

for i in range(2, N):
    if len(facts[i]): continue
    for j in range(i, N, i): facts[j].add(i)

def phi(n):
    for p in facts[n]:
        n = n * (p-1) // p
    return n

print(sum(phi(n) for n in range(2,1000001)))
