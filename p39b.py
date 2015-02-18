import math

num = [0] * 1001

for a in range(1,500):
    for b in range(a+1, 500):
        c = int(math.sqrt(a*a + b*b))
        if a*a + b*b == c*c and a+b+c <= 1000:
            num[a+b+c] += 1

print(max((v,i) for i,v in enumerate(num)))
