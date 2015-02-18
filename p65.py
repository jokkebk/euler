import math

def brahmagupta(N, a, b, k):
    (best, M) = (False, 0)

    for m in range(1,2*abs(k)+1):
        if (a + b*m) % k: continue
        val = abs(m*m - N)
        if not best or val < best:
            (best, M) = (val, m)
        else:
            break

    return ((a*M+N*b)//abs(k), (a+b*M)//abs(k), (M*M-N)//k)

def chakravala(N):
    (a, b, k) = (1, 1, 1-N)
    while k != 1: (a, b, k) = brahmagupta(N, a, b, k)
    return a

squares = {n*n for n in range(2,40)}

print(max((chakravala(N), N) for N in range(2,1001) if N not in squares))
