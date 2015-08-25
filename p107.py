import heapq

S, e, ok, q = 0, [], set(), [(0,0)]

with open('p107.txt') as f:
    for l in f:
        e.append(list())
        for j,v in enumerate(l.split(',')):
            if v[0] != '-': e[-1].append((int(v),j))

while len(q):
    v,i = heapq.heappop(q)
    if i not in ok:
        S -= v*2
        ok.add(i)
        for v,j in e[i]:
            S += v
            heapq.heappush(q, (v,j))

print(S//2)
