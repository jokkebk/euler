# A(x)/x - A(x) = 1 + 3x + x*A(x) <=> A(x) = (3x^2+x) / (1-x-x^2)
# A(x) = n <=> x = (sqrt(5n^2+14n+1)-n-1)/(2n+6) (n=2 first rational solution)
# 5n2+14n+1 = m2 => n = (sqrt(196+20m2-20)-14)/10 = (sqrt(5m2+44)-7)/5
# Also, A(x) = (3x+1)*B(x) where B(x) is from problem 137
# Because 137 solutions are F7, F11, F15, ... fibonacci numbers... it's easy

def gen():
    p, q = 0, 1
    while True:
        yield (p,q)
        p, q = p+q, p+2*q

for p,q in gen():
    if p>100: break
    print(p,q)

exit(1)

sq = {i*i: i for i in range(1,1<<24)}
for i in range(1,1<<24):
    try:
       s = sq[5*i*i+14*i+1]
       print(i) #, s, (s-i-1) / (2*i+6))
    except: pass
