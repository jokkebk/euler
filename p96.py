from itertools import product as pr
from collections import Counter

with open('p96.txt') as fin: lines = [line.strip() for line in fin]

def make_const(i,j,n): # create constraint row for number n at i,j in sudoku
    return {(0,i,j), (1,i,n), (2,j,n), (3,i//3,j//3,n)}

# Return a subset of constraints when const is applied
def apply_const(const, consts):
    return [c for c in consts if c.isdisjoint(const)]

def find_const(key, consts):
    return [c for c in consts if key in c]

def desc_const(c):
    (i,j,n) = (0,0,0)
    for v in c:
        if v[0] == 0: (i,j) = (v[1], v[2])
        if v[0] == 1: n = v[2]
    return (i,j,n)

def print_sudoku(sudoku):
    for j in range(9):
        if not j % 3: print('------------')
        for i in range(9):
            if not i % 3: print('|', end='')
            print('.' if sudoku[j][i] == '0' else sudoku[j][i], end='')
        print()

consts = [make_const(i,j,n) for i,j,n in pr(range(9), range(9), range(1,10))]

sudoku = lines[1:10]
solution = []
cs = consts.copy()

for j,i in pr(range(9), range(9)):
    n = int(sudoku[j][i])
    if not n: continue
    c = make_const(i,j,n)
    cs = apply_const(c, cs)
    solution.append(c)

def solve(sol, cs, indent = ""):
    #print("%ssolve(<%d>, <%d>)" % (indent, len(sol), len(cs)))
    if len(cs) == 0:
        if len(sol) == 81:
            solution = [['x' for i in range(9)] for j in range(9)]
            print("Solution found!")
            for c in sol:
                (i,j,n) = desc_const(c)
                solution[j][i] = str(n)
            print_sudoku(["".join(row) for row in solution])
        return

    cnt = Counter()
    for c in cs: # Find best split
        for k in c: cnt[k] += 1

    pivot = cnt.most_common()[-1][0]

    for c in find_const(pivot, cs):
        solve(sol+[c], apply_const(c, cs), indent+'  ')

print("Solving with %d given numbers, %d constraints..." % (len(solution), len(cs)))
solve(solution, cs)
