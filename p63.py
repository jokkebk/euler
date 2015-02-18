num = 0

for base in range(1,10):
    for exp in range(1,1000):
        s = str(base**exp)
        if len(s) == exp:
            print("%2d ^ %2d = %s" % (base, exp, s))
            num += 1

print(num)
