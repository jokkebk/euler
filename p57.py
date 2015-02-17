n = 0
(a, b) = (1, 2)

for i in range(1000):
    if len(str(a+b)) > len(str(b)): n += 1
    (a, b) = (b, 2*b+a)

print(n)
