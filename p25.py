f = (1, 1)
i = 2

while len(str(f[1])) < 1000:
    f = (f[1], f[0] + f[1])
    i += 1

print("%d. %d" % (i, f[1]))
