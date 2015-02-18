import datetime, math

def sumdigits(s):
    sum = 0
    for ch in s: sum += int(ch)
    return sum

fact = 1

for i in range(1, 101):
    fact *= i

print(sumdigits(str(fact)))
