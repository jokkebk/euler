from p103 import special

sets = []

with open('p105.txt') as fin:
    for line in fin:
        sets.append(list(sorted([int(v) for v in line.split(',')])))

print(sum(sum(s) for s in sets if special(s)))
