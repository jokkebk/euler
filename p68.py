from itertools import permutations

def gon(p):
    sum = 10 + p[4] + p[0]
    used = (1<<p[4])
    start = (10, 0)
    spokes = ["10%d%d" % (p[4], p[0])]
    for i in range(4):
        out = sum - p[i] - p[i+1]
        if out > 9 or out < 1: break
        used |= (1<<p[i]) + (1<<out)
        start = min(start, (out, i+1))
        spokes.append("%d%d%d" % (out, p[i], p[i+1]))
    if used == 1022:
        print("".join([spokes[(i+start[1])%5] for i in range(5)]))

for p in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 5): gon(p)
