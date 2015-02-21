from math import sqrt

def pythag(M): # adapted pythagorean generator
    for n in range(1, int(sqrt(M))+1):
        m = sqrt(3*n*n+1)
        if m % 1: continue # integer solution not possible
        m = int(m)
        yield (m*m-n*n, 2*m*n, m*m+n*n)
        m = 2*n + m # this is always a pair, 2*n - m is not
        yield (2*m*n, m*m-n*n, m*m+n*n)

print(sum(2*(a+c) for a,b,c in pythag(5e8) if a+b+c < 1e9))
