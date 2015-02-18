from collections import defaultdict

mat = []

with open('p83.txt') as fin:
    for line in fin:
        mat.append([int(s) for s in line.split(',')])

#mat = [
#        [131, 673, 234, 103, 18],
#        [201, 96, 342, 965, 150],
#        [630, 803, 746, 422, 111],
#        [537, 699, 497, 121, 956],
#        [805, 732, 524, 37, 331]
#        ]
#
best = defaultdict(lambda: 10**9)
best[(0,-1)] = 0

change = True
while change:
    change = False
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            old = best[(r,c)]
            best[(r,c)] = min(
                    best[(r-1,c)],
                    best[(r+1,c)],
                    best[(r,c-1)],
                    best[(r,c+1)]) + mat[r][c]
            if best[(r,c)] != old: change = True
    #for r in range(len(mat)):
    #    for c in range(len(mat[r])):
    #        print("%5d" % best[(r,c)], end=" ")
    #    print()
    #input('Press ENTER to continue')

print(best[(len(mat)-1,len(mat[0])-1)])
