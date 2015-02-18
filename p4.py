import math, sys

def palindrome(s):
    for i in range(len(s)):
        if s[i] != s[-i-1]: return False
    return True

big = 0

for i in range(100,1000):
    for j in range(100,1000):
        if(palindrome(str(i*j))):
            big = max(big, i*j)
print(big)
