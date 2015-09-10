# S(x)/x - S(x) = 1 + x*S(x) <=> S(x) = x / (1-x-x**2)
# S(x) = n <=> n*x^2 + (n+1)*x - n = 0 => x = (-n-1 + sqrt((n+1)^2+4n^2))/2n
# x is rational when (2n)^2 + (n+1)^2 = m^2 is square
# So we are looking for pythagorean triples (2n, n+1, m)
# Generating them with Euclid's formula gives (2mn, m^2-n^2, m^2+n^2)
# so we are looking for composite numbers where m^2-n^2 = mn+1 so
# m = (n+sqrt(5n^2+4))/2 which is integer when 5n^2+4 is square
# By the way, all n satisfying this are Fibonacci numbers 

sq = {}
for i in range(1,1<<22):
    s = i*i
    sq[s] = i
    if s%5==4 and (s-4)//5 in sq:
        n = sq[(s-4)//5]
        print(n*(n+i)//2)
