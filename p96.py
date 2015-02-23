from itertools import product as pr
from functools import reduce
from collections import Counter

make_const = lambda i,j,n: {(0,i,j), (1,i,n), (2,j,n), (3,i//3,j//3,n)}
apply_const = lambda consts, const: [c for c in consts if c.isdisjoint(const)]
find_const = lambda key, consts: [c for c in consts if key in c]

def solve(sol, cs):
    if len(cs) == 0: return sol if len(sol)==81 else None

    cnt = Counter()
    for c in cs: # Find best split
        for k in c: cnt[k] += 1

    for c in find_const(cnt.most_common()[-1][0], cs):
        s = solve(sol+[c], apply_const(cs, c))
        if s: return s

with open('p96.txt') as fin: sudoku = [line.strip() for line in fin]
consts = [make_const(i,j,n) for i,j,n in pr(range(9), range(9), range(1,10))]
total = 0

for start in range(1, len(sudoku), 10):
    initial = []
    for j,i in pr(range(9), range(9)):
        n = int(sudoku[start+j][i])
        if n: initial.append(make_const(i,j,n))

    s = {}
    for c in solve(initial, reduce(apply_const, initial, consts.copy())):
        parts = sorted(c)
        s[(parts[0][1], parts[0][2])] = parts[1][2]
    total += s[(0,0)]*100 + s[(1,0)]*10 + s[(2,0)]

print(total)
