from math import factorial

def C(n,r): return factorial(n) // factorial(r) // factorial(n-r)

def ways(n, b):
    f = n - b*3 - (b-1)
    for i in range(f+1):
        yield(C(i+b-1, i) * C(f-i+b, b))

N = 50
print(1+sum(sum(ways(N, i)) for i in range(1,(N+1)//3+1)))
