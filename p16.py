import math, sys

def sumdigits(s):
    sum = 0
    for ch in s: sum += int(ch)
    return sum

print(sumdigits(str(2**1000)))
