# In ((a+1)^n + (a-1)^n) mod a^2 only last two terms (a^1, a^2) matter,
# and for even n the terms cancel each other out. For n=2k+1, result is
# C(n, n-1) * a * (1 + (-1)^(n-1)) = 2na = (4k+2)a (mod a^2)
def f(a):
    for k in range(a): yield (4*k+2)*a % (a*a)

print(sum(max(f(i)) for i in range(3,1001)))
