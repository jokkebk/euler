from functools import lru_cache

@lru_cache(maxsize=None)
def dir(n):
    a, b = n//10, n%10
    if n<100: return 0 if a==b else (1 if a<b else 2)
    return dir(a) | dir((a%10)*10 + b)

b = 0
for i in range(101, 2**21):
    if dir(i)==3: b+=1
    if 100*b == 99*i:
        print(i)
        break
