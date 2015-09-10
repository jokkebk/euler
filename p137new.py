# New solution. A(x) = x/(1-x-x*2), if A(p/q) = n we get
# 1/n = q/p - 1 - p/q <=> (n+1)/n = (q*q-p*p)/pq and because gcd(p,q)=1,
# n = pq and pq+1=q*q-p*p <=> p^2+pq-q^2=-1
# Then we just use http://www.numbertheory.org/php/binarygen.php to get sols

def gen():
    F, G = 3, 1
    while True:
        yield ((-F+3*G)//2, (F-G)//2)
        F, G = (F*3+G*5)//2, (F+G*3)//2

print(next(p*q for i,(p,q) in enumerate(gen()) if i==15))
