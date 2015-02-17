def ok(x,n):
    digits = "".join(sorted(str(x)))
    for i in range(n):
        if "".join(sorted(str(x*i+x))) != digits: return False
    return True

x = 1
while not ok(x, 6): x += 1
print(x)
