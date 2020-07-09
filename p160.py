def fivemul(x, y):
    p = x * y
    while p % 10 == 0: p //= 10
    return p % 100000000

p = 1
N = 2000

def red(x):
    while x % 5 == 0: x //= 5
    while x % 2 == 0: x //= 2
    return x

for i in range(1,N+1):
    p *= red(i)
    #p = fivemul(p, i)
print(p)# % 10000000)
