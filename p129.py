def A(n):
    m = 1
    for i in range(2,n):
        m = (10*m+1) % n
        if not m: return i
    return -1

print(next(n for n in range(10**6+1, 10**7, 2) if A(n)>1e6))
