from math import factorial

def pal(s): return s == s[::-1] # palindrome

print(sum(i for i in range(1000000) if pal(str(i)) and pal("{0:b}".format(i))))
