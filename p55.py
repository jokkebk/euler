def pal(s): return s == s[::-1] # palindrome

num = 0

for n in range(10000):
    lychrel = True
    for it in range(50):
        n += int(str(n)[::-1])
        if pal(str(n)):
            lychrel = False
            break
    if lychrel: num += 1

print(num)
