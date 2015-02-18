import math, sys

num = int(sys.argv[1])

for i in range(2, int(math.sqrt(num))):
    while num % i == 0:
        print(i)
        num /= i
