import timeit

start = timeit.default_timer()

rev = lambda n: int(str(n)[::-1])
def isodd(n):
    while n:
        if not n&1: return False
        n //= 10
    return True

isok = lambda n: isodd(n + rev(n))

semi = [n for n in range(10,100) if n%10]
ok = 20
div = 10

for I in range(3):
    semi2, div2 = [], div*10

    for n in semi:
        hi, lo = n//div, n%div
        for i in range(10):
            if isok(hi*div*10 + i*div + lo): ok += 1
        for i in range(100):
            n = hi*div*100 + i*div + lo
            r = rev(n)
            bot = n%div2 + r%div2
            top = n//div2 + r//div2
            if isodd(bot) and (isodd(top) or isodd(top+1)):
                semi2.append(n)
                if isodd(n+r): ok += 1

    semi, div = semi2, div2

print(ok)

stop = timeit.default_timer()

print(stop - start )
