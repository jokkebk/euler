from primes import pythag

M = 10**8
print(sum(M//(a+b+c) for a,b,c in pythag(M//2) if a+b+c<M and c%(b-a)==0))
