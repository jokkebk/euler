def prime(n): return n not in poulet and pow(2, n-1, n) == 1
poulet = {}
with open('poulet.txt', 'r') as f:
    for s in f:
        if int(s) > 1e5: break
        poulet[int(s)] = True
primes = [p for p in range(2,8500) if prime(p)]

nums = set()

for a in primes:
    if a*a > 5e7: break
    for b in primes:
        ab = a*a + b**3
        if ab > 5e7: break
        print(a,b)
        for c in primes:
            abc = ab + c**4
            if abc > 5e7: break
            nums.add(abc)

print(len(nums))
