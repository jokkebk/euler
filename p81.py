from collections import defaultdict

mat = []

with open('p81.txt') as fin:
    for line in fin:
        mat.append([int(s) for s in line.split(',')])

best = defaultdict(lambda: 10**9)
best[(-1,0)] = 0

for r in range(len(mat)):
    for c in range(len(mat[r])):
        best[(r,c)] = min(best[(r-1,c)], best[(r,c-1)]) + mat[r][c]

print(best[(79,79)])
