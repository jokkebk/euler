# A(x)/x - A(x) = 1 + 3x + x*A(x) <=> A(x) = (3x^2+x) / (1-x-x^2)
# A(x) = n <=> x = (sqrt(5n^2+14n+1)-n-1)/(2n+6) (n=2 first rational solution)
# With x=5n+7 we get x^2-44=y^2, http://www.numbertheory.org/php/binarygen.php
from itertools import islice

def gen():
    F, G = -9, -4
    C = [((-13, 25), (5, -13)),
            ((13, 25), (5, 13)),
            ((7, 5), (1, 7)),
            ((-7, 5), (1, -7)),
            ((8, 10), (2, 8)),
            ((-8, 10), (2, -8))]
    while True:
        for s in (-1,1):
            for (a,b), (c,d) in C:
                yield s*(a*F+b*G), s*(c*F+d*G)
        F, G = 9*F+20*G, 4*F+9*G

N = sorted(islice(((i-7)//5 for i,j in gen() if i>7 and i%5==2), 50))
print(sum(N[:30]))
