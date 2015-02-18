import math

def iterate(num, sub, div):
    newdiv = (num - sub*sub) // div
    out = int((math.sqrt(num) + sub)//newdiv)
    newsub = out*newdiv - sub
    return (out, newsub, newdiv)

odd = 0

for num in range(2,10001):
    if int(math.sqrt(num))**2 == num: continue
    (sub, div, period) = (int(math.sqrt(num)), 1, 0)
    seen = {}
    while (sub,div) not in seen:
        seen[(sub,div)] = True
        (out, sub, div) = iterate(num, sub, div)
        period += 1
    if period & 1: odd += 1

print(odd)
