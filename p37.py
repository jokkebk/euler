from math import factorial

prime = [True] * 1000000

for i in range(2, 1001):
    for j in range(2*i, len(prime), i):
        prime[j] = False

prime[1] = False

nums = []

for i in range(10, 1000000):
    if not prime[i]: continue

    s = str(i)
    t = True

    for pos in range(1, len(s)):
        left = int(s[pos:])
        right = int(s[:-pos])
        if not prime[left] or not prime[right]:
            t = False

    if t: nums.append(i)

print(sum(nums))
