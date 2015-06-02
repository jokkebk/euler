def pandigi(s): return "".join(sorted(s)) == "123456789"

(fn, fn1, n) = (1, 1, 2)

while True:
    (fn, fn1, n) = (fn+fn1, fn, n+1)
    if pandigi(str(fn)[-9:]) and pandigi(str(fn)[:9]):
        print(n)
        break
