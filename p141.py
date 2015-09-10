
N = 10**12
sq = {i*i for i in range(10**6)}
S = set()
for m in range(2,10000):
    for n in range(1,m):
        M = m**3 * n
        if M > N: break
        for a in range(1, N):
            num = a**2*M + a*n*n
            if num >= N: break
            if num in sq:
                S.add(num)
print(sum(S))
