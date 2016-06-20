from primes import initpoulet, prime

initpoulet()

add = (1, 3, 7, 9, 13, 27)
S = 10

for n in range(11, 150000000):
    if n%100000==0: print(n, S)
    if all(prime(n*n+a) for a in add): S += n

print(S)
#print(list(prime(n*n+a) for a in add))
