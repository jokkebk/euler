from math import factorial

def C(n,r): return factorial(n) // factorial(r) // factorial(n-r)

def ways(M, N):
    for b in range(1,(N+1)//M+1):
        f = N - b*M - (b-1)
        for i in range(f+1):
            yield(C(i+b-1, i) * C(f-i+b, b))

print(next(m for m in range(51, 200) if sum(ways(50, m)) > 1e6))
