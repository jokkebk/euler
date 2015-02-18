from collections import defaultdict

mat = []

with open('p82.txt') as fin:
    for line in fin:
        mat.append([int(s) for s in line.split(',')])

best = defaultdict(lambda: 10**9)
for r in range(len(mat)): best[(r,-1)] = 0

for c in range(len(mat[0])):
    for r in range(len(mat)):
        best[(r,c)] = min(best[(r-1,c)], best[(r,c-1)]) + mat[r][c]
    for r in range(len(mat)-2, -1, -1):
        best[(r,c)] = min(best[(r,c)], best[(r+1,c)] + mat[r][c])

print(min(best[(r,len(mat)-1)] for r in range(len(mat))))
