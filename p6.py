import math, sys

sum = 0
sum2 = 0

for i in range(1,101):
    sum += i
    sum2 += i*i

print(sum*sum - sum2)
