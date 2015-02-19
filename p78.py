cache = {0: 1}

def p(n):
    if n < 0: return 0
    if n in cache: return cache[n]

    val = 0

    for k in range(1, 100000):
        i = n - k*(3*k-1)//2
        j = n - k*(3*k+1)//2
        if i < 0 and j < 0: break
        val += p(i)+p(j) if k&1 else -p(i)-p(j)

    cache[n] = val
    return val

for n in range(100000):
    if p(n) % 1000000: continue
    print("p(%d) = %d" % (n, p(n)))
    break
