from functools import lru_cache

@lru_cache(maxsize=10**7)
def is89(n):
    if n == 89: return True
    if n == 1: return False
    return is89(sum(int(d)**2 for d in str(n)))

print(sum(1 for n in range(1,10**7+1) if is89(n)))
