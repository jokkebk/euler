N = 5
ways = [1] * N

for n in range(2,N):
    for term in range(n, N, n):
        print("%d: %d" % (term, ways[N-term]))
