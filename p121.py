from collections import defaultdict

P = {0: 1}

for i in range(1,16):
    P2 = defaultdict(int)
    for pts,p in P.items():
        P2[pts] += p*i/(i+1)
        P2[pts+1] += p*1/(i+1)
    P = P2

print(int(1/sum(P[i] for i in range(8,16))))
