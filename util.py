# Babylonian square check
def square(i):
    if i == 1: return True
    x = i // 2
    seen = set([x])
    while x * x != i:
        x = (x + (i // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

# Newton method integer square root
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

# Fibonacci generator
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

# Greatest common divisor
def gcd(a,b):
    while a: a, b = b % a, a
    return b

# Generate pythagorean triples where c < N
def pythag(N, primitive=True):
    for n in range(1,N):
        if 2*n*n > N: break
        for m in range(n+1,int((N-n*n)**.5)+1, 2):
            if gcd(m,n)!=1: continue
            a, b, c = m*m-n*n, 2*m*n, m*m+n*n
            if a>b: a,b = b,a
            if primitive: yield (a,b,c)
            else:
                for k in range(1,N//c): yield (k*a,k*b,k*c)

# Adapted from http://rosettacode.org/wiki/Chinese_remainder_theorem#Python
def chinese_remainder(n, a):
    sum, prod = 0, 1
    for ni in n: prod *= ni
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0, x0, x1 = b, 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
if __name__ == '__main__':
    n = [100, 23] # Project Euler 134 example
    a = [19, 0]
    print(chinese_remainder(n, a))
